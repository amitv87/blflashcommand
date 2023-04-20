# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Mar 30 2023, 01:25:49) 
# [GCC 12.2.1 20220924]
# Embedded file name: pylink/decorators.py
from . import threads
import functools

def async_decorator(func):
    """Asynchronous function decorator.  Interprets the function as being
    asynchronous, so returns a function that will handle calling the
    Function asynchronously.

    Args:
      func (function): function to be called asynchronously

    Returns:
      The wrapped function.

    Raises:
      AttributeError: if ``func`` is not callable
    """

    @functools.wraps(func)
    def async_wrapper(*args, **kwargs):
        if not ('callback' not in kwargs or kwargs['callback']):
            return func(*args, **kwargs)
        callback = kwargs.pop('callback')
        if not callable(callback):
            raise TypeError("Expected 'callback' is not callable.")

        def thread_func(*args, **kwargs):
            exception, res = (None, None)
            try:
                res = func(*args, **kwargs)
            except Exception as e:
                try:
                    exception = e
                finally:
                    e = None
                    del e

            return callback(exception, res)

        thread = threads.ThreadReturn(target=thread_func, args=args,
          kwargs=kwargs)
        thread.daemon = True
        thread.start()
        return thread

    return async_wrapper
# okay decompiling ./pylink/decorators.pyc
