import os
import sys
import select
import threading
import re

from Queue import Queue
from lxml import etree
from lxml import objectify


class XDebugConnection(object):
    """Represents a single connection from an XDebug session"""

    def __init__(self, server, stream, address):
        """Constructor """
        
        self._server = server
        self._stream = stream
        self._address = address

        self._stream.set_close_callback(self._on_close)

        self._init_data = None

        self._next_data_size = 0
        self._process_response()

    def _process_response(self):
        """Process the commands and communication from Xdebug
        :returns: @todo

        """
        self._stream.read_until(b"\0", self._on_next_data_size)

    def _send_command(self, command):
        """@todo: Docstring for process_commands.
        :returns: @todo

        """
        self._stream.write(command, self._process_response)

    def _on_next_data_size(self, datasize):
        """Get the size of the next data chunk

        :datasize: @todo
        :returns: @todo

        """
        self._next_data_size = int(datasize[:-1])

        self._stream.read_until(b"\0", self._on_read_block)

    def _on_read_block(self, data):
        """Read the next block of data from xdebug

        :data: @todo
        :returns: @todo

        """
        # remove the namespace
        clean_xml = re.sub(' xmlns="[^"]+"', '', data[:-1], count=1)

        root = objectify.fromstring(clean_xml)
        etree.cleanup_namespaces(root)
        if root.tag == 'init':
            # here we will process init data
            self._init_data = root
        else:
            self._server.outport.put(root)

        next_command = self._server.inport.get()
        self._send_command(next_command)

    def _on_close(self):
        """The connection has closed
        :returns: @todo

        """
        #print 'closing connection'

