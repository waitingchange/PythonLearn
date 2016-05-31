import base64

str = 'haha'
endStr = base64.b64encode(str)

print 'endstr is ' + endStr



str1 = 'aGFoYQ=='

endStr1 = base64.b64decode(str1)


print 'end str is ' , endStr1

