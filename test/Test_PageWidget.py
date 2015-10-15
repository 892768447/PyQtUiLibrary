#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年9月5日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 
'''

from __future__ import unicode_literals

from os.path import dirname, abspath
import sys

# 解决2.x到3.x的字符串问题
# 父级目录
sys.path.insert(0, dirname(dirname(abspath(sys.argv[0]))))
sys.path.insert(0, dirname(dirname(abspath(__file__))))



from PyQt5.QtWidgets import QVBoxLayout, QWidget, QApplication

from uilib.widgets.PageWidget import PageWidget

__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class Window(QWidget):

    def __init__(self, parent = None):
        super(Window, self).__init__(parent)
        self.setObjectName("Form")
        self.setStyleSheet("QWidget#Form{background-color:white;}")

        vLayout = QVBoxLayout(self)
        vLayout.setSpacing(0)
        vLayout.setContentsMargins(0, 0, 0, 0)
        self.pageWidget = PageWidget(self, pages = 28)
        self.pageWidget.setResPath("../uilib/img")    # 因为这里是test文件夹,需要重新设置
        self.pageWidget.updateStyle()
        vLayout.addWidget(self.pageWidget)

        self.pageWidget.ITEMCLICKED.connect(self.itemClicked)

    def itemClicked(self, item):
        print(item.getNumber())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
