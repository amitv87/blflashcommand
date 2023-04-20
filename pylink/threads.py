# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Mar 30 2023, 01:25:49) 
# [GCC 12.2.1 20220924]
# Embedded file name: pylink/threads.py
import threading

class ThreadReturn(threading.Thread):
    __doc__ = 'Implementation of a thread with a return value.\n\n    See also:\n      `StackOverflow <http://stackoverflow.com/questions/6893968/>`__.\n    '

    def __init__(self, daemon=False, *args, **kwargs):
        """Initializes the thread.

        Args:
          self (ThreadReturn): the ``ThreadReturn`` instance
          daemon (bool): if the thread should be spawned as a daemon
          args: optional list of arguments
          kwargs: optional key-word arguments

        Returns:
          ``None``
        """
        (super(ThreadReturn, self).__init__)(*args, **kwargs)
        self.daemon = daemon
        self._return = None

    def run(self):
        """Runs the thread.

        Args:
          self (ThreadReturn): the ``ThreadReturn`` instance

        Returns:
          ``None``
        """
        target = getattr(self, '_Thread__target', getattr(self, '_target', None))
        args = getattr(self, '_Thread__args', getattr(self, '_args', None))
        kwargs = getattr(self, '_Thread__kwargs', getattr(self, '_kwargs', None))
        if target is not None:
            self._return = target(*args, **kwargs)

    def join(self, *args, **kwargs):
        (super(ThreadReturn, self).join)(*args, **kwargs)
        return self._return
# okay decompiling ./pylink/threads.pyc
