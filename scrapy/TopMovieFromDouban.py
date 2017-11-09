import requests
from PIL import Image
from io import BytesIO
import re
import scrapy.func as func

topMovieURL = "https://movie.douban.com/top250?start="
reg = 'src="(.+?\.jpg)" class='
imgre = re.compile(reg)

index = 0

writeBack = ''
while index <= 250:
    url = topMovieURL + str(index)

    r = requests.get(url)
    content = r.content.decode("utf-8")

    writeBack += func.writeToTxt(index, content)

    index += 25
    print(index)

# print(writeBack)

output = open('TopMovieFromDouban/top250.txt', 'w+', encoding='utf-8')
output.write(writeBack)
output.close()
# print(x)

