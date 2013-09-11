import os
import os.path as osp
import sys
import datetime

import vim

from babelide.tools.wizard import Wizard

import gtk

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

    def get_entry_point_string(self, funcname):
        """Build an entry point string for use in vimscript

        :funcname: @todo
        :returns: @todo

        """
        return '{}_{}'.format(self.name, funcname)


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
            'target' : self.get_entry_point_string('start_debugger_session')
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
    def start_debugger_session(self):
        """Show a list of debugger types and start a session
        :returns: @todo

        """
        if int(vim.eval('has("gui_running")')):
            print 'gui running'
            window = gtk.Window()
            label = gtk.Label("Hello World");

            window.add(label)

            window.resize(640, 480)
            window.show_all()

        return 
        vim.command('tabnew')

        w = Wizard('Debugger Session Types:', self._manager)

        w.add_option('Chrome Debugger', 'HTML5_debug_open_remote_debug_session')
        w.add_option('Python (Remote)', 'Python_debug_open_remote_session')
        w.add_option('Python', 'Python_debug_open_session')

        w.show_list()


