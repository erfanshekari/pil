import os
import time
from argparse import Namespace

from pil import actions
from pil import io as pilio
from pil.utils import (
    conversion,
    check_outpath_before_save,
    print_image_info
)


def handler(args: Namespace):
    if args.verbose:
        start_time = time.time()

    input_as_bytes = pilio.read_input_arg(args.input)

    image = pilio.bytes_to_image(input_as_bytes)

    filename, extension = pilio.parse_input_filename(args.input)

    if args.verbose:
        print_image_info(image, extension, len(input_as_bytes))

    if args.output and not args.overwrite:
        pilio.read_output_arg(args.output)

    if args.output:
        _, o_extension = pilio.export_filename_extension_from_unix_path(args.output)
        if o_extension != extension:
            image = conversion.handle_conversion(image, extension, o_extension)

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

    out_file_size = os.path.getsize(output_path)

    if args.verbose:
        print_image_info(
            image,
            extension if not 'o_extension' in locals() else o_extension,
            out_file_size,
            'OUTPUT',
        )

    if args.verbose:
        end_time = time.time()
        print(f'saved {round((end_time - start_time), 10)} seconds\n{os.path.abspath(output_path)}')
