#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年9月23日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 
'''

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

from uilib.Application import Application
from uilib.widgets.MetroProgressCircleBar import MetroProgressCircleBar


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class Window(QWidget):

    def __init__(self, parent = None):
        super(Window, self).__init__(parent)
        self.setObjectName("Test_MetroProgressCircleBar")
        self.resize(QSize(400, 400))

        self.mpb = MetroProgressCircleBar(self)
        exitBtn = QPushButton("退出", self)
        exitBtn.clicked.connect(self.close)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.mpb)
        layout.addWidget(exitBtn)

        self.setStyleSheet("QWidget#Test_MetroProgressCircleBar{background-color: rgb(0, 170, 255);}")

    def close(self):
        self.mpb.stop()    # 调用
        super(Window, self).close()

if __name__ == "__main__":
    import sys
    app = Application(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
