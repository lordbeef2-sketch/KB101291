# NI PYTHON API DIGEST: nisync-python

<!--NI_PYTHON_API_SNAPSHOT repo=ni/nisync-python commit=8c7529dabd5803a489032f67aae4b56805adcd17 -->

<!--NI_PYTHON_API repo=nisync-python path=nisync/__init__.py -->
## PYTHON MODULE: nisync/__init__.py

### MODULE DOCSTRING

NI-Sync Python API.

<!--NI_PYTHON_API repo=nisync-python path=nisync/_attributes.py -->
## PYTHON MODULE: nisync/_attributes.py

### `class Attribute(object)`

#### `def __init__(self, attribute_id)`

### `class AttributeViInt32(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViReal64(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViBoolean(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViString(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

<!--NI_PYTHON_API repo=nisync-python path=nisync/_errorcodes.py -->
## PYTHON MODULE: nisync/_errorcodes.py

### `class Status(CtypesEnum)`

<!--NI_PYTHON_API repo=nisync-python path=nisync/_library.py -->
## PYTHON MODULE: nisync/_library.py

### `def ascii_encode(value)`

### `class Library(object)`

#### `def __init__(self, ctypes_library)`

#### `def niSync_init(self, resourceName, IDQuery, resetDevice, vi)`

#### `def niSync_close(self, vi)`

#### `def niSync_GetTimeReferenceNames(self, vi, bufferSize, timeReferenceNames)`

#### `def niSync_error_message(self, vi, errorCode, errorMessage)`

#### `def niSync_reset(self, vi)`

#### `def niSync_PersistConfig(self, vi)`

#### `def niSync_self_test(self, vi, selfTestResult, selfTestMessage)`

#### `def niSync_revision_query(self, vi, instrumentDriverRevision, firmwareRevision)`

#### `def niSync_ConfigureFPGA(self, vi, fpgaProgramPath)`

#### `def niSync_ConnectTrigTerminals(self, vi, srcTerminal, destTerminal, syncClock, invert, updateEdge)`

#### `def niSync_DisconnectTrigTerminals(self, vi, srcTerminal, destTerminal)`

#### `def niSync_GetTrigTerminalConnectionInfo(self, vi, destTerminal, srcTerminal, syncClock, invert, updateEdge)`

#### `def niSync_ConnectSWTrigToTerminal(self, vi, srcTerminal, destTerminal, syncClock, invert, updateEdge, delay)`

#### `def niSync_DisconnectSWTrigFromTerminal(self, vi, srcTerminal, destTerminal)`

#### `def niSync_GetSWTrigConnectionInfo(self, vi, destTerminal, srcTerminal, syncClk, invert, updateEdge, delay)`

#### `def niSync_SendSoftwareTrigger(self, vi, srcTerminal)`

#### `def niSync_ConnectClkTerminals(self, vi, srcTerminal, destTerminal)`

#### `def niSync_DisconnectClkTerminals(self, vi, srcTerminal, destTerminal)`

#### `def niSync_GetClkTerminalConnectionInfo(self, vi, destTerminal, srcTerminal)`

#### `def niSync_MeasureFrequency(self, vi, srcTerminal, duration, actualDuration, frequency, frequencyError)`

#### `def niSync_MeasureFrequencyEx(self, vi, srcTerminal, duration, decimationCount, actualDuration, frequency, frequencyError)`

#### `def niSync_Start1588(self, vi)`

#### `def niSync_Stop1588(self, vi)`

#### `def niSync_SetTime(self, vi, timeSource, timeSeconds, timeNanoseconds, timeFractionalNanoseconds)`

#### `def niSync_GetTime(self, vi, timeSeconds, timeNanoseconds, timeFractionalNanoseconds)`

#### `def niSync_ResetFrequency(self, vi)`

#### `def niSync_CreateFutureTimeEvent(self, vi, terminal, outputLevel, timeSeconds, timeNanoseconds, timeFractionalNanoseconds)`

#### `def niSync_ClearFutureTimeEvents(self, vi, terminal)`

#### `def niSync_EnableTimeStampTrigger(self, vi, terminal, activeEdge)`

#### `def niSync_EnableTimeStampTriggerWithDecimation(self, vi, terminal, activeEdge, decimationCount)`

#### `def niSync_ReadTriggerTimeStamp(self, vi, terminal, timeout, timeSeconds, timeNanoseconds, timeFractionalNanoseconds, detectedEdge)`

#### `def niSync_ReadMultipleTriggerTimeStamp(self, vi, terminal, timestampsToRead, timeout, timeSecondsBuffer, timeNanosecondsBuffer, timeFractionalNanosecondsBuffer, detectedEdgeBuffer, timestampsRead)`

#### `def niSync_DisableTimeStampTrigger(self, vi, terminal)`

