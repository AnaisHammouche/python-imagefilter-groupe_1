import sys
from main import apply_filter
import logger
import art


args = sys.argv


def get_help():
    '''
    Display indication to navigate in the CLI interface
    '''
    logger.log('Print the help command')
    print(f'Usage: Image filter\n-h or ---help : To get all the commands\n'
          f'-i or --input-dir <directory>\n-o --output-dir <directory>')


argument = ('-h', '---help', '--log-file', '--filter', '--config-file')

if not (args[1] in argument):
    print('Command not found. Type ---help or -h')
if args[1] in ('-h', '---help'):
    text = art.text2art("HELP")
    print(text)
    get_help()
if args[1] == '--log-file':
    text = art.text2art("LOGS")
    print(text)
    logger.print_log(args[2])
if args[1] == '--config-file':
    apply_filter(args[2])
if args[1] == '--filter':
    text = art.text2art("FILTER")
    print(text)
    if len(args) == 2:
        print('Please entrer a filter')
    else:
        apply_filter(args[2])



