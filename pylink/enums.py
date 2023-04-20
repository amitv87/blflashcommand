# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Mar 30 2023, 01:25:49) 
# [GCC 12.2.1 20220924]
# Embedded file name: pylink/enums.py
import ctypes

class JLinkGlobalErrors(object):
    __doc__ = 'Enumeration for the error codes which any J-Link SDK DLL API-function\n    can have as a return value.'
    UNSPECIFIED_ERROR = -1
    EMU_NO_CONNECTION = -256
    EMU_COMM_ERROR = -257
    DLL_NOT_OPEN = -258
    VCC_FAILURE = -259
    INVALID_HANDLE = -260
    NO_CPU_FOUND = -261
    EMU_FEATURE_UNSUPPORTED = -262
    EMU_NO_MEMORY = -263
    TIF_STATUS_ERROR = -264
    FLASH_PROG_COMPARE_FAILED = -265
    FLASH_PROG_PROGRAM_FAILED = -266
    FLASH_PROG_VERIFY_FAILED = -267
    OPEN_FILE_FAILED = -268
    UNKNOWN_FILE_FORMAT = -269
    WRITE_TARGET_MEMORY_FAILED = -270
    DEVICE_FEATURE_NOT_SUPPORTED = -271
    WRONG_USER_CONFIG = -272
    NO_TARGET_DEVICE_SELECTED = -273
    CPU_IN_LOW_POWER_MODE = -274

    @classmethod
    def to_string(cls, error_code):
        """Returns the string message for the given ``error_code``.

        Args:
          cls (JlinkGlobalErrors): the ``JLinkGlobalErrors`` class
          error_code (int): error code to convert

        Returns:
          An error string corresponding to the error code.

        Raises:
          ValueError: if the error code is invalid.
        """
        if error_code == cls.EMU_NO_CONNECTION:
            return 'No connection to emulator.'
        if error_code == cls.EMU_COMM_ERROR:
            return 'Emulator connection error.'
        if error_code == cls.DLL_NOT_OPEN:
            return "DLL has not been opened.  Did you call '.connect()'?"
        if error_code == cls.VCC_FAILURE:
            return 'Target system has no power.'
        if error_code == cls.INVALID_HANDLE:
            return 'Given file / memory handle is invalid.'
        if error_code == cls.NO_CPU_FOUND:
            return 'Could not find supported CPU.'
        if error_code == cls.EMU_FEATURE_UNSUPPORTED:
            return 'Emulator does not support the selected feature.'
        if error_code == cls.EMU_NO_MEMORY:
            return 'Emulator out of memory.'
        if error_code == cls.TIF_STATUS_ERROR:
            return 'Target interface error.'
        if error_code == cls.FLASH_PROG_COMPARE_FAILED:
            return 'Programmed data differs from source data.'
        if error_code == cls.FLASH_PROG_PROGRAM_FAILED:
            return 'Programming error occured.'
        if error_code == cls.FLASH_PROG_VERIFY_FAILED:
            return 'Error while verifying programmed data.'
        if error_code == cls.OPEN_FILE_FAILED:
            return 'Specified file could not be opened.'
        if error_code == cls.UNKNOWN_FILE_FORMAT:
            return 'File format of selected file is not supported.'
        if error_code == cls.WRITE_TARGET_MEMORY_FAILED:
            return 'Could not write target memory.'
        if error_code == cls.DEVICE_FEATURE_NOT_SUPPORTED:
            return 'Feature not supported by connected device.'
        if error_code == cls.WRONG_USER_CONFIG:
            return 'User configured DLL parameters incorrectly.'
        if error_code == cls.NO_TARGET_DEVICE_SELECTED:
            return 'User did not specify core to connect to.'
        if error_code == cls.CPU_IN_LOW_POWER_MODE:
            return 'Target CPU is in low power mode.'
        if error_code == cls.UNSPECIFIED_ERROR:
            return 'Unspecified error.'
        raise ValueError('Invalid error code: %d' % error_code)


