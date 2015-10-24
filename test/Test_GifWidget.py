#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年10月15日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 
'''

from __future__ import unicode_literals

from os.path import dirname, abspath
import sys

# 解决2.x到3.x的字符串问题
# 父级目录
sys.path.insert(0, dirname(dirname(abspath(sys.argv[0]))))
sys.path.insert(0, dirname(dirname(abspath(__file__))))


from PyQt5.QtCore import QMetaObject, pyqtSlot
from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QFileDialog

from uilib.Utils import QT5
from uilib.widgets.GifWidget import GifWidget

if QT5():
    from PyQt5.QtWidgets import QWidget, QApplication    # @UnusedImport
else:
    from PyQt4.QtGui import QWidget, QApplication    # @UnusedImport @UnresolvedImport @Reimport

__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class Widget(QWidget):

    def __init__(self):
        super(Widget, self).__init__()

        layout = QVBoxLayout(self)

        self.gif = GifWidget(self, "../images/yin.gif")

        startBtn = QPushButton("开始", self)
        startBtn.setObjectName("startBtn")

        stopBtn = QPushButton("停止", self)
        stopBtn.setObjectName("stopBtn")

        changeBtn = QPushButton("改变第二个图", self)
        changeBtn.setObjectName("changeBtn")

        layout.addWidget(self.gif)
        layout.addWidget(startBtn)
        layout.addWidget(stopBtn)
        layout.addWidget(changeBtn)

        QMetaObject.connectSlotsByName(self)    # 通过objectname注册信号

    @pyqtSlot()    # 这里主要是解决qt5和qt4的区别(不加这个会出现点击两次的效果)
    def on_startBtn_clicked(self):
        self.gif.start()

    @pyqtSlot()
    def on_stopBtn_clicked(self):
        self.gif.stop()

    @pyqtSlot()
    def on_changeBtn_clicked(self):
        fn, _ = QFileDialog.getOpenFileName(self, "选择动态图片", None, "Gif Files (*.gif)")
        if fn:
            self.gif.setPath(fn)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    sys.exit(app.exec_())
