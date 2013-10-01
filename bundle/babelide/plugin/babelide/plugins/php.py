import os
import os.path as osp
import sys
import shutil
import socket
import subprocess
import datetime
import vim
import json


from babelide.plugins.base import BabelIDE_Plugin
from babelide.plugins.base import expose
from babelide.plugins.base import autocommand

from babelide.utils import random_string
from babelide.utils import writebuf
from babelide.utils import wait_net_service

from babelide.plugins.phplib.xdebugserver import XDebugServer

class BabelIDE_PHP_Plugin(BabelIDE_Plugin):
    """This class implements HTML5 functionality"""

    name = 'PHP'

    def __init__(self, manager):
        """@todo: to be defined1 """
        super(BabelIDE_PHP_Plugin, self).__init__(manager)

        self._xdebug_server = None

    
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
            if 'php' not in actions:
                actions['php'] = []
            actions['php'].append(MyAction('Action {}'.format(i)))
         
        return actions

    def get_mappings(self):
        """Return the global key mappings defined by this plugin
        :returns: @todo

        """
        mappings = []

        return mappings

    def load_project_definition(self):
        """Load a project definition if one exists
        :returns: @todo

        """
        if not self._project_definition:
            projectfile = os.path.join(os.getcwd(), 'vimphpproject.json')
            if os.path.exists(projectfile):
                with open(projectfile, 'r') as f:
                    self._project_definition = json.load(f)

    def save_project_definition(self):
        """Save project definition to file
        :returns: @todo

        """
        pass
        

    #################################################################
    # PHP Debugger entry points
    #################################################################

    @expose
    def start_debug_session(self):
        """Start a debug session in a new tab
        :returns: @todo

        """
        vim.command('tabnew')

        self._xdebug_server = XDebugServer()

    @expose
    def stop_debug_session(self):
        """Stop a running debug session
        :returns: @todo

        """
        if self._xdebug_server:
            self._xdebug_server.stop()

    @expose
    def get_debug_status(self):
        """@todo: Docstring for get_debug_status.
        :returns: @todo

        """
        if self._xdebug_server:
            self._xdebug_server.send_status()


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

    #@expose
    #@autocommand('FileType', ['php'])
    def file_type(self):
        '''Run after setting filetype'''
        pass


