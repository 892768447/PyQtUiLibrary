#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年9月2日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 继承QApplication
'''

from PyQt5.QtWidgets import QApplication


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class Application(QApplication):

    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        self.qss = ""
        self.initSkin()

    def initSkin(self):
        try:
            if not self.qss:
                self.qss = open("uilib/uilib.qss", "r").read()
            self.setStyleSheet(self.qss)
        except Exception as e:
            print(e)
