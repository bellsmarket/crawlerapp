from colorama import Fore, Back, Style
import sys

BLACK = 'black'
RED = 'red'
GREEN = 'green'
YELLOW = 'yellow'
BLUE = 'blue'
MAGENTA = 'magenta'
CYAN = 'cyan'
WHITE = 'white'


def add_color(text, color):
    if color.lower() == 'green':
        text = Fore.GREEN + str(text) + Style.RESET_ALL
    elif color.lower() == 'red':
        text = Fore.RED + str(text) + Style.RESET_ALL
    elif color.lower() == 'yellow':
        text = Fore.YELLOW + str(text) + Style.RESET_ALL
    elif color.lower() == 'cyan':
        text = Fore.CYAN + str(text) + Style.RESET_ALL
    return text


def print_color(text, color):
    if color.lower() == 'green':
        text = Fore.GREEN + str(text) + Style.RESET_ALL
    elif color.lower() == 'red':
        text = Fore.RED + str(text) + Style.RESET_ALL
    elif color.lower() == 'yellow':
        text = Fore.YELLOW + str(text) + Style.RESET_ALL
    elif color.lower() == 'cyan':
        text = Fore.CYAN + str(text) + Style.RESET_ALL
    return print(text)


def print_status_code(cnt_ok, cnt_ng):
    print('{0}{1} => {2}'.format('ステータスコード', add_color(200, GREEN), cnt_ok))
    print('{0}{1} => {2}'.format('ステータスコード', add_color(404, RED), cnt_ng))


def print_error(text):
    error = Fore.RED + 'Error' + Style.RESET_ALL
    print('{0} => {1}'.format(error, text))


def arg_alert(argv):
    if argv <= 3:
        print_error('引数が足りません。以下を参考に入力して下さい。\n')
    elif argv > 4:
        print_error('引数が多すぎます。以下を参考に入力して下さい。\n')
    print('{} => python3 main.py <TargetCompany> <KeywordFile> <FileID 1〜10>'.format(add_color('各引数', 'green')))
    print('{} => python3 src/main.py aol1 files/keywordsList.csv 1\n'.format(add_color('e.x', 'green')))
    sys.exit(1)