#### `def niSync_CreateClock(self, vi, terminal, highTicks, lowTicks, startTimeSeconds, startTimeNanoseconds, startTimeFractionalNanoseconds, stopTimeSeconds, stopTimeNanoseconds, stopTimeFractionalNanoseconds)`

#### `def niSync_ClearClock(self, vi, terminal)`

#### `def niSync_Start8021AS(self, vi)`

#### `def niSync_Stop8021AS(self, vi)`

#### `def niSync_SetTimeReferenceFreeRunning(self, vi)`

#### `def niSync_SetTimeReferenceGPS(self, vi)`

#### `def niSync_SetTimeReferenceIRIG(self, vi, irigType, terminalName)`

#### `def niSync_SetTimeReferencePPS(self, vi, terminalName, useManualTime, initialTimeSeconds, initialTimeNanoseconds, initialTimeFractionalNanoseconds)`

#### `def niSync_SetTimeReference1588OrdinaryClock(self, vi)`

#### `def niSync_SetTimeReference8021AS(self, vi)`

#### `def niSync_EnableGPSTimestamping(self, vi)`

#### `def niSync_EnableIRIGTimestamping(self, vi, irigType, terminalName)`

#### `def niSync_ReadLastGPSTimestamp(self, vi, timestampSeconds, timestampNanoseconds, timestampFractionalNanoseconds, gpsSeconds, gpsNanoseconds, gpsFractionalNanoseconds)`

#### `def niSync_ReadLastIRIGTimestamp(self, vi, terminal, timestampSeconds, timestampNanoseconds, timestampFractionalNanoseconds, irigbSeconds, irigbNanoseconds, irigbFractionalNanoseconds)`

#### `def niSync_DisableGPSTimestamping(self, vi)`

#### `def niSync_DisableIRIGTimestamping(self, vi, terminalName)`

#### `def niSync_GetVelocity(self, vi, eastVelocity, northVelocity, upVelocity)`

#### `def niSync_GetLocation(self, vi, latitude, longitude, altitude)`

#### `def niSync_GetAttributeViInt32(self, vi, activeItem, attribute, value)`

#### `def niSync_GetAttributeViReal64(self, vi, activeItem, attribute, value)`

#### `def niSync_GetAttributeViBoolean(self, vi, activeItem, attribute, value)`

#### `def niSync_GetAttributeViString(self, vi, activeItem, attribute, bufferSize, value)`

#### `def niSync_SetAttributeViInt32(self, vi, activeItem, attribute, value)`

#### `def niSync_SetAttributeViReal64(self, vi, activeItem, attribute, value)`

#### `def niSync_SetAttributeViBoolean(self, vi, activeItem, attribute, value)`

#### `def niSync_SetAttributeViString(self, vi, activeItem, attribute, value)`

#### `def niSync_GetExtCalLastDateAndTime(self, vi, year, month, day, hour, minute)`

#### `def niSync_GetExtCalLastTemp(self, vi, temp)`

#### `def niSync_GetExtCalRecommendedInterval(self, vi, months)`

#### `def niSync_ChangeExtCalPassword(self, vi, oldPassword, newPassword)`

#### `def niSync_ReadCurrentTemperature(self, vi, temperature)`

#### `def niSync_CalGetOscillatorVoltage(self, vi, voltage)`

#### `def niSync_CalGetClk10PhaseVoltage(self, vi, voltage)`

#### `def niSync_CalGetDDSStartPulsePhaseVoltage(self, vi, voltage)`

#### `def niSync_CalGetDDSInitialPhase(self, vi, phase)`

#### `def niSync_InitExtCal(self, resourceName, password, extCalVi)`

#### `def niSync_CloseExtCal(self, extCalVi, action)`

#### `def niSync_CalAdjustOscillatorVoltage(self, extCalVi, measuredVoltage, oldVoltage)`

#### `def niSync_CalAdjustClk10PhaseVoltage(self, extCalVi, measuredVoltage, oldVoltage)`

#### `def niSync_CalAdjustDDSStartPulsePhaseVoltage(self, extCalVi, measuredVoltage, oldVoltage)`

#### `def niSync_CalAdjustDDSInitialPhase(self, extCalVi, measuredPhase, oldPhase)`

#### `def niSync_StartPTP(self, vi, initialTimeSource, initialTimeSeconds, initialTimeNanoseconds, initialTimeFractionalNanoseconds)`

#### `def niSync_StopPTP(self, vi)`

#### `def niSync_Get1588Time(self, vi, timeSeconds, timeNanoseconds, timeFractionalNanoseconds)`

<!--NI_PYTHON_API repo=nisync-python path=nisync/_library_singleton.py -->
## PYTHON MODULE: nisync/_library_singleton.py

### `def _get_library_name()`

### `def _get_library_type()`

### `def get()`

Returns a singleton instance of the nisync library.

