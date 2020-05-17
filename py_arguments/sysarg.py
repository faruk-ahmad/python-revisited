import sys
import os


if len(sys.argv) > 2:
    print(f'Too many arguments.')
    sys.exit(0)

if len(sys.argv) < 2:
    print(f'Too few arguments.')
    sys.exit(0)

input_path = sys.argv[1]

if not os.path.isdir(input_path):
    print(f'Path specified is not directory.')
    sys.exit(0)

print('\n'.join(os.listdir(input_path)))