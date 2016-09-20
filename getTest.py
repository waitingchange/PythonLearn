import urllib

params = urllib.urlencode({'id': 8, 'name': 'jack', 'age': 25})
f = urllib.urlopen("http://localhost:8080/report/crash_native%s" % params)
print f.read()