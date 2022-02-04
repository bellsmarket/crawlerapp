import json
import sys
import os

# Variable
# exe_path = os.path.dirname(__file__)

def open_json(path):
    json_open = open(path, 'r')
    companies = json.load(json_open)
    return companies

def check_company(jsonfile, company_name):
    check_flag = False
    for company in jsonfile:
        if company['name'] == company_name:
            # url = parse_url(company)
            check_flag = True
            break

    if not check_flag:
        print("企業名が引数にありません。")
        exit()

    return True

def parse_url(obj, keyword):
    prefix = 'https://'
    url = prefix + str(obj['url']) + 'KEYWORD' + str(obj['suffix'])
    return url
