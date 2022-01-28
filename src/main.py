import csv
import requests
import sys
from colorama import Fore, Back, Style
import datetime
import time
import re
import debug as d

# define Variable
args = sys.argv
time_stamp = datetime.datetime.now().strftime('%y%m%d%H%M')
interval = 1 


## Check Input Arugement
def check_argc():
    if len(sys.argv) <= 1:
        print('引数が足りません。')
        print('python3 main.py <TargetURL> <KeywordFile>')
        exit()

    elif len(sys.argv) <= 2: 
        print('URLもしくはファイル指定がありません')
        print('python3 main.py <TargetURL> <KeywordFile>')
        exit()
    else:
        return 0


# Create URL from keywords.
def create_url(target_url, keywords_file):
    print("Call def create_url()")

    # Variable
    urls = []
    prefix = 'https://'

    with open(keywords_file, 'r') as f:
        for line in f.read().splitlines():
            urls.append(['{0}{1}/{2}'.format(prefix, target_url, line), line])
    return urls


# Check the existence.
def check_to_exist(target_url, keywords_file):
    print("Call def check_to_exist()")

    # Variable
    datas = []
    cnt_ok = 0
    cnt_ng = 0
    urls = create_url(target_url, keywords_file)
    
    for i, url in enumerate(urls):
        r = requests.get(url[0])
        if r.status_code == 200:
            flag = Fore.GREEN + str(r.status_code) + Style.RESET_ALL
            cnt_ok += 1
            status = '○'
        else:
            flag = Fore.RED + str(r.status_code) + Style.RESET_ALL
            cnt_ng += 1
            status = '×'

        print('{0: d}: {1} => {2}'.format(i, url[1], flag))

        # Create Datas for WriteCSV.
        datas.append(['-', i+1 , url[1], status])

        # Request Interval
        time.sleep(interval)

    
    d.coloring(200, cnt_ok)
    d.coloring(404, cnt_ng)

    return datas


# Write data to CSV file.
def write_csv(datas, url):
    print("Call def write_csv()")

    # Variable
    DIR_CSV = './csv/'

    # remove Query from URL
    domain_name = re.sub('(?=\/)(.*)', '', url)

    header = ['CompanyName', 'No', 'Keyword', 'Existence']
    second_row = [domain_name, '-', '-', '-']
    f_name = DIR_CSV + domain_name + time_stamp + '.csv'

    with open(f_name, 'a')as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(second_row)

        for data in datas:
            writer.writerow(data)


def main():
    print("Call def main().")
    check_argc()
    url = sys.argv[1]
    keywords_file = sys.argv[2] 
    
    datas = check_to_exist(url, keywords_file)
    write_csv(datas, url)
    return 0


if __name__ == '__main__':
    main()
