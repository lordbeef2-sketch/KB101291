# NI OSS SOURCE SNAPSHOT: nimi-python

<!--NI_OSS_SNAPSHOT repo=ni/nimi-python commit=6511f8025f072f7f7021953888b916bbdc31aa2a -->

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidigital/nidigital/session.py sha256=2844c784d56f5c4497ad718067fc52922e32eac77af97dce8533586dc236188e bytes=234662 -->
## FILE: generated/nidigital/nidigital/session.py

- repository: `ni/nimi-python`
- source_path: `generated/nidigital/nidigital/session.py`
- sha256: `2844c784d56f5c4497ad718067fc52922e32eac77af97dce8533586dc236188e`
- bytes: 234662

````python
# -*- coding: utf-8 -*-
# This file was generated
import array  # noqa: F401
# Used by @ivi_synchronized
from functools import wraps

import nidigital._attributes as _attributes
import nidigital._converters as _converters
import nidigital._library_interpreter as _library_interpreter
import nidigital.enums as enums
import nidigital.errors as errors

import nidigital.history_ram_cycle_information as history_ram_cycle_information  # noqa: F401

import hightime
import nitclk

# Used for __repr__
import pprint
pp = pprint.PrettyPrinter(indent=4)


class _Burst(object):
    def __init__(self, session):
        self._session = session
        self._session._initiate()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session.abort()


# From https://stackoverflow.com/questions/5929107/decorators-with-parameters
def ivi_synchronized(f):
    @wraps(f)
    def aux(*xs, **kws):
        session = xs[0]  # parameter 0 is 'self' which is the session object
        with session.lock():
            return f(*xs, **kws)
    return aux


class _Lock(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        # _lock_session is called from the lock() function, not here
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session.unlock()


class _RepeatedCapabilities(object):
    def __init__(self, session, prefix, current_repeated_capability_list):
        self._session = session
        self._prefix = prefix
        # We need at least one element. If we get an empty list, make the one element an empty string
        self._current_repeated_capability_list = current_repeated_capability_list if len(current_repeated_capability_list) > 0 else ['']
        # Now we know there is at lease one entry, so we look if it is an empty string or not
        self._separator = '/' if len(self._current_repeated_capability_list[0]) > 0 else ''

    def __getitem__(self, repeated_capability):
        '''Set/get properties or call methods with a repeated capability (i.e. channels)'''
        rep_caps_list = _converters.convert_repeated_capabilities(repeated_capability, self._prefix)
        complete_rep_cap_list = [current_rep_cap + self._separator + rep_cap for current_rep_cap in self._current_repeated_capability_list for rep_cap in rep_caps_list]

        return _SessionBase(
            repeated_capability_list=complete_rep_cap_list,
            all_channels_in_session=self._session._all_channels_in_session,
            interpreter=self._session._interpreter,
            freeze_it=True
        )


# This is a very simple context manager we can use when we need to set/get attributes
# or call functions from _SessionBase that require no channels. It is tied to the specific
# implementation of _SessionBase and how repeated capabilities are handled.
class _NoChannel(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        self._repeated_capability_cache = self._session._repeated_capability
        self._session._repeated_capability = ''

    def __exit__(self, exc_type, exc_value, traceback):
        self._session._repeated_capability = self._repeated_capability_cache


class _SessionBase(object):
    '''Base class for all NI-Digital Pattern Driver sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    active_load_ioh = _attributes.AttributeViReal64(1150013)
    '''Type: float

    Specifies the current that the DUT sources to the active load while outputting a voltage above VCOM.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].active_load_ioh`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.active_load_ioh`
    '''
    active_load_iol = _attributes.AttributeViReal64(1150012)
    '''Type: float

    Specifies the current that the DUT sinks from the active load while outputting a voltage below VCOM.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].active_load_iol`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.active_load_iol`
    '''
    active_load_vcom = _attributes.AttributeViReal64(1150014)
    '''Type: float

    Specifies the voltage level at which the active load circuit switches between sourcing current and sinking current.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].active_load_vcom`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.active_load_vcom`
    '''
    cache = _attributes.AttributeViBoolean(1050004)
    '''Type: bool

    Specifies whether to cache the value of properties. When caching is enabled, the instrument driver keeps track of the current instrument settings and avoids sending redundant commands to the instrument. This significantly increases execution speed. Caching is always enabled in the driver, regardless of the value of this property.
    '''
    channel_count = _attributes.AttributeViInt32(1050203)
    '''Type: int

    Returns the number of channels that the specific digital pattern instrument driver supports.
    '''
    clock_generator_frequency = _attributes.AttributeViReal64(1150073)
    '''Type: float

    Specifies the frequency for the clock generator.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].clock_generator_frequency`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.clock_generator_frequency`
    '''
    clock_generator_is_running = _attributes.AttributeViBoolean(1150074)
    '''Type: bool

    Indicates whether the clock generator is running.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].clock_generator_is_running`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.clock_generator_is_running`
    '''
    conditional_jump_trigger_terminal_name = _attributes.AttributeViString(1150040)
    '''Type: str

    Specifies the terminal name from which the exported conditional jump trigger signal may be routed to other instruments through the PXI trigger bus. You can use this signal to trigger other instruments when the conditional jump trigger instance asserts on the digital pattern instrument.

    Tip:
    This property can be set/get on specific conditional_jump_triggers within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container conditional_jump_triggers to specify a subset.

    Example: :py:attr:`my_session.conditional_jump_triggers[ ... ].conditional_jump_trigger_terminal_name`

    To set/get on all conditional_jump_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.conditional_jump_trigger_terminal_name`
    '''
    conditional_jump_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerType, 1150033)
    '''Type: enums.TriggerType

    Disables the conditional jump trigger or configures it for either hardware triggering or software triggering.  The default value is TriggerType.NONE.

    +--------------------------+------------------------------------------------------------------+
    | Valid Values:            |                                                                  |
    +==========================+==================================================================+
    | TriggerType.NONE         | Disables the conditional jump trigger.                           |
    +--------------------------+------------------------------------------------------------------+
    | TriggerType.DIGITAL_EDGE | Configures the conditional jump trigger for hardware triggering. |
    +--------------------------+------------------------------------------------------------------+
    | TriggerType.SOFTWARE     | Configures the conditional jump trigger for software triggering. |
    +--------------------------+------------------------------------------------------------------+

    Tip:
    This property can be set/get on specific conditional_jump_triggers within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container conditional_jump_triggers to specify a subset.

    Example: :py:attr:`my_session.conditional_jump_triggers[ ... ].conditional_jump_trigger_type`

    To set/get on all conditional_jump_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.conditional_jump_trigger_type`
    '''
    cycle_number_history_ram_trigger_cycle_number = _attributes.AttributeViInt64(1150044)
    '''Type: int

    Specifies the cycle number on which History RAM starts acquiring pattern information when configured for a cycle number trigger.
    '''
    digital_edge_conditional_jump_trigger_edge = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.DigitalEdge, 1150035)
    '''Type: enums.DigitalEdge

    Configures the active edge of the incoming trigger signal for the conditional jump trigger instance. The default value is DigitalEdge.RISING.

    +---------------------+---------------------------------------------------------------+
    | Valid Values:       |                                                               |
    +=====================+===============================================================+
    | DigitalEdge.RISING  | Specifies the signal transition from low level to high level. |
    +---------------------+---------------------------------------------------------------+
    | DigitalEdge.FALLING | Specifies the signal transition from high level to low level. |
    +---------------------+---------------------------------------------------------------+

    Tip:
    This property can be set/get on specific conditional_jump_triggers within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container conditional_jump_triggers to specify a subset.

    Example: :py:attr:`my_session.conditional_jump_triggers[ ... ].digital_edge_conditional_jump_trigger_edge`

    To set/get on all conditional_jump_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.digital_edge_conditional_jump_trigger_edge`
    '''
    digital_edge_conditional_jump_trigger_source = _attributes.AttributeViString(1150034)
    '''Type: str

    Configures the digital trigger source terminal for a conditional jump trigger instance. The PXIe-6570/6571 supports triggering through the PXI trigger bus. You can specify source terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The source terminal can also be a terminal from another device, in which case the NI-Digital Pattern Driver automatically finds a route (if one is available) from that terminal to the input terminal (going through a physical PXI backplane trigger line). For example, you can set the source terminal on Dev1 to be /Dev2/ConditionalJumpTrigger0. The default value is VI_NULL.

    +----------------------------------------------+
    | Valid Values:                                |
    +==============================================+
    | String identifier to any valid terminal name |
    +----------------------------------------------+

    Tip:
    This property can be set/get on specific conditional_jump_triggers within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container conditional_jump_triggers to specify a subset.

    Example: :py:attr:`my_session.conditional_jump_triggers[ ... ].digital_edge_conditional_jump_trigger_source`

    To set/get on all conditional_jump_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.digital_edge_conditional_jump_trigger_source`
    '''
    digital_edge_rio_trigger_edge = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.DigitalEdge, 1150088)
    '''Type: enums.DigitalEdge

    Configures the active edge of the incoming trigger signal for the RIO trigger instance. The default value is DigitalEdge.RISING.

    +---------------------+---------------------------------------------------------------+
    | Valid Values:       |                                                               |
    +=====================+===============================================================+
    | DigitalEdge.RISING  | Specifies the signal transition from low level to high level. |
    +---------------------+---------------------------------------------------------------+
    | DigitalEdge.FALLING | Specifies the signal transition from high level to low level. |
    +---------------------+---------------------------------------------------------------+

    Tip:
    This property can be set/get on specific rio_triggers within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container rio_triggers to specify a subset.

    Example: :py:attr:`my_session.rio_triggers[ ... ].digital_edge_rio_trigger_edge`

    To set/get on all rio_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.digital_edge_rio_trigger_edge`
    '''
    digital_edge_rio_trigger_source = _attributes.AttributeViString(1150087)
    '''Type: str

    Configures the digital trigger source terminal for a RIO trigger instance. The PXIe-6570/6571 supports triggering through the PXI trigger bus. You can specify source terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The source terminal can also be a terminal from another device, in which case the NI-Digital Pattern Driver automatically finds a route (if one is available) from that terminal to the input terminal (going through a physical PXI backplane trigger line). For example, you can set the source terminal on Dev1 to be /Dev2/RIOTrigger0. The default value is VI_NULL.

    +----------------------------------------------+
    | Valid Values:                                |
    +==============================================+
    | String identifier to any valid terminal name |
    +----------------------------------------------+

    Tip:
    This property can be set/get on specific rio_triggers within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container rio_triggers to specify a subset.

    Example: :py:attr:`my_session.rio_triggers[ ... ].digital_edge_rio_trigger_source`

    To set/get on all rio_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.digital_edge_rio_trigger_source`
    '''
    digital_edge_start_trigger_edge = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.DigitalEdge, 1150031)
    '''Type: enums.DigitalEdge

    Specifies the active edge for the Start trigger. This property is used when the start_trigger_type property is set to Digital Edge.

    +---------------------+-------------------------------------------------------------------------------+
    | Defined Values:     |                                                                               |
    +=====================+===============================================================================+
    | DigitalEdge.RISING  | Asserts the trigger when the signal transitions from low level to high level. |
    +---------------------+-------------------------------------------------------------------------------+
    | DigitalEdge.FALLING | Asserts the trigger when the signal transitions from high level to low level. |
    +---------------------+-------------------------------------------------------------------------------+
    '''
    digital_edge_start_trigger_source = _attributes.AttributeViString(1150030)
    '''Type: str

    Specifies the source terminal for the Start trigger. This property is used when the start_trigger_type property is set to Digital Edge. You can specify source terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The source terminal can also be a terminal from another device, in which case the NI-Digital Pattern Driver automatically finds a route (if one is available) from that terminal to the input terminal (going through a physical PXI backplane trigger line). For example, you can set the source terminal on Dev1 to be /Dev2/StartTrigger.

    +-----------------+--------------------+
    | Defined Values: |                    |
    +=================+====================+
    | PXI_Trig0       | PXI trigger line 0 |
    +-----------------+--------------------+
    | PXI_Trig1       | PXI trigger line 1 |
    +-----------------+--------------------+
    | PXI_Trig2       | PXI trigger line 2 |
    +-----------------+--------------------+
    | PXI_Trig3       | PXI trigger line 3 |
    +-----------------+--------------------+
    | PXI_Trig4       | PXI trigger line 4 |
    +-----------------+--------------------+
    | PXI_Trig5       | PXI trigger line 5 |
    +-----------------+--------------------+
    | PXI_Trig6       | PXI trigger line 6 |
    +-----------------+--------------------+
    | PXI_Trig7       | PXI trigger line 7 |
    +-----------------+--------------------+
    '''
    driver_setup = _attributes.AttributeViString(1050007)
    '''Type: str

    This property returns initial values for NI-Digital Pattern Driver properties as a string.
    '''
    exported_conditional_jump_trigger_output_terminal = _attributes.AttributeViString(1150036)
    '''Type: str

    Specifies the terminal to output the exported signal of the specified instance of the conditional jump trigger. The default value is VI_NULL.

    +---------------+-------------------------+
    | Valid Values: |                         |
    +===============+=========================+
    | VI_NULL ("")  | Returns an empty string |
    +---------------+-------------------------+
    | PXI_Trig0     | PXI trigger line 0      |
    +---------------+-------------------------+
    | PXI_Trig1     | PXI trigger line 1      |
    +---------------+-------------------------+
    | PXI_Trig2     | PXI trigger line 2      |
    +---------------+-------------------------+
    | PXI_Trig3     | PXI trigger line 3      |
    +---------------+-------------------------+
    | PXI_Trig4     | PXI trigger line 4      |
    +---------------+-------------------------+
    | PXI_Trig5     | PXI trigger line 5      |
    +---------------+-------------------------+
    | PXI_Trig6     | PXI trigger line 6      |
    +---------------+-------------------------+
    | PXI_Trig7     | PXI trigger line 7      |
    +---------------+-------------------------+

    Tip:
    This property can be set/get on specific conditional_jump_triggers within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container conditional_jump_triggers to specify a subset.

    Example: :py:attr:`my_session.conditional_jump_triggers[ ... ].exported_conditional_jump_trigger_output_terminal`

    To set/get on all conditional_jump_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.exported_conditional_jump_trigger_output_terminal`
    '''
    exported_pattern_opcode_event_output_terminal = _attributes.AttributeViString(1150041)
    '''Type: str

    Specifies the destination terminal for exporting the Pattern Opcode Event. Terminals can be specified in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

    +-----------------+--------------------+
    | Defined Values: |                    |
    +=================+====================+
    | PXI_Trig0       | PXI trigger line 0 |
    +-----------------+--------------------+
    | PXI_Trig1       | PXI trigger line 1 |
    +-----------------+--------------------+
    | PXI_Trig2       | PXI trigger line 2 |
    +-----------------+--------------------+
    | PXI_Trig3       | PXI trigger line 3 |
    +-----------------+--------------------+
    | PXI_Trig4       | PXI trigger line 4 |
    +-----------------+--------------------+
    | PXI_Trig5       | PXI trigger line 5 |
    +-----------------+--------------------+
    | PXI_Trig6       | PXI trigger line 6 |
    +-----------------+--------------------+
    | PXI_Trig7       | PXI trigger line 7 |
    +-----------------+--------------------+

    Tip:
    This property can be set/get on specific pattern_opcode_events within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container pattern_opcode_events to specify a subset.

    Example: :py:attr:`my_session.pattern_opcode_events[ ... ].exported_pattern_opcode_event_output_terminal`

    To set/get on all pattern_opcode_events, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.exported_pattern_opcode_event_output_terminal`
    '''
    exported_rio_event_output_terminal = _attributes.AttributeViString(1150090)
    '''Type: str

    Specifies the destination terminal for exporting the RIO Event. Terminals can be specified in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

    +-----------------+--------------------+
    | Defined Values: |                    |
    +=================+====================+
    | PXI_Trig0       | PXI trigger line 0 |
    +-----------------+--------------------+
    | PXI_Trig1       | PXI trigger line 1 |
    +-----------------+--------------------+
    | PXI_Trig2       | PXI trigger line 2 |
    +-----------------+--------------------+
    | PXI_Trig3       | PXI trigger line 3 |
    +-----------------+--------------------+
    | PXI_Trig4       | PXI trigger line 4 |
    +-----------------+--------------------+
    | PXI_Trig5       | PXI trigger line 5 |
    +-----------------+--------------------+
    | PXI_Trig6       | PXI trigger line 6 |
    +-----------------+--------------------+
    | PXI_Trig7       | PXI trigger line 7 |
    +-----------------+--------------------+

    Tip:
    This property can be set/get on specific rio_events within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container rio_events to specify a subset.

    Example: :py:attr:`my_session.rio_events[ ... ].exported_rio_event_output_terminal`

    To set/get on all rio_events, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.exported_rio_event_output_terminal`
    '''
    exported_start_trigger_output_terminal = _attributes.AttributeViString(1150032)
    '''Type: str

    Specifies the destination terminal for exporting the Start trigger. Terminals can be specified in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

    +----------------------+-----------------------------+
    | Defined Values:      |                             |
    +======================+=============================+
    | Do not export signal | The signal is not exported. |
    +----------------------+-----------------------------+
    | PXI_Trig0            | PXI trigger line 0          |
    +----------------------+-----------------------------+
    | PXI_Trig1            | PXI trigger line 1          |
    +----------------------+-----------------------------+
    | PXI_Trig2            | PXI trigger line 2          |
    +----------------------+-----------------------------+
    | PXI_Trig3            | PXI trigger line 3          |
    +----------------------+-----------------------------+
    | PXI_Trig4            | PXI trigger line 4          |
    +----------------------+-----------------------------+
    | PXI_Trig5            | PXI trigger line 5          |
    +----------------------+-----------------------------+
    | PXI_Trig6            | PXI trigger line 6          |
    +----------------------+-----------------------------+
    | PXI_Trig7            | PXI trigger line 7          |
    +----------------------+-----------------------------+
    '''
    frequency_counter_hysteresis_enabled = _attributes.AttributeViBoolean(1150085)
    '''Type: bool

    Specifies whether hysteresis is enabled for the frequency counters of the digital pattern instrument.
    '''
    frequency_counter_measurement_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.FrequencyMeasurementMode, 1150084)
    '''Type: enums.FrequencyMeasurementMode

    Determines how the frequency counters of the digital pattern instrument make measurements.

    +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Valid Values:                     |                                                                                                                                                                                                                                                                                                                                                                                       |
    +===================================+=======================================================================================================================================================================================================================================================================================================================================================================================+
    | FrequencyMeasurementMode.BANKED   | Each discrete frequency counter is mapped to specific channels and makes frequency measurements from only those channels. Use banked mode when you need access to the full measure frequency range of the instrument. **Note:** If you request frequency measurements from multiple channels within the same bank, the measurements are made in series for the channels in that bank. |
    +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | FrequencyMeasurementMode.PARALLEL | All discrete frequency counters make frequency measurements from all channels in parallel with one another. Use parallel mode to increase the speed of frequency measurements if you do not need access to the full measure frequency range of the instrument; in parallel mode, you can also add frequency_counter_hysteresis_enabled to reduce measurement noise.                   |
    +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    '''
    frequency_counter_measurement_time = _attributes.AttributeViReal64TimeDeltaSeconds(1150069)
    '''Type: float in seconds or datetime.timedelta

    Specifies the measurement time for the frequency counter.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].frequency_counter_measurement_time`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.frequency_counter_measurement_time`
    '''
    group_capabilities = _attributes.AttributeViString(1050401)
    '''Type: str

    Returns a string that contains a comma-separated list of class-extension groups that the driver implements.
    '''
    halt_on_keep_alive_opcode = _attributes.AttributeViBoolean(1150062)
    '''Type: bool

    Specifies whether keep_alive opcodes should behave like halt opcodes.
    '''
    history_ram_buffer_size_per_site = _attributes.AttributeViInt64(1150079)
    '''Type: int

    Specifies the size, in samples, of the host memory buffer. The default value is 32000.

    +---------------+
    | Valid Values: |
    +===============+
    | 0-INT64_MAX   |
    +---------------+
    '''
    history_ram_cycles_to_acquire = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.HistoryRAMCyclesToAcquire, 1150047)
    '''Type: enums.HistoryRAMCyclesToAcquire

    Configures which cycles History RAM acquires after the trigger conditions are met. If you configure History RAM to only acquire failed cycles, you must set the pretrigger samples for History RAM to 0.

    +----------------------------------+-----------------------------------------------------------------------------------+
    | Defined Values:                  |                                                                                   |
    +==================================+===================================================================================+
    | HistoryRAMCyclesToAcquire.FAILED | Only acquires cycles that fail a compare after the triggering conditions are met. |
    +----------------------------------+-----------------------------------------------------------------------------------+
    | HistoryRAMCyclesToAcquire.ALL    | Acquires all cycles after the triggering conditions are met.                      |
    +----------------------------------+-----------------------------------------------------------------------------------+
    '''
    history_ram_max_samples_to_acquire_per_site = _attributes.AttributeViInt32(1150077)
    '''Type: int

    Specifies the maximum number of History RAM samples to acquire per site. If the property is set to -1, it will acquire until the History RAM buffer is full.
    '''
    history_ram_number_of_samples_is_finite = _attributes.AttributeViBoolean(1150078)
    '''Type: bool

    Specifies whether the instrument acquires a finite number of History Ram samples or acquires continuously. The maximum number of samples that will be acquired when this property is set to True is determined by the instrument History RAM depth specification and the History RAM Max Samples to Acquire Per Site property. The default value is True.

    +---------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Valid Values: |                                                                                                                                                      |
    +===============+======================================================================================================================================================+
    | True          | Specifies that History RAM results will not stream into the host buffer until a History RAM fetch API is called.                                     |
    +---------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
    | False         | Specifies that History RAM results will automatically start streaming into a host buffer after a pattern is burst and the History RAM has triggered. |
    +---------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
    '''
    history_ram_pretrigger_samples = _attributes.AttributeViInt32(1150048)
    '''Type: int

    Specifies the number of samples to acquire before the trigger conditions are met. If you configure History RAM to only acquire failed cycles, you must set the pretrigger samples for History RAM to 0.
    '''
    history_ram_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.HistoryRAMTriggerType, 1150043)
    '''Type: enums.HistoryRAMTriggerType

    Specifies the type of trigger condition on which History RAM starts acquiring pattern information.

    +-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
    | Defined Values:                     |                                                                                                                                     |
    +=====================================+=====================================================================================================================================+
    | HistoryRAMTriggerType.FIRST_FAILURE | Starts acquiring pattern information in History RAM on the first failed cycle in a pattern burst.                                   |
    +-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
    | HistoryRAMTriggerType.CYCLE_NUMBER  | Starts acquiring pattern information in History RAM starting from a specified cycle number.                                         |
    +-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
    | HistoryRAMTriggerType.PATTERN_LABEL | Starts acquiring pattern information in History RAM starting from a specified pattern label, augmented by vector and cycle offsets. |
    +-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
    '''
    instrument_firmware_revision = _attributes.AttributeViString(1050510)
    '''Type: str

    Returns a string that contains the firmware revision information for the digital pattern instrument.

    Tip:
    This property can be set/get on specific instruments within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container instruments to specify a subset.

    Example: :py:attr:`my_session.instruments[ ... ].instrument_firmware_revision`

    To set/get on all instruments, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.instrument_firmware_revision`
    '''
    instrument_manufacturer = _attributes.AttributeViString(1050511)
    '''Type: str

    Returns a string ("National Instruments") that contains the name of the manufacturer of the digital pattern instrument.
    '''
    instrument_model = _attributes.AttributeViString(1050512)
    '''Type: str

    Returns a string that contains the model number or name of the digital pattern instrument.
    '''
    interchange_check = _attributes.AttributeViBoolean(1050021)
    '''Type: bool

    This property is not supported.
    '''
    io_resource_descriptor = _attributes.AttributeViString(1050304)
    '''Type: str

    Returns a string that contains the resource descriptor that the NI-Digital Pattern Driver uses to identify the digital pattern instrument.
    '''
    is_keep_alive_active = _attributes.AttributeViBoolean(1150063)
    '''Type: bool

    Returns True if the digital pattern instrument is driving the keep alive pattern.
    '''
    logical_name = _attributes.AttributeViString(1050305)
    '''Type: str

    Returns a string containing the logical name that you specified when opening the current IVI session. This property is not supported.
    '''
    mask_compare = _attributes.AttributeViBoolean(1150060)
    '''Type: bool

    Specifies whether the pattern comparisons are masked or not. When set to True for a specified pin, failures on that pin will be masked.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].mask_compare`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.mask_compare`
    '''
    pattern_label_history_ram_trigger_cycle_offset = _attributes.AttributeViInt64(1150045)
    '''Type: int

    Specifies the number of cycles that follow the specified pattern label and vector offset, after which History RAM will start acquiring pattern information when configured for a pattern label trigger.
    '''
    pattern_label_history_ram_trigger_label = _attributes.AttributeViString(1150046)
    '''Type: str

    Specifies the pattern label, augmented by the vector and cycle offset, to determine the point where History RAM will start acquiring pattern information when configured for a pattern label trigger.
    '''
    pattern_label_history_ram_trigger_vector_offset = _attributes.AttributeViInt64(1150052)
    '''Type: int

    Specifies the number of vectors that follow the specified pattern label, after which History RAM will start acquiring pattern information when configured for a pattern label trigger.
    '''
    pattern_opcode_event_terminal_name = _attributes.AttributeViString(1150042)
    '''Type: str

    Specifies the terminal name for the output trigger signal of the specified instance of a Pattern Opcode Event. You can use this terminal name as an input signal source for another trigger.

    Tip:
    This property can be set/get on specific pattern_opcode_events within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container pattern_opcode_events to specify a subset.

    Example: :py:attr:`my_session.pattern_opcode_events[ ... ].pattern_opcode_event_terminal_name`

    To set/get on all pattern_opcode_events, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.pattern_opcode_event_terminal_name`
    '''
    ppmu_allow_extended_voltage_range = _attributes.AttributeViBoolean(1150076)
    '''Type: bool

    Enables the instrument to operate in additional voltage ranges where instrument specifications may differ from standard ranges. When set to True, this property enables extended voltage range operation. Review specification deviations for application suitability before using this property. NI recommends setting this property to False when not using the extended voltage range to avoid unintentional use of this range. The extended voltage range is supported only for PPMU, with the output method set to DC Voltage. A voltage glitch may occur when you change the PPMU output voltage from a standard range to the extended voltage range, or vice-versa, while the PPMU is sourcing. NI recommends temporarily changing the selected_function property to Off before sourcing a voltage level that requires a range change.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ppmu_allow_extended_voltage_range`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.ppmu_allow_extended_voltage_range`
    '''
    ppmu_aperture_time = _attributes.AttributeViReal64(1150037)
    '''Type: float

    Specifies the measurement aperture time for the PPMU. The ppmu_aperture_time_units property sets the units of the PPMU aperture time.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ppmu_aperture_time`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.ppmu_aperture_time`
    '''
    ppmu_aperture_time_units = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.PPMUApertureTimeUnits, 1150038)
    '''Type: enums.PPMUApertureTimeUnits

    Specifies the units of the measurement aperture time for the PPMU.

    +-------------------------------+-----------------------------------------+
    | Defined Values:               |                                         |
    +===============================+=========================================+
    | PPMUApertureTimeUnits.SECONDS | Specifies the aperture time in seconds. |
    +-------------------------------+-----------------------------------------+

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ppmu_aperture_time_units`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.ppmu_aperture_time_units`
    '''
    ppmu_current_level = _attributes.AttributeViReal64(1150019)
    '''Type: float

    Specifies the current level, in amps, that the PPMU forces to the DUT. This property is applicable only when you set the ppmu_output_function property to DC Current. Specify valid values for the current level using the PPMU_ConfigureCurrentLevelRange method.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ppmu_current_level`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.ppmu_current_level`
    '''
    ppmu_current_level_range = _attributes.AttributeViReal64(1150020)
    '''Type: float

    Specifies the range of valid values for the current level, in amps, that the PPMU forces to the DUT. This property is applicable only when you set the ppmu_output_function property to DC Current.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ppmu_current_level_range`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.ppmu_current_level_range`
    '''
    ppmu_current_limit = _attributes.AttributeViReal64(1150054)
    '''Type: float

    Specifies the current limit, in amps, that the output cannot exceed while the PPMU forces voltage to the DUT. This property is applicable only when you set the ppmu_output_function property to DC Voltage. The PXIe-6570/6571 does not support the ppmu_current_limit property and only allows configuration of the ppmu_current_limit_range property.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ppmu_current_limit`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.ppmu_current_limit`
    '''
    ppmu_current_limit_behavior = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.PPMUCurrentLimitBehavior, 1150064)
    '''Type: enums.PPMUCurrentLimitBehavior

    Specifies how the output should behave when the current limit is reached.

    +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | Defined Values:                   |                                                                                                                                         |
    +===================================+=========================================================================================================================================+
    | PPMUCurrentLimitBehavior.REGULATE | Controls output current so that it does not exceed the current limit. Power continues to generate even if the current limit is reached. |
    +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ppmu_current_limit_behavior`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.ppmu_current_limit_behavior`
    '''
    ppmu_current_limit_range = _attributes.AttributeViReal64(1150017)
    '''Type: float

    Specifies the valid range, in amps, to which the current limit can be set while the PPMU forces voltage to the DUT. This property is applicable only when you set the ppmu_output_function property to DC Voltage.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ppmu_current_limit_range`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.ppmu_current_limit_range`
    '''
    ppmu_current_limit_supported = _attributes.AttributeViBoolean(1150055)
    '''Type: bool

    Returns whether the device supports configuration of a current limit when you set the ppmu_output_function property to DC Voltage.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ppmu_current_limit_supported`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.ppmu_current_limit_supported`
    '''
    ppmu_output_function = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.PPMUOutputFunction, 1150015)
    '''Type: enums.PPMUOutputFunction

    Specifies whether the PPMU forces voltage or current to the DUT.

    +----------------------------+--------------------------------------------+
    | Defined Values:            |                                            |
    +============================+============================================+
    | PPMUOutputFunction.VOLTAGE | Specifies the output method to DC Voltage. |
    +----------------------------+--------------------------------------------+
    | PPMUOutputFunction.CURRENT | Specifies the output method to DC Current. |
    +----------------------------+--------------------------------------------+

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ppmu_output_function`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.ppmu_output_function`
    '''
    ppmu_voltage_level = _attributes.AttributeViReal64(1150016)
    '''Type: float

    Specifies the voltage level, in volts, that the PPMU forces to the DUT. This property is applicable only when you set the ppmu_output_function property to DC Voltage.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ppmu_voltage_level`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.ppmu_voltage_level`
    '''
    ppmu_voltage_limit_high = _attributes.AttributeViReal64(1150022)
    '''Type: float

    Specifies the maximum voltage limit, or high clamp voltage (V :sub:`CH` ), in volts, at the pin when the PPMU forces current to the DUT. This property is applicable only when you set the ppmu_output_function property to DC Current.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ppmu_voltage_limit_high`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.ppmu_voltage_limit_high`
    '''
    ppmu_voltage_limit_low = _attributes.AttributeViReal64(1150021)
    '''Type: float

    Specifies the minimum voltage limit, or low clamp voltage (V :sub:`CL` ), in volts, at the pin when the PPMU forces current to the DUT. This property is applicable only when you set the ppmu_output_function property to DC Current.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].ppmu_voltage_limit_low`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.ppmu_voltage_limit_low`
    '''
    query_instrument_status = _attributes.AttributeViBoolean(1050003)
    '''Type: bool

    Specifies whether the NI-Digital Pattern Driver queries the digital pattern instrument status after each operation. The instrument status is always queried, regardless of the property setting.
    '''
    range_check = _attributes.AttributeViBoolean(1050002)
    '''Type: bool

    Checks the range and validates parameter and property values you pass to NI-Digital Pattern Driver methods. Ranges are always checked, regardless of the property setting.
    '''
    record_coercions = _attributes.AttributeViBoolean(1050006)
    '''Type: bool

    Specifies whether the IVI engine keeps a list of the value coercions it makes for integer and real type properties. Enabling record value coercions is not supported.
    '''
    rio_event_terminal_name = _attributes.AttributeViString(1150091)
    '''Type: str

    Specifies the terminal name for the output signal of the specified instance of a RIO Event. You can use this terminal name as an input signal source for another trigger.

    Tip:
    This property can be set/get on specific rio_events within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container rio_events to specify a subset.

    Example: :py:attr:`my_session.rio_events[ ... ].rio_event_terminal_name`

    To set/get on all rio_events, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.rio_event_terminal_name`
    '''
    rio_trigger_terminal_name = _attributes.AttributeViString(1150089)
    '''Type: str

    Specifies the terminal name from which the exported RIO trigger signal may be routed to other instruments through the PXI trigger bus. You can use this signal to trigger other instruments when the RIO trigger instance asserts on the digital pattern instrument.

    Tip:
    This property can be set/get on specific rio_triggers within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container rio_triggers to specify a subset.

    Example: :py:attr:`my_session.rio_triggers[ ... ].rio_trigger_terminal_name`

    To set/get on all rio_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.rio_trigger_terminal_name`
    '''
    rio_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerType, 1150086)
    '''Type: enums.TriggerType

    Disables the rio trigger or configures it for hardware triggering.  The default value is TriggerType.NONE.

    +--------------------------+------------------------------------------------------------------+
    | Valid Values:            |                                                                  |
    +==========================+==================================================================+
    | TriggerType.NONE         | Disables the conditional jump trigger.                           |
    +--------------------------+------------------------------------------------------------------+
    | TriggerType.DIGITAL_EDGE | Configures the conditional jump trigger for hardware triggering. |
    +--------------------------+------------------------------------------------------------------+

    Tip:
    This property can be set/get on specific rio_triggers within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container rio_triggers to specify a subset.

    Example: :py:attr:`my_session.rio_triggers[ ... ].rio_trigger_type`

    To set/get on all rio_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.rio_trigger_type`
    '''
    selected_function = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.SelectedFunction, 1150004)
    '''Type: enums.SelectedFunction

    Caution: In the Disconnect state, some I/O protection and sensing circuitry remains exposed. Do not subject the instrument to voltage beyond its operating range.

    Specifies whether digital pattern instrument channels are controlled by the pattern sequencer or PPMU, disconnected, or off.

    +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Defined Values:             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
    +=============================+==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
    | SelectedFunction.DIGITAL    | The pin is connected to the driver, comparator, and active load methods. The PPMU is not sourcing, but can make voltage measurements. The state of the digital pin driver when you change the selected_function to Digital is determined by the most recent call to the write_static method or the last vector of the most recently executed pattern burst, whichever happened last. Use the write_static method to control the state of the digital pin driver through software. Use the burst_pattern method to control the state of the digital pin driver through a pattern. Set the **selectDigitalFunction** parameter of the burst_pattern method to True to automatically switch the selected_function of the pins in the pattern burst to SelectedFunction.DIGITAL. |
    +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | SelectedFunction.PPMU       | The pin is connected to the PPMU. The driver, comparator, and active load are off while this method is selected. Call the ppmu_source method to source a voltage or current. The ppmu_source method automatically switches the selected_function to the PPMU state and starts sourcing from the PPMU. Changing the selected_function to SelectedFunction.DISCONNECT, SelectedFunction.OFF, or SelectedFunction.DIGITAL causes the PPMU to stop sourcing. If you set the selected_function property to PPMU, the PPMU is initially not sourcing.                                                                                                                                                                                                                              |
    +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | SelectedFunction.OFF        | The pin is electrically connected, and the PPMU and digital pin driver are off while this method is selected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
    +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | SelectedFunction.DISCONNECT | The pin is electrically disconnected from instrument methods. Selecting this method causes the PPMU to stop sourcing prior to disconnecting the pin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
    +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    Note: You can make PPMU voltage measurements using the ppmu_measure method from within any selected_function.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].selected_function`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.selected_function`
    '''
    sequencer_flag_terminal_name = _attributes.AttributeViString(1150059)
    '''Type: str

    Specifies the terminal name for the output trigger signal of the Sequencer Flags trigger. You can use this terminal name as an input signal source for another trigger.
    '''
    serial_number = _attributes.AttributeViString(1150001)
    '''Type: str

    Returns the serial number of the device.

    Tip:
    This property can be set/get on specific instruments within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container instruments to specify a subset.

    Example: :py:attr:`my_session.instruments[ ... ].serial_number`

    To set/get on all instruments, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.serial_number`
    '''
    simulate = _attributes.AttributeViBoolean(1050005)
    '''Type: bool

    Simulates I/O operations. After you open a session, you cannot change the simulation state. Use the __init__ method to enable simulation.
    '''
    specific_driver_class_spec_major_version = _attributes.AttributeViInt32(1050515)
    '''Type: int

    Returns the major version number of the class specification with which NI-Digital is compliant. This property is not supported.
    '''
    specific_driver_class_spec_minor_version = _attributes.AttributeViInt32(1050516)
    '''Type: int

    Returns the minor version number of the class specification with which NI-Digital is compliant. This property is not supported.
    '''
    specific_driver_description = _attributes.AttributeViString(1050514)
    '''Type: str

    Returns a string that contains a brief description of the NI-Digital Pattern driver.
    '''
    specific_driver_prefix = _attributes.AttributeViString(1050302)
    '''Type: str

    Returns a string that contains the prefix for the NI-Digital Pattern driver.
    '''
    specific_driver_revision = _attributes.AttributeViString(1050551)
    '''Type: str

    Returns a string that contains additional version information about the NI-Digital Pattern Driver. For example, the driver can return Driver: NI-Digital 16.0 as the value of this property.
    '''
    specific_driver_vendor = _attributes.AttributeViString(1050513)
    '''Type: str

    Returns a string ("National Instruments") that contains the name of the vendor that supplies the NI-Digital Pattern Driver.
    '''
    start_label = _attributes.AttributeViString(1150023)
    '''Type: str

    Specifies the pattern name or exported pattern label from which to start bursting the pattern.
    '''
    start_trigger_terminal_name = _attributes.AttributeViString(1150039)
    '''Type: str

    Specifies the terminal name for the output trigger signal of the Start trigger. You can use this terminal name as an input signal source for another trigger.
    '''
    start_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerType, 1150029)
    '''Type: enums.TriggerType

    Specifies the Start trigger type. The digital pattern instrument waits for this trigger after you call the init method or the burst_pattern method, and does not burst a pattern until this trigger is received.

    +--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Defined Values:          |                                                                                                                                                                                                                                                                                                        |
    +==========================+========================================================================================================================================================================================================================================================================================================+
    | TriggerType.NONE         | Disables the Start trigger. Pattern bursting starts immediately after you call the init method or the burst_pattern method.                                                                                                                                                                            |
    +--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | TriggerType.DIGITAL_EDGE | Pattern bursting does not start until the digital pattern instrument detects a digital edge.                                                                                                                                                                                                           |
    +--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | TriggerType.SOFTWARE     | Pattern bursting does not start until the digital pattern instrument receives a software Start trigger. Create a software Start trigger by calling the send_software_edge_trigger method and selecting start trigger in the **trigger** parameter.Related information: SendSoftwareEdgeTrigger method. |
    +--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    Note:
    One or more of the referenced methods are not in the Python API for this driver.
    '''
    supported_instrument_models = _attributes.AttributeViString(1050327)
    '''Type: str

    Returns a comma delimited string that contains the supported digital pattern instrument models for the specific driver.
    '''
    tdr_endpoint_termination = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TDREndpointTermination, 1150081)
    '''Type: enums.TDREndpointTermination

    Specifies whether TDR Channels are connected to an open circuit or a short to ground.
    '''
    tdr_offset = _attributes.AttributeViReal64TimeDeltaSeconds(1150051)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the TDR Offset.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].tdr_offset`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.tdr_offset`
    '''
    termination_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TerminationMode, 1150006)
    '''Type: enums.TerminationMode

    Specifies the behavior of the pin during non-drive cycles.

    +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Defined Values:             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
    +=============================+======================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
    | TerminationMode.ACTIVE_LOAD | Specifies that, for non-drive pin states (L, H, X, V, M, E), the active load is connected and the instrument sources or sinks a defined amount of current to load the DUT. The amount of current sourced by the instrument and therefore sunk by the DUT is specified by IOL. The amount of current sunk by the instrument and therefore sourced by the DUT is specified by IOH. The voltage at which the instrument changes between sourcing and sinking is specified by VCOM.                                                                                                                                                                                                                                                                                                                                                                                      |
    +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | TerminationMode.VTERM       | Specifies that, for non-drive pin states (L, H, X, V, M, E), the pin driver terminates the pin to the configured VTERM voltage through a 50 Ω impedance. VTERM is adjustable to allow for the pin to terminate at a set level. This is useful for instruments that might operate incorrectly if an instrument pin is unterminated and is allowed to float to any voltage level within the instrument voltage range. To address this issue, enable VTERM by configuring the VTERM pin level to the desired voltage and selecting the VTERM termination mode. Setting VTERM to 0 V and selecting the VTERM termination mode has the effect of connecting a 50 Ω termination to ground, which provides an effective 50 Ω impedance for the pin. This can be useful for improving signal integrity of certain DUTs by reducing reflections while the DUT drives the pin. |
    +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | TerminationMode.HIGH_Z      | Specifies that, for non-drive pin states (L, H, X, V, M, E), the pin driver is put in a high-impedance state and the active load is disabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
    +-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].termination_mode`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.termination_mode`
    '''
    timing_absolute_delay = _attributes.AttributeViReal64TimeDeltaSeconds(1150072)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies a timing delay, measured in seconds, and applies the delay to the digital pattern instrument in addition to TDR and calibration adjustments. If the timing_absolute_delay_enabled property is set to True, this value is the intermodule skew measured by NI-TClk. You can modify this value to override the timing delay and align the I/O timing of this instrument with another instrument that shares the same reference clock. If the timing_absolute_delay_enabled property is False, this property will return 0.0. Changing the timing_absolute_delay_enabled property from False to True will set the timing_absolute_delay value back to your previously set value.

    Tip:
    This property can be set/get on specific instruments within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container instruments to specify a subset.

    Example: :py:attr:`my_session.instruments[ ... ].timing_absolute_delay`

    To set/get on all instruments, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.timing_absolute_delay`
    '''
    timing_absolute_delay_enabled = _attributes.AttributeViBoolean(1150071)
    '''Type: bool

    Specifies whether the timing_absolute_delay property should be applied to adjust the digital pattern instrument timing reference relative to other instruments in the system. Do not use this feature with digital pattern instruments in a Semiconductor Test System (STS). Timing absolute delay conflicts with the adjustment performed during STS timing calibration. When set to True, the digital pattern instrument automatically adjusts the timing absolute delay to correct the instrument timing reference relative to other instruments in the system for better timing alignment among synchronized instruments.
    '''
    vih = _attributes.AttributeViReal64(1150008)
    '''Type: float

    Specifies the voltage that the digital pattern instrument will apply to the input of the DUT when the test instrument drives a logic high (1).

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].vih`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.vih`
    '''
    vil = _attributes.AttributeViReal64(1150007)
    '''Type: float

    Specifies the voltage that the digital pattern instrument will apply to the input of the DUT when the test instrument drives a logic low (0).

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].vil`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.vil`
    '''
    voh = _attributes.AttributeViReal64(1150010)
    '''Type: float

    Specifies the output voltage from the DUT above which the comparator on the digital pattern test instrument interprets a logic high (H).

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].voh`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.voh`
    '''
    vol = _attributes.AttributeViReal64(1150009)
    '''Type: float

    Specifies the output voltage from the DUT below which the comparator on the digital pattern test instrument interprets a logic low (L).

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].vol`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.vol`
    '''
    vterm = _attributes.AttributeViReal64(1150011)
    '''Type: float

    Specifies the termination voltage the digital pattern instrument applies during non-drive cycles when the termination mode is set to V :sub:`term`. The instrument applies the termination voltage through a 50 Ω parallel termination resistance.

    Tip:
    This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
    Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].vterm`

    To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

    Example: :py:attr:`my_session.vterm`
    '''

    def __init__(self, repeated_capability_list, all_channels_in_session, interpreter, freeze_it=False):
        self._repeated_capability_list = repeated_capability_list
        self._repeated_capability = ','.join(repeated_capability_list)
        self._all_channels_in_session = all_channels_in_session
        self._interpreter = interpreter

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("repeated_capability_list=" + pp.pformat(repeated_capability_list))
        param_list.append("interpreter=" + pp.pformat(interpreter))
        self._param_list = ', '.join(param_list)

        # Instantiate any repeated capability objects
        self.channels = _RepeatedCapabilities(self, '', repeated_capability_list)
        self.pins = _RepeatedCapabilities(self, '', repeated_capability_list)
        self.instruments = _RepeatedCapabilities(self, '', repeated_capability_list)
        self.pattern_opcode_events = _RepeatedCapabilities(self, 'patternOpcodeEvent', repeated_capability_list)
        self.conditional_jump_triggers = _RepeatedCapabilities(self, 'conditionalJumpTrigger', repeated_capability_list)
        self.sites = _RepeatedCapabilities(self, 'site', repeated_capability_list)
        self.rio_events = _RepeatedCapabilities(self, 'RIOEvent', repeated_capability_list)
        self.rio_triggers = _RepeatedCapabilities(self, 'RIOTrigger', repeated_capability_list)

        # Finally, set _is_frozen to True which is used to prevent clients from accidentally adding
        # members when trying to set a property with a typo.
        self._is_frozen = freeze_it

    def __repr__(self):
        return '{0}.{1}({2})'.format('nidigital', self.__class__.__name__, self._param_list)

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("'{0}' object has no attribute '{1}'".format(type(self).__name__, key))
        object.__setattr__(self, key, value)

    ''' These are code-generated '''

    @ivi_synchronized
    def apply_levels_and_timing(self, levels_sheet, timing_sheet, initial_state_high_pins=None, initial_state_low_pins=None, initial_state_tristate_pins=None):
        r'''apply_levels_and_timing

        Applies digital levels and timing values defined in previously loaded levels and timing sheets. When applying a levels sheet, only the levels specified in the sheet are affected. Any levels not specified in the sheet remain unchanged. When applying a timing sheet, all existing time sets are deleted before the new time sets are loaded.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].apply_levels_and_timing`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.apply_levels_and_timing`

        Args:
            levels_sheet (str): Name of the levels sheet to apply. Use the name of the sheet or pass the absolute file path you use in the load_specifications_levels_and_timing method. The name of the levels sheet is the file name without the directory and file extension.

            timing_sheet (str): Name of the timing sheet to apply. Use the name of the sheet or pass the absolute file path that you use in the load_specifications_levels_and_timing method. The name of the timing sheet is the file name without the directory and file extension.

            initial_state_high_pins (basic sequence types or str): Comma-delimited list of pins, pin groups, or channels to initialize to a high state.

            initial_state_low_pins (basic sequence types or str): Comma-delimited list of pins, pin groups, or channels to initialize to a low state.

            initial_state_tristate_pins (basic sequence types or str): Comma-delimited list of pins, pin groups, or channels to initialize to a non-drive state (X)

        '''
        initial_state_high_pins = _converters.convert_repeated_capabilities_without_prefix(initial_state_high_pins)
        initial_state_low_pins = _converters.convert_repeated_capabilities_without_prefix(initial_state_low_pins)
        initial_state_tristate_pins = _converters.convert_repeated_capabilities_without_prefix(initial_state_tristate_pins)
        self._interpreter.apply_levels_and_timing(self._repeated_capability, levels_sheet, timing_sheet, initial_state_high_pins, initial_state_low_pins, initial_state_tristate_pins)

    @ivi_synchronized
    def apply_tdr_offsets(self, offsets):
        r'''apply_tdr_offsets

        Applies the correction for propagation delay offsets to a digital pattern instrument. Use this method to apply TDR offsets that are stored from a past measurement or are measured by means other than the tdr method. Also use this method to apply correction for offsets if the **applyOffsets** input of the tdr method was set to False at the time of measurement.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].apply_tdr_offsets`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.apply_tdr_offsets`

        Args:
            offsets (basic sequence of hightime.timedelta, datetime.timedelta, or float in seconds): TDR offsets to apply, in seconds. Specify an offset for each pin or channel in the repeated capabilities. If the repeated capabilities contain pin names, you must specify offsets for each site in the channel map per pin.

        '''
        offsets = _converters.convert_timedeltas_to_seconds_real64(offsets)
        self._interpreter.apply_tdr_offsets(self._repeated_capability, offsets)

    @ivi_synchronized
    def _burst_pattern(self, start_label, select_digital_function=True, wait_until_done=True, timeout=hightime.timedelta(seconds=10.0)):
        r'''_burst_pattern

        Uses the **startLabel** you specify to burst the pattern on the sites you specify and provides the option to wait for the burst to complete. Digital pins retain their state at the end of a pattern burst until the first vector of a subsequent pattern burst, a call to write_static, or a call to apply_levels_and_timing.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ]._burst_pattern`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._burst_pattern`

        Args:
            start_label (str): Pattern name or exported pattern label from which to start bursting the pattern.

            select_digital_function (bool): A Boolean that specifies whether to select the digital method for the pins in the pattern prior to bursting.

            wait_until_done (bool): A Boolean that indicates whether to wait until the bursting is complete.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): Maximum time (in seconds) allowed for this method to complete. If this method does not complete within this time interval, this method returns an error.

        '''
        timeout = _converters.convert_timedelta_to_seconds_real64(timeout)
        self._interpreter.burst_pattern(self._repeated_capability, start_label, select_digital_function, wait_until_done, timeout)

    @ivi_synchronized
    def clock_generator_abort(self):
        r'''clock_generator_abort

        Stops clock generation on the specified channel(s) or pin(s) and pin group(s).

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].clock_generator_abort`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.clock_generator_abort`
        '''
        self._interpreter.clock_generator_abort(self._repeated_capability)

    @ivi_synchronized
    def clock_generator_generate_clock(self, frequency, select_digital_function=True):
        r'''clock_generator_generate_clock

        Configures clock generator frequency and initiates clock generation on the specified channel(s) or pin(s) and pin group(s).

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].clock_generator_generate_clock`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.clock_generator_generate_clock`

        Args:
            frequency (float): The frequency of the clock generation, in Hz.

            select_digital_function (bool): A Boolean that specifies whether to select the digital method for the pins specified prior to starting clock generation.

        '''
        self._interpreter.clock_generator_generate_clock(self._repeated_capability, frequency, select_digital_function)

    @ivi_synchronized
    def configure_active_load_levels(self, iol, ioh, vcom):
        r'''configure_active_load_levels

        Configures I\ :sub:`OL`, I\ :sub:`OH`, and V\ :sub:`COM` levels for the active load on the pins you specify. The DUT sources or sinks current based on the level values. To enable active load, set the termination mode to TerminationMode.ACTIVE_LOAD. To disable active load, set the termination mode of the instrument to TerminationMode.HIGH_Z or TerminationMode.VTERM.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_active_load_levels`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_active_load_levels`

        Args:
            iol (float): Maximum current that the DUT sinks while outputting a voltage below V\ :sub:`COM`.

            ioh (float): Maximum current that the DUT sources while outputting a voltage above V\ :sub:`COM`.

            vcom (float): Commutating voltage level at which the active load circuit switches between sourcing current and sinking current.

        '''
        self._interpreter.configure_active_load_levels(self._repeated_capability, iol, ioh, vcom)

    @ivi_synchronized
    def configure_pattern_burst_sites(self):
        r'''configure_pattern_burst_sites

        Configures which sites burst the pattern on the next call to the initiate method. The pattern burst sites can also be modified through the repeated capabilities for the burst_pattern method. If a site has been disabled through the disable_sites method, the site does not burst a pattern even if included in the pattern burst sites.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].configure_pattern_burst_sites`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_pattern_burst_sites`
        '''
        self._interpreter.configure_pattern_burst_sites(self._repeated_capability)

    @ivi_synchronized
    def configure_time_set_compare_edges_strobe(self, time_set_name, strobe_edge):
        r'''configure_time_set_compare_edges_strobe

        Configures the strobe edge time for the specified pins. Use this method to modify time set values after applying a timing sheet with the apply_levels_and_timing method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to apply_levels_and_timing; it only affects the values of the current timing context.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].configure_time_set_compare_edges_strobe`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_time_set_compare_edges_strobe`

        Args:
            time_set_name (str): The specified time set name.

            strobe_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Time when the comparison happens within a vector period.

        '''
        strobe_edge = _converters.convert_timedelta_to_seconds_real64(strobe_edge)
        self._interpreter.configure_time_set_compare_edges_strobe(self._repeated_capability, time_set_name, strobe_edge)

    @ivi_synchronized
    def configure_time_set_compare_edges_strobe2x(self, time_set_name, strobe_edge, strobe2_edge):
        r'''configure_time_set_compare_edges_strobe2x

        Configures the compare strobes for the specified pins in the time set, including the 2x strobe. Use this method to modify time set values after applying a timing sheet with the apply_levels_and_timing method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to apply_levels_and_timing; it only affects the values of the current timing context.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].configure_time_set_compare_edges_strobe2x`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_time_set_compare_edges_strobe2x`

        Args:
            time_set_name (str): The specified time set name.

            strobe_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Time when the comparison happens within a vector period.

            strobe2_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Time when the comparison happens for the second DUT cycle within a vector period.

        '''
        strobe_edge = _converters.convert_timedelta_to_seconds_real64(strobe_edge)
        strobe2_edge = _converters.convert_timedelta_to_seconds_real64(strobe2_edge)
        self._interpreter.configure_time_set_compare_edges_strobe2x(self._repeated_capability, time_set_name, strobe_edge, strobe2_edge)

    @ivi_synchronized
    def configure_time_set_drive_edges(self, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge):
        r'''configure_time_set_drive_edges

        Configures the drive format and drive edge placement for the specified pins. Use this method to modify time set values after applying a timing sheet with the apply_levels_and_timing method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to apply_levels_and_timing; it only affects the values of the current timing context.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].configure_time_set_drive_edges`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_time_set_drive_edges`

        Args:
            time_set_name (str): The specified time set name.

            format (enums.DriveFormat): Drive format of the time set.

                -   DriveFormat.NR: Non-return.
                -   DriveFormat.RL: Return to low.
                -   DriveFormat.RH: Return to high.
                -   DriveFormat.SBC: Surround by complement.

            drive_on_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period for turning on the pin driver.This option applies only when the prior vector left the pin in a non-drive pin state (L, H, X, V, M, E). For the SBC format, this option specifies the delay from the beginning of the vector period at which the complement of the pattern value is driven.

            drive_data_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period until the pattern data is driven to the pattern value.The ending state from the previous vector persists until this point.

            drive_return_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period until the pin changes from the pattern data to the return value, as specified in the format.

            drive_off_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period to turn off the pin driver when the next vector period uses a non-drive symbol (L, H, X, V, M, E).

        '''
        if type(format) is not enums.DriveFormat:
            raise TypeError('Parameter format must be of type ' + str(enums.DriveFormat))
        drive_on_edge = _converters.convert_timedelta_to_seconds_real64(drive_on_edge)
        drive_data_edge = _converters.convert_timedelta_to_seconds_real64(drive_data_edge)
        drive_return_edge = _converters.convert_timedelta_to_seconds_real64(drive_return_edge)
        drive_off_edge = _converters.convert_timedelta_to_seconds_real64(drive_off_edge)
        self._interpreter.configure_time_set_drive_edges(self._repeated_capability, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge)

    @ivi_synchronized
    def configure_time_set_drive_edges2x(self, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge, drive_data2_edge, drive_return2_edge):
        r'''configure_time_set_drive_edges2x

        Configures the drive edges of the pins in the time set, including 2x edges. Use this method to modify time set values after applying a timing sheet with the apply_levels_and_timing method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to apply_levels_and_timing; it only affects the values of the current timing context.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].configure_time_set_drive_edges2x`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_time_set_drive_edges2x`

        Args:
            time_set_name (str): The specified time set name.

            format (enums.DriveFormat): Drive format of the time set.

                -   DriveFormat.NR: Non-return.
                -   DriveFormat.RL: Return to low.
                -   DriveFormat.RH: Return to high.
                -   DriveFormat.SBC: Surround by complement.

            drive_on_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period for turning on the pin driver.This option applies only when the prior vector left the pin in a non-drive pin state (L, H, X, V, M, E). For the SBC format, this option specifies the delay from the beginning of the vector period at which the complement of the pattern value is driven.

            drive_data_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period until the pattern data is driven to the pattern value.The ending state from the previous vector persists until this point.

            drive_return_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period until the pin changes from the pattern data to the return value, as specified in the format.

            drive_off_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period to turn off the pin driver when the next vector period uses a non-drive symbol (L, H, X, V, M, E).

            drive_data2_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period until the pattern data in the second DUT cycle is driven to the pattern value.

            drive_return2_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period until the pin changes from the pattern data in the second DUT cycle to the return value, as specified in the format.

        '''
        if type(format) is not enums.DriveFormat:
            raise TypeError('Parameter format must be of type ' + str(enums.DriveFormat))
        drive_on_edge = _converters.convert_timedelta_to_seconds_real64(drive_on_edge)
        drive_data_edge = _converters.convert_timedelta_to_seconds_real64(drive_data_edge)
        drive_return_edge = _converters.convert_timedelta_to_seconds_real64(drive_return_edge)
        drive_off_edge = _converters.convert_timedelta_to_seconds_real64(drive_off_edge)
        drive_data2_edge = _converters.convert_timedelta_to_seconds_real64(drive_data2_edge)
        drive_return2_edge = _converters.convert_timedelta_to_seconds_real64(drive_return2_edge)
        self._interpreter.configure_time_set_drive_edges2x(self._repeated_capability, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge, drive_data2_edge, drive_return2_edge)

    @ivi_synchronized
    def configure_time_set_drive_format(self, time_set_name, drive_format):
        r'''configure_time_set_drive_format

        Configures the drive format for the pins specified in the **pinList**. Use this method to modify time set values after applying a timing sheet with the apply_levels_and_timing method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to apply_levels_and_timing; it only affects the values of the current timing context.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].configure_time_set_drive_format`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_time_set_drive_format`

        Args:
            time_set_name (str): The specified time set name.

            drive_format (enums.DriveFormat): Drive format of the time set.

                -   DriveFormat.NR: Non-return.
                -   DriveFormat.RL: Return to low.
                -   DriveFormat.RH: Return to high.
                -   DriveFormat.SBC: Surround by complement.

        '''
        if type(drive_format) is not enums.DriveFormat:
            raise TypeError('Parameter drive_format must be of type ' + str(enums.DriveFormat))
        self._interpreter.configure_time_set_drive_format(self._repeated_capability, time_set_name, drive_format)

    @ivi_synchronized
    def configure_time_set_edge(self, time_set_name, edge, time):
        r'''configure_time_set_edge

        Configures the edge placement for the pins specified in the pin list. Use this method to modify time set values after applying a timing sheet with the apply_levels_and_timing method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to apply_levels_and_timing; it only affects the values of the current timing context.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].configure_time_set_edge`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_time_set_edge`

        Args:
            time_set_name (str): The specified time set name.

            edge (enums.TimeSetEdgeType): Name of the edge.

                -   TimeSetEdgeType.DRIVE_ON
                -   TimeSetEdgeType.DRIVE_DATA
                -   TimeSetEdgeType.DRIVE_RETURN
                -   TimeSetEdgeType.DRIVE_OFF
                -   TimeSetEdgeType.COMPARE_STROBE
                -   TimeSetEdgeType.DRIVE_DATA2
                -   TimeSetEdgeType.DRIVE_RETURN2
                -   TimeSetEdgeType.COMPARE_STROBE2

            time (hightime.timedelta, datetime.timedelta, or float in seconds): The time from the beginning of the vector period in which to place the edge.

        '''
        if type(edge) is not enums.TimeSetEdgeType:
            raise TypeError('Parameter edge must be of type ' + str(enums.TimeSetEdgeType))
        time = _converters.convert_timedelta_to_seconds_real64(time)
        self._interpreter.configure_time_set_edge(self._repeated_capability, time_set_name, edge, time)

    @ivi_synchronized
    def configure_time_set_edge_multiplier(self, time_set_name, edge_multiplier):
        r'''configure_time_set_edge_multiplier

        Configures the edge multiplier of the pins in the time set. Use this method to modify time set values after applying a timing sheet with the apply_levels_and_timing method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to apply_levels_and_timing; it only affects the values of the current timing context.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].configure_time_set_edge_multiplier`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_time_set_edge_multiplier`

        Args:
            time_set_name (str): The specified time set name.

            edge_multiplier (int): The specified edge multiplier for the pins in the pin list.

        '''
        self._interpreter.configure_time_set_edge_multiplier(self._repeated_capability, time_set_name, edge_multiplier)

    @ivi_synchronized
    def configure_voltage_levels(self, vil, vih, vol, voh, vterm):
        r'''configure_voltage_levels

        Configures voltage levels for the pins you specify.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_voltage_levels`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_voltage_levels`

        Args:
            vil (float): Voltage that the instrument will apply to the input of the DUT when the pin driver drives a logic low (0).

            vih (float): Voltage that the instrument will apply to the input of the DUT when the test instrument drives a logic high (1).

            vol (float): Output voltage below which the comparator on the pin driver interprets a logic low (L).

            voh (float): Output voltage above which the comparator on the pin driver interprets a logic high (H).

            vterm (float): Termination voltage the instrument applies during non-drive cycles when the termination mode is set to V\ :sub:`term`. The instrument applies the termination voltage through a 50 ohm parallel termination resistance.

        '''
        self._interpreter.configure_voltage_levels(self._repeated_capability, vil, vih, vol, voh, vterm)

    @ivi_synchronized
    def create_capture_waveform_parallel(self, waveform_name):
        r'''create_capture_waveform_parallel

        Sets the capture waveform settings for parallel acquisition. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].create_capture_waveform_parallel`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.create_capture_waveform_parallel`

        Args:
            waveform_name (str): Waveform name you want to use. Use the waveform_name with the capture_start opcode in your pattern.

        '''
        self._interpreter.create_capture_waveform_parallel(self._repeated_capability, waveform_name)

    @ivi_synchronized
    def create_capture_waveform_serial(self, waveform_name, sample_width, bit_order):
        r'''create_capture_waveform_serial

        Sets the capture waveform settings for serial acquisition. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].create_capture_waveform_serial`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.create_capture_waveform_serial`

        Args:
            waveform_name (str): Waveform name you want to use. Use the waveform_name with the capture_start opcode in your pattern.

            sample_width (int): Width in bits of each serial sample. Valid values are between 1 and 32.

            bit_order (enums.BitOrder): Order in which to shift the bits.

                -   BitOrder.MSB: Specifies the bit order by most significant bit first.
                -   BitOrder.LSB: Specifies the bit order by least significant bit first.

        '''
        if type(bit_order) is not enums.BitOrder:
            raise TypeError('Parameter bit_order must be of type ' + str(enums.BitOrder))
        self._interpreter.create_capture_waveform_serial(self._repeated_capability, waveform_name, sample_width, bit_order)

    @ivi_synchronized
    def create_source_waveform_parallel(self, waveform_name, data_mapping):
        r'''create_source_waveform_parallel

        Sets the source waveform settings required for parallel sourcing. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].create_source_waveform_parallel`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.create_source_waveform_parallel`

        Args:
            waveform_name (str): The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.

            data_mapping (enums.SourceDataMapping): Parameter that specifies how to map data on multiple sites.

                -   SourceDataMapping.BROADCAST: Broadcasts the waveform you specify to all sites.
                -   SourceDataMapping.SITE_UNIQUE: Sources unique waveform data to each site.

        '''
        if type(data_mapping) is not enums.SourceDataMapping:
            raise TypeError('Parameter data_mapping must be of type ' + str(enums.SourceDataMapping))
        self._interpreter.create_source_waveform_parallel(self._repeated_capability, waveform_name, data_mapping)

    @ivi_synchronized
    def create_source_waveform_serial(self, waveform_name, data_mapping, sample_width, bit_order):
        r'''create_source_waveform_serial

        Sets the source waveform settings required for serial sourcing. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].create_source_waveform_serial`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.create_source_waveform_serial`

        Args:
            waveform_name (str): The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.

            data_mapping (enums.SourceDataMapping): Parameter that specifies how to map data on multiple sites.

                -   SourceDataMapping.BROADCAST: Broadcasts the waveform you specify to all sites.
                -   SourceDataMapping.SITE_UNIQUE: Sources unique waveform data to each site.

            sample_width (int): Width in bits of each serial sample. Valid values are between 1 and 32.

            bit_order (enums.BitOrder): Order in which to shift the bits.

                -   BitOrder.MSB: Specifies the bit order by most significant bit first.
                -   BitOrder.LSB: Specifies the bit order by least significant bit first.

        '''
        if type(data_mapping) is not enums.SourceDataMapping:
            raise TypeError('Parameter data_mapping must be of type ' + str(enums.SourceDataMapping))
        if type(bit_order) is not enums.BitOrder:
            raise TypeError('Parameter bit_order must be of type ' + str(enums.BitOrder))
        self._interpreter.create_source_waveform_serial(self._repeated_capability, waveform_name, data_mapping, sample_width, bit_order)

    @ivi_synchronized
    def disable_sites(self):
        r'''disable_sites

        Disables specified sites. Disabled sites are not included in pattern bursts initiated by the initiate method or the burst_pattern method, even if the site is specified in the list of pattern burst sites in configure_pattern_burst_sites method or in the repeated capabilities for the burst_pattern method. Additionally, if you specify a list of pin or pin group names in repeated capabilities in any NI-Digital method, digital pattern instrument channels mapped to disabled sites are not affected by the method. The methods that return per-pin data, such as the ppmu_measure method, do not return data for channels mapped to disabled sites. The digital pattern instrument channels mapped to the sites specified are left in their current state. NI TestStand Semiconductor Module requires all sites to always be enabled, and manages the set of active sites without disabling the sites in the digital instrument session. Do not use this method with the Semiconductor Module.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].disable_sites`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.disable_sites`
        '''
        self._interpreter.disable_sites(self._repeated_capability)

    @ivi_synchronized
    def enable_sites(self):
        r'''enable_sites

        Enables the sites you specify. All sites are enabled by default.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].enable_sites`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.enable_sites`
        '''
        self._interpreter.enable_sites(self._repeated_capability)

    @ivi_synchronized
    def burst_pattern(self, start_label, select_digital_function=True, wait_until_done=True, timeout=hightime.timedelta(seconds=10.0)):
        '''burst_pattern

        Uses the start_label you specify to burst the pattern on the sites you specify. If you
        specify wait_until_done as True, waits for the burst to complete, and returns comparison results for each site.

        Digital pins retain their state at the end of a pattern burst until the first vector of the pattern burst, a call to
        write_static, or a call to apply_levels_and_timing.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].burst_pattern`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.burst_pattern`

        Args:
            start_label (str): Pattern name or exported pattern label from which to start bursting the pattern.

            select_digital_function (bool): A Boolean that specifies whether to select the digital method for the pins in the pattern prior to bursting.

            wait_until_done (bool): A Boolean that indicates whether to wait until the bursting is complete.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): Maximum time (in seconds) allowed for this method to complete. If this method does not complete within this time interval, this method returns an error.


        Returns:
            pass_fail ({ int: bool, int: bool, ... }): Dictionary where each key is a site number and value is pass/fail,
                if wait_until_done is specified as True. Else, None.

        '''
        self._burst_pattern(start_label, select_digital_function, wait_until_done, timeout)

        if wait_until_done:
            return self.get_site_pass_fail()
        else:
            return None

    @ivi_synchronized
    def fetch_capture_waveform(self, waveform_name, samples_to_read, timeout=hightime.timedelta(seconds=10.0)):
        '''fetch_capture_waveform

        Returns dictionary where each key is a site number and value is a collection of digital states representing capture waveform data

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].fetch_capture_waveform`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.fetch_capture_waveform`

        Args:
            waveform_name (str): Waveform name you create with the create capture waveform method. Use the waveform_name parameter with capture_start opcode in your pattern.

            samples_to_read (int): Number of samples to fetch.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): Maximum time (in seconds) allowed for this method to complete. If this method does not complete within this time interval, this method returns an error.


        Returns:
            waveform ({ int: memoryview of array.array of unsigned int, int: memoryview of array.array of unsigned int, ... }): Dictionary where each key is a site number and value is a collection of digital states representing capture waveform data

        '''
        timeout = _converters.convert_timedelta_to_seconds_real64(timeout)
        data, actual_num_waveforms, actual_samples_per_waveform = self._interpreter.fetch_capture_waveform(self._repeated_capability, waveform_name, samples_to_read, timeout)

        # Get the site list
        site_list = self._get_site_results_site_numbers(enums._SiteResultType.CAPTURE_WAVEFORM)
        assert len(site_list) == actual_num_waveforms

        waveforms = {}

        mv = memoryview(data)

        for i in range(actual_num_waveforms):
            start = i * actual_samples_per_waveform
            end = start + actual_samples_per_waveform
            waveforms[site_list[i]] = mv[start:end]

        return waveforms

    @ivi_synchronized
    def fetch_history_ram_cycle_information(self, position, samples_to_read):
        '''fetch_history_ram_cycle_information

        Returns the pattern information acquired for the specified cycles.

        If the pattern is using the edge multiplier feature, cycle numbers represent tester cycles, each of which may
        consist of multiple DUT cycles. When using pins with mixed edge multipliers, pins may return
        PinState.PIN_STATE_NOT_ACQUIRED for DUT cycles where those pins do not have edges defined.

        Site number on which to retrieve pattern information must be specified via sites repeated capability.
        The method returns an error if more than one site is specified.

        Pins for which to retrieve pattern information must be specified via pins repeated capability.
        If pins are not specified, pin list from the pattern containing the start label is used. Call
        get_pattern_pin_names with the start label to retrieve the pins associated with the pattern burst:

        .. code:: python

         session.sites[0].pins['PinA', 'PinB'].fetch_history_ram_cycle_information(0, -1)

        Note:
        Before bursting a pattern, you must configure the History RAM trigger and specify which cycles to acquire.

        history_ram_trigger_type should be used to specify the trigger condition on which History RAM
        starts acquiring pattern information.

        If History RAM trigger is configured as HistoryRAMTriggerType.CYCLE_NUMBER,
        cycle_number_history_ram_trigger_cycle_number should be used to specify the cycle number on which
        History RAM starts acquiring pattern information.

        If History RAM trigger is configured as HistoryRAMTriggerType.PATTERN_LABEL,
        pattern_label_history_ram_trigger_label should be used to specify the pattern label from which to
        start acquiring pattern information.
        pattern_label_history_ram_trigger_vector_offset should be used to specify the number of vectors
        following the specified pattern label from which to start acquiring pattern information.
        pattern_label_history_ram_trigger_cycle_offset should be used to specify the number of cycles
        following the specified pattern label and vector offset from which to start acquiring pattern information.

        For all History RAM trigger conditions, history_ram_pretrigger_samples should be used to specify
        the number of samples to acquire before the trigger conditions are met. If you configure History RAM to only
        acquire failed cycles, you must set history_ram_pretrigger_samples to 0.

        history_ram_cycles_to_acquire should be used to specify which cycles History RAM acquires after
        the trigger conditions are met.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].fetch_history_ram_cycle_information`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.fetch_history_ram_cycle_information`

        Args:
            position (int): Sample index from which to start fetching pattern information.

            samples_to_read (int): Number of samples to fetch. A value of -1 specifies to fetch all available samples.


        Returns:
            history_ram_cycle_information (list of HistoryRAMCycleInformation): Returns a list of class instances with
                the following information about each pattern cycle:

                -  **pattern_name** (str)  Name of the pattern for the acquired cycle.
                -  **time_set_name** (str) Time set for the acquired cycle.
                -  **vector_number** (int) Vector number within the pattern for the acquired cycle. Vector numbers start
                   at 0 from the beginning of the pattern.
                -  **cycle_number** (int) Cycle number acquired by this History RAM sample. Cycle numbers start at 0
                   from the beginning of the pattern burst.
                -  **scan_cycle_number** (int) Scan cycle number acquired by this History RAM sample. Scan cycle numbers
                   start at 0 from the first cycle of the scan vector. Scan cycle numbers are -1 for cycles that do not
                   have a scan opcode.
                -  **expected_pin_states** (list of list of enums.PinState) Pin states as expected by the loaded
                   pattern in the order specified in the pin list. Pins without defined edges in the specified DUT cycle
                   will have a value of PinState.PIN_STATE_NOT_ACQUIRED.
                   Length of the outer list will be equal to the value of edge multiplier for the given vector.
                   Length of the inner list will be equal to the number of pins requested.
                -  **actual_pin_states** (list of list of enums.PinState) Pin states acquired by History RAM in the
                   order specified in the pin list. Pins without defined edges in the specified DUT cycle will have a
                   value of PinState.PIN_STATE_NOT_ACQUIRED.
                   Length of the outer list will be equal to the value of edge multiplier for the given vector.
                   Length of the inner list will be equal to the number of pins requested.
                -  **per_pin_pass_fail** (list of list of bool) Pass fail information for pins in the order specified in
                   the pin list. Pins without defined edges in the specified DUT cycle will have a value of pass (True).
                   Length of the outer list will be equal to the value of edge multiplier for the given vector.
                   Length of the inner list will be equal to the number of pins requested.

        '''
        # Extract the site number and pin list from repeated capability
        repeated_capability_lists = _converters.convert_chained_repeated_capability_to_parts(self._repeated_capability)
        site = repeated_capability_lists[0]
        if not site.startswith('site'):
            raise ValueError('Site number on which to retrieve pattern information must be specified via sites repeated capability.')
        pins = '' if len(repeated_capability_lists) == 1 else repeated_capability_lists[1]

        # Put site back into repeated capability container; it will be used by other
        # sites-rep-cap-based methods that will be called later.
        self._repeated_capability = site

        if position < 0:
            raise ValueError('position should be greater than or equal to 0.')

        if samples_to_read < -1:
            raise ValueError('samples_to_read should be greater than or equal to -1.')

        # site is passed as repeated capability
        samples_available = self.get_history_ram_sample_count()
        if position > samples_available:
            raise ValueError('position: Specified value = {}, Maximum value = {}.'.format(position, samples_available - 1))

        if samples_to_read == -1:
            with _NoChannel(session=self):
                if not self.history_ram_number_of_samples_is_finite:
                    raise RuntimeError(
                        'Specifying -1 to fetch all History RAM samples is not supported when the digital pattern instrument is '
                        'configured for continuous History RAM acquisition. You must specify an exact number of samples to fetch.')
            samples_to_read = samples_available - position

        if position + samples_to_read > samples_available:
            raise ValueError(
                'position: Specified value = {}, samples_to_read: Specified value = {}; Samples available = {}.'
                .format(position, samples_to_read, samples_available - position))

        pattern_names = {}
        time_set_names = {}
        cycle_infos = []
        for _ in range(samples_to_read):

            # site is passed as repeated capability
            pattern_index, time_set_index, vector_number, cycle_number, num_dut_cycles = self._fetch_history_ram_cycle_information(position)

            if pattern_index not in pattern_names:
                # Repeated capability is not used
                pattern_names[pattern_index] = self._get_pattern_name(pattern_index)
            pattern_name = pattern_names[pattern_index]

            if time_set_index not in time_set_names:
                # Repeated capability is not used
                time_set_names[time_set_index] = self._get_time_set_name(time_set_index)
            time_set_name = time_set_names[time_set_index]

            # site is passed as repeated capability
            scan_cycle_number = self._fetch_history_ram_scan_cycle_number(position)

            vector_expected_pin_states = []
            vector_actual_pin_states = []
            vector_per_pin_pass_fail = []
            for dut_cycle_index in range(num_dut_cycles):
                # site is passed as repeated capability
                cycle_expected_pin_states, cycle_actual_pin_states, cycle_per_pin_pass_fail = self._fetch_history_ram_cycle_pin_data(pins, position, dut_cycle_index)
                vector_expected_pin_states.append(cycle_expected_pin_states)
                vector_actual_pin_states.append(cycle_actual_pin_states)
                vector_per_pin_pass_fail.append(cycle_per_pin_pass_fail)

            cycle_infos.append(history_ram_cycle_information.HistoryRAMCycleInformation(
                pattern_name=pattern_name,
                time_set_name=time_set_name,
                vector_number=vector_number,
                cycle_number=cycle_number,
                scan_cycle_number=scan_cycle_number,
                expected_pin_states=vector_expected_pin_states,
                actual_pin_states=vector_actual_pin_states,
                per_pin_pass_fail=vector_per_pin_pass_fail))
            position += 1

        return cycle_infos

    @ivi_synchronized
    def get_pin_results_pin_information(self):
        '''get_pin_results_pin_information

        Returns the pin names, site numbers, and channel names that correspond to per-pin data read from the digital pattern instrument. The method returns pin information in the same order as values read using the read_static method, ppmu_measure method, and get_fail_count method. Use this method to match values the previously listed methods return with pins, sites, and instrument channels.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].get_pin_results_pin_information`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.get_pin_results_pin_information`

        Returns:
            pin_info (list of PinInfo): List of named tuples with fields:

                - **pin_name** (str)
                - **site_number** (int)
                - **channel_name** (str)

        '''
        import collections
        PinInfo = collections.namedtuple('PinInformation', ['pin_name', 'site_number', 'channel_name'])

        pin_indexes, site_numbers, channel_indexes = self._get_pin_results_pin_information()
        assert len(pin_indexes) == len(site_numbers), "length of returned arrays don't match"
        assert len(pin_indexes) == len(channel_indexes), "length of returned arrays don't match"

        pin_infos = []
        for i in range(len(pin_indexes)):
            pin_name = "" if pin_indexes[i] == -1 else self._get_pin_name(pin_indexes[i])
            channel_names = self.get_channel_names(channel_indexes[i] - 1)  # channel_indexes are 1-based
            assert 1 == len(channel_names)
            pin_infos.append(PinInfo(pin_name=pin_name, site_number=site_numbers[i], channel_name=channel_names[0]))

        return pin_infos

    @ivi_synchronized
    def get_site_pass_fail(self):
        '''get_site_pass_fail

        Returns dictionary where each key is a site number and value is pass/fail

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].get_site_pass_fail`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.get_site_pass_fail`

        Returns:
            pass_fail ({ int: bool, int: bool, ... }): Dictionary where each key is a site number and value is pass/fail

        '''
        # For site_list, we just use the repeated capability
        result_list = self._get_site_pass_fail()
        site_list = self._get_site_results_site_numbers(enums._SiteResultType.PASS_FAIL)
        assert len(site_list) == len(result_list)

        return dict(zip(site_list, result_list))

    @ivi_synchronized
    def _fetch_history_ram_cycle_information(self, sample_index):
        r'''_fetch_history_ram_cycle_information

        Gets the per-cycle pattern information acquired for the specified cycle.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ]._fetch_history_ram_cycle_information`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._fetch_history_ram_cycle_information`

        Args:
            sample_index (int): The index of the History RAM sample to fetch. Each History RAM sample contains information about a single cycle in the pattern burst.


        Returns:
            pattern_index (int): The returned index of the pattern for the acquired cycle. Use _get_pattern_name to get the name of the pattern from its index.

            time_set_index (int): The returned time set for the acquired cycle. Use _get_time_set_name to get the name of the time set from its index.

            vector_number (int): The returned vector number within the pattern for the acquired cycle. Vector numbers start at 0 from the beginning of the pattern.

            cycle_number (int): Returns the cycle number acquired by this History RAM sample. Cycle numbers start at 0 from the beginning of the pattern burst.

            num_dut_cycles (int): The returned number of DUT cycles contained in the cycle acquired by this History RAM sample. This is only needed if the pattern uses the edge multiplier feature.

        '''
        pattern_index, time_set_index, vector_number, cycle_number, num_dut_cycles = self._interpreter.fetch_history_ram_cycle_information(self._repeated_capability, sample_index)
        return pattern_index, time_set_index, vector_number, cycle_number, num_dut_cycles

    @ivi_synchronized
    def _fetch_history_ram_cycle_pin_data(self, pin_list, sample_index, dut_cycle_index):
        r'''_fetch_history_ram_cycle_pin_data

        Gets the per-pin pattern data acquired for the specified cycle.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ]._fetch_history_ram_cycle_pin_data`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._fetch_history_ram_cycle_pin_data`

        Args:
            pin_list (str): The specified pins for which to retrieve History RAM data. If empty, the pin list from the pattern containing the start label is used. Call get_pattern_pin_names or GetPatternPinIndexeswith the start label to retrieve the pins associated with the pattern burst.

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

            sample_index (int): The index of the History RAM sample to fetch. Each History RAM sample contains information about a single cycle in the pattern burst.

            dut_cycle_index (int): The specified index of the DUT cycle. If the pattern does not use the edge multiplier feature, pass 0 for this parameter. For History RAM samples that contain multiple DUT cycles, indicated by the **numDutCycles** value returned by _fetch_history_ram_cycle_information, call this method multiple times to retrieve pin states for each DUT cycle. The DUT cycle index should start at 0.


        Returns:
            expected_pin_states (list of enums.PinState): The returned pin state as expected by the loaded pattern in the order specified in **pinList**. Pins without defined edges in the specified DUT cycle will return PinState.NOT_A_PIN_STATE

            actual_pin_states (list of enums.PinState): The returned pin state acquired by History RAM in the order specified in **pinList**. Pins without defined edges in the specified DUT cycle will return PinState.NOT_A_PIN_STATE

            per_pin_pass_fail (list of bool): The returned pass fail information for pins in the order specified in **pinList**. Pins without defined edges in the specified DUT cycle will return pass (True).

        '''
        expected_pin_states, actual_pin_states, per_pin_pass_fail = self._interpreter.fetch_history_ram_cycle_pin_data(self._repeated_capability, pin_list, sample_index, dut_cycle_index)
        return expected_pin_states, actual_pin_states, per_pin_pass_fail

    @ivi_synchronized
    def _fetch_history_ram_scan_cycle_number(self, sample_index):
        r'''_fetch_history_ram_scan_cycle_number

        Fetches the History RAM Scan Cycle Number for the sample index. If the sample is not from a scan vector, the scan cycle number will be returned as -1.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ]._fetch_history_ram_scan_cycle_number`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._fetch_history_ram_scan_cycle_number`

        Args:
            sample_index (int): The index of the History RAM sample to fetch. Each History RAM sample contains information about a single cycle in the pattern burst.


        Returns:
            scan_cycle_number (int): Returns the scan cycle number acquired by this History RAM sample. Scan cycle numbers start at 0 from the first cycle of the scan vector. Scan cycle numbers are -1 for cycles that do not have a scan opcode.

        '''
        scan_cycle_number = self._interpreter.fetch_history_ram_scan_cycle_number(self._repeated_capability, sample_index)
        return scan_cycle_number

    @ivi_synchronized
    def frequency_counter_measure_frequency(self):
        r'''frequency_counter_measure_frequency

        Measures the frequency on the specified channel(s) over the specified measurement time. All channels in the repeated capabilities should have the same measurement time.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].frequency_counter_measure_frequency`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.frequency_counter_measure_frequency`

        Returns:
            frequencies (list of float): The returned frequency counter measurement, in Hz.This method returns -1 if the measurement is invalid for the channel.

        '''
        frequencies = self._interpreter.frequency_counter_measure_frequency(self._repeated_capability)
        return frequencies

    @ivi_synchronized
    def _get_attribute_vi_boolean(self, attribute):
        r'''_get_attribute_vi_boolean

        Queries the value of a ViBoolean property. Use this method to get the values of digital pattern instrument-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_boolean`

        Args:
            attribute (int): The ID of a property.


        Returns:
            value (bool): The returned current value of the property; pass the address of a ViBoolean variable.

        '''
        value = self._interpreter.get_attribute_vi_boolean(self._repeated_capability, attribute)
        return value

    @ivi_synchronized
    def _get_attribute_vi_int32(self, attribute):
        r'''_get_attribute_vi_int32

        Queries the value of a ViInt32 property. Use this method to get the values of digital pattern instrument-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int32`

        Args:
            attribute (int): The ID of a property.


        Returns:
            value (int): The returned current value of the property; pass the address of a ViInt32 variable.

        '''
        value = self._interpreter.get_attribute_vi_int32(self._repeated_capability, attribute)
        return value

    @ivi_synchronized
    def _get_attribute_vi_int64(self, attribute):
        r'''_get_attribute_vi_int64

        Queries the value of a ViInt64 property. Use this method to get the values of digital pattern instrument-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int64`

        Args:
            attribute (int): The ID of a property.


        Returns:
            value (int): The returned current value of the property; pass the address of a ViInt64 variable.

        '''
        value = self._interpreter.get_attribute_vi_int64(self._repeated_capability, attribute)
        return value

    @ivi_synchronized
    def _get_attribute_vi_real64(self, attribute):
        r'''_get_attribute_vi_real64

        This method queries the value of a ViReal64 property. Use this method to get the values of digital pattern instrument-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_real64`

        Args:
            attribute (int): The ID of a property.


        Returns:
            value (float): The returned current value of the property; pass the address of a ViReal64 variable.

        '''
        value = self._interpreter.get_attribute_vi_real64(self._repeated_capability, attribute)
        return value

    @ivi_synchronized
    def _get_attribute_vi_string(self, attribute):
        r'''_get_attribute_vi_string

        Queries the value of a ViString property. Use this method to get the values of digital pattern instrument-specific properties and inherent IVI properties. You must provide a ViChar array to serve as a buffer for the value. You pass the number of bytes in the buffer as the **bufferSize**. If the current value of the property, including the terminating NULL byte, is larger than the size you indicate in the **bufferSize**, the method copies (bufferSize - 1) bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the **bufferSize** you must pass to get the entire value. For example, if the value is "123456" and the **bufferSize** is 4, the method places "123" into the buffer and returns 7. If you want to call this method just to get the required buffer size, you can pass 0 for the **bufferSize** and VI_NULL for the value.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_string`

        Args:
            attribute (int): The ID of a property.


        Returns:
            value (str): The buffer in which the method returns the current value of the property; the buffer must be of type ViChar and have at least as many bytes as indicated in the **bufferSize**.

        '''
        value = self._interpreter.get_attribute_vi_string(self._repeated_capability, attribute)
        return value

    @ivi_synchronized
    def get_channel_names(self, indices):
        r'''get_channel_names

        Returns a list of channel names for given channel indices.

        Args:
            indices (basic sequence types, str, or int): Index list for the channels in the session. Valid values are from zero to the total number of channels in the session minus one. The index string can be one of the following formats:

                -   A comma-separated list—for example, "0,2,3,1"
                -   A range using a hyphen—for example, "0-3"
                -   A range using a colon—for example, "0:3 "

                You can combine comma-separated lists and ranges that use a hyphen or colon. Both out-of-order and repeated indices are supported ("2,3,0", "1,2,2,3"). White space characters, including spaces, tabs, feeds, and carriage returns, are allowed between characters. Ranges can be incrementing or decrementing.


        Returns:
            names (list of str): The channel name(s) at the specified indices.

        '''
        indices = _converters.convert_repeated_capabilities_without_prefix(indices)
        names = self._interpreter.get_channel_names(indices)
        return _converters.convert_comma_separated_string_to_list(names)

    @ivi_synchronized
    def get_fail_count(self):
        r'''get_fail_count

        Returns the comparison fail count for pins in the repeated capabilities.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].get_fail_count`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.get_fail_count`

        Returns:
            failure_count (list of int): Number of failures in an array. If a site is disabled or not enabled for burst, the method does not return data for that site. You can also use the get_pin_results_pin_information method to obtain a sorted list of returned sites and channels.

        '''
        failure_count = self._interpreter.get_fail_count(self._repeated_capability)
        return failure_count

    @ivi_synchronized
    def get_history_ram_sample_count(self):
        r'''get_history_ram_sample_count

        Returns the number of samples History RAM acquired on the last pattern burst.

        Note:
        Before bursting a pattern, you must configure the History RAM trigger and specify which cycles to acquire.

        history_ram_trigger_type should be used to specify the trigger condition on which History RAM
        starts acquiring pattern information.

        If History RAM trigger is configured as HistoryRAMTriggerType.CYCLE_NUMBER,
        cycle_number_history_ram_trigger_cycle_number should be used to specify the cycle number on which
        History RAM starts acquiring pattern information.

        If History RAM trigger is configured as HistoryRAMTriggerType.PATTERN_LABEL,
        pattern_label_history_ram_trigger_label should be used to specify the pattern label from which to
        start acquiring pattern information.
        pattern_label_history_ram_trigger_vector_offset should be used to specify the number of vectors
        following the specified pattern label from which to start acquiring pattern information.
        pattern_label_history_ram_trigger_cycle_offset should be used to specify the number of cycles
        following the specified pattern label and vector offset from which to start acquiring pattern information.

        For all History RAM trigger conditions, history_ram_pretrigger_samples should be used to specify
        the number of samples to acquire before the trigger conditions are met. If you configure History RAM to only
        acquire failed cycles, you must set history_ram_pretrigger_samples to 0.

        history_ram_cycles_to_acquire should be used to specify which cycles History RAM acquires after
        the trigger conditions are met.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].get_history_ram_sample_count`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.get_history_ram_sample_count`

        Returns:
            sample_count (int): The returned number of samples that History RAM acquired.

        '''
        sample_count = self._interpreter.get_history_ram_sample_count(self._repeated_capability)
        return sample_count

    @ivi_synchronized
    def _get_pattern_name(self, pattern_index):
        r'''_get_pattern_name

        TBD

        Args:
            pattern_index (int):


        Returns:
            name (str):

        '''
        name = self._interpreter.get_pattern_name(pattern_index)
        return name

    @ivi_synchronized
    def _get_pin_name(self, pin_index):
        r'''_get_pin_name

        Returns the name of the pin at the index you specify. You must provide a ViChar array to serve as a buffer for the value. You pass the number of bytes in the buffer as the **nameBufferSize**. If the current value of the property, including the terminating NULL byte, is larger than the size you indicate in the buffer size, the method copies (buffer size - 1) bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the method places "123" into the buffer and returns 7. If you want to call this method just to get the required buffer size, you can pass 0 for **nameBufferSize** and VI_NULL for the name.

        Args:
            pin_index (int): Index of pin to query. Pin indexes begin at 0.


        Returns:
            name (str): Returns the pin name at the specified **pinIndex**.

        '''
        name = self._interpreter.get_pin_name(pin_index)
        return name

    @ivi_synchronized
    def _get_pin_results_pin_information(self):
        r'''_get_pin_results_pin_information

        Returns the pin names, site numbers, and channel names that correspond to per-pin data read from the digital pattern instrument. The method returns pin information in the same order as values read using the read_static method, ppmu_measure method, and get_fail_count method. Use this method to match values the previously listed methods return with pins, sites, and instrument channels.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_pin_results_pin_information`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._get_pin_results_pin_information`

        Returns:
            pin_indexes (list of int): The returned index of the pins corresponding to data read from the digital pattern instrument using the specified repeated capabilities. If you do not want to use this parameter, pass VI_NULL.
                Call _get_pin_name to get the name of the pin associated with an index.

            site_numbers (list of int): The returned site numbers that correspond to data read from the digital pattern instrument using the specified repeated capabilities. If you do not want to use this parameter, pass VI_NULL.

            channel_indexes (list of int): The returned index of channels corresponding to data read from the digital pattern instrument using the specified repeated capabilities. If you do not want to use this parameter, pass VI_NULL.
                Call GetChannelName to get the name of the channel associated with an index. Channel indexes are one-based.

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

        '''
        pin_indexes, site_numbers, channel_indexes = self._interpreter.get_pin_results_pin_information(self._repeated_capability)
        return pin_indexes, site_numbers, channel_indexes

    @ivi_synchronized
    def _get_site_pass_fail(self):
        r'''_get_site_pass_fail

        Returns the pass or fail results for each site.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ]._get_site_pass_fail`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._get_site_pass_fail`

        Returns:
            pass_fail (list of bool): The returned array of pass (True) and fail results for the sites you specify in the repeated capabilities. If sites span multiple digital pattern instruments, you must use an AND operator for the partial results for those sites returned by each instrument. If a site is disabled or not enabled for burst, the method does not return data for that site. Use the SortSiteResultsViBoolean method to order and combine the data to match the repeated capabilities. You can also use the _get_site_results_site_numbers method to determine the order of the sites returned from this method call so that you can match the pass array with site numbers.

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

        '''
        pass_fail = self._interpreter.get_site_pass_fail(self._repeated_capability)
        return pass_fail

    @ivi_synchronized
    def _get_site_results_site_numbers(self, site_result_type):
        r'''_get_site_results_site_numbers

        Returns the site numbers that correspond to per-site data read from the digital pattern instrument. The method returns site numbers in the same order as values read using the _get_site_pass_fail and fetch_capture_waveform_u32 methods. Use this method to match values the previously listed methods return with site numbers.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ]._get_site_results_site_numbers`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._get_site_results_site_numbers`

        Args:
            site_result_type (enums.SiteResultType): The type of data specified in the results array.

                -   _SiteResultType.PASS_FAIL: Get site numbers for pass/fail data.
                -   _SiteResultType.CAPTURE_WAVEFORM: Get site numbers for capture waveforms.


        Returns:
            site_numbers (list of int): The returned array of site numbers that correspond to the values specified by **siteResultType**.

        '''
        if type(site_result_type) is not enums._SiteResultType:
            raise TypeError('Parameter site_result_type must be of type ' + str(enums._SiteResultType))
        site_numbers = self._interpreter.get_site_results_site_numbers(self._repeated_capability, site_result_type)
        return site_numbers

    @ivi_synchronized
    def get_time_set_drive_format(self, time_set_name):
        r'''get_time_set_drive_format

        Returns the drive format of a pin in the specified time set.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].get_time_set_drive_format`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.get_time_set_drive_format`

        Args:
            time_set_name (str): The specified time set name.


        Returns:
            format (enums.DriveFormat): Returned drive format of the time set for the specified pin.

        '''
        format = self._interpreter.get_time_set_drive_format(self._repeated_capability, time_set_name)
        return format

    @ivi_synchronized
    def get_time_set_edge(self, time_set_name, edge):
        r'''get_time_set_edge

        Returns the edge time of a pin in the specified time set.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].get_time_set_edge`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.get_time_set_edge`

        Args:
            time_set_name (str): The specified time set name.

            edge (enums.TimeSetEdgeType): Name of the edge.

                -   TimeSetEdgeType.DRIVE_ON
                -   TimeSetEdgeType.DRIVE_DATA
                -   TimeSetEdgeType.DRIVE_RETURN
                -   TimeSetEdgeType.DRIVE_OFF
                -   TimeSetEdgeType.COMPARE_STROBE
                -   TimeSetEdgeType.DRIVE_DATA2
                -   TimeSetEdgeType.DRIVE_RETURN2
                -   TimeSetEdgeType.COMPARE_STROBE2


        Returns:
            time (hightime.timedelta): Time from the beginning of the vector period in which to place the edge.

        '''
        if type(edge) is not enums.TimeSetEdgeType:
            raise TypeError('Parameter edge must be of type ' + str(enums.TimeSetEdgeType))
        time = self._interpreter.get_time_set_edge(self._repeated_capability, time_set_name, edge)
        return _converters.convert_seconds_real64_to_timedelta(time)

    @ivi_synchronized
    def get_time_set_edge_multiplier(self, time_set_name):
        r'''get_time_set_edge_multiplier

        Returns the edge multiplier of the specified time set.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].get_time_set_edge_multiplier`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.get_time_set_edge_multiplier`

        Args:
            time_set_name (str): The specified time set name.


        Returns:
            edge_multiplier (int): Returned edge multiplier of the time set for the specified pin.

        '''
        edge_multiplier = self._interpreter.get_time_set_edge_multiplier(self._repeated_capability, time_set_name)
        return edge_multiplier

    @ivi_synchronized
    def _get_time_set_name(self, time_set_index):
        r'''_get_time_set_name

        TBD

        Args:
            time_set_index (int):


        Returns:
            name (str):

        '''
        name = self._interpreter.get_time_set_name(time_set_index)
        return name

    @ivi_synchronized
    def is_site_enabled(self):
        r'''is_site_enabled

        Checks if a specified site is enabled.

        Note: The method returns an error if more than one site is specified.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].is_site_enabled`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.is_site_enabled`

        Returns:
            enable (bool): Boolean value that returns whether the site is enabled or disabled.

        '''
        enable = self._interpreter.is_site_enabled(self._repeated_capability)
        return enable

    def lock(self):
        '''lock

        Obtains a multithread lock on the device session. Before doing so, the
        software waits until all other execution threads release their locks
        on the device session.

        Other threads may have obtained a lock on this session for the
        following reasons:

            -  The application called the lock method.
            -  A call to NI-Digital Pattern Driver locked the session.
            -  After a call to the lock method returns
               successfully, no other threads can access the device session until
               you call the unlock method or exit out of the with block when using
               lock context manager.
            -  Use the lock method and the
               unlock method around a sequence of calls to
               instrument driver methods if you require that the device retain its
               settings through the end of the sequence.

        You can safely make nested calls to the lock method
        within the same thread. To completely unlock the session, you must
        balance each call to the lock method with a call to
        the unlock method.

        Returns:
            lock (context manager): When used in a with statement, nidigital.Session.lock acts as
            a context manager and unlock will be called when the with block is exited
        '''
        self._interpreter.lock()  # We do not call this in the context manager so that this function can
        # act standalone as well and let the client call unlock() explicitly. If they do use the context manager,
        # that will handle the unlock for them
        return _Lock(self)

    @ivi_synchronized
    def ppmu_measure(self, measurement_type):
        r'''ppmu_measure

        Instructs the PPMU to measure voltage or current. This method can be called to take a voltage measurement even if the pin method is not set to PPMU.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].ppmu_measure`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.ppmu_measure`

        Args:
            measurement_type (enums.PPMUMeasurementType): Parameter that specifies whether the PPMU measures voltage or current from the DUT.

                -   PPMUMeasurementType.CURRENT: The PPMU measures current from the DUT.
                -   PPMUMeasurementType.VOLTAGE: The PPMU measures voltage from the DUT.


        Returns:
            measurements (list of float): The returned array of measurements in the order you specify in the repeated capabilities. If a site is disabled, the method does not return data for that site. You can also use the get_pin_results_pin_information method to obtain a sorted list of returned sites and channels.

        '''
        if type(measurement_type) is not enums.PPMUMeasurementType:
            raise TypeError('Parameter measurement_type must be of type ' + str(enums.PPMUMeasurementType))
        measurements = self._interpreter.ppmu_measure(self._repeated_capability, measurement_type)
        return measurements

    @ivi_synchronized
    def ppmu_source(self):
        r'''ppmu_source

        Starts sourcing voltage or current from the PPMU. This method automatically selects the PPMU method. Changes to PPMU source settings do not take effect until you call this method. If you modify source settings after you call this method, you must call this method again for changes in the configuration to take effect.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].ppmu_source`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.ppmu_source`
        '''
        self._interpreter.ppmu_source(self._repeated_capability)

    @ivi_synchronized
    def read_static(self):
        r'''read_static

        Reads the current state of comparators for pins you specify in the repeated capabilities. If there are uncommitted changes to levels or the termination mode, this method commits the changes to the pins.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].read_static`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.read_static`

        Returns:
            data (list of enums.PinState): The returned array of pin states read from the channels in the repeated capabilities. Data is returned in the order you specify in the repeated capabilities. If a site is disabled, the method does not return data for that site. You can also use the get_pin_results_pin_information method to obtain a sorted list of returned sites and channels.

                -   PinState.L: The comparators read a logic low pin state.
                -   PinState.H: The comparators read a logic high pin state.
                -   PinState.M: The comparators read a midband pin state.
                -   PinState.V: The comparators read a value that is above VOH and below VOL, which can occur when you set VOL higher than VOH.

        '''
        data = self._interpreter.read_static(self._repeated_capability)
        return data

    @ivi_synchronized
    def _set_attribute_vi_boolean(self, attribute, value):
        r'''_set_attribute_vi_boolean

        Sets the value of a ViBoolean property. Use this method to set the values of digital pattern instrument-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_boolean`

        Args:
            attribute (int): The ID of a property.

            value (bool): The value to which you want to set the property; some of the values might not be valid depending on the current settings of the instrument session.

        '''
        self._interpreter.set_attribute_vi_boolean(self._repeated_capability, attribute, value)

    @ivi_synchronized
    def _set_attribute_vi_int32(self, attribute, value):
        r'''_set_attribute_vi_int32

        Sets the value of a ViInt32 property. Use this method to set the values of digital pattern instrument-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int32`

        Args:
            attribute (int): The ID of a property.

            value (int): The value to which you want to set the property; some of the values might not be valid depending on the current settings of the instrument session.

        '''
        self._interpreter.set_attribute_vi_int32(self._repeated_capability, attribute, value)

    @ivi_synchronized
    def _set_attribute_vi_int64(self, attribute, value):
        r'''_set_attribute_vi_int64

        Sets the value of a ViInt64 property. Use this method to set the values of digital pattern instrument-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int64`

        Args:
            attribute (int): The ID of a property.

            value (int): The value to which you want to set the property; some of the values might not be valid depending on the current settings of the instrument session.

        '''
        self._interpreter.set_attribute_vi_int64(self._repeated_capability, attribute, value)

    @ivi_synchronized
    def _set_attribute_vi_real64(self, attribute, value):
        r'''_set_attribute_vi_real64

        Sets the value of a ViIntReal64 property. Use this method to set the values of digital pattern instrument-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_real64`

        Args:
            attribute (int): The ID of a property.

            value (float): The value to which you want to set the property; some of the values might not be valid depending on the current settings of the instrument session.

        '''
        self._interpreter.set_attribute_vi_real64(self._repeated_capability, attribute, value)

    @ivi_synchronized
    def _set_attribute_vi_string(self, attribute, value):
        r'''_set_attribute_vi_string

        Sets the value of a ViString property. Use this method to set the values of digital pattern instrument-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_string`

        Args:
            attribute (int): The ID of a property.

            value (str): The value to which you want to set the property; some of the values might not be valid depending on the current settings of the instrument session.

        '''
        self._interpreter.set_attribute_vi_string(self._repeated_capability, attribute, value)

    @ivi_synchronized
    def tdr(self, apply_offsets=True):
        r'''tdr

        Measures propagation delays through cables, connectors, and load boards using Time-Domain Reflectometry (TDR). Ensure that the channels and pins you select are connected to an open circuit.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].tdr`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.tdr`

        Args:
            apply_offsets (bool): A Boolean that specifies whether to apply the measured TDR offsets. If you need to adjust the measured offsets prior to applying, set this input to False, and call the apply_tdr_offsets method to specify the adjusted TDR offsets values.


        Returns:
            offsets (list of hightime.timedelta): Measured TDR offsets specified in seconds.

        '''
        offsets = self._interpreter.tdr(self._repeated_capability, apply_offsets)
        return _converters.convert_seconds_real64_to_timedeltas(offsets)

    def unlock(self):
        '''unlock

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        '''
        self._interpreter.unlock()

    @ivi_synchronized
    def _write_source_waveform_site_unique_u32(self, waveform_name, num_waveforms, samples_per_waveform, waveform_data):
        r'''_write_source_waveform_site_unique_u32

        Writes one waveform per site. Use this write method if you set the parameter of the create source waveform method to Site Unique.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ]._write_source_waveform_site_unique_u32`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._write_source_waveform_site_unique_u32`

        Args:
            waveform_name (str): The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.

            num_waveforms (int): Number of waveforms.

            samples_per_waveform (int): Number of samples per waveform.

            waveform_data (array.array("L")): An array of samples to use as source data. Data for each site must be appended sequentially in the array (non-interleaved).

        '''
        self._interpreter.write_source_waveform_site_unique_u32(self._repeated_capability, waveform_name, num_waveforms, samples_per_waveform, waveform_data)

    @ivi_synchronized
    def write_static(self, state):
        r'''write_static

        Writes a static state to the specified pins. The selected pins remain in the specified state until the next pattern burst or call to this method. If there are uncommitted changes to levels or the termination mode, this method commits the changes to the pins. This method does not change the selected pin method. If you write a static state to a pin that does not have the Digital method selected, the new static state is stored by the instrument, and affects the state of the pin the next time you change the selected method to Digital.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].write_static`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.write_static`

        Args:
            state (enums.WriteStaticPinState): Parameter that specifies one of the following digital states to assign to the pin.

                -   WriteStaticPinState.ZERO: Specifies to drive low.
                -   WriteStaticPinState.ONE: Specifies to drive high.
                -   WriteStaticPinState.X: Specifies to not drive.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        if type(state) is not enums.WriteStaticPinState:
            raise TypeError('Parameter state must be of type ' + str(enums.WriteStaticPinState))
        self._interpreter.write_static(self._repeated_capability, state)

    def _error_message(self, error_code):
        r'''_error_message

        Takes the error code returned by the digital pattern instrument driver methods, interprets it, and returns it as a user readable string.

        Args:
            error_code (int): The specified error code.


        Returns:
            error_message (str): The error information formatted as a string. The array must contain at least 256 characters.

        '''
        error_message = self._interpreter.error_message(error_code)
        return error_message


class Session(_SessionBase):
    '''An NI-Digital Pattern Driver session'''

    def __init__(self, resource_name, id_query=False, reset_device=False, options={}, *, grpc_options=None):
        r'''An NI-Digital Pattern Driver session

        Creates and returns a new session to the specified digital pattern instrument to use in all subsequent method calls. To place the instrument in a known startup state when creating a new session, set the reset parameter to True, which is equivalent to calling the reset method immediately after initializing the session.

        Args:
            resource_name (str): The specified resource name shown in Measurement & Automation Explorer (MAX) for a digital pattern instrument, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. **resourceName** can also be a logical IVI name. This parameter accepts a comma-delimited list of strings in the form PXI1Slot2,PXI1Slot3, where ``PXI1Slot2`` is one instrument resource name and ``PXI1Slot3`` is another. When including more than one digital pattern instrument in the comma-delimited list of strings, list the instruments in the same order they appear in the pin map.

                +--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | |Note| | Note   You only can specify multiple instruments of the same model. For example, you can list two PXIe-6570s but not a PXIe-6570 and PXIe-6571. The instruments must be in the same chassis. |
                +--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

                .. |Note| image:: note.gif

                Note:

            id_query (bool): A Boolean that verifies that the digital pattern instrument you initialize is supported by NI-Digital. NI-Digital automatically performs this query, so setting this parameter is not necessary.

            reset_device (bool): A Boolean that specifies whether to reset a digital pattern instrument to a known state when the session is initialized. Setting the **resetDevice** value to True is equivalent to calling the reset method immediately after initializing the session.

            options (dict): Specifies the initial value of certain properties for the session. The
                syntax for **options** is a dictionary of properties with an assigned
                value. For example:

                { 'simulate': False }

                You do not have to specify a value for all the properties. If you do not
                specify a value for a property, the default value is used.

                Advanced Example:
                { 'simulate': True, 'driver_setup': { 'Model': '<model number>',  'BoardType': '<type>' } }

                +-------------------------+---------+
                | Property                | Default |
                +=========================+=========+
                | range_check             | True    |
                +-------------------------+---------+
                | query_instrument_status | False   |
                +-------------------------+---------+
                | cache                   | True    |
                +-------------------------+---------+
                | simulate                | False   |
                +-------------------------+---------+
                | record_value_coersions  | False   |
                +-------------------------+---------+
                | driver_setup            | {}      |
                +-------------------------+---------+

            grpc_options (nidigital.grpc_session_options.GrpcSessionOptions): MeasurementLink gRPC session options


        Returns:
            new_vi (int): The returned instrument session.

        '''
        if grpc_options:
            import nidigital._grpc_stub_interpreter as _grpc_stub_interpreter
            interpreter = _grpc_stub_interpreter.GrpcStubInterpreter(grpc_options)
        else:
            interpreter = _library_interpreter.LibraryInterpreter(encoding='windows-1251')

        # Initialize the superclass with default values first, populate them later
        super(Session, self).__init__(
            repeated_capability_list=[],
            interpreter=interpreter,
            freeze_it=False,
            all_channels_in_session=None
        )
        options = _converters.convert_init_with_options_dictionary(options)

        # Call specified init function
        # Note that _interpreter default-initializes the session handle in its constructor, so that
        # if _init_with_options fails, the error handler can reference it.
        # And then here, once _init_with_options succeeds, we call set_session_handle
        # with the actual session handle.
        self._interpreter.set_session_handle(self._init_with_options(resource_name, id_query, reset_device, options))

        # NI-TClk does not work over NI gRPC Device Server
        if not grpc_options:
            self.tclk = nitclk.SessionReference(self._interpreter.get_session_handle())

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("resource_name=" + pp.pformat(resource_name))
        param_list.append("reset_device=" + pp.pformat(reset_device))
        param_list.append("options=" + pp.pformat(options))
        self._param_list = ', '.join(param_list)

        # Store the list of channels in the Session which is needed by some nimi-python modules.
        # Use try/except because not all the modules support channels.
        # self.get_channel_names() and self.channel_count can only be called after the session
        # handle is set
        try:
            self._all_channels_in_session = self.get_channel_names(range(self.channel_count))
        except AttributeError:
            self._all_channels_in_session = None

        # Finally, set _is_frozen to True which is used to prevent clients from accidentally adding
        # members when trying to set a property with a typo.
        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self._interpreter._close_on_exit:
            self.close()

    def initiate(self):
        '''initiate

        Starts bursting the pattern configured by start_label, causing the NI-Digital session to be committed. To stop the pattern burst, call abort. If keep alive pattern is bursting when abort is called or upon exiting the context manager, keep alive pattern will not be stopped. To stop the keep alive pattern, call abort_keep_alive.

        Note:
        This method will return a Python context manager that will initiate on entering and abort on exit.
        '''
        return _Burst(self)

    def close(self):
        '''close

        Closes the specified instrument session to a digital pattern instrument, aborts pattern execution, and unloads pattern memory. The channels on a digital pattern instrument remain in their current state.

        Note:
        This method is not needed when using the session context manager
        '''
        try:
            self._close()
        except errors.DriverError:
            self._interpreter.set_session_handle()
            raise
        self._interpreter.set_session_handle()

    ''' These are code-generated '''

    @ivi_synchronized
    def abort(self):
        r'''abort

        Stops bursting the pattern.
        '''
        self._interpreter.abort()

    @ivi_synchronized
    def abort_keep_alive(self):
        r'''abort_keep_alive

        Stops the keep alive pattern if it is currently running. If a pattern burst is in progress, the method aborts the pattern burst. If you start a new pattern burst while a keep alive pattern is running, the keep alive pattern runs to the last keep alive vector, and the new pattern burst starts on the next cycle.
        '''
        self._interpreter.abort_keep_alive()

    @ivi_synchronized
    def commit(self):
        r'''commit

        Applies all previously configured pin levels, termination modes, clocks, triggers, and pattern timing to a digital pattern instrument. If you do not call the commit method, then the initiate method or the burst_pattern method will implicitly call this method for you. Calling this method moves the session from the Uncommitted state to the Committed state.
        '''
        self._interpreter.commit()

    @ivi_synchronized
    def configure_time_set_period(self, time_set_name, period):
        r'''configure_time_set_period

        Configures the period of a time set. Use this method to modify time set values after applying a timing sheet with the apply_levels_and_timing method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to apply_levels_and_timing; it only affects the values of the current timing context.

        Args:
            time_set_name (str): The specified time set name.

            period (hightime.timedelta, datetime.timedelta, or float in seconds): Period for this time set, in seconds.

        '''
        period = _converters.convert_timedelta_to_seconds_real64(period)
        self._interpreter.configure_time_set_period(time_set_name, period)

    @ivi_synchronized
    def create_capture_waveform_from_file_digicapture(self, waveform_name, waveform_file_path):
        r'''create_capture_waveform_from_file_digicapture

        Creates a capture waveform with the configuration information from a Digicapture file generated by the Digital Pattern Editor.

        Args:
            waveform_name (str): Waveform name you want to use. You must specify waveform_name if the file contains multiple waveforms. Use the waveform_name with the capture_start opcode in your pattern.

            waveform_file_path (str): Absolute file path to the capture waveform file (.digicapture) you want to load.

        '''
        self._interpreter.create_capture_waveform_from_file_digicapture(waveform_name, waveform_file_path)

    @ivi_synchronized
    def create_source_waveform_from_file_tdms(self, waveform_name, waveform_file_path, write_waveform_data=True):
        r'''create_source_waveform_from_file_tdms

        Creates a source waveform with configuration information from a TDMS file generated by the Digital Pattern Editor. It also optionally writes waveform data from the file.

        Args:
            waveform_name (str): The waveform name you want to use from the file. You must specify waveform_name if the file contains multiple waveforms. Use the waveform_name with the source_start opcode in your pattern.

            waveform_file_path (str): Absolute file path to the load source waveform file (.tdms).

            write_waveform_data (bool): A Boolean that writes waveform data to source memory if True and the waveform data is in the file.

        '''
        self._interpreter.create_source_waveform_from_file_tdms(waveform_name, waveform_file_path, write_waveform_data)

    @ivi_synchronized
    def create_time_set(self, name):
        r'''create_time_set

        Creates a time set with the name that you specify. Use this method when you want to create time sets programmatically rather than with a timing sheet.

        Args:
            name (str): The specified name of the new time set.

        '''
        self._interpreter.create_time_set(name)

    @ivi_synchronized
    def delete_all_time_sets(self):
        r'''delete_all_time_sets

        Deletes all time sets from instrument memory.
        '''
        self._interpreter.delete_all_time_sets()

    @ivi_synchronized
    def enable_match_fail_combination(self, sync_session):
        '''enable_match_fail_combination

        Configures digital pattern instruments and the PXIe-6674T timing and synchronization instrument to combine pattern comparison results and control subsequent pattern execution across digital pattern instruments based on those results. You must initialize the PXIe-6674T using NI-Sync and call this method from a multi-instrument session.
        '''
        self._interpreter.enable_match_fail_combination([self._interpreter.get_session_handle()], sync_session.session_handle)

    @ivi_synchronized
    def load_specifications_levels_and_timing(self, specifications_file_paths=None, levels_file_paths=None, timing_file_paths=None):
        '''load_specifications_levels_and_timing

        Loads settings in specifications, levels, and timing sheets. These settings are not
        applied to the digital pattern instrument until apply_levels_and_timing is called.

        If the levels and timing sheets contains formulas, they are evaluated at load time.
        If the formulas refer to variables, the specifications sheets that define those
        variables must be loaded either first, or at the same time as the levels and timing sheets.

        Args:
            specifications_file_paths (str or basic sequence of str): Absolute file path of one or more specifications files.

            levels_file_paths (str or basic sequence of str): Absolute file path of one or more levels sheet files.

            timing_file_paths (str or basic sequence of str): Absolute file path of one or more timing sheet files.

        '''
        self._call_method_with_iterable(self._load_specifications, specifications_file_paths)
        self._call_method_with_iterable(self._load_levels, levels_file_paths)
        self._call_method_with_iterable(self._load_timing, timing_file_paths)

    def _call_method_with_iterable(self, method, files):
        if files is None:
            return
        if isinstance(files, str):
            files = [files]
        for f in files:
            method(f)

    @ivi_synchronized
    def self_test(self):
        '''self_test

        Returns self test results from a digital pattern instrument. This test requires several minutes to execute.

        Raises `SelfTestError` on self test failure. Properties on exception object:

        - code - failure code from driver
        - message - status message from driver

        +----------------+-------------------+
        | Self-Test Code | Description       |
        +================+===================+
        | 0              | Self test passed. |
        +----------------+-------------------+
        | 1              | Self test failed. |
        +----------------+-------------------+
        '''
        code, msg = self._self_test()
        if code:
            raise errors.SelfTestError(code, msg)
        return None

    @ivi_synchronized
    def unload_specifications(self, file_paths):
        '''unload_specifications

        Unloads the given specifications sheets present in the previously loaded
        specifications files that you select.

        You must call load_specifications_levels_and_timing to reload the files with updated
        specifications values. You must then call apply_levels_and_timing in order to apply
        the levels and timing values that reference the updated specifications values.

        Args:
            file_paths (str or basic sequence of str): Absolute file path of one or more loaded specifications files.

        '''
        self._call_method_with_iterable(self._unload_specifications, file_paths)

    @ivi_synchronized
    def write_source_waveform_site_unique(self, waveform_name, waveform_data):
        '''write_source_waveform_site_unique

        Writes one waveform per site. Use this write method if you set the parameter of the create source waveform method to Site Unique.

        Args:
            waveform_name (str): The name to assign to the waveform. Use the waveform_name with source_start opcode in your pattern.

            waveform_data ({ int: basic sequence of unsigned int, int: basic sequence of unsigned int, ... }): Dictionary where each key is a site number and value is a collection of samples to use as source data

        '''
        from collections.abc import Mapping
        if not isinstance(waveform_data, Mapping):
            raise TypeError("Expecting waveform_data to be a dictionary but got {}".format(type(waveform_data)))
        site_list = []
        # We assume all the entries are the same length (we'll check later) to make the array the correct size
        # Get an entry from the dictionary from https://stackoverflow.com/questions/30362391/how-do-you-find-the-first-key-in-a-dictionary
        if len(waveform_data) == 0:
            actual_samples_per_waveform = 0
        else:
            actual_samples_per_waveform = len(waveform_data[next(iter(waveform_data))])
        data = array.array('L', [0]) * (len(waveform_data) * actual_samples_per_waveform)
        mv = memoryview(data)

        i = 0
        for site in waveform_data:
            if len(waveform_data[site]) != actual_samples_per_waveform:
                raise ValueError('Mismatched length of waveforms. All must be the same length.')
            # Check the type by using string comparison so that we don't import numpy unnecessarily.
            if str(type(waveform_data[site])).find("'numpy.ndarray'") != -1:
                import numpy
                if waveform_data[site].dtype == numpy.uint32:
                    wfm = array.array('L', waveform_data[site])
                else:
                    raise TypeError("Unsupported dtype for waveform_data array element type. Is {}, expected {}".format(waveform_data[site].dtype, numpy.int32))

            elif isinstance(waveform_data[site], array.array):
                if waveform_data[site].typecode == 'L':
                    wfm = waveform_data[site]
                else:
                    raise TypeError('Wrong waveform_data array element type. Must be unsigned 32 bit int ("L"), was {}'.format(waveform_data[site].typecode))

            elif isinstance(waveform_data[site], list):
                wfm = array.array('L', waveform_data[site])

            else:
                raise TypeError('Unknown array type: {}'.format(type(waveform_data[site])))

            site_list.append(site)

            start = i * actual_samples_per_waveform
            end = start + actual_samples_per_waveform
            mv[start:end] = wfm

            i += 1

        self.sites[site_list]._write_source_waveform_site_unique_u32(waveform_name, len(waveform_data), actual_samples_per_waveform, data)

    @ivi_synchronized
    def get_pattern_pin_names(self, start_label):
        r'''get_pattern_pin_names

        Returns the pattern pin list.

        Args:
            start_label (str): Pattern name or exported pattern label from which to get the pin names that the pattern references.


        Returns:
            pin_list (list of str): List of pins referenced by the pattern with the **startLabel**.

        '''
        pin_list = self._interpreter.get_pattern_pin_names(start_label)
        return _converters.convert_comma_separated_string_to_list(pin_list)

    @ivi_synchronized
    def get_time_set_period(self, time_set_name):
        r'''get_time_set_period

        Returns the period of the specified time set.

        Args:
            time_set_name (str): The specified time set name.


        Returns:
            period (hightime.timedelta): Returned period, in seconds, that the edge is configured to.

        '''
        period = self._interpreter.get_time_set_period(time_set_name)
        return _converters.convert_seconds_real64_to_timedelta(period)

    def _init_with_options(self, resource_name, id_query=False, reset_device=False, option_string=""):
        r'''_init_with_options

        Creates and returns a new session to the specified digital pattern instrument to use in all subsequent method calls. To place the instrument in a known startup state when creating a new session, set the reset parameter to True, which is equivalent to calling the reset method immediately after initializing the session.

        Args:
            resource_name (str): The specified resource name shown in Measurement & Automation Explorer (MAX) for a digital pattern instrument, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. **resourceName** can also be a logical IVI name. This parameter accepts a comma-delimited list of strings in the form PXI1Slot2,PXI1Slot3, where ``PXI1Slot2`` is one instrument resource name and ``PXI1Slot3`` is another. When including more than one digital pattern instrument in the comma-delimited list of strings, list the instruments in the same order they appear in the pin map.

                +--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | |Note| | Note   You only can specify multiple instruments of the same model. For example, you can list two PXIe-6570s but not a PXIe-6570 and PXIe-6571. The instruments must be in the same chassis. |
                +--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

                .. |Note| image:: note.gif

                Note:

            id_query (bool): A Boolean that verifies that the digital pattern instrument you initialize is supported by NI-Digital. NI-Digital automatically performs this query, so setting this parameter is not necessary.

            reset_device (bool): A Boolean that specifies whether to reset a digital pattern instrument to a known state when the session is initialized. Setting the **resetDevice** value to True is equivalent to calling the reset method immediately after initializing the session.

            option_string (dict): The initial values of certain properties for the NI-Digital Pattern Driver session. The string can be empty. You can use the DriverSetup flag to simulate a digital pattern instrument. When simulating a digital pattern instrument, you must specify the model you want to simulate. For example, Simulate = 1, DriverSetup = Model:6570.


        Returns:
            new_vi (int): The returned instrument session.

        '''
        option_string = _converters.convert_init_with_options_dictionary(option_string)
        new_vi = self._interpreter.init_with_options(resource_name, id_query, reset_device, option_string)
        return new_vi

    @ivi_synchronized
    def _initiate(self):
        r'''_initiate

        Starts bursting the pattern configured by start_label, causing the NI-Digital session to be committed. To stop the pattern burst, call abort. If keep alive pattern is bursting when abort is called or upon exiting the context manager, keep alive pattern will not be stopped. To stop the keep alive pattern, call abort_keep_alive.
        '''
        self._interpreter.initiate()

    @ivi_synchronized
    def is_done(self):
        r'''is_done

        Checks the hardware to determine if the pattern burst has completed or if any errors have occurred.

        Returns:
            done (bool): A Boolean that indicates whether the pattern burst completed.

        '''
        done = self._interpreter.is_done()
        return done

    @ivi_synchronized
    def _load_levels(self, file_path):
        r'''_load_levels

        Loads a levels sheet from a specified file.

        Args:
            file_path (str): Absolute file path to the specified levels sheet file.

        '''
        self._interpreter.load_levels(file_path)

    @ivi_synchronized
    def load_pattern(self, file_path):
        r'''load_pattern

        Loads the specified pattern file.

        Args:
            file_path (str): Absolute file path of the binary .digipat pattern file to load. Specify the pattern to burst using start_label or the start_label parameter of the burst_pattern method.

        '''
        self._interpreter.load_pattern(file_path)

    @ivi_synchronized
    def load_pin_map(self, file_path):
        r'''load_pin_map

        Loads a pin map file. You can load only a single pin and channel map file during an NI-Digital Pattern Driver session. To switch pin maps, create a new session or call the reset method.

        Args:
            file_path (str): Absolute file path to a pin map file created with the Digital Pattern Editor or the NI TestStand Semiconductor Module.

        '''
        self._interpreter.load_pin_map(file_path)

    @ivi_synchronized
    def _load_specifications(self, file_path):
        r'''_load_specifications

        Loads a specifications sheet from a specified file.

        Args:
            file_path (str): Absolute file path to a specifications file.

        '''
        self._interpreter.load_specifications(file_path)

    @ivi_synchronized
    def _load_timing(self, file_path):
        r'''_load_timing

        Loads a timing sheet from a specified file.

        Args:
            file_path (str): Absolute file path to the specified timing sheet file.

        '''
        self._interpreter.load_timing(file_path)

    @ivi_synchronized
    def read_sequencer_flag(self, flag):
        r'''read_sequencer_flag

        Reads the state of a pattern sequencer flag. Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime test program.

        Args:
            flag (enums.SequencerFlag): The pattern sequencer flag you want to read.

                -   SequencerFlag.FLAG0 ("seqflag0"): Reads pattern sequencer flag 0.
                -   SequencerFlag.FLAG1 ("seqflag1"): Reads pattern sequencer flag 1.
                -   SequencerFlag.FLAG2 ("seqflag2"): Reads pattern sequencer flag 2.
                -   SequencerFlag.FLAG3 ("seqflag3"): Reads pattern sequencer flag 3.


        Returns:
            value (bool): A Boolean that indicates the state of the pattern sequencer flag you specify.

        '''
        if type(flag) is not enums.SequencerFlag:
            raise TypeError('Parameter flag must be of type ' + str(enums.SequencerFlag))
        value = self._interpreter.read_sequencer_flag(flag)
        return value

    @ivi_synchronized
    def read_sequencer_register(self, reg):
        r'''read_sequencer_register

        Reads the value of a pattern sequencer register. Use pattern sequencer registers to pass numeric values between the pattern sequencer and a runtime test program. For example, you can use this method to read a register modified by the write_reg opcode during a pattern burst.

        Args:
            reg (enums.SequencerRegister): The sequencer register to read from.

                -   SequencerRegister.REGISTER0 ("reg0"): Reads sequencer register 0.
                -   SequencerRegister.REGISTER1 ("reg1"): Reads sequencer register 1.
                -   SequencerRegister.REGISTER2 ("reg2"): Reads sequencer register 2.
                -   SequencerRegister.REGISTER3 ("reg3"): Reads sequencer register 3.
                -   SequencerRegister.REGISTER4 ("reg4"): Reads sequencer register 4.
                -   SequencerRegister.REGISTER5 ("reg5"): Reads sequencer register 5.
                -   SequencerRegister.REGISTER6 ("reg6"): Reads sequencer register 6.
                -   SequencerRegister.REGISTER7 ("reg7"): Reads sequencer register 7.
                -   SequencerRegister.REGISTER8 ("reg8"): Reads sequencer register 8.
                -   SequencerRegister.REGISTER9 ("reg9"): Reads sequencer register 9.
                -   SequencerRegister.REGISTER10 ("reg10"): Reads sequencer register 10.
                -   SequencerRegister.REGISTER11 ("reg11"): Reads sequencer register 11.
                -   SequencerRegister.REGISTER12 ("reg12"): Reads sequencer register 12.
                -   SequencerRegister.REGISTER13 ("reg13"): Reads sequencer register 13.
                -   SequencerRegister.REGISTER14 ("reg14"): Reads sequencer register 14.
                -   SequencerRegister.REGISTER15 ("reg15"): Reads sequencer register 15.


        Returns:
            value (int): Value read from the sequencer register.

        '''
        if type(reg) is not enums.SequencerRegister:
            raise TypeError('Parameter reg must be of type ' + str(enums.SequencerRegister))
        value = self._interpreter.read_sequencer_register(reg)
        return value

    @ivi_synchronized
    def reset_device(self):
        r'''reset_device

        Returns a digital pattern instrument to a known state. This method performs the following actions:

        - Aborts pattern execution.
        - Clears pin maps, time sets, source and capture waveforms, and patterns.
        - Resets all properties to default values, including the selected_function property that is set to SelectedFunction.DISCONNECT, causing the I/O switches to open.
        - Stops export of all external signals and events.
        - Clears over-temperature and over-power conditions.
        '''
        self._interpreter.reset_device()

    @ivi_synchronized
    def self_calibrate(self):
        r'''self_calibrate

        Performs self-calibration on a digital pattern instrument.
        '''
        self._interpreter.self_calibrate()

    @ivi_synchronized
    def send_software_edge_trigger(self, trigger, trigger_identifier):
        r'''send_software_edge_trigger

        Forces a particular edge-based trigger to occur regardless of how the specified trigger is configured. You can use this method as a software override.

        Args:
            trigger (enums.SoftwareTrigger): Trigger specifies the trigger you want to override.

                +----------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
                | Defined Values                   |                                                                                                                                 |
                +==================================+=================================================================================================================================+
                | SoftwareTrigger.START            | Overrides the Start trigger. You must specify an empty string in the trigger_identifier parameter.                              |
                +----------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
                | SoftwareTrigger.CONDITIONAL_JUMP | Specifies to route a conditional jump trigger. You must specify a conditional jump trigger in the trigger_identifier parameter. |
                +----------------------------------+---------------------------------------------------------------------------------------------------------------------------------+

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            trigger_identifier (str): Trigger Identifier specifies the instance of the trigger you want to override.
                If trigger is specified as NIDIGITAL_VAL_START_TRIGGER, this parameter must be an empty string. If trigger is
                specified as NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER, allowed values are conditionalJumpTrigger0,
                conditionalJumpTrigger1, conditionalJumpTrigger2, and conditionalJumpTrigger3.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        if type(trigger) is not enums.SoftwareTrigger:
            raise TypeError('Parameter trigger must be of type ' + str(enums.SoftwareTrigger))
        self._interpreter.send_software_edge_trigger(trigger, trigger_identifier)

    @ivi_synchronized
    def unload_all_patterns(self, unload_keep_alive_pattern=False):
        r'''unload_all_patterns

        Unloads all patterns, source waveforms, and capture waveforms from a digital pattern instrument.

        Args:
            unload_keep_alive_pattern (bool): A Boolean that specifies whether to keep or unload the keep alive pattern.

        '''
        self._interpreter.unload_all_patterns(unload_keep_alive_pattern)

    @ivi_synchronized
    def _unload_specifications(self, file_path):
        r'''_unload_specifications

        Unloads the given specifications sheet present in the previously loaded specifications file that you select. You must call the _load_specifications method to reload the file with updated specifications values. You must then call the apply_levels_and_timing method in order to apply the levels and timing values that reference the updated specifications values.

        Args:
            file_path (str): Absolute file path to a loaded specifications file.

        '''
        self._interpreter.unload_specifications(file_path)

    @ivi_synchronized
    def wait_until_done(self, timeout=hightime.timedelta(seconds=10.0)):
        r'''wait_until_done

        Waits until the pattern burst has completed or the timeout has expired.

        Args:
            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): Maximum time (in seconds) allowed for this method to complete. If this method does not complete within this time interval, this method returns an error.

        '''
        timeout = _converters.convert_timedelta_to_seconds_real64(timeout)
        self._interpreter.wait_until_done(timeout)

    @ivi_synchronized
    def write_sequencer_flag(self, flag, value):
        r'''write_sequencer_flag

        Writes the state of a pattern sequencer flag. Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime test program.

        Args:
            flag (enums.SequencerFlag): The pattern sequencer flag to write.

                -   SequencerFlag.FLAG0 ("seqflag0"): Writes pattern sequencer flag 0.
                -   SequencerFlag.FLAG1 ("seqflag1"): Writes pattern sequencer flag 1.
                -   SequencerFlag.FLAG2 ("seqflag2"): Writes pattern sequencer flag 2.
                -   SequencerFlag.FLAG3 ("seqflag3"): Writes pattern sequencer flag 3.

            value (bool): A Boolean that assigns a state to the pattern sequencer flag you specify.

        '''
        if type(flag) is not enums.SequencerFlag:
            raise TypeError('Parameter flag must be of type ' + str(enums.SequencerFlag))
        self._interpreter.write_sequencer_flag(flag, value)

    @ivi_synchronized
    def write_sequencer_register(self, reg, value):
        r'''write_sequencer_register

        Writes a value to a pattern sequencer register. Use pattern sequencer registers to pass numeric values between the pattern sequencer and a runtime test program.

        Args:
            reg (enums.SequencerRegister): The sequencer register you want to write to.

                -   SequencerRegister.REGISTER0 ("reg0"): Writes sequencer register 0.
                -   SequencerRegister.REGISTER1 ("reg1"): Writes sequencer register 1.
                -   SequencerRegister.REGISTER2 ("reg2"): Writes sequencer register 2.
                -   SequencerRegister.REGISTER3 ("reg3"): Writes sequencer register 3.
                -   SequencerRegister.REGISTER4 ("reg4"): Writes sequencer register 4.
                -   SequencerRegister.REGISTER5 ("reg5"): Writes sequencer register 5.
                -   SequencerRegister.REGISTER6 ("reg6"): Writes sequencer register 6.
                -   SequencerRegister.REGISTER7 ("reg7"): Writes sequencer register 7.
                -   SequencerRegister.REGISTER8 ("reg8"): Writes sequencer register 8.
                -   SequencerRegister.REGISTER9 ("reg9"): Writes sequencer register 9.
                -   SequencerRegister.REGISTER10 ("reg10"): Writes sequencer register 10.
                -   SequencerRegister.REGISTER11 ("reg11"): Writes sequencer register 11.
                -   SequencerRegister.REGISTER12 ("reg12"): Writes sequencer register 12.
                -   SequencerRegister.REGISTER13 ("reg13"): Writes sequencer register 13.
                -   SequencerRegister.REGISTER14 ("reg14"): Writes sequencer register 14.
                -   SequencerRegister.REGISTER15 ("reg15"): Writes sequencer register 15.

            value (int): The value you want to write to the register.

        '''
        if type(reg) is not enums.SequencerRegister:
            raise TypeError('Parameter reg must be of type ' + str(enums.SequencerRegister))
        self._interpreter.write_sequencer_register(reg, value)

    @ivi_synchronized
    def write_source_waveform_broadcast(self, waveform_name, waveform_data):
        r'''write_source_waveform_broadcast

        Writes the same waveform data to all sites. Use this write method if you set the data_mapping parameter of the create source waveform method to SourceDataMapping.BROADCAST.

        Args:
            waveform_name (str): The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.

            waveform_data (list of int): 1D array of samples to use as source data to apply to all sites.

        '''
        self._interpreter.write_source_waveform_broadcast(waveform_name, waveform_data)

    @ivi_synchronized
    def write_source_waveform_data_from_file_tdms(self, waveform_name, waveform_file_path):
        r'''write_source_waveform_data_from_file_tdms

        Writes a source waveform based on the waveform data and configuration information the file contains.

        Args:
            waveform_name (str): The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.

            waveform_file_path (str): Absolute file path to the load source waveform file (.tdms).

        '''
        self._interpreter.write_source_waveform_data_from_file_tdms(waveform_name, waveform_file_path)

    def _close(self):
        r'''_close

        Closes the specified instrument session to a digital pattern instrument, aborts pattern execution, and unloads pattern memory. The channels on a digital pattern instrument remain in their current state.
        '''
        self._interpreter.close()

    @ivi_synchronized
    def reset(self):
        r'''reset

        Returns a digital pattern instrument to a known state. This method performs the following actions:

        - Aborts pattern execution.
        - Clears pin maps, time sets, source and capture waveforms, and patterns.
        - Resets all properties to default values, including the selected_function property that is set to SelectedFunction.DISCONNECT, causing the I/O switches to open.
        - Stops exporting all external signals and events.
        '''
        self._interpreter.reset()

    @ivi_synchronized
    def _self_test(self):
        r'''_self_test

        Returns self test results from a digital pattern instrument. This test requires several minutes to execute.

        Returns:
            test_result (int): A parameter that indicates if the self test passed (0) or failed (!=0).

            test_message (str): The returned self test status message. The array must contain at least 256 characters.

        '''
        test_result, test_message = self._interpreter.self_test()
        return test_result, test_message
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidigital/nidigital/unit_tests/_matchers.py sha256=0f89d482c107a369de4985092514136c61b488be73e98d283a95a08754add3f9 bytes=12202 -->
## FILE: generated/nidigital/nidigital/unit_tests/_matchers.py

- repository: `ni/nimi-python`
- source_path: `generated/nidigital/nidigital/unit_tests/_matchers.py`
- sha256: `0f89d482c107a369de4985092514136c61b488be73e98d283a95a08754add3f9`
- bytes: 12202

````python
# -*- coding: utf-8 -*-
# This file was generated
'''Matcher classes used by unit tests in order to set mock expectations.
These work well with our visatype definitions.
'''

import ctypes
import nidigital._visatype as _visatype
import pprint

pp = pprint.PrettyPrinter(indent=4)


# Base classes


class _ScalarMatcher(object):
    def __init__(self, expected_type, expected_value):
        self.expected_type = expected_type
        self.expected_value = expected_value

    def __eq__(self, other):
        if not isinstance(other, self.expected_type):
            print("{}: Unexpected type. Expected: {}. Received: {}".format(self.__class__.__name__, self.expected_type, type(other)))
            return False
        if other.value != self.expected_value:
            print("{}: Unexpected value. Expected: {}. Received: {}".format(self.__class__.__name__, self.expected_value, other.value))
            return False
        return True

    def __repr__(self):
        return '{}({}, {})'.format(self.__class__.__name__, pp.pformat(self.expected_type), pp.pformat(self.expected_value))


class _PointerMatcher(object):
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __eq__(self, other):
        if not isinstance(other, ctypes.POINTER(self.expected_type)):
            print("Unexpected type. Expected: {}. Received: {}".format(ctypes.POINTER(self.expected_type), type(other)))
            return False
        return True

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, pp.pformat(self.expected_type))


class _BufferMatcher(object):
    def __init__(self, expected_element_type, expected_size_or_value):
        if isinstance(expected_size_or_value, int):
            # Were given the size of the buffer
            self.expected_value = None
            self.expected_size = expected_size_or_value
        else:
            # Were given a list or something that behaves like a list
            self.expected_value = expected_size_or_value
            self.expected_size = len(expected_size_or_value)
        self.expected_type = expected_element_type * self.expected_size
        # Store params for __repr__
        self._expected_element_type = expected_element_type
        self._expected_size_or_value = expected_size_or_value

    def __eq__(self, other):
        if not isinstance(other, self.expected_type):
            # We try to "dereference" this in case it is a pointer and then do the check again. Only then saying they don't match
            try:
                other = other.contents
            except AttributeError:
                pass

            # Because of object lifetimes, we may need to mock the other instance and provide lists instead of the actual array
            if not isinstance(other, self.expected_type) and not isinstance(other, list):
                print("Unexpected type. Expected: {} or {}. Received: {}".format(self.expected_type, list, type(other)))
                return False
        if self.expected_size != len(other):
            print("Unexpected length. Expected: {}. Received: {}".format(self.expected_size, len(other)))
            return False
        if self.expected_value is not None:
            # Can't compare the objects directly because they're different types (one is list, another is ctypes array).
            # Go element by element, which allows for reporting the first index where different values were found.
            for i in range(0, len(self.expected_value)):
                if self.expected_value[i] != other[i]:
                    print("Unexpected value at index {}. Expected: {}. Received: {}".format(i, self.expected_value[i], other[i]))
                    return False
        return True

    def __repr__(self):
        return '{}({}, {})'.format(self.__class__.__name__, pp.pformat(self._expected_element_type), pp.pformat(self._expected_size_or_value))

    def __str__(self):
        ret_str = self.__repr__() + '\n'
        ret_str += '    expected_type  = ' + str(self.expected_type) + '\n'
        ret_str += '    expected_value = ' + str(self.expected_value) + '\n'
        ret_str += '    expected_size  = ' + str(self.expected_size) + '\n'
        return ret_str


# Strings


class ViStringMatcher(object):
    def __init__(self, expected_string_value):
        self.expected_string_value = expected_string_value

    def __eq__(self, other):
        if not isinstance(other, ctypes.Array):
            # We try to "dereference" this in case it is a pointer and then do the check again. Only then saying they don't match
            try:
                other = other.contents
            except AttributeError:
                pass

            if not isinstance(other, ctypes.Array):
                print("Unexpected type. Expected: {}. Received: {}".format(self.expected_type, type(other)))
                return False
        if len(other) < len(self.expected_string_value) + 1:  # +1 for NULL terminating character
            print("Unexpected length in C string. Expected at least: {}. Received {}".format(len(other), len(self.expected_string_value) + 1))
            return False
        if not isinstance(other[0], bytes):
            print("Unexpected type. Not a string. Received: {}".format(type(other[0])))
            return False
        if other.value.decode("ascii") != self.expected_string_value:
            print("Unexpected value. Expected {}. Received: {}".format(self.expected_string_value, other.value.decode))
            return False
        return True

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, pp.pformat(self.expected_string_value))


# Custom Type


def _compare_ctype_structs(expected, actual):
    # From https://stackoverflow.com/questions/20986330/print-all-fields-of-ctypes-structure-with-introspection
    for field in expected._fields_:
        field_name = field[0]
        expected_val = getattr(expected, field_name)
        actual_val = getattr(actual, field_name)
        if expected_val != actual_val:
            print("Unexpected value field {}. Expected: {}. Received: {}".format(field_name, expected_val, actual_val))
            return False
    return True


class CustomTypeMatcher(object):
    def __init__(self, expected_type, expected_value):
        self.expected_type = expected_type
        self.expected_value = expected_value

    def __eq__(self, actual):
        if not isinstance(actual, self.expected_type):
            print("Unexpected type. Expected: {}. Received: {}".format(self.expected_type, type(actual)))
            return False
        return _compare_ctype_structs(self.expected_value, actual)

    def __repr__(self):
        return '{}({}, {})'.format(self.__class__.__name__, pp.pformat(self.expected_type), pp.pformat(self.expected_value))


class CustomTypeBufferMatcher(object):
    def __init__(self, expected_element_type, expected_value):
        self.expected_value = expected_value
        self.expected_size = len(expected_value)
        self.expected_type = expected_element_type * self.expected_size
        self.expected_element_type = expected_element_type

    def __eq__(self, actual):
        if not isinstance(actual, self.expected_type):
            print("Unexpected array type. Expected: {}. Received: {}".format(self.expected_type, type(actual)))
            return False
        if self.expected_size != len(actual):
            print("Unexpected length. Expected: {}. Received: {}".format(self.expected_size, len(actual)))
            return False
        if self.expected_value is not None:
            # Can't compare the objects directly because they're different types (one is list, another is ctypes array).
            # Go element by element, which allows for reporting the first index where different values were found.
            for a, e in zip(actual, self.expected_value):
                if not isinstance(a, self.expected_element_type):
                    print("Unexpected type. Expected: {}. Received: {}".format(self.expected_element_type, type(a)))
                    return False
                if not _compare_ctype_structs(e, a):
                    return False
        return True

    def __repr__(self):
        expected_val_repr = '[' + ', '.join([x.__repr__() for x in self.expected_value]) + ']'
        return '{}({}, {})'.format(self.__class__.__name__, pp.pformat(self.expected_element_type), expected_val_repr)

    def __str__(self):
        ret_str = self.__repr__() + '\n'
        ret_str += '    expected_type = ' + str(self.expected_type) + '\n'
        ret_str += '    expected_size = ' + str(self.expected_size) + '\n'
        return ret_str


# Scalars


class ViBooleanMatcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViBoolean, 1 if expected_value is True else 0)


class ViSessionMatcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViSession, expected_value)


class ViInt16Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViInt16, expected_value)


class ViInt32Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViInt32, expected_value)


class ViUInt32Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViUInt32, expected_value)


class ViAttrMatcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViAttr, expected_value)


class ViInt64Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViInt64, expected_value)


class ViReal64Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViReal64, expected_value)


# Pointers


class ViBooleanPointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViBoolean)


class ViSessionPointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViSession)


class ViInt16PointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViInt16)


class ViInt32PointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViInt32)


class ViInt64PointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViInt64)


class ViReal64PointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViReal64)


# Buffers


class ViBooleanBufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViBoolean, expected_size_or_value)


class ViCharBufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViChar, expected_size_or_value)


class ViInt8BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViInt8, expected_size_or_value)


class ViInt16BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViInt16, expected_size_or_value)


class ViInt32BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViInt32, expected_size_or_value)


class ViInt64BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViInt64, expected_size_or_value)


class ViReal64BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViReal64, expected_size_or_value)


class ViSessionBufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViSession, expected_size_or_value)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidigital/nidigital/unit_tests/_mock_helper.py sha256=417b9c0941ae064b1e1a72671701a305223d15248297b222c0c8a47c2bd947bd bytes=84344 -->
## FILE: generated/nidigital/nidigital/unit_tests/_mock_helper.py

- repository: `ni/nimi-python`
- source_path: `generated/nidigital/nidigital/unit_tests/_mock_helper.py`
- sha256: `417b9c0941ae064b1e1a72671701a305223d15248297b222c0c8a47c2bd947bd`
- bytes: 84344

````python
# -*- coding: utf-8 -*-
# This file was generated
import sys  # noqa: F401   - Not all mock_helpers will need this


class MockFunctionCallError(Exception):
    def __init__(self, function, param=None):
        self.function = function
        self.param = param
        msg = "{0} called without setting side_effect".format(self.function)
        if param is not None:
            msg += " or setting the {0} parameter return value".format(self.param)
        super(Exception, self).__init__(msg)


class SideEffectsHelper(object):
    def __init__(self):
        self._defaults = {}
        self._defaults['Abort'] = {}
        self._defaults['Abort']['return'] = 0
        self._defaults['AbortKeepAlive'] = {}
        self._defaults['AbortKeepAlive']['return'] = 0
        self._defaults['ApplyLevelsAndTiming'] = {}
        self._defaults['ApplyLevelsAndTiming']['return'] = 0
        self._defaults['ApplyTDROffsets'] = {}
        self._defaults['ApplyTDROffsets']['return'] = 0
        self._defaults['BurstPattern'] = {}
        self._defaults['BurstPattern']['return'] = 0
        self._defaults['ClockGenerator_Abort'] = {}
        self._defaults['ClockGenerator_Abort']['return'] = 0
        self._defaults['ClockGenerator_GenerateClock'] = {}
        self._defaults['ClockGenerator_GenerateClock']['return'] = 0
        self._defaults['Commit'] = {}
        self._defaults['Commit']['return'] = 0
        self._defaults['ConfigureActiveLoadLevels'] = {}
        self._defaults['ConfigureActiveLoadLevels']['return'] = 0
        self._defaults['ConfigurePatternBurstSites'] = {}
        self._defaults['ConfigurePatternBurstSites']['return'] = 0
        self._defaults['ConfigureTimeSetCompareEdgesStrobe'] = {}
        self._defaults['ConfigureTimeSetCompareEdgesStrobe']['return'] = 0
        self._defaults['ConfigureTimeSetCompareEdgesStrobe2x'] = {}
        self._defaults['ConfigureTimeSetCompareEdgesStrobe2x']['return'] = 0
        self._defaults['ConfigureTimeSetDriveEdges'] = {}
        self._defaults['ConfigureTimeSetDriveEdges']['return'] = 0
        self._defaults['ConfigureTimeSetDriveEdges2x'] = {}
        self._defaults['ConfigureTimeSetDriveEdges2x']['return'] = 0
        self._defaults['ConfigureTimeSetDriveFormat'] = {}
        self._defaults['ConfigureTimeSetDriveFormat']['return'] = 0
        self._defaults['ConfigureTimeSetEdge'] = {}
        self._defaults['ConfigureTimeSetEdge']['return'] = 0
        self._defaults['ConfigureTimeSetEdgeMultiplier'] = {}
        self._defaults['ConfigureTimeSetEdgeMultiplier']['return'] = 0
        self._defaults['ConfigureTimeSetPeriod'] = {}
        self._defaults['ConfigureTimeSetPeriod']['return'] = 0
        self._defaults['ConfigureVoltageLevels'] = {}
        self._defaults['ConfigureVoltageLevels']['return'] = 0
        self._defaults['CreateCaptureWaveformFromFileDigicapture'] = {}
        self._defaults['CreateCaptureWaveformFromFileDigicapture']['return'] = 0
        self._defaults['CreateCaptureWaveformParallel'] = {}
        self._defaults['CreateCaptureWaveformParallel']['return'] = 0
        self._defaults['CreateCaptureWaveformSerial'] = {}
        self._defaults['CreateCaptureWaveformSerial']['return'] = 0
        self._defaults['CreateSourceWaveformFromFileTDMS'] = {}
        self._defaults['CreateSourceWaveformFromFileTDMS']['return'] = 0
        self._defaults['CreateSourceWaveformParallel'] = {}
        self._defaults['CreateSourceWaveformParallel']['return'] = 0
        self._defaults['CreateSourceWaveformSerial'] = {}
        self._defaults['CreateSourceWaveformSerial']['return'] = 0
        self._defaults['CreateTimeSet'] = {}
        self._defaults['CreateTimeSet']['return'] = 0
        self._defaults['DeleteAllTimeSets'] = {}
        self._defaults['DeleteAllTimeSets']['return'] = 0
        self._defaults['DisableSites'] = {}
        self._defaults['DisableSites']['return'] = 0
        self._defaults['EnableMatchFailCombination'] = {}
        self._defaults['EnableMatchFailCombination']['return'] = 0
        self._defaults['EnableSites'] = {}
        self._defaults['EnableSites']['return'] = 0
        self._defaults['FetchCaptureWaveformU32'] = {}
        self._defaults['FetchCaptureWaveformU32']['return'] = 0
        self._defaults['FetchCaptureWaveformU32']['actualNumWaveforms'] = None
        self._defaults['FetchCaptureWaveformU32']['actualSamplesPerWaveform'] = None
        self._defaults['FetchCaptureWaveformU32']['data'] = None
        self._defaults['FetchHistoryRAMCycleInformation'] = {}
        self._defaults['FetchHistoryRAMCycleInformation']['return'] = 0
        self._defaults['FetchHistoryRAMCycleInformation']['patternIndex'] = None
        self._defaults['FetchHistoryRAMCycleInformation']['timeSetIndex'] = None
        self._defaults['FetchHistoryRAMCycleInformation']['vectorNumber'] = None
        self._defaults['FetchHistoryRAMCycleInformation']['cycleNumber'] = None
        self._defaults['FetchHistoryRAMCycleInformation']['numDutCycles'] = None
        self._defaults['FetchHistoryRAMCyclePinData'] = {}
        self._defaults['FetchHistoryRAMCyclePinData']['return'] = 0
        self._defaults['FetchHistoryRAMCyclePinData']['actualNumPinData'] = None
        self._defaults['FetchHistoryRAMCyclePinData']['expectedPinStates'] = None
        self._defaults['FetchHistoryRAMCyclePinData']['actualPinStates'] = None
        self._defaults['FetchHistoryRAMCyclePinData']['perPinPassFail'] = None
        self._defaults['FetchHistoryRAMScanCycleNumber'] = {}
        self._defaults['FetchHistoryRAMScanCycleNumber']['return'] = 0
        self._defaults['FetchHistoryRAMScanCycleNumber']['scanCycleNumber'] = None
        self._defaults['FrequencyCounter_MeasureFrequency'] = {}
        self._defaults['FrequencyCounter_MeasureFrequency']['return'] = 0
        self._defaults['FrequencyCounter_MeasureFrequency']['actualNumFrequencies'] = None
        self._defaults['FrequencyCounter_MeasureFrequency']['frequencies'] = None
        self._defaults['GetAttributeViBoolean'] = {}
        self._defaults['GetAttributeViBoolean']['return'] = 0
        self._defaults['GetAttributeViBoolean']['value'] = None
        self._defaults['GetAttributeViInt32'] = {}
        self._defaults['GetAttributeViInt32']['return'] = 0
        self._defaults['GetAttributeViInt32']['value'] = None
        self._defaults['GetAttributeViInt64'] = {}
        self._defaults['GetAttributeViInt64']['return'] = 0
        self._defaults['GetAttributeViInt64']['value'] = None
        self._defaults['GetAttributeViReal64'] = {}
        self._defaults['GetAttributeViReal64']['return'] = 0
        self._defaults['GetAttributeViReal64']['value'] = None
        self._defaults['GetAttributeViString'] = {}
        self._defaults['GetAttributeViString']['return'] = 0
        self._defaults['GetAttributeViString']['value'] = None
        self._defaults['GetChannelNameFromString'] = {}
        self._defaults['GetChannelNameFromString']['return'] = 0
        self._defaults['GetChannelNameFromString']['name'] = None
        self._defaults['GetError'] = {}
        self._defaults['GetError']['return'] = 0
        self._defaults['GetError']['errorCode'] = None
        self._defaults['GetError']['errorDescription'] = None
        self._defaults['GetFailCount'] = {}
        self._defaults['GetFailCount']['return'] = 0
        self._defaults['GetFailCount']['actualNumRead'] = None
        self._defaults['GetFailCount']['failureCount'] = None
        self._defaults['GetHistoryRAMSampleCount'] = {}
        self._defaults['GetHistoryRAMSampleCount']['return'] = 0
        self._defaults['GetHistoryRAMSampleCount']['sampleCount'] = None
        self._defaults['GetPatternName'] = {}
        self._defaults['GetPatternName']['return'] = 0
        self._defaults['GetPatternName']['name'] = None
        self._defaults['GetPatternPinList'] = {}
        self._defaults['GetPatternPinList']['return'] = 0
        self._defaults['GetPatternPinList']['pinList'] = None
        self._defaults['GetPinName'] = {}
        self._defaults['GetPinName']['return'] = 0
        self._defaults['GetPinName']['name'] = None
        self._defaults['GetPinResultsPinInformation'] = {}
        self._defaults['GetPinResultsPinInformation']['return'] = 0
        self._defaults['GetPinResultsPinInformation']['actualNumValues'] = None
        self._defaults['GetPinResultsPinInformation']['pinIndexes'] = None
        self._defaults['GetPinResultsPinInformation']['siteNumbers'] = None
        self._defaults['GetPinResultsPinInformation']['channelIndexes'] = None
        self._defaults['GetSitePassFail'] = {}
        self._defaults['GetSitePassFail']['return'] = 0
        self._defaults['GetSitePassFail']['actualNumSites'] = None
        self._defaults['GetSitePassFail']['passFail'] = None
        self._defaults['GetSiteResultsSiteNumbers'] = {}
        self._defaults['GetSiteResultsSiteNumbers']['return'] = 0
        self._defaults['GetSiteResultsSiteNumbers']['actualNumSiteNumbers'] = None
        self._defaults['GetSiteResultsSiteNumbers']['siteNumbers'] = None
        self._defaults['GetTimeSetDriveFormat'] = {}
        self._defaults['GetTimeSetDriveFormat']['return'] = 0
        self._defaults['GetTimeSetDriveFormat']['format'] = None
        self._defaults['GetTimeSetEdge'] = {}
        self._defaults['GetTimeSetEdge']['return'] = 0
        self._defaults['GetTimeSetEdge']['time'] = None
        self._defaults['GetTimeSetEdgeMultiplier'] = {}
        self._defaults['GetTimeSetEdgeMultiplier']['return'] = 0
        self._defaults['GetTimeSetEdgeMultiplier']['edgeMultiplier'] = None
        self._defaults['GetTimeSetName'] = {}
        self._defaults['GetTimeSetName']['return'] = 0
        self._defaults['GetTimeSetName']['name'] = None
        self._defaults['GetTimeSetPeriod'] = {}
        self._defaults['GetTimeSetPeriod']['return'] = 0
        self._defaults['GetTimeSetPeriod']['period'] = None
        self._defaults['InitWithOptions'] = {}
        self._defaults['InitWithOptions']['return'] = 0
        self._defaults['InitWithOptions']['newVi'] = None
        self._defaults['Initiate'] = {}
        self._defaults['Initiate']['return'] = 0
        self._defaults['IsDone'] = {}
        self._defaults['IsDone']['return'] = 0
        self._defaults['IsDone']['done'] = None
        self._defaults['IsSiteEnabled'] = {}
        self._defaults['IsSiteEnabled']['return'] = 0
        self._defaults['IsSiteEnabled']['enable'] = None
        self._defaults['LoadLevels'] = {}
        self._defaults['LoadLevels']['return'] = 0
        self._defaults['LoadPattern'] = {}
        self._defaults['LoadPattern']['return'] = 0
        self._defaults['LoadPinMap'] = {}
        self._defaults['LoadPinMap']['return'] = 0
        self._defaults['LoadSpecifications'] = {}
        self._defaults['LoadSpecifications']['return'] = 0
        self._defaults['LoadTiming'] = {}
        self._defaults['LoadTiming']['return'] = 0
        self._defaults['LockSession'] = {}
        self._defaults['LockSession']['return'] = 0
        self._defaults['LockSession']['callerHasLock'] = None
        self._defaults['PPMU_Measure'] = {}
        self._defaults['PPMU_Measure']['return'] = 0
        self._defaults['PPMU_Measure']['actualNumRead'] = None
        self._defaults['PPMU_Measure']['measurements'] = None
        self._defaults['PPMU_Source'] = {}
        self._defaults['PPMU_Source']['return'] = 0
        self._defaults['ReadSequencerFlag'] = {}
        self._defaults['ReadSequencerFlag']['return'] = 0
        self._defaults['ReadSequencerFlag']['value'] = None
        self._defaults['ReadSequencerRegister'] = {}
        self._defaults['ReadSequencerRegister']['return'] = 0
        self._defaults['ReadSequencerRegister']['value'] = None
        self._defaults['ReadStatic'] = {}
        self._defaults['ReadStatic']['return'] = 0
        self._defaults['ReadStatic']['actualNumRead'] = None
        self._defaults['ReadStatic']['data'] = None
        self._defaults['ResetDevice'] = {}
        self._defaults['ResetDevice']['return'] = 0
        self._defaults['SelfCalibrate'] = {}
        self._defaults['SelfCalibrate']['return'] = 0
        self._defaults['SendSoftwareEdgeTrigger'] = {}
        self._defaults['SendSoftwareEdgeTrigger']['return'] = 0
        self._defaults['SetAttributeViBoolean'] = {}
        self._defaults['SetAttributeViBoolean']['return'] = 0
        self._defaults['SetAttributeViInt32'] = {}
        self._defaults['SetAttributeViInt32']['return'] = 0
        self._defaults['SetAttributeViInt64'] = {}
        self._defaults['SetAttributeViInt64']['return'] = 0
        self._defaults['SetAttributeViReal64'] = {}
        self._defaults['SetAttributeViReal64']['return'] = 0
        self._defaults['SetAttributeViString'] = {}
        self._defaults['SetAttributeViString']['return'] = 0
        self._defaults['SetRuntimeEnvironment'] = {}
        self._defaults['SetRuntimeEnvironment']['return'] = 0
        self._defaults['TDR'] = {}
        self._defaults['TDR']['return'] = 0
        self._defaults['TDR']['actualNumOffsets'] = None
        self._defaults['TDR']['offsets'] = None
        self._defaults['UnloadAllPatterns'] = {}
        self._defaults['UnloadAllPatterns']['return'] = 0
        self._defaults['UnloadSpecifications'] = {}
        self._defaults['UnloadSpecifications']['return'] = 0
        self._defaults['UnlockSession'] = {}
        self._defaults['UnlockSession']['return'] = 0
        self._defaults['UnlockSession']['callerHasLock'] = None
        self._defaults['WaitUntilDone'] = {}
        self._defaults['WaitUntilDone']['return'] = 0
        self._defaults['WriteSequencerFlag'] = {}
        self._defaults['WriteSequencerFlag']['return'] = 0
        self._defaults['WriteSequencerRegister'] = {}
        self._defaults['WriteSequencerRegister']['return'] = 0
        self._defaults['WriteSourceWaveformBroadcastU32'] = {}
        self._defaults['WriteSourceWaveformBroadcastU32']['return'] = 0
        self._defaults['WriteSourceWaveformDataFromFileTDMS'] = {}
        self._defaults['WriteSourceWaveformDataFromFileTDMS']['return'] = 0
        self._defaults['WriteSourceWaveformSiteUniqueU32'] = {}
        self._defaults['WriteSourceWaveformSiteUniqueU32']['return'] = 0
        self._defaults['WriteStatic'] = {}
        self._defaults['WriteStatic']['return'] = 0
        self._defaults['close'] = {}
        self._defaults['close']['return'] = 0
        self._defaults['error_message'] = {}
        self._defaults['error_message']['return'] = 0
        self._defaults['error_message']['errorMessage'] = None
        self._defaults['reset'] = {}
        self._defaults['reset']['return'] = 0
        self._defaults['self_test'] = {}
        self._defaults['self_test']['return'] = 0
        self._defaults['self_test']['testResult'] = None
        self._defaults['self_test']['testMessage'] = None

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

    def niDigital_Abort(self, vi):  # noqa: N802
        if self._defaults['Abort']['return'] != 0:
            return self._defaults['Abort']['return']
        return self._defaults['Abort']['return']

    def niDigital_AbortKeepAlive(self, vi):  # noqa: N802
        if self._defaults['AbortKeepAlive']['return'] != 0:
            return self._defaults['AbortKeepAlive']['return']
        return self._defaults['AbortKeepAlive']['return']

    def niDigital_ApplyLevelsAndTiming(self, vi, site_list, levels_sheet, timing_sheet, initial_state_high_pins, initial_state_low_pins, initial_state_tristate_pins):  # noqa: N802
        if self._defaults['ApplyLevelsAndTiming']['return'] != 0:
            return self._defaults['ApplyLevelsAndTiming']['return']
        return self._defaults['ApplyLevelsAndTiming']['return']

    def niDigital_ApplyTDROffsets(self, vi, channel_list, num_offsets, offsets):  # noqa: N802
        if self._defaults['ApplyTDROffsets']['return'] != 0:
            return self._defaults['ApplyTDROffsets']['return']
        return self._defaults['ApplyTDROffsets']['return']

    def niDigital_BurstPattern(self, vi, site_list, start_label, select_digital_function, wait_until_done, timeout):  # noqa: N802
        if self._defaults['BurstPattern']['return'] != 0:
            return self._defaults['BurstPattern']['return']
        return self._defaults['BurstPattern']['return']

    def niDigital_ClockGenerator_Abort(self, vi, channel_list):  # noqa: N802
        if self._defaults['ClockGenerator_Abort']['return'] != 0:
            return self._defaults['ClockGenerator_Abort']['return']
        return self._defaults['ClockGenerator_Abort']['return']

    def niDigital_ClockGenerator_GenerateClock(self, vi, channel_list, frequency, select_digital_function):  # noqa: N802
        if self._defaults['ClockGenerator_GenerateClock']['return'] != 0:
            return self._defaults['ClockGenerator_GenerateClock']['return']
        return self._defaults['ClockGenerator_GenerateClock']['return']

    def niDigital_Commit(self, vi):  # noqa: N802
        if self._defaults['Commit']['return'] != 0:
            return self._defaults['Commit']['return']
        return self._defaults['Commit']['return']

    def niDigital_ConfigureActiveLoadLevels(self, vi, channel_list, iol, ioh, vcom):  # noqa: N802
        if self._defaults['ConfigureActiveLoadLevels']['return'] != 0:
            return self._defaults['ConfigureActiveLoadLevels']['return']
        return self._defaults['ConfigureActiveLoadLevels']['return']

    def niDigital_ConfigurePatternBurstSites(self, vi, site_list):  # noqa: N802
        if self._defaults['ConfigurePatternBurstSites']['return'] != 0:
            return self._defaults['ConfigurePatternBurstSites']['return']
        return self._defaults['ConfigurePatternBurstSites']['return']

    def niDigital_ConfigureTimeSetCompareEdgesStrobe(self, vi, pin_list, time_set_name, strobe_edge):  # noqa: N802
        if self._defaults['ConfigureTimeSetCompareEdgesStrobe']['return'] != 0:
            return self._defaults['ConfigureTimeSetCompareEdgesStrobe']['return']
        return self._defaults['ConfigureTimeSetCompareEdgesStrobe']['return']

    def niDigital_ConfigureTimeSetCompareEdgesStrobe2x(self, vi, pin_list, time_set_name, strobe_edge, strobe2_edge):  # noqa: N802
        if self._defaults['ConfigureTimeSetCompareEdgesStrobe2x']['return'] != 0:
            return self._defaults['ConfigureTimeSetCompareEdgesStrobe2x']['return']
        return self._defaults['ConfigureTimeSetCompareEdgesStrobe2x']['return']

    def niDigital_ConfigureTimeSetDriveEdges(self, vi, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge):  # noqa: N802
        if self._defaults['ConfigureTimeSetDriveEdges']['return'] != 0:
            return self._defaults['ConfigureTimeSetDriveEdges']['return']
        return self._defaults['ConfigureTimeSetDriveEdges']['return']

    def niDigital_ConfigureTimeSetDriveEdges2x(self, vi, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge, drive_data2_edge, drive_return2_edge):  # noqa: N802
        if self._defaults['ConfigureTimeSetDriveEdges2x']['return'] != 0:
            return self._defaults['ConfigureTimeSetDriveEdges2x']['return']
        return self._defaults['ConfigureTimeSetDriveEdges2x']['return']

    def niDigital_ConfigureTimeSetDriveFormat(self, vi, pin_list, time_set_name, drive_format):  # noqa: N802
        if self._defaults['ConfigureTimeSetDriveFormat']['return'] != 0:
            return self._defaults['ConfigureTimeSetDriveFormat']['return']
        return self._defaults['ConfigureTimeSetDriveFormat']['return']

    def niDigital_ConfigureTimeSetEdge(self, vi, pin_list, time_set_name, edge, time):  # noqa: N802
        if self._defaults['ConfigureTimeSetEdge']['return'] != 0:
            return self._defaults['ConfigureTimeSetEdge']['return']
        return self._defaults['ConfigureTimeSetEdge']['return']

    def niDigital_ConfigureTimeSetEdgeMultiplier(self, vi, pin_list, time_set_name, edge_multiplier):  # noqa: N802
        if self._defaults['ConfigureTimeSetEdgeMultiplier']['return'] != 0:
            return self._defaults['ConfigureTimeSetEdgeMultiplier']['return']
        return self._defaults['ConfigureTimeSetEdgeMultiplier']['return']

    def niDigital_ConfigureTimeSetPeriod(self, vi, time_set_name, period):  # noqa: N802
        if self._defaults['ConfigureTimeSetPeriod']['return'] != 0:
            return self._defaults['ConfigureTimeSetPeriod']['return']
        return self._defaults['ConfigureTimeSetPeriod']['return']

    def niDigital_ConfigureVoltageLevels(self, vi, channel_list, vil, vih, vol, voh, vterm):  # noqa: N802
        if self._defaults['ConfigureVoltageLevels']['return'] != 0:
            return self._defaults['ConfigureVoltageLevels']['return']
        return self._defaults['ConfigureVoltageLevels']['return']

    def niDigital_CreateCaptureWaveformFromFileDigicapture(self, vi, waveform_name, waveform_file_path):  # noqa: N802
        if self._defaults['CreateCaptureWaveformFromFileDigicapture']['return'] != 0:
            return self._defaults['CreateCaptureWaveformFromFileDigicapture']['return']
        return self._defaults['CreateCaptureWaveformFromFileDigicapture']['return']

    def niDigital_CreateCaptureWaveformParallel(self, vi, pin_list, waveform_name):  # noqa: N802
        if self._defaults['CreateCaptureWaveformParallel']['return'] != 0:
            return self._defaults['CreateCaptureWaveformParallel']['return']
        return self._defaults['CreateCaptureWaveformParallel']['return']

    def niDigital_CreateCaptureWaveformSerial(self, vi, pin_list, waveform_name, sample_width, bit_order):  # noqa: N802
        if self._defaults['CreateCaptureWaveformSerial']['return'] != 0:
            return self._defaults['CreateCaptureWaveformSerial']['return']
        return self._defaults['CreateCaptureWaveformSerial']['return']

    def niDigital_CreateSourceWaveformFromFileTDMS(self, vi, waveform_name, waveform_file_path, write_waveform_data):  # noqa: N802
        if self._defaults['CreateSourceWaveformFromFileTDMS']['return'] != 0:
            return self._defaults['CreateSourceWaveformFromFileTDMS']['return']
        return self._defaults['CreateSourceWaveformFromFileTDMS']['return']

    def niDigital_CreateSourceWaveformParallel(self, vi, pin_list, waveform_name, data_mapping):  # noqa: N802
        if self._defaults['CreateSourceWaveformParallel']['return'] != 0:
            return self._defaults['CreateSourceWaveformParallel']['return']
        return self._defaults['CreateSourceWaveformParallel']['return']

    def niDigital_CreateSourceWaveformSerial(self, vi, pin_list, waveform_name, data_mapping, sample_width, bit_order):  # noqa: N802
        if self._defaults['CreateSourceWaveformSerial']['return'] != 0:
            return self._defaults['CreateSourceWaveformSerial']['return']
        return self._defaults['CreateSourceWaveformSerial']['return']

    def niDigital_CreateTimeSet(self, vi, name):  # noqa: N802
        if self._defaults['CreateTimeSet']['return'] != 0:
            return self._defaults['CreateTimeSet']['return']
        return self._defaults['CreateTimeSet']['return']

    def niDigital_DeleteAllTimeSets(self, vi):  # noqa: N802
        if self._defaults['DeleteAllTimeSets']['return'] != 0:
            return self._defaults['DeleteAllTimeSets']['return']
        return self._defaults['DeleteAllTimeSets']['return']

    def niDigital_DisableSites(self, vi, site_list):  # noqa: N802
        if self._defaults['DisableSites']['return'] != 0:
            return self._defaults['DisableSites']['return']
        return self._defaults['DisableSites']['return']

    def niDigital_EnableMatchFailCombination(self, session_count, sessions, sync_session):  # noqa: N802
        if self._defaults['EnableMatchFailCombination']['return'] != 0:
            return self._defaults['EnableMatchFailCombination']['return']
        return self._defaults['EnableMatchFailCombination']['return']

    def niDigital_EnableSites(self, vi, site_list):  # noqa: N802
        if self._defaults['EnableSites']['return'] != 0:
            return self._defaults['EnableSites']['return']
        return self._defaults['EnableSites']['return']

    def niDigital_FetchCaptureWaveformU32(self, vi, site_list, waveform_name, samples_to_read, timeout, data_buffer_size, data, actual_num_waveforms, actual_samples_per_waveform):  # noqa: N802
        if self._defaults['FetchCaptureWaveformU32']['return'] != 0:
            return self._defaults['FetchCaptureWaveformU32']['return']
        # actual_num_waveforms
        if self._defaults['FetchCaptureWaveformU32']['actualNumWaveforms'] is None:
            raise MockFunctionCallError("niDigital_FetchCaptureWaveformU32", param='actualNumWaveforms')
        if actual_num_waveforms is not None:
            actual_num_waveforms.contents.value = self._defaults['FetchCaptureWaveformU32']['actualNumWaveforms']
        # actual_samples_per_waveform
        if self._defaults['FetchCaptureWaveformU32']['actualSamplesPerWaveform'] is None:
            raise MockFunctionCallError("niDigital_FetchCaptureWaveformU32", param='actualSamplesPerWaveform')
        if actual_samples_per_waveform is not None:
            actual_samples_per_waveform.contents.value = self._defaults['FetchCaptureWaveformU32']['actualSamplesPerWaveform']
        # data
        if self._defaults['FetchCaptureWaveformU32']['data'] is None:
            raise MockFunctionCallError("niDigital_FetchCaptureWaveformU32", param='data')
        if data_buffer_size.value == 0:
            return len(self._defaults['FetchCaptureWaveformU32']['data'])
        try:
            data_ref = data.contents
        except AttributeError:
            data_ref = data
        for i in range(len(self._defaults['FetchCaptureWaveformU32']['data'])):
            data_ref[i] = self._defaults['FetchCaptureWaveformU32']['data'][i]
        return self._defaults['FetchCaptureWaveformU32']['return']

    def niDigital_FetchHistoryRAMCycleInformation(self, vi, site, sample_index, pattern_index, time_set_index, vector_number, cycle_number, num_dut_cycles):  # noqa: N802
        if self._defaults['FetchHistoryRAMCycleInformation']['return'] != 0:
            return self._defaults['FetchHistoryRAMCycleInformation']['return']
        # pattern_index
        if self._defaults['FetchHistoryRAMCycleInformation']['patternIndex'] is None:
            raise MockFunctionCallError("niDigital_FetchHistoryRAMCycleInformation", param='patternIndex')
        if pattern_index is not None:
            pattern_index.contents.value = self._defaults['FetchHistoryRAMCycleInformation']['patternIndex']
        # time_set_index
        if self._defaults['FetchHistoryRAMCycleInformation']['timeSetIndex'] is None:
            raise MockFunctionCallError("niDigital_FetchHistoryRAMCycleInformation", param='timeSetIndex')
        if time_set_index is not None:
            time_set_index.contents.value = self._defaults['FetchHistoryRAMCycleInformation']['timeSetIndex']
        # vector_number
        if self._defaults['FetchHistoryRAMCycleInformation']['vectorNumber'] is None:
            raise MockFunctionCallError("niDigital_FetchHistoryRAMCycleInformation", param='vectorNumber')
        if vector_number is not None:
            vector_number.contents.value = self._defaults['FetchHistoryRAMCycleInformation']['vectorNumber']
        # cycle_number
        if self._defaults['FetchHistoryRAMCycleInformation']['cycleNumber'] is None:
            raise MockFunctionCallError("niDigital_FetchHistoryRAMCycleInformation", param='cycleNumber')
        if cycle_number is not None:
            cycle_number.contents.value = self._defaults['FetchHistoryRAMCycleInformation']['cycleNumber']
        # num_dut_cycles
        if self._defaults['FetchHistoryRAMCycleInformation']['numDutCycles'] is None:
            raise MockFunctionCallError("niDigital_FetchHistoryRAMCycleInformation", param='numDutCycles')
        if num_dut_cycles is not None:
            num_dut_cycles.contents.value = self._defaults['FetchHistoryRAMCycleInformation']['numDutCycles']
        return self._defaults['FetchHistoryRAMCycleInformation']['return']

    def niDigital_FetchHistoryRAMCyclePinData(self, vi, site, pin_list, sample_index, dut_cycle_index, pin_data_buffer_size, expected_pin_states, actual_pin_states, per_pin_pass_fail, actual_num_pin_data):  # noqa: N802
        if self._defaults['FetchHistoryRAMCyclePinData']['return'] != 0:
            return self._defaults['FetchHistoryRAMCyclePinData']['return']
        # actual_num_pin_data
        if self._defaults['FetchHistoryRAMCyclePinData']['actualNumPinData'] is None:
            raise MockFunctionCallError("niDigital_FetchHistoryRAMCyclePinData", param='actualNumPinData')
        if actual_num_pin_data is not None:
            actual_num_pin_data.contents.value = self._defaults['FetchHistoryRAMCyclePinData']['actualNumPinData']
        # expected_pin_states
        if self._defaults['FetchHistoryRAMCyclePinData']['expectedPinStates'] is None:
            raise MockFunctionCallError("niDigital_FetchHistoryRAMCyclePinData", param='expectedPinStates')
        if pin_data_buffer_size.value == 0:
            return len(self._defaults['FetchHistoryRAMCyclePinData']['expectedPinStates'])
        try:
            expected_pin_states_ref = expected_pin_states.contents
        except AttributeError:
            expected_pin_states_ref = expected_pin_states
        for i in range(len(self._defaults['FetchHistoryRAMCyclePinData']['expectedPinStates'])):
            expected_pin_states_ref[i] = self._defaults['FetchHistoryRAMCyclePinData']['expectedPinStates'][i]
        # actual_pin_states
        if self._defaults['FetchHistoryRAMCyclePinData']['actualPinStates'] is None:
            raise MockFunctionCallError("niDigital_FetchHistoryRAMCyclePinData", param='actualPinStates')
        if pin_data_buffer_size.value == 0:
            return len(self._defaults['FetchHistoryRAMCyclePinData']['actualPinStates'])
        try:
            actual_pin_states_ref = actual_pin_states.contents
        except AttributeError:
            actual_pin_states_ref = actual_pin_states
        for i in range(len(self._defaults['FetchHistoryRAMCyclePinData']['actualPinStates'])):
            actual_pin_states_ref[i] = self._defaults['FetchHistoryRAMCyclePinData']['actualPinStates'][i]
        # per_pin_pass_fail
        if self._defaults['FetchHistoryRAMCyclePinData']['perPinPassFail'] is None:
            raise MockFunctionCallError("niDigital_FetchHistoryRAMCyclePinData", param='perPinPassFail')
        if pin_data_buffer_size.value == 0:
            return len(self._defaults['FetchHistoryRAMCyclePinData']['perPinPassFail'])
        try:
            per_pin_pass_fail_ref = per_pin_pass_fail.contents
        except AttributeError:
            per_pin_pass_fail_ref = per_pin_pass_fail
        for i in range(len(self._defaults['FetchHistoryRAMCyclePinData']['perPinPassFail'])):
            per_pin_pass_fail_ref[i] = self._defaults['FetchHistoryRAMCyclePinData']['perPinPassFail'][i]
        return self._defaults['FetchHistoryRAMCyclePinData']['return']

    def niDigital_FetchHistoryRAMScanCycleNumber(self, vi, site, sample_index, scan_cycle_number):  # noqa: N802
        if self._defaults['FetchHistoryRAMScanCycleNumber']['return'] != 0:
            return self._defaults['FetchHistoryRAMScanCycleNumber']['return']
        # scan_cycle_number
        if self._defaults['FetchHistoryRAMScanCycleNumber']['scanCycleNumber'] is None:
            raise MockFunctionCallError("niDigital_FetchHistoryRAMScanCycleNumber", param='scanCycleNumber')
        if scan_cycle_number is not None:
            scan_cycle_number.contents.value = self._defaults['FetchHistoryRAMScanCycleNumber']['scanCycleNumber']
        return self._defaults['FetchHistoryRAMScanCycleNumber']['return']

    def niDigital_FrequencyCounter_MeasureFrequency(self, vi, channel_list, frequencies_buffer_size, frequencies, actual_num_frequencies):  # noqa: N802
        if self._defaults['FrequencyCounter_MeasureFrequency']['return'] != 0:
            return self._defaults['FrequencyCounter_MeasureFrequency']['return']
        # actual_num_frequencies
        if self._defaults['FrequencyCounter_MeasureFrequency']['actualNumFrequencies'] is None:
            raise MockFunctionCallError("niDigital_FrequencyCounter_MeasureFrequency", param='actualNumFrequencies')
        if actual_num_frequencies is not None:
            actual_num_frequencies.contents.value = self._defaults['FrequencyCounter_MeasureFrequency']['actualNumFrequencies']
        # frequencies
        if self._defaults['FrequencyCounter_MeasureFrequency']['frequencies'] is None:
            raise MockFunctionCallError("niDigital_FrequencyCounter_MeasureFrequency", param='frequencies')
        if frequencies_buffer_size.value == 0:
            return len(self._defaults['FrequencyCounter_MeasureFrequency']['frequencies'])
        try:
            frequencies_ref = frequencies.contents
        except AttributeError:
            frequencies_ref = frequencies
        for i in range(len(self._defaults['FrequencyCounter_MeasureFrequency']['frequencies'])):
            frequencies_ref[i] = self._defaults['FrequencyCounter_MeasureFrequency']['frequencies'][i]
        return self._defaults['FrequencyCounter_MeasureFrequency']['return']

    def niDigital_GetAttributeViBoolean(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['GetAttributeViBoolean']['return'] != 0:
            return self._defaults['GetAttributeViBoolean']['return']
        # value
        if self._defaults['GetAttributeViBoolean']['value'] is None:
            raise MockFunctionCallError("niDigital_GetAttributeViBoolean", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViBoolean']['value']
        return self._defaults['GetAttributeViBoolean']['return']

    def niDigital_GetAttributeViInt32(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['GetAttributeViInt32']['return'] != 0:
            return self._defaults['GetAttributeViInt32']['return']
        # value
        if self._defaults['GetAttributeViInt32']['value'] is None:
            raise MockFunctionCallError("niDigital_GetAttributeViInt32", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViInt32']['value']
        return self._defaults['GetAttributeViInt32']['return']

    def niDigital_GetAttributeViInt64(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['GetAttributeViInt64']['return'] != 0:
            return self._defaults['GetAttributeViInt64']['return']
        # value
        if self._defaults['GetAttributeViInt64']['value'] is None:
            raise MockFunctionCallError("niDigital_GetAttributeViInt64", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViInt64']['value']
        return self._defaults['GetAttributeViInt64']['return']

    def niDigital_GetAttributeViReal64(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['GetAttributeViReal64']['return'] != 0:
            return self._defaults['GetAttributeViReal64']['return']
        # value
        if self._defaults['GetAttributeViReal64']['value'] is None:
            raise MockFunctionCallError("niDigital_GetAttributeViReal64", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViReal64']['value']
        return self._defaults['GetAttributeViReal64']['return']

    def niDigital_GetAttributeViString(self, vi, channel_name, attribute, buffer_size, value):  # noqa: N802
        if self._defaults['GetAttributeViString']['return'] != 0:
            return self._defaults['GetAttributeViString']['return']
        # value
        if self._defaults['GetAttributeViString']['value'] is None:
            raise MockFunctionCallError("niDigital_GetAttributeViString", param='value')
        if buffer_size.value == 0:
            return len(self._defaults['GetAttributeViString']['value'])
        value.value = self._defaults['GetAttributeViString']['value'].encode('ascii')
        return self._defaults['GetAttributeViString']['return']

    def niDigital_GetChannelNameFromString(self, vi, indices, name_buffer_size, names):  # noqa: N802
        if self._defaults['GetChannelNameFromString']['return'] != 0:
            return self._defaults['GetChannelNameFromString']['return']
        # names
        if self._defaults['GetChannelNameFromString']['name'] is None:
            raise MockFunctionCallError("niDigital_GetChannelNameFromString", param='name')
        if name_buffer_size.value == 0:
            return len(self._defaults['GetChannelNameFromString']['name'])
        names.value = self._defaults['GetChannelNameFromString']['name'].encode('ascii')
        return self._defaults['GetChannelNameFromString']['return']

    def niDigital_GetError(self, vi, error_code, error_description_buffer_size, error_description):  # noqa: N802
        if self._defaults['GetError']['return'] != 0:
            return self._defaults['GetError']['return']
        # error_code
        if self._defaults['GetError']['errorCode'] is None:
            raise MockFunctionCallError("niDigital_GetError", param='errorCode')
        if error_code is not None:
            error_code.contents.value = self._defaults['GetError']['errorCode']
        # error_description
        if self._defaults['GetError']['errorDescription'] is None:
            raise MockFunctionCallError("niDigital_GetError", param='errorDescription')
        if error_description_buffer_size.value == 0:
            return len(self._defaults['GetError']['errorDescription'])
        error_description.value = self._defaults['GetError']['errorDescription'].encode('ascii')
        return self._defaults['GetError']['return']

    def niDigital_GetFailCount(self, vi, channel_list, buffer_size, failure_count, actual_num_read):  # noqa: N802
        if self._defaults['GetFailCount']['return'] != 0:
            return self._defaults['GetFailCount']['return']
        # actual_num_read
        if self._defaults['GetFailCount']['actualNumRead'] is None:
            raise MockFunctionCallError("niDigital_GetFailCount", param='actualNumRead')
        if actual_num_read is not None:
            actual_num_read.contents.value = self._defaults['GetFailCount']['actualNumRead']
        # failure_count
        if self._defaults['GetFailCount']['failureCount'] is None:
            raise MockFunctionCallError("niDigital_GetFailCount", param='failureCount')
        if buffer_size.value == 0:
            return len(self._defaults['GetFailCount']['failureCount'])
        try:
            failure_count_ref = failure_count.contents
        except AttributeError:
            failure_count_ref = failure_count
        for i in range(len(self._defaults['GetFailCount']['failureCount'])):
            failure_count_ref[i] = self._defaults['GetFailCount']['failureCount'][i]
        return self._defaults['GetFailCount']['return']

    def niDigital_GetHistoryRAMSampleCount(self, vi, site, sample_count):  # noqa: N802
        if self._defaults['GetHistoryRAMSampleCount']['return'] != 0:
            return self._defaults['GetHistoryRAMSampleCount']['return']
        # sample_count
        if self._defaults['GetHistoryRAMSampleCount']['sampleCount'] is None:
            raise MockFunctionCallError("niDigital_GetHistoryRAMSampleCount", param='sampleCount')
        if sample_count is not None:
            sample_count.contents.value = self._defaults['GetHistoryRAMSampleCount']['sampleCount']
        return self._defaults['GetHistoryRAMSampleCount']['return']

    def niDigital_GetPatternName(self, vi, pattern_index, name_buffer_size, name):  # noqa: N802
        if self._defaults['GetPatternName']['return'] != 0:
            return self._defaults['GetPatternName']['return']
        # name
        if self._defaults['GetPatternName']['name'] is None:
            raise MockFunctionCallError("niDigital_GetPatternName", param='name')
        if name_buffer_size.value == 0:
            return len(self._defaults['GetPatternName']['name'])
        name.value = self._defaults['GetPatternName']['name'].encode('ascii')
        return self._defaults['GetPatternName']['return']

    def niDigital_GetPatternPinList(self, vi, start_label, pin_list_buffer_size, pin_list):  # noqa: N802
        if self._defaults['GetPatternPinList']['return'] != 0:
            return self._defaults['GetPatternPinList']['return']
        # pin_list
        if self._defaults['GetPatternPinList']['pinList'] is None:
            raise MockFunctionCallError("niDigital_GetPatternPinList", param='pinList')
        if pin_list_buffer_size.value == 0:
            return len(self._defaults['GetPatternPinList']['pinList'])
        pin_list.value = self._defaults['GetPatternPinList']['pinList'].encode('ascii')
        return self._defaults['GetPatternPinList']['return']

    def niDigital_GetPinName(self, vi, pin_index, name_buffer_size, name):  # noqa: N802
        if self._defaults['GetPinName']['return'] != 0:
            return self._defaults['GetPinName']['return']
        # name
        if self._defaults['GetPinName']['name'] is None:
            raise MockFunctionCallError("niDigital_GetPinName", param='name')
        if name_buffer_size.value == 0:
            return len(self._defaults['GetPinName']['name'])
        name.value = self._defaults['GetPinName']['name'].encode('ascii')
        return self._defaults['GetPinName']['return']

    def niDigital_GetPinResultsPinInformation(self, vi, channel_list, buffer_size, pin_indexes, site_numbers, channel_indexes, actual_num_values):  # noqa: N802
        if self._defaults['GetPinResultsPinInformation']['return'] != 0:
            return self._defaults['GetPinResultsPinInformation']['return']
        # actual_num_values
        if self._defaults['GetPinResultsPinInformation']['actualNumValues'] is None:
            raise MockFunctionCallError("niDigital_GetPinResultsPinInformation", param='actualNumValues')
        if actual_num_values is not None:
            actual_num_values.contents.value = self._defaults['GetPinResultsPinInformation']['actualNumValues']
        # pin_indexes
        if self._defaults['GetPinResultsPinInformation']['pinIndexes'] is None:
            raise MockFunctionCallError("niDigital_GetPinResultsPinInformation", param='pinIndexes')
        if buffer_size.value == 0:
            return len(self._defaults['GetPinResultsPinInformation']['pinIndexes'])
        try:
            pin_indexes_ref = pin_indexes.contents
        except AttributeError:
            pin_indexes_ref = pin_indexes
        for i in range(len(self._defaults['GetPinResultsPinInformation']['pinIndexes'])):
            pin_indexes_ref[i] = self._defaults['GetPinResultsPinInformation']['pinIndexes'][i]
        # site_numbers
        if self._defaults['GetPinResultsPinInformation']['siteNumbers'] is None:
            raise MockFunctionCallError("niDigital_GetPinResultsPinInformation", param='siteNumbers')
        if buffer_size.value == 0:
            return len(self._defaults['GetPinResultsPinInformation']['siteNumbers'])
        try:
            site_numbers_ref = site_numbers.contents
        except AttributeError:
            site_numbers_ref = site_numbers
        for i in range(len(self._defaults['GetPinResultsPinInformation']['siteNumbers'])):
            site_numbers_ref[i] = self._defaults['GetPinResultsPinInformation']['siteNumbers'][i]
        # channel_indexes
        if self._defaults['GetPinResultsPinInformation']['channelIndexes'] is None:
            raise MockFunctionCallError("niDigital_GetPinResultsPinInformation", param='channelIndexes')
        if buffer_size.value == 0:
            return len(self._defaults['GetPinResultsPinInformation']['channelIndexes'])
        try:
            channel_indexes_ref = channel_indexes.contents
        except AttributeError:
            channel_indexes_ref = channel_indexes
        for i in range(len(self._defaults['GetPinResultsPinInformation']['channelIndexes'])):
            channel_indexes_ref[i] = self._defaults['GetPinResultsPinInformation']['channelIndexes'][i]
        return self._defaults['GetPinResultsPinInformation']['return']

    def niDigital_GetSitePassFail(self, vi, site_list, pass_fail_buffer_size, pass_fail, actual_num_sites):  # noqa: N802
        if self._defaults['GetSitePassFail']['return'] != 0:
            return self._defaults['GetSitePassFail']['return']
        # actual_num_sites
        if self._defaults['GetSitePassFail']['actualNumSites'] is None:
            raise MockFunctionCallError("niDigital_GetSitePassFail", param='actualNumSites')
        if actual_num_sites is not None:
            actual_num_sites.contents.value = self._defaults['GetSitePassFail']['actualNumSites']
        # pass_fail
        if self._defaults['GetSitePassFail']['passFail'] is None:
            raise MockFunctionCallError("niDigital_GetSitePassFail", param='passFail')
        if pass_fail_buffer_size.value == 0:
            return len(self._defaults['GetSitePassFail']['passFail'])
        try:
            pass_fail_ref = pass_fail.contents
        except AttributeError:
            pass_fail_ref = pass_fail
        for i in range(len(self._defaults['GetSitePassFail']['passFail'])):
            pass_fail_ref[i] = self._defaults['GetSitePassFail']['passFail'][i]
        return self._defaults['GetSitePassFail']['return']

    def niDigital_GetSiteResultsSiteNumbers(self, vi, site_list, site_result_type, site_numbers_buffer_size, site_numbers, actual_num_site_numbers):  # noqa: N802
        if self._defaults['GetSiteResultsSiteNumbers']['return'] != 0:
            return self._defaults['GetSiteResultsSiteNumbers']['return']
        # actual_num_site_numbers
        if self._defaults['GetSiteResultsSiteNumbers']['actualNumSiteNumbers'] is None:
            raise MockFunctionCallError("niDigital_GetSiteResultsSiteNumbers", param='actualNumSiteNumbers')
        if actual_num_site_numbers is not None:
            actual_num_site_numbers.contents.value = self._defaults['GetSiteResultsSiteNumbers']['actualNumSiteNumbers']
        # site_numbers
        if self._defaults['GetSiteResultsSiteNumbers']['siteNumbers'] is None:
            raise MockFunctionCallError("niDigital_GetSiteResultsSiteNumbers", param='siteNumbers')
        if site_numbers_buffer_size.value == 0:
            return len(self._defaults['GetSiteResultsSiteNumbers']['siteNumbers'])
        try:
            site_numbers_ref = site_numbers.contents
        except AttributeError:
            site_numbers_ref = site_numbers
        for i in range(len(self._defaults['GetSiteResultsSiteNumbers']['siteNumbers'])):
            site_numbers_ref[i] = self._defaults['GetSiteResultsSiteNumbers']['siteNumbers'][i]
        return self._defaults['GetSiteResultsSiteNumbers']['return']

    def niDigital_GetTimeSetDriveFormat(self, vi, pin, time_set_name, format):  # noqa: N802
        if self._defaults['GetTimeSetDriveFormat']['return'] != 0:
            return self._defaults['GetTimeSetDriveFormat']['return']
        # format
        if self._defaults['GetTimeSetDriveFormat']['format'] is None:
            raise MockFunctionCallError("niDigital_GetTimeSetDriveFormat", param='format')
        if format is not None:
            format.contents.value = self._defaults['GetTimeSetDriveFormat']['format']
        return self._defaults['GetTimeSetDriveFormat']['return']

    def niDigital_GetTimeSetEdge(self, vi, pin, time_set_name, edge, time):  # noqa: N802
        if self._defaults['GetTimeSetEdge']['return'] != 0:
            return self._defaults['GetTimeSetEdge']['return']
        # time
        if self._defaults['GetTimeSetEdge']['time'] is None:
            raise MockFunctionCallError("niDigital_GetTimeSetEdge", param='time')
        if time is not None:
            time.contents.value = self._defaults['GetTimeSetEdge']['time']
        return self._defaults['GetTimeSetEdge']['return']

    def niDigital_GetTimeSetEdgeMultiplier(self, vi, pin, time_set_name, edge_multiplier):  # noqa: N802
        if self._defaults['GetTimeSetEdgeMultiplier']['return'] != 0:
            return self._defaults['GetTimeSetEdgeMultiplier']['return']
        # edge_multiplier
        if self._defaults['GetTimeSetEdgeMultiplier']['edgeMultiplier'] is None:
            raise MockFunctionCallError("niDigital_GetTimeSetEdgeMultiplier", param='edgeMultiplier')
        if edge_multiplier is not None:
            edge_multiplier.contents.value = self._defaults['GetTimeSetEdgeMultiplier']['edgeMultiplier']
        return self._defaults['GetTimeSetEdgeMultiplier']['return']

    def niDigital_GetTimeSetName(self, vi, time_set_index, name_buffer_size, name):  # noqa: N802
        if self._defaults['GetTimeSetName']['return'] != 0:
            return self._defaults['GetTimeSetName']['return']
        # name
        if self._defaults['GetTimeSetName']['name'] is None:
            raise MockFunctionCallError("niDigital_GetTimeSetName", param='name')
        if name_buffer_size.value == 0:
            return len(self._defaults['GetTimeSetName']['name'])
        name.value = self._defaults['GetTimeSetName']['name'].encode('ascii')
        return self._defaults['GetTimeSetName']['return']

    def niDigital_GetTimeSetPeriod(self, vi, time_set_name, period):  # noqa: N802
        if self._defaults['GetTimeSetPeriod']['return'] != 0:
            return self._defaults['GetTimeSetPeriod']['return']
        # period
        if self._defaults['GetTimeSetPeriod']['period'] is None:
            raise MockFunctionCallError("niDigital_GetTimeSetPeriod", param='period')
        if period is not None:
            period.contents.value = self._defaults['GetTimeSetPeriod']['period']
        return self._defaults['GetTimeSetPeriod']['return']

    def niDigital_InitWithOptions(self, resource_name, id_query, reset_device, option_string, new_vi):  # noqa: N802
        if self._defaults['InitWithOptions']['return'] != 0:
            return self._defaults['InitWithOptions']['return']
        # new_vi
        if self._defaults['InitWithOptions']['newVi'] is None:
            raise MockFunctionCallError("niDigital_InitWithOptions", param='newVi')
        if new_vi is not None:
            new_vi.contents.value = self._defaults['InitWithOptions']['newVi']
        return self._defaults['InitWithOptions']['return']

    def niDigital_Initiate(self, vi):  # noqa: N802
        if self._defaults['Initiate']['return'] != 0:
            return self._defaults['Initiate']['return']
        return self._defaults['Initiate']['return']

    def niDigital_IsDone(self, vi, done):  # noqa: N802
        if self._defaults['IsDone']['return'] != 0:
            return self._defaults['IsDone']['return']
        # done
        if self._defaults['IsDone']['done'] is None:
            raise MockFunctionCallError("niDigital_IsDone", param='done')
        if done is not None:
            done.contents.value = self._defaults['IsDone']['done']
        return self._defaults['IsDone']['return']

    def niDigital_IsSiteEnabled(self, vi, site, enable):  # noqa: N802
        if self._defaults['IsSiteEnabled']['return'] != 0:
            return self._defaults['IsSiteEnabled']['return']
        # enable
        if self._defaults['IsSiteEnabled']['enable'] is None:
            raise MockFunctionCallError("niDigital_IsSiteEnabled", param='enable')
        if enable is not None:
            enable.contents.value = self._defaults['IsSiteEnabled']['enable']
        return self._defaults['IsSiteEnabled']['return']

    def niDigital_LoadLevels(self, vi, file_path):  # noqa: N802
        if self._defaults['LoadLevels']['return'] != 0:
            return self._defaults['LoadLevels']['return']
        return self._defaults['LoadLevels']['return']

    def niDigital_LoadPattern(self, vi, file_path):  # noqa: N802
        if self._defaults['LoadPattern']['return'] != 0:
            return self._defaults['LoadPattern']['return']
        return self._defaults['LoadPattern']['return']

    def niDigital_LoadPinMap(self, vi, file_path):  # noqa: N802
        if self._defaults['LoadPinMap']['return'] != 0:
            return self._defaults['LoadPinMap']['return']
        return self._defaults['LoadPinMap']['return']

    def niDigital_LoadSpecifications(self, vi, file_path):  # noqa: N802
        if self._defaults['LoadSpecifications']['return'] != 0:
            return self._defaults['LoadSpecifications']['return']
        return self._defaults['LoadSpecifications']['return']

    def niDigital_LoadTiming(self, vi, file_path):  # noqa: N802
        if self._defaults['LoadTiming']['return'] != 0:
            return self._defaults['LoadTiming']['return']
        return self._defaults['LoadTiming']['return']

    def niDigital_LockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['LockSession']['return'] != 0:
            return self._defaults['LockSession']['return']
        # caller_has_lock
        if self._defaults['LockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niDigital_LockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['LockSession']['callerHasLock']
        return self._defaults['LockSession']['return']

    def niDigital_PPMU_Measure(self, vi, channel_list, measurement_type, buffer_size, measurements, actual_num_read):  # noqa: N802
        if self._defaults['PPMU_Measure']['return'] != 0:
            return self._defaults['PPMU_Measure']['return']
        # actual_num_read
        if self._defaults['PPMU_Measure']['actualNumRead'] is None:
            raise MockFunctionCallError("niDigital_PPMU_Measure", param='actualNumRead')
        if actual_num_read is not None:
            actual_num_read.contents.value = self._defaults['PPMU_Measure']['actualNumRead']
        # measurements
        if self._defaults['PPMU_Measure']['measurements'] is None:
            raise MockFunctionCallError("niDigital_PPMU_Measure", param='measurements')
        if buffer_size.value == 0:
            return len(self._defaults['PPMU_Measure']['measurements'])
        try:
            measurements_ref = measurements.contents
        except AttributeError:
            measurements_ref = measurements
        for i in range(len(self._defaults['PPMU_Measure']['measurements'])):
            measurements_ref[i] = self._defaults['PPMU_Measure']['measurements'][i]
        return self._defaults['PPMU_Measure']['return']

    def niDigital_PPMU_Source(self, vi, channel_list):  # noqa: N802
        if self._defaults['PPMU_Source']['return'] != 0:
            return self._defaults['PPMU_Source']['return']
        return self._defaults['PPMU_Source']['return']

    def niDigital_ReadSequencerFlag(self, vi, flag, value):  # noqa: N802
        if self._defaults['ReadSequencerFlag']['return'] != 0:
            return self._defaults['ReadSequencerFlag']['return']
        # value
        if self._defaults['ReadSequencerFlag']['value'] is None:
            raise MockFunctionCallError("niDigital_ReadSequencerFlag", param='value')
        if value is not None:
            value.contents.value = self._defaults['ReadSequencerFlag']['value']
        return self._defaults['ReadSequencerFlag']['return']

    def niDigital_ReadSequencerRegister(self, vi, reg, value):  # noqa: N802
        if self._defaults['ReadSequencerRegister']['return'] != 0:
            return self._defaults['ReadSequencerRegister']['return']
        # value
        if self._defaults['ReadSequencerRegister']['value'] is None:
            raise MockFunctionCallError("niDigital_ReadSequencerRegister", param='value')
        if value is not None:
            value.contents.value = self._defaults['ReadSequencerRegister']['value']
        return self._defaults['ReadSequencerRegister']['return']

    def niDigital_ReadStatic(self, vi, channel_list, buffer_size, data, actual_num_read):  # noqa: N802
        if self._defaults['ReadStatic']['return'] != 0:
            return self._defaults['ReadStatic']['return']
        # actual_num_read
        if self._defaults['ReadStatic']['actualNumRead'] is None:
            raise MockFunctionCallError("niDigital_ReadStatic", param='actualNumRead')
        if actual_num_read is not None:
            actual_num_read.contents.value = self._defaults['ReadStatic']['actualNumRead']
        # data
        if self._defaults['ReadStatic']['data'] is None:
            raise MockFunctionCallError("niDigital_ReadStatic", param='data')
        if buffer_size.value == 0:
            return len(self._defaults['ReadStatic']['data'])
        try:
            data_ref = data.contents
        except AttributeError:
            data_ref = data
        for i in range(len(self._defaults['ReadStatic']['data'])):
            data_ref[i] = self._defaults['ReadStatic']['data'][i]
        return self._defaults['ReadStatic']['return']

    def niDigital_ResetDevice(self, vi):  # noqa: N802
        if self._defaults['ResetDevice']['return'] != 0:
            return self._defaults['ResetDevice']['return']
        return self._defaults['ResetDevice']['return']

    def niDigital_SelfCalibrate(self, vi):  # noqa: N802
        if self._defaults['SelfCalibrate']['return'] != 0:
            return self._defaults['SelfCalibrate']['return']
        return self._defaults['SelfCalibrate']['return']

    def niDigital_SendSoftwareEdgeTrigger(self, vi, trigger, trigger_identifier):  # noqa: N802
        if self._defaults['SendSoftwareEdgeTrigger']['return'] != 0:
            return self._defaults['SendSoftwareEdgeTrigger']['return']
        return self._defaults['SendSoftwareEdgeTrigger']['return']

    def niDigital_SetAttributeViBoolean(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['SetAttributeViBoolean']['return'] != 0:
            return self._defaults['SetAttributeViBoolean']['return']
        return self._defaults['SetAttributeViBoolean']['return']

    def niDigital_SetAttributeViInt32(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['SetAttributeViInt32']['return'] != 0:
            return self._defaults['SetAttributeViInt32']['return']
        return self._defaults['SetAttributeViInt32']['return']

    def niDigital_SetAttributeViInt64(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['SetAttributeViInt64']['return'] != 0:
            return self._defaults['SetAttributeViInt64']['return']
        return self._defaults['SetAttributeViInt64']['return']

    def niDigital_SetAttributeViReal64(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['SetAttributeViReal64']['return'] != 0:
            return self._defaults['SetAttributeViReal64']['return']
        return self._defaults['SetAttributeViReal64']['return']

    def niDigital_SetAttributeViString(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['SetAttributeViString']['return'] != 0:
            return self._defaults['SetAttributeViString']['return']
        return self._defaults['SetAttributeViString']['return']

    def niDigital_SetRuntimeEnvironment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        if self._defaults['SetRuntimeEnvironment']['return'] != 0:
            return self._defaults['SetRuntimeEnvironment']['return']
        return self._defaults['SetRuntimeEnvironment']['return']

    def niDigital_TDR(self, vi, channel_list, apply_offsets, offsets_buffer_size, offsets, actual_num_offsets):  # noqa: N802
        if self._defaults['TDR']['return'] != 0:
            return self._defaults['TDR']['return']
        # actual_num_offsets
        if self._defaults['TDR']['actualNumOffsets'] is None:
            raise MockFunctionCallError("niDigital_TDR", param='actualNumOffsets')
        if actual_num_offsets is not None:
            actual_num_offsets.contents.value = self._defaults['TDR']['actualNumOffsets']
        # offsets
        if self._defaults['TDR']['offsets'] is None:
            raise MockFunctionCallError("niDigital_TDR", param='offsets')
        if offsets_buffer_size.value == 0:
            return len(self._defaults['TDR']['offsets'])
        try:
            offsets_ref = offsets.contents
        except AttributeError:
            offsets_ref = offsets
        for i in range(len(self._defaults['TDR']['offsets'])):
            offsets_ref[i] = self._defaults['TDR']['offsets'][i]
        return self._defaults['TDR']['return']

    def niDigital_UnloadAllPatterns(self, vi, unload_keep_alive_pattern):  # noqa: N802
        if self._defaults['UnloadAllPatterns']['return'] != 0:
            return self._defaults['UnloadAllPatterns']['return']
        return self._defaults['UnloadAllPatterns']['return']

    def niDigital_UnloadSpecifications(self, vi, file_path):  # noqa: N802
        if self._defaults['UnloadSpecifications']['return'] != 0:
            return self._defaults['UnloadSpecifications']['return']
        return self._defaults['UnloadSpecifications']['return']

    def niDigital_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['UnlockSession']['return'] != 0:
            return self._defaults['UnlockSession']['return']
        # caller_has_lock
        if self._defaults['UnlockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niDigital_UnlockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['UnlockSession']['callerHasLock']
        return self._defaults['UnlockSession']['return']

    def niDigital_WaitUntilDone(self, vi, timeout):  # noqa: N802
        if self._defaults['WaitUntilDone']['return'] != 0:
            return self._defaults['WaitUntilDone']['return']
        return self._defaults['WaitUntilDone']['return']

    def niDigital_WriteSequencerFlag(self, vi, flag, value):  # noqa: N802
        if self._defaults['WriteSequencerFlag']['return'] != 0:
            return self._defaults['WriteSequencerFlag']['return']
        return self._defaults['WriteSequencerFlag']['return']

    def niDigital_WriteSequencerRegister(self, vi, reg, value):  # noqa: N802
        if self._defaults['WriteSequencerRegister']['return'] != 0:
            return self._defaults['WriteSequencerRegister']['return']
        return self._defaults['WriteSequencerRegister']['return']

    def niDigital_WriteSourceWaveformBroadcastU32(self, vi, waveform_name, waveform_size, waveform_data):  # noqa: N802
        if self._defaults['WriteSourceWaveformBroadcastU32']['return'] != 0:
            return self._defaults['WriteSourceWaveformBroadcastU32']['return']
        return self._defaults['WriteSourceWaveformBroadcastU32']['return']

    def niDigital_WriteSourceWaveformDataFromFileTDMS(self, vi, waveform_name, waveform_file_path):  # noqa: N802
        if self._defaults['WriteSourceWaveformDataFromFileTDMS']['return'] != 0:
            return self._defaults['WriteSourceWaveformDataFromFileTDMS']['return']
        return self._defaults['WriteSourceWaveformDataFromFileTDMS']['return']

    def niDigital_WriteSourceWaveformSiteUniqueU32(self, vi, site_list, waveform_name, num_waveforms, samples_per_waveform, waveform_data):  # noqa: N802
        if self._defaults['WriteSourceWaveformSiteUniqueU32']['return'] != 0:
            return self._defaults['WriteSourceWaveformSiteUniqueU32']['return']
        return self._defaults['WriteSourceWaveformSiteUniqueU32']['return']

    def niDigital_WriteStatic(self, vi, channel_list, state):  # noqa: N802
        if self._defaults['WriteStatic']['return'] != 0:
            return self._defaults['WriteStatic']['return']
        return self._defaults['WriteStatic']['return']

    def niDigital_close(self, vi):  # noqa: N802
        if self._defaults['close']['return'] != 0:
            return self._defaults['close']['return']
        return self._defaults['close']['return']

    def niDigital_error_message(self, vi, error_code, error_message):  # noqa: N802
        if self._defaults['error_message']['return'] != 0:
            return self._defaults['error_message']['return']
        # error_message
        if self._defaults['error_message']['errorMessage'] is None:
            raise MockFunctionCallError("niDigital_error_message", param='errorMessage')
        test_value = self._defaults['error_message']['errorMessage']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(error_message) >= len(test_value)
        for i in range(len(test_value)):
            error_message[i] = test_value[i]
        return self._defaults['error_message']['return']

    def niDigital_reset(self, vi):  # noqa: N802
        if self._defaults['reset']['return'] != 0:
            return self._defaults['reset']['return']
        return self._defaults['reset']['return']

    def niDigital_self_test(self, vi, test_result, test_message):  # noqa: N802
        if self._defaults['self_test']['return'] != 0:
            return self._defaults['self_test']['return']
        # test_result
        if self._defaults['self_test']['testResult'] is None:
            raise MockFunctionCallError("niDigital_self_test", param='testResult')
        if test_result is not None:
            test_result.contents.value = self._defaults['self_test']['testResult']
        # test_message
        if self._defaults['self_test']['testMessage'] is None:
            raise MockFunctionCallError("niDigital_self_test", param='testMessage')
        test_value = self._defaults['self_test']['testMessage']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(test_message) >= len(test_value)
        for i in range(len(test_value)):
            test_message[i] = test_value[i]
        return self._defaults['self_test']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niDigital_Abort.side_effect = MockFunctionCallError("niDigital_Abort")
        mock_library.niDigital_Abort.return_value = 0
        mock_library.niDigital_AbortKeepAlive.side_effect = MockFunctionCallError("niDigital_AbortKeepAlive")
        mock_library.niDigital_AbortKeepAlive.return_value = 0
        mock_library.niDigital_ApplyLevelsAndTiming.side_effect = MockFunctionCallError("niDigital_ApplyLevelsAndTiming")
        mock_library.niDigital_ApplyLevelsAndTiming.return_value = 0
        mock_library.niDigital_ApplyTDROffsets.side_effect = MockFunctionCallError("niDigital_ApplyTDROffsets")
        mock_library.niDigital_ApplyTDROffsets.return_value = 0
        mock_library.niDigital_BurstPattern.side_effect = MockFunctionCallError("niDigital_BurstPattern")
        mock_library.niDigital_BurstPattern.return_value = 0
        mock_library.niDigital_ClockGenerator_Abort.side_effect = MockFunctionCallError("niDigital_ClockGenerator_Abort")
        mock_library.niDigital_ClockGenerator_Abort.return_value = 0
        mock_library.niDigital_ClockGenerator_GenerateClock.side_effect = MockFunctionCallError("niDigital_ClockGenerator_GenerateClock")
        mock_library.niDigital_ClockGenerator_GenerateClock.return_value = 0
        mock_library.niDigital_Commit.side_effect = MockFunctionCallError("niDigital_Commit")
        mock_library.niDigital_Commit.return_value = 0
        mock_library.niDigital_ConfigureActiveLoadLevels.side_effect = MockFunctionCallError("niDigital_ConfigureActiveLoadLevels")
        mock_library.niDigital_ConfigureActiveLoadLevels.return_value = 0
        mock_library.niDigital_ConfigurePatternBurstSites.side_effect = MockFunctionCallError("niDigital_ConfigurePatternBurstSites")
        mock_library.niDigital_ConfigurePatternBurstSites.return_value = 0
        mock_library.niDigital_ConfigureTimeSetCompareEdgesStrobe.side_effect = MockFunctionCallError("niDigital_ConfigureTimeSetCompareEdgesStrobe")
        mock_library.niDigital_ConfigureTimeSetCompareEdgesStrobe.return_value = 0
        mock_library.niDigital_ConfigureTimeSetCompareEdgesStrobe2x.side_effect = MockFunctionCallError("niDigital_ConfigureTimeSetCompareEdgesStrobe2x")
        mock_library.niDigital_ConfigureTimeSetCompareEdgesStrobe2x.return_value = 0
        mock_library.niDigital_ConfigureTimeSetDriveEdges.side_effect = MockFunctionCallError("niDigital_ConfigureTimeSetDriveEdges")
        mock_library.niDigital_ConfigureTimeSetDriveEdges.return_value = 0
        mock_library.niDigital_ConfigureTimeSetDriveEdges2x.side_effect = MockFunctionCallError("niDigital_ConfigureTimeSetDriveEdges2x")
        mock_library.niDigital_ConfigureTimeSetDriveEdges2x.return_value = 0
        mock_library.niDigital_ConfigureTimeSetDriveFormat.side_effect = MockFunctionCallError("niDigital_ConfigureTimeSetDriveFormat")
        mock_library.niDigital_ConfigureTimeSetDriveFormat.return_value = 0
        mock_library.niDigital_ConfigureTimeSetEdge.side_effect = MockFunctionCallError("niDigital_ConfigureTimeSetEdge")
        mock_library.niDigital_ConfigureTimeSetEdge.return_value = 0
        mock_library.niDigital_ConfigureTimeSetEdgeMultiplier.side_effect = MockFunctionCallError("niDigital_ConfigureTimeSetEdgeMultiplier")
        mock_library.niDigital_ConfigureTimeSetEdgeMultiplier.return_value = 0
        mock_library.niDigital_ConfigureTimeSetPeriod.side_effect = MockFunctionCallError("niDigital_ConfigureTimeSetPeriod")
        mock_library.niDigital_ConfigureTimeSetPeriod.return_value = 0
        mock_library.niDigital_ConfigureVoltageLevels.side_effect = MockFunctionCallError("niDigital_ConfigureVoltageLevels")
        mock_library.niDigital_ConfigureVoltageLevels.return_value = 0
        mock_library.niDigital_CreateCaptureWaveformFromFileDigicapture.side_effect = MockFunctionCallError("niDigital_CreateCaptureWaveformFromFileDigicapture")
        mock_library.niDigital_CreateCaptureWaveformFromFileDigicapture.return_value = 0
        mock_library.niDigital_CreateCaptureWaveformParallel.side_effect = MockFunctionCallError("niDigital_CreateCaptureWaveformParallel")
        mock_library.niDigital_CreateCaptureWaveformParallel.return_value = 0
        mock_library.niDigital_CreateCaptureWaveformSerial.side_effect = MockFunctionCallError("niDigital_CreateCaptureWaveformSerial")
        mock_library.niDigital_CreateCaptureWaveformSerial.return_value = 0
        mock_library.niDigital_CreateSourceWaveformFromFileTDMS.side_effect = MockFunctionCallError("niDigital_CreateSourceWaveformFromFileTDMS")
        mock_library.niDigital_CreateSourceWaveformFromFileTDMS.return_value = 0
        mock_library.niDigital_CreateSourceWaveformParallel.side_effect = MockFunctionCallError("niDigital_CreateSourceWaveformParallel")
        mock_library.niDigital_CreateSourceWaveformParallel.return_value = 0
        mock_library.niDigital_CreateSourceWaveformSerial.side_effect = MockFunctionCallError("niDigital_CreateSourceWaveformSerial")
        mock_library.niDigital_CreateSourceWaveformSerial.return_value = 0
        mock_library.niDigital_CreateTimeSet.side_effect = MockFunctionCallError("niDigital_CreateTimeSet")
        mock_library.niDigital_CreateTimeSet.return_value = 0
        mock_library.niDigital_DeleteAllTimeSets.side_effect = MockFunctionCallError("niDigital_DeleteAllTimeSets")
        mock_library.niDigital_DeleteAllTimeSets.return_value = 0
        mock_library.niDigital_DisableSites.side_effect = MockFunctionCallError("niDigital_DisableSites")
        mock_library.niDigital_DisableSites.return_value = 0
        mock_library.niDigital_EnableMatchFailCombination.side_effect = MockFunctionCallError("niDigital_EnableMatchFailCombination")
        mock_library.niDigital_EnableMatchFailCombination.return_value = 0
        mock_library.niDigital_EnableSites.side_effect = MockFunctionCallError("niDigital_EnableSites")
        mock_library.niDigital_EnableSites.return_value = 0
        mock_library.niDigital_FetchCaptureWaveformU32.side_effect = MockFunctionCallError("niDigital_FetchCaptureWaveformU32")
        mock_library.niDigital_FetchCaptureWaveformU32.return_value = 0
        mock_library.niDigital_FetchHistoryRAMCycleInformation.side_effect = MockFunctionCallError("niDigital_FetchHistoryRAMCycleInformation")
        mock_library.niDigital_FetchHistoryRAMCycleInformation.return_value = 0
        mock_library.niDigital_FetchHistoryRAMCyclePinData.side_effect = MockFunctionCallError("niDigital_FetchHistoryRAMCyclePinData")
        mock_library.niDigital_FetchHistoryRAMCyclePinData.return_value = 0
        mock_library.niDigital_FetchHistoryRAMScanCycleNumber.side_effect = MockFunctionCallError("niDigital_FetchHistoryRAMScanCycleNumber")
        mock_library.niDigital_FetchHistoryRAMScanCycleNumber.return_value = 0
        mock_library.niDigital_FrequencyCounter_MeasureFrequency.side_effect = MockFunctionCallError("niDigital_FrequencyCounter_MeasureFrequency")
        mock_library.niDigital_FrequencyCounter_MeasureFrequency.return_value = 0
        mock_library.niDigital_GetAttributeViBoolean.side_effect = MockFunctionCallError("niDigital_GetAttributeViBoolean")
        mock_library.niDigital_GetAttributeViBoolean.return_value = 0
        mock_library.niDigital_GetAttributeViInt32.side_effect = MockFunctionCallError("niDigital_GetAttributeViInt32")
        mock_library.niDigital_GetAttributeViInt32.return_value = 0
        mock_library.niDigital_GetAttributeViInt64.side_effect = MockFunctionCallError("niDigital_GetAttributeViInt64")
        mock_library.niDigital_GetAttributeViInt64.return_value = 0
        mock_library.niDigital_GetAttributeViReal64.side_effect = MockFunctionCallError("niDigital_GetAttributeViReal64")
        mock_library.niDigital_GetAttributeViReal64.return_value = 0
        mock_library.niDigital_GetAttributeViString.side_effect = MockFunctionCallError("niDigital_GetAttributeViString")
        mock_library.niDigital_GetAttributeViString.return_value = 0
        mock_library.niDigital_GetChannelNameFromString.side_effect = MockFunctionCallError("niDigital_GetChannelNameFromString")
        mock_library.niDigital_GetChannelNameFromString.return_value = 0
        mock_library.niDigital_GetError.side_effect = MockFunctionCallError("niDigital_GetError")
        mock_library.niDigital_GetError.return_value = 0
        mock_library.niDigital_GetFailCount.side_effect = MockFunctionCallError("niDigital_GetFailCount")
        mock_library.niDigital_GetFailCount.return_value = 0
        mock_library.niDigital_GetHistoryRAMSampleCount.side_effect = MockFunctionCallError("niDigital_GetHistoryRAMSampleCount")
        mock_library.niDigital_GetHistoryRAMSampleCount.return_value = 0
        mock_library.niDigital_GetPatternName.side_effect = MockFunctionCallError("niDigital_GetPatternName")
        mock_library.niDigital_GetPatternName.return_value = 0
        mock_library.niDigital_GetPatternPinList.side_effect = MockFunctionCallError("niDigital_GetPatternPinList")
        mock_library.niDigital_GetPatternPinList.return_value = 0
        mock_library.niDigital_GetPinName.side_effect = MockFunctionCallError("niDigital_GetPinName")
        mock_library.niDigital_GetPinName.return_value = 0
        mock_library.niDigital_GetPinResultsPinInformation.side_effect = MockFunctionCallError("niDigital_GetPinResultsPinInformation")
        mock_library.niDigital_GetPinResultsPinInformation.return_value = 0
        mock_library.niDigital_GetSitePassFail.side_effect = MockFunctionCallError("niDigital_GetSitePassFail")
        mock_library.niDigital_GetSitePassFail.return_value = 0
        mock_library.niDigital_GetSiteResultsSiteNumbers.side_effect = MockFunctionCallError("niDigital_GetSiteResultsSiteNumbers")
        mock_library.niDigital_GetSiteResultsSiteNumbers.return_value = 0
        mock_library.niDigital_GetTimeSetDriveFormat.side_effect = MockFunctionCallError("niDigital_GetTimeSetDriveFormat")
        mock_library.niDigital_GetTimeSetDriveFormat.return_value = 0
        mock_library.niDigital_GetTimeSetEdge.side_effect = MockFunctionCallError("niDigital_GetTimeSetEdge")
        mock_library.niDigital_GetTimeSetEdge.return_value = 0
        mock_library.niDigital_GetTimeSetEdgeMultiplier.side_effect = MockFunctionCallError("niDigital_GetTimeSetEdgeMultiplier")
        mock_library.niDigital_GetTimeSetEdgeMultiplier.return_value = 0
        mock_library.niDigital_GetTimeSetName.side_effect = MockFunctionCallError("niDigital_GetTimeSetName")
        mock_library.niDigital_GetTimeSetName.return_value = 0
        mock_library.niDigital_GetTimeSetPeriod.side_effect = MockFunctionCallError("niDigital_GetTimeSetPeriod")
        mock_library.niDigital_GetTimeSetPeriod.return_value = 0
        mock_library.niDigital_InitWithOptions.side_effect = MockFunctionCallError("niDigital_InitWithOptions")
        mock_library.niDigital_InitWithOptions.return_value = 0
        mock_library.niDigital_Initiate.side_effect = MockFunctionCallError("niDigital_Initiate")
        mock_library.niDigital_Initiate.return_value = 0
        mock_library.niDigital_IsDone.side_effect = MockFunctionCallError("niDigital_IsDone")
        mock_library.niDigital_IsDone.return_value = 0
        mock_library.niDigital_IsSiteEnabled.side_effect = MockFunctionCallError("niDigital_IsSiteEnabled")
        mock_library.niDigital_IsSiteEnabled.return_value = 0
        mock_library.niDigital_LoadLevels.side_effect = MockFunctionCallError("niDigital_LoadLevels")
        mock_library.niDigital_LoadLevels.return_value = 0
        mock_library.niDigital_LoadPattern.side_effect = MockFunctionCallError("niDigital_LoadPattern")
        mock_library.niDigital_LoadPattern.return_value = 0
        mock_library.niDigital_LoadPinMap.side_effect = MockFunctionCallError("niDigital_LoadPinMap")
        mock_library.niDigital_LoadPinMap.return_value = 0
        mock_library.niDigital_LoadSpecifications.side_effect = MockFunctionCallError("niDigital_LoadSpecifications")
        mock_library.niDigital_LoadSpecifications.return_value = 0
        mock_library.niDigital_LoadTiming.side_effect = MockFunctionCallError("niDigital_LoadTiming")
        mock_library.niDigital_LoadTiming.return_value = 0
        mock_library.niDigital_LockSession.side_effect = MockFunctionCallError("niDigital_LockSession")
        mock_library.niDigital_LockSession.return_value = 0
        mock_library.niDigital_PPMU_Measure.side_effect = MockFunctionCallError("niDigital_PPMU_Measure")
        mock_library.niDigital_PPMU_Measure.return_value = 0
        mock_library.niDigital_PPMU_Source.side_effect = MockFunctionCallError("niDigital_PPMU_Source")
        mock_library.niDigital_PPMU_Source.return_value = 0
        mock_library.niDigital_ReadSequencerFlag.side_effect = MockFunctionCallError("niDigital_ReadSequencerFlag")
        mock_library.niDigital_ReadSequencerFlag.return_value = 0
        mock_library.niDigital_ReadSequencerRegister.side_effect = MockFunctionCallError("niDigital_ReadSequencerRegister")
        mock_library.niDigital_ReadSequencerRegister.return_value = 0
        mock_library.niDigital_ReadStatic.side_effect = MockFunctionCallError("niDigital_ReadStatic")
        mock_library.niDigital_ReadStatic.return_value = 0
        mock_library.niDigital_ResetDevice.side_effect = MockFunctionCallError("niDigital_ResetDevice")
        mock_library.niDigital_ResetDevice.return_value = 0
        mock_library.niDigital_SelfCalibrate.side_effect = MockFunctionCallError("niDigital_SelfCalibrate")
        mock_library.niDigital_SelfCalibrate.return_value = 0
        mock_library.niDigital_SendSoftwareEdgeTrigger.side_effect = MockFunctionCallError("niDigital_SendSoftwareEdgeTrigger")
        mock_library.niDigital_SendSoftwareEdgeTrigger.return_value = 0
        mock_library.niDigital_SetAttributeViBoolean.side_effect = MockFunctionCallError("niDigital_SetAttributeViBoolean")
        mock_library.niDigital_SetAttributeViBoolean.return_value = 0
        mock_library.niDigital_SetAttributeViInt32.side_effect = MockFunctionCallError("niDigital_SetAttributeViInt32")
        mock_library.niDigital_SetAttributeViInt32.return_value = 0
        mock_library.niDigital_SetAttributeViInt64.side_effect = MockFunctionCallError("niDigital_SetAttributeViInt64")
        mock_library.niDigital_SetAttributeViInt64.return_value = 0
        mock_library.niDigital_SetAttributeViReal64.side_effect = MockFunctionCallError("niDigital_SetAttributeViReal64")
        mock_library.niDigital_SetAttributeViReal64.return_value = 0
        mock_library.niDigital_SetAttributeViString.side_effect = MockFunctionCallError("niDigital_SetAttributeViString")
        mock_library.niDigital_SetAttributeViString.return_value = 0
        mock_library.niDigital_SetRuntimeEnvironment.side_effect = MockFunctionCallError("niDigital_SetRuntimeEnvironment")
        mock_library.niDigital_SetRuntimeEnvironment.return_value = 0
        mock_library.niDigital_TDR.side_effect = MockFunctionCallError("niDigital_TDR")
        mock_library.niDigital_TDR.return_value = 0
        mock_library.niDigital_UnloadAllPatterns.side_effect = MockFunctionCallError("niDigital_UnloadAllPatterns")
        mock_library.niDigital_UnloadAllPatterns.return_value = 0
        mock_library.niDigital_UnloadSpecifications.side_effect = MockFunctionCallError("niDigital_UnloadSpecifications")
        mock_library.niDigital_UnloadSpecifications.return_value = 0
        mock_library.niDigital_UnlockSession.side_effect = MockFunctionCallError("niDigital_UnlockSession")
        mock_library.niDigital_UnlockSession.return_value = 0
        mock_library.niDigital_WaitUntilDone.side_effect = MockFunctionCallError("niDigital_WaitUntilDone")
        mock_library.niDigital_WaitUntilDone.return_value = 0
        mock_library.niDigital_WriteSequencerFlag.side_effect = MockFunctionCallError("niDigital_WriteSequencerFlag")
        mock_library.niDigital_WriteSequencerFlag.return_value = 0
        mock_library.niDigital_WriteSequencerRegister.side_effect = MockFunctionCallError("niDigital_WriteSequencerRegister")
        mock_library.niDigital_WriteSequencerRegister.return_value = 0
        mock_library.niDigital_WriteSourceWaveformBroadcastU32.side_effect = MockFunctionCallError("niDigital_WriteSourceWaveformBroadcastU32")
        mock_library.niDigital_WriteSourceWaveformBroadcastU32.return_value = 0
        mock_library.niDigital_WriteSourceWaveformDataFromFileTDMS.side_effect = MockFunctionCallError("niDigital_WriteSourceWaveformDataFromFileTDMS")
        mock_library.niDigital_WriteSourceWaveformDataFromFileTDMS.return_value = 0
        mock_library.niDigital_WriteSourceWaveformSiteUniqueU32.side_effect = MockFunctionCallError("niDigital_WriteSourceWaveformSiteUniqueU32")
        mock_library.niDigital_WriteSourceWaveformSiteUniqueU32.return_value = 0
        mock_library.niDigital_WriteStatic.side_effect = MockFunctionCallError("niDigital_WriteStatic")
        mock_library.niDigital_WriteStatic.return_value = 0
        mock_library.niDigital_close.side_effect = MockFunctionCallError("niDigital_close")
        mock_library.niDigital_close.return_value = 0
        mock_library.niDigital_error_message.side_effect = MockFunctionCallError("niDigital_error_message")
        mock_library.niDigital_error_message.return_value = 0
        mock_library.niDigital_reset.side_effect = MockFunctionCallError("niDigital_reset")
        mock_library.niDigital_reset.return_value = 0
        mock_library.niDigital_self_test.side_effect = MockFunctionCallError("niDigital_self_test")
        mock_library.niDigital_self_test.return_value = 0
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidigital/nidigital/unit_tests/test_nidigital.py sha256=ab5bdad4c60f120ee1a6d5d9723e9e83a8908ed8693f01536b39ca238d32e7a3 bytes=27168 -->
## FILE: generated/nidigital/nidigital/unit_tests/test_nidigital.py

- repository: `ni/nimi-python`
- source_path: `generated/nidigital/nidigital/unit_tests/test_nidigital.py`
- sha256: `ab5bdad4c60f120ee1a6d5d9723e9e83a8908ed8693f01536b39ca238d32e7a3`
- bytes: 27168

````python
import _mock_helper

import nidigital
import nitclk

import pytest
from unittest.mock import MagicMock
from unittest.mock import patch

session_id_for_test = 42


class TestSession:
    class PatchedLibrary(nidigital._library.Library):
        def __init__(self, ctypes_library):
            super().__init__(ctypes_library)

            for f in dir(self):
                if f.startswith("niDigital_") and not f.endswith("_cfunc"):
                    setattr(self, f, MagicMock())

    class PatchedTClkLibrary(nitclk._library.Library):
        def __init__(self, ctypes_library):
            super().__init__(ctypes_library)

            for f in dir(self):
                if f.startswith("niTClk_") and not f.endswith("_cfunc"):
                    setattr(self, f, MagicMock())

    def setup_method(self, method):
        self.patched_library = self.PatchedLibrary(None)
        self.patched_library_singleton_get = patch('nidigital._library_interpreter._library_singleton.get', return_value=self.patched_library)
        self.patched_library_singleton_get.start()

        self.patched_tclk_library = self.PatchedTClkLibrary(None)
        self.patched_tclk_library_singleton_get = patch('nitclk._library_interpreter._library_singleton.get', return_value=self.patched_tclk_library)
        self.patched_tclk_library_singleton_get.start()

        self.side_effects_helper = _mock_helper.SideEffectsHelper()
        self.side_effects_helper.set_side_effects_and_return_values(self.patched_library)

        # The side effect must be set for this, because it's called.
        # No need to set argument values; the method is tested in nifake unit tests, not here.
        self.patched_library.niDigital_SetRuntimeEnvironment.side_effect = self.side_effects_helper.niDigital_SetRuntimeEnvironment

        self.patched_library.niDigital_InitWithOptions.side_effect = self.side_effects_helper.niDigital_InitWithOptions
        self.side_effects_helper['InitWithOptions']['newVi'] = session_id_for_test

        self.patched_library.niDigital_close.side_effect = self.side_effects_helper.niDigital_close

        self.patched_library.niDigital_LockSession.side_effect = self.side_effects_helper.niDigital_LockSession
        self.side_effects_helper['LockSession']['callerHasLock'] = True

        self.patched_library.niDigital_UnlockSession.side_effect = self.side_effects_helper.niDigital_UnlockSession
        self.side_effects_helper['UnlockSession']['callerHasLock'] = True

        # For trying to set `_all_channels_in_session` in the Session constructor
        self.patched_library.niDigital_GetAttributeViInt32.side_effect = self.side_effects_helper.niDigital_GetAttributeViInt32
        self.side_effects_helper['GetAttributeViInt32']['value'] = 1  # channel_count
        self.patched_library.niDigital_GetChannelNameFromString.side_effect = self.side_effects_helper.niDigital_GetChannelNameFromString
        self.side_effects_helper['GetChannelNameFromString']['name'] = '0'  # get_channel_names()

        # for niDigital_FetchHistoryRAMCycleInformation_looping
        self.pattern_indices_looping = [0, 0, 0, 0, 0, 0, 0]
        self.time_set_indices_looping = [0, 1, 1, 2, 2, 2, 0]
        self.vector_numbers_looping = [5, 6, 6, 7, 7, 8, 9]
        self.cycle_numbers_looping = [5, 6, 7, 8, 9, 10, 11]
        self.num_duty_cycles_looping = [1, 1, 1, 2, 2, 2, 1]

        # for niDigital_GetTimeSetName_looping
        self.time_set_name_looping = ['t0', 'tScan', 't2X']

        # for niDigital_FetchHistoryRAMScanCycleNumber_looping
        self.scan_cycle_number_looping = [-1, 0, 1, -1, -1, -1, -1]

        # for niDigital_FetchHistoryRAMCyclePinData_looping
        self.expected_pin_states_looping = [
            [[nidigital.PinState.ZERO, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.ZERO, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.ZERO, nidigital.PinState.ONE, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.H]],
            [[nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.ONE, nidigital.PinState.ZERO, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.L]],
            [[nidigital.PinState.ONE, nidigital.PinState.ONE, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X],
             [nidigital.PinState.ZERO, nidigital.PinState.ZERO, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.ONE, nidigital.PinState.ONE, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X],
             [nidigital.PinState.ZERO, nidigital.PinState.ZERO, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.ZERO, nidigital.PinState.ONE, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X],
             [nidigital.PinState.ONE, nidigital.PinState.ZERO, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X]]
        ]
        self.actual_pin_states_looping = [
            [[nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.H]],
            [[nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.L]],
            [[nidigital.PinState.H, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X],
             [nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.H, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X],
             [nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.L, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.L, nidigital.PinState.H, nidigital.PinState.X, nidigital.PinState.X],
             [nidigital.PinState.H, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.H, nidigital.PinState.L, nidigital.PinState.X, nidigital.PinState.X]],
            [[nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X, nidigital.PinState.X]]
        ]
        self.per_pin_pass_fail_looping = [
            [[True, False, True, True, False, True, True, True]],
            [[True, True, True, True, True, True, True, True]],
            [[True, True, True, True, True, True, True, True]],
            [[True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True]],
            [[True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True]],
            [[True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True]],
            [[True, True, True, True, True, True, True, True]],
        ]

        # for niDigital_FetchHistoryRAMCyclePinData_check_pins_looping
        self.expected_pin_list_check_pins_looping = None
        self.expected_pin_states_check_pins_looping = [[[nidigital.PinState.ZERO, nidigital.PinState.H]]]
        self.actual_pin_states_check_pins_looping = [[[nidigital.PinState.L, nidigital.PinState.L]]]
        self.per_pin_pass_fail_check_pins_looping = [[[True, False]]]

        # for niDigital_GetHistoryRAMSampleCount_check_site_looping
        self.iteration_check_site_looping = 0
        self.site_numbers_looping = [0, 1, 2]

    def teardown_method(self, method):
        self.patched_tclk_library_singleton_get.stop()
        self.patched_library_singleton_get.stop()

    # API Tests

    # TODO(sbethur): When nidigital driver provides better simulation support (internal bug# 992370),
    #  this test should be converted to a system test. (GitHub issue# 1353).
    def test_fetch_history_ram_cycle_information_position_out_of_bound(self):

        self.patched_library.niDigital_GetHistoryRAMSampleCount.side_effect = self.side_effects_helper.niDigital_GetHistoryRAMSampleCount
        self.side_effects_helper['GetHistoryRAMSampleCount']['sampleCount'] = 7
        with nidigital.Session('') as session:
            with pytest.raises(ValueError, match='position: Specified value = 8, Maximum value = 6.'):
                session.sites[1].fetch_history_ram_cycle_information(position=8, samples_to_read=-1)

    # TODO(sbethur): When nidigital driver provides better simulation support (internal bug# 992370),
    #  this test should be converted to a system test. (GitHub issue# 1353).
    def test_fetch_history_ram_cycle_information_position_last(self):

        self.patched_library.niDigital_GetHistoryRAMSampleCount.side_effect = self.side_effects_helper.niDigital_GetHistoryRAMSampleCount
        self.side_effects_helper['GetHistoryRAMSampleCount']['sampleCount'] = 7
        self.patched_library.niDigital_GetAttributeViBoolean.side_effect = self.side_effects_helper.niDigital_GetAttributeViBoolean
        self.side_effects_helper['GetAttributeViBoolean']['value'] = True  # history_ram_number_of_samples_is_finite
        self.patched_library.niDigital_FetchHistoryRAMCycleInformation.side_effect = self.side_effects_helper.niDigital_FetchHistoryRAMCycleInformation
        self.side_effects_helper['FetchHistoryRAMCycleInformation']['patternIndex'] = 0
        self.side_effects_helper['FetchHistoryRAMCycleInformation']['timeSetIndex'] = 0
        self.side_effects_helper['FetchHistoryRAMCycleInformation']['vectorNumber'] = 9
        self.side_effects_helper['FetchHistoryRAMCycleInformation']['cycleNumber'] = 11
        self.side_effects_helper['FetchHistoryRAMCycleInformation']['numDutCycles'] = 1
        self.patched_library.niDigital_GetPatternName.side_effect = self.side_effects_helper.niDigital_GetPatternName
        self.side_effects_helper['GetPatternName']['name'] = 'new_pattern'
        self.patched_library.niDigital_GetTimeSetName.side_effect = self.side_effects_helper.niDigital_GetTimeSetName
        self.side_effects_helper['GetTimeSetName']['name'] = 't0'
        self.patched_library.niDigital_FetchHistoryRAMScanCycleNumber.side_effect = self.side_effects_helper.niDigital_FetchHistoryRAMScanCycleNumber
        self.side_effects_helper['FetchHistoryRAMScanCycleNumber']['scanCycleNumber'] = -1
        self.patched_library.niDigital_FetchHistoryRAMCyclePinData.side_effect = self.side_effects_helper.niDigital_FetchHistoryRAMCyclePinData
        self.side_effects_helper['FetchHistoryRAMCyclePinData']['actualNumPinData'] = 8
        self.side_effects_helper['FetchHistoryRAMCyclePinData']['expectedPinStates'] = [nidigital.PinState.X.value] * 8
        self.side_effects_helper['FetchHistoryRAMCyclePinData']['actualPinStates'] = [nidigital.PinState.NOT_A_PIN_STATE.value] * 8
        self.side_effects_helper['FetchHistoryRAMCyclePinData']['perPinPassFail'] = [True] * 8
        with nidigital.Session('') as session:
            history_ram_cycle_info = session.sites[1].fetch_history_ram_cycle_information(
                position=6,
                samples_to_read=-1)
            self.patched_library.niDigital_FetchHistoryRAMCycleInformation.assert_called_once()
            assert self.patched_library.niDigital_GetPatternName.call_count == 2
            assert self.patched_library.niDigital_GetTimeSetName.call_count == 2
            self.patched_library.niDigital_FetchHistoryRAMScanCycleNumber.assert_called_once()
            assert self.patched_library.niDigital_FetchHistoryRAMCyclePinData.call_count == 2

        assert len(history_ram_cycle_info) == 1
        assert history_ram_cycle_info[0].vector_number == 9
        assert history_ram_cycle_info[0].cycle_number == 11

    # TODO(sbethur): When nidigital driver provides better simulation support (internal bug# 992370),
    #  this test should be converted to a system test. (GitHub issue# 1353).
    def test_fetch_history_ram_cycle_information_samples_to_read_too_much(self):

        self.patched_library.niDigital_GetHistoryRAMSampleCount.side_effect = self.side_effects_helper.niDigital_GetHistoryRAMSampleCount
        self.side_effects_helper['GetHistoryRAMSampleCount']['sampleCount'] = 7
        self.patched_library.niDigital_GetAttributeViBoolean.side_effect = self.side_effects_helper.niDigital_GetAttributeViBoolean
        self.side_effects_helper['GetAttributeViBoolean']['value'] = True  # history_ram_number_of_samples_is_finite

        with nidigital.Session('') as session:
            assert session.sites[1].get_history_ram_sample_count() == 7

            expected_error_description = (
                'position: Specified value = 3, samples_to_read: Specified value = 5; Samples available = 4.')
            with pytest.raises(ValueError, match=expected_error_description):
                session.sites[1].fetch_history_ram_cycle_information(position=3, samples_to_read=5)

    # Helper function for mocking multiple calls
    def niDigital_FetchHistoryRAMCycleInformation_looping(self, vi, site, sample_index, pattern_index, time_set_index, vector_number, cycle_number, num_dut_cycles):  # noqa: N802
        sample_index_int = int(sample_index.value)
        pattern_index.contents.value = self.pattern_indices_looping[sample_index_int]
        time_set_index.contents.value = self.time_set_indices_looping[sample_index_int]
        vector_number.contents.value = self.vector_numbers_looping[sample_index_int]
        cycle_number.contents.value = self.cycle_numbers_looping[sample_index_int]
        num_dut_cycles.contents.value = self.num_duty_cycles_looping[sample_index_int]
        return 0

    # Helper function for mocking multiple calls
    def niDigital_GetTimeSetName_looping(self, vi, time_set_index, name_buffer_size, name):  # noqa: N802
        time_set_index_int = int(time_set_index.value)
        if int(name_buffer_size.value) == 0:
            return (len(self.time_set_name_looping[time_set_index_int]))
        bytes_to_copy = self.time_set_name_looping[time_set_index_int].encode('ascii')
        for i in range(0, len(bytes_to_copy)):
            name[i] = bytes_to_copy[i]
        return 0

    # Helper function for mocking multiple calls
    def niDigital_FetchHistoryRAMScanCycleNumber_looping(self, vi, site, sample_index, scan_cycle_number):  # noqa: N802
        sample_index_int = int(sample_index.value)
        scan_cycle_number.contents.value = self.scan_cycle_number_looping[sample_index_int]
        return 0

    # Helper function for mocking multiple calls
    def niDigital_FetchHistoryRAMCyclePinData_looping(self, vi, site, pin_list, sample_index, dut_cycle_index, pin_data_buffer_size, expected_pin_states, actual_pin_states, per_pin_pass_fail, actual_num_pin_data):  # noqa: N802
        sample_index_int = int(sample_index.value)
        dut_cycle_index_int = int(dut_cycle_index.value)
        if int(pin_data_buffer_size.value) == 0:
            actual_num_pin_data.contents.value = len(self.expected_pin_states_looping[sample_index_int][dut_cycle_index_int])
            return actual_num_pin_data.contents.value
        for i in range(0, int(pin_data_buffer_size.value)):
            expected_pin_states[i] = self.expected_pin_states_looping[sample_index_int][dut_cycle_index_int][i].value
            actual_pin_states[i] = self.actual_pin_states_looping[sample_index_int][dut_cycle_index_int][i].value
            per_pin_pass_fail[i] = self.per_pin_pass_fail_looping[sample_index_int][dut_cycle_index_int][i]
        return 0

    # TODO(sbethur): When nidigital driver provides better simulation support (internal bug# 992370),
    #  this test should be converted to a system test. (GitHub issue# 1353).
    def test_fetch_history_ram_cycle_information_samples_to_read_all(self):

        self.patched_library.niDigital_GetHistoryRAMSampleCount.side_effect = self.side_effects_helper.niDigital_GetHistoryRAMSampleCount
        self.side_effects_helper['GetHistoryRAMSampleCount']['sampleCount'] = 7
        self.patched_library.niDigital_GetAttributeViBoolean.side_effect = self.side_effects_helper.niDigital_GetAttributeViBoolean
        self.side_effects_helper['GetAttributeViBoolean']['value'] = True  # history_ram_number_of_samples_is_finite
        self.patched_library.niDigital_FetchHistoryRAMCycleInformation.side_effect = self.niDigital_FetchHistoryRAMCycleInformation_looping
        self.patched_library.niDigital_GetPatternName.side_effect = self.side_effects_helper.niDigital_GetPatternName
        self.side_effects_helper['GetPatternName']['name'] = 'new_pattern'
        self.patched_library.niDigital_GetTimeSetName.side_effect = self.niDigital_GetTimeSetName_looping
        self.patched_library.niDigital_FetchHistoryRAMScanCycleNumber.side_effect = self.niDigital_FetchHistoryRAMScanCycleNumber_looping
        self.patched_library.niDigital_FetchHistoryRAMCyclePinData.side_effect = self.niDigital_FetchHistoryRAMCyclePinData_looping
        self.patched_library.niDigital_GetPatternPinList.side_effect = self.side_effects_helper.niDigital_GetPatternPinList
        pin_list = ['LO' + str(i) for i in range(4)] + ['HI' + str(i) for i in range(4)]
        self.side_effects_helper['GetPatternPinList']['pinList'] = ','.join(pin_list)
        with nidigital.Session('') as session:
            history_ram_cycle_info = session.sites[1].fetch_history_ram_cycle_information(
                position=0,
                samples_to_read=-1)
            assert self.patched_library.niDigital_FetchHistoryRAMCycleInformation.call_count == 7
            assert self.patched_library.niDigital_GetPatternName.call_count == 2  # there's only one pattern, so this is a 2
            assert self.patched_library.niDigital_GetTimeSetName.call_count == 6  # 3 time sets, so this is a 6
            assert self.patched_library.niDigital_FetchHistoryRAMScanCycleNumber.call_count == 7
            assert self.patched_library.niDigital_FetchHistoryRAMCyclePinData.call_count == 20  # 10 DUT cycles

            assert len(history_ram_cycle_info) == 7
            assert all([i.pattern_name == 'new_pattern' for i in history_ram_cycle_info])

            time_set_names = [i.time_set_name for i in history_ram_cycle_info]
            assert time_set_names == ['t0', 'tScan', 'tScan', 't2X', 't2X', 't2X', 't0']

            vector_numbers = [i.vector_number for i in history_ram_cycle_info]
            assert vector_numbers == [5, 6, 6, 7, 7, 8, 9]

            cycle_numbers = [i.cycle_number for i in history_ram_cycle_info]
            assert cycle_numbers == list(range(5, 12))

            scan_cycle_numbers = [i.scan_cycle_number for i in history_ram_cycle_info]
            assert scan_cycle_numbers == [-1, 0, 1, -1, -1, -1, -1]

            pin_names = session.get_pattern_pin_names('new_pattern')
            assert self.patched_library.niDigital_GetPatternPinList.call_count == 2
            assert pin_names == pin_list

        expected_pin_states = [i.expected_pin_states for i in history_ram_cycle_info]
        assert expected_pin_states == self.expected_pin_states_looping

        # If test expects actual pin state to be 'X', then value returned by the API can be anything.
        # So, need to skip those pin states while comparing.
        actual_pin_states = [i.actual_pin_states for i in history_ram_cycle_info]
        assert len(actual_pin_states) == len(self.actual_pin_states_looping)
        for vector_pin_states, vector_pin_states_expected_by_test in zip(actual_pin_states, self.actual_pin_states_looping):
            for cycle_pin_states, cycle_pin_states_expected_by_test in zip(vector_pin_states, vector_pin_states_expected_by_test):
                for pin_state, pin_state_expected_by_test in zip(cycle_pin_states, cycle_pin_states_expected_by_test):
                    if pin_state_expected_by_test is not nidigital.PinState.X:
                        assert pin_state == pin_state_expected_by_test

        # Only the first cycle returned is expected to have failures
        per_pin_pass_fail = [i.per_pin_pass_fail for i in history_ram_cycle_info]
        assert per_pin_pass_fail == self.per_pin_pass_fail_looping

    # Helper function for validating pin list behavior in fetch_history_ram_cycle_information.
    def niDigital_FetchHistoryRAMCyclePinData_check_pins_looping(self, vi, site, pin_list, sample_index, dut_cycle_index, pin_data_buffer_size, expected_pin_states, actual_pin_states, per_pin_pass_fail, actual_num_pin_data):  # noqa: N802
        sample_index_int = int(sample_index.value)
        dut_cycle_index_int = int(dut_cycle_index.value)
        if int(pin_data_buffer_size.value) == 0:
            actual_num_pin_data.contents.value = len(self.expected_pin_states_check_pins_looping[sample_index_int][dut_cycle_index_int])
            return actual_num_pin_data.contents.value
        for i in range(0, int(pin_data_buffer_size.value)):
            expected_pin_states[i] = self.expected_pin_states_check_pins_looping[sample_index_int][dut_cycle_index_int][i].value
            actual_pin_states[i] = self.actual_pin_states_check_pins_looping[sample_index_int][dut_cycle_index_int][i].value
            per_pin_pass_fail[i] = self.per_pin_pass_fail_check_pins_looping[sample_index_int][dut_cycle_index_int][i]
        assert self.expected_pin_list_check_pins_looping is not None
        assert pin_list.value.decode('ascii') == self.expected_pin_list_check_pins_looping
        return 0

    def test_fetch_history_ram_cycle_information_pin_list(self):

        self.patched_library.niDigital_GetHistoryRAMSampleCount.side_effect = self.side_effects_helper.niDigital_GetHistoryRAMSampleCount
        self.side_effects_helper['GetHistoryRAMSampleCount']['sampleCount'] = 1
        self.patched_library.niDigital_GetAttributeViBoolean.side_effect = self.side_effects_helper.niDigital_GetAttributeViBoolean
        self.side_effects_helper['GetAttributeViBoolean']['value'] = True  # history_ram_number_of_samples_is_finite
        self.patched_library.niDigital_FetchHistoryRAMCycleInformation.side_effect = self.side_effects_helper.niDigital_FetchHistoryRAMCycleInformation
        self.side_effects_helper['FetchHistoryRAMCycleInformation']['patternIndex'] = 0
        self.side_effects_helper['FetchHistoryRAMCycleInformation']['timeSetIndex'] = 0
        self.side_effects_helper['FetchHistoryRAMCycleInformation']['vectorNumber'] = 0
        self.side_effects_helper['FetchHistoryRAMCycleInformation']['cycleNumber'] = 0
        self.side_effects_helper['FetchHistoryRAMCycleInformation']['numDutCycles'] = 1
        self.patched_library.niDigital_GetPatternName.side_effect = self.side_effects_helper.niDigital_GetPatternName
        self.side_effects_helper['GetPatternName']['name'] = 'new_pattern'
        self.patched_library.niDigital_GetTimeSetName.side_effect = self.side_effects_helper.niDigital_GetTimeSetName
        self.side_effects_helper['GetTimeSetName']['name'] = 't0'
        self.patched_library.niDigital_FetchHistoryRAMScanCycleNumber.side_effect = self.side_effects_helper.niDigital_FetchHistoryRAMScanCycleNumber
        self.side_effects_helper['FetchHistoryRAMScanCycleNumber']['scanCycleNumber'] = -1
        self.patched_library.niDigital_FetchHistoryRAMCyclePinData.side_effect = self.niDigital_FetchHistoryRAMCyclePinData_check_pins_looping
        with nidigital.Session('') as session:
            self.expected_pin_list_check_pins_looping = 'PinA,PinB'
            session.sites[0].pins['PinA', 'PinB'].fetch_history_ram_cycle_information(position=0, samples_to_read=-1)
            self.expected_pin_list_check_pins_looping = ''
            session.sites[0].fetch_history_ram_cycle_information(position=0, samples_to_read=-1)
            assert self.patched_library.niDigital_FetchHistoryRAMCyclePinData.call_count == 4

    # Helper function for validating site behavior in fetch_history_ram_cycle_information.
    def niDigital_GetHistoryRAMSampleCount_check_site_looping(self, vi, site, sample_count):  # noqa: N802
        assert site.value.decode('ascii') == f'site{self.site_numbers_looping[self.iteration_check_site_looping]}'
        sample_count.contents.value = 0  # we don't care if this is right as long as the fetch does not error
        self.iteration_check_site_looping += 1
        return 0

    def test_fetch_history_ram_cycle_information_site_n(self):

        self.patched_library.niDigital_GetHistoryRAMSampleCount.side_effect = self.niDigital_GetHistoryRAMSampleCount_check_site_looping
        self.side_effects_helper['GetHistoryRAMSampleCount']['sampleCount'] = 1

        with nidigital.Session('') as session:
            for s in self.site_numbers_looping:
                session.sites[s].fetch_history_ram_cycle_information(position=0, samples_to_read=0)
            assert self.patched_library.niDigital_GetHistoryRAMSampleCount.call_count == len(self.site_numbers_looping)

    def test_pin_state_enum_print(self):

        assert str(nidigital.PinState.ZERO) == '0'
        assert str(nidigital.PinState.ONE) == '1'
        assert str(nidigital.PinState.NOT_A_PIN_STATE) == 'Not a Pin State'
        assert str(nidigital.PinState.PIN_STATE_NOT_ACQUIRED) == 'Pin State Not Acquired'
        assert str(nidigital.PinState.L) == 'L'
        assert str(nidigital.PinState.H) == 'H'
        assert str(nidigital.PinState.X) == 'X'
        assert str(nidigital.PinState.M) == 'M'
        assert str(nidigital.PinState.V) == 'V'
        assert str(nidigital.PinState.D) == 'D'
        assert str(nidigital.PinState.E) == 'E'

    def test_write_static_pin_state_enum_print(self):

        assert str(nidigital.WriteStaticPinState.ZERO) == '0'
        assert str(nidigital.WriteStaticPinState.ONE) == '1'
        assert str(nidigital.WriteStaticPinState.X) == 'X'
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidigital/nidigital/VERSION sha256=5f2df6d86b73b1668c81b8c2b11cfa05ed74b6c42453c2bd4badfc93a2d47b0d bytes=13 -->
## FILE: generated/nidigital/nidigital/VERSION

- repository: `ni/nimi-python`
- source_path: `generated/nidigital/nidigital/VERSION`
- sha256: `5f2df6d86b73b1668c81b8c2b11cfa05ed74b6c42453c2bd4badfc93a2d47b0d`
- bytes: 13

````text
1.4.10.dev0
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidigital/README.rst sha256=aa4c70dc06d81fc7aee6690cccc4f8c7314c7dbdc55a35874891c8d85822900a bytes=8678 -->
## FILE: generated/nidigital/README.rst

- repository: `ni/nimi-python`
- source_path: `generated/nidigital/README.rst`
- sha256: `aa4c70dc06d81fc7aee6690cccc4f8c7314c7dbdc55a35874891c8d85822900a`
- bytes: 8678

````rst
Overall Status
--------------

+----------------------+------------------------------------------------------------------------------------------------------------------------------------+
| master branch status | |BuildStatus| |MITLicense| |CoverageStatus|                                                                                        |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------+
| GitHub status        | |OpenIssues| |OpenPullRequests|                                                                                                    |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------+

===========  ============================================================================================================================
Info         NI Modular Instrument driver APIs for Python.
Author       NI
===========  ============================================================================================================================

.. |BuildStatus| image:: https://api.travis-ci.com/ni/nimi-python.svg
    :alt: Build Status - master branch
    :target: https://travis-ci.org/ni/nimi-python

.. |MITLicense| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :alt: MIT License
    :target: https://opensource.org/licenses/MIT

.. |CoverageStatus| image:: https://codecov.io/github/ni/nimi-python/graph/badge.svg
    :alt: Test Coverage - master branch
    :target: https://codecov.io/github/ni/nimi-python

.. |OpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python.svg
    :alt: Open Issues + Pull Requests
    :target: https://github.com/ni/nimi-python/issues

.. |OpenPullRequests| image:: https://img.shields.io/github/issues-pr/ni/nimi-python.svg
    :alt: Open Pull Requests
    :target: https://github.com/ni/nimi-python/pulls


.. _about-section:

About
=====

The **nidigital** module provides a Python API for NI-Digital Pattern Driver. The code is maintained in the Open Source repository for `nimi-python <https://github.com/ni/nimi-python>`_.

Support Policy
--------------
**nidigital** supports all the Operating Systems supported by NI-Digital Pattern Driver.

It follows `Python Software Foundation <https://devguide.python.org/#status-of-python-branches>`_ support policy for different versions of CPython.

NI created and supports **nidigital**.


NI-Digital Pattern Driver Python API Status
-------------------------------------------

+---------------------------------------+--------------------------+
| NI-Digital Pattern Driver (nidigital) |                          |
+=======================================+==========================+
| Driver Version Tested Against         | 2025 Q4                  |
+---------------------------------------+--------------------------+
| PyPI Version                          | |nidigitalLatestVersion| |
+---------------------------------------+--------------------------+
| Supported Python Version              | |nidigitalPythonVersion| |
+---------------------------------------+--------------------------+
| Documentation                         | |nidigitalDocs|          |
+---------------------------------------+--------------------------+
| Open Issues                           | |nidigitalOpenIssues|    |
+---------------------------------------+--------------------------+
| Open Pull Requests                    | |nidigitalOpenPRs|       |
+---------------------------------------+--------------------------+


.. |nidigitalLatestVersion| image:: http://img.shields.io/pypi/v/nidigital.svg
    :alt: Latest NI-Digital Pattern Driver Version
    :target: http://pypi.python.org/pypi/nidigital


.. |nidigitalPythonVersion| image:: http://img.shields.io/pypi/pyversions/nidigital.svg
    :alt: NI-Digital Pattern Driver supported Python versions
    :target: http://pypi.python.org/pypi/nidigital


.. |nidigitalDocs| image:: https://readthedocs.org/projects/nidigital/badge/?version=latest
    :alt: NI-Digital Pattern Driver Python API Documentation Status
    :target: https://nidigital.readthedocs.io/en/latest


.. |nidigitalOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/nidigital.svg
    :alt: Open Issues + Pull Requests for NI-Digital Pattern Driver
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Anidigital


.. |nidigitalOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/nidigital.svg
    :alt: Pull Requests for NI-Digital Pattern Driver
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Anidigital



.. _nidigital_installation-section:

Installation
------------

As a prerequisite to using the **nidigital** module, you must install the NI-Digital Pattern Driver runtime on your system. Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the driver runtime for your devices.

The nimi-python modules (i.e. for **NI-Digital Pattern Driver**) can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install nidigital


Contributing
============

We welcome contributions! You can clone the project repository, build it, and install it by `following these instructions <https://github.com/ni/nimi-python/blob/master/CONTRIBUTING.md>`_.

Usage
------

The following is a basic example of using the **nidigital** module to open a session to a digital pattern instrument,
source current, and measure both voltage and current using the PPMU on selected channels.

.. code-block:: python

    import nidigital
    import time

    with nidigital.Session(resource_name='PXI1Slot2') as session:

        channels = 'PXI1Slot2/0,PXI1Slot2/1'

        # Configure PPMU measurements
        session.channels[channels].ppmu_aperture_time = 0.000004
        session.channels[channels].ppmu_aperture_time_units = nidigital.PPMUApertureTimeUnits.SECONDS

        session.channels[channels].ppmu_output_function = nidigital.PPMUOutputFunction.CURRENT

        session.channels[channels].ppmu_current_level_range = 0.000002
        session.channels[channels].ppmu_current_level = 0.000002
        session.channels[channels].ppmu_voltage_limit_high = 3.3
        session.channels[channels].ppmu_voltage_limit_low = 0

        # Sourcing
        session.channels[channels].ppmu_source()

        # Settling time between sourcing and measuring
        time.sleep(0.01)

        # Measuring
        current_measurements = session.channels[channels].ppmu_measure(nidigital.PPMUMeasurementType.CURRENT)
        voltage_measurements = session.channels[channels].ppmu_measure(nidigital.PPMUMeasurementType.VOLTAGE)

        print('{:<20} {:<10} {:<10}'.format('Channel Name', 'Current', 'Voltage'))
        for channel, current, voltage in zip(channels.split(','), current_measurements, voltage_measurements):
            print('{:<20} {:<10f} {:<10f}'.format(channel, current, voltage))

        # Disconnect all channels using programmable onboard switching
        session.channels[channels].selected_function = nidigital.SelectedFunction.DISCONNECT

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nidigital/examples>`_

.. _support-section:

Support / Feedback
==================

For support specific to the Python API, follow the processs in `Bugs / Feature Requests`_.
For support with hardware, the driver runtime or any other questions not specific to the Python API, please visit `NI Community Forums <https://forums.ni.com/>`_.

.. _bugs-section:

Bugs / Feature Requests
=======================

To report a bug or submit a feature request specific to Python API, please use the
`GitHub issues page <https://github.com/ni/nimi-python/issues>`_.

Fill in the issue template as completely as possible and we will respond as soon
as we can.


.. _documentation-section:

Documentation
=============

Documentation is available `here <http://nidigital.readthedocs.io>`_.


.. _license-section:

License
=======

**nimi-python** is licensed under an MIT-style license (`see
LICENSE <https://github.com/ni/nimi-python/blob/master/LICENSE>`_).
Other incorporated projects may be licensed under different licenses. All
licenses allow for non-commercial and commercial use.


**gRPC Features**

For driver APIs that support it, passing a GrpcSessionOptions instance as a parameter to Session.__init__() is
subject to the NI General Purpose EULA (`see NILICENSE <https://github.com/ni/nimi-python/blob/master/NILICENSE>`_).
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidigital/setup.py sha256=a7a649f70db3a50b73ff45e9228cd1438a63b966b815c636afa217a844025a05 bytes=1851 -->
## FILE: generated/nidigital/setup.py

- repository: `ni/nimi-python`
- source_path: `generated/nidigital/setup.py`
- sha256: `a7a649f70db3a50b73ff45e9228cd1438a63b966b815c636afa217a844025a05`
- bytes: 1851

````python
#!/usr/bin/python
# This file was generated


from setuptools import setup


pypi_name = 'nidigital'


def read_contents(file_to_read):
    with open(file_to_read, 'r') as f:
        return f.read()


setup(
    name=pypi_name,
    zip_safe=True,
    version='1.4.10.dev0',
    description='NI-Digital Pattern Driver Python API',
    long_description=read_contents('README.rst'),
    long_description_content_type='text/x-rst',
    author='NI',
    author_email="opensource@ni.com",
    url="https://github.com/ni/nimi-python",
    maintainer="NI",
    maintainer_email="opensource@ni.com",
    keywords=['nidigital'],
    license='MIT',
    include_package_data=True,
    packages=['nidigital'],
    python_requires='>=3.10',
    install_requires=[
        'hightime>=0.2.0',
        'nitclk',
    ],
    extras_require={
        'grpc': [
            'grpcio>=1.59.0,<2.0',
            'protobuf>=4.21.6',
            'ni.grpcdevice.v1.proto>=1.0.0'
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering :: Instrument Drivers",
        "Topic :: System :: Hardware :: Hardware Drivers"
    ],
    package_data={pypi_name: ['VERSION']},
)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidigital/tox-system_tests.ini sha256=4fb10b9584f4a71b285964d874a839fb8ed6c7f26564f6083f44714be437474f bytes=3237 -->
## FILE: generated/nidigital/tox-system_tests.ini

- repository: `ni/nimi-python`
- source_path: `generated/nidigital/tox-system_tests.ini`
- sha256: `4fb10b9584f4a71b285964d874a839fb8ed6c7f26564f6083f44714be437474f`
- bytes: 3237

````ini
# Tox (http://tox.testrun.org/) is a tool for running tests
# in multiple virtualenvs. This configuration file will run the
# test suite on all supported python versions. To use it, "pip install tox"
# and then run "tox -c tox-system_tests.ini" from the driver directory. (generated/nidigital)
[tox]
envlist = py{310,311,312,313,314}-nidigital-wheel_dep,py{310,311,312,313,314}-nidigital-system_tests, py314-nidigital-coverage
skip_missing_interpreters=True
ignore_basepython_conflict=True
# We put the .tox directory outside of the Jenkins workspace so that it isn't wiped with the rest of the repo
toxworkdir = ../../../.tox

[testenv]
description =
    nidigital-wheel_dep: Build the nitclk wheel because we use it in nidigital tests
    nidigital-system_tests: Run nidigital system tests (requires NI-Digital Pattern Driver runtime to be installed)
    nidigital-coverage: Prepare coverage report for upload to codecov.io  # upload handled by GitHub Actions

changedir =
    nidigital-wheel_dep: ../nitclk
    nidigital-system_tests: .
    nidigital-coverage: .

commands =
    nidigital-wheel_dep: python -m build --wheel

    # --disable-pip-version-check prevents pip from telling us we need to upgrade pip, since we are doing that now
    nidigital-system_tests: python -m pip install --disable-pip-version-check --upgrade pip
    nidigital-system_tests: python ../../tools/install_local_wheel.py --driver nitclk --start-path ../..
    nidigital-system_tests: python -c "import nidigital; nidigital.print_diagnostic_information()"
    nidigital-system_tests: coverage run --rcfile=../../tools/coverage_system_tests.rc --source nidigital --parallel-mode -m pytest ../../src/nidigital/examples --junitxml=../junit/junit-nidigital-{envname}-examples-{env:BITNESS:64}.xml {posargs}
    nidigital-system_tests: coverage run --rcfile=../../tools/coverage_system_tests.rc --source nidigital --parallel-mode -m pytest ../../src/nidigital/system_tests -c tox-system_tests.ini --junitxml=../junit/junit-nidigital-{envname}-{env:BITNESS:64}.xml --durations=5 {posargs}

    nidigital-coverage: coverage combine --rcfile=../../tools/coverage_system_tests.rc ./
    # Create the report to upload
    nidigital-coverage: coverage xml -i --rcfile=../../tools/coverage_system_tests.rc
    # Display the coverage results
    nidigital-coverage: coverage report --rcfile=../../tools/coverage_system_tests.rc

deps =
    nidigital-wheel_dep: build

    nidigital-system_tests: nisync
    nidigital-system_tests: pytest
    nidigital-system_tests: coverage
    nidigital-system_tests: numpy
    nidigital-system_tests: hightime
    nidigital-system_tests: fasteners
    nidigital-system_tests: pytest-json
    nidigital-system_tests: .[grpc]

    nidigital-coverage: coverage

depends =
    nidigital-coverage: py{310,311,312,313,314}-nidigital-system_tests
    nidigital-system_tests: py{310,311,312,313,314}-nidigital-wheel_dep,

passenv =
    GIT_BRANCH
    GIT_COMMIT
    BUILD_URL
    BRANCH_NAME
    JENKINS_URL
    BUILD_NUMBER

[pytest]
addopts = --verbose
filterwarnings =
   error::pytest.PytestUnhandledThreadExceptionWarning
norecursedirs = .* build dist CVS _darcs {arch} *.egg venv
junit_suite_name = nimi-python
junit_family = xunit1
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidmm/nidmm/__init__.py sha256=e623347ac46b23b60929c6078d536ad977511b2a98461555d0100bc3e1412247 bytes=3282 -->
## FILE: generated/nidmm/nidmm/__init__.py

- repository: `ni/nimi-python`
- source_path: `generated/nidmm/nidmm/__init__.py`
- sha256: `e623347ac46b23b60929c6078d536ad977511b2a98461555d0100bc3e1412247`
- bytes: 3282

````python
# -*- coding: utf-8 -*-
# This file was generated


__version__ = '1.4.10.dev0'

from nidmm.enums import *  # noqa: F403,F401,H303
from nidmm.errors import DriverWarning  # noqa: F401
from nidmm.errors import Error  # noqa: F401
from nidmm.grpc_session_options import *  # noqa: F403,F401,H303
from nidmm.session import Session  # noqa: F401


def get_diagnostic_information():
    '''Get diagnostic information about the system state that is suitable for printing or logging

    returns: dict

    note: Python bitness may be incorrect when running in a virtual environment
    '''
    import importlib.metadata
    import os
    import platform
    import struct
    import sys

    def is_python_64bit():
        return (struct.calcsize("P") == 8)

    def is_os_64bit():
        return platform.machine().endswith('64')

    def is_venv():
        return 'VIRTUAL_ENV' in os.environ

    info = {}
    info['os'] = {}
    info['python'] = {}
    info['driver'] = {}
    info['module'] = {}
    if platform.system() == 'Windows':
        try:
            import winreg as winreg
        except ImportError:
            import _winreg as winreg

        os_name = 'Windows'
        try:
            driver_version_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\National Instruments\NI-DMM\CurrentVersion")
            driver_version = winreg.QueryValueEx(driver_version_key, "Version")[0]
        except WindowsError:
            driver_version = 'Unknown'
    elif platform.system() == 'Linux':
        os_name = 'Linux'
        driver_version = 'Unknown'
    else:
        raise SystemError('Unsupported platform: {}'.format(platform.system()))

    installed_packages_names = [
        name
        for name_list in importlib.metadata.packages_distributions().values()
        for name in name_list
    ]
    installed_packages_names = set(installed_packages_names)
    installed_packages_list = [
        {'name': name, 'version': importlib.metadata.distribution(name).version}
        for name in sorted(installed_packages_names)
    ]

    info['os']['name'] = os_name
    info['os']['version'] = platform.version()
    info['os']['bits'] = '64' if is_os_64bit() else '32'
    info['driver']['name'] = "NI-DMM"
    info['driver']['version'] = driver_version
    info['module']['name'] = 'nidmm'
    info['module']['version'] = "1.4.10.dev0"
    info['python']['version'] = sys.version
    info['python']['bits'] = '64' if is_python_64bit() else '32'
    info['python']['is_venv'] = is_venv()
    info['python']['packages'] = installed_packages_list

    return info


def print_diagnostic_information():
    '''Print diagnostic information in a format suitable for issue report

    note: Python bitness may be incorrect when running in a virtual environment
    '''
    info = get_diagnostic_information()

    row_format = '    {:<10} {}'
    for type in ['OS', 'Driver', 'Module', 'Python']:
        typename = type.lower()
        print(type + ':')
        for item in info[typename]:
            if item != 'packages':
                print(row_format.format(item.title() + ':', info[typename][item]))
    print('    Installed Packages:')
    for p in info['python']['packages']:
        print((' ' * 8) + p['name'] + '==' + p['version'])

    return info
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidmm/nidmm/_attributes.py sha256=73b84c3f5e1ac8e91810348f6f94983f2b12c7ad50e8cd4ce4d64c4e036f64e6 bytes=6171 -->
## FILE: generated/nidmm/nidmm/_attributes.py

- repository: `ni/nimi-python`
- source_path: `generated/nidmm/nidmm/_attributes.py`
- sha256: `73b84c3f5e1ac8e91810348f6f94983f2b12c7ad50e8cd4ce4d64c4e036f64e6`
- bytes: 6171

````python
# -*- coding: utf-8 -*-
# This file was generated
import nidmm._converters as _converters
import nidmm.errors as errors

import hightime


class Attribute(object):
    '''Base class for all typed attributes.'''

    def __init__(self, attribute_id):
        self._attribute_id = attribute_id


class AttributeViInt32(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_int32(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_int32(self._attribute_id, value)


class AttributeViInt32TimeDeltaMilliseconds(Attribute):

    def __get__(self, session, session_type):
        return hightime.timedelta(milliseconds=session._get_attribute_vi_int32(self._attribute_id))

    def __set__(self, session, value):
        session._set_attribute_vi_int32(self._attribute_id, _converters.convert_timedelta_to_milliseconds_int32(value))


class AttributeViInt32TimeDeltaMonths(Attribute):

    def __get__(self, session, session_type):
        return _converters.convert_month_to_timedelta(session._get_attribute_vi_int32(self._attribute_id))

    def __set__(self, session, value):
        session._set_attribute_vi_int32(self._attribute_id, _converters.convert_timedelta_to_months_int32(value))


class AttributeViInt64(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_int64(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_int64(self._attribute_id, value)


class AttributeViReal64(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_real64(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_real64(self._attribute_id, value)


class AttributeViReal64TimeDeltaSeconds(Attribute):

    def __get__(self, session, session_type):
        return hightime.timedelta(seconds=session._get_attribute_vi_real64(self._attribute_id))

    def __set__(self, session, value):
        session._set_attribute_vi_real64(self._attribute_id, _converters.convert_timedelta_to_seconds_real64(value))


class AttributeViString(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_string(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_string(self._attribute_id, value)


class AttributeViStringRepeatedCapability(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_string(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_string(self._attribute_id, _converters.convert_repeated_capabilities_without_prefix(value))


class AttributeViStringCommaSeparated(Attribute):

    def __get__(self, session, session_type):
        return _converters.convert_comma_separated_string_to_list(session._get_attribute_vi_string(self._attribute_id))

    def __set__(self, session, value):
        session._set_attribute_vi_string(self._attribute_id, _converters.convert_list_to_comma_separated_string(value))


class AttributeViBoolean(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_boolean(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_boolean(self._attribute_id, value)


class AttributeEnum(Attribute):

    def __init__(self, underlying_attribute_meta_class, enum_meta_class, attribute_id):
        super(AttributeEnum, self).__init__(attribute_id)
        self._underlying_attribute = underlying_attribute_meta_class(attribute_id)
        self._attribute_type = enum_meta_class

    def __get__(self, session, session_type):
        return self._attribute_type(self._underlying_attribute.__get__(session, session_type))

    def __set__(self, session, value):
        if type(value) is not self._attribute_type:
            raise TypeError('must be ' + str(self._attribute_type.__name__) + ' not ' + str(type(value).__name__))
        return self._underlying_attribute.__set__(session, value.value)


class AttributeEnumWithConverter(Attribute):
    '''Class for attributes that use enums internally but are exposed in the nidmm Python module as something else, thus need conversion.'''

    def __init__(self, underlying_attribute_enum, getter_converter, setter_converter):
        '''Creates and returns an instance of AttributeEnumWithConverter attribute meta class.

        Args:
            underlying_attribute_enum (AttributeEnum): The AttributeEnum instance for the underlying
                enum

            getter_converter (function): The function that converts the enum value to its converted
                value

            setter_converter (function): The function that converts the converted value back to the
                enum value
        '''
        super(AttributeEnumWithConverter, self).__init__(underlying_attribute_enum._attribute_id)
        self._underlying_attribute_enum = underlying_attribute_enum
        self._getter_converter = getter_converter
        self._setter_converter = setter_converter

    def __get__(self, session, session_type):
        try:
            return self._getter_converter(
                self._underlying_attribute_enum.__get__(session, session_type)
            )
        except (KeyError, ValueError):
            raise errors.DriverTooNewError()

    def __set__(self, session, value):
        try:
            return self._underlying_attribute_enum.__set__(session, self._setter_converter(value))
        except KeyError:
            raise ValueError(f'Invalid value: {value}')


# nitclk specific attribute type
class AttributeSessionReference(Attribute):

    def __get__(self, session, session_type):
        # Import here to avoid a circular dependency when initial import happens
        from nidmm.session import SessionReference
        return SessionReference(session._get_attribute_vi_session(self._attribute_id))

    def __set__(self, session, value):
        session._set_attribute_vi_session(self._attribute_id, _converters.convert_to_nitclk_session_number(value))
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidmm/nidmm/_converters.py sha256=3f1a659d6b5f98e9f2d4e1c0ade80142a69c2cc7c7a28d5c922d970f5f30e7db bytes=14619 -->
## FILE: generated/nidmm/nidmm/_converters.py

- repository: `ni/nimi-python`
- source_path: `generated/nidmm/nidmm/_converters.py`
- sha256: `3f1a659d6b5f98e9f2d4e1c0ade80142a69c2cc7c7a28d5c922d970f5f30e7db`
- bytes: 14619

````python
# -*- coding: utf-8 -*-
# This file was generated
import nidmm._visatype as _visatype
import nidmm.errors as errors

import array
import collections
import hightime
import numbers

from functools import singledispatch


@singledispatch
def _convert_repeated_capabilities(arg, prefix):  # noqa: F811
    '''Base version that should not be called

    Overall purpose is to convert the repeated capabilities to a list of strings with prefix from what ever form

    Supported types:
    - str - List (comma delimited)
    - str - Range (using '-' or ':')
    - str - single item
    - int
    - tuple
    - range
    - slice

    Each instance should return a list of strings, without prefix
    - '0' --> ['0']
    - 0 --> ['0']
    - '0, 1' --> ['0', '1']
    - 'ScriptTrigger0, ScriptTrigger1' --> ['0', '1']
    - '0-1' --> ['0', '1']
    - '0:1' --> ['0', '1']
    - '0-1,4' --> ['0', '1', '4']
    - range(0, 2) --> ['0', '1']
    - slice(0, 2) --> ['0', '1']
    - (0, 1, 4) --> ['0', '1', '4']
    - ('0-1', 4) --> ['0', '1', '4']
    - (slice(0, 1), '2', [4, '5-6'], '7-9', '11:14', '16, 17') -->
        ['0', '2', '4', '5', '6', '7', '8', '9', '11', '12', '13', '14', '16', '17']
    '''
    raise errors.InvalidRepeatedCapabilityError('Invalid type', type(arg))


@_convert_repeated_capabilities.register(numbers.Integral)  # noqa: F811
def _(repeated_capability, prefix):
    '''Integer version'''
    return [str(repeated_capability)]


# This parsing function duplicate the parsing in the driver, so if changes to the allowed format are made there, they will need to be replicated here.
@_convert_repeated_capabilities.register(str)  # noqa: F811
def _(repeated_capability, prefix):
    '''String version (this is the most complex)

    We need to deal with a range ('0-3' or '0:3'), a list ('0,1,2,3') and a single item
    '''
    # First we deal with a list
    rep_cap_list = repeated_capability.split(',')
    if len(rep_cap_list) > 1:
        # We have a list so call ourselves again to let the iterable instance handle it
        return _convert_repeated_capabilities(rep_cap_list, prefix)

    # Now we deal with ranges
    # We remove any prefix and change ':' to '-'
    r = repeated_capability.strip().replace(prefix, '').replace(':', '-')
    rc = r.split('-')
    if len(rc) > 1:
        if len(rc) > 2:
            raise errors.InvalidRepeatedCapabilityError("Multiple '-' or ':'", repeated_capability)
        try:
            start = int(rc[0])
            end = int(rc[1])
        except ValueError:
            # This exception is raised when repeated_capability is of the form "dev/0-1". rc[0] == "dev/0" in this case.
            # Just return the repeated_capability string as-is in that case.
            pass
        else:
            if end < start:
                rng = range(start, end - 1, -1)
            else:
                rng = range(start, end + 1)
            return _convert_repeated_capabilities(rng, prefix)

    # If we made it here, it must be a simple item so we remove any prefix and return
    return [repeated_capability.replace(prefix, '').strip()]


# We cannot use collections.abc.Iterable here because strings are also iterable and then this
# instance is what gets called instead of the string one.
@_convert_repeated_capabilities.register(list)  # noqa: F811
@_convert_repeated_capabilities.register(range)  # noqa: F811
@_convert_repeated_capabilities.register(tuple)  # noqa: F811
def _(repeated_capability, prefix):
    '''Iterable version - can handle lists, ranges, and tuples'''
    rep_cap_list = []
    for r in repeated_capability:
        rep_cap_list += _convert_repeated_capabilities(r, prefix)
    return rep_cap_list


@_convert_repeated_capabilities.register(slice)  # noqa: F811
def _(repeated_capability, prefix):
    '''slice version'''
    def ifnone(a, b):
        return b if a is None else a
    # Turn the slice into a list and call ourselves again to let the iterable instance handle it
    rng = range(ifnone(repeated_capability.start, 0), repeated_capability.stop, ifnone(repeated_capability.step, 1))
    return _convert_repeated_capabilities(rng, prefix)


def convert_repeated_capabilities(repeated_capability, prefix=''):
    '''Convert a repeated capabilities object to a comma delimited list

    Args:
        repeated_capability (str, list, tuple, slice, None) -
        prefix (str) - common prefix for all strings

    Returns:
        rep_cap_list (list of str) - list of each repeated capability item with ranges expanded and prefix added
    '''
    # We need to explicitly handle None here. Everything else we can pass on to the singledispatch functions
    if repeated_capability is None:
        return []
    return [prefix + r for r in _convert_repeated_capabilities(repeated_capability, prefix)]


def convert_repeated_capabilities_without_prefix(repeated_capability):
    '''Convert a repeated capabilities object, without any prefix, to a comma delimited list

    Args:
        repeated_capability - Supported types:
            - str - list (comma-delimited)
            - str - range (using '-' or ':')
            - str - single item
            - int
            - list of str
            - tuple of str
            - range of str
            - slice of str
            - None

    Returns:
        rep_cap (str) - comma delimited string of each repeated capability item with ranges expanded
    '''
    return ','.join(convert_repeated_capabilities(repeated_capability, ''))


def expand_channel_string(channel_string, all_channels_in_session):
    '''Expands a channel_string to a list of individual channel names.

    The individual channel names may or may not be fully qualified channel names as applicable for
    the session. In other words, the individual channel names will be a subset of
    all_channels_in_session.

    Examples:
        - expand_channel_string('1', ['0', '1', '2', '3']) --> ['1']
        - expand_channel_string('4,1:2', ['1', '2', '4']) --> ['4', '1', '2']
        - expand_channel_string('2:3,0', ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/3'])
            --> ['Dev1/2', 'Dev1/3', 'Dev1/0']
        - expand_channel_string('Dev1/1', ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/3'])
            --> ['Dev1/1']
        - expand_channel_string('4,Dev1/1:2', ['Dev1/1', 'Dev1/2', 'Dev1/4'])
            --> ['Dev1/4', 'Dev1/1', 'Dev1/2']
        - expand_channel_string('Dev1/4,Dev1/2,Dev1/3', ['Dev1/2', 'Dev1/3', 'Dev1/4'])
            --> ['Dev1/4', 'Dev1/2', 'Dev1/3']
        - expand_channel_string('Dev1/1,Dev2/2', ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/3', 'Dev2/0', 'Dev2/1', 'Dev2/2', 'Dev2/3'])
            --> ['Dev1/1', 'Dev2/2']
        - expand_channel_string(' Dev1 / 1 : 2 , 4 ', ['Dev1/1', 'Dev1/2', 'Dev1/4'])
            --> ['Dev1/1', 'Dev1/2', 'Dev1/4']
        - expand_channel_string('DEV1/0-1    , Dev1/3', ['dev1/0', 'dev1/1', 'dev1/2', 'dev1/3'])
            --> ['dev1/0', 'dev1/1', 'dev1/3']

    Args:
        channel_string (str) - refer to _convert_repeated_capabilities() for the
            supported formats (this string is expected to be used as the index of session.channels)

        all_channels_in_session (list of str) - names of all the channels in the session as returned
            by get_channel_names()

    Returns:
        channel_names (list of str) - A list in which each element is the name of a single channel,
            with the exact capitalization used by the driver runtime.
    '''
    if channel_string.strip() == '':
        return all_channels_in_session

    # Rule 1: If all_channels_in_session is fully-qualified then returned channel names should be
    #         fully-qualified, otherwise returned channel names should not be fully-qualified.
    # Rule 2: If any channel in the input is not fully-qualified, but we need to return
    #         fully-qualified channels because of Rule 1, then use the channel qualifier obtained
    #         from all_channels_in_session. This can only happen on a single-instrument session,
    #         so all the channel qualifiers are the same and we pick the first one.

    instrument, separator, channel = all_channels_in_session[0].rpartition('/')
    default_channel_qualifier = instrument + separator

    expanded_channel_list = []
    for token in channel_string.split(','):
        instrument, separator, channel = token.rpartition('/')
        instrument = instrument.strip()
        channel_qualifier = instrument + separator if instrument else default_channel_qualifier
        expanded_channel_list.extend(
            convert_repeated_capabilities(channel.strip(), channel_qualifier)
        )

    # Convert the expanded channel names to their canonical form based on all_channels_in_session
    lowercase_channel_name_to_session_channel_name_dict = {
        channel_name.lower(): channel_name for channel_name in all_channels_in_session
    }
    return [
        lowercase_channel_name_to_session_channel_name_dict[channel_name.lower()]
        for channel_name in expanded_channel_list
    ]


def _convert_timedelta(value, library_type, scaling):
    try:
        # We first assume it is a timedelta object
        scaled_value = value.total_seconds() * scaling
    except AttributeError:
        # If that doesn't work, assume it is a value in seconds
        # cast to float so scaled_value is always a float. This allows `timeout=10` to work as expected
        scaled_value = float(value) * scaling

    # ctype integer types don't convert to int from float so we need to
    if library_type in [_visatype.ViInt64, _visatype.ViInt32, _visatype.ViUInt32, _visatype.ViInt16, _visatype.ViUInt16, _visatype.ViInt8]:
        scaled_value = int(scaled_value)

    return scaled_value


def convert_timedelta_to_seconds_real64(value):
    return _convert_timedelta(value, _visatype.ViReal64, 1)


def convert_timedelta_to_milliseconds_int32(value):
    return _convert_timedelta(value, _visatype.ViInt32, 1000)


def convert_timedeltas_to_seconds_real64(values):
    return [convert_timedelta_to_seconds_real64(i) for i in values]


def convert_seconds_real64_to_timedelta(value):
    return hightime.timedelta(seconds=value)


def convert_seconds_real64_to_timedeltas(values):
    return [convert_seconds_real64_to_timedelta(i) for i in values]


def convert_month_to_timedelta(months):
    return hightime.timedelta(days=(30.4167 * months))


# Scaling factor to apply on seconds to get months
# would be 1/(60 seconds * 60 minutes * 24 hours * 30.4167 days)
def convert_timedelta_to_months_int32(value):
    return _convert_timedelta(value, _visatype.ViInt32, 1.0 / (60 * 60 * 24 * 30.4167))


# This converter is not called from the normal codegen path for function. Instead it is
# call from init and is a special case.
def convert_init_with_options_dictionary(values):
    if type(values) is str:
        init_with_options_string = values
    else:
        good_keys = {
            'rangecheck': 'RangeCheck',
            'queryinstrstatus': 'QueryInstrStatus',
            'cache': 'Cache',
            'simulate': 'Simulate',
            'recordcoercions': 'RecordCoercions',
            'interchangecheck': 'InterchangeCheck',
            'driversetup': 'DriverSetup',
            'range_check': 'RangeCheck',
            'query_instr_status': 'QueryInstrStatus',
            'record_coercions': 'RecordCoercions',
            'interchange_check': 'InterchangeCheck',
            'driver_setup': 'DriverSetup',
        }
        init_with_options = []
        for k in sorted(values.keys()):
            value = None
            if k.lower() in good_keys and not good_keys[k.lower()] == 'DriverSetup':
                value = good_keys[k.lower()] + ('=1' if values[k] is True else '=0')
            elif k.lower() in good_keys and good_keys[k.lower()] == 'DriverSetup':
                if not isinstance(values[k], dict):
                    raise TypeError('DriverSetup must be a dictionary')
                value = 'DriverSetup=' + (';'.join([key + ':' + values[k][key] for key in sorted(values[k])]))
            else:
                value = k + ('=1' if values[k] is True else '=0')

            init_with_options.append(value)

        init_with_options_string = ','.join(init_with_options)

    return init_with_options_string


# convert value to bytes
@singledispatch
def _convert_to_bytes(value):  # noqa: F811
    pass


@_convert_to_bytes.register(list)  # noqa: F811
@_convert_to_bytes.register(bytes)  # noqa: F811
@_convert_to_bytes.register(bytearray)  # noqa: F811
@_convert_to_bytes.register(array.array)  # noqa: F811
def _(value):
    return value


@_convert_to_bytes.register(str)  # noqa: F811
def _(value):
    return value.encode()


def convert_to_bytes(value):  # noqa: F811
    return bytes(_convert_to_bytes(value))


def convert_comma_separated_string_to_list(comma_separated_string):
    return [x.strip() for x in comma_separated_string.split(',')]


def convert_list_to_comma_separated_string(list_of_strings):
    '''Convert a list or tuple of strings into a comma-separated string.

    Args:
        list_of_strings (list or tuple of str): List or tuple of strings.

    Returns:
        str: Comma-separated string.
    '''
    if not isinstance(list_of_strings, (list, tuple)) or not all(isinstance(item, str) for item in list_of_strings):
        raise TypeError('Input must be a list or tuple of str')
    return ','.join(list_of_strings)


def convert_chained_repeated_capability_to_parts(chained_repeated_capability):
    '''Convert a chained repeated capabilities string to a list of comma-delimited repeated capabilities string.

    Converter assumes that the input contains the full cartesian product of its parts.
    e.g. If chained_repeated_capability is 'site0/PinA,site0/PinB,site1/PinA,site1/PinB',
    ['site0,site1', 'PinA,PinB'] is returned.

    Args:
        chained_repeated_capability (str) - comma-delimited repeated capabilities string where each
        item is a chain of slash-delimited repeated capabilities

    Returns:
        rep_cap_list (list of str) - list of comma-delimited repeated capabilities string
    '''
    chained_repeated_capability_items = convert_comma_separated_string_to_list(chained_repeated_capability)
    repeated_capability_lists = [[] for _ in range(chained_repeated_capability_items[0].count('/') + 1)]
    for item in chained_repeated_capability_items:
        repeated_capability_lists = [x + [y] for x, y in zip(repeated_capability_lists, item.split('/'))]
    return [','.join(collections.OrderedDict.fromkeys(x)) for x in repeated_capability_lists]
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidmm/nidmm/_grpc_stub_interpreter.py sha256=c15af28753dfa8337a4fbeb8a22228b94a22c454841e451535a69a7a023abad4 bytes=16527 -->
## FILE: generated/nidmm/nidmm/_grpc_stub_interpreter.py

- repository: `ni/nimi-python`
- source_path: `generated/nidmm/nidmm/_grpc_stub_interpreter.py`
- sha256: `c15af28753dfa8337a4fbeb8a22228b94a22c454841e451535a69a7a023abad4`
- bytes: 16527

````python
# -*- coding: utf-8 -*-
# This file was generated

import grpc
import hightime  # noqa: F401
import session_pb2 as session_grpc_types
import threading
import warnings

from . import enums as enums  # noqa: F401
from . import errors as errors
from . import nidmm_pb2 as grpc_types
from . import nidmm_pb2_grpc as nidmm_grpc


class GrpcStubInterpreter(object):
    '''Interpreter for interacting with a gRPC Stub class'''

    def __init__(self, grpc_options):
        self._grpc_options = grpc_options
        self._lock = threading.RLock()
        self._client = nidmm_grpc.NiDmmStub(grpc_options.grpc_channel)
        self.set_session_handle()

    def set_session_handle(self, value=session_grpc_types.Session()):
        self._vi = value

    def get_session_handle(self):
        return self._vi

    def _invoke(self, func, request, metadata=None):
        try:
            response = func(request, metadata=metadata)
            error_code = response.status
            error_message = ''
        except grpc.RpcError as rpc_error:
            error_code = None
            error_message = rpc_error.details()
            for entry in rpc_error.trailing_metadata() or []:
                if entry.key == 'ni-error':
                    value = entry.value if isinstance(entry.value, str) else entry.value.decode('utf-8')
                    try:
                        error_code = int(value)
                    except ValueError:
                        error_message += f'\nError status: {value}'

            grpc_error = rpc_error.code()
            if grpc_error == grpc.StatusCode.NOT_FOUND:
                raise errors.DriverTooOldError() from None
            elif grpc_error == grpc.StatusCode.INVALID_ARGUMENT:
                raise ValueError(error_message) from None
            elif grpc_error == grpc.StatusCode.UNAVAILABLE:
                error_message = 'Failed to connect to server'
            elif grpc_error == grpc.StatusCode.UNIMPLEMENTED:
                error_message = (
                    'This operation is not supported by the NI gRPC Device Server being used. Upgrade NI gRPC Device Server.'
                )

            if error_code is None:
                raise errors.RpcError(grpc_error, error_message) from None

        if error_code < 0:
            raise errors.DriverError(error_code, error_message)
        elif error_code > 0:
            if not error_message:
                try:
                    error_message = self.error_message(error_code)
                except errors.Error:
                    error_message = 'Failed to retrieve error description.'
            warnings.warn(errors.DriverWarning(error_code, error_message))
        return response

    def abort(self):  # noqa: N802
        self._invoke(
            self._client.Abort,
            grpc_types.AbortRequest(vi=self._vi),
        )

    def configure_measurement_absolute(self, measurement_function, range, resolution_absolute):  # noqa: N802
        self._invoke(
            self._client.ConfigureMeasurementAbsolute,
            grpc_types.ConfigureMeasurementAbsoluteRequest(vi=self._vi, measurement_function_raw=measurement_function.value, range=range, resolution_absolute=resolution_absolute),
        )

    def configure_measurement_digits(self, measurement_function, range, resolution_digits):  # noqa: N802
        self._invoke(
            self._client.ConfigureMeasurementDigits,
            grpc_types.ConfigureMeasurementDigitsRequest(vi=self._vi, measurement_function_raw=measurement_function.value, range=range, resolution_digits=resolution_digits),
        )

    def configure_multi_point(self, trigger_count, sample_count, sample_trigger, sample_interval):  # noqa: N802
        self._invoke(
            self._client.ConfigureMultiPoint,
            grpc_types.ConfigureMultiPointRequest(vi=self._vi, trigger_count_raw=trigger_count, sample_count_raw=sample_count, sample_trigger_raw=sample_trigger.value, sample_interval_raw=sample_interval),
        )

    def configure_rtd_custom(self, rtd_a, rtd_b, rtd_c):  # noqa: N802
        self._invoke(
            self._client.ConfigureRTDCustom,
            grpc_types.ConfigureRTDCustomRequest(vi=self._vi, rtd_a=rtd_a, rtd_b=rtd_b, rtd_c=rtd_c),
        )

    def configure_rtd_type(self, rtd_type, rtd_resistance):  # noqa: N802
        self._invoke(
            self._client.ConfigureRTDType,
            grpc_types.ConfigureRTDTypeRequest(vi=self._vi, rtd_type_raw=rtd_type.value, rtd_resistance=rtd_resistance),
        )

    def configure_thermistor_custom(self, thermistor_a, thermistor_b, thermistor_c):  # noqa: N802
        self._invoke(
            self._client.ConfigureThermistorCustom,
            grpc_types.ConfigureThermistorCustomRequest(vi=self._vi, thermistor_a=thermistor_a, thermistor_b=thermistor_b, thermistor_c=thermistor_c),
        )

    def configure_thermocouple(self, thermocouple_type, reference_junction_type):  # noqa: N802
        self._invoke(
            self._client.ConfigureThermocouple,
            grpc_types.ConfigureThermocoupleRequest(vi=self._vi, thermocouple_type_raw=thermocouple_type.value, reference_junction_type_raw=reference_junction_type.value),
        )

    def configure_trigger(self, trigger_source, trigger_delay):  # noqa: N802
        self._invoke(
            self._client.ConfigureTrigger,
            grpc_types.ConfigureTriggerRequest(vi=self._vi, trigger_source_raw=trigger_source.value, trigger_delay_raw=trigger_delay),
        )

    def configure_waveform_acquisition(self, measurement_function, range, rate, waveform_points):  # noqa: N802
        self._invoke(
            self._client.ConfigureWaveformAcquisition,
            grpc_types.ConfigureWaveformAcquisitionRequest(vi=self._vi, measurement_function_raw=measurement_function.value, range=range, rate=rate, waveform_points=waveform_points),
        )

    def disable(self):  # noqa: N802
        self._invoke(
            self._client.Disable,
            grpc_types.DisableRequest(vi=self._vi),
        )

    def export_attribute_configuration_buffer(self):  # noqa: N802
        response = self._invoke(
            self._client.ExportAttributeConfigurationBuffer,
            grpc_types.ExportAttributeConfigurationBufferRequest(vi=self._vi),
        )
        return response.configuration

    def export_attribute_configuration_file(self, file_path):  # noqa: N802
        self._invoke(
            self._client.ExportAttributeConfigurationFile,
            grpc_types.ExportAttributeConfigurationFileRequest(vi=self._vi, file_path=file_path),
        )

    def fetch(self, maximum_time):  # noqa: N802
        response = self._invoke(
            self._client.Fetch,
            grpc_types.FetchRequest(vi=self._vi, maximum_time_raw=maximum_time),
        )
        return response.reading

    def fetch_multi_point(self, maximum_time, array_size):  # noqa: N802
        response = self._invoke(
            self._client.FetchMultiPoint,
            grpc_types.FetchMultiPointRequest(vi=self._vi, maximum_time_raw=maximum_time, array_size=array_size),
        )
        return response.reading_array

    def fetch_waveform(self, maximum_time, array_size):  # noqa: N802
        response = self._invoke(
            self._client.FetchWaveform,
            grpc_types.FetchWaveformRequest(vi=self._vi, maximum_time_raw=maximum_time, array_size=array_size),
        )
        return response.waveform_array

    def fetch_waveform_into(self, maximum_time, array_size):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')

    def get_attribute_vi_boolean(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViBoolean,
            grpc_types.GetAttributeViBooleanRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.attribute_value

    def get_attribute_vi_int32(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViInt32,
            grpc_types.GetAttributeViInt32Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.attribute_value

    def get_attribute_vi_real64(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViReal64,
            grpc_types.GetAttributeViReal64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.attribute_value

    def get_attribute_vi_string(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViString,
            grpc_types.GetAttributeViStringRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.attribute_value

    def get_cal_date_and_time(self, cal_type):  # noqa: N802
        response = self._invoke(
            self._client.GetCalDateAndTime,
            grpc_types.GetCalDateAndTimeRequest(vi=self._vi, cal_type=cal_type),
        )
        return response.month, response.day, response.year, response.hour, response.minute

    def get_dev_temp(self, options):  # noqa: N802
        response = self._invoke(
            self._client.GetDevTemp,
            grpc_types.GetDevTempRequest(vi=self._vi, options=options),
        )
        return response.temperature

    def get_error(self):  # noqa: N802
        response = self._invoke(
            self._client.GetError,
            grpc_types.GetErrorRequest(vi=self._vi),
        )
        return response.error_code, response.description

    def get_ext_cal_recommended_interval(self):  # noqa: N802
        response = self._invoke(
            self._client.GetExtCalRecommendedInterval,
            grpc_types.GetExtCalRecommendedIntervalRequest(vi=self._vi),
        )
        return response.months

    def get_last_cal_temp(self, cal_type):  # noqa: N802
        response = self._invoke(
            self._client.GetLastCalTemp,
            grpc_types.GetLastCalTempRequest(vi=self._vi, cal_type=cal_type),
        )
        return response.temperature

    def get_self_cal_supported(self):  # noqa: N802
        response = self._invoke(
            self._client.GetSelfCalSupported,
            grpc_types.GetSelfCalSupportedRequest(vi=self._vi),
        )
        return response.self_cal_supported

    def import_attribute_configuration_buffer(self, configuration):  # noqa: N802
        self._invoke(
            self._client.ImportAttributeConfigurationBuffer,
            grpc_types.ImportAttributeConfigurationBufferRequest(vi=self._vi, configuration=configuration),
        )

    def import_attribute_configuration_file(self, file_path):  # noqa: N802
        self._invoke(
            self._client.ImportAttributeConfigurationFile,
            grpc_types.ImportAttributeConfigurationFileRequest(vi=self._vi, file_path=file_path),
        )

    def init_with_options(self, resource_name, id_query, reset_device, option_string):  # noqa: N802
        metadata = (
            ('ni-api-key', self._grpc_options.api_key),
        )
        response = self._invoke(
            self._client.InitWithOptions,
            grpc_types.InitWithOptionsRequest(resource_name=resource_name, id_query=id_query, reset_device=reset_device, option_string=option_string, session_name=self._grpc_options.session_name, initialization_behavior=self._grpc_options.initialization_behavior),
            metadata=metadata,
        )
        self._close_on_exit = response.new_session_initialized
        return response.vi

    def initiate(self):  # noqa: N802
        self._invoke(
            self._client.Initiate,
            grpc_types.InitiateRequest(vi=self._vi),
        )

    def lock(self):  # noqa: N802
        self._lock.acquire()

    def perform_open_cable_comp(self):  # noqa: N802
        response = self._invoke(
            self._client.PerformOpenCableComp,
            grpc_types.PerformOpenCableCompRequest(vi=self._vi),
        )
        return response.conductance, response.susceptance

    def perform_short_cable_comp(self):  # noqa: N802
        response = self._invoke(
            self._client.PerformShortCableComp,
            grpc_types.PerformShortCableCompRequest(vi=self._vi),
        )
        return response.resistance, response.reactance

    def read(self, maximum_time):  # noqa: N802
        response = self._invoke(
            self._client.Read,
            grpc_types.ReadRequest(vi=self._vi, maximum_time_raw=maximum_time),
        )
        return response.reading

    def read_multi_point(self, maximum_time, array_size):  # noqa: N802
        response = self._invoke(
            self._client.ReadMultiPoint,
            grpc_types.ReadMultiPointRequest(vi=self._vi, maximum_time_raw=maximum_time, array_size=array_size),
        )
        return response.reading_array

    def read_status(self):  # noqa: N802
        response = self._invoke(
            self._client.ReadStatus,
            grpc_types.ReadStatusRequest(vi=self._vi),
        )
        return response.acquisition_backlog, enums.AcquisitionStatus(response.acquisition_status_raw)

    def read_waveform(self, maximum_time, array_size):  # noqa: N802
        response = self._invoke(
            self._client.ReadWaveform,
            grpc_types.ReadWaveformRequest(vi=self._vi, maximum_time_raw=maximum_time, array_size=array_size),
        )
        return response.waveform_array

    def reset_with_defaults(self):  # noqa: N802
        self._invoke(
            self._client.ResetWithDefaults,
            grpc_types.ResetWithDefaultsRequest(vi=self._vi),
        )

    def self_cal(self):  # noqa: N802
        self._invoke(
            self._client.SelfCal,
            grpc_types.SelfCalRequest(vi=self._vi),
        )

    def send_software_trigger(self):  # noqa: N802
        self._invoke(
            self._client.SendSoftwareTrigger,
            grpc_types.SendSoftwareTriggerRequest(vi=self._vi),
        )

    def set_attribute_vi_boolean(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViBoolean,
            grpc_types.SetAttributeViBooleanRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, attribute_value=attribute_value),
        )

    def set_attribute_vi_int32(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViInt32,
            grpc_types.SetAttributeViInt32Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, attribute_value_raw=attribute_value),
        )

    def set_attribute_vi_real64(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViReal64,
            grpc_types.SetAttributeViReal64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, attribute_value_raw=attribute_value),
        )

    def set_attribute_vi_string(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViString,
            grpc_types.SetAttributeViStringRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, attribute_value_raw=attribute_value),
        )

    def set_runtime_environment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        raise NotImplementedError('set_runtime_environment is not supported over gRPC')

    def unlock(self):  # noqa: N802
        self._lock.release()

    def close(self):  # noqa: N802
        self._invoke(
            self._client.Close,
            grpc_types.CloseRequest(vi=self._vi),
        )

    def error_message(self, error_code):  # noqa: N802
        response = self._invoke(
            self._client.GetErrorMessage,
            grpc_types.GetErrorMessageRequest(vi=self._vi, error_code=error_code),
        )
        return response.error_message

    def reset(self):  # noqa: N802
        self._invoke(
            self._client.Reset,
            grpc_types.ResetRequest(vi=self._vi),
        )

    def self_test(self):  # noqa: N802
        response = self._invoke(
            self._client.SelfTest,
            grpc_types.SelfTestRequest(vi=self._vi),
        )
        return response.self_test_result, response.self_test_message
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidmm/nidmm/_library.py sha256=42684e8b317ea87c4cc685a23cfefb02514420501a3bc1b6b59c88ab0de994fc bytes=32338 -->
## FILE: generated/nidmm/nidmm/_library.py

- repository: `ni/nimi-python`
- source_path: `generated/nidmm/nidmm/_library.py`
- sha256: `42684e8b317ea87c4cc685a23cfefb02514420501a3bc1b6b59c88ab0de994fc`
- bytes: 32338

````python
# -*- coding: utf-8 -*-
# This file was generated

import ctypes
import nidmm.errors as errors
import threading

from nidmm._visatype import *  # noqa: F403,H303


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, ctypes_library):
        self._func_lock = threading.Lock()
        self._library = ctypes_library
        # We cache the cfunc object from the ctypes.CDLL object
        self.niDMM_Abort_cfunc = None
        self.niDMM_ConfigureMeasurementAbsolute_cfunc = None
        self.niDMM_ConfigureMeasurementDigits_cfunc = None
        self.niDMM_ConfigureMultiPoint_cfunc = None
        self.niDMM_ConfigureRTDCustom_cfunc = None
        self.niDMM_ConfigureRTDType_cfunc = None
        self.niDMM_ConfigureThermistorCustom_cfunc = None
        self.niDMM_ConfigureThermocouple_cfunc = None
        self.niDMM_ConfigureTrigger_cfunc = None
        self.niDMM_ConfigureWaveformAcquisition_cfunc = None
        self.niDMM_Disable_cfunc = None
        self.niDMM_ExportAttributeConfigurationBuffer_cfunc = None
        self.niDMM_ExportAttributeConfigurationFile_cfunc = None
        self.niDMM_Fetch_cfunc = None
        self.niDMM_FetchMultiPoint_cfunc = None
        self.niDMM_FetchWaveform_cfunc = None
        self.niDMM_GetAttributeViBoolean_cfunc = None
        self.niDMM_GetAttributeViInt32_cfunc = None
        self.niDMM_GetAttributeViReal64_cfunc = None
        self.niDMM_GetAttributeViString_cfunc = None
        self.niDMM_GetCalDateAndTime_cfunc = None
        self.niDMM_GetDevTemp_cfunc = None
        self.niDMM_GetError_cfunc = None
        self.niDMM_GetExtCalRecommendedInterval_cfunc = None
        self.niDMM_GetLastCalTemp_cfunc = None
        self.niDMM_GetSelfCalSupported_cfunc = None
        self.niDMM_ImportAttributeConfigurationBuffer_cfunc = None
        self.niDMM_ImportAttributeConfigurationFile_cfunc = None
        self.niDMM_InitWithOptions_cfunc = None
        self.niDMM_Initiate_cfunc = None
        self.niDMM_LockSession_cfunc = None
        self.niDMM_PerformOpenCableComp_cfunc = None
        self.niDMM_PerformShortCableComp_cfunc = None
        self.niDMM_Read_cfunc = None
        self.niDMM_ReadMultiPoint_cfunc = None
        self.niDMM_ReadStatus_cfunc = None
        self.niDMM_ReadWaveform_cfunc = None
        self.niDMM_ResetWithDefaults_cfunc = None
        self.niDMM_SelfCal_cfunc = None
        self.niDMM_SendSoftwareTrigger_cfunc = None
        self.niDMM_SetAttributeViBoolean_cfunc = None
        self.niDMM_SetAttributeViInt32_cfunc = None
        self.niDMM_SetAttributeViReal64_cfunc = None
        self.niDMM_SetAttributeViString_cfunc = None
        self.niDMM_SetRuntimeEnvironment_cfunc = None
        self.niDMM_UnlockSession_cfunc = None
        self.niDMM_close_cfunc = None
        self.niDMM_error_message_cfunc = None
        self.niDMM_reset_cfunc = None
        self.niDMM_self_test_cfunc = None

    def _get_library_function(self, name):
        try:
            function = getattr(self._library, name)
        except AttributeError as e:
            raise errors.DriverTooOldError() from e
        return function

    def niDMM_Abort(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_Abort_cfunc is None:
                self.niDMM_Abort_cfunc = self._get_library_function('niDMM_Abort')
                self.niDMM_Abort_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDMM_Abort_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_Abort_cfunc(vi)

    def niDMM_ConfigureMeasurementAbsolute(self, vi, measurement_function, range, resolution_absolute):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureMeasurementAbsolute_cfunc is None:
                self.niDMM_ConfigureMeasurementAbsolute_cfunc = self._get_library_function('niDMM_ConfigureMeasurementAbsolute')
                self.niDMM_ConfigureMeasurementAbsolute_cfunc.argtypes = [ViSession, ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niDMM_ConfigureMeasurementAbsolute_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ConfigureMeasurementAbsolute_cfunc(vi, measurement_function, range, resolution_absolute)

    def niDMM_ConfigureMeasurementDigits(self, vi, measurement_function, range, resolution_digits):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureMeasurementDigits_cfunc is None:
                self.niDMM_ConfigureMeasurementDigits_cfunc = self._get_library_function('niDMM_ConfigureMeasurementDigits')
                self.niDMM_ConfigureMeasurementDigits_cfunc.argtypes = [ViSession, ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niDMM_ConfigureMeasurementDigits_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ConfigureMeasurementDigits_cfunc(vi, measurement_function, range, resolution_digits)

    def niDMM_ConfigureMultiPoint(self, vi, trigger_count, sample_count, sample_trigger, sample_interval):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureMultiPoint_cfunc is None:
                self.niDMM_ConfigureMultiPoint_cfunc = self._get_library_function('niDMM_ConfigureMultiPoint')
                self.niDMM_ConfigureMultiPoint_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ViInt32, ViReal64]  # noqa: F405
                self.niDMM_ConfigureMultiPoint_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ConfigureMultiPoint_cfunc(vi, trigger_count, sample_count, sample_trigger, sample_interval)

    def niDMM_ConfigureRTDCustom(self, vi, rtd_a, rtd_b, rtd_c):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureRTDCustom_cfunc is None:
                self.niDMM_ConfigureRTDCustom_cfunc = self._get_library_function('niDMM_ConfigureRTDCustom')
                self.niDMM_ConfigureRTDCustom_cfunc.argtypes = [ViSession, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niDMM_ConfigureRTDCustom_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ConfigureRTDCustom_cfunc(vi, rtd_a, rtd_b, rtd_c)

    def niDMM_ConfigureRTDType(self, vi, rtd_type, rtd_resistance):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureRTDType_cfunc is None:
                self.niDMM_ConfigureRTDType_cfunc = self._get_library_function('niDMM_ConfigureRTDType')
                self.niDMM_ConfigureRTDType_cfunc.argtypes = [ViSession, ViInt32, ViReal64]  # noqa: F405
                self.niDMM_ConfigureRTDType_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ConfigureRTDType_cfunc(vi, rtd_type, rtd_resistance)

    def niDMM_ConfigureThermistorCustom(self, vi, thermistor_a, thermistor_b, thermistor_c):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureThermistorCustom_cfunc is None:
                self.niDMM_ConfigureThermistorCustom_cfunc = self._get_library_function('niDMM_ConfigureThermistorCustom')
                self.niDMM_ConfigureThermistorCustom_cfunc.argtypes = [ViSession, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niDMM_ConfigureThermistorCustom_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ConfigureThermistorCustom_cfunc(vi, thermistor_a, thermistor_b, thermistor_c)

    def niDMM_ConfigureThermocouple(self, vi, thermocouple_type, reference_junction_type):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureThermocouple_cfunc is None:
                self.niDMM_ConfigureThermocouple_cfunc = self._get_library_function('niDMM_ConfigureThermocouple')
                self.niDMM_ConfigureThermocouple_cfunc.argtypes = [ViSession, ViInt32, ViInt32]  # noqa: F405
                self.niDMM_ConfigureThermocouple_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ConfigureThermocouple_cfunc(vi, thermocouple_type, reference_junction_type)

    def niDMM_ConfigureTrigger(self, vi, trigger_source, trigger_delay):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureTrigger_cfunc is None:
                self.niDMM_ConfigureTrigger_cfunc = self._get_library_function('niDMM_ConfigureTrigger')
                self.niDMM_ConfigureTrigger_cfunc.argtypes = [ViSession, ViInt32, ViReal64]  # noqa: F405
                self.niDMM_ConfigureTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ConfigureTrigger_cfunc(vi, trigger_source, trigger_delay)

    def niDMM_ConfigureWaveformAcquisition(self, vi, measurement_function, range, rate, waveform_points):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ConfigureWaveformAcquisition_cfunc is None:
                self.niDMM_ConfigureWaveformAcquisition_cfunc = self._get_library_function('niDMM_ConfigureWaveformAcquisition')
                self.niDMM_ConfigureWaveformAcquisition_cfunc.argtypes = [ViSession, ViInt32, ViReal64, ViReal64, ViInt32]  # noqa: F405
                self.niDMM_ConfigureWaveformAcquisition_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ConfigureWaveformAcquisition_cfunc(vi, measurement_function, range, rate, waveform_points)

    def niDMM_Disable(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_Disable_cfunc is None:
                self.niDMM_Disable_cfunc = self._get_library_function('niDMM_Disable')
                self.niDMM_Disable_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDMM_Disable_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_Disable_cfunc(vi)

    def niDMM_ExportAttributeConfigurationBuffer(self, vi, size, configuration):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ExportAttributeConfigurationBuffer_cfunc is None:
                self.niDMM_ExportAttributeConfigurationBuffer_cfunc = self._get_library_function('niDMM_ExportAttributeConfigurationBuffer')
                self.niDMM_ExportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niDMM_ExportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ExportAttributeConfigurationBuffer_cfunc(vi, size, configuration)

    def niDMM_ExportAttributeConfigurationFile(self, vi, file_path):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ExportAttributeConfigurationFile_cfunc is None:
                self.niDMM_ExportAttributeConfigurationFile_cfunc = self._get_library_function('niDMM_ExportAttributeConfigurationFile')
                self.niDMM_ExportAttributeConfigurationFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDMM_ExportAttributeConfigurationFile_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ExportAttributeConfigurationFile_cfunc(vi, file_path)

    def niDMM_Fetch(self, vi, maximum_time, reading):  # noqa: N802
        with self._func_lock:
            if self.niDMM_Fetch_cfunc is None:
                self.niDMM_Fetch_cfunc = self._get_library_function('niDMM_Fetch')
                self.niDMM_Fetch_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDMM_Fetch_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_Fetch_cfunc(vi, maximum_time, reading)

    def niDMM_FetchMultiPoint(self, vi, maximum_time, array_size, reading_array, actual_number_of_points):  # noqa: N802
        with self._func_lock:
            if self.niDMM_FetchMultiPoint_cfunc is None:
                self.niDMM_FetchMultiPoint_cfunc = self._get_library_function('niDMM_FetchMultiPoint')
                self.niDMM_FetchMultiPoint_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDMM_FetchMultiPoint_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_FetchMultiPoint_cfunc(vi, maximum_time, array_size, reading_array, actual_number_of_points)

    def niDMM_FetchWaveform(self, vi, maximum_time, array_size, waveform_array, actual_number_of_points):  # noqa: N802
        with self._func_lock:
            if self.niDMM_FetchWaveform_cfunc is None:
                self.niDMM_FetchWaveform_cfunc = self._get_library_function('niDMM_FetchWaveform')
                self.niDMM_FetchWaveform_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDMM_FetchWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_FetchWaveform_cfunc(vi, maximum_time, array_size, waveform_array, actual_number_of_points)

    def niDMM_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetAttributeViBoolean_cfunc is None:
                self.niDMM_GetAttributeViBoolean_cfunc = self._get_library_function('niDMM_GetAttributeViBoolean')
                self.niDMM_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDMM_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_GetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetAttributeViInt32_cfunc is None:
                self.niDMM_GetAttributeViInt32_cfunc = self._get_library_function('niDMM_GetAttributeViInt32')
                self.niDMM_GetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDMM_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_GetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetAttributeViReal64_cfunc is None:
                self.niDMM_GetAttributeViReal64_cfunc = self._get_library_function('niDMM_GetAttributeViReal64')
                self.niDMM_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDMM_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_GetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_GetAttributeViString(self, vi, channel_name, attribute_id, buffer_size, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetAttributeViString_cfunc is None:
                self.niDMM_GetAttributeViString_cfunc = self._get_library_function('niDMM_GetAttributeViString')
                self.niDMM_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDMM_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_GetAttributeViString_cfunc(vi, channel_name, attribute_id, buffer_size, attribute_value)

    def niDMM_GetCalDateAndTime(self, vi, cal_type, month, day, year, hour, minute):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetCalDateAndTime_cfunc is None:
                self.niDMM_GetCalDateAndTime_cfunc = self._get_library_function('niDMM_GetCalDateAndTime')
                self.niDMM_GetCalDateAndTime_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDMM_GetCalDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_GetCalDateAndTime_cfunc(vi, cal_type, month, day, year, hour, minute)

    def niDMM_GetDevTemp(self, vi, options, temperature):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetDevTemp_cfunc is None:
                self.niDMM_GetDevTemp_cfunc = self._get_library_function('niDMM_GetDevTemp')
                self.niDMM_GetDevTemp_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDMM_GetDevTemp_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_GetDevTemp_cfunc(vi, options, temperature)

    def niDMM_GetError(self, vi, error_code, buffer_size, description):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetError_cfunc is None:
                self.niDMM_GetError_cfunc = self._get_library_function('niDMM_GetError')
                self.niDMM_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDMM_GetError_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_GetError_cfunc(vi, error_code, buffer_size, description)

    def niDMM_GetExtCalRecommendedInterval(self, vi, months):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetExtCalRecommendedInterval_cfunc is None:
                self.niDMM_GetExtCalRecommendedInterval_cfunc = self._get_library_function('niDMM_GetExtCalRecommendedInterval')
                self.niDMM_GetExtCalRecommendedInterval_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDMM_GetExtCalRecommendedInterval_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_GetExtCalRecommendedInterval_cfunc(vi, months)

    def niDMM_GetLastCalTemp(self, vi, cal_type, temperature):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetLastCalTemp_cfunc is None:
                self.niDMM_GetLastCalTemp_cfunc = self._get_library_function('niDMM_GetLastCalTemp')
                self.niDMM_GetLastCalTemp_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDMM_GetLastCalTemp_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_GetLastCalTemp_cfunc(vi, cal_type, temperature)

    def niDMM_GetSelfCalSupported(self, vi, self_cal_supported):  # noqa: N802
        with self._func_lock:
            if self.niDMM_GetSelfCalSupported_cfunc is None:
                self.niDMM_GetSelfCalSupported_cfunc = self._get_library_function('niDMM_GetSelfCalSupported')
                self.niDMM_GetSelfCalSupported_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDMM_GetSelfCalSupported_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_GetSelfCalSupported_cfunc(vi, self_cal_supported)

    def niDMM_ImportAttributeConfigurationBuffer(self, vi, size, configuration):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ImportAttributeConfigurationBuffer_cfunc is None:
                self.niDMM_ImportAttributeConfigurationBuffer_cfunc = self._get_library_function('niDMM_ImportAttributeConfigurationBuffer')
                self.niDMM_ImportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niDMM_ImportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ImportAttributeConfigurationBuffer_cfunc(vi, size, configuration)

    def niDMM_ImportAttributeConfigurationFile(self, vi, file_path):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ImportAttributeConfigurationFile_cfunc is None:
                self.niDMM_ImportAttributeConfigurationFile_cfunc = self._get_library_function('niDMM_ImportAttributeConfigurationFile')
                self.niDMM_ImportAttributeConfigurationFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDMM_ImportAttributeConfigurationFile_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ImportAttributeConfigurationFile_cfunc(vi, file_path)

    def niDMM_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_InitWithOptions_cfunc is None:
                self.niDMM_InitWithOptions_cfunc = self._get_library_function('niDMM_InitWithOptions')
                self.niDMM_InitWithOptions_cfunc.argtypes = [ctypes.POINTER(ViChar), ViBoolean, ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niDMM_InitWithOptions_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_InitWithOptions_cfunc(resource_name, id_query, reset_device, option_string, vi)

    def niDMM_Initiate(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_Initiate_cfunc is None:
                self.niDMM_Initiate_cfunc = self._get_library_function('niDMM_Initiate')
                self.niDMM_Initiate_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDMM_Initiate_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_Initiate_cfunc(vi)

    def niDMM_LockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niDMM_LockSession_cfunc is None:
                self.niDMM_LockSession_cfunc = self._get_library_function('niDMM_LockSession')
                self.niDMM_LockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDMM_LockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_LockSession_cfunc(vi, caller_has_lock)

    def niDMM_PerformOpenCableComp(self, vi, conductance, susceptance):  # noqa: N802
        with self._func_lock:
            if self.niDMM_PerformOpenCableComp_cfunc is None:
                self.niDMM_PerformOpenCableComp_cfunc = self._get_library_function('niDMM_PerformOpenCableComp')
                self.niDMM_PerformOpenCableComp_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDMM_PerformOpenCableComp_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_PerformOpenCableComp_cfunc(vi, conductance, susceptance)

    def niDMM_PerformShortCableComp(self, vi, resistance, reactance):  # noqa: N802
        with self._func_lock:
            if self.niDMM_PerformShortCableComp_cfunc is None:
                self.niDMM_PerformShortCableComp_cfunc = self._get_library_function('niDMM_PerformShortCableComp')
                self.niDMM_PerformShortCableComp_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDMM_PerformShortCableComp_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_PerformShortCableComp_cfunc(vi, resistance, reactance)

    def niDMM_Read(self, vi, maximum_time, reading):  # noqa: N802
        with self._func_lock:
            if self.niDMM_Read_cfunc is None:
                self.niDMM_Read_cfunc = self._get_library_function('niDMM_Read')
                self.niDMM_Read_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDMM_Read_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_Read_cfunc(vi, maximum_time, reading)

    def niDMM_ReadMultiPoint(self, vi, maximum_time, array_size, reading_array, actual_number_of_points):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ReadMultiPoint_cfunc is None:
                self.niDMM_ReadMultiPoint_cfunc = self._get_library_function('niDMM_ReadMultiPoint')
                self.niDMM_ReadMultiPoint_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDMM_ReadMultiPoint_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ReadMultiPoint_cfunc(vi, maximum_time, array_size, reading_array, actual_number_of_points)

    def niDMM_ReadStatus(self, vi, acquisition_backlog, acquisition_status):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ReadStatus_cfunc is None:
                self.niDMM_ReadStatus_cfunc = self._get_library_function('niDMM_ReadStatus')
                self.niDMM_ReadStatus_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt16)]  # noqa: F405
                self.niDMM_ReadStatus_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ReadStatus_cfunc(vi, acquisition_backlog, acquisition_status)

    def niDMM_ReadWaveform(self, vi, maximum_time, array_size, waveform_array, actual_number_of_points):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ReadWaveform_cfunc is None:
                self.niDMM_ReadWaveform_cfunc = self._get_library_function('niDMM_ReadWaveform')
                self.niDMM_ReadWaveform_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDMM_ReadWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ReadWaveform_cfunc(vi, maximum_time, array_size, waveform_array, actual_number_of_points)

    def niDMM_ResetWithDefaults(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_ResetWithDefaults_cfunc is None:
                self.niDMM_ResetWithDefaults_cfunc = self._get_library_function('niDMM_ResetWithDefaults')
                self.niDMM_ResetWithDefaults_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDMM_ResetWithDefaults_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_ResetWithDefaults_cfunc(vi)

    def niDMM_SelfCal(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_SelfCal_cfunc is None:
                self.niDMM_SelfCal_cfunc = self._get_library_function('niDMM_SelfCal')
                self.niDMM_SelfCal_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDMM_SelfCal_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_SelfCal_cfunc(vi)

    def niDMM_SendSoftwareTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_SendSoftwareTrigger_cfunc is None:
                self.niDMM_SendSoftwareTrigger_cfunc = self._get_library_function('niDMM_SendSoftwareTrigger')
                self.niDMM_SendSoftwareTrigger_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDMM_SendSoftwareTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_SendSoftwareTrigger_cfunc(vi)

    def niDMM_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDMM_SetAttributeViBoolean_cfunc is None:
                self.niDMM_SetAttributeViBoolean_cfunc = self._get_library_function('niDMM_SetAttributeViBoolean')
                self.niDMM_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niDMM_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_SetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDMM_SetAttributeViInt32_cfunc is None:
                self.niDMM_SetAttributeViInt32_cfunc = self._get_library_function('niDMM_SetAttributeViInt32')
                self.niDMM_SetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niDMM_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_SetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDMM_SetAttributeViReal64_cfunc is None:
                self.niDMM_SetAttributeViReal64_cfunc = self._get_library_function('niDMM_SetAttributeViReal64')
                self.niDMM_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niDMM_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_SetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDMM_SetAttributeViString_cfunc is None:
                self.niDMM_SetAttributeViString_cfunc = self._get_library_function('niDMM_SetAttributeViString')
                self.niDMM_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDMM_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_SetAttributeViString_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDMM_SetRuntimeEnvironment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        with self._func_lock:
            if self.niDMM_SetRuntimeEnvironment_cfunc is None:
                self.niDMM_SetRuntimeEnvironment_cfunc = self._get_library_function('niDMM_SetRuntimeEnvironment')
                self.niDMM_SetRuntimeEnvironment_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDMM_SetRuntimeEnvironment_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_SetRuntimeEnvironment_cfunc(environment, environment_version, reserved1, reserved2)

    def niDMM_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niDMM_UnlockSession_cfunc is None:
                self.niDMM_UnlockSession_cfunc = self._get_library_function('niDMM_UnlockSession')
                self.niDMM_UnlockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDMM_UnlockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_UnlockSession_cfunc(vi, caller_has_lock)

    def niDMM_close(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_close_cfunc is None:
                self.niDMM_close_cfunc = self._get_library_function('niDMM_close')
                self.niDMM_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDMM_close_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_close_cfunc(vi)

    def niDMM_error_message(self, vi, error_code, error_message):  # noqa: N802
        with self._func_lock:
            if self.niDMM_error_message_cfunc is None:
                self.niDMM_error_message_cfunc = self._get_library_function('niDMM_error_message')
                self.niDMM_error_message_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDMM_error_message_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_error_message_cfunc(vi, error_code, error_message)

    def niDMM_reset(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDMM_reset_cfunc is None:
                self.niDMM_reset_cfunc = self._get_library_function('niDMM_reset')
                self.niDMM_reset_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDMM_reset_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_reset_cfunc(vi)

    def niDMM_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        with self._func_lock:
            if self.niDMM_self_test_cfunc is None:
                self.niDMM_self_test_cfunc = self._get_library_function('niDMM_self_test')
                self.niDMM_self_test_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDMM_self_test_cfunc.restype = ViStatus  # noqa: F405
        return self.niDMM_self_test_cfunc(vi, self_test_result, self_test_message)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidmm/nidmm/_library_interpreter.py sha256=413bba1fdbe08c9f3db59da40d0f526d0b219dfa886486739e959609a4fd08b0 bytes=36044 -->
## FILE: generated/nidmm/nidmm/_library_interpreter.py

- repository: `ni/nimi-python`
- source_path: `generated/nidmm/nidmm/_library_interpreter.py`
- sha256: `413bba1fdbe08c9f3db59da40d0f526d0b219dfa886486739e959609a4fd08b0`
- bytes: 36044

````python
# -*- coding: utf-8 -*-
# This file was generated

import array
import ctypes
import hightime  # noqa: F401
import platform

import nidmm._library_singleton as _library_singleton
import nidmm._visatype as _visatype
import nidmm.enums as enums  # noqa: F401
import nidmm.errors as errors


_was_runtime_environment_set = None


# Helper functions for creating ctypes needed for calling into the driver DLL
def _get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None):
    if isinstance(value, array.array):
        assert library_type is not None, 'library_type is required for array.array'
        addr, _ = value.buffer_info()
        return ctypes.cast(addr, ctypes.POINTER(library_type))
    elif str(type(value)).find("'numpy.ndarray'") != -1:
        import numpy
        return numpy.ctypeslib.as_ctypes(value)
    elif isinstance(value, bytes):
        return ctypes.cast(value, ctypes.POINTER(library_type))
    elif isinstance(value, list):
        assert library_type is not None, 'library_type is required for list'
        return (library_type * len(value))(*value)
    else:
        if library_type is not None and size is not None:
            return (library_type * size)()
        else:
            return None


def _convert_to_array(value, array_type):
    if value is not None:
        if isinstance(value, array.array):
            value_array = value
        else:
            value_array = array.array(array_type, value)
    else:
        value_array = None

    return value_array


class LibraryInterpreter(object):
    '''Library C<->Python interpreter.

    This class is responsible for interpreting the Library's C API. It is responsible for:
    * Converting ctypes to native Python types.
    * Dealing with string encoding.
    * Allocating memory.
    * Converting errors returned by Library into Python exceptions.
    '''

    def __init__(self, encoding):
        self._encoding = encoding
        self._library = _library_singleton.get()
        global _was_runtime_environment_set
        if _was_runtime_environment_set is None:
            try:
                runtime_env = platform.python_implementation()
                version = platform.python_version()
                self.set_runtime_environment(
                    runtime_env,
                    version,
                    '',
                    ''
                )
            except errors.DriverTooOldError:
                pass
            finally:
                _was_runtime_environment_set = True
        # Initialize _vi to 0 for now.
        # Session will directly update it once the driver runtime init function has been called and
        # we have a valid session handle.
        self.set_session_handle()

    def set_session_handle(self, value=0):
        self._vi = value

    def get_session_handle(self):
        return self._vi

    def get_error_description(self, error_code):
        '''get_error_description

        Returns the error description.
        '''
        try:
            returned_error_code, error_string = self.get_error()
            if returned_error_code == error_code:
                return error_string
        except errors.Error:
            pass

        try:
            # get_error reads the session's error queue, which may have been overwritten,
            # causing it to return a mismatched error code. error_message takes the error
            # code directly as a parameter and looks up its description without reading the
            # queue, it will return the description for the specific error code.
            # Use error_message in current session before the handle reset in the next block.

            error_string = self.error_message(error_code)
            return error_string
        except errors.Error:
            pass

        save_vi = self.get_session_handle()
        try:
            # It is expected for get_error to raise when the session is invalid
            # (IVI spec requires GetError to fail).
            # Use error_message instead. It doesn't require a session.

            self.set_session_handle()
            error_string = self.error_message(error_code)
            return error_string
        except errors.Error:
            pass
        finally:
            self.set_session_handle(save_vi)
        return "Failed to retrieve error description."

    def abort(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDMM_Abort(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_measurement_absolute(self, measurement_function, range, resolution_absolute):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        measurement_function_ctype = _visatype.ViInt32(measurement_function.value)  # case S130
        range_ctype = _visatype.ViReal64(range)  # case S150
        resolution_absolute_ctype = _visatype.ViReal64(resolution_absolute)  # case S150
        error_code = self._library.niDMM_ConfigureMeasurementAbsolute(vi_ctype, measurement_function_ctype, range_ctype, resolution_absolute_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_measurement_digits(self, measurement_function, range, resolution_digits):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        measurement_function_ctype = _visatype.ViInt32(measurement_function.value)  # case S130
        range_ctype = _visatype.ViReal64(range)  # case S150
        resolution_digits_ctype = _visatype.ViReal64(resolution_digits)  # case S150
        error_code = self._library.niDMM_ConfigureMeasurementDigits(vi_ctype, measurement_function_ctype, range_ctype, resolution_digits_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_multi_point(self, trigger_count, sample_count, sample_trigger, sample_interval):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_count_ctype = _visatype.ViInt32(trigger_count)  # case S150
        sample_count_ctype = _visatype.ViInt32(sample_count)  # case S150
        sample_trigger_ctype = _visatype.ViInt32(sample_trigger.value)  # case S130
        sample_interval_ctype = _visatype.ViReal64(sample_interval)  # case S150
        error_code = self._library.niDMM_ConfigureMultiPoint(vi_ctype, trigger_count_ctype, sample_count_ctype, sample_trigger_ctype, sample_interval_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_rtd_custom(self, rtd_a, rtd_b, rtd_c):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        rtd_a_ctype = _visatype.ViReal64(rtd_a)  # case S150
        rtd_b_ctype = _visatype.ViReal64(rtd_b)  # case S150
        rtd_c_ctype = _visatype.ViReal64(rtd_c)  # case S150
        error_code = self._library.niDMM_ConfigureRTDCustom(vi_ctype, rtd_a_ctype, rtd_b_ctype, rtd_c_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_rtd_type(self, rtd_type, rtd_resistance):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        rtd_type_ctype = _visatype.ViInt32(rtd_type.value)  # case S130
        rtd_resistance_ctype = _visatype.ViReal64(rtd_resistance)  # case S150
        error_code = self._library.niDMM_ConfigureRTDType(vi_ctype, rtd_type_ctype, rtd_resistance_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_thermistor_custom(self, thermistor_a, thermistor_b, thermistor_c):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        thermistor_a_ctype = _visatype.ViReal64(thermistor_a)  # case S150
        thermistor_b_ctype = _visatype.ViReal64(thermistor_b)  # case S150
        thermistor_c_ctype = _visatype.ViReal64(thermistor_c)  # case S150
        error_code = self._library.niDMM_ConfigureThermistorCustom(vi_ctype, thermistor_a_ctype, thermistor_b_ctype, thermistor_c_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_thermocouple(self, thermocouple_type, reference_junction_type):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        thermocouple_type_ctype = _visatype.ViInt32(thermocouple_type.value)  # case S130
        reference_junction_type_ctype = _visatype.ViInt32(reference_junction_type.value)  # case S130
        error_code = self._library.niDMM_ConfigureThermocouple(vi_ctype, thermocouple_type_ctype, reference_junction_type_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger(self, trigger_source, trigger_delay):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_source_ctype = _visatype.ViInt32(trigger_source.value)  # case S130
        trigger_delay_ctype = _visatype.ViReal64(trigger_delay)  # case S150
        error_code = self._library.niDMM_ConfigureTrigger(vi_ctype, trigger_source_ctype, trigger_delay_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_waveform_acquisition(self, measurement_function, range, rate, waveform_points):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        measurement_function_ctype = _visatype.ViInt32(measurement_function.value)  # case S130
        range_ctype = _visatype.ViReal64(range)  # case S150
        rate_ctype = _visatype.ViReal64(rate)  # case S150
        waveform_points_ctype = _visatype.ViInt32(waveform_points)  # case S150
        error_code = self._library.niDMM_ConfigureWaveformAcquisition(vi_ctype, measurement_function_ctype, range_ctype, rate_ctype, waveform_points_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDMM_Disable(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def export_attribute_configuration_buffer(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        size_ctype = _visatype.ViInt32()  # case S170
        configuration_ctype = None  # case B580
        error_code = self._library.niDMM_ExportAttributeConfigurationBuffer(vi_ctype, size_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        size_ctype = _visatype.ViInt32(error_code)  # case S180
        configuration_size = size_ctype.value  # case B590
        configuration_array = array.array("b", [0]) * configuration_size  # case B590
        configuration_ctype = _get_ctypes_pointer_for_buffer(value=configuration_array, library_type=_visatype.ViInt8)  # case B590
        error_code = self._library.niDMM_ExportAttributeConfigurationBuffer(vi_ctype, size_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return configuration_array

    def export_attribute_configuration_file(self, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDMM_ExportAttributeConfigurationFile(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def fetch(self, maximum_time):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_time_ctype = _visatype.ViInt32(maximum_time)  # case S150
        reading_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDMM_Fetch(vi_ctype, maximum_time_ctype, None if reading_ctype is None else (ctypes.pointer(reading_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(reading_ctype.value)

    def fetch_multi_point(self, maximum_time, array_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_time_ctype = _visatype.ViInt32(maximum_time)  # case S150
        array_size_ctype = _visatype.ViInt32(array_size)  # case S210
        reading_array_size = array_size  # case B600
        reading_array_array = array.array("d", [0]) * reading_array_size  # case B600
        reading_array_ctype = _get_ctypes_pointer_for_buffer(value=reading_array_array, library_type=_visatype.ViReal64)  # case B600
        actual_number_of_points_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDMM_FetchMultiPoint(vi_ctype, maximum_time_ctype, array_size_ctype, reading_array_ctype, None if actual_number_of_points_ctype is None else (ctypes.pointer(actual_number_of_points_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return reading_array_array

    def fetch_waveform(self, maximum_time, array_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_time_ctype = _visatype.ViInt32(maximum_time)  # case S150
        array_size_ctype = _visatype.ViInt32(array_size)  # case S210
        waveform_array_size = array_size  # case B600
        waveform_array_array = array.array("d", [0]) * waveform_array_size  # case B600
        waveform_array_ctype = _get_ctypes_pointer_for_buffer(value=waveform_array_array, library_type=_visatype.ViReal64)  # case B600
        actual_number_of_points_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDMM_FetchWaveform(vi_ctype, maximum_time_ctype, array_size_ctype, waveform_array_ctype, None if actual_number_of_points_ctype is None else (ctypes.pointer(actual_number_of_points_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return waveform_array_array

    def fetch_waveform_into(self, waveform_array, maximum_time):  # noqa: N802
        array_size = len(waveform_array)
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_time_ctype = _visatype.ViInt32(maximum_time)  # case S150
        array_size_ctype = _visatype.ViInt32(array_size)  # case S210
        waveform_array_ctype = _get_ctypes_pointer_for_buffer(value=waveform_array)  # case B510
        actual_number_of_points_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDMM_FetchWaveform(vi_ctype, maximum_time_ctype, array_size_ctype, waveform_array_ctype, None if actual_number_of_points_ctype is None else (ctypes.pointer(actual_number_of_points_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def get_attribute_vi_boolean(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDMM_GetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(attribute_value_ctype.value)

    def get_attribute_vi_int32(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDMM_GetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def get_attribute_vi_real64(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDMM_GetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(attribute_value_ctype.value)

    def get_attribute_vi_string(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        attribute_value_ctype = None  # case C050
        error_code = self._library.niDMM_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        attribute_value_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDMM_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode(self._encoding)

    def get_cal_date_and_time(self, cal_type):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        cal_type_ctype = _visatype.ViInt32(cal_type)  # case S150
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        year_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDMM_GetCalDateAndTime(vi_ctype, cal_type_ctype, None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if year_ctype is None else (ctypes.pointer(year_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(month_ctype.value), int(day_ctype.value), int(year_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_dev_temp(self, options):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        options_ctype = ctypes.create_string_buffer(options.encode(self._encoding))  # case C020
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDMM_GetDevTemp(vi_ctype, options_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def get_error(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus()  # case S220
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        description_ctype = None  # case C050
        error_code = self._library.niDMM_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        description_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDMM_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), description_ctype.value.decode(self._encoding)

    def get_ext_cal_recommended_interval(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        months_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDMM_GetExtCalRecommendedInterval(vi_ctype, None if months_ctype is None else (ctypes.pointer(months_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(months_ctype.value)

    def get_last_cal_temp(self, cal_type):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        cal_type_ctype = _visatype.ViInt32(cal_type)  # case S150
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDMM_GetLastCalTemp(vi_ctype, cal_type_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def get_self_cal_supported(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        self_cal_supported_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDMM_GetSelfCalSupported(vi_ctype, None if self_cal_supported_ctype is None else (ctypes.pointer(self_cal_supported_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(self_cal_supported_ctype.value)

    def import_attribute_configuration_buffer(self, configuration):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        size_ctype = _visatype.ViInt32(0 if configuration is None else len(configuration))  # case S160
        configuration_ctype = _get_ctypes_pointer_for_buffer(value=configuration, library_type=_visatype.ViInt8)  # case B550
        error_code = self._library.niDMM_ImportAttributeConfigurationBuffer(vi_ctype, size_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def import_attribute_configuration_file(self, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDMM_ImportAttributeConfigurationFile(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def init_with_options(self, resource_name, id_query, reset_device, option_string):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        id_query_ctype = _visatype.ViBoolean(id_query)  # case S150
        reset_device_ctype = _visatype.ViBoolean(reset_device)  # case S150
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case C020
        vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niDMM_InitWithOptions(resource_name_ctype, id_query_ctype, reset_device_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        self._close_on_exit = True
        return int(vi_ctype.value)

    def initiate(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDMM_Initiate(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def lock(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDMM_LockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def perform_open_cable_comp(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        conductance_ctype = _visatype.ViReal64()  # case S220
        susceptance_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDMM_PerformOpenCableComp(vi_ctype, None if conductance_ctype is None else (ctypes.pointer(conductance_ctype)), None if susceptance_ctype is None else (ctypes.pointer(susceptance_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(conductance_ctype.value), float(susceptance_ctype.value)

    def perform_short_cable_comp(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        resistance_ctype = _visatype.ViReal64()  # case S220
        reactance_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDMM_PerformShortCableComp(vi_ctype, None if resistance_ctype is None else (ctypes.pointer(resistance_ctype)), None if reactance_ctype is None else (ctypes.pointer(reactance_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(resistance_ctype.value), float(reactance_ctype.value)

    def read(self, maximum_time):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_time_ctype = _visatype.ViInt32(maximum_time)  # case S150
        reading_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDMM_Read(vi_ctype, maximum_time_ctype, None if reading_ctype is None else (ctypes.pointer(reading_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(reading_ctype.value)

    def read_multi_point(self, maximum_time, array_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_time_ctype = _visatype.ViInt32(maximum_time)  # case S150
        array_size_ctype = _visatype.ViInt32(array_size)  # case S210
        reading_array_size = array_size  # case B600
        reading_array_array = array.array("d", [0]) * reading_array_size  # case B600
        reading_array_ctype = _get_ctypes_pointer_for_buffer(value=reading_array_array, library_type=_visatype.ViReal64)  # case B600
        actual_number_of_points_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDMM_ReadMultiPoint(vi_ctype, maximum_time_ctype, array_size_ctype, reading_array_ctype, None if actual_number_of_points_ctype is None else (ctypes.pointer(actual_number_of_points_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return reading_array_array

    def read_status(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        acquisition_backlog_ctype = _visatype.ViInt32()  # case S220
        acquisition_status_ctype = _visatype.ViInt16()  # case S220
        error_code = self._library.niDMM_ReadStatus(vi_ctype, None if acquisition_backlog_ctype is None else (ctypes.pointer(acquisition_backlog_ctype)), None if acquisition_status_ctype is None else (ctypes.pointer(acquisition_status_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(acquisition_backlog_ctype.value), enums.AcquisitionStatus(acquisition_status_ctype.value)

    def read_waveform(self, maximum_time, array_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_time_ctype = _visatype.ViInt32(maximum_time)  # case S150
        array_size_ctype = _visatype.ViInt32(array_size)  # case S210
        waveform_array_size = array_size  # case B600
        waveform_array_array = array.array("d", [0]) * waveform_array_size  # case B600
        waveform_array_ctype = _get_ctypes_pointer_for_buffer(value=waveform_array_array, library_type=_visatype.ViReal64)  # case B600
        actual_number_of_points_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDMM_ReadWaveform(vi_ctype, maximum_time_ctype, array_size_ctype, waveform_array_ctype, None if actual_number_of_points_ctype is None else (ctypes.pointer(actual_number_of_points_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return waveform_array_array

    def reset_with_defaults(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDMM_ResetWithDefaults(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_cal(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDMM_SelfCal(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def send_software_trigger(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDMM_SendSoftwareTrigger(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_boolean(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean(attribute_value)  # case S150
        error_code = self._library.niDMM_SetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_int32(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32(attribute_value)  # case S150
        error_code = self._library.niDMM_SetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_real64(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64(attribute_value)  # case S150
        error_code = self._library.niDMM_SetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_string(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = ctypes.create_string_buffer(attribute_value.encode(self._encoding))  # case C020
        error_code = self._library.niDMM_SetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_runtime_environment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        environment_ctype = ctypes.create_string_buffer(environment.encode(self._encoding))  # case C020
        environment_version_ctype = ctypes.create_string_buffer(environment_version.encode(self._encoding))  # case C020
        reserved1_ctype = ctypes.create_string_buffer(reserved1.encode(self._encoding))  # case C020
        reserved2_ctype = ctypes.create_string_buffer(reserved2.encode(self._encoding))  # case C020
        error_code = self._library.niDMM_SetRuntimeEnvironment(environment_ctype, environment_version_ctype, reserved1_ctype, reserved2_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDMM_UnlockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def close(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDMM_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def error_message(self, error_code):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niDMM_error_message(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)

    def reset(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDMM_reset(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_test(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        self_test_result_ctype = _visatype.ViInt16()  # case S220
        self_test_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niDMM_self_test(vi_ctype, None if self_test_result_ctype is None else (ctypes.pointer(self_test_result_ctype)), self_test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(self._encoding)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidmm/nidmm/_library_singleton.py sha256=8d8c20a46dce098a8120c7c43e52b651e948249ebb54c8b59561e875a003a134 bytes=1687 -->
## FILE: generated/nidmm/nidmm/_library_singleton.py

- repository: `ni/nimi-python`
- source_path: `generated/nidmm/nidmm/_library_singleton.py`
- sha256: `8d8c20a46dce098a8120c7c43e52b651e948249ebb54c8b59561e875a003a134`
- bytes: 1687

````python
# -*- coding: utf-8 -*-
# This file was generated

import platform

import ctypes
import ctypes.util
import nidmm._library as _library
import nidmm.errors as errors
import threading


_instance = None
_instance_lock = threading.Lock()
_library_info = {'Linux': {'64bit': {'name': 'nidmm', 'type': 'cdll'}},
                 'Windows': {'32bit': {'name': 'nidmm_32.dll', 'type': 'windll'},
                             '64bit': {'name': 'nidmm_64.dll', 'type': 'cdll'}}}


def _get_library_name():
    try:
        lib_name = ctypes.util.find_library(_library_info[platform.system()][platform.architecture()[0]]['name'])  # We find and return full path to the DLL
        if lib_name is None:
            raise errors.DriverNotInstalledError()
        return lib_name
    except KeyError:
        raise errors.UnsupportedConfigurationError


def _get_library_type():
    try:
        return _library_info[platform.system()][platform.architecture()[0]]['type']
    except KeyError:
        raise errors.UnsupportedConfigurationError


def get():
    '''get

    Returns the library.Library singleton for nidmm.
    '''
    global _instance

    with _instance_lock:
        if _instance is None:
            try:
                library_type = _get_library_type()
                if library_type == 'windll':
                    ctypes_library = ctypes.WinDLL(_get_library_name())
                else:
                    assert library_type == 'cdll'
                    ctypes_library = ctypes.CDLL(_get_library_name())
            except OSError:
                raise errors.DriverNotInstalledError()
            _instance = _library.Library(ctypes_library)
        return _instance
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidmm/nidmm/_visatype.py sha256=ac436ae1613f5e807cd16d2df951c7a502f37996234e4d324c5412b3633e1c92 bytes=662 -->
## FILE: generated/nidmm/nidmm/_visatype.py

- repository: `ni/nimi-python`
- source_path: `generated/nidmm/nidmm/_visatype.py`
- sha256: `ac436ae1613f5e807cd16d2df951c7a502f37996234e4d324c5412b3633e1c92`
- bytes: 662

````python
import ctypes


'''Definitions of the VISA types used by the C API of the driver runtime.
These are aliased directly to ctypes types so can be used directly to call into the library.
'''


ViChar = ctypes.c_char
ViInt8 = ctypes.c_int8
ViUInt8 = ctypes.c_uint8
ViInt16 = ctypes.c_int16
ViUInt16 = ctypes.c_uint16
ViInt32 = ctypes.c_int32
ViUInt32 = ctypes.c_uint32
ViInt64 = ctypes.c_int64
ViUInt64 = ctypes.c_uint64
ViString = ctypes.c_char_p
ViReal32 = ctypes.c_float
ViReal64 = ctypes.c_double

# Types that are based on other visatypes
ViBoolean = ViUInt16
ViStatus = ViInt32
ViSession = ViUInt32
ViAttr = ViUInt32
ViConstString = ViString
ViRsrc = ViString
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidmm/nidmm/enums.py sha256=bbf1dc51ff4fe7214f0e776cc09b08e20caa72f49fc64365ea60667ea824d836 bytes=8301 -->
## FILE: generated/nidmm/nidmm/enums.py

- repository: `ni/nimi-python`
- source_path: `generated/nidmm/nidmm/enums.py`
- sha256: `bbf1dc51ff4fe7214f0e776cc09b08e20caa72f49fc64365ea60667ea824d836`
- bytes: 8301

````python
# -*- coding: utf-8 -*-
# This file was generated

from enum import Enum


class ADCCalibration(Enum):
    AUTO = -1
    r'''
    The DMM enables or disables ADC calibration for you.
    '''
    OFF = 0
    r'''
    The DMM does not compensate for changes to the gain.
    '''
    ON = 1
    r'''
    The DMM measures an internal reference to calculate the correct gain for the  measurement.
    '''


class AcquisitionStatus(Enum):
    RUNNING = 0
    r'''
    Running
    '''
    FINISHED_WITH_BACKLOG = 1
    r'''
    Finished with **Backlog**
    '''
    FINISHED_WITH_NO_BACKLOG = 2
    r'''
    Finished with no **Backlog**
    '''
    PAUSED = 3
    r'''
    Paused
    '''
    NO_ACQUISITION_IN_PROGRESS = 4
    r'''
    No acquisition in progress
    '''


class ApertureTimeUnits(Enum):
    SECONDS = 0
    r'''
    Seconds
    '''
    POWER_LINE_CYCLES = 1
    r'''
    Powerline Cycles
    '''


class AutoZero(Enum):
    AUTO = -1
    r'''
    The drivers chooses the AutoZero setting based on the configured method  and resolution.
    '''
    OFF = 0
    r'''
    Disables AutoZero.
    '''
    ON = 1
    r'''
    The DMM internally disconnects the input signal following each measurement  and takes a zero reading. It then subtracts the zero reading from the  preceding reading.
    '''
    ONCE = 2
    r'''
    The DMM internally disconnects the input signal for the first measurement  and takes a zero reading. It then subtracts the zero reading from the first  reading and the following readings.
    '''


class CableCompensationType(Enum):
    NONE = 0
    r'''
    No Cable Compensation
    '''
    OPEN = 1
    r'''
    Open Cable Compensation
    '''
    SHORT = 2
    r'''
    Short Cable Compensation
    '''
    OPEN_AND_SHORT = 3
    r'''
    Open and Short Cable Compensation
    '''


class DCNoiseRejection(Enum):
    AUTO = -1
    r'''
    The driver chooses the DC noise rejection setting based on the configured  method and resolution.
    '''
    NORMAL = 0
    r'''
    NI-DMM weighs all samples equally.
    '''
    SECOND_ORDER = 1
    r'''
    NI-DMM weighs the samples taken in the middle of the aperture time more than  samples taken at the beginning and the end of the measurement using a  triangular weighing method.
    '''
    HIGH_ORDER = 2
    r'''
    NI-DMM weighs the samples taken in the middle of the aperture time more than  samples taken at the beginning and the end of the measurement using a  bell-curve weighing method.
    '''


class Function(Enum):
    DC_VOLTS = 1
    r'''
    DC Voltage
    '''
    AC_VOLTS = 2
    r'''
    AC Voltage
    '''
    DC_CURRENT = 3
    r'''
    DC Current
    '''
    AC_CURRENT = 4
    r'''
    AC Current
    '''
    TWO_WIRE_RES = 5
    r'''
    2-Wire Resistance
    '''
    FOUR_WIRE_RES = 101
    r'''
    4-Wire Resistance
    '''
    FREQ = 104
    r'''
    Frequency
    '''
    PERIOD = 105
    r'''
    Period
    '''
    TEMPERATURE = 108
    r'''
    NI 4065, NI 4070/4071/4072, and NI 4080/4081/4182 supported.
    '''
    AC_VOLTS_DC_COUPLED = 1001
    r'''
    AC Voltage with DC Coupling
    '''
    DIODE = 1002
    r'''
    Diode
    '''
    WAVEFORM_VOLTAGE = 1003
    r'''
    Waveform voltage
    '''
    WAVEFORM_CURRENT = 1004
    r'''
    Waveform current
    '''
    CAPACITANCE = 1005
    r'''
    Capacitance
    '''
    INDUCTANCE = 1006
    r'''
    Inductance
    '''


class LCCalculationModel(Enum):
    AUTO = -1
    r'''
    NI-DMM chooses the algorithm based on method and range
    '''
    SERIES = 0
    r'''
    NI-DMM uses the series impedance model to calculate capacitance and inductance
    '''
    PARALLEL = 1
    r'''
    NI-DMM uses the parallel admittance model to calculate capacitance and inductance
    '''


class MeasurementCompleteDest(Enum):
    NONE = -1
    r'''
    No Trigger
    '''
    EXTERNAL = 2
    r'''
    AUX I/O Connector
    '''
    PXI_TRIG0 = 111
    r'''
    PXI Trigger Line 0
    '''
    PXI_TRIG1 = 112
    r'''
    PXI Trigger Line 1
    '''
    PXI_TRIG2 = 113
    r'''
    PXI Trigger Line 2
    '''
    PXI_TRIG3 = 114
    r'''
    PXI Trigger Line 3
    '''
    PXI_TRIG4 = 115
    r'''
    PXI Trigger Line 4
    '''
    PXI_TRIG5 = 116
    r'''
    PXI Trigger Line 5
    '''
    PXI_TRIG6 = 117
    r'''
    PXI Trigger Line 6
    '''
    PXI_TRIG7 = 118
    r'''
    PXI Trigger Line 7
    '''
    LBR_TRIG0 = 1003
    r'''
    Internal Trigger Line of a PXI/SCXI Combination Chassis
    '''


class OperationMode(Enum):
    IVIDMM = 0
    r'''
    IviDmm Mode
    '''
    WAVEFORM = 1
    r'''
    Waveform acquisition mode
    '''


class RTDType(Enum):
    CUSTOM = 0
    r'''
    Performs Callendar-Van Dusen RTD scaling with the user-specified A, B,
    and C coefficients.
    '''
    PT3750 = 1
    r'''
    Performs scaling for a Pt 3750 RTD.
    '''
    PT3851 = 2
    r'''
    Performs scaling for a Pt 3851 RTD.
    '''
    PT3911 = 3
    r'''
    Performs scaling for a Pt 3911 RTD.
    '''
    PT3916 = 4
    r'''
    Performs scaling for a Pt 3916 RTD.
    '''
    PT3920 = 5
    r'''
    Performs scaling for a Pt 3920 RTD.
    '''
    PT3928 = 6
    r'''
    Performs scaling for a Pt 3928 RTD.
    '''


class SampleTrigger(Enum):
    IMMEDIATE = 1
    r'''
    No Trigger
    '''
    EXTERNAL = 2
    r'''
    AUX I/O Connector Trigger Line 0
    '''
    SOFTWARE_TRIG = 3
    r'''
    Software Trigger
    '''
    INTERVAL = 10
    r'''
    Interval Trigger
    '''
    PXI_TRIG0 = 111
    r'''
    PXI Trigger Line 0
    '''
    PXI_TRIG1 = 112
    r'''
    PXI Trigger Line 1
    '''
    PXI_TRIG2 = 113
    r'''
    PXI Trigger Line 2
    '''
    PXI_TRIG3 = 114
    r'''
    PXI Trigger Line 3
    '''
    PXI_TRIG4 = 115
    r'''
    PXI Trigger Line 4
    '''
    PXI_TRIG5 = 116
    r'''
    PXI Trigger Line 5
    '''
    PXI_TRIG6 = 117
    r'''
    PXI Trigger Line 6
    '''
    PXI_TRIG7 = 118
    r'''
    PXI Trigger Line 7
    '''
    PXI_STAR = 131
    r'''
    PXI Star Trigger Line
    '''
    AUX_TRIG1 = 1001
    r'''
    AUX I/0 Connector Trigger Line 1
    '''
    LBR_TRIG1 = 1004
    r'''
    Internal Trigger Line of a PXI/SCXI Combination Chassis
    '''


class ThermistorType(Enum):
    CUSTOM = 0
    r'''
    Custom
    '''
    THERMISTOR_44004 = 1
    r'''
    44004
    '''
    THERMISTOR_44006 = 2
    r'''
    44006
    '''
    THERMISTOR_44007 = 3
    r'''
    44007
    '''


class ThermocoupleReferenceJunctionType(Enum):
    FIXED = 2
    r'''
    Thermocouple reference juction is fixed at the user-specified
    temperature.
    '''


class ThermocoupleType(Enum):
    B = 1
    r'''
    Thermocouple type B
    '''
    E = 4
    r'''
    Thermocouple type E
    '''
    J = 6
    r'''
    Thermocouple type J
    '''
    K = 7
    r'''
    Thermocouple type K
    '''
    N = 8
    r'''
    Thermocouple type N
    '''
    R = 9
    r'''
    Thermocouple type R
    '''
    S = 10
    r'''
    Thermocouple type S
    '''
    T = 11
    r'''
    Thermocouple type T
    '''


class TransducerType(Enum):
    THERMOCOUPLE = 1
    r'''
    Thermocouple
    '''
    THERMISTOR = 2
    r'''
    Thermistor
    '''
    TWO_WIRE_RTD = 3
    r'''
    2-wire RTD
    '''
    FOUR_WIRE_RTD = 4
    r'''
    4-wire RTD
    '''


class TriggerSource(Enum):
    IMMEDIATE = 1
    r'''
    No Trigger
    '''
    EXTERNAL = 2
    r'''
    AUX I/O Connector Trigger Line 0
    '''
    SOFTWARE_TRIG = 3
    r'''
    Software Trigger
    '''
    PXI_TRIG0 = 111
    r'''
    PXI Trigger Line 0
    '''
    PXI_TRIG1 = 112
    r'''
    PXI Trigger Line 1
    '''
    PXI_TRIG2 = 113
    r'''
    PXI Trigger Line 2
    '''
    PXI_TRIG3 = 114
    r'''
    PXI Trigger Line 3
    '''
    PXI_TRIG4 = 115
    r'''
    PXI Trigger Line 4
    '''
    PXI_TRIG5 = 116
    r'''
    PXI Trigger Line 5
    '''
    PXI_TRIG6 = 117
    r'''
    PXI Trigger Line 6
    '''
    PXI_TRIG7 = 118
    r'''
    PXI Trigger Line 7
    '''
    PXI_STAR = 131
    r'''
    PXI Star Trigger Line
    '''
    AUX_TRIG1 = 1001
    r'''
    AUX I/O Connector Trigger Line 1
    '''
    LBR_TRIG1 = 1004
    r'''
    Internal Trigger Line of a PXI/SCXI Combination Chassis
    '''


class WaveformCoupling(Enum):
    AC = 0
    r'''
    AC Coupled
    '''
    DC = 1
    r'''
    DC Coupled
    '''
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidmm/nidmm/errors.py sha256=114b6ec464fcddea5a06fa55eb1b8f9588e877e1d1d8380a38f322691ecc757e bytes=4338 -->
## FILE: generated/nidmm/nidmm/errors.py

- repository: `ni/nimi-python`
- source_path: `generated/nidmm/nidmm/errors.py`
- sha256: `114b6ec464fcddea5a06fa55eb1b8f9588e877e1d1d8380a38f322691ecc757e`
- bytes: 4338

````python
# -*- coding: utf-8 -*-
# This file was generated


import platform
import warnings


def _is_success(code):
    return (code == 0)


def _is_error(code):
    return (code < 0)


def _is_warning(code):
    return (code > 0)


class Error(Exception):
    '''Base error class for NI-DMM'''

    def __init__(self, message):
        super(Error, self).__init__(message)


class DriverError(Error):
    '''An error originating from the NI-DMM driver'''

    def __init__(self, code, description):
        assert _is_error(code), "Should not raise Error if code is not fatal."
        self.code = code
        self.description = description
        super(DriverError, self).__init__(str(self.code) + ": " + self.description)


class DriverWarning(Warning):
    '''A warning originating from the NI-DMM driver'''

    def __init__(self, code, description):
        assert _is_warning(code), "Should not create Warning if code is not positive."
        super(DriverWarning, self).__init__('Warning {} occurred.\n\n{}'.format(code, description))


class RpcError(Error):
    '''An error specific to sessions to the NI gRPC Device Server'''

    def __init__(self, rpc_code, description):
        self.rpc_code = rpc_code
        self.description = description
        try:
            import grpc
            rpc_error = str(grpc.StatusCode(self.rpc_code))
        except Exception:
            rpc_error = str(self.rpc_code)
        super(RpcError, self).__init__(rpc_error + ": " + self.description)


class UnsupportedConfigurationError(Error):
    '''An error due to using this module in an usupported platform.'''

    def __init__(self):
        super(UnsupportedConfigurationError, self).__init__('System configuration is unsupported: ' + platform.architecture()[0] + ' ' + platform.system())


class DriverNotInstalledError(Error):
    '''An error due to using this module without the driver runtime installed.'''

    def __init__(self):
        super(DriverNotInstalledError, self).__init__('The NI-DMM runtime could not be loaded. Make sure it is installed and its bitness matches that of your Python interpreter. Please visit http://www.ni.com/downloads/drivers/ to download and install it.')


class DriverTooOldError(Error):
    '''An error due to using this module with an older version of the NI-DMM driver runtime.'''

    def __init__(self):
        super(DriverTooOldError, self).__init__('A function was not found in the NI-DMM runtime. Please visit http://www.ni.com/downloads/drivers/ to download a newer version and install it.')


class DriverTooNewError(Error):
    '''An error due to the NI-DMM driver runtime being too new for this module.'''

    def __init__(self):
        super(DriverTooNewError, self).__init__('The NI-DMM runtime returned an unexpected value. This can occur if it is too new for the nidmm Python module. Upgrade the nidmm Python module.')


class InvalidRepeatedCapabilityError(Error):
    '''An error due to an invalid character in a repeated capability'''

    def __init__(self, invalid_character, invalid_string):
        super(InvalidRepeatedCapabilityError, self).__init__('An invalid character ({}) was found in repeated capability string ({})'.format(invalid_character, invalid_string))


class SelfTestError(Error):
    '''An error due to a failed self-test'''

    def __init__(self, code, msg):
        self.code = code
        self.message = msg
        super(SelfTestError, self).__init__('Self-test failed with code {}: {}'.format(code, msg))


def handle_error(library_interpreter, code, ignore_warnings, is_error_handling):
    '''handle_error

    Helper function for handling errors returned by nidmm.Library.
    It calls back into the LibraryInterpreter to get the corresponding error
    description and raises if necessary.
    '''

    if _is_success(code) or (_is_warning(code) and ignore_warnings):
        return

    if is_error_handling:
        # The caller is in the midst of error handling and an error occurred.
        # Don't try to get the description or we'll start recursing until the stack overflows.
        description = ''
    else:
        description = library_interpreter.get_error_description(code)

    if _is_error(code):
        raise DriverError(code, description)

    assert _is_warning(code)
    warnings.warn(DriverWarning(code, description))
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidmm/nidmm/grpc_session_options.py sha256=dc2aec820ca780669bc9565ea8da694c14d5469b364657a03c59510e6370989f bytes=3450 -->
## FILE: generated/nidmm/nidmm/grpc_session_options.py

- repository: `ni/nimi-python`
- source_path: `generated/nidmm/nidmm/grpc_session_options.py`
- sha256: `dc2aec820ca780669bc9565ea8da694c14d5469b364657a03c59510e6370989f`
- bytes: 3450

````python
# -*- coding: utf-8 -*-
# This file was generated

from enum import IntEnum


# This constant specifies the gRPC package and service used by this API.
# Customers can pass this value to the MeasurementLink discovery service to resolve the server instance that provides this interface.
GRPC_SERVICE_INTERFACE_NAME = 'nidmm_grpc.NiDmm'

# This constant specifies the API license key required by the NI gRPC Device Server that comes with
# MeasurementLink 2023 Q1.
MEASUREMENTLINK_23Q1_NIMI_PYTHON_API_KEY = 'DE10751B-3EE0-44EC-A93B-800E6A3C89E4'


class SessionInitializationBehavior(IntEnum):
    AUTO = 0
    r'''
    The NI gRPC Device Server will attach to an existing session with the specified name if it exists, otherwise the server
    will initialize a new session.

    Note:
    When using the Session as a context manager and the context exits, the behavior depends on what happened when the constructor
    was called. If it resulted in a new session being initialized on the NI gRPC Device Server, then it will automatically close the
    server session. If it instead attached to an existing session, then it will detach from the server session and leave it open.
    '''
    INITIALIZE_SERVER_SESSION = 1
    r'''
    Require the NI gRPC Device Server to initialize a new session with the specified name.

    Note:
    When using the Session as a context manager and the context exits, it will automatically close the
    server session.
    '''
    ATTACH_TO_SERVER_SESSION = 2
    r'''
    Require the NI gRPC Device Server to attach to an existing session with the specified name.

    Note:
    When using the Session as a context manager and the context exits, it will detach from the server session
    and leave it open.
    '''


class GrpcSessionOptions(object):
    '''Collection of options that specifies session behaviors related to gRPC.'''

    def __init__(
        self,
        grpc_channel,
        session_name,
        *,
        api_key=MEASUREMENTLINK_23Q1_NIMI_PYTHON_API_KEY,
        initialization_behavior=SessionInitializationBehavior.AUTO
    ):
        r'''Collection of options that specifies session behaviors related to gRPC.

        Creates and returns an object you can pass to a Session constructor.

        Args:
            grpc_channel (grpc.Channel): Specifies the channel to the NI gRPC Device Server.

            session_name (str): User-specified name that identifies the driver session on the NI gRPC Device
                Server. This is different from the resource name parameter many APIs take as a separate
                parameter. Specifying a name makes it easy to share sessions across multiple gRPC clients.
                You can use an empty string if you want to always initialize a new session on the server.
                To attach to an existing session, you must specify the session name it was initialized with.

            api_key (str): Specifies the API license key required by the NI gRPC Device Server.

            initialization_behavior (enum): Specifies whether it is acceptable to initialize a new
                session or attach to an existing one, or if only one of the behaviors is desired.
                The driver session exists on the NI gRPC Device Server.
        '''
        self.grpc_channel = grpc_channel
        self.session_name = session_name
        self.api_key = api_key
        self.initialization_behavior = initialization_behavior
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidmm/nidmm/nidevice_pb2.py sha256=9a935a95cbe830099345438b27f1460989b073de2e873f43cb394ac0df4ced54 bytes=2009 -->
## FILE: generated/nidmm/nidmm/nidevice_pb2.py

- repository: `ni/nimi-python`
- source_path: `generated/nidmm/nidmm/nidevice_pb2.py`
- sha256: `9a935a95cbe830099345438b27f1460989b073de2e873f43cb394ac0df4ced54`
- bytes: 2009

````python
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nidevice.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0enidevice.proto\x12\rnidevice_grpc\"2\n\x0fNIComplexNumber\x12\x0c\n\x04real\x18\x01 \x01(\x01\x12\x11\n\timaginary\x18\x02 \x01(\x01\"5\n\x12NIComplexNumberF32\x12\x0c\n\x04real\x18\x01 \x01(\x02\x12\x11\n\timaginary\x18\x02 \x01(\x02\"/\n\x0cNIComplexI16\x12\x0c\n\x04real\x18\x01 \x01(\x11\x12\x11\n\timaginary\x18\x02 \x01(\x11\"r\n\x0fSmtSpectrumInfo\x12\x15\n\rspectrum_type\x18\x01 \x01(\r\x12\x11\n\tlinear_db\x18\x02 \x01(\r\x12\x0e\n\x06window\x18\x03 \x01(\r\x12\x13\n\x0bwindow_size\x18\x04 \x01(\x11\x12\x10\n\x08\x66\x66t_size\x18\x05 \x01(\x11\x42\x42\n\x12\x63om.ni.grpc.deviceB\x08NiDeviceP\x01\xaa\x02\x1fNationalInstruments.Grpc.Deviceb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nidevice_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\022com.ni.grpc.deviceB\010NiDeviceP\001\252\002\037NationalInstruments.Grpc.Device'
  _globals['_NICOMPLEXNUMBER']._serialized_start=33
  _globals['_NICOMPLEXNUMBER']._serialized_end=83
  _globals['_NICOMPLEXNUMBERF32']._serialized_start=85
  _globals['_NICOMPLEXNUMBERF32']._serialized_end=138
  _globals['_NICOMPLEXI16']._serialized_start=140
  _globals['_NICOMPLEXI16']._serialized_end=187
  _globals['_SMTSPECTRUMINFO']._serialized_start=189
  _globals['_SMTSPECTRUMINFO']._serialized_end=303
# @@protoc_insertion_point(module_scope)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidmm/nidmm/nidevice_pb2_grpc.py sha256=d686e804f171693117b7d030ec4023f205c70c234c8590f6557aa8702f65fe09 bytes=159 -->
## FILE: generated/nidmm/nidmm/nidevice_pb2_grpc.py

- repository: `ni/nimi-python`
- source_path: `generated/nidmm/nidmm/nidevice_pb2_grpc.py`
- sha256: `d686e804f171693117b7d030ec4023f205c70c234c8590f6557aa8702f65fe09`
- bytes: 159

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidmm/nidmm/nidmm_pb2.py sha256=cafe8f14d8161a272a815e5c66935447be46a2d8b16e6f136ddd4de8c4cb345f bytes=85184 -->
## FILE: generated/nidmm/nidmm/nidmm_pb2.py

- repository: `ni/nimi-python`
- source_path: `generated/nidmm/nidmm/nidmm_pb2.py`
- sha256: `cafe8f14d8161a272a815e5c66935447be46a2d8b16e6f136ddd4de8c4cb345f`
- bytes: 85184

````python
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nidmm.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import session_pb2 as session__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bnidmm.proto\x12\nnidmm_grpc\x1a\rsession.proto\"\xb1\x01\n\x0bInitRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x10\n\x08id_query\x18\x03 \x01(\x08\x12\x14\n\x0creset_device\x18\x04 \x01(\x08\x12M\n\x17initialization_behavior\x18\x05 \x01(\x0e\x32,.nidevice_grpc.SessionInitializationBehavior\"~\n\x0cInitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\"\n\x02vi\x18\x02 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x19\n\rerror_message\x18\x03 \x01(\tB\x02\x18\x01\x12\x1f\n\x17new_session_initialized\x18\x04 \x01(\x08\"\xd3\x01\n\x16InitWithOptionsRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x10\n\x08id_query\x18\x03 \x01(\x08\x12\x14\n\x0creset_device\x18\x04 \x01(\x08\x12\x15\n\roption_string\x18\x05 \x01(\t\x12M\n\x17initialization_behavior\x18\x06 \x01(\x0e\x32,.nidevice_grpc.SessionInitializationBehavior\"\x89\x01\n\x17InitWithOptionsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\"\n\x02vi\x18\x02 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x19\n\rerror_message\x18\x03 \x01(\tB\x02\x18\x01\x12\x1f\n\x17new_session_initialized\x18\x04 \x01(\x08\"2\n\x0c\x43loseRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\x1f\n\rCloseResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"5\n\x0fGetErrorRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"K\n\x10GetErrorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nerror_code\x18\x02 \x01(\x11\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"P\n\x16GetErrorMessageRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x12\n\nerror_code\x18\x02 \x01(\x11\"@\n\x17GetErrorMessageResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t\"7\n\x11\x43learErrorRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"$\n\x12\x43learErrorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"2\n\x0cResetRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\x1f\n\rResetResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"5\n\x0fSelfTestRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"W\n\x10SelfTestResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x18\n\x10self_test_result\x18\x02 \x01(\x11\x12\x19\n\x11self_test_message\x18\x03 \x01(\t\"4\n\x0eSelfCalRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"!\n\x0fSelfCalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\":\n\x14RevisionQueryRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"f\n\x15RevisionQueryResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\"\n\x1ainstrument_driver_revision\x18\x02 \x01(\t\x12\x19\n\x11\x66irmware_revision\x18\x03 \x01(\t\">\n\x18ResetWithDefaultsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"+\n\x19ResetWithDefaultsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"4\n\x0e\x44isableRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"!\n\x0f\x44isableResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"A\n\x1bGetMeasurementPeriodRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\">\n\x1cGetMeasurementPeriodResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0e\n\x06period\x18\x02 \x01(\x01\"\x8e\x02\n\x17\x43onfigureTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x33\n\x0etrigger_source\x18\x02 \x01(\x0e\x32\x19.nidmm_grpc.TriggerSourceH\x00\x12\x1c\n\x12trigger_source_raw\x18\x03 \x01(\x11H\x00\x12\x32\n\rtrigger_delay\x18\x04 \x01(\x0e\x32\x19.nidmm_grpc.TriggerDelaysH\x01\x12\x1b\n\x11trigger_delay_raw\x18\x05 \x01(\x01H\x01\x42\x15\n\x13trigger_source_enumB\x14\n\x12trigger_delay_enum\"*\n\x18\x43onfigureTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x91\x01\n\x0bReadRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12-\n\x0cmaximum_time\x18\x02 \x01(\x0e\x32\x15.nidmm_grpc.TimeLimitH\x00\x12\x1a\n\x10maximum_time_raw\x18\x03 \x01(\x11H\x00\x42\x13\n\x11maximum_time_enum\"/\n\x0cReadResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07reading\x18\x02 \x01(\x01\"\x92\x01\n\x0c\x46\x65tchRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12-\n\x0cmaximum_time\x18\x02 \x01(\x0e\x32\x15.nidmm_grpc.TimeLimitH\x00\x12\x1a\n\x10maximum_time_raw\x18\x03 \x01(\x11H\x00\x42\x13\n\x11maximum_time_enum\"0\n\rFetchResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07reading\x18\x02 \x01(\x01\"2\n\x0c\x41\x62ortRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\x1f\n\rAbortResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"5\n\x0fInitiateRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\"\n\x10InitiateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"S\n\x12IsOverRangeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x19\n\x11measurement_value\x18\x02 \x01(\x01\"<\n\x13IsOverRangeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\ris_over_range\x18\x02 \x01(\x08\"T\n\x13IsUnderRangeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x19\n\x11measurement_value\x18\x02 \x01(\x01\">\n\x14IsUnderRangeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x16\n\x0eis_under_range\x18\x02 \x01(\x08\"\x83\x01\n\x1b\x43onfigureACBandwidthRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x1f\n\x17\x61\x63_minimum_frequency_hz\x18\x02 \x01(\x01\x12\x1f\n\x17\x61\x63_maximum_frequency_hz\x18\x03 \x01(\x01\".\n\x1c\x43onfigureACBandwidthResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xba\x01\n%ConfigureFrequencyVoltageRangeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12:\n\rvoltage_range\x18\x02 \x01(\x0e\x32!.nidmm_grpc.FrequencyVoltageRangeH\x00\x12\x1b\n\x11voltage_range_raw\x18\x03 \x01(\x01H\x00\x42\x14\n\x12voltage_range_enum\"8\n&ConfigureFrequencyVoltageRangeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"i\n ConfigureMeasCompleteDestRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12!\n\x19meas_complete_destination\x18\x02 \x01(\x11\"3\n!ConfigureMeasCompleteDestResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xe0\x03\n\x1a\x43onfigureMultiPointRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x31\n\rtrigger_count\x18\x02 \x01(\x0e\x32\x18.nidmm_grpc.TriggerCountH\x00\x12\x1b\n\x11trigger_count_raw\x18\x03 \x01(\x11H\x00\x12/\n\x0csample_count\x18\x04 \x01(\x0e\x32\x17.nidmm_grpc.SampleCountH\x01\x12\x1a\n\x10sample_count_raw\x18\x05 \x01(\x11H\x01\x12\x33\n\x0esample_trigger\x18\x06 \x01(\x0e\x32\x19.nidmm_grpc.SampleTriggerH\x02\x12\x1c\n\x12sample_trigger_raw\x18\x07 \x01(\x11H\x02\x12\x35\n\x0fsample_interval\x18\x08 \x01(\x0e\x32\x1a.nidmm_grpc.SampleIntervalH\x03\x12\x1d\n\x13sample_interval_raw\x18\t \x01(\x01H\x03\x42\x14\n\x12trigger_count_enumB\x13\n\x11sample_count_enumB\x15\n\x13sample_trigger_enumB\x16\n\x14sample_interval_enum\"-\n\x1b\x43onfigureMultiPointResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xaf\x01\n\x15ReadMultiPointRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12-\n\x0cmaximum_time\x18\x02 \x01(\x0e\x32\x15.nidmm_grpc.TimeLimitH\x00\x12\x1a\n\x10maximum_time_raw\x18\x03 \x01(\x11H\x00\x12\x12\n\narray_size\x18\x04 \x01(\x11\x42\x13\n\x11maximum_time_enum\"`\n\x16ReadMultiPointResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rreading_array\x18\x02 \x03(\x01\x12\x1f\n\x17\x61\x63tual_number_of_points\x18\x03 \x01(\x11\"\xb0\x01\n\x16\x46\x65tchMultiPointRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12-\n\x0cmaximum_time\x18\x02 \x01(\x0e\x32\x15.nidmm_grpc.TimeLimitH\x00\x12\x1a\n\x10maximum_time_raw\x18\x03 \x01(\x11H\x00\x12\x12\n\narray_size\x18\x04 \x01(\x11\x42\x13\n\x11maximum_time_enum\"a\n\x17\x46\x65tchMultiPointResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rreading_array\x18\x02 \x03(\x01\x12\x1f\n\x17\x61\x63tual_number_of_points\x18\x03 \x01(\x11\"\xa8\x01\n\x1c\x43onfigureTriggerSlopeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x31\n\rtrigger_slope\x18\x02 \x01(\x0e\x32\x18.nidmm_grpc.TriggerSlopeH\x00\x12\x1b\n\x11trigger_slope_raw\x18\x03 \x01(\x11H\x00\x42\x14\n\x12trigger_slope_enum\"/\n\x1d\x43onfigureTriggerSlopeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"@\n\x1aSendSoftwareTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"-\n\x1bSendSoftwareTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"@\n\x1aGetApertureTimeInfoRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\xd6\x01\n\x1bGetApertureTimeInfoResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12/\n\raperture_time\x18\x02 \x01(\x0e\x32\x18.nidmm_grpc.ApertureTime\x12\x19\n\x11\x61perture_time_raw\x18\x03 \x01(\x01\x12:\n\x13\x61perture_time_units\x18\x04 \x01(\x0e\x32\x1d.nidmm_grpc.ApertureTimeUnits\x12\x1f\n\x17\x61perture_time_units_raw\x18\x05 \x01(\x11\">\n\x18GetAutoRangeValueRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"A\n\x19GetAutoRangeValueResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x14\n\x0c\x61\x63tual_range\x18\x02 \x01(\x01\"Z\n\x1c\x43onfigureAutoZeroModeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x16\n\x0e\x61uto_zero_mode\x18\x02 \x01(\x11\"/\n\x1d\x43onfigureAutoZeroModeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xd4\x01\n\"ConfigurePowerLineFrequencyRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x43\n\x17power_line_frequency_hz\x18\x02 \x01(\x0e\x32 .nidmm_grpc.PowerLineFrequenciesH\x00\x12%\n\x1bpower_line_frequency_hz_raw\x18\x03 \x01(\x01H\x00\x42\x1e\n\x1cpower_line_frequency_hz_enum\"5\n#ConfigurePowerLineFrequencyResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xe8\x01\n!ConfigureMeasurementDigitsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x34\n\x14measurement_function\x18\x02 \x01(\x0e\x32\x14.nidmm_grpc.FunctionH\x00\x12\"\n\x18measurement_function_raw\x18\x03 \x01(\x11H\x00\x12\r\n\x05range\x18\x04 \x01(\x01\x12\x19\n\x11resolution_digits\x18\x05 \x01(\x01\x42\x1b\n\x19measurement_function_enum\"4\n\"ConfigureMeasurementDigitsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xec\x01\n#ConfigureMeasurementAbsoluteRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x34\n\x14measurement_function\x18\x02 \x01(\x0e\x32\x14.nidmm_grpc.FunctionH\x00\x12\"\n\x18measurement_function_raw\x18\x03 \x01(\x11H\x00\x12\r\n\x05range\x18\x04 \x01(\x01\x12\x1b\n\x13resolution_absolute\x18\x05 \x01(\x01\x42\x1b\n\x19measurement_function_enum\"6\n$ConfigureMeasurementAbsoluteResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"d\n!ConfigureMeasCompleteSlopeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x1b\n\x13meas_complete_slope\x18\x02 \x01(\x11\"4\n\"ConfigureMeasCompleteSlopeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xc6\x01\n\"ConfigureSampleTriggerSlopeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12;\n\x14sample_trigger_slope\x18\x02 \x01(\x0e\x32\x1b.nidmm_grpc.SampleTrigSlopeH\x00\x12\"\n\x18sample_trigger_slope_raw\x18\x03 \x01(\x11H\x00\x42\x1b\n\x19sample_trigger_slope_enum\"5\n#ConfigureSampleTriggerSlopeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"7\n\x11ReadStatusRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\x9c\x01\n\x12ReadStatusResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1b\n\x13\x61\x63quisition_backlog\x18\x02 \x01(\x11\x12\x39\n\x12\x61\x63quisition_status\x18\x03 \x01(\x0e\x32\x1d.nidmm_grpc.AcquisitionStatus\x12\x1e\n\x16\x61\x63quisition_status_raw\x18\x04 \x01(\x11\"\x9e\x01\n\x0e\x43ontrolRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x33\n\x0e\x63ontrol_action\x18\x02 \x01(\x0e\x32\x19.nidmm_grpc.ControlCommitH\x00\x12\x1c\n\x12\x63ontrol_action_raw\x18\x03 \x01(\x11H\x00\x42\x15\n\x13\x63ontrol_action_enum\"!\n\x0f\x43ontrolResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"]\n\x1e\x43onfigureADCCalibrationRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x17\n\x0f\x61\x64\x63_calibration\x18\x02 \x01(\x11\"1\n\x1f\x43onfigureADCCalibrationResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xb6\x01\n\x1e\x43onfigureOffsetCompOhmsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x37\n\x10offset_comp_ohms\x18\x02 \x01(\x0e\x32\x1b.nidmm_grpc.CompensatedOhmsH\x00\x12\x1e\n\x14offset_comp_ohms_raw\x18\x03 \x01(\x11H\x00\x42\x17\n\x15offset_comp_ohms_enum\"1\n\x1f\x43onfigureOffsetCompOhmsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"[\n\x1d\x43onfigureCurrentSourceRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x16\n\x0e\x63urrent_source\x18\x02 \x01(\x01\"0\n\x1e\x43onfigureCurrentSourceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\\\n\x1d\x43onfigureCableCompTypeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x17\n\x0f\x63\x61\x62le_comp_type\x18\x02 \x01(\x11\"0\n\x1e\x43onfigureCableCompTypeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"A\n\x1bPerformOpenCableCompRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"X\n\x1cPerformOpenCableCompResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0b\x63onductance\x18\x02 \x01(\x01\x12\x13\n\x0bsusceptance\x18\x03 \x01(\x01\"B\n\x1cPerformShortCableCompRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"V\n\x1dPerformShortCableCompResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nresistance\x18\x02 \x01(\x01\x12\x11\n\treactance\x18\x03 \x01(\x01\"s\n#ConfigureOpenCableCompValuesRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x13\n\x0b\x63onductance\x18\x02 \x01(\x01\x12\x13\n\x0bsusceptance\x18\x03 \x01(\x01\"6\n$ConfigureOpenCableCompValuesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"q\n$ConfigureShortCableCompValuesRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x12\n\nresistance\x18\x02 \x01(\x01\x12\x11\n\treactance\x18\x03 \x01(\x01\"7\n%ConfigureShortCableCompValuesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xf6\x01\n#ConfigureWaveformAcquisitionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x34\n\x14measurement_function\x18\x02 \x01(\x0e\x32\x14.nidmm_grpc.FunctionH\x00\x12\"\n\x18measurement_function_raw\x18\x03 \x01(\x11H\x00\x12\r\n\x05range\x18\x04 \x01(\x01\x12\x0c\n\x04rate\x18\x05 \x01(\x01\x12\x17\n\x0fwaveform_points\x18\x06 \x01(\x11\x42\x1b\n\x19measurement_function_enum\"6\n$ConfigureWaveformAcquisitionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"a\n ConfigureWaveformCouplingRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x19\n\x11waveform_coupling\x18\x02 \x01(\x11\"3\n!ConfigureWaveformCouplingResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xae\x01\n\x14\x46\x65tchWaveformRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12-\n\x0cmaximum_time\x18\x02 \x01(\x0e\x32\x15.nidmm_grpc.TimeLimitH\x00\x12\x1a\n\x10maximum_time_raw\x18\x03 \x01(\x11H\x00\x12\x12\n\narray_size\x18\x04 \x01(\x11\x42\x13\n\x11maximum_time_enum\"`\n\x15\x46\x65tchWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x16\n\x0ewaveform_array\x18\x02 \x03(\x01\x12\x1f\n\x17\x61\x63tual_number_of_points\x18\x03 \x01(\x11\"\xad\x01\n\x13ReadWaveformRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12-\n\x0cmaximum_time\x18\x02 \x01(\x0e\x32\x15.nidmm_grpc.TimeLimitH\x00\x12\x1a\n\x10maximum_time_raw\x18\x03 \x01(\x11H\x00\x12\x12\n\narray_size\x18\x04 \x01(\x11\x42\x13\n\x11maximum_time_enum\"_\n\x14ReadWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x16\n\x0ewaveform_array\x18\x02 \x03(\x01\x12\x1f\n\x17\x61\x63tual_number_of_points\x18\x03 \x01(\x11\"\x88\x01\n\x1aGetAttributeViInt32Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x30\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1a.nidmm_grpc.NiDmmAttribute\"F\n\x1bGetAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0f\x61ttribute_value\x18\x02 \x01(\x11\"\x81\x02\n\x1aSetAttributeViInt32Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x30\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1a.nidmm_grpc.NiDmmAttribute\x12@\n\x0f\x61ttribute_value\x18\x04 \x01(\x0e\x32%.nidmm_grpc.NiDmmInt32AttributeValuesH\x00\x12\x1d\n\x13\x61ttribute_value_raw\x18\x05 \x01(\x11H\x00\x42\x16\n\x14\x61ttribute_value_enum\"-\n\x1bSetAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x83\x02\n\x1c\x43heckAttributeViInt32Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x30\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1a.nidmm_grpc.NiDmmAttribute\x12@\n\x0f\x61ttribute_value\x18\x04 \x01(\x0e\x32%.nidmm_grpc.NiDmmInt32AttributeValuesH\x00\x12\x1d\n\x13\x61ttribute_value_raw\x18\x05 \x01(\x11H\x00\x42\x16\n\x14\x61ttribute_value_enum\"/\n\x1d\x43heckAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x89\x01\n\x1bGetAttributeViReal64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x30\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1a.nidmm_grpc.NiDmmAttribute\"G\n\x1cGetAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0f\x61ttribute_value\x18\x02 \x01(\x01\"\xd3\x02\n\x1bSetAttributeViReal64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x30\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1a.nidmm_grpc.NiDmmAttribute\x12\x41\n\x0f\x61ttribute_value\x18\x04 \x01(\x0e\x32&.nidmm_grpc.NiDmmReal64AttributeValuesH\x00\x12\x1d\n\x13\x61ttribute_value_raw\x18\x05 \x01(\x01H\x00\x12N\n\x16\x61ttribute_value_mapped\x18\x06 \x01(\x0e\x32,.nidmm_grpc.NiDmmReal64AttributeValuesMappedH\x00\x42\x16\n\x14\x61ttribute_value_enum\".\n\x1cSetAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xd5\x02\n\x1d\x43heckAttributeViReal64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x30\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1a.nidmm_grpc.NiDmmAttribute\x12\x41\n\x0f\x61ttribute_value\x18\x04 \x01(\x0e\x32&.nidmm_grpc.NiDmmReal64AttributeValuesH\x00\x12\x1d\n\x13\x61ttribute_value_raw\x18\x05 \x01(\x01H\x00\x12N\n\x16\x61ttribute_value_mapped\x18\x06 \x01(\x0e\x32,.nidmm_grpc.NiDmmReal64AttributeValuesMappedH\x00\x42\x16\n\x14\x61ttribute_value_enum\"0\n\x1e\x43heckAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x89\x01\n\x1bGetAttributeViStringRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x30\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1a.nidmm_grpc.NiDmmAttribute\"G\n\x1cGetAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0f\x61ttribute_value\x18\x02 \x01(\t\"\xa6\x01\n\x1bSetAttributeViStringRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x30\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1a.nidmm_grpc.NiDmmAttribute\x12\x1b\n\x13\x61ttribute_value_raw\x18\x04 \x01(\t\".\n\x1cSetAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xa8\x01\n\x1d\x43heckAttributeViStringRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x30\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1a.nidmm_grpc.NiDmmAttribute\x12\x1b\n\x13\x61ttribute_value_raw\x18\x04 \x01(\t\"0\n\x1e\x43heckAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x8a\x01\n\x1cGetAttributeViSessionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x30\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1a.nidmm_grpc.NiDmmAttribute\"`\n\x1dGetAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12/\n\x0f\x61ttribute_value\x18\x02 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\xbb\x01\n\x1cSetAttributeViSessionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x30\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1a.nidmm_grpc.NiDmmAttribute\x12/\n\x0f\x61ttribute_value\x18\x04 \x01(\x0b\x32\x16.nidevice_grpc.Session\"/\n\x1dSetAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xbd\x01\n\x1e\x43heckAttributeViSessionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x30\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1a.nidmm_grpc.NiDmmAttribute\x12/\n\x0f\x61ttribute_value\x18\x04 \x01(\x0b\x32\x16.nidevice_grpc.Session\"1\n\x1f\x43heckAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x8a\x01\n\x1cGetAttributeViBooleanRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x30\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1a.nidmm_grpc.NiDmmAttribute\"H\n\x1dGetAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0f\x61ttribute_value\x18\x02 \x01(\x08\"\xa3\x01\n\x1cSetAttributeViBooleanRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x30\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1a.nidmm_grpc.NiDmmAttribute\x12\x17\n\x0f\x61ttribute_value\x18\x04 \x01(\x08\"/\n\x1dSetAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xa5\x01\n\x1e\x43heckAttributeViBooleanRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x30\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1a.nidmm_grpc.NiDmmAttribute\x12\x17\n\x0f\x61ttribute_value\x18\x04 \x01(\x08\"1\n\x1f\x43heckAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"`\n\'ImportAttributeConfigurationFileRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tfile_path\x18\x02 \x01(\t\":\n(ImportAttributeConfigurationFileResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"`\n\'ExportAttributeConfigurationFileRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tfile_path\x18\x02 \x01(\t\":\n(ExportAttributeConfigurationFileResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"f\n)ImportAttributeConfigurationBufferRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x15\n\rconfiguration\x18\x02 \x01(\x0c\"<\n*ImportAttributeConfigurationBufferResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"O\n)ExportAttributeConfigurationBufferRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"S\n*ExportAttributeConfigurationBufferResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rconfiguration\x18\x02 \x01(\x0c\"B\n\x1cResetInterchangeCheckRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"/\n\x1dResetInterchangeCheckResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"E\n\x1f\x43learInterchangeWarningsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"2\n ClearInterchangeWarningsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"J\n\x15GetChannelNameRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\r\n\x05index\x18\x02 \x01(\x11\"@\n\x16GetChannelNameResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x16\n\x0e\x63hannel_string\x18\x02 \x01(\t\"I\n#GetExtCalRecommendedIntervalRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"F\n$GetExtCalRecommendedIntervalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0e\n\x06months\x18\x02 \x01(\x11\"@\n\x1aGetSelfCalSupportedRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"I\n\x1bGetSelfCalSupportedResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1a\n\x12self_cal_supported\x18\x02 \x01(\x08\"\x98\x01\n\x18GetCalDateAndTimeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12/\n\x08\x63\x61l_type\x18\x02 \x01(\x0e\x32\x1b.nidmm_grpc.CalibrationTypeH\x00\x12\x16\n\x0c\x63\x61l_type_raw\x18\x03 \x01(\x11H\x00\x42\x0f\n\rcal_type_enum\"s\n\x19GetCalDateAndTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05month\x18\x02 \x01(\x11\x12\x0b\n\x03\x64\x61y\x18\x03 \x01(\x11\x12\x0c\n\x04year\x18\x04 \x01(\x11\x12\x0c\n\x04hour\x18\x05 \x01(\x11\x12\x0e\n\x06minute\x18\x06 \x01(\x11\"\x95\x01\n\x15GetLastCalTempRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12/\n\x08\x63\x61l_type\x18\x02 \x01(\x0e\x32\x1b.nidmm_grpc.CalibrationTypeH\x00\x12\x16\n\x0c\x63\x61l_type_raw\x18\x03 \x01(\x11H\x00\x42\x0f\n\rcal_type_enum\"=\n\x16GetLastCalTempResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0btemperature\x18\x02 \x01(\x01\"H\n\x11GetDevTempRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0f\n\x07options\x18\x02 \x01(\t\"9\n\x12GetDevTempResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0btemperature\x18\x02 \x01(\x01\"]\n\x1e\x43onfigureTransducerTypeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x17\n\x0ftransducer_type\x18\x02 \x01(\x11\"1\n\x1f\x43onfigureTransducerTypeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xd1\x02\n\x1c\x43onfigureThermocoupleRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x39\n\x11thermocouple_type\x18\x02 \x01(\x0e\x32\x1c.nidmm_grpc.ThermocoupleTypeH\x00\x12\x1f\n\x15thermocouple_type_raw\x18\x03 \x01(\x11H\x00\x12P\n\x17reference_junction_type\x18\x04 \x01(\x0e\x32-.nidmm_grpc.ThermocoupleReferenceJunctionTypeH\x01\x12%\n\x1breference_junction_type_raw\x18\x05 \x01(\x11H\x01\x42\x18\n\x16thermocouple_type_enumB\x1e\n\x1creference_junction_type_enum\"/\n\x1d\x43onfigureThermocoupleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"h\n ConfigureFixedRefJunctionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12 \n\x18\x66ixed_reference_junction\x18\x02 \x01(\x01\"3\n!ConfigureFixedRefJunctionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xa7\x01\n\x17\x43onfigureRTDTypeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\'\n\x08rtd_type\x18\x02 \x01(\x0e\x32\x13.nidmm_grpc.RtdTypeH\x00\x12\x16\n\x0crtd_type_raw\x18\x03 \x01(\x11H\x00\x12\x16\n\x0ertd_resistance\x18\x04 \x01(\x01\x42\x0f\n\rrtd_type_enum\"*\n\x18\x43onfigureRTDTypeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"l\n\x19\x43onfigureRTDCustomRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\r\n\x05rtd_a\x18\x02 \x01(\x01\x12\r\n\x05rtd_b\x18\x03 \x01(\x01\x12\r\n\x05rtd_c\x18\x04 \x01(\x01\",\n\x1a\x43onfigureRTDCustomResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"]\n\x1e\x43onfigureThermistorTypeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x17\n\x0fthermistor_type\x18\x02 \x01(\x11\"1\n\x1f\x43onfigureThermistorTypeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x88\x01\n ConfigureThermistorCustomRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0cthermistor_a\x18\x02 \x01(\x01\x12\x14\n\x0cthermistor_b\x18\x03 \x01(\x01\x12\x14\n\x0cthermistor_c\x18\x04 \x01(\x01\"3\n!ConfigureThermistorCustomResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"D\n\x1eInvalidateAllAttributesRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"1\n\x1fInvalidateAllAttributesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05*\x8a\x1b\n\x0eNiDmmAttribute\x12\x1f\n\x1bNIDMM_ATTRIBUTE_UNSPECIFIED\x10\x00\x12!\n\x1bNIDMM_ATTRIBUTE_RANGE_CHECK\x10\x92\x8b@\x12-\n\'NIDMM_ATTRIBUTE_QUERY_INSTRUMENT_STATUS\x10\x93\x8b@\x12\x1b\n\x15NIDMM_ATTRIBUTE_CACHE\x10\x94\x8b@\x12\x1e\n\x18NIDMM_ATTRIBUTE_SIMULATE\x10\x95\x8b@\x12&\n NIDMM_ATTRIBUTE_RECORD_COERCIONS\x10\x96\x8b@\x12\'\n!NIDMM_ATTRIBUTE_INTERCHANGE_CHECK\x10\xa5\x8b@\x12>\n8NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION\x10\x93\x8f@\x12>\n8NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION\x10\x94\x8f@\x12\x31\n+NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_DESCRIPTION\x10\x92\x8f@\x12,\n&NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_PREFIX\x10\xbe\x8d@\x12,\n&NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_VENDOR\x10\x91\x8f@\x12.\n(NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_REVISION\x10\xb7\x8f@\x12#\n\x1dNIDMM_ATTRIBUTE_CHANNEL_COUNT\x10\xdb\x8c@\x12\x31\n+NIDMM_ATTRIBUTE_SUPPORTED_INSTRUMENT_MODELS\x10\xd7\x8d@\x12(\n\"NIDMM_ATTRIBUTE_GROUP_CAPABILITIES\x10\xa1\x8e@\x12-\n\'NIDMM_ATTRIBUTE_INSTRUMENT_MANUFACTURER\x10\x8f\x8f@\x12&\n NIDMM_ATTRIBUTE_INSTRUMENT_MODEL\x10\x90\x8f@\x12\x32\n,NIDMM_ATTRIBUTE_INSTRUMENT_FIRMWARE_REVISION\x10\x8e\x8f@\x12\"\n\x1cNIDMM_ATTRIBUTE_LOGICAL_NAME\x10\xc1\x8d@\x12,\n&NIDMM_ATTRIBUTE_IO_RESOURCE_DESCRIPTOR\x10\xc0\x8d@\x12\"\n\x1cNIDMM_ATTRIBUTE_DRIVER_SETUP\x10\x97\x8b@\x12\x1e\n\x18NIDMM_ATTRIBUTE_FUNCTION\x10\xd1\xa5L\x12\x1b\n\x15NIDMM_ATTRIBUTE_RANGE\x10\xd2\xa5L\x12)\n#NIDMM_ATTRIBUTE_RESOLUTION_ABSOLUTE\x10\xd8\xa5L\x12\'\n!NIDMM_ATTRIBUTE_RESOLUTION_DIGITS\x10\xd3\xa5L\x12#\n\x1dNIDMM_ATTRIBUTE_TRIGGER_DELAY\x10\xd5\xa5L\x12$\n\x1eNIDMM_ATTRIBUTE_TRIGGER_SOURCE\x10\xd4\xa5L\x12!\n\x1bNIDMM_ATTRIBUTE_AC_MAX_FREQ\x10\xd7\xa5L\x12!\n\x1bNIDMM_ATTRIBUTE_AC_MIN_FREQ\x10\xd6\xa5L\x12(\n\"NIDMM_ATTRIBUTE_FREQ_VOLTAGE_RANGE\x10\xb5\xa6L\x12(\n\"NIDMM_ATTRIBUTE_MEAS_COMPLETE_DEST\x10\x81\xa8L\x12\"\n\x1cNIDMM_ATTRIBUTE_SAMPLE_COUNT\x10\xfd\xa7L\x12%\n\x1fNIDMM_ATTRIBUTE_SAMPLE_INTERVAL\x10\xff\xa7L\x12$\n\x1eNIDMM_ATTRIBUTE_SAMPLE_TRIGGER\x10\xfe\xa7L\x12#\n\x1dNIDMM_ATTRIBUTE_TRIGGER_COUNT\x10\x80\xa8L\x12#\n\x1dNIDMM_ATTRIBUTE_APERTURE_TIME\x10\x91\xa8L\x12)\n#NIDMM_ATTRIBUTE_APERTURE_TIME_UNITS\x10\x92\xa8L\x12&\n NIDMM_ATTRIBUTE_AUTO_RANGE_VALUE\x10\x9b\xa8L\x12\x1f\n\x19NIDMM_ATTRIBUTE_AUTO_ZERO\x10\x9c\xa8L\x12$\n\x1eNIDMM_ATTRIBUTE_POWERLINE_FREQ\x10\x9d\xa8L\x12#\n\x1dNIDMM_ATTRIBUTE_TRIGGER_SLOPE\x10\x9e\xa8L\x12*\n$NIDMM_ATTRIBUTE_SAMPLE_TRIGGER_SLOPE\x10\xba\x98\x46\x12%\n\x1fNIDMM_ATTRIBUTE_MEAS_DEST_SLOPE\x10\xb2\x98\x46\x12%\n\x1fNIDMM_ATTRIBUTE_ADC_CALIBRATION\x10\xc6\x98\x46\x12&\n NIDMM_ATTRIBUTE_OFFSET_COMP_OHMS\x10\xc7\x98\x46\x12(\n\"NIDMM_ATTRIBUTE_NUMBER_OF_AVERAGES\x10\xd0\x98\x46\x12$\n\x1eNIDMM_ATTRIBUTE_CURRENT_SOURCE\x10\xc9\x98\x46\x12(\n\"NIDMM_ATTRIBUTE_DC_NOISE_REJECTION\x10\xca\x98\x46\x12!\n\x1bNIDMM_ATTRIBUTE_SETTLE_TIME\x10\xcc\x98\x46\x12&\n NIDMM_ATTRIBUTE_INPUT_RESISTANCE\x10\xcd\x98\x46\x12\x1d\n\x17NIDMM_ATTRIBUTE_LATENCY\x10\xd2\x98\x46\x12!\n\x1bNIDMM_ATTRIBUTE_BUFFER_SIZE\x10\xd5\x98\x46\x12!\n\x1bNIDMM_ATTRIBUTE_SHUNT_VALUE\x10\xb3\x98\x46\x12$\n\x1eNIDMM_ATTRIBUTE_OPERATION_MODE\x10\xbe\x98\x46\x12#\n\x1dNIDMM_ATTRIBUTE_WAVEFORM_RATE\x10\xc2\x98\x46\x12%\n\x1fNIDMM_ATTRIBUTE_WAVEFORM_POINTS\x10\xc3\x98\x46\x12\'\n!NIDMM_ATTRIBUTE_WAVEFORM_COUPLING\x10\xcb\x98\x46\x12\x33\n-NIDMM_ATTRIBUTE_FREQ_VOLTAGE_AUTO_RANGE_VALUE\x10\xdc\x98\x46\x12%\n\x1fNIDMM_ATTRIBUTE_CABLE_COMP_TYPE\x10\xdd\x98\x46\x12\x30\n*NIDMM_ATTRIBUTE_SHORT_CABLE_COMP_REACTANCE\x10\xde\x98\x46\x12\x31\n+NIDMM_ATTRIBUTE_SHORT_CABLE_COMP_RESISTANCE\x10\xdf\x98\x46\x12\x31\n+NIDMM_ATTRIBUTE_OPEN_CABLE_COMP_SUSCEPTANCE\x10\xe0\x98\x46\x12\x31\n+NIDMM_ATTRIBUTE_OPEN_CABLE_COMP_CONDUCTANCE\x10\xe1\x98\x46\x12*\n$NIDMM_ATTRIBUTE_LC_CALCULATION_MODEL\x10\xe4\x98\x46\x12\x1d\n\x17NIDMM_ATTRIBUTE_DC_BIAS\x10\xe5\x98\x46\x12/\n)NIDMM_ATTRIBUTE_LC_NUMBER_MEAS_TO_AVERAGE\x10\xe7\x98\x46\x12#\n\x1dNIDMM_ATTRIBUTE_SERIAL_NUMBER\x10\xe6\x98\x46\x12+\n%NIDMM_ATTRIBUTE_CONFIG_PRODUCT_NUMBER\x10\xed\x98\x46\x12*\n$NIDMM_ATTRIBUTE_TEMP_TRANSDUCER_TYPE\x10\x99\xa7L\x12+\n%NIDMM_ATTRIBUTE_TEMP_TC_REF_JUNC_TYPE\x10\xb8\xa7L\x12\"\n\x1cNIDMM_ATTRIBUTE_TEMP_TC_TYPE\x10\xb7\xa7L\x12,\n&NIDMM_ATTRIBUTE_TEMP_TC_FIXED_REF_JUNC\x10\xb9\xa7L\x12#\n\x1dNIDMM_ATTRIBUTE_TEMP_RTD_TYPE\x10\xa8\x99\x46\x12\"\n\x1cNIDMM_ATTRIBUTE_TEMP_RTD_RES\x10\xc2\xa7L\x12 \n\x1aNIDMM_ATTRIBUTE_TEMP_RTD_A\x10\xa9\x99\x46\x12 \n\x1aNIDMM_ATTRIBUTE_TEMP_RTD_B\x10\xaa\x99\x46\x12 \n\x1aNIDMM_ATTRIBUTE_TEMP_RTD_C\x10\xab\x99\x46\x12*\n$NIDMM_ATTRIBUTE_TEMP_THERMISTOR_TYPE\x10\xac\x99\x46\x12\'\n!NIDMM_ATTRIBUTE_TEMP_THERMISTOR_A\x10\xad\x99\x46\x12\'\n!NIDMM_ATTRIBUTE_TEMP_THERMISTOR_B\x10\xae\x99\x46\x12\'\n!NIDMM_ATTRIBUTE_TEMP_THERMISTOR_C\x10\xaf\x99\x46\x12\x33\n-NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_MAJOR_VERSION\x10\x87\x8f@\x12\x33\n-NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_MINOR_VERSION\x10\x88\x8f@*\xbb\x04\n\x08\x46unction\x12\x18\n\x14\x46UNCTION_UNSPECIFIED\x10\x00\x12\x1f\n\x1b\x46UNCTION_NIDMM_VAL_DC_VOLTS\x10\x01\x12\x1f\n\x1b\x46UNCTION_NIDMM_VAL_AC_VOLTS\x10\x02\x12!\n\x1d\x46UNCTION_NIDMM_VAL_DC_CURRENT\x10\x03\x12!\n\x1d\x46UNCTION_NIDMM_VAL_AC_CURRENT\x10\x04\x12!\n\x1d\x46UNCTION_NIDMM_VAL_2_WIRE_RES\x10\x05\x12!\n\x1d\x46UNCTION_NIDMM_VAL_4_WIRE_RES\x10\x65\x12\x1b\n\x17\x46UNCTION_NIDMM_VAL_FREQ\x10h\x12\x1d\n\x19\x46UNCTION_NIDMM_VAL_PERIOD\x10i\x12\"\n\x1e\x46UNCTION_NIDMM_VAL_TEMPERATURE\x10l\x12+\n&FUNCTION_NIDMM_VAL_AC_VOLTS_DC_COUPLED\x10\xe9\x07\x12\x1d\n\x18\x46UNCTION_NIDMM_VAL_DIODE\x10\xea\x07\x12(\n#FUNCTION_NIDMM_VAL_WAVEFORM_VOLTAGE\x10\xeb\x07\x12(\n#FUNCTION_NIDMM_VAL_WAVEFORM_CURRENT\x10\xec\x07\x12#\n\x1e\x46UNCTION_NIDMM_VAL_CAPACITANCE\x10\xed\x07\x12\"\n\x1d\x46UNCTION_NIDMM_VAL_INDUCTANCE\x10\xee\x07*\xe4\x04\n\rTriggerSource\x12\x1e\n\x1aTRIGGER_SOURCE_UNSPECIFIED\x10\x00\x12&\n\"TRIGGER_SOURCE_NIDMM_VAL_IMMEDIATE\x10\x01\x12%\n!TRIGGER_SOURCE_NIDMM_VAL_EXTERNAL\x10\x02\x12*\n&TRIGGER_SOURCE_NIDMM_VAL_SOFTWARE_TRIG\x10\x03\x12&\n\"TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG0\x10o\x12&\n\"TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG1\x10p\x12&\n\"TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG2\x10q\x12&\n\"TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG3\x10r\x12&\n\"TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG4\x10s\x12&\n\"TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG5\x10t\x12&\n\"TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG6\x10u\x12&\n\"TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG7\x10v\x12&\n!TRIGGER_SOURCE_NIDMM_VAL_PXI_STAR\x10\x83\x01\x12\'\n\"TRIGGER_SOURCE_NIDMM_VAL_AUX_TRIG1\x10\xe9\x07\x12\'\n\"TRIGGER_SOURCE_NIDMM_VAL_LBR_TRIG1\x10\xec\x07*\x8b\x05\n\rSampleTrigger\x12\x1e\n\x1aSAMPLE_TRIGGER_UNSPECIFIED\x10\x00\x12&\n\"SAMPLE_TRIGGER_NIDMM_VAL_IMMEDIATE\x10\x01\x12%\n!SAMPLE_TRIGGER_NIDMM_VAL_EXTERNAL\x10\x02\x12*\n&SAMPLE_TRIGGER_NIDMM_VAL_SOFTWARE_TRIG\x10\x03\x12%\n!SAMPLE_TRIGGER_NIDMM_VAL_INTERVAL\x10\n\x12&\n\"SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG0\x10o\x12&\n\"SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG1\x10p\x12&\n\"SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG2\x10q\x12&\n\"SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG3\x10r\x12&\n\"SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG4\x10s\x12&\n\"SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG5\x10t\x12&\n\"SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG6\x10u\x12&\n\"SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG7\x10v\x12&\n!SAMPLE_TRIGGER_NIDMM_VAL_PXI_STAR\x10\x83\x01\x12\'\n\"SAMPLE_TRIGGER_NIDMM_VAL_AUX_TRIG1\x10\xe9\x07\x12\'\n\"SAMPLE_TRIGGER_NIDMM_VAL_LBR_TRIG1\x10\xec\x07*Z\n\x0cTriggerSlope\x12$\n TRIGGER_SLOPE_NIDMM_VAL_POSITIVE\x10\x00\x12$\n TRIGGER_SLOPE_NIDMM_VAL_NEGATIVE\x10\x01*e\n\x0fSampleTrigSlope\x12(\n$SAMPLE_TRIG_SLOPE_NIDMM_VAL_POSITIVE\x10\x00\x12(\n$SAMPLE_TRIG_SLOPE_NIDMM_VAL_NEGATIVE\x10\x01*\x9c\x01\n\x14PowerLineFrequencies\x12&\n\"POWER_LINE_FREQUENCIES_UNSPECIFIED\x10\x00\x12-\n)POWER_LINE_FREQUENCIES_NIDMM_VAL_50_HERTZ\x10\x32\x12-\n)POWER_LINE_FREQUENCIES_NIDMM_VAL_60_HERTZ\x10<*s\n\x11\x41pertureTimeUnits\x12)\n%APERTURE_TIME_UNITS_NIDMM_VAL_SECONDS\x10\x00\x12\x33\n/APERTURE_TIME_UNITS_NIDMM_VAL_POWER_LINE_CYCLES\x10\x01*z\n\x0f\x43ompensatedOhms\x12\x33\n/COMPENSATED_OHMS_NIDMM_VAL_OFFSET_COMP_OHMS_OFF\x10\x00\x12\x32\n.COMPENSATED_OHMS_NIDMM_VAL_OFFSET_COMP_OHMS_ON\x10\x01*m\n\x0f\x43\x61librationType\x12,\n(CALIBRATION_TYPE_NIDMM_VAL_INTERNAL_AREA\x10\x00\x12,\n(CALIBRATION_TYPE_NIDMM_VAL_EXTERNAL_AREA\x10\x01*\xa1\x01\n!ThermocoupleReferenceJunctionType\x12\x34\n0THERMOCOUPLE_REFERENCE_JUNCTION_TYPE_UNSPECIFIED\x10\x00\x12\x46\nBTHERMOCOUPLE_REFERENCE_JUNCTION_TYPE_NIDMM_VAL_TEMP_REF_JUNC_FIXED\x10\x02*\x8d\x03\n\x10ThermocoupleType\x12!\n\x1dTHERMOCOUPLE_TYPE_UNSPECIFIED\x10\x00\x12)\n%THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_B\x10\x01\x12)\n%THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_E\x10\x04\x12)\n%THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_J\x10\x06\x12)\n%THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_K\x10\x07\x12)\n%THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_N\x10\x08\x12)\n%THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_R\x10\t\x12)\n%THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_S\x10\n\x12)\n%THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_T\x10\x0b*\xa1\x02\n\x07RtdType\x12&\n\"RTD_TYPE_NIDMM_VAL_TEMP_RTD_CUSTOM\x10\x00\x12&\n\"RTD_TYPE_NIDMM_VAL_TEMP_RTD_PT3750\x10\x01\x12&\n\"RTD_TYPE_NIDMM_VAL_TEMP_RTD_PT3851\x10\x02\x12&\n\"RTD_TYPE_NIDMM_VAL_TEMP_RTD_PT3911\x10\x03\x12&\n\"RTD_TYPE_NIDMM_VAL_TEMP_RTD_PT3916\x10\x04\x12&\n\"RTD_TYPE_NIDMM_VAL_TEMP_RTD_PT3920\x10\x05\x12&\n\"RTD_TYPE_NIDMM_VAL_TEMP_RTD_PT3928\x10\x06*\xa4\x02\n\x11\x41\x63quisitionStatus\x12\x36\n2ACQUISITION_STATUS_NIDMM_VAL_RUNNING_ANTICOLLISION\x10\x00\x12\x36\n2ACQUISITION_STATUS_NIDMM_VAL_FINISHED_WITH_BACKLOG\x10\x01\x12\x39\n5ACQUISITION_STATUS_NIDMM_VAL_FINISHED_WITH_NO_BACKLOG\x10\x02\x12\'\n#ACQUISITION_STATUS_NIDMM_VAL_PAUSED\x10\x03\x12;\n7ACQUISITION_STATUS_NIDMM_VAL_NO_ACQUISITION_IN_PROGRESS\x10\x04*\xe1\x02\n\x0c\x41pertureTime\x12\x1d\n\x19\x41PERTURE_TIME_UNSPECIFIED\x10\x00\x12\x37\n*APERTURE_TIME_NIDMM_VAL_APERTURE_TIME_AUTO\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12!\n\x1d\x41PERTURE_TIME_NIDMM_VAL_1_PLC\x10\x01\x12!\n\x1d\x41PERTURE_TIME_NIDMM_VAL_5_PLC\x10\x05\x12!\n\x1d\x41PERTURE_TIME_NIDMM_VAL_6_PLC\x10\x06\x12\"\n\x1e\x41PERTURE_TIME_NIDMM_VAL_10_PLC\x10\n\x12\"\n\x1e\x41PERTURE_TIME_NIDMM_VAL_12_PLC\x10\x0c\x12#\n\x1f\x41PERTURE_TIME_NIDMM_VAL_100_PLC\x10\x64\x12#\n\x1f\x41PERTURE_TIME_NIDMM_VAL_120_PLC\x10x*<\n\rControlCommit\x12+\n\'CONTROL_COMMIT_NIDMM_VAL_CONTROL_COMMIT\x10\x00*\xbd\x01\n\x15\x46requencyVoltageRange\x12\'\n#FREQUENCY_VOLTAGE_RANGE_UNSPECIFIED\x10\x00\x12<\n/FREQUENCY_VOLTAGE_RANGE_NIDMM_VAL_AUTO_RANGE_ON\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12=\n0FREQUENCY_VOLTAGE_RANGE_NIDMM_VAL_AUTO_RANGE_OFF\x10\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01*?\n\x0bSampleCount\x12\x30\n,SAMPLE_COUNT_NIDMM_VAL_SAMPLE_COUNT_INFINITE\x10\x00*d\n\x0eSampleInterval\x12\x1f\n\x1bSAMPLE_INTERVAL_UNSPECIFIED\x10\x00\x12\x31\n$SAMPLE_INTERVAL_NIDMM_VAL_AUTO_DELAY\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01*Z\n\tTimeLimit\x12\x1a\n\x16TIME_LIMIT_UNSPECIFIED\x10\x00\x12\x31\n$TIME_LIMIT_NIDMM_VAL_TIME_LIMIT_AUTO\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01*?\n\x0cTriggerCount\x12/\n+TRIGGER_COUNT_NIDMM_VAL_TRIG_COUNT_INFINITE\x10\x00*\x9a\x01\n\rTriggerDelays\x12\x1e\n\x1aTRIGGER_DELAYS_UNSPECIFIED\x10\x00\x12\x33\n&TRIGGER_DELAYS_NIDMM_VAL_AUTO_DELAY_ON\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x34\n\'TRIGGER_DELAYS_NIDMM_VAL_AUTO_DELAY_OFF\x10\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01*\xd2.\n\x19NiDmmInt32AttributeValues\x12\x1b\n\x17NIDMM_INT32_UNSPECIFIED\x10\x00\x12\x37\n3NIDMM_INT32_ADC_CALIBRATION_VAL_ADC_CALIBRATION_OFF\x10\x00\x12\x41\n4NIDMM_INT32_ADC_CALIBRATION_VAL_ADC_CALIBRATION_AUTO\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x36\n2NIDMM_INT32_ADC_CALIBRATION_VAL_ADC_CALIBRATION_ON\x10\x01\x12/\n+NIDMM_INT32_APERTURE_TIME_UNITS_VAL_SECONDS\x10\x00\x12\x39\n5NIDMM_INT32_APERTURE_TIME_UNITS_VAL_POWER_LINE_CYCLES\x10\x01\x12+\n\'NIDMM_INT32_AUTO_ZERO_VAL_AUTO_ZERO_OFF\x10\x00\x12\x35\n(NIDMM_INT32_AUTO_ZERO_VAL_AUTO_ZERO_AUTO\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12*\n&NIDMM_INT32_AUTO_ZERO_VAL_AUTO_ZERO_ON\x10\x01\x12,\n(NIDMM_INT32_AUTO_ZERO_VAL_AUTO_ZERO_ONCE\x10\x02\x12\x39\n,NIDMM_INT32_BUFFER_SIZE_VAL_BUFFER_SIZE_AUTO\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12;\n7NIDMM_INT32_CABLE_COMPENSATION_TYPE_VAL_CABLE_COMP_NONE\x10\x00\x12;\n7NIDMM_INT32_CABLE_COMPENSATION_TYPE_VAL_CABLE_COMP_OPEN\x10\x01\x12<\n8NIDMM_INT32_CABLE_COMPENSATION_TYPE_VAL_CABLE_COMP_SHORT\x10\x02\x12\x45\nANIDMM_INT32_CABLE_COMPENSATION_TYPE_VAL_CABLE_COMP_OPEN_AND_SHORT\x10\x03\x12\x39\n5NIDMM_INT32_COMPENSATED_OHMS_VAL_OFFSET_COMP_OHMS_OFF\x10\x00\x12\x38\n4NIDMM_INT32_COMPENSATED_OHMS_VAL_OFFSET_COMP_OHMS_ON\x10\x01\x12\'\n#NIDMM_INT32_DC_BIAS_VAL_DC_BIAS_OFF\x10\x00\x12&\n\"NIDMM_INT32_DC_BIAS_VAL_DC_BIAS_ON\x10\x01\x12\x32\n.NIDMM_INT32_DC_NOISE_REJECTION_VAL_DCNR_NORMAL\x10\x00\x12\x39\n,NIDMM_INT32_DC_NOISE_REJECTION_VAL_DCNR_AUTO\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x38\n4NIDMM_INT32_DC_NOISE_REJECTION_VAL_DCNR_SECOND_ORDER\x10\x01\x12\x36\n2NIDMM_INT32_DC_NOISE_REJECTION_VAL_DCNR_HIGH_ORDER\x10\x02\x12%\n!NIDMM_INT32_FUNCTION_VAL_DC_VOLTS\x10\x01\x12%\n!NIDMM_INT32_FUNCTION_VAL_AC_VOLTS\x10\x02\x12\'\n#NIDMM_INT32_FUNCTION_VAL_DC_CURRENT\x10\x03\x12\'\n#NIDMM_INT32_FUNCTION_VAL_AC_CURRENT\x10\x04\x12\'\n#NIDMM_INT32_FUNCTION_VAL_2_WIRE_RES\x10\x05\x12\'\n#NIDMM_INT32_FUNCTION_VAL_4_WIRE_RES\x10\x65\x12!\n\x1dNIDMM_INT32_FUNCTION_VAL_FREQ\x10h\x12#\n\x1fNIDMM_INT32_FUNCTION_VAL_PERIOD\x10i\x12(\n$NIDMM_INT32_FUNCTION_VAL_TEMPERATURE\x10l\x12\x31\n,NIDMM_INT32_FUNCTION_VAL_AC_VOLTS_DC_COUPLED\x10\xe9\x07\x12#\n\x1eNIDMM_INT32_FUNCTION_VAL_DIODE\x10\xea\x07\x12.\n)NIDMM_INT32_FUNCTION_VAL_WAVEFORM_VOLTAGE\x10\xeb\x07\x12.\n)NIDMM_INT32_FUNCTION_VAL_WAVEFORM_CURRENT\x10\xec\x07\x12)\n$NIDMM_INT32_FUNCTION_VAL_CAPACITANCE\x10\xed\x07\x12(\n#NIDMM_INT32_FUNCTION_VAL_INDUCTANCE\x10\xee\x07\x12\x31\n$NIDMM_INT32_LATENCY_VAL_LATENCY_AUTO\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12:\n6NIDMM_INT32_LC_CALCULATION_MODEL_VAL_CALC_MODEL_SERIES\x10\x00\x12\x41\n4NIDMM_INT32_LC_CALCULATION_MODEL_VAL_CALC_MODEL_AUTO\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12<\n8NIDMM_INT32_LC_CALCULATION_MODEL_VAL_CALC_MODEL_PARALLEL\x10\x01\x12;\n.NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_NONE\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x36\n2NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_EXTERNAL\x10\x02\x12\x37\n3NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG0\x10o\x12\x37\n3NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG1\x10p\x12\x37\n3NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG2\x10q\x12\x37\n3NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG3\x10r\x12\x37\n3NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG4\x10s\x12\x37\n3NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG5\x10t\x12\x37\n3NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG6\x10u\x12\x37\n3NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG7\x10v\x12\x38\n3NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_LBR_TRIG0\x10\xeb\x07\x12:\n6NIDMM_INT32_MEASUREMENT_DESTINATION_SLOPE_VAL_POSITIVE\x10\x00\x12:\n6NIDMM_INT32_MEASUREMENT_DESTINATION_SLOPE_VAL_NEGATIVE\x10\x01\x12.\n*NIDMM_INT32_OPERATION_MODE_VAL_IVIDMM_MODE\x10\x00\x12\x30\n,NIDMM_INT32_OPERATION_MODE_VAL_WAVEFORM_MODE\x10\x01\x12,\n(NIDMM_INT32_RTD_TYPE_VAL_TEMP_RTD_CUSTOM\x10\x00\x12,\n(NIDMM_INT32_RTD_TYPE_VAL_TEMP_RTD_PT3750\x10\x01\x12,\n(NIDMM_INT32_RTD_TYPE_VAL_TEMP_RTD_PT3851\x10\x02\x12,\n(NIDMM_INT32_RTD_TYPE_VAL_TEMP_RTD_PT3911\x10\x03\x12,\n(NIDMM_INT32_RTD_TYPE_VAL_TEMP_RTD_PT3916\x10\x04\x12,\n(NIDMM_INT32_RTD_TYPE_VAL_TEMP_RTD_PT3920\x10\x05\x12,\n(NIDMM_INT32_RTD_TYPE_VAL_TEMP_RTD_PT3928\x10\x06\x12\x36\n2NIDMM_INT32_SAMPLE_COUNT_VAL_SAMPLE_COUNT_INFINITE\x10\x00\x12.\n*NIDMM_INT32_SAMPLE_TRIG_SLOPE_VAL_POSITIVE\x10\x00\x12.\n*NIDMM_INT32_SAMPLE_TRIG_SLOPE_VAL_NEGATIVE\x10\x01\x12,\n(NIDMM_INT32_SAMPLE_TRIGGER_VAL_IMMEDIATE\x10\x01\x12+\n\'NIDMM_INT32_SAMPLE_TRIGGER_VAL_EXTERNAL\x10\x02\x12\x30\n,NIDMM_INT32_SAMPLE_TRIGGER_VAL_SOFTWARE_TRIG\x10\x03\x12+\n\'NIDMM_INT32_SAMPLE_TRIGGER_VAL_INTERVAL\x10\n\x12,\n(NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG0\x10o\x12,\n(NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG1\x10p\x12,\n(NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG2\x10q\x12,\n(NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG3\x10r\x12,\n(NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG4\x10s\x12,\n(NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG5\x10t\x12,\n(NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG6\x10u\x12,\n(NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG7\x10v\x12,\n\'NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_STAR\x10\x83\x01\x12-\n(NIDMM_INT32_SAMPLE_TRIGGER_VAL_AUX_TRIG1\x10\xe9\x07\x12-\n(NIDMM_INT32_SAMPLE_TRIGGER_VAL_LBR_TRIG1\x10\xec\x07\x12:\n6NIDMM_INT32_THERMISTOR_TYPE_VAL_TEMP_THERMISTOR_CUSTOM\x10\x00\x12\x39\n5NIDMM_INT32_THERMISTOR_TYPE_VAL_TEMP_THERMISTOR_44004\x10\x01\x12\x39\n5NIDMM_INT32_THERMISTOR_TYPE_VAL_TEMP_THERMISTOR_44006\x10\x02\x12\x39\n5NIDMM_INT32_THERMISTOR_TYPE_VAL_TEMP_THERMISTOR_44007\x10\x03\x12L\nHNIDMM_INT32_THERMOCOUPLE_REFERENCE_JUNCTION_TYPE_VAL_TEMP_REF_JUNC_FIXED\x10\x02\x12/\n+NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_B\x10\x01\x12/\n+NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_E\x10\x04\x12/\n+NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_J\x10\x06\x12/\n+NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_K\x10\x07\x12/\n+NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_N\x10\x08\x12/\n+NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_R\x10\t\x12/\n+NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_S\x10\n\x12/\n+NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_T\x10\x0b\x12\x30\n,NIDMM_INT32_TRANSDUCER_TYPE_VAL_THERMOCOUPLE\x10\x01\x12.\n*NIDMM_INT32_TRANSDUCER_TYPE_VAL_THERMISTOR\x10\x02\x12.\n*NIDMM_INT32_TRANSDUCER_TYPE_VAL_2_WIRE_RTD\x10\x03\x12.\n*NIDMM_INT32_TRANSDUCER_TYPE_VAL_4_WIRE_RTD\x10\x04\x12\x35\n1NIDMM_INT32_TRIGGER_COUNT_VAL_TRIG_COUNT_INFINITE\x10\x00\x12*\n&NIDMM_INT32_TRIGGER_SLOPE_VAL_POSITIVE\x10\x00\x12*\n&NIDMM_INT32_TRIGGER_SLOPE_VAL_NEGATIVE\x10\x01\x12,\n(NIDMM_INT32_TRIGGER_SOURCE_VAL_IMMEDIATE\x10\x01\x12+\n\'NIDMM_INT32_TRIGGER_SOURCE_VAL_EXTERNAL\x10\x02\x12\x30\n,NIDMM_INT32_TRIGGER_SOURCE_VAL_SOFTWARE_TRIG\x10\x03\x12,\n(NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG0\x10o\x12,\n(NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG1\x10p\x12,\n(NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG2\x10q\x12,\n(NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG3\x10r\x12,\n(NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG4\x10s\x12,\n(NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG5\x10t\x12,\n(NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG6\x10u\x12,\n(NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG7\x10v\x12,\n\'NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_STAR\x10\x83\x01\x12-\n(NIDMM_INT32_TRIGGER_SOURCE_VAL_AUX_TRIG1\x10\xe9\x07\x12-\n(NIDMM_INT32_TRIGGER_SOURCE_VAL_LBR_TRIG1\x10\xec\x07\x12:\n6NIDMM_INT32_WAVEFORM_COUPLING_VAL_WAVEFORM_COUPLING_AC\x10\x00\x12:\n6NIDMM_INT32_WAVEFORM_COUPLING_VAL_WAVEFORM_COUPLING_DC\x10\x01\x1a\x02\x10\x01*\xac\x08\n\x1aNiDmmReal64AttributeValues\x12\x1c\n\x18NIDMM_REAL64_UNSPECIFIED\x10\x00\x12>\n1NIDMM_REAL64_APERTURE_TIME_VAL_APERTURE_TIME_AUTO\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12(\n$NIDMM_REAL64_APERTURE_TIME_VAL_1_PLC\x10\x01\x12(\n$NIDMM_REAL64_APERTURE_TIME_VAL_5_PLC\x10\x05\x12(\n$NIDMM_REAL64_APERTURE_TIME_VAL_6_PLC\x10\x06\x12)\n%NIDMM_REAL64_APERTURE_TIME_VAL_10_PLC\x10\n\x12)\n%NIDMM_REAL64_APERTURE_TIME_VAL_12_PLC\x10\x0c\x12*\n&NIDMM_REAL64_APERTURE_TIME_VAL_100_PLC\x10\x64\x12*\n&NIDMM_REAL64_APERTURE_TIME_VAL_120_PLC\x10x\x12\x43\n6NIDMM_REAL64_FREQUENCY_VOLTAGE_RANGE_VAL_AUTO_RANGE_ON\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x44\n7NIDMM_REAL64_FREQUENCY_VOLTAGE_RANGE_VAL_AUTO_RANGE_OFF\x10\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x34\n0NIDMM_REAL64_POWER_LINE_FREQUENCIES_VAL_50_HERTZ\x10\x32\x12\x34\n0NIDMM_REAL64_POWER_LINE_FREQUENCIES_VAL_60_HERTZ\x10<\x12\x31\n$NIDMM_REAL64_RANGE_VAL_AUTO_RANGE_ON\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x32\n%NIDMM_REAL64_RANGE_VAL_AUTO_RANGE_OFF\x10\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x33\n&NIDMM_REAL64_RANGE_VAL_AUTO_RANGE_ONCE\x10\xfd\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x38\n+NIDMM_REAL64_SAMPLE_INTERVAL_VAL_AUTO_DELAY\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12:\n-NIDMM_REAL64_SETTLE_TIME_VAL_SETTLE_TIME_AUTO\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12:\n-NIDMM_REAL64_TRIGGER_DELAYS_VAL_AUTO_DELAY_ON\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12;\n.NIDMM_REAL64_TRIGGER_DELAYS_VAL_AUTO_DELAY_OFF\x10\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01\x1a\x02\x10\x01*\xac\x03\n NiDmmReal64AttributeValuesMapped\x12#\n\x1fNIDMM_REAL64_MAPPED_UNSPECIFIED\x10\x00\x12.\n*NIDMM_REAL64_CURRENT_SOURCE_VAL_1_MICROAMP\x10\x01\x12/\n+NIDMM_REAL64_CURRENT_SOURCE_VAL_10_MICROAMP\x10\x02\x12\x30\n,NIDMM_REAL64_CURRENT_SOURCE_VAL_100_MICROAMP\x10\x03\x12.\n*NIDMM_REAL64_CURRENT_SOURCE_VAL_1_MILLIAMP\x10\x04\x12/\n+NIDMM_REAL64_INPUT_RESISTANCE_VAL_1_MEGAOHM\x10\x05\x12\x30\n,NIDMM_REAL64_INPUT_RESISTANCE_VAL_10_MEGAOHM\x10\x06\x12=\n9NIDMM_REAL64_INPUT_RESISTANCE_VAL_GREATER_THAN_10_GIGAOHM\x10\x07\x32\xe6\x44\n\x05NiDmm\x12\x39\n\x04Init\x12\x17.nidmm_grpc.InitRequest\x1a\x18.nidmm_grpc.InitResponse\x12Z\n\x0fInitWithOptions\x12\".nidmm_grpc.InitWithOptionsRequest\x1a#.nidmm_grpc.InitWithOptionsResponse\x12<\n\x05\x43lose\x12\x18.nidmm_grpc.CloseRequest\x1a\x19.nidmm_grpc.CloseResponse\x12\x45\n\x08GetError\x12\x1b.nidmm_grpc.GetErrorRequest\x1a\x1c.nidmm_grpc.GetErrorResponse\x12Z\n\x0fGetErrorMessage\x12\".nidmm_grpc.GetErrorMessageRequest\x1a#.nidmm_grpc.GetErrorMessageResponse\x12K\n\nClearError\x12\x1d.nidmm_grpc.ClearErrorRequest\x1a\x1e.nidmm_grpc.ClearErrorResponse\x12<\n\x05Reset\x12\x18.nidmm_grpc.ResetRequest\x1a\x19.nidmm_grpc.ResetResponse\x12\x45\n\x08SelfTest\x12\x1b.nidmm_grpc.SelfTestRequest\x1a\x1c.nidmm_grpc.SelfTestResponse\x12\x42\n\x07SelfCal\x12\x1a.nidmm_grpc.SelfCalRequest\x1a\x1b.nidmm_grpc.SelfCalResponse\x12T\n\rRevisionQuery\x12 .nidmm_grpc.RevisionQueryRequest\x1a!.nidmm_grpc.RevisionQueryResponse\x12`\n\x11ResetWithDefaults\x12$.nidmm_grpc.ResetWithDefaultsRequest\x1a%.nidmm_grpc.ResetWithDefaultsResponse\x12\x42\n\x07\x44isable\x12\x1a.nidmm_grpc.DisableRequest\x1a\x1b.nidmm_grpc.DisableResponse\x12i\n\x14GetMeasurementPeriod\x12\'.nidmm_grpc.GetMeasurementPeriodRequest\x1a(.nidmm_grpc.GetMeasurementPeriodResponse\x12]\n\x10\x43onfigureTrigger\x12#.nidmm_grpc.ConfigureTriggerRequest\x1a$.nidmm_grpc.ConfigureTriggerResponse\x12\x39\n\x04Read\x12\x17.nidmm_grpc.ReadRequest\x1a\x18.nidmm_grpc.ReadResponse\x12<\n\x05\x46\x65tch\x12\x18.nidmm_grpc.FetchRequest\x1a\x19.nidmm_grpc.FetchResponse\x12<\n\x05\x41\x62ort\x12\x18.nidmm_grpc.AbortRequest\x1a\x19.nidmm_grpc.AbortResponse\x12\x45\n\x08Initiate\x12\x1b.nidmm_grpc.InitiateRequest\x1a\x1c.nidmm_grpc.InitiateResponse\x12N\n\x0bIsOverRange\x12\x1e.nidmm_grpc.IsOverRangeRequest\x1a\x1f.nidmm_grpc.IsOverRangeResponse\x12Q\n\x0cIsUnderRange\x12\x1f.nidmm_grpc.IsUnderRangeRequest\x1a .nidmm_grpc.IsUnderRangeResponse\x12i\n\x14\x43onfigureACBandwidth\x12\'.nidmm_grpc.ConfigureACBandwidthRequest\x1a(.nidmm_grpc.ConfigureACBandwidthResponse\x12\x87\x01\n\x1e\x43onfigureFrequencyVoltageRange\x12\x31.nidmm_grpc.ConfigureFrequencyVoltageRangeRequest\x1a\x32.nidmm_grpc.ConfigureFrequencyVoltageRangeResponse\x12x\n\x19\x43onfigureMeasCompleteDest\x12,.nidmm_grpc.ConfigureMeasCompleteDestRequest\x1a-.nidmm_grpc.ConfigureMeasCompleteDestResponse\x12\x66\n\x13\x43onfigureMultiPoint\x12&.nidmm_grpc.ConfigureMultiPointRequest\x1a\'.nidmm_grpc.ConfigureMultiPointResponse\x12W\n\x0eReadMultiPoint\x12!.nidmm_grpc.ReadMultiPointRequest\x1a\".nidmm_grpc.ReadMultiPointResponse\x12Z\n\x0f\x46\x65tchMultiPoint\x12\".nidmm_grpc.FetchMultiPointRequest\x1a#.nidmm_grpc.FetchMultiPointResponse\x12l\n\x15\x43onfigureTriggerSlope\x12(.nidmm_grpc.ConfigureTriggerSlopeRequest\x1a).nidmm_grpc.ConfigureTriggerSlopeResponse\x12\x66\n\x13SendSoftwareTrigger\x12&.nidmm_grpc.SendSoftwareTriggerRequest\x1a\'.nidmm_grpc.SendSoftwareTriggerResponse\x12\x66\n\x13GetApertureTimeInfo\x12&.nidmm_grpc.GetApertureTimeInfoRequest\x1a\'.nidmm_grpc.GetApertureTimeInfoResponse\x12`\n\x11GetAutoRangeValue\x12$.nidmm_grpc.GetAutoRangeValueRequest\x1a%.nidmm_grpc.GetAutoRangeValueResponse\x12l\n\x15\x43onfigureAutoZeroMode\x12(.nidmm_grpc.ConfigureAutoZeroModeRequest\x1a).nidmm_grpc.ConfigureAutoZeroModeResponse\x12~\n\x1b\x43onfigurePowerLineFrequency\x12..nidmm_grpc.ConfigurePowerLineFrequencyRequest\x1a/.nidmm_grpc.ConfigurePowerLineFrequencyResponse\x12{\n\x1a\x43onfigureMeasurementDigits\x12-.nidmm_grpc.ConfigureMeasurementDigitsRequest\x1a..nidmm_grpc.ConfigureMeasurementDigitsResponse\x12\x81\x01\n\x1c\x43onfigureMeasurementAbsolute\x12/.nidmm_grpc.ConfigureMeasurementAbsoluteRequest\x1a\x30.nidmm_grpc.ConfigureMeasurementAbsoluteResponse\x12{\n\x1a\x43onfigureMeasCompleteSlope\x12-.nidmm_grpc.ConfigureMeasCompleteSlopeRequest\x1a..nidmm_grpc.ConfigureMeasCompleteSlopeResponse\x12~\n\x1b\x43onfigureSampleTriggerSlope\x12..nidmm_grpc.ConfigureSampleTriggerSlopeRequest\x1a/.nidmm_grpc.ConfigureSampleTriggerSlopeResponse\x12K\n\nReadStatus\x12\x1d.nidmm_grpc.ReadStatusRequest\x1a\x1e.nidmm_grpc.ReadStatusResponse\x12\x42\n\x07\x43ontrol\x12\x1a.nidmm_grpc.ControlRequest\x1a\x1b.nidmm_grpc.ControlResponse\x12r\n\x17\x43onfigureADCCalibration\x12*.nidmm_grpc.ConfigureADCCalibrationRequest\x1a+.nidmm_grpc.ConfigureADCCalibrationResponse\x12r\n\x17\x43onfigureOffsetCompOhms\x12*.nidmm_grpc.ConfigureOffsetCompOhmsRequest\x1a+.nidmm_grpc.ConfigureOffsetCompOhmsResponse\x12o\n\x16\x43onfigureCurrentSource\x12).nidmm_grpc.ConfigureCurrentSourceRequest\x1a*.nidmm_grpc.ConfigureCurrentSourceResponse\x12o\n\x16\x43onfigureCableCompType\x12).nidmm_grpc.ConfigureCableCompTypeRequest\x1a*.nidmm_grpc.ConfigureCableCompTypeResponse\x12i\n\x14PerformOpenCableComp\x12\'.nidmm_grpc.PerformOpenCableCompRequest\x1a(.nidmm_grpc.PerformOpenCableCompResponse\x12l\n\x15PerformShortCableComp\x12(.nidmm_grpc.PerformShortCableCompRequest\x1a).nidmm_grpc.PerformShortCableCompResponse\x12\x81\x01\n\x1c\x43onfigureOpenCableCompValues\x12/.nidmm_grpc.ConfigureOpenCableCompValuesRequest\x1a\x30.nidmm_grpc.ConfigureOpenCableCompValuesResponse\x12\x84\x01\n\x1d\x43onfigureShortCableCompValues\x12\x30.nidmm_grpc.ConfigureShortCableCompValuesRequest\x1a\x31.nidmm_grpc.ConfigureShortCableCompValuesResponse\x12\x81\x01\n\x1c\x43onfigureWaveformAcquisition\x12/.nidmm_grpc.ConfigureWaveformAcquisitionRequest\x1a\x30.nidmm_grpc.ConfigureWaveformAcquisitionResponse\x12x\n\x19\x43onfigureWaveformCoupling\x12,.nidmm_grpc.ConfigureWaveformCouplingRequest\x1a-.nidmm_grpc.ConfigureWaveformCouplingResponse\x12T\n\rFetchWaveform\x12 .nidmm_grpc.FetchWaveformRequest\x1a!.nidmm_grpc.FetchWaveformResponse\x12Q\n\x0cReadWaveform\x12\x1f.nidmm_grpc.ReadWaveformRequest\x1a .nidmm_grpc.ReadWaveformResponse\x12\x66\n\x13GetAttributeViInt32\x12&.nidmm_grpc.GetAttributeViInt32Request\x1a\'.nidmm_grpc.GetAttributeViInt32Response\x12\x66\n\x13SetAttributeViInt32\x12&.nidmm_grpc.SetAttributeViInt32Request\x1a\'.nidmm_grpc.SetAttributeViInt32Response\x12l\n\x15\x43heckAttributeViInt32\x12(.nidmm_grpc.CheckAttributeViInt32Request\x1a).nidmm_grpc.CheckAttributeViInt32Response\x12i\n\x14GetAttributeViReal64\x12\'.nidmm_grpc.GetAttributeViReal64Request\x1a(.nidmm_grpc.GetAttributeViReal64Response\x12i\n\x14SetAttributeViReal64\x12\'.nidmm_grpc.SetAttributeViReal64Request\x1a(.nidmm_grpc.SetAttributeViReal64Response\x12o\n\x16\x43heckAttributeViReal64\x12).nidmm_grpc.CheckAttributeViReal64Request\x1a*.nidmm_grpc.CheckAttributeViReal64Response\x12i\n\x14GetAttributeViString\x12\'.nidmm_grpc.GetAttributeViStringRequest\x1a(.nidmm_grpc.GetAttributeViStringResponse\x12i\n\x14SetAttributeViString\x12\'.nidmm_grpc.SetAttributeViStringRequest\x1a(.nidmm_grpc.SetAttributeViStringResponse\x12o\n\x16\x43heckAttributeViString\x12).nidmm_grpc.CheckAttributeViStringRequest\x1a*.nidmm_grpc.CheckAttributeViStringResponse\x12l\n\x15GetAttributeViSession\x12(.nidmm_grpc.GetAttributeViSessionRequest\x1a).nidmm_grpc.GetAttributeViSessionResponse\x12l\n\x15SetAttributeViSession\x12(.nidmm_grpc.SetAttributeViSessionRequest\x1a).nidmm_grpc.SetAttributeViSessionResponse\x12r\n\x17\x43heckAttributeViSession\x12*.nidmm_grpc.CheckAttributeViSessionRequest\x1a+.nidmm_grpc.CheckAttributeViSessionResponse\x12l\n\x15GetAttributeViBoolean\x12(.nidmm_grpc.GetAttributeViBooleanRequest\x1a).nidmm_grpc.GetAttributeViBooleanResponse\x12l\n\x15SetAttributeViBoolean\x12(.nidmm_grpc.SetAttributeViBooleanRequest\x1a).nidmm_grpc.SetAttributeViBooleanResponse\x12r\n\x17\x43heckAttributeViBoolean\x12*.nidmm_grpc.CheckAttributeViBooleanRequest\x1a+.nidmm_grpc.CheckAttributeViBooleanResponse\x12\x8d\x01\n ImportAttributeConfigurationFile\x12\x33.nidmm_grpc.ImportAttributeConfigurationFileRequest\x1a\x34.nidmm_grpc.ImportAttributeConfigurationFileResponse\x12\x8d\x01\n ExportAttributeConfigurationFile\x12\x33.nidmm_grpc.ExportAttributeConfigurationFileRequest\x1a\x34.nidmm_grpc.ExportAttributeConfigurationFileResponse\x12\x93\x01\n\"ImportAttributeConfigurationBuffer\x12\x35.nidmm_grpc.ImportAttributeConfigurationBufferRequest\x1a\x36.nidmm_grpc.ImportAttributeConfigurationBufferResponse\x12\x93\x01\n\"ExportAttributeConfigurationBuffer\x12\x35.nidmm_grpc.ExportAttributeConfigurationBufferRequest\x1a\x36.nidmm_grpc.ExportAttributeConfigurationBufferResponse\x12l\n\x15ResetInterchangeCheck\x12(.nidmm_grpc.ResetInterchangeCheckRequest\x1a).nidmm_grpc.ResetInterchangeCheckResponse\x12u\n\x18\x43learInterchangeWarnings\x12+.nidmm_grpc.ClearInterchangeWarningsRequest\x1a,.nidmm_grpc.ClearInterchangeWarningsResponse\x12W\n\x0eGetChannelName\x12!.nidmm_grpc.GetChannelNameRequest\x1a\".nidmm_grpc.GetChannelNameResponse\x12\x81\x01\n\x1cGetExtCalRecommendedInterval\x12/.nidmm_grpc.GetExtCalRecommendedIntervalRequest\x1a\x30.nidmm_grpc.GetExtCalRecommendedIntervalResponse\x12\x66\n\x13GetSelfCalSupported\x12&.nidmm_grpc.GetSelfCalSupportedRequest\x1a\'.nidmm_grpc.GetSelfCalSupportedResponse\x12`\n\x11GetCalDateAndTime\x12$.nidmm_grpc.GetCalDateAndTimeRequest\x1a%.nidmm_grpc.GetCalDateAndTimeResponse\x12W\n\x0eGetLastCalTemp\x12!.nidmm_grpc.GetLastCalTempRequest\x1a\".nidmm_grpc.GetLastCalTempResponse\x12K\n\nGetDevTemp\x12\x1d.nidmm_grpc.GetDevTempRequest\x1a\x1e.nidmm_grpc.GetDevTempResponse\x12r\n\x17\x43onfigureTransducerType\x12*.nidmm_grpc.ConfigureTransducerTypeRequest\x1a+.nidmm_grpc.ConfigureTransducerTypeResponse\x12l\n\x15\x43onfigureThermocouple\x12(.nidmm_grpc.ConfigureThermocoupleRequest\x1a).nidmm_grpc.ConfigureThermocoupleResponse\x12x\n\x19\x43onfigureFixedRefJunction\x12,.nidmm_grpc.ConfigureFixedRefJunctionRequest\x1a-.nidmm_grpc.ConfigureFixedRefJunctionResponse\x12]\n\x10\x43onfigureRTDType\x12#.nidmm_grpc.ConfigureRTDTypeRequest\x1a$.nidmm_grpc.ConfigureRTDTypeResponse\x12\x63\n\x12\x43onfigureRTDCustom\x12%.nidmm_grpc.ConfigureRTDCustomRequest\x1a&.nidmm_grpc.ConfigureRTDCustomResponse\x12r\n\x17\x43onfigureThermistorType\x12*.nidmm_grpc.ConfigureThermistorTypeRequest\x1a+.nidmm_grpc.ConfigureThermistorTypeResponse\x12x\n\x19\x43onfigureThermistorCustom\x12,.nidmm_grpc.ConfigureThermistorCustomRequest\x1a-.nidmm_grpc.ConfigureThermistorCustomResponse\x12r\n\x17InvalidateAllAttributes\x12*.nidmm_grpc.InvalidateAllAttributesRequest\x1a+.nidmm_grpc.InvalidateAllAttributesResponseB9\n\x0f\x63om.ni.grpc.dmmB\x05NiDmmP\x01\xaa\x02\x1cNationalInstruments.Grpc.Dmmb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nidmm_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017com.ni.grpc.dmmB\005NiDmmP\001\252\002\034NationalInstruments.Grpc.Dmm'
  _NIDMMINT32ATTRIBUTEVALUES._options = None
  _NIDMMINT32ATTRIBUTEVALUES._serialized_options = b'\020\001'
  _NIDMMREAL64ATTRIBUTEVALUES._options = None
  _NIDMMREAL64ATTRIBUTEVALUES._serialized_options = b'\020\001'
  _INITRESPONSE.fields_by_name['error_message']._options = None
  _INITRESPONSE.fields_by_name['error_message']._serialized_options = b'\030\001'
  _INITWITHOPTIONSRESPONSE.fields_by_name['error_message']._options = None
  _INITWITHOPTIONSRESPONSE.fields_by_name['error_message']._serialized_options = b'\030\001'
  _globals['_NIDMMATTRIBUTE']._serialized_start=17041
  _globals['_NIDMMATTRIBUTE']._serialized_end=20507
  _globals['_FUNCTION']._serialized_start=20510
  _globals['_FUNCTION']._serialized_end=21081
  _globals['_TRIGGERSOURCE']._serialized_start=21084
  _globals['_TRIGGERSOURCE']._serialized_end=21696
  _globals['_SAMPLETRIGGER']._serialized_start=21699
  _globals['_SAMPLETRIGGER']._serialized_end=22350
  _globals['_TRIGGERSLOPE']._serialized_start=22352
  _globals['_TRIGGERSLOPE']._serialized_end=22442
  _globals['_SAMPLETRIGSLOPE']._serialized_start=22444
  _globals['_SAMPLETRIGSLOPE']._serialized_end=22545
  _globals['_POWERLINEFREQUENCIES']._serialized_start=22548
  _globals['_POWERLINEFREQUENCIES']._serialized_end=22704
  _globals['_APERTURETIMEUNITS']._serialized_start=22706
  _globals['_APERTURETIMEUNITS']._serialized_end=22821
  _globals['_COMPENSATEDOHMS']._serialized_start=22823
  _globals['_COMPENSATEDOHMS']._serialized_end=22945
  _globals['_CALIBRATIONTYPE']._serialized_start=22947
  _globals['_CALIBRATIONTYPE']._serialized_end=23056
  _globals['_THERMOCOUPLEREFERENCEJUNCTIONTYPE']._serialized_start=23059
  _globals['_THERMOCOUPLEREFERENCEJUNCTIONTYPE']._serialized_end=23220
  _globals['_THERMOCOUPLETYPE']._serialized_start=23223
  _globals['_THERMOCOUPLETYPE']._serialized_end=23620
  _globals['_RTDTYPE']._serialized_start=23623
  _globals['_RTDTYPE']._serialized_end=23912
  _globals['_ACQUISITIONSTATUS']._serialized_start=23915
  _globals['_ACQUISITIONSTATUS']._serialized_end=24207
  _globals['_APERTURETIME']._serialized_start=24210
  _globals['_APERTURETIME']._serialized_end=24563
  _globals['_CONTROLCOMMIT']._serialized_start=24565
  _globals['_CONTROLCOMMIT']._serialized_end=24625
  _globals['_FREQUENCYVOLTAGERANGE']._serialized_start=24628
  _globals['_FREQUENCYVOLTAGERANGE']._serialized_end=24817
  _globals['_SAMPLECOUNT']._serialized_start=24819
  _globals['_SAMPLECOUNT']._serialized_end=24882
  _globals['_SAMPLEINTERVAL']._serialized_start=24884
  _globals['_SAMPLEINTERVAL']._serialized_end=24984
  _globals['_TIMELIMIT']._serialized_start=24986
  _globals['_TIMELIMIT']._serialized_end=25076
  _globals['_TRIGGERCOUNT']._serialized_start=25078
  _globals['_TRIGGERCOUNT']._serialized_end=25141
  _globals['_TRIGGERDELAYS']._serialized_start=25144
  _globals['_TRIGGERDELAYS']._serialized_end=25298
  _globals['_NIDMMINT32ATTRIBUTEVALUES']._serialized_start=25301
  _globals['_NIDMMINT32ATTRIBUTEVALUES']._serialized_end=31271
  _globals['_NIDMMREAL64ATTRIBUTEVALUES']._serialized_start=31274
  _globals['_NIDMMREAL64ATTRIBUTEVALUES']._serialized_end=32342
  _globals['_NIDMMREAL64ATTRIBUTEVALUESMAPPED']._serialized_start=32345
  _globals['_NIDMMREAL64ATTRIBUTEVALUESMAPPED']._serialized_end=32773
  _globals['_INITREQUEST']._serialized_start=43
  _globals['_INITREQUEST']._serialized_end=220
  _globals['_INITRESPONSE']._serialized_start=222
  _globals['_INITRESPONSE']._serialized_end=348
  _globals['_INITWITHOPTIONSREQUEST']._serialized_start=351
  _globals['_INITWITHOPTIONSREQUEST']._serialized_end=562
  _globals['_INITWITHOPTIONSRESPONSE']._serialized_start=565
  _globals['_INITWITHOPTIONSRESPONSE']._serialized_end=702
  _globals['_CLOSEREQUEST']._serialized_start=704
  _globals['_CLOSEREQUEST']._serialized_end=754
  _globals['_CLOSERESPONSE']._serialized_start=756
  _globals['_CLOSERESPONSE']._serialized_end=787
  _globals['_GETERRORREQUEST']._serialized_start=789
  _globals['_GETERRORREQUEST']._serialized_end=842
  _globals['_GETERRORRESPONSE']._serialized_start=844
  _globals['_GETERRORRESPONSE']._serialized_end=919
  _globals['_GETERRORMESSAGEREQUEST']._serialized_start=921
  _globals['_GETERRORMESSAGEREQUEST']._serialized_end=1001
  _globals['_GETERRORMESSAGERESPONSE']._serialized_start=1003
  _globals['_GETERRORMESSAGERESPONSE']._serialized_end=1067
  _globals['_CLEARERRORREQUEST']._serialized_start=1069
  _globals['_CLEARERRORREQUEST']._serialized_end=1124
  _globals['_CLEARERRORRESPONSE']._serialized_start=1126
  _globals['_CLEARERRORRESPONSE']._serialized_end=1162
  _globals['_RESETREQUEST']._serialized_start=1164
  _globals['_RESETREQUEST']._serialized_end=1214
  _globals['_RESETRESPONSE']._serialized_start=1216
  _globals['_RESETRESPONSE']._serialized_end=1247
  _globals['_SELFTESTREQUEST']._serialized_start=1249
  _globals['_SELFTESTREQUEST']._serialized_end=1302
  _globals['_SELFTESTRESPONSE']._serialized_start=1304
  _globals['_SELFTESTRESPONSE']._serialized_end=1391
  _globals['_SELFCALREQUEST']._serialized_start=1393
  _globals['_SELFCALREQUEST']._serialized_end=1445
  _globals['_SELFCALRESPONSE']._serialized_start=1447
  _globals['_SELFCALRESPONSE']._serialized_end=1480
  _globals['_REVISIONQUERYREQUEST']._serialized_start=1482
  _globals['_REVISIONQUERYREQUEST']._serialized_end=1540
  _globals['_REVISIONQUERYRESPONSE']._serialized_start=1542
  _globals['_REVISIONQUERYRESPONSE']._serialized_end=1644
  _globals['_RESETWITHDEFAULTSREQUEST']._serialized_start=1646
  _globals['_RESETWITHDEFAULTSREQUEST']._serialized_end=1708
  _globals['_RESETWITHDEFAULTSRESPONSE']._serialized_start=1710
  _globals['_RESETWITHDEFAULTSRESPONSE']._serialized_end=1753
  _globals['_DISABLEREQUEST']._serialized_start=1755
  _globals['_DISABLEREQUEST']._serialized_end=1807
  _globals['_DISABLERESPONSE']._serialized_start=1809
  _globals['_DISABLERESPONSE']._serialized_end=1842
  _globals['_GETMEASUREMENTPERIODREQUEST']._serialized_start=1844
  _globals['_GETMEASUREMENTPERIODREQUEST']._serialized_end=1909
  _globals['_GETMEASUREMENTPERIODRESPONSE']._serialized_start=1911
  _globals['_GETMEASUREMENTPERIODRESPONSE']._serialized_end=1973
  _globals['_CONFIGURETRIGGERREQUEST']._serialized_start=1976
  _globals['_CONFIGURETRIGGERREQUEST']._serialized_end=2246
  _globals['_CONFIGURETRIGGERRESPONSE']._serialized_start=2248
  _globals['_CONFIGURETRIGGERRESPONSE']._serialized_end=2290
  _globals['_READREQUEST']._serialized_start=2293
  _globals['_READREQUEST']._serialized_end=2438
  _globals['_READRESPONSE']._serialized_start=2440
  _globals['_READRESPONSE']._serialized_end=2487
  _globals['_FETCHREQUEST']._serialized_start=2490
  _globals['_FETCHREQUEST']._serialized_end=2636
  _globals['_FETCHRESPONSE']._serialized_start=2638
  _globals['_FETCHRESPONSE']._serialized_end=2686
  _globals['_ABORTREQUEST']._serialized_start=2688
  _globals['_ABORTREQUEST']._serialized_end=2738
  _globals['_ABORTRESPONSE']._serialized_start=2740
  _globals['_ABORTRESPONSE']._serialized_end=2771
  _globals['_INITIATEREQUEST']._serialized_start=2773
  _globals['_INITIATEREQUEST']._serialized_end=2826
  _globals['_INITIATERESPONSE']._serialized_start=2828
  _globals['_INITIATERESPONSE']._serialized_end=2862
  _globals['_ISOVERRANGEREQUEST']._serialized_start=2864
  _globals['_ISOVERRANGEREQUEST']._serialized_end=2947
  _globals['_ISOVERRANGERESPONSE']._serialized_start=2949
  _globals['_ISOVERRANGERESPONSE']._serialized_end=3009
  _globals['_ISUNDERRANGEREQUEST']._serialized_start=3011
  _globals['_ISUNDERRANGEREQUEST']._serialized_end=3095
  _globals['_ISUNDERRANGERESPONSE']._serialized_start=3097
  _globals['_ISUNDERRANGERESPONSE']._serialized_end=3159
  _globals['_CONFIGUREACBANDWIDTHREQUEST']._serialized_start=3162
  _globals['_CONFIGUREACBANDWIDTHREQUEST']._serialized_end=3293
  _globals['_CONFIGUREACBANDWIDTHRESPONSE']._serialized_start=3295
  _globals['_CONFIGUREACBANDWIDTHRESPONSE']._serialized_end=3341
  _globals['_CONFIGUREFREQUENCYVOLTAGERANGEREQUEST']._serialized_start=3344
  _globals['_CONFIGUREFREQUENCYVOLTAGERANGEREQUEST']._serialized_end=3530
  _globals['_CONFIGUREFREQUENCYVOLTAGERANGERESPONSE']._serialized_start=3532
  _globals['_CONFIGUREFREQUENCYVOLTAGERANGERESPONSE']._serialized_end=3588
  _globals['_CONFIGUREMEASCOMPLETEDESTREQUEST']._serialized_start=3590
  _globals['_CONFIGUREMEASCOMPLETEDESTREQUEST']._serialized_end=3695
  _globals['_CONFIGUREMEASCOMPLETEDESTRESPONSE']._serialized_start=3697
  _globals['_CONFIGUREMEASCOMPLETEDESTRESPONSE']._serialized_end=3748
  _globals['_CONFIGUREMULTIPOINTREQUEST']._serialized_start=3751
  _globals['_CONFIGUREMULTIPOINTREQUEST']._serialized_end=4231
  _globals['_CONFIGUREMULTIPOINTRESPONSE']._serialized_start=4233
  _globals['_CONFIGUREMULTIPOINTRESPONSE']._serialized_end=4278
  _globals['_READMULTIPOINTREQUEST']._serialized_start=4281
  _globals['_READMULTIPOINTREQUEST']._serialized_end=4456
  _globals['_READMULTIPOINTRESPONSE']._serialized_start=4458
  _globals['_READMULTIPOINTRESPONSE']._serialized_end=4554
  _globals['_FETCHMULTIPOINTREQUEST']._serialized_start=4557
  _globals['_FETCHMULTIPOINTREQUEST']._serialized_end=4733
  _globals['_FETCHMULTIPOINTRESPONSE']._serialized_start=4735
  _globals['_FETCHMULTIPOINTRESPONSE']._serialized_end=4832
  _globals['_CONFIGURETRIGGERSLOPEREQUEST']._serialized_start=4835
  _globals['_CONFIGURETRIGGERSLOPEREQUEST']._serialized_end=5003
  _globals['_CONFIGURETRIGGERSLOPERESPONSE']._serialized_start=5005
  _globals['_CONFIGURETRIGGERSLOPERESPONSE']._serialized_end=5052
  _globals['_SENDSOFTWARETRIGGERREQUEST']._serialized_start=5054
  _globals['_SENDSOFTWARETRIGGERREQUEST']._serialized_end=5118
  _globals['_SENDSOFTWARETRIGGERRESPONSE']._serialized_start=5120
  _globals['_SENDSOFTWARETRIGGERRESPONSE']._serialized_end=5165
  _globals['_GETAPERTURETIMEINFOREQUEST']._serialized_start=5167
  _globals['_GETAPERTURETIMEINFOREQUEST']._serialized_end=5231
  _globals['_GETAPERTURETIMEINFORESPONSE']._serialized_start=5234
  _globals['_GETAPERTURETIMEINFORESPONSE']._serialized_end=5448
  _globals['_GETAUTORANGEVALUEREQUEST']._serialized_start=5450
  _globals['_GETAUTORANGEVALUEREQUEST']._serialized_end=5512
  _globals['_GETAUTORANGEVALUERESPONSE']._serialized_start=5514
  _globals['_GETAUTORANGEVALUERESPONSE']._serialized_end=5579
  _globals['_CONFIGUREAUTOZEROMODEREQUEST']._serialized_start=5581
  _globals['_CONFIGUREAUTOZEROMODEREQUEST']._serialized_end=5671
  _globals['_CONFIGUREAUTOZEROMODERESPONSE']._serialized_start=5673
  _globals['_CONFIGUREAUTOZEROMODERESPONSE']._serialized_end=5720
  _globals['_CONFIGUREPOWERLINEFREQUENCYREQUEST']._serialized_start=5723
  _globals['_CONFIGUREPOWERLINEFREQUENCYREQUEST']._serialized_end=5935
  _globals['_CONFIGUREPOWERLINEFREQUENCYRESPONSE']._serialized_start=5937
  _globals['_CONFIGUREPOWERLINEFREQUENCYRESPONSE']._serialized_end=5990
  _globals['_CONFIGUREMEASUREMENTDIGITSREQUEST']._serialized_start=5993
  _globals['_CONFIGUREMEASUREMENTDIGITSREQUEST']._serialized_end=6225
  _globals['_CONFIGUREMEASUREMENTDIGITSRESPONSE']._serialized_start=6227
  _globals['_CONFIGUREMEASUREMENTDIGITSRESPONSE']._serialized_end=6279
  _globals['_CONFIGUREMEASUREMENTABSOLUTEREQUEST']._serialized_start=6282
  _globals['_CONFIGUREMEASUREMENTABSOLUTEREQUEST']._serialized_end=6518
  _globals['_CONFIGUREMEASUREMENTABSOLUTERESPONSE']._serialized_start=6520
  _globals['_CONFIGUREMEASUREMENTABSOLUTERESPONSE']._serialized_end=6574
  _globals['_CONFIGUREMEASCOMPLETESLOPEREQUEST']._serialized_start=6576
  _globals['_CONFIGUREMEASCOMPLETESLOPEREQUEST']._serialized_end=6676
  _globals['_CONFIGUREMEASCOMPLETESLOPERESPONSE']._serialized_start=6678
  _globals['_CONFIGUREMEASCOMPLETESLOPERESPONSE']._serialized_end=6730
  _globals['_CONFIGURESAMPLETRIGGERSLOPEREQUEST']._serialized_start=6733
  _globals['_CONFIGURESAMPLETRIGGERSLOPEREQUEST']._serialized_end=6931
  _globals['_CONFIGURESAMPLETRIGGERSLOPERESPONSE']._serialized_start=6933
  _globals['_CONFIGURESAMPLETRIGGERSLOPERESPONSE']._serialized_end=6986
  _globals['_READSTATUSREQUEST']._serialized_start=6988
  _globals['_READSTATUSREQUEST']._serialized_end=7043
  _globals['_READSTATUSRESPONSE']._serialized_start=7046
  _globals['_READSTATUSRESPONSE']._serialized_end=7202
  _globals['_CONTROLREQUEST']._serialized_start=7205
  _globals['_CONTROLREQUEST']._serialized_end=7363
  _globals['_CONTROLRESPONSE']._serialized_start=7365
  _globals['_CONTROLRESPONSE']._serialized_end=7398
  _globals['_CONFIGUREADCCALIBRATIONREQUEST']._serialized_start=7400
  _globals['_CONFIGUREADCCALIBRATIONREQUEST']._serialized_end=7493
  _globals['_CONFIGUREADCCALIBRATIONRESPONSE']._serialized_start=7495
  _globals['_CONFIGUREADCCALIBRATIONRESPONSE']._serialized_end=7544
  _globals['_CONFIGUREOFFSETCOMPOHMSREQUEST']._serialized_start=7547
  _globals['_CONFIGUREOFFSETCOMPOHMSREQUEST']._serialized_end=7729
  _globals['_CONFIGUREOFFSETCOMPOHMSRESPONSE']._serialized_start=7731
  _globals['_CONFIGUREOFFSETCOMPOHMSRESPONSE']._serialized_end=7780
  _globals['_CONFIGURECURRENTSOURCEREQUEST']._serialized_start=7782
  _globals['_CONFIGURECURRENTSOURCEREQUEST']._serialized_end=7873
  _globals['_CONFIGURECURRENTSOURCERESPONSE']._serialized_start=7875
  _globals['_CONFIGURECURRENTSOURCERESPONSE']._serialized_end=7923
  _globals['_CONFIGURECABLECOMPTYPEREQUEST']._serialized_start=7925
  _globals['_CONFIGURECABLECOMPTYPEREQUEST']._serialized_end=8017
  _globals['_CONFIGURECABLECOMPTYPERESPONSE']._serialized_start=8019
  _globals['_CONFIGURECABLECOMPTYPERESPONSE']._serialized_end=8067
  _globals['_PERFORMOPENCABLECOMPREQUEST']._serialized_start=8069
  _globals['_PERFORMOPENCABLECOMPREQUEST']._serialized_end=8134
  _globals['_PERFORMOPENCABLECOMPRESPONSE']._serialized_start=8136
  _globals['_PERFORMOPENCABLECOMPRESPONSE']._serialized_end=8224
  _globals['_PERFORMSHORTCABLECOMPREQUEST']._serialized_start=8226
  _globals['_PERFORMSHORTCABLECOMPREQUEST']._serialized_end=8292
  _globals['_PERFORMSHORTCABLECOMPRESPONSE']._serialized_start=8294
  _globals['_PERFORMSHORTCABLECOMPRESPONSE']._serialized_end=8380
  _globals['_CONFIGUREOPENCABLECOMPVALUESREQUEST']._serialized_start=8382
  _globals['_CONFIGUREOPENCABLECOMPVALUESREQUEST']._serialized_end=8497
  _globals['_CONFIGUREOPENCABLECOMPVALUESRESPONSE']._serialized_start=8499
  _globals['_CONFIGUREOPENCABLECOMPVALUESRESPONSE']._serialized_end=8553
  _globals['_CONFIGURESHORTCABLECOMPVALUESREQUEST']._serialized_start=8555
  _globals['_CONFIGURESHORTCABLECOMPVALUESREQUEST']._serialized_end=8668
  _globals['_CONFIGURESHORTCABLECOMPVALUESRESPONSE']._serialized_start=8670
  _globals['_CONFIGURESHORTCABLECOMPVALUESRESPONSE']._serialized_end=8725
  _globals['_CONFIGUREWAVEFORMACQUISITIONREQUEST']._serialized_start=8728
  _globals['_CONFIGUREWAVEFORMACQUISITIONREQUEST']._serialized_end=8974
  _globals['_CONFIGUREWAVEFORMACQUISITIONRESPONSE']._serialized_start=8976
  _globals['_CONFIGUREWAVEFORMACQUISITIONRESPONSE']._serialized_end=9030
  _globals['_CONFIGUREWAVEFORMCOUPLINGREQUEST']._serialized_start=9032
  _globals['_CONFIGUREWAVEFORMCOUPLINGREQUEST']._serialized_end=9129
  _globals['_CONFIGUREWAVEFORMCOUPLINGRESPONSE']._serialized_start=9131
  _globals['_CONFIGUREWAVEFORMCOUPLINGRESPONSE']._serialized_end=9182
  _globals['_FETCHWAVEFORMREQUEST']._serialized_start=9185
  _globals['_FETCHWAVEFORMREQUEST']._serialized_end=9359
  _globals['_FETCHWAVEFORMRESPONSE']._serialized_start=9361
  _globals['_FETCHWAVEFORMRESPONSE']._serialized_end=9457
  _globals['_READWAVEFORMREQUEST']._serialized_start=9460
  _globals['_READWAVEFORMREQUEST']._serialized_end=9633
  _globals['_READWAVEFORMRESPONSE']._serialized_start=9635
  _globals['_READWAVEFORMRESPONSE']._serialized_end=9730
  _globals['_GETATTRIBUTEVIINT32REQUEST']._serialized_start=9733
  _globals['_GETATTRIBUTEVIINT32REQUEST']._serialized_end=9869
  _globals['_GETATTRIBUTEVIINT32RESPONSE']._serialized_start=9871
  _globals['_GETATTRIBUTEVIINT32RESPONSE']._serialized_end=9941
  _globals['_SETATTRIBUTEVIINT32REQUEST']._serialized_start=9944
  _globals['_SETATTRIBUTEVIINT32REQUEST']._serialized_end=10201
  _globals['_SETATTRIBUTEVIINT32RESPONSE']._serialized_start=10203
  _globals['_SETATTRIBUTEVIINT32RESPONSE']._serialized_end=10248
  _globals['_CHECKATTRIBUTEVIINT32REQUEST']._serialized_start=10251
  _globals['_CHECKATTRIBUTEVIINT32REQUEST']._serialized_end=10510
  _globals['_CHECKATTRIBUTEVIINT32RESPONSE']._serialized_start=10512
  _globals['_CHECKATTRIBUTEVIINT32RESPONSE']._serialized_end=10559
  _globals['_GETATTRIBUTEVIREAL64REQUEST']._serialized_start=10562
  _globals['_GETATTRIBUTEVIREAL64REQUEST']._serialized_end=10699
  _globals['_GETATTRIBUTEVIREAL64RESPONSE']._serialized_start=10701
  _globals['_GETATTRIBUTEVIREAL64RESPONSE']._serialized_end=10772
  _globals['_SETATTRIBUTEVIREAL64REQUEST']._serialized_start=10775
  _globals['_SETATTRIBUTEVIREAL64REQUEST']._serialized_end=11114
  _globals['_SETATTRIBUTEVIREAL64RESPONSE']._serialized_start=11116
  _globals['_SETATTRIBUTEVIREAL64RESPONSE']._serialized_end=11162
  _globals['_CHECKATTRIBUTEVIREAL64REQUEST']._serialized_start=11165
  _globals['_CHECKATTRIBUTEVIREAL64REQUEST']._serialized_end=11506
  _globals['_CHECKATTRIBUTEVIREAL64RESPONSE']._serialized_start=11508
  _globals['_CHECKATTRIBUTEVIREAL64RESPONSE']._serialized_end=11556
  _globals['_GETATTRIBUTEVISTRINGREQUEST']._serialized_start=11559
  _globals['_GETATTRIBUTEVISTRINGREQUEST']._serialized_end=11696
  _globals['_GETATTRIBUTEVISTRINGRESPONSE']._serialized_start=11698
  _globals['_GETATTRIBUTEVISTRINGRESPONSE']._serialized_end=11769
  _globals['_SETATTRIBUTEVISTRINGREQUEST']._serialized_start=11772
  _globals['_SETATTRIBUTEVISTRINGREQUEST']._serialized_end=11938
  _globals['_SETATTRIBUTEVISTRINGRESPONSE']._serialized_start=11940
  _globals['_SETATTRIBUTEVISTRINGRESPONSE']._serialized_end=11986
  _globals['_CHECKATTRIBUTEVISTRINGREQUEST']._serialized_start=11989
  _globals['_CHECKATTRIBUTEVISTRINGREQUEST']._serialized_end=12157
  _globals['_CHECKATTRIBUTEVISTRINGRESPONSE']._serialized_start=12159
  _globals['_CHECKATTRIBUTEVISTRINGRESPONSE']._serialized_end=12207
  _globals['_GETATTRIBUTEVISESSIONREQUEST']._serialized_start=12210
  _globals['_GETATTRIBUTEVISESSIONREQUEST']._serialized_end=12348
  _globals['_GETATTRIBUTEVISESSIONRESPONSE']._serialized_start=12350
  _globals['_GETATTRIBUTEVISESSIONRESPONSE']._serialized_end=12446
  _globals['_SETATTRIBUTEVISESSIONREQUEST']._serialized_start=12449
  _globals['_SETATTRIBUTEVISESSIONREQUEST']._serialized_end=12636
  _globals['_SETATTRIBUTEVISESSIONRESPONSE']._serialized_start=12638
  _globals['_SETATTRIBUTEVISESSIONRESPONSE']._serialized_end=12685
  _globals['_CHECKATTRIBUTEVISESSIONREQUEST']._serialized_start=12688
  _globals['_CHECKATTRIBUTEVISESSIONREQUEST']._serialized_end=12877
  _globals['_CHECKATTRIBUTEVISESSIONRESPONSE']._serialized_start=12879
  _globals['_CHECKATTRIBUTEVISESSIONRESPONSE']._serialized_end=12928
  _globals['_GETATTRIBUTEVIBOOLEANREQUEST']._serialized_start=12931
  _globals['_GETATTRIBUTEVIBOOLEANREQUEST']._serialized_end=13069
  _globals['_GETATTRIBUTEVIBOOLEANRESPONSE']._serialized_start=13071
  _globals['_GETATTRIBUTEVIBOOLEANRESPONSE']._serialized_end=13143
  _globals['_SETATTRIBUTEVIBOOLEANREQUEST']._serialized_start=13146
  _globals['_SETATTRIBUTEVIBOOLEANREQUEST']._serialized_end=13309
  _globals['_SETATTRIBUTEVIBOOLEANRESPONSE']._serialized_start=13311
  _globals['_SETATTRIBUTEVIBOOLEANRESPONSE']._serialized_end=13358
  _globals['_CHECKATTRIBUTEVIBOOLEANREQUEST']._serialized_start=13361
  _globals['_CHECKATTRIBUTEVIBOOLEANREQUEST']._serialized_end=13526
  _globals['_CHECKATTRIBUTEVIBOOLEANRESPONSE']._serialized_start=13528
  _globals['_CHECKATTRIBUTEVIBOOLEANRESPONSE']._serialized_end=13577
  _globals['_IMPORTATTRIBUTECONFIGURATIONFILEREQUEST']._serialized_start=13579
  _globals['_IMPORTATTRIBUTECONFIGURATIONFILEREQUEST']._serialized_end=13675
  _globals['_IMPORTATTRIBUTECONFIGURATIONFILERESPONSE']._serialized_start=13677
  _globals['_IMPORTATTRIBUTECONFIGURATIONFILERESPONSE']._serialized_end=13735
  _globals['_EXPORTATTRIBUTECONFIGURATIONFILEREQUEST']._serialized_start=13737
  _globals['_EXPORTATTRIBUTECONFIGURATIONFILEREQUEST']._serialized_end=13833
  _globals['_EXPORTATTRIBUTECONFIGURATIONFILERESPONSE']._serialized_start=13835
  _globals['_EXPORTATTRIBUTECONFIGURATIONFILERESPONSE']._serialized_end=13893
  _globals['_IMPORTATTRIBUTECONFIGURATIONBUFFERREQUEST']._serialized_start=13895
  _globals['_IMPORTATTRIBUTECONFIGURATIONBUFFERREQUEST']._serialized_end=13997
  _globals['_IMPORTATTRIBUTECONFIGURATIONBUFFERRESPONSE']._serialized_start=13999
  _globals['_IMPORTATTRIBUTECONFIGURATIONBUFFERRESPONSE']._serialized_end=14059
  _globals['_EXPORTATTRIBUTECONFIGURATIONBUFFERREQUEST']._serialized_start=14061
  _globals['_EXPORTATTRIBUTECONFIGURATIONBUFFERREQUEST']._serialized_end=14140
  _globals['_EXPORTATTRIBUTECONFIGURATIONBUFFERRESPONSE']._serialized_start=14142
  _globals['_EXPORTATTRIBUTECONFIGURATIONBUFFERRESPONSE']._serialized_end=14225
  _globals['_RESETINTERCHANGECHECKREQUEST']._serialized_start=14227
  _globals['_RESETINTERCHANGECHECKREQUEST']._serialized_end=14293
  _globals['_RESETINTERCHANGECHECKRESPONSE']._serialized_start=14295
  _globals['_RESETINTERCHANGECHECKRESPONSE']._serialized_end=14342
  _globals['_CLEARINTERCHANGEWARNINGSREQUEST']._serialized_start=14344
  _globals['_CLEARINTERCHANGEWARNINGSREQUEST']._serialized_end=14413
  _globals['_CLEARINTERCHANGEWARNINGSRESPONSE']._serialized_start=14415
  _globals['_CLEARINTERCHANGEWARNINGSRESPONSE']._serialized_end=14465
  _globals['_GETCHANNELNAMEREQUEST']._serialized_start=14467
  _globals['_GETCHANNELNAMEREQUEST']._serialized_end=14541
  _globals['_GETCHANNELNAMERESPONSE']._serialized_start=14543
  _globals['_GETCHANNELNAMERESPONSE']._serialized_end=14607
  _globals['_GETEXTCALRECOMMENDEDINTERVALREQUEST']._serialized_start=14609
  _globals['_GETEXTCALRECOMMENDEDINTERVALREQUEST']._serialized_end=14682
  _globals['_GETEXTCALRECOMMENDEDINTERVALRESPONSE']._serialized_start=14684
  _globals['_GETEXTCALRECOMMENDEDINTERVALRESPONSE']._serialized_end=14754
  _globals['_GETSELFCALSUPPORTEDREQUEST']._serialized_start=14756
  _globals['_GETSELFCALSUPPORTEDREQUEST']._serialized_end=14820
  _globals['_GETSELFCALSUPPORTEDRESPONSE']._serialized_start=14822
  _globals['_GETSELFCALSUPPORTEDRESPONSE']._serialized_end=14895
  _globals['_GETCALDATEANDTIMEREQUEST']._serialized_start=14898
  _globals['_GETCALDATEANDTIMEREQUEST']._serialized_end=15050
  _globals['_GETCALDATEANDTIMERESPONSE']._serialized_start=15052
  _globals['_GETCALDATEANDTIMERESPONSE']._serialized_end=15167
  _globals['_GETLASTCALTEMPREQUEST']._serialized_start=15170
  _globals['_GETLASTCALTEMPREQUEST']._serialized_end=15319
  _globals['_GETLASTCALTEMPRESPONSE']._serialized_start=15321
  _globals['_GETLASTCALTEMPRESPONSE']._serialized_end=15382
  _globals['_GETDEVTEMPREQUEST']._serialized_start=15384
  _globals['_GETDEVTEMPREQUEST']._serialized_end=15456
  _globals['_GETDEVTEMPRESPONSE']._serialized_start=15458
  _globals['_GETDEVTEMPRESPONSE']._serialized_end=15515
  _globals['_CONFIGURETRANSDUCERTYPEREQUEST']._serialized_start=15517
  _globals['_CONFIGURETRANSDUCERTYPEREQUEST']._serialized_end=15610
  _globals['_CONFIGURETRANSDUCERTYPERESPONSE']._serialized_start=15612
  _globals['_CONFIGURETRANSDUCERTYPERESPONSE']._serialized_end=15661
  _globals['_CONFIGURETHERMOCOUPLEREQUEST']._serialized_start=15664
  _globals['_CONFIGURETHERMOCOUPLEREQUEST']._serialized_end=16001
  _globals['_CONFIGURETHERMOCOUPLERESPONSE']._serialized_start=16003
  _globals['_CONFIGURETHERMOCOUPLERESPONSE']._serialized_end=16050
  _globals['_CONFIGUREFIXEDREFJUNCTIONREQUEST']._serialized_start=16052
  _globals['_CONFIGUREFIXEDREFJUNCTIONREQUEST']._serialized_end=16156
  _globals['_CONFIGUREFIXEDREFJUNCTIONRESPONSE']._serialized_start=16158
  _globals['_CONFIGUREFIXEDREFJUNCTIONRESPONSE']._serialized_end=16209
  _globals['_CONFIGURERTDTYPEREQUEST']._serialized_start=16212
  _globals['_CONFIGURERTDTYPEREQUEST']._serialized_end=16379
  _globals['_CONFIGURERTDTYPERESPONSE']._serialized_start=16381
  _globals['_CONFIGURERTDTYPERESPONSE']._serialized_end=16423
  _globals['_CONFIGURERTDCUSTOMREQUEST']._serialized_start=16425
  _globals['_CONFIGURERTDCUSTOMREQUEST']._serialized_end=16533
  _globals['_CONFIGURERTDCUSTOMRESPONSE']._serialized_start=16535
  _globals['_CONFIGURERTDCUSTOMRESPONSE']._serialized_end=16579
  _globals['_CONFIGURETHERMISTORTYPEREQUEST']._serialized_start=16581
  _globals['_CONFIGURETHERMISTORTYPEREQUEST']._serialized_end=16674
  _globals['_CONFIGURETHERMISTORTYPERESPONSE']._serialized_start=16676
  _globals['_CONFIGURETHERMISTORTYPERESPONSE']._serialized_end=16725
  _globals['_CONFIGURETHERMISTORCUSTOMREQUEST']._serialized_start=16728
  _globals['_CONFIGURETHERMISTORCUSTOMREQUEST']._serialized_end=16864
  _globals['_CONFIGURETHERMISTORCUSTOMRESPONSE']._serialized_start=16866
  _globals['_CONFIGURETHERMISTORCUSTOMRESPONSE']._serialized_end=16917
  _globals['_INVALIDATEALLATTRIBUTESREQUEST']._serialized_start=16919
  _globals['_INVALIDATEALLATTRIBUTESREQUEST']._serialized_end=16987
  _globals['_INVALIDATEALLATTRIBUTESRESPONSE']._serialized_start=16989
  _globals['_INVALIDATEALLATTRIBUTESRESPONSE']._serialized_end=17038
  _globals['_NIDMM']._serialized_start=32776
  _globals['_NIDMM']._serialized_end=41582
# @@protoc_insertion_point(module_scope)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidmm/nidmm/nidmm_pb2_grpc.py sha256=8c1d74506859e7d12d6464d4cb31ac38415f47ee7bc788d276562a9e48cff964 bytes=138212 -->
## FILE: generated/nidmm/nidmm/nidmm_pb2_grpc.py

- repository: `ni/nimi-python`
- source_path: `generated/nidmm/nidmm/nidmm_pb2_grpc.py`
- sha256: `8c1d74506859e7d12d6464d4cb31ac38415f47ee7bc788d276562a9e48cff964`
- bytes: 138212

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import nidmm_pb2 as nidmm__pb2


class NiDmmStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Init = channel.unary_unary(
                '/nidmm_grpc.NiDmm/Init',
                request_serializer=nidmm__pb2.InitRequest.SerializeToString,
                response_deserializer=nidmm__pb2.InitResponse.FromString,
                )
        self.InitWithOptions = channel.unary_unary(
                '/nidmm_grpc.NiDmm/InitWithOptions',
                request_serializer=nidmm__pb2.InitWithOptionsRequest.SerializeToString,
                response_deserializer=nidmm__pb2.InitWithOptionsResponse.FromString,
                )
        self.Close = channel.unary_unary(
                '/nidmm_grpc.NiDmm/Close',
                request_serializer=nidmm__pb2.CloseRequest.SerializeToString,
                response_deserializer=nidmm__pb2.CloseResponse.FromString,
                )
        self.GetError = channel.unary_unary(
                '/nidmm_grpc.NiDmm/GetError',
                request_serializer=nidmm__pb2.GetErrorRequest.SerializeToString,
                response_deserializer=nidmm__pb2.GetErrorResponse.FromString,
                )
        self.GetErrorMessage = channel.unary_unary(
                '/nidmm_grpc.NiDmm/GetErrorMessage',
                request_serializer=nidmm__pb2.GetErrorMessageRequest.SerializeToString,
                response_deserializer=nidmm__pb2.GetErrorMessageResponse.FromString,
                )
        self.ClearError = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ClearError',
                request_serializer=nidmm__pb2.ClearErrorRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ClearErrorResponse.FromString,
                )
        self.Reset = channel.unary_unary(
                '/nidmm_grpc.NiDmm/Reset',
                request_serializer=nidmm__pb2.ResetRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ResetResponse.FromString,
                )
        self.SelfTest = channel.unary_unary(
                '/nidmm_grpc.NiDmm/SelfTest',
                request_serializer=nidmm__pb2.SelfTestRequest.SerializeToString,
                response_deserializer=nidmm__pb2.SelfTestResponse.FromString,
                )
        self.SelfCal = channel.unary_unary(
                '/nidmm_grpc.NiDmm/SelfCal',
                request_serializer=nidmm__pb2.SelfCalRequest.SerializeToString,
                response_deserializer=nidmm__pb2.SelfCalResponse.FromString,
                )
        self.RevisionQuery = channel.unary_unary(
                '/nidmm_grpc.NiDmm/RevisionQuery',
                request_serializer=nidmm__pb2.RevisionQueryRequest.SerializeToString,
                response_deserializer=nidmm__pb2.RevisionQueryResponse.FromString,
                )
        self.ResetWithDefaults = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ResetWithDefaults',
                request_serializer=nidmm__pb2.ResetWithDefaultsRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ResetWithDefaultsResponse.FromString,
                )
        self.Disable = channel.unary_unary(
                '/nidmm_grpc.NiDmm/Disable',
                request_serializer=nidmm__pb2.DisableRequest.SerializeToString,
                response_deserializer=nidmm__pb2.DisableResponse.FromString,
                )
        self.GetMeasurementPeriod = channel.unary_unary(
                '/nidmm_grpc.NiDmm/GetMeasurementPeriod',
                request_serializer=nidmm__pb2.GetMeasurementPeriodRequest.SerializeToString,
                response_deserializer=nidmm__pb2.GetMeasurementPeriodResponse.FromString,
                )
        self.ConfigureTrigger = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ConfigureTrigger',
                request_serializer=nidmm__pb2.ConfigureTriggerRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ConfigureTriggerResponse.FromString,
                )
        self.Read = channel.unary_unary(
                '/nidmm_grpc.NiDmm/Read',
                request_serializer=nidmm__pb2.ReadRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ReadResponse.FromString,
                )
        self.Fetch = channel.unary_unary(
                '/nidmm_grpc.NiDmm/Fetch',
                request_serializer=nidmm__pb2.FetchRequest.SerializeToString,
                response_deserializer=nidmm__pb2.FetchResponse.FromString,
                )
        self.Abort = channel.unary_unary(
                '/nidmm_grpc.NiDmm/Abort',
                request_serializer=nidmm__pb2.AbortRequest.SerializeToString,
                response_deserializer=nidmm__pb2.AbortResponse.FromString,
                )
        self.Initiate = channel.unary_unary(
                '/nidmm_grpc.NiDmm/Initiate',
                request_serializer=nidmm__pb2.InitiateRequest.SerializeToString,
                response_deserializer=nidmm__pb2.InitiateResponse.FromString,
                )
        self.IsOverRange = channel.unary_unary(
                '/nidmm_grpc.NiDmm/IsOverRange',
                request_serializer=nidmm__pb2.IsOverRangeRequest.SerializeToString,
                response_deserializer=nidmm__pb2.IsOverRangeResponse.FromString,
                )
        self.IsUnderRange = channel.unary_unary(
                '/nidmm_grpc.NiDmm/IsUnderRange',
                request_serializer=nidmm__pb2.IsUnderRangeRequest.SerializeToString,
                response_deserializer=nidmm__pb2.IsUnderRangeResponse.FromString,
                )
        self.ConfigureACBandwidth = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ConfigureACBandwidth',
                request_serializer=nidmm__pb2.ConfigureACBandwidthRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ConfigureACBandwidthResponse.FromString,
                )
        self.ConfigureFrequencyVoltageRange = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ConfigureFrequencyVoltageRange',
                request_serializer=nidmm__pb2.ConfigureFrequencyVoltageRangeRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ConfigureFrequencyVoltageRangeResponse.FromString,
                )
        self.ConfigureMeasCompleteDest = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ConfigureMeasCompleteDest',
                request_serializer=nidmm__pb2.ConfigureMeasCompleteDestRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ConfigureMeasCompleteDestResponse.FromString,
                )
        self.ConfigureMultiPoint = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ConfigureMultiPoint',
                request_serializer=nidmm__pb2.ConfigureMultiPointRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ConfigureMultiPointResponse.FromString,
                )
        self.ReadMultiPoint = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ReadMultiPoint',
                request_serializer=nidmm__pb2.ReadMultiPointRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ReadMultiPointResponse.FromString,
                )
        self.FetchMultiPoint = channel.unary_unary(
                '/nidmm_grpc.NiDmm/FetchMultiPoint',
                request_serializer=nidmm__pb2.FetchMultiPointRequest.SerializeToString,
                response_deserializer=nidmm__pb2.FetchMultiPointResponse.FromString,
                )
        self.ConfigureTriggerSlope = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ConfigureTriggerSlope',
                request_serializer=nidmm__pb2.ConfigureTriggerSlopeRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ConfigureTriggerSlopeResponse.FromString,
                )
        self.SendSoftwareTrigger = channel.unary_unary(
                '/nidmm_grpc.NiDmm/SendSoftwareTrigger',
                request_serializer=nidmm__pb2.SendSoftwareTriggerRequest.SerializeToString,
                response_deserializer=nidmm__pb2.SendSoftwareTriggerResponse.FromString,
                )
        self.GetApertureTimeInfo = channel.unary_unary(
                '/nidmm_grpc.NiDmm/GetApertureTimeInfo',
                request_serializer=nidmm__pb2.GetApertureTimeInfoRequest.SerializeToString,
                response_deserializer=nidmm__pb2.GetApertureTimeInfoResponse.FromString,
                )
        self.GetAutoRangeValue = channel.unary_unary(
                '/nidmm_grpc.NiDmm/GetAutoRangeValue',
                request_serializer=nidmm__pb2.GetAutoRangeValueRequest.SerializeToString,
                response_deserializer=nidmm__pb2.GetAutoRangeValueResponse.FromString,
                )
        self.ConfigureAutoZeroMode = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ConfigureAutoZeroMode',
                request_serializer=nidmm__pb2.ConfigureAutoZeroModeRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ConfigureAutoZeroModeResponse.FromString,
                )
        self.ConfigurePowerLineFrequency = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ConfigurePowerLineFrequency',
                request_serializer=nidmm__pb2.ConfigurePowerLineFrequencyRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ConfigurePowerLineFrequencyResponse.FromString,
                )
        self.ConfigureMeasurementDigits = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ConfigureMeasurementDigits',
                request_serializer=nidmm__pb2.ConfigureMeasurementDigitsRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ConfigureMeasurementDigitsResponse.FromString,
                )
        self.ConfigureMeasurementAbsolute = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ConfigureMeasurementAbsolute',
                request_serializer=nidmm__pb2.ConfigureMeasurementAbsoluteRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ConfigureMeasurementAbsoluteResponse.FromString,
                )
        self.ConfigureMeasCompleteSlope = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ConfigureMeasCompleteSlope',
                request_serializer=nidmm__pb2.ConfigureMeasCompleteSlopeRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ConfigureMeasCompleteSlopeResponse.FromString,
                )
        self.ConfigureSampleTriggerSlope = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ConfigureSampleTriggerSlope',
                request_serializer=nidmm__pb2.ConfigureSampleTriggerSlopeRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ConfigureSampleTriggerSlopeResponse.FromString,
                )
        self.ReadStatus = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ReadStatus',
                request_serializer=nidmm__pb2.ReadStatusRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ReadStatusResponse.FromString,
                )
        self.Control = channel.unary_unary(
                '/nidmm_grpc.NiDmm/Control',
                request_serializer=nidmm__pb2.ControlRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ControlResponse.FromString,
                )
        self.ConfigureADCCalibration = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ConfigureADCCalibration',
                request_serializer=nidmm__pb2.ConfigureADCCalibrationRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ConfigureADCCalibrationResponse.FromString,
                )
        self.ConfigureOffsetCompOhms = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ConfigureOffsetCompOhms',
                request_serializer=nidmm__pb2.ConfigureOffsetCompOhmsRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ConfigureOffsetCompOhmsResponse.FromString,
                )
        self.ConfigureCurrentSource = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ConfigureCurrentSource',
                request_serializer=nidmm__pb2.ConfigureCurrentSourceRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ConfigureCurrentSourceResponse.FromString,
                )
        self.ConfigureCableCompType = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ConfigureCableCompType',
                request_serializer=nidmm__pb2.ConfigureCableCompTypeRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ConfigureCableCompTypeResponse.FromString,
                )
        self.PerformOpenCableComp = channel.unary_unary(
                '/nidmm_grpc.NiDmm/PerformOpenCableComp',
                request_serializer=nidmm__pb2.PerformOpenCableCompRequest.SerializeToString,
                response_deserializer=nidmm__pb2.PerformOpenCableCompResponse.FromString,
                )
        self.PerformShortCableComp = channel.unary_unary(
                '/nidmm_grpc.NiDmm/PerformShortCableComp',
                request_serializer=nidmm__pb2.PerformShortCableCompRequest.SerializeToString,
                response_deserializer=nidmm__pb2.PerformShortCableCompResponse.FromString,
                )
        self.ConfigureOpenCableCompValues = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ConfigureOpenCableCompValues',
                request_serializer=nidmm__pb2.ConfigureOpenCableCompValuesRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ConfigureOpenCableCompValuesResponse.FromString,
                )
        self.ConfigureShortCableCompValues = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ConfigureShortCableCompValues',
                request_serializer=nidmm__pb2.ConfigureShortCableCompValuesRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ConfigureShortCableCompValuesResponse.FromString,
                )
        self.ConfigureWaveformAcquisition = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ConfigureWaveformAcquisition',
                request_serializer=nidmm__pb2.ConfigureWaveformAcquisitionRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ConfigureWaveformAcquisitionResponse.FromString,
                )
        self.ConfigureWaveformCoupling = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ConfigureWaveformCoupling',
                request_serializer=nidmm__pb2.ConfigureWaveformCouplingRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ConfigureWaveformCouplingResponse.FromString,
                )
        self.FetchWaveform = channel.unary_unary(
                '/nidmm_grpc.NiDmm/FetchWaveform',
                request_serializer=nidmm__pb2.FetchWaveformRequest.SerializeToString,
                response_deserializer=nidmm__pb2.FetchWaveformResponse.FromString,
                )
        self.ReadWaveform = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ReadWaveform',
                request_serializer=nidmm__pb2.ReadWaveformRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ReadWaveformResponse.FromString,
                )
        self.GetAttributeViInt32 = channel.unary_unary(
                '/nidmm_grpc.NiDmm/GetAttributeViInt32',
                request_serializer=nidmm__pb2.GetAttributeViInt32Request.SerializeToString,
                response_deserializer=nidmm__pb2.GetAttributeViInt32Response.FromString,
                )
        self.SetAttributeViInt32 = channel.unary_unary(
                '/nidmm_grpc.NiDmm/SetAttributeViInt32',
                request_serializer=nidmm__pb2.SetAttributeViInt32Request.SerializeToString,
                response_deserializer=nidmm__pb2.SetAttributeViInt32Response.FromString,
                )
        self.CheckAttributeViInt32 = channel.unary_unary(
                '/nidmm_grpc.NiDmm/CheckAttributeViInt32',
                request_serializer=nidmm__pb2.CheckAttributeViInt32Request.SerializeToString,
                response_deserializer=nidmm__pb2.CheckAttributeViInt32Response.FromString,
                )
        self.GetAttributeViReal64 = channel.unary_unary(
                '/nidmm_grpc.NiDmm/GetAttributeViReal64',
                request_serializer=nidmm__pb2.GetAttributeViReal64Request.SerializeToString,
                response_deserializer=nidmm__pb2.GetAttributeViReal64Response.FromString,
                )
        self.SetAttributeViReal64 = channel.unary_unary(
                '/nidmm_grpc.NiDmm/SetAttributeViReal64',
                request_serializer=nidmm__pb2.SetAttributeViReal64Request.SerializeToString,
                response_deserializer=nidmm__pb2.SetAttributeViReal64Response.FromString,
                )
        self.CheckAttributeViReal64 = channel.unary_unary(
                '/nidmm_grpc.NiDmm/CheckAttributeViReal64',
                request_serializer=nidmm__pb2.CheckAttributeViReal64Request.SerializeToString,
                response_deserializer=nidmm__pb2.CheckAttributeViReal64Response.FromString,
                )
        self.GetAttributeViString = channel.unary_unary(
                '/nidmm_grpc.NiDmm/GetAttributeViString',
                request_serializer=nidmm__pb2.GetAttributeViStringRequest.SerializeToString,
                response_deserializer=nidmm__pb2.GetAttributeViStringResponse.FromString,
                )
        self.SetAttributeViString = channel.unary_unary(
                '/nidmm_grpc.NiDmm/SetAttributeViString',
                request_serializer=nidmm__pb2.SetAttributeViStringRequest.SerializeToString,
                response_deserializer=nidmm__pb2.SetAttributeViStringResponse.FromString,
                )
        self.CheckAttributeViString = channel.unary_unary(
                '/nidmm_grpc.NiDmm/CheckAttributeViString',
                request_serializer=nidmm__pb2.CheckAttributeViStringRequest.SerializeToString,
                response_deserializer=nidmm__pb2.CheckAttributeViStringResponse.FromString,
                )
        self.GetAttributeViSession = channel.unary_unary(
                '/nidmm_grpc.NiDmm/GetAttributeViSession',
                request_serializer=nidmm__pb2.GetAttributeViSessionRequest.SerializeToString,
                response_deserializer=nidmm__pb2.GetAttributeViSessionResponse.FromString,
                )
        self.SetAttributeViSession = channel.unary_unary(
                '/nidmm_grpc.NiDmm/SetAttributeViSession',
                request_serializer=nidmm__pb2.SetAttributeViSessionRequest.SerializeToString,
                response_deserializer=nidmm__pb2.SetAttributeViSessionResponse.FromString,
                )
        self.CheckAttributeViSession = channel.unary_unary(
                '/nidmm_grpc.NiDmm/CheckAttributeViSession',
                request_serializer=nidmm__pb2.CheckAttributeViSessionRequest.SerializeToString,
                response_deserializer=nidmm__pb2.CheckAttributeViSessionResponse.FromString,
                )
        self.GetAttributeViBoolean = channel.unary_unary(
                '/nidmm_grpc.NiDmm/GetAttributeViBoolean',
                request_serializer=nidmm__pb2.GetAttributeViBooleanRequest.SerializeToString,
                response_deserializer=nidmm__pb2.GetAttributeViBooleanResponse.FromString,
                )
        self.SetAttributeViBoolean = channel.unary_unary(
                '/nidmm_grpc.NiDmm/SetAttributeViBoolean',
                request_serializer=nidmm__pb2.SetAttributeViBooleanRequest.SerializeToString,
                response_deserializer=nidmm__pb2.SetAttributeViBooleanResponse.FromString,
                )
        self.CheckAttributeViBoolean = channel.unary_unary(
                '/nidmm_grpc.NiDmm/CheckAttributeViBoolean',
                request_serializer=nidmm__pb2.CheckAttributeViBooleanRequest.SerializeToString,
                response_deserializer=nidmm__pb2.CheckAttributeViBooleanResponse.FromString,
                )
        self.ImportAttributeConfigurationFile = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ImportAttributeConfigurationFile',
                request_serializer=nidmm__pb2.ImportAttributeConfigurationFileRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ImportAttributeConfigurationFileResponse.FromString,
                )
        self.ExportAttributeConfigurationFile = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ExportAttributeConfigurationFile',
                request_serializer=nidmm__pb2.ExportAttributeConfigurationFileRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ExportAttributeConfigurationFileResponse.FromString,
                )
        self.ImportAttributeConfigurationBuffer = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ImportAttributeConfigurationBuffer',
                request_serializer=nidmm__pb2.ImportAttributeConfigurationBufferRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ImportAttributeConfigurationBufferResponse.FromString,
                )
        self.ExportAttributeConfigurationBuffer = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ExportAttributeConfigurationBuffer',
                request_serializer=nidmm__pb2.ExportAttributeConfigurationBufferRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ExportAttributeConfigurationBufferResponse.FromString,
                )
        self.ResetInterchangeCheck = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ResetInterchangeCheck',
                request_serializer=nidmm__pb2.ResetInterchangeCheckRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ResetInterchangeCheckResponse.FromString,
                )
        self.ClearInterchangeWarnings = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ClearInterchangeWarnings',
                request_serializer=nidmm__pb2.ClearInterchangeWarningsRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ClearInterchangeWarningsResponse.FromString,
                )
        self.GetChannelName = channel.unary_unary(
                '/nidmm_grpc.NiDmm/GetChannelName',
                request_serializer=nidmm__pb2.GetChannelNameRequest.SerializeToString,
                response_deserializer=nidmm__pb2.GetChannelNameResponse.FromString,
                )
        self.GetExtCalRecommendedInterval = channel.unary_unary(
                '/nidmm_grpc.NiDmm/GetExtCalRecommendedInterval',
                request_serializer=nidmm__pb2.GetExtCalRecommendedIntervalRequest.SerializeToString,
                response_deserializer=nidmm__pb2.GetExtCalRecommendedIntervalResponse.FromString,
                )
        self.GetSelfCalSupported = channel.unary_unary(
                '/nidmm_grpc.NiDmm/GetSelfCalSupported',
                request_serializer=nidmm__pb2.GetSelfCalSupportedRequest.SerializeToString,
                response_deserializer=nidmm__pb2.GetSelfCalSupportedResponse.FromString,
                )
        self.GetCalDateAndTime = channel.unary_unary(
                '/nidmm_grpc.NiDmm/GetCalDateAndTime',
                request_serializer=nidmm__pb2.GetCalDateAndTimeRequest.SerializeToString,
                response_deserializer=nidmm__pb2.GetCalDateAndTimeResponse.FromString,
                )
        self.GetLastCalTemp = channel.unary_unary(
                '/nidmm_grpc.NiDmm/GetLastCalTemp',
                request_serializer=nidmm__pb2.GetLastCalTempRequest.SerializeToString,
                response_deserializer=nidmm__pb2.GetLastCalTempResponse.FromString,
                )
        self.GetDevTemp = channel.unary_unary(
                '/nidmm_grpc.NiDmm/GetDevTemp',
                request_serializer=nidmm__pb2.GetDevTempRequest.SerializeToString,
                response_deserializer=nidmm__pb2.GetDevTempResponse.FromString,
                )
        self.ConfigureTransducerType = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ConfigureTransducerType',
                request_serializer=nidmm__pb2.ConfigureTransducerTypeRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ConfigureTransducerTypeResponse.FromString,
                )
        self.ConfigureThermocouple = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ConfigureThermocouple',
                request_serializer=nidmm__pb2.ConfigureThermocoupleRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ConfigureThermocoupleResponse.FromString,
                )
        self.ConfigureFixedRefJunction = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ConfigureFixedRefJunction',
                request_serializer=nidmm__pb2.ConfigureFixedRefJunctionRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ConfigureFixedRefJunctionResponse.FromString,
                )
        self.ConfigureRTDType = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ConfigureRTDType',
                request_serializer=nidmm__pb2.ConfigureRTDTypeRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ConfigureRTDTypeResponse.FromString,
                )
        self.ConfigureRTDCustom = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ConfigureRTDCustom',
                request_serializer=nidmm__pb2.ConfigureRTDCustomRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ConfigureRTDCustomResponse.FromString,
                )
        self.ConfigureThermistorType = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ConfigureThermistorType',
                request_serializer=nidmm__pb2.ConfigureThermistorTypeRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ConfigureThermistorTypeResponse.FromString,
                )
        self.ConfigureThermistorCustom = channel.unary_unary(
                '/nidmm_grpc.NiDmm/ConfigureThermistorCustom',
                request_serializer=nidmm__pb2.ConfigureThermistorCustomRequest.SerializeToString,
                response_deserializer=nidmm__pb2.ConfigureThermistorCustomResponse.FromString,
                )
        self.InvalidateAllAttributes = channel.unary_unary(
                '/nidmm_grpc.NiDmm/InvalidateAllAttributes',
                request_serializer=nidmm__pb2.InvalidateAllAttributesRequest.SerializeToString,
                response_deserializer=nidmm__pb2.InvalidateAllAttributesResponse.FromString,
                )


class NiDmmServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Init(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InitWithOptions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Close(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetError(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetErrorMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearError(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Reset(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SelfTest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SelfCal(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RevisionQuery(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetWithDefaults(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Disable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMeasurementPeriod(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Fetch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Abort(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Initiate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IsOverRange(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IsUnderRange(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureACBandwidth(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureFrequencyVoltageRange(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureMeasCompleteDest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureMultiPoint(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadMultiPoint(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FetchMultiPoint(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureTriggerSlope(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendSoftwareTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetApertureTimeInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAutoRangeValue(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureAutoZeroMode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigurePowerLineFrequency(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureMeasurementDigits(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureMeasurementAbsolute(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureMeasCompleteSlope(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureSampleTriggerSlope(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Control(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureADCCalibration(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureOffsetCompOhms(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureCurrentSource(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureCableCompType(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PerformOpenCableComp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PerformShortCableComp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureOpenCableCompValues(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureShortCableCompValues(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureWaveformAcquisition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureWaveformCoupling(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FetchWaveform(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadWaveform(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttributeViInt32(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAttributeViInt32(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckAttributeViInt32(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttributeViReal64(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAttributeViReal64(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckAttributeViReal64(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttributeViString(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAttributeViString(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckAttributeViString(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttributeViSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAttributeViSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckAttributeViSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttributeViBoolean(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAttributeViBoolean(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckAttributeViBoolean(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ImportAttributeConfigurationFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExportAttributeConfigurationFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ImportAttributeConfigurationBuffer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExportAttributeConfigurationBuffer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetInterchangeCheck(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearInterchangeWarnings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetChannelName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetExtCalRecommendedInterval(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSelfCalSupported(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCalDateAndTime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLastCalTemp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDevTemp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureTransducerType(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureThermocouple(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureFixedRefJunction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureRTDType(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureRTDCustom(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureThermistorType(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureThermistorCustom(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InvalidateAllAttributes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NiDmmServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Init': grpc.unary_unary_rpc_method_handler(
                    servicer.Init,
                    request_deserializer=nidmm__pb2.InitRequest.FromString,
                    response_serializer=nidmm__pb2.InitResponse.SerializeToString,
            ),
            'InitWithOptions': grpc.unary_unary_rpc_method_handler(
                    servicer.InitWithOptions,
                    request_deserializer=nidmm__pb2.InitWithOptionsRequest.FromString,
                    response_serializer=nidmm__pb2.InitWithOptionsResponse.SerializeToString,
            ),
            'Close': grpc.unary_unary_rpc_method_handler(
                    servicer.Close,
                    request_deserializer=nidmm__pb2.CloseRequest.FromString,
                    response_serializer=nidmm__pb2.CloseResponse.SerializeToString,
            ),
            'GetError': grpc.unary_unary_rpc_method_handler(
                    servicer.GetError,
                    request_deserializer=nidmm__pb2.GetErrorRequest.FromString,
                    response_serializer=nidmm__pb2.GetErrorResponse.SerializeToString,
            ),
            'GetErrorMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.GetErrorMessage,
                    request_deserializer=nidmm__pb2.GetErrorMessageRequest.FromString,
                    response_serializer=nidmm__pb2.GetErrorMessageResponse.SerializeToString,
            ),
            'ClearError': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearError,
                    request_deserializer=nidmm__pb2.ClearErrorRequest.FromString,
                    response_serializer=nidmm__pb2.ClearErrorResponse.SerializeToString,
            ),
            'Reset': grpc.unary_unary_rpc_method_handler(
                    servicer.Reset,
                    request_deserializer=nidmm__pb2.ResetRequest.FromString,
                    response_serializer=nidmm__pb2.ResetResponse.SerializeToString,
            ),
            'SelfTest': grpc.unary_unary_rpc_method_handler(
                    servicer.SelfTest,
                    request_deserializer=nidmm__pb2.SelfTestRequest.FromString,
                    response_serializer=nidmm__pb2.SelfTestResponse.SerializeToString,
            ),
            'SelfCal': grpc.unary_unary_rpc_method_handler(
                    servicer.SelfCal,
                    request_deserializer=nidmm__pb2.SelfCalRequest.FromString,
                    response_serializer=nidmm__pb2.SelfCalResponse.SerializeToString,
            ),
            'RevisionQuery': grpc.unary_unary_rpc_method_handler(
                    servicer.RevisionQuery,
                    request_deserializer=nidmm__pb2.RevisionQueryRequest.FromString,
                    response_serializer=nidmm__pb2.RevisionQueryResponse.SerializeToString,
            ),
            'ResetWithDefaults': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetWithDefaults,
                    request_deserializer=nidmm__pb2.ResetWithDefaultsRequest.FromString,
                    response_serializer=nidmm__pb2.ResetWithDefaultsResponse.SerializeToString,
            ),
            'Disable': grpc.unary_unary_rpc_method_handler(
                    servicer.Disable,
                    request_deserializer=nidmm__pb2.DisableRequest.FromString,
                    response_serializer=nidmm__pb2.DisableResponse.SerializeToString,
            ),
            'GetMeasurementPeriod': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMeasurementPeriod,
                    request_deserializer=nidmm__pb2.GetMeasurementPeriodRequest.FromString,
                    response_serializer=nidmm__pb2.GetMeasurementPeriodResponse.SerializeToString,
            ),
            'ConfigureTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureTrigger,
                    request_deserializer=nidmm__pb2.ConfigureTriggerRequest.FromString,
                    response_serializer=nidmm__pb2.ConfigureTriggerResponse.SerializeToString,
            ),
            'Read': grpc.unary_unary_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=nidmm__pb2.ReadRequest.FromString,
                    response_serializer=nidmm__pb2.ReadResponse.SerializeToString,
            ),
            'Fetch': grpc.unary_unary_rpc_method_handler(
                    servicer.Fetch,
                    request_deserializer=nidmm__pb2.FetchRequest.FromString,
                    response_serializer=nidmm__pb2.FetchResponse.SerializeToString,
            ),
            'Abort': grpc.unary_unary_rpc_method_handler(
                    servicer.Abort,
                    request_deserializer=nidmm__pb2.AbortRequest.FromString,
                    response_serializer=nidmm__pb2.AbortResponse.SerializeToString,
            ),
            'Initiate': grpc.unary_unary_rpc_method_handler(
                    servicer.Initiate,
                    request_deserializer=nidmm__pb2.InitiateRequest.FromString,
                    response_serializer=nidmm__pb2.InitiateResponse.SerializeToString,
            ),
            'IsOverRange': grpc.unary_unary_rpc_method_handler(
                    servicer.IsOverRange,
                    request_deserializer=nidmm__pb2.IsOverRangeRequest.FromString,
                    response_serializer=nidmm__pb2.IsOverRangeResponse.SerializeToString,
            ),
            'IsUnderRange': grpc.unary_unary_rpc_method_handler(
                    servicer.IsUnderRange,
                    request_deserializer=nidmm__pb2.IsUnderRangeRequest.FromString,
                    response_serializer=nidmm__pb2.IsUnderRangeResponse.SerializeToString,
            ),
            'ConfigureACBandwidth': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureACBandwidth,
                    request_deserializer=nidmm__pb2.ConfigureACBandwidthRequest.FromString,
                    response_serializer=nidmm__pb2.ConfigureACBandwidthResponse.SerializeToString,
            ),
            'ConfigureFrequencyVoltageRange': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureFrequencyVoltageRange,
                    request_deserializer=nidmm__pb2.ConfigureFrequencyVoltageRangeRequest.FromString,
                    response_serializer=nidmm__pb2.ConfigureFrequencyVoltageRangeResponse.SerializeToString,
            ),
            'ConfigureMeasCompleteDest': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureMeasCompleteDest,
                    request_deserializer=nidmm__pb2.ConfigureMeasCompleteDestRequest.FromString,
                    response_serializer=nidmm__pb2.ConfigureMeasCompleteDestResponse.SerializeToString,
            ),
            'ConfigureMultiPoint': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureMultiPoint,
                    request_deserializer=nidmm__pb2.ConfigureMultiPointRequest.FromString,
                    response_serializer=nidmm__pb2.ConfigureMultiPointResponse.SerializeToString,
            ),
            'ReadMultiPoint': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadMultiPoint,
                    request_deserializer=nidmm__pb2.ReadMultiPointRequest.FromString,
                    response_serializer=nidmm__pb2.ReadMultiPointResponse.SerializeToString,
            ),
            'FetchMultiPoint': grpc.unary_unary_rpc_method_handler(
                    servicer.FetchMultiPoint,
                    request_deserializer=nidmm__pb2.FetchMultiPointRequest.FromString,
                    response_serializer=nidmm__pb2.FetchMultiPointResponse.SerializeToString,
            ),
            'ConfigureTriggerSlope': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureTriggerSlope,
                    request_deserializer=nidmm__pb2.ConfigureTriggerSlopeRequest.FromString,
                    response_serializer=nidmm__pb2.ConfigureTriggerSlopeResponse.SerializeToString,
            ),
            'SendSoftwareTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.SendSoftwareTrigger,
                    request_deserializer=nidmm__pb2.SendSoftwareTriggerRequest.FromString,
                    response_serializer=nidmm__pb2.SendSoftwareTriggerResponse.SerializeToString,
            ),
            'GetApertureTimeInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetApertureTimeInfo,
                    request_deserializer=nidmm__pb2.GetApertureTimeInfoRequest.FromString,
                    response_serializer=nidmm__pb2.GetApertureTimeInfoResponse.SerializeToString,
            ),
            'GetAutoRangeValue': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAutoRangeValue,
                    request_deserializer=nidmm__pb2.GetAutoRangeValueRequest.FromString,
                    response_serializer=nidmm__pb2.GetAutoRangeValueResponse.SerializeToString,
            ),
            'ConfigureAutoZeroMode': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureAutoZeroMode,
                    request_deserializer=nidmm__pb2.ConfigureAutoZeroModeRequest.FromString,
                    response_serializer=nidmm__pb2.ConfigureAutoZeroModeResponse.SerializeToString,
            ),
            'ConfigurePowerLineFrequency': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigurePowerLineFrequency,
                    request_deserializer=nidmm__pb2.ConfigurePowerLineFrequencyRequest.FromString,
                    response_serializer=nidmm__pb2.ConfigurePowerLineFrequencyResponse.SerializeToString,
            ),
            'ConfigureMeasurementDigits': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureMeasurementDigits,
                    request_deserializer=nidmm__pb2.ConfigureMeasurementDigitsRequest.FromString,
                    response_serializer=nidmm__pb2.ConfigureMeasurementDigitsResponse.SerializeToString,
            ),
            'ConfigureMeasurementAbsolute': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureMeasurementAbsolute,
                    request_deserializer=nidmm__pb2.ConfigureMeasurementAbsoluteRequest.FromString,
                    response_serializer=nidmm__pb2.ConfigureMeasurementAbsoluteResponse.SerializeToString,
            ),
            'ConfigureMeasCompleteSlope': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureMeasCompleteSlope,
                    request_deserializer=nidmm__pb2.ConfigureMeasCompleteSlopeRequest.FromString,
                    response_serializer=nidmm__pb2.ConfigureMeasCompleteSlopeResponse.SerializeToString,
            ),
            'ConfigureSampleTriggerSlope': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureSampleTriggerSlope,
                    request_deserializer=nidmm__pb2.ConfigureSampleTriggerSlopeRequest.FromString,
                    response_serializer=nidmm__pb2.ConfigureSampleTriggerSlopeResponse.SerializeToString,
            ),
            'ReadStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadStatus,
                    request_deserializer=nidmm__pb2.ReadStatusRequest.FromString,
                    response_serializer=nidmm__pb2.ReadStatusResponse.SerializeToString,
            ),
            'Control': grpc.unary_unary_rpc_method_handler(
                    servicer.Control,
                    request_deserializer=nidmm__pb2.ControlRequest.FromString,
                    response_serializer=nidmm__pb2.ControlResponse.SerializeToString,
            ),
            'ConfigureADCCalibration': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureADCCalibration,
                    request_deserializer=nidmm__pb2.ConfigureADCCalibrationRequest.FromString,
                    response_serializer=nidmm__pb2.ConfigureADCCalibrationResponse.SerializeToString,
            ),
            'ConfigureOffsetCompOhms': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureOffsetCompOhms,
                    request_deserializer=nidmm__pb2.ConfigureOffsetCompOhmsRequest.FromString,
                    response_serializer=nidmm__pb2.ConfigureOffsetCompOhmsResponse.SerializeToString,
            ),
            'ConfigureCurrentSource': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureCurrentSource,
                    request_deserializer=nidmm__pb2.ConfigureCurrentSourceRequest.FromString,
                    response_serializer=nidmm__pb2.ConfigureCurrentSourceResponse.SerializeToString,
            ),
            'ConfigureCableCompType': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureCableCompType,
                    request_deserializer=nidmm__pb2.ConfigureCableCompTypeRequest.FromString,
                    response_serializer=nidmm__pb2.ConfigureCableCompTypeResponse.SerializeToString,
            ),
            'PerformOpenCableComp': grpc.unary_unary_rpc_method_handler(
                    servicer.PerformOpenCableComp,
                    request_deserializer=nidmm__pb2.PerformOpenCableCompRequest.FromString,
                    response_serializer=nidmm__pb2.PerformOpenCableCompResponse.SerializeToString,
            ),
            'PerformShortCableComp': grpc.unary_unary_rpc_method_handler(
                    servicer.PerformShortCableComp,
                    request_deserializer=nidmm__pb2.PerformShortCableCompRequest.FromString,
                    response_serializer=nidmm__pb2.PerformShortCableCompResponse.SerializeToString,
            ),
            'ConfigureOpenCableCompValues': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureOpenCableCompValues,
                    request_deserializer=nidmm__pb2.ConfigureOpenCableCompValuesRequest.FromString,
                    response_serializer=nidmm__pb2.ConfigureOpenCableCompValuesResponse.SerializeToString,
            ),
            'ConfigureShortCableCompValues': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureShortCableCompValues,
                    request_deserializer=nidmm__pb2.ConfigureShortCableCompValuesRequest.FromString,
                    response_serializer=nidmm__pb2.ConfigureShortCableCompValuesResponse.SerializeToString,
            ),
            'ConfigureWaveformAcquisition': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureWaveformAcquisition,
                    request_deserializer=nidmm__pb2.ConfigureWaveformAcquisitionRequest.FromString,
                    response_serializer=nidmm__pb2.ConfigureWaveformAcquisitionResponse.SerializeToString,
            ),
            'ConfigureWaveformCoupling': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureWaveformCoupling,
                    request_deserializer=nidmm__pb2.ConfigureWaveformCouplingRequest.FromString,
                    response_serializer=nidmm__pb2.ConfigureWaveformCouplingResponse.SerializeToString,
            ),
            'FetchWaveform': grpc.unary_unary_rpc_method_handler(
                    servicer.FetchWaveform,
                    request_deserializer=nidmm__pb2.FetchWaveformRequest.FromString,
                    response_serializer=nidmm__pb2.FetchWaveformResponse.SerializeToString,
            ),
            'ReadWaveform': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadWaveform,
                    request_deserializer=nidmm__pb2.ReadWaveformRequest.FromString,
                    response_serializer=nidmm__pb2.ReadWaveformResponse.SerializeToString,
            ),
            'GetAttributeViInt32': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViInt32,
                    request_deserializer=nidmm__pb2.GetAttributeViInt32Request.FromString,
                    response_serializer=nidmm__pb2.GetAttributeViInt32Response.SerializeToString,
            ),
            'SetAttributeViInt32': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttributeViInt32,
                    request_deserializer=nidmm__pb2.SetAttributeViInt32Request.FromString,
                    response_serializer=nidmm__pb2.SetAttributeViInt32Response.SerializeToString,
            ),
            'CheckAttributeViInt32': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckAttributeViInt32,
                    request_deserializer=nidmm__pb2.CheckAttributeViInt32Request.FromString,
                    response_serializer=nidmm__pb2.CheckAttributeViInt32Response.SerializeToString,
            ),
            'GetAttributeViReal64': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViReal64,
                    request_deserializer=nidmm__pb2.GetAttributeViReal64Request.FromString,
                    response_serializer=nidmm__pb2.GetAttributeViReal64Response.SerializeToString,
            ),
            'SetAttributeViReal64': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttributeViReal64,
                    request_deserializer=nidmm__pb2.SetAttributeViReal64Request.FromString,
                    response_serializer=nidmm__pb2.SetAttributeViReal64Response.SerializeToString,
            ),
            'CheckAttributeViReal64': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckAttributeViReal64,
                    request_deserializer=nidmm__pb2.CheckAttributeViReal64Request.FromString,
                    response_serializer=nidmm__pb2.CheckAttributeViReal64Response.SerializeToString,
            ),
            'GetAttributeViString': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViString,
                    request_deserializer=nidmm__pb2.GetAttributeViStringRequest.FromString,
                    response_serializer=nidmm__pb2.GetAttributeViStringResponse.SerializeToString,
            ),
            'SetAttributeViString': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttributeViString,
                    request_deserializer=nidmm__pb2.SetAttributeViStringRequest.FromString,
                    response_serializer=nidmm__pb2.SetAttributeViStringResponse.SerializeToString,
            ),
            'CheckAttributeViString': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckAttributeViString,
                    request_deserializer=nidmm__pb2.CheckAttributeViStringRequest.FromString,
                    response_serializer=nidmm__pb2.CheckAttributeViStringResponse.SerializeToString,
            ),
            'GetAttributeViSession': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViSession,
                    request_deserializer=nidmm__pb2.GetAttributeViSessionRequest.FromString,
                    response_serializer=nidmm__pb2.GetAttributeViSessionResponse.SerializeToString,
            ),
            'SetAttributeViSession': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttributeViSession,
                    request_deserializer=nidmm__pb2.SetAttributeViSessionRequest.FromString,
                    response_serializer=nidmm__pb2.SetAttributeViSessionResponse.SerializeToString,
            ),
            'CheckAttributeViSession': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckAttributeViSession,
                    request_deserializer=nidmm__pb2.CheckAttributeViSessionRequest.FromString,
                    response_serializer=nidmm__pb2.CheckAttributeViSessionResponse.SerializeToString,
            ),
            'GetAttributeViBoolean': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViBoolean,
                    request_deserializer=nidmm__pb2.GetAttributeViBooleanRequest.FromString,
                    response_serializer=nidmm__pb2.GetAttributeViBooleanResponse.SerializeToString,
            ),
            'SetAttributeViBoolean': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttributeViBoolean,
                    request_deserializer=nidmm__pb2.SetAttributeViBooleanRequest.FromString,
                    response_serializer=nidmm__pb2.SetAttributeViBooleanResponse.SerializeToString,
            ),
            'CheckAttributeViBoolean': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckAttributeViBoolean,
                    request_deserializer=nidmm__pb2.CheckAttributeViBooleanRequest.FromString,
                    response_serializer=nidmm__pb2.CheckAttributeViBooleanResponse.SerializeToString,
            ),
            'ImportAttributeConfigurationFile': grpc.unary_unary_rpc_method_handler(
                    servicer.ImportAttributeConfigurationFile,
                    request_deserializer=nidmm__pb2.ImportAttributeConfigurationFileRequest.FromString,
                    response_serializer=nidmm__pb2.ImportAttributeConfigurationFileResponse.SerializeToString,
            ),
            'ExportAttributeConfigurationFile': grpc.unary_unary_rpc_method_handler(
                    servicer.ExportAttributeConfigurationFile,
                    request_deserializer=nidmm__pb2.ExportAttributeConfigurationFileRequest.FromString,
                    response_serializer=nidmm__pb2.ExportAttributeConfigurationFileResponse.SerializeToString,
            ),
            'ImportAttributeConfigurationBuffer': grpc.unary_unary_rpc_method_handler(
                    servicer.ImportAttributeConfigurationBuffer,
                    request_deserializer=nidmm__pb2.ImportAttributeConfigurationBufferRequest.FromString,
                    response_serializer=nidmm__pb2.ImportAttributeConfigurationBufferResponse.SerializeToString,
            ),
            'ExportAttributeConfigurationBuffer': grpc.unary_unary_rpc_method_handler(
                    servicer.ExportAttributeConfigurationBuffer,
                    request_deserializer=nidmm__pb2.ExportAttributeConfigurationBufferRequest.FromString,
                    response_serializer=nidmm__pb2.ExportAttributeConfigurationBufferResponse.SerializeToString,
            ),
            'ResetInterchangeCheck': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetInterchangeCheck,
                    request_deserializer=nidmm__pb2.ResetInterchangeCheckRequest.FromString,
                    response_serializer=nidmm__pb2.ResetInterchangeCheckResponse.SerializeToString,
            ),
            'ClearInterchangeWarnings': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearInterchangeWarnings,
                    request_deserializer=nidmm__pb2.ClearInterchangeWarningsRequest.FromString,
                    response_serializer=nidmm__pb2.ClearInterchangeWarningsResponse.SerializeToString,
            ),
            'GetChannelName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetChannelName,
                    request_deserializer=nidmm__pb2.GetChannelNameRequest.FromString,
                    response_serializer=nidmm__pb2.GetChannelNameResponse.SerializeToString,
            ),
            'GetExtCalRecommendedInterval': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExtCalRecommendedInterval,
                    request_deserializer=nidmm__pb2.GetExtCalRecommendedIntervalRequest.FromString,
                    response_serializer=nidmm__pb2.GetExtCalRecommendedIntervalResponse.SerializeToString,
            ),
            'GetSelfCalSupported': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSelfCalSupported,
                    request_deserializer=nidmm__pb2.GetSelfCalSupportedRequest.FromString,
                    response_serializer=nidmm__pb2.GetSelfCalSupportedResponse.SerializeToString,
            ),
            'GetCalDateAndTime': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCalDateAndTime,
                    request_deserializer=nidmm__pb2.GetCalDateAndTimeRequest.FromString,
                    response_serializer=nidmm__pb2.GetCalDateAndTimeResponse.SerializeToString,
            ),
            'GetLastCalTemp': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLastCalTemp,
                    request_deserializer=nidmm__pb2.GetLastCalTempRequest.FromString,
                    response_serializer=nidmm__pb2.GetLastCalTempResponse.SerializeToString,
            ),
            'GetDevTemp': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDevTemp,
                    request_deserializer=nidmm__pb2.GetDevTempRequest.FromString,
                    response_serializer=nidmm__pb2.GetDevTempResponse.SerializeToString,
            ),
            'ConfigureTransducerType': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureTransducerType,
                    request_deserializer=nidmm__pb2.ConfigureTransducerTypeRequest.FromString,
                    response_serializer=nidmm__pb2.ConfigureTransducerTypeResponse.SerializeToString,
            ),
            'ConfigureThermocouple': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureThermocouple,
                    request_deserializer=nidmm__pb2.ConfigureThermocoupleRequest.FromString,
                    response_serializer=nidmm__pb2.ConfigureThermocoupleResponse.SerializeToString,
            ),
            'ConfigureFixedRefJunction': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureFixedRefJunction,
                    request_deserializer=nidmm__pb2.ConfigureFixedRefJunctionRequest.FromString,
                    response_serializer=nidmm__pb2.ConfigureFixedRefJunctionResponse.SerializeToString,
            ),
            'ConfigureRTDType': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureRTDType,
                    request_deserializer=nidmm__pb2.ConfigureRTDTypeRequest.FromString,
                    response_serializer=nidmm__pb2.ConfigureRTDTypeResponse.SerializeToString,
            ),
            'ConfigureRTDCustom': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureRTDCustom,
                    request_deserializer=nidmm__pb2.ConfigureRTDCustomRequest.FromString,
                    response_serializer=nidmm__pb2.ConfigureRTDCustomResponse.SerializeToString,
            ),
            'ConfigureThermistorType': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureThermistorType,
                    request_deserializer=nidmm__pb2.ConfigureThermistorTypeRequest.FromString,
                    response_serializer=nidmm__pb2.ConfigureThermistorTypeResponse.SerializeToString,
            ),
            'ConfigureThermistorCustom': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureThermistorCustom,
                    request_deserializer=nidmm__pb2.ConfigureThermistorCustomRequest.FromString,
                    response_serializer=nidmm__pb2.ConfigureThermistorCustomResponse.SerializeToString,
            ),
            'InvalidateAllAttributes': grpc.unary_unary_rpc_method_handler(
                    servicer.InvalidateAllAttributes,
                    request_deserializer=nidmm__pb2.InvalidateAllAttributesRequest.FromString,
                    response_serializer=nidmm__pb2.InvalidateAllAttributesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'nidmm_grpc.NiDmm', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NiDmm(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Init(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/Init',
            nidmm__pb2.InitRequest.SerializeToString,
            nidmm__pb2.InitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InitWithOptions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/InitWithOptions',
            nidmm__pb2.InitWithOptionsRequest.SerializeToString,
            nidmm__pb2.InitWithOptionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Close(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/Close',
            nidmm__pb2.CloseRequest.SerializeToString,
            nidmm__pb2.CloseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetError(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/GetError',
            nidmm__pb2.GetErrorRequest.SerializeToString,
            nidmm__pb2.GetErrorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetErrorMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/GetErrorMessage',
            nidmm__pb2.GetErrorMessageRequest.SerializeToString,
            nidmm__pb2.GetErrorMessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClearError(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ClearError',
            nidmm__pb2.ClearErrorRequest.SerializeToString,
            nidmm__pb2.ClearErrorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Reset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/Reset',
            nidmm__pb2.ResetRequest.SerializeToString,
            nidmm__pb2.ResetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SelfTest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/SelfTest',
            nidmm__pb2.SelfTestRequest.SerializeToString,
            nidmm__pb2.SelfTestResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SelfCal(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/SelfCal',
            nidmm__pb2.SelfCalRequest.SerializeToString,
            nidmm__pb2.SelfCalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RevisionQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/RevisionQuery',
            nidmm__pb2.RevisionQueryRequest.SerializeToString,
            nidmm__pb2.RevisionQueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResetWithDefaults(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ResetWithDefaults',
            nidmm__pb2.ResetWithDefaultsRequest.SerializeToString,
            nidmm__pb2.ResetWithDefaultsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Disable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/Disable',
            nidmm__pb2.DisableRequest.SerializeToString,
            nidmm__pb2.DisableResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMeasurementPeriod(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/GetMeasurementPeriod',
            nidmm__pb2.GetMeasurementPeriodRequest.SerializeToString,
            nidmm__pb2.GetMeasurementPeriodResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ConfigureTrigger',
            nidmm__pb2.ConfigureTriggerRequest.SerializeToString,
            nidmm__pb2.ConfigureTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/Read',
            nidmm__pb2.ReadRequest.SerializeToString,
            nidmm__pb2.ReadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Fetch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/Fetch',
            nidmm__pb2.FetchRequest.SerializeToString,
            nidmm__pb2.FetchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Abort(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/Abort',
            nidmm__pb2.AbortRequest.SerializeToString,
            nidmm__pb2.AbortResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Initiate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/Initiate',
            nidmm__pb2.InitiateRequest.SerializeToString,
            nidmm__pb2.InitiateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IsOverRange(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/IsOverRange',
            nidmm__pb2.IsOverRangeRequest.SerializeToString,
            nidmm__pb2.IsOverRangeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IsUnderRange(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/IsUnderRange',
            nidmm__pb2.IsUnderRangeRequest.SerializeToString,
            nidmm__pb2.IsUnderRangeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureACBandwidth(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ConfigureACBandwidth',
            nidmm__pb2.ConfigureACBandwidthRequest.SerializeToString,
            nidmm__pb2.ConfigureACBandwidthResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureFrequencyVoltageRange(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ConfigureFrequencyVoltageRange',
            nidmm__pb2.ConfigureFrequencyVoltageRangeRequest.SerializeToString,
            nidmm__pb2.ConfigureFrequencyVoltageRangeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureMeasCompleteDest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ConfigureMeasCompleteDest',
            nidmm__pb2.ConfigureMeasCompleteDestRequest.SerializeToString,
            nidmm__pb2.ConfigureMeasCompleteDestResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureMultiPoint(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ConfigureMultiPoint',
            nidmm__pb2.ConfigureMultiPointRequest.SerializeToString,
            nidmm__pb2.ConfigureMultiPointResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadMultiPoint(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ReadMultiPoint',
            nidmm__pb2.ReadMultiPointRequest.SerializeToString,
            nidmm__pb2.ReadMultiPointResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FetchMultiPoint(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/FetchMultiPoint',
            nidmm__pb2.FetchMultiPointRequest.SerializeToString,
            nidmm__pb2.FetchMultiPointResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureTriggerSlope(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ConfigureTriggerSlope',
            nidmm__pb2.ConfigureTriggerSlopeRequest.SerializeToString,
            nidmm__pb2.ConfigureTriggerSlopeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendSoftwareTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/SendSoftwareTrigger',
            nidmm__pb2.SendSoftwareTriggerRequest.SerializeToString,
            nidmm__pb2.SendSoftwareTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetApertureTimeInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/GetApertureTimeInfo',
            nidmm__pb2.GetApertureTimeInfoRequest.SerializeToString,
            nidmm__pb2.GetApertureTimeInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAutoRangeValue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/GetAutoRangeValue',
            nidmm__pb2.GetAutoRangeValueRequest.SerializeToString,
            nidmm__pb2.GetAutoRangeValueResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureAutoZeroMode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ConfigureAutoZeroMode',
            nidmm__pb2.ConfigureAutoZeroModeRequest.SerializeToString,
            nidmm__pb2.ConfigureAutoZeroModeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigurePowerLineFrequency(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ConfigurePowerLineFrequency',
            nidmm__pb2.ConfigurePowerLineFrequencyRequest.SerializeToString,
            nidmm__pb2.ConfigurePowerLineFrequencyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureMeasurementDigits(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ConfigureMeasurementDigits',
            nidmm__pb2.ConfigureMeasurementDigitsRequest.SerializeToString,
            nidmm__pb2.ConfigureMeasurementDigitsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureMeasurementAbsolute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ConfigureMeasurementAbsolute',
            nidmm__pb2.ConfigureMeasurementAbsoluteRequest.SerializeToString,
            nidmm__pb2.ConfigureMeasurementAbsoluteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureMeasCompleteSlope(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ConfigureMeasCompleteSlope',
            nidmm__pb2.ConfigureMeasCompleteSlopeRequest.SerializeToString,
            nidmm__pb2.ConfigureMeasCompleteSlopeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureSampleTriggerSlope(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ConfigureSampleTriggerSlope',
            nidmm__pb2.ConfigureSampleTriggerSlopeRequest.SerializeToString,
            nidmm__pb2.ConfigureSampleTriggerSlopeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ReadStatus',
            nidmm__pb2.ReadStatusRequest.SerializeToString,
            nidmm__pb2.ReadStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Control(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/Control',
            nidmm__pb2.ControlRequest.SerializeToString,
            nidmm__pb2.ControlResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureADCCalibration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ConfigureADCCalibration',
            nidmm__pb2.ConfigureADCCalibrationRequest.SerializeToString,
            nidmm__pb2.ConfigureADCCalibrationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureOffsetCompOhms(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ConfigureOffsetCompOhms',
            nidmm__pb2.ConfigureOffsetCompOhmsRequest.SerializeToString,
            nidmm__pb2.ConfigureOffsetCompOhmsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureCurrentSource(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ConfigureCurrentSource',
            nidmm__pb2.ConfigureCurrentSourceRequest.SerializeToString,
            nidmm__pb2.ConfigureCurrentSourceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureCableCompType(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ConfigureCableCompType',
            nidmm__pb2.ConfigureCableCompTypeRequest.SerializeToString,
            nidmm__pb2.ConfigureCableCompTypeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PerformOpenCableComp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/PerformOpenCableComp',
            nidmm__pb2.PerformOpenCableCompRequest.SerializeToString,
            nidmm__pb2.PerformOpenCableCompResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PerformShortCableComp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/PerformShortCableComp',
            nidmm__pb2.PerformShortCableCompRequest.SerializeToString,
            nidmm__pb2.PerformShortCableCompResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureOpenCableCompValues(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ConfigureOpenCableCompValues',
            nidmm__pb2.ConfigureOpenCableCompValuesRequest.SerializeToString,
            nidmm__pb2.ConfigureOpenCableCompValuesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureShortCableCompValues(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ConfigureShortCableCompValues',
            nidmm__pb2.ConfigureShortCableCompValuesRequest.SerializeToString,
            nidmm__pb2.ConfigureShortCableCompValuesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureWaveformAcquisition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ConfigureWaveformAcquisition',
            nidmm__pb2.ConfigureWaveformAcquisitionRequest.SerializeToString,
            nidmm__pb2.ConfigureWaveformAcquisitionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureWaveformCoupling(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ConfigureWaveformCoupling',
            nidmm__pb2.ConfigureWaveformCouplingRequest.SerializeToString,
            nidmm__pb2.ConfigureWaveformCouplingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FetchWaveform(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/FetchWaveform',
            nidmm__pb2.FetchWaveformRequest.SerializeToString,
            nidmm__pb2.FetchWaveformResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadWaveform(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ReadWaveform',
            nidmm__pb2.ReadWaveformRequest.SerializeToString,
            nidmm__pb2.ReadWaveformResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAttributeViInt32(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/GetAttributeViInt32',
            nidmm__pb2.GetAttributeViInt32Request.SerializeToString,
            nidmm__pb2.GetAttributeViInt32Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAttributeViInt32(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/SetAttributeViInt32',
            nidmm__pb2.SetAttributeViInt32Request.SerializeToString,
            nidmm__pb2.SetAttributeViInt32Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckAttributeViInt32(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/CheckAttributeViInt32',
            nidmm__pb2.CheckAttributeViInt32Request.SerializeToString,
            nidmm__pb2.CheckAttributeViInt32Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAttributeViReal64(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/GetAttributeViReal64',
            nidmm__pb2.GetAttributeViReal64Request.SerializeToString,
            nidmm__pb2.GetAttributeViReal64Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAttributeViReal64(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/SetAttributeViReal64',
            nidmm__pb2.SetAttributeViReal64Request.SerializeToString,
            nidmm__pb2.SetAttributeViReal64Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckAttributeViReal64(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/CheckAttributeViReal64',
            nidmm__pb2.CheckAttributeViReal64Request.SerializeToString,
            nidmm__pb2.CheckAttributeViReal64Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAttributeViString(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/GetAttributeViString',
            nidmm__pb2.GetAttributeViStringRequest.SerializeToString,
            nidmm__pb2.GetAttributeViStringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAttributeViString(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/SetAttributeViString',
            nidmm__pb2.SetAttributeViStringRequest.SerializeToString,
            nidmm__pb2.SetAttributeViStringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckAttributeViString(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/CheckAttributeViString',
            nidmm__pb2.CheckAttributeViStringRequest.SerializeToString,
            nidmm__pb2.CheckAttributeViStringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAttributeViSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/GetAttributeViSession',
            nidmm__pb2.GetAttributeViSessionRequest.SerializeToString,
            nidmm__pb2.GetAttributeViSessionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAttributeViSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/SetAttributeViSession',
            nidmm__pb2.SetAttributeViSessionRequest.SerializeToString,
            nidmm__pb2.SetAttributeViSessionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckAttributeViSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/CheckAttributeViSession',
            nidmm__pb2.CheckAttributeViSessionRequest.SerializeToString,
            nidmm__pb2.CheckAttributeViSessionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAttributeViBoolean(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/GetAttributeViBoolean',
            nidmm__pb2.GetAttributeViBooleanRequest.SerializeToString,
            nidmm__pb2.GetAttributeViBooleanResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAttributeViBoolean(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/SetAttributeViBoolean',
            nidmm__pb2.SetAttributeViBooleanRequest.SerializeToString,
            nidmm__pb2.SetAttributeViBooleanResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckAttributeViBoolean(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/CheckAttributeViBoolean',
            nidmm__pb2.CheckAttributeViBooleanRequest.SerializeToString,
            nidmm__pb2.CheckAttributeViBooleanResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ImportAttributeConfigurationFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ImportAttributeConfigurationFile',
            nidmm__pb2.ImportAttributeConfigurationFileRequest.SerializeToString,
            nidmm__pb2.ImportAttributeConfigurationFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExportAttributeConfigurationFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ExportAttributeConfigurationFile',
            nidmm__pb2.ExportAttributeConfigurationFileRequest.SerializeToString,
            nidmm__pb2.ExportAttributeConfigurationFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ImportAttributeConfigurationBuffer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ImportAttributeConfigurationBuffer',
            nidmm__pb2.ImportAttributeConfigurationBufferRequest.SerializeToString,
            nidmm__pb2.ImportAttributeConfigurationBufferResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExportAttributeConfigurationBuffer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ExportAttributeConfigurationBuffer',
            nidmm__pb2.ExportAttributeConfigurationBufferRequest.SerializeToString,
            nidmm__pb2.ExportAttributeConfigurationBufferResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResetInterchangeCheck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ResetInterchangeCheck',
            nidmm__pb2.ResetInterchangeCheckRequest.SerializeToString,
            nidmm__pb2.ResetInterchangeCheckResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClearInterchangeWarnings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ClearInterchangeWarnings',
            nidmm__pb2.ClearInterchangeWarningsRequest.SerializeToString,
            nidmm__pb2.ClearInterchangeWarningsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetChannelName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/GetChannelName',
            nidmm__pb2.GetChannelNameRequest.SerializeToString,
            nidmm__pb2.GetChannelNameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetExtCalRecommendedInterval(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/GetExtCalRecommendedInterval',
            nidmm__pb2.GetExtCalRecommendedIntervalRequest.SerializeToString,
            nidmm__pb2.GetExtCalRecommendedIntervalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSelfCalSupported(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/GetSelfCalSupported',
            nidmm__pb2.GetSelfCalSupportedRequest.SerializeToString,
            nidmm__pb2.GetSelfCalSupportedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCalDateAndTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/GetCalDateAndTime',
            nidmm__pb2.GetCalDateAndTimeRequest.SerializeToString,
            nidmm__pb2.GetCalDateAndTimeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLastCalTemp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/GetLastCalTemp',
            nidmm__pb2.GetLastCalTempRequest.SerializeToString,
            nidmm__pb2.GetLastCalTempResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDevTemp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/GetDevTemp',
            nidmm__pb2.GetDevTempRequest.SerializeToString,
            nidmm__pb2.GetDevTempResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureTransducerType(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ConfigureTransducerType',
            nidmm__pb2.ConfigureTransducerTypeRequest.SerializeToString,
            nidmm__pb2.ConfigureTransducerTypeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureThermocouple(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ConfigureThermocouple',
            nidmm__pb2.ConfigureThermocoupleRequest.SerializeToString,
            nidmm__pb2.ConfigureThermocoupleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureFixedRefJunction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ConfigureFixedRefJunction',
            nidmm__pb2.ConfigureFixedRefJunctionRequest.SerializeToString,
            nidmm__pb2.ConfigureFixedRefJunctionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureRTDType(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ConfigureRTDType',
            nidmm__pb2.ConfigureRTDTypeRequest.SerializeToString,
            nidmm__pb2.ConfigureRTDTypeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureRTDCustom(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ConfigureRTDCustom',
            nidmm__pb2.ConfigureRTDCustomRequest.SerializeToString,
            nidmm__pb2.ConfigureRTDCustomResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureThermistorType(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ConfigureThermistorType',
            nidmm__pb2.ConfigureThermistorTypeRequest.SerializeToString,
            nidmm__pb2.ConfigureThermistorTypeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureThermistorCustom(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/ConfigureThermistorCustom',
            nidmm__pb2.ConfigureThermistorCustomRequest.SerializeToString,
            nidmm__pb2.ConfigureThermistorCustomResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InvalidateAllAttributes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidmm_grpc.NiDmm/InvalidateAllAttributes',
            nidmm__pb2.InvalidateAllAttributesRequest.SerializeToString,
            nidmm__pb2.InvalidateAllAttributesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidmm/nidmm/session.py sha256=bd4df52626bba87105bf1ffa2bf174fd23a97efd9f29c2ae48d2acbe8f95f2b9 bytes=126858 -->
## FILE: generated/nidmm/nidmm/session.py

- repository: `ni/nimi-python`
- source_path: `generated/nidmm/nidmm/session.py`
- sha256: `bd4df52626bba87105bf1ffa2bf174fd23a97efd9f29c2ae48d2acbe8f95f2b9`
- bytes: 126858

````python
# -*- coding: utf-8 -*-
# This file was generated
import array  # noqa: F401
# Used by @ivi_synchronized
from functools import wraps

import nidmm._attributes as _attributes
import nidmm._converters as _converters
import nidmm._library_interpreter as _library_interpreter
import nidmm.enums as enums
import nidmm.errors as errors

import hightime

# Used for __repr__
import pprint
pp = pprint.PrettyPrinter(indent=4)


class _Acquisition(object):
    def __init__(self, session):
        self._session = session
        self._session._initiate()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session.abort()


# From https://stackoverflow.com/questions/5929107/decorators-with-parameters
def ivi_synchronized(f):
    @wraps(f)
    def aux(*xs, **kws):
        session = xs[0]  # parameter 0 is 'self' which is the session object
        with session.lock():
            return f(*xs, **kws)
    return aux


class _Lock(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        # _lock_session is called from the lock() function, not here
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session.unlock()


class _SessionBase(object):
    '''Base class for all NI-DMM sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    ac_max_freq = _attributes.AttributeViReal64(1250007)
    '''Type: float

    Specifies the maximum frequency component of the input signal for AC  measurements. This property is used only for error checking and verifies  that the value of this parameter is less than the maximum frequency  of the device. This property affects the DMM only when you set the   method property to AC measurements.
    The valid range is 1 Hz-300 kHz for the NI 4070/4071/4072, 10 Hz-100 kHz  for the NI 4065, and 20 Hz-25 kHz for the NI 4050 and NI 4060.
    '''
    ac_min_freq = _attributes.AttributeViReal64(1250006)
    '''Type: float

    Specifies the minimum frequency component of the input signal for AC  measurements. This property affects the DMM only when you set the  method property to AC measurements.
    The valid range is 1 Hz-300 kHz for the NI 4070/4071/4072, 10 Hz-100 kHz  for the NI 4065, and 20 Hz-25 kHz for the NI 4050 and NI 4060.
    '''
    adc_calibration = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ADCCalibration, 1150022)
    '''Type: enums.ADCCalibration

    For the NI 4070/4071/4072 only, specifies the ADC calibration mode.
    '''
    aperture_time = _attributes.AttributeViReal64(1250321)
    '''Type: float

    Specifies the measurement aperture time for the current configuration.  Aperture time is specified in units set by aperture_time_units. To  override the default aperture, set this property to the desired  aperture time after calling ConfigureMeasurement. To return to the  default, set this property to NIDMM_VAL_APERTURE_TIME_AUTO (-1).
    On the NI 4070/4071/4072, the minimum aperture time is 8.89 usec,  and the maximum aperture time is 149 sec. Any number of powerline cycles (PLCs)  within the minimum and maximum ranges is allowed on the NI 4070/4071/4072.
    On the NI 4065 the minimum aperture time is 333 µs, and the maximum aperture time  is 78.2 s. If setting the number of averages directly, the total measurement time is  aperture time X the number of averages, which must be less than 72.8 s. The aperture  times allowed are 333 µs, 667 µs, or multiples of 1.11 ms-for example 1.11 ms, 2.22 ms,  3.33 ms, and so on. If you set an aperture time other than 333 µs, 667 µs, or multiples  of 1.11 ms, the value will be coerced up to the next supported aperture time.
    On the NI 4060, when the powerline frequency is 60 Hz, the PLCs allowed are  1 PLC, 6 PLC, 12 PLC, and 120 PLC. When the powerline frequency is 50 Hz, the  PLCs allowed are 1 PLC, 5 PLC, 10 PLC, and 100 PLC.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    aperture_time_units = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ApertureTimeUnits, 1250322)
    '''Type: enums.ApertureTimeUnits

    Specifies the units of aperture time for the current configuration.
    The NI 4060 does not support an aperture time set in seconds.
    '''
    auto_range_value = _attributes.AttributeViReal64(1250331)
    '''Type: float

    Specifies the value of the range. If auto ranging, shows the actual value of  the active range. The value of this property is set during a read operation.
    '''
    auto_zero = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AutoZero, 1250332)
    '''Type: enums.AutoZero

    Specifies the AutoZero mode.
    The NI 4050 is not supported.
    '''
    buffer_size = _attributes.AttributeViInt32(1150037)
    '''Type: int

    Size in samples of the internal data buffer. Maximum is 134,217,727 (OX7FFFFFF) samples. When  set to NIDMM_VAL_BUFFER_SIZE_AUTO (-1), NI-DMM chooses the buffer size.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    cable_comp_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.CableCompensationType, 1150045)
    '''Type: enums.CableCompensationType

    For the NI 4072 only,  the type of cable compensation that is applied to the current capacitance  or inductance measurement for the current range.
    Changing the method or the range through this property or through configure_measurement_digits  resets the value of this property to the default value.
    '''
    channel_count = _attributes.AttributeViInt32(1050203)
    '''Type: int

    Indicates the number of channels that the specific instrument driver  supports. For each property for which the IVI_VAL_MULTI_CHANNEL flag  property is set, the IVI engine maintains a separate cache value for each  channel.
    '''
    current_source = _attributes.AttributeViReal64(1150025)
    '''Type: float

    Specifies the current source provided during diode measurements.
    The NI 4050 and NI 4060 are not supported.
    '''
    dc_bias = _attributes.AttributeViInt32(1150053)
    '''Type: int

    For the NI 4072 only, controls the available DC bias for capacitance measurements.
    '''
    dc_noise_rejection = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.DCNoiseRejection, 1150026)
    '''Type: enums.DCNoiseRejection

    Specifies the DC noise rejection mode.
    The NI 4050 and NI 4060 are not supported.
    '''
    driver_setup = _attributes.AttributeViString(1050007)
    '''Type: str

    This property indicates the Driver Setup string that the user specified when  initializing the driver.
    Some cases exist where the end-user must specify instrument driver options  at initialization time.  An example of this is specifying a particular  instrument model from among a family of instruments that the driver supports.   This is useful when using simulation.  The end-user can specify  driver-specific options through the DriverSetup keyword in the optionsString  parameter to the niDMM Init With Options.vi.
    If the user does not specify a Driver Setup string, this property returns  an empty string.
    '''
    freq_voltage_auto_range = _attributes.AttributeViReal64(1150044)
    '''Type: float

    For the NI 4070/4071/4072 only, specifies the value of the frequency voltage range.  If Auto Ranging, shows the actual value of the active frequency voltage range.  If not Auto Ranging, the value of this property is the same as that of  freq_voltage_range.
    '''
    freq_voltage_range = _attributes.AttributeViReal64(1250101)
    '''Type: float

    Specifies the maximum amplitude of the input signal for frequency  measurements.
    '''
    function = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.Function, 1250001)
    '''Type: enums.Function

    Specifies the measurement method.
    Refer to the method topic in  the NI Digital Multimeters Help for device-specific information.
    If you are setting this property directly, you must also set the operation_mode property,  which controls whether the DMM takes standard single or multipoint measurements, or acquires a waveform.  If you are programming properties directly, you must set the operation_mode property before  setting other configuration properties. If the operation_mode property is set to OperationMode.WAVEFORM,  the only valid method types are Method.WAVEFORM_VOLTAGE and Method.WAVEFORM_CURRENT. Set the  operation_mode property to OperationMode.IVIDMM to set all other method values.
    '''
    input_resistance = _attributes.AttributeViReal64(1150029)
    '''Type: float

    Specifies the input resistance of the instrument.
    The NI 4050 and NI 4060 are not supported.
    '''
    instrument_firmware_revision = _attributes.AttributeViString(1050510)
    '''Type: str

    A string containing the instrument firmware revision number.
    '''
    instrument_manufacturer = _attributes.AttributeViString(1050511)
    '''Type: str

    A string containing the manufacturer of the instrument.
    '''
    instrument_model = _attributes.AttributeViString(1050512)
    '''Type: str

    A string containing the instrument model.
    '''
    instrument_product_id = _attributes.AttributeViInt32(1150061)
    '''Type: int

    The PCI product ID.
    '''
    io_resource_descriptor = _attributes.AttributeViString(1050304)
    '''Type: str

    A string containing the resource descriptor of the instrument.
    '''
    lc_calculation_model = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.LCCalculationModel, 1150052)
    '''Type: enums.LCCalculationModel

    For the NI 4072 only, specifies the type of algorithm that the measurement processing uses for  capacitance and inductance measurements.
    '''
    lc_number_meas_to_average = _attributes.AttributeViInt32(1150055)
    '''Type: int

    For the NI 4072 only, specifies the number of LC measurements that are averaged to produce one reading.
    '''
    logical_name = _attributes.AttributeViString(1050305)
    '''Type: str

    A string containing the logical name of the instrument.
    '''
    meas_complete_dest = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.MeasurementCompleteDest, 1250305)
    '''Type: enums.MeasurementCompleteDest

    Specifies the destination of the measurement complete (MC) signal.
    The NI 4050 is not supported.
    To determine which values are supported by each device, refer to the LabWindows/CVI Trigger Routing section in  the NI Digital Multimeters Help.
    '''
    number_of_averages = _attributes.AttributeViInt32(1150032)
    '''Type: int

    Specifies the number of averages to perform in a measurement. For the NI 4070/4071/4072,  applies only when the aperture time is not set to AUTO and Auto Zero is ON.  The default is 1.
    The NI 4050 and NI 4060 are not supported.
    '''
    offset_comp_ohms = _attributes.AttributeViInt32(1150023)
    '''Type: int

    For the NI 4070/4071/4072 only, enables or disables offset compensated ohms.
    '''
    open_cable_comp_conductance = _attributes.AttributeViReal64(1150049)
    '''Type: float

    For the NI 4072 only, specifies the active part (conductance) of the open cable compensation.  The valid range is any real number greater than 0. The default value (-1.0)  indicates that compensation has not taken place.
    Changing the method or the range through this property or through configure_measurement_digits  resets the value of this property to the default value.
    '''
    open_cable_comp_susceptance = _attributes.AttributeViReal64(1150048)
    '''Type: float

    For the NI 4072 only, specifies the reactive part (susceptance) of the open cable compensation.  The valid range is any real number greater than 0. The default value (-1.0)  indicates that compensation has not taken place.
    Changing the method or the range through this property or through configure_measurement_digits  resets the value of this property to the default value.
    '''
    operation_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.OperationMode, 1150014)
    '''Type: enums.OperationMode

    Specifies how the NI 4065 and NI 4070/4071/4072 acquire data. When you call  configure_measurement_digits, NI-DMM sets this property to OperationMode.IVIDMM.  When you call configure_waveform_acquisition, NI-DMM sets this property to OperationMode.WAVEFORM.  If you are programming properties directly, you must set this property before  setting other configuration properties.
    '''
    powerline_freq = _attributes.AttributeViReal64(1250333)
    '''Type: float

    Specifies the powerline frequency. The NI 4050 and NI 4060 use this value to select an aperture time to reject  powerline noise by selecting the appropriate internal sample clock and filter. The NI 4065 and  NI 4070/4071/4072 use this value to select a timebase for setting the aperture_time  property in powerline cycles (PLCs).
    After configuring powerline frequency, set the aperture_time_units property to PLCs.  When setting the aperture_time property, select the number of PLCs for the powerline frequency.  For example, if powerline frequency = 50 Hz (or 20ms) and aperture time in PLCs = 5, then aperture time in  Seconds = 20ms * 5 PLCs = 100 ms. Similarly, if powerline frequency = 60 Hz (or 16.667 ms) and aperture time  in PLCs = 6, then aperture time in Seconds = 16.667 ms * 6 PLCs = 100 ms.
    '''
    range = _attributes.AttributeViReal64(1250002)
    '''Type: float

    Specifies the measurement range. Use positive values to represent the  absolute value of the maximum expected measurement. The value is in units  appropriate for the current value of the method property. For  example, if method is set to NIDMM_VAL_VOLTS, the units are  volts.
    The NI 4050 and NI 4060 only support Auto Range when the trigger and  sample trigger is set to IMMEDIATE.
    NIDMM_VAL_AUTO_RANGE_ON -1.0
    NI-DMM performs an Auto Range before acquiring the measurement.
    NIDMM_VAL_AUTO_RANGE_OFF -2.0
    NI-DMM sets the Range to the current auto_range_value and uses this range  for all subsequent measurements until the measurement configuration is changed.
    NIDMM_VAL_AUTO_RANGE_ONCE -3.0
    NI-DMM performs an Auto Range before acquiring the next measurement. The auto_range_value  is stored and used for all subsequent measurements until the measurement configuration is changed.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    resolution_absolute = _attributes.AttributeViReal64(1250008)
    '''Type: float

    Specifies the measurement resolution in absolute units. Setting this  property to higher values increases the measurement accuracy. Setting this  property to lower values increases the measurement speed.
    NI-DMM ignores this property for capacitance and inductance measurements on the NI 4072.  To achieve better resolution for such measurements, use the lc_number_meas_to_average property.
    '''
    resolution_digits = _attributes.AttributeViReal64(1250003)
    '''Type: float

    Specifies the measurement resolution in digits. Setting this  property to higher values increases the measurement accuracy. Setting this  property to lower values increases the measurement speed.
    NI-DMM ignores this property for capacitance and inductance measurements on the NI 4072.  To achieve better resolution for such measurements, use the lc_number_meas_to_average property.
    '''
    sample_count = _attributes.AttributeViInt32(1250301)
    '''Type: int

    Specifies the number of measurements the DMM takes each time it receives a  trigger in a multiple point acquisition.
    '''
    sample_interval = _attributes.AttributeViReal64TimeDeltaSeconds(1250303)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the amount of time in seconds the DMM waits between measurement cycles.  This property only applies when the sample_trigger property is set to INTERVAL.
    On the NI 4060, the value for this property is used as the settling time.  When this property is set to 0, the NI 4060 does not settle between  measurement cycles. The onboard timing resolution is 1 µs on the NI 4060.
    The NI 4065 and NI 4070/4071/4072 use the value specified in this property as additional  delay. On the NI 4065 and NI 4070/4071/4072, the onboard timing resolution is 34.72 ns and  the valid range is 0-149 s.
    Only positive values are valid when setting the sample interval.
    The NI 4050 is not supported.
    '''
    sample_trigger = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.SampleTrigger, 1250302)
    '''Type: enums.SampleTrigger

    Specifies the sample trigger source.
    To determine which values are supported by each device, refer to the LabWindows/CVI Trigger Routing section in  the NI Digital Multimeters Help.
    '''
    serial_number = _attributes.AttributeViString(1150054)
    '''Type: str

    A string containing the serial number of the instrument. This property corresponds  to the serial number label that is attached to most products.
    '''
    settle_time = _attributes.AttributeViReal64TimeDeltaSeconds(1150028)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the settling time in seconds. To override the default settling time,  set this property. To return to the default, set this property to  NIDMM_VAL_SETTLE_TIME_AUTO (-1).
    The NI 4050 and NI 4060 are not supported.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    short_cable_comp_reactance = _attributes.AttributeViReal64(1150046)
    '''Type: float

    For the NI 4072 only, represents the reactive part (reactance) of the short cable compensation.  The valid range is any real number greater than 0. The default value (-1)  indicates that compensation has not taken place.
    Changing the method or the range through this property or through configure_measurement_digits  resets the value of this property to the default value.
    '''
    short_cable_comp_resistance = _attributes.AttributeViReal64(1150047)
    '''Type: float

    For the NI 4072 only, represents the active part (resistance) of the short cable compensation.  The valid range is any real number greater than 0. The default value (-1)  indicates that compensation has not taken place.
    Changing the method or the range through this property or through configure_measurement_digits  resets the value of this property to the default value.
    '''
    simulate = _attributes.AttributeViBoolean(1050005)
    '''Type: bool

    Specifies whether or not to simulate instrument driver I/O operations. If  simulation is enabled, instrument driver methods perform range checking and  call IVI Get and Set methods, but they do not perform  instrument I/O. For output parameters that represent instrument data, the  instrument driver methods return calculated values.
    The default value is False (0). Use the __init__ method to  override this setting.
    Simulate can only be set within the InitWithOptions method.  The property value cannot be changed outside of the method.
    '''
    specific_driver_description = _attributes.AttributeViString(1050514)
    '''Type: str

    A string containing a description of the specific driver.
    '''
    specific_driver_major_version = _attributes.AttributeViInt32(1050503)
    '''Type: int

    Returns the major version number of this instrument driver.
    '''
    specific_driver_minor_version = _attributes.AttributeViInt32(1050504)
    '''Type: int

    The minor version number of this instrument driver.
    '''
    specific_driver_revision = _attributes.AttributeViString(1050551)
    '''Type: str

    A string that contains additional version information about this specific  instrument driver.
    '''
    specific_driver_vendor = _attributes.AttributeViString(1050513)
    '''Type: str

    A string containing the vendor of the specific driver.
    '''
    supported_instrument_models = _attributes.AttributeViString(1050327)
    '''Type: str

    A string containing the instrument models supported by the specific driver.
    '''
    temp_rtd_a = _attributes.AttributeViReal64(1150121)
    '''Type: float

    Specifies the Callendar-Van Dusen A coefficient for RTD scaling when the RTD Type property   is set to Custom. The default value is 3.9083e-3 (Pt3851).
    '''
    temp_rtd_b = _attributes.AttributeViReal64(1150122)
    '''Type: float

    Specifies the Callendar-Van Dusen B coefficient for RTD scaling when the RTD Type property  is set to Custom. The default value is -5.775e-7(Pt3851).
    '''
    temp_rtd_c = _attributes.AttributeViReal64(1150123)
    '''Type: float

    Specifies the Callendar-Van Dusen C coefficient for RTD scaling when the RTD Type property  is set to Custom. The default value is -4.183e-12(Pt3851).
    '''
    temp_rtd_res = _attributes.AttributeViReal64(1250242)
    '''Type: float

    Specifies the RTD resistance at 0 degrees Celsius. This applies to all supported RTDs,  including custom RTDs. The default value is 100 (?).
    '''
    temp_rtd_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.RTDType, 1150120)
    '''Type: enums.RTDType

    Specifies the type of RTD used to measure temperature. The default value is RTDType.PT3851.
    Refer to the temp_rtd_type topic in the NI Digital Multimeters Help for additional information about defined values.
    '''
    temp_tc_fixed_ref_junc = _attributes.AttributeViReal64(1250233)
    '''Type: float

    Specifies the reference junction temperature when a fixed reference junction is used to take  a thermocouple measurement. The default value is 25.0 (°C).
    '''
    temp_tc_ref_junc_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ThermocoupleReferenceJunctionType, 1250232)
    '''Type: enums.ThermocoupleReferenceJunctionType

    Specifies the type of reference junction to be used in the reference junction compensation  of a thermocouple. The only supported value, ThermocoupleReferenceJunctionType.FIXED, is fixed.
    '''
    temp_tc_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ThermocoupleType, 1250231)
    '''Type: enums.ThermocoupleType

    Specifies the type of thermocouple used to measure the temperature. The default value is ThermocoupleType.J.
    '''
    temp_thermistor_a = _attributes.AttributeViReal64(1150125)
    '''Type: float

    Specifies the Steinhart-Hart A coefficient for thermistor scaling when the Thermistor Type  property is set to Custom. The default value is 0.0010295 (44006).
    '''
    temp_thermistor_b = _attributes.AttributeViReal64(1150126)
    '''Type: float

    Specifies the Steinhart-Hart B coefficient for thermistor scaling when the Thermistor Type  proerty is set to Custom. The default value is 0.0002391 (44006).
    '''
    temp_thermistor_c = _attributes.AttributeViReal64(1150127)
    '''Type: float

    Specifies the Steinhart-Hart C coefficient for thermistor scaling when the Thermistor Type  property is set to Custom. The default value is 1.568e-7 (44006).
    '''
    temp_thermistor_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ThermistorType, 1150124)
    '''Type: enums.ThermistorType

    Specifies the type of thermistor used to measure the temperature. The default value is  ThermistorType.THERMISTOR_44006.
    Refer to the temp_thermistor_type topic in the NI Digital Multimeters Help for additional information about defined values.
    '''
    temp_transducer_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TransducerType, 1250201)
    '''Type: enums.TransducerType

    Specifies the type of device used to measure the temperature. The default value is NIDMM_VAL_4_THERMOCOUPLE.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    trigger_count = _attributes.AttributeViInt32(1250304)
    '''Type: int

    Specifies the number of triggers the DMM receives before returning to the  Idle state.
    This property can be set to any positive ViInt32 value for the NI 4065 and NI 4070/4071/4072.
    The NI 4050 and NI 4060 support this property being set to 1.
    Refer to the Multiple Point Acquisitions section of the NI Digital Multimeters Help for more information.
    '''
    trigger_delay = _attributes.AttributeViReal64TimeDeltaSeconds(1250005)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the time (in seconds) that the DMM waits after it has received a trigger before taking a measurement.  The default value is AUTO DELAY (-1), which means that the DMM waits an appropriate settling time before taking  the measurement. (-1) signifies that AUTO DELAY is on, and (-2) signifies that AUTO DELAY is off.
    The NI 4065 and NI 4070/4071/4072 use the value specified in this property as additional settling time.  For the The NI 4065 and NI 4070/4071/4072, the valid range for Trigger Delay is AUTO DELAY (-1) or 0.0-149.0  seconds and the onboard timing resolution is 34.72 ns.
    On the NI 4060, if this property is set to 0, the DMM does not settle before taking the measurement.  On the NI 4060, the valid range for AUTO DELAY (-1) is 0.0-12.0 seconds and the onboard timing resolution  is 100 ms.
    When using the NI 4050, this property must be set to AUTO DELAY (-1).
    Use positive values to set the trigger delay in seconds.
    Valid Range: NIDMM_VAL_AUTO_DELAY (-1.0), 0.0-12.0 seconds (NI 4060 only)
    Default Value: NIDMM_VAL_AUTO_DELAY

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    trigger_source = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerSource, 1250004)
    '''Type: enums.TriggerSource

    Specifies the trigger source. When _initiate is called, the DMM waits  for the trigger specified with this property. After it receives the trigger,  the DMM waits the length of time specified with the trigger_delay  property. The DMM then takes a measurement.
    This property is not supported on the NI 4050.
    To determine which values are supported by each device, refer to the LabWindows/CVI Trigger Routing section in  the NI Digital Multimeters Help.
    '''
    waveform_coupling = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.WaveformCoupling, 1150027)
    '''Type: enums.WaveformCoupling

    For the NI 4070/4071/4072 only, specifies the coupling during a waveform acquisition.
    '''
    waveform_points = _attributes.AttributeViInt32(1150019)
    '''Type: int

    For the NI 4070/4071/4072 only, specifies the number of points to acquire in a waveform acquisition.
    '''
    waveform_rate = _attributes.AttributeViReal64(1150018)
    '''Type: float

    For the NI 4070/4071/4072 only, specifies the rate of the waveform acquisition in Samples per second (S/s).  The valid Range is 10.0-1,800,000 S/s. Values are coerced to the  closest integer divisor of 1,800,000. The default value is 1,800,000.
    '''

    def __init__(self, repeated_capability_list, all_channels_in_session, interpreter, freeze_it=False):
        self._repeated_capability_list = repeated_capability_list
        self._repeated_capability = ','.join(repeated_capability_list)
        self._all_channels_in_session = all_channels_in_session
        self._interpreter = interpreter

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("repeated_capability_list=" + pp.pformat(repeated_capability_list))
        param_list.append("interpreter=" + pp.pformat(interpreter))
        self._param_list = ', '.join(param_list)

        # Finally, set _is_frozen to True which is used to prevent clients from accidentally adding
        # members when trying to set a property with a typo.
        self._is_frozen = freeze_it

    def __repr__(self):
        return '{0}.{1}({2})'.format('nidmm', self.__class__.__name__, self._param_list)

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("'{0}' object has no attribute '{1}'".format(type(self).__name__, key))
        object.__setattr__(self, key, value)

    ''' These are code-generated '''

    @ivi_synchronized
    def _get_attribute_vi_boolean(self, attribute_id):
        r'''_get_attribute_vi_boolean

        Queries the value of a ViBoolean property. You can use this method to
        get the values of instrument-specific properties and inherent IVI
        properties.

        If the property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled, and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nidmm.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nidmm.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_boolean`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (bool): Returns the current value of the property. Pass the address of a
                ViBoolean variable.

        '''
        attribute_value = self._interpreter.get_attribute_vi_boolean(self._repeated_capability, attribute_id)
        return attribute_value

    @ivi_synchronized
    def _get_attribute_vi_int32(self, attribute_id):
        r'''_get_attribute_vi_int32

        Queries the value of a ViInt32 property. You can use this method to
        get the values of instrument-specific properties and inherent IVI
        properties.

        If the property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled, and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nidmm.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nidmm.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int32`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (int): Returns the current value of the property. Pass the address of a
                ViInt32 variable.

        '''
        attribute_value = self._interpreter.get_attribute_vi_int32(self._repeated_capability, attribute_id)
        return attribute_value

    @ivi_synchronized
    def _get_attribute_vi_real64(self, attribute_id):
        r'''_get_attribute_vi_real64

        Queries the value of a ViReal64 property. You can use this method to
        get the values of instrument-specific properties and inherent IVI
        properties.

        If the property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled, and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nidmm.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nidmm.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_real64`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (float): Returns the current value of the property. Pass the address of a
                ViReal64 variable.

        '''
        attribute_value = self._interpreter.get_attribute_vi_real64(self._repeated_capability, attribute_id)
        return attribute_value

    @ivi_synchronized
    def _get_attribute_vi_string(self, attribute_id):
        r'''_get_attribute_vi_string

        Queries the value of a ViString property. You can use this method to
        get the values of instrument-specific properties and inherent IVI
        properties.

        If the property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled, and the currently cached value is invalid.
           You must provide a ViChar array to serve as a buffer for the value.
           You pass the number of bytes in the buffer as the Array Size
           parameter.

        Tip:
        This method can be called on specific channels within your :py:class:`nidmm.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nidmm.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_string`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (str): The buffer in which the method returns the current value of the
                property. The buffer must be of type ViChar and have at least as many
                bytes as indicated in the **Buffer_Size** parameter.

                If you specify 0 for the **Buffer_Size** parameter, you can pass
                VI_NULL for this parameter.

        '''
        attribute_value = self._interpreter.get_attribute_vi_string(self._repeated_capability, attribute_id)
        return attribute_value

    def lock(self):
        '''lock

        Obtains a multithread lock on the device session. Before doing so, the
        software waits until all other execution threads release their locks
        on the device session.

        Other threads may have obtained a lock on this session for the
        following reasons:

            -  The application called the lock method.
            -  A call to NI-DMM locked the session.
            -  After a call to the lock method returns
               successfully, no other threads can access the device session until
               you call the unlock method or exit out of the with block when using
               lock context manager.
            -  Use the lock method and the
               unlock method around a sequence of calls to
               instrument driver methods if you require that the device retain its
               settings through the end of the sequence.

        You can safely make nested calls to the lock method
        within the same thread. To completely unlock the session, you must
        balance each call to the lock method with a call to
        the unlock method.

        Returns:
            lock (context manager): When used in a with statement, nidmm.Session.lock acts as
            a context manager and unlock will be called when the with block is exited
        '''
        self._interpreter.lock()  # We do not call this in the context manager so that this function can
        # act standalone as well and let the client call unlock() explicitly. If they do use the context manager,
        # that will handle the unlock for them
        return _Lock(self)

    @ivi_synchronized
    def _set_attribute_vi_boolean(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_boolean

        This method sets the value of a ViBoolean property.

        This is a low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties.

        If the property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled, and the currently cached value is invalid
           or is different than the value you specify.

        This instrument driver contains high-level methods that set most of
        the instrument properties. It is best to use the high-level driver
        methods as much as possible. They handle order dependencies and
        multithread locking for you. In addition, they perform status checking
        only after setting all of the properties.

        In contrast, when you set multiple properties using the SetAttribute
        methods, the methods check the instrument status after each call.
        Also, when state caching is enabled, the high-level methods that
        configure multiple properties perform instrument I/O only for the
        properties whose value you change. Thus, you can safely call the
        high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nidmm.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nidmm.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_boolean`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (bool): Pass the value that you want to set the property to.

        '''
        self._interpreter.set_attribute_vi_boolean(self._repeated_capability, attribute_id, attribute_value)

    @ivi_synchronized
    def _set_attribute_vi_int32(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_int32

        This method sets the value of a ViInt32 property.

        This is a low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties.

        If the property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled, and the currently cached value is invalid
           or is different than the value you specify.

        This instrument driver contains high-level methods that set most of
        the instrument properties. It is best to use the high-level driver
        methods as much as possible. They handle order dependencies and
        multithread locking for you. In addition, they perform status checking
        only after setting all of the properties.

        In contrast, when you set multiple properties using the SetAttribute
        methods, the methods check the instrument status after each call.
        Also, when state caching is enabled, the high-level methods that
        configure multiple properties perform instrument I/O only for the
        properties whose value you change. Thus, you can safely call the
        high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nidmm.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nidmm.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int32`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (int): Pass the value that you want to set the property to.

        '''
        self._interpreter.set_attribute_vi_int32(self._repeated_capability, attribute_id, attribute_value)

    @ivi_synchronized
    def _set_attribute_vi_real64(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_real64

        This method sets the value of a ViReal64 property.

        This is a low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties.

        If the property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled, and the currently cached value is invalid
           or is different than the value you specify.

        This instrument driver contains high-level methods that set most of
        the instrument properties. It is best to use the high-level driver
        methods as much as possible. They handle order dependencies and
        multithread locking for you. In addition, they perform status checking
        only after setting all of the properties.

        In contrast, when you set multiple properties using the SetAttribute
        methods, the methods check the instrument status after each call.
        Also, when state caching is enabled, the high-level methods that
        configure multiple properties perform instrument I/O only for the
        properties whose value you change. Thus, you can safely call the
        high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nidmm.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nidmm.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_real64`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (float): Pass the value that you want to set the property to.

        '''
        self._interpreter.set_attribute_vi_real64(self._repeated_capability, attribute_id, attribute_value)

    @ivi_synchronized
    def _set_attribute_vi_string(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_string

        This method sets the value of a ViString property.

        This is a low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties.

        If the property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled, and the currently cached value is invalid
           or is different than the value you specify.

        This instrument driver contains high-level methods that set most of
        the instrument properties. It is best to use the high-level driver
        methods as much as possible. They handle order dependencies and
        multithread locking for you. In addition, they perform status checking
        only after setting all of the properties.

        In contrast, when you set multiple properties using the SetAttribute
        methods, the methods check the instrument status after each call.
        Also, when state caching is enabled, the high-level methods that
        configure multiple properties perform instrument I/O only for the
        properties whose value you change. Thus, you can safely call the
        high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nidmm.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nidmm.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_string`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (str): Pass the value that you want to set the property to.

        '''
        self._interpreter.set_attribute_vi_string(self._repeated_capability, attribute_id, attribute_value)

    def unlock(self):
        '''unlock

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        '''
        self._interpreter.unlock()

    def _error_message(self, error_code):
        r'''_error_message

        Takes the **Error_Code** returned by the instrument driver methods,
        interprets it, and returns it as a user-readable string.

        Note:
        When using grpc-device, this method will call GetErrorMessage server-side while providing the same interface.

        Args:
            error_code (int): The **error_code** returned from the instrument. The default is 0,
                indicating VI_SUCCESS.


        Returns:
            error_message (str): The error information formatted into a string.

        '''
        error_message = self._interpreter.error_message(error_code)
        return error_message


class Session(_SessionBase):
    '''An NI-DMM session to an NI digital multimeter'''

    def __init__(self, resource_name, id_query=False, reset_device=False, options={}, *, grpc_options=None):
        r'''An NI-DMM session to an NI digital multimeter

        This method completes the following tasks:

        -  Creates a new IVI instrument driver session and, optionally, sets the
           initial state of the following session properties:
           RANGE_CHECK, QUERY_INSTR_STATUS,
           CACHE, simulate,
           RECORD_COERCIONS.
        -  Opens a session to the device you specify for the **Resource_Name**
           parameter. If the **ID_Query** parameter is set to True, this
           method queries the instrument ID and checks that it is valid for
           this instrument driver.
        -  If the **Reset_Device** parameter is set to True, this method
           resets the instrument to a known state. Sends initialization commands
           to set the instrument to the state necessary for the operation of the
           instrument driver.
        -  Returns a ViSession handle that you use to identify the instrument in
           all subsequent instrument driver method calls.

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Args:
            resource_name (str): Caution:
                All IVI names for the **Resource_Name**, such as logical names or
                virtual names, are case-sensitive. If you use logical names, driver
                session names, or virtual names in your program, you must make sure that
                the name you use matches the name in the IVI Configuration Store file
                exactly, without any variations in the case of the characters in the
                name.

                | Contains the **resource_name** of the device to initialize. The
                  **resource_name** is assigned in Measurement & Automation Explorer
                  (MAX). Refer to `Related
                  Documentation <REPLACE_DRIVER_SPECIFIC_URL_1(related_documentation)>`__
                  for the *NI Digital Multimeters Getting Started Guide* for more
                  information about configuring and testing the DMM in MAX.
                | Valid Syntax:

                -  NI-DAQmx name
                -  DAQ::NI-DAQmx name[::INSTR]
                -  DAQ::Traditional NI-DAQ device number[::INSTR]
                -  IVI logical name

            id_query (bool): Verifies that the device you initialize is one that the driver supports.
                NI-DMM automatically performs this query, so setting this parameter is
                not necessary.
                Defined Values:

                +----------------+---+------------------+
                | True (default) | 1 | Perform ID Query |
                +----------------+---+------------------+
                | False          | 0 | Skip ID Query    |
                +----------------+---+------------------+

            reset_device (bool): Specifies whether to reset the instrument during the initialization
                procedure.
                Defined Values:

                +----------------+---+--------------+
                | True (default) | 1 | Reset Device |
                +----------------+---+--------------+
                | False          | 0 | Don't Reset  |
                +----------------+---+--------------+

            options (dict): Specifies the initial value of certain properties for the session. The
                syntax for **options** is a dictionary of properties with an assigned
                value. For example:

                { 'simulate': False }

                You do not have to specify a value for all the properties. If you do not
                specify a value for a property, the default value is used.

                Advanced Example:
                { 'simulate': True, 'driver_setup': { 'Model': '<model number>',  'BoardType': '<type>' } }

                +-------------------------+---------+
                | Property                | Default |
                +=========================+=========+
                | range_check             | True    |
                +-------------------------+---------+
                | query_instrument_status | False   |
                +-------------------------+---------+
                | cache                   | True    |
                +-------------------------+---------+
                | simulate                | False   |
                +-------------------------+---------+
                | record_value_coersions  | False   |
                +-------------------------+---------+
                | driver_setup            | {}      |
                +-------------------------+---------+

            grpc_options (nidmm.grpc_session_options.GrpcSessionOptions): MeasurementLink gRPC session options


        Returns:
            session (nidmm.Session): A session object representing the device.

        '''
        if grpc_options:
            import nidmm._grpc_stub_interpreter as _grpc_stub_interpreter
            interpreter = _grpc_stub_interpreter.GrpcStubInterpreter(grpc_options)
        else:
            interpreter = _library_interpreter.LibraryInterpreter(encoding='windows-1251')

        # Initialize the superclass with default values first, populate them later
        super(Session, self).__init__(
            repeated_capability_list=[],
            interpreter=interpreter,
            freeze_it=False,
            all_channels_in_session=None
        )
        options = _converters.convert_init_with_options_dictionary(options)

        # Call specified init function
        # Note that _interpreter default-initializes the session handle in its constructor, so that
        # if _init_with_options fails, the error handler can reference it.
        # And then here, once _init_with_options succeeds, we call set_session_handle
        # with the actual session handle.
        self._interpreter.set_session_handle(self._init_with_options(resource_name, id_query, reset_device, options))

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("resource_name=" + pp.pformat(resource_name))
        param_list.append("reset_device=" + pp.pformat(reset_device))
        param_list.append("options=" + pp.pformat(options))
        self._param_list = ', '.join(param_list)

        # Store the list of channels in the Session which is needed by some nimi-python modules.
        # Use try/except because not all the modules support channels.
        # self.get_channel_names() and self.channel_count can only be called after the session
        # handle is set
        try:
            self._all_channels_in_session = self.get_channel_names(range(self.channel_count))
        except AttributeError:
            self._all_channels_in_session = None

        # Finally, set _is_frozen to True which is used to prevent clients from accidentally adding
        # members when trying to set a property with a typo.
        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self._interpreter._close_on_exit:
            self.close()

    def initiate(self):
        '''initiate

        Initiates an acquisition. After you call this method, the DMM leaves
        the Idle state and enters the Wait-for-Trigger state. If trigger is set
        to Immediate mode, the DMM begins acquiring measurement data. Use
        fetch, fetch_multi_point, or fetch_waveform to
        retrieve the measurement data.

        Note:
        This method will return a Python context manager that will initiate on entering and abort on exit.
        '''
        return _Acquisition(self)

    def close(self):
        '''close

        Closes the specified session and deallocates resources that it reserved.

        Note:
        This method is not needed when using the session context manager
        '''
        try:
            self._close()
        except errors.DriverError:
            self._interpreter.set_session_handle()
            raise
        self._interpreter.set_session_handle()

    ''' These are code-generated '''

    @ivi_synchronized
    def abort(self):
        r'''abort

        Aborts a previously initiated measurement and returns the DMM to the
        Idle state.
        '''
        self._interpreter.abort()

    @ivi_synchronized
    def configure_measurement_absolute(self, measurement_function, range, resolution_absolute):
        r'''configure_measurement_absolute

        Configures the common properties of the measurement. These properties
        include method, range, and
        resolution_absolute.

        Args:
            measurement_function (enums.Function): Specifies the **measurement_function** used to acquire the measurement.
                The driver sets method to this value.

            range (float): Specifies the **range** for the method specified in the
                **Measurement_Function** parameter. When frequency is specified in the
                **Measurement_Function** parameter, you must supply the minimum
                frequency expected in the **range** parameter. For example, you must
                type in 100 Hz if you are measuring 101 Hz or higher.
                For all other methods, you must supply a **range** that exceeds the
                value that you are measuring. For example, you must type in 10 V if you
                are measuring 9 V. **range** values are coerced up to the closest input
                **range**. Refer to the `Devices
                Overview <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__ for a list of valid
                ranges. The driver sets range to this value. The default is
                0.02 V.

                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_RANGE_ON   | -1.0 | NI-DMM performs an Auto Range before acquiring the measurement.                                                                                                                         |
                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_RANGE_OFF  | -2.0 | NI-DMM sets the Range to the current auto_range_value and uses this range for all subsequent measurements until the measurement configuration is changed.                               |
                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_RANGE_ONCE | -3.0 | NI-DMM performs an Auto Range before acquiring the measurement. The auto_range_value is stored and used for all subsequent measurements until the measurement configuration is changed. |
                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

                Note:
                The NI 4050, NI 4060, and NI 4065 only support Auto Range when the
                trigger and sample trigger are set to IMMEDIATE.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            resolution_absolute (float): Specifies the absolute resolution for the measurement. NI-DMM sets
                resolution_absolute to this value. The PXIe-4080/4081/4082
                uses the resolution you specify. The NI 4065 and NI 4070/4071/4072
                ignore this parameter when the **Range** parameter is set to
                NIDMM_VAL_AUTO_RANGE_ON (-1.0) or NIDMM_VAL_AUTO_RANGE_ONCE
                (-3.0). The default is 0.001 V.

                Note:
                NI-DMM ignores this parameter for capacitance and inductance
                measurements on the NI 4072. To achieve better resolution for such
                measurements, use the lc_number_meas_to_average
                property.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        if type(measurement_function) is not enums.Function:
            raise TypeError('Parameter measurement_function must be of type ' + str(enums.Function))
        self._interpreter.configure_measurement_absolute(measurement_function, range, resolution_absolute)

    @ivi_synchronized
    def configure_measurement_digits(self, measurement_function, range, resolution_digits):
        r'''configure_measurement_digits

        Configures the common properties of the measurement. These properties
        include method, range, and
        resolution_digits.

        Args:
            measurement_function (enums.Function): Specifies the **measurement_function** used to acquire the measurement.
                The driver sets method to this value.

            range (float): Specifies the range for the method specified in the
                **Measurement_Function** parameter. When frequency is specified in the
                **Measurement_Function** parameter, you must supply the minimum
                frequency expected in the **range** parameter. For example, you must
                type in 100 Hz if you are measuring 101 Hz or higher.
                For all other methods, you must supply a range that exceeds the value
                that you are measuring. For example, you must type in 10 V if you are
                measuring 9 V. range values are coerced up to the closest input range.
                Refer to the `Devices
                Overview <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__ for a list of valid
                ranges. The driver sets range to this value. The default is
                0.02 V.

                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_RANGE_ON   | -1.0 | NI-DMM performs an Auto Range before acquiring the measurement.                                                                                                                         |
                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_RANGE_OFF  | -2.0 | NI-DMM sets the Range to the current auto_range_value and uses this range for all subsequent measurements until the measurement configuration is changed.                               |
                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_RANGE_ONCE | -3.0 | NI-DMM performs an Auto Range before acquiring the measurement. The auto_range_value is stored and used for all subsequent measurements until the measurement configuration is changed. |
                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

                Note:
                The NI 4050, NI 4060, and NI 4065 only support Auto Range when the
                trigger and sample trigger are set to IMMEDIATE.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            resolution_digits (float): Specifies the resolution of the measurement in digits. The driver sets
                the `Devices Overview <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__ for a
                list of valid ranges. The driver sets resolution_digits
                property to this value. The PXIe-4080/4081/4082 uses the resolution you
                specify. The NI 4065 and NI 4070/4071/4072 ignore this parameter when
                the **Range** parameter is set to NIDMM_VAL_AUTO_RANGE_ON (-1.0) or
                NIDMM_VAL_AUTO_RANGE_ONCE (-3.0). The default is 5½.

                Note:
                NI-DMM ignores this parameter for capacitance and inductance
                measurements on the NI 4072. To achieve better resolution for such
                measurements, use the lc_number_meas_to_average
                property.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        if type(measurement_function) is not enums.Function:
            raise TypeError('Parameter measurement_function must be of type ' + str(enums.Function))
        self._interpreter.configure_measurement_digits(measurement_function, range, resolution_digits)

    @ivi_synchronized
    def configure_multi_point(self, trigger_count, sample_count, sample_trigger=enums.SampleTrigger.IMMEDIATE, sample_interval=hightime.timedelta(seconds=-1)):
        r'''configure_multi_point

        Configures the properties for multipoint measurements. These properties
        include trigger_count, sample_count,
        sample_trigger, and sample_interval.

        For continuous acquisitions, set trigger_count or
        sample_count to zero. For more information, refer to
        `Multiple Point
        Acquisitions <REPLACE_DRIVER_SPECIFIC_URL_1(multi_point)>`__,
        `Triggering <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__, and `Using
        Switches <REPLACE_DRIVER_SPECIFIC_URL_1(switch_selection)>`__.

        Args:
            trigger_count (int): Sets the number of triggers you want the DMM to receive before returning
                to the Idle state. The driver sets trigger_count to this
                value. The default value is 1.

            sample_count (int): Sets the number of measurements the DMM makes in each measurement
                sequence initiated by a trigger. The driver sets
                sample_count to this value. The default value is 1.

            sample_trigger (enums.SampleTrigger): Specifies the **sample_trigger** source you want to use. The driver
                sets sample_trigger to this value. The default is
                Immediate.

                Note:
                To determine which values are supported by each device, refer to the
                `LabWindows/CVI Trigger
                Routing <REPLACE_DRIVER_SPECIFIC_URL_1(cvitrigger_routing)>`__ section.

            sample_interval (hightime.timedelta, datetime.timedelta, or float in seconds): Sets the amount of time in seconds the DMM waits between measurement
                cycles. The driver sets sample_interval to this value.
                Specify a sample interval to add settling time between measurement
                cycles or to decrease the measurement rate. **sample_interval** only
                applies when the **Sample_Trigger** is set to INTERVAL.

                On the NI 4060, the **sample_interval** value is used as the settling
                time. When sample interval is set to 0, the DMM does not settle between
                measurement cycles. The NI 4065 and NI 4070/4071/4072 use the value
                specified in **sample_interval** as additional delay. The default value
                (-1) ensures that the DMM settles for a recommended time. This is the
                same as using an Immediate trigger.

                Note: This property is not used on the NI 4080/4081/4082 and the NI 4050.

        '''
        if type(sample_trigger) is not enums.SampleTrigger:
            raise TypeError('Parameter sample_trigger must be of type ' + str(enums.SampleTrigger))
        sample_interval = _converters.convert_timedelta_to_seconds_real64(sample_interval)
        self._interpreter.configure_multi_point(trigger_count, sample_count, sample_trigger, sample_interval)

    @ivi_synchronized
    def configure_rtd_custom(self, rtd_a, rtd_b, rtd_c):
        r'''configure_rtd_custom

        Configures the A, B, and C parameters for a custom RTD.

        Args:
            rtd_a (float): Specifies the Callendar-Van Dusen A coefficient for RTD scaling when RTD
                Type parameter is set to Custom in the configure_rtd_type method.
                The default is 3.9083e-3 (Pt3851)

            rtd_b (float): Specifies the Callendar-Van Dusen B coefficient for RTD scaling when RTD
                Type parameter is set to Custom in the configure_rtd_type method.
                The default is -5.775e-7 (Pt3851).

            rtd_c (float): Specifies the Callendar-Van Dusen C coefficient for RTD scaling when RTD
                Type parameter is set to Custom in the configure_rtd_type method.
                The default is -4.183e-12 (Pt3851).

        '''
        self._interpreter.configure_rtd_custom(rtd_a, rtd_b, rtd_c)

    @ivi_synchronized
    def configure_rtd_type(self, rtd_type, rtd_resistance):
        r'''configure_rtd_type

        Configures the RTD Type and RTD Resistance parameters for an RTD.

        Args:
            rtd_type (enums.RTDType): Specifies the type of RTD used to measure the temperature resistance.
                NI-DMM uses this value to set the RTD Type property. The default is
                RTDType.PT3851.

                +---------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | Enum                            | Standards                                     | Material | TCR (α) | Typical R\ :sub:`0` (Ω) | Notes                                                                         |                               |
                +=================================+===============================================+==========+=========+=========================+===============================================================================+===============================+
                | Callendar-Van Dusen Coefficient |                                               |          |         |                         |                                                                               |                               |
                +---------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | RTDType.PT3851                  | IEC-751 DIN 43760 BS 1904 ASTM-E1137 EN-60751 | Platinum | .003851 | 100 Ω 1000 Ω            | A = 3.9083 × 10\ :sup:`–3` B = –5.775×10:sup:`–7` C = –4.183×10:sup:`–12`     | Most common RTDs              |
                +---------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | RTDType.PT3750                  | Low-cost vendor compliant RTD\*               | Platinum | .003750 | 1000 Ω                  | A = 3.81 × 10\ :sup:`–3` B = –6.02×10:sup:`–7` C = –6.0×10:sup:`–12`          | Low-cost RTD                  |
                +---------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | RTDType.PT3916                  | JISC 1604                                     | Platinum | .003916 | 100 Ω                   | A = 3.9739 × 10\ :sup:`–3` B = –5.870×10:sup:`–7` C = –4.4 ×10\ :sup:`–12`    | Used in primarily in Japan    |
                +---------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | RTDType.PT3920                  | US Industrial Standard D-100 American         | Platinum | .003920 | 100 Ω                   | A = 3.9787 × 10\ :sup:`–3` B = –5.8686×10:sup:`–7` C = –4.167 ×10\ :sup:`–12` | Low-cost RTD                  |
                +---------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | RTDType.PT3911                  | US Industrial Standard American               | Platinum | .003911 | 100 Ω                   | A = 3.9692 × 10\ :sup:`–3` B = –5.8495×10:sup:`–7` C = –4.233 ×10\ :sup:`–12` | Low-cost RTD                  |
                +---------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | RTDType.PT3928                  | ITS-90                                        | Platinum | .003928 | 100 Ω                   | A = 3.9888 × 10\ :sup:`–3` B = –5.915×10:sup:`–7` C = –3.85 ×10\ :sup:`–12`   | The definition of temperature |
                +---------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | \*No standard. Check the TCR.   |                                               |          |         |                         |                                                                               |                               |
                +---------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+

            rtd_resistance (float): Specifies the RTD resistance in ohms at 0 °C. NI-DMM uses this value to
                set the RTD Resistance property. The default is 100 (Ω).

        '''
        if type(rtd_type) is not enums.RTDType:
            raise TypeError('Parameter rtd_type must be of type ' + str(enums.RTDType))
        self._interpreter.configure_rtd_type(rtd_type, rtd_resistance)

    @ivi_synchronized
    def configure_thermistor_custom(self, thermistor_a, thermistor_b, thermistor_c):
        r'''configure_thermistor_custom

        Configures the A, B, and C parameters for a custom thermistor.

        Args:
            thermistor_a (float): Specifies the Steinhart-Hart A coefficient for thermistor scaling when
                Thermistor Type is set to Custom in the ConfigureThermistorType
                method. The default is 1.0295e-3 (44006).

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

            thermistor_b (float): Specifies the Steinhart-Hart B coefficient for thermistor scaling when
                Thermistor Type is set to Custom in the ConfigureThermistorType
                method. The default is 2.391e-4 (44006).

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

            thermistor_c (float): Specifies the Steinhart-Hart C coefficient for thermistor scaling when
                Thermistor Type is set to Custom in the ConfigureThermistorType
                method. The default is 1.568e-7 (44006).

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

        '''
        self._interpreter.configure_thermistor_custom(thermistor_a, thermistor_b, thermistor_c)

    @ivi_synchronized
    def configure_thermocouple(self, thermocouple_type, reference_junction_type=enums.ThermocoupleReferenceJunctionType.FIXED):
        r'''configure_thermocouple

        Configures the thermocouple type and reference junction type for a
        chosen thermocouple.

        Args:
            thermocouple_type (enums.ThermocoupleType): Specifies the type of thermocouple used to measure the temperature.
                NI-DMM uses this value to set the Thermocouple Type property. The
                default is ThermocoupleType.J.

                +--------------------+---------------------+
                | ThermocoupleType.B | Thermocouple type B |
                +--------------------+---------------------+
                | ThermocoupleType.E | Thermocouple type E |
                +--------------------+---------------------+
                | ThermocoupleType.J | Thermocouple type J |
                +--------------------+---------------------+
                | ThermocoupleType.K | Thermocouple type K |
                +--------------------+---------------------+
                | ThermocoupleType.N | Thermocouple type N |
                +--------------------+---------------------+
                | ThermocoupleType.R | Thermocouple type R |
                +--------------------+---------------------+
                | ThermocoupleType.S | Thermocouple type S |
                +--------------------+---------------------+
                | ThermocoupleType.T | Thermocouple type T |
                +--------------------+---------------------+

            reference_junction_type (enums.ThermocoupleReferenceJunctionType): Specifies the type of reference junction to be used in the reference
                junction compensation of a thermocouple measurement. NI-DMM uses this
                value to set the Reference Junction Type property. The only supported
                value is ThermocoupleReferenceJunctionType.FIXED.

        '''
        if type(thermocouple_type) is not enums.ThermocoupleType:
            raise TypeError('Parameter thermocouple_type must be of type ' + str(enums.ThermocoupleType))
        if type(reference_junction_type) is not enums.ThermocoupleReferenceJunctionType:
            raise TypeError('Parameter reference_junction_type must be of type ' + str(enums.ThermocoupleReferenceJunctionType))
        self._interpreter.configure_thermocouple(thermocouple_type, reference_junction_type)

    @ivi_synchronized
    def configure_trigger(self, trigger_source, trigger_delay=hightime.timedelta(seconds=-1)):
        r'''configure_trigger

        Configures the DMM **Trigger_Source** and **Trigger_Delay**. Refer to
        `Triggering <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__ and `Using
        Switches <REPLACE_DRIVER_SPECIFIC_URL_1(switch_selection)>`__ for more
        information.

        Args:
            trigger_source (enums.TriggerSource): Specifies the **trigger_source** that initiates the acquisition. The
                driver sets trigger_source to this value. Software
                configures the DMM to wait until send_software_trigger is called
                before triggering the DMM.

                Note:
                To determine which values are supported by each device, refer to the
                `LabWindows/CVI Trigger
                Routing <REPLACE_DRIVER_SPECIFIC_URL_1(cvitrigger_routing)>`__ section.

            trigger_delay (hightime.timedelta, datetime.timedelta, or float in seconds): Specifies the time that the DMM waits after it has received a trigger
                before taking a measurement. The driver sets the
                trigger_delay property to this value. By default,
                **trigger_delay** is NIDMM_VAL_AUTO_DELAY (-1), which means the DMM
                waits an appropriate settling time before taking the measurement. On the
                NI 4060, if you set **trigger_delay** to 0, the DMM does not settle
                before taking the measurement. The NI 4065 and NI 4070/4071/4072 use the
                value specified in **trigger_delay** as additional settling time.

                Note:
                When using the NI 4050, **Trigger_Delay** must be set to
                NIDMM_VAL_AUTO_DELAY (-1).

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        if type(trigger_source) is not enums.TriggerSource:
            raise TypeError('Parameter trigger_source must be of type ' + str(enums.TriggerSource))
        trigger_delay = _converters.convert_timedelta_to_seconds_real64(trigger_delay)
        self._interpreter.configure_trigger(trigger_source, trigger_delay)

    @ivi_synchronized
    def configure_waveform_acquisition(self, measurement_function, range, rate, waveform_points):
        r'''configure_waveform_acquisition

        Configures the DMM for waveform acquisitions. This feature is supported
        on the NI 4080/4081/4082 and the NI 4070/4071/4072.

        Args:
            measurement_function (enums.Function): Specifies the **measurement_function** used in a waveform acquisition.
                The driver sets method to this value.

                +-----------------------------------+------+------------------+
                | Method.WAVEFORM_VOLTAGE (default) | 1003 | Voltage Waveform |
                +-----------------------------------+------+------------------+
                | Method.WAVEFORM_CURRENT           | 1004 | Current Waveform |
                +-----------------------------------+------+------------------+

            range (float): Specifies the expected maximum amplitude of the input signal and sets
                the **range** for the **Measurement_Function**. NI-DMM sets
                range to this value. **range** values are coerced up to the
                closest input **range**. The default is 10.0.

                For valid ranges refer to the topics in
                `Devices <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__.

                Auto-ranging is not supported during waveform acquisitions.

            rate (float): Specifies the **rate** of the acquisition in samples per second. NI-DMM
                sets waveform_rate to this value.

                The valid **Range** is 10.0–1,800,000 S/s. **rate** values are coerced
                to the closest integer divisor of 1,800,000. The default value is
                1,800,000.

            waveform_points (int): Specifies the number of points to acquire before the waveform
                acquisition completes. NI-DMM sets waveform_points to this
                value.

                To calculate the maximum and minimum number of waveform points that you
                can acquire in one acquisition, refer to the `Waveform Acquisition
                Measurement Cycle <REPLACE_DRIVER_SPECIFIC_URL_1(waveform_cycle)>`__.

                The default value is 500.

        '''
        if type(measurement_function) is not enums.Function:
            raise TypeError('Parameter measurement_function must be of type ' + str(enums.Function))
        self._interpreter.configure_waveform_acquisition(measurement_function, range, rate, waveform_points)

    @ivi_synchronized
    def disable(self):
        r'''disable

        Places the instrument in a quiescent state where it has minimal or no
        impact on the system to which it is connected. If a measurement is in
        progress when this method is called, the measurement is aborted.
        '''
        self._interpreter.disable()

    @ivi_synchronized
    def export_attribute_configuration_buffer(self):
        r'''export_attribute_configuration_buffer

        Exports the property configuration of the session to the specified
        configuration buffer.

        You can export and import session property configurations only between
        devices with identical model numbers.

        This method verifies that the properties you have configured for the
        session are valid. If the configuration is invalid, NI‑DMM returns an
        error.

        **Coercion Behavior for Certain Devices**

        Imported and exported property configurations contain coerced values
        for the following NI‑DMM devices:

        -  PXI/PCI/PCIe/USB‑4065
        -  PXI/PCI‑4070
        -  PXI‑4071
        -  PXI‑4072

        NI‑DMM coerces property values when the value you set is within the
        allowed range for the property but is not one of the discrete valid
        values the property supports. For example, for a property that
        coerces values up, if you choose a value of 4 when the adjacent valid
        values are 1 and 10, the property coerces the value to 10.

        **Related Topics:**

        `Using Properties and Properties with
        NI‑DMM <REPLACE_DRIVER_SPECIFIC_URL_1(properties)>`__

        `Setting Properties Before Reading
        Properties <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

        Note: Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.

        Returns:
            configuration (bytes): Specifies the byte array buffer to be populated with the exported
                property configuration.

        '''
        configuration = self._interpreter.export_attribute_configuration_buffer()
        return _converters.convert_to_bytes(configuration)

    @ivi_synchronized
    def export_attribute_configuration_file(self, file_path):
        r'''export_attribute_configuration_file

        Exports the property configuration of the session to the specified
        file.

        You can export and import session property configurations only between
        devices with identical model numbers.

        This method verifies that the properties you have configured for the
        session are valid. If the configuration is invalid, NI‑DMM returns an
        error.

        **Coercion Behavior for Certain Devices**

        Imported and exported property configurations contain coerced values
        for the following NI‑DMM devices:

        -  PXI/PCI/PCIe/USB‑4065
        -  PXI/PCI‑4070
        -  PXI‑4071
        -  PXI‑4072

        NI‑DMM coerces property values when the value you set is within the
        allowed range for the property but is not one of the discrete valid
        values the property supports. For example, for a property that
        coerces values up, if you choose a value of 4 when the adjacent valid
        values are 1 and 10, the property coerces the value to 10.

        **Related Topics:**

        `Using Properties and Properties with
        NI‑DMM <REPLACE_DRIVER_SPECIFIC_URL_1(properties)>`__

        `Setting Properties Before Reading
        Properties <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

        Note: Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.

        Args:
            file_path (str): Specifies the absolute path to the file to contain the exported
                property configuration. If you specify an empty or relative path, this
                method returns an error.
                **Default file extension:**\  .nidmmconfig

        '''
        self._interpreter.export_attribute_configuration_file(file_path)

    @ivi_synchronized
    def fetch(self, maximum_time=hightime.timedelta(milliseconds=-1)):
        r'''fetch

        Returns the value from a previously initiated measurement. You must call
        _initiate before calling this method. Value is in base units.

        Args:
            maximum_time (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            reading (float): The measured value returned from the DMM.

        '''
        maximum_time = _converters.convert_timedelta_to_milliseconds_int32(maximum_time)
        reading = self._interpreter.fetch(maximum_time)
        return reading

    @ivi_synchronized
    def fetch_multi_point(self, array_size, maximum_time=hightime.timedelta(milliseconds=-1)):
        r'''fetch_multi_point

        Returns an array of values from a previously initiated multipoint
        measurement. The number of measurements the DMM makes is determined by
        the values you specify for the **Trigger_Count** and **Sample_Count**
        parameters of configure_multi_point. You must first call
        _initiate to initiate a measurement before calling this method. Values are in base units.

        Args:
            array_size (int): Specifies the number of measurements to acquire. The maximum number of
                measurements for a finite acquisition is the (**Trigger Count** x
                **Sample Count**) parameters in configure_multi_point.

                For continuous acquisitions, up to 100,000 points can be returned at
                once. The number of measurements can be a subset. The valid range is any
                positive ViInt32. The default value is 1.

            maximum_time (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            reading_array (array.array("d")): An array of measurement values.

                Note:
                The size of the **Reading_Array** must be at least the size that you
                specify for the **Array_Size** parameter.

        '''
        maximum_time = _converters.convert_timedelta_to_milliseconds_int32(maximum_time)
        reading_array = self._interpreter.fetch_multi_point(maximum_time, array_size)
        return reading_array

    @ivi_synchronized
    def fetch_waveform(self, array_size, maximum_time=hightime.timedelta(milliseconds=-1)):
        r'''fetch_waveform

        For the NI 4080/4081/4082 and the NI 4070/4071/4072, returns an array of
        values from a previously initiated waveform acquisition. You must call
        _initiate before calling this method.

        Args:
            array_size (int): Specifies the number of waveform points to return. You specify the total
                number of points that the DMM acquires in the **Waveform Points**
                parameter of configure_waveform_acquisition. The default value is
                1.

            maximum_time (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            waveform_array (array.array("d")): **Waveform Array** is an array of measurement values stored in waveform
                data type.

        '''
        maximum_time = _converters.convert_timedelta_to_milliseconds_int32(maximum_time)
        waveform_array = self._interpreter.fetch_waveform(maximum_time, array_size)
        return waveform_array

    @ivi_synchronized
    def fetch_waveform_into(self, waveform_array, maximum_time=hightime.timedelta(milliseconds=-1)):
        r'''fetch_waveform_into

        For the NI 4080/4081/4082 and the NI 4070/4071/4072, returns an array of
        values from a previously initiated waveform acquisition. You must call
        _initiate before calling this method.

        Args:
            waveform_array (numpy.array(dtype=numpy.float64)): **Waveform Array** is an array of measurement values stored in waveform
                data type.

            maximum_time (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        import numpy

        if type(waveform_array) is not numpy.ndarray:
            raise TypeError('waveform_array must be {0}, is {1}'.format(numpy.ndarray, type(waveform_array)))
        if numpy.isfortran(waveform_array) is True:
            raise TypeError('waveform_array must be in C-order')
        if waveform_array.dtype is not numpy.dtype('float64'):
            raise TypeError('waveform_array must be numpy.ndarray of dtype=float64, is ' + str(waveform_array.dtype))
        maximum_time = _converters.convert_timedelta_to_milliseconds_int32(maximum_time)
        self._interpreter.fetch_waveform_into(waveform_array, maximum_time)

    @ivi_synchronized
    def _get_cal_date_and_time(self, cal_type):
        r'''_get_cal_date_and_time

        Returns the date and time of the last calibration performed.

        Note: The NI 4050 and NI 4060 are not supported.

        Args:
            cal_type (int): Specifies the type of calibration performed (external or
                self-calibration).

                +-----------------------------------+---+----------------------+
                | NIDMM_VAL_INTERNAL_AREA (default) | 0 | Self-Calibration     |
                +-----------------------------------+---+----------------------+
                | NIDMM_VAL_EXTERNAL_AREA           | 1 | External Calibration |
                +-----------------------------------+---+----------------------+

                Note: The NI 4065 does not support self-calibration.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            month (int): Indicates the **month** of the last calibration.

            day (int): Indicates the **day** of the last calibration.

            year (int): Indicates the **year** of the last calibration.

            hour (int): Indicates the **hour** of the last calibration.

            minute (int): Indicates the **minute** of the last calibration.

        '''
        month, day, year, hour, minute = self._interpreter.get_cal_date_and_time(cal_type)
        return month, day, year, hour, minute

    @ivi_synchronized
    def get_dev_temp(self, options=""):
        r'''get_dev_temp

        Returns the current **Temperature** of the device.

        Note: The NI 4050 and NI 4060 are not supported.

        Args:
            options (str): Reserved.


        Returns:
            temperature (float): Returns the current **temperature** of the device.

        '''
        temperature = self._interpreter.get_dev_temp(options)
        return temperature

    @ivi_synchronized
    def get_ext_cal_recommended_interval(self):
        r'''get_ext_cal_recommended_interval

        Returns the recommended interval between external recalibration in
        **Months**.

        Note: The NI 4050 and NI 4060 are not supported.

        Returns:
            months (hightime.timedelta): Returns the recommended number of **months** between external
                calibrations.

        '''
        months = self._interpreter.get_ext_cal_recommended_interval()
        return _converters.convert_month_to_timedelta(months)

    @ivi_synchronized
    def get_cal_date_and_time(self, cal_type):
        '''get_cal_date_and_time

        Returns the date and time of the last calibration performed.

        Note: The NI 4050 and NI 4060 are not supported.

        Args:
            cal_type (int): Specifies the type of calibration performed (external or self-calibration).

                +-----------------------------------+---+----------------------+
                | NIDMM_VAL_INTERNAL_AREA (default) | 0 | Self-Calibration     |
                +-----------------------------------+---+----------------------+
                | NIDMM_VAL_EXTERNAL_AREA           | 1 | External Calibration |
                +-----------------------------------+---+----------------------+

                Note: The NI 4065 does not support self-calibration.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            last_cal_datetime (hightime.datetime): Indicates date and time of the last calibration.

        '''
        month, day, year, hour, minute = self._get_cal_date_and_time(cal_type)
        return hightime.datetime(year, month, day, hour, minute)

    @ivi_synchronized
    def get_last_cal_temp(self, cal_type):
        r'''get_last_cal_temp

        Returns the **Temperature** during the last calibration procedure.

        Note: The NI 4050 and NI 4060 are not supported.

        Args:
            cal_type (int): Specifies the type of calibration performed (external or
                self-calibration).

                +-----------------------------------+---+----------------------+
                | NIDMM_VAL_INTERNAL_AREA (default) | 0 | Self-Calibration     |
                +-----------------------------------+---+----------------------+
                | NIDMM_VAL_EXTERNAL_AREA           | 1 | External Calibration |
                +-----------------------------------+---+----------------------+

                Note: The NI 4065 does not support self-calibration.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            temperature (float): Returns the **temperature** during the last calibration.

        '''
        temperature = self._interpreter.get_last_cal_temp(cal_type)
        return temperature

    @ivi_synchronized
    def get_self_cal_supported(self):
        r'''get_self_cal_supported

        Returns a Boolean value that expresses whether or not the DMM that you
        are using can perform self-calibration.

        Returns:
            self_cal_supported (bool): Returns whether Self Cal is supported for the device specified by the
                given session.

                +-------+---+-------------------------------------------------------------+
                | True  | 1 | The DMM that you are using can perform self-calibration.    |
                +-------+---+-------------------------------------------------------------+
                | False | 0 | The DMM that you are using cannot perform self-calibration. |
                +-------+---+-------------------------------------------------------------+

        '''
        self_cal_supported = self._interpreter.get_self_cal_supported()
        return self_cal_supported

    @ivi_synchronized
    def import_attribute_configuration_buffer(self, configuration):
        r'''import_attribute_configuration_buffer

        Imports a property configuration to the session from the specified
        configuration buffer.

        You can export and import session property configurations only between
        devices with identical model numbers.

        **Coercion Behavior for Certain Devices**

        Imported and exported property configurations contain coerced values
        for the following NI‑DMM devices:

        -  PXI/PCI/PCIe/USB‑4065
        -  PXI/PCI‑4070
        -  PXI‑4071
        -  PXI‑4072

        NI‑DMM coerces property values when the value you set is within the
        allowed range for the property but is not one of the discrete valid
        values the property supports. For example, for a property that
        coerces values up, if you choose a value of 4 when the adjacent valid
        values are 1 and 10, the property coerces the value to 10.

        **Related Topics:**

        `Using Properties and Properties with
        NI‑DMM <REPLACE_DRIVER_SPECIFIC_URL_1(properties)>`__

        `Setting Properties Before Reading
        Properties <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

        Note: Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.

        Args:
            configuration (bytes): Specifies the byte array buffer that contains the property
                configuration to import.

        '''
        configuration = _converters.convert_to_bytes(configuration)
        self._interpreter.import_attribute_configuration_buffer(configuration)

    @ivi_synchronized
    def import_attribute_configuration_file(self, file_path):
        r'''import_attribute_configuration_file

        Imports a property configuration to the session from the specified
        file.

        You can export and import session property configurations only between
        devices with identical model numbers.

        **Coercion Behavior for Certain Devices**

        Imported and exported property configurations contain coerced values
        for the following NI‑DMM devices:

        -  PXI/PCI/PCIe/USB‑4065
        -  PXI/PCI‑4070
        -  PXI‑4071
        -  PXI‑4072

        NI‑DMM coerces property values when the value you set is within the
        allowed range for the property but is not one of the discrete valid
        values the property supports. For example, for a property that
        coerces values up, if you choose a value of 4 when the adjacent valid
        values are 1 and 10, the property coerces the value to 10.

        **Related Topics:**

        `Using Properties and Properties with
        NI‑DMM <REPLACE_DRIVER_SPECIFIC_URL_1(properties)>`__

        `Setting Properties Before Reading
        Properties <javascript:LaunchHelp('DMM.chm::/setting_before_reading_attributes')>`__

        Note: Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.

        Args:
            file_path (str): Specifies the absolute path to the file containing the property
                configuration to import. If you specify an empty or relative path, this
                method returns an error.
                **Default File Extension:**\  .nidmmconfig

        '''
        self._interpreter.import_attribute_configuration_file(file_path)

    def _init_with_options(self, resource_name, id_query=False, reset_device=False, option_string=""):
        r'''_init_with_options

        This method completes the following tasks:

        -  Creates a new IVI instrument driver session and, optionally, sets the
           initial state of the following session properties:
           RANGE_CHECK, QUERY_INSTR_STATUS,
           CACHE, simulate,
           RECORD_COERCIONS.
        -  Opens a session to the device you specify for the **Resource_Name**
           parameter. If the **ID_Query** parameter is set to True, this
           method queries the instrument ID and checks that it is valid for
           this instrument driver.
        -  If the **Reset_Device** parameter is set to True, this method
           resets the instrument to a known state. Sends initialization commands
           to set the instrument to the state necessary for the operation of the
           instrument driver.
        -  Returns a ViSession handle that you use to identify the instrument in
           all subsequent instrument driver method calls.

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Args:
            resource_name (str): Caution:
                All IVI names for the **Resource_Name**, such as logical names or
                virtual names, are case-sensitive. If you use logical names, driver
                session names, or virtual names in your program, you must make sure that
                the name you use matches the name in the IVI Configuration Store file
                exactly, without any variations in the case of the characters in the
                name.

                | Contains the **resource_name** of the device to initialize. The
                  **resource_name** is assigned in Measurement & Automation Explorer
                  (MAX). Refer to `Related
                  Documentation <REPLACE_DRIVER_SPECIFIC_URL_1(related_documentation)>`__
                  for the *NI Digital Multimeters Getting Started Guide* for more
                  information about configuring and testing the DMM in MAX.
                | Valid Syntax:

                -  NI-DAQmx name
                -  DAQ::NI-DAQmx name[::INSTR]
                -  DAQ::Traditional NI-DAQ device number[::INSTR]
                -  IVI logical name

            id_query (bool): Verifies that the device you initialize is one that the driver supports.
                NI-DMM automatically performs this query, so setting this parameter is
                not necessary.
                Defined Values:

                +----------------+---+------------------+
                | True (default) | 1 | Perform ID Query |
                +----------------+---+------------------+
                | False          | 0 | Skip ID Query    |
                +----------------+---+------------------+

            reset_device (bool): Specifies whether to reset the instrument during the initialization
                procedure.
                Defined Values:

                +----------------+---+--------------+
                | True (default) | 1 | Reset Device |
                +----------------+---+--------------+
                | False          | 0 | Don't Reset  |
                +----------------+---+--------------+

            option_string (dict): | Sets the initial value of certain properties for the session. The
                  following table specifies the property name, property constant, and
                  default value for each property that you can use in this parameter:

                The format of this string is, "AttributeName=Value." To set multiple
                properties, separate their assignments with a comma.

                If you pass NULL or an empty string for this parameter, the session uses
                the default values for the properties. You can override the default
                values by assigning a value explicitly in an **option_string**
                parameter. You do not have to specify all of the properties and may
                leave any of them out (those left out use the default value).

                Refer to `Simulating NI Digital
                Multimeters <REPLACE_DRIVER_SPECIFIC_URL_1(simulation)>`__ for more
                information.

                +------------------+--------------------+-------------------+----+
                | Check            | RANGE_CHECK        | True              | 1  |
                +------------------+--------------------+-------------------+----+
                | QueryInstrStatus | QUERY_INSTR_STATUS | False             | 0  |
                +------------------+--------------------+-------------------+----+
                | Cache            | CACHE              | True              | 1  |
                +------------------+--------------------+-------------------+----+
                | Simulate         | simulate           | False             | 0  |
                +------------------+--------------------+-------------------+----+
                | RecordCoercions  | RECORD_COERCIONS   | False             | 0  |
                +------------------+--------------------+-------------------+----+
                | DriverSetup      | driver_setup       | "" (empty string) | "" |
                +------------------+--------------------+-------------------+----+

                Note:
                One or more of the referenced properties are not in the Python API for this driver.


        Returns:
            vi (int): Returns a ViSession handle that you use to identify the instrument in
                all subsequent instrument driver method calls.

        '''
        option_string = _converters.convert_init_with_options_dictionary(option_string)
        vi = self._interpreter.init_with_options(resource_name, id_query, reset_device, option_string)
        return vi

    @ivi_synchronized
    def _initiate(self):
        r'''_initiate

        Initiates an acquisition. After you call this method, the DMM leaves
        the Idle state and enters the Wait-for-Trigger state. If trigger is set
        to Immediate mode, the DMM begins acquiring measurement data. Use
        fetch, fetch_multi_point, or fetch_waveform to
        retrieve the measurement data.
        '''
        self._interpreter.initiate()

    @ivi_synchronized
    def perform_open_cable_comp(self):
        r'''perform_open_cable_comp

        For the NI 4082 and NI 4072 only, performs the open cable compensation
        measurements for the current capacitance/inductance range, and returns
        open cable compensation **Conductance** and **Susceptance** values. You
        can use the return values of this method as inputs to
        ConfigureOpenCableCompValues.

        This method returns an error if the value of the method
        property is not set to Method.CAPACITANCE (1005) or
        Method.INDUCTANCE (1006).

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Returns:
            conductance (float): **conductance** is the measured value of open cable compensation
                **conductance**.

            susceptance (float): **susceptance** is the measured value of open cable compensation
                **susceptance**.

        '''
        conductance, susceptance = self._interpreter.perform_open_cable_comp()
        return conductance, susceptance

    @ivi_synchronized
    def perform_short_cable_comp(self):
        r'''perform_short_cable_comp

        Performs the short cable compensation measurements for the current
        capacitance/inductance range, and returns short cable compensation
        **Resistance** and **Reactance** values. You can use the return values
        of this method as inputs to ConfigureShortCableCompValues.

        This method returns an error if the value of the method
        property is not set to Method.CAPACITANCE (1005) or
        Method.INDUCTANCE (1006).

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Returns:
            resistance (float): **resistance** is the measured value of short cable compensation
                **resistance**.

            reactance (float): **reactance** is the measured value of short cable compensation
                **reactance**.

        '''
        resistance, reactance = self._interpreter.perform_short_cable_comp()
        return resistance, reactance

    @ivi_synchronized
    def read(self, maximum_time=hightime.timedelta(milliseconds=-1)):
        r'''read

        Acquires a single measurement and returns the measured value in base units.

        Args:
            maximum_time (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            reading (float): The measured value returned from the DMM.

        '''
        maximum_time = _converters.convert_timedelta_to_milliseconds_int32(maximum_time)
        reading = self._interpreter.read(maximum_time)
        return reading

    @ivi_synchronized
    def read_multi_point(self, array_size, maximum_time=hightime.timedelta(milliseconds=-1)):
        r'''read_multi_point

        Acquires multiple measurements and returns an array of measured values.
        The number of measurements the DMM makes is determined by the values you
        specify for the **Trigger_Count** and **Sample_Count** parameters in
        configure_multi_point.

        Args:
            array_size (int): Specifies the number of measurements to acquire. The maximum number of
                measurements for a finite acquisition is the (**Trigger Count** x
                **Sample Count**) parameters in configure_multi_point.

                For continuous acquisitions, up to 100,000 points can be returned at
                once. The number of measurements can be a subset. The valid range is any
                positive ViInt32. The default value is 1.

            maximum_time (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            reading_array (array.array("d")): An array of measurement values.

                Note:
                The size of the **Reading_Array** must be at least the size that you
                specify for the **Array_Size** parameter.

        '''
        maximum_time = _converters.convert_timedelta_to_milliseconds_int32(maximum_time)
        reading_array = self._interpreter.read_multi_point(maximum_time, array_size)
        return reading_array

    @ivi_synchronized
    def read_status(self):
        r'''read_status

        Returns measurement backlog and acquisition status. Use this method to
        determine how many measurements are available before calling
        fetch, fetch_multi_point, or fetch_waveform.

        Note: The NI 4050 is not supported.

        Returns:
            acquisition_backlog (int): The number of measurements available to be read. If the backlog
                continues to increase, data is eventually overwritten, resulting in an
                error.

                Note:
                On the NI 4060, the **Backlog** does not increase when autoranging. On
                the NI 4065, the **Backlog** does not increase when Range is set to AUTO
                RANGE ON (-1), or before the first point is fetched when Range is set to
                AUTO RANGE ONCE (-3). These behaviors are due to the autorange model of
                the devices.

            acquisition_status (enums.AcquisitionStatus): Indicates status of the acquisition. The following table shows the
                acquisition states:

                +---+----------------------------+
                | 0 | Running                    |
                +---+----------------------------+
                | 1 | Finished with backlog      |
                +---+----------------------------+
                | 2 | Finished with no backlog   |
                +---+----------------------------+
                | 3 | Paused                     |
                +---+----------------------------+
                | 4 | No acquisition in progress |
                +---+----------------------------+

        '''
        acquisition_backlog, acquisition_status = self._interpreter.read_status()
        return acquisition_backlog, acquisition_status

    @ivi_synchronized
    def read_waveform(self, array_size, maximum_time=hightime.timedelta(milliseconds=-1)):
        r'''read_waveform

        For the NI 4080/4081/4082 and the NI 4070/4071/4072, acquires a waveform
        and returns data as an array of values or as a waveform data type. The
        number of elements in the **Waveform_Array** is determined by the
        values you specify for the **Waveform_Points** parameter in
        configure_waveform_acquisition.

        Args:
            array_size (int): Specifies the number of waveform points to return. You specify the total
                number of points that the DMM acquires in the **Waveform Points**
                parameter of configure_waveform_acquisition. The default value is
                1.

            maximum_time (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            waveform_array (array.array("d")): An array of measurement values.

                Note:
                The size of the **Waveform_Array** must be at least the size that you
                specify for the **Array_Size** parameter.

        '''
        maximum_time = _converters.convert_timedelta_to_milliseconds_int32(maximum_time)
        waveform_array = self._interpreter.read_waveform(maximum_time, array_size)
        return waveform_array

    @ivi_synchronized
    def reset_with_defaults(self):
        r'''reset_with_defaults

        Resets the instrument to a known state and sends initialization commands
        to the DMM. The initialization commands set the DMM settings to the
        state necessary for the operation of NI-DMM. All user-defined default
        values associated with a logical name are applied after setting the DMM.
        '''
        self._interpreter.reset_with_defaults()

    @ivi_synchronized
    def self_cal(self):
        r'''self_cal

        For the NI 4080/4081/4082 and the NI 4070/4071/4072, executes the
        self-calibration routine to maintain measurement accuracy.

        Note:
        This method calls reset, and any configurations previous to
        the call will be lost. All properties will be set to their default
        values after the call returns.
        '''
        self._interpreter.self_cal()

    @ivi_synchronized
    def send_software_trigger(self):
        r'''send_software_trigger

        Sends a command to trigger the DMM. Call this method if you have
        configured either the trigger_source or
        sample_trigger properties. If the
        trigger_source and/or sample_trigger
        properties are set to NIDMM_VAL_EXTERNAL or NIDMM_VAL_TTL\ *n*, you
        can use this method to override the trigger source that you configured
        and trigger the device. The NI 4050 and NI 4060 are not supported.

        Note:
        One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
        '''
        self._interpreter.send_software_trigger()

    def _close(self):
        r'''_close

        Closes the specified session and deallocates resources that it reserved.
        '''
        self._interpreter.close()

    @ivi_synchronized
    def self_test(self):
        '''self_test

        Performs a self-test on the DMM to ensure that the DMM is functioning
        properly. Self-test does not calibrate the DMM. Zero
        indicates success.

        On the NI 4080/4082 and NI 4070/4072, the error code 1013 indicates that
        you should check the fuse and replace it, if necessary.

        Raises `SelfTestError` on self test failure. Properties on exception object:

        - code - failure code from driver
        - message - status message from driver

        Note: Self-test does not check the fuse on the NI 4065, NI 4071, and NI 4081. Hence, even if the fuse is blown on the device, self-test does not return error code 1013.

        Note: This method calls reset, and any configurations previous to the call will be lost. All properties will be set to their default values after the call returns.
        '''
        code, msg = self._self_test()
        if code:
            raise errors.SelfTestError(code, msg)
        return None

    @ivi_synchronized
    def reset(self):
        r'''reset

        Resets the instrument to a known state and sends initialization commands
        to the instrument. The initialization commands set instrument settings
        to the state necessary for the operation of the instrument driver.
        '''
        self._interpreter.reset()

    @ivi_synchronized
    def _self_test(self):
        r'''_self_test

        Performs a self-test on the DMM to ensure that the DMM is functioning
        properly. Self-test does not calibrate the DMM.

        Note:
        This method calls reset, and any configurations previous to
        the call will be lost. All properties will be set to their default
        values after the call returns.

        Returns:
            self_test_result (int): Contains the value returned from the instrument self-test. Zero
                indicates success.

                On the NI 4080/4082 and NI 4070/4072, the error code 1013 indicates that
                you should check the fuse and replace it, if necessary.

                Note:
                Self-test does not check the fuse on the NI 4065, NI 4071, and
                NI 4081. Hence, even if the fuse is blown on the device, self-test does
                not return error code 1013.

            self_test_message (str): This parameter contains the string returned from the instrument
                self-test. The array must contain at least 256 elements.

                For the NI 4050 and NI 4060, the error codes returned for self-test
                failures include the following:

                -  NIDMM_ERROR_AC_TEST_FAILURE
                -  NIDMM_ERROR_DC_TEST_FAILURE
                -  NIDMM_ERROR_RESISTANCE_TEST_FAILURE

                These error codes indicate that the DMM should be repaired.

                For the NI 4080/4081/4082 and the NI 4070/4071/4072, the error code
                returned for a self-test failure is NIDMM_ERROR_SELF_TEST_FAILURE.
                This error code indicates that the DMM should be repaired.

        '''
        self_test_result, self_test_message = self._interpreter.self_test()
        return self_test_result, self_test_message
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidmm/nidmm/unit_tests/_matchers.py sha256=b2b548f92273e42d3146eb9b31f0c402d57a2b05f18e2a31318e99f9d0c4d700 bytes=12198 -->
## FILE: generated/nidmm/nidmm/unit_tests/_matchers.py

- repository: `ni/nimi-python`
- source_path: `generated/nidmm/nidmm/unit_tests/_matchers.py`
- sha256: `b2b548f92273e42d3146eb9b31f0c402d57a2b05f18e2a31318e99f9d0c4d700`
- bytes: 12198

````python
# -*- coding: utf-8 -*-
# This file was generated
'''Matcher classes used by unit tests in order to set mock expectations.
These work well with our visatype definitions.
'''

import ctypes
import nidmm._visatype as _visatype
import pprint

pp = pprint.PrettyPrinter(indent=4)


# Base classes


class _ScalarMatcher(object):
    def __init__(self, expected_type, expected_value):
        self.expected_type = expected_type
        self.expected_value = expected_value

    def __eq__(self, other):
        if not isinstance(other, self.expected_type):
            print("{}: Unexpected type. Expected: {}. Received: {}".format(self.__class__.__name__, self.expected_type, type(other)))
            return False
        if other.value != self.expected_value:
            print("{}: Unexpected value. Expected: {}. Received: {}".format(self.__class__.__name__, self.expected_value, other.value))
            return False
        return True

    def __repr__(self):
        return '{}({}, {})'.format(self.__class__.__name__, pp.pformat(self.expected_type), pp.pformat(self.expected_value))


class _PointerMatcher(object):
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __eq__(self, other):
        if not isinstance(other, ctypes.POINTER(self.expected_type)):
            print("Unexpected type. Expected: {}. Received: {}".format(ctypes.POINTER(self.expected_type), type(other)))
            return False
        return True

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, pp.pformat(self.expected_type))


class _BufferMatcher(object):
    def __init__(self, expected_element_type, expected_size_or_value):
        if isinstance(expected_size_or_value, int):
            # Were given the size of the buffer
            self.expected_value = None
            self.expected_size = expected_size_or_value
        else:
            # Were given a list or something that behaves like a list
            self.expected_value = expected_size_or_value
            self.expected_size = len(expected_size_or_value)
        self.expected_type = expected_element_type * self.expected_size
        # Store params for __repr__
        self._expected_element_type = expected_element_type
        self._expected_size_or_value = expected_size_or_value

    def __eq__(self, other):
        if not isinstance(other, self.expected_type):
            # We try to "dereference" this in case it is a pointer and then do the check again. Only then saying they don't match
            try:
                other = other.contents
            except AttributeError:
                pass

            # Because of object lifetimes, we may need to mock the other instance and provide lists instead of the actual array
            if not isinstance(other, self.expected_type) and not isinstance(other, list):
                print("Unexpected type. Expected: {} or {}. Received: {}".format(self.expected_type, list, type(other)))
                return False
        if self.expected_size != len(other):
            print("Unexpected length. Expected: {}. Received: {}".format(self.expected_size, len(other)))
            return False
        if self.expected_value is not None:
            # Can't compare the objects directly because they're different types (one is list, another is ctypes array).
            # Go element by element, which allows for reporting the first index where different values were found.
            for i in range(0, len(self.expected_value)):
                if self.expected_value[i] != other[i]:
                    print("Unexpected value at index {}. Expected: {}. Received: {}".format(i, self.expected_value[i], other[i]))
                    return False
        return True

    def __repr__(self):
        return '{}({}, {})'.format(self.__class__.__name__, pp.pformat(self._expected_element_type), pp.pformat(self._expected_size_or_value))

    def __str__(self):
        ret_str = self.__repr__() + '\n'
        ret_str += '    expected_type  = ' + str(self.expected_type) + '\n'
        ret_str += '    expected_value = ' + str(self.expected_value) + '\n'
        ret_str += '    expected_size  = ' + str(self.expected_size) + '\n'
        return ret_str


# Strings


class ViStringMatcher(object):
    def __init__(self, expected_string_value):
        self.expected_string_value = expected_string_value

    def __eq__(self, other):
        if not isinstance(other, ctypes.Array):
            # We try to "dereference" this in case it is a pointer and then do the check again. Only then saying they don't match
            try:
                other = other.contents
            except AttributeError:
                pass

            if not isinstance(other, ctypes.Array):
                print("Unexpected type. Expected: {}. Received: {}".format(self.expected_type, type(other)))
                return False
        if len(other) < len(self.expected_string_value) + 1:  # +1 for NULL terminating character
            print("Unexpected length in C string. Expected at least: {}. Received {}".format(len(other), len(self.expected_string_value) + 1))
            return False
        if not isinstance(other[0], bytes):
            print("Unexpected type. Not a string. Received: {}".format(type(other[0])))
            return False
        if other.value.decode("ascii") != self.expected_string_value:
            print("Unexpected value. Expected {}. Received: {}".format(self.expected_string_value, other.value.decode))
            return False
        return True

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, pp.pformat(self.expected_string_value))


# Custom Type


def _compare_ctype_structs(expected, actual):
    # From https://stackoverflow.com/questions/20986330/print-all-fields-of-ctypes-structure-with-introspection
    for field in expected._fields_:
        field_name = field[0]
        expected_val = getattr(expected, field_name)
        actual_val = getattr(actual, field_name)
        if expected_val != actual_val:
            print("Unexpected value field {}. Expected: {}. Received: {}".format(field_name, expected_val, actual_val))
            return False
    return True


class CustomTypeMatcher(object):
    def __init__(self, expected_type, expected_value):
        self.expected_type = expected_type
        self.expected_value = expected_value

    def __eq__(self, actual):
        if not isinstance(actual, self.expected_type):
            print("Unexpected type. Expected: {}. Received: {}".format(self.expected_type, type(actual)))
            return False
        return _compare_ctype_structs(self.expected_value, actual)

    def __repr__(self):
        return '{}({}, {})'.format(self.__class__.__name__, pp.pformat(self.expected_type), pp.pformat(self.expected_value))


class CustomTypeBufferMatcher(object):
    def __init__(self, expected_element_type, expected_value):
        self.expected_value = expected_value
        self.expected_size = len(expected_value)
        self.expected_type = expected_element_type * self.expected_size
        self.expected_element_type = expected_element_type

    def __eq__(self, actual):
        if not isinstance(actual, self.expected_type):
            print("Unexpected array type. Expected: {}. Received: {}".format(self.expected_type, type(actual)))
            return False
        if self.expected_size != len(actual):
            print("Unexpected length. Expected: {}. Received: {}".format(self.expected_size, len(actual)))
            return False
        if self.expected_value is not None:
            # Can't compare the objects directly because they're different types (one is list, another is ctypes array).
            # Go element by element, which allows for reporting the first index where different values were found.
            for a, e in zip(actual, self.expected_value):
                if not isinstance(a, self.expected_element_type):
                    print("Unexpected type. Expected: {}. Received: {}".format(self.expected_element_type, type(a)))
                    return False
                if not _compare_ctype_structs(e, a):
                    return False
        return True

    def __repr__(self):
        expected_val_repr = '[' + ', '.join([x.__repr__() for x in self.expected_value]) + ']'
        return '{}({}, {})'.format(self.__class__.__name__, pp.pformat(self.expected_element_type), expected_val_repr)

    def __str__(self):
        ret_str = self.__repr__() + '\n'
        ret_str += '    expected_type = ' + str(self.expected_type) + '\n'
        ret_str += '    expected_size = ' + str(self.expected_size) + '\n'
        return ret_str


# Scalars


class ViBooleanMatcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViBoolean, 1 if expected_value is True else 0)


class ViSessionMatcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViSession, expected_value)


class ViInt16Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViInt16, expected_value)


class ViInt32Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViInt32, expected_value)


class ViUInt32Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViUInt32, expected_value)


class ViAttrMatcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViAttr, expected_value)


class ViInt64Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViInt64, expected_value)


class ViReal64Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViReal64, expected_value)


# Pointers


class ViBooleanPointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViBoolean)


class ViSessionPointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViSession)


class ViInt16PointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViInt16)


class ViInt32PointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViInt32)


class ViInt64PointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViInt64)


class ViReal64PointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViReal64)


# Buffers


class ViBooleanBufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViBoolean, expected_size_or_value)


class ViCharBufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViChar, expected_size_or_value)


class ViInt8BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViInt8, expected_size_or_value)


class ViInt16BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViInt16, expected_size_or_value)


class ViInt32BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViInt32, expected_size_or_value)


class ViInt64BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViInt64, expected_size_or_value)


class ViReal64BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViReal64, expected_size_or_value)


class ViSessionBufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViSession, expected_size_or_value)
````
