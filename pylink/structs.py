# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Mar 30 2023, 01:25:49) 
# [GCC 12.2.1 20220924]
# Embedded file name: pylink/structs.py
from . import enums
import ctypes

class JLinkConnectInfo(ctypes.Structure):
    __doc__ = 'J-Link connection info structure.\n\n    Attributes:\n      SerialNumber: J-Link serial number.\n      Connection: type of connection (e.g. ``enums.JLinkHost.USB``)\n      USBAddr: USB address if connected via USB.\n      aIPAddr: IP address if connected via IP.\n      Time: Time period (ms) after which UDP discover answer was received.\n      Time_us: Time period (uS) after which UDP discover answer was received.\n      HWVersion: Hardware version of J-Link, if connected via IP.\n      abMACAddr: MAC Address, if connected via IP.\n      acProduct: Product name, if connected via IP.\n      acNickname: Nickname, if connected via IP.\n      acFWString: Firmware string, if connected via IP.\n      IsDHCPAssignedIP: Is IP address reception via DHCP.\n      IsDHCPAssignedIPIsValid: True if connected via IP.\n      NumIPConnections: Number of IP connections currently established.\n      NumIPConnectionsIsValid: True if connected via IP.\n      aPadding: Bytes reserved for future use.\n    '
    _fields_ = [
     (
      'SerialNumber', ctypes.c_uint32),
     (
      'Connection', ctypes.c_ubyte),
     (
      'USBAddr', ctypes.c_uint32),
     (
      'aIPAddr', ctypes.c_uint8 * 16),
     (
      'Time', ctypes.c_int),
     (
      'Time_us', ctypes.c_uint64),
     (
      'HWVersion', ctypes.c_uint32),
     (
      'abMACAddr', ctypes.c_uint8 * 6),
     (
      'acProduct', ctypes.c_char * 32),
     (
      'acNickname', ctypes.c_char * 32),
     (
      'acFWString', ctypes.c_char * 112),
     (
      'IsDHCPAssignedIP', ctypes.c_char),
     (
      'IsDHCPAssignedIPIsValid', ctypes.c_char),
     (
      'NumIPConnections', ctypes.c_char),
     (
      'NumIPConnectionsIsValid', ctypes.c_char),
     (
      'aPadding', ctypes.c_uint8 * 34)]

    def __repr__(self):
        """Returns a representation of this class.

        Args:
          self (JLinkConnectInfo): the ``JlinkConnectInfo`` instance

        Returns:
          String representation of the class.
        """
        return 'JLinkConnectInfo(%s)' % self.__str__()

    def __str__(self):
        """Returns a string representation of the connection info.

        Args:
          self (JLinkConnectInfo): the ``JLinkConnectInfo`` instance

        Returns:
          String specifying the product, its serial number, and the type of
          connection that it has (one of USB or IP).
        """
        conn = 'USB' if self.Connection == 1 else 'IP'
        return '%s <Serial No. %s, Conn. %s>' % (self.acProduct.decode(), self.SerialNumber, conn)


class JLinkFlashArea(ctypes.Structure):
    __doc__ = 'Definition for a region of Flash.\n\n    Attributes:\n      Addr: address where the flash area starts.\n      Size: size of the flash area.\n    '
    _fields_ = [
     (
      'Addr', ctypes.c_uint32),
     (
      'Size', ctypes.c_uint32)]

    def __repr__(self):
        """Returns a representation of the instance.

        Args:
          self (FlashArea): the ``FlashArea`` instance

        Returns:
          String representation of the Flash Area.
        """
        return '%s(%s)' % (self.__class__.__name__, self.__str__())

    def __str__(self):
        """Returns a string representation of the instance.

        Args:
          self (FlashArea): the ``FlashArea`` instance

        Returns:
          String specifying address of flash region, and its size.
        """
        return 'Address = 0x%x, Size = %s' % (self.Addr, self.Size)


