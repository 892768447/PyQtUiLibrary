#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年9月3日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 
'''

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QWidget


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class BaseWidget(QWidget):

    def __init__(self, parent = None):
        super(BaseWidget, self).__init__(parent)
        self.resize(QSize(400, 400))
        self._isDrag = False
        self.setCDrag(False)
        self.setShaked(False)

    def testWindowFlags(self, windowFlags):
        return self.windowFlags() & windowFlags

    def setAnimation(self, animation):
        self.animation = animation

    def setShaked(self, shaked):
        self.shaked = shaked

    def setCDrag(self, cdrag):
        self.cDrag = cdrag

    def setMouseTracking(self, tracking):
        super(BaseWidget, self).setMouseTracking(tracking)
        if tracking and self.testWindowFlags(Qt.FramelessWindowHint):
            # 设置了mouseTracking 和 无边框的时候
            self.setCDrag(True)

    def shake(self):
        if self.isMaximized() or self.isMinimized() or (not hasattr(self, "animation")):
            return    # 如果最大化或者最小化则不抖动
        self.setShaked(True)
        self.animation.shake()
        self.animation.finished.connect(lambda:self.setShaked(False))

    def resizeEvent(self, event):
        '''控件大小改变事件'''
        result = super(BaseWidget, self).resizeEvent(event)
        if hasattr(self, "animation"):
            self.animation.update()
        return result

    def show(self):
        super(BaseWidget, self).show()
        if hasattr(self, "animation"):
            self.animation.update()

    def showEvent(self, event):
        '''显示事件'''
        if hasattr(self, "animation"):
            self.animation.show()
        return super(BaseWidget, self).showEvent(event)

    def moveEvent(self, event):
        '''窗口移动事件'''
        if not self.shaked and hasattr(self, "animation"):    # 因为抖动的时候会触发该事件导致深度遍历异常
            self.animation.update()    # 没有抖动时窗口移动后更新动画抖动位置
        return super(BaseWidget, self).moveEvent(event)

    def mousePressEvent(self, event):
        '''鼠标按下事件'''
        if event.button() == Qt.LeftButton and self.cDrag:
            self._isDrag = True
            self.dragPos = event.globalPos() - self.pos()    # self.frameGeometry().topLeft()
        return super(BaseWidget, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        '''鼠标释放事件'''
        if self.cDrag:
            self._isDrag = False
        super(BaseWidget, self).mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        '''鼠标移动事件'''
        if self._isDrag and event.buttons() == Qt.LeftButton and self.cDrag:
            self.move(event.globalPos() - self.dragPos)
        return super(BaseWidget, self).mouseMoveEvent(event)

#     def event(self, event):
#         if not hasattr(self, "animation"):
#             return super(BaseWidget, self).event(event)
#         if self.animation.__name__ not in self.SHOW_CLOSE_ANIMS:
#             # 排除抖动
#             return super(BaseWidget, self).event(event)
#         if event.type() == QEvent.Show:
#             # 显示
#                 self.animation.show()
#         if event.type() == QEvent.Close or event.type() == QEvent.Hide:
#             # 隐藏和关闭
#             event.ignore()
#             self.animation.close()
#             self.animation.finished.connect(self.destroy)
#             return True
#         return super(BaseWidget, self).event(event)
