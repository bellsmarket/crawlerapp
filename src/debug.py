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


# for debug.
def debug_csv(url):
    datas = []

    for i in range(0, 40000):
        # print(str(i) + 'cat' + '○')
        if i % 3 == 0:
            keyword = 'cat'
        elif i % 3 == 1:
            keyword = 'dog'
        else:
            keyword = 'bird'
 
        datas.append(['-', i, keyword, '○'])
    print(len(datas))
    return datas
