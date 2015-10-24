#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年10月22日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 
'''

from __future__ import unicode_literals

import os
from os.path import dirname, abspath
import random
import sys

# 解决2.x到3.x的字符串问题
# 父级目录
sys.path.insert(0, dirname(dirname(abspath(sys.argv[0]))))
sys.path.insert(0, dirname(dirname(abspath(__file__))))

from PyQt5.QtCore import QMetaObject, pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, \
    QPushButton, QHBoxLayout, QListWidgetItem, QTextEdit

from uilib.widgets.NinePatchLabel import NinePatchLabel

__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

SCROLLBARSTYLE = """
/*QScrollBar Style*/

QScrollBar:vertical {
    background: transparent;
    width: 10px;
    margin: 0px 0px 0px 0px;
    padding-top: 12px;
    padding-bottom: 12px;
}
QScrollBar:horizontal {
    background: transparent;
    height: 10px;
    margin: 0px 0px 0px 0px;
    padding-left: 12px;
    padding-right: 12px;
}

QScrollBar:vertical:hover,QScrollBar:horizontal:hover {
    background: rgba(0, 0, 0, 30);
    border-radius: 5px;
}

QScrollBar::handle:vertical {
    background: rgba(0, 0, 0, 50);
    width: 10px;
    border-radius: 5px;
    border: none;
}
QScrollBar::handle:horizontal {
    background: rgba(0, 0, 0, 50);
    height: 10px;
    border-radius: 5px;
    border: none;
}

QScrollBar::handle:vertical:hover,QScrollBar::handle:horizontal:hover {
    background: rgba(0, 0, 0, 100);
}

QScrollBar::add-page:vertical {
    width: 10px;
    background: transparent;
}
QScrollBar::add-page:horizontal {
    height: 10px;
    background: transparent;
}

QScrollBar::sub-page:vertical {
    width: 10px;
    background: transparent;
}
QScrollBar::sub-page:horizontal {
    height: 10px;
    background: transparent;
}

QScrollBar::sub-line:vertical {
    height: 12px;
    width: 10px;
    background: transparent;
    subcontrol-position: top;
}
QScrollBar::sub-line:horizontal {
    height: 10px;
    width: 12px;
    background: transparent;
    subcontrol-position: left;
}

QScrollBar::up-arrow:vertical {
    image: url(../uilib/img/scrollbar_arrowup_normal.png);
}
QScrollBar::left-arrow:horizontal {
    image: url(../uilib/img/scrollbar_arrowleft_normal.png);
}

QScrollBar::up-arrow:vertical:hover {
    image: url(../uilib/img/scrollbar_arrowup_down.png);
}
QScrollBar::left-arrow:horizontal:hover {
    image: url(../uilib/img/scrollbar_arrowleft_down.png);
}

QScrollBar::up-arrow:vertical:pressed {
    image: url(../uilib/img/scrollbar_arrowup_highlight.png);
}
QScrollBar::left-arrow:horizontal:pressed {
    image: url(../uilib/img/scrollbar_arrowleft_highlight.png);
}

QScrollBar::add-line:vertical {
    height: 12px;
    width: 10px;
    background: transparent;
    subcontrol-position: bottom;
}
QScrollBar::add-line:horizontal {
    height: 10px;
    width: 12px;
    background: transparent;
    subcontrol-position: right;
}

QScrollBar::down-arrow:vertical {
    image: url(../uilib/img/scrollbar_arrowdown_normal.png);
}
QScrollBar::right-arrow:horizontal {
    image: url(../uilib/img/scrollbar_arrowright_normal.png);
}

QScrollBar::down-arrow:vertical:hover {
    image: url(../uilib/img/scrollbar_arrowdown_down.png);
}
QScrollBar::right-arrow:horizontal:hover {
    image: url(../uilib/img/scrollbar_arrowright_down.png);
}

QScrollBar::down-arrow:vertical:pressed {
    image: url(../uilib/img/scrollbar_arrowdown_highlight.png);
}
QScrollBar::right-arrow:horizontal:pressed {
    image: url(../uilib/img/scrollbar_arrowright_highlight.png);
}
"""

class Item(NinePatchLabel):

    def __init__(self, parent = None, text = "", norImage = None, preImage = None):
        super(Item, self).__init__(parent, text, norImage, preImage)
        self.setStyleSheet("margin: 30px;")

class TestNinePatchLabel(QWidget):

    skin_aio_friend_bubble_nor = "skin_aio_friend_bubble_nor.9.png"
    skin_aio_friend_bubble_pressed = "skin_aio_friend_bubble_pressed.9.png"
    skin_aio_user_bubble_nor = "skin_aio_user_bubble_nor.9.png"
    skin_aio_user_bubble_pressed = "skin_aio_user_bubble_pressed.9.png"

    def __init__(self):
        super(TestNinePatchLabel, self).__init__()
        self.resize(400, 600)

        self.listWidget = QListWidget(self)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("""
            QListWidget::item:selected {
                background: rgba(0,0,0,0);
            }
            QListWidget::item:hover {
                background: rgba(0,0,0,0);
            }
        """)

        self.textEdit = QTextEdit(self)
        self.textEdit.setMaximumHeight(100)
        self.textEdit.setObjectName("textEdit")

        self.sendBtn = QPushButton("发送", self)
        self.sendBtn.setObjectName("sendBtn")

        hlayout = QHBoxLayout()
        hlayout.setContentsMargins(0, 0, 0, 0)
        hlayout.setSpacing(0)
        hlayout.addWidget(self.textEdit)
        hlayout.addWidget(self.sendBtn)

        vlayout = QVBoxLayout(self)
        vlayout.setContentsMargins(0, 0, 0, 0)
        vlayout.setSpacing(0)
        vlayout.addWidget(self.listWidget)
        vlayout.addItem(hlayout)

        QMetaObject.connectSlotsByName(self)    # 通过objectname注册信号
        self.init()
        self.setStyleSheet(SCROLLBARSTYLE)

    def init(self):
        '''加载气泡数组'''
        paths = os.listdir("..\\bubble")
        self.bubble = [
            (
             os.path.join(os.path.join("..\\bubble", path), self.skin_aio_friend_bubble_nor),
             os.path.join(os.path.join("..\\bubble", path), self.skin_aio_friend_bubble_pressed),
             os.path.join(os.path.join("..\\bubble", path), self.skin_aio_user_bubble_nor),
             os.path.join(os.path.join("..\\bubble", path), self.skin_aio_user_bubble_pressed)
            )
            for path in paths
        ]

    @pyqtSlot()
    def on_sendBtn_clicked(self):
        self.send()

    def send(self):
        '''发送消息'''
        text = self.textEdit.toPlainText().strip()
        if not text:
            return
        fn , fp, un, up = random.choice(self.bubble)    # 从中随机一个

        # 我说
        item = QListWidgetItem()
        self.listWidget.addItem(item)
        pItem = Item(None, "我说: " + text, un, up)
        item.setSizeHint(pItem.size())    # 把item的大小变得和label一样
        self.listWidget.setItemWidget(item, pItem)

        # 对方说
        item = QListWidgetItem()
        self.listWidget.addItem(item)
        pItem = Item(None, "她说: " + text, fn, fp)
        item.setSizeHint(pItem.size())    # 把item的大小变得和label一样
        self.listWidget.setItemWidget(item, pItem)

        self.listWidget.scrollTo(self.listWidget.indexFromItem(item))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestNinePatchLabel()
    window.show()
    sys.exit(app.exec_())
