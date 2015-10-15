#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年10月6日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: MpbAnimation
'''
from PyQt5.QtCore import QSequentialAnimationGroup, QEasingCurve, \
    QPropertyAnimation, QPauseAnimation, QPoint, QParallelAnimationGroup, QRectF
from PyQt5.QtGui import QPainterPath


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class _MoveAnimation(QPropertyAnimation):
    '''move animation'''

    MOVE1 = 1
    MOVE2 = 2
    MOVE3 = 3

    def __init__(self, target, parent, easing = QEasingCurve.Custom):
        super(_MoveAnimation, self).__init__(target, b"pos")
        self.parent = parent
        self.easing = easing
        if easing != -1:
            self.setEasingCurve(easing)
        self.m_path = QPainterPath()

    def setMoveType(self, _type):
        self._type = _type

    def updateCurrentTime(self, currentTime):
        if self.m_path.isEmpty():
            # end = self.endValue()
            start = self.startValue()
            if self._type == self.MOVE1:
                end = QPoint(self.parent.width() / 4.0, 0)
            elif self._type == self.MOVE2:
                end = QPoint((self.parent.width() / 4.0) * 3.0, 0)
                if not start:
                    start = QPoint(self.parent.width() / 4.0, 0)
                    # 第二个移动没有设置开始坐标,这里以第一个移动结束为开始
            elif self._type == self.MOVE3:
                if not start:
                    start = QPoint((self.parent.width() / 4.0) * 3.0, 0)
                    # 第三个移动没有设置开始坐标,这里以第二个移动结束为开始
                end = QPoint(self.parent.width(), 0)
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
        super(_MoveAnimation, self).updateCurrentTime(currentTime)

class MpbAnimation(QSequentialAnimationGroup):
    '''MpbAnimation动画'''

    def __init__(self, parent, target, index, easing = QEasingCurve.Custom):
        super(MpbAnimation, self).__init__()
        self.parent = parent
        self.easing = easing
        self.createAnimation(target, index)

    def createAnimation(self, target, index):
        '''创建动画'''
        # 暂停动画一
        PauseAnimation1 = QPauseAnimation(target)
        PauseAnimation1.setDuration(150 * index)

        # 并行动画组一
        # #透明度动画一
        OpacityAnimation1 = QPropertyAnimation(target, b"opacity")
        OpacityAnimation1.setDuration(400)
        OpacityAnimation1.setStartValue(0)
        OpacityAnimation1.setEndValue(1)
        # #移动动画一
        MoveAnimation1 = _MoveAnimation(target, self.parent, self.easing)
        MoveAnimation1.setMoveType(_MoveAnimation.MOVE1)
        MoveAnimation1.setDuration(400)
        MoveAnimation1.setStartValue(QPoint(0, 0))
        MoveAnimation1.setEndValue(QPoint(self.parent.width() / 4.0, 0))
        # 添加到并行动画里面
        ParallelAnimation1 = QParallelAnimationGroup()
        ParallelAnimation1.addAnimation(OpacityAnimation1)
        ParallelAnimation1.addAnimation(MoveAnimation1)

        # 移动动画二
        MoveAnimation2 = _MoveAnimation(target, self.parent, self.easing)
        MoveAnimation2.setMoveType(_MoveAnimation.MOVE2)
        MoveAnimation2.setDuration(2000)
        MoveAnimation2.setEndValue(QPoint((self.parent.width() / 4.0) * 3.0, 0))

        # 并行动画组二
        # #透明度动画二
        OpacityAnimation2 = QPropertyAnimation(target, b"opacity")
        OpacityAnimation2.setDuration(400)
        OpacityAnimation2.setStartValue(1)
        OpacityAnimation2.setEndValue(0)
        # #移动动画三
        MoveAnimation3 = _MoveAnimation(target, self.parent, self.easing)
        MoveAnimation3.setMoveType(_MoveAnimation.MOVE3)
        MoveAnimation3.setDuration(400)
        MoveAnimation3.setEndValue(QPoint(self.parent.width(), 0))
        # 添加到并行动画里面
        ParallelAnimation2 = QParallelAnimationGroup()
        ParallelAnimation2.addAnimation(OpacityAnimation2)
        ParallelAnimation2.addAnimation(MoveAnimation3)

        # 暂停动画二
        PauseAnimation2 = QPauseAnimation(target)
        PauseAnimation2.setDuration(150 * (5 - index - 1))

        # 串行动画组
        self.setLoopCount(-1)    # 无限循环
        self.addAnimation(PauseAnimation1)
        self.addAnimation(ParallelAnimation1)
        self.addAnimation(MoveAnimation2)
        self.addAnimation(ParallelAnimation2)
        self.addAnimation(PauseAnimation2)