class JLinkEraseErrors(JLinkGlobalErrors):
    __doc__ = 'Enumeration for the error codes generated during an erase operation.'
    ILLEGAL_COMMAND = -5

    @classmethod
    def to_string(cls, error_code):
        if error_code == cls.ILLEGAL_COMMAND:
            return 'Failed to erase sector.'
        return super(JLinkEraseErrors, cls).to_string(error_code)


class JLinkFlashErrors(JLinkGlobalErrors):
    __doc__ = 'Enumeration for the error codes generated during a flash operation.'
    COMPARE_ERROR = -2
    PROGRAM_ERASE_ERROR = -3
    VERIFICATION_ERROR = -4

    @classmethod
    def to_string(cls, error_code):
        if error_code == cls.COMPARE_ERROR:
            return 'Error comparing flash content to programming data.'
        if error_code == cls.PROGRAM_ERASE_ERROR:
            return 'Error during program/erase phase.'
        if error_code == cls.VERIFICATION_ERROR:
            return 'Error verifying programmed data.'
        return super(JLinkFlashErrors, cls).to_string(error_code)


class JLinkWriteErrors(JLinkGlobalErrors):
    __doc__ = 'Enumeration for the error codes generated during a write.'
    ZONE_NOT_FOUND_ERROR = -5

    @classmethod
    def to_string(cls, error_code):
        if error_code == cls.ZONE_NOT_FOUND_ERROR:
            return 'Zone not found'
        return super(JLinkWriteErrors, cls).to_string(error_code)


class JLinkReadErrors(JLinkGlobalErrors):
    __doc__ = 'Enumeration for the error codes generated during a read.'
    ZONE_NOT_FOUND_ERROR = -5

    @classmethod
    def to_string(cls, error_code):
        if error_code == cls.ZONE_NOT_FOUND_ERROR:
            return 'Zone not found'
        return super(JLinkReadErrors, cls).to_string(error_code)


class JLinkDataErrors(JLinkGlobalErrors):
    __doc__ = 'Enumeration for the error codes generated when setting a data event.'
    ERROR_UNKNOWN = 2147483648
    ERROR_NO_MORE_EVENTS = 2147483649
    ERROR_NO_MORE_ADDR_COMP = 2147483650
    ERROR_NO_MORE_DATA_COMP = 2147483652
    ERROR_INVALID_ADDR_MASK = 2147483680
    ERROR_INVALID_DATA_MASK = 2147483712
    ERROR_INVALID_ACCESS_MASK = 2147483776

    @classmethod
    def to_string(cls, error_code):
        if error_code == cls.ERROR_UNKNOWN:
            return 'Unknown error.'
        if error_code == cls.ERROR_NO_MORE_EVENTS:
            return 'There are no more available watchpoint units.'
        if error_code == cls.ERROR_NO_MORE_ADDR_COMP:
            return 'No more address comparisons can be set.'
        if error_code == cls.ERROR_NO_MORE_DATA_COMP:
            return 'No more data comparisons can be set.'
        if error_code == cls.ERROR_INVALID_ADDR_MASK:
            return 'Invalid flags passed for the address mask.'
        if error_code == cls.ERROR_INVALID_DATA_MASK:
            return 'Invalid flags passed for the data mask.'
        if error_code == cls.ERROR_INVALID_ACCESS_MASK:
            return 'Invalid flags passed for the access mask.'
        return super(JLinkDataErrors, cls).to_string(error_code)


class JLinkRTTErrors(JLinkGlobalErrors):
    __doc__ = 'Enumeration for error codes from RTT.'
    RTT_ERROR_CONTROL_BLOCK_NOT_FOUND = -2

    @classmethod
    def to_string(cls, error_code):
        if error_code == cls.RTT_ERROR_CONTROL_BLOCK_NOT_FOUND:
            return 'The RTT Control Block has not yet been found (wait?)'
        return super(JLinkRTTErrors, cls).to_string(error_code)


