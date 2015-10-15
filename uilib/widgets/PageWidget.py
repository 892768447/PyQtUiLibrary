#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年9月5日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 分页控件
'''
from PyQt5.QtCore import Qt, QSize, pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QListWidget, \
    QFrame, QListWidgetItem, QListView, QWidget, QPushButton, \
    QHBoxLayout, QSpacerItem, QSizePolicy


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class CustomPageItem(QListWidgetItem):
    '''中间普通页面'''

    def __init__(self, number, parent = None):
        super(CustomPageItem, self).__init__(parent)
        self.setNumber(number)
        # 设置item大小
        self.setSizeHint(QSize(40, 40))
        # 居中
        self.setTextAlignment(Qt.AlignCenter)

    def setNumber(self, number):
        '''设置页数数字(数字,大于0)'''
        self.number = number
        self.setText(str(number))
        self.setToolTip("第{page}页".format(page = number))

    def getNumber(self):
        if getattr(self, "number"):
            return self.number
        return 0

class BothSidesItem(QPushButton):

    def __init__(self, parent = None, which = ""):
        super(BothSidesItem, self).__init__(parent)
        if which == "left":
            self.setObjectName("_previous_btn")
        elif which == "right":
            self.setObjectName("_next_btn")

class PageWidget(QWidget):

    ITEMCLICKED = pyqtSignal(CustomPageItem)

    RES_PATH = "uilib/img"    # 图片资源的路径

    STYLE = """
QPushButton#_previous_btn,QPushButton#_next_btn {{
    max-width: 49px;
    max-height: 39px;
    min-width: 49px;
    min-height: 39px;
    width: 49px;
    height: 39px;
    border-color: #E4E7EA;
    
}}
QPushButton#_previous_btn:hover,QPushButton#_next_btn:hover {{
    border-color: #1ABC9C;
    background-color: #1ABC9C;
    
}}
QPushButton#_previous_btn:pressed,QPushButton#_next_btn:pressed {{
    border-color: #1ABC9C;
    background-color: #1ABC9C;
    
}}
QPushButton#_previous_btn {{
    padding-right: 1px;
    border-top-left-radius: 6px;
    border-top-right-radius: 0px;
    border-bottom-left-radius: 6px;
    border-bottom-right-radius: 0px;
    background: #E4E7EA url({RES_PATH}/arrow_left_white.png) no-repeat center center;
}}
QPushButton#_next_btn {{
    padding-left: 1px;
    border-top-left-radius: 0px;
    border-top-right-radius: 6px;
    border-bottom-left-radius: 0px;
    border-bottom-right-radius: 6px;
    background: #E4E7EA url({RES_PATH}/arrow_right_white.png) no-repeat center center;
}}

QListView#_page_list_widget {{
    max-height: 40px;
    background-color: rgba(0,0,0,0);
}}
QListView#_page_list_widget::item {{
    margin: 1px;
    color: white;
    background-color: #E4E7EA;
    height: 40px;
}}

QListView#_page_list_widget::item:selected {{
    background-color: #1ABC9C;
}}
QListView#_page_list_widget::item:focus {{
    background-color: #1ABC9C;
}}

QListView#_page_list_widget::item:hover {{
    background-color: #1ABC9C;
}}"""

    def __init__(self, parent = None, pages = 0):
        super(PageWidget, self).__init__(parent)
        self.setObjectName("_page_widget")
        self.pages = pages    # 页数
        self.cpage = 0

        # 左边按钮
        self._previous_btn = BothSidesItem(self, which = "left")
        self._previous_btn.clicked.connect(self._previous)
        self._previous_btn.setToolTip("上一页")
        # 右边按钮
        self._next_btn = BothSidesItem(self, which = "right")
        self._next_btn.clicked.connect(self._next)
        self._next_btn.setToolTip("下一页")

        self._page_list_widget = QListWidget(self)
        self._page_list_widget.setObjectName("_page_list_widget")
        # 无边框
        self._page_list_widget.setFrameShape(QFrame.NoFrame)
        # 无滑动条
        self._page_list_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self._page_list_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # 禁止自动滚动
        self._page_list_widget.setAutoScroll(False)
        # tab切换
        self._page_list_widget.setTabKeyNavigation(True)
        # 设置为横向
        self._page_list_widget.setFlow(QListView.LeftToRight)
        # 设置字体
        font = QFont()
        font.setPointSize(14)
        self._page_list_widget.setFont(font)
        # item点击事件
        self._page_list_widget.itemClicked.connect(self.ITEMCLICKED.emit)

        # 布局
        hLayout = QHBoxLayout(self)
        hLayout.setSpacing(0)
        hLayout.setContentsMargins(0, 0, 0, 0)
        spacerItem = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hLayout.addItem(spacerItem)
        hLayout.addWidget(self._previous_btn)
        hLayout.addWidget(self._page_list_widget)
        hLayout.addWidget(self._next_btn)
        hLayout.addItem(spacerItem)

        self._refresh(pages)

        self.updateStyle()    # 设置样式

    def _refresh(self, pages):
        # 动态调整宽度
        if pages == 0:
            self.resize(100, 40)
        elif pages >= 8:
            self._page_list_widget.setMinimumSize(320, 40)
            self._page_list_widget.resize(320, 40)
            self.resize(420, 40)
        self._page_list_widget.clear()
        # 中间
        for i in range(1, pages + 1):
            CustomPageItem(i, self._page_list_widget)

    def _previous(self, clicked):
        '''上一页'''
        num = int(self.pages / 8)
        if num == 0:
            return
        self.cpage -= 1
        if self.cpage >= 0:
            print("_previous: ", self.cpage)
            if self.cpage == 0:
                previousItem = self._page_list_widget.item(0)
            else:
                previousItem = self._page_list_widget.item(self.cpage * 8 - 4)
            self._page_list_widget.scrollTo(self._page_list_widget.indexFromItem(previousItem))
        else:
            self.cpage += 1

    def _next(self, clicked):
        '''下一页'''
        num = int(self.pages / 8)
        if num == 0:
            return
        self.cpage += 1
        if self.cpage <= num:
            print("_next: ", self.cpage)
            remainder = self.pages - self.cpage * 8
            if remainder > 8:
                nextItem = self._page_list_widget.item(self.cpage * 8 + 7)
            else:
                nextItem = self._page_list_widget.item(self.pages - 1)
            self._page_list_widget.scrollTo(self._page_list_widget.indexFromItem(nextItem))
        else:
            self.cpage -= 1

    def setResPath(self, resPath):
        '''设置资源路径'''
        self.RES_PATH = resPath

    def getResPath(self):
        return self.RES_PATH

    def updateStyle(self):
        '''刷新样式'''
        self.setStyleSheet(self.STYLE.format(RES_PATH = self.RES_PATH))

    def setPages(self, pages):
        '''设置页数'''
        self.pages = pages
        self._refresh(pages)

    def getPages(self):
        '''得到当前总的页数'''
        return self.pages
