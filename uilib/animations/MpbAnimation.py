#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年9月25日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: MetroProgressBar Animation
'''
from PyQt5.QtCore import QSequentialAnimationGroup, QPauseAnimation, \
    QPropertyAnimation, QPoint, QParallelAnimationGroup


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class MpbAnimation(QSequentialAnimationGroup):
    '''MetroProgressBar动画'''

    def __init__(self, parent, target, index):
        super(MpbAnimation, self).__init__()
        self.parent = parent
        self.createAnimation(target, index)

    def updateAnimation(self):
        '''更新动画'''
        self.pause()    # 暂停
        self.MoveAnimation2.setEndValue(QPoint(self.parent.width() / 4.0, 0))
        self.MoveAnimation3.setEndValue(QPoint((self.parent.width() / 4.0) * 3.0, 0))
        self.MoveAnimation5.setEndValue(QPoint(self.parent.width(), 0))
        self.resume()    # 恢复

    def createAnimation(self, target, index):
        '''创建动画'''
        # 动画一(暂停)
        PauseAnimation1 = QPauseAnimation(target)
        PauseAnimation1.setDuration(150 * index)

        # 动画二(并行动画组)
        MoveAnimation1 = QPropertyAnimation(target, b"windowOpacity")
        MoveAnimation1.setDuration(400)
        MoveAnimation1.setStartValue(0)
        MoveAnimation1.setEndValue(1)

        self.MoveAnimation2 = QPropertyAnimation(target, b"pos")
        self.MoveAnimation2.setDuration(400)
        self.MoveAnimation2.setStartValue(QPoint(0, 0))
        self.MoveAnimation2.setEndValue(QPoint(self.parent.width() / 4.0, 0))

        ParallelAnimation1 = QParallelAnimationGroup()
        ParallelAnimation1.addAnimation(MoveAnimation1)
        ParallelAnimation1.addAnimation(self.MoveAnimation2)

        # 动画三
        self.MoveAnimation3 = QPropertyAnimation(target, b"pos")
        self.MoveAnimation3.setDuration(2000)
        self.MoveAnimation3.setEndValue(QPoint((self.parent.width() / 4.0) * 3.0, 0))

        # 动画四(并行动画组)
        MoveAnimation4 = QPropertyAnimation(target, b"windowOpacity")
        MoveAnimation4.setDuration(400)
        MoveAnimation4.setStartValue(1)
        MoveAnimation4.setEndValue(0)

        self.MoveAnimation5 = QPropertyAnimation(target, b"pos")
        self.MoveAnimation5.setDuration(400)
        self.MoveAnimation5.setEndValue(QPoint(self.parent.width(), 0))

        ParallelAnimation2 = QParallelAnimationGroup()
        ParallelAnimation2.addAnimation(MoveAnimation4)
        ParallelAnimation2.addAnimation(self.MoveAnimation5)

        # 动画五(暂停)
        PauseAnimation2 = QPauseAnimation(target)
        PauseAnimation2.setDuration(150 * (5 - index - 1))

        # 串行动画组
        self.setLoopCount(-1)    # 无限循环
        self.addAnimation(PauseAnimation1)
        self.addAnimation(ParallelAnimation1)
        self.addAnimation(self.MoveAnimation3)
        self.addAnimation(ParallelAnimation2)
        self.addAnimation(PauseAnimation2)
