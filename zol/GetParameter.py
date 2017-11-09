# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs
import re
import scrapy.Reg as reg

# url = "http://detail.zol.com.cn/1165/1164573/param.shtml"

tab = "    "

def writeFile(name, url):
    output = open(name + '.txt', 'w+', encoding='utf-8')
    c = requests.get(url).content.decode('gbk')
    soup = bs(c, 'lxml')
    table_items = soup.find_all('table')
    # print(table_items[1])

    index = 0
    for table_item in table_items:
        if index > 0 and index < len(table_items)-1:
            soup1 = bs(str(table_item), 'lxml')
            th = soup1.find('th')
            lis = soup1.find_all('li')
            output.write(reg.html(str(th)) + "\n")
            # print(reg.html(str(th)))

            for li in lis:
                soupTemp = bs(str(li), 'lxml')
                spans = soupTemp.find_all('span')
                s = ''
                x = 0
                for span in spans:
                    s += str(span)
                    if x == 0:
                        s += " - "
                    x += 1

                # print(reg.html(str(s)))
                output.write(reg.html(str(s)) + "\n")
        index += 1
    output.close()


writeFile("whatever", "http://detail.zol.com.cn/367/366984/param.shtml")
