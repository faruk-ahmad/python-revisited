import os
import sys
import argparse


# create the argument parser
"""
prog: this text will be displayed instead of scirpt name if there is any error.
usage: customizing the error message format.
decription: this text will be displayed before the standard help message
epilog: this text will be displayed after the standard help message.
"""

my_parser = argparse.ArgumentParser(prog="Advance Argument Parser",
                                    usage="%(prog)s [options] path",
                                    description="An advance argument parser example",
                                    epilog="Enjoy the program. :)")
"""
default: if the argument is not given by user, the default value will be used.
"""
my_parser.add_argument("-p",
                        "--path",
                        help="path to list content.",
                        default="/home/faruk/Desktop/exp/"
                        )

"""
choices: are the values from where the user can pick a value , list required
required: if set True, force the user to input this optional argument.
"""
my_parser.add_argument("-show",
                        "--show",
                        help="Argument to show the list of directory or not",
                        choices=["yes", "no"],
                        default="yes",
                        required=True
                        )

args = my_parser.parse_args()

print(args.path)

input_path = args.path
show = args.show

print(input_path)

if not os.path.isdir(input_path):
    print(f'Path specified is not a directory')
    sys.exit(0)

if show == "yes":
    print('\n'.join(os.listdir(input_path)))