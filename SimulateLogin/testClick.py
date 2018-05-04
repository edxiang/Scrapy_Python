# -*- coding: utf-8 -*-
from selenium import webdriver
import time

chromePath = r'D:\webDriver\chromedriver.exe'
browser = webdriver.Chrome(executable_path=chromePath)
url = "https://www.zhihu.com"
browser.get(url)
time.sleep(20)
browser.find_element_by_class_name("VoteButton--up").click()
print(browser.find_element_by_class_name("VoteButton--up").text)
# browser.find_element_by_id("su").click()

