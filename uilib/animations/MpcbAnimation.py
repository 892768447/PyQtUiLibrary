#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年10月6日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: MpcbAnimation
'''
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QPointF, QRectF, \
    QSequentialAnimationGroup, QPauseAnimation
from PyQt5.QtGui import QPainterPath


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class _MpcbAnimation(QPropertyAnimation):

    def __init__(self, parent, target, index, easing = QEasingCurve.InQuad):
        super(_MpcbAnimation, self).__init__(target, b"pos")
        self.parent = parent
        self.m_pathType = 1
        self.easing = easing
        self.createAnimation(target, index)

    def createAnimation(self, target, index):
        '''创建动画'''
        self.m_path = QPainterPath()
        if self.easing != -1:
            self.setEasingCurve(self.easing)
        self.setStartValue(QPointF(0, 0))
        self.setEndValue(QPointF(90, 90))
        self.setDuration(2000)
        self.setLoopCount(-1)

    def updateCurrentTime(self, currentTime):
        if self.m_pathType:
            if self.m_path.isEmpty():
                end = self.endValue()
                start = self.startValue()
                self.m_path.moveTo(start)
                self.m_path.addEllipse(QRectF(start, end))

            dura = self.duration()
            if dura == 0:
                progress = 1.0
            else:
                progress = (((currentTime - 1) % dura) + 1) / float(dura)

            easedProgress = self.easingCurve().valueForProgress(progress)
            if easedProgress > 1.0:
                easedProgress -= 1.0
            elif easedProgress < 0:
                easedProgress += 1.0

            pt = self.m_path.pointAtPercent(easedProgress)
            self.updateCurrentValue(pt)
            self.valueChanged.emit(pt)
        else:
            super(_MpcbAnimation, self).updateCurrentTime(currentTime)

class MpcbAnimation(QSequentialAnimationGroup):
    '''MetroProgressCircleBar动画'''

    def __init__(self, parent, target, index, easing = QEasingCurve.InQuad):
        super(MpcbAnimation, self).__init__()
        self.easing = easing
        self.createAnimation(parent, target, index)

    def createAnimation(self, parent, target, index):

        # 动画一(暂停)
        PauseAnimation1 = QPauseAnimation(target)
        PauseAnimation1.setDuration(150 * index)

        # 圆周动画
        manimation = _MpcbAnimation(parent, target, index, self.easing)

        self.addAnimation(PauseAnimation1)
        self.addAnimation(manimation)
