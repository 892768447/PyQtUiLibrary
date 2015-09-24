#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年9月24日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 
'''
from PyQt5.QtCore import QSize, QRect, QPauseAnimation, QPropertyAnimation, \
    QPoint, QParallelAnimationGroup, QSequentialAnimationGroup
from PyQt5.QtWidgets import QWidget


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

class Ui_MetroProgressBar(object):

    def setupUi(self, MetroProgressBar):
        MetroProgressBar.setObjectName("MetroProgressBar")
        MetroProgressBar.resize(400, 8)
        MetroProgressBar.setMinimumSize(QSize(0, 8))
        MetroProgressBar.setMaximumSize(QSize(16777215, 8))
        self.MetroProgressBarCircle1 = QWidget(MetroProgressBar)
        self.MetroProgressBarCircle1.setGeometry(QRect(0, 0, 8, 8))
        self.MetroProgressBarCircle1.setObjectName("MetroProgressBarCircle1")
        self.MetroProgressBarCircle1.setProperty("circle", True)
        self.MetroProgressBarCircle2 = QWidget(MetroProgressBar)
        self.MetroProgressBarCircle2.setGeometry(QRect(0, 0, 8, 8))
        self.MetroProgressBarCircle2.setObjectName("MetroProgressBarCircle2")
        self.MetroProgressBarCircle2.setProperty("circle", True)
        self.MetroProgressBarCircle3 = QWidget(MetroProgressBar)
        self.MetroProgressBarCircle3.setGeometry(QRect(0, 0, 8, 8))
        self.MetroProgressBarCircle3.setObjectName("MetroProgressBarCircle3")
        self.MetroProgressBarCircle3.setProperty("circle", True)
        self.MetroProgressBarCircle4 = QWidget(MetroProgressBar)
        self.MetroProgressBarCircle4.setGeometry(QRect(0, 0, 8, 8))
        self.MetroProgressBarCircle4.setObjectName("MetroProgressBarCircle4")
        self.MetroProgressBarCircle4.setProperty("circle", True)
        self.MetroProgressBarCircle5 = QWidget(MetroProgressBar)
        self.MetroProgressBarCircle5.setGeometry(QRect(0, 0, 8, 8))
        self.MetroProgressBarCircle5.setObjectName("MetroProgressBarCircle5")
        self.MetroProgressBarCircle5.setProperty("circle", True)

class MetroProgressBar(QWidget, Ui_MetroProgressBar):

    def __init__(self, parent = None):
        super(MetroProgressBar, self).__init__(parent)
        self.setupUi(self)
        self._isFirst = True
        self.animations = []
        self.childWidgets = {
            0:self.MetroProgressBarCircle1,
            1:self.MetroProgressBarCircle2,
            2:self.MetroProgressBarCircle3,
            3:self.MetroProgressBarCircle4,
            4:self.MetroProgressBarCircle5,
        }
        self.setStyleSheet(STYLE)

    def stop(self):
        for animation in self.animations:
            animation[3].stop()
        print("anll animation stop")

    def resizeEvent(self, event):
        '''控件大小改变事件'''
        result = super(MetroProgressBar, self).resizeEvent(event)
        print("width: {width} height: {height}".format(width = self.width(), height = self.height()))
        self.initAnimation()
        return result

    def initAnimation(self):
        '''为每个圆形的widget创建动画'''
        if self._isFirst:    # 首次则根据ui的宽度初始化动画事件的里的宽带值
            self._isFirst = False
            print("first initAnimation")
            for index in range(5):
                self.createAnimation(index)
        else:    # 修改宽度值
            print("changed initAnimation")
            self.updateAnimation()

    def updateAnimation(self):
        '''更新动画'''
        for (MoveAnimation2, MoveAnimation3, MoveAnimation5, SequentialAnimation) in self.animations:
            SequentialAnimation.pause()    # 暂停
            MoveAnimation2.setEndValue(QPoint(self.width() / 4.0, 0))
            MoveAnimation3.setEndValue(QPoint((self.width() / 4.0) * 3.0, 0))
            MoveAnimation5.setEndValue(QPoint(self.width(), 0))
            SequentialAnimation.resume()    # 恢复

    def createAnimation(self, index):
        '''创建动画'''
        target = self.childWidgets.get(index)
        # 动画一(暂停)
        PauseAnimation1 = QPauseAnimation(target)
        PauseAnimation1.setDuration(150 * index)

        # 动画二(并行动画组)
        MoveAnimation1 = QPropertyAnimation(target, b"windowOpacity")
        MoveAnimation1.setDuration(400)
        MoveAnimation1.setStartValue(0)
        MoveAnimation1.setEndValue(1)

        MoveAnimation2 = QPropertyAnimation(target, b"pos")
        MoveAnimation2.setDuration(400)
        MoveAnimation2.setStartValue(QPoint(0, 0))
        MoveAnimation2.setEndValue(QPoint(self.width() / 4.0, 0))

        ParallelAnimation1 = QParallelAnimationGroup()
        ParallelAnimation1.addAnimation(MoveAnimation1)
        ParallelAnimation1.addAnimation(MoveAnimation2)

        # 动画三
        MoveAnimation3 = QPropertyAnimation(target, b"pos")
        MoveAnimation3.setDuration(2000)
        MoveAnimation3.setEndValue(QPoint((self.width() / 4.0) * 3.0, 0))

        # 动画四(并行动画组)
        MoveAnimation4 = QPropertyAnimation(target, b"windowOpacity")
        MoveAnimation4.setDuration(400)
        MoveAnimation4.setStartValue(1)
        MoveAnimation4.setEndValue(0)

        MoveAnimation5 = QPropertyAnimation(target, b"pos")
        MoveAnimation5.setDuration(400)
        MoveAnimation5.setEndValue(QPoint(self.width(), 0))

        ParallelAnimation2 = QParallelAnimationGroup()
        ParallelAnimation2.addAnimation(MoveAnimation4)
        ParallelAnimation2.addAnimation(MoveAnimation5)

        # 动画五(暂停)
        PauseAnimation2 = QPauseAnimation(target)
        PauseAnimation2.setDuration(150 * (5 - index - 1))

        # 串行动画组
        SequentialAnimation = QSequentialAnimationGroup()
        SequentialAnimation.setLoopCount(-1)    # 无限循环
        SequentialAnimation.addAnimation(PauseAnimation1)
        SequentialAnimation.addAnimation(ParallelAnimation1)
        SequentialAnimation.addAnimation(MoveAnimation3)
        SequentialAnimation.addAnimation(ParallelAnimation2)
        SequentialAnimation.addAnimation(PauseAnimation2)

        # 把需要修改的动画放到数组中
        self.animations.append((MoveAnimation2, MoveAnimation3, MoveAnimation5, SequentialAnimation))
        SequentialAnimation.start()
