import json
from argparse import Namespace

from pil import io as pilio


def handler(args: Namespace):
    input_as_bytes = pilio.read_input_arg(args.input)

    image = pilio.bytes_to_image(input_as_bytes)

    filename, extension = pilio.parse_input_filename(args.input)

    details = {
        'contentType': image.get_format_mimetype(),
        'size': len(input_as_bytes),
        'extension': extension,
        'name': filename,
        'width': image.width,
        'height': image.height
    }

    print(json.dumps(details))
   