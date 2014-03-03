import os
import sys
import time
import vim
import requests
import pprint
import json
import threading
import urlparse

import websocket

from Queue import Queue
from threading import Thread

class BaseTab(object):
    """Base class to manage the debugger commands"""

    def __init__(self, plugin):
        """Constructor """
        # only do local import to make sure we dont hit
        # cyclic import dependancy
        from babelide import BabelIDE_Manager as manager
        self._manager = manager
        self._plugin = plugin

    def set_inqueue(self, inqueue):
        """Set the queue for incoming messages

        :inqueue: @todo
        :returns: @todo

        """
        self._inqueue = inqueue

    def set_outqueue(self, outqueue):
        """Set the queue for outgoing messages

        :outqueue: @todo
        :returns: @todo

        """
        self._outqueue = outqueue

    def process_messages(self):
        """Process the messages from the in queue
        :returns: @todo

        """

        def _process():
            self._processing = True
            while self._processing:
                message = self._inqueue.get()
                callee = message['method'].replace('.', '_')
                callee = callee.lower()
                if hasattr(self, callee):
                    getattr(self, callee)(message)
                else:
                    errtxt = 'no function {} for {}'

                    print errtxt.format(callee, message['method'])
                self._inqueue.task_done()

        self._in_thread = Thread(target=_process)
        self._in_thread.daemon = True
        self._in_thread.start()

    def stop_processing(self):
        """Stop processing messages
        :returns: @todo

        """
        self._processing = False


class DebuggerTab(BaseTab):
    """Manage the debugger commands"""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        BaseTab.__init__(self, *args, **kwargs)

        self._scripts = {}

    def init(self):
        """Initialize tab

        """
        request = {}
        request['id'] = 101
        request['method'] = 'Debugger.enable'

        self._outqueue.put(request)

    def save_buffer_to_remote(self):
        """Save the buffer contents to the remote instance

        """
        buf = vim.current.buffer
        fullname = vim.eval('expand("%:p")')

        data_to_save = None
        for key, val in self._scripts.iteritems():
            if fullname.endswith(key):
                print 'saving buffer ', fullname
                print val
                data_to_save = val['params']

        if data_to_save:
            request = {}
            request['id'] = 200
            request['method'] = 'Debugger.setScriptSource'
            request['params'] = {
                'scriptId': data_to_save['scriptId'],
                'scriptSource': '\n'.join(buf[:])
            }

            self._outqueue.put(request)


    def debugger_scriptparsed(self, data):
        """Process when a script has been loaded into chrome

        :data: @todo
        :returns: @todo

        """
        path = urlparse.urlparse(data['params']['url']).path
        self._scripts[path] = data

class NetworkTab(BaseTab):
    """Class for network tab functionality"""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        BaseTab.__init__(self, *args, **kwargs)

    def init(self):
        """Initialize the network tab object
        :returns: @todo

        """
        request = {}
        request['id'] = 103
        request['method'] = 'Network.enable'

        self._outqueue.put(request)

    def save_buffer_to_remoate(self):
        """Force resource files to reload in browser
        :returns: @todo

        """
        pass
        

class ChromeRemoteDebugger(object):
    """Main chrome debugger object"""

    def __init__(self, host, port, plugin=None):
        """Constructor"""
        self._plugin = plugin
        self._host = 'http://{}'.format(host)
        self._port = port

        self._debugger_inqueue = Queue()
        self._network_inqueue = Queue()
        self._outqueue = Queue()

        self._debuggertab = DebuggerTab(self._plugin)
        self._debuggertab.set_inqueue(self._debugger_inqueue)
        self._debuggertab.set_outqueue(self._outqueue)

        self._networktab = NetworkTab(self._plugin)
        self._networktab.set_inqueue(self._network_inqueue)
        self._networktab.set_outqueue(self._outqueue)

        # get basic configs from browser
        r = requests.get('{}:{}/json'.format(self._host, self._port))
        self._tabsjson = r.json()

        self._tabs = {}

        for t in self._tabsjson:
            self._tabs[t['id']] = t

        websocketurl = self._tabsjson[0]['webSocketDebuggerUrl']
        self._ws = websocket.WebSocketApp(websocketurl,
                on_message = self.on_message,
                on_error = self.on_error,
                on_close = self.on_close,
                on_open = self.on_open)

        # start main message processing thread
        self._processing_messages = True
        def send_out_messages():
            while self._processing_messages:
                outgoing_message = self._outqueue.get()
                s = json.dumps(outgoing_message)
                self._ws.send(s)
                self._outqueue.task_done()

        self._message_thread = Thread(target=lambda : send_out_messages())
        self._message_thread.daemon = True
        self._message_thread.start()

        # start main websocket event loop thread
        def runfunc(ws):
            ws.run_forever()

        self._runthread = Thread(target=lambda : runfunc(self._ws))
        self._runthread.daemon = True
        self._runthread.start()


    def on_message(self, ws, str_message):

        message = json.loads(str_message)
        # check if a notification
        if 'method' in message:
            component, method = message['method'].split('.')
            if component.lower() == 'debugger':
                self._debugger_inqueue.put(message)
            elif component.lower() == 'network':
                self._network_inqueue.put(message)

        # check if a response message
        if 'id' in message:
            pass

    def on_error(self, ws, error):
        print 'error: ', error

    def on_close(self, ws):
        print 'closing websocket'

    def on_open(self, ws):

        request = {}
        request['id'] = 100
        request['method'] = 'Page.navigate'
        request['params'] = {
            'url': 'http://localhost:5000'
        }
        s = json.dumps(request)
        ws.send(s)

        self._debuggertab.init()
        self._networktab.init()

        self._debuggertab.process_messages()
        self._networktab.process_messages()


    def show_tab_list(self):
        """Show the list of tabs we can connect to
        :returns: @todo

        """
        return ''

    def __getattr__(self, name):
        """Custom attribute lookup for debug functionality
        """
        if name.index('__') < 0:
            raise AttributeError

        tab, func = name.split('__', 1)

        debugtabs = {
            'debugger': self._debuggertab,
            'network': self._networktab
        }

        if tab in debugtabs:
            t = debugtabs[tab]
            if hasattr(t, func):
                return getattr(t, func)
            else:
                raise AttributeError




        
        
