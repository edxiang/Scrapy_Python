# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs
import re
from scrapy import Reg as reg

regHref = re.compile(r'href="(.*?)"')

url = "https://www.douban.com/group/explore/culture?start=4350"
r = requests.get(url).content.decode('utf-8')
soup = bs(r, 'lxml')
article = soup.find('div', attrs={'class': 'article'})

soupi = bs(str(article), 'lxml')
item = soupi.find_all('h3')
for link in item:
    soutl = bs(str(link), 'lxml')
    href = soutl.find('a')
    want = regHref.findall(str(href))[0]
    print(want)

