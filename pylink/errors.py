# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Mar 30 2023, 01:25:49) 
# [GCC 12.2.1 20220924]
# Embedded file name: pylink/errors.py
from . import enums
from . import util

class JLinkException(enums.JLinkGlobalErrors, Exception):
    __doc__ = 'Generic J-Link exception.'

    def __init__(self, code):
        message = code
        self.code = None
        if util.is_integer(code):
            message = self.to_string(code)
            self.code = code
        super(JLinkException, self).__init__(message)
        self.message = message


class JLinkEraseException(enums.JLinkEraseErrors, JLinkException):
    __doc__ = 'J-Link erase exception.'


class JLinkFlashException(enums.JLinkFlashErrors, JLinkException):
    __doc__ = 'J-Link flash exception.'


class JLinkWriteException(enums.JLinkWriteErrors, JLinkException):
    __doc__ = 'J-Link write exception.'


class JLinkReadException(enums.JLinkReadErrors, JLinkException):
    __doc__ = 'J-Link read exception.'


class JLinkDataException(enums.JLinkDataErrors, JLinkException):
    __doc__ = 'J-Link data event exception.'


class JLinkRTTException(enums.JLinkRTTErrors, JLinkException):
    __doc__ = 'J-Link RTT exception.'
# okay decompiling ./pylink/errors.pyc
