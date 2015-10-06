#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年10月5日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 
'''
from PyQt5.QtWidgets import QLineEdit

from uilib.utils import QT5, SELF


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class LineEdit(QLineEdit):

    STYLE = """
        QLineEdit {{
            font-size: {font_size}px;
            border-radius: {border_radius}px;
            color: {text_color};
            min-width: {min_width}px;
            min-height: {min_height}px;
            border: {border_width}px {border_style} {border_color};
        }}
        QLineEdit:focus {{
            outline: 0;
            border-color: {focus_border_color};
        }}
        QLineEdit[echoMode="2"],QLineEdit[echoMode="3"] {{
            lineedit-password-character: {character};
        }}
        QLineEdit[enabled="false"] {{
            color: {enabled_text_color};
            border: {border_width}px {border_style} {enabled_text_color};
            background-color: {enabled_background_color};
            cursor: default;
            opacity: 0.7;
        }}
        QLineEdit[{style}="true"] {{
            color: {text_color};
            border: {border_width}px {border_style} {border_color};
        }}
        QLineEdit[{style}="true"]:focus {{
            outline: 0;
        }}
    """

    DEFAULT_STYLE = "DefaultStyle"
    ERROR_STYLE = "ErrorStyle"
    SUCCESS_STYLE = "SuccessStyle"

    def __init__(self, parent = None, text = "", style = "DefaultStyle"):
        super(LineEdit, self).__init__(text, parent)
        self._autoClearButtonEnabled = False

        # 以下是一些默认的样式值
        self.font_size = 15
        self.border_radius = 6
        self.text_color = "#34495e"
        self.min_width = 180
        self.min_height = 35
        self.border_width = 2
        self.border_style = "solid"
        self.border_color = "#bdc3c7"
        self.focus_border_color = "#1abc9c"
        self.character = 42
        self.enabled_text_color = "#d5dbdb"
        self.enabled_background_color = "#f4f6f6"

        try:
            method = getattr(self, "set" + style)
            method()    # 动态执行set样式的方法
            self.updateStyle(style)
        except:
            print("error style,use the default style")
            self.setDefaultStyle(True)
            self.updateStyle(self.DEFAULT_STYLE)

    def focusOutEvent(self, event):
        '''设置清空按钮隐藏'''
        if QT5() and self.getAutoClearButtonEnabled():
            self.setClearButtonEnabled(False)
        super(LineEdit, self).focusOutEvent(event)

    def focusInEvent(self, event):
        '''设置清空按钮显示'''
        if QT5() and self.getAutoClearButtonEnabled():
            self.setClearButtonEnabled(True)
        super(LineEdit, self).focusInEvent(event)

    @SELF
    def setAutoClearButtonEnabled(self, value):
        '''设置是否自动隐藏清空按钮(要求满足PyQt5)'''
        if QT5():
            self._autoClearButtonEnabled = value
        else:
            self._autoClearButtonEnabled = False

    def updateStyle(self, style):
        '''更新样式'''
        self.setStyleSheet(self.STYLE.format(
            style = style, font_size = self.font_size,
            border_radius = self.border_radius, text_color = self.text_color,
            min_width = self.min_width, min_height = self.min_height,
            border_width = self.border_width, border_style = self.border_style,
            border_color = self.border_color, focus_border_color = self.focus_border_color,
            character = self.character, enabled_text_color = self.enabled_text_color,
            enabled_background_color = self.enabled_background_color
        ))

    @SELF
    def setDefaultStyle(self, value = True):
        self.setProperty(self.DEFAULT_STYLE, value)
        self.setTextColor("#34495e")
        self.setBorderColor("#bdc3c7")
        self.setFocusBorderColor("#1abc9c")

    @SELF
    def setErrorStyle(self, value = True):
        self.setProperty(self.ERROR_STYLE, value)
        self.setTextColor("#e74c3c")
        self.setBorderColor("#e74c3c")

    @SELF
    def setSuccessStyle(self, value = True):
        self.setProperty(self.SUCCESS_STYLE, value)
        self.setTextColor("#2ecc71")
        self.setBorderColor("#2ecc71")

    @SELF
    def setFontSize(self, value):
        self.font_size = value

    @SELF
    def setBorderRadius(self, value):
        self.border_radius = value

    @SELF
    def setTextColor(self, value):
        self.text_color = value

    @SELF
    def setMinWidth(self, value):
        self.min_width = value

    @SELF
    def setMinHeight(self, value):
        self.min_height = value

    @SELF
    def setBorderWidth(self, value):
        self.border_width = value

    @SELF
    def setBorderStyle(self, value):
        self.border_style = value

    @SELF
    def setBorderColor(self, value):
        self.border_color = value

    @SELF
    def setFocusBorderColor(self, value):
        self.focus_border_color = value

    @SELF
    def setCharacter(self, value):
        self.character = value

    @SELF
    def setEnabledTextColor(self, value):
        self.enabled_text_color = value

    @SELF
    def setEnabledBackgroundColor(self, value):
        self.enabled_background_color = value

    def getDefaultStyle(self):
        return self.property(self.DEFAULT_STYLE)

    def getErrorStyle(self):
        return self.property(self.ERROR_STYLE)

    def getSuccessStyle(self):
        return self.property(self.SUCCESS_STYLE)

    def getAutoClearButtonEnabled(self):
        return self._autoClearButtonEnabled

    def getFontSize(self):
        return self.font_size

    def getBorderRadius(self):
        return self.border_radius

    def getTextColor(self):
        return self.text_color

    def getMinWidth(self):
        return self.min_width

    def getMinHeight(self):
        return self.min_height

    def getBorderWidth(self):
        return self.border_width

    def getBorderStyle(self):
        return self.border_style

    def getBorderColor(self):
        return self.border_color

    def getFocusBorderColor(self):
        return self.focus_border_color

    def getCharacter(self):
        return self.character

    def getEnabledTextColor(self):
        return self.enabled_text_color

    def getEnabledBackgroundColor(self):
        return self.enabled_background_color
