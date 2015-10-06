#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年10月4日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: TestPushButton
'''
from __future__ import unicode_literals
# 解决2.x到3.x的字符串问题
from os.path import dirname, abspath
import sys
# 父级目录
sys.path.insert(0, dirname(dirname(abspath(sys.argv[0]))))
sys.path.insert(0, dirname(dirname(abspath(__file__))))

from uilib.utils import PY3, QT5
from uilib.widgets.PushButton import PushButton

if PY3() and QT5():
    from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout    # @UnresolvedImport @UnusedImport
else:
    from PyQt4.QtGui import QWidget, QVBoxLayout, QApplication    # @Reimport @UnresolvedImport


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class TestPushButton(QWidget):

    def __init__(self):
        super(TestPushButton, self).__init__()
        self.setMinimumWidth(300)

        defaultButton = PushButton(self, "default")
        defaultButton.setFontSize(33)
        # 这里通过的更新qss样式代码来设置字体大小
        # 当然也可以用QFont就不用updateStyle
        defaultButton.updateStyle(PushButton.DEFAULT_STYLE)

        primaryButton = PushButton(self, "primary")
        primaryButton.setBorderRadius(15)    # 修改圆角
        primaryButton.setPrimaryStyle(True)    # 使用primary样式
        primaryButton.updateStyle(PushButton.PRIMARY_STYLE)    # 需要更新

        # 也可以这样设置样式
        warningButton = PushButton(self, "warning", style = PushButton.WARNING_STYLE)
        warningButton.setMinHeight(55)    # 修改最小高度
        warningButton.updateStyle(PushButton.WARNING_STYLE)

        dangerButton = PushButton(self, "danger", style = PushButton.DANGER_STYLE)

        successButton = PushButton(self, "success", style = PushButton.SUCCESS_STYLE)
        inverseButton = PushButton(self, "inverse", style = PushButton.INVERSE_STYLE)
        infoButton = PushButton(self, "info", style = PushButton.INFO_STYLE)

        disableButton = PushButton(self, "disable")
        disableButton.setDisabled(True)

        layout = QVBoxLayout(self)
        layout.addWidget(defaultButton)
        layout.addWidget(primaryButton)
        layout.addWidget(warningButton)
        layout.addWidget(dangerButton)
        layout.addWidget(successButton)
        layout.addWidget(inverseButton)
        layout.addWidget(infoButton)
        layout.addWidget(disableButton)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestPushButton()
    window.show()
    sys.exit(app.exec_())
