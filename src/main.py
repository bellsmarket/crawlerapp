import os
import csv
import requests
import sys
from colorama import Fore, Back, Style
import datetime
import time
import re
import func
from debug import create_dummydata, coloring
import debug


# define Variable
###########################
#   Input Arugements
#   args[1] => companyName
#   args[2] => KeywordsFile
#   args[3] => FileID
###########################

args = sys.argv
exe_time_stamp = datetime.datetime.now().strftime('%y%m%d%H%M')
interval = 3
num_request = 5

## Check Input Arugement
def check_argc():
    if len(sys.argv) <= 3:
        debug.arg_alert(len(sys.argv))
    elif len(sys.argv) > 4:
        debug.arg_alert(len(sys.argv))
    else:
        ## Check Input FileID
        if int(sys.argv[3]) < 1 or int(sys.argv[3]) > 10:
            print("<FileID>は1〜10以内で指定して下さい。")
            sys.exit()

        return True

# Create URL from keywords.
def create_url(company_info, keywords_file, file_id):

    # Variable
    urls = []
    target_range = func.calc_from_to(args, num_request)

    # debug.check_fileid(args)

    try:
        with open(keywords_file, 'r') as f:
            # for keyword in f.read()[target_range[0]: target_range[1]].splitlines():
            for keyword in f.readlines()[target_range[0]: target_range[1]]:
                # print(keyword.rstrip('\n'))
                urls.append(['{0}{1}{2}{3}'.format(company_info.prefix, company_info.url, keyword.rstrip('\n'), company_info.suffix), keyword.rstrip('\n')])

    except IsADirectoryError as e:
        print('キーワードファイルにディレクトリが選択されています。')
        print('正しいファイルパスを指定して下さい。')
        print('python3 main.py <TargetURL> <KeywordFile>')

    # print(len(urls))
    # print(urls)
    return urls


# Check the existence.
def check_to_exist(company_info, urls):

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

        datas.append([url[1],  company_info.create_full_url(url[1]), datetime.datetime.now().strftime('%y/%m/%d %H:%M:%S')])
        # datas.append(['-', i+1 , url[1], status])

        # Request Interval
        time.sleep(interval)


    coloring(200, cnt_ok)
    coloring(404, cnt_ng)

    return datas


# Write data to CSV file.
def write_csv(company_info, datas, json, file_id):

    # Variable
    CSV_DIR = os.path.dirname(__file__) +'/csv'

    # Check the Export Directory.
    if not os.path.isdir(CSV_DIR):
        os.makedirs(CSV_DIR)
        print('Create Directory => ' + CSV_DIR)

    header = ['企業名', 'URL', '調査日時']
    f_name = CSV_DIR + '/' + company_info.filename + f'{file_id:02}' + '.csv'

    with open(f_name, 'a')as f:
        writer = csv.writer(f)
        if file_id == 1:
            writer.writerow(header)

        try:
            for data in datas:
                writer.writerow(data)
            print('Writing Completed => {}'.format(os.path.basename(f_name)))
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num,e))

    return True

# WorkFlow functions.
def work_flow(target_company, keywords_file, file_id):

    target_range = func.calc_from_to(args, num_request)

    # Check CompanyName to JsonFile
    json = func.check_company(target_company)
    company_info = func.cast(json)
    company_info.print_full_url('xxxxxxxxxx')

    # 環境切り替え
    # 0 => デバッグ
    # 1 => 本番環境
    env_flags = 0
    if env_flags == 0:
        print("デバッグ環境")
        datas = create_dummydata(company_info, file_id)
        write_csv(company_info, datas, json, file_id)
    else:
        print("本番環境")
        urls =  create_url(company_info, keywords_file, file_id)
        datas = check_to_exist(company_info, urls)
        write_csv(company_info, datas, json, file_id)

    return 0



def main():
    # debug.all(args)
    check_argc()

    # Variable
    target_company = sys.argv[1].lower()
    keywords_file = sys.argv[2]
    file_id = int(sys.argv[3])

    work_flow(target_company, keywords_file, file_id)

    return 0


if __name__ == '__main__':
    main()
