from colorama import Fore, Back, Style

def t(string):
    print(type(string))

def color():
    print(Fore.RED + "Red")
    print(Fore.GREEN + "Green")
    print(Style.DIM + "dim")
    print(Style.RESET_ALL)
    print("normal")


