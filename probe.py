import argparse
from pil.probe import cli

def main(args): cli.handler(args)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='PIL probe',
        description='inspect image details',
        usage="pilprobe -i INPUT"
    )

    parser.add_argument(
        '--input', '-i', 
        type=str, 
        help='The input image can be a Unix path or url', 
        required=True,
    )

    main(parser.parse_args())
   
