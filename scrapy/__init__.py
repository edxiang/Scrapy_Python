import requests
import re

r = requests.get("https://movie.douban.com/top250?start=125")
content = r.content.decode('utf-8')

reg = re.compile(r'class="info">(.*?)</li>', re.M | re.S)
regHTML = re.compile(r'<.*?>', re.S)
regBlank = re.compile(r'\s{2}', re.S | re.M)
regSquare = re.compile(r'\[.*?\]', re.S)
regLine = re.compile(r'\s{3}', re.S | re.M)
regNext = re.compile(r'\n', re.M)


def writeToTxt(contents):

    contentList = reg.findall(contents)

    x = 0
    for c in contentList:
        s = re.sub(regBlank, "", c)
        ss = re.sub(regHTML, "", s)
        sss = re.sub(regLine, "\n", ss)

        statements = regNext.findall(sss)
        ssss = sss[1:len(sss) - 2]

        print(ssss)
        x += 1

# print(x)

# print(content)
