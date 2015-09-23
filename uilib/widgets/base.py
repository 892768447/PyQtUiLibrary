#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年9月3日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 
'''
from PyQt5.QtCore import QObject

__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class Base(QObject):

    def shake(self):
        print("shake")