class JLinkRAMArea(JLinkFlashArea):
    __doc__ = 'Definition for a region of RAM.\n\n    Attributes:\n      Addr: address where the flash area starts.\n      Size: size of the flash area.\n    '


class JLinkDeviceInfo(ctypes.Structure):
    __doc__ = 'J-Link device information.\n\n    This structure is used to represent a device that is supported by the\n    J-Link.\n\n    Attributes:\n      SizeOfStruct: Size of the struct (DO NOT CHANGE).\n      sName: name of the device.\n      CoreId: core identifier of the device.\n      FlashAddr: base address of the internal flash of the device.\n      RAMAddr: base address of the internal RAM of the device.\n      EndianMode: the endian mode of the device (0 -> only little endian,\n          1 -> only big endian, 2 -> both).\n      FlashSize: total flash size in bytes.\n      RAMSize: total RAM size in bytes.\n      sManu: device manufacturer.\n      aFlashArea: a list of ``JLinkFlashArea`` instances.\n      aRamArea: a list of ``JLinkRAMArea`` instances.\n      Core: CPU core.\n    '
    _fields_ = [
     (
      'SizeofStruct', ctypes.c_uint32),
     (
      'sName', ctypes.POINTER(ctypes.c_char)),
     (
      'CoreId', ctypes.c_uint32),
     (
      'FlashAddr', ctypes.c_uint32),
     (
      'RAMAddr', ctypes.c_uint32),
     (
      'EndianMode', ctypes.c_char),
     (
      'FlashSize', ctypes.c_uint32),
     (
      'RAMSize', ctypes.c_uint32),
     (
      'sManu', ctypes.POINTER(ctypes.c_char)),
     (
      'aFlashArea', JLinkFlashArea * 32),
     (
      'aRAMArea', JLinkRAMArea * 32),
     (
      'Core', ctypes.c_uint32)]

    def __init__(self, *args, **kwargs):
        (super(JLinkDeviceInfo, self).__init__)(*args, **kwargs)
        self.SizeofStruct = ctypes.sizeof(self)

    def __repr__(self):
        """Returns a representation of this instance.

        Args:
          self (JLinkDeviceInfo): the ``JLinkDeviceInfo`` instance

        Returns:
          Returns a string representation of the instance.
        """
        return 'JLinkDeviceInfo(%s)' % self.__str__()

    def __str__(self):
        """Returns a string representation of this instance.

        Args:
          self (JLinkDeviceInfo): the ``JLinkDeviceInfo`` instance

        Returns:
          Returns a string specifying the device name, core, and manufacturer.
        """
        manu = self.manufacturer
        return '%s <Core Id. %s, Manu. %s>' % (self.name, self.Core, manu)

    @property
    def name(self):
        """Returns the name of the device.

        Args:
          self (JLinkDeviceInfo): the ``JLinkDeviceInfo`` instance

        Returns:
          Device name.
        """
        return ctypes.cast(self.sName, ctypes.c_char_p).value.decode()

    @property
    def manufacturer(self):
        """Returns the name of the manufacturer of the device.

        Args:
          self (JLinkDeviceInfo): the ``JLinkDeviceInfo`` instance

        Returns:
          Manufacturer name.
        """
        buf = ctypes.cast(self.sManu, ctypes.c_char_p).value
        if buf:
            return buf.decode()


class JLinkHardwareStatus(ctypes.Structure):
    __doc__ = 'Definition for the hardware status information for a J-Link.\n\n    Attributes:\n      VTarget: target supply voltage.\n      tck: measured state of TCK pin.\n      tdi: measured state of TDI pin.\n      tdo: measured state of TDO pin.\n      tms: measured state of TMS pin.\n      tres: measured state of TRES pin.\n      trst: measured state of TRST pin.\n    '
    _fields_ = [
     (
      'VTarget', ctypes.c_uint16),
     (
      'tck', ctypes.c_uint8),
     (
      'tdi', ctypes.c_uint8),
     (
      'tdo', ctypes.c_uint8),
     (
      'tms', ctypes.c_uint8),
     (
      'tres', ctypes.c_uint8),
     (
      'trst', ctypes.c_uint8)]

    def __repr__(self):
        """Returns a string representation of the instance.

        Args:
          self (JLinkHardwareStatus): the ``JlinkHardwareStatus`` instance

        Returns:
          String representation of the instance.
        """
        return '%s(VTarget=%dmV)' % (self.__class__.__name__, self.voltage)

    @property
    def voltage(self):
        """Returns the target supply voltage.

        This is an alias for ``.VTarget``.

        Args:
          self (JLInkHardwareStatus): the ``JLinkHardwareStatus`` instance

        Returns:
          Target supply voltage as an integer.
        """
        return self.VTarget


