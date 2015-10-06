#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年10月4日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 
'''

from uilib.utils import SELF, PY3


if PY3():
    from PyQt5.QtGui import QIcon    # @UnresolvedImport @UnusedImport
    from PyQt5.QtWidgets import QPushButton    # @UnresolvedImport @UnusedImport
else:
    from PyQt4.QtGui import QPushButton, QIcon    # @UnresolvedImport @Reimport


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class PushButton(QPushButton):

    STYLE = """
        QPushButton {
            font-size: %(font_size)spx;
            border-radius: %(border_radius)spx;
            color: %(text_color)s;
            min-width: %(min_width)s;
            min-height: %(min_height)s;
        }
        QPushButton[%(style)s="true"] {
            background-color: %(background_color)s;
        }
        QPushButton[%(style)s="true"]:hover {
            border-color: %(hover_border_color)s;
            background-color: %(hover_background_color)s;
        }
        QPushButton[%(style)s="true"]:pressed {
            border-color: %(pressed_border_color)s;
            background-color: %(pressed_background_color)s;
        }
        QPushButton[enabled="false"] {
            border-color: #1abc9c;
            background-color: #bdc3c7;
        }
    """

    DEFAULT_STYLE = "DefaultStyle"
    PRIMARY_STYLE = "PrimaryStyle"
    WARNING_STYLE = "WarningStyle"
    DANGER_STYLE = "DangerStyle"
    SUCCESS_STYLE = "SuccessStyle"
    INVERSE_STYLE = "InverseStyle"
    INFO_STYLE = "InfoStyle"

    def __init__(self, parent = None, text = "", icon = "", style = "DefaultStyle"):
        if icon:
            super(PushButton, self).__init__(QIcon(icon), text, parent)
        else:
            super(PushButton, self).__init__(text, parent)

        # 以下是一些默认的样式值
        self.font_size = 17
        self.border_radius = 6
        self.text_color = "#fff"
        self.min_width = 150
        self.min_height = 45
        self.background_color = "#bdc3c7"
        self.hover_border_color = "#cacfd2"    # hover border-color
        self.hover_background_color = "#cacfd2"    # hover
        self.pressed_border_color = "#a1a6a9"    # pressed
        self.pressed_background_color = "#a1a6a9"    # pressed

        try:
            method = getattr(self, "set" + style)
            method()    # 动态执行set样式的方法
            self.updateStyle(style)
        except:
            print("error style,use the default style")
            self.setDefaultStyle(True)
            self.updateStyle(self.DEFAULT_STYLE)

    def updateStyle(self, style):
        '''更新样式'''
        self.setStyleSheet(self.STYLE % {"style":style,
            "font_size":self.font_size, "border_radius":self.border_radius,
            "text_color":self.text_color, "min_width":self.min_width,
            "min_height":self.min_height, "background_color":self.background_color,
            "hover_border_color":self.hover_border_color, "hover_background_color":self.hover_background_color,
            "pressed_border_color":self.pressed_border_color, "pressed_background_color":self.pressed_background_color
        })

    @SELF
    def setDefaultStyle(self, value = True):
        self.setProperty(self.DEFAULT_STYLE, value)
        self.setBackgroundColor("#bdc3c7")
        self.setHoverBorderColor("#cacfd2")
        self.setHoverBackgroundColor("#cacfd2")
        self.setPressedBorderColor("#a1a6a9")
        self.setPressedBackgroundColor("#a1a6a9")

    @SELF
    def setPrimaryStyle(self, value = True):
        self.setProperty(self.PRIMARY_STYLE, value)
        self.setBackgroundColor("#1abc9c")
        self.setHoverBorderColor("#48c9b0")
        self.setHoverBackgroundColor("#48c9b0")
        self.setPressedBorderColor("#16a085")
        self.setPressedBackgroundColor("#16a085")

    @SELF
    def setWarningStyle(self, value = True):
        self.setProperty(self.WARNING_STYLE, value)
        self.setBackgroundColor("#f1c40f")
        self.setHoverBorderColor("#f4d313")
        self.setHoverBackgroundColor("#f4d313")
        self.setPressedBorderColor("#cda70d")
        self.setPressedBackgroundColor("#cda70d")

    @SELF
    def setDangerStyle(self, value = True):
        self.setProperty(self.DANGER_STYLE, value)
        self.setBackgroundColor("#e74c3c")
        self.setHoverBorderColor("#ec7063")
        self.setHoverBackgroundColor("#ec7063")
        self.setPressedBorderColor("#c44133")
        self.setPressedBackgroundColor("#c44133")

    @SELF
    def setSuccessStyle(self, value = True):
        self.setProperty(self.SUCCESS_STYLE, value)
        self.setBackgroundColor("#2ecc71")
        self.setHoverBorderColor("#58d68d")
        self.setHoverBackgroundColor("#58d68d")
        self.setPressedBorderColor("#27ad60")
        self.setPressedBackgroundColor("#27ad60")

    @SELF
    def setInverseStyle(self, value = True):
        self.setProperty(self.INVERSE_STYLE, value)
        self.setBackgroundColor("#34495e")
        self.setHoverBorderColor("#415b76")
        self.setHoverBackgroundColor("#415b76")
        self.setPressedBorderColor("#2c3e50")
        self.setPressedBackgroundColor("#2c3e50")

    @SELF
    def setInfoStyle(self, value = True):
        self.setProperty(self.INFO_STYLE, value)
        self.setBackgroundColor("#3498db")
        self.setHoverBorderColor("#5dade2")
        self.setHoverBackgroundColor("#5dade2")
        self.setPressedBorderColor("#2c81ba")
        self.setPressedBackgroundColor("#2c81ba")

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

    def getBackgroundColor(self):
        return self.background_color

    def getHoverBorderColor(self):
        return self.hover_border_color

    def getHoverBackgroundColor(self):
        return self.hover_background_color

    def getPressedBorderColor(self):
        return self.pressed_border_color

    def getPressedBackgroundColor(self):
        return self.pressed_background_color

    def getDefaultStyle(self):
        return self.property(self.DEFAULT_STYLE)

    def getPrimaryStyle(self):
        return self.property(self.PRIMARY_STYLE)

    def getWarningStyle(self):
        return self.property(self.WARNING_STYLE)

    def getDangerStyle(self):
        return self.property(self.DANGER_STYLE)

    def getSuccessStyle(self):
        return self.property(self.SUCCESS_STYLE)

    def getInverseStyle(self):
        return self.property(self.INVERSE_STYLE)

    def getInfoStyle(self):
        return self.property(self.INFO_STYLE)

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
    def setBackgroundColor(self, value):
        self.background_color = value

    @SELF
    def setHoverBorderColor(self, value):
        self.hover_border_color = value

    @SELF
    def setHoverBackgroundColor(self, value):
        self.hover_background_color = value

    @SELF
    def setPressedBorderColor(self, value):
        self.pressed_border_color = value

    @SELF
    def setPressedBackgroundColor(self, value):
        self.pressed_background_color = value
