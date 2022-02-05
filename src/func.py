import json
import sys
import os

# Open the JsonFile of Company Info.
def open_json():

    # Variable
    json_path = os.path.dirname(__file__) + '/files/companies_info.json'

    json_open = open(json_path, 'r')
    companies = json.load(json_open)

    return companies


# Check the CompanyName from Jsonfile.
def check_company(company_name):
    jsonfile = open_json()

    check_flag = False
    for company in jsonfile:
        if company['name'] == company_name:
            check_flag = True
            break

    if not check_flag:
        print("企業名が引数にありません。")
        exit()

    return company


def parse_url(obj):
    prefix = 'https://'
    url = prefix + str(obj['url']) + 'KEYWORD' + str(obj['suffix'])
    return url


def calc_from_to(args, num):
    num_request = num
    target_from = num_request * int(args[3]) - num_request
    target_to = num_request * int(args[3])

    return target_from, target_to


class cast:
    def __init__(self, json):
        self.list = json
        self.prefix = 'https://'
        self.id =       json['id']
        self.name =     json['name']
        self.filename = json['filename']
        self.url =       json['url']
        self.suffix = json['suffix']

    def profile(self):
        # print(self.list)
        print('self.prefix => ' + str(self.prefix))
        print('self.id => ' + str(self.id))
        print('self.name => ' + str(self.name))
        print('self.filename => ' + str(self.filename))
        print('self.url => ' + str(self.url))
        print('self.suffix => ' + str(self.suffix))
        print('')
        exit()

    def create_full_url(self, keyword):
        self.keyword = keyword
        self.full_url = '{0}{1}{2}{3}'.format(self.prefix, self.url, self.keyword, self.suffix)
        return self.full_url

    def print_full_url(self, keyword):
        self.keyword = keyword
        self.full_url = '{0}{1}{2}{3}'.format(self.prefix, self.url, self.keyword, self.suffix)
        print(self.full_url)
        print('')
        exit()
