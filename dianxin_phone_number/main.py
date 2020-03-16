# -*- coding: utf-8 -*-
# @Time    : 19/11/27 22:21
# @Author  : sloth
# @File    : main.py
import requests as req
import re, os, time
from dianxin_phone_number.headers_cookies import *

URL = 'http://bj.189.cn/iframe/business/qryPhoneNbr.action'


def get_html(data):
    res = req.post(url=URL, data=data, headers=get_headers(), cookies=get_cookie_use_hand())
    return res.text


def analyze(html):
    phone = re.findall(r'\d{11}', html)
    return sorted(set(phone))


if __name__ == '__main__':
    numberHead = ''
    numberTail = ''
    numberTailWithout = '4'
    matchNum = ''
    data = {
        'numberHead': numberHead,
        'numberTail': numberTail,
        'numberTailWithout': numberTailWithout,
        'matchNum': matchNum,
        'preStore': '0-0',
        'sortType': 'rank_down',
    }
    all_num = []
    # if os.path.exists('phone.txt'):
    #     with open('phone.txt', 'r') as f:
    #         all_num = f.readlines()
    file_num = 0
    while True:
        html = get_html(data)
        phone = analyze(html)
        file_num += 1
        file_name = 'phone_{}.txt'.format(str(file_num))
        for num in phone:
            if num not in all_num:
                all_num.append(num)
                # with open('phone.txt', 'a+') as f:
                #     f.write(num + '\n')
        print(file_name + '*' * 20 + 're write' + '*' * 20)
        # open('phone.txt', 'w')

        for i in sorted(set(all_num)):
            with open(file_name, 'a+') as f:
                f.write(i + '\n')
                print(i)
        # time.sleep(2)
