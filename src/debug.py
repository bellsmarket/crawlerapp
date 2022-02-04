from colorama import Fore, Back, Style
import sys

def t(string):
    print(type(string))
    print(string)

def color():
    print(Fore.RED + "Red")
    print(Fore.GREEN + "Green")
    print(Style.DIM + "dim")
    print(Style.RESET_ALL)
    print("normal")

def coloring(code, num):
    if code == 200:
        print(Fore.GREEN + str(code) + Style.RESET_ALL + ' => ' + str(num)+ 'ページ')
    else:
        print(Fore.RED + str(code) + Style.RESET_ALL + ' => ' + str(num)+ 'ページ')


# for debug.
def debug_csv(url):
    datas = []
    max_len = 40000
    print('degug用のリストファイルを作成')

    for i in range(0, max_len):
        if i % 3 == 0:
            keyword = 'cat'
        elif i % 3 == 1:
            keyword = 'dog'
        else:
            keyword = 'bird'

        datas.append(['-', i, keyword, '○'])
    return datas

def arg_alert(argv):
    if argv <= 3:
        print('引数が足りません。以下のように入力して下さい。')
    elif argv > 4:
        print('引数が多すぎます。以下のように入力して下さい。')
    print('python3 main.py <TargetCompany> <KeywordFile> <FileID 1〜10>')
    print('e.x: python3 src/main.py aol1 files/keywordsList.csv 1')
    sys.exit()
