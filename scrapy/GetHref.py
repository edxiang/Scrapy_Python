# -*- coding: utf-8 -*-

import requests
import re
import scrapy.GetName as name

baseURL = "https://movie.douban.com/top250?start="
reg = re.compile(r'<a href="(.*?)" class=""')
index = 230
writeBack = ''
while index < 250:
    url = baseURL + str(index)
    r = requests.get(url)
    content = r.content.decode('utf-8')

    contentList = reg.findall(content)
    for c in contentList:
        writeBack += name.getname(index, c)
        index += 1
        # print(c)
    print(index)

# output = open('TopMovieFromDouban/top250_new.txt', 'w+', encoding='utf-8')
# output.write(writeBack)
# output.close()
# print(content)
# done!

