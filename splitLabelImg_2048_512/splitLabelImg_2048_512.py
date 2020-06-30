import os
#import cv2
import argparse
import sys

from splitImg import SplitImgAndLabel

def main():
    parser = argparse.ArgumentParser(description='split image 2048 x 2048 in 16 x 512 x 512')
    parser.add_argument('-s', help='source directory of orginal images and txt files', default='source')
    parser.add_argument('-o', help='target directory of splited images and txt files', default='out')
    args = parser.parse_args()

    source_dir = os.path.join(os.path.dirname(os.path.realpath('__file__')), args.s)
    if not os.path.exists(source_dir):
        print('Provide the correct folder for images')
        sys.exit()

    out_dir = os.path.join(os.path.dirname(os.path.realpath('__file__')), args.o)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    if not os.access(out_dir, os.W_OK):
        print("%s folder is not writeable.")
        sys.exit()

    split = SplitImgAndLabel(source_dir=source_dir, out_dir=out_dir)
    split.start()


if __name__ == "__main__":
    main()