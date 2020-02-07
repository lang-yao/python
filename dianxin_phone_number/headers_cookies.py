# coding   :utf-8
# @Time    : 2017/7/30 16:42
# @Author  : Jingxiao Fu
# @File    : headers_cookies.py
import random

header_str = '''Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'''

aaa = 1
_bbb = 1


def get_headers():
    header = header_str.split('\n')
    header_length = len(header)
    headers = {
        'user-agent': header[random.randint(0, header_length - 1)],
        "Accept": "text/html, */*; q=0.01",
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '84',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'bj.189.cn',
        'Origin': 'http://bj.189.cn',
        'Referer': 'http://bj.189.cn/iframe/business/phoneNbrReservationInit.action?indexPage=INDEX6&fastcode=20000664&intaid=bj-sy-xy-y2-&cityCode=bj',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    return headers


def get_cookie_use_hand():
    '''手动复制cookie'''
    cookie = "Cookie: name=value; dqmhIpCityInfos=%E5%8C%97%E4%BA%AC%E5%B8%82+%E8%81%94%E9%80%9A; cityCode=bj; svid=989348891A1456D6; s_fid=79CDA65B5173F830-3C945BFD4B5EB7C2; lvid=211facc6ca7ccf2692d751088e39c07b; nvid=1; trkId=2DC94934-E735-45B8-8509-4841A43764A3; SHOPID_COOKIEID=10001; WT_FPC=id=1fc65c6c85471705eec1574604386722; UM_distinctid=16ea0d8811749-05be5dd9cb15ae-2393f61-144000-16ea0d8811890d; loginStatus=non-logined; s_cc=true; s_sq=%5B%5BB%5D%5D; trkHmPageName=%2Fbj%2F; JSESSIONID_bj=7F-tMbhge7H_gD15vtyPS31af6mpEJlsMRIMLWAK3A77CK98x1mC!-541758347; dcs_c=SESSIONID::7F-tMbhge7H_gD15vtyPS31af6mpEJlsMRIMLWAK3A77CK98x1mC!-541758347!1574863747168; grey_nbr=; trkintaid=1; trkHmCoords=0; trkHmCity=0; trkHmLinks=0; trkHmClickCoords=0; Hm_lvt_5b3beae528c7fc9af9c016650f4581e0=1574654681,1574747899,1574772833,1574863749; Hm_lpvt_5b3beae528c7fc9af9c016650f4581e0=1574863749; WT_SS=157486375610570b56c0e6; WT_si_n=WEB_B_MOBILE_PHONENBR_RESERVATION"

    cookie = cookie.replace('Cookie:', '')
    cookie = cookie.replace(' ', '')
    cookies = cookie.split(';')
    for i in range(len(cookies)):
        cookies[i] = cookies[i].replace('=', ':', 1)
    cookies_dict = {}
    for header in cookies:
        L = header.split(':', 1)
        cookies_dict[L[0]] = L[1]
    return cookies_dict
