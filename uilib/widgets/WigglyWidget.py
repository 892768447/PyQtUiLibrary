#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年10月2日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 
'''
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QFontMetrics, QColor, QPainter
from PyQt5.QtWidgets import QWidget, QApplication


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class WigglyWidget(QWidget):

    def __init__(self, parent = None):
        super(WigglyWidget, self).__init__(parent)
        newFont = self.font()
        newFont.setPointSize(newFont.pointSize() + 20)
        self.setFont(newFont)
        self.timer = QBasicTimer()
        self.text = ""
        self.step = 0
        self.timer.start(60, self)

    def paintEvent(self, event):
        sineTable = (0, 38, 71, 92, 100, 92, 71, 38, 0, -38, -71, -92, -100, -92, -71, -38)

        metrics = QFontMetrics(self.font())
        x = (self.width() - metrics.width(self.text)) / 2
        y = (self.height() + metrics.ascent() - metrics.descent()) / 2
        color = QColor()

        painter = QPainter(self)

        for i, ch in enumerate(self.text):
            index = (self.step + i) % 16
            color.setHsv((15 - index) * 16, 255, 191)
            painter.setPen(color)
            painter.drawText(x, y - ((sineTable[index] * metrics.height()) / 400), ch)
            x += metrics.width(ch)

    def setText(self, newText):
        self.text = newText

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.step += 1
            self.update()
        else:
            super(WigglyWidget, self).timerEvent(event)

if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)
    window = WigglyWidget()
    window.setText("hello word")
    window.show()
    sys.exit(app.exec_())