class JLinkHost(object):
    __doc__ = 'Enumeration for the different JLink hosts: currently only IP and USB.'
    USB = 1
    IP = 2
    USB_OR_IP = USB | IP


class JLinkInterfaces(object):
    __doc__ = 'Target interfaces for the J-Link.'
    JTAG = 0
    SWD = 1
    FINE = 3
    ICSP = 4
    SPI = 5
    C2 = 6


class JLinkResetStrategyCortexM3(object):
    __doc__ = 'Target reset strategies for the J-Link.\n\n    Attributes:\n      NORMAL: default reset strategy, does whatever is best to reset.\n      CORE: only the core is reset via the ``VECTRESET`` bit.\n      RESETPIN: pulls the reset pin low to reset the core and peripherals.\n      CONNECT_UNDER_RESET: J-Link connects to target while keeping reset\n        active.  This is recommented for STM32 devices.\n      HALT_AFTER_BTL: halt the core after the bootloader is executed.\n      HALT_BEFORE_BTL: halt the core before the bootloader is executed.\n      KINETIS: performs a normal reset, but also disables the watchdog.\n      ADI_HALT_AFTER_KERNEL: sets the ``SYSRESETREQ`` bit in the ``AIRCR`` in\n        order to reset the device.\n      CORE_AND_PERIPHERALS: sets the ``SYSRESETREQ`` bit in the ``AIRCR``, and\n        the ``VC_CORERESET`` bit in the ``DEMCR`` to make sure that the CPU is\n        halted immediately after reset.\n      LPC1200: reset for LPC1200 devices.\n      S3FN60D: reset for Samsung S3FN60D devices.\n\n    Note:\n      Please see the J-Link SEGGER Documentation, UM8001, for full information\n      about the different reset strategies.\n    '
    NORMAL = 0
    CORE = 1
    RESETPIN = 2
    CONNECT_UNDER_RESET = 3
    HALT_AFTER_BTL = 4
    HALT_BEFORE_BTL = 5
    KINETIS = 6
    ADI_HALT_AFTER_KERNEL = 7
    CORE_AND_PERIPHERALS = 8
    LPC1200 = 9
    S3FN60D = 10


class JLinkFunctions(object):
    __doc__ = 'Collection of function prototype and type builders for the J-Link SDK\n    API calls.'
    LOG_PROTOTYPE = ctypes.CFUNCTYPE(None, ctypes.c_char_p)
    UNSECURE_HOOK_PROTOTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint32)
    FLASH_PROGRESS_PROTOTYPE = ctypes.CFUNCTYPE(None, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int)


