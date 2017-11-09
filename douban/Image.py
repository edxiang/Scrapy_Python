# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

# url = "https://www.douban.com/group/topic/108946341/"
# url = "https://www.douban.com/group/topic/108946546/"
url = "https://www.douban.com/group/topic/107707140/"

r = requests.get(url)
c = r.content
x = c.decode('utf-8')
b1 = bytearray(x.encode())
x = c.split(b'\r')
bytesL = ''
for line in x:
    bytesL += line.decode('utf-8')

soup = BeautifulSoup(bytesL, 'lxml')
# 获取整张网页的正文部分，包括图片
list = soup.find('div', attrs={'class': 'topic-content'})

temp = BeautifulSoup(str(list), 'lxml')
# 获取内容图片
fori = temp.find_all('img')


# /***************************/
# get the picture
# done
for img in fori:
    s = BeautifulSoup(str(img), 'lxml')
    print(s.img['src'])
