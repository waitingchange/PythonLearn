# coding=utf-8
import StringIO
import gzip
import os
import re
import urllib
import urllib2


def schedule(a, b, c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print '%.2f%%' % per


def getHtml(url):
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


def getImg(html):
    reg = r'original=.+?\.jpg'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)

    picpath = 'pic'
    if not os.path.exists(picpath):
        os.makedirs(picpath)

    x = 0
    for imgurl in imglist:
        url = imgurl[10:]
        urllib.urlretrieve(url, picpath + '/%s.jpg' % x, schedule)
        x = x + 1


if __name__ == '__main__':
    html = getHtml("http://www.mzitu.com/xinggan/")
    getImg(html)


#   请执行 python downloadPic.py   福利不谢