class JLinkGPIODescriptor(ctypes.Structure):
    __doc__ = 'Definition for the structure that details the name and capabilities of a\n    user-controllable GPIO.\n\n    Attributes:\n      acName: name of the GPIO.\n      Caps: bitfield of capabilities.\n    '
    _fields_ = [
     (
      'acName', ctypes.c_char * 32),
     (
      'Caps', ctypes.c_uint32)]

    def __repr__(self):
        """Returns a string representation of the instance.

        Args:
          self (JLinkGPIODescriptor): the ``JLinkGPIODescriptor`` instance

        Returns:
          String representation of the instance.
        """
        return '%s(%s)' % (self.__class__.__name__, self.__str__())

    def __str__(self):
        """Returns the GPIO name.

        Args:
          self (JLinkGPIODescriptor): the ``JLInkGPIODescriptor`` instance

        Returns:
          GPIO name.
        """
        return self.acName.decode()


class JLinkMemoryZone(ctypes.Structure):
    __doc__ = 'Represents a CPU memory zone.\n\n    Attributes:\n      sName: initials of the memory zone.\n      sDesc: name of the memory zone.\n      VirtAddr: start address of the virtual address space of the memory zone.\n      abDummy: reserved for future use.\n    '
    _fields_ = [
     (
      'sName', ctypes.c_char_p),
     (
      'sDesc', ctypes.c_char_p),
     (
      'VirtAddr', ctypes.c_uint64),
     (
      'abDummy', ctypes.c_uint8 * 16)]

    def __repr__(self):
        """Returns a string representation of the instance

        Args:
          self: the ``JLinkMemoryZone`` instance

        Returns:
          String representation of the instance.
        """
        return '%s(%s)' % (self.__class__.__name__, self.__str__())

    def __str__(self):
        """Returns a formatted string describing the memory zone.

        Args:
          self: the ``JLinkMemoryZone`` instance

        Returns:
          String representation of the memory zone.
        """
        return '%s <Desc. %s, VirtAddr. 0x%x>' % (self.sName, self.sDesc, self.VirtAddr)

    @property
    def name(self):
        """Alias for the memory zone name.

        Args:
          self (JLinkMemoryZone): the ``JLinkMemoryZone`` instance

        Returns:
          The memory zone name.
        """
        return self.sName


class JLinkSpeedInfo(ctypes.Structure):
    __doc__ = "Represents information about an emulator's supported speeds.\n\n    The emulator can support all target interface speeds calculated by dividing\n    the base frequency by atleast ``MinDiv``.\n\n    Attributes:\n      SizeOfStruct: the size of this structure.\n      BaseFreq: Base frequency (in HZ) used to calculate supported speeds.\n      MinDiv: minimum divider allowed to divide the base frequency.\n      SupportAdaptive: ``1`` if emulator supports adaptive clocking, otherwise\n          ``0``.\n    "
    _fields_ = [
     (
      'SizeOfStruct', ctypes.c_uint32),
     (
      'BaseFreq', ctypes.c_uint32),
     (
      'MinDiv', ctypes.c_uint16),
     (
      'SupportAdaptive', ctypes.c_uint16)]

    def __init__(self):
        super(JLinkSpeedInfo, self).__init__()
        self.SizeOfStruct = ctypes.sizeof(self)

    def __repr__(self):
        """Returns a string representation of the instance.

        Args:
          self (JLinkSpeedInfo): the ``JLinkSpeedInfo`` instance

        Returns:
          String representation of the instance.
        """
        return self.__str__()

    def __str__(self):
        """Returns this instance formatted as a string.

        Args:
          self (JLinkSpeedInfo): the ``JLinkSpeedInfo`` instance

        Returns:
          String formatted instance.
        """
        return '%s(Freq=%sHz)' % (self.__class__.__name__, self.BaseFreq)


