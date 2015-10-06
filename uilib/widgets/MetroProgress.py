#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年10月6日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 
'''
from PyQt5.QtCore import QSize, QRect, Qt, QEasingCurve
from PyQt5.QtWidgets import QWidget, QGridLayout, QSpacerItem, QSizePolicy

from uilib.animations.MpbAnimation import MpbAnimation
from uilib.animations.MpcbAnimation import MpcbAnimation


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class Ui_MetroProgressBar(object):

    def setupUi(self, MetroProgressBar):
        MetroProgressBar.setObjectName("MetroProgressBar")
        MetroProgressBar.resize(400, 8)
        MetroProgressBar.setMinimumSize(QSize(0, 8))
        MetroProgressBar.setMaximumSize(QSize(16777215, 8))
        self.MetroProgressBarCircle1 = QWidget(MetroProgressBar)
        self.MetroProgressBarCircle1.setGeometry(QRect(0, 0, 8, 8))
        self.MetroProgressBarCircle1.setObjectName("MetroProgressBarCircle1")
        self.MetroProgressBarCircle2 = QWidget(MetroProgressBar)
        self.MetroProgressBarCircle2.setGeometry(QRect(0, 0, 8, 8))
        self.MetroProgressBarCircle2.setObjectName("MetroProgressBarCircle2")
        self.MetroProgressBarCircle3 = QWidget(MetroProgressBar)
        self.MetroProgressBarCircle3.setGeometry(QRect(0, 0, 8, 8))
        self.MetroProgressBarCircle3.setObjectName("MetroProgressBarCircle3")
        self.MetroProgressBarCircle4 = QWidget(MetroProgressBar)
        self.MetroProgressBarCircle4.setGeometry(QRect(0, 0, 8, 8))
        self.MetroProgressBarCircle4.setObjectName("MetroProgressBarCircle4")
        self.MetroProgressBarCircle5 = QWidget(MetroProgressBar)
        self.MetroProgressBarCircle5.setGeometry(QRect(0, 0, 8, 8))
        self.MetroProgressBarCircle5.setObjectName("MetroProgressBarCircle5")

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
        self.MetroProgressBarCircle1 = QWidget(self.MetroProgressCircleBar)
        self.MetroProgressBarCircle1.setGeometry(QRect(92, 46, 8, 8))
        self.MetroProgressBarCircle1.setObjectName("MetroProgressBarCircle1")
        self.MetroProgressBarCircle2 = QWidget(self.MetroProgressCircleBar)
        self.MetroProgressBarCircle2.setGeometry(QRect(92, 46, 8, 8))
        self.MetroProgressBarCircle2.setObjectName("MetroProgressBarCircle2")
        self.MetroProgressBarCircle3 = QWidget(self.MetroProgressCircleBar)
        self.MetroProgressBarCircle3.setGeometry(QRect(92, 46, 8, 8))
        self.MetroProgressBarCircle3.setObjectName("MetroProgressBarCircle3")
        self.MetroProgressBarCircle4 = QWidget(self.MetroProgressCircleBar)
        self.MetroProgressBarCircle4.setGeometry(QRect(92, 46, 8, 8))
        self.MetroProgressBarCircle4.setObjectName("MetroProgressBarCircle4")
        self.MetroProgressBarCircle5 = QWidget(self.MetroProgressCircleBar)
        self.MetroProgressBarCircle5.setGeometry(QRect(92, 46, 8, 8))
        self.MetroProgressBarCircle5.setObjectName("MetroProgressBarCircle5")
        self.gridLayout.addWidget(self.MetroProgressCircleBar, 1, 1, 1, 1)
        spacerItem3 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)

class _MetroProgress(QWidget):

    STYLE = """
        QWidget[CircleBar="true"] {
            background-color: white;
            max-width: 8px;
            max-height: 8px;
            border-radius: 4px;
        }
    """

    def __init__(self, parent = None, easing = QEasingCurve.InQuad):
        super(_MetroProgress, self).__init__(parent)
        self.setupUi(self)
        self.easing = easing
        self.animations = []
        self.childWidgets = {
            0:self.MetroProgressBarCircle1,
            1:self.MetroProgressBarCircle2,
            2:self.MetroProgressBarCircle3,
            3:self.MetroProgressBarCircle4,
            4:self.MetroProgressBarCircle5,
        }
        for childs in self.childWidgets:
            child = self.childWidgets.get(childs)
            child.setProperty("CircleBar", True)
            child.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet(self.STYLE)
        self.createAnimation()

    def stop(self):
        for animation in self.animations:
            animation.stop()
        print("anll animation stop")

    def createAnimation(self):
        '''为每个圆形的widget创建动画'''
        pass

class MetroProgressBar(_MetroProgress, Ui_MetroProgressBar):

    def createAnimation(self):
        for index in range(5):
            animation = MpbAnimation(self, self.childWidgets.get(index), index, self.easing)
            self.animations.append(animation)
            animation.start()

class MetroProgressCircleBar(_MetroProgress, Ui_MetroProgressCircleBar):

    def createAnimation(self):
        for index in range(5):
            animation = MpcbAnimation(self, self.childWidgets.get(index), index, self.easing)
            self.animations.append(animation)
            animation.start()
