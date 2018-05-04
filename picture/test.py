# -*- coding: utf-8 -*-
import requests
import time
import os

url = "http://sc.chinaz.com/tubiao/171026234820.htm"
c = requests.get(url).content.decode('utf-8')
print(c)


# if os.path.exists('test'):
#     os.makedirs('你好啊`')
