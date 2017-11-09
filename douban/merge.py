# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup as bs
import douban.Information as inf

regHref = re.compile(r'href="(.*?)"')

# technology
# url = "https://www.douban.com/group/explore/tech?start="

url = "https://www.douban.com/group/explore/ent?start="
index = 1
loc = 0
while index <= 56:
    location = url + str(loc)
    print(location)
    soup = bs(requests.get(location).content.decode('utf-8'), 'lxml')
    article = soup.find('div', attrs={'class': 'article'})
    soupi = bs(str(article), 'lxml')
    item = soupi.find_all('h3')
    for link in item:
        soupl = bs(str(link), 'lxml')
        href = soupl.find('a')
        link_href = regHref.findall(str(href))[0]
        inf.info(link_href)
    index += 1
    loc += 30
    print(index)

# done
