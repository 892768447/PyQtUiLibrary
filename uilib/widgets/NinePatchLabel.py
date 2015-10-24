#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年10月22日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 
'''


from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QLabel

from uilib.NinePatch import NinePatch
from PyQt5.QtCore import pyqtSignal


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class NinePatchLabel(QLabel):

    clicked = pyqtSignal(str)    # 点击信号

    def __init__(self, parent = None, text = "", norImage = None, preImage = None):
        super(NinePatchLabel, self).__init__(text, parent)
        self.norImage = norImage
        self.preImage = preImage
        self.norNinePatch = NinePatch(norImage)
        self.preNinePatch = NinePatch(preImage)
        self.curNinePatch = self.norNinePatch

        if norImage and preImage:
            minWidth = min(self.norNinePatch.width(), self.preNinePatch.width())
            minHeight = min(self.norNinePatch.height(), self.preNinePatch.height())
        elif norImage:
            minWidth = self.norNinePatch.width()
            minHeight = self.norNinePatch.height()
        self.setWordWrap(True)
        self.adjustSize()
        self.resize(minWidth, minHeight)

    def __del__(self):
        if hasattr(self, "ninepatch"):
            del self.ninepatch

    def mousePressEvent(self, event):
        self.clicked.emit(self.text())
        super(NinePatchLabel, self).mousePressEvent(event)
        self.curNinePatch = self.preNinePatch    # 按下鼠标的效果
        if self.norImage and self.preImage:
            self.update()

    def mouseReleaseEvent(self, event):
        super(NinePatchLabel, self).mouseReleaseEvent(event)
        self.curNinePatch = self.norNinePatch    # 释放鼠标的效果
        if self.norImage and self.preImage:
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        try:
            self.curNinePatch.SetImageSize(self.width(), self.height())
            self.curNinePatch.Draw(painter, 0, 0)
        except Exception as e:
            print(e)
        super(NinePatchLabel, self).paintEvent(event)
