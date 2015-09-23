#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年9月7日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 
'''
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from uilib.Application import Application
from PyQt5.QtCore import QTimer


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class Window(QWidget):

    def __init__(self, parent = None):
        super(Window, self).__init__(parent)
        self.value = 1
        # 加载ui文件
        self.ui = uic.loadUi("ui/Ui_QScrollBar_QProgressBar_QSlider.ui", self)
        self.ui.setStyleSheet("QWidget#Form{background-color:white;}")

        timer = QTimer(self)
        timer.timeout.connect(self.setProgress)
        timer.start(100)

    def setProgress(self):
        if self.value == 101:
            self.value = 1
        self.ui.progressBar.setValue(self.value)
        self.ui.progressBar_2.setValue(self.value)
        self.value += 1

if __name__ == "__main__":
    import sys
    app = Application(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
