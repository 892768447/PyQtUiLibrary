# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_MetroProgressBar.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MetroProgressBar(object):
    def setupUi(self, MetroProgressBar):
        MetroProgressBar.setObjectName("MetroProgressBar")
        MetroProgressBar.resize(400, 16)
        MetroProgressBar.setMaximumSize(QtCore.QSize(16777215, 16))
        MetroProgressBar.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.MetroProgressBarCircle1 = QtWidgets.QWidget(MetroProgressBar)
        self.MetroProgressBarCircle1.setGeometry(QtCore.QRect(0, 4, 8, 8))
        self.MetroProgressBarCircle1.setObjectName("MetroProgressBarCircle1")
        self.MetroProgressBarCircle2 = QtWidgets.QWidget(MetroProgressBar)
        self.MetroProgressBarCircle2.setGeometry(QtCore.QRect(0, 4, 8, 8))
        self.MetroProgressBarCircle2.setObjectName("MetroProgressBarCircle2")
        self.MetroProgressBarCircle5 = QtWidgets.QWidget(MetroProgressBar)
        self.MetroProgressBarCircle5.setGeometry(QtCore.QRect(0, 4, 8, 8))
        self.MetroProgressBarCircle5.setObjectName("MetroProgressBarCircle5")
        self.MetroProgressBarCircle4 = QtWidgets.QWidget(MetroProgressBar)
        self.MetroProgressBarCircle4.setGeometry(QtCore.QRect(0, 4, 8, 8))
        self.MetroProgressBarCircle4.setObjectName("MetroProgressBarCircle4")
        self.MetroProgressBarCircle3 = QtWidgets.QWidget(MetroProgressBar)
        self.MetroProgressBarCircle3.setGeometry(QtCore.QRect(0, 4, 8, 8))
        self.MetroProgressBarCircle3.setObjectName("MetroProgressBarCircle3")

        self.retranslateUi(MetroProgressBar)
        QtCore.QMetaObject.connectSlotsByName(MetroProgressBar)

    def retranslateUi(self, MetroProgressBar):
        _translate = QtCore.QCoreApplication.translate
        MetroProgressBar.setWindowTitle(_translate("MetroProgressBar", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MetroProgressBar = QtWidgets.QWidget()
    ui = Ui_MetroProgressBar()
    ui.setupUi(MetroProgressBar)
    MetroProgressBar.show()
    sys.exit(app.exec_())