class JLinkSWOStartInfo(ctypes.Structure):
    __doc__ = 'Represents configuration information for collecting Serial Wire Output\n    (SWO) information.\n\n    Attributes:\n      SizeofStruct: size of the structure.\n      Interface: the interface type used for SWO.\n      Speed: the frequency used for SWO communication in Hz.\n\n    Note:\n      You should *never* change ``.SizeofStruct`` or ``.Interface``.\n    '
    _fields_ = [
     (
      'SizeofStruct', ctypes.c_uint32),
     (
      'Interface', ctypes.c_uint32),
     (
      'Speed', ctypes.c_uint32)]

    def __init__(self):
        super(JLinkSWOStartInfo, self).__init__()
        self.SizeofStruct = ctypes.sizeof(self)
        self.Interface = enums.JLinkSWOInterfaces.UART

    def __repr__(self):
        """Returns a representation of this instance.

        Args:
          self (JLinkSWOStartInfo): the ``JLinkSWOStartInfo`` instance

        Returns:
          The string representation of this instance.
        """
        return self.__str__()

    def __str__(self):
        """Returns a string representation of this instance.

        Args:
          self (JLinkSWOStartInfo): the ``JLinkSWOStartInfo`` instance

        Returns:
          The string representation of this instance.
        """
        return '%s(Speed=%sHz)' % (self.__class__.__name__, self.Speed)


class JLinkSWOSpeedInfo(ctypes.Structure):
    __doc__ = "Structure representing information about target's supported SWO speeds.\n\n    To calculate the supported SWO speeds, the base frequency is taken and\n    divide by a number in the range of ``[ MinDiv, MaxDiv ]``.\n\n    Attributes:\n      SizeofStruct: size of the structure.\n      Interface: interface type for the speed information.\n      BaseFreq: base frequency (Hz) used to calculate supported SWO speeds.\n      MinDiv: minimum divider allowed to divide the base frequency.\n      MaxDiv: maximum divider allowed to divide the base frequency.\n      MinPrescale: minimum prescaler allowed to adjust the base frequency.\n      MaxPrescale: maximum prescaler allowed to adjust the base frequency.\n\n    Note:\n      You should *never* change ``.SizeofStruct`` or ``.Interface``.\n    "
    _fields_ = [
     (
      'SizeofStruct', ctypes.c_uint32),
     (
      'Interface', ctypes.c_uint32),
     (
      'BaseFreq', ctypes.c_uint32),
     (
      'MinDiv', ctypes.c_uint32),
     (
      'MaxDiv', ctypes.c_uint32),
     (
      'MinPrescale', ctypes.c_uint32),
     (
      'MaxPrescale', ctypes.c_uint32)]

    def __init__(self):
        super(JLinkSWOSpeedInfo, self).__init__()
        self.SizeofStruct = ctypes.sizeof(self)
        self.Interface = enums.JLinkSWOInterfaces.UART

    def __repr__(self):
        """Returns a representation of the instance.

        Args:
          self (JLinkSWOSpeedInfo): the ``JLinkSWOSpeedInfo`` instance

        Returns:
          ``None``
        """
        return self.__str__()

    def __str__(self):
        """Returns a string representaton of the instance.

        Args:
          self (JLinkSWOSpeedInfo): the ``JLinkSWOSpeedInfo`` instance

        Returns:
          ``None``
        """
        return '%s(Interface=UART, Freq=%sHz)' % (self.__class__.__name__, self.BaseFreq)


