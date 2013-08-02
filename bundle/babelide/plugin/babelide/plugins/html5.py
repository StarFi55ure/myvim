import os
import os.path as osp
import sys
import shutil
import subprocess
import datetime
import vim

from babelide.plugins.base import BabelIDE_Plugin
from babelide.plugins.base import expose
from babelide.plugins.base import autocommand

from babelide.utils import random_string

class BabelIDE_HTML5_Plugin(BabelIDE_Plugin):
    """This class implements HTML5 functionality"""

    def __init__(self, manager):
        """@todo: to be defined1 """
        super(BabelIDE_HTML5_Plugin, self).__init__(manager)

        # remote chrome attributes
        self.__remote_chrome_inst = None
        self.__chrome_bin = '/usr/bin/google-chrome'
        self.__chrome_userdir = \
                '~/.config/google-chrome/{}'.format(random_string())
        self.__chrome_userdir = osp.expanduser(self.__chrome_userdir)

        self.__chrome_remote_port = 9222
    
    def get_actions(self):
        """Get the list of all filetypes actions that can be performed

        @returns Dictionary of filetype to action mappings
        """
        class MyAction(object):

            def __init__(self, name):
                """
                :returns: @todo

                """
                self.name = name

        actions = {}
        for i in range(10):
            if 'python' not in actions:
                actions['python'] = []
            actions['python'].append(MyAction('Action {}'.format(i)))
         
        return actions

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

    #@autocommand('CursorMovedI', ['*.vim', '*.py', '*.html'])
    def cursor_moved(self):
        '''Move cursor'''
        print "cursor has moved"

    #@autocommand('InsertLeave', ['*.vim', '*.js'])
    def insert_leave(self):
        '''Leave insert mode'''
        print 'insert leave'

