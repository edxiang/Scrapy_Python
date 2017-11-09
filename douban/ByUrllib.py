# -*- coding: utf-8 -*-
import urllib.request as ur
import re

page = ur.urlopen("https://www.douban.com/group/topic/108652796/").read()

# s = str.encode('raw_unicode_escape')
# print(s)
# sss = s.decode()
# print(sss)
str = '123\r456\r'
reg = re.compile(r'\r')
s = re.sub(reg, "", str)
print(s)

# print(page)
