import argparse
from pil import cli

def main(args): cli.handler(args)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='PIL cli',
        description='edit images on cmd, powerd by pillow and python',
        usage="pil [...Options] -i INPUT -o OUTPUT"
    )

    parser.add_argument(
        '--input', '-i', 
        type=str, 
        help='The input image can be a Unix path or url', 
        required=True,
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
        help='Spacify image quality', 
        required=False,
    )

    parser.add_argument(
        '--optimize', '-O', 
        action='store_true',
        help='Optimize image', 
    )

    main(parser.parse_args())