# -*- coding: utf-8 -*-

from selenium import webdriver
import time

driver = webdriver.Chrome(r'D:\webDriver\chromedriver.exe')
driver.get('https://www.taobao.com')
time.sleep(5)
print(driver.page_source)
