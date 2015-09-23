#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年9月2日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 
'''
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMessageBox

from uilib.Application import Application
from uilib.widgets.LineEdit import LineEdit


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class Window(QWidget):

    def __init__(self, parent = None):
        super(Window, self).__init__(parent)
        # 加载ui文件
        self.ui = uic.loadUi("ui/Ui_QLineEdit.ui", self)

        # 设置按钮属性(不同的属性对应不同的样式)
        self.ui.errorEdit.setProperty("error", True)
        self.ui.successEdit.setProperty("success", True)

        self.ui.searchEdit.setProperty("search-right", True)

        # 同时带有两种属性
        self.ui.search2Edit.setProperty("search-left", True)
        self.ui.search2Edit.setProperty("error", True)

        # 由于设置属性后需要重新设置样式
        Application.instance().initSkin()

class Window2(QWidget):

    def __init__(self, parent = None):
        super(Window2, self).__init__(parent)

        defaultEdit = LineEdit(self)
        errorEdit = LineEdit(self, styles = ["error"])
        successEdit = LineEdit(self, styles = ["success"])
        searchEdit = LineEdit(self, styles = ["search-right"])
        search2Edit = LineEdit(self, styles = ["search-left", "error"])
        search2Edit.setAutoClearButtonEnabled(True)    # 开启焦点变化自动隐藏清空按钮
        search2Edit.SEARCH.connect(self.onSearch)

        vbLayout = QVBoxLayout(self)
        vbLayout.addWidget(defaultEdit)
        vbLayout.addWidget(errorEdit)
        vbLayout.addWidget(successEdit)
        vbLayout.addWidget(searchEdit)
        vbLayout.addWidget(search2Edit)

        # 修改了属性需要重新设置样式
        Application.instance().initSkin()

    def onSearch(self, text):
        QMessageBox.about(self, "提示", text)

if __name__ == "__main__":
    import sys
    app = Application(sys.argv)
    window = Window()
    window.show()
    window2 = Window2()
    window2.show()
    sys.exit(app.exec_())
