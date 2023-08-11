import os
from argparse import Namespace
from pil import io as pilio
from pil.utils import conversion, check_outpath_before_save
from pil import actions

def handler(args: Namespace):
    
    image = pilio.bytes_to_image(pilio.read_input_arg(args.input))

    filename, extension = pilio.parse_input_filename(args.input)
    
    if args.output and not args.overwrite:
        pilio.read_output_arg(args.output)

    if args.output:
        _, o_extenstion = pilio.export_filename_extension_from_unix_path(args.output)
        if o_extenstion != extension:
            image = conversion.handle_conversion(image, extension, o_extenstion)

    output_path = args.output
    if not output_path:
        output_path = os.path.join(os.path.curdir, f'{filename}.{extension}')
        if not args.overwrite:
            pilio.read_output_arg(output_path)


    if args.actions:
        image = actions.handler(image, args.actions)

    quality = args.quality

    if not quality:
        quality = 0
    if quality and quality > 100:
        quality = 100

    check_outpath_before_save(output_path)
    image.save(output_path, optimize=args.optimize, quality=quality)