import os
import sys
import select
import threading

from Queue import Queue


class XDebugConnection(object):
    """Represents a single connection from an XDebug session"""

    def __init__(self, stream, address):
        """Constructor """
        
        self._stream = stream
        self._address = address

        self._stream.set_close_callback(self._on_close)

        self._next_data_size = 0

    def process_response(self):
        """Process the commands and communication from Xdebug
        :returns: @todo

        """
        #print 'current thread: {}'.format(threading.current_thread())
        self._stream.read_until(b"\0", self._on_next_data_size)

    def send_command(self, command):
        """@todo: Docstring for process_commands.
        :returns: @todo

        """
        # not sure why calling process_response from here as callback causes a
        # segfault
        self._stream.write(command)

    def _on_next_data_size(self, datasize):
        """Get the size of the next data chunk

        :datasize: @todo
        :returns: @todo

        """
        self._next_data_size = int(datasize[:-1])
        print 'next data size is {}'.format(self._next_data_size)

        self._stream.read_until(b"\0", self._on_read_block)

    def _on_read_block(self, data):
        """Read the next block of data from xdebug

        :data: @todo
        :returns: @todo

        """
        print('Read {} bytes'.format(len(data[:-1]))) 
        print 'done'

    def _on_close(self):
        """The connection has closed
        :returns: @todo

        """
        print 'closing connection'

