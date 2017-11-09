# coding = utf-8
import requests
import re

r = requests.get("https://img1.doubanio.com/view/group_topic/l/public/p96799829.jpg")
sz = open('helloworld/logo.jpg', 'wb').write(r.content)
print('helloworld/logo.jpg', sz, 'bytes')

# response = requests.get("http:" + imgurl)
# image = Image.open(BytesIO(response.content))
# image.save('helloworld/%s.jpg' % x)
