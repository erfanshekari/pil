import argparse
import tracemalloc

from pil import cli
from pil.utils.file_size import file_size


def main(args):
    cli.handler(args)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        prog='PIL',
        description='edit images on cmd, powered by pillow and python',
        usage="pil [...Options] -i INPUT -o OUTPUT"
    )

    parser.add_argument(
        '--input', '-i',
        type=str,
        help='The input image can be a Unix path or url',
        required=True,
        metavar='-I'
    )

    parser.add_argument(
        '--actions', '-a',
        type=str,
        help='Chain of actions',
        required=False,
    )

    parser.add_argument(
        '--output', '-o',
        type=str,
        help='The output path to save the image will be the current directory by default',
        required=False,
    )

    parser.add_argument(
        '--overwrite',
        action='store_true',
        help='Overwrite an existing file',
    )

    parser.add_argument(
        '--quality', '-q',
        type=int,
        help='Specify image quality',
        required=False,
    )

    parser.add_argument(
        '--optimize', '-O',
        action='store_true',
        help='Optimize image',
    )

    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='print details of operation',
    )

    args = parser.parse_args()

    if args.verbose:
        tracemalloc.start()

    main(args)

    if args.verbose:
        _, peak = tracemalloc.get_traced_memory()

        print(f'Total Memory Usage: {file_size(peak)}')

        tracemalloc.stop()