class JLinkCore(object):
    __doc__ = 'Enumeration for the different CPU core identifiers.\n\n    These are the possible cores for targets the J-Link is connected to.\n    Note that these are bitfields.'
    NONE = 0
    ANY = 4294967295
    CORTEX_M1 = 16777471
    COLDFIRE = 50331647
    CORTEX_M3 = 50331903
    CORTEX_M3_R1P0 = 50331664
    CORTEX_M3_R1P1 = 50331665
    CORTEX_M3_R2P0 = 50331680
    SIM = 83886079
    XSCALE = 100663295
    CORTEX_M0 = 100663551
    CORTEX_M_V8BASEL = 100729087
    ARM7 = 134217727
    ARM7TDMI = 117440767
    ARM7TDMI_R3 = 117440575
    ARM7TDMI_R4 = 117440591
    ARM7TDMI_S = 117441023
    ARM7TDMI_S_R3 = 117440831
    ARM7TDMI_S_R4 = 117440847
    CORTEX_A8 = 134217983
    CORTEX_A7 = 134742271
    CORTEX_A9 = 134807807
    CORTEX_A12 = 134873343
    CORTEX_A15 = 134938879
    CORTEX_A17 = 135004415
    ARM9 = 167772159
    ARM9TDMI_S = 150995455
    ARM920T = 153092351
    ARM922T = 153223423
    ARM926EJ_S = 153485823
    ARM946E_S = 155582975
    ARM966E_S = 157680127
    ARM968E_S = 157811199
    ARM11 = 201326591
    ARM1136 = 188153855
    ARM1136J = 188089087
    ARM1136J_S = 188089343
    ARM1136JF = 188090111
    ARM1136JF_S = 188090367
    ARM1156 = 190251007
    ARM1176 = 192348159
    ARM1176J = 192283391
    ARM1176J_S = 192283647
    ARM1176JF = 192284415
    ARM1176JF_S = 192284671
    CORTEX_R4 = 201326847
    CORTEX_R5 = 201392383
    RX = 234881023
    RX610 = 218169343
    RX62N = 218234879
    RX62T = 218300415
    RX63N = 218365951
    RX630 = 218431487
    RX63T = 218497023
    RX621 = 218562559
    RX62G = 218628095
    RX631 = 218693631
    RX210 = 219217919
    RX21A = 219283455
    RX220 = 219348991
    RX230 = 219414527
    RX231 = 219480063
    RX23T = 219545599
    RX111 = 220266495
    RX110 = 220332031
    RX113 = 220397567
    RX64M = 221315071
    RX71M = 221380607
    CORTEX_M4 = 234881279
    CORTEX_M7 = 234946815
    CORTEX_M_V8MAINL = 235012351
    CORTEX_A5 = 251658495
    POWER_PC = 285212671
    POWER_PC_N1 = 285147391
    POWER_PC_N2 = 285147647
    MIPS = 301989887
    MIPS_M4K = 285278207
    MIPS_MICROAPTIV = 285343743
    EFM8_UNSPEC = 318767103
    CIP51 = 302055423


class JLinkDeviceFamily(object):
    __doc__ = 'Enumeration for the difference device families.\n\n    These are the possible device families for targets that the J-Link is\n    connected to.'
    AUTO = 0
    CORTEX_M1 = 1
    COLDFIRE = 2
    CORTEX_M3 = 3
    SIMULATOR = 4
    XSCALE = 5
    CORTEX_M0 = 6
    ARM7 = 7
    CORTEX_A8 = 8
    CORTEX_A9 = 8
    ARM9 = 9
    ARM10 = 10
    ARM11 = 11
    CORTEX_R4 = 12
    RX = 13
    CORTEX_M4 = 14
    CORTEX_A5 = 15
    POWERPC = 16
    MIPS = 17
    EFM8 = 18
    ANY = 255


class JLinkFlags(object):
    __doc__ = 'Enumeration for the different flags that are passed to the J-Link C SDK\n    API methods.'
    GO_OVERSTEP_BP = 1
    DLG_BUTTON_YES = 1
    DLG_BUTTON_NO = 2
    DLG_BUTTON_OK = 4
    DLG_BUTTON_CANCEL = 8
    HW_PIN_STATUS_LOW = 0
    HW_PIN_STATUS_HIGH = 1
    HW_PIN_STATUS_UNKNOWN = 255


class JLinkSWOInterfaces(object):
    __doc__ = 'Serial Wire Output (SWO) interfaces.'
    UART = 0
    MANCHESTER = 1


class JLinkSWOCommands(object):
    __doc__ = 'Serial Wire Output (SWO) commands.'
    START = 0
    STOP = 1
    FLUSH = 2
    GET_SPEED_INFO = 3
    GET_NUM_BYTES = 10
    SET_BUFFERSIZE_HOST = 20
    SET_BUFFERSIZE_EMU = 21


