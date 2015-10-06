#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年10月5日
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

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication

from uilib.widgets.LineEdit import LineEdit


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class TestLineEdit(QWidget):

    def __init__(self):
        super(TestLineEdit, self).__init__()
        self.setMinimumWidth(300)

        defaultLineEdit = LineEdit(self, "default", LineEdit.DEFAULT_STYLE)
        defaultLineEdit.setAutoClearButtonEnabled(True)
        defaultLineEdit.setFontSize(25)
        defaultLineEdit.setMinHeight(50)
        defaultLineEdit.setTextColor("#2ecc71")
        defaultLineEdit.updateStyle(LineEdit.DEFAULT_STYLE)

        errorLineEdit = LineEdit(self, style = LineEdit.ERROR_STYLE)
        errorLineEdit.setText("error")

        successLineEdit = LineEdit(self, "success", LineEdit.SUCCESS_STYLE)

        layout = QVBoxLayout(self)
        layout.addWidget(defaultLineEdit)
        layout.addWidget(errorLineEdit)
        layout.addWidget(successLineEdit)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestLineEdit()
    window.show()
    sys.exit(app.exec_())
