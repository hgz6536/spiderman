# -*-coding:UTF-8 -*-
import requests
import os
from pyquery import PyQuery as pq
'''
cook = {
    '2446045991': '82a6dZLGvG%2FA7QOtyZM0mzV7cmSuMBDj7f%2BFr0XTDg',
    '2407064163': '8b52JWdYpPNBJJNd09XSZmRmVMsY2mB%2Bv4LakKtr',
    'Hm_lvt_fd93b7fb546adcfbcf80c4fc2b54da2c': '1464344539, 1464573922',
    '_ga': 'GA1.2.538355161.1464344539',
    'jdna': '596e6fb28c1bb47f949e65e1ae03f7f5 #1464591028803',
    'Hm_lpvt_fd93b7fb546adcfbcf80c4fc2b54da2c': '1464591030',
    '_gat': '1',
}

'''


def GetProxy(filename):
    doc = pq(filename=filename)
    for tr in doc('tr').items():
        proxy = []
        for i in tr('.odd').items():
            ip = i.eq(0).text().split()[0]
            port = i.eq(0).text().split()[1]
            proxy.append(ip + ":" + port)
    return proxy


def GetHtml(url, filename):
    my_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
        'Referer': url,
        'Connection': 'keep-alive',
    }

    urlpage = requests.get(url, headers=my_header)
    print(u'下载-----%s' % url)
    if urlpage.status_code == 200:
        urlpage.encoding = 'utf-8'
        try:
            fp = open(filename, 'w')
        except Exception as e:
            print(e)
        else:
            fp.writelines(urlpage.text)
        finally:
            fp.close()
            print(u'下载-----%s-----成功' % url)
    else:
        print(u'HTTP状态码:%d,反爬机制起作用了,我们开始启用自动代理' % urlpage.status_code)
        ip_list = GetProxy('daili.html')
        proxies = {
            'http': 'http://%s' % ip_list[0]
        }

        urlpage = requests.get(url, headers=my_header, proxies=proxies)
        while urlpage.status_code != 200:
            del ip_list[0]
            if len(ip_list) == 0:
                GetHtml('http://www.xicidaili.com/nn', 'daili.html')
                ip_list = GetProxy('daili.html')
            proxies = {
                'http': 'http://%s' % ip_list[0]}
            urlpage = requests.get(url, headers=my_header, proxies=proxies)
        urlpage.encoding = 'utf-8'
        try:
            fp = open(filename, 'w')
        except Exception as e:
            print(e)
        finally:
            fp.close()
            print(u'下载-----%s-----成功' % url)


def GetPageNum():
    GetHtml('http://jandan.net/ooxx', 'ooxx.html')
    html = pq(filename='ooxx.html')
    current_page_num = html('.current-comment-page')
    current_page_num = current_page_num.eq(0).text().strip('[]')
    return current_page_num


def GetImageUrl(filename):
    html = pq(filename=filename)
    data = html('.view_img_link')
    lst = []
    for a in data.items():
        url = a('a').attr('href')
        lst.append(url)
    return lst


def GetImage(url, path):
    if url is None:
        pass
    else:
        if not os.path.exists(path):
            os.mkdir(path)
        path = path.rstrip('/')
        try:
            image_name = url.split('/')[-1]
        except Exception as e:
            print(u'%s 出现了问题:%s' % (url, e))
            pass
        if not os.path.exists(path + "/" + image_name):
            print(u'下载图片-----%s' % image_name)
            r = requests.get(url)
            with open(path + "/" + image_name, 'wb') as f:
                f.write(r.content)
        else:
            print(u'文件已经存在')
            pass
