# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup as bs
import scrapy.Reg as reg


headers = {
    "Host": "www.douban.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Cookie": 'bid=b2xcDFPqLyE; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1508979672%2C%22https%3A%2F%2Faccounts.douban.com%2Flogin%3F%22%5D; _pk_id.100001.8cb4=1dbbda3993a5b692.1496827801.4.1508979681.1508925264.; __yadk_uid=mlaCNnEPX8hrUlNtS0BXot7OefwPq5dJ; ps=y; ue="229270808@qq.com"; push_noty_num=0; push_doumail_num=0; __utma=30149280.891040440.1508915824.1508923730.1508979674.3; __utmz=30149280.1508915824.1.1.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/login; __utmv=30149280.7366; ct=y; ap=1; _pk_ses.100001.8cb4=*; __utmb=30149280.12.5.1508979682515; __utmc=30149280; __utmt=1',
    "Connection": "keep-alive",
    "Upgrade_Insecure-Requests": "1",
    "Cache-Control": "max-age=0"
}

def info(url):
    print(url)
    # 获取整张网页
    output = open('douban/topic_ent.txt', 'a', encoding='utf-8')
    try:
        bx = requests.get(url, allow_redirects=False, timeout=10, headers=headers).content.split(b'\r')
        bl = ''
        for line in bx:
            bl += line.decode('utf-8')

        # 获取网页主要内容
        soup = bs(bl, 'lxml')
        list = soup.find('div', attrs={'id': 'content'})

        # get the title
        soup1 = bs(str(list), 'lxml')
        list1 = soup1.find('h1')
        title = reg.html(str(list1))
        title = reg.blank(title)
        output.write("    " + title[0:len(title) - 1] + "    ( " + url + " )\n")
        print(title[0:len(title)-1])

        # get the author and update time
        list2 = soup1.find('h3')
        s = reg.html(str(list2))
        ss = s.split('\n')
        if len(ss) >= 3:
            at = ss[1] + " - " + ss[2]
        else:
            at = str(ss)
        output.write("        ----" + at + "\n")
        # print(at)

        # get the essay
        paragraph = soup.find('div', attrs={'class': 'topic-content'})
        temp = bs(str(paragraph), 'lxml')
        forp = temp.find_all('p')
        regN = re.compile(r'<br/>')
        ps = ''
        for para in forp:
            s = re.sub(regN, '\n', str(para))
            ss = reg.html(s)
            sss = reg.blank(ss)
            ps += sss
        ps = reg.doubleLine(ps)
        output.write(ps)
        output.write('\n\n\n                    ' + "/**********************************/" + '\n\n\n\n')
    except Exception:
        print(url + " -------------------------------------------")
        info(url)
    finally:
        output.close()