<!--NI_PYTHON_API repo=nisync-python path=nisync/constants.py -->
## PYTHON MODULE: nisync/constants.py

### MODULE DOCSTRING

This module defines constants for trigger and clock terminal names.

- `PXI_TRIG0 = 'PXI_Trig0'`

- `PXI_TRIG1 = 'PXI_Trig1'`

- `PXI_TRIG2 = 'PXI_Trig2'`

- `PXI_TRIG3 = 'PXI_Trig3'`

- `PXI_TRIG4 = 'PXI_Trig4'`

- `PXI_TRIG5 = 'PXI_Trig5'`

- `PXI_TRIG6 = 'PXI_Trig6'`

- `PXI_TRIG7 = 'PXI_Trig7'`

- `PXI_STAR0 = 'PXI_Star0'`

- `PXI_STAR1 = 'PXI_Star1'`

- `PXI_STAR2 = 'PXI_Star2'`

- `PXI_STAR3 = 'PXI_Star3'`

- `PXI_STAR4 = 'PXI_Star4'`

- `PXI_STAR5 = 'PXI_Star5'`

- `PXI_STAR6 = 'PXI_Star6'`

- `PXI_STAR7 = 'PXI_Star7'`

- `PXI_STAR8 = 'PXI_Star8'`

- `PXI_STAR9 = 'PXI_Star9'`

- `PXI_STAR10 = 'PXI_Star10'`

- `PXI_STAR11 = 'PXI_Star11'`

- `PXI_STAR12 = 'PXI_Star12'`

- `PXI_STAR13 = 'PXI_Star13'`

- `PXI_STAR14 = 'PXI_Star14'`

- `PXI_STAR15 = 'PXI_Star15'`

- `PXI_STAR16 = 'PXI_Star16'`

- `PXI_STAR = 'PXI_Star'`

- `PXIE_DSTARA0 = 'PXIe_DStarA0'`

- `PXIE_DSTARA1 = 'PXIe_DStarA1'`

- `PXIE_DSTARA2 = 'PXIe_DStarA2'`

- `PXIE_DSTARA3 = 'PXIe_DStarA3'`

- `PXIE_DSTARA4 = 'PXIe_DStarA4'`

- `PXIE_DSTARA5 = 'PXIe_DStarA5'`

- `PXIE_DSTARA6 = 'PXIe_DStarA6'`

- `PXIE_DSTARA7 = 'PXIe_DStarA7'`

- `PXIE_DSTARA8 = 'PXIe_DStarA8'`

- `PXIE_DSTARA9 = 'PXIe_DStarA9'`

- `PXIE_DSTARA10 = 'PXIe_DStarA10'`

- `PXIE_DSTARA11 = 'PXIe_DStarA11'`

- `PXIE_DSTARA12 = 'PXIe_DStarA12'`

- `PXIE_DSTARA13 = 'PXIe_DStarA13'`

- `PXIE_DSTARA14 = 'PXIe_DStarA14'`

- `PXIE_DSTARA15 = 'PXIe_DStarA15'`

- `PXIE_DSTARA16 = 'PXIe_DStarA16'`

- `PXIE_DSTARA = 'PXIe_DStarA'`

- `PXIE_DSTARB0 = 'PXIe_DStarB0'`

- `PXIE_DSTARB1 = 'PXIe_DStarB1'`

- `PXIE_DSTARB2 = 'PXIe_DStarB2'`

- `PXIE_DSTARB3 = 'PXIe_DStarB3'`

- `PXIE_DSTARB4 = 'PXIe_DStarB4'`

- `PXIE_DSTARB5 = 'PXIe_DStarB5'`

- `PXIE_DSTARB6 = 'PXIe_DStarB6'`

- `PXIE_DSTARB7 = 'PXIe_DStarB7'`

- `PXIE_DSTARB8 = 'PXIe_DStarB8'`

- `PXIE_DSTARB9 = 'PXIe_DStarB9'`

- `PXIE_DSTARB10 = 'PXIe_DStarB10'`

- `PXIE_DSTARB11 = 'PXIe_DStarB11'`

- `PXIE_DSTARB12 = 'PXIe_DStarB12'`

- `PXIE_DSTARB13 = 'PXIe_DStarB13'`

- `PXIE_DSTARB14 = 'PXIe_DStarB14'`

- `PXIE_DSTARB15 = 'PXIe_DStarB15'`

- `PXIE_DSTARB16 = 'PXIe_DStarB16'`

- `PXIE_DSTARB = 'PXIe_DStarB'`

- `PXIE_DSTARC0 = 'PXIe_DStarC0'`

- `PXIE_DSTARC1 = 'PXIe_DStarC1'`

- `PXIE_DSTARC2 = 'PXIe_DStarC2'`

- `PXIE_DSTARC3 = 'PXIe_DStarC3'`

- `PXIE_DSTARC4 = 'PXIe_DStarC4'`

