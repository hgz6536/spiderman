#!env python
import requests
from pyquery import PyQuery as pq


my_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
    'Referer': 'http://jandan.net/ooxx',
}

html = requests.get(
    'http://jandan.net/ooxx/page-2001#comments', headers=my_header)
html = html.text
data = pq(html)
# print(data)
# current_page_num = data('.current-comment-page')

# current_page_num = current_page_num.eq(0).text().strip('[]')

images_url = data('.view_img_link')
print(images_url('a').attr('href'))
