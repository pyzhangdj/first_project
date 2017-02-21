#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import os
#linux命令执行脚本
def execute_cmd(cmd):
	result = os.popen(cmd)
	text = result.read()
	result.close()
	return text

if __name__ == "__main__":
	result = execute_cmd('ifconfig')
	print(result)
