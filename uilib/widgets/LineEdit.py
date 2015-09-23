#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年9月3日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 
'''
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QLineEdit

from uilib.widgets.base import Base


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class LineEdit(QLineEdit, Base):

    SEARCH = pyqtSignal(str)    # 搜索信号

    def __init__(self, parent = None, contents = "", styles = []):
        super(LineEdit, self).__init__(contents, parent)
        self.search_left = False
        self.autoClearButtonEnabled = False
        for style in styles:
            self.setProperty(style, True)
            if style == "search-left":
                self.search_left = True

    def setAutoClearButtonEnabled(self, enabled = False):
        '''设置是否自动隐藏清空按钮'''
        self.autoClearButtonEnabled = enabled

    def focusOutEvent(self, event):
        '''设置清空按钮隐藏'''
        if self.autoClearButtonEnabled:
            self.setClearButtonEnabled(False)
        return super(LineEdit, self).focusOutEvent(event)

    def focusInEvent(self, event):
        '''设置清空按钮显示'''
        if self.autoClearButtonEnabled:
            self.setClearButtonEnabled(True)
        return super(LineEdit, self).focusInEvent(event)

    def mouseMoveEvent(self, event):
        '''鼠标移动到搜索区域 时改变形状'''
        if self.search_left:
            x = event.x()
            y = event.y()
            height = self.height()
            if (x > 0 and x < height) and (y > 0 and y < height):
                self.setCursor(Qt.ArrowCursor)
            else:
                self.setCursor(Qt.IBeamCursor)
        return super(LineEdit, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        '''点击搜索区域'''
        if self.search_left:
            x = event.x()
            y = event.y()
            height = self.height()
            if (x > 0 and x < height) and (y > 0 and y < height):
                self.SEARCH.emit(self.text())
        return super(LineEdit, self).mouseReleaseEvent(event)