class JLinkCPUCapabilities(object):
    __doc__ = 'Target CPU Cabilities.'
    READ_MEMORY = 2
    WRITE_MEMORY = 4
    READ_REGISTERS = 8
    WRITE_REGISTERS = 16
    GO = 32
    STEP = 64
    HALT = 128
    IS_HALTED = 256
    RESET = 512
    RUN_STOP = 1024
    TERMINAL = 2048
    DCC = 16384
    HSS = 32768


class JLinkHaltReasons(object):
    __doc__ = 'Halt reasons for the CPU.\n\n    Attributes:\n      DBGRQ: CPU has been halted because DBGRQ signal asserted.\n      CODE_BREAKPOINT: CPU has been halted because of code breakpoint match.\n      DATA_BREAKPOINT: CPU has been halted because of data breakpoint match.\n      VECTOR_CATCH: CPU has been halted because of vector catch.\n    '
    DBGRQ = 0
    CODE_BREAKPOINT = 1
    DATA_BREAKPOINT = 2
    VECTOR_CATCH = 3


class JLinkVectorCatchCortexM3(object):
    __doc__ = 'Vector catch types for the ARM Cortex M3.\n\n    Attributes:\n      CORE_RESET: The CPU core reset.\n      MEM_ERROR: A memory management error occurred.\n      COPROCESSOR_ERROR: Usage fault error accessing the Coprocessor.\n      CHECK_ERROR: Usage fault error on enabled check.\n      STATE_ERROR: Usage fault state error.\n      BUS_ERROR: Normal bus error.\n      INT_ERROR: Interrupt or exception service error.\n      HARD_ERROR: Hard fault error.\n    '
    CORE_RESET = 1
    MEM_ERROR = 16
    COPROCESSOR_ERROR = 32
    CHECK_ERROR = 64
    STATE_ERROR = 128
    BUS_ERROR = 256
    INT_ERROR = 512
    HARD_ERROR = 1024


class JLinkBreakpoint(object):
    __doc__ = 'J-Link breakpoint types.\n\n    Attributes:\n      SW_RAM: Software breakpont located in RAM.\n      SW_FLASH: Software breakpoint located in flash.\n      SW: Software breakpoint located in RAM or flash.\n      HW: Hardware breakpoint.\n      ANY: Allows specifying any time of breakpoint.\n      ARM: Breakpoint in ARM mode (only available on ARM 7/9 cores).\n      THUMB: Breakpoint in THUMB mode (only available on ARM 7/9 cores).\n    '
    SW_RAM = 16
    SW_FLASH = 32
    SW = 240
    HW = 4294967040
    ANY = 4294967280
    ARM = 1
    THUMB = 2


class JLinkBreakpointImplementation(object):
    __doc__ = 'J-Link breakpoint implementation types.\n\n    Attributes:\n      HARD: Hardware breakpoint using a breakpoint unit.\n      SOFT: Software breakpoint using a breakpoint instruction.\n      PENDING: Breakpoint has not been set yet.\n      FLASH: Breakpoint set in flash.\n    '
    HARD = 1
    SOFT = 2
    PENDING = 4
    FLASH = 16


class JLinkEventTypes(object):
    __doc__ = 'J-Link data event types.\n\n    Attributes:\n      BREAKPOINT: breakpoint data event.\n    '
    BREAKPOINT = 1


class JLinkAccessFlags(object):
    __doc__ = 'J-Link access types for data events.\n\n    These access types allow specifying the different types of access events\n    that should be monitored.\n\n    Attributes:\n      READ: specifies to monitor read accesses.\n      WRITE: specifies to monitor write accesses.\n      PRIVILEGED: specifies to monitor privileged accesses.\n      SIZE_8BIT: specifies to monitor an 8-bit access width.\n      SIZE_16BIT: specifies to monitor an 16-bit access width.\n      SIZE_32BIT: specifies to monitor an 32-bit access width.\n    '
    READ = 0
    WRITE = 1
    PRIV = 16
    SIZE_8BIT = 0
    SIZE_16BIT = 2
    SIZE_32BIT = 4


