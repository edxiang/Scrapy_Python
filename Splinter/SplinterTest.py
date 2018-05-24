# -*- coding: utf-8 -*-

from splinter import Browser
import time

executable_path = {'executable_path': r'D:\webDriver\chromedriver.exe'}
b = Browser('chrome', **executable_path)
b.visit('https://www.zhihu.com/people/si-kao-de-yu-di/answers')
# time.sleep(15)
b.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(1)
b.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(1)
b.execute_script('window.scrollTo(0,document.body.scrollHeight)')
htmlCode = b.html
print(htmlCode)
index = 0
#  works!
# for element in b.find_by_css(".ContentItem-more"):
#     try:
#         element.click()
#         time.sleep(1)
#     except Exception:
#         print(element.value)

# the vote button can't be clicked.
# b.find_by_css(".VoteButton--up").first.click()







# b.find_by_css(".AppHeader-profileAvatar").click()
# htmlCode1 = b.html
# print(htmlCode1)

