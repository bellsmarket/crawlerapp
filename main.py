import csv
import debug as d
import requests
import sys


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
    print("Call def check_to_exist()")
    for url in urls:
        # print(url)
        r = requests.get(url)
        print(url + ':' + str(r))
        # process to request




def main():
    print("Call def main().")
    urls = create_url(url, dir_list)
    check_to_exist(urls)

    return 0


if __name__ == '__main__':
    main()
