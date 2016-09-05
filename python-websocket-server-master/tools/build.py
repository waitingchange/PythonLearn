#!/usr/bin/env python
#coding=utf-8

# build.py
 
#深度混淆游戏代码，混淆后直接替换源目录libs/ddz.js文件
#python build.py -d ../../trunk/singleddz_1.0/
#会自动读取project.json判断是否有before.js，如果有，则需要增加before.js为--extern参数

import sys

if sys.version_info < (2, 7):
	print("This script requires at least Python 2.7.")
	print("Please, update to a newer version: http://www.python.org/download/releases/")
	exit()

import argparse
import json
import os
import shutil

def build(pro_root):
	cocos_path = os.path.join(pro_root, "libs/cocos.js")	
	output = os.path.join(pro_root, "libs/ddz.js")
	currentdir = os.path.dirname(os.path.abspath(__file__))
	jsonpath = "includes.json"	
	hasbefore = False
	
	#读取project.json里的jslist，获得需要混淆的js列表，并加上刚才生成的main.js
	pf = open(os.path.join(pro_root, "project.json"), "r")
	ps = pf.read()
	pf.close()
	po = json.loads(ps)
	jslist = po["jsList"]
	if(jslist[0] == "src/before.js"):	# before.js存储不能被混淆的作用域，如果没有则不需要此文件。例如代码里使用了eval方法时，其字符串内涉及的命名空间不能被混淆
		hasbefore = True
		jslist.pop(0)
	jslist = [x for x in jslist if not "/test/" in x]
	sources = [pro_root + filename for filename in jslist]
	sources.append(os.path.join(pro_root, "main.js"))	#把刚才生成的 main.js加上	
	source = ' '.join(sources)
	# print source
	
	# jscomp_off 关闭某个类型的警告信息， externs 表示使用到的外部的库，这里面的库函数的名字不能在混淆时被改变
	# Source Map 用于将压缩后的代码和压缩前的做一个映射，这样在使用压缩过的代码来进行调试时，可以单步跟入原来的代码
	# 优化的级别可以是 WHITESPACE_ONLY SIMPLE_OPTIMIZATIONS ADVANCED_OPTIMIZATIONS   --language_in=ECMASCRIPT5_STRICT 是会添加 'use strict';
	cmd = ""
	
	compiler_path = os.path.join(currentdir, "compiler.jar")
	if hasbefore:
		before_path = pro_root + "src/before.js"
		cmd = 'java -jar %s --compilation_level ADVANCED_OPTIMIZATIONS --jscomp_off uselessCode --jscomp_off globalThis --externs %s --externs %s --js %s --js_output_file %s' % (compiler_path, cocos_path, before_path, source, output)
	else:
 		cmd = 'java -jar %s --compilation_level ADVANCED_OPTIMIZATIONS --jscomp_off uselessCode --jscomp_off globalThis --externs %s --js %s --js_output_file %s' % (compiler_path, cocos_path, source, output)
	os.system(cmd)

	#如果libs下有before_uncompressed.js，则混淆此文件
	beforepath = os.path.join(pro_root, "libs/before_uncompressed.js")
	beforeoutpath = os.path.join(pro_root, "libs/before.js")
	if os.path.exists(beforepath):
		cmd = 'java -jar %s --compilation_level ADVANCED_OPTIMIZATIONS --js %s --js_output_file %s' % (compiler_path, beforepath, beforeoutpath)
		os.system(cmd)

def main(argv=None):
	parser = argparse.ArgumentParser()
	parser.add_argument('-d', '--directory', default='../') # 项目路径，src必须以此路径为根目录

	args = parser.parse_args()
	pro_root = args.directory
	build(pro_root)

if __name__ == "__main__":
	main()
