import json
import sys
import os
import stdout as out

BLACK = 'black'
RED = 'red'
GREEN = 'green'
YELLOW = 'yellow'
BLUE = 'blue'
MAGENTA = 'magenta'
CYAN = 'cyan'
WHITE = 'white'


# Open the JsonFile of Company Info.
def open_json():
    JSON_PATH = os.path.dirname(__file__) + '/files/companies_info.json'
    json_obj = open(JSON_PATH, 'r')
    companies = json.load(json_obj)

    return companies


def print_company_info():
    jsonfile = open_json()
    for com in jsonfile:
        print(com['name'])
    exit()


# Check the CompanyName from Jsonfile.
def check_company(company_name):
    jsonfile = open_json()

    company_flag = False
    for company in jsonfile:
        if company['name'] == company_name:
            company_flag = True
            break

    if not company_flag:
        print('{} => 指定された引数と企業名が一致しません。'.format(out.add_color("Error", RED)))
        print('以下の値から選択し、引数に入力してください。')
        print_company_info()
        sys.exit(1)

    return company


def get_from_to(args, num):
    num_request = num
    target_from = num_request * int(args[3]) - num_request
    target_to = num_request * int(args[3])

    return target_from, target_to


class cast_obj_from_json:
    def __init__(self, json):
        self.list = json
        self.prefix = 'https://'
        self.id = json['id']
        self.name = json['name']
        self.filename = json['filename']
        self.url = json['url']
        self.suffix = json['suffix']

    def profile(self):
        print('self.prefix => ' + str(self.prefix))
        print('self.id => ' + str(self.id))
        print('self.name => ' + str(self.name))
        print('self.filename => ' + str(self.filename))
        print('self.url => ' + str(self.url))
        print('self.suffix => ' + str(self.suffix))
        print('')
        exit(1)

    def create_fqdn(self, keyword):
        self.keyword = keyword
        self.fqdn = '{0}{1}{2}{3}'.format(self.prefix, self.url, self.keyword, self.suffix)
        return self.fqdn

    def print_fqdn(self, keyword):
        self.keyword = keyword
        self.fqdn = '{0}{1}{2}{3}'.format(self.prefix, self.url, self.keyword, self.suffix)
        print(self.fqdn)
        print('')
        exit(1)
