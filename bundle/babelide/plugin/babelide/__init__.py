import os
import sys

from utils import install_virtual_env
from utils import install_package

class IDEManager(object):
    """Docstring for BabelIDE_Manager """

    def __init__(self):
        """@todo: Constructor """

    def init(self, babelide_basedir):
        """Initialize the plugin
        :returns: @todo

        """

        # check if the virtual env is setup
        if not os.path.exists(os.path.join(babelide_basedir, 'pyenv')):
            virtualenv_path = install_virtual_env( babelide_basedir )
            install_package(virtualenv_path, 'requests')

        

BabelIDE_Manager = IDEManager()
