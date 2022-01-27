import csv
import debug as d
import requests
import sys
from colorama import Fore, Back, Style

# define Variable
args = sys.argv
prefix = 'https://'
url = 'bells-audio.com'

dir_list = args[1] 


def create_url(target_url, directory):
    print("Call def create_url()")
    urls = []

    with open(directory, 'r') as f:
        for line in f.read().splitlines():
            urls.append('{0}{1}/{2}'.format(prefix, target_url, line))
            # url = '{0}{1}/{2}'.format(prefix, target_url, line)
            # print(line) #200ms

        # 処理速度計測
        # for line in f:
            # print(line)
            # print(line.replace('\n','')) #250 -270ms
            # print(line.rstrip('\n')) #259ms

    return urls

def check_to_exist(urls):
    ok = 0
    ng = 0
    print("Call def check_to_exist()")
    for i, url in enumerate(urls):
        r = requests.get(url)
        # print(str(i) + ':' + url + ':' + str(r))
        if r.status_code == 200:
            flag = Fore.GREEN + str(r.status_code) + Style.RESET_ALL
            ok+=1
        else:
            flag = Fore.RED + str(r.status_code) + Style.RESET_ALL
            ng+=1
        print('{0: d}: {1} => {2}'.format(i, url, flag))
        # process to request

    coloring(200, ok)
    coloring(404, ng)


def coloring(code, num):
    if code == 200:
        print(Fore.GREEN + str(code) + Style.RESET_ALL + ' => ' + str(num)+ 'ページ')
    else:
        print(Fore.RED + str(code) + Style.RESET_ALL + ' => ' + str(num)+ 'ページ')



def main():
    print("Call def main().")
    urls = create_url(url, dir_list)
    check_to_exist(urls)
    # d.color()

    return 0


if __name__ == '__main__':
    main()
