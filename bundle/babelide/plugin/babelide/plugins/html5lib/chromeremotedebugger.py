import os
import sys
import thread
import time
import vim
import requests

import websocket

class ChromeRemoteDebugger(object):
    """Main chrome debugger object"""

    def __init__(self, host, port):
        """Constructor"""
        self._host = 'http://{}'.format(host)
        self._port = port

        r = requests.get('{}:{}/json'.format(self._host, self._port))
        self._tabsjson = r.json()

        print self._tabsjson

    def show_tab_list(self):
        """Show the list of tabs we can connect to
        :returns: @todo

        """
        return ''

        
        
