#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年9月25日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 
'''
from PyQt5.QtCore import QRect, QSize
from PyQt5.QtWidgets import QWidget, QGridLayout, QSpacerItem, QSizePolicy

from uilib.animations.MpcbAnimation import MpcbAnimation


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

STYLE = """
QWidget[circle="true"] {
    background-color: white;
    max-width: 8px;
    max-height: 8px;
    border-radius: 4px;
}
"""

class Ui_MetroProgressCircleBar(object):
    def setupUi(self, MetroProgressCircle):
        MetroProgressCircle.setObjectName("MetroProgressCircle")
        MetroProgressCircle.resize(100, 100)
        self.gridLayout = QGridLayout(MetroProgressCircle)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.MetroProgressCircleBar = QWidget(MetroProgressCircle)
        self.MetroProgressCircleBar.setMinimumSize(QSize(100, 100))
        self.MetroProgressCircleBar.setMaximumSize(QSize(100, 100))
        self.MetroProgressCircleBar.setObjectName("MetroProgressCircleBar")
        self.MetroProgressCircleBar1 = QWidget(self.MetroProgressCircleBar)
        self.MetroProgressCircleBar1.setGeometry(QRect(92, 46, 8, 8))
        self.MetroProgressCircleBar1.setObjectName("MetroProgressCircleBar1")
        # 这里设置属性
        self.MetroProgressCircleBar1.setProperty("circle", True)
        self.MetroProgressCircleBar2 = QWidget(self.MetroProgressCircleBar)
        self.MetroProgressCircleBar2.setGeometry(QRect(92, 46, 8, 8))
        self.MetroProgressCircleBar2.setObjectName("MetroProgressCircleBar2")
        self.MetroProgressCircleBar2.setProperty("circle", True)
        self.MetroProgressCircleBar3 = QWidget(self.MetroProgressCircleBar)
        self.MetroProgressCircleBar3.setGeometry(QRect(92, 46, 8, 8))
        self.MetroProgressCircleBar3.setObjectName("MetroProgressCircleBar3")
        self.MetroProgressCircleBar3.setProperty("circle", True)
        self.MetroProgressCircleBar4 = QWidget(self.MetroProgressCircleBar)
        self.MetroProgressCircleBar4.setGeometry(QRect(92, 46, 8, 8))
        self.MetroProgressCircleBar4.setObjectName("MetroProgressCircleBar4")
        self.MetroProgressCircleBar4.setProperty("circle", True)
        self.MetroProgressCircleBar5 = QWidget(self.MetroProgressCircleBar)
        self.MetroProgressCircleBar5.setGeometry(QRect(92, 46, 8, 8))
        self.MetroProgressCircleBar5.setObjectName("MetroProgressCircleBar5")
        self.MetroProgressCircleBar5.setProperty("circle", True)
        self.gridLayout.addWidget(self.MetroProgressCircleBar, 1, 1, 1, 1)
        spacerItem3 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)

class MetroProgressCircleBar(QWidget, Ui_MetroProgressCircleBar):

    def __init__(self, parent = None):
        super(MetroProgressCircleBar, self).__init__(parent)
        self.setupUi(self)
        self._isFirst = True
        self.animations = []
        self.childWidgets = {
            0:self.MetroProgressCircleBar1,
            1:self.MetroProgressCircleBar2,
            2:self.MetroProgressCircleBar3,
            3:self.MetroProgressCircleBar4,
            4:self.MetroProgressCircleBar5,
        }
        self.setStyleSheet(STYLE)

    def stop(self):
        for animation in self.animations:
            animation.stop()
        print("anll animation stop")

    def resizeEvent(self, event):
        '''控件大小改变事件'''
        result = super(MetroProgressCircleBar, self).resizeEvent(event)
        print(self.MetroProgressCircleBar.width())
        print("width: {width} height: {height}".format(width = self.width(), height = self.height()))
        self.initAnimation()
        return result

    def initAnimation(self):
        '''为每个圆形的widget创建动画'''
        if self._isFirst:    # 首次则根据ui的宽度初始化动画事件的里的宽带值
            self._isFirst = False
            print("first initAnimation")
            for index in range(5):
                animation = MpcbAnimation(self, self.childWidgets.get(index), index)
                self.animations.append(animation)
                animation.start()
        else:    # 修改宽度值
            print("changed initAnimation")
            for animation in self.animations:
                animation.updateAnimation()
