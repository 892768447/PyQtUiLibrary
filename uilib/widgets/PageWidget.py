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

    def setPages(self, pages):
        '''设置页数'''
        self.pages = pages
        self._refresh(pages)

    def getPages(self):
        '''得到当前总的页数'''
        return self.pages
