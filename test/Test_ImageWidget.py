#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年10月2日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 
'''
from __future__ import unicode_literals
# 解决2.x到3.x的字符串问题
from os.path import dirname, abspath
import sys

# 父级目录
sys.path.insert(0, dirname(dirname(abspath(sys.argv[0]))))
sys.path.insert(0, dirname(dirname(abspath(__file__))))

from uilib.utils import QT5
from uilib.widgets.images.BaseImageWidget import BaseImageWidget
from uilib.widgets.images.CircleImageWidget import CircleImageWidget
from uilib.widgets.images.OverlayImageWidget import OverlayImageWidget
from uilib.widgets.images.RoundImageWidget import RoundImageWidget

if QT5():
    from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QApplication    # @UnresolvedImport @UnusedImport
else:
    from PyQt4.QtGui import QWidget, QVBoxLayout, QHBoxLayout, QApplication    # @Reimport @UnresolvedImport

__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class TestImageWidget(QWidget):

    def __init__(self):
        super(TestImageWidget, self).__init__()
        self.resize(600, 600)

        # Normal Style
        imageWidget1 = BaseImageWidget(self, "../images/3.jpg")
        imageWidget1.setContent("图片1标题", "图片1的详细内容", titleColor = "red", textColor = "white")
        imageWidget1.setAlphaColorStr("#000000", 100)
        imageWidget1.setAutoHideText(True)    # 自动隐藏
        imageWidget1.setAlignment(imageWidget1.ALIGN_TOP)

        imageWidget11 = BaseImageWidget(self, "../images/1.jpg")
        imageWidget11.setContent("图片1标题", "图片1的详细内容", titleColor = "red", textColor = "white")
        imageWidget11.setAlphaColorStr("#000000", 100)
        imageWidget11.setAutoHideText(True)    # 自动隐藏
        imageWidget11.setAlignment(imageWidget11.ALIGN_CENTER)

        imageWidget111 = BaseImageWidget(self, "../images/1.jpg")
        imageWidget111.setContent("图片1标题", "图片1的详细内容", titleColor = "red", textColor = "white")
        imageWidget111.setAlphaColorStr("#000000", 100)
        imageWidget111.setAutoHideText(True)    # 自动隐藏
        imageWidget111.setAlignment(imageWidget111.ALIGN_BOTTOM)

        imageWidget2 = RoundImageWidget(self, "../images/2.jpg")
        imageWidget2.setContent("图片2标题", "图片2的详细内容", titleColor = "red", textColor = "white")
        imageWidget2.setAlphaColorInt(0, 0, 0, 100)
        imageWidget2.setAutoHideText(True)
        imageWidget2.setAlignment(imageWidget2.ALIGN_TOP)

        imageWidget22 = RoundImageWidget(self, "../images/2.jpg")
        imageWidget22.setContent("图片2标题", "图片2的详细内容", titleColor = "red", textColor = "white")
        imageWidget22.setAlphaColorInt(0, 0, 0, 100)
        imageWidget22.setAutoHideText(True)
        imageWidget22.setAlignment(imageWidget22.ALIGN_CENTER)

        imageWidget222 = RoundImageWidget(self, "../images/2.jpg")
        imageWidget222.setContent("图片2标题", "图片2的详细内容", titleColor = "red", textColor = "white")
        imageWidget222.setAlphaColorInt(0, 0, 0, 100)
        imageWidget222.setAutoHideText(True)
        imageWidget222.setAlignment(imageWidget222.ALIGN_BOTTOM)

        imageWidget3 = CircleImageWidget(self, "../images/3.jpg")
        imageWidget3.setContent("图片3标题", "图片3的详细内容", titleColor = "red", textColor = "green")
        imageWidget3.setAlphaColorInt(0, 0, 0, 100)
        imageWidget3.setAutoHideText(True)
        imageWidget3.setAlignment(imageWidget3.ALIGN_TOP)

        imageWidget33 = CircleImageWidget(self, "../images/3.jpg")
        imageWidget33.setContent("图片3标题", "图片3的详细内容", titleColor = "red", textColor = "green")
        imageWidget33.setAlphaColorInt(0, 0, 0, 100)
        imageWidget33.setAutoHideText(True)
        imageWidget33.setAlignment(imageWidget33.ALIGN_CENTER)

        imageWidget333 = CircleImageWidget(self, "../images/3.jpg")
        imageWidget333.setContent("图片3标题", "图片3的详细内容", titleColor = "red", textColor = "green")
        imageWidget333.setAlphaColorInt(0, 0, 0, 100)
        imageWidget333.setAutoHideText(True)
        imageWidget333.setAlignment(imageWidget333.ALIGN_BOTTOM)

        imageWidget4 = OverlayImageWidget(self, "../images/4.jpg")
        imageWidget4.setAlphaColorInt(0, 0, 0, 100)
        imageWidget4.setContent("图片4标题", "图片4的详细内容", titleColor = "red", textColor = "white", visible = False)

        # 横向分布局一
        hLayout1 = QHBoxLayout()
        hLayout1.addWidget(imageWidget1)
        hLayout1.addWidget(imageWidget11)
        hLayout1.addWidget(imageWidget111)

        # 横向分布局二
        hLayout2 = QHBoxLayout()
        hLayout2.addWidget(imageWidget2)
        hLayout2.addWidget(imageWidget22)
        hLayout2.addWidget(imageWidget222)

        # 横向分布局三
        hLayout3 = QHBoxLayout()
        hLayout3.addWidget(imageWidget3)
        hLayout3.addWidget(imageWidget33)
        hLayout3.addWidget(imageWidget333)

        # 横向分布局四
        hLayout4 = QHBoxLayout()
        hLayout4.addWidget(imageWidget4)

        vLayout = QVBoxLayout(self)    # 纵向总布局
        vLayout.addLayout(hLayout1)
        vLayout.addLayout(hLayout2)
        vLayout.addLayout(hLayout3)
        vLayout.addLayout(hLayout4)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestImageWidget()
    window.show()
    sys.exit(app.exec_())
