#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年10月2日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 
'''

from uilib.widgets.images.BaseImageWidget import BaseImageWidget
from PyQt5.QtGui import QRegion    # @UnresolvedImport @UnusedImport

__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class CircleImageWidget(BaseImageWidget):

#     def __init__(self, parent = None, path = None):
#         super(CircleImageWidget, self).__init__(None)
#         self.setObjectName("CircleImageWidget")

    def enterEvent(self, event):
        # 顶部
        width, height = self._imageLabel.width(), self._imageLabel.height()
        diameter = min(width, height)
        radius = diameter / 2
        topLeft = topRight = bottomLeft = bottomRight = 0
        if self._alignment == self.ALIGN_TOP:
            self._textLabel.resize(diameter, diameter / 2)    # 调整为一半
            self._textLabel.move(self._imageLabel.x() + (width - diameter) / 2, self._imageLabel.y() + (height - diameter) / 2)    # 居中
            topLeft = topRight = int(radius)
        elif self._alignment == self.ALIGN_BOTTOM:
            self._textLabel.resize(diameter, diameter / 2)
            self._textLabel.move(self._imageLabel.x() + (width - diameter) / 2, self._imageLabel.y() + height / 2)    # 居下中
            bottomLeft = bottomRight = int(radius)
        else:
            self._textLabel.resize(diameter, diameter)    # 调整为和圆的直径一样大的正方形
            self._textLabel.move(self._imageLabel.x() + (width - diameter) / 2, self._imageLabel.y() + (height - diameter) / 2)    # 居中
            topLeft = topRight = bottomLeft = bottomRight = int(radius)
        if self._autoHideText:
            self.showText(True)
            self._textLabel.setStyleSheet(self.ALPHA_COLOR % {
                "red":self._red, "green":self._green,
                "blue":self._blue, "alpha":self._alpha
            } + self.BORDER_RADIUS_STYLE % {
                    "topLeft":topLeft, "topRight":topRight,
                    "bottomLeft":bottomLeft, "bottomRight":bottomRight
            })

    def resizeEvent(self, event):
        '''圆形图片'''
        super(CircleImageWidget, self).resizeEvent(event)
        width = self._imageLabel.width()
        height = self._imageLabel.height()
        side = min(width, height)
        circleRegion = QRegion(width / 2 - side / 2, height / 2 - side / 2, side, side, QRegion.Ellipse)
        self._imageLabel.setMask(circleRegion)
