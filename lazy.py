# lazy.py


import os
import sys


def main():
    curPath = os.getcwd()
    os.listdir(curPath)

    for i in os.listdir(curPath):
        if os.path.isfile(os.path.join(curPath,i)):
            pass
        else:
            print 'remove folder' , i
            os.system('rm -rf ' + i)

    os.system('mkdir test')

    desPath = os.path.join(curPath,'test')

    print 'des path ' , desPath
    os.chdir(desPath)
    os.system('mv ../test.tar .')
    os.system('tar xvf test.tar')


    print 'clean complete'

if __name__ == '__main__':
    main()
