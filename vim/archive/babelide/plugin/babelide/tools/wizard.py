import os
import sys
import vim


class Wizard(object):
    """Base class for all wizard objects"""

    _options = {}

    def __init__(self, title='Selection Window', manager=None):
        """Constructor"""
        self._title = title
        self._manager = manager
        self._labellist = []

    def add_option(self, label, entry_point):
        """Add an option for the list

        :key: @todo
        :val: @todo
        :returns: @todo

        """
        self._options[label] = entry_point

    def show_list(self):
        """Show the wizard list and wait for selection
        :returns: @todo
        """


        # build sorted option labels
        self._labellist = {item:idx for idx, item in enumerate(sorted(self._options.keys()))}

        self.build_selection_mappings()

        template_data = {
            'options': self._options
        }
        
        tpl = self._manager.tmpl_loader.get_template('debugger_sessions.tpl')

        buf = vim.current.buffer
        buf[:] = [str(x) for x in tpl.render(template_data).split('\n')]

        
    def build_selection_mappings(self):
        """Build the buffer mappings for the selections
        :returns: @todo

        """
        selection_format = "map <buffer> {} :execute(\"BabelIDE('{}')\")<cr>"
        for label, entry_point in self._options.iteritems():
            
            selection = selection_format.format(self._labellist[label] + 1, entry_point)
            vim.command(selection)
        


