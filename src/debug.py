import sys
import datetime

args = sys.argv


def t(string):
    print(type(string))
    print(string)


def check_fileid(args):
    num_request = 3500
    target_from = num_request * int(args[3]) - num_request
    target_to = num_request * int(args[3])

    print("From To : " + str(target_from) + "〜" + str(target_to))
    exit(1)


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

        fqdn = company_info.create_fqdn(keyword) if not keyword == '' else keyword
        keyword = keyword = 'lion' if keyword == '' else keyword
        datas.append([keyword, fqdn, datetime.datetime.now().strftime('%y/%m/%d %H:%M:%S')])

    return datas


def all(args):
    check_fileid(args)
    exit(1)