class JLinkMOEInfo(ctypes.Structure):
    __doc__ = 'Structure representing the Method of Debug Entry (MOE).\n\n    The method of debug entry is a reason for which a CPU has stopped.  At any\n    given time, there may be multiple methods of debug entry.\n\n    Attributes:\n      HaltReason: reason why the CPU stopped.\n      Index: if cause of CPU stop was a code/data breakpoint, this identifies\n        the index of the code/data breakpoint unit which causes the CPU to\n        stop, otherwise it is ``-1``.\n    '
    _fields_ = [
     (
      'HaltReason', ctypes.c_uint32),
     (
      'Index', ctypes.c_int)]

    def __repr__(self):
        """Returns a string representation of the instance.

        Args:
          self (JLinkMOEInfo): the ``JLinkMOEInfo`` instance

        Returns:
          A string representation of the instance.
        """
        return '%s(%s)' % (self.__class__.__name__, self.__str__())

    def __str__(self):
        """Returns a string representation of the instance.

        Args:
          self (JLinkMOEInfo): the ``JLinkMOEInfo`` instance

        Returns:
          A string representation of the instance.
        """
        d = enums.JLinkHaltReasons.__dict__
        s = next((k for k, v in d.items() if v == self.HaltReason))
        if self.dbgrq():
            return s
        return s.replace('_', ' ').title()

    def dbgrq(self):
        """Returns whether this a DBGRQ.

        Args:
          self (JLinkMOEInfo): the ``JLinkMOEInfo`` instance

        Returns:
          ``True`` if this is a DBGRQ, otherwise ``False``.
        """
        return self.HaltReason == enums.JLinkHaltReasons.DBGRQ

    def code_breakpoint(self):
        """Returns whether this a code breakpoint.

        Args:
          self (JLinkMOEInfo): the ``JLinkMOEInfo`` instance

        Returns:
          ``True`` if this is a code breakpoint, otherwise ``False``.
        """
        return self.HaltReason == enums.JLinkHaltReasons.CODE_BREAKPOINT

    def data_breakpoint(self):
        """Returns whether this a data breakpoint.

        Args:
          self (JLinkMOEInfo): the ``JLinkMOEInfo`` instance

        Returns:
          ``True`` if this is a data breakpoint, otherwise ``False``.
        """
        return self.HaltReason == enums.JLinkHaltReasons.DATA_BREAKPOINT

    def vector_catch(self):
        """Returns whether this a vector catch.

        Args:
          self (JLinkMOEInfo): the ``JLinkMOEInfo`` instance

        Returns:
          ``True`` if this is a vector catch, otherwise ``False``.
        """
        return self.HaltReason == enums.JLinkHaltReasons.VECTOR_CATCH


