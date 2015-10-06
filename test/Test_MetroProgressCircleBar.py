#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年10月6日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: Test_MetroProgressCircleBar
'''
from __future__ import unicode_literals
# 解决2.x到3.x的字符串问题
from os.path import dirname, abspath
import sys
# 父级目录
sys.path.insert(0, dirname(dirname(abspath(sys.argv[0]))))
sys.path.insert(0, dirname(dirname(abspath(__file__))))

from PyQt5.QtCore import QSize, QEasingCurve
from PyQt5.QtWidgets import QApplication, QMainWindow, QScrollArea, QWidget, \
    QGridLayout, QLabel, QVBoxLayout

from uilib.widgets.MetroProgress import MetroProgressCircleBar

__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class TestMetroProgressCircleBar(QMainWindow):

    def __init__(self, parent = None):
        super(TestMetroProgressCircleBar, self).__init__(parent)
        self.setObjectName("Test_MetroProgressCircleBar")
        self.resize(QSize(800, 600))
        self.mpbs = []    # 所有的进度条
        self.initView()
        self.setStyleSheet("QScrollArea,QWidget{background-color: rgb(0, 170, 255);}")

    def closeEvent(self, event):
        for mpb in self.mpbs:    # @UnusedVariable
            mpb.stop()    # 调用停止动画
        super(TestMetroProgressCircleBar, self).closeEvent(event)

    def initView(self):
        '''创建界面'''
        scrollArea = QScrollArea(self)    # 滚动区域
        scrollArea.setWidgetResizable(True)
        self.setCentralWidget(scrollArea)

        scrollWidget = QWidget()
        scrollArea.setWidget(scrollWidget)
        gridLayout = QGridLayout(scrollWidget)    # 网格布局

        # 从QEasingCurve获取所有的type
        curve_types = [(n, c) for n, c in QEasingCurve.__dict__.items()
            if isinstance(c, QEasingCurve.Type)]
        curve_types.sort(key = lambda ct: ct[1])
        i = 0
        for curve_name, curve_type in curve_types:
            index = curve_type % 4
            widget = QWidget()
            widget.setObjectName("_BorderWidget")
            widget.setStyleSheet("QWidget#_BorderWidget{border: 1px solid black;}")
            name = QLabel("QEasingCurve." + curve_name, widget)
            mpb = MetroProgressCircleBar(widget, curve_type)
            layout = QVBoxLayout(widget)
            layout.addWidget(name)
            layout.addWidget(mpb)
            gridLayout.addWidget(widget, i, index, 1, 1)
            if index == 3:
                i += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestMetroProgressCircleBar()
    window.show()
    sys.exit(app.exec_())
