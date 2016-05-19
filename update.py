# coding=utf-8
# 遍历循环当前文件夹下的文件夹,然后每一个执行up

import os
import sys


def main():
    curPath = os.getcwd()

    print os.listdir(curPath)

    for i in os.listdir(curPath):
        if os.path.isfile(os.path.join(curPath,i)):
            pass
        else:
            childPath = os.path.join(curPath,i)
            os.chdir(childPath)
            os.system('svn up')

    print 'update complete'


if __name__ == '__main__':
    main()


