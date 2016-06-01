# -*-coding:UTF-8 -*-
import os
from DownHtml import GetHtml, GetPageNum, GetImageUrl, GetImage, GetProxy


page_num = GetPageNum()
print(u'当前ooxx总页数:%s' % page_num)
ip_list = GetProxy('daili.html')
for i in range(1500, int(page_num)):
    print(u'正在下载---------第%d页' % i)
    if os.path.exists(r'/root/PycharmProjects/myspider/html/ooxx/%d.html' % i):
        print(u'%d.html 已经下载,跳过' % i)
        urls = GetImageUrl(
            '/root/PycharmProjects/myspider/html/ooxx/%d.html' % i)
        for url in urls:
            GetImage(url, "./meizitu")
    else:
        status = GetHtml('http://jandan.net/ooxx/page-%d#comments' % i,
                         '/root/PycharmProjects/myspider/html/ooxx/%d.html' % i)
        if status == 503:
            print(u'HTTP状态码:%d,反爬机制起作用了,我们开始启用自动代理' % status)
            proxies = {
                'http': 'http://%s' % ip_list[0]
            }
            print(u'当前代理：%s' % ip_list[0])
            status = GetHtml('http://jandan.net/ooxx/page-%d#comments' %
                             i, '/root/PycharmProjects/myspider/html/ooxx/%d.html' % i, proxy=proxies)

            if status != 200:
                print(status)
                print(u'-----代理不可用了,换代理------')
                del ip_list[0]
                if len(ip_list) == 0:
                    os.remove('daili.html')
                    ip_list = GetProxy('daili.html')
                proxies = {
                    'http': 'http://%s' % ip_list[0]
                }

                print(u'当前代理：%s' % ip_list[0])
                status = GetHtml('http://jandan.net/ooxx/page-%d#comments' %
                                 i, '/root/PycharmProjects/myspider/html/ooxx/%d.html' % i, proxy=proxies)
