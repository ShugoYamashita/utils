import argparse

parser = argparse.ArgumentParser(description='Hyper-parameters for network')

parser.add_argument('-seed', help='set random seed', default=19, type=int)
parser.add_argument('-pretrained_mixmae', help='use pretrained weights', action='store_true')
parser.add_argument('-fix_pretrained_weights', help='fix pretrained weights', action='store_true')

args = parser.parse_args()

seed = args.seed
print(args.pretrained)
print(args.fix_pretrained_weights)

if args.pretrained:
    print('argparse: ', args.pretrained)
