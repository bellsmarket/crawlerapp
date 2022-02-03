import os
import csv
import requests
import sys
from colorama import Fore, Back, Style
import datetime
import time
import re
from debug import debug_csv, coloring

# define Variable
args = sys.argv
time_stamp = datetime.datetime.now().strftime('%y%m%d%H%M')
interval = 3


## Check Input Arugement
def check_argc():
    if len(sys.argv) <= 1:
        print('引数が足りません。以下のように入力して下さい。')
        print('python3 main.py <TargetURL> <KeywordFile>')
        sys.exit()

    elif len(sys.argv) <= 2: 
        print('URLかファイル指定がありません')
        print('python3 main.py <TargetURL> <KeywordFile>')
        sys.exit()
    else:
        return 0

# Create URL from keywords.
def create_url(target_url, keywords_file):

    # Variable
    urls = []
    prefix = 'https://'

    try:
        with open(keywords_file, 'r') as f:
            for line in f.read().splitlines():
                urls.append(['{0}{1}/{2}'.format(prefix, target_url, line), line])
    except IsADirectoryError as e:
        print('キーワードファイルにディレクトリが選択されています。')
        print('正しいファイルパスを指定して下さい。')
        print('python3 main.py <TargetURL> <KeywordFile>')
    return urls


# Check the existence.
def check_to_exist(target_url, urls):

    # Variable
    datas = []
    cnt_ok = 0
    cnt_ng = 0
    
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

    
    coloring(200, cnt_ok)
    coloring(404, cnt_ng)

    return datas


# Write data to CSV file.
def write_csv(target_url, datas):

    # Variable
    CSV_DIR = os.getcwd() +'/csv'

    # Check the Export Directory.
    if not os.path.isdir(CSV_DIR):
        os.makedirs(CSV_DIR)
        print('Create Directory => ' + CSV_DIR)

    # remove Query from URL
    domain_name = re.sub('(?=[\/|?])(.*)', '', target_url)

    header = ['CompanyName', 'No', 'Keyword', 'Existence']
    second_row = [domain_name, '-', '-', '-']
    f_name = CSV_DIR + '/' +domain_name + '_' + time_stamp + '.csv'

    with open(f_name, 'a')as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(second_row)

        try:
            for data in datas:
                writer.writerow(data)
            print('Writing Completed => {}'.format(os.path.basename(f_name)))
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num,e))

    return 0 

# WorkFlow functions.
def work_flow(target_url, keywords_file):

    # 環境切り替え
    # 0 => デバッグ
    # 1 => 本番環境
    env_flags = 0
    if env_flags == 0:
        print("デバッグ環境")
        datas = debug_csv(target_url)
        write_csv(target_url, datas)
    else:
        print("本番環境")
        urls =  create_url(target_url, keywords_file)
        datas = check_to_exist(target_url, urls)
        write_csv(target_url, datas)
        
    return 0


def main():
    check_argc()
    target_url = sys.argv[1]
    keywords_file = sys.argv[2]

    work_flow(target_url, keywords_file) 

    return 0


if __name__ == '__main__':
    main()
