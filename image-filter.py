import sys
from main import apply_filter

args = sys.argv


def help():
    '''
    Display indication to navigate in the CLI interface
    '''
    print(f'Usage: Image filter\n-h or ---help : To get all the commands\n'
          f'-i or --input-dir <directory>\n-o --output-dir <directory>')


if args[1] in ('-h', '---help'):
    help()
if args[1] == '--filter':
    apply_filter(args[2])
