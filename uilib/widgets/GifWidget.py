#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年10月15日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: GifWidget
'''
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QMovie

__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class GifWidget(QLabel):

    def __init__(self, parent = None, path = None):
        super(GifWidget, self).__init__(parent)
        self.setPath(path)

    def __del__(self):
        print("GifWidget __del__")
        if hasattr(self, "_movie"):
            self._movie.stop()
            del self._movie

    def setPath(self, path):
        if hasattr(self, "_movie"):
            self._movie.stop()
            del self._movie
        if not path:
            return
        self._movie = QMovie(path)
        self.setMovie(self._movie)
        self._movie.start()

    def start(self):
        if hasattr(self, "_movie"):
            self._movie.start()

    def stop(self):
        if hasattr(self, "_movie"):
            self._movie.stop()
