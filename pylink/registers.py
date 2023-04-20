# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Mar 30 2023, 01:25:49) 
# [GCC 12.2.1 20220924]
# Embedded file name: pylink/registers.py
import ctypes

class IDCodeRegisterBits(ctypes.LittleEndianStructure):
    __doc__ = 'This class holds the different bit masks for the IDCode register.\n\n    Attributes:\n      valid: validity bit, should always be ``0``.\n      manufactuer: the JEDEC Manufacturer ID.\n      part_no: the part number defined by the manufacturer.\n      version_code: the version code.\n    '
    _fields_ = [
     (
      'valid', ctypes.c_uint32, 1),
     (
      'manufacturer', ctypes.c_uint32, 11),
     (
      'part_no', ctypes.c_uint32, 16),
     (
      'version_code', ctypes.c_uint32, 4)]


class IDCodeRegisterFlags(ctypes.Union):
    __doc__ = 'Mask for the IDCode register bits.\n\n    Attributes:\n      value: the value stored in the mask.\n    '
    _anonymous_ = ('bit', )
    _fields_ = [
     (
      'bit', IDCodeRegisterBits),
     (
      'value', ctypes.c_uint32)]


class AbortRegisterBits(ctypes.LittleEndianStructure):
    __doc__ = 'This class holds the different bit mask for the Abort Register.\n\n    Attributes:\n      DAPABORT: write ``1`` to trigger a DAP abort.\n      STKCMPCLR: write ``1`` to clear the ``STICKYCMP`` sticky compare flag\n          (only supported on SW-DP).\n      STKERRCLR: write ``1`` to clear the ``STICKYERR`` sticky error flag\n          (only supported on SW-DP).\n      WDERRCLR: write ``1`` to clear the ``WDATAERR`` write data error flag\n          (only supported on SW-DP).\n      ORUNERRCLR: write ``1`` to clear the ``STICKYORUN`` overrun error flag\n          (only supported on SW-DP).\n    '
    _fields_ = [
     (
      'DAPABORT', ctypes.c_uint32, 1),
     (
      'STKCMPCLR', ctypes.c_uint32, 1),
     (
      'STKERRCLR', ctypes.c_uint32, 1),
     (
      'WDERRCLR', ctypes.c_uint32, 1),
     (
      'ORUNERRCLR', ctypes.c_uint32, 1),
     (
      'RESERVED', ctypes.c_uint32, 27)]


class AbortRegisterFlags(ctypes.Union):
    __doc__ = 'Mask for the abort register bits.\n\n    Attributes:\n      value: the value stored in the mask.\n    '
    _anonymous_ = ('bit', )
    _fields_ = [
     (
      'bit', AbortRegisterBits),
     (
      'value', ctypes.c_uint32)]


