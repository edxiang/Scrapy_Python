# encoding=utf-8
import requests
from bs4 import BeautifulSoup
import re
import scrapy.Reg as reg

headers = {
    "Host": "www.douban.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Cookie": 'bid=b2xcDFPqLyE; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1508979672%2C%22https%3A%2F%2Faccounts.douban.com%2Flogin%3F%22%5D; _pk_id.100001.8cb4=1dbbda3993a5b692.1496827801.4.1508979681.1508925264.; __yadk_uid=mlaCNnEPX8hrUlNtS0BXot7OefwPq5dJ; ps=y; ue="229270808@qq.com"; push_noty_num=0; push_doumail_num=0; __utma=30149280.891040440.1508915824.1508923730.1508979674.3; __utmz=30149280.1508915824.1.1.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/login; __utmv=30149280.7366; ct=y; ap=1; _pk_ses.100001.8cb4=*; __utmb=30149280.12.5.1508979682515; __utmc=30149280; __utmt=1',
    "Connection": "keep-alive",
    "Upgrade_Insecure-Requests": "1",
    "Cache-Control": "max-age=0"
}

cookies = {
    "bid": "b2xcDFPqLyE",
    "_pk_ref.100001.8cb4": '["","",1508979672,"https://accounts.douban.com/login?"]',
    "_pk_id.100001.8cb4": "1dbbda3993a5b692.1496827801.4.1508979681.1508925264.",
    "__yadk_uid": "mlaCNnEPX8hrUlNtS0BXot7OefwPq5dJ",
    "ps": "y",
    "ue": '"229270808@qq.com"',
    "push_noty_num": "0",
    "push_doumail_num": "0",
    "__utma": "30149280.891040440.1508915824.1508923730.1508979674.3",
    "__utmz": '30149280.1508915824.1.1.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/login',
    "__utmv": "30149280.7366",
    "ct": "y",
    "ap": "1",
    "_pk_ses.100001.8cb4": "*",
    "__utmb": "30149280.12.5.1508979682515",
    "__utmc": "30149280",
    "__utmt": "1"
}

simpleHeader = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36"
}

url = "https://www.douban.com/group/topic/108946341/"

r = requests.get(url)
c = r.content
x = c.decode('utf-8')
b1 = bytearray(x.encode())
x = c.split(b'\r')
bytesL = ''
for line in x:
    bytesL += line.decode('utf-8')
# print(bytesL)

soup = BeautifulSoup(bytesL, 'lxml')
list = soup.find('div', attrs={'class': 'topic-content'})

regP = re.compile(r'<p>(.*?)</p>')
target = regP.findall(str(list))[0]
regN = re.compile(r'<br/>')
p = re.sub(regN, "\n", str(list))

print(p)




# YES!!!!!!!!!!!!!!!!!!!!!!!!!