class JLinkBreakpointInfo(ctypes.Structure):
    __doc__ = 'Class representing information about a breakpoint.\n\n    Attributes:\n      SizeOfStruct: the size of the structure (this should not be modified).\n      Handle: breakpoint handle.\n      Addr: address of where the breakpoint has been set.\n      Type: type flags which were specified when the breakpoint was created.\n      ImpFlags: describes the current state of the breakpoint.\n      UseCnt: describes how often the breakpoint is set at the same address.\n    '
    _fields_ = [
     (
      'SizeOfStruct', ctypes.c_uint32),
     (
      'Handle', ctypes.c_uint32),
     (
      'Addr', ctypes.c_uint32),
     (
      'Type', ctypes.c_uint32),
     (
      'ImpFlags', ctypes.c_uint32),
     (
      'UseCnt', ctypes.c_uint32)]

    def __init__(self):
        super(JLinkBreakpointInfo, self).__init__()
        self.SizeOfStruct = ctypes.sizeof(self)

    def __repr__(self):
        """Returns a formatted string describing the breakpoint.

        Args:
          self (JLinkBreakpointInfo): the ``JLinkBreakpointInfo`` instance

        Returns:
          Stirng representation of the breakpoint.
        """
        return self.__str__()

    def __str__(self):
        """Returns a formatted string describing the breakpoint.

        Args:
          self (JLinkBreakpointInfo): the ``JLinkBreakpointInfo`` instance

        Returns:
          Stirng representation of the breakpoint.
        """
        name = self.__class__.__name__
        return '%s(Handle %d, Address %d)' % (name, self.Handle, self.Addr)

    def software_breakpoint(self):
        """Returns whether this is a software breakpoint.

        Args:
          self (JLinkBreakpointInfo): the ``JLinkBreakpointInfo`` instance

        Returns:
          ``True`` if the breakpoint is a software breakpoint, otherwise
          ``False``.
        """
        software_types = [
         enums.JLinkBreakpoint.SW_RAM,
         enums.JLinkBreakpoint.SW_FLASH,
         enums.JLinkBreakpoint.SW]
        return any((self.Type & stype for stype in software_types))

    def hardware_breakpoint(self):
        """Returns whether this is a hardware breakpoint.

        Args:
          self (JLinkBreakpointInfo): the ``JLinkBreakpointInfo`` instance

        Returns:
          ``True`` if the breakpoint is a hardware breakpoint, otherwise
          ``False``.
        """
        return self.Type & enums.JLinkBreakpoint.HW

    def pending(self):
        """Returns if this breakpoint is pending.

        Args:
          self (JLinkBreakpointInfo): the ``JLinkBreakpointInfo`` instance

        Returns:
          ``True`` if the breakpoint is still pending, otherwise ``False``.
        """
        return self.ImpFlags & enums.JLinkBreakpointImplementation.PENDING


class JLinkDataEvent(ctypes.Structure):
    __doc__ = 'Class representing a data event.\n\n    A data may halt the CPU, trigger SWO output, or trigger trace output.\n\n    Attributes:\n      SizeOfStruct: the size of the structure (this should not be modified).\n      Type: the type of the data event (this should not be modified).\n      Addr: the address on which the watchpoint was set\n      AddrMask: the address mask used for comparision.\n      Data: the data on which the watchpoint has been set.\n      DataMask: the data mask used for comparision.\n      Access: the control data on which the event has been set.\n      AccessMask: the control mask used for comparison.\n    '
    _fields_ = [
     (
      'SizeOfStruct', ctypes.c_int),
     (
      'Type', ctypes.c_int),
     (
      'Addr', ctypes.c_uint32),
     (
      'AddrMask', ctypes.c_uint32),
     (
      'Data', ctypes.c_uint32),
     (
      'DataMask', ctypes.c_uint32),
     (
      'Access', ctypes.c_uint8),
     (
      'AccessMask', ctypes.c_uint8)]

    def __init__(self):
        super(JLinkDataEvent, self).__init__()
        self.SizeOfStruct = ctypes.sizeof(self)
        self.Type = enums.JLinkEventTypes.BREAKPOINT

    def __repr__(self):
        """Returns a string representation of the data event.

        Args:
          self (JLinkDataEvent): the ``JLinkDataEvent`` instance

        Returns:
          A string representation of the data event.
        """
        return self.__str__()

    def __str__(self):
        """Returns a string representation of the data event.

        Args:
          self (JLinkDataEvent): the ``JLinkDataEvent`` instance

        Returns:
          A string representation of the data event.
        """
        name = self.__class__.__name__
        return '%s(Type %d, Address %d)' % (name, self.Type, self.Addr)


