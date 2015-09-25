#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年9月24日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: Animation动画
'''
from PyQt5.QtCore import QPropertyAnimation, QPoint


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class BaseAnimation():

    @property
    def __name__(self):
        return self.__class__.__name__

    def show(self):
        pass

    def close(self):
        pass

    def update(self):
        pass

    def shake(self):
        pass

class ShakeAnimation(QPropertyAnimation, BaseAnimation):
    '''晃动动画'''

    def __init__(self, parent):
        super(ShakeAnimation, self).__init__(parent, b"pos")
        self.setDuration(500)
        self.parent = parent
        x = parent.x()
        y = parent.y()
        print("x: {x} y:{y}".format(x = x, y = y))
        x3 = QPoint(x - 3, y)
        x6 = QPoint(x + 6, y)
        x66 = QPoint(x - 6, y)
        self.setKeyValueAt(0, x3)
        self.setKeyValueAt(0.1, x6)
        self.setKeyValueAt(0.2, x66)
        self.setKeyValueAt(0.3, x6)
        self.setKeyValueAt(0.4, x66)
        self.setKeyValueAt(0.5, x6)
        self.setKeyValueAt(0.6, x66)
        self.setKeyValueAt(0.7, x6)
        self.setKeyValueAt(0.8, x66)
        self.setKeyValueAt(0.9, x6)
        self.setKeyValueAt(1, x3)

    def update(self):
        x = self.parent.x()
        y = self.parent.y()
        print("update x: {x} y:{y}".format(x = x, y = y))
        x3 = QPoint(x - 3, y)
        x6 = QPoint(x + 6, y)
        x66 = QPoint(x - 6, y)
        self.setKeyValueAt(0, x3)
        self.setKeyValueAt(0.1, x6)
        self.setKeyValueAt(0.2, x66)
        self.setKeyValueAt(0.3, x6)
        self.setKeyValueAt(0.4, x66)
        self.setKeyValueAt(0.5, x6)
        self.setKeyValueAt(0.6, x66)
        self.setKeyValueAt(0.7, x6)
        self.setKeyValueAt(0.8, x66)
        self.setKeyValueAt(0.9, x6)
        self.setKeyValueAt(1, x3)

    def shake(self):
        self.start()

class OpacityAnimation(QPropertyAnimation, BaseAnimation):
    '''透明度动画'''

    def __init__(self, parent):
        super(OpacityAnimation, self).__init__(parent, b"windowOpacity")
        self.setDuration(1000)

    def show(self):
        self.stop()
        self.setStartValue(0)
        self.setEndValue(1)
        self.start()

    def close(self):
        self.stop()
        self.setStartValue(1)
        self.setEndValue(0)
        self.start()