- `PXIE_DSTARC5 = 'PXIe_DStarC5'`

- `PXIE_DSTARC6 = 'PXIe_DStarC6'`

- `PXIE_DSTARC7 = 'PXIe_DStarC7'`

- `PXIE_DSTARC8 = 'PXIe_DStarC8'`

- `PXIE_DSTARC9 = 'PXIe_DStarC9'`

- `PXIE_DSTARC10 = 'PXIe_DStarC10'`

- `PXIE_DSTARC11 = 'PXIe_DStarC11'`

- `PXIE_DSTARC12 = 'PXIe_DStarC12'`

- `PXIE_DSTARC13 = 'PXIe_DStarC13'`

- `PXIE_DSTARC14 = 'PXIe_DStarC14'`

- `PXIE_DSTARC15 = 'PXIe_DStarC15'`

- `PXIE_DSTARC16 = 'PXIe_DStarC16'`

- `PXIE_DSTARC = 'PXIe_DStarC'`

- `PFI_LVDS0 = 'PFI_LVDS0'`

- `PFI_LVDS1 = 'PFI_LVDS1'`

- `PFI_LVDS2 = 'PFI_LVDS2'`

- `PFI0 = 'PFI0'`

- `PFI1 = 'PFI1'`

- `PFI2 = 'PFI2'`

- `PFI3 = 'PFI3'`

- `PFI4 = 'PFI4'`

- `PFI5 = 'PFI5'`

- `GROUND = 'Ground'`

- `SYNC_CLK_FULL_SPEED = 'SyncClkFullSpeed'`

- `SYNC_CLK_DIVIDED1 = 'SyncClkDivided1'`

- `SYNC_CLK_DIVIDED2 = 'SyncClkDivided2'`

- `SYNC_CLK_ASYNC = 'SyncClkAsync'`

- `GLOBAL_SOFTWARE_TRIGGER = 'GlobalSoftwareTrigger'`

- `PXI_CLK10 = 'PXI_Clk10'`

- `PXI_CLK10_IN = 'PXI_Clk10_In'`

- `CLK_IN = 'ClkIn'`

- `CLK_OUT = 'ClkOut'`

- `OSCILLATOR = 'Oscillator'`

- `DDS = 'DDS'`

- `PXIE_CLK100 = 'PXIe_Clk100'`

- `ALL_CONNECTED = 'AllConnected'`

- `DDS_UPDATE_IMMEDIATE = 'DDS_UpdateImmediate'`

- `RTSI0 = 'RTSI0'`

- `RTSI1 = 'RTSI1'`

- `RTSI2 = 'RTSI2'`

- `RTSI3 = 'RTSI3'`

- `RTSI4 = 'RTSI4'`

- `RTSI5 = 'RTSI5'`

- `RTSI6 = 'RTSI6'`

- `RTSI7 = 'RTSI7'`

- `BOARD_CLK = 'BoardClk'`

<!--NI_PYTHON_API repo=nisync-python path=nisync/enums.py -->
## PYTHON MODULE: nisync/enums.py

### `class CtypesEnum(IntEnum)`

#### `def from_param(cls, obj)`

### `class BMCAMode(CtypesEnum)`

### `class Edge(CtypesEnum)`

### `class ExternalCalibrationAction(CtypesEnum)`

### `class GPSStatus(CtypesEnum)`

### `class IEEE1588ClockAccuracy(CtypesEnum)`

### `class IEEE1588ClockClass(CtypesEnum)`

### `class IEEE1588PortState(CtypesEnum)`

### `class IEEE8021ASClockAccuracy(CtypesEnum)`

### `class IEEE8021ASPortState(CtypesEnum)`

### `class IRIGType(CtypesEnum)`

### `class InitialTimeSource(CtypesEnum)`

### `class Level(CtypesEnum)`

### `class SyncInterval(CtypesEnum)`

### `class TimeReference(CtypesEnum)`

### `class UpdateEdge(CtypesEnum)`

<!--NI_PYTHON_API repo=nisync-python path=nisync/errors.py -->
## PYTHON MODULE: nisync/errors.py

### `def _is_success(code)`

### `def _is_error(code)`

### `def _is_warning(code)`

### `class Error(Exception)`

#### `def __init__(self, message)`

### `class DriverError(Error)`

#### `def __init__(self, code, description)`

### `class DriverWarning(Warning)`

#### `def __init__(self, code, description)`

### `class UnsupportedConfigurationError(Error)`

#### `def __init__(self)`

### `class DriverNotInstalledError(Error)`

#### `def __init__(self)`

### `def _lookup_error_code(code)`

### `def handle_error(session, code, ignore_warnings=False, is_error_handling=False)`

<!--NI_PYTHON_API repo=nisync-python path=nisync/session.py -->
## PYTHON MODULE: nisync/session.py

