import os
import os.path as osp
import sys
import shutil
import subprocess
import datetime
import vim

from babelide.plugins.base import BabelIDE_Plugin
from babelide.plugins.base import expose

from babelide.utils import random_string

class BabelIDE_HTML5_Plugin(BabelIDE_Plugin):
    """This class implements HTML5 functionality"""

    def __init__(self):
        """@todo: to be defined1 """
        BabelIDE_Plugin.__init__(self)

        # remote chrome attributes
        self.__remote_chrome_inst = None
        self.__chrome_bin = '/usr/bin/google-chrome'
        self.__chrome_userdir = \
                '~/.config/google-chrome/{}'.format(random_string())
        self.__chrome_userdir = osp.expanduser(self.__chrome_userdir)

        self.__chrome_remote_port = 9222

    @expose
    def open_remote_chrome_debug_session(self):
        """ Open a remote chrome debug session as a subprocess"""

        if not self.__remote_chrome_inst:
            self.__remote_chrome_inst = subprocess.Popen([self.__chrome_bin,
                '--user-data-dir={}'.format(self.__chrome_userdir),
                '--remote-debugging-port={}'.format(self.__chrome_remote_port)]
                )


    @expose
    def close_remote_chrome_debug_session(self):
        """Close the open session
        :returns: @todo

        """
        if self.__remote_chrome_inst:
            self.__remote_chrome_inst.terminate()
            self.__remote_chrome_inst.wait()

            if osp.exists(self.__chrome_userdir):
                shutil.rmtree(self.__chrome_userdir)

    @expose
    def save_to_remote_chrome(self):
        """Save buffer contents to remote chrome

        """
    
        if self.__remote_chrome_inst:
            b = vim.current.buffer

            lines = b[0:len(b)]

            print 'buffer contents: '
            print '\n'.join(lines)



