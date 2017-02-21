#!/usr/bin/env python3
#-*- coding:utf-8 -*-

class BaseSaltModule():
    def __init__(self,sys_argvs):
        self.sys_argvs = sys_argvs
        self.fetch_hosts()

    def fetch_hosts(self):
        print("--fetching hosts--")