### `def _tai_timestamp_to_tai_time(tai_timestamp)`

### `def _tai_time_to_tai_timestamp(tai_time)`

### `def _tai_time_parts_to_date_time(seconds, nanoseconds, frac_nanoseconds)`

### `def _date_time_to_tai_time_parts(date_time=None)`

### `def _encode_c_string(value)`

### `class _SessionBase(object)`

#### `def __init__(self, vi, library, active_item=None)`

#### `def __call__(self, active_item)`

#### `def _get_active_session(self, active_item)`

#### `def _get_error_description(self, code)`

#### `def _get_attribute_vi_int32(self, attribute)`

#### `def _set_attribute_vi_int32(self, attribute, value)`

#### `def _get_attribute_vi_real64(self, attribute)`

#### `def _set_attribute_vi_real64(self, attribute, value)`

#### `def _get_attribute_vi_boolean(self, attribute)`

#### `def _set_attribute_vi_boolean(self, attribute, value)`

#### `def _get_attribute_vi_string(self, attribute)`

#### `def _set_attribute_vi_string(self, attribute, value)`

#### `def _init(self, resource_name, id_query=False, reset_device=False)`

#### `def _close(self)`

### `class Session(_SessionBase)`


    Create a new NI-Sync session to the specified in the resource_name parameter.

    :param resource_name: Resource name of the NI-Sync device to initialize.
    :type resource_name: str
    :param id_query: Ignored
    :type id_query: bool
    :param reset_device: Specifies whether to reset the device during the initialization process.


    :type reset_device: bool
    

#### `def __init__(self, resource_name, id_query=False, reset_device=False)`

#### `def __enter__(self)`

#### `def __exit__(self, exc_type, exc_value, traceback)`

#### `def close(self)`

#### `def reset(self)`

#### `def reset_frequency(self)`

#### `def connect_trigger_terminals(self, source, destination, sync_clock='SyncClkAsync', invert=False, update_edge=enums.UpdateEdge.RISING)`

#### `def disconnect_trigger_terminals(self, source, destination)`

#### `def connect_clock_terminals(self, source, destination)`

#### `def disconnect_clock_terminals(self, source, destination)`

#### `def connect_software_trigger(self, source, destination, sync_clock='SyncClkFullSpeed', invert=False, update_edge=enums.UpdateEdge.RISING, delay=0.0)`

#### `def disconnect_software_trigger(self, source, destination)`

#### `def send_software_trigger(self, source)`

#### `def get_time(self)`


        Gets the time on the device.
        Returns a timezone-naive datetime in the TAI timescale.
        

#### `def set_time(self, time_source=enums.InitialTimeSource.SYSTEM_CLK, date_time=None)`


        Sets the time on the device.
        date_time is a timezone-naive datetime in the TAI timescale.
        

#### `def read_current_temperature(self)`

#### `def get_ext_cal_last_temp(self)`

#### `def get_ext_cal_last_time(self)`

#### `def get_location(self)`

#### `def get_velocity(self)`

#### `def create_future_time_event(self, terminal, level=enums.Level.LOW, time=None)`

#### `def clear_future_time_events(self, terminal)`

#### `def enable_timestamp_trigger(self, terminal, active_edge=enums.Edge.RISING, decimation=None)`

#### `def read_trigger_timestamp(self, terminal, timeout=10.0)`

#### `def read_multiple_trigger_timestamp(self, terminal, count=1, timeout=10.0)`

#### `def disable_timestamp_trigger(self, terminal)`

#### `def create_clock(self, terminal, high_ticks, low_ticks, start_time=None, stop_time=None)`

#### `def clear_clock(self, terminal)`

#### `def persist_config(self)`

#### `def self_test(self)`

#### `def set_timereference_freerunning(self)`

#### `def set_timereference_1588(self)`

#### `def set_timereference_8021as(self)`

#### `def set_timereference_irig(self, irig_type, terminal)`

#### `def set_timereference_gps(self)`

#### `def set_timereference_pps(self, terminal, initial_time=None)`

#### `def read_last_gps_timestamp(self)`

#### `def enable_gps_timestamping(self)`

#### `def disable_gps_timestamping(self)`

#### `def read_last_irig_timestamp(self, terminal='PFI0')`

#### `def enable_irig_timestamping(self, irig_type, terminal='PFI0')`

#### `def disable_irig_timestamping(self, terminal='PFI0')`

#### `def start_1588(self)`

#### `def stop_1588(self)`

#### `def start_8021as(self)`

#### `def stop_8021as(self)`

#### `def measure_frequency(self, terminal, duration=1e-06)`

#### `def measure_frequency_ex(self, terminal, duration=1e-06, decimation_count=1)`

#### `def revision_query(self)`

#### `def time_reference_names(self)`

#### `def time_references(self)`


        Returns a list of :class:`~nisync.session.TimeReference` objects
        

