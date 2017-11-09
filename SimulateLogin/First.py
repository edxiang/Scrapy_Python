# -*- coding: utf-8 -*-

import requests
# from bs4 import BeautifulSoup

email = '229270808@qq.com'
password = '6252db754'
login_url = 'https://accounts.douban.com/login'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh",
    "Connection": "Keep_Alive",
    "Host": "www.zhihu.com",
    "Cookie": 'aliyungf_tc=AQAAAL9PDUsOwwcAn2fleCZvKJQCeUzp; l_n_c=1; q_c1=e2c2b7e96d2140be896fdbc9127f82f9|1508916768000|1508916768000; _xsrf=c81a47615951f91753879213850d7214; r_cap_id="Yjk0YTIwYWJhZTFmNGIzYzhjYTgyZDkyNGUxODA0YTg=|1508916768|638a7c3045bd0adf624aefca15b409716472da81"; cap_id="YjAzYTg3Yjk1NmYzNDFiZjg5MTcwM2FmYzc2NDlmZWM=|1508916768|ea74791fc0bd6ac6c81b24ed17bc790be855c019"; d_c0="AECC2lewlAyPTuZGfF3lRJA8CfeIS0zNEvk=|1508916769"; __utma=51854390.1501688304.1508916743.1508916743.1508916743.1; __utmb=51854390.0.10.1508916743; __utmc=51854390; __utmz=51854390.1508916743.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.000--|3=entry_date=20171025=1; _zap=85870e2d-d4c1-46cd-880d-c3e7b0d7505e; z_c0=Mi4xV0x2N0FBQUFBQUFBUUlMYVY3Q1VEQmNBQUFCaEFsVk5WSXpkV2dDWmx0S19kN3Q4cUliTTBfY1hmaHRYemxnRkNB|1508916820|36c5f98f41366de5f9c0e5086aa2e861dff6d46b; _xsrf=c81a47615951f91753879213850d7214',
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36"
}
# login_data = {
#     "source": "None",
#     "redir": "https://www.douban.com",
#     "form_email": "229270808@qq.com",
#     "form_password": "6252db754",
#     "login": "登陆"
# }
# 38152376720414
# login_cookies = {
#     "bid": "b2xcDFPqLyE",
#     "_pk_ref.100001.8cb4": '["","",1496827801,"http://localhost:8080/album/62"]',
#     "_pk_id.100001.8cb4": "1dbbda3993a5b692.1496827801.1.1496827801.1496827801.",
#     "__yadk_uid": "mlaCNnEPX8hrUlNtS0BXot7OefwPq5dJ",
#     "ps": "y",
#     "ue": "229270808@qq.com",
#     "dbcl2": "73662444:kZ8cxT2ErhE"
# }
#
# zhihu_cookies = {
#     "aliyunf_tc": "AQAAAL9PDUsOwwcAn2fleCZvKJQCeUzp",
#     "l_n_c": "1",
#     "q_c1": "e2c2b7e96d2140be896fdbc9127f82f9",
#     "_xsrf": "c81a47615951f91753879213850d7214",
#     "r_cap_id": '"Yjk0YTIwYWJhZTFmNGIzYzhjYTgyZDkyNGUxODA0YTg=|1508916768|638a7c3045bd0adf624aefca15b409716472da81"',
#     "cap_id": '"YjAzYTg3Yjk1NmYzNDFiZjg5MTcwM2FmYzc2NDlmZWM=|1508916768|ea74791fc0bd6ac6c81b24ed17bc790be855c019"',
#     "d_c0": '"AECC2lewlAyPTuZGfF3lRJA8CfeIS0zNEvk=|1508916769"',
#     "__utma": "51854390.1501688304.1508916743.1508916743.1508916743.1",
#     "__utmb": "51854390.0.10.1508916743",
#     "__utmc": "51854390",
#     "__utmz": "51854390.1508916743.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
#     "__utmv": "51854390.000--|3=entry_date=20171025=1",
#     "_zap": "85870e2d-d4c1-46cd-880d-c3e7b0d7505e",
#     "z_c0": "Mi4xV0x2N0FBQUFBQUFBUUlMYVY3Q1VEQmNBQUFCaEFsVk5WSXpkV2dDWmx0S19kN3Q4cUliTTBfY1hmaHRYemxnRkNB|1508916820|36c5f98f41366de5f9c0e5086aa2e861dff6d46b"
# }

s = requests.Session()
# r = requests.get("https://www.douban.com/", cookies=login_cookies)
r = requests.get("https://www.zhihu.com/", headers=headers)
print(r.content.decode('utf-8'))
