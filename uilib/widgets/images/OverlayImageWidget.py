#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年10月2日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 
'''

from uilib.animations.images.OverlayImageAnimation import OverlayImageAnimation
from uilib.widgets.images.BaseImageWidget import BaseImageWidget


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class OverlayImageWidget(BaseImageWidget):

    def __init__(self, parent = None, path = None):
        super(OverlayImageWidget, self).__init__(parent, path)
        self._animation = OverlayImageAnimation(self._borderWidget, self)

    def enterEvent(self, event):
        '''鼠标进入事件'''
        # 显示白色边框
        self._borderWidget.setStyleSheet(self.ENTER_STYLE)
        self.showText(True)
        self._textLabel.setStyleSheet(self.ALPHA_COLOR % {
            "red":self._red, "green":self._green,
            "blue":self._blue, "alpha":self._alpha
        })
        self._borderWidget.setVisible(True)
        self._animation.start()

    def leaveEvent(self, event):
        '''鼠标离开事件'''
        # 隐藏白色边框
        self._borderWidget.setStyleSheet(self.LEAVE_STYLE)
        self.showText(False)
        self._borderWidget.setVisible(False)
        self._animation.stop()