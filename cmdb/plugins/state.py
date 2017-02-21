#!/usr/bin/env python3
#-*- coding:utf-8 -*-
from cmdb.backends.base_module import BaseSaltModule

class State(BaseSaltModule):
    def __init__(self):
        print("in state module")
