# -*- coding: utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup
import scrapy.Reg as reg

url = "https://www.douban.com/group/topic/108625461/"

r = requests.get(url)
c = r.content
x = c.split(b'\r')
bytesL = ''
for line in x:
    bytesL += line.decode('utf-8')

soup = BeautifulSoup(bytesL, 'lxml')
list = soup.find('div', attrs={'id': 'content'})

# get the title
soup1 = BeautifulSoup(str(list), 'lxml')
list1 = soup1.find('h1')
title = reg.html(str(list1))
title = reg.blank(title)
print(title)

soup2 = BeautifulSoup(str(list), 'lxml')
list2 = soup2.find('h3')
s = reg.html(str(list2))
ss = s.split('\n')
print(ss[1])
print(ss[2])
