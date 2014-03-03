import os
import sys
import threading

from Queue import Queue
from tornado.tcpserver import TCPServer
from tornado.ioloop import IOLoop
from tornado.iostream import IOStream

from babelide.plugins.phplib.xdebugconnection import XDebugConnection


class XDebugServer(TCPServer):

    """Class to listen for xdebug requests"""

    def __init__(self):
        """Constructor """
        self.ioloop = IOLoop()
        super(XDebugServer, self).__init__(io_loop=self.ioloop)

        self.listen(9000)

        # this is for cross thread communication
        self.inport = Queue()
        self.outport = Queue()

        self._xdebug_connection = None

        def listenfunc():
            self.ioloop.make_current()
            self.ioloop.start()
            self.ioloop.close(all_fds=True)

        self.listener_thread = threading.Thread(target=listenfunc)
        self.listener_thread.daemon = True
        self.listener_thread.start()


    def handle_stream(self, stream, address):
        """Handle a connection

        Only one connection at a time, for now

        :stream: @todo
        :address: @todo
        :returns: @todo

        """
        self._xdebug_connection = XDebugConnection(self, stream, address)

    def run_command(self, command, data=None):
        """Send status
        :returns: @todo

        """
        self.inport.put("{} -i 1\0".format(str(command)))
        return self.outport.get()
        

    def stop(self):
        """Stop tornado event loop
        :returns: @todo

        """
        self.ioloop.stop()
        self.listener_thread.join()

        del self.ioloop
        del self.listener_thread

