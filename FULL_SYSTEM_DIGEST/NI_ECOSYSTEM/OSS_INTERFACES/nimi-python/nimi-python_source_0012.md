# NI OSS SOURCE SNAPSHOT: nimi-python

<!--NI_OSS_SNAPSHOT repo=ni/nimi-python commit=6511f8025f072f7f7021953888b916bbdc31aa2a -->

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nirfsg/nirfsg/session.py sha256=07ad970db81a85fa8bcaf0802164c5a3d07f8583bfd43a53c9b8b540f9be7103 bytes=525910 -->
## FILE: generated/nirfsg/nirfsg/session.py

- repository: `ni/nimi-python`
- source_path: `generated/nirfsg/nirfsg/session.py`
- sha256: `07ad970db81a85fa8bcaf0802164c5a3d07f8583bfd43a53c9b8b540f9be7103`
- bytes: 525910

````python
# -*- coding: utf-8 -*-
# This file was generated
import array  # noqa: F401
# Used by @ivi_synchronized
from functools import wraps

import nirfsg._attributes as _attributes
import nirfsg._converters as _converters
import nirfsg._library_interpreter as _library_interpreter
import nirfsg.enums as enums
import nirfsg.errors as errors

import hightime
import nitclk

# Used for __repr__
import pprint
pp = pprint.PrettyPrinter(indent=4)


class _Generation(object):
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
    '''Base class for all NI-RFSG sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    absolute_delay = _attributes.AttributeViReal64TimeDeltaSeconds(1150225)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the sub-Sample Clock delay, in seconds, to apply to the I/Q waveform. Use this property to reduce the trigger jitter when synchronizing multiple devices with NI-TClk. This property can also help maintain synchronization repeatability by writing the absolute delay value of a previous measurement to the current session.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Units:** Seconds

    **Valid Values:** Plus or minus half of one Sample Clock period

    **Supported Devices:** PXIe-5820/5840/5841/5842

    Note: - The resolution of this property is a method of the I/Q sample period at 15E(-6) times that sample period.

     - If this property is set, NI-TClk cannot perform any sub-Sample Clock adjustment.
    '''
    ae_temperature = _attributes.AttributeViReal64(1150182)
    '''Type: float

    Returns the amplitude extender module temperature in degrees Celsius.

    **Units**: degrees Celsius (°C)

    **Supported Devices:** PXIe-5654 with PXIe-5696
    '''
    alc_control = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AutomaticLevelControl, 1150195)
    '''Type: enums.AutomaticLevelControl

    Enables or disables the automatic leveling control (ALC).

    PXIe-5654 with PXIe-5696: If this property is enabled, the ALC is closed (closed-loop mode) and allows for better amplitude accuracy and wider amplitude dynamic range. If this property is disabled, the ALC is open (open-loop mode), which is ideal when using modulation. Disabling the alc_control property also allows for NI-RFSG to perform an automatic power search.

    PXIe-5654: AutomaticLevelControl.DISABLE is the only supported value for this device. The PXIe-5654 does not support the ALC when used as a stand-alone device.

    **Default Value:**

    PXIe-5654: AutomaticLevelControl.DISABLE

    PXIe-5654 with PXIe-5696: AutomaticLevelControl.ENABLE

    **Supported Devices:** PXIe-5654/5654 with PXIe-5696

    **Related Topics**

    `Power Level Adjustment <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_power_level_adjustment.html>`_

    `ALC Closed Loop Versus Open Loop <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_alc_closed_loop_vs_open_loop.html>`_

    `Power Search <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_power_search.html>`_

    **Defined Values**:

    +-------------------------------+---------+------------------+
    | Name                          | Value   | Description      |
    +===============================+=========+==================+
    | AutomaticLevelControl.DISABLE | 0 (0x0) | Disables ALC.    |
    +-------------------------------+---------+------------------+
    | AutomaticLevelControl.ENABLE  | 1 (0x1) | Enables the ALC. |
    +-------------------------------+---------+------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    allow_out_of_specification_user_settings = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AllowOutOfSpecificationUserSettings, 1150014)
    '''Type: enums.AllowOutOfSpecificationUserSettings

    Enables or disables warnings or errors when you set the frequency, power, and bandwidth values beyond the limits of the NI-RFSG device specifications. When you enable the allow_out_of_specification_user_settings property, the driver does not report out-of-specification warnings or errors.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** AllowOutOfSpecificationUserSettings.DISABLE

    **Supported Devices:** PXI/PXIe-5650/5651/5652, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +---------------------------------------------+---------+----------------------------------------------+
    | Name                                        | Value   | Description                                  |
    +=============================================+=========+==============================================+
    | AllowOutOfSpecificationUserSettings.DISABLE | 0 (0x0) | Disables out-of-specification user settings. |
    +---------------------------------------------+---------+----------------------------------------------+
    | AllowOutOfSpecificationUserSettings.ENABLE  | 1 (0x1) | Enables out-of-specification user settings.  |
    +---------------------------------------------+---------+----------------------------------------------+

    Note: Accuracy cannot be guaranteed outside of device specifications, and results may vary by module.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    amplitude_settling = _attributes.AttributeViReal64(1150137)
    '''Type: float

    Configures the amplitude settling accuracy in decibels. NI-RFSG waits until the RF power settles within the specified accuracy level after calling the _initiate method or wait_until_settled method or prior to advancing to next step if using RF list mode.

    Any specified amplitude settling value that is above the acceptable minimum value is coerced down to the closest valid value.

    PXI/PXIe-5650/5651/5652: This property is for NI internal use only.

    **Units**: dB

    **Default Value:**

    PXIe-5654: 4

    PXIe-5654 with PXIe-5696 (ALC disabled): 4

    PXIe-5654 with PXIe-5696 (ALC enabled): 0.2

    PXIe-5820/5830/5831/5832/5840/5841/5842/5860: 0.5

    **Valid Values:**

    PXIe-5654: 1.5, 2, 4

    PXIe-5654 with PXIe-5696 (ALC disabled): 1.5, 2, 4

    PXIe-5654 with PXIe-5696 (ALC enabled): 0.2, 0.5

    PXIe-5820/5830/5831/5832/5840/5841/5842/5860: 0.01 to 1

    **Supported Devices:** PXIe-5654/5654 with PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Amplitude Settling Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_amplitude_settling_times.html>`_
    '''
    amp_path = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AmpPath, 1150185)
    '''Type: enums.AmpPath

    Specifies the amplification path to use. The low harmonic path provides greater second and third harmonic spurious response, and the high power path provides higher output power.

    NI-RFSG automatically sets the value of this property based on power and frequency settings. Setting this property overrides the value chosen by NI-RFSG.

    **Default Value:** AmpPath.LOW_HARMONIC

    **Supported Devices:** PXIe-5654 with PXIe-5696

    **Related Topics**

    `Low Harmonic Path Versus High Power Path <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/low_harmonic_path_vs_high_power_path.html>`_

    **Defined Values**:

    +----------------------+----------------+-----------------------------------------------------------+
    | Name                 | Value          | Description                                               |
    +======================+================+===========================================================+
    | AmpPath.HIGH_POWER   | 16000 (0x3e80) | Sets the amplification path to use the high power path.   |
    +----------------------+----------------+-----------------------------------------------------------+
    | AmpPath.LOW_HARMONIC | 16001 (0x3e81) | Sets the amplification path to use the low harmonic path. |
    +----------------------+----------------+-----------------------------------------------------------+

    Note: Resetting this property reverts back to the default unset behavior.
    '''
    analog_modulation_am_sensitivity = _attributes.AttributeViReal64(1150167)
    '''Type: float

    Specifies an uncalibrated digital-to-analog converter (DAC) value that scales the input signal before the signal modulates the carrier. A value of 0 completely attenuates the signal, and a value of 100 passes the full-scale signal to the modulator.

    When using the PXIe-5654 with PXIe-5696, NI-RFSG may coerce AM sensitivity. Coercing the AM sensitivity prevents overpower conditions at the PXIe-5696 input. Read this property to determine the coerced value.

    **Default Value:** 100

    **Valid Values:** 0 to 100

    **Supported Devices:** PXIe-5654/5654 with PXIe-5696

    **Related Topics**

    `Amplitude Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_amplitude_modulation.html>`_
    '''
    analog_modulation_fm_band = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AnalogModulationFmBand, 1150191)
    '''Type: enums.AnalogModulationFmBand

    Specifies the analog modulation frequency modulation (FM) band to use. Wideband FM allows for modulating signals higher than 100kHz. Narrowband FM allows for modulating lower frequency signals.

    **Default Value:** AnalogModulationFmBand.WIDEBAND

    **Supported Devices:** PXIe-5654/5654 with PXIe-5696

    **Related Topics**

    `Frequency Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_frequency_modulation.html>`_

    **Defined Values**:

    +-----------------------------------+----------------+--------------------------------------------+
    | Name                              | Value          | Description                                |
    +===================================+================+============================================+
    | AnalogModulationFmBand.NARROWBAND | 17000 (0x4268) | Specifies narrowband frequency modulation. |
    +-----------------------------------+----------------+--------------------------------------------+
    | AnalogModulationFmBand.WIDEBAND   | 17001 (0x4269) | Specifies wideband frequency modulation.   |
    +-----------------------------------+----------------+--------------------------------------------+
    '''
    analog_modulation_fm_narrowband_integrator = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AnalogModulationFmNarrowbandIntegrator, 1150165)
    '''Type: enums.AnalogModulationFmNarrowbandIntegrator

    Specifies the narrowband frequency modulation (FM) range to apply by sending the signal through an integrator.

    This property is valid only when you set the analog_modulation_type property to AnalogModulationType.FM and the analog_modulation_fm_band property to AnalogModulationFmBand.NARROWBAND.

    **Default Value:** AnalogModulationFmNarrowbandIntegrator.RANGE_100_HERTZ_TO_1_KILOHERTZ

    **Supported Devices:** PXIe-5654/5654 with PXIe-5696

    **Related Topics**

    `Frequency Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_frequency_modulation.html>`_

    **Defined Values**:

    +----------------------------------------------------------------------------+----------------+---------------------------------------------+
    | Name                                                                       | Value          | Description                                 |
    +============================================================================+================+=============================================+
    | AnalogModulationFmNarrowbandIntegrator.RANGE_100_HERTZ_TO_1_KILOHERTZ      | 18000 (0x4650) | Specifies a range from 100Â Hz to 1Â kHz.   |
    +----------------------------------------------------------------------------+----------------+---------------------------------------------+
    | AnalogModulationFmNarrowbandIntegrator.RANGE_10_KILOHERTZ_TO_100_KILOHERTZ | 18002 (0x4652) | Specifies a range from 10Â kHz to 100Â kHz. |
    +----------------------------------------------------------------------------+----------------+---------------------------------------------+
    | AnalogModulationFmNarrowbandIntegrator.RANGE_1_KILOHERTZ_TO_10_KILOHERTZ   | 18001 (0x4651) | Specifies a range from 1Â kHz to 10Â kHz.   |
    +----------------------------------------------------------------------------+----------------+---------------------------------------------+
    '''
    analog_modulation_fm_sensitivity = _attributes.AttributeViReal64(1150166)
    '''Type: float

    Specifies an uncalibrated digital-to-analog converter (DAC) value that scales the input signal before the signal modulates the carrier. A value of 0 completely attenuates the signal, and a value of 100 passes the full-scale signal to the modulator.

    **Default Value:** 100

    **Valid Values:** 0 to 100

    **Supported Devices:** PXIe-5654/5654 with PXIe-5696

    **Related Topics**

    `Frequency Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_frequency_modulation.html>`_
    '''
    analog_modulation_pm_deviation = _attributes.AttributeViReal64(1150062)
    '''Type: float

    Specifies the `deviation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/glossary.html>`_ to use in phase modulation, in degrees.

    **Units**: degrees (°)

    **Default Value:** 90°

    **Supported Devices:** PXI/PXIe-5650/5651/5652, PXIe-5653

    **Related Topics**

    `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_
    '''
    analog_modulation_pm_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AnalogModulationPmMode, 1150192)
    '''Type: enums.AnalogModulationPmMode

    Specifies the phase modulation (PM) mode to use.

    **Default Value:** AnalogModulationPmMode.LOW_PHASE_NOISE

    **Supported Devices:** PXIe-5654/5654 with PXIe-5696

    **Related Topics**

    `Phase Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_phase_modulation.html>`_

    **Defined Values**:

    +----------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
    | Name                                   | Value          | Description                                                                                   |
    +========================================+================+===============================================================================================+
    | AnalogModulationPmMode.HIGH_DEVIATION  | 19000 (0x4a38) | Specifies high deviation. High deviation comes at the expense of a higher phase noise.        |
    +----------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
    | AnalogModulationPmMode.LOW_PHASE_NOISE | 19001 (0x4a39) | Specifies low phase noise. Low phase noise comes at the expense of a lower maximum deviation. |
    +----------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
    '''
    analog_modulation_pm_sensitivity = _attributes.AttributeViReal64(1150168)
    '''Type: float

    Specifies an uncalibrated digital-to-analog converter (DAC) value that scales the input signal before the signal modulates the carrier. A value of 0 completely attenuates the signal, and a value of 100 passes the full-scale signal to the modulator.

    **Default Value:** 100

    **Valid Values:** 0 to 100

    **Supported Devices:** PXIe-5654/5654 with PXIe-5696

    **Related Topics**

    `Phase Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_phase_modulation.html>`_
    '''
    analog_modulation_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AnalogModulationType, 1150032)
    '''Type: enums.AnalogModulationType

    Specifies the analog modulation format to use.

    **Default Value:** AnalogModulationType.NONE

    **Supported Devices:** PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696

    **Related Topics**

    `Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation.html>`_

    `PXI/PXIe-5650/5651/5652 Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_

    `PXIe-5654/5654 with PXIe-5696 Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_modulation_modes.html>`_

    **Defined Values**:

    +---------------------------+--------------+--------------------------------------------------+
    | Name                      | Value        | Description                                      |
    +===========================+==============+==================================================+
    | AnalogModulationType.AM   | 2002 (0x7d2) | Specifies that the analog modulation type is AM. |
    +---------------------------+--------------+--------------------------------------------------+
    | AnalogModulationType.FM   | 2000 (0x7d0) | Specifies that the analog modulation type is FM. |
    +---------------------------+--------------+--------------------------------------------------+
    | AnalogModulationType.NONE | 0 (0x0)      | Disables analog modulation.                      |
    +---------------------------+--------------+--------------------------------------------------+
    | AnalogModulationType.PM   | 2001 (0x7d1) | Specifies that the analog modulation type is PM. |
    +---------------------------+--------------+--------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    arb_carrier_frequency = _attributes.AttributeViReal64(1150015)
    '''Type: float

    **Units**: hertz (Hz)

    **Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_—Refer to this topic for more information about using this property to associate a carrier frequency with a waveform.
    Indicates the carrier frequency generated by the arbitrary waveform generator (AWG) module. The specified carrier frequency is related to the RF output as shown in the following equations:

    +-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Device                                                                        | Equations                                                                                                                                                                                                                                                                                                     |
    +===============================================================================+===============================================================================================================================================================================================================================================================================================================+
    | PXI-5610, PXI-5670/5671, PXIe-5672                                            | RF Frequency (MHz) = *Upconverter Center Frequency* + *Arb Carrier Frequency* – 25 MHz                                                                                                                                                                                                                        |
    +-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860 | RF Frequency (MHz) = *Upconverter Center Frequency* + *Arb Carrier Frequency*.Note that - the upconverter_center_frequency property and the arb_carrier_frequency property cannot be set at the same time. The only time the carrier frequency is nonzero on these devices is when in-band retuning is used.  |
    +-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    Note: - Use this property to associate a carrier frequency with a waveform.

     - This property is read-only on the PXI-5670/5671 and PXIe-5672.
    '''
    arb_digital_gain = _attributes.AttributeViReal64(1150204)
    '''Type: float

    Specifies the digital gain, in decibels. The digital gain is applied to the waveform data after filtering. Use this property to adjust the output power of the device while keeping the analog path fixed. This may cause clipping, overflows, or quantization noise if used improperly.

    To set this property, the NI-RFSG device must be in the Configuration or Generation state.

    **Default Value:** 0 dB

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    arb_max_number_waveforms = _attributes.AttributeViInt32(1250454)
    '''Type: int

    Returns the maximum number of waveforms the device can hold in memory.

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **High-Level Methods**:

    - query_arb_waveform_capabilities
    '''
    arb_onboard_sample_clock_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ArbOnboardSampleClockMode, 1150029)
    '''Type: enums.ArbOnboardSampleClockMode

    Specifies the Sample Clock mode on the device. To set this property, the device must be in the Configuration state.

    PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: ArbOnboardSampleClockMode.DIVIDE_DOWN is the only supported value for this device.

    **Default Values:**

    PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: ArbOnboardSampleClockMode.DIVIDE_DOWN

    PXIe-5673/5673E: ArbOnboardSampleClockMode.HIGH_RESOLUTION

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Clocking Modes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/clocking.html>`_

    **Valid Values**:

    +-------------------------------------------+--------------------------------------------------------------+
    | Name                                      | Description                                                  |
    +===========================================+==============================================================+
    | ArbOnboardSampleClockMode.HIGH_RESOLUTION | Sample rates are generated by a high-resolution clock.       |
    +-------------------------------------------+--------------------------------------------------------------+
    | ArbOnboardSampleClockMode.DIVIDE_DOWN     | Sample rates are generated by dividing the source frequency. |
    +-------------------------------------------+--------------------------------------------------------------+

    Note: Using the high resolution clock may result in increased phase noise.
    '''
    arb_pre_filter_gain = _attributes.AttributeViReal64(1150025)
    '''Type: float

    Specifies the AWG prefilter gain. The prefilter gain is applied to the waveform data before any other signal processing. Reduce this value to prevent overflow in the AWG interpolation filters. Other gains on the NI-RFSG device are automatically adjusted to compensate for nonunity AWG prefilter gain. The PXI-5671, PXIe-5672 must be in the Configuration state to use this property. However, the PXIe-5644/5645/5646, PXIe-5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842 can be in either the Configuration or the Generation state to use this property. PXIe-5860 can only be in the Configuration state to use this property.

    On the PXI-5671, this property applies only when the iq_rate property is set to a value less than or equal to 8.33MS/s. On the PXIe-5644/5645/5646, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860, this property is always applicable.

    **Units**: dB

    **Default Value:** 0dB

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    arb_sample_clock_rate = _attributes.AttributeViReal64(1150031)
    '''Type: float

    Returns the rate of the Sample Clock on the device.

    **Units**: hertz (Hz)

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    arb_sample_clock_source = _attributes.AttributeEnum(_attributes.AttributeViString, enums.ArbSampleClockSource, 1150030)
    '''Type: enums.ArbSampleClockSource

    Specifies the Sample Clock source for the device. To set this property, the NI-RFSG device must be in the Configuration state.

    PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: OnboardClock is the only supported value for this device.

    **Default Value:** OnboardClock

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_

    **Possible Values**:

    +----------------+---------------------------------------------------------------+
    | Possible Value | Description                                                   |
    +================+===============================================================+
    | "ClkIn"        | Uses the external clock as the Sample Clock source.           |
    +----------------+---------------------------------------------------------------+
    | "OnboardClock" | Uses the AWG module onboard clock as the Sample Clock source. |
    +----------------+---------------------------------------------------------------+
    '''
    arb_selected_waveform = _attributes.AttributeViString(1250451)
    '''Type: str

    Specifies the waveform in onboard memory to generate upon calling the Init method when the generation_mode property is set to GenerationMode.ARB_WAVEFORM. The arb_selected_waveform property is ignored when the generation_mode property is set to GenerationMode.SCRIPT or GenerationMode.CW. To set the arb_selected_waveform property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** "" (empty string)

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_

    **High-Level Methods**:

    - select_arb_waveform
    '''
    arb_temperature = _attributes.AttributeViReal64(1150068)
    '''Type: float

    Returns the AWG module temperature in degrees Celsius.

    PXIe-5820/5840/5841/5842: If you query this property during RF list mode, list steps may take longer to complete during list execution.

    **Units**: degrees Celsius (°C)

    **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5840/5841/5842/5860
    '''
    arb_waveform_quantum = _attributes.AttributeViInt32(1250455)
    '''Type: int

    Returns the waveform quantum for the device. The number of samples in a waveform must be an integer multiple of the waveform quantum. The other restrictions on the length of the waveform are the arb_waveform_size_min and arb_waveform_size_max arbitrary waveform sizes.

    PXI-5671, PXIe-5672: The value of this property depends on the I/Q rate. Set the iq_rate property before reading this property.

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **High-Level Methods**:

    - query_arb_waveform_capabilities
    '''
    arb_waveform_repeat_count = _attributes.AttributeViInt32(1150158)
    '''Type: int

    Specifies the repeat count of a waveform when you set the arb_waveform_repeat_count_is_finite property to True. This property is valid only when you set the generation_mode property to GenerationMode.ARB_WAVEFORM. To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** 1

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    arb_waveform_repeat_count_is_finite = _attributes.AttributeViBoolean(1150157)
    '''Type: bool

    Specifies the repetition mode of a waveform when you set the generation_mode property to GenerationMode.ARB_WAVEFORM. If you set this property to True, the number of repetitions is determined by the arb_waveform_repeat_count property. To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** False

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +-------+-------------------------------------------------------------------+
    | Value | Description                                                       |
    +=======+===================================================================+
    | True  | Repeats the waveform a finite number of times.                    |
    +-------+-------------------------------------------------------------------+
    | False | Repeats the waveform continuously until you abort the generation. |
    +-------+-------------------------------------------------------------------+
    '''
    arb_waveform_size_max = _attributes.AttributeViInt32(1250457)
    '''Type: int

    Returns the size of the largest waveform that is allowed.

    To read this property, the NI-RFSG device must be in the Configuration state.

    For the PXI-5671 and PXIe-5672, the value of this property depends on the I/Q rate. Set the iq_rate before reading this property. For the PXIe-5673/5673E, the maximum waveform size is reduced to account for the amount of device memory currently used.

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **High-Level Methods**:

    - query_arb_waveform_capabilities

    Note: Not all onboard memory is available for waveform storage. A portion of onboard memory stores scripts that specify how the waveforms are generated. These scripts typically require less than 1KB of onboard memory.
    '''
    arb_waveform_size_min = _attributes.AttributeViInt32(1250456)
    '''Type: int

    Returns the smallest allowable waveform size. For the PXI-5671 and PXIe-5672, the value of this property depends on the I/Q rate. Set the iq_rate property before reading this property.

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **High-Level Methods**:

    - query_arb_waveform_capabilities
    '''
    arb_waveform_software_scaling_factor = _attributes.AttributeViReal64(1150052)
    '''Type: float

    Specifies how much to scale the data before writing it with the WriteArbWaveform method. The resulting waveform must be smaller than 1.0 in complex magnitude. This property is supported only if you set the power_level_type property to PowerLevelType.PEAK.

    **Default Value:** 1.0

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Spurious Performance <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/spurious_performance.html>`_
    '''
    attenuator_setting = _attributes.AttributeViReal64(1150173)
    '''Type: float

    Specifies the level of attenuation in the attenuator path. Setting this property overrides the value chosen by NI-RFSG. Not all power levels are achievable if you set this property.

    **Units**: dB

    **Valid Values**: 0dB to 110dB in steps of 10

    **Supported Devices:** PXIe-5654 with PXIe-5696

    Note: Resetting this property reverts back to the default unset behavior.
    '''
    automatic_thermal_correction = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AutomaticThermalCorrection, 1150008)
    '''Type: enums.AutomaticThermalCorrection

    Enables or disables automatic thermal correction. When this property is enabled, changes to settings cause NI-RFSG to check whether the device temperature has changed and adjusts the settings as needed. When this property is disabled, you must explicitly call the perform_thermal_correction method to adjust the device for temperature changes.

    **Default Value:** AutomaticThermalCorrection.ENABLE

    **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Temperature Monitoring <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5611_temperature_monitoring.html>`_

    `Settling Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/settling_times.html>`_

    **Defined Values**:

    +------------------------------------+---------+-------------------------------------------+
    | Name                               | Value   | Description                               |
    +====================================+=========+===========================================+
    | AutomaticThermalCorrection.DISABLE | 0 (0x0) | Automatic thermal correction is disabled. |
    +------------------------------------+---------+-------------------------------------------+
    | AutomaticThermalCorrection.ENABLE  | 1 (0x1) | Automatic thermal correction is enabled.  |
    +------------------------------------+---------+-------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    auto_power_search = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AutomaticPowerSearch, 1150196)
    '''Type: enums.AutomaticPowerSearch

    Enables or disables automatic power search. When this property is enabled, a power search performs after the device is initiated, after output power is enabled, or when the frequency or power level changes while the device is generating. When this property is disabled, NI-RFSG does not perform a power search unless you call the perform_power_search method.

    This property is ignored when the alc_control property is enabled.

    PXIe-5654: AutomaticPowerSearch.DISABLE is the only supported value for this device.

    **Default Value:**

    PXIe-5654: AutomaticPowerSearch.DISABLE

    PXIe-5654 with PXIe-5696: AutomaticPowerSearch.ENABLE

    **Supported Devices:** PXIe-5654/5654 with PXIe-5696

    **Related Topics**

    `Power Search <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_power_search.html>`_

    **Defined Values**:

    +------------------------------+---------+----------------------------------+
    | Name                         | Value   | Description                      |
    +==============================+=========+==================================+
    | AutomaticPowerSearch.DISABLE | 0 (0x0) | Disables automatic power search. |
    +------------------------------+---------+----------------------------------+
    | AutomaticPowerSearch.ENABLE  | 1 (0x1) | Enables automatic power search.  |
    +------------------------------+---------+----------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    available_paths = _attributes.AttributeViStringCommaSeparated(1150312)
    '''Type: list of str

    Returns a list of the configurable paths available for use based on your instrument configuration.
    '''
    available_ports = _attributes.AttributeViStringCommaSeparated(1150249)
    '''Type: list of str

    Returns a list of the ports available for use based on your instrument configuration.

    **Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    configuration_settled_event_terminal_name = _attributes.AttributeViString(1150194)
    '''Type: str

    Returns the name of the fully qualified signal name as a string.

    **Supported Devices:** PXIe-5654/5654 with PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842

    **Default Values**:

    PXIe-5654/5654 with PXIe-5696: /*ModuleName*/ConfigurationSettledEvent, where *ModuleName* is the name of your device in MAX.

    PXIe-5830/5831/5832: /*BasebandModule*/ao/0/ConfigurationSettledEvent, where *BasebandModule* is the name of the baseband module of your device in MAX.

    PXIe-5820/5840/5841/5842: /*ModuleName*/ao/0/ConfigurationSettledEvent, where *ModuleName* is the name of your device in MAX.

    **Related Topics**

    `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

    `Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_
    '''
    correction_temperature = _attributes.AttributeViReal64(1150104)
    '''Type: float

    Specifies the temperature, in degrees Celsius, to use for adjusting the device settings to correct for temperature changes. If you set this property, NI-RFSG uses the value you specify and therefore no longer uses the actual device temperature as the correction temperature. If you do not set this property, NI-RFSG checks the current device temperature in the Committed state and automatically sets the value of this property.

    PXIe-5820/5830/5831/5832/5840/5841/5842/5860: This property is read only.

    **Units**: Degrees Celsius

    **Supported Devices**: PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    Note: - Resetting this property reverts back to the default unset behavior.

     - Use this property only when your application requires the same settings to be used every time, regardless of the temperature variation. In these cases, it is best to ensure that the temperature does not vary too much.
    '''
    deembedding_compensation_gain = _attributes.AttributeViReal64(1150289)
    '''Type: float

    Returns the de-embedding gain applied to compensate for the mismatch on the specified port. If de-embedding is enabled, NI-RFSG uses the returned compensation gain to remove the effects of the external network between the instrument and the DUT.

    **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

    Tip:
    This property can be set/get on specific ports within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container ports to specify a subset.

    Example: :py:attr:`my_session.ports[ ... ].deembedding_compensation_gain`

    To set/get on all ports, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.deembedding_compensation_gain`
    '''
    deembedding_selected_table = _attributes.AttributeViString(1150253)
    '''Type: str

    Selects the de-embedding table to apply to the measurements on the specified port.

    To use this property, you must use the channelName parameter of the _set_attribute_vi_string method to specify the name of the port to configure for de-embedding.

    If de-embedding is enabled, NI-RFSG uses the specified table to remove the effects of the external network between the instrument and the DUT.

    Use the create deembedding sparameter table array method to create tables.

    **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

    Tip:
    This property can be set/get on specific ports within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container ports to specify a subset.

    Example: :py:attr:`my_session.ports[ ... ].deembedding_selected_table`

    To set/get on all ports, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.deembedding_selected_table`
    '''
    deembedding_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.DeembeddingType, 1150252)
    '''Type: enums.DeembeddingType

    Specifies the type of de-embedding to apply to measurements on the specified port.

    To use this property, you must use the channelName parameter of the _set_attribute_vi_int32 method to specify the name of the port to configure for de-embedding.

    If you set this property to DeembeddingType.SCALAR or DeembeddingType.VECTOR, NI-RFSG adjusts the instrument settings and the returned data to remove the effects of the external network between the instrument and the DUT.

    **Default Value**: DeembeddingType.SCALAR

    **Valid Values for PXIe-5830/5832/5840/5841/5842/5860** : DeembeddingType.SCALAR or DeembeddingType.NONE

    **Valid Values for PXIe-5831** DeembeddingType.SCALAR, DeembeddingType.VECTOR, or DeembeddingType.NONE. DeembeddingType.VECTOR is only supported for TRX Ports in a Semiconductor Test System (STS).

    **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +------------------------+----------------+------------------------------------------------------------------------+
    | Name                   | Value          | Description                                                            |
    +========================+================+========================================================================+
    | DeembeddingType.NONE   | 25000 (0x61a8) | De-embedding is not applied to the measurement.                        |
    +------------------------+----------------+------------------------------------------------------------------------+
    | DeembeddingType.SCALAR | 25001 (0x61a9) | De-embeds the measurement using only the gain term.                    |
    +------------------------+----------------+------------------------------------------------------------------------+
    | DeembeddingType.VECTOR | 25002 (0x61aa) | De-embeds the measurement using the gain term and the reflection term. |
    +------------------------+----------------+------------------------------------------------------------------------+

    Tip:
    This property can be set/get on specific ports within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container ports to specify a subset.

    Example: :py:attr:`my_session.ports[ ... ].deembedding_type`

    To set/get on all ports, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.deembedding_type`
    '''
    device_instantaneous_bandwidth = _attributes.AttributeViReal64(1150226)
    '''Type: float

    Specifies the bandwidth of the device. The instantaneous bandwidth is the effective real-time bandwidth of the signal path for your configuration.

    The signal_bandwidth centered at the frequency must fit within the device instantaneous bandwidth, which is centered at the upconverter_center_frequency.

    **Units**: Hz

    **Default Value**: N/A

    **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `PXIe-5830 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_

    `PXIe-5831/5832 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_

    `PXIe-5841 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_
    '''
    device_temperature = _attributes.AttributeViReal64(1150017)
    '''Type: float

    Returns the device temperature. If the NI-RFSG session is controlling multiple devices, this property returns the temperature of the primary NI RF device. The NI-RFSG session is opened using the primary RF device name.

    Serial signals between the sensor and the system control unit could modulate the signal being generated, thus causing phase spurs. After the device thoroughly warms up, its temperature varies only slightly (less than 1 degree Celsius) and slowly, and it is not necessary to constantly poll this temperature sensor.

    PXIe-5644/5645/5646, PXIe-5820/5840/5841: If you query this property during RF list mode, list steps may take longer to complete during list execution.

    PXIe-5830/5831/5832: To use this property, you must first set the channelName parameter of the _set_attribute_vi_real64 method to using the appropriate string for your instrument configuration. Setting the _set_attribute_vi_real64 method is not required for the PXIe-3621/3622. Refer to the following table to determine which strings are valid for your configuration.

    **Units**: degrees Celsius (°C)

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Temperature Monitoring <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5611_temperature_monitoring.html>`_

    `Thermal Shutdown <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/thermal_shutdown_monitoring_5650_5651_5652.html>`_

    +----------------------------+--------------------------+-------------------------+
    | Hardware Module            | TRX Port Type            | Active Channel String   |
    +============================+==========================+=========================+
    | PXIe-3621/3622             | —                        | if or "" (empty string) |
    +----------------------------+--------------------------+-------------------------+
    | PXIe-5820                  | —                        | fpga                    |
    +----------------------------+--------------------------+-------------------------+
    | First connected mmRH-5582  | DIRECT TRX PORTS Only    | rf0                     |
    +----------------------------+--------------------------+-------------------------+
    | First connected mmRH-5582  | SWITCHED TRX PORTS [0-7] | rf0switch0              |
    +----------------------------+--------------------------+-------------------------+
    | First connected mmRH-5582  | SWITCHED TRX PORTS [0-7] | rf0switch1              |
    +----------------------------+--------------------------+-------------------------+
    | Second connected mmRH-5582 | DIRECT TRX PORTS Only    | rf1                     |
    +----------------------------+--------------------------+-------------------------+
    | Second connected mmRH-5582 | SWITCHED TRX PORTS [0-7] | rf1switch0              |
    +----------------------------+--------------------------+-------------------------+
    | Second connected mmRH-5582 | SWITCHED TRX PORTS [0-7] | rf1switch1              |
    +----------------------------+--------------------------+-------------------------+

    Tip:
    This property can be set/get on specific device_temperatures within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container device_temperatures to specify a subset.

    Example: :py:attr:`my_session.device_temperatures[ ... ].device_temperature`

    To set/get on all device_temperatures, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.device_temperature`
    '''
    digital_edge_script_trigger_edge = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ScriptTriggerDigitalEdgeEdge, 1150021)
    '''Type: enums.ScriptTriggerDigitalEdgeEdge

    Specifies the active edge for the Script Trigger. This property is used when the script_trigger_type property is set to digital edge. To set the digital_edge_script_trigger_edge property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** ScriptTriggerDigitalEdgeEdge.RISING

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

    `Digital Edge Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_edge.html>`_

    **High-Level Methods**:

    - configure_digital_edge_script_trigger

    **Defined Values**:

    +--------------------------------------+---------+-------------------------------------------------------------------------------+
    | Name                                 | Value   | Description                                                                   |
    +======================================+=========+===============================================================================+
    | ScriptTriggerDigitalEdgeEdge.FALLING | 1 (0x1) | Asserts the trigger when the signal transitions from high level to low level. |
    +--------------------------------------+---------+-------------------------------------------------------------------------------+
    | ScriptTriggerDigitalEdgeEdge.RISING  | 0 (0x0) | Asserts the trigger when the signal transitions from low level to high level. |
    +--------------------------------------+---------+-------------------------------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

    Tip:
    This property can be set/get on specific script_triggers within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

    Example: :py:attr:`my_session.script_triggers[ ... ].digital_edge_script_trigger_edge`

    To set/get on all script_triggers, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.digital_edge_script_trigger_edge`
    '''
    digital_edge_script_trigger_source = _attributes.AttributeViString(1150020)
    '''Type: str

    Specifies the source terminal for the Script Trigger. This property is used when the script_trigger_type property is set to digital edge. To set this property, the NI-RFSG device must be in the Configuration state.

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

    `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_

    `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_

    **High-Level Methods**:

    - configure_digital_edge_script_trigger

    **Possible Values**:

    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | Possible Value | Description                                                                                                                             |
    +================+=========================================================================================================================================+
    | "PFI0"         | The trigger is received on PFI 0.                                                                                                       |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI1"         | The trigger is received on PFI 1.                                                                                                       |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI2"         | The trigger is received on PFI 2.                                                                                                       |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI3"         | The trigger is received on PFI 3.                                                                                                       |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Star"     | The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.                              |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig0"    | The trigger is received on PXI trigger line 0.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig1"    | The trigger is received on PXI trigger line 1.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig2"    | The trigger is received on PXI trigger line 2.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig3"    | The trigger is received on PXI trigger line 3.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig4"    | The trigger is received on PXI trigger line 4.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig5"    | The trigger is received on PXI trigger line 5.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig6"    | The trigger is received on PXI trigger line 6.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig7"    | The trigger is received on PXI trigger line 7.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXIe_DStarB"  | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PulseIn"      | The trigger is received on the PULSE IN terminal. This value is valid on only the PXIe-5842.                                            |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI0"     | The trigger is received on PFI0 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI1"     | The trigger is received on PFI1 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI2"     | The trigger is received on PFI2 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI3"     | The trigger is received on PFI3 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI4"     | The trigger is received on PFI4 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI5"     | The trigger is received on PFI5 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI6"     | The trigger is received on PFI6 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI7"     | The trigger is received on PFI7 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "Sync_Script"  | The trigger is received on the Sync Script trigger line. This value is valid on only the PXIe-5644/5645/5646.                           |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+

    Tip:
    This property can be set/get on specific script_triggers within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

    Example: :py:attr:`my_session.script_triggers[ ... ].digital_edge_script_trigger_source`

    To set/get on all script_triggers, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.digital_edge_script_trigger_source`
    '''
    digital_edge_start_trigger_edge = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.StartTriggerDigitalEdgeEdge, 1250459)
    '''Type: enums.StartTriggerDigitalEdgeEdge

    Specifies the active edge for the Start Trigger. This property is used when the start_trigger_type property is set to digital edge. To set the digital_edge_start_trigger_edge property, the NI-RFSG device must be in the Configuration state.

    PXIe-5654/5654 with PXIe-5696: The Start Trigger is valid only with a timer-based list when RF list mode is enabled.

    **Default Value:** StartTriggerDigitalEdgeEdge.RISING

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_

    `Digital Edge Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_edge.html>`_

    **High-Level Methods**:

    - configure_digital_edge_start_trigger

    **Defined Values**:

    +-------------------------------------+---------+------------------------------------------------------------------+
    | Name                                | Value   | Description                                                      |
    +=====================================+=========+==================================================================+
    | StartTriggerDigitalEdgeEdge.FALLING | 1 (0x1) | Occurs when the signal transitions from high level to low level. |
    +-------------------------------------+---------+------------------------------------------------------------------+
    | StartTriggerDigitalEdgeEdge.RISING  | 0 (0x0) | Occurs when the signal transitions from low level to high level. |
    +-------------------------------------+---------+------------------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    digital_edge_start_trigger_source = _attributes.AttributeViString(1150002)
    '''Type: str

    Specifies the source terminal for the Start Trigger. This property is used when the start_trigger_type property is set to digital edge. The digital_edge_start_trigger_source property is not case-sensitive. To set the digital_edge_start_trigger_source property, the NI-RFSG device must be in the Configuration state.

    PXIe-5654/5654 with PXIe-5696: The Start Trigger is valid only with a timer-based list when RF list mode is enabled.

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_

    `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_

    `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_

    **High-Level Methods**:

    - configure_digital_edge_start_trigger

     **Possible Values**:

    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | Possible Value | Description                                                                                                                            |
    +================+========================================================================================================================================+
    | "PFI0"         | The trigger is received on PFI 0.                                                                                                      |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI1"         | The trigger is received on PFI 1.                                                                                                      |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI2"         | The trigger is received on PFI 2.                                                                                                      |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI3"         | The trigger is received on PFI 3.                                                                                                      |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Star"     | The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.                             |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig0"    | The trigger is received on PXI trigger line 0.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig1"    | The trigger is received on PXI trigger line 1.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig2"    | The trigger is received on PXI trigger line 2.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig3"    | The trigger is received on PXI trigger line 3.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig4"    | The trigger is received on PXI trigger line 4.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig5"    | The trigger is received on PXI trigger line 5.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig6"    | The trigger is received on PXI trigger line 6.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig7"    | The trigger is received on PXI trigger line 7.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXIe_DStarB"  | The trigger is received on the PXI DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "TrigIn"       | The trigger is received on the TRIG IN/OUT terminal. This value is valid on only the PXIe-5654/5654 with PXIe-5696.                    |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI0"     | The trigger is received on PFI0 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI1"     | The trigger is received on PFI1 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI2"     | The trigger is received on PFI2 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI3"     | The trigger is received on PFI3 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI4"     | The trigger is received on PFI4 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI5"     | The trigger is received on PFI5 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI6"     | The trigger is received on PFI6 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI7"     | The trigger is received on PFI7 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "Sync_Script"  | The trigger is received on the Sync Script trigger line. This value is valid on only the PXIe-5644/5645/5646.                          |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    '''
    digital_equalization_enabled = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.DigitalEqualizationEnabled, 1150012)
    '''Type: enums.DigitalEqualizationEnabled

    When this property is enabled, NI-RFSG equalizes the waveform data to correct for variations in the response of the NI-RFSG device. Enabling digital equalization improves the modulation error rates (MER) and error vector magnitude (EVM) for signals with large bandwidths (>500 kHz), but it increases tuning times.

    On the PXI-5670/5671, equalization is performed in the software, so tuning time is increased. On the PXIe-5672, equalization is performed in the hardware so that there is no compromise in performance.

    This property applies only when the generation_mode property is set to GenerationMode.ARB_WAVEFORM or GenerationMode.SCRIPT. To set this property, the NI-RFSG device must be in the Configuration state.

    PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: DigitalEqualizationEnabled.ENABLE is the only supported value for this device.

    **Default Value:**

    PXI-5670/5671: DigitalEqualizationEnabled.DISABLE

    PXIe-5644/5645/5646, PXIe-5672, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: DigitalEqualizationEnabled.ENABLE

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Response and Software Equalization <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/if_response_and_equalizer.html>`_—Refer to this topic for more information about equalization performed in software.

    `Frequency Tuning Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_tuning_times.html>`_

    **Defined Values**:

    +------------------------------------+---------+-----------------------+
    | Name                               | Value   | Description           |
    +====================================+=========+=======================+
    | DigitalEqualizationEnabled.DISABLE | 0 (0x0) | Filter is not applied |
    +------------------------------------+---------+-----------------------+
    | DigitalEqualizationEnabled.ENABLE  | 1 (0x1) | Filter is applied.    |
    +------------------------------------+---------+-----------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    digital_level_script_trigger_active_level = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ScriptTriggerDigitalLevelActiveLevel, 1150055)
    '''Type: enums.ScriptTriggerDigitalLevelActiveLevel

    Specifies the active level for the Script Trigger. This property is used when the script_trigger_type property is set to ScriptTriggerType.DIGITAL_LEVEL.

    **Default Value:** ScriptTriggerDigitalLevelActiveLevel.HIGH

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

    `Digital Level Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_level.html>`_

    **Defined Values**:

    +-------------------------------------------+---------------+--------------------------------------------------+
    | Name                                      | Value         | Description                                      |
    +===========================================+===============+==================================================+
    | ScriptTriggerDigitalLevelActiveLevel.HIGH | 9000 (0x2328) | Trigger when the digital trigger signal is high. |
    +-------------------------------------------+---------------+--------------------------------------------------+
    | ScriptTriggerDigitalLevelActiveLevel.LOW  | 9001 (0x2329) | Trigger when the digital trigger signal is low.  |
    +-------------------------------------------+---------------+--------------------------------------------------+

    Tip:
    This property can be set/get on specific script_triggers within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

    Example: :py:attr:`my_session.script_triggers[ ... ].digital_level_script_trigger_active_level`

    To set/get on all script_triggers, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.digital_level_script_trigger_active_level`
    '''
    digital_level_script_trigger_source = _attributes.AttributeViString(1150054)
    '''Type: str

    Specifies the source terminal for the Script Trigger. This property is used when the script_trigger_type property is set to ScriptTriggerType.DIGITAL_LEVEL. The digital_level_script_trigger_source property is not case-sensitive.

    To set the digital_level_script_trigger_source property, the NI-RFSG device must be in the Configuration state.

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

    `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_

    `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_

    **Possible Values**:

    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | Possible Value | Description                                                                                                                             |
    +================+=========================================================================================================================================+
    | "PFI0"         | The trigger is received on PFI 0.                                                                                                       |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI1"         | The trigger is received on PFI 1.                                                                                                       |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI2"         | The trigger is received on PFI 2.                                                                                                       |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI3"         | The trigger is received on PFI 3.                                                                                                       |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Star"     | The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.                              |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig0"    | The trigger is received on PXI trigger line 0.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig1"    | The trigger is received on PXI trigger line 1.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig2"    | The trigger is received on PXI trigger line 2.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig3"    | The trigger is received on PXI trigger line 3.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig4"    | The trigger is received on PXI trigger line 4.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig5"    | The trigger is received on PXI trigger line 5.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig6"    | The trigger is received on PXI trigger line 6.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig7"    | The trigger is received on PXI trigger line 7.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXIe_DStarB"  | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PulseIn"      | The trigger is received on the PULSE IN terminal. This value is valid on only the PXIe-5842.                                            |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI0"     | The trigger is received on PFI0 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI1"     | The trigger is received on PFI1 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI2"     | The trigger is received on PFI2 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI3"     | The trigger is received on PFI3 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI4"     | The trigger is received on PFI4 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI5"     | The trigger is received on PFI5 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI6"     | The trigger is received on PFI6 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI7"     | The trigger is received on PFI7 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+

    Tip:
    This property can be set/get on specific script_triggers within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

    Example: :py:attr:`my_session.script_triggers[ ... ].digital_level_script_trigger_source`

    To set/get on all script_triggers, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.digital_level_script_trigger_source`
    '''
    direct_download = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.DirectDownload, 1150042)
    '''Type: enums.DirectDownload

    Specifies whether the WriteArbWaveform method immediately writes waveforms to the device or copies the waveform to host memory for later download. NI-RFSG reads and validates this property when an arbitrary waveform is first allocated.

    For the PXI-5670, direct download is always disabled. For all other devices, direct download is always enabled.

    PXI-5671: To increase performance when using large waveforms, enable direct download. To maximize reconfigurability, disable direct download.

    Perform the following steps to enable direct download:

    1. Set the I/Q rate to less than or equal to 8.33MS/s with the iq_rate property.

    2. Set the power_level_type property to PowerLevelType.PEAK.

    3. Disable the iq_swap_enabled property.

    4. Disable the digital_equalization_enabled property.

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5840/5841/5842/5860

    **Defined Values**:

    +----------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | Name                       | Value     | Description                                                                                                                             |
    +============================+===========+=========================================================================================================================================+
    | DirectDownload.DISABLE     | 0 (0x0)   | The RF In local oscillator signal is not present at the front panel LO OUT connector.                                                   |
    +----------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | DirectDownload.ENABLE      | 1 (0x1)   | The RF In local oscillator signal is present at the front panel LO OUT connector.                                                       |
    +----------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | DirectDownload.UNSPECIFIED | -2 (-0x2) | The RF IN local oscillator signal may or may not be present at the front panel LO OUT connector, because NI-RFSA may be controlling it. |
    +----------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    done_event_terminal_name = _attributes.AttributeViString(1150113)
    '''Type: str

    Returns the name of the fully qualified signal name as a string.

    **Default Values**:

    PXI-5670/5671, PXIe-5672/5673/5673E: /*AWGName*/DoneEvent, where *AWGName* is the name of your associated AWG module in MAX.

    PXIe-5830/5831/5832: /*BasebandModule*/ao/0/DoneEvent, where *BasebandModule* is the name of the baseband module of your device in MAX.

    PXIe-5820/5840/5841: /*ModuleName*/ao/0/DoneEvent, where *ModuleName* is the name of your device in MAX.

    PXIe-5860: /*ModuleName*/ao/*ChannelNumber*/DoneEvent, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

    **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

    `Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_

    **High-Level Methods**:

    - get_terminal_name
    '''
    events_delay = _attributes.AttributeViReal64TimeDeltaSeconds(1150154)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the delay, in seconds, applied to the Started Event, Done Event, and all Marker Events with respect to the analog output of the RF signal generator. To set this property, the NI-RFSG device must be in the Configuration or Generation state.

    By default, markers and events are delayed to align with the waveform data generated from the device. This property adds an additional delay to markers and events. Use this property to adjust the time delay between events and the corresponding data.

    **Units:** Seconds

    **Valid Values:**

    PXIe-5644/5645: -1.217 μs to 67.050 μs

    PXIe-5646: -0.896 μs to 64.640 μs

    PXIe-5820/5830/5831/5832/5840/5841/5842: 0 μs to 3.276 μs

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

    Note: If you decrease the event delay during generation, some markers may be dropped.
    '''
    exported_configuration_settled_event_output_terminal = _attributes.AttributeViString(1150129)
    '''Type: str

    Specifies the destination terminal for exporting the Configuration Settled event. To set this property, the NI-RFSG device must be in the Configuration state.

    **Supported Devices:** PXIe-5654/5654 with PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_

    `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

    `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_

    `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_

    **Possible Values**:

    +----------------+--------------------------------------------------------------------------------------------------------------------+
    | Possible Value | Description                                                                                                        |
    +================+====================================================================================================================+
    | ""             | The signal is not exported.                                                                                        |
    +----------------+--------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig0"    | The trigger is received on PXI trigger line 0.                                                                     |
    +----------------+--------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig1"    | The trigger is received on PXI trigger line 1.                                                                     |
    +----------------+--------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig2"    | The trigger is received on PXI trigger line 2.                                                                     |
    +----------------+--------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig3"    | The trigger is received on PXI trigger line 3.                                                                     |
    +----------------+--------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig4"    | The trigger is received on PXI trigger line 4.                                                                     |
    +----------------+--------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig5"    | The trigger is received on PXI trigger line 5.                                                                     |
    +----------------+--------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig6"    | The trigger is received on PXI trigger line 6.                                                                     |
    +----------------+--------------------------------------------------------------------------------------------------------------------+
    | "PXIe_DStarC"  | The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5840/5841/5842. |
    +----------------+--------------------------------------------------------------------------------------------------------------------+
    | "TrigOut"      | TRIG IN/OUT terminal.                                                                                              |
    +----------------+--------------------------------------------------------------------------------------------------------------------+
    '''
    exported_done_event_output_terminal = _attributes.AttributeViString(1150063)
    '''Type: str

    Specifies the destination terminal for exporting the Done event. To set this property, the NI-RFSG device must be in the Configuration state.

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_

    `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

    `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_

    `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_

    **Possible Values**:

    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | Posible Value | Description                                                                                                                     |
    +===============+=================================================================================================================================+
    | ""            | The signal is not exported.                                                                                                     |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PFI0"        | The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0. |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PFI1"        | The signal is exported to the PFI 1 connector.                                                                                  |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PFI4"        | The signal is exported to the PFI 4 connector.                                                                                  |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PFI5"        | The signal is exported to the PFI 5 connector.                                                                                  |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig0"   | The trigger is received on PXI trigger line 0.                                                                                  |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig1"   | The trigger is received on PXI trigger line 1.                                                                                  |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig2"   | The trigger is received on PXI trigger line 2.                                                                                  |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig3"   | The trigger is received on PXI trigger line 3.                                                                                  |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig4"   | The trigger is received on PXI trigger line 4.                                                                                  |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig5"   | The trigger is received on PXI trigger line 5.                                                                                  |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig6"   | The trigger is received on PXI trigger line 6.                                                                                  |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXIe_DStarC" | The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.    |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI0"    | The trigger is received on PFI0 from the front panel DIO terminal.                                                              |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI1"    | The trigger is received on PFI1 from the front panel DIO terminal.                                                              |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI2"    | The trigger is received on PFI2 from the front panel DIO terminal.                                                              |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI3"    | The trigger is received on PFI3 from the front panel DIO terminal.                                                              |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI4"    | The trigger is received on PFI4 from the front panel DIO terminal.                                                              |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI5"    | The trigger is received on PFI5 from the front panel DIO terminal.                                                              |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI6"    | The trigger is received on PFI6 from the front panel DIO terminal.                                                              |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI7"    | The trigger is received on PFI7 from the front panel DIO terminal.                                                              |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    '''
    exported_marker_event_output_terminal = _attributes.AttributeViString(1150064)
    '''Type: str

    Specifies the destination terminal for exporting the Marker Event. To set this property, the NI-RFSG device must be in the Configuration state.

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_

    `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_

    `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_

    **Possible Values**:

    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | Possible Value | Description                                                                                                                     |
    +================+=================================================================================================================================+
    | ""             | The signal is not exported.                                                                                                     |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PFI0"         | The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0. |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PFI1"         | The signal is exported to the PFI 1 connector.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PFI4"         | The signal is exported to the PFI 4 connector.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PFI5"         | The signal is exported to the PFI 5 connector.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig0"    | The trigger is received on PXI trigger line 0.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig1"    | The trigger is received on PXI trigger line 1.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig2"    | The trigger is received on PXI trigger line 2.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig3"    | The trigger is received on PXI trigger line 3.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig4"    | The trigger is received on PXI trigger line 4.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig5"    | The trigger is received on PXI trigger line 5.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig6"    | The trigger is received on PXI trigger line 6.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXIe_DStarC"  | The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.    |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI0"     | The trigger is received on PFI0 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI1"     | The trigger is received on PFI1 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI2"     | The trigger is received on PFI2 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI3"     | The trigger is received on PFI3 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI4"     | The trigger is received on PFI4 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI5"     | The trigger is received on PFI5 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI6"     | The trigger is received on PFI6 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI7"     | The trigger is received on PFI7 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+

    Tip:
    This property can be set/get on specific markers within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container markers to specify a subset.

    Example: :py:attr:`my_session.markers[ ... ].exported_marker_event_output_terminal`

    To set/get on all markers, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.exported_marker_event_output_terminal`
    '''
    exported_pulse_modulation_event_active_level = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ScriptTriggerDigitalLevelActiveLevel, 1150310)
    '''Type: enums.ScriptTriggerDigitalLevelActiveLevel

    Specifies the active level of the exported Pulse Modulation Event. When `property pulse modulation enabled` is Enabled, `pulse modulation active level` is `active high`, `exported pulse modulation event output terminal` is `PulseOut`, and this property is `active high`, then the Pulse Modulation Event will transition from Low to High after the the Pulse In signal is set to logic high, and the RF Output has settled. To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** ScriptTriggerDigitalLevelActiveLevel.HIGH

    **Supported Devices:**  PXIe-5842

    **Defined Values**:

    +-------------------------------------------+---------------+--------------------------------------------------+
    | Name                                      | Value         | Description                                      |
    +===========================================+===============+==================================================+
    | ScriptTriggerDigitalLevelActiveLevel.HIGH | 9000 (0x2328) | Trigger when the digital trigger signal is high. |
    +-------------------------------------------+---------------+--------------------------------------------------+
    | ScriptTriggerDigitalLevelActiveLevel.LOW  | 9001 (0x2329) | Trigger when the digital trigger signal is low.  |
    +-------------------------------------------+---------------+--------------------------------------------------+
    '''
    exported_pulse_modulation_event_output_terminal = _attributes.AttributeEnum(_attributes.AttributeViString, enums.PulseModulationOutputTerminal, 1150309)
    '''Type: enums.PulseModulationOutputTerminal

    Specifies the destination terminal for exporting the Pulse Modulation Event. The Pulse Modulation Event tracks the RF Envelope when Pulse Modulation is Enabled. If this property is set to a value other than `do not export str`, calling NI-RFSG Commit will cause the output terminal to be pulled to the logic level that is the inverse of `exported pulse modulation event active level`. You can tri-state this terminal by setting this property to `do not export str` or by calling `niRFSG Reset`. To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** PulseOut

    **Supported Devices:**  PXIe-5842

    **Possible Values**:

    +----------------+---------------------------------------------------------------------+
    | Possible Value | Description                                                         |
    +================+=====================================================================+
    | ""             | Pulse modulation video signal is not exported.                      |
    +----------------+---------------------------------------------------------------------+
    | "PulseOut"     | Export the pulse modulation video signal on the pulse out terminal. |
    +----------------+---------------------------------------------------------------------+
    '''
    exported_ref_clock_output_terminal = _attributes.AttributeEnum(_attributes.AttributeViString, enums.ReferenceClockExportOutputTerminal, 1150053)
    '''Type: enums.ReferenceClockExportOutputTerminal

    Specifies the destination terminal for exporting the Reference Clock on the RF signal generators. To set this property, the NI-RFSG device must be in the Configuration state.

    **Possible Values**:

    Possible Value: Description

    "" :The Reference Clock signal is not exported.

    "RefOut" :Exports the Reference Clock signal to the REF OUT connector of the device.

    "RefOut2" :Exports the Reference Clock signal to the REF OUT2 connector of the device, if applicable.

    "ClkOut" :Exports the Reference Clock signal to the CLK OUT connector of the device.

    **Default Value:** '""'

    **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Interconnecting Multiple NI 5673E Modules <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/interconnecting_multiple_ni_5673_modules.html>`_

    +----------------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Possible Value | Description                                                                                | Supported devices                                                                                                                                                     |
    +================+============================================================================================+=======================================================================================================================================================================+
    | "ClkOut"       | Exports the Reference Clock signal to the CLK OUT connector of the device.                 | Supported on PXIe-5673, 5673E                                                                                                                                         |
    +----------------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ""             | The Reference Clock signal is not exported.                                                | Supported on PXIe-5644/5645/5646, 5820/5830/5831/5832/5840/5841/5842/5860, 5650/5651/5652, 5654, 5673, 5673E, PXIe-5654 with PXIe-5696, PXI-5650/5651/5652 (See Note) |
    +----------------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | "RefOut"       | Exports the Reference Clock signal to the REF OUT connector of the device.                 | Supported on PXIe-5644/5645/5646, 5820/5830/5831/5832/5840/5841/5842/5860, 5650/5651/5653, 5653, 5654, 5673, 5673E, PXIe-5654 with PXIe-5696, PXI-5650/5651/5653,     |
    +----------------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | "RefOut2"      | Exports the Reference Clock signal to the REF OUT2 connector of the device, if applicable. | Supported on PXIe-5650/5651/5652, 5654, 5673E, PXIe-5654 with PXIe-5696                                                                                               |
    +----------------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    Note: The RefOut2 output terminal value is valid for only the PXIe-5650/5651/5652, not the PXI-5650/5651/5652.
    '''
    exported_ref_clock_rate = _attributes.AttributeViReal64(1150292)
    '''Type: float

    Specifies the Reference Clock Rate, in Hz, of the signal sent to the Reference Clock Export Output Terminal. To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** 10MHz

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +--------------+-------------------------------------+
    | Value        | Description                         |
    +==============+=====================================+
    | 10000000.0   | Uses a 10MHz Reference Clock rate.  |
    +--------------+-------------------------------------+
    | 100000000.0  | Uses a 100MHz Reference Clock rate. |
    +--------------+-------------------------------------+
    | 1000000000.0 | Uses a 1GHz Reference Clock rate.   |
    +--------------+-------------------------------------+
    '''
    exported_script_trigger_output_terminal = _attributes.AttributeViString(1150022)
    '''Type: str

    Specifies the destination terminal for exporting the Script Trigger. To set this property, the NI-RFSG device must be in the Configuration state.

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_ —Refer to this topic for information about trigger delay.

    `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_

    `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_

    **Possible Values**:

    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | Possible Value | Description                                                                                                                     |
    +================+=================================================================================================================================+
    | ""             | The signal is not exported.                                                                                                     |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PFI0"         | The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0. |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PFI1"         | The signal is exported to the PFI 1 connector.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PFI4"         | The signal is exported to the PFI 4 connector.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PFI5"         | The signal is exported to the PFI 5 connector.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig0"    | The trigger is received on PXI trigger line 0.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig1"    | The trigger is received on PXI trigger line 1.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig2"    | The trigger is received on PXI trigger line 2.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig3"    | The trigger is received on PXI trigger line 3.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig4"    | The trigger is received on PXI trigger line 4.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig5"    | The trigger is received on PXI trigger line 5.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig6"    | The trigger is received on PXI trigger line 6.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXIe_DStarC"  | The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.    |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI0"     | The trigger is received on PFI0 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI1"     | The trigger is received on PFI1 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI2"     | The trigger is received on PFI2 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI3"     | The trigger is received on PFI3 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI4"     | The trigger is received on PFI4 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI5"     | The trigger is received on PFI5 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI6"     | The trigger is received on PFI6 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI7"     | The trigger is received on PFI7 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+

    Tip:
    This property can be set/get on specific script_triggers within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

    Example: :py:attr:`my_session.script_triggers[ ... ].exported_script_trigger_output_terminal`

    To set/get on all script_triggers, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.exported_script_trigger_output_terminal`
    '''
    exported_started_event_output_terminal = _attributes.AttributeViString(1150065)
    '''Type: str

    Specifies the destination terminal for exporting the Started event. To set this property, the NI-RFSG device must be in the Configuration state.

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

    `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_

    `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_

    **Possible Values**:

    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | Possible Value | Description                                                                                                                            |
    +================+========================================================================================================================================+
    | ""             | The signal is not exported.                                                                                                            |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI0"         | The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.        |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI1"         | The signal is exported to the PFI 1 connector.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI4"         | The signal is exported to the PFI 4 connector.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI5"         | The signal is exported to the PFI 5 connector.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig0"    | The trigger is received on PXI trigger line 0.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig1"    | The trigger is received on PXI trigger line 1.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig2"    | The trigger is received on PXI trigger line 2.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig3"    | The trigger is received on PXI trigger line 3.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig4"    | The trigger is received on PXI trigger line 4.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig5"    | The trigger is received on PXI trigger line 5.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig6"    | The trigger is received on PXI trigger line 6.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXIe_DStarC"  | The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI0"     | The trigger is received on PFI0 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI1"     | The trigger is received on PFI1 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI2"     | The trigger is received on PFI2 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI3"     | The trigger is received on PFI3 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI4"     | The trigger is received on PFI4 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI5"     | The trigger is received on PFI5 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI6"     | The trigger is received on PFI6 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI7"     | The trigger is received on PFI7 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    '''
    exported_start_trigger_output_terminal = _attributes.AttributeViString(1150003)
    '''Type: str

    Specifies the destination terminal for exporting the Start Trigger. To set this property, the NI-RFSG device must be in the Configuration state.

    PXIe-5654/5654 with PXIe-5696: The Start Trigger is valid only with a timer-based list when RF list mode is enabled.

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_

    `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_

    `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_

    **Possible Values**:

    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | Possible Value | Description                                                                                                                            |
    +================+========================================================================================================================================+
    | ""             | The signal is not exported.                                                                                                            |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI0"         | The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.        |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI1"         | The signal is exported to the PFI 1 connector.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI4"         | The signal is exported to the PFI 4 connector.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI5"         | The signal is exported to the PFI 5 connector.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig0"    | The trigger is received on PXI trigger line 0.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig1"    | The trigger is received on PXI trigger line 1.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig2"    | The trigger is received on PXI trigger line 2.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig3"    | The trigger is received on PXI trigger line 3.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig4"    | The trigger is received on PXI trigger line 4.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig5"    | The trigger is received on PXI trigger line 5.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig6"    | The trigger is received on PXI trigger line 6.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXIe_DStarC"  | The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "TrigOut"      | The signal is exported to the TRIG IN/OUT terminal. This value is valid on only the PXIe-5654/5654 with PXIe-5696.                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI0"     | The trigger is received on PFI0 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI1"     | The trigger is received on PFI1 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI2"     | The trigger is received on PFI2 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI3"     | The trigger is received on PFI3 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI4"     | The trigger is received on PFI4 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI5"     | The trigger is received on PFI5 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI6"     | The trigger is received on PFI6 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI7"     | The trigger is received on PFI7 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    '''
    external_calibration_recommended_interval = _attributes.AttributeViInt32TimeDeltaMonths(1150076)
    '''Type: hightime.timedelta

    Returns the recommended interval between each external calibration of the device.

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    external_calibration_temperature = _attributes.AttributeViReal64(1150077)
    '''Type: float

    Returns the temperature of the device at the time of the last external calibration.

    **Units**: degrees Celsius (°C)

    **Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E
    '''
    external_gain = _attributes.AttributeViReal64(1150085)
    '''Type: float

    Specifies the external amplification or attenuation, if any, between the RF signal generator and the device under test.

    Positive values for this property represent amplification, and negative values for this property represent attenuation.

    **Valid Values:** -INF dB to +INF dB

    **Default Value:** 0dB

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    Note: - Setting this property adjusts the actual device output power to compensate for any amplification or attenuation between the RF signal generator and the device under test.

     - For the PXIe-5645, this property is ignored if you are using the I/Q ports.
    '''
    fast_tuning_option = _attributes.AttributeViBoolean(1150188)
    '''Type: bool

    Returns whether the NI RF signal generator has the fast tuning option available.

    **Supported Devices:** PXIe-5654/5654 with PXIe-5696

    **Related Topics**

    `Frequency Tuning Times for 5654 <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_tuning_times.5654.html>`_

    **Defined Values**:

    +-------+------------------------------------------------------------+
    | Value | Description                                                |
    +=======+============================================================+
    | True  | The RF signal generator has the fast 100 µs tuning option. |
    +-------+------------------------------------------------------------+
    | False | The RF signal generator has the 1 ms tuning option.        |
    +-------+------------------------------------------------------------+
    '''
    fixed_group_delay_across_ports = _attributes.AttributeViStringCommaSeparated(1150271)
    '''Type: list of str

    Specifies a list of ports for which to fix the group delay.


    **Supported Devices:** PXIe-5831/5832
    '''
    fpga_bitfile_path = _attributes.AttributeViString(1150186)
    '''Type: str

    Returns a string containing the path to the location of the current NI-RFSG instrument driver FPGA extensions bitfile, a .lvbitx file, that is programmed on the device. You can specify the bitfile location using the Driver Setup string in the **optionString** parameter of the __init__ method.

    NI-RFSG instrument driver FPGA extensions enable you to use pre-compiled FPGA bitfiles to customize the behavior of the vector signal transceiver FPGA while maintaining the functionality of the NI-RFSG instrument driver.

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `NI-RFSG Instrument Driver FPGA Extensions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/fpga_extensions.html>`_
    '''
    fpga_target_name = _attributes.AttributeViString(1150251)
    '''Type: str

    Returns a string that contains the name of the FPGA target being used. This name can be used with the RIO open session to open a reference to the FPGA.

    This property is channel dependent if multiple FPGA targets are supported.

    **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    fpga_temperature = _attributes.AttributeViReal64(1150211)
    '''Type: float

    Returns the FPGA temperature in degrees Celsius.

    Serial signals between the sensor and the system control unit can potentially modulate the signal being generated, thus causing phase spurs. After the device thoroughly warms up, its temperature varies only slightly (less than 1 degree Celsius) and slowly, and it is not necessary to constantly poll this temperature sensor.

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    Note: If you query this property during RF list mode, list steps may take longer to complete during list execution.
    '''
    frequency = _attributes.AttributeViReal64(1250001)
    '''Type: float

    Specifies the frequency of the generated RF signal. For arbitrary waveform generation, this property specifies the center frequency of the signal.

    The PXI-5670/5671, PXIe-5672, PXIe-5820, and PXIe-5860 must be in the Configuration state to use this property. However, the PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673/5673E, and PXIe-5830/5831/5832/5840/5841/5842 can be in the Configuration or the Generation state to use this property.

    **Units**: hertz (Hz)

    **Defined Values**:
    Refer to the specifications document for your device allowable frequency settings.

    **Default Value:**

    PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E: 100MHz

    PXIe-5653: 4GHz

    PXIe-5820: 0Hz

    PXIe-5830/5831/5832: 6.5 GHz

    PXIe-5840/5841/5860, PXI-5842 (500 MHz, 1 GHz, and 2 GHz bandwidth options): 1GHz

    PXIe-5842 (4 GHz bandwidth option) using the Standard personality: 1GHz

    PXIe-5842 (4 GHz bandwidth option) using the 4 GHz Bandwidth personality: 6.5GHz

    **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_

    **High-Level Methods**:

    - ConfigureRf

    Note: For the PXIe-5645, this property is ignored if you are using the I/Q ports.
    '''
    frequency_settling = _attributes.AttributeViReal64(1150083)
    '''Type: float

    Specifies the frequency settling time. Interpretation of this value depends on the frequency_settling_units property.

    **Valid Values:**

    The valid values for this property depend on the frequency_settling_units property.



    **Default Value**: 1.0

    **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Settling Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/settling_times.html>`_

    `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_
    '''
    frequency_settling_units = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.FrequencySettlingUnits, 1150082)
    '''Type: enums.FrequencySettlingUnits

    Specifies the interpretation of the value passed to the frequency_settling property.

    PXIe-5650/5651/5652/5653, PXIe-5673E: When the ACTIVE_CONFIGURATION_LIST property is set to a valid list name, the frequency_settling_units property supports only FrequencySettlingUnits.TIME_AFTER_IO as a valid value.

    PXIe-5654/5654 with PXIe-5696: The frequency_settling_units property supports only FrequencySettlingUnits.TIME_AFTER_IO and FrequencySettlingUnits.PPM as valid values.

    **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842

    **Default Value**: FrequencySettlingUnits.PPM

    **Related Topics**

    `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

    **Defined Values**:

    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
    | Name                                   | Description                                                                                                     |
    +========================================+=================================================================================================================+
    | FrequencySettlingUnits.TIME_AFTER_LOCK | Specifies the time to wait after the frequency PLL locks.                                                       |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
    | FrequencySettlingUnits.TIME_AFTER_IO   | Specifies the time to wait after all writes occur to change the frequency.                                      |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
    | FrequencySettlingUnits.PPM             | Specifies the minimum frequency accuracy when settling completes. Units are in parts per million (PPM or 1E-6). |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------+

    Note: If you set this property to FrequencySettlingUnits.TIME_AFTER_IO, the definition of settled for the Configuration Settled event changes.

    Note:
    One or more of the referenced properties are not in the Python API for this driver.
    '''
    generation_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.GenerationMode, 1150018)
    '''Type: enums.GenerationMode

    Specifies whether to generate a continuous wave (CW) signal, the arbitrary waveform specified by the arb_selected_waveform property, or the script specified by the selected_script property, upon calling the _initiate method.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** GenerationMode.CW

    **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696 (CW support only), PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_

    `Scripting Instructions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_instructions.html>`_—Refer to this topic for more information about scripting.

    **Defined Values**:

    +-----------------------------+--------------+------------------------------------------------------------------------------------------------------------------------+
    | Name                        | Value        | Description                                                                                                            |
    +=============================+==============+========================================================================================================================+
    | GenerationMode.ARB_WAVEFORM | 1001 (0x3e9) | Configures the RF signal generator to generate the arbitrary waveform specified by the arb_selected_waveform property. |
    +-----------------------------+--------------+------------------------------------------------------------------------------------------------------------------------+
    | GenerationMode.CW           | 1000 (0x3e8) | Configures the RF signal generator to generate a CW signal.                                                            |
    +-----------------------------+--------------+------------------------------------------------------------------------------------------------------------------------+
    | GenerationMode.SCRIPT       | 1002 (0x3ea) | Configures the RF signal generator to generate arbitrary waveforms as directed by the selected_script property..       |
    +-----------------------------+--------------+------------------------------------------------------------------------------------------------------------------------+
    '''
    group_capabilities = _attributes.AttributeViStringCommaSeparated(1050401)
    '''Type: list of str

    Returns a list of class-extension groups that NI-RFSG implements.

    **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    host_dma_buffer_size = _attributes.AttributeViInt64(1150239)
    '''Type: int

    Specifies the size of the DMA buffer in computer memory, in bytes. To set this property, the NI-RFSG device must be in the Configuration state.

    A sufficiently large host DMA buffer improves performance by allowing large writes to be transferred more efficiently.

    **Units:** bytes

    **Default Value:** 8MB

    **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    instrument_firmware_revision = _attributes.AttributeViString(1050510)
    '''Type: str

    Returns a string that contains the firmware revision information for the NI-RFSG device you are currently using.

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    instrument_manufacturer = _attributes.AttributeViString(1050511)
    '''Type: str

    Returns a string that contains the name of the manufacturer of the NI-RFSG device you are currently using.

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    instrument_model = _attributes.AttributeViString(1050512)
    '''Type: str

    Returns a string that contains the model number or name of the NI-RFSG device that you are currently using. For drivers that support more than one device, this property returns a comma-separated list of supported devices.

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    interpolation_delay = _attributes.AttributeViReal64TimeDeltaSeconds(1150153)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the delay, in seconds, to apply to the I/Q waveform. To set this property, the NI-RFSG device must be in the Configuration state.

    **Units:** Seconds

    **Valid Values:** Plus or minus half of one I/Q sample period

    **Supported Devices:** PXIe-5644/5645/5646
    '''
    io_resource_descriptor = _attributes.AttributeViString(1050304)
    '''Type: str

    Returns a string that contains the resource name NI-RFSG uses to identify the physical device. If you initialize NI-RFSG with a logical name, this property contains the resource name that corresponds to the entry in the IVI Configuration Utility. If you initialize NI-RFSG with the resource name, this property contains that value.

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    iq_gain_imbalance = _attributes.AttributeViReal64(1150072)
    '''Type: float

    Specifies the gain imbalance of the I/Q modulator (I versus Q).

    Gain imbalance is calculated with the following equation:

    **Units**: dB

    **Valid Values:**-6dB to 6dB

    **Default Value:** 0dB

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Impairment Calibration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/vector_calibration.html>`_

    `Spurious Performance <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/spurious_performance.html>`_
    '''
    iq_impairment_enabled = _attributes.AttributeViBoolean(1150069)
    '''Type: bool

    Enables or disables I/Q impairment. The iq_i_offset, iq_q_offset, iq_gain_imbalance, and iq_skew properties are ignored when the iq_impairment_enabled property is disabled.

    **Default Value:** True

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

    **Defined Values**:

    +-------+-----------------------------+
    | Value | Description                 |
    +=======+=============================+
    | True  | I/Q impairment is enabled.  |
    +-------+-----------------------------+
    | False | I/Q impairment is disabled. |
    +-------+-----------------------------+
    '''
    iq_i_offset = _attributes.AttributeViReal64(1150070)
    '''Type: float

    When using a National Instruments AWG module or vector signal transceiver (VST), this property specifies the I-signal DC offset. Units are either percent (%) or volts (V), depending on the iq_offset_units property setting.

    PXIe-5673/5673E: Actual AWG signal offset is equal to the I/Q modulator offset correction plus the value specified by this property. When using an external AWG (non–National Instruments AWG), this property is read-only and indicates the I/Q modulator I-offset. Units are volts, as specified by the iq_offset_units property.

    **Valid Values:**-100 to 100% or -0.2V to 0.2V

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Impairment Calibration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/vector_calibration.html>`_
    '''
    iq_offset_units = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.OffsetUnits, 1150081)
    '''Type: enums.OffsetUnits

    Specifies the units of the iq_i_offset property and iq_q_offset property. Offset units are either percent or volts.

    The AWG or VST offset is the specified percentage of the AWG or VST peak power level when the iq_offset_units property is set to OffsetUnits.PERCENT. Given perfect carrier leakage suppression, the following equation is satisfied


    or equivalently

    If the iq_i_offset property is set to 100%, iq_q_offset property is set to 0%, and power_level property set to 0 dBm, the desired RF signal is at 0 dBm and the carrier leakage is also at 0 dBm.

    The AWG or VST peak power level changes when settings change in other properties such as the power_level, frequency, iq_skew, iq_gain_imbalance and arb_pre_filter_gain properties. When the iq_offset_units property is set to OffsetUnits.PERCENT, the actual AWG or VST offset changes as the AWG or VST peak power level changes to satisfy the preceding equations. These changes are useful if you are intentionally adding carrier leakage to test the tolerance of a receiver. When the iq_offset_units property is set to OffsetUnits.PERCENT, the carrier leakage, in dBc, remains at a consistent level.

    If you are trying to eliminate residual carrier leakage due to calibration inaccuracies or drift, set the iq_offset_units property to OffsetUnits.VOLTS. Offset correction voltage is applied to the I/Q modulator or VST, regardless of changes to the AWG or VST peak power level.

    **Default Value**: OffsetUnits.PERCENT

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

    **Defined Values**:

    +---------------------+----------------------------------------------------------------------+
    | Name                | Description                                                          |
    +=====================+======================================================================+
    | OffsetUnits.PERCENT | Specifies the iq_i_offset and iq_q_offset property units as percent. |
    +---------------------+----------------------------------------------------------------------+
    | OffsetUnits.VOLTS   | Specifies the iq_i_offset and iq_q_offset property units as volts.   |
    +---------------------+----------------------------------------------------------------------+

    Note: For any devices except PXIe-5820, if the iq_offset_units property is set to OffsetUnits.VOLTS, a 0.1 I offset results in a 0.1 V offset in the output. For PXIe-5820 devices, 0.1 I offset results in a 10% offset in the output.
    '''
    iq_out_port_carrier_frequency = _attributes.AttributeViReal64(1150145)
    '''Type: float

    Specifies the frequency of the I/Q OUT port signal. The onboard signal processing (OSP) applies the specified frequency shift to the I/Q data before the data is sent to the digital-to-analog converter (DAC). To set this property, the NI-RFSG device must be in the Configuration state.

    **Units:** hertz (Hz)

    **Valid Values:**

    PXIe-5645: -60MHz to 60MHz

    PXIe-5820: -500MHz to 500MHz

    **Supported Devices:** PXIe-5645, PXIe-5820

    Note: - For the PXIe-5820, NI recommends using the frequency property.

     - For the PXIe-5645, this property is ignored if you are using the RF ports.
    '''
    iq_out_port_common_mode_offset = _attributes.AttributeViReal64(1150148)
    '''Type: float

    Specifies the common-mode offset applied to the signals generated at each differential output terminal. This property applies only when you set the iq_out_port_terminal_configuration property to IQOutPortTerminalConfiguration.DIFFERENTIAL. Common-mode offset shifts both positive and negative terminals in the same direction.

    To use this property, you must use the channelName parameter of the _set_attribute_vi_real64 method to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Units:** Volts

    **Valid Values:**

    PXIe-5645: -0.8V to 0.8V if you set the iq_out_port_load_impedance property to 50 Ω. The valid values are -1.2V to 1.2V if you set the iq_out_port_load_impedance property to 100 Ω.

    PXIe-5820: -0.25V to 1.5V

    **Supported Devices:** PXIe-5645, PXIe-5820

    Note: - For the PXIe-5645, this property is ignored if you are using the RF ports.

     - The valid range is dependent on the load impedance.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].iq_out_port_common_mode_offset`

    To set/get on all channels, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.iq_out_port_common_mode_offset`
    '''
    iq_out_port_level = _attributes.AttributeViReal64(1150147)
    '''Type: float

    Specifies the amplitude of the generated signal in volts, peak-to-peak (V). For example, if you set this property to 1.0, the output signal ranges from -0.5 volts to 0.5 volts.

    To use this property, you must use the channelName parameter of the _set_attribute_vi_real64 method to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).

    To set this property, the NI-RFSG device must be in the Configuration state.

    Refer to the specifications document for your device for allowable output levels.

    **Units:** Volts, peak-to-peak (V :sub:`pk-pk` )

    **Valid Values:**

    PXIe-5645: 1V :sub:`pk-pk`  maximum if you set the iq_out_port_terminal_configuration property to IQOutPortTerminalConfiguration.DIFFERENTIAL, and 0.5V :sub:`pk-pk`

    maximum if you set the iq_out_port_terminal_configuration property to IQOutPortTerminalConfiguration.SINGLE_ENDED.

    PXIe-5820: 3.4V :sub:`pk-pk` maximum for signal bandwidth less than 160MHz, and 2V :sub:`pk-pk`

    maximum for signal bandwidth greater than 160MHz.

    **Default Value:** 0.5volts

    **Supported Devices:** PXIe-5645, PXIe-5820

    Note: - For the PXIe-5645, this property is ignored if you are using the RF ports.

     - The valid values are only applicable when you set the iq_out_port_load_impedance property to 50 Ω and when you set the iq_out_port_offset property to 0.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].iq_out_port_level`

    To set/get on all channels, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.iq_out_port_level`
    '''
    iq_out_port_load_impedance = _attributes.AttributeViReal64(1150163)
    '''Type: float

    Specifies the load impedance connected to the I/Q OUT port. To set this property, the NI-RFSG device must be in the Configuration state.

    To use this property, you must use the channelName parameter of the _set_attribute_vi_real64 method to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).

    **Units:** Ohms

    **Valid Values:** Any value greater than 0. Values greater than or equal to 1 megaohms (MΩ) are interpreted as high impedance.

    **Default Value:** 50 Ω if you set the iq_out_port_terminal_configuration property to IQOutPortTerminalConfiguration.SINGLE_ENDED, and 100 Ω if you set the iq_out_port_terminal_configuration property to IQOutPortTerminalConfiguration.DIFFERENTIAL.

    **Supported Devices:** PXIe-5645, PXIe-5820

    Note: For the PXIe-5645, this property is ignored if you are using the RF ports.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].iq_out_port_load_impedance`

    To set/get on all channels, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.iq_out_port_load_impedance`
    '''
    iq_out_port_offset = _attributes.AttributeViReal64(1150149)
    '''Type: float

    Specifies the value, in volts, that the signal generator adds to the arbitrary waveform data. To set this property, the NI-RFSG device must be in the Configuration state.

    To use this property, you must use the channelName parameter of the _set_attribute_vi_real64 method to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).

    PXIe-5645: The waveform may be scaled in DSP prior to adding offset and the device state may be changed in order to accommodate the requested offset.

    PXIe-5820: The waveform is not automatically scaled in DSP. To prevent DSP overflows, use the arb_pre_filter_gain property to scale the waveform to provide additional headroom for offsets.

    **Units:** Volts

    **Supported Devices:** PXIe-5645, PXIe-5820

    Note: For the PXIe-5645, this property is ignored if you are using the RF ports.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].iq_out_port_offset`

    To set/get on all channels, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.iq_out_port_offset`
    '''
    iq_out_port_temperature = _attributes.AttributeViReal64(1150161)
    '''Type: float

    Returns the temperature, in degrees Celsius, of the I/Q Out circuitry on the device.

    **Units:** Degrees Celsius

    **Supported Devices:** PXIe-5645, PXIe-5820

    Note: If you query this property during RF list mode, list steps may take longer to complete during list execution.
    '''
    iq_out_port_terminal_configuration = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.IQOutPortTerminalConfiguration, 1150146)
    '''Type: enums.IQOutPortTerminalConfiguration

    Specifies whether to use the I/Q OUT port for differential configuration or single-ended configuration. If you set this property to IQOutPortTerminalConfiguration.SINGLE_ENDED, you must terminate the negative I and Q output connectors with a 50 Ohm termination.

    If you set this property to IQOutPortTerminalConfiguration.SINGLE_ENDED, the positive I and Q connectors generate the resulting waveform. If you set this property to IQOutPortTerminalConfiguration.DIFFERENTIAL, both the positive and negative I and Q connectors generate the resulting waveform.

    To use this property, you must use the channelName parameter of the _set_attribute_vi_int32 method to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** IQOutPortTerminalConfiguration.DIFFERENTIAL

    PXIe-5820: The only valid value for this property is IQOutPortTerminalConfiguration.DIFFERENTIAL.

    **Supported Devices:** PXIe-5645, PXIe-5820

    **Related Topics**

    `Differential and Single-Ended Operation (I/O Interface) <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/differential_single_ended_operation.html>`_

    **Defined Values**:

    +---------------------------------------------+----------------+--------------------------------------------------+
    | Name                                        | Value          | Description                                      |
    +=============================================+================+==================================================+
    | IQOutPortTerminalConfiguration.DIFFERENTIAL | 15000 (0x3a98) | Sets the terminal configuration to differential. |
    +---------------------------------------------+----------------+--------------------------------------------------+
    | IQOutPortTerminalConfiguration.SINGLE_ENDED | 15001 (0x3a99) | Sets the terminal configuration to single-ended. |
    +---------------------------------------------+----------------+--------------------------------------------------+

    Note: For the PXIe-5645, this property is ignored if you are using the RF ports.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].iq_out_port_terminal_configuration`

    To set/get on all channels, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.iq_out_port_terminal_configuration`
    '''
    iq_q_offset = _attributes.AttributeViReal64(1150071)
    '''Type: float

    When using a National Instruments AWG module or VST device, this property specifies the Q-signal DC offset. Units are either percent (%) or volts (V), depending on the iq_offset_units property setting.
    PXIe-5673/5673E: Actual AWG signal offset is equal to the I/Q modulator offset correction plus the value specified by this property. When using an external AWG (non–National Instruments AWG), the iq_q_offset property is read-only and indicates the I/Q modulator Q-offset. Units are volts, as indicated by the iq_offset_units property.
    **Valid Values**: -100% to 100% or -0.2V to 0.2V
    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842
    **Related Topics**
    `Impairment Calibration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/vector_calibration.html>`_
    '''
    iq_rate = _attributes.AttributeViReal64(1250452)
    '''Type: float

    This property specifies the I/Q rate of the arbitrary waveform. The I/Q rate is coerced to a value the hardware can achieve. Read this value back after setting it to see the actual I/Q rate. NI-RFSG internally uses an FIR filter with flat response up to (0.4 × IQ rate). Given a desired signal with the maximum frequency content *f*, sample the signal at an I/Q rate greater than or equal to ( *f*/0.4).

    This property applies only when the generation_mode property is set to GenerationMode.ARB_WAVEFORM or GenerationMode.SCRIPT.

    To set this property, the NI-RFSG device must be in the Configuration state.

    Setting this property to 50 MS/s on the PXI-5670/5671 and PXIe-5672 has the following implications:
    - NI-RFSG is forced to place the carrier frequency at 18 MHz ± 1 MHz to avoid aliasing. This means that NI-RFSG cannot select a carrier frequency that could optimize waveform size if phase continuity is enabled.
    - Output signal bandwidth must be <5 MHz to avoid aliasing.
    - Close-in phase noise is higher.

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_

    `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_—Refer to this topic for more information about using this property to associate an I/Q rate with a waveform.

    `Digital Upconverter <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/duc.html>`_

    **Valid Values**:

    +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Device                                                                   | I/Q Rates                                                                                                                                                                                                                                          |
    +==========================================================================+====================================================================================================================================================================================================================================================+
    | PXIe-5644/5645                                                           | Up to 120 MS/s.                                                                                                                                                                                                                                    |
    +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | PXIe-5646                                                                | Up to 250 MS/s.                                                                                                                                                                                                                                    |
    +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | PXI-5670                                                                 | 50 MS/s ((100 MS/s)/n, where n is divisible by 2 between 12 to 512, and divisible by 4 between 512 to 1,024 (n = 12, 14, 16, ..., 512, 516, 520, ..., 1,024). Setting the I/Q rate to one of these value enables the DUC.)                         |
    +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    |                                                                          | 100 MS/s ((100 MS/s)/n, where n is divisible by 2 between 12 to 512, and divisible by 4 between 512 to 1,024 (n = 12, 14, 16, ..., 512, 516, 520, ..., 1,024). Setting the I/Q rate to one of these value enables the DUC.)                        |
    +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | PXI-5671                                                                 | 50 MS/s ((100 MS/s)/n, where n is divisible by 2 between 12 to 512, and divisible by 4 between 512 to 1,024 (n = 12, 14, 16, ..., 512, 516, 520, ..., 1,024). Setting the I/Q rate to one of these value enables the DUC.)                         |
    +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    |                                                                          | 100 MS/s                                                                                                                                                                                                                                           |
    +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | PXIe-5672                                                                | Up to 100 MS/s.                                                                                                                                                                                                                                    |
    +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | PXIe-5673/5673E                                                          | Up to 200 MS/s. Note that -  If an PXIe-5450 with module revisions A or B is used as part of your PXIe-5673/5673E, the NI-FGEN NIFGEN_ATTR_COMPENSATE_FOR_FILTER_GROUP_DELAY property is disabled if the requested I/Q rate is less than 1.5 MS/s. |
    +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | PXIe-5820/5830/5831/5832/5840/5841/5860                                  | Up to 1.25 GS/s.                                                                                                                                                                                                                                   |
    +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | PXI-5842 (500 MHz, 1 GHz, and 2 GHz bandwidth options)                   | Up to 2.5 GS/s                                                                                                                                                                                                                                     |
    +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    |  PXIe-5842 (4 GHz bandwidth option) using the Standard personality       | Up to 2.5 GS/s                                                                                                                                                                                                                                     |
    +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | PXIe-5842 (4 GHz bandwidth option) using the 4 GHz Bandwidth personality | 5 GS/s only.                                                                                                                                                                                                                                       |
    +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    Note: Use this property to associate an I/Q rate with a waveform.
    '''
    iq_skew = _attributes.AttributeViReal64(1150073)
    '''Type: float

    Specifies the adjustment of the phase angle between the I and Q vectors. If the skew is zero, the phase angle is 90 degrees.

    This property is ignored when the iq_impairment_enabled property is disabled.

    **Units**: degrees (°)

    **Valid Values:**-30° to 30°

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Impairment Calibration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/vector_calibration.html>`_
    '''
    iq_swap_enabled = _attributes.AttributeViBoolean(1250404)
    '''Type: bool

    Enables or disables the inverse phase rotation of the I/Q signal by swapping the I and Q inputs.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** False

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

    **Defined Values**:

    +-------+---------------------------------------------------------------------+
    | Value | Description                                                         |
    +=======+=====================================================================+
    | True  | NI-RFSG device applies noninverse phase rotation of the I/Q signal. |
    +-------+---------------------------------------------------------------------+
    | False | NI-RFSG device applies inverse phase rotation of the I/Q signal.    |
    +-------+---------------------------------------------------------------------+
    '''
    load_configurations_from_file_load_options = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.LoadOptions, 1150290)
    '''Type: enums.LoadOptions

    Specifies the configurations to skip while loading from a file.

    **Default Value:**  NIRFSG_VAL_SKIP_NONE

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +--------------------------------------------------------------------+-------------------------------------------------------------------+
    | Value                                                              | Description                                                       |
    +====================================================================+===================================================================+
    | RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_LOAD_OPTIONS_SKIP_NONE      | NI-RFSG loads all the configurations to the session.              |
    +--------------------------------------------------------------------+-------------------------------------------------------------------+
    | RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_LOAD_OPTIONS_SKIP_WAVEFORMS | NI-RFSG skips loading the waveform configurations to the session. |
    +--------------------------------------------------------------------+-------------------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    load_configurations_from_file_reset_options = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.LoadConfigurationResetOptions, 1150291)
    '''Type: enums.LoadConfigurationResetOptions

    Specifies the configurations to skip to reset while loading configurations from a file.

    **Default Value:**  NIRFSG_VAL_SKIP_NONE
    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +------------------------------------------------------------------------------+------------------------------------------------------+
    | Value                                                                        | Description                                          |
    +==============================================================================+======================================================+
    | RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_NONE               | NI-RFSG resets all configurations.                   |
    +------------------------------------------------------------------------------+------------------------------------------------------+
    | RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_WAVEFORMS          | NI-RFSG skips resetting the waveform configurations. |
    +------------------------------------------------------------------------------+------------------------------------------------------+
    | RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_SCRIPTS            | NI-RFSG skips resetting the scripts.                 |
    +------------------------------------------------------------------------------+------------------------------------------------------+
    | RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_DEEMBEDDING_TABLES | NI-RFSG skips resetting the de-embedding tables.     |
    +------------------------------------------------------------------------------+------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    logical_name = _attributes.AttributeViString(1050305)
    '''Type: str

    Returns a string that contains the logical name you specified when opening the current IVI session. You can pass a logical name to the Init method or the __init__ method. The IVI Configuration Utility must contain an entry for the logical name. The logical name entry refers to a driver session section in the IVI Configuration file. The driver session section specifies a physical device and initial user options.

    **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    loop_bandwidth = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.LoopBandwidth, 1150027)
    '''Type: enums.LoopBandwidth

    Configures the loop bandwidth of the tuning PLLs. This property is ignored on the PXI-5610, PXI-5670/5671, and PXIe-5672 for signal bandwidths greater than or equal to 10MHz. This property is ignored on the PXI/PXIe-5650/5651/5652 for RF frequencies less than 50MHz.

    To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the _set_attribute_vi_int32 method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

    **Default Value:**

    PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842: LoopBandwidth.MEDIUM

    PXI/PXIe-5650/5651/5652, PXIe-5673/5673E: LoopBandwidth.NARROW

    **Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Phase-Locked Loop Bandwidth <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phased_lock_loop_bandwidth.html>`_

    `Modulation Implementation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5650_5651_5652_modulation_implementation.html>`_

    `Sinusoidal Tone Versus Modulation Operation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/sinusoidal_tone_versus_modulation_implementation.html>`_

    **Defined Values**:

    +----------------------+---------+--------------------------------------------------------+
    | Name                 | Value   | Description                                            |
    +======================+=========+========================================================+
    | LoopBandwidth.MEDIUM | 1 (0x1) | Uses the medium loop bandwidth setting for the PLL.    |
    +----------------------+---------+--------------------------------------------------------+
    | LoopBandwidth.NARROW | 0 (0x0) | Uses the narrowest loop bandwidth setting for the PLL. |
    +----------------------+---------+--------------------------------------------------------+
    | LoopBandwidth.WIDE   | 2 (0x2) | Uses the widest loop bandwidth setting for the PLL.    |
    +----------------------+---------+--------------------------------------------------------+

    Note: Setting this property to LoopBandwidth.WIDE on the PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, or the PXIe-5673/5673E allows the frequency to settle significantly faster at the expense of increased phase noise. Setting this property to LoopBandwidth.MEDIUM is not a valid option on the PXI/PXIe-5650/5651/5652 or PXIe-5673/5673E. LoopBandwidth.MEDIUM is the only supported value for the PXIe-5840/5841/5842.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

    Tip:
    This property can be set/get on specific los within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container los to specify a subset.

    Example: :py:attr:`my_session.los[ ... ].loop_bandwidth`

    To set/get on all los, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.loop_bandwidth`
    '''
    lo_frequency = _attributes.AttributeViReal64(1150199)
    '''Type: float

    Specifies the frequency of the LO source.

    To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the _set_attribute_vi_real64 method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

    **Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842

    **Related Topics**

    `PXIe-5830 Frequency and Bandwidth Configuration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_configuration.html>`_

    `PXIe-5831/5832 Frequency and Bandwidth Configuration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_configuration.html>`_

    Note: This property is read/write if you are using an external LO. Otherwise, this property is read-only.

    Tip:
    This property can be set/get on specific los within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container los to specify a subset.

    Example: :py:attr:`my_session.los[ ... ].lo_frequency`

    To set/get on all los, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.lo_frequency`
    '''
    lo_frequency_step_size = _attributes.AttributeViReal64(1150151)
    '''Type: float

    Specifies the step size for tuning the local oscillator (LO) phase-locked loop (PLL).

    When the lo_pll_fractional_mode_enabled property is enabled, the specified step size affects the fractional spur performance of the device. When the lo_pll_fractional_mode_enabled property is disabled, the specified step size affects the phase noise performance of the device.

    The valid values for this property depend on the lo_pll_fractional_mode_enabled property.

    **PXIe-5644/5645/5646**—If you disable the lo_pll_fractional_mode_enabled property, the specified value is coerced to the nearest valid value.

    **PXIe-5840/5841**—If you disable the lo_pll_fractional_mode_enabled property, the specified value is coerced to the nearest valid value that is less than or equal to the desired step size.

    **Units:** hertz (Hz)

    **Default Values:**

    PXIe-5644/5645/5646: 200kHz

    PXIe-5830: 2MHz

    PXIe-5831/5832 (RF port): 8MHz

    PXIe-5831/5832 (IF port): 2MHz, 4MHz

    PXIe-5840/5841:

    - Fractional mode: 500 kHz
    - Integer mode: 10 MHz for frequencies less than or equal to 4 GHz. 20 MHz for frequencies greater than 4 GHz.

    PXIe-5841 with PXIe-5655: 500kHz

    PXIe-5842: 1Hz

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

    +--------------------------------------------------------------------------------------------------+-------------------+--------------------------------------------------+
    | lo_pll_fractional_mode_enabled Property Setting                                                  | NIRFSG_VAL_ENABLE | NIRFSG_VAL_DISABLE                               |
    +==================================================================================================+===================+==================================================+
    | lo_frequency_step_size Property Valid Values on PXIe-5644/5645                                   | 50 kHz to 24 MHz  | 4 MHz, 5 MHz, 6 MHz, 12 MHz, or 24 MHz           |
    +--------------------------------------------------------------------------------------------------+-------------------+--------------------------------------------------+
    | lo_frequency_step_size Property Valid Values on PXIe-5646                                        | 50 kHz to 25 MHz  | 2 MHz, 5 MHz, 10 MHz, or 25 MHz                  |
    +--------------------------------------------------------------------------------------------------+-------------------+--------------------------------------------------+
    | lo_frequency_step_size Property Valid Values on PXIe-5840/5841                                   | 50 kHz to 100 MHz | 1 MHz, 5 MHz, 10 MHz, 25 MHz, 50 MHz, or 100 MHz |
    +--------------------------------------------------------------------------------------------------+-------------------+--------------------------------------------------+
    | lo_frequency_step_size Property Valid Values on PXIe-5830/5831/ 5832 LO1                         | 8 Hz to 400 MHz   | —                                                |
    +--------------------------------------------------------------------------------------------------+-------------------+--------------------------------------------------+
    | lo_frequency_step_size Property Valid Values on PXIe-5830/5831/ 5832 LO2                         | 4 Hz to 400 MHz   | —                                                |
    +--------------------------------------------------------------------------------------------------+-------------------+--------------------------------------------------+
    | lo_frequency_step_size Property Valid Values on PXIe-5841 with PXIe-5655/NI PXIe-5842 (See note) | 1 nHz to 100 MHz  | 1 nHz to 50 MHz                                  |
    +--------------------------------------------------------------------------------------------------+-------------------+--------------------------------------------------+

    Note: Values up to 100 MHz are coerced to 50 MHz.
    '''
    lo_in_power = _attributes.AttributeViReal64(1150067)
    '''Type: float

    Specifies the power level of the signal at the LO IN front panel connector.

    To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the _set_attribute_vi_real64 method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

    **Units**: dBm

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842

    **Related Topics**

    `LO OUT <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/loout.html>`_

    Note: - This property is read/write if you are using an external LO. Otherwise, this property is read-only.

     - For the PXIe-5644/5645/5646, this property is always read-only.

    Tip:
    This property can be set/get on specific los within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container los to specify a subset.

    Example: :py:attr:`my_session.los[ ... ].lo_in_power`

    To set/get on all los, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.lo_in_power`
    '''
    lo_out_enabled = _attributes.AttributeViBoolean(1150013)
    '''Type: bool

    Specifies whether the local oscillator signal is present at the LO OUT front panel connector. The local oscillator signal remains at the LO OUT front panel connector until this property is set to False, even if the output_enabled property is set to False, the abort method is called, or the NI-RFSG session is closed.

    To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the _set_attribute_vi_boolean method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

    **Default Value:** NIRFSG_VAL_DISABLE

    **Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842

    **Related Topics**

    `LO OUT <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/loout.html>`_

    **Defined Values**:

    +--------------------+---------------------------------------------------------------------------------+
    | Name               | Description                                                                     |
    +====================+=================================================================================+
    | NIRFSG_VAL_ENABLE  | The local oscillator signal is present at the LO OUT front panel connector.     |
    +--------------------+---------------------------------------------------------------------------------+
    | NIRFSG_VAL_DISABLE | The local oscillator signal is not present at the LO OUT front panel connector. |
    +--------------------+---------------------------------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

    Tip:
    This property can be set/get on specific los within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container los to specify a subset.

    Example: :py:attr:`my_session.los[ ... ].lo_out_enabled`

    To set/get on all los, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.lo_out_enabled`
    '''
    lo_out_export_configure_from_rfsa = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.LoOutExportConfigureFromRfsaEnable, 1150242)
    '''Type: enums.LoOutExportConfigureFromRfsaEnable

    Specifies whether to allow NI-RFSA to control the NI-RFSG LO out export.

    Set this property to LoOutExportConfigureFromRfsaEnable.ENABLE to allow NI-RFSA to control the LO out export. Use the RF OUT LO EXPORT ENABLED property to control the LO out export from NI-RFSA.

    **Default Value:** LoOutExportConfigureFromRfsaEnable.DISABLE

    **Supported Devices**: PXIe-5840/5841/5842

    **Defined Values**:

    +--------------------------------------------+---------+----------------------------------------------------------------------+
    | Name                                       | Value   | Description                                                          |
    +============================================+=========+======================================================================+
    | LoOutExportConfigureFromRfsaEnable.ENABLE  | 0 (0x0) | Do not allow NI-RFSA to control the NI-RFSG local oscillator export. |
    +--------------------------------------------+---------+----------------------------------------------------------------------+
    | LoOutExportConfigureFromRfsaEnable.DISABLE | 1 (0x1) | Allow NI-RFSA to control the NI-RFSG local oscillator export.        |
    +--------------------------------------------+---------+----------------------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    lo_out_power = _attributes.AttributeViReal64(1150066)
    '''Type: float

    Specifies the power level of the signal at the LO OUT front panel connector.

    To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the _set_attribute_vi_real64 method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

    **Units**: dBm

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842

    **Related Topics**

    `LO OUT <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/loout.html>`_

    Note: For the PXIe-5644/5645/5646 and PXIe-5673/5673E, this property is always read-only.

    Tip:
    This property can be set/get on specific los within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container los to specify a subset.

    Example: :py:attr:`my_session.los[ ... ].lo_out_power`

    To set/get on all los, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.lo_out_power`
    '''
    lo_pll_fractional_mode_enabled = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.LoPllFractionalModeEnabled, 1150152)
    '''Type: enums.LoPllFractionalModeEnabled

    Specifies whether to use fractional mode for the local oscillator (LO) phase-locked loop (PLL). This property enables or disables fractional frequency tuning in the LO. Fractional mode provides a finer frequency step resolution and allows smaller values for the lo_frequency_step_size property. However, fractional mode may introduce non-harmonic spurs.

    This property applies only if you set the lo_source property to Onboard.

    To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the _set_attribute_vi_int32 method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" .

    **Default Value:** LoPllFractionalModeEnabled.ENABLE

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

    **Related Topics**

    Refer to the local oscillators topic appropriate to your device for more information about using fractional mode.

    **Defined Values**:

    +------------------------------------+---------+------------------------------------------+
    | Name                               | Value   | Description                              |
    +====================================+=========+==========================================+
    | LoPllFractionalModeEnabled.ENABLE  | 0 (0x0) | Disables fractional mode for the LO PLL. |
    +------------------------------------+---------+------------------------------------------+
    | LoPllFractionalModeEnabled.DISABLE | 1 (0x1) | Enables fractional mode for the LO PLL.  |
    +------------------------------------+---------+------------------------------------------+

    Note: For the PXIe-5841 with PXIe-5655, this property is ignored if the PXIe-5655 is used as the LO source.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

    Tip:
    This property can be set/get on specific los within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container los to specify a subset.

    Example: :py:attr:`my_session.los[ ... ].lo_pll_fractional_mode_enabled`

    To set/get on all los, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.lo_pll_fractional_mode_enabled`
    '''
    lo_source = _attributes.AttributeEnum(_attributes.AttributeViString, enums.LoSource, 1150150)
    '''Type: enums.LoSource

    Specifies whether to use the internal or external local oscillator (LO) source. If the lo_source property is set to "" (empty string), NI-RFSG uses the internal LO source. To set this property, the NI-RFSG device must be in the Configuration state.

    To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the _set_attribute_vi_string method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

    **Default Value:** Onboard

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

    **Related Topics**

    `PXIe-5830 LO Sharing Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/lo_sharing_using_rfsa_rfsg.html>`_

    `PXIe-5831/5832 LO Sharing Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/lo_sharing_using_rfsa_rfsg.html>`_

    **Possible Values**:

    +--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Possible Value           | Description                                                                                                                                                                                                                                                      |
    +==========================+==================================================================================================================================================================================================================================================================+
    | "Automatic_SG_SA_Shared" | NI-RFSG internally makes the configuration to share the LO between NI-RFSA and NI-RFSG. This value is valid only on the PXIe-5820/5830/5831/5832/5840/5841/5842.                                                                                                 |
    +--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | "LO_In"                  | Uses an external LO as the LO source. Connect a signal to the LO IN connector on the device and use the upconverter_center_frequency property to specify the LO frequency.                                                                                       |
    +--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | "Onboard"                | Uses an internal LO as the LO source. If you specify an internal LO source, the LO is generated inside the device itself.                                                                                                                                        |
    +--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | "SG_SA_Shared"           | Uses the same internal LO during NI-RFSA and NI-RFSG sessions. NI-RFSG selects an internal synthesizer and the synthesizer signal is switched to both the RF In and RF Out mixers. This value is valid only on the PXIe-5830/5831/5832/5841 with PXIe-5655/5842. |
    +--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | "Secondary"              | Uses the PXIe-5831/5840 internal LO as the LO source. This value is valid only on the PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653.                                                                                                                     |
    +--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    Note: For the PXIe-5841 with PXIe-5655, RF list mode is not supported when this property is set to SG_SA_Shared.

    Tip:
    This property can be set/get on specific los within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container los to specify a subset.

    Example: :py:attr:`my_session.los[ ... ].lo_source`

    To set/get on all los, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.lo_source`
    '''
    lo_temperature = _attributes.AttributeViReal64(1150075)
    '''Type: float

    Returns the LO module temperature in degrees Celsius.

    PXIe-5840/5841: If you query this property during RF list mode, list steps may take longer to complete during list execution.

    **Units**: degrees Celsius (°C)

    **Supported Devices:** PXIe-5673/5673E, PXIe-5840/5841/5842
    '''
    lo_vco_frequency_step_size = _attributes.AttributeViReal64(1150257)
    '''Type: float

    Specifies the step size for tuning the internal voltage-controlled oscillator (VCO) used to generate the LO signal.

    **Valid Values**:

    LO1: 1 Hz to 50 MHz

    LO2: 1 Hz to 100 MHz

    **Default Value**: 1 MHz

    **Supported Devices**: PXIe-5830/5831/5832
    '''
    marker_event_output_behavior = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.MarkerEventOutputBehavior, 1150206)
    '''Type: enums.MarkerEventOutputBehavior

    Specifies the output behavior for the Marker Event. To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** MarkerEventOutputBehavior.PULSE

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_

    **Defined Values**:

    +----------------------------------+----------------+-------------------------------------------------------+
    | Name                             | Value          | Description                                           |
    +==================================+================+=======================================================+
    | MarkerEventOutputBehavior.PULSE  | 23000 (0x59d8) | Specifies the Marker Event output behavior as pulse.  |
    +----------------------------------+----------------+-------------------------------------------------------+
    | MarkerEventOutputBehavior.TOGGLE | 23001 (0x59d9) | Specifies the Marker Event output behavior as toggle. |
    +----------------------------------+----------------+-------------------------------------------------------+

    Tip:
    This property can be set/get on specific markers within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container markers to specify a subset.

    Example: :py:attr:`my_session.markers[ ... ].marker_event_output_behavior`

    To set/get on all markers, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.marker_event_output_behavior`
    '''
    marker_event_pulse_width = _attributes.AttributeViReal64(1150207)
    '''Type: float

    Specifies the pulse width value for the Marker Event. Use the marker_event_pulse_width_units property to set the units for the pulse width value. This property is valid only when the marker_event_output_behavior property is set to MarkerEventOutputBehavior.PULSE.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** 200 ns

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_

    Tip:
    This property can be set/get on specific markers within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container markers to specify a subset.

    Example: :py:attr:`my_session.markers[ ... ].marker_event_pulse_width`

    To set/get on all markers, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.marker_event_pulse_width`
    '''
    marker_event_pulse_width_units = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.MarkerEventPulseWidthUnits, 1150208)
    '''Type: enums.MarkerEventPulseWidthUnits

    Specifies the pulse width units for the Marker Event. This property is valid only when the marker_event_output_behavior property is set to MarkerEventOutputBehavior.PULSE.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** MarkerEventPulseWidthUnits.SECONDS

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_

    **Defined Values**:

    +----------------------------------+----------------+-------------------------------------------------------+
    | Name                             | Value          | Description                                           |
    +==================================+================+=======================================================+
    | MarkerEventOutputBehavior.PULSE  | 23000 (0x59d8) | Specifies the Marker Event output behavior as pulse.  |
    +----------------------------------+----------------+-------------------------------------------------------+
    | MarkerEventOutputBehavior.TOGGLE | 23001 (0x59d9) | Specifies the Marker Event output behavior as toggle. |
    +----------------------------------+----------------+-------------------------------------------------------+

    Tip:
    This property can be set/get on specific markers within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container markers to specify a subset.

    Example: :py:attr:`my_session.markers[ ... ].marker_event_pulse_width_units`

    To set/get on all markers, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.marker_event_pulse_width_units`
    '''
    marker_event_terminal_name = _attributes.AttributeViString(1150115)
    '''Type: str

    Returns the name of the fully qualified signal name as a string.

    **Default Values**:

    PXI-5670/5671, PXIe-5672/5673/5673E: /*AWGName*/Marker *X* Event, where *AWGName* is the name of your associated AWG module in MAX and *X* is Marker Event 0 through 3.

    PXIe-5830/5831/5832: /*BasebandModule*/ao/0/Marker *X* Event, where *BasebandModule* is the name of the baseband module of your device in MAX and *X* is Marker Event 0 through 3.

    PXIe-5820/5840/5841: /*ModuleName*/ao/0/Marker *X* Event, where *ModuleName* is the name of your device in MAX and *X* is Marker Event 0 through 3.

    **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

    `Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_

    **High-Level Methods**:

    - get_terminal_name

    Tip:
    This property can be set/get on specific markers within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container markers to specify a subset.

    Example: :py:attr:`my_session.markers[ ... ].marker_event_terminal_name`

    To set/get on all markers, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.marker_event_terminal_name`
    '''
    marker_event_toggle_initial_state = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.MarkerEventToggleInitialState, 1150209)
    '''Type: enums.MarkerEventToggleInitialState

    Specifies the initial state for the Marker Event when the marker_event_output_behavior property is set to MarkerEventOutputBehavior.TOGGLE.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** MarkerEventToggleInitialState.LOW

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_

    **Defined Values**:

    +------------------------------------+----------------+----------------------------------------------------------------------------------+
    | Name                               | Value          | Description                                                                      |
    +====================================+================+==================================================================================+
    | MarkerEventToggleInitialState.HIGH | 21001 (0x5209) | Specifies the initial state of the Marker Event toggle behavior as digital high. |
    +------------------------------------+----------------+----------------------------------------------------------------------------------+
    | MarkerEventToggleInitialState.LOW  | 21000 (0x5208) | Specifies the initial state of the Marker Event toggle behavior as digital low.  |
    +------------------------------------+----------------+----------------------------------------------------------------------------------+

    Tip:
    This property can be set/get on specific markers within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container markers to specify a subset.

    Example: :py:attr:`my_session.markers[ ... ].marker_event_toggle_initial_state`

    To set/get on all markers, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.marker_event_toggle_initial_state`
    '''
    memory_size = _attributes.AttributeViInt64(1150061)
    '''Type: int

    The total amount of memory on the signal generator in bytes.

    **Units:** bytes

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Memory Options <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/memory_options.html>`_

    `Phase Continuity <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phasecontinuity.html>`_

    Note: Not all onboard memory is available for waveform storage. A portion of onboard memory stores scripts that specify how the waveforms are generated. These scripts typically require less than 1KB of onboard memory.
    '''
    module_power_consumption = _attributes.AttributeViReal64(1150210)
    '''Type: float

    Returns the total power consumption of the device.

    **Units:** watts

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    Note: If you query this property during RF list mode, list steps may take longer to complete during list execution.
    '''
    module_revision = _attributes.AttributeViString(1150084)
    '''Type: str

    Returns the module revision letter. If the NI-RFSG session is controlling multiple modules, this property returns the revision letter of the primary RF module. The NI-RFSG session is opened using the primary RF device name.

    **Supported Devices:** PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Identifying Module Revision <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/identifying_device_revision.html>`_
    '''
    output_enabled = _attributes.AttributeViBoolean(1250004)
    '''Type: bool

    Specifies whether signal output is enabled. Setting the output_enabled property to False while in the Generation state stops signal output, although generation continues internally. For the PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653, PXI-5670/5671, and PXIe-5672/5673/5673E, setting the output_enabled property while in the Committed state does not transition the device to the Configuration state, but output changes immediately.

    **Default Value:** True

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Output Enabled <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/outputenable.html>`_

    `NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_

    **Defined Values**:

    +-------+-------------------------+
    | Value | Description             |
    +=======+=========================+
    | True  | Enables signal output.  |
    +-------+-------------------------+
    | False | Disables signal output. |
    +-------+-------------------------+

    Note: - For the PXIe-5653, this property controls only the LO1 terminal.

     - For the PXIe-5645, this property is ignored if you are using the I/Q ports.

     - When the ACTIVE_CONFIGURATION_LIST property is set to a valid list name, setting the output_enabled property transitions the device to the Configuration state.

    Note:
    One or more of the referenced properties are not in the Python API for this driver.
    '''
    output_port = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.OutputPort, 1150144)
    '''Type: enums.OutputPort

    Specifies the connector(s) to use to generate the signal. To set this property, the NI-RFSG device must be in the Configuration state.

    You must write complex I and Q data for all options. The Q data has no effect if you set this property to I Only and set the iq_out_port_carrier_frequency property to 0. If you set the iq_out_port_carrier_frequency property to a value other than 0, the onboard signal processing (OSP) frequency shifts I and Q as a complex value and outputs the real portion of the result on the I connector(s) of the device.

    If you set the output_port property to OutputPort.I_ONLY or OutputPort.IQ_OUT, the iq_out_port_terminal_configuration property applies.

    **Default Value:**

    PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860: OutputPort.RF_OUT

    PXIe-5820: OutputPort.IQ_OUT

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +--------------------+----------------+------------------------------------------------------------------------------------------+
    | Name               | Value          | Description                                                                              |
    +====================+================+==========================================================================================+
    | OutputPort.CAL_OUT | 14002 (0x36b2) | Enables the CAL OUT port.                                                                |
    +--------------------+----------------+------------------------------------------------------------------------------------------+
    | OutputPort.I_ONLY  | 14003 (0x36b3) | Enables the I connectors of the I/Q OUT port. This value is valid on only the PXIe-5645. |
    +--------------------+----------------+------------------------------------------------------------------------------------------+
    | OutputPort.IQ_OUT  | 14001 (0x36b1) | Enables the I/Q OUT port. This value is valid on only the PXIe-5645 and PXIe-5820.       |
    +--------------------+----------------+------------------------------------------------------------------------------------------+
    | OutputPort.RF_OUT  | 14000 (0x36b0) | Enables the RF OUT port. This value is not valid for the PXIe-5820.                      |
    +--------------------+----------------+------------------------------------------------------------------------------------------+
    '''
    overflow_error_reporting = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.OverflowErrorReporting, 1150228)
    '''Type: enums.OverflowErrorReporting

    Configures error reporting for onboard signal processing (OSP) overflows. Overflows lead to clipping of the waveform.

    **Default Value:** OverflowErrorReporting.WARNING

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +---------------------------------+--------------+----------------------------------------------------------------------------+
    | Name                            | Value        | Description                                                                |
    +=================================+==============+============================================================================+
    | OverflowErrorReporting.DISABLED | 1302 (0x516) | NI-RFSG does not return an error or a warning when an OSP overflow occurs. |
    +---------------------------------+--------------+----------------------------------------------------------------------------+
    | OverflowErrorReporting.WARNING  | 1301 (0x515) | NI-RFSG returns a warning when an OSP overflow occurs.                     |
    +---------------------------------+--------------+----------------------------------------------------------------------------+
    '''
    peak_envelope_power = _attributes.AttributeViReal64(1150011)
    '''Type: float

    Returns the maximum instantaneous power of the RF output signal.

    **Units**: dBm

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    Note: - This property is valid only when the power_level_type property is set to PowerLevelType.AVERAGE.

     - The arb_digital_gain property is not included in the calculation of the peak_envelope_power property.
    '''
    peak_power_adjustment = _attributes.AttributeViReal64(1150132)
    '''Type: float

    Specifies the adjustment for the power_level property. This property is valid only when you set the power_level_type property to PowerLevelType.PEAK. The value of the peak_power_adjustment property adds to the power_level property. The peak_power_adjustment property typically specifies the peak-to-average power ratio (PAPR) of a waveform. If the PAPR is specified, the specified power level becomes the average power level of the waveform, even if the power_level_type property is set to PowerLevelType.PEAK.

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_—Refer to this topic for more information about using this property to associate a peak power adjustment with a waveform.

    Note: - For the PXIe-5673/5673E only, use this property to associate a peak power adjustment with a waveform.

     - For the PXIe-5645, this property is ignored if you are using the I/Q ports.
    '''
    phase_continuity_enabled = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.PhaseContinuityEnabled, 1150005)
    '''Type: enums.PhaseContinuityEnabled

    Specifies whether the driver maintains phase continuity in the arbitrary waveforms. When this property is set to PhaseContinuityEnabled.ENABLE, NI-RFSG may increase the waveform size. To set the phase_continuity_enabled property, the NI-RFSG device must be in the Configuration state. phase_continuity_enabled applies only when the generation_mode property is set to GenerationMode.ARB_WAVEFORM or GenerationMode.SCRIPT.

    PXI-5671: When using the PXI-5671 with I/Q rates less than or equal to 8.33MS/s, an input phase-continuous signal is always phase-continuous upon output, and this property has no effect.

    PXIe-5644/5645/5646, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: Phase continuity is *always* enabled on this device.

    **Default Value:** PhaseContinuityEnabled.AUTO

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Phase Continuity <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phasecontinuity.html>`_

    `Arb Waveform Mode Tuning Speed Factors <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5670_arb_waveform_mode_tuning_speed_factors.html>`_

    **Defined Values**:

    +-------------------------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | phase_continuity_enabled Property Setting | Value     | With I/Q Rates > 8.33 MS/s.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
    +===========================================+===========+==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
    | PhaseContinuityEnabled.AUTO               | -1 (-0x1) | When the Generation Mode property is set to Arb Waveform, the arbitrary waveform may be repeated to ensure phase continuity after upconversion. This setting could cause waveform size to increase. When the Generation Mode property is set to Script, the Phase Continuity Enabled property indicates a warning condition. NI-RFSG cannot guarantee a phase-continuous output signal in Script mode. Phase continuity is automatically disabled in script mode, and the arbitrary waveform plays back without regard to any possible phase discontinuities introduced by upconversion. |
    +-------------------------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | PhaseContinuityEnabled.DISABLE            | 0 (0x0)   | When the Generation Mode property is set to Arb Waveform, the arbitrary waveform is played back without regard to any possible phase discontinuities introduced by upconversion. The time duration of the original waveform is maintained. When the Generation Mode property is set to Script, the arbitrary waveform plays back without regard to any possible phase discontinuities introduced by upconversion. The time duration of the original waveform is maintained.                                                                                                              |
    +-------------------------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | PhaseContinuityEnabled.ENABLE             | 1 (0x1)   | When the Generation Mode property is set to Arb Waveform, the arbitrary waveform may be repeated to ensure phase continuity after upconversion. Enabling this property could cause waveform size to increase. When the Generation Mode property is set to Script, the arbitrary waveform plays back without regard to any possible phase discontinuities introduced by upconversion. The time duration of the original waveform is maintained.                                                                                                                                           |
    +-------------------------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    phase_offset = _attributes.AttributeViReal64(1150024)
    '''Type: float

    Specifies the phase of the RF output signal. Use this property to align the phase of the RF output with the phase of the RF output of another device, as long as the two devices are phase-coherent.

    **Units**: degrees (°)

    **Default Value:** 0

    **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Phase Synchronization and Phase Coherency <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phase_synchronization_and_phase_coherency.html>`_
    '''
    power_level = _attributes.AttributeViReal64(1250002)
    '''Type: float

    Specifies either the average power level or peak power level of the generated RF signal, depending on the power_level_type property setting.

    The PXI-5670/5671, PXIe-5672, and PXIe-5860 must be in the Configuration state to use this property. However, the PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXIe-5673/5673E and PXIe-5830/5831/5832/5840/5841/5842 can be in the Configuration or the Generation state to use this property.

    Refer to the specifications document for your device for allowable power level settings.

    **Units**: dBm

    **Default Values:**

    PXIe-5644/5645/5646, PXIe-5673/5673E: -100

    PXI/PXIe-5650/5651/5652: -90

    PXIe-5654: -7

    PXIe-5654 with PXIe-5696: -110

    PXI-5670/5671, PXIe-5672: -145

    PXIe-5830/5831/5832/5840/5841/5842/5860: -174

    **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860
    **High-Level Methods**:

    - ConfigureRf

    Note: - For the PXIe-5653, this property is read-only.

     - For the PXIe-5645, this property is ignored if you are using the I/Q ports.
    '''
    power_level_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.PowerLevelType, 1150043)
    '''Type: enums.PowerLevelType

    Specifies how NI-RFSG interprets the value of the power_level property. The power_level_type property also affects how waveforms are scaled.

    PXI-5670/5671: While in Script generation mode, if this property is set to PowerLevelType.AVERAGE, NI-RFSG scales each waveform so that all waveforms have the same average power. The average power level of each waveform matches the value set with the power_level property. You can disable this scaling operation by setting the power_level_type property to PowerLevelType.PEAK.

    PXIe-5644/5645/5646, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: While in Script generation mode, this property must be set to PowerLevelType.PEAK.

    Converting from Average Power to Peak Power

    Typically, this property is set to PowerLevelType.AVERAGE. However, some instrument modes require this property to be set to PowerLevelType.PEAK. Use the following equations to calculate the equivalent peak power given the desired average power for your waveform:

    Where 1 is the highest possible magnitude in the waveform.

    **Default Value:**

    PXIe-5820: PowerLevelType.PEAK

    All other devices: PowerLevelType.AVERAGE

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Spurious Performance <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/spurious_performance.html>`_

    `Optimizing for Low Power Generation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/optimizing_for_low_power_generation.html>`_

    **Defined Values**:

    +------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Value                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
    +========================+====================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
    | PowerLevelType.AVERAGE | Indicates the desired power averaged in time. The driver maximizes the dynamic range by scaling the I/Q waveform so that its peak magnitude is equal to one. If your write more than one waveform, NI-RFSG scales each waveform without preserving the power level ratio between the waveforms. This value is not valid for the PXIe-5820.                                                                                                                                                                                                                                                                                                                                                                                                                         |
    +------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | PowerLevelType.PEAK    | Indicates the maximum power level of the RF signal averaged over one period of the RF carrier frequency (the peak envelope power). This setting requires that the magnitude of the I/Q waveform must always be less than or equal to one. When using peak power, the power level of the RF signal matches the specified power level at moments when the magnitude of the I/Q waveform equals one. If you write more than one waveform, the relative scaling between waveforms is preserved. In peak power mode, waveforms are scaled according to the arb_waveform_software_scaling_factor property. You can use the peak_power_adjustment property in conjunction with the power_level property when the power_level_type property is set to PowerLevelType.PEAK. |
    +------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    '''
    pulse_modulation_active_level = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ScriptTriggerDigitalLevelActiveLevel, 1150307)
    '''Type: enums.ScriptTriggerDigitalLevelActiveLevel

    Specifies the active level of the pulse modulation signal when pulse modulation is enabled. To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** ScriptTriggerDigitalLevelActiveLevel.HIGH

    **Supported Devices:**  PXIe-5842

    **Defined Values**:

    +-------------------------------------------+---------------+--------------------------------------------------+
    | Name                                      | Value         | Description                                      |
    +===========================================+===============+==================================================+
    | ScriptTriggerDigitalLevelActiveLevel.HIGH | 9000 (0x2328) | Trigger when the digital trigger signal is high. |
    +-------------------------------------------+---------------+--------------------------------------------------+
    | ScriptTriggerDigitalLevelActiveLevel.LOW  | 9001 (0x2329) | Trigger when the digital trigger signal is low.  |
    +-------------------------------------------+---------------+--------------------------------------------------+
    '''
    pulse_modulation_enabled = _attributes.AttributeViBoolean(1250051)
    '''Type: bool

    Enables or disables pulse modulation.

    PXIe-5654/5654 with PXIe-5696: If this property is enabled and the signal at the PULSEIN front panel connector is high, the device generates a signal. If the signal is low, output generation is disabled.

    PXIe-5673/5673E: If this property is enabled and the signal at the PLSMOD front panel connector is high, the device generates a signal. If the signal is low, output generation is disabled.

    PXIe-5842: If this property is enabled and the signal at the PULSE IN front panel connector is high, the device generates a signal. If the signal is low, output generation is disabled. This behavior can be modified by setting pulse modulation active level.

    **Default Value:** False

    **Supported Devices:** PXIe-5654/5654 with PXIe-5696, PXIe-5673/5673E

    **Related Topics**

    `Pulse Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/pulse_modulation.html>`_

    **Defined Values**:

    +-------+----------------------------+
    | Value | Description                |
    +=======+============================+
    | True  | Enables pulse modulation.  |
    +-------+----------------------------+
    | False | Disables pulse modulation. |
    +-------+----------------------------+
    '''
    pulse_modulation_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.PulseModulationMode, 1150190)
    '''Type: enums.PulseModulationMode

    PXIe-5654/5654 with PXIe-5696: Specifies the pulse modulation mode to use.

    PXIe-5842: This property allows you to choose a tradeoff between switching speed and On/Off Ratio when using pulse modulation. Refer to the product specifications document for the switching characteristics of each mode. This property is settable while the device is generating, but some output pulses may be dropped.

    **Default Value:** PulseModulationMode.ANALOG

    **Supported Devices:** PXIe-5842/5654/5654 with PXIe-5696

    **Defined Values**:

    +---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
    | Value                                             | Description                                                                                                                                 |
    +===================================================+=============================================================================================================================================+
    | PulseModulationMode.OPTIMAL_MATCH                 | Provides for a more optimal power output match for the device during the off cycle of the pulse mode operation. Not supported on PXIe-5842. |
    +---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
    | NIRFSG_VAL_PULSE_MODULATION_ANALOG_HIGH_ISOLATION | Allows for the best on/off power ratio of the pulsed signal.                                                                                |
    +---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
    | NIRFSG_VAL_PULSE_MODULATION_ANALOG                | Analog switch blanking. Balance between switching speed and on/off power ratio of the pulsed signal.                                        |
    +---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
    | NIRFSG_VAL_PULSE_MODULATION_DIGITAL               | Digital only modulation. Provides the best on/off switching speed of the pulsed signal at the cost of signal isolation.                     |
    +---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    pulse_modulation_source = _attributes.AttributeEnum(_attributes.AttributeViString, enums.PulseModulationSource, 1150308)
    '''Type: enums.PulseModulationSource

    Specifies the source of the pulse modulation signal. When Pulse In in used, the pulse modulation is applied with the lowest latency and jitter, but is not aligned to any particular waveform sample. When a marker is used, the RF pulse is aligned to a specific sample in the arbitrary waveform. To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** PulseIn

    **Supported Devices:**  PXIe-5842

     **Possible Values**:

    +----------------+----------------------------------------------------------------------------------------------+
    | Possible Value | Description                                                                                  |
    +================+==============================================================================================+
    | "PulseIn"      | The trigger is received on the PULSE IN terminal. This value is valid on only the PXIe-5842. |
    +----------------+----------------------------------------------------------------------------------------------+
    | "Marker0"      | The trigger is received from the Marker 0.                                                   |
    +----------------+----------------------------------------------------------------------------------------------+
    | "Marker1"      | The trigger is received from the Marker 1.                                                   |
    +----------------+----------------------------------------------------------------------------------------------+
    | "Marker2"      | The trigger is received from the Marker 2.                                                   |
    +----------------+----------------------------------------------------------------------------------------------+
    | "Marker3"      | The trigger is received from the Marker 3.                                                   |
    +----------------+----------------------------------------------------------------------------------------------+
    '''
    ref_clock_rate = _attributes.AttributeViReal64(1250322)
    '''Type: float

    Specifies the Reference Clock rate, in Hz, of the signal present at the REF IN or CLK IN connector. This property is only valid when the ref_clock_source property is set to ClkIn, RefIn, or RefIn2

    To set this property, the NI-RFSG device must be in the Configuration state. If you are using the PXIe-5654/5654 with PXIe-5696, the NI-RFSG device must be in the Committed state to read this property. When you read this property, it returns the frequency the device is locked to during the Committed state.

    If you set this property to Auto, NI-RFSG uses the default Reference Clock rate for the device or automatically detects the Reference Clock rate if automatic detection is supported by the device.

    **Valid Values:**

    PXIe-5654/5654 with PXIe-5696: Values between 1MHz to 20MHz in 1MHz steps are supported in addition to the Auto and 10MHz values.

    PXIe-5841 with PXIe-5655, PXIe-5842: 10 MHz, 100 MHz, 270 MHz, and 3.84 MHz

    y, where

    y is 4, 8, 16, 24, 25, or 32.

    PXIe-5860: 10 MHz, 100 MHz

    **Units**: hertz (Hz)

    **Default Value:** Auto

    **Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_

    **High-Level Methods**:

    - configure_ref_clock

    **Defined Values**:

    +-------+------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | Name  | Value      | Description                                                                                                                       |
    +=======+============+===================================================================================================================================+
    | Auto  | -1.0       | Uses the default Reference Clock rate for the device or automatically detects the Reference Clock rate if the device supports it. |
    +-------+------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | 10MHz | 10000000.0 | Uses a 10 MHz Reference Clock rate.                                                                                               |
    +-------+------------+-----------------------------------------------------------------------------------------------------------------------------------+

    Note: Automatic detection of the Reference Clock rate is supported on only the PXIe-5654/5654 with PXIe-5696. For all other supported devices, NI-RFSG uses the default Reference Clock rate of 10MHz.
    '''
    ref_clock_source = _attributes.AttributeEnum(_attributes.AttributeViString, enums.ReferenceClockSource, 1150001)
    '''Type: enums.ReferenceClockSource

    Specifies the Reference Clock source. To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** OnboardClock

    **Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_

    **High-Level Methods**:

    - configure_ref_clock

    **Possible Values**:

    +-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Possible Value  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
    +=================+=========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
    | "OnboardClock"  | Uses the onboard Reference Clock as the clock source. **PXIe-5830/5831** —For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831/5832, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. ** PXIe-5831/5832 with PXIe-5653** —Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. **PXIe-5841 with PXIe-5655** —Lock to the PXIe-5655 onboard clock. Connect the REF OUT connector on the PXIe-5655 to the PXIe-5841 REF IN connector.                                                                                                                                                                                                                                                                                                      |
    +-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | "ClkIn"         | Uses the clock signal present at the front panel CLK IN connector as the Reference Clock source. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5841 with PXIe-5655.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
    +-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | "RefIn"         | Uses the clock signal present at the front panel REF IN connector as the Reference Clock source. **PXIe-5830/5831** —For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831/5832, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For the PXIe-5831/5832, lock the external signal to the PXIe-3622 REF IN connector. **PXIe-5831/5832 with PXIe-5653** —Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. **PXIe-5841 with PXIe-5655** —Lock to the signal at the REF IN connector on the associated PXIe-5655. Connect the PXIe-5655 REF OUT connector to the PXIe-5841 REF IN connector. |
    +-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_CLK"       | Uses the PXI_CLK signal, which is present on the PXI backplane, as the Reference Clock source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
    +-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | "RefIn2"        | This value is not valid on any supported devices.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
    +-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_ClkMaster" | This value is valid on only the PXIe-5831/5832 with PXIe-5653. **PXIe-5831/5832 with PXIe-5653** —NI-RFSG configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3622 to use PXI_CLK as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
    +-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    '''
    ref_pll_bandwidth = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ReferencePllBandwidth, 1150133)
    '''Type: enums.ReferencePllBandwidth

    Configures the loop bandwidth of the reference PLL.

    **Default Value:** ReferencePllBandwidth.NARROW

    **Supported Devices:** PXIe-5653

    **Related Topics**

    `Phase-Locked Loop Bandwidth <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phased_lock_loop_bandwidth.html>`_

    **Defined Values**:

    +------------------------------+--------------------------------------------------------+
    | Value                        | Description                                            |
    +==============================+========================================================+
    | ReferencePllBandwidth.NARROW | Uses the narrowest loop bandwidth setting for the PLL. |
    +------------------------------+--------------------------------------------------------+
    | ReferencePllBandwidth.MEDIUM | Uses the medium loop bandwidth setting for the PLL.    |
    +------------------------------+--------------------------------------------------------+
    | ReferencePllBandwidth.WIDE   | Uses the widest loop bandwidth setting for the PLL.    |
    +------------------------------+--------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    relative_delay = _attributes.AttributeViReal64TimeDeltaSeconds(1150220)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the delay, in seconds, to apply to the I/Q waveform.

    Relative delay allows for delaying the generated signal from one device relative to the generated signal of another device after those devices have been synchronized. You can achieve a negative relative delay by delaying both synchronized devices by the same value (1 μs) before generation begins and then changing the relative delay to a smaller amount than the initial value on only one of the devices.

    To set this property, the NI-RFSG device must be in the Configuration or Generation state.

    **Units:** Seconds

    **Valid Values:**

    PXIe-PXIe-5820/5830/5831/5832/5840/5841: 0 μs to 3.2 μs

    PXIe-5842: 0 μs to 6.5 μs

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842

    **Related Topics**

    `NI-TClk Overview <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_tclk_help.html>`_

    Note: - To obtain a negative relative delay when synchronizing the PXIe-5840/5841 with a module that does not support this property, use the NITCLK_ATTR_SAMPLE_CLOCK_DELAY property.

     - The resolution of this property is a method of the I/Q sample period at 15E(-6) of the sample period but not worse than one Sample Clock period.
    '''
    rf_blanking_source = _attributes.AttributeViString(1150162)
    '''Type: str

    Specifies the Marker Event at which RF blanking occurs. RF blanking quickly attenuates the RF OUT signal. Use Marker Events to toggle the state of RF blanking. The RF Output always starts in the unblanked state.

    To set this property, the NI-RFSG device must be in the Configuration state.

    You can specify Marker Events by using scripts to trigger blanking at a certain point in a waveform. For example, if you set this property to marker0 str}, and marker0 occurs on samples 1,000 and 2,000 of a script, then the RF Output will be blanked (attenuated) between samples 1,000 and 2,000.

    PXIe-5645: This property is ignored if you are using the I/Q ports.

    PXIe-5840/5841: RF blanking does not occur for frequencies below 120MHz.

    For PXIe-5830/5831/5832: The RF Blanking reserves a PXI trigger line. If you are calling any Reset or `niRFSA_reset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_reset.html>`_ on the same device, NI recommends calling it before committing blanking properties. Alternatively, you can call reset_with_options or `niRFSA_ResetWithOptions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_resetwithoptions.html>`_. Select **Routes** in the **steps to omit** parameter.

    **Default Value:** "" (empty string)

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_

    **Valid Values**:

    +-----------+---------------------------------+
    | Value     | Description                     |
    +===========+=================================+
    | ""        | RF blanking is disabled.        |
    +-----------+---------------------------------+
    | "Marker0" | RF blanking is tied to marker0. |
    +-----------+---------------------------------+
    | "Marker1" | RF blanking is tied to marker1. |
    +-----------+---------------------------------+
    | "Marker2" | RF blanking is tied to marker2. |
    +-----------+---------------------------------+
    | "Marker3" | RF blanking is tied to marker3. |
    +-----------+---------------------------------+

    Note: The shortest supported blanking interval is eight microseconds.
    '''
    rf_in_lo_export_enabled = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.RFInLoExportEnabled, 1150243)
    '''Type: enums.RFInLoExportEnabled

    Specifies whether to enable the RF IN LO OUT terminal on the PXIe-5840/5841.

    Set this property to RFInLoExportEnabled.ENABLE to export the LO signal from the RF IN LO OUT terminal.

    When this property is enabled, if the lo_source property is set to LO_In and you do not set the lo_frequency or upconverter_center_frequency properties, NI-RFSG rounds the LO frequency to approximately an LO step size as if the source was OnboardClock. This ensures that when you configure NI-RFSA and NI-RFSG with compatible settings that result in the same LO frequency, the rounding also is compatible.

    **Default Value:** RFInLoExportEnabled.UNSPECIFIED

    **Supported Devices**: PXIe-5840/5841/5842

    **Defined Values**:

    +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | Value                           | Description                                                                                                                             |
    +=================================+=========================================================================================================================================+
    | RFInLoExportEnabled.DISABLE     | The RF In local oscillator signal is not present at the front panel LO OUT connector.                                                   |
    +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | RFInLoExportEnabled.ENABLE      | The RF In local oscillator signal is present at the front panel LO OUT connector.                                                       |
    +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | RFInLoExportEnabled.UNSPECIFIED | The RF IN local oscillator signal may or may not be present at the front panel LO OUT connector, because NI-RFSA may be controlling it. |
    +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    script_trigger_terminal_name = _attributes.AttributeViString(1150116)
    '''Type: str

    Returns the name of the fully qualified signal name as a string.

    **Default Values**:

    PXI-5670/5671, PXIe-5672/5673/5673E: /*AWGName*/ScriptTrigger *X*, where *AWGName* is the name of your associated AWG module in MAX and *X* is Script Trigger 0 through 3.

    PXIe-5830/5831/5832: /*BasebandModule*/ao/0/ScriptTrigger *X*, where *BasebandModule* is the name of the baseband module of your device in MAX and *X* is Script Trigger 0 through 3.

    PXIe-5820/5840/5841/5842: /*ModuleName*/ao/0/ScriptTrigger *X*, where *ModuleName* is the name of your device in MAX and *X* is Script Trigger 0 through 3.

    PXIe-5860: /*ModuleName*/ao/*ChannelNumber*/ScriptTrigger *X*, where *ModuleName* is the name of your device in MAX, *ChannelNumber* is the channel number (0 or 1), and *X* is Script Trigger 0 through 3.

    **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_

    `Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_

    **High-Level Methods**:

    - get_terminal_name

    Tip:
    This property can be set/get on specific script_triggers within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

    Example: :py:attr:`my_session.script_triggers[ ... ].script_trigger_terminal_name`

    To set/get on all script_triggers, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.script_trigger_terminal_name`
    '''
    script_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ScriptTriggerType, 1150019)
    '''Type: enums.ScriptTriggerType

    Specifies the Script Trigger type. Depending upon the value of this property, more properties may be needed to fully configure the trigger. To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** ScriptTriggerType.NONE

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

    `Trigger Types <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_types.html>`_

    **High-Level Methods**:

    - configure_digital_edge_script_trigger

    **Defined Values**:

    +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Value                           | Description                                                                                                                                                                                                                                                           |
    +=================================+=======================================================================================================================================================================================================================================================================+
    | ScriptTriggerType.NONE          | No trigger is configured. Signal generation starts immediately.                                                                                                                                                                                                       |
    +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ScriptTriggerType.DIGITAL_EDGE  | The data operation does not start until a digital edge is detected. The source of the digital edge is specified with the digital_edge_start_trigger_source property, and the active edge is specified with the digital_edge_start_trigger_edge property.              |
    +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ScriptTriggerType.DIGITAL_LEVEL | The data operation does not start until the digital level is detected. The source of the digital level is specified in the digital_level_script_trigger_source property, and the active level is specified in the digital_level_script_trigger_active_level property. |
    +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ScriptTriggerType.SOFTWARE      | The data operation does not start until a software trigger occurs. You can create a software event by calling the send_software_edge_trigger method.                                                                                                                  |
    +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

    Tip:
    This property can be set/get on specific script_triggers within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

    Example: :py:attr:`my_session.script_triggers[ ... ].script_trigger_type`

    To set/get on all script_triggers, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.script_trigger_type`
    '''
    selected_path = _attributes.AttributeViString(1150311)
    '''Type: str

    Specifies which path to configure to generate a signal.
    '''
    selected_ports = _attributes.AttributeViString(1150241)
    '''Type: str

    Specifies the port to configure.

    **Valid Values**:

    PXIe-5644/5645/5646, PXIe-5820/5840/5841: "" (empty string)

    PXIe-5830: if0, if1

    PXIe-5831/5832: if0, if1, rf*0-1*/port*x*, where *0-1* indicates one (*0*) or two (*1*) mmRH-5582 connections and *x* is the port number on the mmRH-5582 front panel.

    **Default Value:**

    PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860: "" (empty string)

    PXIe-5830/5831/5832: if0

    **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    available_ports

    Note: When using RF list mode, ports cannot be shared with NI-RFSA.
    '''
    selected_script = _attributes.AttributeViString(1150023)
    '''Type: str

    Specifies the script in onboard memory to generate upon calling the _initiate method when the generation_mode property is set to GenerationMode.SCRIPT.

    The selected_script property is ignored when the generation_mode property is set to GenerationMode.ARB_WAVEFORM or GenerationMode.CW. To set the selected_script property, the NI-RFSG device must be in the Configuration state.

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_

    `Scripting Instructions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_instructions.html>`_
    '''
    self_calibration_temperature = _attributes.AttributeViReal64(1150136)
    '''Type: float

    Indicates, in degrees Celsius, the temperature of the device at the time of the last self calibration.

    **Supported Devices:** PXIe-5644/5645/5646
    '''
    serial_number = _attributes.AttributeViString(1150026)
    '''Type: str

    Returns the serial number of the RF module. If the NI-RFSG session is controlling multiple modules, this property returns the serial number of the primary RF module.

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    signal_bandwidth = _attributes.AttributeViReal64(1150007)
    '''Type: float

    Specifies the bandwidth of the arbitrary signal. This value must be less than or equal to (0.8× iq_rate).

    NI-RFSG defines *signal bandwidth* as twice the maximum baseband signal deviation from 0 Hz. Usually, the baseband signal center frequency is 0 Hz. In such cases, the signal bandwidth is simply the baseband signal's minimum frequency subtracted from its maximum frequency, or *f* :sub:`max` - *f* :sub:`min` .

    This property applies only when the generation_mode property is set to GenerationMode.ARB_WAVEFORM or GenerationMode.SCRIPT, except for when using the PXIe-5830/5831/5832/5840/5841, which supports setting this property in all supported generation modes. To set the signal_bandwidth property, the NI-RFSG device must be in the Configuration state.

    PXI-5670/5671, PXIe-5672: Based on your signal bandwidth, NI-RFSG determines whether to configure the upconverter center frequency in increments of 1MHz or 5MHz. Failure to configure this property may result in the signal being placed outside the upconverter passband.

    PXIe-5644/5645/5646, PXIe-5673/5673E: This property is used only for error-checking purposes. Otherwise, this property is ignored.

    PXIe-5820/5830/5831/5832/5840/5841/5842/5860: Based on your signal bandwidth, NI-RFSG decides the equalized bandwidth. If this property is not set, NI-RFSG uses the maximum available signal bandwidth. For the PXIe-5840/5841, the maximum allowed signal bandwidth depends on the upconverter center frequency. Refer to the specifications document for your device for more information about signal bandwidth. The device specifications depend on the signal bandwidth.

    **Units**: hertz (Hz)

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Phase-Locked Loop Bandwidth <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phased_lock_loop_bandwidth.html>`_

    `Frequency Tuning Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_tuning_times.html>`_

    `PXIe-5830 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_

    `PXIe-5831/5832 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_

    `PXIe-5841 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_
    '''
    specific_driver_class_spec_major_version = _attributes.AttributeViInt32(1050515)
    '''Type: int

    Returns the major version number of the class specification with which NI-RFSG is compliant.

    **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    specific_driver_class_spec_minor_version = _attributes.AttributeViInt32(1050516)
    '''Type: int

    Returns the minor version number of the class specification with which NI-RFSG is compliant.

    **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    specific_driver_description = _attributes.AttributeViString(1050514)
    '''Type: str

    Returns a string that contains a brief description of NI-RFSG. This property returns

    National Instruments RF Signal Generator Instrument Driver.

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    specific_driver_prefix = _attributes.AttributeViString(1050302)
    '''Type: str

    Returns a string that contains the prefix for NI-RFSG. The name of each user-callable method in NI-RFSG starts with this prefix. This property returns

    niRFSG.

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    specific_driver_revision = _attributes.AttributeViString(1050551)
    '''Type: str

    Returns a string that contains additional version information about NI-RFSG. For example, NI-RFSG can return

    Driver: NI-RFSG14.5.0, Compiler: MSVC9.00, Components: IVI Engine4.00, VISA-Spec4.00 as the value of this property.

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    specific_driver_vendor = _attributes.AttributeViString(1050513)
    '''Type: str

    Returns a string that contains the name of the vendor that supplies NI-RFSG. This property returns

    National Instruments.

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    started_event_terminal_name = _attributes.AttributeViString(1150112)
    '''Type: str

    Returns the name of the fully qualified signal name as a string.

    **Default Values**:

    PXI-5670/5671, PXIe-5672/5673/5673E: /*AWGName*/StartedEvent, where *AWGName* is the name of your associated AWG module in MAX.

    PXIe-5830/5831/5832: /*BasebandModule*/ao/0/StartedEvent, where *BasebandModule* is the name of the baseband module of your device in MAX.

    PXIe-5820/5840/5841: /*ModuleName*/ao/0/StartedEvent, where *ModuleName* is the name of your device in MAX.

    PXIe-5860: /*ModuleName*/ao/*ChannelNumber*/StartedEvent, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

    **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

    `Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_

    **High-Level Methods**:

    - get_terminal_name
    '''
    start_trigger_terminal_name = _attributes.AttributeViString(1150114)
    '''Type: str

    Returns the name of the fully qualified signal name as a string.

    **Default Values**:

    PXIe-5654/5654 with PXIe-5696: /*ModuleName*/StartTrigger, where *ModuleName* is the name of your device in MAX.

    PXI-5670/5671, PXIe-5672/5673/5673E: /*AWGName*/StartTrigger, where *ModuleName* is the name of your associated AWG module in MAX.

    PXIe-5830/5831/5832: /*BasebandModule*/ao/0/StartTrigger, where *BasebandModule* is the name of the baseband module of your device in MAX.

    PXIe-5820/5840/5841/5842: /*ModuleName*/ao/0/StartTrigger, where *ModuleName* is the name of your device in MAX.

    PXIe-5860: /*ModuleName*/ao/*ChannelNumber*/StartTrigger, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

    **Supported Devices:** PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_

    `Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_

    **High-Level Methods**:

    - get_terminal_name
    '''
    start_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.StartTriggerType, 1250458)
    '''Type: enums.StartTriggerType

    Specifies the Start Trigger type. Depending upon the value of this property, more properties may be needed to fully configure the trigger. To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** StartTriggerType.NONE

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_

    `Trigger Types <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_types.html>`_

    **High-Level Methods**:

    - configure_digital_edge_start_trigger
    - configure_software_start_trigger
    - disable_start_trigger

    **Defined Values**:

    +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Value                         | Description                                                                                                                                                                                                                                            |
    +===============================+========================================================================================================================================================================================================================================================+
    | StartTriggerType.NONE         | No trigger is configured.                                                                                                                                                                                                                              |
    +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | StartTriggerType.DIGITAL_EDGE | The data operation does not start until a digital edge is detected. The source of the digital edge is specified with the digital_edge_start_trigger_source property, and the active edge is specified in the digital_edge_start_trigger_edge property. |
    +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | StartTriggerType.SOFTWARE     | The data operation does not start until a software event occurs. You may create a software trigger by calling the send_software_edge_trigger method.                                                                                                   |
    +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    streaming_enabled = _attributes.AttributeViBoolean(1150045)
    '''Type: bool

    Enables and disables continuous streaming of waveform data.

    **Default Value:** False

    **Supported Devices:** PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_

    **Defined Values**:

    +-------+------------------------+
    | Value | Description            |
    +=======+========================+
    | True  | Streaming is enabled.  |
    +-------+------------------------+
    | False | Streaming is disabled. |
    +-------+------------------------+
    '''
    streaming_space_available_in_waveform = _attributes.AttributeViInt64(1150047)
    '''Type: int

    Indicates the space available, in samples, in the streaming waveform for writing new data. For optimal performance, write new data to the waveform in a fixed size that is an integer divisor of the total size of the streaming waveform. This waveform size ensures that writes do not have to wrap around from the end to the beginning of the waveform buffer.

    To read this property, the NI-RFSG device must be in the Committed state.

    **Units**: samples

    **Supported Devices:** PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_
    '''
    streaming_waveform_name = _attributes.AttributeViString(1150046)
    '''Type: str

    Specifies the name of the waveform used to continually stream data during generation.

    **Default Value:** "" (empty string)

    **Supported Devices:** PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_

    `Streaming Waveform Data <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming_waveform_data.html>`_
    '''
    streaming_write_timeout = _attributes.AttributeViReal64TimeDeltaSeconds(1150140)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Indicates the maximum amount of time allowed to complete a streaming write operation.

    **Default Value:** 10.0seconds

    **Supported Devices:** PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_

    `Streaming Waveform Data <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming_waveform_data.html>`_
    '''
    supported_instrument_models = _attributes.AttributeViStringCommaSeparated(1050327)
    '''Type: list of str

    Returns a list of supported devices.

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    sync_sample_clock_dist_line = _attributes.AttributeViString(1150181)
    '''Type: str

    Specifies which external trigger line distributes the Sample Clock sync signal. When synchronizing the Sample Clock between multiple devices, configure all devices to use the same Sample Clock sync distribution line.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0

    **Default Value:** "" (empty string)

    **Supported Devices:** PXIe-5646

    **Related Topics**

    `Synchronization Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/synchronization_rfsa_g.html>`_—Refer to this topic for more information about PXIe-5646 device synchronization.
    '''
    sync_sample_clock_master = _attributes.AttributeViBoolean(1150180)
    '''Type: bool

    Specifies whether the device is the master device when synchronizing the Sample Clock between multiple devices. The master device distributes the Sample Clock sync signal to all devices in the system through the Sample Clock sync distribution line.

    When synchronizing the Sample Clock, one device must always be designated as the master. The master device actively drives the Sample Clock sync distribution line.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** False

    **Supported Devices:** PXIe-5646

    **Related Topics**

    `Synchronization Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/synchronization_rfsa_g.html>`_—Refer to this topic for more information about PXIe-5646 device synchronization.

    **Defined Values**:

    +-------+---------------------------------------------------------------------+
    | Value | Description                                                         |
    +=======+=====================================================================+
    | True  | The device is the master device for synchronizing the Sample Clock. |
    +-------+---------------------------------------------------------------------+
    | False | The device is not the master for synchronizing the Sample Clock.    |
    +-------+---------------------------------------------------------------------+
    '''
    sync_script_trigger_dist_line = _attributes.AttributeViString(1150143)
    '''Type: str

    Specifies which external trigger line distributes the synchronized Script Trigger signal. When synchronizing the Script Trigger, configure all devices to use the same Script Trigger distribution line.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0

    **Default Value:** "" (empty string)

    **Supported Devices:** PXIe-5644/5645/5646

    **Related Topics**

    `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

    `Synchronizing Sample Clock and Sampled Reference Clock Signals <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/sample_clock_sync.html>`_

    Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device for more information about device synchronization for vector signal transceivers.
    '''
    sync_script_trigger_master = _attributes.AttributeViBoolean(1150142)
    '''Type: bool

    Specifies whether the device is the master device when synchronizing the Script Trigger.

    The master device distributes the synchronized Script Trigger to all devices in the system through the Script Trigger distribution line.

    When synchronizing the Script trigger, one device must always be designated as the master. The master device actively drives the Script Trigger distribution line. For slave devices, set the script_trigger_type property to digital edge, and set the digital_edge_script_trigger_source property to sync_script.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** False

    **Supported Devices:** PXIe-5644/5645/5646

    **Related Topics**

    `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

    `Synchronizing Sample Clock and Sampled Reference Clock Signals <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/sample_clock_sync.html>`_

    Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device for more information about device synchronization for vector signal transceivers.

    **Defined Values**:

    +-------+-----------------------------------------------------------------------+
    | Value | Description                                                           |
    +=======+=======================================================================+
    | True  | The device is the master device for synchronizing the Script Trigger. |
    +-------+-----------------------------------------------------------------------+
    | False | The device is not the master for synchronizing the Script Trigger.    |
    +-------+-----------------------------------------------------------------------+
    '''
    sync_start_trigger_dist_line = _attributes.AttributeViString(1150156)
    '''Type: str

    Specifies which external trigger line distributes the synchronized Start Trigger signal. When synchronizing the Start Trigger, configure all devices to use the same Start Trigger distribution line.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0

    **Default Value:** "" (empty string)

    **Supported Devices:** PXIe-5644/5645/5646

    **Related Topics**

    `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_

    Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device for more information about device synchronization for vector signal transceivers.
    '''
    sync_start_trigger_master = _attributes.AttributeViBoolean(1150155)
    '''Type: bool

    Specifies whether the device is the master device when synchronizing the Start Trigger. The master device distributes the synchronized Start Trigger to all devices in the system through the Start Trigger distribution line.

    When synchronizing the Start Trigger, one device must always be designated as the master. The master device actively drives the Start Trigger distribution line. For slave devices, set the start_trigger_type property to digital edge, and set the digital_edge_start_trigger_source property to sync_script.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** False

    **Supported Devices:** PXIe-5644/5645/5646

    **Related Topics**

    `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_

    Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device for more information about device synchronization for vector signal transceivers.

    **Defined Values**:

    +-------+----------------------------------------------------------------------+
    | Value | Description                                                          |
    +=======+======================================================================+
    | True  | The device is the master device for synchronizing the Start Trigger. |
    +-------+----------------------------------------------------------------------+
    | False | The device is not the master for synchronizing the Start Trigger.    |
    +-------+----------------------------------------------------------------------+
    '''
    temperature_read_interval = _attributes.AttributeViReal64TimeDeltaSeconds(1150212)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the minimum time between temperature sensor readings.

    **Units:** Seconds

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    thermal_correction_headroom_range = _attributes.AttributeViReal64(1150258)
    '''Type: float

    Specifies the expected thermal operating range of the instrument from the self-calibration temperature, in degrees Celsius, returned from the device_temperature property.

    For example, if this property is set to 5.0, and the device is self-calibrated at 35°C, then you can expect to run the device from 30°C to 40°C with corrected accuracy and no overflows. Setting this property with a smaller value can result in improved dynamic range, but you must ensure thermal stability while the instrument is running. Operating the instrument outside of the specified range may cause degraded performance or DSP overflows.

    **Units:** degrees Celsius (°C)

    **Default Value**:

    **PXIe-5830/5831/5832/5842/5860**: 5

    **PXIe-5840/5841**: 10

    **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860
    '''
    thermal_correction_temperature_resolution = _attributes.AttributeViReal64(1150244)
    '''Type: float

    Specifies the temperature change, in degrees Celsius, that is required before NI-RFSG recalculates the thermal correction settings when entering the Generation state.

    **Units:** degrees Celsius (°C)

    **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Default Values:**

    PXIe-5830/5831/5832/5842/5860: 0.2

    PXIe-5840/5841: 1.0
    '''
    timer_event_interval = _attributes.AttributeViReal64TimeDeltaSeconds(1150100)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the time before the timer emits an event after the task is started and specifies the time interval between Timer events after the first event.

    **Units**: seconds (s)

    **Default Value:** 0

    **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

    Note: For the PXIe-5820/5840/5841/5842/5860, this property must be set for the timer to start. If you do not set this property, the timer is disabled.
    '''
    upconverter_center_frequency = _attributes.AttributeViReal64(1154098)
    '''Type: float

    Indicates the center frequency of the passband containing the upconverted RF signal. Writing a value to this property while using the PXIe-5644/5645/5646, PXIe-5672/5673/5673E, or PXIe-5820/5840/5841 device enables in-band retuning. In-band retuning increases the speed of frequency sweeps by reducing the amount of upconverter retunes.

    **Units**: hertz (Hz)

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

    Note: - This property is read/write on the PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842, and is read-only on the PXI-5670/5671.

     - Resetting this property disables in-band retuning, however, for the PXIe-5820, in-band retuning is always enabled.

     - For the PXIe-5820, the only valid value for this property is 0.

     - Setting this property while the PXIe-5644/5645/5646, PXIe-5673/5673E, or PXIe-5820/5830/5831/5832/5840/5841/5842 device is generating has no effect until a dynamic property is set.
    '''
    upconverter_frequency_offset = _attributes.AttributeViReal64(1150160)
    '''Type: float

    This property offsets the upconverter_center_frequency from the RF frequency. Use this property to keep the local oscillator (LO) leakage at a determined offset from the RF signal.

    **Valid Values:**

    PXIe-5644/5645: -42MHz to +42MHz

    PXIe-5646: -100MHz to +100MHz

    PXIe-5830/5831/5832/5840/5841: -500MHz to +500MHz

    PXI-5842 (500 MHz bandwidth option): -250MHz to +250MHz

    PXI-5842 (1 GHz bandwidth option): -500MHz to +500MHz

    PXI-5842 (2 GHz bandwidth option): -1GHz to +1GHz

    PXIe-5842 (4 GHz bandwidth option) using the Standard personality: -1GHz to +1GHz

    PXIe-5842 (4 GHz bandwidth option) using the 4 GHz Bandwidth personality: -2GHz to +2GHz

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

    **Related Topics**

    `PXIe-5830 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_

    `PXIe-5831/5832 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_

    `PXIe-5841 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_

    Note: - You cannot set the upconverter_center_frequency property or the arb_carrier_frequency property at the same time as the upconverter_frequency_offset property.

     - Resetting this property disables the upconverter frequency offset.
    '''
    upconverter_frequency_offset_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.UpconverterFrequencyOffsetMode, 1150248)
    '''Type: enums.UpconverterFrequencyOffsetMode

    Specifies whether to allow NI-RFSG to select the upconverter frequency offset. You can either set an offset yourself or let NI-RFSG select one for you.

    Placing the upconverter center frequency outside the bandwidth of your waveform can help avoid issues such as LO leakage.

    To set an offset yourself, set this property to UpconverterFrequencyOffsetMode.AUTO or UpconverterFrequencyOffsetMode.USER_DEFINED, and set either the upconverter_center_frequency or the upconverter_frequency_offset property.

    To allow NI-RFSG to automatically select the upconverter frequency offset, set this property to UpconverterFrequencyOffsetMode.AUTO or UpconverterFrequencyOffsetMode.ENABLE and set the signal_bandwidth to describe the bandwidth of your waveform. The signal bandwidth must be no greater than half the value of the device_instantaneous_bandwidth property, minus a device-specific guard band. Do not set the upconverter_center_frequency or upconverter_frequency_offset properties. If all conditions are met, NI-RFSG places the upconverter center frequency outside the signal bandwidth. Set this property to UpconverterFrequencyOffsetMode.ENABLE if you want to receive an error any time NI-RFSG is unable to apply automatic offset.

    When you set an offset yourself or do not use an offset, the reference frequency for gain is near the upconverter center frequency, and upconverter_frequency_offset_mode returns UpconverterFrequencyOffsetMode.USER_DEFINED. When NI-RFSG automatically sets an offset, the reference frequency for gain is near the frequency and upconverter_frequency_offset_mode returns UpconverterFrequencyOffsetMode.ENABLE.

    **Default Value:** UpconverterFrequencyOffsetMode.AUTO

    **Supported Devices**: PXIe-5830/5831/5832/5841/5842

    **Related Topics**

    `PXIe-5830 Automatic Frequency Offset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/automatic_frequency_offset.html>`_

    `PXIe-5831/5832 Automatic Frequency Offset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/automatic_frequency_offset.html>`_

    `PXIe-5841 Automatic Frequency Offset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/automatic_frequency_offset.html>`_

    **Defined Values**:

    +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Value                                       | Description                                                                                                                                                                                                                                                            |
    +=============================================+========================================================================================================================================================================================================================================================================+
    | UpconverterFrequencyOffsetMode.ENABLE       | NI-RFSG places the upconverter center frequency outside of the signal bandwidth if the signal_bandwidth property has been set and can be avoided. NI-RFSG returns an error if the signal_bandwidth property has not been set, or if the signal bandwidth is too large. |
    +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | UpconverterFrequencyOffsetMode.AUTO         | NI-RFSG places the upconverter center frequency outside of the signal bandwidth if the signal_bandwidth property has been set and can be avoided.                                                                                                                      |
    +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | UpconverterFrequencyOffsetMode.USER_DEFINED | NI-RFSG uses the offset that you specified with the upconverter_frequency_offset or upconverter_center_frequency properties.                                                                                                                                           |
    +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    Note: Below 120 MHz, the PXIe-5841 does not use an LO and UpconverterFrequencyOffsetMode.ENABLE is unavailable. Refer to the *PXIe-5841 Automatic Frequency Offset* topic for more information about using an automatic offset with an external LO.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    upconverter_gain = _attributes.AttributeViReal64(1154097)
    '''Type: float

    Specifies the gain the upconverter applies to the signal.

    **Units**: dB

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    Note: This property is read/write on the PXI-5610 and PXIe-5611 and is read-only on the PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860.
    '''
    waveform_iq_rate = _attributes.AttributeViReal64(1150263)
    '''Type: float

    Specifies the I/Q rate of the waveform. To set this property, the NI-RFSG device must be in the Configuration state.

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_

    `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_—Refer to this topic for more information about using this property to associate an I/Q rate with a waveform.

    `Digital Upconverter <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/duc.html>`_

    Tip:
    This property can be set/get on specific waveforms within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container waveforms to specify a subset.

    Example: :py:attr:`my_session.waveforms[ ... ].waveform_iq_rate`

    To set/get on all waveforms, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.waveform_iq_rate`
    '''
    waveform_papr = _attributes.AttributeViReal64(1150266)
    '''Type: float

    Specifies the peak-to-average power ratio (PAPR).

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    Tip:
    This property can be set/get on specific waveforms within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container waveforms to specify a subset.

    Example: :py:attr:`my_session.waveforms[ ... ].waveform_papr`

    To set/get on all waveforms, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.waveform_papr`
    '''
    waveform_rf_blanking = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.RFBlanking, 1150278)
    '''Type: enums.RFBlanking

    **Defined Values**:

    Name (Value): Description

    RFBlanking.DISABLE (0):	RF blanking is disabled.

    RFBlanking.ENABLE (1):	RF blanking is enabled.

    **Default Value:** RFBlanking.DISABLE

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_

    Enables or disables RF blanking.

    +-----------------------------------------------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------+
    | rf_blanking_source                                                                | waveform_rf_blanking | Behaviour                                                                                                 |
    +===================================================================================+======================+===========================================================================================================+
    | "" (empty string)                                                                 | RFBlanking.DISABLE   | No blanking performed.                                                                                    |
    +-----------------------------------------------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------+
    | "" (empty string)                                                                 | RFBlanking.ENABLE    | Blanking performed based on burst start and stop values and blanking source set to private marker.        |
    +-----------------------------------------------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------+
    | NIRFSG_VAL_MARKER0, NIRFSG_VAL_MARKER1, NIRFSG_VAL_MARKER2, or NIRFSG_VAL_MARKER3 | RFBlanking.DISABLE   | Blanking performed based on the marker locations for the marker that the user set in the blanking source. |
    +-----------------------------------------------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------+
    | NIRFSG_VAL_MARKER0, NIRFSG_VAL_MARKER1, NIRFSG_VAL_MARKER2, or NIRFSG_VAL_MARKER3 | RFBlanking.ENABLE    | Error is shown.                                                                                           |
    +-----------------------------------------------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------+

    Note: For PXIe-5830/5831/5832: The RF Blanking reserves a PXI trigger line. If you are calling any Reset or `niRFSA_reset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_reset.html>`_ on the same device, NI recommends calling it before committing blanking properties. Alternatively, you can call reset_with_options or `niRFSA_ResetWithOptions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_resetwithoptions.html>`_. Select **Routes** in the **steps to omit** parameter.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

    Tip:
    This property can be set/get on specific waveforms within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container waveforms to specify a subset.

    Example: :py:attr:`my_session.waveforms[ ... ].waveform_rf_blanking`

    To set/get on all waveforms, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.waveform_rf_blanking`
    '''
    waveform_runtime_scaling = _attributes.AttributeViReal64(1150265)
    '''Type: float

    Specifies the waveform runtime scaling. The waveform runtime scaling is applied to the waveform data before any other signal processing.

    **Units**: dB

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860, PXIe-5841 with PXIe-5655

    Tip:
    This property can be set/get on specific waveforms within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container waveforms to specify a subset.

    Example: :py:attr:`my_session.waveforms[ ... ].waveform_runtime_scaling`

    To set/get on all waveforms, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.waveform_runtime_scaling`
    '''
    waveform_signal_bandwidth = _attributes.AttributeViReal64(1150264)
    '''Type: float

    Specifies the bandwidth of the arbitrary signal. This value must be less than or equal to (0.8× iq_rate).

    **Units**: hertz (Hz)

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    Tip:
    This property can be set/get on specific waveforms within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container waveforms to specify a subset.

    Example: :py:attr:`my_session.waveforms[ ... ].waveform_signal_bandwidth`

    To set/get on all waveforms, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.waveform_signal_bandwidth`
    '''
    waveform_waveform_size = _attributes.AttributeViInt32(1150297)
    '''Type: int

    Specifies the size of the waveform specified by an active channel.

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5841 with PXIe-5655/5842/5860

    Tip:
    This property can be set/get on specific waveforms within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container waveforms to specify a subset.

    Example: :py:attr:`my_session.waveforms[ ... ].waveform_waveform_size`

    To set/get on all waveforms, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.waveform_waveform_size`
    '''
    write_waveform_burst_detection = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.WriteWaveformBurstDetection, 1150273)
    '''Type: enums.WriteWaveformBurstDetection

    Enables the detection of burst start and burst stop locations in the waveform. You can read the detected burst start and burst stop locations using get_waveform_burst_start_locations and get_waveform_burst_stop_locations methods respectively.

    **Default Value:** WriteWaveformBurstDetection.DISABLE

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +-------------------------------------+------------------------------+
    | Value                               | Description                  |
    +=====================================+==============================+
    | WriteWaveformBurstDetection.ENABLE  | Burst detection is enabled.  |
    +-------------------------------------+------------------------------+
    | WriteWaveformBurstDetection.DISABLE | Burst detection is disabled. |
    +-------------------------------------+------------------------------+

    Note: - When you download a waveform using ReadAndDownloadWaveformFromFileTdms method and if waveform_rf_blanking property is enabled, you must set the write_waveform_burst_detection property to WriteWaveformBurstDetection.DISABLE.

     - For PXIe-5830/5831/5832: The RF Blanking reserves a PXI trigger line. If you are calling any Reset or `niRFSA_reset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_reset.html>`_ on the same device, NI recommends calling it before committing blanking properties. Alternatively, you can call reset_with_options or `niRFSA_ResetWithOptions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_resetwithoptions.html>`_. Select **Routes** in the **steps to omit** parameter.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    write_waveform_burst_detection_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.WriteWaveformBurstDetectionMode, 1150274)
    '''Type: enums.WriteWaveformBurstDetectionMode

    Specifies the algorithm that NI-RFSG uses to detect the burst start and burst stop locations in the waveform when burst detection is enabled using the write_waveform_burst_detection property. When you set write_waveform_burst_detection_mode to WriteWaveformBurstDetectionMode.AUTO, NI-RFSG automatically detects the burst start and burst stop locations by analyzing the waveform. To fine-tune the burst detection process parameters yourself, you can set this property to WriteWaveformBurstDetectionMode.MANUAL and specify the burst detection parameters using the write waveform burst detection minimum quiet time, write_waveform_burst_detection_power_threshold, write waveform burst detection minimum burst time properties.

    **Default Value:** WriteWaveformBurstDetectionMode.AUTO

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +----------------------------------------+---------------------------------------------------------------------------------------------------+
    | Value                                  | Description                                                                                       |
    +========================================+===================================================================================================+
    | WriteWaveformBurstDetectionMode.AUTO   | NI-RFSG automatically detects the burst start and burst stop locations by analyzing the waveform. |
    +----------------------------------------+---------------------------------------------------------------------------------------------------+
    | WriteWaveformBurstDetectionMode.MANUAL | User sets the burst detection parameters.                                                         |
    +----------------------------------------+---------------------------------------------------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    write_waveform_burst_detection_power_threshold = _attributes.AttributeViReal64(1150276)
    '''Type: float

    Specifies the relative power level at which burst start or stop locations are detected. The threshold is relative to the peak power in the waveform. NI-RFSG detects burst start (or burst stop) locations when the signal exceeds (or falls below) the level specified by this property. This property is ignored when you disable the write_waveform_burst_detection property or when you set the write_waveform_burst_detection_mode property to NIRFSG_VAL_AUTO.

    **Units:** dB

    **Default Value:** 0

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    write_waveform_normalization = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.WriteWaveformNormalization, 1150293)
    '''Type: enums.WriteWaveformNormalization

    Specifies whether to perform the normalization on a waveform.

    **Default Value:** WriteWaveformNormalization.DISABLE

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
    | Value                              | Description                                                                                                             |
    +====================================+=========================================================================================================================+
    | WriteWaveformNormalization.ENABLE  | Enables normalization on a waveform to transform the waveform data so that its maximum is 1.00 and its minimum is -1.00 |
    +------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
    | WriteWaveformNormalization.DISABLE | Disables normalization on the waveform.                                                                                 |
    +------------------------------------+-------------------------------------------------------------------------------------------------------------------------+

    Note: You can not set write_waveform_normalization and power_level_type properties at the same time.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    yig_main_coil_drive = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.YigMainCoilDrive, 1150118)
    '''Type: enums.YigMainCoilDrive

    Adjusts the dynamics of the current driving the YIG main coil.

    **Default Value:** YigMainCoilDrive.MANUAL

    **Supported Devices:** PXIe-5653

    **Defined Values**:

    +-----------------------+--------------------------------------------------------+
    | Value                 | Description                                            |
    +=======================+========================================================+
    | NIRFSG_VAL_SLOW       | Adjusts the YIG main coil for an underdamped response. |
    +-----------------------+--------------------------------------------------------+
    | YigMainCoilDrive.FAST | Adjusts the YIG main coil for an overdamped response.  |
    +-----------------------+--------------------------------------------------------+

    Note: Setting this property to YigMainCoilDrive.FAST on the PXIe-5653 allows the frequency to settle significantly faster for some frequency transitions at the expense of increased phase noise.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
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
        self.markers = _RepeatedCapabilities(self, 'marker', repeated_capability_list)
        self.script_triggers = _RepeatedCapabilities(self, 'scripttrigger', repeated_capability_list)
        self.waveforms = _RepeatedCapabilities(self, 'waveform::', repeated_capability_list)
        self.ports = _RepeatedCapabilities(self, '', repeated_capability_list)
        self.los = _RepeatedCapabilities(self, 'LO', repeated_capability_list)
        self.device_temperatures = _RepeatedCapabilities(self, '', repeated_capability_list)
        self.channels = _RepeatedCapabilities(self, '', repeated_capability_list)

        # Finally, set _is_frozen to True which is used to prevent clients from accidentally adding
        # members when trying to set a property with a typo.
        self._is_frozen = freeze_it

    def __repr__(self):
        return '{0}.{1}({2})'.format('nirfsg', self.__class__.__name__, self._param_list)

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("'{0}' object has no attribute '{1}'".format(type(self).__name__, key))
        object.__setattr__(self, key, value)

    ''' These are code-generated '''

    @ivi_synchronized
    def configure_digital_edge_script_trigger(self, source, edge):
        r'''configure_digital_edge_script_trigger

        Configures the specified Script Trigger for digital edge triggering.

        The NI-RFSG device must be in the Configuration state before calling this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

        `Digital Edge Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_edge.html>`_

        Tip:
        This method can be called on specific script_triggers within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container script_triggers to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.script_triggers[ ... ].configure_digital_edge_script_trigger`

        To call the method on all script_triggers, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.configure_digital_edge_script_trigger`

        Args:
            source (str): Specifies the source terminal for the digital edge Script Trigger. NI-RFSG sets the digital_edge_script_trigger_source property to this value.

            edge (enums.ScriptTriggerDigitalEdgeEdge): Specifies the active edge for the digital edge Script Trigger. NI-RFSG sets the digital_edge_script_trigger_edge property to this value.

        '''
        if type(edge) is not enums.ScriptTriggerDigitalEdgeEdge:
            raise TypeError('Parameter edge must be of type ' + str(enums.ScriptTriggerDigitalEdgeEdge))
        self._interpreter.configure_digital_edge_script_trigger(self._repeated_capability, source, edge)

    @ivi_synchronized
    def configure_digital_level_script_trigger(self, source, level):
        r'''configure_digital_level_script_trigger

        Configures a specified Script Trigger for digital level triggering.

        The NI-RFSG device must be in the Configuration state before calling this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

        `Digital Level Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_level.html>`_

        Tip:
        This method can be called on specific script_triggers within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container script_triggers to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.script_triggers[ ... ].configure_digital_level_script_trigger`

        To call the method on all script_triggers, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.configure_digital_level_script_trigger`

        Args:
            source (str): Specifies the trigger source terminal for the digital level Script Trigger. NI-RFSG sets the digital_level_script_trigger_source property to this value.

            level (int): Specifies the active level for the digital level Script Trigger. NI-RFSG sets the digital_level_script_trigger_active_level property to this value.

        '''
        self._interpreter.configure_digital_level_script_trigger(self._repeated_capability, source, level)

    @ivi_synchronized
    def configure_software_script_trigger(self):
        r'''configure_software_script_trigger

        Configures the Script Trigger for software triggering.

        Refer to the send_software_edge_trigger method for more information about using the software Script Trigger. The NI-RFSG device must be in the Configuration state before calling this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

        `Trigger Types <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_types.html>`_

        Tip:
        This method can be called on specific script_triggers within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container script_triggers to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.script_triggers[ ... ].configure_software_script_trigger`

        To call the method on all script_triggers, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.configure_software_script_trigger`
        '''
        self._interpreter.configure_software_script_trigger(self._repeated_capability)

    @ivi_synchronized
    def disable_script_trigger(self):
        r'''disable_script_trigger

        Configures the device not to wait for the specified Script Trigger.

        Call this method only if you previously configured a Script Trigger and now want it disabled. The NI-RFSG device must be in the Configuration state before you call this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

        Tip:
        This method can be called on specific script_triggers within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container script_triggers to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.script_triggers[ ... ].disable_script_trigger`

        To call the method on all script_triggers, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.disable_script_trigger`
        '''
        self._interpreter.disable_script_trigger(self._repeated_capability)

    def error_message(self, error_code):
        r'''error_message

        Converts an error code returned by an NI-RFSG method into a user-readable string.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Args:
            error_code (int): Pass the status parameter that is returned from any NI-RFSG method.

                **Default Value** : 0 (VI_SUCCESS)


        Returns:
            error_message (str): Returns the user-readable message string that corresponds to the status code you specify.

        '''
        error_message = self._interpreter.error_message(error_code)
        return error_message

    @ivi_synchronized
    def _get_attribute_vi_boolean(self, attribute):
        r'''_get_attribute_vi_boolean

        Queries the value of a ViBoolean property.

        Use this low-level method to get the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_boolean`

        Args:
            attribute (int): Pass the ID of a property.


        Returns:
            value (bool): Returns the current value of the property. Pass the address of a ViBoolean variable.

        '''
        value = self._interpreter.get_attribute_vi_boolean(self._repeated_capability, attribute)
        return value

    @ivi_synchronized
    def _get_attribute_vi_int32(self, attribute):
        r'''_get_attribute_vi_int32

        Queries the value of a ViInt32 property.

        Use this low-level method to get the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int32`

        Args:
            attribute (int): Pass the ID of a property.


        Returns:
            value (int): Returns the current value of the property. Pass the address of a ViInt32 variable.

        '''
        value = self._interpreter.get_attribute_vi_int32(self._repeated_capability, attribute)
        return value

    @ivi_synchronized
    def _get_attribute_vi_int64(self, attribute):
        r'''_get_attribute_vi_int64

        Queries the value of a ViInt64 property.

        You can use this low-level method to get the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int64`

        Args:
            attribute (int): Pass the ID of a property.


        Returns:
            value (int): Returns the current value of the property. Pass the address of a ViInt64 variable.

        '''
        value = self._interpreter.get_attribute_vi_int64(self._repeated_capability, attribute)
        return value

    @ivi_synchronized
    def _get_attribute_vi_real64(self, attribute):
        r'''_get_attribute_vi_real64

        Queries the value of a ViReal64 property.

        Use this low-level method to get the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_real64`

        Args:
            attribute (int): Pass the ID of a property.


        Returns:
            value (float): Returns the current value of the property. Pass the address of a ViReal64 variable.

        '''
        value = self._interpreter.get_attribute_vi_real64(self._repeated_capability, attribute)
        return value

    @ivi_synchronized
    def _get_attribute_vi_session(self, attribute):
        r'''_get_attribute_vi_session

        Queries the value of a ViSession property.

        Use this low-level method to get the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_session`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_session`

        Args:
            attribute (int): Pass the ID of a property.


        Returns:
            value (int): Returns the current value of the property. Pass the address of a ViSession variable.

        '''
        value = self._interpreter.get_attribute_vi_session(self._repeated_capability, attribute)
        return value

    @ivi_synchronized
    def _get_attribute_vi_string(self, attribute):
        r'''_get_attribute_vi_string

        Queries the value of a ViString property.

        Use this low-level method to get the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid.

        You must provide a ViString (ViChar array) to serve as a buffer for the value. Pass the number of bytes in the buffer as the Buffer Size parameter. If the current value of the property, including the terminating NULL byte, is larger than the size you indicate in the buffer size parameter, the method copies buffer size-1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the method places "123" into the buffer and returns 7.

        To call this method to get only the required buffer size, pass 0 for the buffer size and VI_NULL for the property value buffer.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_string`

        Args:
            attribute (int): Pass the ID of a property.


        Returns:
            value (str): The buffer in which the method returns the current value of the property. The buffer must be of type ViChar and have at least as many bytes as indicated in the **bufferSize** parameter.

                If you specify 0 for the **bufferSize** parameter, you can pass VI_NULL for this parameter.

        '''
        value = self._interpreter.get_attribute_vi_string(self._repeated_capability, attribute)
        return value

    @ivi_synchronized
    def get_waveform_burst_start_locations(self):
        r'''get_waveform_burst_start_locations

        Returns the burst start locations of the waveform stored in the NI-RFSG session.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842

        Tip:
        This method can be called on specific waveforms within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container waveforms to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.waveforms[ ... ].get_waveform_burst_start_locations`

        To call the method on all waveforms, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.get_waveform_burst_start_locations`

        Returns:
            locations (list of float): Returns the burst start locations stored in the NI-RFSG session for the waveform that you specified in the CHANNEL_NAME parameter. This value is expressed in samples.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

        '''
        locations = self._interpreter.get_waveform_burst_start_locations(self._repeated_capability)
        return locations

    @ivi_synchronized
    def get_waveform_burst_stop_locations(self):
        r'''get_waveform_burst_stop_locations

        Returns the burst stop locations of the waveform stored in the NI-RFSG session.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842

        Tip:
        This method can be called on specific waveforms within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container waveforms to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.waveforms[ ... ].get_waveform_burst_stop_locations`

        To call the method on all waveforms, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.get_waveform_burst_stop_locations`

        Returns:
            locations (list of float): Returns the burst start locations stored in the NI-RFSG session for the waveform that you specified in the CHANNEL_NAME parameter. This value is expressed in samples.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

        '''
        locations = self._interpreter.get_waveform_burst_stop_locations(self._repeated_capability)
        return locations

    @ivi_synchronized
    def get_waveform_marker_event_locations(self):
        r'''get_waveform_marker_event_locations

        Returns the marker locations associated with the waveform and the marker stored in the NI-RFSG session.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842

        Tip:
        This method can be called on specific markers within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container markers to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.markers[ ... ].get_waveform_marker_event_locations`

        To call the method on all markers, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.get_waveform_marker_event_locations`

        Returns:
            locations (list of float): Returns the marker locations stored in the NI-RFSG database for the channel you specified in the CHANNEL_NAME parameter. This value is expressed in samples.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

        '''
        locations = self._interpreter.get_waveform_marker_event_locations(self._repeated_capability)
        return locations

    @ivi_synchronized
    def load_configurations_from_file(self, file_path):
        r'''load_configurations_from_file

        Loads the configurations from the specified file to the NI-RFSG driver session.

        The VI does an implicit reset before loading the configurations from the file.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].load_configurations_from_file`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.load_configurations_from_file`

        Args:
            file_path (str): Specifies the absolute path of the file from which the NI-RFSG loads the configurations.

        '''
        self._interpreter.load_configurations_from_file(self._repeated_capability, file_path)

    def lock(self):
        '''lock

        Obtains a multithread lock on the device session. Before doing so, the
        software waits until all other execution threads release their locks
        on the device session.

        Other threads may have obtained a lock on this session for the
        following reasons:

            -  The application called the lock method.
            -  A call to NI-RFSG locked the session.
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
            lock (context manager): When used in a with statement, nirfsg.Session.lock acts as
            a context manager and unlock will be called when the with block is exited
        '''
        self._interpreter.lock()  # We do not call this in the context manager so that this function can
        # act standalone as well and let the client call unlock() explicitly. If they do use the context manager,
        # that will handle the unlock for them
        return _Lock(self)

    @ivi_synchronized
    def save_configurations_to_file(self, file_path):
        r'''save_configurations_to_file

        Saves the configurations of the session to the specified file.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].save_configurations_to_file`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.save_configurations_to_file`

        Args:
            file_path (str): Specifies the absolute path of the file to which the NI-RFSG saves the configurations.

        '''
        self._interpreter.save_configurations_to_file(self._repeated_capability, file_path)

    @ivi_synchronized
    def send_software_edge_trigger(self, trigger, trigger_identifier):
        r'''send_software_edge_trigger

        Forces a trigger to occur.

        The specified trigger generates regardless of whether the trigger has been configured as a software trigger.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_

        Args:
            trigger (enums.SoftwareTriggerType): Specifies the trigger to send.

                **Default Value:** SoftwareTriggerType.START

                **Defined Values:**

                +----------------------------+---------+-------------------------------+
                | Name                       | Value   | Description                   |
                +============================+=========+===============================+
                | SoftwareTriggerType.START  | 0 (0x0) | Specifies the Start Trigger.  |
                +----------------------------+---------+-------------------------------+
                | SoftwareTriggerType.SCRIPT | 1 (0x1) | Specifies the Script Trigger. |
                +----------------------------+---------+-------------------------------+

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            trigger_identifier (enums.TriggerIdentifier): Specifies the Script Trigger to configure. This parameter is valid only when you set the TRIGGER parameter to NIRFSG_VAL_START_TRIGGER. Otherwise, set the TRIGGER_IDENTIFIER parameter to "" (empty string).

                **Default Value:** "" (empty string)

                **Possible Values:**

                +----------------+-----------------------------+
                | Possible Value | Description                 |
                +================+=============================+
                | scriptTrigger0 | Specifies Script Trigger 0. |
                +----------------+-----------------------------+
                | scriptTrigger1 | Specifies Script Trigger 1. |
                +----------------+-----------------------------+
                | scriptTrigger2 | Specifies Script Trigger 2. |
                +----------------+-----------------------------+
                | scriptTrigger3 | Specifies Script Trigger 3. |
                +----------------+-----------------------------+
                |                | None (no signal to export)  |
                +----------------+-----------------------------+

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        if type(trigger) is not enums.SoftwareTriggerType:
            raise TypeError('Parameter trigger must be of type ' + str(enums.SoftwareTriggerType))
        if type(trigger_identifier) is not enums.TriggerIdentifier:
            raise TypeError('Parameter trigger_identifier must be of type ' + str(enums.TriggerIdentifier))
        self._interpreter.send_software_edge_trigger(trigger, trigger_identifier)

    @ivi_synchronized
    def _set_attribute_vi_boolean(self, attribute, value):
        r'''_set_attribute_vi_boolean

        Sets the value of a ViBoolean property.

        Use this low-level method to set the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid or is different than the value you specify.

        NI-RFSG contains high-level methods that set most of the instrument properties. Use the high-level driver methods as much as possible, as they handle order dependencies and multithread locking. The high-level methods also perform status checking only after setting all of the properties. In contrast, when you set multiple properties using the SetAttribute methods, the methods check the instrument status after each call.

        Also, when state caching is enabled, the high-level methods that configure multiple properties perform instrument I/O only for the properties whose value you change. Thus, you can safely call the high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_boolean`

        Args:
            attribute (int): Pass the ID of a property.

            value (bool): Pass the value to which you want to set the property.

                Note: Some values may not be valid. The allowed values depend on the current settings of the instrument session.

        '''
        self._interpreter.set_attribute_vi_boolean(self._repeated_capability, attribute, value)

    @ivi_synchronized
    def _set_attribute_vi_int32(self, attribute, value):
        r'''_set_attribute_vi_int32

        Sets the value of a ViInt32 property.

        Use this low-level method to set the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid or is different than the value you specify.

        NI-RFSG contains high-level methods that set most of the instrument properties. Use the high-level driver methods as much as possible, as they handle order dependencies and multithread locking. The high-level methods also perform status checking only after setting all of the properties. In contrast, when you set multiple properties using the SetAttribute methods, the methods check the instrument status after each call.

        Also, when state caching is enabled, the high-level methods that configure multiple properties perform instrument I/O only for the properties whose value you change. Thus, you can safely call the high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int32`

        Args:
            attribute (int): Pass the ID of a property.

            value (int): Specifies the value to which you want to set the property.

                Note: Some values may not be valid. The allowed values depend on the current settings of the instrument session.

        '''
        self._interpreter.set_attribute_vi_int32(self._repeated_capability, attribute, value)

    @ivi_synchronized
    def _set_attribute_vi_int64(self, attribute, value):
        r'''_set_attribute_vi_int64

        Sets the value of a ViInt64 property.

        Use this low-level method to set the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid or is different than the value you specify.

        NI-RFSG contains high-level methods that set most of the instrument properties. Use the high-level driver methods as much as possible, as they handle order dependencies and multithread locking. The high-level methods also perform status checking only after setting all of the properties. In contrast, when you set multiple properties using the SetAttribute methods, the methods check the instrument status after each call.

        Also, when state caching is enabled, the high-level methods that configure multiple properties perform instrument I/O only for the properties whose value you change. Thus, you can safely call the high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int64`

        Args:
            attribute (int): Pass the ID of a property.

            value (int): Pass the value to which you want to set the property.

                <blockquote>
                Some values may not be valid. The allowed values depend on the current settings of the instrument session.
                </blockquote>

        '''
        self._interpreter.set_attribute_vi_int64(self._repeated_capability, attribute, value)

    @ivi_synchronized
    def _set_attribute_vi_real64(self, attribute, value):
        r'''_set_attribute_vi_real64

        Sets the value of a ViReal64 property.

        Use this low-level method to set the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid or is different than the value you specify.

        NI-RFSG contains high-level methods that set most of the instrument properties. Use the high-level driver methods as much as possible, as they handle order dependencies and multithread locking. The high-level methods also perform status checking only after setting all of the properties. In contrast, when you set multiple properties using the SetAttribute methods, the methods check the instrument status after each call.

        Also, when state caching is enabled, the high-level methods that configure multiple properties perform instrument I/O only for the properties whose value you change. Thus, you can safely call the high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_real64`

        Args:
            attribute (int): Pass the ID of a property.

            value (float): Pass the value to which you want to set the property.

                Note: Some values may not be valid. The allowed values depend on the current settings of the instrument session.

        '''
        self._interpreter.set_attribute_vi_real64(self._repeated_capability, attribute, value)

    @ivi_synchronized
    def _set_attribute_vi_session(self, attribute):
        r'''_set_attribute_vi_session

        Sets the value of a ViSession property.

        Use this low-level method to set the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid or is different than the value you specify.

        NI-RFSG contains high-level methods that set most of the instrument properties. Use the high-level driver methods as much as possible, as they handle order dependencies and multithread locking. The high-level methods also perform status checking only after setting all of the properties. In contrast, when you set multiple properties using the SetAttribute methods, the methods check the instrument status after each call.

        Also, when state caching is enabled, the high-level methods that configure multiple properties perform instrument I/O only for the properties whose value you change. Thus, you can safely call the high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_session`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_session`

        Args:
            attribute (int): Pass the ID of a property.

        '''
        self._interpreter.set_attribute_vi_session(self._repeated_capability, attribute)

    @ivi_synchronized
    def _set_attribute_vi_string(self, attribute, value):
        r'''_set_attribute_vi_string

        Sets the value of a ViString property.

        Use this low-level method to set the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid or is different than the value you specify.

        NI-RFSG contains high-level methods that set most of the instrument properties. Use the high-level driver methods as much as possible, as they handle order dependencies and multithread locking. The high-level methods also perform status checking only after setting all of the properties. In contrast, when you set multiple properties using the SetAttribute methods, the methods check the instrument status after each call.

        Also, when state caching is enabled, the high-level methods that configure multiple properties perform instrument I/O only for the properties whose value you change. Thus, you can safely call the high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_string`

        Args:
            attribute (int): Pass the ID of a property.

            value (str): Pass the value to which you want to set the property.

                Note: Some values may not be valid. The allowed values depend on the current settings of the instrument session.

        '''
        self._interpreter.set_attribute_vi_string(self._repeated_capability, attribute, value)

    @ivi_synchronized
    def set_waveform_burst_start_locations(self, locations):
        r'''set_waveform_burst_start_locations

        Configures the start location of the burst in samples where the burst refers to the active portion of a waveform.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842

        Tip:
        This method can be called on specific waveforms within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container waveforms to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.waveforms[ ... ].set_waveform_burst_start_locations`

        To call the method on all waveforms, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.set_waveform_burst_start_locations`

        Args:
            locations (list of float): Returns the burst start locations stored in the NI-RFSG session for the waveform that you specified in the CHANNEL_NAME parameter. This value is expressed in samples.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

        '''
        self._interpreter.set_waveform_burst_start_locations(self._repeated_capability, locations)

    @ivi_synchronized
    def set_waveform_burst_stop_locations(self, locations):
        r'''set_waveform_burst_stop_locations

        Configures the stop location of the burst in samples where the burst refers to the active portion of a waveform.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842

        Tip:
        This method can be called on specific waveforms within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container waveforms to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.waveforms[ ... ].set_waveform_burst_stop_locations`

        To call the method on all waveforms, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.set_waveform_burst_stop_locations`

        Args:
            locations (list of float): Specifies the burst stop locations, in samples, to store in the NI-RFSG session.

        '''
        self._interpreter.set_waveform_burst_stop_locations(self._repeated_capability, locations)

    @ivi_synchronized
    def set_waveform_marker_event_locations(self, locations):
        r'''set_waveform_marker_event_locations

        Configures the marker locations associated with waveform and marker in the NI-RFSG session.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842

        Tip:
        This method can be called on specific markers within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container markers to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.markers[ ... ].set_waveform_marker_event_locations`

        To call the method on all markers, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.set_waveform_marker_event_locations`

        Args:
            locations (list of float): Specifies the marker location, in samples, to store in the NI-RFSG database.

        '''
        self._interpreter.set_waveform_marker_event_locations(self._repeated_capability, locations)

    def unlock(self):
        '''unlock

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        '''
        self._interpreter.unlock()


class Session(_SessionBase):
    '''An NI-RFSG session to the NI-RFSG driver'''

    def __init__(self, resource_name, id_query=False, reset_device=False, options={}, *, grpc_options=None):
        r'''An NI-RFSG session to the NI-RFSG driver

        Opens a session to the device you specify as the RESOURCE_NAME and returns a ViSession handle that you use to identify the NI-RFSG device in all subsequent NI-RFSG method calls.

        This method also configures the device through the OPTION_STRING input.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Simulating an NI RF Signal Generator <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/simulate.html>`_

        Note: For multichannel devices such as the PXIe-5860, the resource name must include the channel number to use. The channel number is specified by appending /*ChannelNumber* to the device name, where *ChannelNumber* is the channel number (0, 1, etc.). For example, if the device name is PXI1Slot2 and you want to use channel 0, use the resource name PXI1Slot2/0.

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Args:
            resource_name (str): Specifies the resource name of the device to initialize.

                For NI-DAQmx devices, the syntax is the device name specified in MAX. Typical default names for NI-DAQmx devices in MAX are Dev2 or PXISlot2. You can rename an NI-DAQmx device in MAX.

                You can also specify the name of an IVI logical name configured with the IVI Configuration utility. Refer to the *IVI* topic of the *Measurement & Automation Explorer Help* for more information.

                Note: NI-RFSG device names are not case-sensitive. However, all IVI names, such as logical names, are case-sensitive. If you use an IVI logical name, make sure the name is identical to the name shown in the IVI Configuration Utility.

            id_query (bool): Specifies whether you want NI-RFSG to perform an ID query.

                **Defined Values** :

                +-----------+--------------------------+
                | Value     | Description              |
                +===========+==========================+
                | True (1)  | Perform ID query.        |
                +-----------+--------------------------+
                | False (0) | Do not perform ID query. |
                +-----------+--------------------------+

            reset_device (bool): Specifies whether you want to reset the NI-RFSG device during the initialization procedure.

                **Defined Values** :

                +-----------+----------------------+
                | Value     | Description          |
                +===========+======================+
                | True (1)  | Reset device.        |
                +-----------+----------------------+
                | False (0) | Do not reset device. |
                +-----------+----------------------+

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

            grpc_options (nirfsg.grpc_session_options.GrpcSessionOptions): MeasurementLink gRPC session options


        Returns:
            new_vi (int): Returns a ViSession handle that you use to identify the NI-RFSG device in all subsequent NI-RFSG method calls.

        '''
        if grpc_options:
            import nirfsg._grpc_stub_interpreter as _grpc_stub_interpreter
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
        param_list.append("id_query=" + pp.pformat(id_query))
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

        Initiates signal generation, causing the NI-RFSG device to leave the Configuration state and enter the Generation state.

        If the settings have not been committed to the device before you call this method, they are committed by this method. The operation returns when the RF output signal settles. To return to the Configuration state, call the abort method.

        **Supported Devices** : PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_

        Note:
        This method will return a Python context manager that will initiate on entering and abort on exit.
        '''
        return _Generation(self)

    def close(self):
        '''close

        Aborts any signal generation in progress and destroys the instrument driver session.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_

        `NI-RFSG Programming State Model <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5670_programming_state_model.html>`_

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

        Stops signal generation.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `NI-RFSG Programming State Model <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5670_programming_state_model.html>`_
        '''
        self._interpreter.abort()

    @ivi_synchronized
    def allocate_arb_waveform(self, waveform_name, size_in_samples):
        r'''allocate_arb_waveform

        Allocates onboard memory space for the arbitrary waveform.

        Use this method to specify the total size of a waveform before writing the data. Use this method only if you are calling the WriteArbWaveform method multiple times to write a large waveform in smaller blocks.

        The NI-RFSG device must be in the Configuration state before you call this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Streaming Waveform Data <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming_waveform_data.html>`_

        Args:
            waveform_name (str): Specifies the name used to identify the waveform. This string is case-insensitive and alphanumeric, and it does not use reserved words.

            size_in_samples (int): Specifies the number of samples to reserve in the onboard memory for the specified waveform. Each I/Q pair is considered one sample.

        '''
        self._interpreter.allocate_arb_waveform(waveform_name, size_in_samples)

    @ivi_synchronized
    def change_external_calibration_password(self, old_password, new_password):
        r'''change_external_calibration_password

        Changes the external calibration password of the device.

        **Supported Devices:** PXIe-5611, PXIe-5653/5654, PXIe-5673/5673E, PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Args:
            old_password (str): Specifies the old (current) external calibration password. This password is case sensitive.

            new_password (str): Specifies the new (desired) external calibration password.

        '''
        self._interpreter.change_external_calibration_password(old_password, new_password)

    @ivi_synchronized
    def check_generation_status(self):
        r'''check_generation_status

        Checks the status of the generation.

        Call this method to check for any errors that might occur during the signal generation or to check whether the device has finished generating.

        **Supported Devices** : PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`

        Returns:
            is_done (bool): Returns information about the completion of signal generation.

                **Defined Values** :

                +-------+---------------------------------+
                | Value | Description                     |
                +=======+=================================+
                | True  | Signal generation is complete.  |
                +-------+---------------------------------+
                | False | Signal generation is occurring. |
                +-------+---------------------------------+

        '''
        is_done = self._interpreter.check_generation_status()
        return is_done

    @ivi_synchronized
    def check_if_script_exists(self, script_name):
        r'''check_if_script_exists

        Returns whether the script that you specify as SCRIPT_NAME exists.

        **Supported Devices** : PXIe-5673/5673E. PXIe-5830/5831/5840/5841/5842/5860

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Args:
            script_name (str): Specifies the name of the script. This string is case-insensitive.


        Returns:
            script_exists (bool): Returns True if the script exists.

                **Defined Values** :

                +-------+----------------------------+
                | Value | Description                |
                +=======+============================+
                | True  | The script exists.         |
                +-------+----------------------------+
                | False | The script does not exist. |
                +-------+----------------------------+

        '''
        script_exists = self._interpreter.check_if_script_exists(script_name)
        return script_exists

    @ivi_synchronized
    def check_if_waveform_exists(self, waveform_name):
        r'''check_if_waveform_exists

        Returns whether the waveform that you specify as WAVEFORM_NAME exists.

        **Supported Devices** : PXIe-5673/5673E, PXIe-5830/5831/5840/5841/5842/5860

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Args:
            waveform_name (str): Specifies the name used to store the waveform. This string is case-insensitive.


        Returns:
            waveform_exists (bool): Returns True if the waveform exists.

                **Defined Values** :

                +-------+------------------------------+
                | Value | Description                  |
                +=======+==============================+
                | True  | The waveform exists.         |
                +-------+------------------------------+
                | False | The waveform does not exist. |
                +-------+------------------------------+

        '''
        waveform_exists = self._interpreter.check_if_waveform_exists(waveform_name)
        return waveform_exists

    @ivi_synchronized
    def clear_all_arb_waveforms(self):
        r'''clear_all_arb_waveforms

        Deletes all currently defined waveforms and scripts.

        The NI-RFSG device must be in the Configuration state before you call this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
        '''
        self._interpreter.clear_all_arb_waveforms()

    @ivi_synchronized
    def clear_arb_waveform(self, waveform_name):
        r'''clear_arb_waveform

        Deletes a specified waveform from the pool of currently defined waveforms.

        The NI-RFSG device must be in the Configuration state before you call this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Args:
            waveform_name (str): Name of the stored waveform to delete.

        '''
        self._interpreter.clear_arb_waveform(waveform_name)

    @ivi_synchronized
    def clear_self_calibrate_range(self):
        r'''clear_self_calibrate_range

        Clears the data obtained from the self_calibrate_range method.

        **Supported Devices** : PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842
        '''
        self._interpreter.clear_self_calibrate_range()

    @ivi_synchronized
    def commit(self):
        r'''commit

        Programs the device with the correct settings.

        Calling this method moves the NI-RFSG device from the Configuration state to the Committed state. After this method executes, a change to any property reverts the NI-RFSG device to the Configuration state.

        **Supported devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `NI-RFSG Programming State Model <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5670_programming_state_model.html>`_
        '''
        self._interpreter.commit()

    @ivi_synchronized
    def configure_deembedding_table_interpolation_linear(self, port, table_name, format):
        r'''configure_deembedding_table_interpolation_linear

        Selects the linear interpolation method.

        If the carrier frequency does not match a row in the de-embedding table, NI-RFSG performs a linear interpolation based on the entries in the de-embedding table to determine the parameters to use for de-embedding.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

        Args:
            port (str): Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

            table_name (str): Specifies the name of the table.

            format (enums.Format): Specifies the format of parameters to interpolate. **Defined Values** :

                +-------------------------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
                | Name                          | Value          | Description                                                                                                                             |
                +===============================+================+=========================================================================================================================================+
                | Format.REAL_AND_IMAGINARY     | 26000 (0x6590) | Results in a linear interpolation of the real portion of the complex number and a separate linear interpolation of the complex portion. |
                +-------------------------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
                | Format.MAGNITUDE_AND_PHASE    | 26001 (0x6591) | Results in a linear interpolation of the magnitude and a separate linear interpolation of the phase.                                    |
                +-------------------------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
                | Format.MAGNITUDE_DB_AND_PHASE | 26002 (0x6592) | Results in a linear interpolation of the magnitude, in decibels, and a separate linear interpolation of the phase.                      |
                +-------------------------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------+

        '''
        if type(format) is not enums.Format:
            raise TypeError('Parameter format must be of type ' + str(enums.Format))
        self._interpreter.configure_deembedding_table_interpolation_linear(port, table_name, format)

    @ivi_synchronized
    def configure_deembedding_table_interpolation_nearest(self, port, table_name):
        r'''configure_deembedding_table_interpolation_nearest

        Selects the nearest interpolation method.

        NI-RFSG uses the parameters of the table nearest to the carrier frequency for de-embedding.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

        Args:
            port (str): Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

            table_name (str): Specifies the name of the table.

        '''
        self._interpreter.configure_deembedding_table_interpolation_nearest(port, table_name)

    @ivi_synchronized
    def configure_deembedding_table_interpolation_spline(self, port, table_name):
        r'''configure_deembedding_table_interpolation_spline

        Selects the spline interpolation method.

        If the carrier frequency does not match a row in the de-embedding table, NI-RFSG performs a spline interpolation based on the entries in the de-embedding table to determine the parameters to use for de-embedding.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

        Args:
            port (str): Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

            table_name (str): Specifies the name of the table.

        '''
        self._interpreter.configure_deembedding_table_interpolation_spline(port, table_name)

    @ivi_synchronized
    def configure_digital_edge_start_trigger(self, source, edge):
        r'''configure_digital_edge_start_trigger

        Configures the Start Trigger for digital edge triggering.

        The NI-RFSG device must be in the Configuration state before calling this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_

        `Digital Edge Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_edge.html>`_

        Note: For the PXIe-5654/5654 with PXIe-5696, the Start Trigger is valid only with a timer-based list when RF list mode is enabled.

        Args:
            source (str): Specifies the source terminal for the digital edge trigger. NI-RFSG sets the digital_edge_start_trigger_source property to this value.

            edge (enums.StartTriggerDigitalEdgeEdge): Specifies the active edge for the Start Trigger. NI-RFSG sets the digital_edge_start_trigger_edge property to this value.

        '''
        if type(edge) is not enums.StartTriggerDigitalEdgeEdge:
            raise TypeError('Parameter edge must be of type ' + str(enums.StartTriggerDigitalEdgeEdge))
        self._interpreter.configure_digital_edge_start_trigger(source, edge)

    @ivi_synchronized
    def configure_rf(self, frequency, power_level):
        r'''configure_rf

        Configures the frequency and power level of the RF output signal.

        The PXI-5670/5671, PXIe-5672, and PXIe-5860 device must be in the Configuration state before calling this method. The PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXIe-5673/5673E, and PXIe-5830/5831/5832/5840/5841/5842 device can be in the Configuration or Generation state when you call this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_

        Args:
            frequency (float): Specifies the frequency of the generated RF signal, in hertz. For arbitrary waveform generation, this parameter specifies the center frequency of the signal.

                **Units** : hertz (Hz)

            power_level (float): Specifies either the average power level or peak power level of the generated RF signal, depending on the power_level_type property.

                **Units** : dBm

        '''
        self._interpreter.configure_rf(frequency, power_level)

    @ivi_synchronized
    def configure_ref_clock(self, ref_clock_source, ref_clock_rate):
        r'''configure_ref_clock

        Configures the NI-RFSG device Reference Clock.

        The Reference Clock ensures that the NI-RFSG devices are operating from a common timebase. The NI-RFSG device must be in the Configuration state before calling this method.

        **Supported Devices** : PXI-5610, PXIe-5644/5645/5646, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `PXIe-5672 Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_

        `PXIe-5673 Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/10mhzreference_phase1.html>`_

        `PXIe-5673E Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/10mhzreference.html>`_

        `PXIe-5830 Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_

        `PXIe-5831 Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_

        Args:
            ref_clock_source (str): Specifies the source of Reference Clock signal.

                +-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | Possible Values | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
                +=================+=================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
                | "OnboardClock"  |  Uses the onboard Reference Clock as the clock source. **PXIe-5830/5831/5832** :For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. **PXIe-5831 with PXIe-5653** :Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. **PXIe-5832 with PXIe-5653** :Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. **PXIe-5841 with PXIe-5655** :Lock to the PXIe-5655 onboard clock. Connect the REF OUT connector on the PXIe-5655 to the PXIe-5841 REF IN connector. **PXIe-5842** :Lock to the PXIe-5655 onboard clock. Cables between modules are required as shown in the Getting Started Guide for the instrument.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
                +-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | "RefIn"         | Uses the clock signal present at the front panel REF IN connector as the clock source. **PXIe-5830/5831/5832** :For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. For the PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For the PXIe-5831, lock the external signal to the PXIe-3622 REF IN connector. For the PXIe-5832, lock the external signal to the PXIe-3623 REF IN connector. **PXIe-5831 with PXIe-5653** :Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. **PXIe-5832 with PXIe-5653** :Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector.  **PXIe-5841 with PXIe-5655** :Lock to the signal at the REF IN connector on the associated PXIe-5655. Connect the PXIe-5655 REF OUT connector to the PXIe-5841 REF IN connector. **PXIe-5842** :Lock to the signal at the REF IN connector on the associated PXIe-5655. Cables between modules are required as shown in the Getting Started Guide for the instrument. |
                +-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | "PXI_CLK"       | Uses the PXI_CLK signal, which is present on the PXI backplane, as the clock source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
                +-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | "ClkIn"         | Uses the clock signal present at the front panel CLK IN connector as the clock source. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5841 with PXIe-5655/5842.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
                +-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | "RefIn2"        | \-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
                +-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | "PXI_ClkMaster" | This value is valid on only the PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653. **PXIe-5831 with PXIe-5653** :NI-RFSG configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3622 to use PXI_Clk as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. **PXIe-5832 with PXIe-5653** :NI-RFSG configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3623 to use PXI_Clk as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
                +-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

            ref_clock_rate (float): Specifies the Reference Clock rate, in hertz (Hz), of the signal present at the REF IN or CLK IN connector. The default value is NIRFSG_VAL_AUTO, which allows NI-RFSG to use the default Reference Clock rate for the device or automatically detect the Reference Clock rate, if supported. This parameter is only valid when the ref_clock_source parameter is set to ClkIn, RefIn or RefIn2. Refer to the ref_clock_rate property for possible values.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        self._interpreter.configure_ref_clock(ref_clock_source, ref_clock_rate)

    @ivi_synchronized
    def configure_software_start_trigger(self):
        r'''configure_software_start_trigger

        Configures the Start Trigger for software triggering.

        Refer to the send_software_edge_trigger method for more information about using a software trigger. The NI-RFSG device must be in the Configuration state before calling this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_

        `Trigger Types <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_types.html>`_
        '''
        self._interpreter.configure_software_start_trigger()

    @ivi_synchronized
    def _create_deembedding_sparameter_table_array(self, port, table_name, frequencies, sparameter_table, number_of_ports, sparameter_orientation):
        r'''_create_deembedding_sparameter_table_array

        Creates an s-parameter de-embedding table for the port from the input data.

        If you only create one table for a port, NI-RFSG automatically selects that table to de-embed the measurement.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `De-embedding Overview <https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html>`_

        Args:
            port (str): Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

            table_name (str): Specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced.

            frequencies (numpy.array(dtype=numpy.float64)): Specifies the frequencies for the SPARAMETER_TABLE rows. Frequencies must be unique and in ascending order.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

            sparameter_table (numpy.array(dtype=numpy.complex128)): Specifies the S-parameters for each frequency. S-parameters for each frequency are placed in the array in the following order: s11, s12, s21, s22.

            sparameter_orientation (enums.SparameterOrientation): Specifies the orientation of the input data relative to the port on the DUT port.

                **Defined Values** :

                +-----------------------------------------+----------------+-----------------------------------------------------+
                | Name                                    | Value          | Description                                         |
                +=========================================+================+=====================================================+
                | SparameterOrientation.PORT1_TOWARDS_DUT | 24000 (0x5dc0) | Port 1 of the S2P is oriented towards the DUT port. |
                +-----------------------------------------+----------------+-----------------------------------------------------+
                | SparameterOrientation.PORT2_TOWARDS_DUT | 24001 (0x5dc1) | Port 2 of the S2P is oriented towards the DUT port. |
                +-----------------------------------------+----------------+-----------------------------------------------------+

        '''
        import numpy

        if type(sparameter_orientation) is not enums.SparameterOrientation:
            raise TypeError('Parameter sparameter_orientation must be of type ' + str(enums.SparameterOrientation))
        if type(frequencies) is not numpy.ndarray:
            raise TypeError('frequencies must be {0}, is {1}'.format(numpy.ndarray, type(frequencies)))
        if numpy.isfortran(frequencies) is True:
            raise TypeError('frequencies must be in C-order')
        if frequencies.dtype is not numpy.dtype('float64'):
            raise TypeError('frequencies must be numpy.ndarray of dtype=float64, is ' + str(frequencies.dtype))
        if frequencies.ndim != 1:
            raise TypeError('frequencies must be numpy.ndarray of dimension=1, is ' + str(frequencies.ndim))
        if type(sparameter_table) is not numpy.ndarray:
            raise TypeError('sparameter_table must be {0}, is {1}'.format(numpy.ndarray, type(sparameter_table)))
        if numpy.isfortran(sparameter_table) is True:
            raise TypeError('sparameter_table must be in C-order')
        if sparameter_table.dtype is not numpy.dtype('complex128'):
            raise TypeError('sparameter_table must be numpy.ndarray of dtype=complex128, is ' + str(sparameter_table.dtype))
        if sparameter_table.ndim != 3:
            raise TypeError('sparameter_table must be numpy.ndarray of dimension=3, is ' + str(sparameter_table.ndim))
        self._interpreter.create_deembedding_sparameter_table_array(port, table_name, frequencies, sparameter_table, number_of_ports, sparameter_orientation)

    @ivi_synchronized
    def create_deembedding_sparameter_table_s2p_file(self, port, table_name, s2p_file_path, sparameter_orientation):
        r'''create_deembedding_sparameter_table_s2p_file

        Creates an S-parameter de-embedding table for the port based on the specified S2P file.

        If you only create one table for a port, NI-RFSG automatically selects that table to de-embed the measurement.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `De-embedding Overview <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/de_embedding_overview.html>`_

        `S-parameters <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/s_parameters.html>`_

        Args:
            port (str): Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842 is empty string.

            table_name (str): Specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced.

            s2p_file_path (str): Specifies the path to the S2P file that contains de-embedding information for the specified port.

            sparameter_orientation (enums.SparameterOrientation): Specifies the orientation of the data in the S2P file relative to the port on the DUT port. **Defined Values** :

                +-----------------------------------------+----------------+-----------------------------------------------------+
                | Name                                    | Value          | Description                                         |
                +=========================================+================+=====================================================+
                | SparameterOrientation.PORT1_TOWARDS_DUT | 24000 (0x5dc0) | Port 1 of the S2P is oriented towards the DUT port. |
                +-----------------------------------------+----------------+-----------------------------------------------------+
                | SparameterOrientation.PORT2_TOWARDS_DUT | 24001 (0x5dc1) | Port 2 of the S2P is oriented towards the DUT port. |
                +-----------------------------------------+----------------+-----------------------------------------------------+

        '''
        if type(sparameter_orientation) is not enums.SparameterOrientation:
            raise TypeError('Parameter sparameter_orientation must be of type ' + str(enums.SparameterOrientation))
        self._interpreter.create_deembedding_sparameter_table_s2p_file(port, table_name, s2p_file_path, sparameter_orientation)

    @ivi_synchronized
    def delete_all_deembedding_tables(self):
        r'''delete_all_deembedding_tables

        Deletes all configured de-embedding tables for the session.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860
        '''
        self._interpreter.delete_all_deembedding_tables()

    @ivi_synchronized
    def delete_deembedding_table(self, port, table_name):
        r'''delete_deembedding_table

        Deletes the selected de-embedding table for a given port.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

        Args:
            port (str): Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

            table_name (str): Specifies the name of the table.

        '''
        self._interpreter.delete_deembedding_table(port, table_name)

    @ivi_synchronized
    def delete_script(self, script_name):
        r'''delete_script

        Deletes a specified script from the pool of currently defined scripts. The NI-RFSG device must be in the Configuration state before you call this method.

        **Supported Devices** :PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Args:
            script_name (str): Specifies the name of the script to delete. This string is case-insensitive.

        '''
        self._interpreter.delete_script(script_name)

    @ivi_synchronized
    def disable_start_trigger(self):
        r'''disable_start_trigger

        Configures the device not to wait for a Start Trigger.

        This method is necessary only if you previously configured a Start Trigger and now want it disabled. The NI-RFSG device must be in the Configuration state before calling this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_
        '''
        self._interpreter.disable_start_trigger()

    def create_deembedding_sparameter_table_array(self, port, table_name, frequencies, sparameter_table, sparameter_orientation):
        '''create_deembedding_sparameter_table_array

        Creates an s-parameter de-embedding table for the port from the input data.

        If you only create one table for a port, NI-RFSG automatically selects that table to de-embed the measurement.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `De-embedding Overview<https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html>`_

        Args:
            port (str): Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

            table_name (str): Specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced.

            frequencies (numpy.array(dtype=numpy.float64)): Specifies the frequencies for the SPARAMETER_TABLE rows. Frequencies must be unique and in ascending order.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

            sparameter_table (numpy.array(dtype=numpy.complex128)): Specifies the S-parameters for each frequency. S-parameters for each frequency are placed in the array in the following order: s11, s12, s21, s22.

            sparameter_orientation (enums.SparameterOrientation): Specifies the orientation of the input data relative to the port on the DUT port.

                **Defined Values** :

                +-----------------------------------------+----------------+-----------------------------------------------------+
                | Name                                    | Value          | Description                                         |
                +=========================================+================+=====================================================+
                | SparameterOrientation.PORT1_TOWARDS_DUT | 24000 (0x5dc0) | Port 1 of the S2P is oriented towards the DUT port. |
                +-----------------------------------------+----------------+-----------------------------------------------------+
                | SparameterOrientation.PORT2_TOWARDS_DUT | 24001 (0x5dc1) | Port 2 of the S2P is oriented towards the DUT port. |
                +-----------------------------------------+----------------+-----------------------------------------------------+

        '''
        if (str(type(sparameter_table)).find("'numpy.ndarray'") != -1) or (str(type(frequencies)).find("'numpy.ndarray'") != -1):
            if sparameter_table.ndim == 3:
                if frequencies.size == sparameter_table.shape[0]:
                    if sparameter_table.shape[1] == sparameter_table.shape[2]:
                        number_of_ports = sparameter_table.shape[1]
                        return self._create_deembedding_sparameter_table_array(port, table_name, frequencies, sparameter_table, number_of_ports, sparameter_orientation)
                    else:
                        raise ValueError("Row and column count of sparameter table should be equal. Table row count is {} and column count is {}.".format(sparameter_table.shape[1], sparameter_table.shape[2]))
                else:
                    raise ValueError("Frequencies count does not match the sparameter table count. Frequencies count is {} and sparameter table count is {}.".format(frequencies.size, sparameter_table.shape[0]))
            else:
                raise ValueError("Unsupported array dimension. Is {}, expected 3".format(sparameter_table.ndim))
        else:
            raise TypeError("Unsupported datatype. Expected numpy array.")

    def get_deembedding_sparameters(self):
        r'''get_deembedding_sparameters

        Returns the S-parameters used for de-embedding a measurement on the selected port.

        This includes interpolation of the parameters based on the configured carrier frequency. This method returns an empty array if no de-embedding is done.

        If you want to call this method just to get the required buffer size, you can pass 0 for **S-parameter Size** and VI_NULL for the **S-parameters** buffer.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

        Note: The port orientation for the returned S-parameters is normalized to SparameterOrientation.PORT1_TOWARDS_DUT.

        Returns:
            sparameters (numpy.array(dtype=numpy.complex128)): Returns an array of S-parameters. The S-parameters are returned in the following order: s11, s12, s21, s22.

        '''
        sparameters = self._interpreter.get_deembedding_sparameters()
        return sparameters

    @ivi_synchronized
    def get_all_named_waveform_names(self):
        r'''get_all_named_waveform_names

        Return names of the waveforms present in the memory.

        **Supported Devices** :PXIe-5830/5831/5840/5841/5842E

        Returns:
            waveform_names (list of str): Returns a list of string having waveform names.

        '''
        waveform_names = self._interpreter.get_all_named_waveform_names()
        return _converters.convert_comma_separated_string_to_list(waveform_names)

    @ivi_synchronized
    def get_all_script_names(self):
        r'''get_all_script_names

        Return names of the scripts present in the memory.

        **Supported Devices** :PXIe-5830/5831/5840/5841/5842E

        Returns:
            script_names (list of str): Returns a list of string having script names.

        '''
        script_names = self._interpreter.get_all_script_names()
        return _converters.convert_comma_separated_string_to_list(script_names)

    @ivi_synchronized
    def _get_external_calibration_last_date_and_time(self):
        r'''_get_external_calibration_last_date_and_time

        Returns the date and time of the last successful external calibration.

        The time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30PM, this method returns

        14 for the hours parameter and

        30 for the minutes parameter.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Returns:
            year (int): Returns the year of the last successful calibration.

            month (int): Returns the month of the last successful calibration.

            day (int): Returns the day of the last successful calibration.

            hour (int): Returns the hour of the last successful calibration.

            minute (int): Returns the minute of the last successful calibration.

            second (int): Returns the second of the last successful calibration.

        '''
        year, month, day, hour, minute, second = self._interpreter.get_external_calibration_last_date_and_time()
        return year, month, day, hour, minute, second

    @ivi_synchronized
    def get_ext_cal_last_date_and_time(self):
        '''get_ext_cal_last_date_and_time

        Returns the date and time of the last successful external calibration.

        The time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30PM, this method returns

        14 for the hours parameter and

        30 for the minutes parameter.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Returns:
            last_cal_datetime (hightime.datetime):

        '''
        year, month, day, hour, minute, second = self._get_external_calibration_last_date_and_time()
        return hightime.datetime(year, month, day, hour, minute, second)

    @ivi_synchronized
    def get_self_cal_last_date_and_time(self, module=enums.Module.PRIMARY_MODULE):
        '''get_self_cal_last_date_and_time

        Returns the date and time of the last successful self-calibration.

        The time returned is 24-hour local time. For example, if the device was calibrated at 2:30PM, this method returns

        14 for the hours parameter and

        30 for the minutes parameter.

        **Supported Devices** : PXI-5610, PXIe-5644/5645/5646, PXIe-5653, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Args:
            module (enums.Module): Specifies from which stand-alone module to retrieve the last successful self-calibration date and time.


        Returns:
            last_cal_datetime (hightime.datetime):

        '''
        year, month, day, hour, minute, second = self._get_self_calibration_date_and_time(module)
        return hightime.datetime(year, month, day, hour, minute, second)

    @ivi_synchronized
    def get_max_settable_power(self):
        r'''get_max_settable_power

        Returns the maximum settable output power level for the current configuration.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

        Returns:
            value (float): Returns maximum settable power level in dBm.

        '''
        value = self._interpreter.get_max_settable_power()
        return value

    @ivi_synchronized
    def get_script(self, script_name):
        r'''get_script

        Returns the content of specified script.

        **Supported Devices** :PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Args:
            script_name (str): Specifies the name of the script. This string is case-insensitive.


        Returns:
            script (str): Returns the script.

        '''
        script = self._interpreter.get_script(script_name)
        return script

    @ivi_synchronized
    def _get_self_calibration_date_and_time(self, module):
        r'''_get_self_calibration_date_and_time

        Returns the date and time of the last successful self-calibration.

        The time returned is 24-hour local time. For example, if the device was calibrated at 2:30PM, this method returns

        14 for the hours parameter and

        30 for the minutes parameter.

        **Supported Devices** : PXI-5610, PXIe-5644/5645/5646, PXIe-5653, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Args:
            module (enums.Module): Specifies from which stand-alone module to retrieve the last successful self-calibration date and time.


        Returns:
            year (int): Returns the year of the last successful calibration.

            month (int): Returns the month of the last successful calibration.

            day (int): Returns the day of the last successful calibration.

            hour (int): Returns the hour of the last successful calibration.

            minute (int): Returns the minute of the last successful calibration.

            second (int): Returns the second of the last successful calibration.

        '''
        if type(module) is not enums.Module:
            raise TypeError('Parameter module must be of type ' + str(enums.Module))
        year, month, day, hour, minute, second = self._interpreter.get_self_calibration_date_and_time(module)
        return year, month, day, hour, minute, second

    @ivi_synchronized
    def get_self_calibration_temperature(self, module=enums.Module.PRIMARY_MODULE):
        r'''get_self_calibration_temperature

        Returns the temperature, in degrees Celsius, of the device at the last successful self-calibration.

        **Supported Devices** : PXI-5610, PXIe-5653, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831 (IF only)/5832 (IF only)/5840/5841/5842/5860

        Args:
            module (enums.Module): Specifies from which stand-alone module to retrieve the last successful self-calibration temperature.
                                    **Default Value** : Module.PRIMARY_MODULE
                                    **Defined Values** :

                +-----------------------+----------------+---------------------------------------------------------------------+
                | Name                  | Value          | Description                                                         |
                +=======================+================+=====================================================================+
                | Module.PRIMARY_MODULE | 13000 (0x32c8) | The stand-alone device or the main module in a multi-module device. |
                +-----------------------+----------------+---------------------------------------------------------------------+
                | Module.AWG            | 13001 (0x32c9) | The AWG associated with the primary module.                         |
                +-----------------------+----------------+---------------------------------------------------------------------+
                | Module.LO             | 13002 (0x32ca) | The LO associated with the primary module.                          |
                +-----------------------+----------------+---------------------------------------------------------------------+


        Returns:
            temperature (float): Returns the temperature, in degrees Celsius, of the device at the last successful self-calibration.

        '''
        if type(module) is not enums.Module:
            raise TypeError('Parameter module must be of type ' + str(enums.Module))
        temperature = self._interpreter.get_self_calibration_temperature(module)
        return temperature

    @ivi_synchronized
    def get_terminal_name(self, signal, signal_identifier):
        r'''get_terminal_name

        Returns the fully-qualified name of the specified signal.

        The fully-qualified name is helpful to automatically route signals in a multisegment chassis.

        **Supported Devices** : PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_

        `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

        `Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_

        Args:
            signal (enums.Signal): Specifies the signal to query. **Defined Values** :

                +--------------------------------------------+---------+--------------------------------------------+
                | Name                                       | Value   | Description                                |
                +============================================+=========+============================================+
                | Signal.START_TRIGGER                       | 0 (0x0) | Exports a Start Trigger.                   |
                +--------------------------------------------+---------+--------------------------------------------+
                | Signal.SCRIPT_TRIGGER                      | 1 (0x1) | Exports a Script Trigger.                  |
                +--------------------------------------------+---------+--------------------------------------------+
                | Signal.MARKER_EVENT                        | 2 (0x2) | Exports a Marker Event.                    |
                +--------------------------------------------+---------+--------------------------------------------+
                | Signal.REF_CLOCK                           | 3 (0x3) | Exports the Reference Clock.               |
                +--------------------------------------------+---------+--------------------------------------------+
                | Signal.STARTED_EVENT                       | 4 (0x4) | Exports a Started Event.                   |
                +--------------------------------------------+---------+--------------------------------------------+
                | Signal.DONE_EVENT                          | 5 (0x5) | Exports a Done Event.                      |
                +--------------------------------------------+---------+--------------------------------------------+
                | NIRFSG_VAL_CONFIGURATION_LIST_STEP_TRIGGER | 6 (0x6) | Exports a Configuration List Step Trigger. |
                +--------------------------------------------+---------+--------------------------------------------+
                | NIRFSG_VAL_CONFIGURATION_SETTLED_EVENT     | 7 (0x7) | Exports a Configuration Settled Event.     |
                +--------------------------------------------+---------+--------------------------------------------+

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            signal_identifier (str): Specifies which instance of the selected signal to query. This parameter is necessary when you set the SIGNAL parameter to NIRFSG_VAL_SCRIPT_TRIGGER or Signal.MARKER_EVENT  . Otherwise, set the SIGNAL_IDENTIFIER parameter to "" (empty string). **Possible Values** :

                +------------------+-----------------------------+
                | Possible Value   | Description                 |
                +==================+=============================+
                | "marker0"        | Specifies Marker 0.         |
                +------------------+-----------------------------+
                | "marker1"        | Specifies Marker 1.         |
                +------------------+-----------------------------+
                | "marker2"        | Specifies Marker 2.         |
                +------------------+-----------------------------+
                | "marker3"        | Specifies Marker 3.         |
                +------------------+-----------------------------+
                | "scriptTrigger0" | Specifies Script Trigger 0. |
                +------------------+-----------------------------+
                | "scriptTrigger1" | Specifies Script Trigger 1. |
                +------------------+-----------------------------+
                | "scriptTrigger2" | Specifies Script Trigger 2. |
                +------------------+-----------------------------+
                | "scriptTrigger3" | Specifies Script Trigger 3. |
                +------------------+-----------------------------+

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            terminal_name (str): Returns the string to use as the source for other devices.

        '''
        if type(signal) is not enums.Signal:
            raise TypeError('Parameter signal must be of type ' + str(enums.Signal))
        terminal_name = self._interpreter.get_terminal_name(signal, signal_identifier)
        return terminal_name

    def _init_with_options(self, resource_name, id_query=False, reset_device=False, option_string=""):
        r'''_init_with_options

        Opens a session to the device you specify as the RESOURCE_NAME and returns a ViSession handle that you use to identify the NI-RFSG device in all subsequent NI-RFSG method calls.

        This method also configures the device through the OPTION_STRING input.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Simulating an NI RF Signal Generator <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/simulate.html>`_

        Note: For multichannel devices such as the PXIe-5860, the resource name must include the channel number to use. The channel number is specified by appending /*ChannelNumber* to the device name, where *ChannelNumber* is the channel number (0, 1, etc.). For example, if the device name is PXI1Slot2 and you want to use channel 0, use the resource name PXI1Slot2/0.

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Args:
            resource_name (str): Specifies the resource name of the device to initialize.

                For NI-DAQmx devices, the syntax is the device name specified in MAX. Typical default names for NI-DAQmx devices in MAX are Dev2 or PXISlot2. You can rename an NI-DAQmx device in MAX.

                You can also specify the name of an IVI logical name configured with the IVI Configuration utility. Refer to the *IVI* topic of the *Measurement & Automation Explorer Help* for more information.

                Note: NI-RFSG device names are not case-sensitive. However, all IVI names, such as logical names, are case-sensitive. If you use an IVI logical name, make sure the name is identical to the name shown in the IVI Configuration Utility.

            id_query (bool): Specifies whether you want NI-RFSG to perform an ID query.

                **Defined Values** :

                +-----------+--------------------------+
                | Value     | Description              |
                +===========+==========================+
                | True (1)  | Perform ID query.        |
                +-----------+--------------------------+
                | False (0) | Do not perform ID query. |
                +-----------+--------------------------+

            reset_device (bool): Specifies whether you want to reset the NI-RFSG device during the initialization procedure.

                **Defined Values** :

                +-----------+----------------------+
                | Value     | Description          |
                +===========+======================+
                | True (1)  | Reset device.        |
                +-----------+----------------------+
                | False (0) | Do not reset device. |
                +-----------+----------------------+

            option_string (dict): Specifies the initial value of certain properties for the session. The following table lists the properties and the name you pass in this parameter to identify the property.

                The format of this string consists of the following relations:
                "AttributeName=Value"

                where
                *AttributeName* is the name of the property and *Value* is the value to which the property is set. To set multiple properties, separate their assignments with a comma, as shown in the following option string:

                "RangeCheck=1,QueryInstrStatus=0,Cache=1,DriverSetup=AWG:pxi1slot4"

                The `DriverSetup string <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/driver_setup_string.html>`_ is required in order to simulate a specific device.


        Returns:
            new_vi (int): Returns a ViSession handle that you use to identify the NI-RFSG device in all subsequent NI-RFSG method calls.

        '''
        option_string = _converters.convert_init_with_options_dictionary(option_string)
        new_vi = self._interpreter.init_with_options(resource_name, id_query, reset_device, option_string)
        return new_vi

    @ivi_synchronized
    def _initiate(self):
        r'''_initiate

        Initiates signal generation, causing the NI-RFSG device to leave the Configuration state and enter the Generation state.

        If the settings have not been committed to the device before you call this method, they are committed by this method. The operation returns when the RF output signal settles. To return to the Configuration state, call the abort method.

        **Supported Devices** : PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_
        '''
        self._interpreter.initiate()

    @ivi_synchronized
    def perform_power_search(self):
        r'''perform_power_search

        Performs a power search if the alc_control property is disabled.

        Calling this method disables modulation for a short time while the device levels the output signal.

        **Supported Devices** : PXIe-5654 with PXIe-5696

        **Related Topics**

        `Power Search <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_power_search.html>`_

        Note: Power search temporarily enables the ALC, so ensure the appropriate included cable is connected between the PXIe-5654 ALCIN connector and the PXIe-5696 ALCOUT connector to successfully perform a power search.
        '''
        self._interpreter.perform_power_search()

    @ivi_synchronized
    def perform_thermal_correction(self):
        r'''perform_thermal_correction

        Corrects for any signal drift due to environmental temperature variation when generating the same signal for extended periods of time without a parameter change.

        Under normal circumstances of short-term signal generation, NI-RFSG performs thermal correction automatically by ensuring stable power levels, and you do not need to call this method.

        Use this method when generating the same signal for an extended period of time in a temperature-fluctuating environment. The NI-RFSG device must be in the Generation state before calling this method.

        **Supported Devices** : PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Thermal Management <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/thermal_management.html>`_

        `Impairment Calibration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/vector_calibration.html>`_
        '''
        self._interpreter.perform_thermal_correction()

    @ivi_synchronized
    def query_arb_waveform_capabilities(self):
        r'''query_arb_waveform_capabilities

        Queries and returns the waveform capabilities of the NI-RFSG device.

        These capabilities are related to the current device configuration. The NI-RFSG device must be in the Configuration or the Generation state before calling this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Returns:
            max_number_waveforms (int): Returns the value of the arb_max_number_waveforms property. This value is the maximum number of waveforms you can write.

            waveform_quantum (int): Returns the value of the arb_waveform_quantum property. If the waveform quantum is *q*, then the size of the waveform that you write should be a multiple of *q*. The units are expressed in samples.

            min_waveform_size (int): Returns the value of the arb_waveform_size_min property. The number of samples of the waveform that you write must be greater than or equal to this value.

            max_waveform_size (int): Returns the value of the arb_waveform_size_max property. The number of samples of the waveform that you write must be less than or equal to this value.

        '''
        max_number_waveforms, waveform_quantum, min_waveform_size, max_waveform_size = self._interpreter.query_arb_waveform_capabilities()
        return max_number_waveforms, waveform_quantum, min_waveform_size, max_waveform_size

    @ivi_synchronized
    def read_and_download_waveform_from_file_tdms(self, waveform_name, file_path, waveform_index):
        r'''read_and_download_waveform_from_file_tdms

        Reads the waveforms from a TDMS file and downloads one waveform into each of the NI RF vector signal generators.

        This method reads the following information from the TDMS file and writes it into the NI-RFSG session:

        - Sample Rate
        - PAPR
        - Runtime Scaling
        - RF Blanking Marker Locations
        - RF Blanking Enabled
        - Burst Start Locations
        - Burst Stop Locations
        - RF Blanking Marker Source
        - Signal Bandwidth
        - Waveform Size

        If RF blanking marker locations are present in the file but burst locations are not present, burst locations are calculated from RF blanking marker locations and stored in the NI-RFSG session.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842

        Args:
            waveform_name (str): Specifies the name used to store the waveform. This string is case-insensitive.

                Example:

                "waveform::waveform0"

            file_path (str): Specifies the absolute path to the TDMS file from which the NI-RFSG reads the waveforms.

            waveform_index (int): Specifies the index of the waveform to be read from the TDMS file.

        '''
        self._interpreter.read_and_download_waveform_from_file_tdms(waveform_name, file_path, waveform_index)

    @ivi_synchronized
    def reset_device(self):
        r'''reset_device

        Performs a hard reset on the device which consists of the following actions:

        - Signal generation is stopped.
        - All routes are released.
        - External bidirectional terminals are tristated.
        - FPGAs are reset.
        - Hardware is configured to its default state.
        - All session properties are reset to their default states.

        During a device reset, routes of signals between this and other devices are released, regardless of which device created the route.

        - PXI-5610, PXI-5670/5671, PXIe-5672-- After calling this method, the device requires 25 seconds before returning to full functionality. NI-RFSG enforces this condition by adding a wait, if needed, the next time you try to access the device.

        **Supported Devices** : PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E

        **Related Topics**

        `Thermal Shutdown <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/thermal_shutdown_monitoring_5650_5651_5652.html>`_

        Note: You must call the reset_device method if the NI-RFSG device has shut down because of a high-temperature condition.
        '''
        self._interpreter.reset_device()

    @ivi_synchronized
    def reset_with_defaults(self):
        r'''reset_with_defaults

        Performs a software reset of the device, returning it to the default state and applying any initial default settings from the IVI Configuration Store.

        **Supported Devices** : PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696,PXI-5670/5671, PXIe-5672/5673/5673E
        '''
        self._interpreter.reset_with_defaults()

    @ivi_synchronized
    def reset_with_options(self, steps_to_omit):
        r'''reset_with_options

        Resets all properties to default values and specifies steps to omit during the reset process, such as signal routes.

        By default, this method exhibits the same behavior as Reset. You can specify steps to omit using the steps to omit parameter. For example, if you specify ResetWithOptionsStepsToOmit.ROUTES for the STEPS_TO_OMIT parameter, this method does not release signal routes during the reset process.

        When routes of signals between two devices are released, they are released regardless of which device created the route.

        To avoid resetting routes on PXIe-5820/5830/5831/5832/5840/5841/5842/5860 that are in use by NI-RFSA sessions, NI recommends using this method instead of Reset, with STEPS_TO_OMIT set to ResetWithOptionsStepsToOmit.ROUTES.

        **Supported Devices** : PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_

        `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Args:
            steps_to_omit (Bitwise combination of enums.ResetWithOptionsStepsToOmit flags): Specifies a list of steps to skip during the reset process. The default value is ResetWithOptionsStepsToOmit.NONE, which specifies that no step is omitted during reset. **Defined Values** :

                +------------------------------------------------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | Name                                           | Value   | Description                                                                                                                                                                                                |
                +================================================+=========+============================================================================================================================================================================================================+
                | ResetWithOptionsStepsToOmit.NONE               | 0 (0x0) | No step is omitted during reset.                                                                                                                                                                           |
                +------------------------------------------------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ResetWithOptionsStepsToOmit.WAVEFORMS          | 1 (0x1) | Omits clearing waveforms.                                                                                                                                                                                  |
                +------------------------------------------------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ResetWithOptionsStepsToOmit.SCRIPTS            | 2 (0x2) | Omits clearing scripts.                                                                                                                                                                                    |
                +------------------------------------------------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ResetWithOptionsStepsToOmit.ROUTES             | 4 (0x4) | Omits the routing reset step. Routing is preserved after a reset. However, routing related properties are reset to default, and routing is released if the default properties are committed after a reset. |
                +------------------------------------------------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ResetWithOptionsStepsToOmit.DEEMBEDDING_TABLES | 8 (0x8) | Omits deleting de-embedding tables. This step is valid only for the PXIe-5830/5831/5832/5840.                                                                                                              |
                +------------------------------------------------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

                Note: ResetWithOptionsStepsToOmit.ROUTES is not supported in external calibration or alignment sessions.
                You can combine multiple enums.ResetWithOptionsStepsToOmit flags using the bitwise OR (|) operator.

        '''
        if type(steps_to_omit) is not enums.ResetWithOptionsStepsToOmit:
            raise TypeError('Parameter steps_to_omit must be of type ' + str(enums.ResetWithOptionsStepsToOmit))
        self._interpreter.reset_with_options(steps_to_omit)

    @ivi_synchronized
    def select_arb_waveform(self, waveform_name):
        r'''select_arb_waveform

        Specifies the waveform that is generated upon a call to the _initiate method when the generation_mode property is set to GenerationMode.ARB_WAVEFORM.

        You must specify a waveform using the NAME parameter if you have written multiple waveforms. The NI-RFSG device must be in the Configuration state before you call this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Args:
            waveform_name (str): Specifies the name of the stored waveform to generate. This is a case-insensitive alphanumeric string that does not use reserved words. NI-RFSG sets the arb_selected_waveform property to this value.

        '''
        self._interpreter.select_arb_waveform(waveform_name)

    @ivi_synchronized
    def self_cal(self):
        r'''self_cal

        Performs an internal self-calibration on the device and associated modules that support self-calibration.

        If the calibration is successful, new calibration data and constants are stored in the onboard nonvolatile memory of the module.

        The PXIe-5841 maintains separate self-calibration data for both the PXIe-5841 standalone and when associated with the PXIe-5655. Use this method once for each intended configuration.

        **Supported Devices** : PXI-5610, PXIe-5653, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Note: If there is an existing NI-RFSA session open for the same PXIe-5820/5830/5831/5832/5840/5841/5842/5860 while this method runs, it may remain open but cannot be used for operations that access the hardware, for example niRFSA_Commit or niRFSA_Initiate. For the existing open session to use the new self-calibration data, the session will need to be closed and reopened.

        **PXIe-5860**

        While this VI is running on one channel, if there are any existing NI-RFSG or NI-RFSA sessions open on the other channel, they may remain open but cannot be used for operations that access the hardware, for example niRFSG Commit or niRFSG Initiate or niRFSA Commit or niRFSA Initiate. For the existing open session to use the new self-calibration data, the session will need to be closed and reopened.
        '''
        self._interpreter.self_cal()

    @ivi_synchronized
    def self_calibrate_range(self, steps_to_omit, min_frequency, max_frequency, min_power_level, max_power_level):
        r'''self_calibrate_range

        Self-calibrates all configurations within the specified frequency and peak power level limits.

        Self-calibration range data is valid until you restart the system or call the clear_self_calibrate_range method.

        NI recommends that no external signals are present on the RF In or IQ In ports during the calibration.

        For best results, NI recommends that you perform self-calibration without omitting any steps. However, if certain aspects of performance are less important for your application, you can omit certain steps for faster calibration.

        **Supported Devices** : PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842

        Note: - This method does not update self-calibration date and temperature.

         - If there is an existing NI-RFSA session open for the same PXIe-5644/5645/5646, it may remain open but cannot be used while this method runs.

         - If there is an existing NI-RFSA session open for the same PXIe-5820/5830/5831/5832/5840/5841/5842 while this method runs, it may remain open but cannot be used for operations that access the hardware, for example niRFSA_Commit or niRFSA_Initiate.

        Args:
            steps_to_omit (Bitwise combination of enums.SelfCalibrateRangeStepsToOmit flags): Specifies which calibration steps to skip during the self-calibration process. The default value is an empty array, which indicates that no calibration steps are omitted.

                **Default Value** : SelfCalibrateRangeStepsToOmit.OMIT_NONE

                **Defined Values:**

                +-----------------------------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
                | Name                                                | Value     | Description                                                                                                         |
                +=====================================================+===========+=====================================================================================================================+
                | SelfCalibrateRangeStepsToOmit.OMIT_NONE             | 0 (0x0)   | No calibration steps are omitted.                                                                                   |
                +-----------------------------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
                | SelfCalibrateRangeStepsToOmit.LO_SELF_CAL           | 1 (0x1)   | Omits the LO Self Cal step. If you omit this step, the power level of the LO is not adjusted.                       |
                +-----------------------------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
                | SelfCalibrateRangeStepsToOmit.POWER_LEVEL_ACCURACY  | 2 (0x2)   | Omits the Power Level Accuracy step. If you omit this step, the power level accuracy of the device is not adjusted. |
                +-----------------------------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
                | SelfCalibrateRangeStepsToOmit.RESIDUAL_LO_POWER     | 4 (0x4)   | Omits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted.         |
                +-----------------------------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
                | SelfCalibrateRangeStepsToOmit.IMAGE_SUPPRESSION     | 8 (0x8)   | Omits the Image Suppression step. If you omit this step, the Residual Sideband Image performance is not adjusted.   |
                +-----------------------------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
                | SelfCalibrateRangeStepsToOmit.SYNTHESIZER_ALIGNMENT | 16 (0x10) | Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.    |
                +-----------------------------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------+

                Note: You can combine multiple enums.SelfCalibrateRangeStepsToOmit flags using the bitwise OR (|) operator.

            min_frequency (float): Specifies the minimum frequency to calibrate.

            max_frequency (float): Specifies the maximum frequency to calibrate.

            min_power_level (float): Specifies the minimum power level to calibrate.

            max_power_level (float): Specifies the maximum power level to calibrate.

        '''
        if type(steps_to_omit) is not enums.SelfCalibrateRangeStepsToOmit:
            raise TypeError('Parameter steps_to_omit must be of type ' + str(enums.SelfCalibrateRangeStepsToOmit))
        self._interpreter.self_calibrate_range(steps_to_omit, min_frequency, max_frequency, min_power_level, max_power_level)

    @ivi_synchronized
    def set_arb_waveform_next_write_position(self, waveform_name, relative_to, offset):
        r'''set_arb_waveform_next_write_position

        Configures the start position to use for writing a waveform before calling the WriteArbWaveform method.

        This method allows you to write to arbitrary locations within the waveform. These settings apply only to the next write to the waveform specified by the **name** input of the allocate_arb_waveform method or the WriteArbWaveform method. Subsequent writes to that waveform begin where the last write ended, unless this method is called again.

        **Supported Devices** : PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Note: If you use this method to write the waveform that is currently generating, an undefined output may result.

        Args:
            waveform_name (str): Specifies the name of the waveform. This string is case-insensitive and alphanumeric, and it cannot use `reserved words <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_instructions.html>`_.

            relative_to (enums.RelativeTo): Specifies the reference position in the waveform. The position and OFFSET together determine where to start loading data into the waveform.

                **Defined Values:**

                +------------------------------+---------------+------------------------------------------------------------------+
                | Name                         | Value         | Description                                                      |
                +==============================+===============+==================================================================+
                | RelativeTo.START_OF_WAVEFORM | 8000 (0x1f40) | The reference position is relative to the start of the waveform. |
                +------------------------------+---------------+------------------------------------------------------------------+
                | RelativeTo.CURRENT_POSITION  | 8001 (0x1f41) | The reference position is relative to the current position.      |
                +------------------------------+---------------+------------------------------------------------------------------+

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

            offset (int): Specifies the offset from the **relative to** parameter at which to start loading the data into the waveform.

        '''
        if type(relative_to) is not enums.RelativeTo:
            raise TypeError('Parameter relative_to must be of type ' + str(enums.RelativeTo))
        self._interpreter.set_arb_waveform_next_write_position(waveform_name, relative_to, offset)

    @ivi_synchronized
    def wait_until_settled(self, max_time_milliseconds=hightime.timedelta(seconds=10.0)):
        r'''wait_until_settled

        Waits until the RF output signal has settled. This method is useful for devices that support changes while in the Generation state.

        Call this method after making a dynamic change to wait for the output signal to settle.

        You can also call this method after calling the commit method to wait for changes to settle. The wait_until_settled method is not required after calling the _initiate method because the _initiate automatically waits for the output to settle.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Args:
            max_time_milliseconds (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the maximum time the method waits for the output to settle. If the maximum time is exceeded, this method returns an error. The units are expressed in milliseconds.

                **Default Value** : 10000

        '''
        max_time_milliseconds = _converters.convert_timedelta_to_milliseconds_int32(max_time_milliseconds)
        self._interpreter.wait_until_settled(max_time_milliseconds)

    @ivi_synchronized
    def _write_arb_waveform_complex_f32(self, waveform_name, waveform_data_array, more_data_pending):
        r'''_write_arb_waveform_complex_f32

        Writes an arbitrary waveform to the NI-RFSG device starting at the position of the last data written in onboard memory.

        This method accepts the complex baseband data in the form of complex singles. If the waveform to write is already allocated using the allocate_arb_waveform method, the more_data_pending parameter is ignored. The PXI-5670/5671 must be in the Configuration state before you call this method. When streaming is enabled, you can call this method when the PXIe-5672/5673/5673E or PXIe-5820/5830/5831/5832/5840/5841/5842/5860 is in the Generation state.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Streaming <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/streaming.html>`_

        `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/assigning-properties-or-properties-to-a-wavef.html>`_

        Note: On the PXIe-5644/5645/5646, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860, the more_data_pending parameter is always ignored. To write data in blocks on these devices, you must allocate the waveform before writing it.

        Args:
            waveform_name (str): Specifies the name used to identify the waveform. This string is case-insensitive and alphanumeric, and it does not use reserved words.

            waveform_data_array (numpy.array(dtype=numpy.complex64)): Specifies the array of data to load into the waveform. The array must have at least as many elements as the value in the **size_in_samples** parameter in the allocate_arb_waveform method.

            more_data_pending (bool): Specifies whether or not the data block contains the end of the waveform. Set this parameter to True to allow data to be appended later to the waveform. Splitting the waveform into multiple data blocks can reduce the memory requirements of the write operation. Append data to a previously written waveform by using the same waveform in the WAVEFORM_NAME parameter. Set more_data_pending to False to indicate that this data block contains the end of the waveform. If the waveform is already allocated, this parameter is ignored.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

        '''
        import numpy

        if type(waveform_data_array) is not numpy.ndarray:
            raise TypeError('waveform_data_array must be {0}, is {1}'.format(numpy.ndarray, type(waveform_data_array)))
        if numpy.isfortran(waveform_data_array) is True:
            raise TypeError('waveform_data_array must be in C-order')
        if waveform_data_array.dtype is not numpy.dtype('complex64'):
            raise TypeError('waveform_data_array must be numpy.ndarray of dtype=complex64, is ' + str(waveform_data_array.dtype))
        if waveform_data_array.ndim != 1:
            raise TypeError('waveform_data_array must be numpy.ndarray of dimension=1, is ' + str(waveform_data_array.ndim))
        self._interpreter.write_arb_waveform_complex_f32(waveform_name, waveform_data_array, more_data_pending)

    @ivi_synchronized
    def _write_arb_waveform_complex_f64(self, waveform_name, waveform_data_array, more_data_pending):
        r'''_write_arb_waveform_complex_f64

        Writes an arbitrary waveform to the NI-RFSG device starting at the position of the last data written in onboard memory.

        This method accepts the complex baseband data in the form of complex doubles. If the waveform to write is already allocated using the allocate_arb_waveform, the more_data_pending parameter is ignored. The PXI-5670/5671 must be in the Configuration state before you call this method. When streaming is enabled, you can call this method when the PXIe-5672/5673/5673E or PXIe-5820/5830/5831/5832/5840/5841/5842 is in the Generation state.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

        **Related Topics**

        `Streaming <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/streaming.html>`_

        `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/assigning-properties-or-properties-to-a-wavef.html>`_

        Note: On the PXIe-5644/5645/5646, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842, the more_data_pending parameter is always ignored. To write data in blocks on these devices, you must allocate the waveform before writing it.

        Args:
            waveform_name (str): Specifies the name used to identify the waveform. This string is case-insensitive and alphanumeric, and it does not use reserved words.

            waveform_data_array (numpy.array(dtype=numpy.complex128)): Specifies the array of data to load into the waveform. The array must have at least as many elements as the value in the **size_in_samples** parameter in the allocate_arb_waveform method.

            more_data_pending (bool): Specifies whether or not the data block contains the end of the waveform. Set this parameter to True to allow data to be appended later to the waveform. Splitting the waveform into multiple data blocks can reduce the memory requirements of the write operation. Append data to a previously written waveform by using the same waveform in the **name** parameter. Set more_data_pending to False to indicate that this data block contains the end of the waveform. If the waveform is already allocated, this parameter is ignored.

        '''
        import numpy

        if type(waveform_data_array) is not numpy.ndarray:
            raise TypeError('waveform_data_array must be {0}, is {1}'.format(numpy.ndarray, type(waveform_data_array)))
        if numpy.isfortran(waveform_data_array) is True:
            raise TypeError('waveform_data_array must be in C-order')
        if waveform_data_array.dtype is not numpy.dtype('complex128'):
            raise TypeError('waveform_data_array must be numpy.ndarray of dtype=complex128, is ' + str(waveform_data_array.dtype))
        if waveform_data_array.ndim != 1:
            raise TypeError('waveform_data_array must be numpy.ndarray of dimension=1, is ' + str(waveform_data_array.ndim))
        self._interpreter.write_arb_waveform_complex_f64(waveform_name, waveform_data_array, more_data_pending)

    @ivi_synchronized
    def _write_arb_waveform_complex_i16(self, waveform_name, waveform_data_array):
        r'''_write_arb_waveform_complex_i16

        Writes an arbitrary waveform to the NI-RFSG device starting at the position of the last data written in onboard memory.

        This method accepts the interleaved I/Q data of a complex baseband signal. The PXI-5670/5671 must be in the Configuration state before you call this method. When streaming is enabled, this method can be called when the PXIe-5672/5673/5673E or PXIe-5820/5830/5831/5832/5840/5841/5842/5860 is in the Generation state.

        **Supported Devices** : PXIe-5644/5645/5646, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Streaming <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/streaming.html>`_

        `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/assigning-properties-or-properties-to-a-wavef.html>`_

        Note: This method only supports PowerLevelType.PEAK mode as specified in the power_level_type property. If you download a waveform when using this method, you cannot set the power_level_type to PowerLevelType.AVERAGE without causing error in the output.

        Args:
            waveform_name (str): Specifies the name used to identify the waveform. This string is case-insensitive and alphanumeric, and it does not use reserved words.

            waveform_data_array (numpy.array(dtype=numpy.int16)): Specifies the array of data to load into the waveform. The array must have at least as many elements as the value in the **size_in_samples** parameter in the allocate_arb_waveform method.

        '''
        import numpy

        if type(waveform_data_array) is not numpy.ndarray:
            raise TypeError('waveform_data_array must be {0}, is {1}'.format(numpy.ndarray, type(waveform_data_array)))
        if numpy.isfortran(waveform_data_array) is True:
            raise TypeError('waveform_data_array must be in C-order')
        if waveform_data_array.dtype is not numpy.dtype('int16'):
            raise TypeError('waveform_data_array must be numpy.ndarray of dtype=int16, is ' + str(waveform_data_array.dtype))
        if waveform_data_array.ndim != 1:
            raise TypeError('waveform_data_array must be numpy.ndarray of dimension=1, is ' + str(waveform_data_array.ndim))
        self._interpreter.write_arb_waveform_complex_i16(waveform_name, waveform_data_array)

    def write_arb_waveform(self, waveform_name, waveform_data_array, more_data_pending=False):
        '''write_arb_waveform

        Writes an arbitrary waveform to the NI-RFSG device starting at the position of the last data written in onboard memory.

        This method accepts the complex baseband data in the form of numpy array of numpy.complex64 or numpy.complex128 or interleaved numpy array of numpy.int16. If the waveform to write is already allocated using the allocate_arb_waveform, the more_data_pending parameter is ignored. The PXI-5670/5671 must be in the Configuration state before you call this method. When streaming is enabled, you can call this method when the PXIe-5672/5673/5673E or PXIe-5820/5830/5831/5832/5840/5841/5842/5860 is in the Generation state.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Streaming <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/streaming.html>`_

        `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/assigning-properties-or-properties-to-a-wavef.html>`_

        Note: On the PXIe-5644/5645/5646, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860, the more_data_pending parameter is always ignored. To write data in blocks on these devices, you must allocate the waveform before writing it.
        If you are writing interleaved numpy array of numpy.int16, then this method only supports PowerLevelType.PEAK mode as specified in the power_level_type property. If you download a waveform as interleaved numpy array of numpy.int16 when using this method, you cannot set the power_level_type to PowerLevelType.AVERAGE without causing error in the output.

        Args:
            waveform_name (str): Specifies the name used to identify the waveform. This string is case-insensitive and alphanumeric, and it does not use reserved words.

            waveform_data_array (numpy array of numpy.complex64, numpy array of numpy.complex128 or interleaved complex data in the form of numpy array of numpy.int16): Specifies the array of data to load into the waveform. The array must have at least as many elements as the value in the **size_in_samples** parameter in the allocate_arb_waveform method.

            more_data_pending (bool): Specifies whether or not the data block contains the end of the waveform. Set this parameter to True to allow data to be appended later to the waveform. Splitting the waveform into multiple data blocks can reduce the memory requirements of the write operation. Append data to a previously written waveform by using the same waveform in the **name** parameter. Set more_data_pending to False to indicate that this data block contains the end of the waveform. If the waveform is already allocated, this parameter is ignored.

        '''
        import numpy
        if str(type(waveform_data_array)).find("'numpy.ndarray'") != -1:
            if waveform_data_array.dtype == numpy.complex128:
                return self._write_arb_waveform_complex_f64(waveform_name, waveform_data_array, more_data_pending)
            elif waveform_data_array.dtype == numpy.complex64:
                return self._write_arb_waveform_complex_f32(waveform_name, waveform_data_array, more_data_pending)
            elif waveform_data_array.dtype == numpy.int16:
                return self._write_arb_waveform_complex_i16(waveform_name, waveform_data_array)
            else:
                raise TypeError("Unsupported datatype. Is {}, expected {} or {} or {}".format(waveform_data_array.dtype, numpy.complex128, numpy.complex64, numpy.int16))
        else:
            raise TypeError("Unsupported datatype. Expected numpy array of {} or {} or {}".format(numpy.complex128, numpy.complex64, numpy.int16))

    @ivi_synchronized
    def write_script(self, script):
        r'''write_script

        Writes a script to the device to control waveform generation in Script mode.

        First, configure your device for Script mode by setting the generation_mode property. The NI-RFSG device must be in the Configuration state before calling the write_script method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Scripting Instructions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_instructions.html>`_--Refer to this topic for more information about VST restrictions on scripts.

        `Common Scripting Use Cases <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_use_cases.html>`_

        Note: If you are using an RF vector signal transceiver (VST) device, some script instructions may not be supported.

        Args:
            script (str): Specifies a string containing a syntactically correct script. NI-RFSG supports multiple scripts that are selected with the selected_script property. Refer to `Scripting Instructions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_instructions.html>`_ for more information about using scripts.

        '''
        self._interpreter.write_script(script)

    def _close(self):
        r'''_close

        Aborts any signal generation in progress and destroys the instrument driver session.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_

        `NI-RFSG Programming State Model <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5670_programming_state_model.html>`_
        '''
        self._interpreter.close()

    @ivi_synchronized
    def self_test(self):
        '''self_test

        Performs a self-test on the NI-RFSG device and returns the test results.

        This method performs a simple series of tests to ensure that the NI-RFSG device is powered up and responding.

        This method does not affect external I/O connections or connections between devices. Complete functional testing and calibration are not performed by this method. The NI-RFSG device must be in the Configuration state before you call this method.

        **Supported Devices** : PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Device Warm-Up <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/warmup.html>`_

        +----------------+------------------+
        | Self-Test Code | Description      |
        +================+==================+
        | 0              | Passed self-test |
        +----------------+------------------+
        | 1              | Self-test failed |
        +----------------+------------------+
        '''
        code, msg = self._self_test()
        if code:
            raise errors.SelfTestError(code, msg)
        return None

    @ivi_synchronized
    def reset(self):
        r'''reset

        Resets all properties to their default values and moves the NI-RFSG device to the Configuration state.

        This method aborts the generation, deletes all de-embedding tables, clears all routes, and resets session properties to their initial values. During a reset, routes of signals between this and other devices are released, regardless of which device created the route.

        Generally, calling this method instead of the reset_device method is acceptable. The Reset method executes faster than the reset_device method.

        To avoid resetting routes on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860 that are in use by NI-RFSA sessions, NI recommends using the reset_with_options method, with **stepsToOmit** set to ResetWithOptionsStepsToOmit.ROUTES .

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Note: This method resets all configured routes for the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860 in NI-RFSA and NI-RFSG.
        '''
        self._interpreter.reset()

    @ivi_synchronized
    def _self_test(self):
        r'''_self_test

        Performs a self-test on the NI-RFSG device and returns the test results.

        This method performs a simple series of tests to ensure that the NI-RFSG device is powered up and responding.

        This method does not affect external I/O connections or connections between devices. Complete functional testing and calibration are not performed by this method. The NI-RFSG device must be in the Configuration state before you call this method.

        **Supported Devices** : PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Device Warm-Up <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/warmup.html>`_

        Returns:
            self_test_result (int): This parameter contains the value returned from the NI-RFSG device self test.

                +----------------+------------------+
                | Self-Test Code | Description      |
                +================+==================+
                | 0              | Self test passed |
                +----------------+------------------+
                | 1              | Self test failed |
                +----------------+------------------+

            self_test_message (str): Returns the self-test response string from the NI-RFSG device. For an explanation of the string contents, refer to the **status** parameter of this method.

                You must pass a ViChar array with at least 256 bytes.

        '''
        self_test_result, self_test_message = self._interpreter.self_test()
        return self_test_result, self_test_message
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nirfsg/nirfsg/unit_tests/_matchers.py sha256=cd0b98524db709f5a535fb8090d0f7c927c6bc6f5e53879e126743d747e7e71d bytes=14043 -->
## FILE: generated/nirfsg/nirfsg/unit_tests/_matchers.py

- repository: `ni/nimi-python`
- source_path: `generated/nirfsg/nirfsg/unit_tests/_matchers.py`
- sha256: `cd0b98524db709f5a535fb8090d0f7c927c6bc6f5e53879e126743d747e7e71d`
- bytes: 14043

````python
# -*- coding: utf-8 -*-
# This file was generated
'''Matcher classes used by unit tests in order to set mock expectations.
These work well with our visatype definitions.
'''

import ctypes
import nirfsg._complextype as _complextype
import nirfsg._visatype as _visatype
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


def _compare_complex_number_arrays(expected, actual):
    for i in range(expected.expected_size):
        expected_value = expected.expected_data[i]
        actual_value = actual[i]
        if expected_value.real != actual_value.real or expected_value.imag != actual_value.imag:
            return False
    return True


class NIComplexNumberPointerMatcher(_PointerMatcher):
    def __init__(self, expected_data, expected_size):
        _PointerMatcher.__init__(self, _complextype.NIComplexNumber)
        self.expected_data = expected_data
        self.expected_size = expected_size

    def __eq__(self, other):
        _PointerMatcher.__eq__(self, other)
        return _compare_complex_number_arrays(self, other)

    def __repr__(self):
        return f"NIComplexNumberPointerMatcher({self.expected_data})"


class NIComplexNumberF32PointerMatcher(_PointerMatcher):
    def __init__(self, expected_data, expected_size):
        _PointerMatcher.__init__(self, _complextype.NIComplexNumberF32)
        self.expected_data = expected_data
        self.expected_size = expected_size

    def __eq__(self, other):
        _PointerMatcher.__eq__(self, other)
        return _compare_complex_number_arrays(self, other)

    def __repr__(self):
        return f"NIComplexNumberF32PointerMatcher({self.expected_data})"


class NIComplexI16PointerMatcher(_PointerMatcher):
    def __init__(self, expected_data, expected_size):
        _PointerMatcher.__init__(self, _complextype.NIComplexI16)
        self.expected_data = expected_data
        self.expected_size = expected_size

    def __eq__(self, other):
        _PointerMatcher.__eq__(self, other)
        return _compare_complex_number_arrays(self, other)

    def __repr__(self):
        return f"NIComplexI16PointerMatcher({self.expected_data})"


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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nirfsg/nirfsg/unit_tests/_mock_helper.py sha256=5d5d71c3e011fdcdadfd874bfc0536618694cc7032b6bc409582bb7b10e277a8 bytes=73381 -->
## FILE: generated/nirfsg/nirfsg/unit_tests/_mock_helper.py

- repository: `ni/nimi-python`
- source_path: `generated/nirfsg/nirfsg/unit_tests/_mock_helper.py`
- sha256: `5d5d71c3e011fdcdadfd874bfc0536618694cc7032b6bc409582bb7b10e277a8`
- bytes: 73381

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
        self._defaults['AllocateArbWaveform'] = {}
        self._defaults['AllocateArbWaveform']['return'] = 0
        self._defaults['ChangeExternalCalibrationPassword'] = {}
        self._defaults['ChangeExternalCalibrationPassword']['return'] = 0
        self._defaults['CheckGenerationStatus'] = {}
        self._defaults['CheckGenerationStatus']['return'] = 0
        self._defaults['CheckGenerationStatus']['isDone'] = None
        self._defaults['CheckIfScriptExists'] = {}
        self._defaults['CheckIfScriptExists']['return'] = 0
        self._defaults['CheckIfScriptExists']['scriptExists'] = None
        self._defaults['CheckIfWaveformExists'] = {}
        self._defaults['CheckIfWaveformExists']['return'] = 0
        self._defaults['CheckIfWaveformExists']['waveformExists'] = None
        self._defaults['ClearAllArbWaveforms'] = {}
        self._defaults['ClearAllArbWaveforms']['return'] = 0
        self._defaults['ClearArbWaveform'] = {}
        self._defaults['ClearArbWaveform']['return'] = 0
        self._defaults['ClearSelfCalibrateRange'] = {}
        self._defaults['ClearSelfCalibrateRange']['return'] = 0
        self._defaults['Commit'] = {}
        self._defaults['Commit']['return'] = 0
        self._defaults['ConfigureDeembeddingTableInterpolationLinear'] = {}
        self._defaults['ConfigureDeembeddingTableInterpolationLinear']['return'] = 0
        self._defaults['ConfigureDeembeddingTableInterpolationNearest'] = {}
        self._defaults['ConfigureDeembeddingTableInterpolationNearest']['return'] = 0
        self._defaults['ConfigureDeembeddingTableInterpolationSpline'] = {}
        self._defaults['ConfigureDeembeddingTableInterpolationSpline']['return'] = 0
        self._defaults['ConfigureDigitalEdgeScriptTrigger'] = {}
        self._defaults['ConfigureDigitalEdgeScriptTrigger']['return'] = 0
        self._defaults['ConfigureDigitalEdgeStartTrigger'] = {}
        self._defaults['ConfigureDigitalEdgeStartTrigger']['return'] = 0
        self._defaults['ConfigureDigitalLevelScriptTrigger'] = {}
        self._defaults['ConfigureDigitalLevelScriptTrigger']['return'] = 0
        self._defaults['ConfigureRF'] = {}
        self._defaults['ConfigureRF']['return'] = 0
        self._defaults['ConfigureRefClock'] = {}
        self._defaults['ConfigureRefClock']['return'] = 0
        self._defaults['ConfigureSoftwareScriptTrigger'] = {}
        self._defaults['ConfigureSoftwareScriptTrigger']['return'] = 0
        self._defaults['ConfigureSoftwareStartTrigger'] = {}
        self._defaults['ConfigureSoftwareStartTrigger']['return'] = 0
        self._defaults['CreateDeembeddingSparameterTableArray'] = {}
        self._defaults['CreateDeembeddingSparameterTableArray']['return'] = 0
        self._defaults['CreateDeembeddingSparameterTableS2PFile'] = {}
        self._defaults['CreateDeembeddingSparameterTableS2PFile']['return'] = 0
        self._defaults['DeleteAllDeembeddingTables'] = {}
        self._defaults['DeleteAllDeembeddingTables']['return'] = 0
        self._defaults['DeleteDeembeddingTable'] = {}
        self._defaults['DeleteDeembeddingTable']['return'] = 0
        self._defaults['DeleteScript'] = {}
        self._defaults['DeleteScript']['return'] = 0
        self._defaults['DisableScriptTrigger'] = {}
        self._defaults['DisableScriptTrigger']['return'] = 0
        self._defaults['DisableStartTrigger'] = {}
        self._defaults['DisableStartTrigger']['return'] = 0
        self._defaults['ErrorMessage'] = {}
        self._defaults['ErrorMessage']['return'] = 0
        self._defaults['ErrorMessage']['errorMessage'] = None
        self._defaults['GetAllNamedWaveformNames'] = {}
        self._defaults['GetAllNamedWaveformNames']['return'] = 0
        self._defaults['GetAllNamedWaveformNames']['actualBufferSize'] = None
        self._defaults['GetAllNamedWaveformNames']['waveformNames'] = None
        self._defaults['GetAllScriptNames'] = {}
        self._defaults['GetAllScriptNames']['return'] = 0
        self._defaults['GetAllScriptNames']['actualBufferSize'] = None
        self._defaults['GetAllScriptNames']['scriptNames'] = None
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
        self._defaults['GetAttributeViSession'] = {}
        self._defaults['GetAttributeViSession']['return'] = 0
        self._defaults['GetAttributeViSession']['value'] = None
        self._defaults['GetAttributeViString'] = {}
        self._defaults['GetAttributeViString']['return'] = 0
        self._defaults['GetAttributeViString']['value'] = None
        self._defaults['GetDeembeddingSparameters'] = {}
        self._defaults['GetDeembeddingSparameters']['return'] = 0
        self._defaults['GetDeembeddingSparameters']['sparameters'] = None
        self._defaults['GetDeembeddingSparameters']['numberOfSparameters'] = None
        self._defaults['GetDeembeddingSparameters']['numberOfPorts'] = None
        self._defaults['GetDeembeddingTableNumberOfPorts'] = {}
        self._defaults['GetDeembeddingTableNumberOfPorts']['return'] = 0
        self._defaults['GetDeembeddingTableNumberOfPorts']['numberOfPorts'] = None
        self._defaults['GetError'] = {}
        self._defaults['GetError']['return'] = 0
        self._defaults['GetError']['errorCode'] = None
        self._defaults['GetError']['errorDescription'] = None
        self._defaults['GetExternalCalibrationLastDateAndTime'] = {}
        self._defaults['GetExternalCalibrationLastDateAndTime']['return'] = 0
        self._defaults['GetExternalCalibrationLastDateAndTime']['year'] = None
        self._defaults['GetExternalCalibrationLastDateAndTime']['month'] = None
        self._defaults['GetExternalCalibrationLastDateAndTime']['day'] = None
        self._defaults['GetExternalCalibrationLastDateAndTime']['hour'] = None
        self._defaults['GetExternalCalibrationLastDateAndTime']['minute'] = None
        self._defaults['GetExternalCalibrationLastDateAndTime']['second'] = None
        self._defaults['GetMaxSettablePower'] = {}
        self._defaults['GetMaxSettablePower']['return'] = 0
        self._defaults['GetMaxSettablePower']['value'] = None
        self._defaults['GetScript'] = {}
        self._defaults['GetScript']['return'] = 0
        self._defaults['GetScript']['actualBufferSize'] = None
        self._defaults['GetScript']['script'] = None
        self._defaults['GetSelfCalibrationDateAndTime'] = {}
        self._defaults['GetSelfCalibrationDateAndTime']['return'] = 0
        self._defaults['GetSelfCalibrationDateAndTime']['year'] = None
        self._defaults['GetSelfCalibrationDateAndTime']['month'] = None
        self._defaults['GetSelfCalibrationDateAndTime']['day'] = None
        self._defaults['GetSelfCalibrationDateAndTime']['hour'] = None
        self._defaults['GetSelfCalibrationDateAndTime']['minute'] = None
        self._defaults['GetSelfCalibrationDateAndTime']['second'] = None
        self._defaults['GetSelfCalibrationTemperature'] = {}
        self._defaults['GetSelfCalibrationTemperature']['return'] = 0
        self._defaults['GetSelfCalibrationTemperature']['temperature'] = None
        self._defaults['GetTerminalName'] = {}
        self._defaults['GetTerminalName']['return'] = 0
        self._defaults['GetTerminalName']['terminalName'] = None
        self._defaults['GetWaveformBurstStartLocations'] = {}
        self._defaults['GetWaveformBurstStartLocations']['return'] = 0
        self._defaults['GetWaveformBurstStartLocations']['requiredSize'] = None
        self._defaults['GetWaveformBurstStartLocations']['locations'] = None
        self._defaults['GetWaveformBurstStopLocations'] = {}
        self._defaults['GetWaveformBurstStopLocations']['return'] = 0
        self._defaults['GetWaveformBurstStopLocations']['requiredSize'] = None
        self._defaults['GetWaveformBurstStopLocations']['locations'] = None
        self._defaults['GetWaveformMarkerEventLocations'] = {}
        self._defaults['GetWaveformMarkerEventLocations']['return'] = 0
        self._defaults['GetWaveformMarkerEventLocations']['requiredSize'] = None
        self._defaults['GetWaveformMarkerEventLocations']['locations'] = None
        self._defaults['InitWithOptions'] = {}
        self._defaults['InitWithOptions']['return'] = 0
        self._defaults['InitWithOptions']['newVi'] = None
        self._defaults['Initiate'] = {}
        self._defaults['Initiate']['return'] = 0
        self._defaults['LoadConfigurationsFromFile'] = {}
        self._defaults['LoadConfigurationsFromFile']['return'] = 0
        self._defaults['LockSession'] = {}
        self._defaults['LockSession']['return'] = 0
        self._defaults['LockSession']['callerHasLock'] = None
        self._defaults['PerformPowerSearch'] = {}
        self._defaults['PerformPowerSearch']['return'] = 0
        self._defaults['PerformThermalCorrection'] = {}
        self._defaults['PerformThermalCorrection']['return'] = 0
        self._defaults['QueryArbWaveformCapabilities'] = {}
        self._defaults['QueryArbWaveformCapabilities']['return'] = 0
        self._defaults['QueryArbWaveformCapabilities']['maxNumberWaveforms'] = None
        self._defaults['QueryArbWaveformCapabilities']['waveformQuantum'] = None
        self._defaults['QueryArbWaveformCapabilities']['minWaveformSize'] = None
        self._defaults['QueryArbWaveformCapabilities']['maxWaveformSize'] = None
        self._defaults['ReadAndDownloadWaveformFromFileTDMS'] = {}
        self._defaults['ReadAndDownloadWaveformFromFileTDMS']['return'] = 0
        self._defaults['ResetDevice'] = {}
        self._defaults['ResetDevice']['return'] = 0
        self._defaults['ResetWithDefaults'] = {}
        self._defaults['ResetWithDefaults']['return'] = 0
        self._defaults['ResetWithOptions'] = {}
        self._defaults['ResetWithOptions']['return'] = 0
        self._defaults['SaveConfigurationsToFile'] = {}
        self._defaults['SaveConfigurationsToFile']['return'] = 0
        self._defaults['SelectArbWaveform'] = {}
        self._defaults['SelectArbWaveform']['return'] = 0
        self._defaults['SelfCal'] = {}
        self._defaults['SelfCal']['return'] = 0
        self._defaults['SelfCalibrateRange'] = {}
        self._defaults['SelfCalibrateRange']['return'] = 0
        self._defaults['SendSoftwareEdgeTrigger'] = {}
        self._defaults['SendSoftwareEdgeTrigger']['return'] = 0
        self._defaults['SetArbWaveformNextWritePosition'] = {}
        self._defaults['SetArbWaveformNextWritePosition']['return'] = 0
        self._defaults['SetAttributeViBoolean'] = {}
        self._defaults['SetAttributeViBoolean']['return'] = 0
        self._defaults['SetAttributeViInt32'] = {}
        self._defaults['SetAttributeViInt32']['return'] = 0
        self._defaults['SetAttributeViInt64'] = {}
        self._defaults['SetAttributeViInt64']['return'] = 0
        self._defaults['SetAttributeViReal64'] = {}
        self._defaults['SetAttributeViReal64']['return'] = 0
        self._defaults['SetAttributeViSession'] = {}
        self._defaults['SetAttributeViSession']['return'] = 0
        self._defaults['SetAttributeViString'] = {}
        self._defaults['SetAttributeViString']['return'] = 0
        self._defaults['SetWaveformBurstStartLocations'] = {}
        self._defaults['SetWaveformBurstStartLocations']['return'] = 0
        self._defaults['SetWaveformBurstStopLocations'] = {}
        self._defaults['SetWaveformBurstStopLocations']['return'] = 0
        self._defaults['SetWaveformMarkerEventLocations'] = {}
        self._defaults['SetWaveformMarkerEventLocations']['return'] = 0
        self._defaults['UnlockSession'] = {}
        self._defaults['UnlockSession']['return'] = 0
        self._defaults['UnlockSession']['callerHasLock'] = None
        self._defaults['WaitUntilSettled'] = {}
        self._defaults['WaitUntilSettled']['return'] = 0
        self._defaults['WriteArbWaveformComplexF32'] = {}
        self._defaults['WriteArbWaveformComplexF32']['return'] = 0
        self._defaults['WriteArbWaveformComplexF64'] = {}
        self._defaults['WriteArbWaveformComplexF64']['return'] = 0
        self._defaults['WriteArbWaveformComplexI16'] = {}
        self._defaults['WriteArbWaveformComplexI16']['return'] = 0
        self._defaults['WriteScript'] = {}
        self._defaults['WriteScript']['return'] = 0
        self._defaults['close'] = {}
        self._defaults['close']['return'] = 0
        self._defaults['reset'] = {}
        self._defaults['reset']['return'] = 0
        self._defaults['self_test'] = {}
        self._defaults['self_test']['return'] = 0
        self._defaults['self_test']['selfTestResult'] = None
        self._defaults['self_test']['selfTestMessage'] = None

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

    def niRFSG_Abort(self, vi):  # noqa: N802
        if self._defaults['Abort']['return'] != 0:
            return self._defaults['Abort']['return']
        return self._defaults['Abort']['return']

    def niRFSG_AllocateArbWaveform(self, vi, waveform_name, size_in_samples):  # noqa: N802
        if self._defaults['AllocateArbWaveform']['return'] != 0:
            return self._defaults['AllocateArbWaveform']['return']
        return self._defaults['AllocateArbWaveform']['return']

    def niRFSG_ChangeExternalCalibrationPassword(self, vi, old_password, new_password):  # noqa: N802
        if self._defaults['ChangeExternalCalibrationPassword']['return'] != 0:
            return self._defaults['ChangeExternalCalibrationPassword']['return']
        return self._defaults['ChangeExternalCalibrationPassword']['return']

    def niRFSG_CheckGenerationStatus(self, vi, is_done):  # noqa: N802
        if self._defaults['CheckGenerationStatus']['return'] != 0:
            return self._defaults['CheckGenerationStatus']['return']
        # is_done
        if self._defaults['CheckGenerationStatus']['isDone'] is None:
            raise MockFunctionCallError("niRFSG_CheckGenerationStatus", param='isDone')
        if is_done is not None:
            is_done.contents.value = self._defaults['CheckGenerationStatus']['isDone']
        return self._defaults['CheckGenerationStatus']['return']

    def niRFSG_CheckIfScriptExists(self, vi, script_name, script_exists):  # noqa: N802
        if self._defaults['CheckIfScriptExists']['return'] != 0:
            return self._defaults['CheckIfScriptExists']['return']
        # script_exists
        if self._defaults['CheckIfScriptExists']['scriptExists'] is None:
            raise MockFunctionCallError("niRFSG_CheckIfScriptExists", param='scriptExists')
        if script_exists is not None:
            script_exists.contents.value = self._defaults['CheckIfScriptExists']['scriptExists']
        return self._defaults['CheckIfScriptExists']['return']

    def niRFSG_CheckIfWaveformExists(self, vi, waveform_name, waveform_exists):  # noqa: N802
        if self._defaults['CheckIfWaveformExists']['return'] != 0:
            return self._defaults['CheckIfWaveformExists']['return']
        # waveform_exists
        if self._defaults['CheckIfWaveformExists']['waveformExists'] is None:
            raise MockFunctionCallError("niRFSG_CheckIfWaveformExists", param='waveformExists')
        if waveform_exists is not None:
            waveform_exists.contents.value = self._defaults['CheckIfWaveformExists']['waveformExists']
        return self._defaults['CheckIfWaveformExists']['return']

    def niRFSG_ClearAllArbWaveforms(self, vi):  # noqa: N802
        if self._defaults['ClearAllArbWaveforms']['return'] != 0:
            return self._defaults['ClearAllArbWaveforms']['return']
        return self._defaults['ClearAllArbWaveforms']['return']

    def niRFSG_ClearArbWaveform(self, vi, waveform_name):  # noqa: N802
        if self._defaults['ClearArbWaveform']['return'] != 0:
            return self._defaults['ClearArbWaveform']['return']
        return self._defaults['ClearArbWaveform']['return']

    def niRFSG_ClearSelfCalibrateRange(self, vi):  # noqa: N802
        if self._defaults['ClearSelfCalibrateRange']['return'] != 0:
            return self._defaults['ClearSelfCalibrateRange']['return']
        return self._defaults['ClearSelfCalibrateRange']['return']

    def niRFSG_Commit(self, vi):  # noqa: N802
        if self._defaults['Commit']['return'] != 0:
            return self._defaults['Commit']['return']
        return self._defaults['Commit']['return']

    def niRFSG_ConfigureDeembeddingTableInterpolationLinear(self, vi, port, table_name, format):  # noqa: N802
        if self._defaults['ConfigureDeembeddingTableInterpolationLinear']['return'] != 0:
            return self._defaults['ConfigureDeembeddingTableInterpolationLinear']['return']
        return self._defaults['ConfigureDeembeddingTableInterpolationLinear']['return']

    def niRFSG_ConfigureDeembeddingTableInterpolationNearest(self, vi, port, table_name):  # noqa: N802
        if self._defaults['ConfigureDeembeddingTableInterpolationNearest']['return'] != 0:
            return self._defaults['ConfigureDeembeddingTableInterpolationNearest']['return']
        return self._defaults['ConfigureDeembeddingTableInterpolationNearest']['return']

    def niRFSG_ConfigureDeembeddingTableInterpolationSpline(self, vi, port, table_name):  # noqa: N802
        if self._defaults['ConfigureDeembeddingTableInterpolationSpline']['return'] != 0:
            return self._defaults['ConfigureDeembeddingTableInterpolationSpline']['return']
        return self._defaults['ConfigureDeembeddingTableInterpolationSpline']['return']

    def niRFSG_ConfigureDigitalEdgeScriptTrigger(self, vi, trigger_id, source, edge):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgeScriptTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgeScriptTrigger']['return']
        return self._defaults['ConfigureDigitalEdgeScriptTrigger']['return']

    def niRFSG_ConfigureDigitalEdgeStartTrigger(self, vi, source, edge):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgeStartTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgeStartTrigger']['return']
        return self._defaults['ConfigureDigitalEdgeStartTrigger']['return']

    def niRFSG_ConfigureDigitalLevelScriptTrigger(self, vi, trigger_id, source, level):  # noqa: N802
        if self._defaults['ConfigureDigitalLevelScriptTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalLevelScriptTrigger']['return']
        return self._defaults['ConfigureDigitalLevelScriptTrigger']['return']

    def niRFSG_ConfigureRF(self, vi, frequency, power_level):  # noqa: N802
        if self._defaults['ConfigureRF']['return'] != 0:
            return self._defaults['ConfigureRF']['return']
        return self._defaults['ConfigureRF']['return']

    def niRFSG_ConfigureRefClock(self, vi, ref_clock_source, ref_clock_rate):  # noqa: N802
        if self._defaults['ConfigureRefClock']['return'] != 0:
            return self._defaults['ConfigureRefClock']['return']
        return self._defaults['ConfigureRefClock']['return']

    def niRFSG_ConfigureSoftwareScriptTrigger(self, vi, trigger_id):  # noqa: N802
        if self._defaults['ConfigureSoftwareScriptTrigger']['return'] != 0:
            return self._defaults['ConfigureSoftwareScriptTrigger']['return']
        return self._defaults['ConfigureSoftwareScriptTrigger']['return']

    def niRFSG_ConfigureSoftwareStartTrigger(self, vi):  # noqa: N802
        if self._defaults['ConfigureSoftwareStartTrigger']['return'] != 0:
            return self._defaults['ConfigureSoftwareStartTrigger']['return']
        return self._defaults['ConfigureSoftwareStartTrigger']['return']

    def niRFSG_CreateDeembeddingSparameterTableArray(self, vi, port, table_name, frequencies, frequencies_size, sparameter_table, sparameter_table_size, number_of_ports, sparameter_orientation):  # noqa: N802
        if self._defaults['CreateDeembeddingSparameterTableArray']['return'] != 0:
            return self._defaults['CreateDeembeddingSparameterTableArray']['return']
        return self._defaults['CreateDeembeddingSparameterTableArray']['return']

    def niRFSG_CreateDeembeddingSparameterTableS2PFile(self, vi, port, table_name, s2p_file_path, sparameter_orientation):  # noqa: N802
        if self._defaults['CreateDeembeddingSparameterTableS2PFile']['return'] != 0:
            return self._defaults['CreateDeembeddingSparameterTableS2PFile']['return']
        return self._defaults['CreateDeembeddingSparameterTableS2PFile']['return']

    def niRFSG_DeleteAllDeembeddingTables(self, vi):  # noqa: N802
        if self._defaults['DeleteAllDeembeddingTables']['return'] != 0:
            return self._defaults['DeleteAllDeembeddingTables']['return']
        return self._defaults['DeleteAllDeembeddingTables']['return']

    def niRFSG_DeleteDeembeddingTable(self, vi, port, table_name):  # noqa: N802
        if self._defaults['DeleteDeembeddingTable']['return'] != 0:
            return self._defaults['DeleteDeembeddingTable']['return']
        return self._defaults['DeleteDeembeddingTable']['return']

    def niRFSG_DeleteScript(self, vi, script_name):  # noqa: N802
        if self._defaults['DeleteScript']['return'] != 0:
            return self._defaults['DeleteScript']['return']
        return self._defaults['DeleteScript']['return']

    def niRFSG_DisableScriptTrigger(self, vi, trigger_id):  # noqa: N802
        if self._defaults['DisableScriptTrigger']['return'] != 0:
            return self._defaults['DisableScriptTrigger']['return']
        return self._defaults['DisableScriptTrigger']['return']

    def niRFSG_DisableStartTrigger(self, vi):  # noqa: N802
        if self._defaults['DisableStartTrigger']['return'] != 0:
            return self._defaults['DisableStartTrigger']['return']
        return self._defaults['DisableStartTrigger']['return']

    def niRFSG_ErrorMessage(self, vi, error_code, error_message):  # noqa: N802
        if self._defaults['ErrorMessage']['return'] != 0:
            return self._defaults['ErrorMessage']['return']
        # error_message
        if self._defaults['ErrorMessage']['errorMessage'] is None:
            raise MockFunctionCallError("niRFSG_ErrorMessage", param='errorMessage')
        test_value = self._defaults['ErrorMessage']['errorMessage']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(error_message) >= len(test_value)
        for i in range(len(test_value)):
            error_message[i] = test_value[i]
        return self._defaults['ErrorMessage']['return']

    def niRFSG_GetAllNamedWaveformNames(self, vi, waveform_names, buffer_size, actual_buffer_size):  # noqa: N802
        if self._defaults['GetAllNamedWaveformNames']['return'] != 0:
            return self._defaults['GetAllNamedWaveformNames']['return']
        # actual_buffer_size
        if self._defaults['GetAllNamedWaveformNames']['actualBufferSize'] is None:
            raise MockFunctionCallError("niRFSG_GetAllNamedWaveformNames", param='actualBufferSize')
        if actual_buffer_size is not None:
            actual_buffer_size.contents.value = self._defaults['GetAllNamedWaveformNames']['actualBufferSize']
        # waveform_names
        if self._defaults['GetAllNamedWaveformNames']['waveformNames'] is None:
            raise MockFunctionCallError("niRFSG_GetAllNamedWaveformNames", param='waveformNames')
        if buffer_size.value == 0:
            return len(self._defaults['GetAllNamedWaveformNames']['waveformNames'])
        waveform_names.value = self._defaults['GetAllNamedWaveformNames']['waveformNames'].encode('ascii')
        return self._defaults['GetAllNamedWaveformNames']['return']

    def niRFSG_GetAllScriptNames(self, vi, script_names, buffer_size, actual_buffer_size):  # noqa: N802
        if self._defaults['GetAllScriptNames']['return'] != 0:
            return self._defaults['GetAllScriptNames']['return']
        # actual_buffer_size
        if self._defaults['GetAllScriptNames']['actualBufferSize'] is None:
            raise MockFunctionCallError("niRFSG_GetAllScriptNames", param='actualBufferSize')
        if actual_buffer_size is not None:
            actual_buffer_size.contents.value = self._defaults['GetAllScriptNames']['actualBufferSize']
        # script_names
        if self._defaults['GetAllScriptNames']['scriptNames'] is None:
            raise MockFunctionCallError("niRFSG_GetAllScriptNames", param='scriptNames')
        if buffer_size.value == 0:
            return len(self._defaults['GetAllScriptNames']['scriptNames'])
        script_names.value = self._defaults['GetAllScriptNames']['scriptNames'].encode('ascii')
        return self._defaults['GetAllScriptNames']['return']

    def niRFSG_GetAttributeViBoolean(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['GetAttributeViBoolean']['return'] != 0:
            return self._defaults['GetAttributeViBoolean']['return']
        # value
        if self._defaults['GetAttributeViBoolean']['value'] is None:
            raise MockFunctionCallError("niRFSG_GetAttributeViBoolean", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViBoolean']['value']
        return self._defaults['GetAttributeViBoolean']['return']

    def niRFSG_GetAttributeViInt32(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['GetAttributeViInt32']['return'] != 0:
            return self._defaults['GetAttributeViInt32']['return']
        # value
        if self._defaults['GetAttributeViInt32']['value'] is None:
            raise MockFunctionCallError("niRFSG_GetAttributeViInt32", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViInt32']['value']
        return self._defaults['GetAttributeViInt32']['return']

    def niRFSG_GetAttributeViInt64(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['GetAttributeViInt64']['return'] != 0:
            return self._defaults['GetAttributeViInt64']['return']
        # value
        if self._defaults['GetAttributeViInt64']['value'] is None:
            raise MockFunctionCallError("niRFSG_GetAttributeViInt64", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViInt64']['value']
        return self._defaults['GetAttributeViInt64']['return']

    def niRFSG_GetAttributeViReal64(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['GetAttributeViReal64']['return'] != 0:
            return self._defaults['GetAttributeViReal64']['return']
        # value
        if self._defaults['GetAttributeViReal64']['value'] is None:
            raise MockFunctionCallError("niRFSG_GetAttributeViReal64", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViReal64']['value']
        return self._defaults['GetAttributeViReal64']['return']

    def niRFSG_GetAttributeViSession(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['GetAttributeViSession']['return'] != 0:
            return self._defaults['GetAttributeViSession']['return']
        # value
        if self._defaults['GetAttributeViSession']['value'] is None:
            raise MockFunctionCallError("niRFSG_GetAttributeViSession", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetAttributeViSession']['value']
        return self._defaults['GetAttributeViSession']['return']

    def niRFSG_GetAttributeViString(self, vi, channel_name, attribute, buf_size, value):  # noqa: N802
        if self._defaults['GetAttributeViString']['return'] != 0:
            return self._defaults['GetAttributeViString']['return']
        # value
        if self._defaults['GetAttributeViString']['value'] is None:
            raise MockFunctionCallError("niRFSG_GetAttributeViString", param='value')
        if buf_size.value == 0:
            return len(self._defaults['GetAttributeViString']['value'])
        value.value = self._defaults['GetAttributeViString']['value'].encode('ascii')
        return self._defaults['GetAttributeViString']['return']

    def niRFSG_GetDeembeddingSparameters(self, vi, sparameters, sparameters_array_size, number_of_sparameters, number_of_ports):  # noqa: N802
        if self._defaults['GetDeembeddingSparameters']['return'] != 0:
            return self._defaults['GetDeembeddingSparameters']['return']
        # sparameters
        if self._defaults['GetDeembeddingSparameters']['sparameters'] is None:
            raise MockFunctionCallError("niRFSG_GetDeembeddingSparameters", param='sparameters')
        test_value = self._defaults['GetDeembeddingSparameters']['sparameters']
        try:
            sparameters_ref = sparameters.contents
        except AttributeError:
            sparameters_ref = sparameters
        assert len(sparameters_ref) >= len(test_value)
        for i in range(len(test_value)):
            sparameters_ref[i] = test_value[i]
        # number_of_sparameters
        if self._defaults['GetDeembeddingSparameters']['numberOfSparameters'] is None:
            raise MockFunctionCallError("niRFSG_GetDeembeddingSparameters", param='numberOfSparameters')
        if number_of_sparameters is not None:
            number_of_sparameters.contents.value = self._defaults['GetDeembeddingSparameters']['numberOfSparameters']
        # number_of_ports
        if self._defaults['GetDeembeddingSparameters']['numberOfPorts'] is None:
            raise MockFunctionCallError("niRFSG_GetDeembeddingSparameters", param='numberOfPorts')
        if number_of_ports is not None:
            number_of_ports.contents.value = self._defaults['GetDeembeddingSparameters']['numberOfPorts']
        return self._defaults['GetDeembeddingSparameters']['return']

    def niRFSG_GetDeembeddingTableNumberOfPorts(self, vi, number_of_ports):  # noqa: N802
        if self._defaults['GetDeembeddingTableNumberOfPorts']['return'] != 0:
            return self._defaults['GetDeembeddingTableNumberOfPorts']['return']
        # number_of_ports
        if self._defaults['GetDeembeddingTableNumberOfPorts']['numberOfPorts'] is None:
            raise MockFunctionCallError("niRFSG_GetDeembeddingTableNumberOfPorts", param='numberOfPorts')
        if number_of_ports is not None:
            number_of_ports.contents.value = self._defaults['GetDeembeddingTableNumberOfPorts']['numberOfPorts']
        return self._defaults['GetDeembeddingTableNumberOfPorts']['return']

    def niRFSG_GetError(self, vi, error_code, error_description_buffer_size, error_description):  # noqa: N802
        if self._defaults['GetError']['return'] != 0:
            return self._defaults['GetError']['return']
        # error_code
        if self._defaults['GetError']['errorCode'] is None:
            raise MockFunctionCallError("niRFSG_GetError", param='errorCode')
        if error_code is not None:
            error_code.contents.value = self._defaults['GetError']['errorCode']
        # error_description
        if self._defaults['GetError']['errorDescription'] is None:
            raise MockFunctionCallError("niRFSG_GetError", param='errorDescription')
        if error_description_buffer_size.value == 0:
            return len(self._defaults['GetError']['errorDescription'])
        error_description.value = self._defaults['GetError']['errorDescription'].encode('ascii')
        return self._defaults['GetError']['return']

    def niRFSG_GetExternalCalibrationLastDateAndTime(self, vi, year, month, day, hour, minute, second):  # noqa: N802
        if self._defaults['GetExternalCalibrationLastDateAndTime']['return'] != 0:
            return self._defaults['GetExternalCalibrationLastDateAndTime']['return']
        # year
        if self._defaults['GetExternalCalibrationLastDateAndTime']['year'] is None:
            raise MockFunctionCallError("niRFSG_GetExternalCalibrationLastDateAndTime", param='year')
        if year is not None:
            year.contents.value = self._defaults['GetExternalCalibrationLastDateAndTime']['year']
        # month
        if self._defaults['GetExternalCalibrationLastDateAndTime']['month'] is None:
            raise MockFunctionCallError("niRFSG_GetExternalCalibrationLastDateAndTime", param='month')
        if month is not None:
            month.contents.value = self._defaults['GetExternalCalibrationLastDateAndTime']['month']
        # day
        if self._defaults['GetExternalCalibrationLastDateAndTime']['day'] is None:
            raise MockFunctionCallError("niRFSG_GetExternalCalibrationLastDateAndTime", param='day')
        if day is not None:
            day.contents.value = self._defaults['GetExternalCalibrationLastDateAndTime']['day']
        # hour
        if self._defaults['GetExternalCalibrationLastDateAndTime']['hour'] is None:
            raise MockFunctionCallError("niRFSG_GetExternalCalibrationLastDateAndTime", param='hour')
        if hour is not None:
            hour.contents.value = self._defaults['GetExternalCalibrationLastDateAndTime']['hour']
        # minute
        if self._defaults['GetExternalCalibrationLastDateAndTime']['minute'] is None:
            raise MockFunctionCallError("niRFSG_GetExternalCalibrationLastDateAndTime", param='minute')
        if minute is not None:
            minute.contents.value = self._defaults['GetExternalCalibrationLastDateAndTime']['minute']
        # second
        if self._defaults['GetExternalCalibrationLastDateAndTime']['second'] is None:
            raise MockFunctionCallError("niRFSG_GetExternalCalibrationLastDateAndTime", param='second')
        if second is not None:
            second.contents.value = self._defaults['GetExternalCalibrationLastDateAndTime']['second']
        return self._defaults['GetExternalCalibrationLastDateAndTime']['return']

    def niRFSG_GetMaxSettablePower(self, vi, value):  # noqa: N802
        if self._defaults['GetMaxSettablePower']['return'] != 0:
            return self._defaults['GetMaxSettablePower']['return']
        # value
        if self._defaults['GetMaxSettablePower']['value'] is None:
            raise MockFunctionCallError("niRFSG_GetMaxSettablePower", param='value')
        if value is not None:
            value.contents.value = self._defaults['GetMaxSettablePower']['value']
        return self._defaults['GetMaxSettablePower']['return']

    def niRFSG_GetScript(self, vi, script_name, script, buffer_size, actual_buffer_size):  # noqa: N802
        if self._defaults['GetScript']['return'] != 0:
            return self._defaults['GetScript']['return']
        # actual_buffer_size
        if self._defaults['GetScript']['actualBufferSize'] is None:
            raise MockFunctionCallError("niRFSG_GetScript", param='actualBufferSize')
        if actual_buffer_size is not None:
            actual_buffer_size.contents.value = self._defaults['GetScript']['actualBufferSize']
        # script
        if self._defaults['GetScript']['script'] is None:
            raise MockFunctionCallError("niRFSG_GetScript", param='script')
        if buffer_size.value == 0:
            return len(self._defaults['GetScript']['script'])
        script.value = self._defaults['GetScript']['script'].encode('ascii')
        return self._defaults['GetScript']['return']

    def niRFSG_GetSelfCalibrationDateAndTime(self, vi, module, year, month, day, hour, minute, second):  # noqa: N802
        if self._defaults['GetSelfCalibrationDateAndTime']['return'] != 0:
            return self._defaults['GetSelfCalibrationDateAndTime']['return']
        # year
        if self._defaults['GetSelfCalibrationDateAndTime']['year'] is None:
            raise MockFunctionCallError("niRFSG_GetSelfCalibrationDateAndTime", param='year')
        if year is not None:
            year.contents.value = self._defaults['GetSelfCalibrationDateAndTime']['year']
        # month
        if self._defaults['GetSelfCalibrationDateAndTime']['month'] is None:
            raise MockFunctionCallError("niRFSG_GetSelfCalibrationDateAndTime", param='month')
        if month is not None:
            month.contents.value = self._defaults['GetSelfCalibrationDateAndTime']['month']
        # day
        if self._defaults['GetSelfCalibrationDateAndTime']['day'] is None:
            raise MockFunctionCallError("niRFSG_GetSelfCalibrationDateAndTime", param='day')
        if day is not None:
            day.contents.value = self._defaults['GetSelfCalibrationDateAndTime']['day']
        # hour
        if self._defaults['GetSelfCalibrationDateAndTime']['hour'] is None:
            raise MockFunctionCallError("niRFSG_GetSelfCalibrationDateAndTime", param='hour')
        if hour is not None:
            hour.contents.value = self._defaults['GetSelfCalibrationDateAndTime']['hour']
        # minute
        if self._defaults['GetSelfCalibrationDateAndTime']['minute'] is None:
            raise MockFunctionCallError("niRFSG_GetSelfCalibrationDateAndTime", param='minute')
        if minute is not None:
            minute.contents.value = self._defaults['GetSelfCalibrationDateAndTime']['minute']
        # second
        if self._defaults['GetSelfCalibrationDateAndTime']['second'] is None:
            raise MockFunctionCallError("niRFSG_GetSelfCalibrationDateAndTime", param='second')
        if second is not None:
            second.contents.value = self._defaults['GetSelfCalibrationDateAndTime']['second']
        return self._defaults['GetSelfCalibrationDateAndTime']['return']

    def niRFSG_GetSelfCalibrationTemperature(self, vi, module, temperature):  # noqa: N802
        if self._defaults['GetSelfCalibrationTemperature']['return'] != 0:
            return self._defaults['GetSelfCalibrationTemperature']['return']
        # temperature
        if self._defaults['GetSelfCalibrationTemperature']['temperature'] is None:
            raise MockFunctionCallError("niRFSG_GetSelfCalibrationTemperature", param='temperature')
        if temperature is not None:
            temperature.contents.value = self._defaults['GetSelfCalibrationTemperature']['temperature']
        return self._defaults['GetSelfCalibrationTemperature']['return']

    def niRFSG_GetTerminalName(self, vi, signal, signal_identifier, buffer_size, terminal_name):  # noqa: N802
        if self._defaults['GetTerminalName']['return'] != 0:
            return self._defaults['GetTerminalName']['return']
        # terminal_name
        if self._defaults['GetTerminalName']['terminalName'] is None:
            raise MockFunctionCallError("niRFSG_GetTerminalName", param='terminalName')
        if buffer_size.value == 0:
            return len(self._defaults['GetTerminalName']['terminalName'])
        terminal_name.value = self._defaults['GetTerminalName']['terminalName'].encode('ascii')
        return self._defaults['GetTerminalName']['return']

    def niRFSG_GetWaveformBurstStartLocations(self, vi, channel_name, number_of_locations, locations, required_size):  # noqa: N802
        if self._defaults['GetWaveformBurstStartLocations']['return'] != 0:
            return self._defaults['GetWaveformBurstStartLocations']['return']
        # required_size
        if self._defaults['GetWaveformBurstStartLocations']['requiredSize'] is None:
            raise MockFunctionCallError("niRFSG_GetWaveformBurstStartLocations", param='requiredSize')
        if required_size is not None:
            required_size.contents.value = self._defaults['GetWaveformBurstStartLocations']['requiredSize']
        # locations
        if self._defaults['GetWaveformBurstStartLocations']['locations'] is None:
            raise MockFunctionCallError("niRFSG_GetWaveformBurstStartLocations", param='locations')
        if number_of_locations.value == 0:
            return len(self._defaults['GetWaveformBurstStartLocations']['locations'])
        try:
            locations_ref = locations.contents
        except AttributeError:
            locations_ref = locations
        for i in range(len(self._defaults['GetWaveformBurstStartLocations']['locations'])):
            locations_ref[i] = self._defaults['GetWaveformBurstStartLocations']['locations'][i]
        return self._defaults['GetWaveformBurstStartLocations']['return']

    def niRFSG_GetWaveformBurstStopLocations(self, vi, channel_name, number_of_locations, locations, required_size):  # noqa: N802
        if self._defaults['GetWaveformBurstStopLocations']['return'] != 0:
            return self._defaults['GetWaveformBurstStopLocations']['return']
        # required_size
        if self._defaults['GetWaveformBurstStopLocations']['requiredSize'] is None:
            raise MockFunctionCallError("niRFSG_GetWaveformBurstStopLocations", param='requiredSize')
        if required_size is not None:
            required_size.contents.value = self._defaults['GetWaveformBurstStopLocations']['requiredSize']
        # locations
        if self._defaults['GetWaveformBurstStopLocations']['locations'] is None:
            raise MockFunctionCallError("niRFSG_GetWaveformBurstStopLocations", param='locations')
        if number_of_locations.value == 0:
            return len(self._defaults['GetWaveformBurstStopLocations']['locations'])
        try:
            locations_ref = locations.contents
        except AttributeError:
            locations_ref = locations
        for i in range(len(self._defaults['GetWaveformBurstStopLocations']['locations'])):
            locations_ref[i] = self._defaults['GetWaveformBurstStopLocations']['locations'][i]
        return self._defaults['GetWaveformBurstStopLocations']['return']

    def niRFSG_GetWaveformMarkerEventLocations(self, vi, channel_name, number_of_locations, locations, required_size):  # noqa: N802
        if self._defaults['GetWaveformMarkerEventLocations']['return'] != 0:
            return self._defaults['GetWaveformMarkerEventLocations']['return']
        # required_size
        if self._defaults['GetWaveformMarkerEventLocations']['requiredSize'] is None:
            raise MockFunctionCallError("niRFSG_GetWaveformMarkerEventLocations", param='requiredSize')
        if required_size is not None:
            required_size.contents.value = self._defaults['GetWaveformMarkerEventLocations']['requiredSize']
        # locations
        if self._defaults['GetWaveformMarkerEventLocations']['locations'] is None:
            raise MockFunctionCallError("niRFSG_GetWaveformMarkerEventLocations", param='locations')
        if number_of_locations.value == 0:
            return len(self._defaults['GetWaveformMarkerEventLocations']['locations'])
        try:
            locations_ref = locations.contents
        except AttributeError:
            locations_ref = locations
        for i in range(len(self._defaults['GetWaveformMarkerEventLocations']['locations'])):
            locations_ref[i] = self._defaults['GetWaveformMarkerEventLocations']['locations'][i]
        return self._defaults['GetWaveformMarkerEventLocations']['return']

    def niRFSG_InitWithOptions(self, resource_name, id_query, reset_device, option_string, new_vi):  # noqa: N802
        if self._defaults['InitWithOptions']['return'] != 0:
            return self._defaults['InitWithOptions']['return']
        # new_vi
        if self._defaults['InitWithOptions']['newVi'] is None:
            raise MockFunctionCallError("niRFSG_InitWithOptions", param='newVi')
        if new_vi is not None:
            new_vi.contents.value = self._defaults['InitWithOptions']['newVi']
        return self._defaults['InitWithOptions']['return']

    def niRFSG_Initiate(self, vi):  # noqa: N802
        if self._defaults['Initiate']['return'] != 0:
            return self._defaults['Initiate']['return']
        return self._defaults['Initiate']['return']

    def niRFSG_LoadConfigurationsFromFile(self, vi, channel_name, file_path):  # noqa: N802
        if self._defaults['LoadConfigurationsFromFile']['return'] != 0:
            return self._defaults['LoadConfigurationsFromFile']['return']
        return self._defaults['LoadConfigurationsFromFile']['return']

    def niRFSG_LockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['LockSession']['return'] != 0:
            return self._defaults['LockSession']['return']
        # caller_has_lock
        if self._defaults['LockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niRFSG_LockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['LockSession']['callerHasLock']
        return self._defaults['LockSession']['return']

    def niRFSG_PerformPowerSearch(self, vi):  # noqa: N802
        if self._defaults['PerformPowerSearch']['return'] != 0:
            return self._defaults['PerformPowerSearch']['return']
        return self._defaults['PerformPowerSearch']['return']

    def niRFSG_PerformThermalCorrection(self, vi):  # noqa: N802
        if self._defaults['PerformThermalCorrection']['return'] != 0:
            return self._defaults['PerformThermalCorrection']['return']
        return self._defaults['PerformThermalCorrection']['return']

    def niRFSG_QueryArbWaveformCapabilities(self, vi, max_number_waveforms, waveform_quantum, min_waveform_size, max_waveform_size):  # noqa: N802
        if self._defaults['QueryArbWaveformCapabilities']['return'] != 0:
            return self._defaults['QueryArbWaveformCapabilities']['return']
        # max_number_waveforms
        if self._defaults['QueryArbWaveformCapabilities']['maxNumberWaveforms'] is None:
            raise MockFunctionCallError("niRFSG_QueryArbWaveformCapabilities", param='maxNumberWaveforms')
        if max_number_waveforms is not None:
            max_number_waveforms.contents.value = self._defaults['QueryArbWaveformCapabilities']['maxNumberWaveforms']
        # waveform_quantum
        if self._defaults['QueryArbWaveformCapabilities']['waveformQuantum'] is None:
            raise MockFunctionCallError("niRFSG_QueryArbWaveformCapabilities", param='waveformQuantum')
        if waveform_quantum is not None:
            waveform_quantum.contents.value = self._defaults['QueryArbWaveformCapabilities']['waveformQuantum']
        # min_waveform_size
        if self._defaults['QueryArbWaveformCapabilities']['minWaveformSize'] is None:
            raise MockFunctionCallError("niRFSG_QueryArbWaveformCapabilities", param='minWaveformSize')
        if min_waveform_size is not None:
            min_waveform_size.contents.value = self._defaults['QueryArbWaveformCapabilities']['minWaveformSize']
        # max_waveform_size
        if self._defaults['QueryArbWaveformCapabilities']['maxWaveformSize'] is None:
            raise MockFunctionCallError("niRFSG_QueryArbWaveformCapabilities", param='maxWaveformSize')
        if max_waveform_size is not None:
            max_waveform_size.contents.value = self._defaults['QueryArbWaveformCapabilities']['maxWaveformSize']
        return self._defaults['QueryArbWaveformCapabilities']['return']

    def niRFSG_ReadAndDownloadWaveformFromFileTDMS(self, vi, waveform_name, file_path, waveform_index):  # noqa: N802
        if self._defaults['ReadAndDownloadWaveformFromFileTDMS']['return'] != 0:
            return self._defaults['ReadAndDownloadWaveformFromFileTDMS']['return']
        return self._defaults['ReadAndDownloadWaveformFromFileTDMS']['return']

    def niRFSG_ResetDevice(self, vi):  # noqa: N802
        if self._defaults['ResetDevice']['return'] != 0:
            return self._defaults['ResetDevice']['return']
        return self._defaults['ResetDevice']['return']

    def niRFSG_ResetWithDefaults(self, vi):  # noqa: N802
        if self._defaults['ResetWithDefaults']['return'] != 0:
            return self._defaults['ResetWithDefaults']['return']
        return self._defaults['ResetWithDefaults']['return']

    def niRFSG_ResetWithOptions(self, vi, steps_to_omit):  # noqa: N802
        if self._defaults['ResetWithOptions']['return'] != 0:
            return self._defaults['ResetWithOptions']['return']
        return self._defaults['ResetWithOptions']['return']

    def niRFSG_SaveConfigurationsToFile(self, vi, channel_name, file_path):  # noqa: N802
        if self._defaults['SaveConfigurationsToFile']['return'] != 0:
            return self._defaults['SaveConfigurationsToFile']['return']
        return self._defaults['SaveConfigurationsToFile']['return']

    def niRFSG_SelectArbWaveform(self, vi, waveform_name):  # noqa: N802
        if self._defaults['SelectArbWaveform']['return'] != 0:
            return self._defaults['SelectArbWaveform']['return']
        return self._defaults['SelectArbWaveform']['return']

    def niRFSG_SelfCal(self, vi):  # noqa: N802
        if self._defaults['SelfCal']['return'] != 0:
            return self._defaults['SelfCal']['return']
        return self._defaults['SelfCal']['return']

    def niRFSG_SelfCalibrateRange(self, vi, steps_to_omit, min_frequency, max_frequency, min_power_level, max_power_level):  # noqa: N802
        if self._defaults['SelfCalibrateRange']['return'] != 0:
            return self._defaults['SelfCalibrateRange']['return']
        return self._defaults['SelfCalibrateRange']['return']

    def niRFSG_SendSoftwareEdgeTrigger(self, vi, trigger, trigger_identifier):  # noqa: N802
        if self._defaults['SendSoftwareEdgeTrigger']['return'] != 0:
            return self._defaults['SendSoftwareEdgeTrigger']['return']
        return self._defaults['SendSoftwareEdgeTrigger']['return']

    def niRFSG_SetArbWaveformNextWritePosition(self, vi, waveform_name, relative_to, offset):  # noqa: N802
        if self._defaults['SetArbWaveformNextWritePosition']['return'] != 0:
            return self._defaults['SetArbWaveformNextWritePosition']['return']
        return self._defaults['SetArbWaveformNextWritePosition']['return']

    def niRFSG_SetAttributeViBoolean(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['SetAttributeViBoolean']['return'] != 0:
            return self._defaults['SetAttributeViBoolean']['return']
        return self._defaults['SetAttributeViBoolean']['return']

    def niRFSG_SetAttributeViInt32(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['SetAttributeViInt32']['return'] != 0:
            return self._defaults['SetAttributeViInt32']['return']
        return self._defaults['SetAttributeViInt32']['return']

    def niRFSG_SetAttributeViInt64(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['SetAttributeViInt64']['return'] != 0:
            return self._defaults['SetAttributeViInt64']['return']
        return self._defaults['SetAttributeViInt64']['return']

    def niRFSG_SetAttributeViReal64(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['SetAttributeViReal64']['return'] != 0:
            return self._defaults['SetAttributeViReal64']['return']
        return self._defaults['SetAttributeViReal64']['return']

    def niRFSG_SetAttributeViSession(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['SetAttributeViSession']['return'] != 0:
            return self._defaults['SetAttributeViSession']['return']
        return self._defaults['SetAttributeViSession']['return']

    def niRFSG_SetAttributeViString(self, vi, channel_name, attribute, value):  # noqa: N802
        if self._defaults['SetAttributeViString']['return'] != 0:
            return self._defaults['SetAttributeViString']['return']
        return self._defaults['SetAttributeViString']['return']

    def niRFSG_SetWaveformBurstStartLocations(self, vi, channel_name, number_of_locations, locations):  # noqa: N802
        if self._defaults['SetWaveformBurstStartLocations']['return'] != 0:
            return self._defaults['SetWaveformBurstStartLocations']['return']
        return self._defaults['SetWaveformBurstStartLocations']['return']

    def niRFSG_SetWaveformBurstStopLocations(self, vi, channel_name, number_of_locations, locations):  # noqa: N802
        if self._defaults['SetWaveformBurstStopLocations']['return'] != 0:
            return self._defaults['SetWaveformBurstStopLocations']['return']
        return self._defaults['SetWaveformBurstStopLocations']['return']

    def niRFSG_SetWaveformMarkerEventLocations(self, vi, channel_name, number_of_locations, locations):  # noqa: N802
        if self._defaults['SetWaveformMarkerEventLocations']['return'] != 0:
            return self._defaults['SetWaveformMarkerEventLocations']['return']
        return self._defaults['SetWaveformMarkerEventLocations']['return']

    def niRFSG_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['UnlockSession']['return'] != 0:
            return self._defaults['UnlockSession']['return']
        # caller_has_lock
        if self._defaults['UnlockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niRFSG_UnlockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['UnlockSession']['callerHasLock']
        return self._defaults['UnlockSession']['return']

    def niRFSG_WaitUntilSettled(self, vi, max_time_milliseconds):  # noqa: N802
        if self._defaults['WaitUntilSettled']['return'] != 0:
            return self._defaults['WaitUntilSettled']['return']
        return self._defaults['WaitUntilSettled']['return']

    def niRFSG_WriteArbWaveformComplexF32(self, vi, waveform_name, number_of_samples, waveform_data_array, more_data_pending):  # noqa: N802
        if self._defaults['WriteArbWaveformComplexF32']['return'] != 0:
            return self._defaults['WriteArbWaveformComplexF32']['return']
        return self._defaults['WriteArbWaveformComplexF32']['return']

    def niRFSG_WriteArbWaveformComplexF64(self, vi, waveform_name, number_of_samples, waveform_data_array, more_data_pending):  # noqa: N802
        if self._defaults['WriteArbWaveformComplexF64']['return'] != 0:
            return self._defaults['WriteArbWaveformComplexF64']['return']
        return self._defaults['WriteArbWaveformComplexF64']['return']

    def niRFSG_WriteArbWaveformComplexI16(self, vi, waveform_name, number_of_samples, waveform_data_array):  # noqa: N802
        if self._defaults['WriteArbWaveformComplexI16']['return'] != 0:
            return self._defaults['WriteArbWaveformComplexI16']['return']
        return self._defaults['WriteArbWaveformComplexI16']['return']

    def niRFSG_WriteScript(self, vi, script):  # noqa: N802
        if self._defaults['WriteScript']['return'] != 0:
            return self._defaults['WriteScript']['return']
        return self._defaults['WriteScript']['return']

    def niRFSG_close(self, vi):  # noqa: N802
        if self._defaults['close']['return'] != 0:
            return self._defaults['close']['return']
        return self._defaults['close']['return']

    def niRFSG_reset(self, vi):  # noqa: N802
        if self._defaults['reset']['return'] != 0:
            return self._defaults['reset']['return']
        return self._defaults['reset']['return']

    def niRFSG_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        if self._defaults['self_test']['return'] != 0:
            return self._defaults['self_test']['return']
        # self_test_result
        if self._defaults['self_test']['selfTestResult'] is None:
            raise MockFunctionCallError("niRFSG_self_test", param='selfTestResult')
        if self_test_result is not None:
            self_test_result.contents.value = self._defaults['self_test']['selfTestResult']
        # self_test_message
        if self._defaults['self_test']['selfTestMessage'] is None:
            raise MockFunctionCallError("niRFSG_self_test", param='selfTestMessage')
        test_value = self._defaults['self_test']['selfTestMessage']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(self_test_message) >= len(test_value)
        for i in range(len(test_value)):
            self_test_message[i] = test_value[i]
        return self._defaults['self_test']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niRFSG_Abort.side_effect = MockFunctionCallError("niRFSG_Abort")
        mock_library.niRFSG_Abort.return_value = 0
        mock_library.niRFSG_AllocateArbWaveform.side_effect = MockFunctionCallError("niRFSG_AllocateArbWaveform")
        mock_library.niRFSG_AllocateArbWaveform.return_value = 0
        mock_library.niRFSG_ChangeExternalCalibrationPassword.side_effect = MockFunctionCallError("niRFSG_ChangeExternalCalibrationPassword")
        mock_library.niRFSG_ChangeExternalCalibrationPassword.return_value = 0
        mock_library.niRFSG_CheckGenerationStatus.side_effect = MockFunctionCallError("niRFSG_CheckGenerationStatus")
        mock_library.niRFSG_CheckGenerationStatus.return_value = 0
        mock_library.niRFSG_CheckIfScriptExists.side_effect = MockFunctionCallError("niRFSG_CheckIfScriptExists")
        mock_library.niRFSG_CheckIfScriptExists.return_value = 0
        mock_library.niRFSG_CheckIfWaveformExists.side_effect = MockFunctionCallError("niRFSG_CheckIfWaveformExists")
        mock_library.niRFSG_CheckIfWaveformExists.return_value = 0
        mock_library.niRFSG_ClearAllArbWaveforms.side_effect = MockFunctionCallError("niRFSG_ClearAllArbWaveforms")
        mock_library.niRFSG_ClearAllArbWaveforms.return_value = 0
        mock_library.niRFSG_ClearArbWaveform.side_effect = MockFunctionCallError("niRFSG_ClearArbWaveform")
        mock_library.niRFSG_ClearArbWaveform.return_value = 0
        mock_library.niRFSG_ClearSelfCalibrateRange.side_effect = MockFunctionCallError("niRFSG_ClearSelfCalibrateRange")
        mock_library.niRFSG_ClearSelfCalibrateRange.return_value = 0
        mock_library.niRFSG_Commit.side_effect = MockFunctionCallError("niRFSG_Commit")
        mock_library.niRFSG_Commit.return_value = 0
        mock_library.niRFSG_ConfigureDeembeddingTableInterpolationLinear.side_effect = MockFunctionCallError("niRFSG_ConfigureDeembeddingTableInterpolationLinear")
        mock_library.niRFSG_ConfigureDeembeddingTableInterpolationLinear.return_value = 0
        mock_library.niRFSG_ConfigureDeembeddingTableInterpolationNearest.side_effect = MockFunctionCallError("niRFSG_ConfigureDeembeddingTableInterpolationNearest")
        mock_library.niRFSG_ConfigureDeembeddingTableInterpolationNearest.return_value = 0
        mock_library.niRFSG_ConfigureDeembeddingTableInterpolationSpline.side_effect = MockFunctionCallError("niRFSG_ConfigureDeembeddingTableInterpolationSpline")
        mock_library.niRFSG_ConfigureDeembeddingTableInterpolationSpline.return_value = 0
        mock_library.niRFSG_ConfigureDigitalEdgeScriptTrigger.side_effect = MockFunctionCallError("niRFSG_ConfigureDigitalEdgeScriptTrigger")
        mock_library.niRFSG_ConfigureDigitalEdgeScriptTrigger.return_value = 0
        mock_library.niRFSG_ConfigureDigitalEdgeStartTrigger.side_effect = MockFunctionCallError("niRFSG_ConfigureDigitalEdgeStartTrigger")
        mock_library.niRFSG_ConfigureDigitalEdgeStartTrigger.return_value = 0
        mock_library.niRFSG_ConfigureDigitalLevelScriptTrigger.side_effect = MockFunctionCallError("niRFSG_ConfigureDigitalLevelScriptTrigger")
        mock_library.niRFSG_ConfigureDigitalLevelScriptTrigger.return_value = 0
        mock_library.niRFSG_ConfigureRF.side_effect = MockFunctionCallError("niRFSG_ConfigureRF")
        mock_library.niRFSG_ConfigureRF.return_value = 0
        mock_library.niRFSG_ConfigureRefClock.side_effect = MockFunctionCallError("niRFSG_ConfigureRefClock")
        mock_library.niRFSG_ConfigureRefClock.return_value = 0
        mock_library.niRFSG_ConfigureSoftwareScriptTrigger.side_effect = MockFunctionCallError("niRFSG_ConfigureSoftwareScriptTrigger")
        mock_library.niRFSG_ConfigureSoftwareScriptTrigger.return_value = 0
        mock_library.niRFSG_ConfigureSoftwareStartTrigger.side_effect = MockFunctionCallError("niRFSG_ConfigureSoftwareStartTrigger")
        mock_library.niRFSG_ConfigureSoftwareStartTrigger.return_value = 0
        mock_library.niRFSG_CreateDeembeddingSparameterTableArray.side_effect = MockFunctionCallError("niRFSG_CreateDeembeddingSparameterTableArray")
        mock_library.niRFSG_CreateDeembeddingSparameterTableArray.return_value = 0
        mock_library.niRFSG_CreateDeembeddingSparameterTableS2PFile.side_effect = MockFunctionCallError("niRFSG_CreateDeembeddingSparameterTableS2PFile")
        mock_library.niRFSG_CreateDeembeddingSparameterTableS2PFile.return_value = 0
        mock_library.niRFSG_DeleteAllDeembeddingTables.side_effect = MockFunctionCallError("niRFSG_DeleteAllDeembeddingTables")
        mock_library.niRFSG_DeleteAllDeembeddingTables.return_value = 0
        mock_library.niRFSG_DeleteDeembeddingTable.side_effect = MockFunctionCallError("niRFSG_DeleteDeembeddingTable")
        mock_library.niRFSG_DeleteDeembeddingTable.return_value = 0
        mock_library.niRFSG_DeleteScript.side_effect = MockFunctionCallError("niRFSG_DeleteScript")
        mock_library.niRFSG_DeleteScript.return_value = 0
        mock_library.niRFSG_DisableScriptTrigger.side_effect = MockFunctionCallError("niRFSG_DisableScriptTrigger")
        mock_library.niRFSG_DisableScriptTrigger.return_value = 0
        mock_library.niRFSG_DisableStartTrigger.side_effect = MockFunctionCallError("niRFSG_DisableStartTrigger")
        mock_library.niRFSG_DisableStartTrigger.return_value = 0
        mock_library.niRFSG_ErrorMessage.side_effect = MockFunctionCallError("niRFSG_ErrorMessage")
        mock_library.niRFSG_ErrorMessage.return_value = 0
        mock_library.niRFSG_GetAllNamedWaveformNames.side_effect = MockFunctionCallError("niRFSG_GetAllNamedWaveformNames")
        mock_library.niRFSG_GetAllNamedWaveformNames.return_value = 0
        mock_library.niRFSG_GetAllScriptNames.side_effect = MockFunctionCallError("niRFSG_GetAllScriptNames")
        mock_library.niRFSG_GetAllScriptNames.return_value = 0
        mock_library.niRFSG_GetAttributeViBoolean.side_effect = MockFunctionCallError("niRFSG_GetAttributeViBoolean")
        mock_library.niRFSG_GetAttributeViBoolean.return_value = 0
        mock_library.niRFSG_GetAttributeViInt32.side_effect = MockFunctionCallError("niRFSG_GetAttributeViInt32")
        mock_library.niRFSG_GetAttributeViInt32.return_value = 0
        mock_library.niRFSG_GetAttributeViInt64.side_effect = MockFunctionCallError("niRFSG_GetAttributeViInt64")
        mock_library.niRFSG_GetAttributeViInt64.return_value = 0
        mock_library.niRFSG_GetAttributeViReal64.side_effect = MockFunctionCallError("niRFSG_GetAttributeViReal64")
        mock_library.niRFSG_GetAttributeViReal64.return_value = 0
        mock_library.niRFSG_GetAttributeViSession.side_effect = MockFunctionCallError("niRFSG_GetAttributeViSession")
        mock_library.niRFSG_GetAttributeViSession.return_value = 0
        mock_library.niRFSG_GetAttributeViString.side_effect = MockFunctionCallError("niRFSG_GetAttributeViString")
        mock_library.niRFSG_GetAttributeViString.return_value = 0
        mock_library.niRFSG_GetDeembeddingSparameters.side_effect = MockFunctionCallError("niRFSG_GetDeembeddingSparameters")
        mock_library.niRFSG_GetDeembeddingSparameters.return_value = 0
        mock_library.niRFSG_GetDeembeddingTableNumberOfPorts.side_effect = MockFunctionCallError("niRFSG_GetDeembeddingTableNumberOfPorts")
        mock_library.niRFSG_GetDeembeddingTableNumberOfPorts.return_value = 0
        mock_library.niRFSG_GetError.side_effect = MockFunctionCallError("niRFSG_GetError")
        mock_library.niRFSG_GetError.return_value = 0
        mock_library.niRFSG_GetExternalCalibrationLastDateAndTime.side_effect = MockFunctionCallError("niRFSG_GetExternalCalibrationLastDateAndTime")
        mock_library.niRFSG_GetExternalCalibrationLastDateAndTime.return_value = 0
        mock_library.niRFSG_GetMaxSettablePower.side_effect = MockFunctionCallError("niRFSG_GetMaxSettablePower")
        mock_library.niRFSG_GetMaxSettablePower.return_value = 0
        mock_library.niRFSG_GetScript.side_effect = MockFunctionCallError("niRFSG_GetScript")
        mock_library.niRFSG_GetScript.return_value = 0
        mock_library.niRFSG_GetSelfCalibrationDateAndTime.side_effect = MockFunctionCallError("niRFSG_GetSelfCalibrationDateAndTime")
        mock_library.niRFSG_GetSelfCalibrationDateAndTime.return_value = 0
        mock_library.niRFSG_GetSelfCalibrationTemperature.side_effect = MockFunctionCallError("niRFSG_GetSelfCalibrationTemperature")
        mock_library.niRFSG_GetSelfCalibrationTemperature.return_value = 0
        mock_library.niRFSG_GetTerminalName.side_effect = MockFunctionCallError("niRFSG_GetTerminalName")
        mock_library.niRFSG_GetTerminalName.return_value = 0
        mock_library.niRFSG_GetWaveformBurstStartLocations.side_effect = MockFunctionCallError("niRFSG_GetWaveformBurstStartLocations")
        mock_library.niRFSG_GetWaveformBurstStartLocations.return_value = 0
        mock_library.niRFSG_GetWaveformBurstStopLocations.side_effect = MockFunctionCallError("niRFSG_GetWaveformBurstStopLocations")
        mock_library.niRFSG_GetWaveformBurstStopLocations.return_value = 0
        mock_library.niRFSG_GetWaveformMarkerEventLocations.side_effect = MockFunctionCallError("niRFSG_GetWaveformMarkerEventLocations")
        mock_library.niRFSG_GetWaveformMarkerEventLocations.return_value = 0
        mock_library.niRFSG_InitWithOptions.side_effect = MockFunctionCallError("niRFSG_InitWithOptions")
        mock_library.niRFSG_InitWithOptions.return_value = 0
        mock_library.niRFSG_Initiate.side_effect = MockFunctionCallError("niRFSG_Initiate")
        mock_library.niRFSG_Initiate.return_value = 0
        mock_library.niRFSG_LoadConfigurationsFromFile.side_effect = MockFunctionCallError("niRFSG_LoadConfigurationsFromFile")
        mock_library.niRFSG_LoadConfigurationsFromFile.return_value = 0
        mock_library.niRFSG_LockSession.side_effect = MockFunctionCallError("niRFSG_LockSession")
        mock_library.niRFSG_LockSession.return_value = 0
        mock_library.niRFSG_PerformPowerSearch.side_effect = MockFunctionCallError("niRFSG_PerformPowerSearch")
        mock_library.niRFSG_PerformPowerSearch.return_value = 0
        mock_library.niRFSG_PerformThermalCorrection.side_effect = MockFunctionCallError("niRFSG_PerformThermalCorrection")
        mock_library.niRFSG_PerformThermalCorrection.return_value = 0
        mock_library.niRFSG_QueryArbWaveformCapabilities.side_effect = MockFunctionCallError("niRFSG_QueryArbWaveformCapabilities")
        mock_library.niRFSG_QueryArbWaveformCapabilities.return_value = 0
        mock_library.niRFSG_ReadAndDownloadWaveformFromFileTDMS.side_effect = MockFunctionCallError("niRFSG_ReadAndDownloadWaveformFromFileTDMS")
        mock_library.niRFSG_ReadAndDownloadWaveformFromFileTDMS.return_value = 0
        mock_library.niRFSG_ResetDevice.side_effect = MockFunctionCallError("niRFSG_ResetDevice")
        mock_library.niRFSG_ResetDevice.return_value = 0
        mock_library.niRFSG_ResetWithDefaults.side_effect = MockFunctionCallError("niRFSG_ResetWithDefaults")
        mock_library.niRFSG_ResetWithDefaults.return_value = 0
        mock_library.niRFSG_ResetWithOptions.side_effect = MockFunctionCallError("niRFSG_ResetWithOptions")
        mock_library.niRFSG_ResetWithOptions.return_value = 0
        mock_library.niRFSG_SaveConfigurationsToFile.side_effect = MockFunctionCallError("niRFSG_SaveConfigurationsToFile")
        mock_library.niRFSG_SaveConfigurationsToFile.return_value = 0
        mock_library.niRFSG_SelectArbWaveform.side_effect = MockFunctionCallError("niRFSG_SelectArbWaveform")
        mock_library.niRFSG_SelectArbWaveform.return_value = 0
        mock_library.niRFSG_SelfCal.side_effect = MockFunctionCallError("niRFSG_SelfCal")
        mock_library.niRFSG_SelfCal.return_value = 0
        mock_library.niRFSG_SelfCalibrateRange.side_effect = MockFunctionCallError("niRFSG_SelfCalibrateRange")
        mock_library.niRFSG_SelfCalibrateRange.return_value = 0
        mock_library.niRFSG_SendSoftwareEdgeTrigger.side_effect = MockFunctionCallError("niRFSG_SendSoftwareEdgeTrigger")
        mock_library.niRFSG_SendSoftwareEdgeTrigger.return_value = 0
        mock_library.niRFSG_SetArbWaveformNextWritePosition.side_effect = MockFunctionCallError("niRFSG_SetArbWaveformNextWritePosition")
        mock_library.niRFSG_SetArbWaveformNextWritePosition.return_value = 0
        mock_library.niRFSG_SetAttributeViBoolean.side_effect = MockFunctionCallError("niRFSG_SetAttributeViBoolean")
        mock_library.niRFSG_SetAttributeViBoolean.return_value = 0
        mock_library.niRFSG_SetAttributeViInt32.side_effect = MockFunctionCallError("niRFSG_SetAttributeViInt32")
        mock_library.niRFSG_SetAttributeViInt32.return_value = 0
        mock_library.niRFSG_SetAttributeViInt64.side_effect = MockFunctionCallError("niRFSG_SetAttributeViInt64")
        mock_library.niRFSG_SetAttributeViInt64.return_value = 0
        mock_library.niRFSG_SetAttributeViReal64.side_effect = MockFunctionCallError("niRFSG_SetAttributeViReal64")
        mock_library.niRFSG_SetAttributeViReal64.return_value = 0
        mock_library.niRFSG_SetAttributeViSession.side_effect = MockFunctionCallError("niRFSG_SetAttributeViSession")
        mock_library.niRFSG_SetAttributeViSession.return_value = 0
        mock_library.niRFSG_SetAttributeViString.side_effect = MockFunctionCallError("niRFSG_SetAttributeViString")
        mock_library.niRFSG_SetAttributeViString.return_value = 0
        mock_library.niRFSG_SetWaveformBurstStartLocations.side_effect = MockFunctionCallError("niRFSG_SetWaveformBurstStartLocations")
        mock_library.niRFSG_SetWaveformBurstStartLocations.return_value = 0
        mock_library.niRFSG_SetWaveformBurstStopLocations.side_effect = MockFunctionCallError("niRFSG_SetWaveformBurstStopLocations")
        mock_library.niRFSG_SetWaveformBurstStopLocations.return_value = 0
        mock_library.niRFSG_SetWaveformMarkerEventLocations.side_effect = MockFunctionCallError("niRFSG_SetWaveformMarkerEventLocations")
        mock_library.niRFSG_SetWaveformMarkerEventLocations.return_value = 0
        mock_library.niRFSG_UnlockSession.side_effect = MockFunctionCallError("niRFSG_UnlockSession")
        mock_library.niRFSG_UnlockSession.return_value = 0
        mock_library.niRFSG_WaitUntilSettled.side_effect = MockFunctionCallError("niRFSG_WaitUntilSettled")
        mock_library.niRFSG_WaitUntilSettled.return_value = 0
        mock_library.niRFSG_WriteArbWaveformComplexF32.side_effect = MockFunctionCallError("niRFSG_WriteArbWaveformComplexF32")
        mock_library.niRFSG_WriteArbWaveformComplexF32.return_value = 0
        mock_library.niRFSG_WriteArbWaveformComplexF64.side_effect = MockFunctionCallError("niRFSG_WriteArbWaveformComplexF64")
        mock_library.niRFSG_WriteArbWaveformComplexF64.return_value = 0
        mock_library.niRFSG_WriteArbWaveformComplexI16.side_effect = MockFunctionCallError("niRFSG_WriteArbWaveformComplexI16")
        mock_library.niRFSG_WriteArbWaveformComplexI16.return_value = 0
        mock_library.niRFSG_WriteScript.side_effect = MockFunctionCallError("niRFSG_WriteScript")
        mock_library.niRFSG_WriteScript.return_value = 0
        mock_library.niRFSG_close.side_effect = MockFunctionCallError("niRFSG_close")
        mock_library.niRFSG_close.return_value = 0
        mock_library.niRFSG_reset.side_effect = MockFunctionCallError("niRFSG_reset")
        mock_library.niRFSG_reset.return_value = 0
        mock_library.niRFSG_self_test.side_effect = MockFunctionCallError("niRFSG_self_test")
        mock_library.niRFSG_self_test.return_value = 0
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nirfsg/nirfsg/VERSION sha256=6e2a1b2ebc11dbf0a7cb0011b1825adb84166efda02fdeddcec9d40c3c6a5100 bytes=12 -->
## FILE: generated/nirfsg/nirfsg/VERSION

- repository: `ni/nimi-python`
- source_path: `generated/nirfsg/nirfsg/VERSION`
- sha256: `6e2a1b2ebc11dbf0a7cb0011b1825adb84166efda02fdeddcec9d40c3c6a5100`
- bytes: 12

````text
1.1.1.dev0
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nirfsg/README.rst sha256=c7b74d86585d7dc9452eca6dc20043c1341cd81c51f858a258983b8ef78c7bfe bytes=7179 -->
## FILE: generated/nirfsg/README.rst

- repository: `ni/nimi-python`
- source_path: `generated/nirfsg/README.rst`
- sha256: `c7b74d86585d7dc9452eca6dc20043c1341cd81c51f858a258983b8ef78c7bfe`
- bytes: 7179

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

The **nirfsg** module provides a Python API for NI-RFSG. The code is maintained in the Open Source repository for `nimi-python <https://github.com/ni/nimi-python>`_.

Support Policy
--------------
**nirfsg** supports all the Operating Systems supported by NI-RFSG.

It follows `Python Software Foundation <https://devguide.python.org/#status-of-python-branches>`_ support policy for different versions of CPython.

NI created and supports **nirfsg**.


NI-RFSG Python API Status
-------------------------

+-------------------------------+-----------------------+
| NI-RFSG (nirfsg)              |                       |
+===============================+=======================+
| Driver Version Tested Against | 2025 Q4 Patch 1       |
+-------------------------------+-----------------------+
| PyPI Version                  | |nirfsgLatestVersion| |
+-------------------------------+-----------------------+
| Supported Python Version      | |nirfsgPythonVersion| |
+-------------------------------+-----------------------+
| Documentation                 | |nirfsgDocs|          |
+-------------------------------+-----------------------+
| Open Issues                   | |nirfsgOpenIssues|    |
+-------------------------------+-----------------------+
| Open Pull Requests            | |nirfsgOpenPRs|       |
+-------------------------------+-----------------------+


.. |nirfsgLatestVersion| image:: http://img.shields.io/pypi/v/nirfsg.svg
    :alt: Latest NI-RFSG Version
    :target: http://pypi.python.org/pypi/nirfsg


.. |nirfsgPythonVersion| image:: http://img.shields.io/pypi/pyversions/nirfsg.svg
    :alt: NI-RFSG supported Python versions
    :target: http://pypi.python.org/pypi/nirfsg


.. |nirfsgDocs| image:: https://readthedocs.org/projects/nirfsg/badge/?version=latest
    :alt: NI-RFSG Python API Documentation Status
    :target: https://nirfsg.readthedocs.io/en/latest


.. |nirfsgOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/nirfsg.svg
    :alt: Open Issues + Pull Requests for NI-RFSG
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Anirfsg


.. |nirfsgOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/nirfsg.svg
    :alt: Pull Requests for NI-RFSG
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Anirfsg



.. _nirfsg_installation-section:

Installation
------------

As a prerequisite to using the **nirfsg** module, you must install the NI-RFSG runtime on your system. Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the driver runtime for your devices.

The nimi-python modules (i.e. for **NI-RFSG**) can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install nirfsg


Contributing
============

We welcome contributions! You can clone the project repository, build it, and install it by `following these instructions <https://github.com/ni/nimi-python/blob/master/CONTRIBUTING.md>`_.

Usage
------

The following is a basic example of using the **nirfsg** module to open a session to an RF Signal Generator and generate a continuous wave (CW) signal.

.. code-block:: python

    import nirfsg

    # Configure the session
    with nirfsg.Session(resource_name='5841', id_query=False, reset_device=False, options='Simulate=1, DriverSetup=Model:5841') as session:
        # Configure RF settings
        session.configure_rf(
            frequency=1e9,  # Frequency in Hz
            power_level=-10.0  # Power level in dBm
        )
        session.generation_mode = nirfsg.GenerationMode.CW

        # Start signal generation
        with session.initiate():
            input("Press Enter to stop generation")

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nirfsg/examples>`_.. _support-section:

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

Documentation is available `here <http://nirfsg.readthedocs.io>`_.


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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nirfsg/setup.py sha256=8677738d469a6bfb736d574e012f67cdec565bd813b27f8e3121e9f2ac545985 bytes=1839 -->
## FILE: generated/nirfsg/setup.py

- repository: `ni/nimi-python`
- source_path: `generated/nirfsg/setup.py`
- sha256: `8677738d469a6bfb736d574e012f67cdec565bd813b27f8e3121e9f2ac545985`
- bytes: 1839

````python
#!/usr/bin/python
# This file was generated


from setuptools import setup


pypi_name = 'nirfsg'


def read_contents(file_to_read):
    with open(file_to_read, 'r') as f:
        return f.read()


setup(
    name=pypi_name,
    zip_safe=True,
    version='1.1.1.dev0',
    description='NI-RFSG Python API',
    long_description=read_contents('README.rst'),
    long_description_content_type='text/x-rst',
    author='NI',
    author_email="opensource@ni.com",
    url="https://github.com/ni/nimi-python",
    maintainer="NI",
    maintainer_email="opensource@ni.com",
    keywords=['nirfsg'],
    license='MIT',
    include_package_data=True,
    packages=['nirfsg'],
    python_requires='>=3.10',
    install_requires=[
        'hightime>=0.2.0',
        'nitclk',
        'numpy',
    ],
    extras_require={
        'grpc': [
            'grpcio>=1.59.0,<2.0',
            'protobuf>=4.21.6',
            'ni.grpcdevice.v1.proto>=1.0.0'
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nirfsg/tox-system_tests.ini sha256=75e7336073ab9473f0b67d4456b89acf505afb41090feba29f647b07205486d7 bytes=3058 -->
## FILE: generated/nirfsg/tox-system_tests.ini

- repository: `ni/nimi-python`
- source_path: `generated/nirfsg/tox-system_tests.ini`
- sha256: `75e7336073ab9473f0b67d4456b89acf505afb41090feba29f647b07205486d7`
- bytes: 3058

````ini
# Tox (http://tox.testrun.org/) is a tool for running tests
# in multiple virtualenvs. This configuration file will run the
# test suite on all supported python versions. To use it, "pip install tox"
# and then run "tox -c tox-system_tests.ini" from the driver directory. (generated/nirfsg)
[tox]
envlist = py{310,311,312,313,314}-nirfsg-wheel_dep,py{310,311,312,313,314}-nirfsg-system_tests, py314-nirfsg-coverage
skip_missing_interpreters=True
ignore_basepython_conflict=True
# We put the .tox directory outside of the Jenkins workspace so that it isn't wiped with the rest of the repo
toxworkdir = ../../../.tox

[testenv]
description =
    nirfsg-wheel_dep: Build the nitclk wheel because we use it in nirfsg tests
    nirfsg-system_tests: Run nirfsg system tests (requires NI-RFSG runtime to be installed)
    nirfsg-coverage: Prepare coverage report for upload to codecov.io  # upload handled by GitHub Actions

changedir =
    nirfsg-wheel_dep: ../nitclk
    nirfsg-system_tests: .
    nirfsg-coverage: .

commands =
    nirfsg-wheel_dep: python -m build --wheel

    # --disable-pip-version-check prevents pip from telling us we need to upgrade pip, since we are doing that now
    nirfsg-system_tests: python -m pip install --disable-pip-version-check --upgrade pip
    nirfsg-system_tests: python ../../tools/install_local_wheel.py --driver nitclk --start-path ../..
    nirfsg-system_tests: python -c "import nirfsg; nirfsg.print_diagnostic_information()"
    nirfsg-system_tests: coverage run --rcfile=../../tools/coverage_system_tests.rc --source nirfsg --parallel-mode -m pytest ../../src/nirfsg/examples --junitxml=../junit/junit-nirfsg-{envname}-examples-{env:BITNESS:64}.xml {posargs}
    nirfsg-system_tests: coverage run --rcfile=../../tools/coverage_system_tests.rc --source nirfsg --parallel-mode -m pytest ../../src/nirfsg/system_tests -c tox-system_tests.ini --junitxml=../junit/junit-nirfsg-{envname}-{env:BITNESS:64}.xml --durations=5 {posargs}

    nirfsg-coverage: coverage combine --rcfile=../../tools/coverage_system_tests.rc ./
    # Create the report to upload
    nirfsg-coverage: coverage xml -i --rcfile=../../tools/coverage_system_tests.rc
    # Display the coverage results
    nirfsg-coverage: coverage report --rcfile=../../tools/coverage_system_tests.rc

deps =
    nirfsg-wheel_dep: build

    nirfsg-system_tests: pytest
    nirfsg-system_tests: coverage
    nirfsg-system_tests: numpy
    nirfsg-system_tests: hightime
    nirfsg-system_tests: fasteners
    nirfsg-system_tests: pytest-json
    nirfsg-system_tests: .[grpc]

    nirfsg-coverage: coverage

depends =
    nirfsg-coverage: py{310,311,312,313,314}-nirfsg-system_tests
    nirfsg-system_tests: py{310,311,312,313,314}-nirfsg-wheel_dep,

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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/niscope/niscope/__init__.py sha256=194e8637d5adad5008c403fd0d618713681e7396ebe931320d989fe744f8b36b bytes=3502 -->
## FILE: generated/niscope/niscope/__init__.py

- repository: `ni/nimi-python`
- source_path: `generated/niscope/niscope/__init__.py`
- sha256: `194e8637d5adad5008c403fd0d618713681e7396ebe931320d989fe744f8b36b`
- bytes: 3502

````python
# -*- coding: utf-8 -*-
# This file was generated


__version__ = '1.4.10.dev0'

from niscope.enums import *  # noqa: F403,F401,H303
from niscope.errors import DriverWarning  # noqa: F401
from niscope.errors import Error  # noqa: F401
from niscope.grpc_session_options import *  # noqa: F403,F401,H303
from niscope.session import Session  # noqa: F401

from niscope.waveform_info import WaveformInfo  # noqa: F401

from niscope.waveform_info import struct_niScope_wfmInfo  # noqa: F401

from niscope.measurement_stats import MeasurementStats  # noqa: F401


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
            driver_version_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\National Instruments\NI-SCOPE\CurrentVersion")
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
    info['driver']['name'] = "NI-SCOPE"
    info['driver']['version'] = driver_version
    info['module']['name'] = 'niscope'
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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/niscope/niscope/_attributes.py sha256=c0c88f7193f1dbffc7cafbbe9d0823ff7320793cde761d31a42758486ecd2a35 bytes=6179 -->
## FILE: generated/niscope/niscope/_attributes.py

- repository: `ni/nimi-python`
- source_path: `generated/niscope/niscope/_attributes.py`
- sha256: `c0c88f7193f1dbffc7cafbbe9d0823ff7320793cde761d31a42758486ecd2a35`
- bytes: 6179

````python
# -*- coding: utf-8 -*-
# This file was generated
import niscope._converters as _converters
import niscope.errors as errors

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
    '''Class for attributes that use enums internally but are exposed in the niscope Python module as something else, thus need conversion.'''

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
        from niscope.session import SessionReference
        return SessionReference(session._get_attribute_vi_session(self._attribute_id))

    def __set__(self, session, value):
        session._set_attribute_vi_session(self._attribute_id, _converters.convert_to_nitclk_session_number(value))
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/niscope/niscope/_converters.py sha256=02d77fc5b78128a19169b24259d2cf12a61e8285f4ada36444757080f3165938 bytes=14623 -->
## FILE: generated/niscope/niscope/_converters.py

- repository: `ni/nimi-python`
- source_path: `generated/niscope/niscope/_converters.py`
- sha256: `02d77fc5b78128a19169b24259d2cf12a61e8285f4ada36444757080f3165938`
- bytes: 14623

````python
# -*- coding: utf-8 -*-
# This file was generated
import niscope._visatype as _visatype
import niscope.errors as errors

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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/niscope/niscope/_grpc_stub_interpreter.py sha256=601067c169fa12202e5053968d52734e2159f8beed17e775cc226e5b04d4a4d6 bytes=20920 -->
## FILE: generated/niscope/niscope/_grpc_stub_interpreter.py

- repository: `ni/nimi-python`
- source_path: `generated/niscope/niscope/_grpc_stub_interpreter.py`
- sha256: `601067c169fa12202e5053968d52734e2159f8beed17e775cc226e5b04d4a4d6`
- bytes: 20920

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
from . import niscope_pb2 as grpc_types
from . import niscope_pb2_grpc as niscope_grpc

from . import waveform_info as waveform_info  # noqa: F401

from . import measurement_stats as measurement_stats  # noqa: F401


class GrpcStubInterpreter(object):
    '''Interpreter for interacting with a gRPC Stub class'''

    def __init__(self, grpc_options):
        self._grpc_options = grpc_options
        self._lock = threading.RLock()
        self._client = niscope_grpc.NiScopeStub(grpc_options.grpc_channel)
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

    def acquisition_status(self):  # noqa: N802
        response = self._invoke(
            self._client.AcquisitionStatus,
            grpc_types.AcquisitionStatusRequest(vi=self._vi),
        )
        return enums.AcquisitionStatus(response.acquisition_status_raw)

    def actual_meas_wfm_size(self, array_meas_function):  # noqa: N802
        response = self._invoke(
            self._client.ActualMeasWfmSize,
            grpc_types.ActualMeasWfmSizeRequest(vi=self._vi, array_meas_function_raw=array_meas_function.value),
        )
        return response.meas_waveform_size

    def actual_num_wfms(self, channel_list):  # noqa: N802
        response = self._invoke(
            self._client.ActualNumWfms,
            grpc_types.ActualNumWfmsRequest(vi=self._vi, channel_list=channel_list),
        )
        return response.num_wfms

    def add_waveform_processing(self, channel_list, meas_function):  # noqa: N802
        self._invoke(
            self._client.AddWaveformProcessing,
            grpc_types.AddWaveformProcessingRequest(vi=self._vi, channel_list=channel_list, meas_function_raw=meas_function.value),
        )

    def auto_setup(self):  # noqa: N802
        self._invoke(
            self._client.AutoSetup,
            grpc_types.AutoSetupRequest(vi=self._vi),
        )

    def cal_fetch_date(self, which_one):  # noqa: N802
        response = self._invoke(
            self._client.CalFetchDate,
            grpc_types.CalFetchDateRequest(vi=self._vi, which_one_raw=which_one.value),
        )
        return response.year, response.month, response.day

    def cal_fetch_temperature(self, which_one):  # noqa: N802
        response = self._invoke(
            self._client.CalFetchTemperature,
            grpc_types.CalFetchTemperatureRequest(vi=self._vi, which_one_raw=which_one),
        )
        return response.temperature

    def self_cal(self, channel_list, option):  # noqa: N802
        self._invoke(
            self._client.CalSelfCalibrate,
            grpc_types.CalSelfCalibrateRequest(vi=self._vi, channel_list=channel_list, option_raw=option.value),
        )

    def clear_waveform_measurement_stats(self, channel_list, clearable_measurement_function):  # noqa: N802
        self._invoke(
            self._client.ClearWaveformMeasurementStats,
            grpc_types.ClearWaveformMeasurementStatsRequest(vi=self._vi, channel_list=channel_list, clearable_measurement_function_raw=clearable_measurement_function.value),
        )

    def clear_waveform_processing(self, channel_list):  # noqa: N802
        self._invoke(
            self._client.ClearWaveformProcessing,
            grpc_types.ClearWaveformProcessingRequest(vi=self._vi, channel_list=channel_list),
        )

    def commit(self):  # noqa: N802
        self._invoke(
            self._client.Commit,
            grpc_types.CommitRequest(vi=self._vi),
        )

    def configure_chan_characteristics(self, channel_list, input_impedance, max_input_frequency):  # noqa: N802
        self._invoke(
            self._client.ConfigureChanCharacteristics,
            grpc_types.ConfigureChanCharacteristicsRequest(vi=self._vi, channel_list=channel_list, input_impedance=input_impedance, max_input_frequency=max_input_frequency),
        )

    def configure_equalization_filter_coefficients(self, channel_list, coefficients):  # noqa: N802
        self._invoke(
            self._client.ConfigureEqualizationFilterCoefficients,
            grpc_types.ConfigureEqualizationFilterCoefficientsRequest(vi=self._vi, channel_list=channel_list, coefficients=coefficients),
        )

    def configure_horizontal_timing(self, min_sample_rate, min_num_pts, ref_position, num_records, enforce_realtime):  # noqa: N802
        self._invoke(
            self._client.ConfigureHorizontalTiming,
            grpc_types.ConfigureHorizontalTimingRequest(vi=self._vi, min_sample_rate=min_sample_rate, min_num_pts=min_num_pts, ref_position=ref_position, num_records=num_records, enforce_realtime=enforce_realtime),
        )

    def configure_ref_levels(self, low, mid, high):  # noqa: N802
        raise NotImplementedError('configure_ref_levels is not supported over gRPC')

    def configure_trigger_digital(self, trigger_source, slope, holdoff, delay):  # noqa: N802
        self._invoke(
            self._client.ConfigureTriggerDigital,
            grpc_types.ConfigureTriggerDigitalRequest(vi=self._vi, trigger_source=trigger_source, slope_raw=slope.value, holdoff=holdoff, delay=delay),
        )

    def configure_trigger_edge(self, trigger_source, level, slope, trigger_coupling, holdoff, delay):  # noqa: N802
        self._invoke(
            self._client.ConfigureTriggerEdge,
            grpc_types.ConfigureTriggerEdgeRequest(vi=self._vi, trigger_source=trigger_source, level=level, slope_raw=slope.value, trigger_coupling_raw=trigger_coupling.value, holdoff=holdoff, delay=delay),
        )

    def configure_trigger_hysteresis(self, trigger_source, level, hysteresis, slope, trigger_coupling, holdoff, delay):  # noqa: N802
        self._invoke(
            self._client.ConfigureTriggerHysteresis,
            grpc_types.ConfigureTriggerHysteresisRequest(vi=self._vi, trigger_source=trigger_source, level=level, hysteresis=hysteresis, slope_raw=slope.value, trigger_coupling_raw=trigger_coupling.value, holdoff=holdoff, delay=delay),
        )

    def configure_trigger_immediate(self):  # noqa: N802
        self._invoke(
            self._client.ConfigureTriggerImmediate,
            grpc_types.ConfigureTriggerImmediateRequest(vi=self._vi),
        )

    def configure_trigger_software(self, holdoff, delay):  # noqa: N802
        self._invoke(
            self._client.ConfigureTriggerSoftware,
            grpc_types.ConfigureTriggerSoftwareRequest(vi=self._vi, holdoff=holdoff, delay=delay),
        )

    def configure_trigger_video(self, trigger_source, enable_dc_restore, signal_format, event, line_number, polarity, trigger_coupling, holdoff, delay):  # noqa: N802
        self._invoke(
            self._client.ConfigureTriggerVideo,
            grpc_types.ConfigureTriggerVideoRequest(vi=self._vi, trigger_source=trigger_source, enable_dc_restore=enable_dc_restore, signal_format_raw=signal_format.value, event_raw=event.value, line_number=line_number, polarity_raw=polarity.value, trigger_coupling_raw=trigger_coupling.value, holdoff=holdoff, delay=delay),
        )

    def configure_trigger_window(self, trigger_source, low_level, high_level, window_mode, trigger_coupling, holdoff, delay):  # noqa: N802
        self._invoke(
            self._client.ConfigureTriggerWindow,
            grpc_types.ConfigureTriggerWindowRequest(vi=self._vi, trigger_source=trigger_source, low_level=low_level, high_level=high_level, window_mode_raw=window_mode.value, trigger_coupling_raw=trigger_coupling.value, holdoff=holdoff, delay=delay),
        )

    def configure_vertical(self, channel_list, range, offset, coupling, probe_attenuation, enabled):  # noqa: N802
        self._invoke(
            self._client.ConfigureVertical,
            grpc_types.ConfigureVerticalRequest(vi=self._vi, channel_list=channel_list, range=range, offset=offset, coupling_raw=coupling.value, probe_attenuation=probe_attenuation, enabled=enabled),
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

    def fetch(self, channel_list, timeout, num_samples):  # noqa: N802
        response = self._invoke(
            self._client.Fetch,
            grpc_types.FetchRequest(vi=self._vi, channel_list=channel_list, timeout=timeout, num_samples=num_samples),
        )
        return response.waveform, [waveform_info.WaveformInfo(x) for x in response.wfm_info]

    def fetch_into_numpy(self, channel_list, timeout, num_samples):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')

    def fetch_array_measurement(self, channel_list, timeout, array_meas_function, measurement_waveform_size):  # noqa: N802
        response = self._invoke(
            self._client.FetchArrayMeasurement,
            grpc_types.FetchArrayMeasurementRequest(vi=self._vi, channel_list=channel_list, timeout=timeout, array_meas_function_raw=array_meas_function.value, meas_wfm_size=measurement_waveform_size),
        )
        return response.meas_wfm, [waveform_info.WaveformInfo(x) for x in response.wfm_info]

    def fetch_binary16_into_numpy(self, channel_list, timeout, num_samples):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')

    def fetch_binary32_into_numpy(self, channel_list, timeout, num_samples):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')

    def fetch_binary8_into_numpy(self, channel_list, timeout, num_samples):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')

    def fetch_measurement_stats(self, channel_list, timeout, scalar_meas_function):  # noqa: N802
        response = self._invoke(
            self._client.FetchMeasurementStats,
            grpc_types.FetchMeasurementStatsRequest(vi=self._vi, channel_list=channel_list, timeout=timeout, scalar_meas_function_raw=scalar_meas_function.value),
        )
        return response.result, response.mean, response.stdev, response.min, response.max, response.num_in_stats

    def get_attribute_vi_boolean(self, channel_list, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViBoolean,
            grpc_types.GetAttributeViBooleanRequest(vi=self._vi, channel_list=channel_list, attribute_id=attribute_id),
        )
        return response.value

    def get_attribute_vi_int32(self, channel_list, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViInt32,
            grpc_types.GetAttributeViInt32Request(vi=self._vi, channel_list=channel_list, attribute_id=attribute_id),
        )
        return response.value

    def get_attribute_vi_int64(self, channel_list, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViInt64,
            grpc_types.GetAttributeViInt64Request(vi=self._vi, channel_list=channel_list, attribute_id=attribute_id),
        )
        return response.value

    def get_attribute_vi_real64(self, channel_list, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViReal64,
            grpc_types.GetAttributeViReal64Request(vi=self._vi, channel_list=channel_list, attribute_id=attribute_id),
        )
        return response.value

    def get_attribute_vi_string(self, channel_list, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViString,
            grpc_types.GetAttributeViStringRequest(vi=self._vi, channel_list=channel_list, attribute_id=attribute_id),
        )
        return response.value

    def get_channel_names(self, indices):  # noqa: N802
        response = self._invoke(
            self._client.GetChannelNameFromString,
            grpc_types.GetChannelNameFromStringRequest(vi=self._vi, index=indices),
        )
        return response.name

    def get_equalization_filter_coefficients(self, channel, number_of_coefficients):  # noqa: N802
        response = self._invoke(
            self._client.GetEqualizationFilterCoefficients,
            grpc_types.GetEqualizationFilterCoefficientsRequest(vi=self._vi, channel=channel, number_of_coefficients=number_of_coefficients),
        )
        return response.coefficients

    def get_error(self):  # noqa: N802
        response = self._invoke(
            self._client.GetError,
            grpc_types.GetErrorRequest(vi=self._vi),
        )
        return response.error_code, response.description

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

    def initiate_acquisition(self):  # noqa: N802
        self._invoke(
            self._client.InitiateAcquisition,
            grpc_types.InitiateAcquisitionRequest(vi=self._vi),
        )

    def lock(self):  # noqa: N802
        self._lock.acquire()

    def probe_compensation_signal_start(self):  # noqa: N802
        self._invoke(
            self._client.ProbeCompensationSignalStart,
            grpc_types.ProbeCompensationSignalStartRequest(vi=self._vi),
        )

    def probe_compensation_signal_stop(self):  # noqa: N802
        self._invoke(
            self._client.ProbeCompensationSignalStop,
            grpc_types.ProbeCompensationSignalStopRequest(vi=self._vi),
        )

    def read(self, channel_list, timeout, num_samples):  # noqa: N802
        response = self._invoke(
            self._client.Read,
            grpc_types.ReadRequest(vi=self._vi, channel_list=channel_list, timeout=timeout, num_samples=num_samples),
        )
        return response.waveform, [waveform_info.WaveformInfo(x) for x in response.wfm_info]

    def reset_device(self):  # noqa: N802
        self._invoke(
            self._client.ResetDevice,
            grpc_types.ResetDeviceRequest(vi=self._vi),
        )

    def reset_with_defaults(self):  # noqa: N802
        raise NotImplementedError('reset_with_defaults is not supported over gRPC')

    def send_software_trigger_edge(self, which_trigger):  # noqa: N802
        self._invoke(
            self._client.SendSoftwareTriggerEdge,
            grpc_types.SendSoftwareTriggerEdgeRequest(vi=self._vi, which_trigger_raw=which_trigger.value),
        )

    def set_attribute_vi_boolean(self, channel_list, attribute_id, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViBoolean,
            grpc_types.SetAttributeViBooleanRequest(vi=self._vi, channel_list=channel_list, attribute_id=attribute_id, value=value),
        )

    def set_attribute_vi_int32(self, channel_list, attribute_id, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViInt32,
            grpc_types.SetAttributeViInt32Request(vi=self._vi, channel_list=channel_list, attribute_id=attribute_id, value_raw=value),
        )

    def set_attribute_vi_int64(self, channel_list, attribute_id, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViInt64,
            grpc_types.SetAttributeViInt64Request(vi=self._vi, channel_list=channel_list, attribute_id=attribute_id, value_raw=value),
        )

    def set_attribute_vi_real64(self, channel_list, attribute_id, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViReal64,
            grpc_types.SetAttributeViReal64Request(vi=self._vi, channel_list=channel_list, attribute_id=attribute_id, value_raw=value),
        )

    def set_attribute_vi_string(self, channel_list, attribute_id, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViString,
            grpc_types.SetAttributeViStringRequest(vi=self._vi, channel_list=channel_list, attribute_id=attribute_id, value_raw=value),
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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/niscope/niscope/_library.py sha256=09c3d498fc2649decc1d29aad7e64756218efe92d1bf4c024108e5e025232ceb bytes=43533 -->
## FILE: generated/niscope/niscope/_library.py

- repository: `ni/nimi-python`
- source_path: `generated/niscope/niscope/_library.py`
- sha256: `09c3d498fc2649decc1d29aad7e64756218efe92d1bf4c024108e5e025232ceb`
- bytes: 43533

````python
# -*- coding: utf-8 -*-
# This file was generated

import ctypes
import niscope.errors as errors
import threading

from niscope._visatype import *  # noqa: F403,H303

import niscope.waveform_info as waveform_info  # noqa: F401

import niscope.measurement_stats as measurement_stats  # noqa: F401


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, ctypes_library):
        self._func_lock = threading.Lock()
        self._library = ctypes_library
        # We cache the cfunc object from the ctypes.CDLL object
        self.niScope_Abort_cfunc = None
        self.niScope_AcquisitionStatus_cfunc = None
        self.niScope_ActualMeasWfmSize_cfunc = None
        self.niScope_ActualNumWfms_cfunc = None
        self.niScope_AddWaveformProcessing_cfunc = None
        self.niScope_AutoSetup_cfunc = None
        self.niScope_CalFetchDate_cfunc = None
        self.niScope_CalFetchTemperature_cfunc = None
        self.niScope_CalSelfCalibrate_cfunc = None
        self.niScope_ClearWaveformMeasurementStats_cfunc = None
        self.niScope_ClearWaveformProcessing_cfunc = None
        self.niScope_Commit_cfunc = None
        self.niScope_ConfigureChanCharacteristics_cfunc = None
        self.niScope_ConfigureEqualizationFilterCoefficients_cfunc = None
        self.niScope_ConfigureHorizontalTiming_cfunc = None
        self.niScope_ConfigureRefLevels_cfunc = None
        self.niScope_ConfigureTriggerDigital_cfunc = None
        self.niScope_ConfigureTriggerEdge_cfunc = None
        self.niScope_ConfigureTriggerHysteresis_cfunc = None
        self.niScope_ConfigureTriggerImmediate_cfunc = None
        self.niScope_ConfigureTriggerSoftware_cfunc = None
        self.niScope_ConfigureTriggerVideo_cfunc = None
        self.niScope_ConfigureTriggerWindow_cfunc = None
        self.niScope_ConfigureVertical_cfunc = None
        self.niScope_Disable_cfunc = None
        self.niScope_ExportAttributeConfigurationBuffer_cfunc = None
        self.niScope_ExportAttributeConfigurationFile_cfunc = None
        self.niScope_Fetch_cfunc = None
        self.niScope_FetchArrayMeasurement_cfunc = None
        self.niScope_FetchBinary16_cfunc = None
        self.niScope_FetchBinary32_cfunc = None
        self.niScope_FetchBinary8_cfunc = None
        self.niScope_FetchMeasurementStats_cfunc = None
        self.niScope_GetAttributeViBoolean_cfunc = None
        self.niScope_GetAttributeViInt32_cfunc = None
        self.niScope_GetAttributeViInt64_cfunc = None
        self.niScope_GetAttributeViReal64_cfunc = None
        self.niScope_GetAttributeViString_cfunc = None
        self.niScope_GetChannelNameFromString_cfunc = None
        self.niScope_GetEqualizationFilterCoefficients_cfunc = None
        self.niScope_GetError_cfunc = None
        self.niScope_ImportAttributeConfigurationBuffer_cfunc = None
        self.niScope_ImportAttributeConfigurationFile_cfunc = None
        self.niScope_InitWithOptions_cfunc = None
        self.niScope_InitiateAcquisition_cfunc = None
        self.niScope_LockSession_cfunc = None
        self.niScope_ProbeCompensationSignalStart_cfunc = None
        self.niScope_ProbeCompensationSignalStop_cfunc = None
        self.niScope_Read_cfunc = None
        self.niScope_ResetDevice_cfunc = None
        self.niScope_ResetWithDefaults_cfunc = None
        self.niScope_SendSoftwareTriggerEdge_cfunc = None
        self.niScope_SetAttributeViBoolean_cfunc = None
        self.niScope_SetAttributeViInt32_cfunc = None
        self.niScope_SetAttributeViInt64_cfunc = None
        self.niScope_SetAttributeViReal64_cfunc = None
        self.niScope_SetAttributeViString_cfunc = None
        self.niScope_SetRuntimeEnvironment_cfunc = None
        self.niScope_UnlockSession_cfunc = None
        self.niScope_close_cfunc = None
        self.niScope_error_message_cfunc = None
        self.niScope_reset_cfunc = None
        self.niScope_self_test_cfunc = None

    def _get_library_function(self, name):
        try:
            function = getattr(self._library, name)
        except AttributeError as e:
            raise errors.DriverTooOldError() from e
        return function

    def niScope_Abort(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_Abort_cfunc is None:
                self.niScope_Abort_cfunc = self._get_library_function('niScope_Abort')
                self.niScope_Abort_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_Abort_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_Abort_cfunc(vi)

    def niScope_AcquisitionStatus(self, vi, acquisition_status):  # noqa: N802
        with self._func_lock:
            if self.niScope_AcquisitionStatus_cfunc is None:
                self.niScope_AcquisitionStatus_cfunc = self._get_library_function('niScope_AcquisitionStatus')
                self.niScope_AcquisitionStatus_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niScope_AcquisitionStatus_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_AcquisitionStatus_cfunc(vi, acquisition_status)

    def niScope_ActualMeasWfmSize(self, vi, array_meas_function, meas_waveform_size):  # noqa: N802
        with self._func_lock:
            if self.niScope_ActualMeasWfmSize_cfunc is None:
                self.niScope_ActualMeasWfmSize_cfunc = self._get_library_function('niScope_ActualMeasWfmSize')
                self.niScope_ActualMeasWfmSize_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niScope_ActualMeasWfmSize_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ActualMeasWfmSize_cfunc(vi, array_meas_function, meas_waveform_size)

    def niScope_ActualNumWfms(self, vi, channel_list, num_wfms):  # noqa: N802
        with self._func_lock:
            if self.niScope_ActualNumWfms_cfunc is None:
                self.niScope_ActualNumWfms_cfunc = self._get_library_function('niScope_ActualNumWfms')
                self.niScope_ActualNumWfms_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niScope_ActualNumWfms_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ActualNumWfms_cfunc(vi, channel_list, num_wfms)

    def niScope_AddWaveformProcessing(self, vi, channel_list, meas_function):  # noqa: N802
        with self._func_lock:
            if self.niScope_AddWaveformProcessing_cfunc is None:
                self.niScope_AddWaveformProcessing_cfunc = self._get_library_function('niScope_AddWaveformProcessing')
                self.niScope_AddWaveformProcessing_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niScope_AddWaveformProcessing_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_AddWaveformProcessing_cfunc(vi, channel_list, meas_function)

    def niScope_AutoSetup(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_AutoSetup_cfunc is None:
                self.niScope_AutoSetup_cfunc = self._get_library_function('niScope_AutoSetup')
                self.niScope_AutoSetup_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_AutoSetup_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_AutoSetup_cfunc(vi)

    def niScope_CalFetchDate(self, vi, which_one, year, month, day):  # noqa: N802
        with self._func_lock:
            if self.niScope_CalFetchDate_cfunc is None:
                self.niScope_CalFetchDate_cfunc = self._get_library_function('niScope_CalFetchDate')
                self.niScope_CalFetchDate_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niScope_CalFetchDate_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_CalFetchDate_cfunc(vi, which_one, year, month, day)

    def niScope_CalFetchTemperature(self, vi, which_one, temperature):  # noqa: N802
        with self._func_lock:
            if self.niScope_CalFetchTemperature_cfunc is None:
                self.niScope_CalFetchTemperature_cfunc = self._get_library_function('niScope_CalFetchTemperature')
                self.niScope_CalFetchTemperature_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niScope_CalFetchTemperature_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_CalFetchTemperature_cfunc(vi, which_one, temperature)

    def niScope_CalSelfCalibrate(self, vi, channel_list, option):  # noqa: N802
        with self._func_lock:
            if self.niScope_CalSelfCalibrate_cfunc is None:
                self.niScope_CalSelfCalibrate_cfunc = self._get_library_function('niScope_CalSelfCalibrate')
                self.niScope_CalSelfCalibrate_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niScope_CalSelfCalibrate_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_CalSelfCalibrate_cfunc(vi, channel_list, option)

    def niScope_ClearWaveformMeasurementStats(self, vi, channel_list, clearable_measurement_function):  # noqa: N802
        with self._func_lock:
            if self.niScope_ClearWaveformMeasurementStats_cfunc is None:
                self.niScope_ClearWaveformMeasurementStats_cfunc = self._get_library_function('niScope_ClearWaveformMeasurementStats')
                self.niScope_ClearWaveformMeasurementStats_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niScope_ClearWaveformMeasurementStats_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ClearWaveformMeasurementStats_cfunc(vi, channel_list, clearable_measurement_function)

    def niScope_ClearWaveformProcessing(self, vi, channel_list):  # noqa: N802
        with self._func_lock:
            if self.niScope_ClearWaveformProcessing_cfunc is None:
                self.niScope_ClearWaveformProcessing_cfunc = self._get_library_function('niScope_ClearWaveformProcessing')
                self.niScope_ClearWaveformProcessing_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_ClearWaveformProcessing_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ClearWaveformProcessing_cfunc(vi, channel_list)

    def niScope_Commit(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_Commit_cfunc is None:
                self.niScope_Commit_cfunc = self._get_library_function('niScope_Commit')
                self.niScope_Commit_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_Commit_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_Commit_cfunc(vi)

    def niScope_ConfigureChanCharacteristics(self, vi, channel_list, input_impedance, max_input_frequency):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureChanCharacteristics_cfunc is None:
                self.niScope_ConfigureChanCharacteristics_cfunc = self._get_library_function('niScope_ConfigureChanCharacteristics')
                self.niScope_ConfigureChanCharacteristics_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureChanCharacteristics_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureChanCharacteristics_cfunc(vi, channel_list, input_impedance, max_input_frequency)

    def niScope_ConfigureEqualizationFilterCoefficients(self, vi, channel_list, number_of_coefficients, coefficients):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureEqualizationFilterCoefficients_cfunc is None:
                self.niScope_ConfigureEqualizationFilterCoefficients_cfunc = self._get_library_function('niScope_ConfigureEqualizationFilterCoefficients')
                self.niScope_ConfigureEqualizationFilterCoefficients_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niScope_ConfigureEqualizationFilterCoefficients_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureEqualizationFilterCoefficients_cfunc(vi, channel_list, number_of_coefficients, coefficients)

    def niScope_ConfigureHorizontalTiming(self, vi, min_sample_rate, min_num_pts, ref_position, num_records, enforce_realtime):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureHorizontalTiming_cfunc is None:
                self.niScope_ConfigureHorizontalTiming_cfunc = self._get_library_function('niScope_ConfigureHorizontalTiming')
                self.niScope_ConfigureHorizontalTiming_cfunc.argtypes = [ViSession, ViReal64, ViInt32, ViReal64, ViInt32, ViBoolean]  # noqa: F405
                self.niScope_ConfigureHorizontalTiming_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureHorizontalTiming_cfunc(vi, min_sample_rate, min_num_pts, ref_position, num_records, enforce_realtime)

    def niScope_ConfigureRefLevels(self, vi, low, mid, high):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureRefLevels_cfunc is None:
                self.niScope_ConfigureRefLevels_cfunc = self._get_library_function('niScope_ConfigureRefLevels')
                self.niScope_ConfigureRefLevels_cfunc.argtypes = [ViSession, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureRefLevels_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureRefLevels_cfunc(vi, low, mid, high)

    def niScope_ConfigureTriggerDigital(self, vi, trigger_source, slope, holdoff, delay):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureTriggerDigital_cfunc is None:
                self.niScope_ConfigureTriggerDigital_cfunc = self._get_library_function('niScope_ConfigureTriggerDigital')
                self.niScope_ConfigureTriggerDigital_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureTriggerDigital_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureTriggerDigital_cfunc(vi, trigger_source, slope, holdoff, delay)

    def niScope_ConfigureTriggerEdge(self, vi, trigger_source, level, slope, trigger_coupling, holdoff, delay):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureTriggerEdge_cfunc is None:
                self.niScope_ConfigureTriggerEdge_cfunc = self._get_library_function('niScope_ConfigureTriggerEdge')
                self.niScope_ConfigureTriggerEdge_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureTriggerEdge_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureTriggerEdge_cfunc(vi, trigger_source, level, slope, trigger_coupling, holdoff, delay)

    def niScope_ConfigureTriggerHysteresis(self, vi, trigger_source, level, hysteresis, slope, trigger_coupling, holdoff, delay):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureTriggerHysteresis_cfunc is None:
                self.niScope_ConfigureTriggerHysteresis_cfunc = self._get_library_function('niScope_ConfigureTriggerHysteresis')
                self.niScope_ConfigureTriggerHysteresis_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64, ViInt32, ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureTriggerHysteresis_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureTriggerHysteresis_cfunc(vi, trigger_source, level, hysteresis, slope, trigger_coupling, holdoff, delay)

    def niScope_ConfigureTriggerImmediate(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureTriggerImmediate_cfunc is None:
                self.niScope_ConfigureTriggerImmediate_cfunc = self._get_library_function('niScope_ConfigureTriggerImmediate')
                self.niScope_ConfigureTriggerImmediate_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_ConfigureTriggerImmediate_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureTriggerImmediate_cfunc(vi)

    def niScope_ConfigureTriggerSoftware(self, vi, holdoff, delay):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureTriggerSoftware_cfunc is None:
                self.niScope_ConfigureTriggerSoftware_cfunc = self._get_library_function('niScope_ConfigureTriggerSoftware')
                self.niScope_ConfigureTriggerSoftware_cfunc.argtypes = [ViSession, ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureTriggerSoftware_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureTriggerSoftware_cfunc(vi, holdoff, delay)

    def niScope_ConfigureTriggerVideo(self, vi, trigger_source, enable_dc_restore, signal_format, event, line_number, polarity, trigger_coupling, holdoff, delay):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureTriggerVideo_cfunc is None:
                self.niScope_ConfigureTriggerVideo_cfunc = self._get_library_function('niScope_ConfigureTriggerVideo')
                self.niScope_ConfigureTriggerVideo_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViBoolean, ViInt32, ViInt32, ViInt32, ViInt32, ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureTriggerVideo_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureTriggerVideo_cfunc(vi, trigger_source, enable_dc_restore, signal_format, event, line_number, polarity, trigger_coupling, holdoff, delay)

    def niScope_ConfigureTriggerWindow(self, vi, trigger_source, low_level, high_level, window_mode, trigger_coupling, holdoff, delay):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureTriggerWindow_cfunc is None:
                self.niScope_ConfigureTriggerWindow_cfunc = self._get_library_function('niScope_ConfigureTriggerWindow')
                self.niScope_ConfigureTriggerWindow_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64, ViInt32, ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureTriggerWindow_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureTriggerWindow_cfunc(vi, trigger_source, low_level, high_level, window_mode, trigger_coupling, holdoff, delay)

    def niScope_ConfigureVertical(self, vi, channel_list, range, offset, coupling, probe_attenuation, enabled):  # noqa: N802
        with self._func_lock:
            if self.niScope_ConfigureVertical_cfunc is None:
                self.niScope_ConfigureVertical_cfunc = self._get_library_function('niScope_ConfigureVertical')
                self.niScope_ConfigureVertical_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64, ViInt32, ViReal64, ViBoolean]  # noqa: F405
                self.niScope_ConfigureVertical_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ConfigureVertical_cfunc(vi, channel_list, range, offset, coupling, probe_attenuation, enabled)

    def niScope_Disable(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_Disable_cfunc is None:
                self.niScope_Disable_cfunc = self._get_library_function('niScope_Disable')
                self.niScope_Disable_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_Disable_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_Disable_cfunc(vi)

    def niScope_ExportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration):  # noqa: N802
        with self._func_lock:
            if self.niScope_ExportAttributeConfigurationBuffer_cfunc is None:
                self.niScope_ExportAttributeConfigurationBuffer_cfunc = self._get_library_function('niScope_ExportAttributeConfigurationBuffer')
                self.niScope_ExportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niScope_ExportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ExportAttributeConfigurationBuffer_cfunc(vi, size_in_bytes, configuration)

    def niScope_ExportAttributeConfigurationFile(self, vi, file_path):  # noqa: N802
        with self._func_lock:
            if self.niScope_ExportAttributeConfigurationFile_cfunc is None:
                self.niScope_ExportAttributeConfigurationFile_cfunc = self._get_library_function('niScope_ExportAttributeConfigurationFile')
                self.niScope_ExportAttributeConfigurationFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_ExportAttributeConfigurationFile_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ExportAttributeConfigurationFile_cfunc(vi, file_path)

    def niScope_Fetch(self, vi, channel_list, timeout, num_samples, waveform, wfm_info):  # noqa: N802
        with self._func_lock:
            if self.niScope_Fetch_cfunc is None:
                self.niScope_Fetch_cfunc = self._get_library_function('niScope_Fetch')
                self.niScope_Fetch_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(waveform_info.struct_niScope_wfmInfo)]  # noqa: F405
                self.niScope_Fetch_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_Fetch_cfunc(vi, channel_list, timeout, num_samples, waveform, wfm_info)

    def niScope_FetchArrayMeasurement(self, vi, channel_list, timeout, array_meas_function, measurement_waveform_size, meas_wfm, wfm_info):  # noqa: N802
        with self._func_lock:
            if self.niScope_FetchArrayMeasurement_cfunc is None:
                self.niScope_FetchArrayMeasurement_cfunc = self._get_library_function('niScope_FetchArrayMeasurement')
                self.niScope_FetchArrayMeasurement_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(waveform_info.struct_niScope_wfmInfo)]  # noqa: F405
                self.niScope_FetchArrayMeasurement_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_FetchArrayMeasurement_cfunc(vi, channel_list, timeout, array_meas_function, measurement_waveform_size, meas_wfm, wfm_info)

    def niScope_FetchBinary16(self, vi, channel_list, timeout, num_samples, waveform, wfm_info):  # noqa: N802
        with self._func_lock:
            if self.niScope_FetchBinary16_cfunc is None:
                self.niScope_FetchBinary16_cfunc = self._get_library_function('niScope_FetchBinary16')
                self.niScope_FetchBinary16_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ctypes.POINTER(ViInt16), ctypes.POINTER(waveform_info.struct_niScope_wfmInfo)]  # noqa: F405
                self.niScope_FetchBinary16_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_FetchBinary16_cfunc(vi, channel_list, timeout, num_samples, waveform, wfm_info)

    def niScope_FetchBinary32(self, vi, channel_list, timeout, num_samples, waveform, wfm_info):  # noqa: N802
        with self._func_lock:
            if self.niScope_FetchBinary32_cfunc is None:
                self.niScope_FetchBinary32_cfunc = self._get_library_function('niScope_FetchBinary32')
                self.niScope_FetchBinary32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(waveform_info.struct_niScope_wfmInfo)]  # noqa: F405
                self.niScope_FetchBinary32_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_FetchBinary32_cfunc(vi, channel_list, timeout, num_samples, waveform, wfm_info)

    def niScope_FetchBinary8(self, vi, channel_list, timeout, num_samples, waveform, wfm_info):  # noqa: N802
        with self._func_lock:
            if self.niScope_FetchBinary8_cfunc is None:
                self.niScope_FetchBinary8_cfunc = self._get_library_function('niScope_FetchBinary8')
                self.niScope_FetchBinary8_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ctypes.POINTER(ViInt8), ctypes.POINTER(waveform_info.struct_niScope_wfmInfo)]  # noqa: F405
                self.niScope_FetchBinary8_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_FetchBinary8_cfunc(vi, channel_list, timeout, num_samples, waveform, wfm_info)

    def niScope_FetchMeasurementStats(self, vi, channel_list, timeout, scalar_meas_function, result, mean, stdev, min, max, num_in_stats):  # noqa: N802
        with self._func_lock:
            if self.niScope_FetchMeasurementStats_cfunc is None:
                self.niScope_FetchMeasurementStats_cfunc = self._get_library_function('niScope_FetchMeasurementStats')
                self.niScope_FetchMeasurementStats_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niScope_FetchMeasurementStats_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_FetchMeasurementStats_cfunc(vi, channel_list, timeout, scalar_meas_function, result, mean, stdev, min, max, num_in_stats)

    def niScope_GetAttributeViBoolean(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_GetAttributeViBoolean_cfunc is None:
                self.niScope_GetAttributeViBoolean_cfunc = self._get_library_function('niScope_GetAttributeViBoolean')
                self.niScope_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niScope_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_GetAttributeViBoolean_cfunc(vi, channel_list, attribute_id, value)

    def niScope_GetAttributeViInt32(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_GetAttributeViInt32_cfunc is None:
                self.niScope_GetAttributeViInt32_cfunc = self._get_library_function('niScope_GetAttributeViInt32')
                self.niScope_GetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niScope_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_GetAttributeViInt32_cfunc(vi, channel_list, attribute_id, value)

    def niScope_GetAttributeViInt64(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_GetAttributeViInt64_cfunc is None:
                self.niScope_GetAttributeViInt64_cfunc = self._get_library_function('niScope_GetAttributeViInt64')
                self.niScope_GetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niScope_GetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_GetAttributeViInt64_cfunc(vi, channel_list, attribute_id, value)

    def niScope_GetAttributeViReal64(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_GetAttributeViReal64_cfunc is None:
                self.niScope_GetAttributeViReal64_cfunc = self._get_library_function('niScope_GetAttributeViReal64')
                self.niScope_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niScope_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_GetAttributeViReal64_cfunc(vi, channel_list, attribute_id, value)

    def niScope_GetAttributeViString(self, vi, channel_list, attribute_id, buf_size, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_GetAttributeViString_cfunc is None:
                self.niScope_GetAttributeViString_cfunc = self._get_library_function('niScope_GetAttributeViString')
                self.niScope_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_GetAttributeViString_cfunc(vi, channel_list, attribute_id, buf_size, value)

    def niScope_GetChannelNameFromString(self, vi, indices, buffer_size, names):  # noqa: N802
        with self._func_lock:
            if self.niScope_GetChannelNameFromString_cfunc is None:
                self.niScope_GetChannelNameFromString_cfunc = self._get_library_function('niScope_GetChannelNameFromString')
                self.niScope_GetChannelNameFromString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_GetChannelNameFromString_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_GetChannelNameFromString_cfunc(vi, indices, buffer_size, names)

    def niScope_GetEqualizationFilterCoefficients(self, vi, channel, number_of_coefficients, coefficients):  # noqa: N802
        with self._func_lock:
            if self.niScope_GetEqualizationFilterCoefficients_cfunc is None:
                self.niScope_GetEqualizationFilterCoefficients_cfunc = self._get_library_function('niScope_GetEqualizationFilterCoefficients')
                self.niScope_GetEqualizationFilterCoefficients_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niScope_GetEqualizationFilterCoefficients_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_GetEqualizationFilterCoefficients_cfunc(vi, channel, number_of_coefficients, coefficients)

    def niScope_GetError(self, vi, error_code, buffer_size, description):  # noqa: N802
        with self._func_lock:
            if self.niScope_GetError_cfunc is None:
                self.niScope_GetError_cfunc = self._get_library_function('niScope_GetError')
                self.niScope_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_GetError_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_GetError_cfunc(vi, error_code, buffer_size, description)

    def niScope_ImportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration):  # noqa: N802
        with self._func_lock:
            if self.niScope_ImportAttributeConfigurationBuffer_cfunc is None:
                self.niScope_ImportAttributeConfigurationBuffer_cfunc = self._get_library_function('niScope_ImportAttributeConfigurationBuffer')
                self.niScope_ImportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niScope_ImportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ImportAttributeConfigurationBuffer_cfunc(vi, size_in_bytes, configuration)

    def niScope_ImportAttributeConfigurationFile(self, vi, file_path):  # noqa: N802
        with self._func_lock:
            if self.niScope_ImportAttributeConfigurationFile_cfunc is None:
                self.niScope_ImportAttributeConfigurationFile_cfunc = self._get_library_function('niScope_ImportAttributeConfigurationFile')
                self.niScope_ImportAttributeConfigurationFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_ImportAttributeConfigurationFile_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ImportAttributeConfigurationFile_cfunc(vi, file_path)

    def niScope_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_InitWithOptions_cfunc is None:
                self.niScope_InitWithOptions_cfunc = self._get_library_function('niScope_InitWithOptions')
                self.niScope_InitWithOptions_cfunc.argtypes = [ctypes.POINTER(ViChar), ViBoolean, ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niScope_InitWithOptions_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_InitWithOptions_cfunc(resource_name, id_query, reset_device, option_string, vi)

    def niScope_InitiateAcquisition(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_InitiateAcquisition_cfunc is None:
                self.niScope_InitiateAcquisition_cfunc = self._get_library_function('niScope_InitiateAcquisition')
                self.niScope_InitiateAcquisition_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_InitiateAcquisition_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_InitiateAcquisition_cfunc(vi)

    def niScope_LockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niScope_LockSession_cfunc is None:
                self.niScope_LockSession_cfunc = self._get_library_function('niScope_LockSession')
                self.niScope_LockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niScope_LockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_LockSession_cfunc(vi, caller_has_lock)

    def niScope_ProbeCompensationSignalStart(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_ProbeCompensationSignalStart_cfunc is None:
                self.niScope_ProbeCompensationSignalStart_cfunc = self._get_library_function('niScope_ProbeCompensationSignalStart')
                self.niScope_ProbeCompensationSignalStart_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_ProbeCompensationSignalStart_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ProbeCompensationSignalStart_cfunc(vi)

    def niScope_ProbeCompensationSignalStop(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_ProbeCompensationSignalStop_cfunc is None:
                self.niScope_ProbeCompensationSignalStop_cfunc = self._get_library_function('niScope_ProbeCompensationSignalStop')
                self.niScope_ProbeCompensationSignalStop_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_ProbeCompensationSignalStop_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ProbeCompensationSignalStop_cfunc(vi)

    def niScope_Read(self, vi, channel_list, timeout, num_samples, waveform, wfm_info):  # noqa: N802
        with self._func_lock:
            if self.niScope_Read_cfunc is None:
                self.niScope_Read_cfunc = self._get_library_function('niScope_Read')
                self.niScope_Read_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(waveform_info.struct_niScope_wfmInfo)]  # noqa: F405
                self.niScope_Read_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_Read_cfunc(vi, channel_list, timeout, num_samples, waveform, wfm_info)

    def niScope_ResetDevice(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_ResetDevice_cfunc is None:
                self.niScope_ResetDevice_cfunc = self._get_library_function('niScope_ResetDevice')
                self.niScope_ResetDevice_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_ResetDevice_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ResetDevice_cfunc(vi)

    def niScope_ResetWithDefaults(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_ResetWithDefaults_cfunc is None:
                self.niScope_ResetWithDefaults_cfunc = self._get_library_function('niScope_ResetWithDefaults')
                self.niScope_ResetWithDefaults_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_ResetWithDefaults_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_ResetWithDefaults_cfunc(vi)

    def niScope_SendSoftwareTriggerEdge(self, vi, which_trigger):  # noqa: N802
        with self._func_lock:
            if self.niScope_SendSoftwareTriggerEdge_cfunc is None:
                self.niScope_SendSoftwareTriggerEdge_cfunc = self._get_library_function('niScope_SendSoftwareTriggerEdge')
                self.niScope_SendSoftwareTriggerEdge_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niScope_SendSoftwareTriggerEdge_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_SendSoftwareTriggerEdge_cfunc(vi, which_trigger)

    def niScope_SetAttributeViBoolean(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_SetAttributeViBoolean_cfunc is None:
                self.niScope_SetAttributeViBoolean_cfunc = self._get_library_function('niScope_SetAttributeViBoolean')
                self.niScope_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niScope_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_SetAttributeViBoolean_cfunc(vi, channel_list, attribute_id, value)

    def niScope_SetAttributeViInt32(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_SetAttributeViInt32_cfunc is None:
                self.niScope_SetAttributeViInt32_cfunc = self._get_library_function('niScope_SetAttributeViInt32')
                self.niScope_SetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niScope_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_SetAttributeViInt32_cfunc(vi, channel_list, attribute_id, value)

    def niScope_SetAttributeViInt64(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_SetAttributeViInt64_cfunc is None:
                self.niScope_SetAttributeViInt64_cfunc = self._get_library_function('niScope_SetAttributeViInt64')
                self.niScope_SetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt64]  # noqa: F405
                self.niScope_SetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_SetAttributeViInt64_cfunc(vi, channel_list, attribute_id, value)

    def niScope_SetAttributeViReal64(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_SetAttributeViReal64_cfunc is None:
                self.niScope_SetAttributeViReal64_cfunc = self._get_library_function('niScope_SetAttributeViReal64')
                self.niScope_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niScope_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_SetAttributeViReal64_cfunc(vi, channel_list, attribute_id, value)

    def niScope_SetAttributeViString(self, vi, channel_list, attribute_id, value):  # noqa: N802
        with self._func_lock:
            if self.niScope_SetAttributeViString_cfunc is None:
                self.niScope_SetAttributeViString_cfunc = self._get_library_function('niScope_SetAttributeViString')
                self.niScope_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_SetAttributeViString_cfunc(vi, channel_list, attribute_id, value)

    def niScope_SetRuntimeEnvironment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        with self._func_lock:
            if self.niScope_SetRuntimeEnvironment_cfunc is None:
                self.niScope_SetRuntimeEnvironment_cfunc = self._get_library_function('niScope_SetRuntimeEnvironment')
                self.niScope_SetRuntimeEnvironment_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_SetRuntimeEnvironment_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_SetRuntimeEnvironment_cfunc(environment, environment_version, reserved1, reserved2)

    def niScope_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niScope_UnlockSession_cfunc is None:
                self.niScope_UnlockSession_cfunc = self._get_library_function('niScope_UnlockSession')
                self.niScope_UnlockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niScope_UnlockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_UnlockSession_cfunc(vi, caller_has_lock)

    def niScope_close(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_close_cfunc is None:
                self.niScope_close_cfunc = self._get_library_function('niScope_close')
                self.niScope_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_close_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_close_cfunc(vi)

    def niScope_error_message(self, vi, error_code, error_message):  # noqa: N802
        with self._func_lock:
            if self.niScope_error_message_cfunc is None:
                self.niScope_error_message_cfunc = self._get_library_function('niScope_error_message')
                self.niScope_error_message_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_error_message_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_error_message_cfunc(vi, error_code, error_message)

    def niScope_reset(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niScope_reset_cfunc is None:
                self.niScope_reset_cfunc = self._get_library_function('niScope_reset')
                self.niScope_reset_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_reset_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_reset_cfunc(vi)

    def niScope_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        with self._func_lock:
            if self.niScope_self_test_cfunc is None:
                self.niScope_self_test_cfunc = self._get_library_function('niScope_self_test')
                self.niScope_self_test_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_self_test_cfunc.restype = ViStatus  # noqa: F405
        return self.niScope_self_test_cfunc(vi, self_test_result, self_test_message)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/niscope/niscope/_library_interpreter.py sha256=df2fceb0fc6d61b3a05020bc3897390ad872758f7b0d7729084190cd1368619f bytes=49328 -->
## FILE: generated/niscope/niscope/_library_interpreter.py

- repository: `ni/nimi-python`
- source_path: `generated/niscope/niscope/_library_interpreter.py`
- sha256: `df2fceb0fc6d61b3a05020bc3897390ad872758f7b0d7729084190cd1368619f`
- bytes: 49328

````python
# -*- coding: utf-8 -*-
# This file was generated

import array
import ctypes
import hightime  # noqa: F401
import platform

import niscope._library_singleton as _library_singleton
import niscope._visatype as _visatype
import niscope.enums as enums  # noqa: F401
import niscope.errors as errors

import niscope.waveform_info as waveform_info  # noqa: F401

import niscope.measurement_stats as measurement_stats  # noqa: F401


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
        error_code = self._library.niScope_Abort(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def acquisition_status(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        acquisition_status_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niScope_AcquisitionStatus(vi_ctype, None if acquisition_status_ctype is None else (ctypes.pointer(acquisition_status_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return enums.AcquisitionStatus(acquisition_status_ctype.value)

    def actual_meas_wfm_size(self, array_meas_function):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        array_meas_function_ctype = _visatype.ViInt32(array_meas_function.value)  # case S130
        meas_waveform_size_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niScope_ActualMeasWfmSize(vi_ctype, array_meas_function_ctype, None if meas_waveform_size_ctype is None else (ctypes.pointer(meas_waveform_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(meas_waveform_size_ctype.value)

    def actual_num_wfms(self, channel_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        num_wfms_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niScope_ActualNumWfms(vi_ctype, channel_list_ctype, None if num_wfms_ctype is None else (ctypes.pointer(num_wfms_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(num_wfms_ctype.value)

    def add_waveform_processing(self, channel_list, meas_function):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        meas_function_ctype = _visatype.ViInt32(meas_function.value)  # case S130
        error_code = self._library.niScope_AddWaveformProcessing(vi_ctype, channel_list_ctype, meas_function_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def auto_setup(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niScope_AutoSetup(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def cal_fetch_date(self, which_one):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        which_one_ctype = _visatype.ViInt32(which_one.value)  # case S130
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niScope_CalFetchDate(vi_ctype, which_one_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value)

    def cal_fetch_temperature(self, which_one):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        which_one_ctype = _visatype.ViInt32(which_one)  # case S150
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niScope_CalFetchTemperature(vi_ctype, which_one_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def self_cal(self, channel_list, option):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        option_ctype = _visatype.ViInt32(option.value)  # case S130
        error_code = self._library.niScope_CalSelfCalibrate(vi_ctype, channel_list_ctype, option_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_waveform_measurement_stats(self, channel_list, clearable_measurement_function):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        clearable_measurement_function_ctype = _visatype.ViInt32(clearable_measurement_function.value)  # case S130
        error_code = self._library.niScope_ClearWaveformMeasurementStats(vi_ctype, channel_list_ctype, clearable_measurement_function_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_waveform_processing(self, channel_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        error_code = self._library.niScope_ClearWaveformProcessing(vi_ctype, channel_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def commit(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niScope_Commit(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_chan_characteristics(self, channel_list, input_impedance, max_input_frequency):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        input_impedance_ctype = _visatype.ViReal64(input_impedance)  # case S150
        max_input_frequency_ctype = _visatype.ViReal64(max_input_frequency)  # case S150
        error_code = self._library.niScope_ConfigureChanCharacteristics(vi_ctype, channel_list_ctype, input_impedance_ctype, max_input_frequency_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_equalization_filter_coefficients(self, channel_list, coefficients):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        number_of_coefficients_ctype = _visatype.ViInt32(0 if coefficients is None else len(coefficients))  # case S160
        coefficients_ctype = _get_ctypes_pointer_for_buffer(value=coefficients, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.niScope_ConfigureEqualizationFilterCoefficients(vi_ctype, channel_list_ctype, number_of_coefficients_ctype, coefficients_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_horizontal_timing(self, min_sample_rate, min_num_pts, ref_position, num_records, enforce_realtime):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        min_sample_rate_ctype = _visatype.ViReal64(min_sample_rate)  # case S150
        min_num_pts_ctype = _visatype.ViInt32(min_num_pts)  # case S150
        ref_position_ctype = _visatype.ViReal64(ref_position)  # case S150
        num_records_ctype = _visatype.ViInt32(num_records)  # case S150
        enforce_realtime_ctype = _visatype.ViBoolean(enforce_realtime)  # case S150
        error_code = self._library.niScope_ConfigureHorizontalTiming(vi_ctype, min_sample_rate_ctype, min_num_pts_ctype, ref_position_ctype, num_records_ctype, enforce_realtime_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_ref_levels(self, low, mid, high):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        low_ctype = _visatype.ViReal64(low)  # case S150
        mid_ctype = _visatype.ViReal64(mid)  # case S150
        high_ctype = _visatype.ViReal64(high)  # case S150
        error_code = self._library.niScope_ConfigureRefLevels(vi_ctype, low_ctype, mid_ctype, high_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_digital(self, trigger_source, slope, holdoff, delay):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_source_ctype = ctypes.create_string_buffer(trigger_source.encode(self._encoding))  # case C020
        slope_ctype = _visatype.ViInt32(slope.value)  # case S130
        holdoff_ctype = _visatype.ViReal64(holdoff)  # case S150
        delay_ctype = _visatype.ViReal64(delay)  # case S150
        error_code = self._library.niScope_ConfigureTriggerDigital(vi_ctype, trigger_source_ctype, slope_ctype, holdoff_ctype, delay_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_edge(self, trigger_source, level, slope, trigger_coupling, holdoff, delay):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_source_ctype = ctypes.create_string_buffer(trigger_source.encode(self._encoding))  # case C020
        level_ctype = _visatype.ViReal64(level)  # case S150
        slope_ctype = _visatype.ViInt32(slope.value)  # case S130
        trigger_coupling_ctype = _visatype.ViInt32(trigger_coupling.value)  # case S130
        holdoff_ctype = _visatype.ViReal64(holdoff)  # case S150
        delay_ctype = _visatype.ViReal64(delay)  # case S150
        error_code = self._library.niScope_ConfigureTriggerEdge(vi_ctype, trigger_source_ctype, level_ctype, slope_ctype, trigger_coupling_ctype, holdoff_ctype, delay_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_hysteresis(self, trigger_source, level, hysteresis, slope, trigger_coupling, holdoff, delay):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_source_ctype = ctypes.create_string_buffer(trigger_source.encode(self._encoding))  # case C020
        level_ctype = _visatype.ViReal64(level)  # case S150
        hysteresis_ctype = _visatype.ViReal64(hysteresis)  # case S150
        slope_ctype = _visatype.ViInt32(slope.value)  # case S130
        trigger_coupling_ctype = _visatype.ViInt32(trigger_coupling.value)  # case S130
        holdoff_ctype = _visatype.ViReal64(holdoff)  # case S150
        delay_ctype = _visatype.ViReal64(delay)  # case S150
        error_code = self._library.niScope_ConfigureTriggerHysteresis(vi_ctype, trigger_source_ctype, level_ctype, hysteresis_ctype, slope_ctype, trigger_coupling_ctype, holdoff_ctype, delay_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_immediate(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niScope_ConfigureTriggerImmediate(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_software(self, holdoff, delay):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        holdoff_ctype = _visatype.ViReal64(holdoff)  # case S150
        delay_ctype = _visatype.ViReal64(delay)  # case S150
        error_code = self._library.niScope_ConfigureTriggerSoftware(vi_ctype, holdoff_ctype, delay_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_video(self, trigger_source, enable_dc_restore, signal_format, event, line_number, polarity, trigger_coupling, holdoff, delay):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_source_ctype = ctypes.create_string_buffer(trigger_source.encode(self._encoding))  # case C020
        enable_dc_restore_ctype = _visatype.ViBoolean(enable_dc_restore)  # case S150
        signal_format_ctype = _visatype.ViInt32(signal_format.value)  # case S130
        event_ctype = _visatype.ViInt32(event.value)  # case S130
        line_number_ctype = _visatype.ViInt32(line_number)  # case S150
        polarity_ctype = _visatype.ViInt32(polarity.value)  # case S130
        trigger_coupling_ctype = _visatype.ViInt32(trigger_coupling.value)  # case S130
        holdoff_ctype = _visatype.ViReal64(holdoff)  # case S150
        delay_ctype = _visatype.ViReal64(delay)  # case S150
        error_code = self._library.niScope_ConfigureTriggerVideo(vi_ctype, trigger_source_ctype, enable_dc_restore_ctype, signal_format_ctype, event_ctype, line_number_ctype, polarity_ctype, trigger_coupling_ctype, holdoff_ctype, delay_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_window(self, trigger_source, low_level, high_level, window_mode, trigger_coupling, holdoff, delay):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_source_ctype = ctypes.create_string_buffer(trigger_source.encode(self._encoding))  # case C020
        low_level_ctype = _visatype.ViReal64(low_level)  # case S150
        high_level_ctype = _visatype.ViReal64(high_level)  # case S150
        window_mode_ctype = _visatype.ViInt32(window_mode.value)  # case S130
        trigger_coupling_ctype = _visatype.ViInt32(trigger_coupling.value)  # case S130
        holdoff_ctype = _visatype.ViReal64(holdoff)  # case S150
        delay_ctype = _visatype.ViReal64(delay)  # case S150
        error_code = self._library.niScope_ConfigureTriggerWindow(vi_ctype, trigger_source_ctype, low_level_ctype, high_level_ctype, window_mode_ctype, trigger_coupling_ctype, holdoff_ctype, delay_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_vertical(self, channel_list, range, offset, coupling, probe_attenuation, enabled):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        range_ctype = _visatype.ViReal64(range)  # case S150
        offset_ctype = _visatype.ViReal64(offset)  # case S150
        coupling_ctype = _visatype.ViInt32(coupling.value)  # case S130
        probe_attenuation_ctype = _visatype.ViReal64(probe_attenuation)  # case S150
        enabled_ctype = _visatype.ViBoolean(enabled)  # case S150
        error_code = self._library.niScope_ConfigureVertical(vi_ctype, channel_list_ctype, range_ctype, offset_ctype, coupling_ctype, probe_attenuation_ctype, enabled_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niScope_Disable(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def export_attribute_configuration_buffer(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        size_in_bytes_ctype = _visatype.ViInt32()  # case S170
        configuration_ctype = None  # case B580
        error_code = self._library.niScope_ExportAttributeConfigurationBuffer(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        size_in_bytes_ctype = _visatype.ViInt32(error_code)  # case S180
        configuration_size = size_in_bytes_ctype.value  # case B590
        configuration_array = array.array("b", [0]) * configuration_size  # case B590
        configuration_ctype = _get_ctypes_pointer_for_buffer(value=configuration_array, library_type=_visatype.ViInt8)  # case B590
        error_code = self._library.niScope_ExportAttributeConfigurationBuffer(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return configuration_array

    def export_attribute_configuration_file(self, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niScope_ExportAttributeConfigurationFile(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def fetch(self, channel_list, timeout, num_samples):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        num_samples_ctype = _visatype.ViInt32(num_samples)  # case S150
        waveform_size = (num_samples * self.actual_num_wfms(channel_list))  # case B560
        waveform_array = array.array("d", [0]) * waveform_size  # case B560
        waveform_ctype = _get_ctypes_pointer_for_buffer(value=waveform_array, library_type=_visatype.ViReal64)  # case B560
        wfm_info_size = self.actual_num_wfms(channel_list)  # case B560
        wfm_info_ctype = _get_ctypes_pointer_for_buffer(library_type=waveform_info.struct_niScope_wfmInfo, size=wfm_info_size)  # case B560
        error_code = self._library.niScope_Fetch(vi_ctype, channel_list_ctype, timeout_ctype, num_samples_ctype, waveform_ctype, wfm_info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return waveform_array, [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self.actual_num_wfms(channel_list))]

    def fetch_into_numpy(self, channel_list, num_samples, waveform, timeout):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        num_samples_ctype = _visatype.ViInt32(num_samples)  # case S150
        waveform_ctype = _get_ctypes_pointer_for_buffer(value=waveform)  # case B510
        wfm_info_size = self.actual_num_wfms(channel_list)  # case B560
        wfm_info_ctype = _get_ctypes_pointer_for_buffer(library_type=waveform_info.struct_niScope_wfmInfo, size=wfm_info_size)  # case B560
        error_code = self._library.niScope_Fetch(vi_ctype, channel_list_ctype, timeout_ctype, num_samples_ctype, waveform_ctype, wfm_info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self.actual_num_wfms(channel_list))]

    def fetch_array_measurement(self, channel_list, timeout, array_meas_function, measurement_waveform_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        array_meas_function_ctype = _visatype.ViInt32(array_meas_function.value)  # case S130
        measurement_waveform_size_ctype = _visatype.ViInt32(measurement_waveform_size)  # case S150
        meas_wfm_size = (measurement_waveform_size * self.actual_num_wfms(channel_list))  # case B560
        meas_wfm_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=meas_wfm_size)  # case B560
        wfm_info_size = self.actual_num_wfms(channel_list)  # case B560
        wfm_info_ctype = _get_ctypes_pointer_for_buffer(library_type=waveform_info.struct_niScope_wfmInfo, size=wfm_info_size)  # case B560
        error_code = self._library.niScope_FetchArrayMeasurement(vi_ctype, channel_list_ctype, timeout_ctype, array_meas_function_ctype, measurement_waveform_size_ctype, meas_wfm_ctype, wfm_info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(meas_wfm_ctype[i]) for i in range((measurement_waveform_size * self.actual_num_wfms(channel_list)))], [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self.actual_num_wfms(channel_list))]

    def fetch_binary16_into_numpy(self, channel_list, num_samples, waveform, timeout):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        num_samples_ctype = _visatype.ViInt32(num_samples)  # case S150
        waveform_ctype = _get_ctypes_pointer_for_buffer(value=waveform)  # case B510
        wfm_info_size = self.actual_num_wfms(channel_list)  # case B560
        wfm_info_ctype = _get_ctypes_pointer_for_buffer(library_type=waveform_info.struct_niScope_wfmInfo, size=wfm_info_size)  # case B560
        error_code = self._library.niScope_FetchBinary16(vi_ctype, channel_list_ctype, timeout_ctype, num_samples_ctype, waveform_ctype, wfm_info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self.actual_num_wfms(channel_list))]

    def fetch_binary32_into_numpy(self, channel_list, num_samples, waveform, timeout):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        num_samples_ctype = _visatype.ViInt32(num_samples)  # case S150
        waveform_ctype = _get_ctypes_pointer_for_buffer(value=waveform)  # case B510
        wfm_info_size = self.actual_num_wfms(channel_list)  # case B560
        wfm_info_ctype = _get_ctypes_pointer_for_buffer(library_type=waveform_info.struct_niScope_wfmInfo, size=wfm_info_size)  # case B560
        error_code = self._library.niScope_FetchBinary32(vi_ctype, channel_list_ctype, timeout_ctype, num_samples_ctype, waveform_ctype, wfm_info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self.actual_num_wfms(channel_list))]

    def fetch_binary8_into_numpy(self, channel_list, num_samples, waveform, timeout):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        num_samples_ctype = _visatype.ViInt32(num_samples)  # case S150
        waveform_ctype = _get_ctypes_pointer_for_buffer(value=waveform)  # case B510
        wfm_info_size = self.actual_num_wfms(channel_list)  # case B560
        wfm_info_ctype = _get_ctypes_pointer_for_buffer(library_type=waveform_info.struct_niScope_wfmInfo, size=wfm_info_size)  # case B560
        error_code = self._library.niScope_FetchBinary8(vi_ctype, channel_list_ctype, timeout_ctype, num_samples_ctype, waveform_ctype, wfm_info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self.actual_num_wfms(channel_list))]

    def fetch_measurement_stats(self, channel_list, timeout, scalar_meas_function):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        scalar_meas_function_ctype = _visatype.ViInt32(scalar_meas_function.value)  # case S130
        result_size = self.actual_num_wfms(channel_list)  # case B560
        result_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=result_size)  # case B560
        mean_size = self.actual_num_wfms(channel_list)  # case B560
        mean_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=mean_size)  # case B560
        stdev_size = self.actual_num_wfms(channel_list)  # case B560
        stdev_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=stdev_size)  # case B560
        min_size = self.actual_num_wfms(channel_list)  # case B560
        min_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=min_size)  # case B560
        max_size = self.actual_num_wfms(channel_list)  # case B560
        max_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=max_size)  # case B560
        num_in_stats_size = self.actual_num_wfms(channel_list)  # case B560
        num_in_stats_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=num_in_stats_size)  # case B560
        error_code = self._library.niScope_FetchMeasurementStats(vi_ctype, channel_list_ctype, timeout_ctype, scalar_meas_function_ctype, result_ctype, mean_ctype, stdev_ctype, min_ctype, max_ctype, num_in_stats_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(result_ctype[i]) for i in range(self.actual_num_wfms(channel_list))], [float(mean_ctype[i]) for i in range(self.actual_num_wfms(channel_list))], [float(stdev_ctype[i]) for i in range(self.actual_num_wfms(channel_list))], [float(min_ctype[i]) for i in range(self.actual_num_wfms(channel_list))], [float(max_ctype[i]) for i in range(self.actual_num_wfms(channel_list))], [int(num_in_stats_ctype[i]) for i in range(self.actual_num_wfms(channel_list))]

    def get_attribute_vi_boolean(self, channel_list, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niScope_GetAttributeViBoolean(vi_ctype, channel_list_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(value_ctype.value)

    def get_attribute_vi_int32(self, channel_list, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niScope_GetAttributeViInt32(vi_ctype, channel_list_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def get_attribute_vi_int64(self, channel_list, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niScope_GetAttributeViInt64(vi_ctype, channel_list_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def get_attribute_vi_real64(self, channel_list, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niScope_GetAttributeViReal64(vi_ctype, channel_list_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(value_ctype.value)

    def get_attribute_vi_string(self, channel_list, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        buf_size_ctype = _visatype.ViInt32()  # case S170
        value_ctype = None  # case C050
        error_code = self._library.niScope_GetAttributeViString(vi_ctype, channel_list_ctype, attribute_id_ctype, buf_size_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buf_size_ctype = _visatype.ViInt32(error_code)  # case S180
        value_ctype = (_visatype.ViChar * buf_size_ctype.value)()  # case C060
        error_code = self._library.niScope_GetAttributeViString(vi_ctype, channel_list_ctype, attribute_id_ctype, buf_size_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return value_ctype.value.decode(self._encoding)

    def get_channel_names(self, indices):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        indices_ctype = ctypes.create_string_buffer(indices.encode(self._encoding))  # case C020
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        names_ctype = None  # case C050
        error_code = self._library.niScope_GetChannelNameFromString(vi_ctype, indices_ctype, buffer_size_ctype, names_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        names_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niScope_GetChannelNameFromString(vi_ctype, indices_ctype, buffer_size_ctype, names_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return names_ctype.value.decode(self._encoding)

    def get_equalization_filter_coefficients(self, channel, number_of_coefficients):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_ctype = ctypes.create_string_buffer(channel.encode(self._encoding))  # case C010
        number_of_coefficients_ctype = _visatype.ViInt32(number_of_coefficients)  # case S210
        coefficients_size = number_of_coefficients  # case B600
        coefficients_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=coefficients_size)  # case B600
        error_code = self._library.niScope_GetEqualizationFilterCoefficients(vi_ctype, channel_ctype, number_of_coefficients_ctype, coefficients_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(coefficients_ctype[i]) for i in range(number_of_coefficients_ctype.value)]

    def get_error(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus()  # case S220
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        description_ctype = None  # case C050
        error_code = self._library.niScope_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        description_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niScope_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), description_ctype.value.decode(self._encoding)

    def import_attribute_configuration_buffer(self, configuration):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        size_in_bytes_ctype = _visatype.ViInt32(0 if configuration is None else len(configuration))  # case S160
        configuration_ctype = _get_ctypes_pointer_for_buffer(value=configuration, library_type=_visatype.ViInt8)  # case B550
        error_code = self._library.niScope_ImportAttributeConfigurationBuffer(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def import_attribute_configuration_file(self, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niScope_ImportAttributeConfigurationFile(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def init_with_options(self, resource_name, id_query, reset_device, option_string):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        id_query_ctype = _visatype.ViBoolean(id_query)  # case S150
        reset_device_ctype = _visatype.ViBoolean(reset_device)  # case S150
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case C020
        vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niScope_InitWithOptions(resource_name_ctype, id_query_ctype, reset_device_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        self._close_on_exit = True
        return int(vi_ctype.value)

    def initiate_acquisition(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niScope_InitiateAcquisition(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def lock(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niScope_LockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def probe_compensation_signal_start(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niScope_ProbeCompensationSignalStart(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def probe_compensation_signal_stop(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niScope_ProbeCompensationSignalStop(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def read(self, channel_list, timeout, num_samples):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        num_samples_ctype = _visatype.ViInt32(num_samples)  # case S150
        waveform_size = (num_samples * self.actual_num_wfms(channel_list))  # case B560
        waveform_array = array.array("d", [0]) * waveform_size  # case B560
        waveform_ctype = _get_ctypes_pointer_for_buffer(value=waveform_array, library_type=_visatype.ViReal64)  # case B560
        wfm_info_size = self.actual_num_wfms(channel_list)  # case B560
        wfm_info_ctype = _get_ctypes_pointer_for_buffer(library_type=waveform_info.struct_niScope_wfmInfo, size=wfm_info_size)  # case B560
        error_code = self._library.niScope_Read(vi_ctype, channel_list_ctype, timeout_ctype, num_samples_ctype, waveform_ctype, wfm_info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return waveform_array, [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self.actual_num_wfms(channel_list))]

    def reset_device(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niScope_ResetDevice(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_with_defaults(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niScope_ResetWithDefaults(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def send_software_trigger_edge(self, which_trigger):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        which_trigger_ctype = _visatype.ViInt32(which_trigger.value)  # case S130
        error_code = self._library.niScope_SendSoftwareTriggerEdge(vi_ctype, which_trigger_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_boolean(self, channel_list, attribute_id, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViBoolean(value)  # case S150
        error_code = self._library.niScope_SetAttributeViBoolean(vi_ctype, channel_list_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_int32(self, channel_list, attribute_id, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViInt32(value)  # case S150
        error_code = self._library.niScope_SetAttributeViInt32(vi_ctype, channel_list_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_int64(self, channel_list, attribute_id, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViInt64(value)  # case S150
        error_code = self._library.niScope_SetAttributeViInt64(vi_ctype, channel_list_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_real64(self, channel_list, attribute_id, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViReal64(value)  # case S150
        error_code = self._library.niScope_SetAttributeViReal64(vi_ctype, channel_list_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_string(self, channel_list, attribute_id, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = ctypes.create_string_buffer(value.encode(self._encoding))  # case C020
        error_code = self._library.niScope_SetAttributeViString(vi_ctype, channel_list_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_runtime_environment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        environment_ctype = ctypes.create_string_buffer(environment.encode(self._encoding))  # case C020
        environment_version_ctype = ctypes.create_string_buffer(environment_version.encode(self._encoding))  # case C020
        reserved1_ctype = ctypes.create_string_buffer(reserved1.encode(self._encoding))  # case C020
        reserved2_ctype = ctypes.create_string_buffer(reserved2.encode(self._encoding))  # case C020
        error_code = self._library.niScope_SetRuntimeEnvironment(environment_ctype, environment_version_ctype, reserved1_ctype, reserved2_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niScope_UnlockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def close(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niScope_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def error_message(self, error_code):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niScope_error_message(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)

    def reset(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niScope_reset(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_test(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        self_test_result_ctype = _visatype.ViInt16()  # case S220
        self_test_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niScope_self_test(vi_ctype, None if self_test_result_ctype is None else (ctypes.pointer(self_test_result_ctype)), self_test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(self._encoding)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/niscope/niscope/_library_singleton.py sha256=4038f4f552cdb9624066fba6d51ce4bc2355a34a2fa64b7dbe4b44b9ab9e922c bytes=1699 -->
## FILE: generated/niscope/niscope/_library_singleton.py

- repository: `ni/nimi-python`
- source_path: `generated/niscope/niscope/_library_singleton.py`
- sha256: `4038f4f552cdb9624066fba6d51ce4bc2355a34a2fa64b7dbe4b44b9ab9e922c`
- bytes: 1699

````python
# -*- coding: utf-8 -*-
# This file was generated

import platform

import ctypes
import ctypes.util
import niscope._library as _library
import niscope.errors as errors
import threading


_instance = None
_instance_lock = threading.Lock()
_library_info = {'Linux': {'64bit': {'name': 'niscope', 'type': 'cdll'}},
                 'Windows': {'32bit': {'name': 'niScope_32.dll', 'type': 'windll'},
                             '64bit': {'name': 'niScope_64.dll', 'type': 'cdll'}}}


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

    Returns the library.Library singleton for niscope.
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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/niscope/niscope/_visatype.py sha256=ac436ae1613f5e807cd16d2df951c7a502f37996234e4d324c5412b3633e1c92 bytes=662 -->
## FILE: generated/niscope/niscope/_visatype.py

- repository: `ni/nimi-python`
- source_path: `generated/niscope/niscope/_visatype.py`
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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/niscope/niscope/enums.py sha256=0c0d6fce8b1652ca2f6f49369b835d92eea5913882f0012155fcf850d97d37d2 bytes=18294 -->
## FILE: generated/niscope/niscope/enums.py

- repository: `ni/nimi-python`
- source_path: `generated/niscope/niscope/enums.py`
- sha256: `0c0d6fce8b1652ca2f6f49369b835d92eea5913882f0012155fcf850d97d37d2`
- bytes: 18294

````python
# -*- coding: utf-8 -*-
# This file was generated

from enum import Enum


class AcquisitionStatus(Enum):
    COMPLETE = 1
    IN_PROGRESS = 0
    STATUS_UNKNOWN = -1


class AcquisitionType(Enum):
    NORMAL = 0
    r'''
    Sets the digitizer to normal resolution mode. The digitizer can use real-time sampling or equivalent-time sampling.
    '''
    FLEXRES = 1001
    r'''
    Sets the digitizer to flexible resolution mode if supported.  The digitizer uses different hardware configurations to change the resolution depending on the sampling rate used.
    '''
    DDC = 1002
    r'''
    Sets the digitizer to DDC mode on the NI 5620/5621.
    '''


class ArrayMeasurement(Enum):
    NO_MEASUREMENT = 4000
    r'''
    None
    '''
    LAST_ACQ_HISTOGRAM = 4001
    r'''
    Last Acquisition Histogram
    '''
    FFT_PHASE_SPECTRUM = 4002
    r'''
    FFT Phase Spectrum
    '''
    FFT_AMP_SPECTRUM_VOLTS_RMS = 4003
    r'''
    FFT Amp. Spectrum (Volts RMS)
    '''
    MULTI_ACQ_VOLTAGE_HISTOGRAM = 4004
    r'''
    Multi Acquisition Voltage Histogram
    '''
    MULTI_ACQ_TIME_HISTOGRAM = 4005
    r'''
    Multi Acquisition Time Histogram
    '''
    ARRAY_INTEGRAL = 4006
    r'''
    Array Integral
    '''
    DERIVATIVE = 4007
    r'''
    Derivative
    '''
    INVERSE = 4008
    r'''
    Inverse
    '''
    HANNING_WINDOW = 4009
    r'''
    Hanning Window
    '''
    FLAT_TOP_WINDOW = 4010
    r'''
    Flat Top Window
    '''
    POLYNOMIAL_INTERPOLATION = 4011
    r'''
    Polynomial Interpolation
    '''
    MULTIPLY_CHANNELS = 4012
    r'''
    Multiply Channels
    '''
    ADD_CHANNELS = 4013
    r'''
    Add Channels
    '''
    SUBTRACT_CHANNELS = 4014
    r'''
    Subtract Channels
    '''
    DIVIDE_CHANNELS = 4015
    r'''
    Divide Channels
    '''
    MULTI_ACQ_AVERAGE = 4016
    r'''
    Multi Acquisition Average
    '''
    BUTTERWORTH_FILTER = 4017
    r'''
    Butterworth IIR Filter
    '''
    CHEBYSHEV_FILTER = 4018
    r'''
    Chebyshev IIR Filter
    '''
    FFT_AMP_SPECTRUM_DB = 4019
    r'''
    FFT Amp. Spectrum (dB)
    '''
    HAMMING_WINDOW = 4020
    r'''
    Hamming Window
    '''
    WINDOWED_FIR_FILTER = 4021
    r'''
    FIR Windowed Filter
    '''
    BESSEL_FILTER = 4022
    r'''
    Bessel IIR Filter
    '''
    TRIANGLE_WINDOW = 4023
    r'''
    Triangle Window
    '''
    BLACKMAN_WINDOW = 4024
    r'''
    Blackman Window
    '''
    ARRAY_OFFSET = 4025
    r'''
    Array Offset
    '''
    ARRAY_GAIN = 4026
    r'''
    Array Gain
    '''


class CableSenseMode(Enum):
    DISABLED = 0
    r'''
    The oscilloscope is not configured to emit a CableSense signal.
    '''
    ON_DEMAND = 1
    r'''
    The oscilloscope is configured to emit a single CableSense pulse.
    '''


class _CalibrationTypes(Enum):
    SELF = 1
    EXTERNAL = 0
    MANUFACTURE = 2


class ClearableMeasurement(Enum):
    ALL_MEASUREMENTS = 10000
    MULTI_ACQ_VOLTAGE_HISTOGRAM = 4004
    MULTI_ACQ_TIME_HISTOGRAM = 4005
    MULTI_ACQ_AVERAGE = 4016
    FREQUENCY = 2
    AVERAGE_FREQUENCY = 1016
    FFT_FREQUENCY = 1008
    PERIOD = 3
    AVERAGE_PERIOD = 1015
    RISE_TIME = 0
    FALL_TIME = 1
    RISE_SLEW_RATE = 1010
    FALL_SLEW_RATE = 1011
    OVERSHOOT = 18
    PRESHOOT = 19
    VOLTAGE_RMS = 4
    VOLTAGE_CYCLE_RMS = 16
    AC_ESTIMATE = 1012
    FFT_AMPLITUDE = 1009
    VOLTAGE_AVERAGE = 10
    VOLTAGE_CYCLE_AVERAGE = 17
    DC_ESTIMATE = 1013
    VOLTAGE_MAX = 6
    VOLTAGE_MIN = 7
    VOLTAGE_PEAK_TO_PEAK = 5
    VOLTAGE_HIGH = 8
    VOLTAGE_LOW = 9
    AMPLITUDE = 15
    VOLTAGE_TOP = 1007
    VOLTAGE_BASE = 1006
    VOLTAGE_BASE_TO_TOP = 1017
    WIDTH_NEG = 11
    WIDTH_POS = 12
    DUTY_CYCLE_NEG = 13
    DUTY_CYCLE_POS = 14
    INTEGRAL = 1005
    AREA = 1003
    CYCLE_AREA = 1004
    TIME_DELAY = 1014
    PHASE_DELAY = 1018
    LOW_REF_VOLTS = 1000
    MID_REF_VOLTS = 1001
    HIGH_REF_VOLTS = 1002
    VOLTAGE_HISTOGRAM_MEAN = 2000
    VOLTAGE_HISTOGRAM_STDEV = 2001
    VOLTAGE_HISTOGRAM_MEDIAN = 2003
    VOLTAGE_HISTOGRAM_MODE = 2010
    VOLTAGE_HISTOGRAM_MAX = 2005
    VOLTAGE_HISTOGRAM_MIN = 2006
    VOLTAGE_HISTOGRAM_PEAK_TO_PEAK = 2002
    VOLTAGE_HISTOGRAM_MEAN_PLUS_STDEV = 2007
    VOLTAGE_HISTOGRAM_MEAN_PLUS_2_STDEV = 2008
    VOLTAGE_HISTOGRAM_MEAN_PLUS_3_STDEV = 2009
    VOLTAGE_HISTOGRAM_HITS = 2004
    VOLTAGE_HISTOGRAM_NEW_HITS = 2011
    TIME_HISTOGRAM_MEAN = 3000
    TIME_HISTOGRAM_STDEV = 3001
    TIME_HISTOGRAM_MEDIAN = 3003
    TIME_HISTOGRAM_MODE = 3010
    TIME_HISTOGRAM_MAX = 3005
    TIME_HISTOGRAM_MIN = 3006
    TIME_HISTOGRAM_PEAK_TO_PEAK = 3002
    TIME_HISTOGRAM_MEAN_PLUS_STDEV = 3007
    TIME_HISTOGRAM_MEAN_PLUS_2_STDEV = 3008
    TIME_HISTOGRAM_MEAN_PLUS_3_STDEV = 3009
    TIME_HISTOGRAM_HITS = 3004
    TIME_HISTOGRAM_NEW_HITS = 3011


class FIRFilterWindow(Enum):
    NONE = 0
    r'''
    No window.
    '''
    HANNING = 409
    r'''
    Specifies a Hanning window.
    '''
    FLAT_TOP = 410
    r'''
    Specifies a Flat Top window.
    '''
    HAMMING = 420
    r'''
    Specifies a Hamming window.
    '''
    TRIANGLE = 423
    r'''
    Specifies a Triangle window.
    '''
    BLACKMAN = 424
    r'''
    Specifies a Blackman window.
    '''


class FetchRelativeTo(Enum):
    READ_POINTER = 388
    r'''
    The read pointer is set to zero when a new acquisition is initiated. After every fetch the read pointer is incremeted to be the sample after the last sample retrieved.  Therefore, you can repeatedly fetch relative to the read pointer for a continuous acquisition program.
    '''
    PRETRIGGER = 477
    r'''
    Fetches relative to the first pretrigger point requested with configure_horizontal_timing.
    '''
    NOW = 481
    r'''
    Fetch data at the last sample acquired.
    '''
    START = 482
    r'''
    Fetch data starting at the first point sampled by the digitizer.
    '''
    TRIGGER = 483
    r'''
    Fetch at the first posttrigger sample.
    '''


class FilterType(Enum):
    LOWPASS = 0
    r'''
    Specifies lowpass as the filter type.
    '''
    HIGHPASS = 1
    r'''
    Specifies highpass as the filter type.
    '''
    BANDPASS = 2
    r'''
    Specifies bandpass as the filter type.
    '''
    BANDSTOP = 3
    r'''
    Specifies bandstop as the filter type.
    '''


class FlexFIRAntialiasFilterType(Enum):
    FOURTYEIGHT_TAP_STANDARD = 0
    r'''
    This filter is optimized for alias protection and frequency-domain flatness
    '''
    FOURTYEIGHT_TAP_HANNING = 1
    r'''
    This filter is optimized for the lowest possible bandwidth for a 48 tap filter and maximizes the SNR
    '''
    SIXTEEN_TAP_HANNING = 2
    r'''
    This filter is optimized for the lowest possible bandwidth for a 16 tap filter and maximizes the SNR
    '''
    EIGHT_TAP_HANNING = 3
    r'''
    This filter is optimized for the lowest possible bandwidth for a 8 tap filter and maximizes the SNR
    '''


class GlitchCondition(Enum):
    GREATER = 2
    r'''
    Trigger on pulses with a duration greater than the specified glitch width.
    '''
    LESS = 1
    r'''
    Trigger on pulses with a duration shorter than the specified glitch width.
    '''


class GlitchPolarity(Enum):
    POSITIVE = 1
    r'''
    Trigger on pulses of positive polarity relative to the trigger threshold.
    '''
    NEGATIVE = 2
    r'''
    Trigger on pulses of negative polarity relative to the trigger threshold.
    '''
    EITHER = 3
    r'''
    Trigger on pulses of either positive or negative polarity.
    '''


class Option(Enum):
    SELF_CALIBRATE_ALL_CHANNELS = 0
    r'''
    Self Calibrating all Channels
    '''
    RESTORE_EXTERNAL_CALIBRATION = 1
    r'''
    Restore External Calibration.
    '''


class PercentageMethod(Enum):
    LOWHIGH = 0
    r'''
    Specifies that the reference level percentages should be computed using
    the low/high method,
    '''
    MINMAX = 1
    r'''
    Reference level percentages are computed using the min/max method.
    '''
    BASETOP = 2
    r'''
    Reference level percentages are computed using the base/top method.
    '''


class RISMethod(Enum):
    EXACT_NUM_AVERAGES = 1
    r'''
    Acquires exactly the specified number of records for each bin in the RIS acquisition.  An error is returned from the fetch method if the RIS acquisition does not successfully acquire the specified number of waveforms within the timeout period.  You may call the fetch method again to allow more time for the acquisition to finish.
    '''
    MIN_NUM_AVERAGES = 2
    r'''
    Each RIS sample is the average of a least a minimum number of randomly
    distributed points.
    '''
    INCOMPLETE = 3
    r'''
    Returns the RIS waveform after the specified timeout even if it is incomplete.  If no waveforms have been acquired in certain bins, these bins will have a NaN (when fetching scaled data) or a zero (when fetching binary data). A warning (positive error code) is returned from the fetch method if the RIS acquisition did not finish.  The acquisition aborts when data is returned.
    '''
    LIMITED_BIN_WIDTH = 5
    r'''
    Limits the waveforms in the various bins to be within 200 ps of the center of the bin.
    '''


class RefLevelUnits(Enum):
    VOLTS = 0
    r'''
    Specifies that the reference levels are given in units of volts.
    '''
    PERCENTAGE = 1
    r'''
    (Default) Specifies that the reference levels are given in percentage
    units.
    '''


class RefTriggerDetectorLocation(Enum):
    ANALOG_DETECTION_CIRCUIT = 0
    r'''
    use the hardware analog circuitry to implement the reference trigger.  This option will trigger before any onboard signal processing.
    '''
    DDC_OUTPUT = 1
    r'''
    use the onboard signal processing logic to implement the reference trigger.  This option will trigger based on the onboard signal processed data.
    '''


class RuntPolarity(Enum):
    POSITIVE = 1
    r'''
    Trigger on pulses of positive polarity relative to runt_low_threshold that do not cross runt_high_threshold.
    '''
    NEGATIVE = 2
    r'''
    Trigger on pulses of negative polarity relative to runt_high_threshold that do not cross runt_low_threshold.
    '''
    EITHER = 3
    r'''
    Trigger on pulses of either positive or negative polarity.
    '''


class RuntTimeCondition(Enum):
    NONE = 0
    r'''
    Time qualification is disabled. Trigger on runt pulses based solely on the voltage level of the pulses.
    '''
    WITHIN = 1
    r'''
    Trigger on pulses that, in addition to meeting runt voltage criteria, have a duration within the range bounded by runt_time_low_limit and runt_time_high_limit.
    '''
    OUTSIDE = 2
    r'''
    Trigger on pulses that, in addition to meeting runt voltage criteria, have a duration not within the range bounded by runt_time_low_limit and runt_time_high_limit.
    '''


class ScalarMeasurement(Enum):
    NO_MEASUREMENT = 4000
    r'''
    None
    '''
    RISE_TIME = 0
    FALL_TIME = 1
    FREQUENCY = 2
    PERIOD = 3
    VOLTAGE_RMS = 4
    VOLTAGE_PEAK_TO_PEAK = 5
    VOLTAGE_MAX = 6
    VOLTAGE_MIN = 7
    VOLTAGE_HIGH = 8
    VOLTAGE_LOW = 9
    VOLTAGE_AVERAGE = 10
    WIDTH_NEG = 11
    WIDTH_POS = 12
    DUTY_CYCLE_NEG = 13
    DUTY_CYCLE_POS = 14
    AMPLITUDE = 15
    VOLTAGE_CYCLE_RMS = 16
    VOLTAGE_CYCLE_AVERAGE = 17
    OVERSHOOT = 18
    PRESHOOT = 19
    LOW_REF_VOLTS = 1000
    MID_REF_VOLTS = 1001
    HIGH_REF_VOLTS = 1002
    AREA = 1003
    CYCLE_AREA = 1004
    INTEGRAL = 1005
    VOLTAGE_BASE = 1006
    VOLTAGE_TOP = 1007
    FFT_FREQUENCY = 1008
    FFT_AMPLITUDE = 1009
    RISE_SLEW_RATE = 1010
    FALL_SLEW_RATE = 1011
    AC_ESTIMATE = 1012
    DC_ESTIMATE = 1013
    TIME_DELAY = 1014
    AVERAGE_PERIOD = 1015
    AVERAGE_FREQUENCY = 1016
    VOLTAGE_BASE_TO_TOP = 1017
    PHASE_DELAY = 1018


class TerminalConfiguration(Enum):
    SINGLE_ENDED = 0
    r'''
    Channel is single ended
    '''
    UNBALANCED_DIFFERENTIAL = 1
    r'''
    Channel is unbalanced differential
    '''
    DIFFERENTIAL = 2
    r'''
    Channel is differential
    '''


class TriggerCoupling(Enum):
    AC = 0
    r'''
    AC coupling
    '''
    DC = 1
    r'''
    DC coupling
    '''
    HF_REJECT = 3
    r'''
    Highpass filter coupling
    '''
    LF_REJECT = 4
    r'''
    Lowpass filter coupling
    '''
    AC_PLUS_HF_REJECT = 1001
    r'''
    Highpass and lowpass filter coupling
    '''


class TriggerModifier(Enum):
    NO_TRIGGER_MOD = 1
    r'''
    Normal triggering.
    '''
    AUTO = 2
    r'''
    Software will trigger an acquisition automatically if no trigger arrives
    after a certain amount of time.
    '''
    AUTO_LEVEL = 3


class TriggerSlope(Enum):
    NEGATIVE = 0
    r'''
    Falling edge
    '''
    POSITIVE = 1
    r'''
    Rising edge
    '''
    SLOPE_EITHER = 3
    r'''
    Either edge
    '''


class TriggerType(Enum):
    EDGE = 1
    r'''
    Configures the digitizer for edge triggering.  An edge trigger occurs when the trigger signal crosses the trigger level specified with the set trigger slope.  You configure the trigger level and slope with configure_trigger_edge.
    '''
    HYSTERESIS = 1001
    r'''
    Configures the digitizer for hysteresis triggering.  A hysteresis trigger occurs when the trigger signal crosses the trigger level with the specified slope and passes through the hysteresis window you specify. You configure the trigger level, slope, and hysteresis with configure_trigger_hysteresis.
    '''
    DIGITAL = 1002
    r'''
    Configures the digitizer for digital triggering. A digital trigger occurs when the trigger signal has the specified slope. You configure the trigger slope with configure_trigger_digital.
    '''
    WINDOW = 1003
    r'''
    Configures the digitizer for window triggering.  A window trigger occurs when the trigger signal enters or leaves the window defined by the values you specify with the Low Window Level, High Window Level, and Window Mode Parameters.  You configure the low window level high window level, and window mode with configure_trigger_window.
    '''
    SOFTWARE = 1004
    r'''
    Configures the digitizer for software triggering.  A software trigger occurs when SendSoftwareTrigger is called.
    '''
    TV = 5
    r'''
    Configures the digitizer for video/TV triggering.   You configure the video trigger parameters like signal Format, Line to trigger off of, Polarity, and Enable DC Restore with configure_trigger_video.
    '''
    GLITCH = 4
    WIDTH = 2
    RUNT = 3
    IMMEDIATE = 6
    r'''
    Configures the digitizer for immediate triggering.   An immediate trigger occurs as soon as the pretrigger samples are acquired.
    '''


class TriggerWindowMode(Enum):
    ENTERING = 0
    r'''
    Trigger upon entering the window
    '''
    LEAVING = 1
    r'''
    Trigger upon leaving the window
    '''
    ENTERING_OR_LEAVING = 2


class VerticalCoupling(Enum):
    AC = 0
    r'''
    AC coupling
    '''
    DC = 1
    r'''
    DC coupling
    '''
    GND = 2
    r'''
    GND coupling
    '''


class VideoPolarity(Enum):
    POSITIVE = 1
    r'''
    Specifies that the video signal has positive polarity.
    '''
    NEGATIVE = 2
    r'''
    Specifies that the video signal has negative polarity.
    '''


class VideoSignalFormat(Enum):
    NTSC = 1
    r'''
    NTSC signal format supports line numbers from 1 to 525
    '''
    PAL = 2
    r'''
    PAL signal format supports line numbers from 1 to 625
    '''
    SECAM = 3
    r'''
    SECAM signal format supports line numbers from 1 to 625
    '''
    M_PAL = 1001
    r'''
    M-PAL signal format supports line numbers from 1 to 525
    '''
    VIDEO_480I_59_94_FIELDS_PER_SECOND = 1010
    r'''
    480 lines, interlaced, 59.94 fields per second
    '''
    VIDEO_480I_60_FIELDS_PER_SECOND = 1011
    r'''
    480 lines, interlaced, 60 fields per second
    '''
    VIDEO_480P_59_94_FRAMES_PER_SECOND = 1015
    r'''
    480 lines, progressive, 59.94 frames per second
    '''
    VIDEO_480P_60_FRAMES_PER_SECOND = 1016
    r'''
    480 lines, progressive,60 frames per second
    '''
    VIDEO_576I_50_FIELDS_PER_SECOND = 1020
    r'''
    576 lines, interlaced, 50 fields per second
    '''
    VIDEO_576P_50_FRAMES_PER_SECOND = 1025
    r'''
    576 lines, progressive, 50 frames per second
    '''
    VIDEO_720P_50_FRAMES_PER_SECOND = 1031
    r'''
    720 lines, progressive, 50 frames per second
    '''
    VIDEO_720P_59_94_FRAMES_PER_SECOND = 1032
    r'''
    720 lines, progressive, 59.94 frames per second
    '''
    VIDEO_720P_60_FRAMES_PER_SECOND = 1033
    r'''
    720 lines, progressive, 60 frames per second
    '''
    VIDEO_1080I_50_FIELDS_PER_SECOND = 1040
    r'''
    1,080 lines, interlaced, 50 fields per second
    '''
    VIDEO_1080I_59_94_FIELDS_PER_SECOND = 1041
    r'''
    1,080 lines, interlaced, 59.94 fields per second
    '''
    VIDEO_1080I_60_FIELDS_PER_SECOND = 1042
    r'''
    1,080 lines, interlaced, 60 fields per second
    '''
    VIDEO_1080P_24_FRAMES_PER_SECOND = 1045
    r'''
    1,080 lines, progressive, 24 frames per second
    '''


class VideoTriggerEvent(Enum):
    FIELD1 = 1
    r'''
    Trigger on field 1 of the signal
    '''
    FIELD2 = 2
    r'''
    Trigger on field 2 of the signal
    '''
    ANY_FIELD = 3
    r'''
    Trigger on the first field acquired
    '''
    ANY_LINE = 4
    r'''
    Trigger on the first line acquired
    '''
    LINE_NUMBER = 5
    r'''
    Trigger on a specific line of a video signal.  Valid values vary depending on the signal format configured.
    '''


class WhichTrigger(Enum):
    START = 0
    ARM_REFERENCE = 1
    REFERENCE = 2
    ADVANCE = 3


class WidthCondition(Enum):
    WITHIN = 1
    r'''
    Trigger on pulses with a duration within the range bounded by width_low_threshold and width_high_threshold.
    '''
    OUTSIDE = 2
    r'''
    Trigger on pulses with a duration not within the range bounded by width_low_threshold and width_high_threshold.
    '''


class WidthPolarity(Enum):
    POSITIVE = 1
    r'''
    Trigger on pulses of positive polarity relative to the trigger threshold.
    '''
    NEGATIVE = 2
    r'''
    Trigger on pulses of negative polarity relative to the trigger threshold.
    '''
    EITHER = 3
    r'''
    Trigger on pulses of either positive or negative polarity.
    '''
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/niscope/niscope/errors.py sha256=8d5c0ce0ded03f5884e2c39382c8baa8656fb0da92d5f8822c886c25de3650f6 bytes=4360 -->
## FILE: generated/niscope/niscope/errors.py

- repository: `ni/nimi-python`
- source_path: `generated/niscope/niscope/errors.py`
- sha256: `8d5c0ce0ded03f5884e2c39382c8baa8656fb0da92d5f8822c886c25de3650f6`
- bytes: 4360

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
    '''Base error class for NI-SCOPE'''

    def __init__(self, message):
        super(Error, self).__init__(message)


class DriverError(Error):
    '''An error originating from the NI-SCOPE driver'''

    def __init__(self, code, description):
        assert _is_error(code), "Should not raise Error if code is not fatal."
        self.code = code
        self.description = description
        super(DriverError, self).__init__(str(self.code) + ": " + self.description)


class DriverWarning(Warning):
    '''A warning originating from the NI-SCOPE driver'''

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
        super(DriverNotInstalledError, self).__init__('The NI-SCOPE runtime could not be loaded. Make sure it is installed and its bitness matches that of your Python interpreter. Please visit http://www.ni.com/downloads/drivers/ to download and install it.')


class DriverTooOldError(Error):
    '''An error due to using this module with an older version of the NI-SCOPE driver runtime.'''

    def __init__(self):
        super(DriverTooOldError, self).__init__('A function was not found in the NI-SCOPE runtime. Please visit http://www.ni.com/downloads/drivers/ to download a newer version and install it.')


class DriverTooNewError(Error):
    '''An error due to the NI-SCOPE driver runtime being too new for this module.'''

    def __init__(self):
        super(DriverTooNewError, self).__init__('The NI-SCOPE runtime returned an unexpected value. This can occur if it is too new for the niscope Python module. Upgrade the niscope Python module.')


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

    Helper function for handling errors returned by niscope.Library.
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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/niscope/niscope/grpc_session_options.py sha256=fdd54e03b09a3e04fd001bb5ee7bde43cab80910b4ead3d9a1f469457b8e0f18 bytes=3454 -->
## FILE: generated/niscope/niscope/grpc_session_options.py

- repository: `ni/nimi-python`
- source_path: `generated/niscope/niscope/grpc_session_options.py`
- sha256: `fdd54e03b09a3e04fd001bb5ee7bde43cab80910b4ead3d9a1f469457b8e0f18`
- bytes: 3454

````python
# -*- coding: utf-8 -*-
# This file was generated

from enum import IntEnum


# This constant specifies the gRPC package and service used by this API.
# Customers can pass this value to the MeasurementLink discovery service to resolve the server instance that provides this interface.
GRPC_SERVICE_INTERFACE_NAME = 'niscope_grpc.NiScope'

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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/niscope/niscope/measurement_stats.py sha256=666cc48ad3ee3e5c4dc00b84f0100981f0d5ba0a52d1a9ad7cd2100567a22a6d bytes=1690 -->
## FILE: generated/niscope/niscope/measurement_stats.py

- repository: `ni/nimi-python`
- source_path: `generated/niscope/niscope/measurement_stats.py`
- sha256: `666cc48ad3ee3e5c4dc00b84f0100981f0d5ba0a52d1a9ad7cd2100567a22a6d`
- bytes: 1690

````python
class MeasurementStats:
    def __init__(self, result=0.0, mean=0.0, stdev=0.0, min_val=0.0, max_val=0.0, num_in_stats=0):
        self.result = result
        self.mean = mean
        self.stdev = stdev
        self.min_val = min_val
        self.max_val = max_val
        self.num_in_stats = num_in_stats

        self.channel = None
        self.record = None

    def __repr__(self):
        parameter_list = [
            f'result={self.result}',
            f'mean={self.mean}',
            f'stdev={self.stdev}',
            f'min_val={self.min_val}',
            f'max_val={self.max_val}',
            f'num_in_stats={self.num_in_stats}'
        ]

        return '{}({})'.format(self.__class__.__name__, ', '.join(parameter_list))

    def __str__(self):
        row_format_g = '{:<20}: {:,.6g}\n'
        row_format_d = '{:<20}: {:,}\n'
        row_format_s = '{:<20}: {:}\n'

        string_representation = ''
        if self.channel is not None:
            string_representation += row_format_s.format('Channel', self.channel)
        if self.record is not None:
            string_representation += row_format_d.format('Record', self.record)

        string_representation += row_format_g.format('Result', self.result)
        string_representation += row_format_g.format('Mean', self.mean)
        string_representation += row_format_g.format('Standard Deviation', self.stdev)
        string_representation += row_format_g.format('Minimum Value', self.min_val)
        string_representation += row_format_g.format('Maximum Value', self.max_val)
        string_representation += row_format_d.format('Number in Stats', self.num_in_stats)

        return string_representation
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/niscope/niscope/nidevice_pb2.py sha256=9a935a95cbe830099345438b27f1460989b073de2e873f43cb394ac0df4ced54 bytes=2009 -->
## FILE: generated/niscope/niscope/nidevice_pb2.py

- repository: `ni/nimi-python`
- source_path: `generated/niscope/niscope/nidevice_pb2.py`
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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/niscope/niscope/nidevice_pb2_grpc.py sha256=d686e804f171693117b7d030ec4023f205c70c234c8590f6557aa8702f65fe09 bytes=159 -->
## FILE: generated/niscope/niscope/nidevice_pb2_grpc.py

- repository: `ni/nimi-python`
- source_path: `generated/niscope/niscope/nidevice_pb2_grpc.py`
- sha256: `d686e804f171693117b7d030ec4023f205c70c234c8590f6557aa8702f65fe09`
- bytes: 159

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
````
