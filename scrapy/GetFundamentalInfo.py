import requests
import re
import scrapy.func as func

r = requests.get("https://movie.douban.com/subject/1293929/")
content = r.content.decode('utf-8')
# print(content)

reg = re.compile(r'id="info">(.*?)<div id="interest_sectl">', re.S | re.M)
s = reg.findall(content)[0]

regBlank = re.compile(r'\s{2}', re.S | re.M)
ss = re.sub(regBlank, "", s)

regNextLine = re.compile(r'<br/>')
sss = re.sub(regNextLine, "\n", ss)

regIMDb = re.compile(r'href="(.*?)" target')
imdb = regIMDb.findall(sss)[0]

regHTML = re.compile(r'<.*?>', re.S)
ssss = re.sub(regHTML, "", sss)
print(ssss, imdb)

# print(s)
# done!