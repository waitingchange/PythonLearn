# coding=utf-8
# !/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import argparse
import fileinput
import build


def main():

    build.main()



    # print 'input upload args'

    # host =  raw_input("host:")
    # needRemove =  raw_input("needRemove:")

    # parser = argparse.ArgumentParser()
    # parser.add_argument('-ho', '--host', default='42.62.24.250')
    #
    # parser.add_argument('-r', '--needRemove', default='true')




    # args = parser.parse_args()

    host = '42.62.24.250'
    needRemove = True






    path = os.getcwd()
    parent_path = os.path.dirname(path)
    dir = parent_path + "/"


    os.chdir(dir) # 切换到上层文件夹
    hasTest = os.path.exists('test.tar')
    if hasTest:
        print 'has tar,remove First'
        os.remove('test.tar')

    ddzFile = dir + 'libs/ddz.js'
    sstr = '"":"http://h5ali.tuyoo.com/helloh5/magictexas/"'

    if needRemove:
        properties = open(ddzFile,'rb+')
        lines = properties.readlines()
        d = ''
        for line in lines:
            c = line.replace(sstr, '"":""')
            d += c
            properties.seek(0)      #不要让python记住执行到这里，从文件头还始
            properties.truncate()   #清空文件
            properties.write(d)
        properties.close()

    compressFiles()
    upload(host)


    print 'complete'


def compressFiles():
    cmd = 'ls -l | xargs tar cvf test.tar'
    os.system(cmd)


def upload(host):

    if host:
        cmd = 'scp -i ~/Desktop/id_rsa.wjp -rp test.tar wangjunpeng@'+ host + ':/home/wangjunpeng/'
        os.system(cmd)
    else:
        print 'host error'


if __name__ == '__main__':
    main()
