# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup as bs
import scrapy.Reg as Reg
import xml.etree.ElementTree as ET

# 对于 xml 的标签而言，先过滤掉特殊字符
r1 = re.compile(r'/')
r2 = re.compile(r'\s')
r3 = re.compile(r'[\W]')
r4 = re.compile(r'\s{2,}')
r5 = re.compile(r'^[\d]+')

# 添加子节点
def subElement(root, tag, text):
    ele = ET.SubElement(root, tag)
    ele.text = text

# 头部信息，没有这一部分 requests 获取不到网页
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
# 查询链接
searchUrl = "http://detail.zol.com.cn/index.php?c=SearchList&kword="
page = "&page="  # 页数
baseUrl = 'http://detail.zol.com.cn'  # 基本的 url
keyWord = 'AMDCPU'  # 关键字
index = 38  # 总的页数

root = ET.Element(keyWord)

while 1 == 1:
    print(index)
    url = searchUrl + keyWord + page + str(index)
    try:
        r = requests.get(url, headers=headers).content.decode('GB2312')
    except Exception:
        r = requests.get(url, headers=headers).content.decode('GBK')
    soup = bs(r, 'lxml')
    items = soup.find_all('div', attrs={'class', 'list-item'})

    for item in items:
        soup1 = bs(str(item), 'lxml')
        h3 = soup1.find('h3')
        name = Reg.html(str(h3))
        name = re.sub(r1, "-", name)
        name = re.sub(r2, "_", name)
        name = re.sub(r3, '-', name)
        nameNode = ET.Element(name)

        price_div = soup1.find('b', attrs={'class', 'price-type'})
        price = Reg.html(str(price_div))
        subElement(nameNode, '价格', price)

        href = ''

        try:
            ul = soup1.find('ul')
            soup2 = bs(str(ul), 'lxml')
            li_items = soup2.find_all('li')
            soup3 = bs(str(li_items[len(li_items) - 1]), 'lxml')
            hrefParam = soup3.find('a').get('href')
            href = baseUrl + hrefParam

            c = requests.get(href).content.decode('gbk')
            soupc = bs(c, 'lxml')
            table_items = soupc.find_all('table')
            indexc = 0

            parameterNode = ET.Element("参数")

            for table_item in table_items:
                if indexc > 0 and indexc < len(table_items) - 1:
                    soupc1 = bs(str(table_item), 'lxml')
                    th = soupc1.find('th')
                    thString = str(th)
                    thString = Reg.html(thString)
                    thString = re.sub(r3, '-', thString)
                    thNode = ET.Element(thString)

                    lis = soupc1.find_all('li')
                    for li in lis:
                        soupTemp = bs(str(li), 'lxml')
                        spans = soupTemp.find_all('span')
                        tag = ''
                        text = ''
                        x = 0
                        for span in spans:
                            if x == 0:
                                tag = Reg.html(str(span))
                                tag = re.sub(r3, '-', tag)
                                b = re.match(r5, tag)
                                if b:
                                    tag = 'x' + tag
                            else:
                                text = Reg.html(str(span))
                                text = re.sub(r4, '\n', text)
                            x += 1
                        subElement(thNode, tag, text)
                    parameterNode.append(thNode)
                indexc += 1
            nameNode.append(parameterNode)
        except Exception:
            print("no detail page")

        print(name + " --- " + price + ":   " + href)
        # gp.writeFile('folder/' + name + '-' + price, href)
        root.append(nameNode)
    try:
        next = soup.find('a', attrs={'class', 'next'})
        nextPage = next.get('href')
        index += 1
    except Exception:
        print("not next page")
        break
tree = ET.ElementTree(root)
tree.write("folder/" + keyWord + 'temp.xml', encoding='utf-8', xml_declaration=True)
