from pyquery import PyQuery as pq
fileToSave = open('imglinks.txt', 'w')

my_header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
    'referer': 'http://jandan.net/ooxx',
}

for page_number in range(9190, 9192):
    url = "http://jandan.net/pic/page-" + str(page_number)
    html_content = pq(url, headers=my_header)

    jpg_container = []
    for anchor in html_content('#comments p>img'):
        anchor = html_content(anchor)
        jpg_link = anchor.attr('src')
        jpg_container.append(jpg_link)
        fileToSave.write(jpg_link + '\n')

    print(page_number)
fileToSave.close
