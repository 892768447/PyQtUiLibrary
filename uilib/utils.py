#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年9月29日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 
'''
from functools import wraps
import sys


_QT5 = _QT4 = False

try:
    import PyQt5.QtCore    # @UnusedImport
    _QT5 = True
except:
    import PyQt4.QtCore    # @UnresolvedImport @UnusedImport
    _QT4 = True

__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

def SELF(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        method(self, *args, **kwargs)
        return self
    return wrapper

def PY3():
    return sys.version_info.major >= 3

def QT5():
    return _QT5

def QT4():
    return _QT4
