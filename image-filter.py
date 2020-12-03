import sys
from main import call_filter

args = sys.argv


def help():
    print(f'Usage: Image filter\n-h or ---help : To get all the commands\n'
          f'-i or --input-dir <directory>\n-o --output-dir <directory>')


arg2 = int(args[2])


if args[1] in ('-h', '---help'):
    help()
elif args[1] == "--filters":
    call_filter(args[1], arg2)
