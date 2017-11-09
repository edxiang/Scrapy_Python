# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs
import scrapy.Reg as reg
import re

# url = "http://detail.zol.com.cn/index.php?c=SearchList&kword=canon"
url = "http://detail.zol.com.cn/index.php?c=SearchList&keyword=amdcpu&page=39"
baseUrl = 'http://detail.zol.com.cn'
keyWord = 'canon'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-live',
    'Cookie': 'ip_ck=4MaE5PP/j7QuNzE1Mzk4LjE1MDEwNTE3ODU%3D; vjuids=-66aa156f.15dc9ea4c04.0.e6c12fb2b72bb; vjlast=1502331162.1502331162.30; __utma=139727160.1521220798.1503049184.1503049184.1503544195.2; __utmz=139727160.1503544195.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_ae5edc2bc4fc71370807f6187f0a2dd0=1509611224; proIp=123; z_pro_city=s_provice%3Dguangdong%26s_city%3Ddong; userProvinceId=30; userCityId=354; userCountyId=0; userLocationId=9; realLocationId=9; userFidLocationId=9; lv=1510108600; vn=6; afpCT=1; Hm_lvt_63bf9e4e99a63f89aa91dd6bd5978c7a=1509611450,1509611739,1509611744,1510108242; Hm_lpvt_63bf9e4e99a63f89aa91dd6bd5978c7a=1510119479; Adshow=1; visited_subcateId=268|15|28; visited_subcateProId=268-0|15-395552,336780|28-1165663|6-400963|57-1182639; visited_serachKw=canon%7CAMDCPU%7Camd; listSubcateId=268',
    'Host': 'detail.zol.com.cn',
    'If-Modify-Since': 'Wed, 08 Nov 2017 05:38:37 GMT',
    'Upgrade-Insecure-Request': '1',
    'User_Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
}

r = requests.get(url, headers=headers)
print(r.status_code)
c = r.content.decode('GB2312')
soup = bs(c, 'lxml')
items = soup.find_all('div', attrs={'class': 'list-item'})

itemContent = str(items[1])
soup1 = bs(itemContent, 'lxml')

h3 = soup1.find('h3')
soup2 = bs(str(h3), 'lxml')
href = soup2.find('a').get('href')
# detail page: baseUrl + href

name = reg.html(str(h3))
# product's name

price = soup1.find('span', attrs={'class': 'price-normal'})
price1 = reg.html(str(price))

ul = soup1.find('ul')
soup3 = bs(str(ul), 'lxml')
li_items = soup3.find_all('li')
# soup4 = bs(str(li_items[len(li_items) - 1]), 'lxml')
# hrefParam = soup4.find('a').get('href')
# print(baseUrl + hrefParam)
# print(len(li_items))
# for li in li_items:
#     soup4 = bs(str(li), 'lxml')
#     hrefParam = soup4.find('a').get('href')
#     print(baseUrl + hrefParam)

# print(items[1])
next = soup.find('a', attrs={'class', 'next'})
print(next.get('href'))

