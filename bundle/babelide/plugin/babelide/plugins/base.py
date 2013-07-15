import os
import os.path as osp
import sys

def expose(func, *args, **kwargs):
    ''' Decorator to mark a method as exposed to the outside world'''
    func.__exposed__ = True 

    return func


class BabelIDE_Plugin(object):
    """Base class for BabelIDE plugins"""

    def __init__(self):
        """Constructor """
        pass
