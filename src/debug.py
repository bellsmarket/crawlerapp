from colorama import Fore, Back, Style

def t(string):
    print(type(string))

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