#### `def resource_name(self)`

#### `def session_handle(self)`

### `class TimeReference(object)`

#### `def __init__(self, session)`

#### `def name(self)`


        Returns the name of the time references instance.
        

#### `def present(self)`

#### `def present(self, value)`

#### `def current(self)`

#### `def current(self, value)`

#### `def offset(self)`

#### `def offset(self, value)`

#### `def utc_offset(self)`

#### `def utc_offset(self, value)`

#### `def utc_offset_valid(self)`

#### `def utc_offset_valid(self, value)`

#### `def last_sync_id(self)`

#### `def last_sync_id(self, value)`

#### `def offset_ns(self)`

#### `def offset_ns(self, value)`

#### `def type(self)`

#### `def type(self, value)`

#### `def enabled(self)`

#### `def enabled(self, value)`

#### `def is_selected(self)`

#### `def is_selected(self, value)`

### `class IEEE1588TimeReference(TimeReference)`

#### `def ip_address(self)`

#### `def ip_address(self, value)`

#### `def steps_to_grandmaster(self)`

#### `def steps_to_grandmaster(self, value)`

#### `def clock_id(self)`

#### `def clock_id(self, value)`

#### `def clock_class(self)`

#### `def clock_class(self, value)`

#### `def clock_accuracy(self)`

#### `def clock_accuracy(self, value)`

#### `def priority1(self)`

#### `def priority1(self, value)`

#### `def priority2(self)`

#### `def priority2(self, value)`

#### `def grandmaster_clock_id(self)`

#### `def grandmaster_clock_id(self, value)`

#### `def grandmaster_clock_class(self)`

#### `def grandmaster_clock_class(self, value)`

#### `def grandmaster_clock_accuracy(self)`

#### `def grandmaster_clock_accuracy(self, value)`

#### `def grandmaster_priority1(self)`

#### `def grandmaster_priority1(self, value)`

#### `def grandmaster_priority2(self)`

#### `def grandmaster_priority2(self, value)`

#### `def mean_path_delay(self)`

#### `def mean_path_delay(self, value)`

#### `def grandmaster_ip_address(self)`

#### `def grandmaster_ip_address(self, value)`

#### `def bmca_mode(self)`

#### `def bmca_mode(self, value)`

#### `def offset_scaled_log_variance(self)`

#### `def offset_scaled_log_variance(self, value)`

#### `def leap59(self)`

#### `def leap59(self, value)`

#### `def leap61(self)`

#### `def leap61(self, value)`

#### `def time_traceable(self)`

#### `def time_traceable(self, value)`

#### `def frequency_traceable(self)`

#### `def frequency_traceable(self, value)`

#### `def time_source(self)`

#### `def time_source(self, value)`

### `class IEEE8021ASTimeReference(TimeReference)`

#### `def clock_id(self)`

#### `def clock_id(self, value)`

#### `def clock_class(self)`

#### `def clock_class(self, value)`

#### `def clock_accuracy(self)`

#### `def clock_accuracy(self, value)`

#### `def priority1(self)`

#### `def priority1(self, value)`

#### `def priority2(self)`

#### `def priority2(self, value)`

#### `def grandmaster_clock_id(self)`

#### `def grandmaster_clock_id(self, value)`

#### `def grandmaster_clock_class(self)`

#### `def grandmaster_clock_class(self, value)`

#### `def grandmaster_clock_accuracy(self)`

#### `def grandmaster_clock_accuracy(self, value)`

#### `def grandmaster_priority1(self)`

#### `def grandmaster_priority1(self, value)`

#### `def grandmaster_priority2(self)`

#### `def grandmaster_priority2(self, value)`

### `class GPSTimeReference(TimeReference)`

#### `def antenna_connected(self)`

#### `def antenna_connected(self, value)`

#### `def recalculate_position(self)`

#### `def recalculate_position(self, value)`

#### `def satellites_available(self)`

#### `def satellites_available(self, value)`

#### `def self_survey(self)`

#### `def self_survey(self, value)`

#### `def mobile_mode(self)`

#### `def mobile_mode(self, value)`

#### `def status(self)`

#### `def status(self, value)`

### `class IRIGBTimeReference(TimeReference)`

### `class EtherCATTimeReference(TimeReference)`

### `class PPSTimeReference(TimeReference)`

<!--NI_PYTHON_API repo=nisync-python path=samples/__init__.py -->
## PYTHON MODULE: samples/__init__.py

### MODULE DOCSTRING

NI-Sync sample code.

<!--NI_PYTHON_API repo=nisync-python path=samples/connect_oscillator_to_pxi_clk10_in.py -->
## PYTHON MODULE: samples/connect_oscillator_to_pxi_clk10_in.py

### MODULE DOCSTRING

Connect the Oscillator to PXI_CLK10_IN terminal on an NI-Sync device.

