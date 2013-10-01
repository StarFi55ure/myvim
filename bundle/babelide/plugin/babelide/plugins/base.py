import os
import os.path as osp
import sys
import datetime
import threading
import functools

import vim

from PySide.QtCore import *
from PySide.QtGui import *

from babelide.plugins.baselib.DebuggerSelector import DebuggerSelector


def expose(func, *args, **kwargs):
    ''' Decorator to mark a method as exposed to the outside world'''
    func.__exposed__ = True 

    return func

def autocommand(event, pattern, filetype='*'):
    '''Decorator to register an autocommand from a plugin'''

    def wrap(func):
        if not hasattr(func, '__autocmd__'):
            func.__autocmd__ = []

        acmd = {}
        acmd['event'] = event
        acmd['filetype'] = filetype
        acmd['pattern'] = pattern
        acmd['is_buffer_local'] = pattern == '<buffer>'

        func.__autocmd__.append(acmd)
        return func

    return wrap


class BabelIDE_Plugin(object):
    """Base class for BabelIDE plugins"""

    _manager = None

    def __init__(self, manager):
        """Constructor """
        self._manager = manager

    def get_entry_point_string(self, funcname, plugin=None):
        """Build an entry point string for use in vimscript

        :funcname: @todo
        :returns: @todo

        """
        if plugin:
            ep_name = '{}_{}'.format(plugin, funcname)
        else:
            ep_name = '{}_{}'.format(self.name, funcname)
        return ep_name

    def call_entry_point(self, funcname, plugin=None):
        """Call an entry point

        :plugin: @todo
        :funcname: @todo
        :returns: @todo

        """
        ep = self.get_entry_point_string(funcname, plugin)
        self._manager.call_entry_point(ep)


class BabelIDE_Base_Plugin(BabelIDE_Plugin):
    """ Provides default functionality for the ide"""

    name = 'Base'

    _wizard_classes = {}
    _current_wizard = None
    
    _debugger_entry_points = {}

    def __init__(self, manager):
        """Constructor"""
        super(BabelIDE_Base_Plugin, self).__init__(manager)
        
        pass
        
        
    def get_actions(self):
        """Return list of actions
        :returns: @todo

        """
        return {}

    def get_mappings(self):
        """Return global key mappings
        :returns: @todo

        """
        mappings = []
        m = {
            'mapping': 'nnoremap <leader>id',
            'target' : self.get_entry_point_string('select_debugger_session')
        }
        mappings.append(m)

        return mappings

    @expose
    def show_actions(self):
        """Show the actions for the current buffer and selection
        :returns: @todo

        """
        filetype = vim.eval('&filetype')

        actions = self._manager.get_action_list(filetype)
        action_names = [x.name for x in actions]

        vim.command('rightbelow vnew')
        vim.command('startinsert')
        vim.eval(r'feedkeys("Hello world\<CR>\<CR>")')

        current_date = str(datetime.datetime.now())[0:10]
        vim.eval('feedkeys("Current DateTime: {}\<CR>\<CR>")'.format(current_date))

        action_names_txt = '\<CR>'.join(action_names)
        vim.eval('feedkeys("{}")'.format(action_names_txt))

    @expose
    def build_mapping_to_python(self, mapping, pytarget):
        """Build a mapping string to call into python

        :mapping: @todo
        :pytarget: @todo
        :returns: @todo

        """
        return '{} :BabelIDE("{}")<CR>'.format(mapping, pytarget)


    ################################################################
    # Debugger entry poins
    ################################################################

    @expose
    def select_debugger_session(self):
        """Show a list of debugger types and start a session
        :returns: @todo

        """
        if int(vim.eval('has("gui_running")')):

            if QApplication.instance():
                app = QApplication.instance()
            else:
                app = QApplication(sys.argv)

            ds = DebuggerSelector()
            ds.show()

            app.exec_()
            if ds.returnval:
                {
                    'php': functools.partial(self.call_entry_point,
                        'start_debug_session', 'PHP')
                }[ds.returnval['debugger']]()


