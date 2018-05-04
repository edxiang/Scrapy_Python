# Scrapy_Python

最开始做的是 scrapy 这个包里面的东西，爬了豆瓣电影 Top250（存储在 txt 的文本中），其中还包括图片（虽然不是高清的。）

接着是 douban 这个包，爬取了豆瓣一些话题下的所有文章，当初好像只爬了两个话题 科技 和 娱乐。
有空可以整理整理这个包的东西，不然以后要用 Python 来爬东西又得花一堆时间去找资料。

最后是中关村的一些电子产品，在包 zol 里面。这个是17年12月份做完的吧，爬下来的数据用 xml 文件保存。
算是比较完整和可读的一个例子了。。。

最开始学习 Python，其实是想爬 知乎 上的数据，兜兜转转，最终使用模拟器来获取 知乎 回答的源码（模拟点击还是有问题，本来想着把页面上的所有答案都赞一遍）。
知乎 好像是控制爬虫最严格的网站了，不然也不会用到 模拟器（chromedriver.exe）了。

至于为什么没有做下去了，一部分原因是不知道怎么使用 python 多线程来爬网页；一部分原因是无法连接上数据库。
其实都是用的 java 的思维来考虑这语言：java 的多线程用 concurrent 包很容易实现；连接数据库的话，有 mybatis 和 hibernate，方便了许多。
因此，帮同学爬了一部分 zol 的数据后，就转头研究 java 的爬虫技术了。
而 java 爬数据，虽说代码多了一些，但也挺方便的，有了 Apache 的 http 包，和解析网页的 jsoup（好像也上传到 github 上了）。
用 java 的多线程爬了一几个G的图片（具体耗费的时间不知道有没有记录），就停在这里了。想着爬下来的数据似乎也没有什么用。


大致就是这么回事了。听说 Python 好像可以用在 人工智能上？
不过嘛，还是比较喜欢 java。