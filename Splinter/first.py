# -*- coding: utf-8 -*-
from splinter.browser import Browser
import time

# executable_path = {'executable_path': r'D:\webDriver\chromedriver.exe'}
# b = Browser('chrome', **executable_path)
b = Browser('firefox')
b.visit('https://www.manhuaren.com/m76571/')
time.sleep(30)
print(b.html)
# cs = b.cookies.all()
cs = b.find_elements_by_class_name("TopstoryItem--experimentExpand")
contentDivs = b.find_by_css("TopstoryItem--experimentExpand")
print(len(contentDivs))
print(len(cs))

