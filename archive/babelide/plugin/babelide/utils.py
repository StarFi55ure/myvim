import os
import sys
import random
import subprocess
import socket
import errno



'''
=====================================================
These functions manage the virtual env
=====================================================
'''

_pip_bin = 'pip'
_pyenv_name = 'pyenv'


def install_virtual_env(root_dir):

    print 'Installing virtualenv'
    print 'Root dir: ', root_dir

    _virtualenv_path = os.path.join(root_dir, _pyenv_name)

    proc = subprocess.Popen(
            ['virtualenv',
                '--python=python',
                _virtualenv_path])
    proc.wait()
    print 'Virtual env installed'

    return _virtualenv_path



def install_package(virtualenv_path, package_name):
    '''
    Might not be used in the future
    '''
    pass
    

def random_string():
    """Return a randomly generated string

    :length: @todo
    :returns: @todo

    """
    return '%030x' % random.randrange(16**30)

def writebuf(buf, msg):
    '''
    Write a string to the end of the buffer
    '''
    buf[len(buf):] = [msg]

def wait_net_service(server, port, timeout=None):
    """ Wait for network service to appear 
        @param timeout: in seconds, if None or 0 wait forever
        @return: True of False, if timeout is None may return only True or
                 throw unhandled network exception

        cut-and-paste from: 

        http://code.activestate.com/recipes/576655-wait-for-network-service-to-appear/
    """
    s = socket.socket()
    if timeout:
        from time import time as now
        # time module is needed to calc timeout shared between two exceptions
        end = now() + timeout

    while True:
        try:
            if timeout:
                next_timeout = end - now()
                if next_timeout < 0:
                    return False
                else:
            	    s.settimeout(next_timeout)
            
            s.connect((server, port))
        
        except socket.timeout, err:
            # this exception occurs only if timeout is set
            if timeout:
                return False
      
        except socket.error, err:
            # catch timeout exception from underlying network library
            # this one is different from socket.timeout
            if type(err.args) != tuple or err[0] != errno.ETIMEDOUT:
                continue
        else:
            s.close()
            return True
