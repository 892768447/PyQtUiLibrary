#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年9月3日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 
'''
from PyQt5.QtCore import QRectF, QRect
from PyQt5.QtGui import QPalette, QPainter, QPen, QColor
from PyQt5.QtWidgets import QPushButton, QSizePolicy


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class PushButton(QPushButton):

    def __init__(self, parent = None, text = "", icon = None, styles = []):
        if icon:
            super(PushButton, self).__init__(icon, text, parent)
        else:
            super(PushButton, self).__init__(text, parent)
        for style in styles:
            self.setProperty(style, True)
        self.floatBased = True
        self.antialiased = True
        self.frameNo = 0
        self.setBackgroundRole(QPalette.Base)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def nextAnimationFrame(self):
        self.frameNo += 1
        self.update()

    def mouseReleaseEvent(self, event):
        '''鼠标点击释放事件'''
        print(event.pos())
        super(PushButton, self).mouseReleaseEvent(event)

    def paintEvent(self, event):
        super(PushButton, self).paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, self.antialiased)
        painter.translate(self.width() / 2, self.height() / 2)

        for diameter in range(0, 256, 9):
            delta = abs((self.frameNo % 128) - diameter / 2)
            alpha = 255 - (delta * delta) / 4 - diameter
            if alpha > 0:
                painter.setPen(QPen(QColor(0, diameter / 2, 127, alpha), 3))

                if self.floatBased:
                    painter.drawEllipse(QRectF(-diameter / 2.0,
                            - diameter / 2.0, diameter, diameter))
                else:
                    painter.drawEllipse(QRect(-diameter / 2,
                            - diameter / 2, diameter, diameter))
