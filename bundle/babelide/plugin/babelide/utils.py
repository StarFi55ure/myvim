import os
import sys
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
    
    pip_exe = os.path.join(virtualenv_path, 'bin', _pip_bin);

    print 'using pip_exe ', pip_exe
    proc = subprocess.Popen(
            [pip_exe,
                'install',
                package_name])
    proc.wait()


