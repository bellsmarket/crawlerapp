import os
import csv
import requests
import sys
import datetime
import time
import func
from colorama import Fore, Style
from debug import create_dummydata
import stdout as out
from stdout import print_color, add_color, print_error

# define Variable
###########################
#   Input Arugements
#   args[1] => companyName
#   args[2] => KeywordsFile
#   args[3] => FileID
###########################

BLACK = 'black'
RED = 'red'
GREEN = 'green'
YELLOW = 'yellow'
BLUE = 'blue'
MAGENTA = 'magenta'
CYAN = 'cyan'
WHITE = 'white'

args = sys.argv
exe_time_stamp = datetime.datetime.now().strftime('%y%m%d%H%M')
interval = 3
num_request = 3

# 環境切り替え
# 0 => デバッグ
# 1 => 本番環境
env_flags = 1


# Check Input Arugement
def check_argc():
    if len(sys.argv) <= 3:
        out.arg_alert(len(sys.argv))
    elif len(sys.argv) > 4:
        out.arg_alert(len(sys.argv))
    else:
        # Check Input FileID
        if int(sys.argv[3]) < 1 or int(sys.argv[3]) > 10:
            print_error('<FileID>は1〜10以内で指定して下さい。')
            sys.exit(1)

        return True


# Create URL from keywords.
def create_url(company_info, keywords_file, file_id):
    urls = []
    target_range = func.get_from_to(args, num_request)

    try:
        with open(keywords_file, 'r') as f:
            for keyword in f.readlines()[target_range[0]: target_range[1]]:
                urls.append(['{0}{1}{2}{3}'.format(company_info.prefix, company_info.url, keyword.rstrip('\n'), company_info.suffix), keyword.rstrip('\n')])

    except IsADirectoryError as e:
        print_error('キーワードファイルにディレクトリが選択されています。')
        print('正しいファイルパスを指定して下さい。')
        print('python3 main.py <TargetURL> <KeywordFile>')
        print(e)
        sys.exit(1)
    except OSError as e:
        print_error('ファイルが存在しません')
        print(e)
        sys.exit(1)

    # print(len(urls))
    # print(urls)
    return urls


# Check the existence.
def check_statuscode(company_info, urls, file_id):
    datas = []
    cnt_ok = 0
    cnt_ng = 0

    for i, url in enumerate(urls):
        r = requests.get(url[0])
        if r.status_code == 200:
            flag = Fore.GREEN + str(r.status_code) + Style.RESET_ALL
            cnt_ok += 1
        else:
            flag = Fore.RED + str(r.status_code) + Style.RESET_ALL
            cnt_ng += 1

        keyword = url[1]
        fqdn = company_info.create_fqdn(keyword)
        time_stamp = datetime.datetime.now().strftime('%y/%m/%d %H:%M:%S')

        print('{0: d}: {1} => {2}'.format(i, keyword, flag))

        # Create Datas for WriteCSV.
        datas.append([keyword, fqdn, time_stamp])

        # Request Interval
        time.sleep(interval)

    out.print_status_code(cnt_ok, cnt_ng)

    return datas


# Write data to CSV file.
def write_csv(company_info, datas, file_id):
    CSV_PATH = os.path.dirname(__file__) + '/csv'

    # Check the Export Directory.
    if not os.path.isdir(CSV_PATH):
        os.makedirs(CSV_PATH)
        print('Create Directory => ' + CSV_PATH)

    header = ['企業名', 'URL', '調査日時']
    export_csv_name = CSV_PATH + '/' + company_info.filename + f'{file_id:02}' + '.csv'

    with open(export_csv_name, 'a')as f:
        writer = csv.writer(f)
        if file_id == 1:
            writer.writerow(header)

        try:
            for data in datas:
                writer.writerow(data)
            print('{} => {}'.format(add_color('Writing Completed', GREEN), os.path.basename(export_csv_name)))
        except csv.Error as e:
            sys.exit('file {}, line :{}'.format(export_csv_name, e))

    return True


# WorkFlow functions.
def work_flow(target_company, keywords_file, file_id):
    # Check CompanyName to JsonFile
    json = func.check_company(target_company)
    company_info = func.cast_obj_from_json(json)

    if env_flags == 0:
        print_color("ENV => Debug", RED)
        datas = create_dummydata(company_info, file_id)
        write_csv(company_info, datas, file_id)
    else:
        print_color("ENV => Prod", GREEN)
        urls = create_url(company_info, keywords_file, file_id)
        datas = check_statuscode(company_info, urls, file_id)
        write_csv(company_info, datas, file_id)

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
