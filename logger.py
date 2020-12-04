from datetime import datetime


def log(msg, file='image.log'):
    f"""
    Save a msg in a log file {file} and print it in the console
    :param msg: The msg to append in the log file
    """
    now = datetime.now()
    format_time = now.strftime("%d/%m/%Y    %H:%M:%S")
    formatted = f'{format_time} | {msg}\n'
    with open(file, 'a') as f:
        f.write(formatted)


def print_log(file='image.log'):
    f"""
    Display in the console the content of log file {file}
    """
    try:
        with open(file, 'r') as f:
            print(f.read())
    except FileNotFoundError as e:
        print(f'Cannot open {file}\nError : {e} ')
