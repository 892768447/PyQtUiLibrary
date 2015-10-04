#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年9月29日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 
'''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from uilib.widgets.BaseView import BaseView


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class BaseWidget(QWidget, BaseView):

    def __init__(self, parent = None):
        super(BaseWidget, self).__init__(parent)

    def setMouseTracking(self, tracking):
        super(BaseWidget, self).setMouseTracking(tracking)
        if tracking and self.testWindowFlags(Qt.FramelessWindowHint):
            # 设置了mouseTracking 和 无边框的时候
            self.setCanDrag(tracking)
            self.setDraged(tracking)
        else:
            self.setCanDrag(tracking)
            self.setDraged(tracking)

    def mousePressEvent(self, event):
        '''鼠标按下事件'''
        super(BaseWidget, self).mousePressEvent(event)
        self.dragParams["x"] = event.x()
        self.dragParams["y"] = event.y()
        self.dragParams["globalX"] = event.globalX()
        self.dragParams["globalY"] = event.globalY()
        self.dragParams["width"] = self.width()
        self.dragParams["height"] = self.height()
        if self.dragParams["type"] != self.MOVE and \
            event.button() == Qt.LeftButton and \
            not self.isMaximized() and \
            not self.isFullScreen() and self.getCanDrag():
            self.setDraged(True)
            self.dragParams["draging"] = True
            # self.dragPos = event.globalPos() - self.pos()    # self.frameGeometry().topLeft()

    def mouseReleaseEvent(self, event):
        '''鼠标释放事件'''
        super(BaseWidget, self).mouseReleaseEvent(event)
        self.setDraged(False)
        self.dragParams["type"] = self.MOVE
        self.dragParams["draging"] = False

    def mouseMoveEvent(self, event):
        '''鼠标移动事件'''
        super(BaseWidget, self).mouseMoveEvent(event)
        if self.getCanDrag() and not self.isMaximized() and not self.isFullScreen():
            # 判断鼠标类型
            cursorType = self.dragParams["type"]
            if not self.dragParams["draging"]:
                cursorType = self.dragParams["type"] = self.getCursorType(event.x(), event.y())
            # 设置鼠标形状
            if cursorType in (self.RESIZETOP, self.RESIZEBOTTOM):
                self.setCursor(Qt.SizeVerCursor)
            elif cursorType in (self.RESIZELEFT, self.RESIZERIGHT):
                self.setCursor(Qt.SizeHorCursor)
            elif cursorType in (self.RESIZETOP | self.RESIZERIGHT, self.RESIZELEFT | self.RESIZEBOTTOM):
                self.setCursor(Qt.SizeBDiagCursor)
            elif cursorType in (self.RESIZETOP | self.RESIZELEFT, self.RESIZERIGHT | self.RESIZEBOTTOM):
                self.setCursor(Qt.SizeFDiagCursor)
            elif self.dragParams["draging"]:
                self.setCursor(Qt.ArrowCursor)
            else:
                self.setCursor(Qt.ArrowCursor)
        # 判断窗口拖动
        dragType = self.dragParams["type"]
        print("dragType: ", dragType, " draging: ", self.dragParams["draging"])
        if self.dragParams["draging"] and \
            self.getDraged() and not self.isMaximized() and \
            not self.isFullScreen() and \
            event.buttons() == Qt.LeftButton and self.getCanDrag():
            x = self.x()
            y = self.y()
            width = self.width()
            height = self.height()
            if dragType == self.MOVE:
                x = event.globalX() - self.dragParams["x"]
                y = event.globalY() - self.dragParams["y"]
            elif self.getCanDrag():
                if dragType & self.RESIZETOP == self.RESIZETOP:
                    y = event.globalY() - self.dragParams["margin"]
                    height = self.dragParams["height"] + self.dragParams["globalY"] - event.globalY()
                elif dragType & self.RESIZEBOTTOM == self.RESIZEBOTTOM:
                    height = self.dragParams["height"] - self.dragParams["globalY"] + event.globalY()
                if dragType & self.RESIZELEFT == self.RESIZELEFT:
                    x = event.globalX() - self.dragParams["margin"]
                    width = self.dragParams["width"] + self.dragParams["globalX"] - event.globalX()
                elif dragType & self.RESIZERIGHT == self.RESIZERIGHT:
                    width = self.dragParams["width"] - self.dragParams["globalX"] + event.globalX()
            else:
                return

            if width < self.minimumWidth():
                width = self.minimumWidth()
            elif width > self.maximumWidth():
                width = self.maximumWidth()
            if height < self.minimumHeight():
                height = self.minimumHeight()
            elif height > self.maximumHeight():
                height = self.maximumHeight()

            self.setGeometry(x, y, width, height)
            # self.move(event.globalPos() - self.dragPos)
