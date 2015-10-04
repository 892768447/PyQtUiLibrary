#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年10月2日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 
'''

from uilib.widgets.images.BaseImageWidget import BaseImageWidget
from PyQt5.QtGui import QRegion


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class RoundImageWidget(BaseImageWidget):

    def enterEvent(self, event):
        # 顶部
        width = self._imageLabel.width()
        height = self._imageLabel.height()
        radius = min(width, height) / 10 / 2
        topLeft = topRight = bottomLeft = bottomRight = 0
        if self._alignment == self.ALIGN_TOP:
            self._textLabel.resize(width, height / 4)
            self._textLabel.move(self._imageLabel.x(), self._imageLabel.y())
            topLeft = topRight = radius
        elif self._alignment == self.ALIGN_BOTTOM:
            self._textLabel.resize(width, height / 4)
            self._textLabel.move(self._imageLabel.x(), height - height / 4)
            bottomLeft = bottomRight = radius
        else:
            self._textLabel.resize(width, height)
            self._textLabel.move(self._imageLabel.x(), self._imageLabel.y())
            topLeft = topRight = bottomLeft = bottomRight = radius
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
        super(RoundImageWidget, self).resizeEvent(event)

        width = self._imageLabel.width()
        height = self._imageLabel.height()
        radius = min(width, height) / 10 / 2
        verticalRegion = QRegion(0, radius, width, height - 2 * radius)
        horizontalRegion = QRegion(radius, 0, width - 2 * radius, height)
        circle = QRegion(0, 0, 2 * radius, 2 * radius, QRegion.Ellipse)
        region = verticalRegion.united(horizontalRegion)
        region = region.united(circle)
        region = region.united(circle.translated(width - 2 * radius, 0))
        region = region.united(circle.translated(width - 2 * radius, height - 2 * radius))
        region = region.united(circle.translated(0, height - 2 * radius))
        self._imageLabel.setMask(region)
