# -*- coding: utf-8 -*-

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('https:www.zhihu.com')
time.sleep(20)
js = "var q=document.documentElement.scrollTop=100;"
driver.execute_script(js)
driver.execute_script(js)
driver.execute_script(js)
print(driver.page_source)
cs = driver.find_elements_by_class_name("TopstoryItem--experimentExpand")
# 点击不能成功执行
for c in cs:
    d = c.find_element_by_class_name("VoteButton--up")
    d.click()
    break
print(len(cs))
