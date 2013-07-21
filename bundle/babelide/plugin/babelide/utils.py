import os
import sys
import random
import subprocess


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
