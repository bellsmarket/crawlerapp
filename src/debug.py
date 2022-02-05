from colorama import Fore, Back, Style
import sys
import datetime
import func


def t(string):
    print(type(string))
    print(string)


def coloring(code, num):
    if code == 200:
        print(Fore.GREEN + str(code) + Style.RESET_ALL + ' => ' + str(num)+ 'ページ')
    else:
        print(Fore.RED + str(code) + Style.RESET_ALL + ' => ' + str(num)+ 'ページ')


def check_fileid(args):
    num_request = 3500
    target_from = num_request * int(args[3]) - num_request
    target_to = num_request * int(args[3])

    print("From To : " + str(target_from) +"〜" +  str(target_to))
    exit()

# for debug.
def create_dummydata(company_info, file_id):
    datas = []
    num_request = 3500
    target_from = num_request * int(args[3]) - num_request
    target_to = num_request * int(args[3])

    print('デバッグ用のダミーデータを作成')


    for i in range(target_from, target_to):
        if i % 4 == 0:
            keyword = 'cat'
        elif i % 4 == 1:
            keyword = 'dog'
        elif i % 4 == 2:
            keyword = 'bird'
        else:
            keyword = ''

        full_url = company_info.create_full_url(keyword) if not keyword == '' else keyword
        keyword = keyword = 'lion' if keyword == '' else keyword
        datas.append([keyword,  full_url, datetime.datetime.now().strftime('%y/%m/%d %H:%M:%S')])

    return datas


def arg_alert(argv):
    if argv <= 3:
        print('引数が足りません。以下のように入力して下さい。')
    elif argv > 4:
        print('引数が多すぎます。以下のように入力して下さい。')
    print('python3 main.py <TargetCompany> <KeywordFile> <FileID 1〜10>')
    print('e.x: python3 src/main.py aol1 files/keywordsList.csv 1')
    sys.exit()




def all(args):
    check_fileid(args)
    exit()
