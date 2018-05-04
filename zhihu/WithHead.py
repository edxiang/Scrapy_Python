# -*- coding: utf-8 -*-
import requests

baseUrl = "https://www.zhihu.com/#signin"
headers = {
    'Host': 'zhihu-web-analytics.zhihu.com',
    'User_Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.zhihu.com/',
    'X-ZA-log-Version': '2.0.2',
    'Content-Type': 'application/x-protobuf',
    'X-ZA-Product': '1',
    'X-ZA-Platform': '1',
    'X-ZA-Batch-Size': '2',
    'Content-Encoding': 'gzip',
    'Content-Length': '897',
    'Origin': 'https://www.zhihu.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0'
}

r = requests.get(baseUrl, headers=headers)
print(r.status_code)

c = r.content.decode('utf-8')
print(c)
