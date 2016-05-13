# coding=utf-8
# !/usr/bin/python
# -*- coding: UTF-8 -*-

    # -ss 命令, --dirww 参数,可以获取到,供代码使用   接受命令

import argparse


def main():
    paser = argparse.ArgumentParser()
    paser.add_argument("-ss","--dirww",default="aaa")

    args = paser.parse_args()


    print "pring...." , args

    dirww = args.dirww

    print "ddd" , dirww


if __name__ == '__main__':
    main()