class JLinkAccessMaskFlags(object):
    __doc__ = 'J-Link access mask flags.\n\n    Attributes:\n      SIZE: specifies to not care about the access size of the event.\n      DIR: specifies to not care about the access direction of the event.\n      PRIV: specifies to not care about the access privilege of the event.\n    '
    SIZE = 6
    DIR = 1
    PRIV = 16


class JLinkStraceCommand(object):
    __doc__ = 'STRACE commmands.'
    TRACE_EVENT_SET = 0
    TRACE_EVENT_CLR = 1
    TRACE_EVENT_CLR_ALL = 2
    SET_BUFFER_SIZE = 3


class JLinkStraceEvent(object):
    __doc__ = 'STRACE events.'
    CODE_FETCH = 0
    DATA_ACCESS = 1
    DATA_LOAD = 2
    DATA_STORE = 3


class JLinkStraceOperation(object):
    __doc__ = 'STRACE operation specifiers.'
    TRACE_START = 0
    TRACE_STOP = 1
    TRACE_INCLUDE_RANGE = 2
    TRACE_EXCLUDE_RANGE = 3


class JLinkTraceSource(object):
    __doc__ = 'Sources for tracing.'
    ETB = 0
    ETM = 1
    MTB = 2


class JLinkTraceCommand(object):
    __doc__ = 'J-Link trace commands.'
    START = 0
    STOP = 1
    FLUSH = 2
    GET_NUM_SAMPLES = 16
    GET_CONF_CAPACITY = 17
    SET_CAPACITY = 18
    GET_MIN_CAPACITY = 19
    GET_MAX_CAPACITY = 20
    SET_FORMAT = 32
    GET_FORMAT = 33
    GET_NUM_REGIONS = 48
    GET_REGION_PROPS = 49
    GET_REGION_PROPS_EX = 50


class JLinkTraceFormat(object):
    __doc__ = 'J-Link trace formats.\n\n    Attributes:\n      FORMAT_4BIT: 4-bit data.\n      FORMAT_8BIT: 8-bit data.\n      FORMAT_16BIT: 16-bit data.\n      FORMAT_MULTIPLEXED: multiplexing on ETM / buffer link.\n      FORMAT_DEMULTIPLEXED: de-multiplexing on ETM / buffer link.\n      FORMAT_DOUBLE_EDGE: clock data on both ETM / buffer link edges.\n      FORMAT_ETM7_9: ETM7/ETM9 protocol.\n      FORMAT_ETM10: ETM10 protocol.\n      FORMAT_1BIT: 1-bit data.\n      FORMAT_2BIT: 2-bit data.\n    '
    FORMAT_4BIT = 1
    FORMAT_8BIT = 2
    FORMAT_16BIT = 4
    FORMAT_MULTIPLEXED = 8
    FORMAT_DEMULTIPLEXED = 16
    FORMAT_DOUBLE_EDGE = 32
    FORMAT_ETM7_9 = 64
    FORMAT_ETM10 = 128
    FORMAT_1BIT = 256
    FORMAT_2BIT = 512


class JLinkROMTable(object):
    __doc__ = 'The J-Link ROM tables.'
    NONE = 256
    ETM = 257
    MTB = 258
    TPIU = 259
    ITM = 260
    DWT = 261
    FPB = 262
    NVIC = 263
    TMC = 264
    TF = 265
    PTM = 266
    ETB = 267
    DBG = 268
    APBAP = 269
    AHBAP = 270
    SECURE = 271


class JLinkRTTCommand(object):
    __doc__ = 'RTT commands.'
    START = 0
    STOP = 1
    GETDESC = 2
    GETNUMBUF = 3
    GETSTAT = 4


class JLinkRTTDirection(object):
    __doc__ = 'RTT Direction.'
    UP = 0
    DOWN = 1
# okay decompiling ./pylink/enums.pyc
