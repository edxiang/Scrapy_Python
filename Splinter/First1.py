# -*- coding: utf-8 -*-
from splinter import Browser

html = 'https://kyfw.12306.cn/otn/index/init'

executable_path = {'executable_path': r'D:\webDriver\chromedriver.exe'}
b = Browser('chrome', **executable_path)
b.visit(html)
b.find_by_text(u'登录').click()
username = '229270808@qq.com'
pwd = 'edxiao333'
b.fill('loginUserDTO.user_name', username)
b.fill('userDTO.password', pwd)

