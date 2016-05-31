# coding=utf-8




# 进度回调
import StringIO
import gzip
import os
import re
import urllib
import urllib2
from bs4 import BeautifulSoup


def schedule(a, b, c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print '%.2f%%' % per


def downLoadAll(urls):
    pass


def getImg(html, index):
    reg = r'original=.+?\.jpg'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)

    picpath = 'pic/' + str(index)
    if not os.path.exists(picpath):
        os.makedirs(picpath)

    x = 0
    for imgurl in imglist:
        print imgurl
        url = imgurl[10:]
        urllib.urlretrieve(url, picpath + '/%s.jpg' % x, schedule)
        x = x + 1


def getUrls(url):
    # soup = BeautifulSoup(url,'html.parser',from_encoding='utf-8')

    reg = r'http:\/\/www.mzitu.com\/[0-9]{3,10}'
    urlre = re.compile(reg)
    urllist = urlre.findall(url)

    index = 0
    for uri in urllist:
        print 'link is ' + uri
        data = paraseHtml(uri)
        getImg(data, index)
        index = index + 1



        # urls = []
        # return urls


def paraseHtml(url):
    req_header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.86 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Connection': 'keep-alive',
        'Host': 'www.mzitu.com'
    }
    req_timeout = 5
    req = urllib2.Request(url, None, req_header)
    resp = urllib2.urlopen(req, None, req_timeout)
    html = resp.read()
    data = StringIO.StringIO(html)
    gzipper = gzip.GzipFile(fileobj=data)
    html = gzipper.read()
    return html


def main():
    url = "http://www.mzitu.com/xinggan/"
    data = paraseHtml(url)
    lenth = 100

    getUrls(data)
    # urls = getUrls(url)
    # downLoadAll(urls)

if __name__ == '__main__':
    main()
