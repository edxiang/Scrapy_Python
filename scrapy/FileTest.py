import requests
import re
from bs4 import BeautifulSoup

# r = requests.get("https://movie.douban.com/top250?start=0")

login_cookies = {
    "bid": "b2xcDFPqLyE",
    "_pk_ref.100001.8cb4": '["","",1496827801,"http://localhost:8080/album/62"]',
    "_pk_id.100001.8cb4": "1dbbda3993a5b692.1496827801.1.1496827801.1496827801.",
    "__yadk_uid": "mlaCNnEPX8hrUlNtS0BXot7OefwPq5dJ",
    "ps": "y",
    "ue": "229270808@qq.com",
    "dbcl2": "73662444:kZ8cxT2ErhE"
}
headers = {
    "Accept": "text/event-stream",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
    "Host": "push.douban.com:4397",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
    "Referer": "https://www.douban.com/group/topic/93369105/",
    "Origin": "https://www.douban.com",
    "Pargma": "no-cache",
    "Cache-Control": "no-cache",
    "Cookie": 'll="118297"; bid=1kDfLtnhQ7M; __yadk_uid=KoUBpSUyxOTiMKK5ePLvclDH49qDpgHg; ct=y; ap=1; gr_user_id=74f12538-02b7-4ad8-b0d7-2e2d2c94a68e; _vwo_uuid_v2=FD8C71DC2B82B6D9C199B310B2D31500|03a10dd96aec6b02f857957ec6c93345; ps=y; ue="229270808@qq.com"; dbcl2="73662444:rd9yUWd0zUw"; ck=O6l9; push_noty_num=0; push_doumail_num=0; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1508925690%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DHsiZwX_o1xuSQbXjJjdzvBIcnredJj5XaQZpe9RCpLS%26wd%3D%26eqid%3Dd8ce0ad00001520f0000000659edb7a6%22%5D; _pk_id.100001.8cb4=2c63b81b66fd08fe.1501229483.9.1508925690.1508914744.; _pk_ses.100001.8cb4=*; __utmt=1; __utma=30149280.1024000994.1500542751.1508910160.1508925691.23; __utmb=30149280.6.5.1508925691; __utmc=30149280; __utmz=30149280.1508910160.22.15.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=30149280.7366'
}
# s = requests.Session()
# s.cookies = headers
# scont = s.get("https://www.douban.com/group/topic/93369105/")
# soup = BeautifulSoup(scont.text, 'lxml', from_encoding='utf-8')
# print(soup)

r = requests.get("https://www.douban.com/group/topic/93369105/", headers=headers)
c = r.content.decode("utf-8")
print(c)

#
# reg = re.compile(r'<a href="(.*?)" class=""')
# list = reg.findall(c)
#
# for l in list:
#     print(l)