class ControlStatusRegisterBits(ctypes.LittleEndianStructure):
    __doc__ = 'This class holds the different bit masks for the DP Control / Status\n    Register bit assignments.\n\n    Attributes:\n      ORUNDETECT: if set, enables overrun detection.\n      STICKYORUN: if overrun is enabled, is set when overrun occurs.\n      TRNMODE: transfer mode for acess port operations.\n      STICKYCMP: is set when a match occurs on a pushed compare or verify\n          operation.\n      STICKYERR: is set when an error is returned by an access port\n          transaction.\n      READOK: is set when the response to a previous access port or ``RDBUFF``\n          was ``OK``.\n      WDATAERR: set to ``1`` if a Write Data Error occurs.\n      MASKLANE: bytes to be masked in pushed compare and verify operations.\n      TRNCNT: transaction counter.\n      RESERVED: reserved.\n      CDBGRSTREQ: debug reset request.\n      CDBGRSTACK: debug reset acknowledge.\n      CDBGPWRUPREQ: debug power-up request.\n      CDBGPWRUPACK: debug power-up acknowledge.\n      CSYSPWRUPREQ: system power-up request\n      CSYSPWRUPACK: system power-up acknowledge.\n\n    See also:\n      See the ARM documentation on the significance of these masks\n      `here <http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.ihi0031c/index.html>`_.\n    '
    _fields_ = [
     (
      'ORUNDETECT', ctypes.c_uint32, 1),
     (
      'STICKYORUN', ctypes.c_uint32, 1),
     (
      'TRNMODE', ctypes.c_uint32, 2),
     (
      'STICKYCMP', ctypes.c_uint32, 1),
     (
      'STICKYERR', ctypes.c_uint32, 1),
     (
      'READOK', ctypes.c_uint32, 1),
     (
      'WDATAERR', ctypes.c_uint32, 1),
     (
      'MASKLANE', ctypes.c_uint32, 4),
     (
      'TRNCNT', ctypes.c_uint32, 12),
     (
      'RESERVED', ctypes.c_uint32, 2),
     (
      'CDBGRSTREQ', ctypes.c_uint32, 1),
     (
      'CDBGRSTACK', ctypes.c_uint32, 1),
     (
      'CDBGPWRUPREQ', ctypes.c_uint32, 1),
     (
      'CDBGPWRUPACK', ctypes.c_uint32, 1),
     (
      'CSYSPWRUPREQ', ctypes.c_uint32, 1),
     (
      'CSYSPWRUPACK', ctypes.c_uint32, 1)]


class ControlStatusRegisterFlags(ctypes.Union):
    __doc__ = 'Mask for the control/status register bits.\n\n    Attributes:\n      value: the value stored in the mask.\n    '
    _anonymous_ = ('bit', )
    _fields_ = [
     (
      'bit', ControlStatusRegisterBits),
     (
      'value', ctypes.c_uint32)]


class SelectRegisterBits(ctypes.LittleEndianStructure):
    __doc__ = 'This class holds the different bit masks for the AP Select Register.\n\n    Attributes:\n      CTRLSEL: SW-DP debug port address bank select.\n      RESERVED_A: reserved.\n      APBANKSEL: selects the active four-word register window on the current\n          access port.\n      RESERVED_B: reserved.\n      APSEL: selects the current access port.\n    '
    _fields_ = [
     (
      'CTRLSEL', ctypes.c_uint32, 1),
     (
      'RESERVED_A', ctypes.c_uint32, 3),
     (
      'APBANKSEL', ctypes.c_uint32, 4),
     (
      'RESERVED_B', ctypes.c_uint32, 16),
     (
      'APSEL', ctypes.c_uint32, 8)]


class SelectRegisterFlags(ctypes.Union):
    __doc__ = 'Mask for the select register bits.\n\n    Attributes:\n      value: the value stored in the mask.\n    '
    _anonymous_ = ('bit', )
    _fields_ = [
     (
      'bit', SelectRegisterBits),
     (
      'value', ctypes.c_uint32)]


class MDMAPControlRegisterBits(ctypes.LittleEndianStructure):
    __doc__ = 'This class holds the different bit masks for the MDM-AP Control\n    Register.\n\n    Attributes:\n      flash_mass_erase: set to cause a mass erase, this is cleared\n          automatically when a mass erase finishes.\n      debug_disable: set to disable debug, clear to allow debug.\n      debug_request: set to force the core to halt.\n      sys_reset_request: set to force a system reset.\n      core_hold_reset: set to suspend the core in reset at the end of reset\n          sequencing.\n      VLLDBGREQ: set to hold the system in reset after the next recovery from\n          VLLSx (Very Low Leakage Stop).\n      VLLDBGACK: set to release a system held in reset following a VLLSx\n          (Very Low Leakage Stop) recovery.\n      VLLSTATACK: set to acknowledge that the DAP LLS (Low Leakage Stop) and\n          VLLS (Very Low Leakage Stop) status bits have read.\n    '
    _fields_ = [
     (
      'flash_mass_erase', ctypes.c_uint8, 1),
     (
      'debug_disable', ctypes.c_uint8, 1),
     (
      'debug_request', ctypes.c_uint8, 1),
     (
      'sys_reset_request', ctypes.c_uint8, 1),
     (
      'core_hold_reset', ctypes.c_uint8, 1),
     (
      'VLLDBGREQ', ctypes.c_uint8, 1),
     (
      'VLLDBGACK', ctypes.c_uint8, 1),
     (
      'VLLSTATACK', ctypes.c_uint8, 1)]


