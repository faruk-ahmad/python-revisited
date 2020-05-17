import os
import sys
import argparse


# create the argument parser

my_parser = argparse.ArgumentParser(prog="Advance Argument Parser",
                                    usage="%(prog)s [options] path",
                                    description="An advance argument parser example")

my_parser.add_argument("Path",
                        metavar="path",
                        type=str,
                        help="path to list content.")

args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print(f'Path specified is not a directory')
    sys.exit(0)

print('\n'.join(os.listdir(input_path)))