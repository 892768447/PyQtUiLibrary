#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年9月3日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 
'''

from PyQt5.QtCore import Qt


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class BaseView(object):

    MOVE = 0
    RESIZETOP = 1
    RESIZERIGHT = 2
    RESIZEBOTTOM = 3
    RESIZELEFT = 4

    def __init__(self, *args, **kwargs):
        self.setDraged(False)
        self.setCanDrag(False)
        self.dragParams = {"type":0, "x":0, "y":0, "size":5, \
            "margin":0, "draging":False}

    def testWindowFlags(self, windowFlags):
        '''判断窗口是否拥有某个flag'''
        return self.windowFlags() & windowFlags

    def setCanDrag(self, cdrag):
        '''设置窗口是否可以拖动'''
        self._cDrag = cdrag

    def getCanDrag(self):
        return self._cDrag

    def setDraged(self, draged):
        self._isDrag = draged

    def getDraged(self):
        return self._isDrag

    def setHintFramelessWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMouseTracking(True)

    def isResizableX(self):
        '''
        @description: # 获取宽度是否可调整
        @return: true or false
        '''
        return self.minimumWidth() != self.maximumWidth()

    def isResizableY(self):
        '''
        @description: # 获取高度是否可调整
        @return: true or false
        '''
        return self.minimumHeight() != self.maximumHeight()

    def getCursorType(self, x, y):
        '''
        @description: #获取鼠标类型
        @type x: int
        @type y: int
        @param x: x坐标
        @param y: y坐标 
        @return: int
        '''
        width = self.width()
        height = self.height()
        size = self.dragParams["size"]
        margin = self.dragParams["margin"]
        isResizableX = self.isResizableX()
        isResizableY = self.isResizableY()
        cursorType = self.MOVE
        if x >= margin and x <= width - margin and y >= margin and y <= height - margin:
            if y <= size + margin and isResizableY:
                cursorType |= self.RESIZETOP
            elif y >= height - margin - size and isResizableY:
                cursorType |= self.RESIZEBOTTOM
            if x <= size + margin and isResizableX:
                cursorType |= self.RESIZELEFT
            elif x >= width - margin - size and isResizableX:
                cursorType |= self.RESIZERIGHT
        return cursorType
