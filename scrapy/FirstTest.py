import requests
from PIL import Image
from io import BytesIO
import re

r = requests.get("https://jandan.net/ooxx")
print(r.status_code)
# print(r.headers['content-type'])
# print(r.encoding)

a = r.content.decode('utf-8')
reg = '<img src="(.+?\.jpg)" '
imgre = re.compile(reg)
imglist = imgre.findall(a)

x = 110

for imgurl in imglist:
    print("http:" + imgurl)
    # response = requests.get("http:" + imgurl)
    # image = Image.open(BytesIO(response.content))
    # image.save('helloworld/%s.jpg' % x)
    # x += 1
print(x)
# print(a)
# print(a)
