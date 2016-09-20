# structTest.py
#coding=utf8

import logging

import struct
import sys
import os



print '===== pack - unpack ====='  
  
str = struct.pack("ii", 20, 400)  
print 'str:', str  
print 'len(str):', len(str) # len(str): 8 

a1, a2 = struct.unpack("ii", str)  
print "a1:", a1  # a1: 20  
print "a2:", a2  # a2: 400  
  
print 'struct.calcsize:', struct.calcsize("ii") # struct.calcsize: 8  


print '===== unpack ====='  
  
string = 'test astring'  
format = '5s 4x 3s'  
print struct.unpack(format, string) # ('test ', 'ing')  
  
string = 'he is not very happy'  
format = '2s 1x 2s 5x 4s 1x 5s'  
print struct.unpack(format, string) # ('he', 'is', 'very', 'happy')  

FILE = os.getcwd()
logging.basicConfig(filename=os.path.join(FILE,'log.txt'),level=logging.DEBUG)
logging.debug('写进去')
logging.info('滚进去')
logging.warning('也滚进去')