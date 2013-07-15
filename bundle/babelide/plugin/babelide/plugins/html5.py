import os
import os.path as osp
import sys
import datetime

import vim

from babelide.plugins.base import BabelIDE_Plugin
from babelide.plugins.base import expose

class BabelIDE_HTML5_Plugin(BabelIDE_Plugin):
    """This class implements HTML5 functionality"""

    def __init__(self):
        """@todo: to be defined1 """
        BabelIDE_Plugin.__init__(self)

        pass

    @expose
    def open_remote_chrome_debug_session(self):
        """ Open a remote chrome debug session as a subprocess"""
        vim.current.line = 'hello world {}'.format(datetime.datetime.now())
        pass

    @expose
    def close_remote_chrome_debug_session(self):
        """Close the open session
        :returns: @todo

        """
        vim.current.line = 'and now we are done'
        pass

