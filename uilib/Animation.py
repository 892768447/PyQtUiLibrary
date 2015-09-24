#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年9月24日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: Animation动画
'''
from PyQt5.QtCore import QPropertyAnimation

__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class OpacityAnimation():
    '''透明度动画'''

    def __init__(self, parent):
        self.animation = QPropertyAnimation(parent, b"windowOpacity")
        self.animation.setDuration(1000)

    def show(self):
        self.animation.stop()
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def close(self):
        self.animation.stop()
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()
