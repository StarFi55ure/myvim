import os
import sys
import time
import vim
import requests
import pprint
import json
import threading

import websocket

from threading import Thread

class ChromeRemoteDebugger(object):
    """Main chrome debugger object"""

    def __init__(self, host, port):
        """Constructor"""
        self._host = 'http://{}'.format(host)
        self._port = port

        r = requests.get('{}:{}/json'.format(self._host, self._port))
        self._tabsjson = r.json()

        print pprint.pprint(self._tabsjson)

        self._tabs = {}

        for t in self._tabsjson:
            self._tabs[t['id']] = t

        def on_message(ws, message):
            print 'message: ', message

        def on_error(ws, error):
            print 'error: ', error

        def on_close(ws):
            print 'closing websocket'

        def on_open(ws):
            print 'calling on open'
            request = {}
            request['id'] = 100
            request['method'] = 'Page.navigate'
            request['params'] = {
                'url': 'http://www.google.co.za'
            }
            s = json.dumps(request)
            print 'sending: ', s
            ws.send(s)

        time.sleep(5)
        websocketurl = self._tabsjson[0]['webSocketDebuggerUrl']
        print 'connecting to: ', websocketurl
        self._ws = websocket.WebSocketApp(websocketurl,
                on_message = on_message,
                on_error = on_error,
                on_close = on_close,
                on_open = on_open)

        def runfunc(ws):
            print 'inside runfunc'
            ws.run_forever()
            print 'done with runfunc'

        self._runthread = Thread(target=lambda : runfunc(self._ws))
        print 'starting thread'
        self._runthread.start()
        #self._ws.send('hello')
        

    def show_tab_list(self):
        """Show the list of tabs we can connect to
        :returns: @todo

        """
        return ''

        
        
