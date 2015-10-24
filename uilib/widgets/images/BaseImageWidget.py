#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年10月2日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 
'''

from __future__ import unicode_literals
from uilib.Utils import SELF, PY3

if PY3():
    from PyQt5.QtCore import Qt    # @UnresolvedImport @UnusedImport
    from PyQt5.QtGui import QPalette, QImage, QPixmap, QColor    # @UnresolvedImport @UnusedImport
    from PyQt5.QtWidgets import QWidget, QLabel, QSizePolicy    # @UnresolvedImport @UnusedImport
else:
    from PyQt4.QtGui import QPalette, QImage, QPixmap, QColor, QWidget, QLabel, QSizePolicy    # @Reimport @UnresolvedImport
    from PyQt4.QtCore import Qt    # @Reimport @UnresolvedImport


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class BaseImageWidget(QWidget):

    ALIGN_TOP = Qt.AlignHCenter | Qt.AlignTop
    ALIGN_CENTER = Qt.AlignCenter
    ALIGN_BOTTOM = Qt.AlignHCenter | Qt.AlignBottom

    ALPHA_COLOR = """
        background-color: rgba(%(red)s,%(green)s,%(blue)s,%(alpha)s);
    """

    BORDER_RADIUS_STYLE = """
        border-top-left-radius: %(topLeft)spx;
        border-top-right-radius: %(topRight)spx;
        border-bottom-left-radius: %(bottomLeft)spx;
        border-bottom-right-radius: %(bottomRight)spx;
    """

    ENTER_STYLE = """
        border: 1px solid white;
    """

    LEAVE_STYLE = """
        border: none;
    """

    LABEL_TEXT = """
    <html>
        <head/>
        <body>
            <p><span style="font-size:%(titleSize)spt; color:%(titleColor)s; font-weight:600;">%(title)s</span></p>
            <p><span style="font-size:%(textSize)spt; color:%(textColor)s;">%(text)s</span></p>
        </body>
    </html>
    """

    def __init__(self, parent = None, path = None):
        super(BaseImageWidget, self).__init__(parent)
        self.setObjectName("BaseImageWidget")

        # 图片label
        self._imageLabel = QLabel(self)
        self._imageLabel.setBackgroundRole(QPalette.Base)
        self._imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self._imageLabel.setScaledContents(True)    # 图片拉伸
        self._imageLabel.setObjectName("_ImageLabel")

        # 文字label
        self._textLabel = QLabel(self)
        self._textLabel.setAlignment(Qt.AlignCenter)    # 字体居中
        self._textLabel.setObjectName("_TextLabel")

        # 边框widget
        self._borderWidget = QWidget(self)
        self._borderWidget.setObjectName("_BorderWidget")

        self._alignment = self.ALIGN_CENTER
        self._red = self._green = self._blue = 255
        self._alpha = 100
        self._autoHideText = False
        self._title = self._text = ""
        self._titleSize = 14
        self._textSize = 10
        self._titleColor = self._textColor = "black"
        self.setImage(path)

    def resizeEvent(self, event):
        '''大小改变事件'''
        super(BaseImageWidget, self).resizeEvent(event)
        self._imageLabel.resize(self.size())
        self._textLabel.resize(self.size())
        self._borderWidget.resize(self.size())
        # 调整Widget的大小和外部一样

    def enterEvent(self, event):
        super(BaseImageWidget, self).enterEvent(event)
        # 顶部
        width = self._imageLabel.width()
        height = self._imageLabel.height()
        if self._alignment == self.ALIGN_TOP:
            self._textLabel.resize(width, height / 4)
            self._textLabel.move(self._imageLabel.x(), self._imageLabel.y())
        elif self._alignment == self.ALIGN_BOTTOM:
            self._textLabel.resize(width, height / 4)
            self._textLabel.move(self._imageLabel.x(), height - height / 4)
        else:
            self._textLabel.resize(width, height)
            self._textLabel.move(self._imageLabel.x(), self._imageLabel.y())
        if self._autoHideText:
            self.showText(True)
            self._textLabel.setStyleSheet(self.ALPHA_COLOR % {
                "red":self._red, "green":self._green,
                "blue":self._blue, "alpha":self._alpha
            })

    def leaveEvent(self, event):
        super(BaseImageWidget, self).leaveEvent(event)
        if self._autoHideText:
            self.showText(False)

    def _initImage(self):
        self._image = QImage(self._path)
        if not self._image.isNull():
            self._imageLabel.setPixmap(QPixmap.fromImage(self._image))
        else:
            print("image path is wrong")

    @SELF
    def setAlignment(self, alignment):
        '''设置文字居上,居中,居下'''
        self._alignment = alignment
        self._textLabel.setAlignment(alignment)

    @SELF
    def setImage(self, path = None):
        '''设置图片'''
        self._path = path
        self._initImage()

    @SELF
    def setContent(self, title = "", text = "", titleSize = 14,
        textSize = 10, titleColor = "black", textColor = "black", visible = True):
        '''设置图片上面显示的文字'''
        self._title = title
        self._text = text
        self._titleSize = titleSize
        self._textSize = textSize
        self._titleColor = titleColor
        self._textColor = textColor
        self._setText()
        self.showText(visible)

    @SELF
    def setAlphaColorInt(self, red = 255, green = 255, blue = 255, alpha = 100):
        '''通过rgb值设置半透明颜色'''
        self.setRed(red).setGreen(green).setBlue(blue).setAlpha(alpha)

    @SELF
    def setAlphaColorStr(self, color = "#ffffff", alpha = 100):
        '''通过字符串值设置半透明颜色'''
        alphaColor = QColor(color)
        alphaColor.setAlpha(alpha)
        red, green, blue, alpha = alphaColor.getRgb()
        self.setRed(red).setGreen(green).setBlue(blue).setAlpha(alpha)
        del alphaColor

    def showText(self, visible):
        '''显示图片上面的文字'''
        self._textLabel.setVisible(visible)

    def _setText(self):
        self._textLabel.setText(self.LABEL_TEXT % {
            "title":self._title, "text":self._text,
            "titleSize":self._titleSize, "textSize":self._textSize,
            "titleColor":self._titleColor, "textColor":self._textColor
        })

    def getAutoHideText(self):
        return self._autoHideText

    def getPath(self):
        return self._path

    def getTitle(self):
        return self._title

    def getText(self):
        return self._text

    def getTitleSize(self):
        return self._titleSize

    def getTextSize(self):
        return self._textSize

    def getTitleColor(self):
        return self._titleColor

    def getTextColor(self):
        return self._textColor

    @SELF
    def setAutoHideText(self, value):
        '''是否根据鼠标悬停显示或隐藏文字'''
        self._autoHideText = value
        self.showText(not value)

    @SELF
    def setPath(self, path):
        self.setImage(path)

    @SELF
    def setTitle(self, value):
        self._title = value
        self._setText()

    @SELF
    def setText(self, value):
        self._text = value
        self._setText()

    @SELF
    def setTitleSize(self, value):
        self._titleSize = value
        self._setText()

    @SELF
    def setTextSize(self, value):
        self._textSize = value
        self._setText()

    @SELF
    def setTitleColor(self, value):
        self._titleColor = value
        self._setText()

    @SELF
    def setTextColor(self, value):
        self._textColor = value
        self._setText()

    def getRed(self):
        return self._red

    def getGreen(self):
        return self._green

    def getBlue(self):
        return self._blue

    def getAlpha(self):
        return self._alpha

    @SELF
    def setRed(self, value):
        self._red = value

    @SELF
    def setGreen(self, value):
        self._green = value

    @SELF
    def setBlue(self, value):
        self._blue = value

    @SELF
    def setAlpha(self, value):
        self._alpha = value
