# -*-coding:UTF-8 -*-
import os
from DownHtml import GetHtml, GetPageNum, GetImageUrl, GetImage


page_num = GetPageNum()
print(u'当前ooxx总页数:%s' % page_num)

for i in range(1500, int(page_num)):
    print(u'正在下载---------第%d页' % i)
    if os.path.exists(r'/root/PycharmProjects/myspider/html/ooxx/%d.html' % i):
        print(u'%d.html 已经下载,跳过' % i)
        urls = GetImageUrl(
            '/root/PycharmProjects/myspider/html/ooxx/%d.html' % i)
        for url in urls:
            GetImage(url, "./meizitu")
    else:
        GetHtml('http://jandan.net/ooxx/page-%d#comments' % i,
                '/root/PycharmProjects/myspider/html/ooxx/%d.html' % i)
