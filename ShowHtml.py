# -*- coding: utf-8 -*-
import requests

html = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=splinter&rsv_pq=ffe5817c00002ce5&rsv_t=3686JjDzPkxvZZevzTwQAqV4ESN8BZPlYE3C0IquMAcHLvW3BHb6uyJikZo&rqlang=cn&rsv_enter=0&rsv_sug3=8&inputT=153&rsv_sug4=153'

r = requests.get(html)
print(r.content.decode('utf-8'))