This script demonstrates how to use the nisync library to connect the internal oscillator signal
of an NI-Sync device to the PXI_CLK10_IN terminal of the chassis.


- `RESOURCE_NAME = 'PXI1Slot10'`

### `def connect_oscillator_to_pxi_clk10_in(resource_name)`

Connect the oscillator to PXI_CLK10_IN on the specified NI-Sync device.

    Args:
        resource_name (str): The resource name of the NI-Sync device.
    

<!--NI_PYTHON_API repo=nisync-python path=samples/reset_device.py -->
## PYTHON MODULE: samples/reset_device.py

### MODULE DOCSTRING

Module for resetting an NI-Sync device.

This module provides functionality to reset an NI-Sync device using the nisync library.


- `RESOURCE_NAME = 'PXI1Slot10'`

### `def reset_device(resource_name)`

Reset the specified NI-Sync device.

    Args:
        resource_name (str): The resource name of the NI-Sync device to reset.
    

<!--NI_PYTHON_API repo=nisync-python path=samples/self_test.py -->
## PYTHON MODULE: samples/self_test.py

### MODULE DOCSTRING

Module for performing a self-test on an NI-Sync device.

This module provides functionality to perform a self-test on an NI-Sync device using the nisync
library.


- `RESOURCE_NAME = 'PXI1Slot10'`

### `def self_test(resource_name)`

Perform a self-test on the specified NI-Sync device.

    Args:
        resource_name (str): The resource name of the NI-Sync device to test.
    

<!--NI_PYTHON_API repo=nisync-python path=scripts/gen_templates.py -->
## PYTHON MODULE: scripts/gen_templates.py

### MODULE DOCSTRING

Extracts metadata from header files and generates Python API.

- `ROOT_DIR = pathlib.Path(__file__).parent.parent`

### `def main()`

Main function to generate templates based on specified input files.

<!--NI_PYTHON_API repo=nisync-python path=tests/__init__.py -->
## PYTHON MODULE: tests/__init__.py

### MODULE DOCSTRING

Automated tests for the nisync package.

<!--NI_PYTHON_API repo=nisync-python path=tests/acceptance/__init__.py -->
## PYTHON MODULE: tests/acceptance/__init__.py

### MODULE DOCSTRING

init file for ni-sync acceptance tests.

<!--NI_PYTHON_API repo=nisync-python path=tests/acceptance/test_reset.py -->
## PYTHON MODULE: tests/acceptance/test_reset.py

### `def test___session___reset___does_not_raise(sync_session)`

<!--NI_PYTHON_API repo=nisync-python path=tests/acceptance/test_self_test.py -->
## PYTHON MODULE: tests/acceptance/test_self_test.py

### `def test___self_test___check_returned_error(sync_session_with_reset)`

<!--NI_PYTHON_API repo=nisync-python path=tests/acceptance/test_session.py -->
## PYTHON MODULE: tests/acceptance/test_session.py

### `def test___open_session_with_reset___close_session(resource_name, reset_device)`

### `def test___open_session___invalid_resource_name___assert_expected_error(resource_name, error_type, error_code)`

<!--NI_PYTHON_API repo=nisync-python path=tests/acceptance/test_signal_and_clock_routing.py -->
## PYTHON MODULE: tests/acceptance/test_signal_and_clock_routing.py

### `def test___session___connect_clock_terminal(sync_session, source, destination)`

<!--NI_PYTHON_API repo=nisync-python path=tests/conftest.py -->
## PYTHON MODULE: tests/conftest.py

### MODULE DOCSTRING

Configure pytest for testing with nisync devices.

This module includes fixtures for setting up resources
and command line options for specifying resource names needed by test_session.py.


### `def pytest_addoption(parser)`

Add command-line option for specifying the resource name.

### `def pytest_collection_modifyitems(config, items)`

Skip functional tests if --resource_name command argurment is not provided.

### `def resource_name(request)`

Provide the resource name specified by the command-line option.

### `def sync_session_with_reset(resource_name)`

Open a session with reset_device=True and close it after the test.

### `def sync_session(resource_name)`

Open a session with reset_device=False and close it after the test.

<!--NI_PYTHON_API repo=nisync-python path=tests/unit/__init__.py -->
## PYTHON MODULE: tests/unit/__init__.py

### MODULE DOCSTRING

Unit tests for the nisync package.

<!--NI_PYTHON_API repo=nisync-python path=tests/unit/samples/__init__.py -->
## PYTHON MODULE: tests/unit/samples/__init__.py

### MODULE DOCSTRING

Unit tests for the nisync sample code.

<!--NI_PYTHON_API repo=nisync-python path=tests/unit/samples/test_connect_oscillator_to_clk10_in.py -->
## PYTHON MODULE: tests/unit/samples/test_connect_oscillator_to_clk10_in.py

### `def test_connect_oscillator_to_pxi_clk10_in(mocker, capfd)`

