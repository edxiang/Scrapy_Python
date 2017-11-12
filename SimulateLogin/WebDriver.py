import requests
import time
from selenium import webdriver

chromePath = r'D:\webDriver\chromedriver.exe'
wd = webdriver.Chrome(executable_path=chromePath)
time.sleep(45)
cookies = wd.get_cookies()
req = requests.Session()
for cookie in cookies:
    req.cookies.set(cookie['name'], cookie['value'])

req.headers.clear()
test = req.get("https://www.zhihu.com/question/67000176/answer/258369494")
c = test.content.decode('utf-8')
print(c)
