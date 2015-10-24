#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年10月1日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 
'''

from uilib.Utils import PY3

if PY3():
    from PyQt5.QtCore import QPropertyAnimation, QRect    # @UnresolvedImport @UnusedImport
else:
    from PyQt4.QtCore import QPropertyAnimation, QRect    # @Reimport @UnresolvedImport

__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class OverlayImageAnimation(QPropertyAnimation):

    def __init__(self, target, parent = None):
        super(OverlayImageAnimation, self).__init__(target, b"geometry", parent)
        self.parent = parent
        self.setDuration(200)
        self._width = self.parent.width()
        self._height = self.parent.height()
        self.setStartValue(QRect(0, 0, self._width, self._height))
        self.setEndValue(QRect(20, 20, self._width - 40, self._height - 40))

    def updateCurrentTime(self, currentTime):
        width = self.parent.width()
        height = self.parent.height()
        if width != self._width or height != self._height:
            self.setStartValue(QRect(0, 0, width, height))
            self.setEndValue(QRect(20, 20, width - 40, height - 40))
        super(OverlayImageAnimation, self).updateCurrentTime(currentTime)
