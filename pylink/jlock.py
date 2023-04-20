# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Mar 30 2023, 01:25:49) 
# [GCC 12.2.1 20220924]
# Embedded file name: pylink/jlock.py
import psutil, errno, tempfile, os

class JLock(object):
    __doc__ = 'Lockfile for accessing a particular J-Link.\n\n    The J-Link SDK does not prevent accessing the same J-Link multiple times\n    from the same process or multiple processes.  As a result, a user can\n    have the same J-Link being accessed by multiple processes.  This class\n    provides an interface to a lock-file like structure for the physical\n    J-Links to ensure that any instance of a ``JLink`` with an open emulator\n    connection will be the only one accessing that emulator.\n\n    This class uses a PID-style lockfile to allow acquiring of the lockfile in\n    the instances where the lockfile exists, but the process which created it\n    is no longer running.\n\n    To share the same emulator connection between multiple threads, processes,\n    or functions, a single instance of a ``JLink`` should be created and passed\n    between the threads and processes.\n\n    Attributes:\n      name: the name of the lockfile.\n      path: full path to the lockfile.\n      fd: file description of the lockfile.\n      acquired: boolean indicating if the lockfile lock has been acquired.\n    '
    SERIAL_NAME_FMT = '.pylink-usb-{}.lck'
    IPADDR_NAME_FMT = '.pylink-ip-{}.lck'

    def __init__(self, serial_no):
        """Creates an instance of a ``JLock`` and populates the name.

        Note:
          This method may fail if there is no temporary directory in which to
          have the lockfile placed.

        Args:
          self (JLock): the ``JLock`` instance
          serial_no (int): the serial number of the J-Link

        Returns:
          ``None``
        """
        self.name = self.SERIAL_NAME_FMT.format(serial_no)
        self.acquired = False
        self.fd = None
        self.path = None
        self.path = os.path.join(tempfile.tempdir, self.name)

    def __del__(self):
        """Cleans up the lockfile instance if it was acquired.

        Args:
          self (JLock): the ``JLock`` instance

        Returns:
          ``None``
        """
        self.release()

    def acquire(self):
        """Attempts to acquire a lock for the J-Link lockfile.

        If the lockfile exists but does not correspond to an active process,
        the lockfile is first removed, before an attempt is made to acquire it.

        Args:
          self (Jlock): the ``JLock`` instance

        Returns:
          ``True`` if the lock was acquired, otherwise ``False``.

        Raises:
          OSError: on file errors.
        """
        if os.path.exists(self.path):
            try:
                pid = None
                with open(self.path, 'r') as f:
                    line = f.readline().strip()
                    pid = int(line)
                if not psutil.pid_exists(pid):
                    os.remove(self.path)
            except ValueError as e:
                try:
                    os.remove(self.path)
                finally:
                    e = None
                    del e

            except IOError as e:
                try:
                    pass
                finally:
                    e = None
                    del e

            try:
                self.fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_RDWR)
                to_write = '%s%s' % (os.getpid(), os.linesep)
                os.write(self.fd, to_write.encode())
            except OSError as e:
                try:
                    if not os.path.exists(self.path):
                        raise
                    return False
                finally:
                    e = None
                    del e

            self.acquired = True
            return True

    def release(self):
        """Cleans up the lockfile if it was acquired.

        Args:
          self (JLock): the ``JLock`` instance

        Returns:
          ``False`` if the lock was not released or the lock is not acquired,
          otherwise ``True``.
        """
        if not self.acquired:
            return False
        os.close(self.fd)
        if os.path.exists(self.path):
            os.remove(self.path)
        self.acquired = False
        return True
# okay decompiling ./pylink/jlock.pyc
