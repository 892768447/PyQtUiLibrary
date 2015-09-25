#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年9月24日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 动画测试
'''

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

from uilib.Animation import ShakeAnimation, OpacityAnimation
from uilib.Application import Application
from uilib.widgets.base import BaseWidget


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class OpacityWindow(BaseWidget):
    '''淡入淡出窗口'''

    def __init__(self, parent = None):
        super(OpacityWindow, self).__init__(parent)

class ShakeWindow(BaseWidget):
    '''抖动窗口'''

    def __init__(self, parent = None):
        super(ShakeWindow, self).__init__(parent)
        shakeBtn = QPushButton("抖动", self)
        shakeBtn.clicked.connect(self.shake)
        layout = QVBoxLayout(self)
        layout.addWidget(shakeBtn)

class HintFramelessWindow(BaseWidget):
    '''无边框窗口'''

    def __init__(self, parent = None):
        super(HintFramelessWindow, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)    # 无边框
        self.setMouseTracking(True)
        shakeBtn = QPushButton("抖动", self)
        shakeBtn.clicked.connect(self.shake)
        exitBtn = QPushButton("退出", self)
        exitBtn.clicked.connect(self.close)
        layout = QVBoxLayout(self)
        layout.addWidget(shakeBtn)
        layout.addWidget(exitBtn)

class Window(QWidget):

    WINDOWS = []

    def __init__(self, parent = None):
        super(Window, self).__init__(parent)
        # 加载ui文件
        self.ui = uic.loadUi("ui/Ui_Animation.ui", self)
        self.ui.closeButton.clicked.connect(self.close)
        self.ui.listWidget.itemClicked.connect(self.onItemClick)

    def closeEvent(self, event):
        for window in self.WINDOWS:
            window.close()
        super(Window, self).closeEvent(event)

    def onItemClick(self, item):
        '''列表单击事件'''
        which = self.ui.listWidget.indexFromItem(item).row()
        if which == 0:    # 淡入淡出
            self.w = OpacityWindow()
            self.w.setAnimation(OpacityAnimation(self.w))
            self.w.show()
            self.WINDOWS.append(self.w)
        if which == 1:    # 左进右出
            pass
        if which == 2:    # 右进左出
            pass
        if which == 3:    # 上进下出
            pass
        if which == 4:    # 下进上出
            pass
        if which == 5:    # 抖动动画
            self.w = ShakeWindow()
            self.w.setAnimation(ShakeAnimation(self.w))
            self.w.show()
            self.WINDOWS.append(self.w)
        if which == 6:    # 无边框拖动
            self.w = HintFramelessWindow()
            self.w.setAnimation(ShakeAnimation(self.w))
            self.w.show()
            self.WINDOWS.append(self.w)

if __name__ == "__main__":
    import sys
    app = Application(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
