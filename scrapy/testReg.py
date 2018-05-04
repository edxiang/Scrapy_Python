# -*- coding: utf-8 -*-
import scrapy.Reg as reg
import requests

r = requests.get("https://movie.douban.com/subject/1293929/")
content = r.content.decode('utf-8')
# print(content)

s = reg.html(content)
ss = reg.blank(s)
print(ss)
