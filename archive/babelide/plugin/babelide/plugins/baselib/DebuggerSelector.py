import os

from PySide.QtCore import *
from PySide.QtGui import *

from babelide.plugins.baselib.Ui_DebuggerSelector import Ui_DebuggerSelector

class DebuggerSelector(QMainWindow):
    """Select the debugger to start up"""

    returnval = None

    def __init__(self, parent=None):
        """@todo: to be defined1. """
        super(DebuggerSelector, self).__init__(parent)
        self.ui = Ui_DebuggerSelector()
        self.ui.setupUi(self)

    @Slot()
    def on_btnPHPDebugger_clicked(self, checked=False):
        """Start PHP Debugger
        :returns: @todo

        """
        self.returnval = {'debugger': 'php'}
        QApplication.instance().exit()

