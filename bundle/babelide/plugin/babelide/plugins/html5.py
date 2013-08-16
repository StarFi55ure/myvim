import os
import os.path as osp
import sys
import shutil
import socket
import subprocess
import datetime
import vim

from babelide.plugins.base import BabelIDE_Plugin
from babelide.plugins.base import expose
from babelide.plugins.base import autocommand

from babelide.plugins.html5lib.chromeremotedebugger import ChromeRemoteDebugger

from babelide.utils import random_string
from babelide.utils import writebuf
from babelide.utils import wait_net_service

class BabelIDE_HTML5_Plugin(BabelIDE_Plugin):
    """This class implements HTML5 functionality"""

    name = 'HTML5'

    def __init__(self, manager):
        """@todo: to be defined1 """
        super(BabelIDE_HTML5_Plugin, self).__init__(manager)

        # remote chrome attributes
        self.__remote_chrome_inst = None
        self.__chrome_bin = '/usr/bin/google-chrome'
        self.__chrome_userdir = \
                '~/.config/google-chrome/{}'.format(random_string())
        self.__chrome_userdir = osp.expanduser(self.__chrome_userdir)

        self._chrome_remote_port = 9222
        

        self._chrome_debugger = None

        #self._nullfile = open('out.logging', 'w');

    
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

    def get_mappings(self):
        """Return the global key mappings defined by this plugin
        :returns: @todo

        """
        mappings = []

        return mappings

    #################################################################
    # Chrome Debugger entry points
    #################################################################

    @expose
    def debug_open_remote_debug_session(self):
        """ Open a remote debug session"""

        # Clear the buffer and open a new session
        buf = vim.current.buffer
        buf[:] = ['']
        writebuf(buf, '-> opening remote session')

        if not self.__remote_chrome_inst:
            self.__remote_chrome_inst = subprocess.Popen([self.__chrome_bin,
                '--user-data-dir={}'.format(self.__chrome_userdir),
                '--remote-debugging-port={}'.format(self._chrome_remote_port),
                '--no-first-run',
                '--enable-logging'],
                #stdout=self._nullfile,
                stderr=subprocess.STDOUT
                )

        writebuf(buf, '-> waiting for chrome debug port to open...')
        if not wait_net_service('localhost', self._chrome_remote_port, 30):
            print 'Error waiting from chrome debug port to open'

        # create a debug controller object
        writebuf(buf, '-> creating remote debugger')
        self._chrome_debugger = ChromeRemoteDebugger('localhost',
                self._chrome_remote_port)

        # show list of tab to select from
        self._chrome_debugger.show_tab_list()


    @expose
    def debug_close_remote_debug_session(self):
        """Close the open session
        :returns: @todo

        """
        if self.__remote_chrome_inst:
            self.__remote_chrome_inst.terminate()
            self.__remote_chrome_inst.wait()

            if osp.exists(self.__chrome_userdir):
                shutil.rmtree(self.__chrome_userdir)

    @expose
    def debug_chrome_tab_selected(self):
        """A chrome tab was selected for debugging
        :returns: @todo

        """
        pass

    @expose
    def debug_save_to_remote_chrome(self):
        """Save buffer contents to remote chrome

        """
    
        if self.__remote_chrome_inst:
            b = vim.current.buffer

            lines = b[0:len(b)]

            print 'buffer contents: '
            print '\n'.join(lines)

    ##############################################################
    # These methods were for testing purposes
    ##############################################################

    #@autocommand('CursorMovedI', ['*.vim', '*.py', '*.html'])
    def cursor_moved(self):
        '''Move cursor'''
        print "cursor has moved"

    #@autocommand('InsertLeave', ['*.vim', '*.js'])
    def insert_leave(self):
        '''Leave insert mode'''
        print 'insert leave'

    @expose
    @autocommand('FileType', ['html'])
    def file_type(self):
        '''Run after setting filetype'''
        print 'set the filetype to html :-)'