class JLinkWatchpointInfo(ctypes.Structure):
    __doc__ = 'Class representing information about a watchpoint.\n\n    Attributes:\n      SizeOfStruct: the size of the structure (this should not be modified).\n      Handle: the watchpoint handle.\n      Addr: the address the watchpoint was set at.\n      AddrMask: the address mask used for comparison.\n      Data: the data on which the watchpoint was set.\n      DataMask: the data mask used for comparision.\n      Ctrl: the control data on which the breakpoint was set.\n      CtrlMask: the control mask used for comparison.\n      WPUnit: the index of the watchpoint unit.\n    '
    _fields_ = [
     (
      'SizeOfStruct', ctypes.c_uint32),
     (
      'Handle', ctypes.c_uint32),
     (
      'Addr', ctypes.c_uint32),
     (
      'AddrMask', ctypes.c_uint32),
     (
      'Data', ctypes.c_uint32),
     (
      'DataMask', ctypes.c_uint32),
     (
      'Ctrl', ctypes.c_uint32),
     (
      'CtrlMask', ctypes.c_uint32),
     (
      'WPUnit', ctypes.c_uint8)]

    def __init__(self):
        super(JLinkWatchpointInfo, self).__init__()
        self.SizeOfStruct = ctypes.sizeof(self)

    def __repr__(self):
        """Returns a formatted string describing the watchpoint.

        Args:
          self (JLinkWatchpointInfo): the ``JLinkWatchpointInfo`` instance

        Returns:
          String representation of the watchpoint.
        """
        return self.__str__()

    def __str__(self):
        """Returns a formatted string describing the watchpoint.

        Args:
          self (JLinkWatchpointInfo): the ``JLinkWatchpointInfo`` instance

        Returns:
          String representation of the watchpoint.
        """
        name = self.__class__.__name__
        return '%s(Handle %d, Address %d)' % (name, self.Handle, self.Addr)


class JLinkStraceEventInfo(ctypes.Structure):
    __doc__ = 'Class representing the STRACE event information.\n\n    Attributes:\n      SizeOfStruct: size of the structure.\n      Type: type of event.\n      Op: the STRACE operation to perform.\n      AccessSize: access width for trace events.\n      Reserved0: reserved.\n      Addr: specifies the load/store address for data.\n      Data: the data to be compared for the operation for data access events.\n      DataMask: bitmask for bits of data to omit in comparision for data access\n        events.\n      AddrRangeSize: address range for range events.\n    '
    _fields_ = [
     (
      'SizeOfStruct', ctypes.c_uint32),
     (
      'Type', ctypes.c_uint8),
     (
      'Op', ctypes.c_uint8),
     (
      'AccessSize', ctypes.c_uint8),
     (
      'Reserved0', ctypes.c_uint8),
     (
      'Addr', ctypes.c_uint64),
     (
      'Data', ctypes.c_uint64),
     (
      'DataMask', ctypes.c_uint64),
     (
      'AddrRangeSize', ctypes.c_uint32)]

    def __init__(self):
        super(JLinkStraceEventInfo, self).__init__()
        self.SizeOfStruct = ctypes.sizeof(self)

    def __repr__(self):
        """Returns a formatted string describing the event info.

        Args:
          self (JLinkStraceEventInfo): the ``JLinkStraceEventInfo`` instance

        Returns:
          String representation of the event info.
        """
        return self.__str__()

    def __str__(self):
        """Returns a formatted string describing the event info.

        Args:
          self (JLinkStraceEventInfo): the ``JLinkStraceEventInfo`` instance

        Returns:
          String representation of the event information.
        """
        name = self.__class__.__name__
        return '%s(Type=%d, Op=%d)' % (name, self.Type, self.Op)


