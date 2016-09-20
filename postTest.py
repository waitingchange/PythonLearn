import urllib

params = urllib.urlencode({'uid': 8, 'data': 'jack', 'age': 25})
f = urllib.urlopen("http://localhost:8080/report/rlog",params)
print f.read()