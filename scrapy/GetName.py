# -*- coding: utf-8 -*-
import re
import requests
import scrapy.Reg as reg

regName = re.compile(r'"v:itemreviewed">(.*?)</span>')
regInfo = re.compile(r'id="info">(.*?)<div id="interest_sectl">', re.S | re.M)
regPoint = re.compile(r'"v:average">(.*?)</strong>')

# index = 1
writeBack = ''


def getname(index, url):
    r = requests.get(url)
    content = r.content.decode('utf-8')

    titles = regName.findall(content)
    title = ''

    if len(titles) != 0:
        title = titles[0]

        s = regInfo.findall(content)[0]

        ss = reg.blank(s)
        sss = reg.nextLine(ss)

        regIMDb = re.compile(r'href="(.*?)" target')
        imdb = regIMDb.findall(sss)[0]

        ssss = reg.html(sss)

        point = regPoint.findall(content)[0]

        s = str(index + 1) + " " + title + "\n" + "评分：" + point + "\n" + ssss + " " + imdb + "\n\n"

        output = open('TopMovieFromDouban/top250_new.txt', 'a', encoding='utf-8')
        output.write((s.encode('utf-8').decode('utf-8')))
        output.close()
        return s
    else:
        output = open('TopMovieFromDouban/top250_new.txt', 'a')
        output.write("not exist: " + str(index + 1))
        output.close()
        return "not exist: " + str(index + 1)
