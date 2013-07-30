import os
import os.path as osp
import sys
import datetime

import vim

def expose(func, *args, **kwargs):
    ''' Decorator to mark a method as exposed to the outside world'''
    func.__exposed__ = True 

    return func


class BabelIDE_Plugin(object):
    """Base class for BabelIDE plugins"""

    _manager = None

    def __init__(self, manager):
        """Constructor """
        self._manager = manager

class BabelIDE_Base_Plugin(BabelIDE_Plugin):
    """ Provides default functionality for the ide"""

    def __init__(self, manager):
        """Constructor"""
        super(BabelIDE_Base_Plugin, self).__init__(manager)
        
    def get_actions(self):
        """Return list of actions
        :returns: @todo

        """
        return {}

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

        

