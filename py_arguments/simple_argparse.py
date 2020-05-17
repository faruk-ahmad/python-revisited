# simple argparse
# import the argparse library

import os
import sys
import argparse


# create the parser
my_parser = argparse.ArgumentParser(description="list content of a directory.")


# add argument to the parser
my_parser.add_argument('Path',
                        metavar='path',
                        type=str,
                        help='the path to list')


# Execute the parse_args method
args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print(f'Path specified is not a directory.')
    sys.exit(0)

print('\n'.join(os.listdir(input_path)))