<!--NI_PYTHON_API repo=nisync-python path=tests/unit/samples/test_reset_device.py -->
## PYTHON MODULE: tests/unit/samples/test_reset_device.py

### `def test_reset_device(mocker, capfd)`

<!--NI_PYTHON_API repo=nisync-python path=tests/unit/samples/test_self_test.py -->
## PYTHON MODULE: tests/unit/samples/test_self_test.py

### `def test_self_test_passed(mocker, capfd)`

### `def test_self_test_failed(mocker, capfd)`

<!--NI_PYTHON_API repo=nisync-python path=tests/unit/test_session.py -->
## PYTHON MODULE: tests/unit/test_session.py

### `class CtypesMatcher(object)`

A matcher class for comparing ctypes objects or values.

#### `def __init__(self, value, ctype)`

Initializes the CtypesMatcher.

#### `def __eq__(self, other)`

Compares the CtypesMatcher's value with another object or value.

#### `def __repr__(self)`

Represents the CtypesMatcher's value as a string using its ctype.

- `RESOURCE_NAME = 'MockResource'`

- `SESSION_HANDLE = CtypesMatcher(1, ViSession)`

- `VI_FALSE = CtypesMatcher(0, ViBoolean)`

- `VI_TRUE = CtypesMatcher(1, ViBoolean)`

### `def init_mock(resource_name, id_query, reset_device, vi)`

### `def error_message_mock(vi, status, message)`

### `def lib_mock(mocker)`

### `def test___session___open_and_close___succeeds(lib_mock)`

### `def test___session___open_with_context_manager___succeeds(lib_mock)`

### `def test___session___open_when_init_fails___raises_driver_error(lib_mock)`

### `def test___session___open_with_context_manager_when_init_fails___raises_driver_error(lib_mock)`

### `def test___session___open_with_reset___succeeds(lib_mock)`

### `def test___session___reset___succeeds(lib_mock)`

### `def test___session___self_test___succeeds(lib_mock)`

### `def test___session___connect_clock_terminals___succeeds(lib_mock)`

### `def test___session___disconnect_clock_terminals___succeeds(lib_mock)`

### `def test___session___compare_session_handle___succeeds(lib_mock)`

<!--NI_PYTHON_API repo=nisync-python path=tests/unit/test_time_functions.py -->
## PYTHON MODULE: tests/unit/test_time_functions.py

- `SMALL_TIMESTAMP = 2 ** 9`

- `LARGE_TIMESTAMP = 2 ** 37`

- `SMALL_DATE_YEAR = 1970`

- `SMALL_DATE_MONTH = 1`

- `SMALL_DATE_DAY = 1`

- `SMALL_DATE_HOUR = 0`

- `SMALL_DATE_MINUTE = 8`

- `SMALL_DATE_SECOND = 32`

- `LARGE_DATE_YEAR = 6325`

- `LARGE_DATE_MONTH = 4`

- `LARGE_DATE_DAY = 8`

- `LARGE_DATE_HOUR = 15`

- `LARGE_DATE_MINUTE = 4`

- `LARGE_DATE_SECOND = 32`

- `DATETIMES = {'small': {'timestamp': SMALL_TIMESTAMP, 'datetime': datetime.datetime(year=SMALL_DATE_YEAR, month=SMALL_DATE_MONTH, day=SMALL_DATE_DAY, hour=SMALL_DATE_HOUR, minute=SMALL_DATE_MINUTE, second=SMALL_DATE_SECOND), 'hightime': hightime.datetime(year=SMALL_DATE_YEAR, month=SMALL_DATE_MONTH, day=SMALL_DATE_DAY, hour=SMALL_DATE_HOUR, minute=SMALL_DATE_MINUTE, second=SMALL_DATE_SECOND)}, 'large': {'timestamp': LARGE_TIMESTAMP, 'datetime': datetime.datetime(year=LARGE_DATE_YEAR, month=LARGE_DATE_MONTH, day=LARGE_DATE_DAY, hour=LARGE_DATE_HOUR, minute=LARGE_DATE_MINUTE, second=LARGE_DATE_SECOND), 'hightime': hightime.datetime(year=LARGE_DATE_YEAR, month=LARGE_DATE_MONTH, day=LARGE_DATE_DAY, hour=LARGE_DATE_HOUR, minute=LARGE_DATE_MINUTE, second=LARGE_DATE_SECOND)}}`

### `def _get_base_date(date_size, date_type)`

### `def _get_expected_tai_time(date_size, expected_tai_timestamp)`

### `def test_tai_timestamp_round_trip(date_size, date_type, starting_fractional_seconds, decimal_type)`

### `def test_tai_time_round_trip(date_size, date_type, starting_fractional_seconds)`

### `def test_tai_time_parts_round_trip(date_size, date_type, starting_nanoseconds)`
