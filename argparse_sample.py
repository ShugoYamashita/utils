import argparse
from pathlib import Path

def get_args_parser():
    parser = argparse.ArgumentParser(description='Hyper-parameters for network')
    parser.add_argument('-batch_size', default=32, type=int)
    parser.add_argument('-crop_size', help='Set the crop_size', default=[256, 256], nargs='+', type=int)
    parser.add_argument('-seed', help='set random seed', default=0, type=int)
    parser.add_argument('-pretrained', help='use pretrained weights', action='store_true')
    parser.add_argument('-output_dir', default='./output_dir',
                        help='path where to save, empty for no saving')

    return parser

def main(args):
    if args.pretrained:
        print('argparse: ', args.pretrained)

if __name__ == '__main__':
    args = get_args_parser()
    args = args.parse_args()
    if args.output_dir:
        Path(args.output_dir).mkdir(parents=True, exist_ok=True)
    main(args)