class JLinkTraceData(ctypes.Structure):
    __doc__ = 'Structure representing trace data returned by the trace buffer.\n\n    Attributes:\n      PipeStat: type of trace data.\n      Sync: sync point in buffer.\n      Packet: trace data packet.\n    '
    _fields_ = [
     (
      'PipeStat', ctypes.c_uint8),
     (
      'Sync', ctypes.c_uint8),
     (
      'Packet', ctypes.c_uint16)]

    def __repr__(self):
        """Returns a string representation of the trace data instance.

        Args:
          self (JLinkTraceData): the ``JLinkTraceData`` instance.

        Returns:
          A string representation of the instance.
        """
        return self.__str__()

    def __str__(self):
        """Returns a string representation of the trace data instance.

        Args:
          self (JLinkTraceData): the ``JLinkTraceData`` instance.

        Returns:
          A string representation of the instance.
        """
        return '%s(%d)' % (self.__class__.__name__, self.Packet)

    def instruction(self):
        """Returns whether the data corresponds to an executed instruction.

        Args:
          self (JLinkTraceData): the ``JLinkTraceData`` instance.

        Returns:
          ``True`` if this is trace data for an executed instruction.
        """
        return self.PipeStat == 0

    def data_instruction(self):
        """Returns whether the data corresponds to an data instruction.

        Args:
          self (JLinkTraceData): the ``JLinkTraceData`` instance.

        Returns:
          ``True`` if this is trace data for an data instruction.
        """
        return self.PipeStat == 1

    def non_instruction(self):
        """Returns whether the data corresponds to an un-executed instruction.

        Args:
          self (JLinkTraceData): the ``JLinkTraceData`` instance.

        Returns:
          ``True`` if this is trace data for an un-executed instruction.
        """
        return self.PipeStat == 2

    def wait(self):
        """Returns whether the data corresponds to a wait.

        Args:
          self (JLinkTraceData): the ``JLinkTraceData`` instance.

        Returns:
          ``True`` if this is trace data for a wait.
        """
        return self.PipeStat == 3

    def branch(self):
        """Returns whether the data corresponds to a branch execution.

        Args:
          self (JLinkTraceData): the ``JLinkTraceData`` instance.

        Returns:
          ``True`` if this is trace data for a branch execution.
        """
        return self.PipeStat == 4

    def data_branch(self):
        """Returns whether the data corresponds to a branch with data.

        Args:
          self (JLinkTraceData): the ``JLinkTraceData`` instance.

        Returns:
          ``True`` if this is trace data for a branch with data.
        """
        return self.PipeStat == 5

    def trigger(self):
        """Returns whether the data corresponds to a trigger event.

        Args:
          self (JLinkTraceData): the ``JLinkTraceData`` instance.

        Returns:
          ``True`` if this is trace data for a trigger event.
        """
        return self.PipeStat == 6

    def trace_disabled(self):
        """Returns whether the data corresponds to trace being disabled.

        Args:
          self (JLinkTraceData): the ``JLinkTraceData`` instance.

        Returns:
          ``True`` if this is trace data for the trace disabled event.
        """
        return self.PipeStat == 7


class JLinkTraceRegion(ctypes.Structure):
    __doc__ = 'Structure describing a trace region.\n\n    Attributes:\n      SizeOfStruct: size of the structure.\n      RegionIndex: index of the region.\n      NumSamples: number of samples in the region.\n      Off: offset in the trace buffer.\n      RegionCnt: number of trace regions.\n      Dummy: unused.\n      Timestamp: timestamp of last event written to buffer.\n    '
    _fields_ = [
     (
      'SizeOfStruct', ctypes.c_uint32),
     (
      'RegionIndex', ctypes.c_uint32),
     (
      'NumSamples', ctypes.c_uint32),
     (
      'Off', ctypes.c_uint32),
     (
      'RegionCnt', ctypes.c_uint32),
     (
      'Dummy', ctypes.c_uint32),
     (
      'Timestamp', ctypes.c_uint64)]

    def __init__(self):
        super(JLinkTraceRegion, self).__init__()
        self.SizeOfStruct = ctypes.sizeof(self)

    def __repr__(self):
        """Returns a string representation of the instance.

        Args:
          self (JLinkTraceRegion): the ``JLinkTraceRegion`` instance.

        Returns:
          String representation of the trace region.
        """
        return self.__str__()

    def __str__(self):
        """Returns a string representation of the instance.

        Args:
          self (JLinkTraceRegion): the ``JLinkTraceRegion`` instance.

        Returns:
          String representation of the trace region.
        """
        return '%s(Index=%d)' % (self.__class__.__name__, self.RegionIndex)
# okay decompiling ./pylink/structs.pyc
