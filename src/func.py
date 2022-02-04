import json
import sys
import os

# Open the JsonFile of Company Info.
def open_json():

    # Variable
    json_path = os.path.dirname(__file__) + '/files/company_info.json'

    json_open = open(json_path, 'r')
    companies = json.load(json_open)

    return companies


# Check the CompanyName from Jsonfile.
def check_company(jsonfile, company_name):
    check_flag = False
    for company in jsonfile:
        if company['name'] == company_name:
            url = parse_url(company)
            check_flag = True
            break

    if not check_flag:
        print("企業名が引数にありません。")
        exit()

    print(url)
    return True


def parse_url(obj):
    prefix = 'https://'
    url = prefix + str(obj['url']) + 'KEYWORD' + str(obj['suffix'])
    return url
