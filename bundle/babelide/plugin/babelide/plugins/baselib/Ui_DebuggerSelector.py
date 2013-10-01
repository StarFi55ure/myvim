# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DebuggerSelector.ui'
#
# Created: Sun Sep 29 13:44:26 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DebuggerSelector(object):
    def setupUi(self, DebuggerSelector):
        DebuggerSelector.setObjectName("DebuggerSelector")
        DebuggerSelector.resize(320, 240)
        self.centralwidget = QtGui.QWidget(DebuggerSelector)
        self.centralwidget.setObjectName("centralwidget")
        self.btnPHPDebugger = QtGui.QPushButton(self.centralwidget)
        self.btnPHPDebugger.setGeometry(QtCore.QRect(40, 50, 211, 41))
        self.btnPHPDebugger.setFlat(False)
        self.btnPHPDebugger.setObjectName("btnPHPDebugger")
        self.btnChromeDebugger = QtGui.QPushButton(self.centralwidget)
        self.btnChromeDebugger.setGeometry(QtCore.QRect(40, 100, 211, 41))
        self.btnChromeDebugger.setObjectName("btnChromeDebugger")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        DebuggerSelector.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(DebuggerSelector)
        self.statusbar.setObjectName("statusbar")
        DebuggerSelector.setStatusBar(self.statusbar)

        self.retranslateUi(DebuggerSelector)
        QtCore.QMetaObject.connectSlotsByName(DebuggerSelector)

    def retranslateUi(self, DebuggerSelector):
        DebuggerSelector.setWindowTitle(QtGui.QApplication.translate("DebuggerSelector", "Select Debugger", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPHPDebugger.setText(QtGui.QApplication.translate("DebuggerSelector", "PHP (Xdebug)", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPHPDebugger.setShortcut(QtGui.QApplication.translate("DebuggerSelector", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.btnChromeDebugger.setText(QtGui.QApplication.translate("DebuggerSelector", "Chrome Debugger", None, QtGui.QApplication.UnicodeUTF8))
        self.btnChromeDebugger.setShortcut(QtGui.QApplication.translate("DebuggerSelector", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DebuggerSelector", "Select the debugger you want to start:", None, QtGui.QApplication.UnicodeUTF8))