class MDMAPControlRegisterFlags(ctypes.Union):
    __doc__ = 'Mask for the MDM-AP control register bits.\n\n    Attributes:\n      value: the value stored in the mask.\n    '
    _anonymous_ = ('bit', )
    _fields_ = [
     (
      'bit', MDMAPControlRegisterBits),
     (
      'value', ctypes.c_uint8)]


class MDMAPStatusRegisterBits(ctypes.LittleEndianStructure):
    __doc__ = 'Holds the bit masks for the MDM-AP Status Register.\n\n    Attributes:\n      flash_mass_erase_ack: cleared after a system reset, indicates that a\n          flash mass erase was acknowledged.\n      flash_ready: indicates that flash has been initialized and can be\n          configured.\n      system_security: if set, system is secure and debugger cannot access the\n          memory or system bus.\n      system_reset: ``1`` if system is in reset, otherwise ``0``.\n      mass_erase_enabled: ``1`` if MCU can be mass erased, otherwise ``0``.\n      low_power_enabled: ``1`` if low power stop mode is enabled, otherwise ``0``.\n      very_low_power_mode: ``1`` if device is in very low power mode.\n      LLSMODEEXIT: indicates an exit from LLS mode has occurred.\n      VLLSxMODEEXIT: indicates an exit from VLLSx mode has occured.\n      core_halted; indicates core has entered debug halt mode.\n      core_deep_sleep: indicates core has entered a low power mode.\n      core_sleeping: indicates the core has entered a low power mode.\n\n    Note:\n      if ``core_sleeping & !core_deep_sleep``, then the core is in VLPW (very\n      low power wait) mode, otherwise if ``core_sleeping & core_deep_sleep``,\n      then it is in VLPS (very low power stop) mode.\n    '
    _fields_ = [
     (
      'flash_mass_erase_ack', ctypes.c_uint32, 1),
     (
      'flash_ready', ctypes.c_uint32, 1),
     (
      'system_security', ctypes.c_uint32, 1),
     (
      'system_reset', ctypes.c_uint32, 1),
     (
      'RESERVED_A', ctypes.c_uint32, 1),
     (
      'mass_erase_enabled', ctypes.c_uint32, 1),
     (
      'backdoor_access_enabled', ctypes.c_uint32, 1),
     (
      'low_power_enabled', ctypes.c_uint32, 1),
     (
      'very_low_power_mode', ctypes.c_uint32, 1),
     (
      'LLSMODEEXIT', ctypes.c_uint32, 1),
     (
      'VLLSxMODEEXIT', ctypes.c_uint32, 1),
     (
      'RESERVED_B', ctypes.c_uint32, 5),
     (
      'core_halted', ctypes.c_uint32, 1),
     (
      'core_deep_sleep', ctypes.c_uint32, 1),
     (
      'core_sleeping', ctypes.c_uint32, 1),
     (
      'RESERVED_C', ctypes.c_uint32, 13)]


class MDMAPStatusRegisterFlags(ctypes.Union):
    __doc__ = 'Mask for the MDM-AP status register bits.\n\n    Attributes:\n      value: the value stored in the mask.\n    '
    _anonymous_ = ('bit', )
    _fields_ = [
     (
      'bit', MDMAPStatusRegisterBits),
     (
      'value', ctypes.c_uint32)]
# okay decompiling ./pylink/registers.pyc
