# NI OSS SOURCE SNAPSHOT: nimi-python

<!--NI_OSS_SNAPSHOT repo=ni/nimi-python commit=6511f8025f072f7f7021953888b916bbdc31aa2a -->

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidmm/nidmm/unit_tests/_mock_helper.py sha256=dbc55c421665883fe394eb031e9db123de6156c92e87565eab971bf657df754c bytes=44680 -->
## FILE: generated/nidmm/nidmm/unit_tests/_mock_helper.py

- repository: `ni/nimi-python`
- source_path: `generated/nidmm/nidmm/unit_tests/_mock_helper.py`
- sha256: `dbc55c421665883fe394eb031e9db123de6156c92e87565eab971bf657df754c`
- bytes: 44680

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
        self._defaults['ConfigureMeasurementAbsolute'] = {}
        self._defaults['ConfigureMeasurementAbsolute']['return'] = 0
        self._defaults['ConfigureMeasurementDigits'] = {}
        self._defaults['ConfigureMeasurementDigits']['return'] = 0
        self._defaults['ConfigureMultiPoint'] = {}
        self._defaults['ConfigureMultiPoint']['return'] = 0
        self._defaults['ConfigureRTDCustom'] = {}
        self._defaults['ConfigureRTDCustom']['return'] = 0
        self._defaults['ConfigureRTDType'] = {}
        self._defaults['ConfigureRTDType']['return'] = 0
        self._defaults['ConfigureThermistorCustom'] = {}
        self._defaults['ConfigureThermistorCustom']['return'] = 0
        self._defaults['ConfigureThermocouple'] = {}
        self._defaults['ConfigureThermocouple']['return'] = 0
        self._defaults['ConfigureTrigger'] = {}
        self._defaults['ConfigureTrigger']['return'] = 0
        self._defaults['ConfigureWaveformAcquisition'] = {}
        self._defaults['ConfigureWaveformAcquisition']['return'] = 0
        self._defaults['Disable'] = {}
        self._defaults['Disable']['return'] = 0
        self._defaults['ExportAttributeConfigurationBuffer'] = {}
        self._defaults['ExportAttributeConfigurationBuffer']['return'] = 0
        self._defaults['ExportAttributeConfigurationBuffer']['configuration'] = None
        self._defaults['ExportAttributeConfigurationFile'] = {}
        self._defaults['ExportAttributeConfigurationFile']['return'] = 0
        self._defaults['Fetch'] = {}
        self._defaults['Fetch']['return'] = 0
        self._defaults['Fetch']['reading'] = None
        self._defaults['FetchMultiPoint'] = {}
        self._defaults['FetchMultiPoint']['return'] = 0
        self._defaults['FetchMultiPoint']['readingArray'] = None
        self._defaults['FetchMultiPoint']['actualNumberOfPoints'] = None
        self._defaults['FetchWaveform'] = {}
        self._defaults['FetchWaveform']['return'] = 0
        self._defaults['FetchWaveform']['waveformArray'] = None
        self._defaults['FetchWaveform']['actualNumberOfPoints'] = None
        self._defaults['GetAttributeViBoolean'] = {}
        self._defaults['GetAttributeViBoolean']['return'] = 0
        self._defaults['GetAttributeViBoolean']['attributeValue'] = None
        self._defaults['GetAttributeViInt32'] = {}
        self._defaults['GetAttributeViInt32']['return'] = 0
        self._defaults['GetAttributeViInt32']['attributeValue'] = None
        self._defaults['GetAttributeViReal64'] = {}
        self._defaults['GetAttributeViReal64']['return'] = 0
        self._defaults['GetAttributeViReal64']['attributeValue'] = None
        self._defaults['GetAttributeViString'] = {}
        self._defaults['GetAttributeViString']['return'] = 0
        self._defaults['GetAttributeViString']['attributeValue'] = None
        self._defaults['GetCalDateAndTime'] = {}
        self._defaults['GetCalDateAndTime']['return'] = 0
        self._defaults['GetCalDateAndTime']['month'] = None
        self._defaults['GetCalDateAndTime']['day'] = None
        self._defaults['GetCalDateAndTime']['year'] = None
        self._defaults['GetCalDateAndTime']['hour'] = None
        self._defaults['GetCalDateAndTime']['minute'] = None
        self._defaults['GetDevTemp'] = {}
        self._defaults['GetDevTemp']['return'] = 0
        self._defaults['GetDevTemp']['temperature'] = None
        self._defaults['GetError'] = {}
        self._defaults['GetError']['return'] = 0
        self._defaults['GetError']['errorCode'] = None
        self._defaults['GetError']['description'] = None
        self._defaults['GetExtCalRecommendedInterval'] = {}
        self._defaults['GetExtCalRecommendedInterval']['return'] = 0
        self._defaults['GetExtCalRecommendedInterval']['months'] = None
        self._defaults['GetLastCalTemp'] = {}
        self._defaults['GetLastCalTemp']['return'] = 0
        self._defaults['GetLastCalTemp']['temperature'] = None
        self._defaults['GetSelfCalSupported'] = {}
        self._defaults['GetSelfCalSupported']['return'] = 0
        self._defaults['GetSelfCalSupported']['selfCalSupported'] = None
        self._defaults['ImportAttributeConfigurationBuffer'] = {}
        self._defaults['ImportAttributeConfigurationBuffer']['return'] = 0
        self._defaults['ImportAttributeConfigurationFile'] = {}
        self._defaults['ImportAttributeConfigurationFile']['return'] = 0
        self._defaults['InitWithOptions'] = {}
        self._defaults['InitWithOptions']['return'] = 0
        self._defaults['InitWithOptions']['vi'] = None
        self._defaults['Initiate'] = {}
        self._defaults['Initiate']['return'] = 0
        self._defaults['LockSession'] = {}
        self._defaults['LockSession']['return'] = 0
        self._defaults['LockSession']['callerHasLock'] = None
        self._defaults['PerformOpenCableComp'] = {}
        self._defaults['PerformOpenCableComp']['return'] = 0
        self._defaults['PerformOpenCableComp']['conductance'] = None
        self._defaults['PerformOpenCableComp']['susceptance'] = None
        self._defaults['PerformShortCableComp'] = {}
        self._defaults['PerformShortCableComp']['return'] = 0
        self._defaults['PerformShortCableComp']['resistance'] = None
        self._defaults['PerformShortCableComp']['reactance'] = None
        self._defaults['Read'] = {}
        self._defaults['Read']['return'] = 0
        self._defaults['Read']['reading'] = None
        self._defaults['ReadMultiPoint'] = {}
        self._defaults['ReadMultiPoint']['return'] = 0
        self._defaults['ReadMultiPoint']['readingArray'] = None
        self._defaults['ReadMultiPoint']['actualNumberOfPoints'] = None
        self._defaults['ReadStatus'] = {}
        self._defaults['ReadStatus']['return'] = 0
        self._defaults['ReadStatus']['acquisitionBacklog'] = None
        self._defaults['ReadStatus']['acquisitionStatus'] = None
        self._defaults['ReadWaveform'] = {}
        self._defaults['ReadWaveform']['return'] = 0
        self._defaults['ReadWaveform']['waveformArray'] = None
        self._defaults['ReadWaveform']['actualNumberOfPoints'] = None
        self._defaults['ResetWithDefaults'] = {}
        self._defaults['ResetWithDefaults']['return'] = 0
        self._defaults['SelfCal'] = {}
        self._defaults['SelfCal']['return'] = 0
        self._defaults['SendSoftwareTrigger'] = {}
        self._defaults['SendSoftwareTrigger']['return'] = 0
        self._defaults['SetAttributeViBoolean'] = {}
        self._defaults['SetAttributeViBoolean']['return'] = 0
        self._defaults['SetAttributeViInt32'] = {}
        self._defaults['SetAttributeViInt32']['return'] = 0
        self._defaults['SetAttributeViReal64'] = {}
        self._defaults['SetAttributeViReal64']['return'] = 0
        self._defaults['SetAttributeViString'] = {}
        self._defaults['SetAttributeViString']['return'] = 0
        self._defaults['SetRuntimeEnvironment'] = {}
        self._defaults['SetRuntimeEnvironment']['return'] = 0
        self._defaults['UnlockSession'] = {}
        self._defaults['UnlockSession']['return'] = 0
        self._defaults['UnlockSession']['callerHasLock'] = None
        self._defaults['close'] = {}
        self._defaults['close']['return'] = 0
        self._defaults['error_message'] = {}
        self._defaults['error_message']['return'] = 0
        self._defaults['error_message']['errorMessage'] = None
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

    def niDMM_Abort(self, vi):  # noqa: N802
        if self._defaults['Abort']['return'] != 0:
            return self._defaults['Abort']['return']
        return self._defaults['Abort']['return']

    def niDMM_ConfigureMeasurementAbsolute(self, vi, measurement_function, range, resolution_absolute):  # noqa: N802
        if self._defaults['ConfigureMeasurementAbsolute']['return'] != 0:
            return self._defaults['ConfigureMeasurementAbsolute']['return']
        return self._defaults['ConfigureMeasurementAbsolute']['return']

    def niDMM_ConfigureMeasurementDigits(self, vi, measurement_function, range, resolution_digits):  # noqa: N802
        if self._defaults['ConfigureMeasurementDigits']['return'] != 0:
            return self._defaults['ConfigureMeasurementDigits']['return']
        return self._defaults['ConfigureMeasurementDigits']['return']

    def niDMM_ConfigureMultiPoint(self, vi, trigger_count, sample_count, sample_trigger, sample_interval):  # noqa: N802
        if self._defaults['ConfigureMultiPoint']['return'] != 0:
            return self._defaults['ConfigureMultiPoint']['return']
        return self._defaults['ConfigureMultiPoint']['return']

    def niDMM_ConfigureRTDCustom(self, vi, rtd_a, rtd_b, rtd_c):  # noqa: N802
        if self._defaults['ConfigureRTDCustom']['return'] != 0:
            return self._defaults['ConfigureRTDCustom']['return']
        return self._defaults['ConfigureRTDCustom']['return']

    def niDMM_ConfigureRTDType(self, vi, rtd_type, rtd_resistance):  # noqa: N802
        if self._defaults['ConfigureRTDType']['return'] != 0:
            return self._defaults['ConfigureRTDType']['return']
        return self._defaults['ConfigureRTDType']['return']

    def niDMM_ConfigureThermistorCustom(self, vi, thermistor_a, thermistor_b, thermistor_c):  # noqa: N802
        if self._defaults['ConfigureThermistorCustom']['return'] != 0:
            return self._defaults['ConfigureThermistorCustom']['return']
        return self._defaults['ConfigureThermistorCustom']['return']

    def niDMM_ConfigureThermocouple(self, vi, thermocouple_type, reference_junction_type):  # noqa: N802
        if self._defaults['ConfigureThermocouple']['return'] != 0:
            return self._defaults['ConfigureThermocouple']['return']
        return self._defaults['ConfigureThermocouple']['return']

    def niDMM_ConfigureTrigger(self, vi, trigger_source, trigger_delay):  # noqa: N802
        if self._defaults['ConfigureTrigger']['return'] != 0:
            return self._defaults['ConfigureTrigger']['return']
        return self._defaults['ConfigureTrigger']['return']

    def niDMM_ConfigureWaveformAcquisition(self, vi, measurement_function, range, rate, waveform_points):  # noqa: N802
        if self._defaults['ConfigureWaveformAcquisition']['return'] != 0:
            return self._defaults['ConfigureWaveformAcquisition']['return']
        return self._defaults['ConfigureWaveformAcquisition']['return']

    def niDMM_Disable(self, vi):  # noqa: N802
        if self._defaults['Disable']['return'] != 0:
            return self._defaults['Disable']['return']
        return self._defaults['Disable']['return']

    def niDMM_ExportAttributeConfigurationBuffer(self, vi, size, configuration):  # noqa: N802
        if self._defaults['ExportAttributeConfigurationBuffer']['return'] != 0:
            return self._defaults['ExportAttributeConfigurationBuffer']['return']
        # configuration
        if self._defaults['ExportAttributeConfigurationBuffer']['configuration'] is None:
            raise MockFunctionCallError("niDMM_ExportAttributeConfigurationBuffer", param='configuration')
        if size.value == 0:
            return len(self._defaults['ExportAttributeConfigurationBuffer']['configuration'])
        try:
            configuration_ref = configuration.contents
        except AttributeError:
            configuration_ref = configuration
        for i in range(len(self._defaults['ExportAttributeConfigurationBuffer']['configuration'])):
            configuration_ref[i] = self._defaults['ExportAttributeConfigurationBuffer']['configuration'][i]
        return self._defaults['ExportAttributeConfigurationBuffer']['return']

    def niDMM_ExportAttributeConfigurationFile(self, vi, file_path):  # noqa: N802
        if self._defaults['ExportAttributeConfigurationFile']['return'] != 0:
            return self._defaults['ExportAttributeConfigurationFile']['return']
        return self._defaults['ExportAttributeConfigurationFile']['return']

    def niDMM_Fetch(self, vi, maximum_time, reading):  # noqa: N802
        if self._defaults['Fetch']['return'] != 0:
            return self._defaults['Fetch']['return']
        # reading
        if self._defaults['Fetch']['reading'] is None:
            raise MockFunctionCallError("niDMM_Fetch", param='reading')
        if reading is not None:
            reading.contents.value = self._defaults['Fetch']['reading']
        return self._defaults['Fetch']['return']

    def niDMM_FetchMultiPoint(self, vi, maximum_time, array_size, reading_array, actual_number_of_points):  # noqa: N802
        if self._defaults['FetchMultiPoint']['return'] != 0:
            return self._defaults['FetchMultiPoint']['return']
        # reading_array
        if self._defaults['FetchMultiPoint']['readingArray'] is None:
            raise MockFunctionCallError("niDMM_FetchMultiPoint", param='readingArray')
        test_value = self._defaults['FetchMultiPoint']['readingArray']
        try:
            reading_array_ref = reading_array.contents
        except AttributeError:
            reading_array_ref = reading_array
        assert len(reading_array_ref) >= len(test_value)
        for i in range(len(test_value)):
            reading_array_ref[i] = test_value[i]
        # actual_number_of_points
        if self._defaults['FetchMultiPoint']['actualNumberOfPoints'] is None:
            raise MockFunctionCallError("niDMM_FetchMultiPoint", param='actualNumberOfPoints')
        if actual_number_of_points is not None:
            actual_number_of_points.contents.value = self._defaults['FetchMultiPoint']['actualNumberOfPoints']
        return self._defaults['FetchMultiPoint']['return']

    def niDMM_FetchWaveform(self, vi, maximum_time, array_size, waveform_array, actual_number_of_points):  # noqa: N802
        if self._defaults['FetchWaveform']['return'] != 0:
            return self._defaults['FetchWaveform']['return']
        # waveform_array
        if self._defaults['FetchWaveform']['waveformArray'] is None:
            raise MockFunctionCallError("niDMM_FetchWaveform", param='waveformArray')
        test_value = self._defaults['FetchWaveform']['waveformArray']
        try:
            waveform_array_ref = waveform_array.contents
        except AttributeError:
            waveform_array_ref = waveform_array
        assert len(waveform_array_ref) >= len(test_value)
        for i in range(len(test_value)):
            waveform_array_ref[i] = test_value[i]
        # actual_number_of_points
        if self._defaults['FetchWaveform']['actualNumberOfPoints'] is None:
            raise MockFunctionCallError("niDMM_FetchWaveform", param='actualNumberOfPoints')
        if actual_number_of_points is not None:
            actual_number_of_points.contents.value = self._defaults['FetchWaveform']['actualNumberOfPoints']
        return self._defaults['FetchWaveform']['return']

    def niDMM_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViBoolean']['return'] != 0:
            return self._defaults['GetAttributeViBoolean']['return']
        # attribute_value
        if self._defaults['GetAttributeViBoolean']['attributeValue'] is None:
            raise MockFunctionCallError("niDMM_GetAttributeViBoolean", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViBoolean']['attributeValue']
        return self._defaults['GetAttributeViBoolean']['return']

    def niDMM_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViInt32']['return'] != 0:
            return self._defaults['GetAttributeViInt32']['return']
        # attribute_value
        if self._defaults['GetAttributeViInt32']['attributeValue'] is None:
            raise MockFunctionCallError("niDMM_GetAttributeViInt32", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViInt32']['attributeValue']
        return self._defaults['GetAttributeViInt32']['return']

    def niDMM_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViReal64']['return'] != 0:
            return self._defaults['GetAttributeViReal64']['return']
        # attribute_value
        if self._defaults['GetAttributeViReal64']['attributeValue'] is None:
            raise MockFunctionCallError("niDMM_GetAttributeViReal64", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViReal64']['attributeValue']
        return self._defaults['GetAttributeViReal64']['return']

    def niDMM_GetAttributeViString(self, vi, channel_name, attribute_id, buffer_size, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViString']['return'] != 0:
            return self._defaults['GetAttributeViString']['return']
        # attribute_value
        if self._defaults['GetAttributeViString']['attributeValue'] is None:
            raise MockFunctionCallError("niDMM_GetAttributeViString", param='attributeValue')
        if buffer_size.value == 0:
            return len(self._defaults['GetAttributeViString']['attributeValue'])
        attribute_value.value = self._defaults['GetAttributeViString']['attributeValue'].encode('ascii')
        return self._defaults['GetAttributeViString']['return']

    def niDMM_GetCalDateAndTime(self, vi, cal_type, month, day, year, hour, minute):  # noqa: N802
        if self._defaults['GetCalDateAndTime']['return'] != 0:
            return self._defaults['GetCalDateAndTime']['return']
        # month
        if self._defaults['GetCalDateAndTime']['month'] is None:
            raise MockFunctionCallError("niDMM_GetCalDateAndTime", param='month')
        if month is not None:
            month.contents.value = self._defaults['GetCalDateAndTime']['month']
        # day
        if self._defaults['GetCalDateAndTime']['day'] is None:
            raise MockFunctionCallError("niDMM_GetCalDateAndTime", param='day')
        if day is not None:
            day.contents.value = self._defaults['GetCalDateAndTime']['day']
        # year
        if self._defaults['GetCalDateAndTime']['year'] is None:
            raise MockFunctionCallError("niDMM_GetCalDateAndTime", param='year')
        if year is not None:
            year.contents.value = self._defaults['GetCalDateAndTime']['year']
        # hour
        if self._defaults['GetCalDateAndTime']['hour'] is None:
            raise MockFunctionCallError("niDMM_GetCalDateAndTime", param='hour')
        if hour is not None:
            hour.contents.value = self._defaults['GetCalDateAndTime']['hour']
        # minute
        if self._defaults['GetCalDateAndTime']['minute'] is None:
            raise MockFunctionCallError("niDMM_GetCalDateAndTime", param='minute')
        if minute is not None:
            minute.contents.value = self._defaults['GetCalDateAndTime']['minute']
        return self._defaults['GetCalDateAndTime']['return']

    def niDMM_GetDevTemp(self, vi, options, temperature):  # noqa: N802
        if self._defaults['GetDevTemp']['return'] != 0:
            return self._defaults['GetDevTemp']['return']
        # temperature
        if self._defaults['GetDevTemp']['temperature'] is None:
            raise MockFunctionCallError("niDMM_GetDevTemp", param='temperature')
        if temperature is not None:
            temperature.contents.value = self._defaults['GetDevTemp']['temperature']
        return self._defaults['GetDevTemp']['return']

    def niDMM_GetError(self, vi, error_code, buffer_size, description):  # noqa: N802
        if self._defaults['GetError']['return'] != 0:
            return self._defaults['GetError']['return']
        # error_code
        if self._defaults['GetError']['errorCode'] is None:
            raise MockFunctionCallError("niDMM_GetError", param='errorCode')
        if error_code is not None:
            error_code.contents.value = self._defaults['GetError']['errorCode']
        # description
        if self._defaults['GetError']['description'] is None:
            raise MockFunctionCallError("niDMM_GetError", param='description')
        if buffer_size.value == 0:
            return len(self._defaults['GetError']['description'])
        description.value = self._defaults['GetError']['description'].encode('ascii')
        return self._defaults['GetError']['return']

    def niDMM_GetExtCalRecommendedInterval(self, vi, months):  # noqa: N802
        if self._defaults['GetExtCalRecommendedInterval']['return'] != 0:
            return self._defaults['GetExtCalRecommendedInterval']['return']
        # months
        if self._defaults['GetExtCalRecommendedInterval']['months'] is None:
            raise MockFunctionCallError("niDMM_GetExtCalRecommendedInterval", param='months')
        if months is not None:
            months.contents.value = self._defaults['GetExtCalRecommendedInterval']['months']
        return self._defaults['GetExtCalRecommendedInterval']['return']

    def niDMM_GetLastCalTemp(self, vi, cal_type, temperature):  # noqa: N802
        if self._defaults['GetLastCalTemp']['return'] != 0:
            return self._defaults['GetLastCalTemp']['return']
        # temperature
        if self._defaults['GetLastCalTemp']['temperature'] is None:
            raise MockFunctionCallError("niDMM_GetLastCalTemp", param='temperature')
        if temperature is not None:
            temperature.contents.value = self._defaults['GetLastCalTemp']['temperature']
        return self._defaults['GetLastCalTemp']['return']

    def niDMM_GetSelfCalSupported(self, vi, self_cal_supported):  # noqa: N802
        if self._defaults['GetSelfCalSupported']['return'] != 0:
            return self._defaults['GetSelfCalSupported']['return']
        # self_cal_supported
        if self._defaults['GetSelfCalSupported']['selfCalSupported'] is None:
            raise MockFunctionCallError("niDMM_GetSelfCalSupported", param='selfCalSupported')
        if self_cal_supported is not None:
            self_cal_supported.contents.value = self._defaults['GetSelfCalSupported']['selfCalSupported']
        return self._defaults['GetSelfCalSupported']['return']

    def niDMM_ImportAttributeConfigurationBuffer(self, vi, size, configuration):  # noqa: N802
        if self._defaults['ImportAttributeConfigurationBuffer']['return'] != 0:
            return self._defaults['ImportAttributeConfigurationBuffer']['return']
        return self._defaults['ImportAttributeConfigurationBuffer']['return']

    def niDMM_ImportAttributeConfigurationFile(self, vi, file_path):  # noqa: N802
        if self._defaults['ImportAttributeConfigurationFile']['return'] != 0:
            return self._defaults['ImportAttributeConfigurationFile']['return']
        return self._defaults['ImportAttributeConfigurationFile']['return']

    def niDMM_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi):  # noqa: N802
        if self._defaults['InitWithOptions']['return'] != 0:
            return self._defaults['InitWithOptions']['return']
        # vi
        if self._defaults['InitWithOptions']['vi'] is None:
            raise MockFunctionCallError("niDMM_InitWithOptions", param='vi')
        if vi is not None:
            vi.contents.value = self._defaults['InitWithOptions']['vi']
        return self._defaults['InitWithOptions']['return']

    def niDMM_Initiate(self, vi):  # noqa: N802
        if self._defaults['Initiate']['return'] != 0:
            return self._defaults['Initiate']['return']
        return self._defaults['Initiate']['return']

    def niDMM_LockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['LockSession']['return'] != 0:
            return self._defaults['LockSession']['return']
        # caller_has_lock
        if self._defaults['LockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niDMM_LockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['LockSession']['callerHasLock']
        return self._defaults['LockSession']['return']

    def niDMM_PerformOpenCableComp(self, vi, conductance, susceptance):  # noqa: N802
        if self._defaults['PerformOpenCableComp']['return'] != 0:
            return self._defaults['PerformOpenCableComp']['return']
        # conductance
        if self._defaults['PerformOpenCableComp']['conductance'] is None:
            raise MockFunctionCallError("niDMM_PerformOpenCableComp", param='conductance')
        if conductance is not None:
            conductance.contents.value = self._defaults['PerformOpenCableComp']['conductance']
        # susceptance
        if self._defaults['PerformOpenCableComp']['susceptance'] is None:
            raise MockFunctionCallError("niDMM_PerformOpenCableComp", param='susceptance')
        if susceptance is not None:
            susceptance.contents.value = self._defaults['PerformOpenCableComp']['susceptance']
        return self._defaults['PerformOpenCableComp']['return']

    def niDMM_PerformShortCableComp(self, vi, resistance, reactance):  # noqa: N802
        if self._defaults['PerformShortCableComp']['return'] != 0:
            return self._defaults['PerformShortCableComp']['return']
        # resistance
        if self._defaults['PerformShortCableComp']['resistance'] is None:
            raise MockFunctionCallError("niDMM_PerformShortCableComp", param='resistance')
        if resistance is not None:
            resistance.contents.value = self._defaults['PerformShortCableComp']['resistance']
        # reactance
        if self._defaults['PerformShortCableComp']['reactance'] is None:
            raise MockFunctionCallError("niDMM_PerformShortCableComp", param='reactance')
        if reactance is not None:
            reactance.contents.value = self._defaults['PerformShortCableComp']['reactance']
        return self._defaults['PerformShortCableComp']['return']

    def niDMM_Read(self, vi, maximum_time, reading):  # noqa: N802
        if self._defaults['Read']['return'] != 0:
            return self._defaults['Read']['return']
        # reading
        if self._defaults['Read']['reading'] is None:
            raise MockFunctionCallError("niDMM_Read", param='reading')
        if reading is not None:
            reading.contents.value = self._defaults['Read']['reading']
        return self._defaults['Read']['return']

    def niDMM_ReadMultiPoint(self, vi, maximum_time, array_size, reading_array, actual_number_of_points):  # noqa: N802
        if self._defaults['ReadMultiPoint']['return'] != 0:
            return self._defaults['ReadMultiPoint']['return']
        # reading_array
        if self._defaults['ReadMultiPoint']['readingArray'] is None:
            raise MockFunctionCallError("niDMM_ReadMultiPoint", param='readingArray')
        test_value = self._defaults['ReadMultiPoint']['readingArray']
        try:
            reading_array_ref = reading_array.contents
        except AttributeError:
            reading_array_ref = reading_array
        assert len(reading_array_ref) >= len(test_value)
        for i in range(len(test_value)):
            reading_array_ref[i] = test_value[i]
        # actual_number_of_points
        if self._defaults['ReadMultiPoint']['actualNumberOfPoints'] is None:
            raise MockFunctionCallError("niDMM_ReadMultiPoint", param='actualNumberOfPoints')
        if actual_number_of_points is not None:
            actual_number_of_points.contents.value = self._defaults['ReadMultiPoint']['actualNumberOfPoints']
        return self._defaults['ReadMultiPoint']['return']

    def niDMM_ReadStatus(self, vi, acquisition_backlog, acquisition_status):  # noqa: N802
        if self._defaults['ReadStatus']['return'] != 0:
            return self._defaults['ReadStatus']['return']
        # acquisition_backlog
        if self._defaults['ReadStatus']['acquisitionBacklog'] is None:
            raise MockFunctionCallError("niDMM_ReadStatus", param='acquisitionBacklog')
        if acquisition_backlog is not None:
            acquisition_backlog.contents.value = self._defaults['ReadStatus']['acquisitionBacklog']
        # acquisition_status
        if self._defaults['ReadStatus']['acquisitionStatus'] is None:
            raise MockFunctionCallError("niDMM_ReadStatus", param='acquisitionStatus')
        if acquisition_status is not None:
            acquisition_status.contents.value = self._defaults['ReadStatus']['acquisitionStatus']
        return self._defaults['ReadStatus']['return']

    def niDMM_ReadWaveform(self, vi, maximum_time, array_size, waveform_array, actual_number_of_points):  # noqa: N802
        if self._defaults['ReadWaveform']['return'] != 0:
            return self._defaults['ReadWaveform']['return']
        # waveform_array
        if self._defaults['ReadWaveform']['waveformArray'] is None:
            raise MockFunctionCallError("niDMM_ReadWaveform", param='waveformArray')
        test_value = self._defaults['ReadWaveform']['waveformArray']
        try:
            waveform_array_ref = waveform_array.contents
        except AttributeError:
            waveform_array_ref = waveform_array
        assert len(waveform_array_ref) >= len(test_value)
        for i in range(len(test_value)):
            waveform_array_ref[i] = test_value[i]
        # actual_number_of_points
        if self._defaults['ReadWaveform']['actualNumberOfPoints'] is None:
            raise MockFunctionCallError("niDMM_ReadWaveform", param='actualNumberOfPoints')
        if actual_number_of_points is not None:
            actual_number_of_points.contents.value = self._defaults['ReadWaveform']['actualNumberOfPoints']
        return self._defaults['ReadWaveform']['return']

    def niDMM_ResetWithDefaults(self, vi):  # noqa: N802
        if self._defaults['ResetWithDefaults']['return'] != 0:
            return self._defaults['ResetWithDefaults']['return']
        return self._defaults['ResetWithDefaults']['return']

    def niDMM_SelfCal(self, vi):  # noqa: N802
        if self._defaults['SelfCal']['return'] != 0:
            return self._defaults['SelfCal']['return']
        return self._defaults['SelfCal']['return']

    def niDMM_SendSoftwareTrigger(self, vi):  # noqa: N802
        if self._defaults['SendSoftwareTrigger']['return'] != 0:
            return self._defaults['SendSoftwareTrigger']['return']
        return self._defaults['SendSoftwareTrigger']['return']

    def niDMM_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViBoolean']['return'] != 0:
            return self._defaults['SetAttributeViBoolean']['return']
        return self._defaults['SetAttributeViBoolean']['return']

    def niDMM_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViInt32']['return'] != 0:
            return self._defaults['SetAttributeViInt32']['return']
        return self._defaults['SetAttributeViInt32']['return']

    def niDMM_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViReal64']['return'] != 0:
            return self._defaults['SetAttributeViReal64']['return']
        return self._defaults['SetAttributeViReal64']['return']

    def niDMM_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViString']['return'] != 0:
            return self._defaults['SetAttributeViString']['return']
        return self._defaults['SetAttributeViString']['return']

    def niDMM_SetRuntimeEnvironment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        if self._defaults['SetRuntimeEnvironment']['return'] != 0:
            return self._defaults['SetRuntimeEnvironment']['return']
        return self._defaults['SetRuntimeEnvironment']['return']

    def niDMM_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['UnlockSession']['return'] != 0:
            return self._defaults['UnlockSession']['return']
        # caller_has_lock
        if self._defaults['UnlockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niDMM_UnlockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['UnlockSession']['callerHasLock']
        return self._defaults['UnlockSession']['return']

    def niDMM_close(self, vi):  # noqa: N802
        if self._defaults['close']['return'] != 0:
            return self._defaults['close']['return']
        return self._defaults['close']['return']

    def niDMM_error_message(self, vi, error_code, error_message):  # noqa: N802
        if self._defaults['error_message']['return'] != 0:
            return self._defaults['error_message']['return']
        # error_message
        if self._defaults['error_message']['errorMessage'] is None:
            raise MockFunctionCallError("niDMM_error_message", param='errorMessage')
        test_value = self._defaults['error_message']['errorMessage']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(error_message) >= len(test_value)
        for i in range(len(test_value)):
            error_message[i] = test_value[i]
        return self._defaults['error_message']['return']

    def niDMM_reset(self, vi):  # noqa: N802
        if self._defaults['reset']['return'] != 0:
            return self._defaults['reset']['return']
        return self._defaults['reset']['return']

    def niDMM_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        if self._defaults['self_test']['return'] != 0:
            return self._defaults['self_test']['return']
        # self_test_result
        if self._defaults['self_test']['selfTestResult'] is None:
            raise MockFunctionCallError("niDMM_self_test", param='selfTestResult')
        if self_test_result is not None:
            self_test_result.contents.value = self._defaults['self_test']['selfTestResult']
        # self_test_message
        if self._defaults['self_test']['selfTestMessage'] is None:
            raise MockFunctionCallError("niDMM_self_test", param='selfTestMessage')
        test_value = self._defaults['self_test']['selfTestMessage']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(self_test_message) >= len(test_value)
        for i in range(len(test_value)):
            self_test_message[i] = test_value[i]
        return self._defaults['self_test']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niDMM_Abort.side_effect = MockFunctionCallError("niDMM_Abort")
        mock_library.niDMM_Abort.return_value = 0
        mock_library.niDMM_ConfigureMeasurementAbsolute.side_effect = MockFunctionCallError("niDMM_ConfigureMeasurementAbsolute")
        mock_library.niDMM_ConfigureMeasurementAbsolute.return_value = 0
        mock_library.niDMM_ConfigureMeasurementDigits.side_effect = MockFunctionCallError("niDMM_ConfigureMeasurementDigits")
        mock_library.niDMM_ConfigureMeasurementDigits.return_value = 0
        mock_library.niDMM_ConfigureMultiPoint.side_effect = MockFunctionCallError("niDMM_ConfigureMultiPoint")
        mock_library.niDMM_ConfigureMultiPoint.return_value = 0
        mock_library.niDMM_ConfigureRTDCustom.side_effect = MockFunctionCallError("niDMM_ConfigureRTDCustom")
        mock_library.niDMM_ConfigureRTDCustom.return_value = 0
        mock_library.niDMM_ConfigureRTDType.side_effect = MockFunctionCallError("niDMM_ConfigureRTDType")
        mock_library.niDMM_ConfigureRTDType.return_value = 0
        mock_library.niDMM_ConfigureThermistorCustom.side_effect = MockFunctionCallError("niDMM_ConfigureThermistorCustom")
        mock_library.niDMM_ConfigureThermistorCustom.return_value = 0
        mock_library.niDMM_ConfigureThermocouple.side_effect = MockFunctionCallError("niDMM_ConfigureThermocouple")
        mock_library.niDMM_ConfigureThermocouple.return_value = 0
        mock_library.niDMM_ConfigureTrigger.side_effect = MockFunctionCallError("niDMM_ConfigureTrigger")
        mock_library.niDMM_ConfigureTrigger.return_value = 0
        mock_library.niDMM_ConfigureWaveformAcquisition.side_effect = MockFunctionCallError("niDMM_ConfigureWaveformAcquisition")
        mock_library.niDMM_ConfigureWaveformAcquisition.return_value = 0
        mock_library.niDMM_Disable.side_effect = MockFunctionCallError("niDMM_Disable")
        mock_library.niDMM_Disable.return_value = 0
        mock_library.niDMM_ExportAttributeConfigurationBuffer.side_effect = MockFunctionCallError("niDMM_ExportAttributeConfigurationBuffer")
        mock_library.niDMM_ExportAttributeConfigurationBuffer.return_value = 0
        mock_library.niDMM_ExportAttributeConfigurationFile.side_effect = MockFunctionCallError("niDMM_ExportAttributeConfigurationFile")
        mock_library.niDMM_ExportAttributeConfigurationFile.return_value = 0
        mock_library.niDMM_Fetch.side_effect = MockFunctionCallError("niDMM_Fetch")
        mock_library.niDMM_Fetch.return_value = 0
        mock_library.niDMM_FetchMultiPoint.side_effect = MockFunctionCallError("niDMM_FetchMultiPoint")
        mock_library.niDMM_FetchMultiPoint.return_value = 0
        mock_library.niDMM_FetchWaveform.side_effect = MockFunctionCallError("niDMM_FetchWaveform")
        mock_library.niDMM_FetchWaveform.return_value = 0
        mock_library.niDMM_GetAttributeViBoolean.side_effect = MockFunctionCallError("niDMM_GetAttributeViBoolean")
        mock_library.niDMM_GetAttributeViBoolean.return_value = 0
        mock_library.niDMM_GetAttributeViInt32.side_effect = MockFunctionCallError("niDMM_GetAttributeViInt32")
        mock_library.niDMM_GetAttributeViInt32.return_value = 0
        mock_library.niDMM_GetAttributeViReal64.side_effect = MockFunctionCallError("niDMM_GetAttributeViReal64")
        mock_library.niDMM_GetAttributeViReal64.return_value = 0
        mock_library.niDMM_GetAttributeViString.side_effect = MockFunctionCallError("niDMM_GetAttributeViString")
        mock_library.niDMM_GetAttributeViString.return_value = 0
        mock_library.niDMM_GetCalDateAndTime.side_effect = MockFunctionCallError("niDMM_GetCalDateAndTime")
        mock_library.niDMM_GetCalDateAndTime.return_value = 0
        mock_library.niDMM_GetDevTemp.side_effect = MockFunctionCallError("niDMM_GetDevTemp")
        mock_library.niDMM_GetDevTemp.return_value = 0
        mock_library.niDMM_GetError.side_effect = MockFunctionCallError("niDMM_GetError")
        mock_library.niDMM_GetError.return_value = 0
        mock_library.niDMM_GetExtCalRecommendedInterval.side_effect = MockFunctionCallError("niDMM_GetExtCalRecommendedInterval")
        mock_library.niDMM_GetExtCalRecommendedInterval.return_value = 0
        mock_library.niDMM_GetLastCalTemp.side_effect = MockFunctionCallError("niDMM_GetLastCalTemp")
        mock_library.niDMM_GetLastCalTemp.return_value = 0
        mock_library.niDMM_GetSelfCalSupported.side_effect = MockFunctionCallError("niDMM_GetSelfCalSupported")
        mock_library.niDMM_GetSelfCalSupported.return_value = 0
        mock_library.niDMM_ImportAttributeConfigurationBuffer.side_effect = MockFunctionCallError("niDMM_ImportAttributeConfigurationBuffer")
        mock_library.niDMM_ImportAttributeConfigurationBuffer.return_value = 0
        mock_library.niDMM_ImportAttributeConfigurationFile.side_effect = MockFunctionCallError("niDMM_ImportAttributeConfigurationFile")
        mock_library.niDMM_ImportAttributeConfigurationFile.return_value = 0
        mock_library.niDMM_InitWithOptions.side_effect = MockFunctionCallError("niDMM_InitWithOptions")
        mock_library.niDMM_InitWithOptions.return_value = 0
        mock_library.niDMM_Initiate.side_effect = MockFunctionCallError("niDMM_Initiate")
        mock_library.niDMM_Initiate.return_value = 0
        mock_library.niDMM_LockSession.side_effect = MockFunctionCallError("niDMM_LockSession")
        mock_library.niDMM_LockSession.return_value = 0
        mock_library.niDMM_PerformOpenCableComp.side_effect = MockFunctionCallError("niDMM_PerformOpenCableComp")
        mock_library.niDMM_PerformOpenCableComp.return_value = 0
        mock_library.niDMM_PerformShortCableComp.side_effect = MockFunctionCallError("niDMM_PerformShortCableComp")
        mock_library.niDMM_PerformShortCableComp.return_value = 0
        mock_library.niDMM_Read.side_effect = MockFunctionCallError("niDMM_Read")
        mock_library.niDMM_Read.return_value = 0
        mock_library.niDMM_ReadMultiPoint.side_effect = MockFunctionCallError("niDMM_ReadMultiPoint")
        mock_library.niDMM_ReadMultiPoint.return_value = 0
        mock_library.niDMM_ReadStatus.side_effect = MockFunctionCallError("niDMM_ReadStatus")
        mock_library.niDMM_ReadStatus.return_value = 0
        mock_library.niDMM_ReadWaveform.side_effect = MockFunctionCallError("niDMM_ReadWaveform")
        mock_library.niDMM_ReadWaveform.return_value = 0
        mock_library.niDMM_ResetWithDefaults.side_effect = MockFunctionCallError("niDMM_ResetWithDefaults")
        mock_library.niDMM_ResetWithDefaults.return_value = 0
        mock_library.niDMM_SelfCal.side_effect = MockFunctionCallError("niDMM_SelfCal")
        mock_library.niDMM_SelfCal.return_value = 0
        mock_library.niDMM_SendSoftwareTrigger.side_effect = MockFunctionCallError("niDMM_SendSoftwareTrigger")
        mock_library.niDMM_SendSoftwareTrigger.return_value = 0
        mock_library.niDMM_SetAttributeViBoolean.side_effect = MockFunctionCallError("niDMM_SetAttributeViBoolean")
        mock_library.niDMM_SetAttributeViBoolean.return_value = 0
        mock_library.niDMM_SetAttributeViInt32.side_effect = MockFunctionCallError("niDMM_SetAttributeViInt32")
        mock_library.niDMM_SetAttributeViInt32.return_value = 0
        mock_library.niDMM_SetAttributeViReal64.side_effect = MockFunctionCallError("niDMM_SetAttributeViReal64")
        mock_library.niDMM_SetAttributeViReal64.return_value = 0
        mock_library.niDMM_SetAttributeViString.side_effect = MockFunctionCallError("niDMM_SetAttributeViString")
        mock_library.niDMM_SetAttributeViString.return_value = 0
        mock_library.niDMM_SetRuntimeEnvironment.side_effect = MockFunctionCallError("niDMM_SetRuntimeEnvironment")
        mock_library.niDMM_SetRuntimeEnvironment.return_value = 0
        mock_library.niDMM_UnlockSession.side_effect = MockFunctionCallError("niDMM_UnlockSession")
        mock_library.niDMM_UnlockSession.return_value = 0
        mock_library.niDMM_close.side_effect = MockFunctionCallError("niDMM_close")
        mock_library.niDMM_close.return_value = 0
        mock_library.niDMM_error_message.side_effect = MockFunctionCallError("niDMM_error_message")
        mock_library.niDMM_error_message.return_value = 0
        mock_library.niDMM_reset.side_effect = MockFunctionCallError("niDMM_reset")
        mock_library.niDMM_reset.return_value = 0
        mock_library.niDMM_self_test.side_effect = MockFunctionCallError("niDMM_self_test")
        mock_library.niDMM_self_test.return_value = 0
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidmm/nidmm/VERSION sha256=5f2df6d86b73b1668c81b8c2b11cfa05ed74b6c42453c2bd4badfc93a2d47b0d bytes=13 -->
## FILE: generated/nidmm/nidmm/VERSION

- repository: `ni/nimi-python`
- source_path: `generated/nidmm/nidmm/VERSION`
- sha256: `5f2df6d86b73b1668c81b8c2b11cfa05ed74b6c42453c2bd4badfc93a2d47b0d`
- bytes: 13

````text
1.4.10.dev0
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidmm/README.rst sha256=b2b496a5236e2e1295cd16f4e4ee51c7800476dfc8fe2e6a717a5c18c7b48d51 bytes=6806 -->
## FILE: generated/nidmm/README.rst

- repository: `ni/nimi-python`
- source_path: `generated/nidmm/README.rst`
- sha256: `b2b496a5236e2e1295cd16f4e4ee51c7800476dfc8fe2e6a717a5c18c7b48d51`
- bytes: 6806

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

The **nidmm** module provides a Python API for NI-DMM. The code is maintained in the Open Source repository for `nimi-python <https://github.com/ni/nimi-python>`_.

Support Policy
--------------
**nidmm** supports all the Operating Systems supported by NI-DMM.

It follows `Python Software Foundation <https://devguide.python.org/#status-of-python-branches>`_ support policy for different versions of CPython.

NI created and supports **nidmm**.


NI-DMM Python API Status
------------------------

+-------------------------------+----------------------+
| NI-DMM (nidmm)                |                      |
+===============================+======================+
| Driver Version Tested Against | 2025 Q4              |
+-------------------------------+----------------------+
| PyPI Version                  | |nidmmLatestVersion| |
+-------------------------------+----------------------+
| Supported Python Version      | |nidmmPythonVersion| |
+-------------------------------+----------------------+
| Documentation                 | |nidmmDocs|          |
+-------------------------------+----------------------+
| Open Issues                   | |nidmmOpenIssues|    |
+-------------------------------+----------------------+
| Open Pull Requests            | |nidmmOpenPRs|       |
+-------------------------------+----------------------+


.. |nidmmLatestVersion| image:: http://img.shields.io/pypi/v/nidmm.svg
    :alt: Latest NI-DMM Version
    :target: http://pypi.python.org/pypi/nidmm


.. |nidmmPythonVersion| image:: http://img.shields.io/pypi/pyversions/nidmm.svg
    :alt: NI-DMM supported Python versions
    :target: http://pypi.python.org/pypi/nidmm


.. |nidmmDocs| image:: https://readthedocs.org/projects/nidmm/badge/?version=latest
    :alt: NI-DMM Python API Documentation Status
    :target: https://nidmm.readthedocs.io/en/latest


.. |nidmmOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/nidmm.svg
    :alt: Open Issues + Pull Requests for NI-DMM
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Anidmm


.. |nidmmOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/nidmm.svg
    :alt: Pull Requests for NI-DMM
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Anidmm



.. _nidmm_installation-section:

Installation
------------

As a prerequisite to using the **nidmm** module, you must install the NI-DMM runtime on your system. Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the driver runtime for your devices.

The nimi-python modules (i.e. for **NI-DMM**) can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install nidmm


Contributing
============

We welcome contributions! You can clone the project repository, build it, and install it by `following these instructions <https://github.com/ni/nimi-python/blob/master/CONTRIBUTING.md>`_.

Usage
------

The following is a basic example of using the **nidmm** module to open a session to a DMM and perform a 5.5 digits of resolution voltage measurement in the 10 V range.

.. code-block:: python

    import nidmm
    with nidmm.Session("Dev1") as session:
        session.configure_measurement_digits(nidmm.Function.DC_VOLTS, 10.0, 5.5)
        print("Measurement: " + str(session.read()))

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nidmm/examples>`_

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

Documentation is available `here <http://nidmm.readthedocs.io>`_.


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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidmm/setup.py sha256=9f03ca2bb0a9160e460fc3e75ffa9342016c55f5292e7c051340c98eb7ace9f9 bytes=1802 -->
## FILE: generated/nidmm/setup.py

- repository: `ni/nimi-python`
- source_path: `generated/nidmm/setup.py`
- sha256: `9f03ca2bb0a9160e460fc3e75ffa9342016c55f5292e7c051340c98eb7ace9f9`
- bytes: 1802

````python
#!/usr/bin/python
# This file was generated


from setuptools import setup


pypi_name = 'nidmm'


def read_contents(file_to_read):
    with open(file_to_read, 'r') as f:
        return f.read()


setup(
    name=pypi_name,
    zip_safe=True,
    version='1.4.10.dev0',
    description='NI-DMM Python API',
    long_description=read_contents('README.rst'),
    long_description_content_type='text/x-rst',
    author='NI',
    author_email="opensource@ni.com",
    url="https://github.com/ni/nimi-python",
    maintainer="NI",
    maintainer_email="opensource@ni.com",
    keywords=['nidmm'],
    license='MIT',
    include_package_data=True,
    packages=['nidmm'],
    python_requires='>=3.10',
    install_requires=[
        'hightime>=0.2.0',
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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidmm/tox-system_tests.ini sha256=aac77910392824ba76566c514da61663ac9aae00a718b99eb248c573cb2b25ae bytes=2627 -->
## FILE: generated/nidmm/tox-system_tests.ini

- repository: `ni/nimi-python`
- source_path: `generated/nidmm/tox-system_tests.ini`
- sha256: `aac77910392824ba76566c514da61663ac9aae00a718b99eb248c573cb2b25ae`
- bytes: 2627

````ini
# Tox (http://tox.testrun.org/) is a tool for running tests
# in multiple virtualenvs. This configuration file will run the
# test suite on all supported python versions. To use it, "pip install tox"
# and then run "tox -c tox-system_tests.ini" from the driver directory. (generated/nidmm)
[tox]
envlist = py{310,311,312,313,314}-nidmm-system_tests, py314-nidmm-coverage
skip_missing_interpreters=True
ignore_basepython_conflict=True
# We put the .tox directory outside of the Jenkins workspace so that it isn't wiped with the rest of the repo
toxworkdir = ../../../.tox

[testenv]
description =
    nidmm-system_tests: Run nidmm system tests (requires NI-DMM runtime to be installed)
    nidmm-coverage: Prepare coverage report for upload to codecov.io  # upload handled by GitHub Actions

changedir =
    nidmm-system_tests: .
    nidmm-coverage: .

commands =
    # --disable-pip-version-check prevents pip from telling us we need to upgrade pip, since we are doing that now
    nidmm-system_tests: python -m pip install --disable-pip-version-check --upgrade pip
    nidmm-system_tests: python -c "import nidmm; nidmm.print_diagnostic_information()"
    nidmm-system_tests: coverage run --rcfile=../../tools/coverage_system_tests.rc --source nidmm --parallel-mode -m pytest ../../src/nidmm/examples --junitxml=../junit/junit-nidmm-{envname}-examples-{env:BITNESS:64}.xml {posargs}
    nidmm-system_tests: coverage run --rcfile=../../tools/coverage_system_tests.rc --source nidmm --parallel-mode -m pytest ../../src/nidmm/system_tests -c tox-system_tests.ini --junitxml=../junit/junit-nidmm-{envname}-{env:BITNESS:64}.xml --durations=5 {posargs}

    nidmm-coverage: coverage combine --rcfile=../../tools/coverage_system_tests.rc ./
    # Create the report to upload
    nidmm-coverage: coverage xml -i --rcfile=../../tools/coverage_system_tests.rc
    # Display the coverage results
    nidmm-coverage: coverage report --rcfile=../../tools/coverage_system_tests.rc

deps =
    nidmm-system_tests: pytest
    nidmm-system_tests: coverage
    nidmm-system_tests: numpy
    nidmm-system_tests: hightime
    nidmm-system_tests: fasteners
    nidmm-system_tests: pytest-json
    nidmm-system_tests: .[grpc]

    nidmm-coverage: coverage

depends =
    nidmm-coverage: py{310,311,312,313,314}-nidmm-system_tests

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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/nifake/__init__.py sha256=392bd9d308e9b7d385a7861971057aa352072d37d0ca795035c505a64c2edc53 bytes=3763 -->
## FILE: generated/nifake/nifake/__init__.py

- repository: `ni/nimi-python`
- source_path: `generated/nifake/nifake/__init__.py`
- sha256: `392bd9d308e9b7d385a7861971057aa352072d37d0ca795035c505a64c2edc53`
- bytes: 3763

````python
# -*- coding: utf-8 -*-
# This file was generated


__version__ = '1.4.10.dev0'

from nifake.enums import *  # noqa: F403,F401,H303
from nifake.errors import DriverWarning  # noqa: F401
from nifake.errors import Error  # noqa: F401
from nifake.grpc_session_options import *  # noqa: F403,F401,H303
from nifake.session import Session  # noqa: F401

from nifake.custom_struct import CustomStruct  # noqa: F401

from nifake.custom_struct import struct_CustomStruct  # noqa: F401

from nifake.custom_struct_typedef import CustomStructTypedef  # noqa: F401

from nifake.custom_struct_typedef import struct_CustomStructTypedef  # noqa: F401

from nifake.custom_struct_nested_typedef import CustomStructNestedTypedef  # noqa: F401

from nifake.custom_struct_nested_typedef import struct_CustomStructNestedTypedef  # noqa: F401


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
            driver_version_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\National Instruments\NI-FAKE\CurrentVersion")
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
    info['driver']['name'] = "NI-FAKE"
    info['driver']['version'] = driver_version
    info['module']['name'] = 'nifake'
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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/nifake/_attributes.py sha256=cf648fe3e0db000da7e77ff718b0d2291852b5b7ffdda578ff604fce12806339 bytes=6175 -->
## FILE: generated/nifake/nifake/_attributes.py

- repository: `ni/nimi-python`
- source_path: `generated/nifake/nifake/_attributes.py`
- sha256: `cf648fe3e0db000da7e77ff718b0d2291852b5b7ffdda578ff604fce12806339`
- bytes: 6175

````python
# -*- coding: utf-8 -*-
# This file was generated
import nifake._converters as _converters
import nifake.errors as errors

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
    '''Class for attributes that use enums internally but are exposed in the nifake Python module as something else, thus need conversion.'''

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
        from nifake.session import SessionReference
        return SessionReference(session._get_attribute_vi_session(self._attribute_id))

    def __set__(self, session, value):
        session._set_attribute_vi_session(self._attribute_id, _converters.convert_to_nitclk_session_number(value))
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/nifake/_complextype.py sha256=34dd0419f38f83198ae02f709908816db90dca5f5ed8432b7293ea8f94868764 bytes=456 -->
## FILE: generated/nifake/nifake/_complextype.py

- repository: `ni/nimi-python`
- source_path: `generated/nifake/nifake/_complextype.py`
- sha256: `34dd0419f38f83198ae02f709908816db90dca5f5ed8432b7293ea8f94868764`
- bytes: 456

````python
# -*- coding: utf-8 -*-
# This file was generated
import ctypes
import nifake._visatype as _visatype


class NIComplexNumber(ctypes.Structure):
    _fields_ = [("real", _visatype.ViReal64), ("imag", _visatype.ViReal64)]


class NIComplexNumberF32(ctypes.Structure):
    _fields_ = [("real", _visatype.ViReal32), ("imag", _visatype.ViReal32)]


class NIComplexI16(ctypes.Structure):
    _fields_ = [("real", _visatype.ViInt16), ("imag", _visatype.ViInt16)]
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/nifake/_converters.py sha256=785a37c9a27ab74f87f6c505140512efdea5fdf482c97fabcae2dd1a4d1655f2 bytes=15301 -->
## FILE: generated/nifake/nifake/_converters.py

- repository: `ni/nimi-python`
- source_path: `generated/nifake/nifake/_converters.py`
- sha256: `785a37c9a27ab74f87f6c505140512efdea5fdf482c97fabcae2dd1a4d1655f2`
- bytes: 15301

````python
# -*- coding: utf-8 -*-
# This file was generated
import nifake._visatype as _visatype
import nifake.enums as enums
import nifake.errors as errors

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


# nifake specific converter(s) - used only for testing
def convert_double_each_element(numbers):
    return [x * 2 for x in numbers]


def convert_from_enum_with_converter_enum(value):
    return {
        enums.EnumWithConverter.RED: True,
        enums.EnumWithConverter.BLUE: False,
        enums.EnumWithConverter.YELLOW: 'yellow',
        enums.EnumWithConverter.BLACK: 42,
    }[value]


def convert_to_enum_with_converter_enum(value):
    return {
        True: enums.EnumWithConverter.RED,
        False: enums.EnumWithConverter.BLUE,
        'yellow': enums.EnumWithConverter.YELLOW,
        42: enums.EnumWithConverter.BLACK,
    }[value]
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/nifake/_grpc_stub_interpreter.py sha256=0232162691643e03976a4e61092236fe91947686d056ce7ec7b3a763b84c53b6 bytes=25380 -->
## FILE: generated/nifake/nifake/_grpc_stub_interpreter.py

- repository: `ni/nimi-python`
- source_path: `generated/nifake/nifake/_grpc_stub_interpreter.py`
- sha256: `0232162691643e03976a4e61092236fe91947686d056ce7ec7b3a763b84c53b6`
- bytes: 25380

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
from . import nidevice_pb2 as grpc_complex_types  # noqa: F401
from . import nifake_pb2 as grpc_types
from . import nifake_pb2_grpc as nifake_grpc

from . import custom_struct as custom_struct  # noqa: F401

from . import custom_struct_typedef as custom_struct_typedef  # noqa: F401

from . import custom_struct_nested_typedef as custom_struct_nested_typedef  # noqa: F401


class GrpcStubInterpreter(object):
    '''Interpreter for interacting with a gRPC Stub class'''

    def __init__(self, grpc_options):
        self._grpc_options = grpc_options
        self._lock = threading.RLock()
        self._client = nifake_grpc.NiFakeStub(grpc_options.grpc_channel)
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

    def accept_list_of_durations_in_seconds(self, delays):  # noqa: N802
        self._invoke(
            self._client.AcceptListOfDurationsInSeconds,
            grpc_types.AcceptListOfDurationsInSecondsRequest(vi=self._vi, delays=delays),
        )

    def bool_array_output_function(self, number_of_elements):  # noqa: N802
        response = self._invoke(
            self._client.BoolArrayOutputFunction,
            grpc_types.BoolArrayOutputFunctionRequest(vi=self._vi, number_of_elements=number_of_elements),
        )
        return response.an_array

    def configure_abc(self):  # noqa: N802
        self._invoke(
            self._client.ConfigureAbc,
            grpc_types.ConfigureAbcRequest(vi=self._vi),
        )

    def custom_nested_struct_roundtrip(self, nested_custom_type_in):  # noqa: N802
        response = self._invoke(
            self._client.CustomNestedStructRoundtrip,
            grpc_types.CustomNestedStructRoundtripRequest(nested_custom_type_in=nested_custom_type_in._create_copy(grpc_types.CustomStructNestedTypedef)),
        )
        return custom_struct_nested_typedef.CustomStructNestedTypedef(response.nested_custom_type_out)

    def double_all_the_nums(self, numbers):  # noqa: N802
        self._invoke(
            self._client.DoubleAllTheNums,
            grpc_types.DoubleAllTheNumsRequest(vi=self._vi, numbers=numbers),
        )

    def enum_array_output_function(self, number_of_elements):  # noqa: N802
        response = self._invoke(
            self._client.EnumArrayOutputFunction,
            grpc_types.EnumArrayOutputFunctionRequest(vi=self._vi, number_of_elements=number_of_elements),
        )
        return [enums.Turtle(x) for x in response.an_array_raw]

    def enum_input_function_with_defaults(self, a_turtle):  # noqa: N802
        self._invoke(
            self._client.EnumInputFunctionWithDefaults,
            grpc_types.EnumInputFunctionWithDefaultsRequest(vi=self._vi, a_turtle_raw=a_turtle.value),
        )

    def export_attribute_configuration_buffer(self):  # noqa: N802
        response = self._invoke(
            self._client.ExportAttributeConfigurationBuffer,
            grpc_types.ExportAttributeConfigurationBufferRequest(vi=self._vi),
        )
        return response.configuration

    def fetch_waveform(self, number_of_samples):  # noqa: N802
        response = self._invoke(
            self._client.FetchWaveform,
            grpc_types.FetchWaveformRequest(vi=self._vi, number_of_samples=number_of_samples),
        )
        return response.waveform_data

    def fetch_waveform_into(self, number_of_samples):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')

    def function_with_3d_numpy_array_of_numpy_complex128_input_parameter(self, multidimensional_array):  # noqa: N802
        # Use ravel() so that gRPC always receives a flat numpy array, regardless of input dimensions.
        multidimensional_array_list = [
            grpc_complex_types.NIComplexNumber(real=val.real, imaginary=val.imag)
            for val in multidimensional_array.ravel()
        ]
        self._invoke(
            self._client.FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter,
            grpc_types.FunctionWith3dNumpyArrayOfNumpyComplex128InputParameterRequest(vi=self._vi, multidimensional_array=multidimensional_array_list),
        )

    def function_with_intflag_parameter(self, flag):  # noqa: N802
        self._invoke(
            self._client.FunctionWithIntflagParameter,
            grpc_types.FunctionWithIntflagParameterRequest(vi=self._vi, flag=flag.value),
        )

    def function_with_repeated_capability_type(self, site_list):  # noqa: N802
        raise NotImplementedError('function_with_repeated_capability_type is not supported over gRPC')

    def get_a_boolean(self):  # noqa: N802
        response = self._invoke(
            self._client.GetABoolean,
            grpc_types.GetABooleanRequest(vi=self._vi),
        )
        return response.a_boolean

    def get_a_number(self):  # noqa: N802
        response = self._invoke(
            self._client.GetANumber,
            grpc_types.GetANumberRequest(vi=self._vi),
        )
        return response.a_number

    def get_a_string_of_fixed_maximum_size(self):  # noqa: N802
        response = self._invoke(
            self._client.GetAStringOfFixedMaximumSize,
            grpc_types.GetAStringOfFixedMaximumSizeRequest(vi=self._vi),
        )
        return response.a_string

    def get_a_string_using_python_code(self, a_number):  # noqa: N802
        raise NotImplementedError('get_a_string_using_python_code is not supported over gRPC')

    def get_an_ivi_dance_char_array(self):  # noqa: N802
        response = self._invoke(
            self._client.GetAnIviDanceCharArray,
            grpc_types.GetAnIviDanceCharArrayRequest(vi=self._vi),
        )
        return response.char_array

    def get_an_ivi_dance_with_a_twist_string(self):  # noqa: N802
        response = self._invoke(
            self._client.GetAnIviDanceWithATwistString,
            grpc_types.GetAnIviDanceWithATwistStringRequest(vi=self._vi),
        )
        return response.a_string

    def get_array_for_python_code_custom_type(self):  # noqa: N802
        raise NotImplementedError('get_array_for_python_code_custom_type is not supported over gRPC')

    def get_array_for_python_code_double(self):  # noqa: N802
        raise NotImplementedError('get_array_for_python_code_double is not supported over gRPC')

    def get_array_size_for_python_code(self):  # noqa: N802
        raise NotImplementedError('get_array_size_for_python_code is not supported over gRPC')

    def get_array_using_ivi_dance(self):  # noqa: N802
        response = self._invoke(
            self._client.GetArrayUsingIviDance,
            grpc_types.GetArrayUsingIviDanceRequest(vi=self._vi),
        )
        return response.array_out

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

    def get_attribute_vi_int64(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViInt64,
            grpc_types.GetAttributeViInt64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
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

    def get_cal_interval(self):  # noqa: N802
        response = self._invoke(
            self._client.GetCalInterval,
            grpc_types.GetCalIntervalRequest(vi=self._vi),
        )
        return response.months

    def get_channel_names(self, indices):  # noqa: N802
        raise NotImplementedError('get_channel_names is not supported over gRPC')

    def get_custom_type(self):  # noqa: N802
        response = self._invoke(
            self._client.GetCustomType,
            grpc_types.GetCustomTypeRequest(vi=self._vi),
        )
        return custom_struct.CustomStruct(response.cs)

    def get_custom_type_array(self, number_of_elements):  # noqa: N802
        response = self._invoke(
            self._client.GetCustomTypeArray,
            grpc_types.GetCustomTypeArrayRequest(vi=self._vi, number_of_elements=number_of_elements),
        )
        return [custom_struct.CustomStruct(x) for x in response.cs]

    def get_custom_type_typedef(self):  # noqa: N802
        raise NotImplementedError('get_custom_type_typedef is not supported over gRPC')

    def get_enum_value(self):  # noqa: N802
        response = self._invoke(
            self._client.GetEnumValue,
            grpc_types.GetEnumValueRequest(vi=self._vi),
        )
        return response.a_quantity, enums.Turtle(response.a_turtle_raw)

    def get_error(self):  # noqa: N802
        response = self._invoke(
            self._client.GetError,
            grpc_types.GetErrorRequest(vi=self._vi),
        )
        return response.error_code, response.description

    def get_parameter_with_overridden_grpc_name(self, enum_parameter):  # noqa: N802
        response = self._invoke(
            self._client.GetParameterWithOverriddenGrpcName,
            grpc_types.GetParameterWithOverriddenGrpcNameRequest(vi=self._vi, enum_parameter_raw=enum_parameter.value),
        )
        return response.overridden_parameter

    def import_attribute_configuration_buffer(self, configuration):  # noqa: N802
        self._invoke(
            self._client.ImportAttributeConfigurationBuffer,
            grpc_types.ImportAttributeConfigurationBufferRequest(vi=self._vi, configuration=configuration),
        )

    def import_attribute_configuration_buffer_ex(self, configuration):  # noqa: N802
        self._invoke(
            self._client.ImportAttributeConfigurationBufferEx,
            grpc_types.ImportAttributeConfigurationBufferExRequest(vi=self._vi, configuration=configuration),
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
        raise NotImplementedError('initiate is not supported over gRPC')

    def lock(self):  # noqa: N802
        self._lock.acquire()

    def method_using_whole_and_fractional_numbers(self):  # noqa: N802
        response = self._invoke(
            self._client.MethodUsingWholeAndFractionalNumbers,
            grpc_types.MethodUsingWholeAndFractionalNumbersRequest(),
        )
        return response.whole_number_raw, response.fractional_number_raw

    def method_with_grpc_only_param(self, simple_param):  # noqa: N802
        self._invoke(
            self._client.MethodWithGrpcOnlyParam,
            grpc_types.MethodWithGrpcOnlyParamRequest(simple_param=simple_param),
        )

    def method_with_proto_only_parameter(self, attribute_value):  # noqa: N802
        self._invoke(
            self._client.MethodWithProtoOnlyParameter,
            grpc_types.MethodWithProtoOnlyParameterRequest(attribute_value=attribute_value),
        )

    def mixed_ivi_dance_and_len_mechanism(self, input_values):  # noqa: N802
        response = self._invoke(
            self._client.MixedIviDanceAndLenMechanism,
            grpc_types.MixedIviDanceAndLenMechanismRequest(vi=self._vi, input_values=input_values),
        )
        return response.output_array

    def multiple_array_types(self, output_array_size, input_array_of_floats, input_array_of_integers):  # noqa: N802
        response = self._invoke(
            self._client.MultipleArrayTypes,
            grpc_types.MultipleArrayTypesRequest(vi=self._vi, output_array_size=output_array_size, input_array_of_floats=input_array_of_floats, input_array_of_integers=input_array_of_integers),
        )
        return response.output_array, response.output_array_of_fixed_length

    def multiple_arrays_different_size(self, values_array, data_array):  # noqa: N802
        self._invoke(
            self._client.MultipleArraysDifferentSize,
            grpc_types.MultipleArraysDifferentSizeRequest(vi=self._vi, values_array=values_array, data_array=data_array),
        )

    def multiple_arrays_same_size(self, values1, values2, values3, values4):  # noqa: N802
        self._invoke(
            self._client.MultipleArraysSameSize,
            grpc_types.MultipleArraysSameSizeRequest(vi=self._vi, values1=values1, values2=values2, values3=values3, values4=values4),
        )

    def one_input_function(self, a_number):  # noqa: N802
        self._invoke(
            self._client.OneInputFunction,
            grpc_types.OneInputFunctionRequest(vi=self._vi, a_number=a_number),
        )

    def parameters_are_multiple_types(self, a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, a_string):  # noqa: N802
        self._invoke(
            self._client.ParametersAreMultipleTypes,
            grpc_types.ParametersAreMultipleTypesRequest(vi=self._vi, a_boolean=a_boolean, an_int32=an_int32, an_int64=an_int64, an_int_enum_raw=an_int_enum.value, a_float=a_float, a_float_enum_raw=a_float_enum.value, a_string=a_string),
        )

    def simple_function(self):  # noqa: N802
        self._invoke(
            self._client.PoorlyNamedSimpleFunction,
            grpc_types.PoorlyNamedSimpleFunctionRequest(vi=self._vi),
        )

    def read(self, maximum_time):  # noqa: N802
        response = self._invoke(
            self._client.Read,
            grpc_types.ReadRequest(vi=self._vi, maximum_time=maximum_time),
        )
        return response.reading

    def read_from_channel(self, channel_name, maximum_time):  # noqa: N802
        response = self._invoke(
            self._client.ReadFromChannel,
            grpc_types.ReadFromChannelRequest(vi=self._vi, channel_name=channel_name, maximum_time=maximum_time),
        )
        return response.reading

    def return_a_number_and_a_string(self):  # noqa: N802
        response = self._invoke(
            self._client.ReturnANumberAndAString,
            grpc_types.ReturnANumberAndAStringRequest(vi=self._vi),
        )
        return response.a_number, response.a_string

    def return_duration_in_seconds(self):  # noqa: N802
        response = self._invoke(
            self._client.ReturnDurationInSeconds,
            grpc_types.ReturnDurationInSecondsRequest(vi=self._vi),
        )
        return response.timedelta

    def return_list_of_durations_in_seconds(self, number_of_elements):  # noqa: N802
        response = self._invoke(
            self._client.ReturnListOfDurationsInSeconds,
            grpc_types.ReturnListOfDurationsInSecondsRequest(vi=self._vi, number_of_elements=number_of_elements),
        )
        return response.timedeltas

    def return_multiple_types(self, array_size):  # noqa: N802
        response = self._invoke(
            self._client.ReturnMultipleTypes,
            grpc_types.ReturnMultipleTypesRequest(vi=self._vi, array_size=array_size),
        )
        return response.a_boolean, response.an_int32, response.an_int64, enums.Turtle(response.an_int_enum_raw), response.a_float, enums.FloatEnum(response.a_float_enum_raw), response.an_array, response.a_string

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

    def set_attribute_vi_int64(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViInt64,
            grpc_types.SetAttributeViInt64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, attribute_value_raw=attribute_value),
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

    def set_custom_type(self, cs):  # noqa: N802
        self._invoke(
            self._client.SetCustomType,
            grpc_types.SetCustomTypeRequest(vi=self._vi, cs=cs._create_copy(grpc_types.FakeCustomStruct)),
        )

    def set_custom_type_array(self, cs):  # noqa: N802
        self._invoke(
            self._client.SetCustomTypeArray,
            grpc_types.SetCustomTypeArrayRequest(vi=self._vi, cs=cs and [x._create_copy(grpc_types.FakeCustomStruct) for x in cs]),
        )

    def set_runtime_environment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        raise NotImplementedError('set_runtime_environment is not supported over gRPC')

    def string_valued_enum_input_function_with_defaults(self, a_mobile_os_name):  # noqa: N802
        self._invoke(
            self._client.StringValuedEnumInputFunctionWithDefaults,
            grpc_types.StringValuedEnumInputFunctionWithDefaultsRequest(vi=self._vi, a_mobile_os_name_raw=a_mobile_os_name.value),
        )

    def two_input_function(self, a_number, a_string):  # noqa: N802
        self._invoke(
            self._client.TwoInputFunction,
            grpc_types.TwoInputFunctionRequest(vi=self._vi, a_number=a_number, a_string=a_string),
        )

    def unlock(self):  # noqa: N802
        self._lock.release()

    def use64_bit_number(self, input):  # noqa: N802
        response = self._invoke(
            self._client.Use64BitNumber,
            grpc_types.Use64BitNumberRequest(vi=self._vi, input=input),
        )
        return response.output

    def write_waveform(self, waveform):  # noqa: N802
        self._invoke(
            self._client.WriteWaveform,
            grpc_types.WriteWaveformRequest(vi=self._vi, waveform=waveform),
        )

    def write_waveform_numpy(self, waveform):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')

    def write_waveform_numpy_complex128(self, waveform_data_array):  # noqa: N802
        # Use ravel() so that gRPC always receives a flat numpy array, regardless of input dimensions.
        waveform_data_array_list = [
            grpc_complex_types.NIComplexNumber(real=val.real, imaginary=val.imag)
            for val in waveform_data_array.ravel()
        ]
        self._invoke(
            self._client.WriteWaveformNumpyComplex128,
            grpc_types.WriteWaveformNumpyComplex128Request(vi=self._vi, waveform_data_array=waveform_data_array_list),
        )

    def write_waveform_numpy_complex64(self, waveform_data_array):  # noqa: N802
        # Use ravel() so that gRPC always receives a flat numpy array, regardless of input dimensions.
        waveform_data_array_list = [
            grpc_complex_types.NIComplexNumberF32(real=val.real, imaginary=val.imag)
            for val in waveform_data_array.ravel()
        ]
        self._invoke(
            self._client.WriteWaveformNumpyComplex64,
            grpc_types.WriteWaveformNumpyComplex64Request(vi=self._vi, waveform_data_array=waveform_data_array_list),
        )

    def write_waveform_numpy_complex_interleaved_i16(self, waveform_data_array):  # noqa: N802
        # Use ravel() so that gRPC always receives a flat numpy array, regardless of input dimensions.
        arr = waveform_data_array.ravel()
        if arr.size % 2 != 0:
            raise ValueError("Interleaved int16 array must have even length (real/imag pairs)")
        arr_pairs = arr.reshape(-1, 2)
        waveform_data_array_list = [
            grpc_complex_types.NIComplexI16(real=int(pair[0]), imaginary=int(pair[1]))
            for pair in arr_pairs
        ]
        self._invoke(
            self._client.WriteWaveformNumpyComplexInterleavedI16,
            grpc_types.WriteWaveformNumpyComplexInterleavedI16Request(vi=self._vi, waveform_data_array=waveform_data_array_list),
        )

    def close(self):  # noqa: N802
        self._invoke(
            self._client.Close,
            grpc_types.CloseRequest(vi=self._vi),
        )

    def error_message(self, error_code):  # noqa: N802
        response = self._invoke(
            self._client.ErrorMessage,
            grpc_types.ErrorMessageRequest(vi=self._vi, error_code=error_code),
        )
        return response.error_message

    def self_test(self):  # noqa: N802
        raise NotImplementedError('self_test is not supported over gRPC')
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/nifake/_library.py sha256=6594441d5d58410b67b128a2cda8132dd641e64a4f827bcb3720d9bd303c6a79 bytes=53333 -->
## FILE: generated/nifake/nifake/_library.py

- repository: `ni/nimi-python`
- source_path: `generated/nifake/nifake/_library.py`
- sha256: `6594441d5d58410b67b128a2cda8132dd641e64a4f827bcb3720d9bd303c6a79`
- bytes: 53333

````python
# -*- coding: utf-8 -*-
# This file was generated

import ctypes
import nifake.errors as errors
import threading

from nifake._complextype import *  # noqa: F403
from nifake._visatype import *  # noqa: F403,H303

import nifake.custom_struct as custom_struct  # noqa: F401

import nifake.custom_struct_typedef as custom_struct_typedef  # noqa: F401

import nifake.custom_struct_nested_typedef as custom_struct_nested_typedef  # noqa: F401


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, ctypes_library):
        self._func_lock = threading.Lock()
        self._library = ctypes_library
        # We cache the cfunc object from the ctypes.CDLL object
        self.niFake_Abort_cfunc = None
        self.niFake_AcceptListOfDurationsInSeconds_cfunc = None
        self.niFake_BoolArrayOutputFunction_cfunc = None
        self.niFake_ConfigureABC_cfunc = None
        self.niFake_CustomNestedStructRoundtrip_cfunc = None
        self.niFake_DoubleAllTheNums_cfunc = None
        self.niFake_EnumArrayOutputFunction_cfunc = None
        self.niFake_EnumInputFunctionWithDefaults_cfunc = None
        self.niFake_ExportAttributeConfigurationBuffer_cfunc = None
        self.niFake_FetchWaveform_cfunc = None
        self.niFake_FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter_cfunc = None
        self.niFake_FunctionWithIntflagParameter_cfunc = None
        self.niFake_FunctionWithRepeatedCapabilityType_cfunc = None
        self.niFake_GetABoolean_cfunc = None
        self.niFake_GetANumber_cfunc = None
        self.niFake_GetAStringOfFixedMaximumSize_cfunc = None
        self.niFake_GetAStringUsingPythonCode_cfunc = None
        self.niFake_GetAnIviDanceCharArray_cfunc = None
        self.niFake_GetAnIviDanceWithATwistString_cfunc = None
        self.niFake_GetArrayForPythonCodeCustomType_cfunc = None
        self.niFake_GetArrayForPythonCodeDouble_cfunc = None
        self.niFake_GetArraySizeForPythonCode_cfunc = None
        self.niFake_GetArrayUsingIviDance_cfunc = None
        self.niFake_GetAttributeViBoolean_cfunc = None
        self.niFake_GetAttributeViInt32_cfunc = None
        self.niFake_GetAttributeViInt64_cfunc = None
        self.niFake_GetAttributeViReal64_cfunc = None
        self.niFake_GetAttributeViString_cfunc = None
        self.niFake_GetCalDateAndTime_cfunc = None
        self.niFake_GetCalInterval_cfunc = None
        self.niFake_GetChannelNames_cfunc = None
        self.niFake_GetCustomType_cfunc = None
        self.niFake_GetCustomTypeArray_cfunc = None
        self.niFake_GetCustomTypeTypedef_cfunc = None
        self.niFake_GetEnumValue_cfunc = None
        self.niFake_GetError_cfunc = None
        self.niFake_GetParameterWithOverriddenGrpcName_cfunc = None
        self.niFake_ImportAttributeConfigurationBuffer_cfunc = None
        self.niFake_ImportAttributeConfigurationBufferEx_cfunc = None
        self.niFake_InitWithOptions_cfunc = None
        self.niFake_Initiate_cfunc = None
        self.niFake_LockSession_cfunc = None
        self.niFake_MethodUsingWholeAndFractionalNumbers_cfunc = None
        self.niFake_MethodWithGrpcOnlyParam_cfunc = None
        self.niFake_MethodWithProtoOnlyParameter_cfunc = None
        self.niFake_MixedIviDanceAndLenMechanism_cfunc = None
        self.niFake_MultipleArrayTypes_cfunc = None
        self.niFake_MultipleArraysDifferentSize_cfunc = None
        self.niFake_MultipleArraysSameSize_cfunc = None
        self.niFake_OneInputFunction_cfunc = None
        self.niFake_ParametersAreMultipleTypes_cfunc = None
        self.niFake_PoorlyNamedSimpleFunction_cfunc = None
        self.niFake_Read_cfunc = None
        self.niFake_ReadFromChannel_cfunc = None
        self.niFake_ReturnANumberAndAString_cfunc = None
        self.niFake_ReturnDurationInSeconds_cfunc = None
        self.niFake_ReturnListOfDurationsInSeconds_cfunc = None
        self.niFake_ReturnMultipleTypes_cfunc = None
        self.niFake_SetAttributeViBoolean_cfunc = None
        self.niFake_SetAttributeViInt32_cfunc = None
        self.niFake_SetAttributeViInt64_cfunc = None
        self.niFake_SetAttributeViReal64_cfunc = None
        self.niFake_SetAttributeViString_cfunc = None
        self.niFake_SetCustomType_cfunc = None
        self.niFake_SetCustomTypeArray_cfunc = None
        self.niFake_SetRuntimeEnvironment_cfunc = None
        self.niFake_StringValuedEnumInputFunctionWithDefaults_cfunc = None
        self.niFake_TwoInputFunction_cfunc = None
        self.niFake_UnlockSession_cfunc = None
        self.niFake_Use64BitNumber_cfunc = None
        self.niFake_WriteWaveform_cfunc = None
        self.niFake_WriteWaveformNumpyComplex128_cfunc = None
        self.niFake_WriteWaveformNumpyComplex64_cfunc = None
        self.niFake_WriteWaveformNumpyComplexInterleavedI16_cfunc = None
        self.niFake_close_cfunc = None
        self.niFake_error_message_cfunc = None
        self.niFake_self_test_cfunc = None

    def _get_library_function(self, name):
        try:
            function = getattr(self._library, name)
        except AttributeError as e:
            raise errors.DriverTooOldError() from e
        return function

    def niFake_Abort(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFake_Abort_cfunc is None:
                self.niFake_Abort_cfunc = self._get_library_function('niFake_Abort')
                self.niFake_Abort_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFake_Abort_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_Abort_cfunc(vi)

    def niFake_AcceptListOfDurationsInSeconds(self, vi, count, delays):  # noqa: N802
        with self._func_lock:
            if self.niFake_AcceptListOfDurationsInSeconds_cfunc is None:
                self.niFake_AcceptListOfDurationsInSeconds_cfunc = self._get_library_function('niFake_AcceptListOfDurationsInSeconds')
                self.niFake_AcceptListOfDurationsInSeconds_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_AcceptListOfDurationsInSeconds_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_AcceptListOfDurationsInSeconds_cfunc(vi, count, delays)

    def niFake_BoolArrayOutputFunction(self, vi, number_of_elements, an_array):  # noqa: N802
        with self._func_lock:
            if self.niFake_BoolArrayOutputFunction_cfunc is None:
                self.niFake_BoolArrayOutputFunction_cfunc = self._get_library_function('niFake_BoolArrayOutputFunction')
                self.niFake_BoolArrayOutputFunction_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFake_BoolArrayOutputFunction_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_BoolArrayOutputFunction_cfunc(vi, number_of_elements, an_array)

    def niFake_ConfigureABC(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFake_ConfigureABC_cfunc is None:
                self.niFake_ConfigureABC_cfunc = self._get_library_function('niFake_ConfigureABC')
                self.niFake_ConfigureABC_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFake_ConfigureABC_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_ConfigureABC_cfunc(vi)

    def niFake_CustomNestedStructRoundtrip(self, nested_custom_type_in, nested_custom_type_out):  # noqa: N802
        with self._func_lock:
            if self.niFake_CustomNestedStructRoundtrip_cfunc is None:
                self.niFake_CustomNestedStructRoundtrip_cfunc = self._get_library_function('niFake_CustomNestedStructRoundtrip')
                self.niFake_CustomNestedStructRoundtrip_cfunc.argtypes = [custom_struct_nested_typedef.struct_CustomStructNestedTypedef, ctypes.POINTER(custom_struct_nested_typedef.struct_CustomStructNestedTypedef)]  # noqa: F405
                self.niFake_CustomNestedStructRoundtrip_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_CustomNestedStructRoundtrip_cfunc(nested_custom_type_in, nested_custom_type_out)

    def niFake_DoubleAllTheNums(self, vi, number_count, numbers):  # noqa: N802
        with self._func_lock:
            if self.niFake_DoubleAllTheNums_cfunc is None:
                self.niFake_DoubleAllTheNums_cfunc = self._get_library_function('niFake_DoubleAllTheNums')
                self.niFake_DoubleAllTheNums_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_DoubleAllTheNums_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_DoubleAllTheNums_cfunc(vi, number_count, numbers)

    def niFake_EnumArrayOutputFunction(self, vi, number_of_elements, an_array):  # noqa: N802
        with self._func_lock:
            if self.niFake_EnumArrayOutputFunction_cfunc is None:
                self.niFake_EnumArrayOutputFunction_cfunc = self._get_library_function('niFake_EnumArrayOutputFunction')
                self.niFake_EnumArrayOutputFunction_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt16)]  # noqa: F405
                self.niFake_EnumArrayOutputFunction_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_EnumArrayOutputFunction_cfunc(vi, number_of_elements, an_array)

    def niFake_EnumInputFunctionWithDefaults(self, vi, a_turtle):  # noqa: N802
        with self._func_lock:
            if self.niFake_EnumInputFunctionWithDefaults_cfunc is None:
                self.niFake_EnumInputFunctionWithDefaults_cfunc = self._get_library_function('niFake_EnumInputFunctionWithDefaults')
                self.niFake_EnumInputFunctionWithDefaults_cfunc.argtypes = [ViSession, ViInt16]  # noqa: F405
                self.niFake_EnumInputFunctionWithDefaults_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_EnumInputFunctionWithDefaults_cfunc(vi, a_turtle)

    def niFake_ExportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration):  # noqa: N802
        with self._func_lock:
            if self.niFake_ExportAttributeConfigurationBuffer_cfunc is None:
                self.niFake_ExportAttributeConfigurationBuffer_cfunc = self._get_library_function('niFake_ExportAttributeConfigurationBuffer')
                self.niFake_ExportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niFake_ExportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_ExportAttributeConfigurationBuffer_cfunc(vi, size_in_bytes, configuration)

    def niFake_FetchWaveform(self, vi, number_of_samples, waveform_data, actual_number_of_samples):  # noqa: N802
        with self._func_lock:
            if self.niFake_FetchWaveform_cfunc is None:
                self.niFake_FetchWaveform_cfunc = self._get_library_function('niFake_FetchWaveform')
                self.niFake_FetchWaveform_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFake_FetchWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_FetchWaveform_cfunc(vi, number_of_samples, waveform_data, actual_number_of_samples)

    def niFake_FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter(self, vi, multidimensional_array):  # noqa: N802
        with self._func_lock:
            if self.niFake_FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter_cfunc is None:
                self.niFake_FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter_cfunc = self._get_library_function('niFake_FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter')
                self.niFake_FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter_cfunc.argtypes = [ViSession, ctypes.POINTER(NIComplexNumber)]  # noqa: F405
                self.niFake_FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter_cfunc(vi, multidimensional_array)

    def niFake_FunctionWithIntflagParameter(self, vi, flag):  # noqa: N802
        with self._func_lock:
            if self.niFake_FunctionWithIntflagParameter_cfunc is None:
                self.niFake_FunctionWithIntflagParameter_cfunc = self._get_library_function('niFake_FunctionWithIntflagParameter')
                self.niFake_FunctionWithIntflagParameter_cfunc.argtypes = [ViSession, ViUInt64]  # noqa: F405
                self.niFake_FunctionWithIntflagParameter_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_FunctionWithIntflagParameter_cfunc(vi, flag)

    def niFake_FunctionWithRepeatedCapabilityType(self, vi, site_list):  # noqa: N802
        with self._func_lock:
            if self.niFake_FunctionWithRepeatedCapabilityType_cfunc is None:
                self.niFake_FunctionWithRepeatedCapabilityType_cfunc = self._get_library_function('niFake_FunctionWithRepeatedCapabilityType')
                self.niFake_FunctionWithRepeatedCapabilityType_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_FunctionWithRepeatedCapabilityType_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_FunctionWithRepeatedCapabilityType_cfunc(vi, site_list)

    def niFake_GetABoolean(self, vi, a_boolean):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetABoolean_cfunc is None:
                self.niFake_GetABoolean_cfunc = self._get_library_function('niFake_GetABoolean')
                self.niFake_GetABoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFake_GetABoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetABoolean_cfunc(vi, a_boolean)

    def niFake_GetANumber(self, vi, a_number):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetANumber_cfunc is None:
                self.niFake_GetANumber_cfunc = self._get_library_function('niFake_GetANumber')
                self.niFake_GetANumber_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16)]  # noqa: F405
                self.niFake_GetANumber_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetANumber_cfunc(vi, a_number)

    def niFake_GetAStringOfFixedMaximumSize(self, vi, a_string):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetAStringOfFixedMaximumSize_cfunc is None:
                self.niFake_GetAStringOfFixedMaximumSize_cfunc = self._get_library_function('niFake_GetAStringOfFixedMaximumSize')
                self.niFake_GetAStringOfFixedMaximumSize_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_GetAStringOfFixedMaximumSize_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetAStringOfFixedMaximumSize_cfunc(vi, a_string)

    def niFake_GetAStringUsingPythonCode(self, vi, a_number, a_string):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetAStringUsingPythonCode_cfunc is None:
                self.niFake_GetAStringUsingPythonCode_cfunc = self._get_library_function('niFake_GetAStringUsingPythonCode')
                self.niFake_GetAStringUsingPythonCode_cfunc.argtypes = [ViSession, ViInt16, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_GetAStringUsingPythonCode_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetAStringUsingPythonCode_cfunc(vi, a_number, a_string)

    def niFake_GetAnIviDanceCharArray(self, vi, buffer_size, char_array):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetAnIviDanceCharArray_cfunc is None:
                self.niFake_GetAnIviDanceCharArray_cfunc = self._get_library_function('niFake_GetAnIviDanceCharArray')
                self.niFake_GetAnIviDanceCharArray_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_GetAnIviDanceCharArray_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetAnIviDanceCharArray_cfunc(vi, buffer_size, char_array)

    def niFake_GetAnIviDanceWithATwistString(self, vi, buffer_size, a_string, actual_size):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetAnIviDanceWithATwistString_cfunc is None:
                self.niFake_GetAnIviDanceWithATwistString_cfunc = self._get_library_function('niFake_GetAnIviDanceWithATwistString')
                self.niFake_GetAnIviDanceWithATwistString_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFake_GetAnIviDanceWithATwistString_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetAnIviDanceWithATwistString_cfunc(vi, buffer_size, a_string, actual_size)

    def niFake_GetArrayForPythonCodeCustomType(self, vi, number_of_elements, array_out):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetArrayForPythonCodeCustomType_cfunc is None:
                self.niFake_GetArrayForPythonCodeCustomType_cfunc = self._get_library_function('niFake_GetArrayForPythonCodeCustomType')
                self.niFake_GetArrayForPythonCodeCustomType_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(custom_struct.struct_CustomStruct)]  # noqa: F405
                self.niFake_GetArrayForPythonCodeCustomType_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetArrayForPythonCodeCustomType_cfunc(vi, number_of_elements, array_out)

    def niFake_GetArrayForPythonCodeDouble(self, vi, number_of_elements, array_out):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetArrayForPythonCodeDouble_cfunc is None:
                self.niFake_GetArrayForPythonCodeDouble_cfunc = self._get_library_function('niFake_GetArrayForPythonCodeDouble')
                self.niFake_GetArrayForPythonCodeDouble_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_GetArrayForPythonCodeDouble_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetArrayForPythonCodeDouble_cfunc(vi, number_of_elements, array_out)

    def niFake_GetArraySizeForPythonCode(self, vi, size_out):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetArraySizeForPythonCode_cfunc is None:
                self.niFake_GetArraySizeForPythonCode_cfunc = self._get_library_function('niFake_GetArraySizeForPythonCode')
                self.niFake_GetArraySizeForPythonCode_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFake_GetArraySizeForPythonCode_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetArraySizeForPythonCode_cfunc(vi, size_out)

    def niFake_GetArrayUsingIviDance(self, vi, array_size, array_out):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetArrayUsingIviDance_cfunc is None:
                self.niFake_GetArrayUsingIviDance_cfunc = self._get_library_function('niFake_GetArrayUsingIviDance')
                self.niFake_GetArrayUsingIviDance_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_GetArrayUsingIviDance_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetArrayUsingIviDance_cfunc(vi, array_size, array_out)

    def niFake_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetAttributeViBoolean_cfunc is None:
                self.niFake_GetAttributeViBoolean_cfunc = self._get_library_function('niFake_GetAttributeViBoolean')
                self.niFake_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFake_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFake_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetAttributeViInt32_cfunc is None:
                self.niFake_GetAttributeViInt32_cfunc = self._get_library_function('niFake_GetAttributeViInt32')
                self.niFake_GetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFake_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFake_GetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetAttributeViInt64_cfunc is None:
                self.niFake_GetAttributeViInt64_cfunc = self._get_library_function('niFake_GetAttributeViInt64')
                self.niFake_GetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niFake_GetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetAttributeViInt64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFake_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetAttributeViReal64_cfunc is None:
                self.niFake_GetAttributeViReal64_cfunc = self._get_library_function('niFake_GetAttributeViReal64')
                self.niFake_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFake_GetAttributeViString(self, vi, channel_name, attribute_id, buffer_size, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetAttributeViString_cfunc is None:
                self.niFake_GetAttributeViString_cfunc = self._get_library_function('niFake_GetAttributeViString')
                self.niFake_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetAttributeViString_cfunc(vi, channel_name, attribute_id, buffer_size, attribute_value)

    def niFake_GetCalDateAndTime(self, vi, cal_type, month, day, year, hour, minute):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetCalDateAndTime_cfunc is None:
                self.niFake_GetCalDateAndTime_cfunc = self._get_library_function('niFake_GetCalDateAndTime')
                self.niFake_GetCalDateAndTime_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFake_GetCalDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetCalDateAndTime_cfunc(vi, cal_type, month, day, year, hour, minute)

    def niFake_GetCalInterval(self, vi, months):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetCalInterval_cfunc is None:
                self.niFake_GetCalInterval_cfunc = self._get_library_function('niFake_GetCalInterval')
                self.niFake_GetCalInterval_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFake_GetCalInterval_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetCalInterval_cfunc(vi, months)

    def niFake_GetChannelNames(self, vi, indices, name_size, names):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetChannelNames_cfunc is None:
                self.niFake_GetChannelNames_cfunc = self._get_library_function('niFake_GetChannelNames')
                self.niFake_GetChannelNames_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_GetChannelNames_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetChannelNames_cfunc(vi, indices, name_size, names)

    def niFake_GetCustomType(self, vi, cs):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetCustomType_cfunc is None:
                self.niFake_GetCustomType_cfunc = self._get_library_function('niFake_GetCustomType')
                self.niFake_GetCustomType_cfunc.argtypes = [ViSession, ctypes.POINTER(custom_struct.struct_CustomStruct)]  # noqa: F405
                self.niFake_GetCustomType_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetCustomType_cfunc(vi, cs)

    def niFake_GetCustomTypeArray(self, vi, number_of_elements, cs):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetCustomTypeArray_cfunc is None:
                self.niFake_GetCustomTypeArray_cfunc = self._get_library_function('niFake_GetCustomTypeArray')
                self.niFake_GetCustomTypeArray_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(custom_struct.struct_CustomStruct)]  # noqa: F405
                self.niFake_GetCustomTypeArray_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetCustomTypeArray_cfunc(vi, number_of_elements, cs)

    def niFake_GetCustomTypeTypedef(self, vi, cst, csnt):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetCustomTypeTypedef_cfunc is None:
                self.niFake_GetCustomTypeTypedef_cfunc = self._get_library_function('niFake_GetCustomTypeTypedef')
                self.niFake_GetCustomTypeTypedef_cfunc.argtypes = [ViSession, ctypes.POINTER(custom_struct_typedef.struct_CustomStructTypedef), ctypes.POINTER(custom_struct_nested_typedef.struct_CustomStructNestedTypedef)]  # noqa: F405
                self.niFake_GetCustomTypeTypedef_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetCustomTypeTypedef_cfunc(vi, cst, csnt)

    def niFake_GetEnumValue(self, vi, a_quantity, a_turtle):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetEnumValue_cfunc is None:
                self.niFake_GetEnumValue_cfunc = self._get_library_function('niFake_GetEnumValue')
                self.niFake_GetEnumValue_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt16)]  # noqa: F405
                self.niFake_GetEnumValue_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetEnumValue_cfunc(vi, a_quantity, a_turtle)

    def niFake_GetError(self, vi, error_code, buffer_size, description):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetError_cfunc is None:
                self.niFake_GetError_cfunc = self._get_library_function('niFake_GetError')
                self.niFake_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_GetError_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetError_cfunc(vi, error_code, buffer_size, description)

    def niFake_GetParameterWithOverriddenGrpcName(self, vi, original_parameter, enum_parameter):  # noqa: N802
        with self._func_lock:
            if self.niFake_GetParameterWithOverriddenGrpcName_cfunc is None:
                self.niFake_GetParameterWithOverriddenGrpcName_cfunc = self._get_library_function('niFake_GetParameterWithOverriddenGrpcName')
                self.niFake_GetParameterWithOverriddenGrpcName_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ViInt16]  # noqa: F405
                self.niFake_GetParameterWithOverriddenGrpcName_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_GetParameterWithOverriddenGrpcName_cfunc(vi, original_parameter, enum_parameter)

    def niFake_ImportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration):  # noqa: N802
        with self._func_lock:
            if self.niFake_ImportAttributeConfigurationBuffer_cfunc is None:
                self.niFake_ImportAttributeConfigurationBuffer_cfunc = self._get_library_function('niFake_ImportAttributeConfigurationBuffer')
                self.niFake_ImportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niFake_ImportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_ImportAttributeConfigurationBuffer_cfunc(vi, size_in_bytes, configuration)

    def niFake_ImportAttributeConfigurationBufferEx(self, vi, size, configuration):  # noqa: N802
        with self._func_lock:
            if self.niFake_ImportAttributeConfigurationBufferEx_cfunc is None:
                self.niFake_ImportAttributeConfigurationBufferEx_cfunc = self._get_library_function('niFake_ImportAttributeConfigurationBufferEx')
                self.niFake_ImportAttributeConfigurationBufferEx_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niFake_ImportAttributeConfigurationBufferEx_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_ImportAttributeConfigurationBufferEx_cfunc(vi, size, configuration)

    def niFake_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi):  # noqa: N802
        with self._func_lock:
            if self.niFake_InitWithOptions_cfunc is None:
                self.niFake_InitWithOptions_cfunc = self._get_library_function('niFake_InitWithOptions')
                self.niFake_InitWithOptions_cfunc.argtypes = [ctypes.POINTER(ViChar), ViBoolean, ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niFake_InitWithOptions_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_InitWithOptions_cfunc(resource_name, id_query, reset_device, option_string, vi)

    def niFake_Initiate(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFake_Initiate_cfunc is None:
                self.niFake_Initiate_cfunc = self._get_library_function('niFake_Initiate')
                self.niFake_Initiate_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFake_Initiate_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_Initiate_cfunc(vi)

    def niFake_LockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niFake_LockSession_cfunc is None:
                self.niFake_LockSession_cfunc = self._get_library_function('niFake_LockSession')
                self.niFake_LockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFake_LockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_LockSession_cfunc(vi, caller_has_lock)

    def niFake_MethodUsingWholeAndFractionalNumbers(self, whole_number, fractional_number):  # noqa: N802
        with self._func_lock:
            if self.niFake_MethodUsingWholeAndFractionalNumbers_cfunc is None:
                self.niFake_MethodUsingWholeAndFractionalNumbers_cfunc = self._get_library_function('niFake_MethodUsingWholeAndFractionalNumbers')
                self.niFake_MethodUsingWholeAndFractionalNumbers_cfunc.argtypes = [ctypes.POINTER(ViInt32), ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_MethodUsingWholeAndFractionalNumbers_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_MethodUsingWholeAndFractionalNumbers_cfunc(whole_number, fractional_number)

    def niFake_MethodWithGrpcOnlyParam(self, simple_param):  # noqa: N802
        with self._func_lock:
            if self.niFake_MethodWithGrpcOnlyParam_cfunc is None:
                self.niFake_MethodWithGrpcOnlyParam_cfunc = self._get_library_function('niFake_MethodWithGrpcOnlyParam')
                self.niFake_MethodWithGrpcOnlyParam_cfunc.argtypes = [ViInt32]  # noqa: F405
                self.niFake_MethodWithGrpcOnlyParam_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_MethodWithGrpcOnlyParam_cfunc(simple_param)

    def niFake_MethodWithProtoOnlyParameter(self, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_MethodWithProtoOnlyParameter_cfunc is None:
                self.niFake_MethodWithProtoOnlyParameter_cfunc = self._get_library_function('niFake_MethodWithProtoOnlyParameter')
                self.niFake_MethodWithProtoOnlyParameter_cfunc.argtypes = [ViInt32]  # noqa: F405
                self.niFake_MethodWithProtoOnlyParameter_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_MethodWithProtoOnlyParameter_cfunc(attribute_value)

    def niFake_MixedIviDanceAndLenMechanism(self, vi, input_values, input_values_size, output_size, output_array):  # noqa: N802
        with self._func_lock:
            if self.niFake_MixedIviDanceAndLenMechanism_cfunc is None:
                self.niFake_MixedIviDanceAndLenMechanism_cfunc = self._get_library_function('niFake_MixedIviDanceAndLenMechanism')
                self.niFake_MixedIviDanceAndLenMechanism_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64), ViInt32, ViInt32, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFake_MixedIviDanceAndLenMechanism_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_MixedIviDanceAndLenMechanism_cfunc(vi, input_values, input_values_size, output_size, output_array)

    def niFake_MultipleArrayTypes(self, vi, output_array_size, output_array, output_array_of_fixed_length, input_array_sizes, input_array_of_floats, input_array_of_integers):  # noqa: N802
        with self._func_lock:
            if self.niFake_MultipleArrayTypes_cfunc is None:
                self.niFake_MultipleArrayTypes_cfunc = self._get_library_function('niFake_MultipleArrayTypes')
                self.niFake_MultipleArrayTypes_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt16)]  # noqa: F405
                self.niFake_MultipleArrayTypes_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_MultipleArrayTypes_cfunc(vi, output_array_size, output_array, output_array_of_fixed_length, input_array_sizes, input_array_of_floats, input_array_of_integers)

    def niFake_MultipleArraysDifferentSize(self, vi, values_array, values_array_size, data_array, data_array_size):  # noqa: N802
        with self._func_lock:
            if self.niFake_MultipleArraysDifferentSize_cfunc is None:
                self.niFake_MultipleArraysDifferentSize_cfunc = self._get_library_function('niFake_MultipleArraysDifferentSize')
                self.niFake_MultipleArraysDifferentSize_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64), ViInt32, ctypes.POINTER(ViInt32), ViInt32]  # noqa: F405
                self.niFake_MultipleArraysDifferentSize_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_MultipleArraysDifferentSize_cfunc(vi, values_array, values_array_size, data_array, data_array_size)

    def niFake_MultipleArraysSameSize(self, vi, values1, values2, values3, values4, size):  # noqa: N802
        with self._func_lock:
            if self.niFake_MultipleArraysSameSize_cfunc is None:
                self.niFake_MultipleArraysSameSize_cfunc = self._get_library_function('niFake_MultipleArraysSameSize')
                self.niFake_MultipleArraysSameSize_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ViInt32]  # noqa: F405
                self.niFake_MultipleArraysSameSize_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_MultipleArraysSameSize_cfunc(vi, values1, values2, values3, values4, size)

    def niFake_OneInputFunction(self, vi, a_number):  # noqa: N802
        with self._func_lock:
            if self.niFake_OneInputFunction_cfunc is None:
                self.niFake_OneInputFunction_cfunc = self._get_library_function('niFake_OneInputFunction')
                self.niFake_OneInputFunction_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niFake_OneInputFunction_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_OneInputFunction_cfunc(vi, a_number)

    def niFake_ParametersAreMultipleTypes(self, vi, a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, a_string):  # noqa: N802
        with self._func_lock:
            if self.niFake_ParametersAreMultipleTypes_cfunc is None:
                self.niFake_ParametersAreMultipleTypes_cfunc = self._get_library_function('niFake_ParametersAreMultipleTypes')
                self.niFake_ParametersAreMultipleTypes_cfunc.argtypes = [ViSession, ViBoolean, ViInt32, ViInt64, ViInt16, ViReal64, ViReal64, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_ParametersAreMultipleTypes_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_ParametersAreMultipleTypes_cfunc(vi, a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, a_string)

    def niFake_PoorlyNamedSimpleFunction(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFake_PoorlyNamedSimpleFunction_cfunc is None:
                self.niFake_PoorlyNamedSimpleFunction_cfunc = self._get_library_function('niFake_PoorlyNamedSimpleFunction')
                self.niFake_PoorlyNamedSimpleFunction_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFake_PoorlyNamedSimpleFunction_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_PoorlyNamedSimpleFunction_cfunc(vi)

    def niFake_Read(self, vi, maximum_time, reading):  # noqa: N802
        with self._func_lock:
            if self.niFake_Read_cfunc is None:
                self.niFake_Read_cfunc = self._get_library_function('niFake_Read')
                self.niFake_Read_cfunc.argtypes = [ViSession, ViReal64, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_Read_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_Read_cfunc(vi, maximum_time, reading)

    def niFake_ReadFromChannel(self, vi, channel_name, maximum_time, reading):  # noqa: N802
        with self._func_lock:
            if self.niFake_ReadFromChannel_cfunc is None:
                self.niFake_ReadFromChannel_cfunc = self._get_library_function('niFake_ReadFromChannel')
                self.niFake_ReadFromChannel_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_ReadFromChannel_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_ReadFromChannel_cfunc(vi, channel_name, maximum_time, reading)

    def niFake_ReturnANumberAndAString(self, vi, a_number, a_string):  # noqa: N802
        with self._func_lock:
            if self.niFake_ReturnANumberAndAString_cfunc is None:
                self.niFake_ReturnANumberAndAString_cfunc = self._get_library_function('niFake_ReturnANumberAndAString')
                self.niFake_ReturnANumberAndAString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_ReturnANumberAndAString_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_ReturnANumberAndAString_cfunc(vi, a_number, a_string)

    def niFake_ReturnDurationInSeconds(self, vi, timedelta):  # noqa: N802
        with self._func_lock:
            if self.niFake_ReturnDurationInSeconds_cfunc is None:
                self.niFake_ReturnDurationInSeconds_cfunc = self._get_library_function('niFake_ReturnDurationInSeconds')
                self.niFake_ReturnDurationInSeconds_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_ReturnDurationInSeconds_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_ReturnDurationInSeconds_cfunc(vi, timedelta)

    def niFake_ReturnListOfDurationsInSeconds(self, vi, number_of_elements, timedeltas):  # noqa: N802
        with self._func_lock:
            if self.niFake_ReturnListOfDurationsInSeconds_cfunc is None:
                self.niFake_ReturnListOfDurationsInSeconds_cfunc = self._get_library_function('niFake_ReturnListOfDurationsInSeconds')
                self.niFake_ReturnListOfDurationsInSeconds_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_ReturnListOfDurationsInSeconds_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_ReturnListOfDurationsInSeconds_cfunc(vi, number_of_elements, timedeltas)

    def niFake_ReturnMultipleTypes(self, vi, a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, array_size, an_array, string_size, a_string):  # noqa: N802
        with self._func_lock:
            if self.niFake_ReturnMultipleTypes_cfunc is None:
                self.niFake_ReturnMultipleTypes_cfunc = self._get_library_function('niFake_ReturnMultipleTypes')
                self.niFake_ReturnMultipleTypes_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt64), ctypes.POINTER(ViInt16), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ViInt32, ctypes.POINTER(ViReal64), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_ReturnMultipleTypes_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_ReturnMultipleTypes_cfunc(vi, a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, array_size, an_array, string_size, a_string)

    def niFake_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_SetAttributeViBoolean_cfunc is None:
                self.niFake_SetAttributeViBoolean_cfunc = self._get_library_function('niFake_SetAttributeViBoolean')
                self.niFake_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niFake_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_SetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFake_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_SetAttributeViInt32_cfunc is None:
                self.niFake_SetAttributeViInt32_cfunc = self._get_library_function('niFake_SetAttributeViInt32')
                self.niFake_SetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niFake_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_SetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFake_SetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_SetAttributeViInt64_cfunc is None:
                self.niFake_SetAttributeViInt64_cfunc = self._get_library_function('niFake_SetAttributeViInt64')
                self.niFake_SetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt64]  # noqa: F405
                self.niFake_SetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_SetAttributeViInt64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFake_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_SetAttributeViReal64_cfunc is None:
                self.niFake_SetAttributeViReal64_cfunc = self._get_library_function('niFake_SetAttributeViReal64')
                self.niFake_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niFake_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_SetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFake_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFake_SetAttributeViString_cfunc is None:
                self.niFake_SetAttributeViString_cfunc = self._get_library_function('niFake_SetAttributeViString')
                self.niFake_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_SetAttributeViString_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFake_SetCustomType(self, vi, cs):  # noqa: N802
        with self._func_lock:
            if self.niFake_SetCustomType_cfunc is None:
                self.niFake_SetCustomType_cfunc = self._get_library_function('niFake_SetCustomType')
                self.niFake_SetCustomType_cfunc.argtypes = [ViSession, custom_struct.struct_CustomStruct]  # noqa: F405
                self.niFake_SetCustomType_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_SetCustomType_cfunc(vi, cs)

    def niFake_SetCustomTypeArray(self, vi, number_of_elements, cs):  # noqa: N802
        with self._func_lock:
            if self.niFake_SetCustomTypeArray_cfunc is None:
                self.niFake_SetCustomTypeArray_cfunc = self._get_library_function('niFake_SetCustomTypeArray')
                self.niFake_SetCustomTypeArray_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(custom_struct.struct_CustomStruct)]  # noqa: F405
                self.niFake_SetCustomTypeArray_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_SetCustomTypeArray_cfunc(vi, number_of_elements, cs)

    def niFake_SetRuntimeEnvironment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        with self._func_lock:
            if self.niFake_SetRuntimeEnvironment_cfunc is None:
                self.niFake_SetRuntimeEnvironment_cfunc = self._get_library_function('niFake_SetRuntimeEnvironment')
                self.niFake_SetRuntimeEnvironment_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_SetRuntimeEnvironment_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_SetRuntimeEnvironment_cfunc(environment, environment_version, reserved1, reserved2)

    def niFake_StringValuedEnumInputFunctionWithDefaults(self, vi, a_mobile_os_name):  # noqa: N802
        with self._func_lock:
            if self.niFake_StringValuedEnumInputFunctionWithDefaults_cfunc is None:
                self.niFake_StringValuedEnumInputFunctionWithDefaults_cfunc = self._get_library_function('niFake_StringValuedEnumInputFunctionWithDefaults')
                self.niFake_StringValuedEnumInputFunctionWithDefaults_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_StringValuedEnumInputFunctionWithDefaults_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_StringValuedEnumInputFunctionWithDefaults_cfunc(vi, a_mobile_os_name)

    def niFake_TwoInputFunction(self, vi, a_number, a_string):  # noqa: N802
        with self._func_lock:
            if self.niFake_TwoInputFunction_cfunc is None:
                self.niFake_TwoInputFunction_cfunc = self._get_library_function('niFake_TwoInputFunction')
                self.niFake_TwoInputFunction_cfunc.argtypes = [ViSession, ViReal64, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_TwoInputFunction_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_TwoInputFunction_cfunc(vi, a_number, a_string)

    def niFake_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niFake_UnlockSession_cfunc is None:
                self.niFake_UnlockSession_cfunc = self._get_library_function('niFake_UnlockSession')
                self.niFake_UnlockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFake_UnlockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_UnlockSession_cfunc(vi, caller_has_lock)

    def niFake_Use64BitNumber(self, vi, input, output):  # noqa: N802
        with self._func_lock:
            if self.niFake_Use64BitNumber_cfunc is None:
                self.niFake_Use64BitNumber_cfunc = self._get_library_function('niFake_Use64BitNumber')
                self.niFake_Use64BitNumber_cfunc.argtypes = [ViSession, ViInt64, ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niFake_Use64BitNumber_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_Use64BitNumber_cfunc(vi, input, output)

    def niFake_WriteWaveform(self, vi, number_of_samples, waveform):  # noqa: N802
        with self._func_lock:
            if self.niFake_WriteWaveform_cfunc is None:
                self.niFake_WriteWaveform_cfunc = self._get_library_function('niFake_WriteWaveform')
                self.niFake_WriteWaveform_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFake_WriteWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_WriteWaveform_cfunc(vi, number_of_samples, waveform)

    def niFake_WriteWaveformNumpyComplex128(self, vi, number_of_samples, waveform_data_array):  # noqa: N802
        with self._func_lock:
            if self.niFake_WriteWaveformNumpyComplex128_cfunc is None:
                self.niFake_WriteWaveformNumpyComplex128_cfunc = self._get_library_function('niFake_WriteWaveformNumpyComplex128')
                self.niFake_WriteWaveformNumpyComplex128_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(NIComplexNumber)]  # noqa: F405
                self.niFake_WriteWaveformNumpyComplex128_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_WriteWaveformNumpyComplex128_cfunc(vi, number_of_samples, waveform_data_array)

    def niFake_WriteWaveformNumpyComplex64(self, vi, number_of_samples, waveform_data_array):  # noqa: N802
        with self._func_lock:
            if self.niFake_WriteWaveformNumpyComplex64_cfunc is None:
                self.niFake_WriteWaveformNumpyComplex64_cfunc = self._get_library_function('niFake_WriteWaveformNumpyComplex64')
                self.niFake_WriteWaveformNumpyComplex64_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(NIComplexNumberF32)]  # noqa: F405
                self.niFake_WriteWaveformNumpyComplex64_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_WriteWaveformNumpyComplex64_cfunc(vi, number_of_samples, waveform_data_array)

    def niFake_WriteWaveformNumpyComplexInterleavedI16(self, vi, number_of_samples, waveform_data_array):  # noqa: N802
        with self._func_lock:
            if self.niFake_WriteWaveformNumpyComplexInterleavedI16_cfunc is None:
                self.niFake_WriteWaveformNumpyComplexInterleavedI16_cfunc = self._get_library_function('niFake_WriteWaveformNumpyComplexInterleavedI16')
                self.niFake_WriteWaveformNumpyComplexInterleavedI16_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(NIComplexI16)]  # noqa: F405
                self.niFake_WriteWaveformNumpyComplexInterleavedI16_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_WriteWaveformNumpyComplexInterleavedI16_cfunc(vi, number_of_samples, waveform_data_array)

    def niFake_close(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFake_close_cfunc is None:
                self.niFake_close_cfunc = self._get_library_function('niFake_close')
                self.niFake_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFake_close_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_close_cfunc(vi)

    def niFake_error_message(self, vi, error_code, error_message):  # noqa: N802
        with self._func_lock:
            if self.niFake_error_message_cfunc is None:
                self.niFake_error_message_cfunc = self._get_library_function('niFake_error_message')
                self.niFake_error_message_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_error_message_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_error_message_cfunc(vi, error_code, error_message)

    def niFake_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        with self._func_lock:
            if self.niFake_self_test_cfunc is None:
                self.niFake_self_test_cfunc = self._get_library_function('niFake_self_test')
                self.niFake_self_test_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFake_self_test_cfunc.restype = ViStatus  # noqa: F405
        return self.niFake_self_test_cfunc(vi, self_test_result, self_test_message)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/nifake/_library_interpreter.py sha256=7d4060ad82ab7500ab6be21c6b4ced407750ff66717dea45503dd49d25ee3af0 bytes=58688 -->
## FILE: generated/nifake/nifake/_library_interpreter.py

- repository: `ni/nimi-python`
- source_path: `generated/nifake/nifake/_library_interpreter.py`
- sha256: `7d4060ad82ab7500ab6be21c6b4ced407750ff66717dea45503dd49d25ee3af0`
- bytes: 58688

````python
# -*- coding: utf-8 -*-
# This file was generated

import array
import ctypes
import hightime  # noqa: F401
import platform

import nifake._complextype as _complextype
import nifake._library_singleton as _library_singleton
import nifake._visatype as _visatype
import nifake.enums as enums  # noqa: F401
import nifake.errors as errors

import nifake.custom_struct as custom_struct  # noqa: F401

import nifake.custom_struct_typedef as custom_struct_typedef  # noqa: F401

import nifake.custom_struct_nested_typedef as custom_struct_nested_typedef  # noqa: F401


_was_runtime_environment_set = None


# Helper functions for creating ctypes needed for calling into the driver DLL
def _get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None):
    if isinstance(value, array.array):
        assert library_type is not None, 'library_type is required for array.array'
        addr, _ = value.buffer_info()
        return ctypes.cast(addr, ctypes.POINTER(library_type))
    elif str(type(value)).find("'numpy.ndarray'") != -1:
        import numpy
        if library_type in (_complextype.NIComplexI16, _complextype.NIComplexNumberF32, _complextype.NIComplexNumber):
            complex_dtype = numpy.dtype(library_type)
            if value.ndim > 1:
                # we create a flattened view of the multi-dimensional numpy array
                restructured_array_view = value.ravel().view(complex_dtype)
            else:
                restructured_array_view = value.view(complex_dtype)
            return restructured_array_view.ctypes.data_as(ctypes.POINTER(library_type))
        else:
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
        error_code = self._library.niFake_Abort(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def accept_list_of_durations_in_seconds(self, delays):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        count_ctype = _visatype.ViInt32(0 if delays is None else len(delays))  # case S160
        delays_ctype = _get_ctypes_pointer_for_buffer(value=delays, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.niFake_AcceptListOfDurationsInSeconds(vi_ctype, count_ctype, delays_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def bool_array_output_function(self, number_of_elements):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_elements_ctype = _visatype.ViInt32(number_of_elements)  # case S210
        an_array_size = number_of_elements  # case B600
        an_array_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViBoolean, size=an_array_size)  # case B600
        error_code = self._library.niFake_BoolArrayOutputFunction(vi_ctype, number_of_elements_ctype, an_array_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [bool(an_array_ctype[i]) for i in range(number_of_elements_ctype.value)]

    def configure_abc(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFake_ConfigureABC(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def custom_nested_struct_roundtrip(self, nested_custom_type_in):  # noqa: N802
        nested_custom_type_in_ctype = custom_struct_nested_typedef.struct_CustomStructNestedTypedef(nested_custom_type_in)  # case S150
        nested_custom_type_out_ctype = custom_struct_nested_typedef.struct_CustomStructNestedTypedef()  # case S220
        error_code = self._library.niFake_CustomNestedStructRoundtrip(nested_custom_type_in_ctype, None if nested_custom_type_out_ctype is None else (ctypes.pointer(nested_custom_type_out_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return custom_struct_nested_typedef.CustomStructNestedTypedef(nested_custom_type_out_ctype)

    def double_all_the_nums(self, numbers):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_count_ctype = _visatype.ViInt32(0 if numbers is None else len(numbers))  # case S160
        numbers_ctype = _get_ctypes_pointer_for_buffer(value=numbers, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.niFake_DoubleAllTheNums(vi_ctype, number_count_ctype, numbers_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def enum_array_output_function(self, number_of_elements):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_elements_ctype = _visatype.ViInt32(number_of_elements)  # case S210
        an_array_size = number_of_elements  # case B600
        an_array_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt16, size=an_array_size)  # case B600
        error_code = self._library.niFake_EnumArrayOutputFunction(vi_ctype, number_of_elements_ctype, an_array_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [enums.Turtle(an_array_ctype[i]) for i in range(number_of_elements_ctype.value)]

    def enum_input_function_with_defaults(self, a_turtle):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_turtle_ctype = _visatype.ViInt16(a_turtle.value)  # case S130
        error_code = self._library.niFake_EnumInputFunctionWithDefaults(vi_ctype, a_turtle_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def export_attribute_configuration_buffer(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        size_in_bytes_ctype = _visatype.ViInt32()  # case S170
        configuration_ctype = None  # case B580
        error_code = self._library.niFake_ExportAttributeConfigurationBuffer(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        size_in_bytes_ctype = _visatype.ViInt32(error_code)  # case S180
        configuration_size = size_in_bytes_ctype.value  # case B590
        configuration_array = array.array("b", [0]) * configuration_size  # case B590
        configuration_ctype = _get_ctypes_pointer_for_buffer(value=configuration_array, library_type=_visatype.ViInt8)  # case B590
        error_code = self._library.niFake_ExportAttributeConfigurationBuffer(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return configuration_array

    def fetch_waveform(self, number_of_samples):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_samples_ctype = _visatype.ViInt32(number_of_samples)  # case S210
        waveform_data_size = number_of_samples  # case B600
        waveform_data_array = array.array("d", [0]) * waveform_data_size  # case B600
        waveform_data_ctype = _get_ctypes_pointer_for_buffer(value=waveform_data_array, library_type=_visatype.ViReal64)  # case B600
        actual_number_of_samples_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFake_FetchWaveform(vi_ctype, number_of_samples_ctype, waveform_data_ctype, None if actual_number_of_samples_ctype is None else (ctypes.pointer(actual_number_of_samples_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return waveform_data_array

    def fetch_waveform_into(self, waveform_data):  # noqa: N802
        number_of_samples = len(waveform_data)
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_samples_ctype = _visatype.ViInt32(number_of_samples)  # case S210
        waveform_data_ctype = _get_ctypes_pointer_for_buffer(value=waveform_data)  # case B510
        actual_number_of_samples_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFake_FetchWaveform(vi_ctype, number_of_samples_ctype, waveform_data_ctype, None if actual_number_of_samples_ctype is None else (ctypes.pointer(actual_number_of_samples_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def function_with_3d_numpy_array_of_numpy_complex128_input_parameter(self, multidimensional_array):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        multidimensional_array_ctype = _get_ctypes_pointer_for_buffer(value=multidimensional_array, library_type=_complextype.NIComplexNumber)  # case B510
        error_code = self._library.niFake_FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter(vi_ctype, multidimensional_array_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def function_with_intflag_parameter(self, flag):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        flag_ctype = _visatype.ViUInt64(flag.value)  # case S130
        error_code = self._library.niFake_FunctionWithIntflagParameter(vi_ctype, flag_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def function_with_repeated_capability_type(self, site_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C010
        error_code = self._library.niFake_FunctionWithRepeatedCapabilityType(vi_ctype, site_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def get_a_boolean(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_boolean_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niFake_GetABoolean(vi_ctype, None if a_boolean_ctype is None else (ctypes.pointer(a_boolean_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(a_boolean_ctype.value)

    def get_a_number(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_number_ctype = _visatype.ViInt16()  # case S220
        error_code = self._library.niFake_GetANumber(vi_ctype, None if a_number_ctype is None else (ctypes.pointer(a_number_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(a_number_ctype.value)

    def get_a_string_of_fixed_maximum_size(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_string_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niFake_GetAStringOfFixedMaximumSize(vi_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return a_string_ctype.value.decode(self._encoding)

    def get_a_string_using_python_code(self, a_number):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_number_ctype = _visatype.ViInt16(a_number)  # case S150
        a_string_ctype = (_visatype.ViChar * a_number)()  # case C080
        error_code = self._library.niFake_GetAStringUsingPythonCode(vi_ctype, a_number_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return a_string_ctype.value.decode(self._encoding)

    def get_an_ivi_dance_char_array(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        char_array_ctype = None  # case C050
        error_code = self._library.niFake_GetAnIviDanceCharArray(vi_ctype, buffer_size_ctype, char_array_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        char_array_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niFake_GetAnIviDanceCharArray(vi_ctype, buffer_size_ctype, char_array_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return char_array_ctype.value.decode(self._encoding)

    def get_an_ivi_dance_with_a_twist_string(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        a_string_ctype = None  # case C090
        actual_size_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFake_GetAnIviDanceWithATwistString(vi_ctype, buffer_size_ctype, a_string_ctype, None if actual_size_ctype is None else (ctypes.pointer(actual_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(actual_size_ctype.value)  # case S200
        a_string_ctype = (_visatype.ViChar * actual_size_ctype.value)()  # case C100
        error_code = self._library.niFake_GetAnIviDanceWithATwistString(vi_ctype, buffer_size_ctype, a_string_ctype, None if actual_size_ctype is None else (ctypes.pointer(actual_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return a_string_ctype.value.decode(self._encoding)

    def get_array_for_python_code_custom_type(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_elements_ctype = _visatype.ViInt32(self.get_array_size_for_python_code())  # case S120
        array_out_size = self.get_array_size_for_python_code()  # case B560
        array_out_ctype = _get_ctypes_pointer_for_buffer(library_type=custom_struct.struct_CustomStruct, size=array_out_size)  # case B560
        error_code = self._library.niFake_GetArrayForPythonCodeCustomType(vi_ctype, number_of_elements_ctype, array_out_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [custom_struct.CustomStruct(array_out_ctype[i]) for i in range(self.get_array_size_for_python_code())]

    def get_array_for_python_code_double(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_elements_ctype = _visatype.ViInt32(self.get_array_size_for_python_code())  # case S120
        array_out_size = self.get_array_size_for_python_code()  # case B560
        array_out_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=array_out_size)  # case B560
        error_code = self._library.niFake_GetArrayForPythonCodeDouble(vi_ctype, number_of_elements_ctype, array_out_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(array_out_ctype[i]) for i in range(self.get_array_size_for_python_code())]

    def get_array_size_for_python_code(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        size_out_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFake_GetArraySizeForPythonCode(vi_ctype, None if size_out_ctype is None else (ctypes.pointer(size_out_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(size_out_ctype.value)

    def get_array_using_ivi_dance(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        array_size_ctype = _visatype.ViInt32()  # case S170
        array_out_ctype = None  # case B580
        error_code = self._library.niFake_GetArrayUsingIviDance(vi_ctype, array_size_ctype, array_out_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        array_size_ctype = _visatype.ViInt32(error_code)  # case S180
        array_out_size = array_size_ctype.value  # case B590
        array_out_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=array_out_size)  # case B590
        error_code = self._library.niFake_GetArrayUsingIviDance(vi_ctype, array_size_ctype, array_out_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(array_out_ctype[i]) for i in range(array_size_ctype.value)]

    def get_attribute_vi_boolean(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niFake_GetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(attribute_value_ctype.value)

    def get_attribute_vi_int32(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFake_GetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def get_attribute_vi_int64(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niFake_GetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def get_attribute_vi_real64(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niFake_GetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(attribute_value_ctype.value)

    def get_attribute_vi_string(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        attribute_value_ctype = None  # case C050
        error_code = self._library.niFake_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        attribute_value_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niFake_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
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
        error_code = self._library.niFake_GetCalDateAndTime(vi_ctype, cal_type_ctype, None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if year_ctype is None else (ctypes.pointer(year_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(month_ctype.value), int(day_ctype.value), int(year_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_cal_interval(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        months_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFake_GetCalInterval(vi_ctype, None if months_ctype is None else (ctypes.pointer(months_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(months_ctype.value)

    def get_channel_names(self, indices):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        indices_ctype = ctypes.create_string_buffer(indices.encode(self._encoding))  # case C020
        name_size_ctype = _visatype.ViInt32()  # case S170
        names_ctype = None  # case C050
        error_code = self._library.niFake_GetChannelNames(vi_ctype, indices_ctype, name_size_ctype, names_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        name_size_ctype = _visatype.ViInt32(error_code)  # case S180
        names_ctype = (_visatype.ViChar * name_size_ctype.value)()  # case C060
        error_code = self._library.niFake_GetChannelNames(vi_ctype, indices_ctype, name_size_ctype, names_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return names_ctype.value.decode(self._encoding)

    def get_custom_type(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        cs_ctype = custom_struct.struct_CustomStruct()  # case S220
        error_code = self._library.niFake_GetCustomType(vi_ctype, None if cs_ctype is None else (ctypes.pointer(cs_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return custom_struct.CustomStruct(cs_ctype)

    def get_custom_type_array(self, number_of_elements):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_elements_ctype = _visatype.ViInt32(number_of_elements)  # case S210
        cs_size = number_of_elements  # case B600
        cs_ctype = _get_ctypes_pointer_for_buffer(library_type=custom_struct.struct_CustomStruct, size=cs_size)  # case B600
        error_code = self._library.niFake_GetCustomTypeArray(vi_ctype, number_of_elements_ctype, cs_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [custom_struct.CustomStruct(cs_ctype[i]) for i in range(number_of_elements_ctype.value)]

    def get_custom_type_typedef(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        cst_ctype = custom_struct_typedef.struct_CustomStructTypedef()  # case S220
        csnt_ctype = custom_struct_nested_typedef.struct_CustomStructNestedTypedef()  # case S220
        error_code = self._library.niFake_GetCustomTypeTypedef(vi_ctype, None if cst_ctype is None else (ctypes.pointer(cst_ctype)), None if csnt_ctype is None else (ctypes.pointer(csnt_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return custom_struct_typedef.CustomStructTypedef(cst_ctype), custom_struct_nested_typedef.CustomStructNestedTypedef(csnt_ctype)

    def get_enum_value(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_quantity_ctype = _visatype.ViInt32()  # case S220
        a_turtle_ctype = _visatype.ViInt16()  # case S220
        error_code = self._library.niFake_GetEnumValue(vi_ctype, None if a_quantity_ctype is None else (ctypes.pointer(a_quantity_ctype)), None if a_turtle_ctype is None else (ctypes.pointer(a_turtle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(a_quantity_ctype.value), enums.Turtle(a_turtle_ctype.value)

    def get_error(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus()  # case S220
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        description_ctype = None  # case C050
        error_code = self._library.niFake_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        description_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niFake_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), description_ctype.value.decode(self._encoding)

    def get_parameter_with_overridden_grpc_name(self, enum_parameter):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        original_parameter_ctype = _visatype.ViInt16()  # case S220
        enum_parameter_ctype = _visatype.ViInt16(enum_parameter.value)  # case S130
        error_code = self._library.niFake_GetParameterWithOverriddenGrpcName(vi_ctype, None if original_parameter_ctype is None else (ctypes.pointer(original_parameter_ctype)), enum_parameter_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(original_parameter_ctype.value)

    def import_attribute_configuration_buffer(self, configuration):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        size_in_bytes_ctype = _visatype.ViInt32(0 if configuration is None else len(configuration))  # case S160
        configuration_ctype = _get_ctypes_pointer_for_buffer(value=configuration, library_type=_visatype.ViInt8)  # case B550
        error_code = self._library.niFake_ImportAttributeConfigurationBuffer(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def import_attribute_configuration_buffer_ex(self, configuration):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        size_ctype = _visatype.ViInt32(0 if configuration is None else len(configuration))  # case S160
        configuration_ctype = _get_ctypes_pointer_for_buffer(value=configuration, library_type=_visatype.ViInt8)  # case B550
        error_code = self._library.niFake_ImportAttributeConfigurationBufferEx(vi_ctype, size_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def init_with_options(self, resource_name, id_query, reset_device, option_string):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        id_query_ctype = _visatype.ViBoolean(id_query)  # case S150
        reset_device_ctype = _visatype.ViBoolean(reset_device)  # case S150
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case C020
        vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niFake_InitWithOptions(resource_name_ctype, id_query_ctype, reset_device_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        self._close_on_exit = True
        return int(vi_ctype.value)

    def initiate(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFake_Initiate(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def lock(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFake_LockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def method_using_whole_and_fractional_numbers(self):  # noqa: N802
        whole_number_ctype = _visatype.ViInt32()  # case S220
        fractional_number_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niFake_MethodUsingWholeAndFractionalNumbers(None if whole_number_ctype is None else (ctypes.pointer(whole_number_ctype)), None if fractional_number_ctype is None else (ctypes.pointer(fractional_number_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(whole_number_ctype.value), float(fractional_number_ctype.value)

    def method_with_grpc_only_param(self, simple_param):  # noqa: N802
        simple_param_ctype = _visatype.ViInt32(simple_param)  # case S150
        error_code = self._library.niFake_MethodWithGrpcOnlyParam(simple_param_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def method_with_proto_only_parameter(self, attribute_value):  # noqa: N802
        attribute_value_ctype = _visatype.ViInt32(attribute_value)  # case S150
        error_code = self._library.niFake_MethodWithProtoOnlyParameter(attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def mixed_ivi_dance_and_len_mechanism(self, input_values):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        input_values_ctype = _get_ctypes_pointer_for_buffer(value=input_values, library_type=_visatype.ViReal64)  # case B550
        input_values_size_ctype = _visatype.ViInt32(0 if input_values is None else len(input_values))  # case S160
        output_size_ctype = _visatype.ViInt32()  # case S170
        output_array_ctype = None  # case B580
        error_code = self._library.niFake_MixedIviDanceAndLenMechanism(vi_ctype, input_values_ctype, input_values_size_ctype, output_size_ctype, output_array_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        output_size_ctype = _visatype.ViInt32(error_code)  # case S180
        output_array_size = output_size_ctype.value  # case B590
        output_array_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=output_array_size)  # case B590
        error_code = self._library.niFake_MixedIviDanceAndLenMechanism(vi_ctype, input_values_ctype, input_values_size_ctype, output_size_ctype, output_array_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [int(output_array_ctype[i]) for i in range(output_size_ctype.value)]

    def multiple_array_types(self, output_array_size, input_array_of_floats, input_array_of_integers):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        output_array_size_ctype = _visatype.ViInt32(output_array_size)  # case S210
        output_array_size = output_array_size  # case B600
        output_array_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=output_array_size)  # case B600
        output_array_of_fixed_length_size = 3  # case B570
        output_array_of_fixed_length_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=output_array_of_fixed_length_size)  # case B570
        input_array_sizes_ctype = _visatype.ViInt32(0 if input_array_of_floats is None else len(input_array_of_floats))  # case S160
        input_array_of_floats_ctype = _get_ctypes_pointer_for_buffer(value=input_array_of_floats, library_type=_visatype.ViReal64)  # case B550
        input_array_of_integers_ctype = _get_ctypes_pointer_for_buffer(value=input_array_of_integers, library_type=_visatype.ViInt16)  # case B550
        error_code = self._library.niFake_MultipleArrayTypes(vi_ctype, output_array_size_ctype, output_array_ctype, output_array_of_fixed_length_ctype, input_array_sizes_ctype, input_array_of_floats_ctype, input_array_of_integers_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(output_array_ctype[i]) for i in range(output_array_size_ctype.value)], [float(output_array_of_fixed_length_ctype[i]) for i in range(3)]

    def multiple_arrays_different_size(self, values_array, data_array):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        values_array_ctype = _get_ctypes_pointer_for_buffer(value=values_array, library_type=_visatype.ViReal64)  # case B550
        values_array_size_ctype = _visatype.ViInt32(0 if values_array is None else len(values_array))  # case S160
        data_array_ctype = _get_ctypes_pointer_for_buffer(value=data_array, library_type=_visatype.ViInt32)  # case B550
        data_array_size_ctype = _visatype.ViInt32(0 if data_array is None else len(data_array))  # case S160
        error_code = self._library.niFake_MultipleArraysDifferentSize(vi_ctype, values_array_ctype, values_array_size_ctype, data_array_ctype, data_array_size_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def multiple_arrays_same_size(self, values1, values2, values3, values4):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        values1_ctype = _get_ctypes_pointer_for_buffer(value=values1, library_type=_visatype.ViReal64)  # case B550
        values2_ctype = _get_ctypes_pointer_for_buffer(value=values2, library_type=_visatype.ViReal64)  # case B550
        values3_ctype = _get_ctypes_pointer_for_buffer(value=values3, library_type=_visatype.ViReal64)  # case B550
        values4_ctype = _get_ctypes_pointer_for_buffer(value=values4, library_type=_visatype.ViReal64)  # case B550
        size_ctype = _visatype.ViInt32(0 if values1 is None else len(values1))  # case S160
        error_code = self._library.niFake_MultipleArraysSameSize(vi_ctype, values1_ctype, values2_ctype, values3_ctype, values4_ctype, size_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def one_input_function(self, a_number):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_number_ctype = _visatype.ViInt32(a_number)  # case S150
        error_code = self._library.niFake_OneInputFunction(vi_ctype, a_number_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def parameters_are_multiple_types(self, a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, a_string):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_boolean_ctype = _visatype.ViBoolean(a_boolean)  # case S150
        an_int32_ctype = _visatype.ViInt32(an_int32)  # case S150
        an_int64_ctype = _visatype.ViInt64(an_int64)  # case S150
        an_int_enum_ctype = _visatype.ViInt16(an_int_enum.value)  # case S130
        a_float_ctype = _visatype.ViReal64(a_float)  # case S150
        a_float_enum_ctype = _visatype.ViReal64(a_float_enum.value)  # case S130
        a_string_ctype = ctypes.create_string_buffer(a_string.encode(self._encoding))  # case C020
        error_code = self._library.niFake_ParametersAreMultipleTypes(vi_ctype, a_boolean_ctype, an_int32_ctype, an_int64_ctype, an_int_enum_ctype, a_float_ctype, a_float_enum_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def simple_function(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFake_PoorlyNamedSimpleFunction(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def read(self, maximum_time):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_time_ctype = _visatype.ViReal64(maximum_time)  # case S150
        reading_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niFake_Read(vi_ctype, maximum_time_ctype, None if reading_ctype is None else (ctypes.pointer(reading_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(reading_ctype.value)

    def read_from_channel(self, channel_name, maximum_time):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        maximum_time_ctype = _visatype.ViInt32(maximum_time)  # case S150
        reading_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niFake_ReadFromChannel(vi_ctype, channel_name_ctype, maximum_time_ctype, None if reading_ctype is None else (ctypes.pointer(reading_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(reading_ctype.value)

    def return_a_number_and_a_string(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_number_ctype = _visatype.ViInt16()  # case S220
        a_string_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niFake_ReturnANumberAndAString(vi_ctype, None if a_number_ctype is None else (ctypes.pointer(a_number_ctype)), a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(a_number_ctype.value), a_string_ctype.value.decode(self._encoding)

    def return_duration_in_seconds(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        timedelta_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niFake_ReturnDurationInSeconds(vi_ctype, None if timedelta_ctype is None else (ctypes.pointer(timedelta_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(timedelta_ctype.value)

    def return_list_of_durations_in_seconds(self, number_of_elements):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_elements_ctype = _visatype.ViInt32(number_of_elements)  # case S210
        timedeltas_size = number_of_elements  # case B600
        timedeltas_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=timedeltas_size)  # case B600
        error_code = self._library.niFake_ReturnListOfDurationsInSeconds(vi_ctype, number_of_elements_ctype, timedeltas_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(timedeltas_ctype[i]) for i in range(number_of_elements_ctype.value)]

    def return_multiple_types(self, array_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_boolean_ctype = _visatype.ViBoolean()  # case S220
        an_int32_ctype = _visatype.ViInt32()  # case S220
        an_int64_ctype = _visatype.ViInt64()  # case S220
        an_int_enum_ctype = _visatype.ViInt16()  # case S220
        a_float_ctype = _visatype.ViReal64()  # case S220
        a_float_enum_ctype = _visatype.ViReal64()  # case S220
        array_size_ctype = _visatype.ViInt32(array_size)  # case S210
        an_array_size = array_size  # case B600
        an_array_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=an_array_size)  # case B600
        string_size_ctype = _visatype.ViInt32()  # case S170
        a_string_ctype = None  # case C050
        error_code = self._library.niFake_ReturnMultipleTypes(vi_ctype, None if a_boolean_ctype is None else (ctypes.pointer(a_boolean_ctype)), None if an_int32_ctype is None else (ctypes.pointer(an_int32_ctype)), None if an_int64_ctype is None else (ctypes.pointer(an_int64_ctype)), None if an_int_enum_ctype is None else (ctypes.pointer(an_int_enum_ctype)), None if a_float_ctype is None else (ctypes.pointer(a_float_ctype)), None if a_float_enum_ctype is None else (ctypes.pointer(a_float_enum_ctype)), array_size_ctype, an_array_ctype, string_size_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        string_size_ctype = _visatype.ViInt32(error_code)  # case S180
        a_string_ctype = (_visatype.ViChar * string_size_ctype.value)()  # case C060
        error_code = self._library.niFake_ReturnMultipleTypes(vi_ctype, None if a_boolean_ctype is None else (ctypes.pointer(a_boolean_ctype)), None if an_int32_ctype is None else (ctypes.pointer(an_int32_ctype)), None if an_int64_ctype is None else (ctypes.pointer(an_int64_ctype)), None if an_int_enum_ctype is None else (ctypes.pointer(an_int_enum_ctype)), None if a_float_ctype is None else (ctypes.pointer(a_float_ctype)), None if a_float_enum_ctype is None else (ctypes.pointer(a_float_enum_ctype)), array_size_ctype, an_array_ctype, string_size_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(a_boolean_ctype.value), int(an_int32_ctype.value), int(an_int64_ctype.value), enums.Turtle(an_int_enum_ctype.value), float(a_float_ctype.value), enums.FloatEnum(a_float_enum_ctype.value), [float(an_array_ctype[i]) for i in range(array_size_ctype.value)], a_string_ctype.value.decode(self._encoding)

    def set_attribute_vi_boolean(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean(attribute_value)  # case S150
        error_code = self._library.niFake_SetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_int32(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32(attribute_value)  # case S150
        error_code = self._library.niFake_SetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_int64(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt64(attribute_value)  # case S150
        error_code = self._library.niFake_SetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_real64(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64(attribute_value)  # case S150
        error_code = self._library.niFake_SetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_string(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = ctypes.create_string_buffer(attribute_value.encode(self._encoding))  # case C020
        error_code = self._library.niFake_SetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_custom_type(self, cs):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        cs_ctype = custom_struct.struct_CustomStruct(cs)  # case S150
        error_code = self._library.niFake_SetCustomType(vi_ctype, cs_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_custom_type_array(self, cs):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_elements_ctype = _visatype.ViInt32(0 if cs is None else len(cs))  # case S160
        cs_ctype = _get_ctypes_pointer_for_buffer([custom_struct.struct_CustomStruct(c) for c in cs], library_type=custom_struct.struct_CustomStruct)  # case B540
        error_code = self._library.niFake_SetCustomTypeArray(vi_ctype, number_of_elements_ctype, cs_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_runtime_environment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        environment_ctype = ctypes.create_string_buffer(environment.encode(self._encoding))  # case C020
        environment_version_ctype = ctypes.create_string_buffer(environment_version.encode(self._encoding))  # case C020
        reserved1_ctype = ctypes.create_string_buffer(reserved1.encode(self._encoding))  # case C020
        reserved2_ctype = ctypes.create_string_buffer(reserved2.encode(self._encoding))  # case C020
        error_code = self._library.niFake_SetRuntimeEnvironment(environment_ctype, environment_version_ctype, reserved1_ctype, reserved2_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def string_valued_enum_input_function_with_defaults(self, a_mobile_os_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_mobile_os_name_ctype = ctypes.create_string_buffer(a_mobile_os_name.value.encode(self._encoding))  # case C030
        error_code = self._library.niFake_StringValuedEnumInputFunctionWithDefaults(vi_ctype, a_mobile_os_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def two_input_function(self, a_number, a_string):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        a_number_ctype = _visatype.ViReal64(a_number)  # case S150
        a_string_ctype = ctypes.create_string_buffer(a_string.encode(self._encoding))  # case C020
        error_code = self._library.niFake_TwoInputFunction(vi_ctype, a_number_ctype, a_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFake_UnlockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def use64_bit_number(self, input):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        input_ctype = _visatype.ViInt64(input)  # case S150
        output_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niFake_Use64BitNumber(vi_ctype, input_ctype, None if output_ctype is None else (ctypes.pointer(output_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(output_ctype.value)

    def write_waveform(self, waveform):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_samples_ctype = _visatype.ViInt32(0 if waveform is None else len(waveform))  # case S160
        waveform_array = _convert_to_array(value=waveform, array_type="d")  # case B550
        waveform_ctype = _get_ctypes_pointer_for_buffer(value=waveform_array, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.niFake_WriteWaveform(vi_ctype, number_of_samples_ctype, waveform_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_waveform_numpy(self, waveform):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_samples_ctype = _visatype.ViInt32(0 if waveform is None else len(waveform))  # case S160
        waveform_ctype = _get_ctypes_pointer_for_buffer(value=waveform)  # case B510
        error_code = self._library.niFake_WriteWaveform(vi_ctype, number_of_samples_ctype, waveform_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_waveform_numpy_complex128(self, waveform_data_array):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_samples_ctype = _visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array))  # case S160
        waveform_data_array_ctype = _get_ctypes_pointer_for_buffer(value=waveform_data_array, library_type=_complextype.NIComplexNumber)  # case B510
        error_code = self._library.niFake_WriteWaveformNumpyComplex128(vi_ctype, number_of_samples_ctype, waveform_data_array_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_waveform_numpy_complex64(self, waveform_data_array):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_samples_ctype = _visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array))  # case S160
        waveform_data_array_ctype = _get_ctypes_pointer_for_buffer(value=waveform_data_array, library_type=_complextype.NIComplexNumberF32)  # case B510
        error_code = self._library.niFake_WriteWaveformNumpyComplex64(vi_ctype, number_of_samples_ctype, waveform_data_array_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_waveform_numpy_complex_interleaved_i16(self, waveform_data_array):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_samples_ctype = _visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array) // 2)  # case S160
        waveform_data_array_ctype = _get_ctypes_pointer_for_buffer(value=waveform_data_array, library_type=_complextype.NIComplexI16)  # case B510
        error_code = self._library.niFake_WriteWaveformNumpyComplexInterleavedI16(vi_ctype, number_of_samples_ctype, waveform_data_array_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def close(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFake_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def error_message(self, error_code):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niFake_error_message(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)

    def self_test(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        self_test_result_ctype = _visatype.ViInt16()  # case S220
        self_test_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niFake_self_test(vi_ctype, None if self_test_result_ctype is None else (ctypes.pointer(self_test_result_ctype)), self_test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(self._encoding)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/nifake/_library_singleton.py sha256=deff6d6fb31ddd12d3708a4ab51c9956e6795401bde184d3c9c3a4b35e5cf24f bytes=1693 -->
## FILE: generated/nifake/nifake/_library_singleton.py

- repository: `ni/nimi-python`
- source_path: `generated/nifake/nifake/_library_singleton.py`
- sha256: `deff6d6fb31ddd12d3708a4ab51c9956e6795401bde184d3c9c3a4b35e5cf24f`
- bytes: 1693

````python
# -*- coding: utf-8 -*-
# This file was generated

import platform

import ctypes
import ctypes.util
import nifake._library as _library
import nifake.errors as errors
import threading


_instance = None
_instance_lock = threading.Lock()
_library_info = {'Linux': {'64bit': {'name': 'nifake', 'type': 'cdll'}},
                 'Windows': {'32bit': {'name': 'nifake_32.dll', 'type': 'windll'},
                             '64bit': {'name': 'nifake_64.dll', 'type': 'cdll'}}}


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

    Returns the library.Library singleton for nifake.
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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/nifake/_visatype.py sha256=ac436ae1613f5e807cd16d2df951c7a502f37996234e4d324c5412b3633e1c92 bytes=662 -->
## FILE: generated/nifake/nifake/_visatype.py

- repository: `ni/nimi-python`
- source_path: `generated/nifake/nifake/_visatype.py`
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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/nifake/custom_struct.py sha256=a94d67bd1b3a7360b5c4bf85a25d3a98a7fc2fbb21115c17778cf9191115b00e bytes=1582 -->
## FILE: generated/nifake/nifake/custom_struct.py

- repository: `ni/nimi-python`
- source_path: `generated/nifake/nifake/custom_struct.py`
- sha256: `a94d67bd1b3a7360b5c4bf85a25d3a98a7fc2fbb21115c17778cf9191115b00e`
- bytes: 1582

````python
import ctypes

import nifake._visatype


# This class is an internal implementation detail
# ctypes definition
# Name must match exactly what the name of the structure type is named in the C API.
class struct_CustomStruct(ctypes.Structure):  # noqa N801
    _fields_ = [
        ('struct_int', nifake._visatype.ViInt32),
        ('struct_double', nifake._visatype.ViReal64),
    ]

    def __init__(self, data=None, struct_int=0, struct_double=0.0):
        super(ctypes.Structure, self).__init__()
        if data is not None:
            self.struct_int = data.struct_int
            self.struct_double = data.struct_double
        else:
            self.struct_int = struct_int
            self.struct_double = struct_double

    def __repr__(self):
        return f'{self.__class__.__name__}(data=None, struct_int={self.struct_int}, struct_double={self.struct_double})'

    def __str__(self):
        return self.__repr__()


class CustomStruct:
    def __init__(self, data=None, struct_int=0, struct_double=0.0):
        if data is not None:
            self.struct_int = data.struct_int
            self.struct_double = data.struct_double
        else:
            self.struct_int = struct_int
            self.struct_double = struct_double

    def _create_copy(self, target_class):
        return target_class(struct_int=self.struct_int, struct_double=self.struct_double)

    def __repr__(self):
        return f'{self.__class__.__name__}(data=None, struct_int={self.struct_int}, struct_double={self.struct_double})'

    def __str__(self):
        return self.__repr__()
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/nifake/custom_struct_nested_typedef.py sha256=4945f5fb3dbd8e7d62062595649762a1eeab969b4e5c6bb37edf891f513163ae bytes=2363 -->
## FILE: generated/nifake/nifake/custom_struct_nested_typedef.py

- repository: `ni/nimi-python`
- source_path: `generated/nifake/nifake/custom_struct_nested_typedef.py`
- sha256: `4945f5fb3dbd8e7d62062595649762a1eeab969b4e5c6bb37edf891f513163ae`
- bytes: 2363

````python
import ctypes

import nifake.custom_struct as custom_struct
import nifake.custom_struct_typedef as custom_struct_typedef


class struct_CustomStructNestedTypedef(ctypes.Structure):  # noqa N801
    _fields_ = [
        ('struct_custom_struct', custom_struct.struct_CustomStruct),
        ('struct_custom_struct_typedef', custom_struct_typedef.struct_CustomStructTypedef),
    ]

    def __init__(self, data=None):
        super(ctypes.Structure, self).__init__()
        if data is not None:
            self.struct_custom_struct = custom_struct.struct_CustomStruct(data.struct_custom_struct)
            self.struct_custom_struct_typedef = custom_struct_typedef.struct_CustomStructTypedef(
                data.struct_custom_struct_typedef
            )
        else:
            self.struct_custom_struct = custom_struct.struct_CustomStruct()
            self.struct_custom_struct_typedef = custom_struct_typedef.struct_CustomStructTypedef()


class CustomStructNestedTypedef:
    def __init__(
        self,
        data=None,
        struct_custom_struct=custom_struct.CustomStruct(),
        struct_custom_struct_typedef=custom_struct_typedef.CustomStructTypedef()
    ):
        if data is not None:
            self.struct_custom_struct = custom_struct.CustomStruct(data.struct_custom_struct)
            self.struct_custom_struct_typedef = custom_struct_typedef.CustomStructTypedef(
                data.struct_custom_struct_typedef
            )
        else:
            self.struct_custom_struct = struct_custom_struct
            self.struct_custom_struct_typedef = struct_custom_struct_typedef

    def _create_copy(self, target_class):
        sample_object = target_class()
        return target_class(
            struct_custom_struct=self.struct_custom_struct._create_copy(
                type(sample_object.struct_custom_struct)
            ),
            struct_custom_struct_typedef=self.struct_custom_struct_typedef._create_copy(
                type(sample_object.struct_custom_struct_typedef)
            ),
        )

    def __repr__(self):
        return '{}(data=None, struct_custom_struct={}, struct_custom_struct_typedef={})'.format(
            self.__class__.__name__,
            repr(self.struct_custom_struct),
            repr(self.struct_custom_struct_typedef)
        )

    def __str__(self):
        return self.__repr__()
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/nifake/custom_struct_typedef.py sha256=be78d97161bdae9a5886f24a56ec10d128035da22248361ecb04b91e57e66bc1 bytes=1246 -->
## FILE: generated/nifake/nifake/custom_struct_typedef.py

- repository: `ni/nimi-python`
- source_path: `generated/nifake/nifake/custom_struct_typedef.py`
- sha256: `be78d97161bdae9a5886f24a56ec10d128035da22248361ecb04b91e57e66bc1`
- bytes: 1246

````python
import ctypes

import nifake._visatype


class struct_CustomStructTypedef(ctypes.Structure):  # noqa N801
    _fields_ = [
        ('struct_int', nifake._visatype.ViInt32),
        ('struct_double', nifake._visatype.ViReal64),
    ]

    def __init__(self, data=None):
        super(ctypes.Structure, self).__init__()
        if data is not None:
            self.struct_int = data.struct_int
            self.struct_double = data.struct_double
        else:
            self.struct_int = 0
            self.struct_double = 0.0


class CustomStructTypedef:
    def __init__(self, data=None, struct_int=0, struct_double=0.0):
        if data is not None:
            self.struct_int = data.struct_int
            self.struct_double = data.struct_double
        else:
            self.struct_int = struct_int
            self.struct_double = struct_double

    def _create_copy(self, target_class):
        return target_class(struct_int=self.struct_int, struct_double=self.struct_double)

    def __repr__(self):
        return '{}(data=None, struct_int={}, struct_double={})'.format(
            self.__class__.__name__,
            self.struct_int,
            self.struct_double
        )

    def __str__(self):
        return self.__repr__()
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/nifake/enums.py sha256=0923ab60f5cce4466a1ad5ce8b6d02ae000880d6aff39779e5620d95e426ce5a bytes=1476 -->
## FILE: generated/nifake/nifake/enums.py

- repository: `ni/nimi-python`
- source_path: `generated/nifake/nifake/enums.py`
- sha256: `0923ab60f5cce4466a1ad5ce8b6d02ae000880d6aff39779e5620d95e426ce5a`
- bytes: 1476

````python
# -*- coding: utf-8 -*-
# This file was generated

from enum import Enum
from enum import IntFlag


class Color(Enum):
    RED = 1
    r'''
    Like blood.
    '''
    BLUE = 2
    r'''
    Like the sky.
    '''
    YELLOW = 5
    r'''
    Like a banana.
    '''
    BLACK = 42
    r'''
    Like this developer's conscience.
    '''


class EnumWithConverter(Enum):
    RED = 1
    BLUE = 2
    YELLOW = 5
    BLACK = 42


class FloatEnum(Enum):
    THREE_POINT_FIVE = 3.5
    r'''
    Specifies 3.5 digits resolution.
    '''
    FOUR_POINT_FIVE = 4.5
    r'''
    Specifies 4.5 digits resolution.
    '''
    FIVE_POINT_FIVE = 5.5
    r'''
    Specifies 5.5 digits resolution.
    '''
    SIX_POINT_FIVE = 6.5
    r'''
    Specifies 6.5 digits resolution.
    '''
    SEVEN_POINT_FIVE = 7.5
    r'''
    Specifies 7.5 digits resolution.
    '''


class IntFlagEnum(IntFlag):
    A = 1
    r'''
    Flag A option.
    '''
    B = 2
    r'''
    Flag B option.
    '''
    E = 1073741824
    r'''
    Flag E option.
    '''


class MobileOSNames(Enum):
    ANDROID = 'Android'
    r'''
    Most popular OS.
    '''
    IOS = 'iOS'
    r'''
    Most secure OS.
    '''
    NONE = 'None'
    r'''
    Remember Symbian?.
    '''


class Turtle(Enum):
    LEONARDO = 0
    r'''
    Wields two katanas.
    '''
    DONATELLO = 1
    r'''
    Uses a bo staff.
    '''
    RAPHAEL = 2
    r'''
    Has a pair of sai.
    '''
    MICHELANGELO = 3
    r'''
    Owns nunchucks.
    '''
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/nifake/errors.py sha256=cf759ba89b0f07fc3c7fcf8cb2e95fde6dfba9ea67971b26c05397dec30507fb bytes=4349 -->
## FILE: generated/nifake/nifake/errors.py

- repository: `ni/nimi-python`
- source_path: `generated/nifake/nifake/errors.py`
- sha256: `cf759ba89b0f07fc3c7fcf8cb2e95fde6dfba9ea67971b26c05397dec30507fb`
- bytes: 4349

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
    '''Base error class for NI-FAKE'''

    def __init__(self, message):
        super(Error, self).__init__(message)


class DriverError(Error):
    '''An error originating from the NI-FAKE driver'''

    def __init__(self, code, description):
        assert _is_error(code), "Should not raise Error if code is not fatal."
        self.code = code
        self.description = description
        super(DriverError, self).__init__(str(self.code) + ": " + self.description)


class DriverWarning(Warning):
    '''A warning originating from the NI-FAKE driver'''

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
        super(DriverNotInstalledError, self).__init__('The NI-FAKE runtime could not be loaded. Make sure it is installed and its bitness matches that of your Python interpreter. Please visit http://www.ni.com/downloads/drivers/ to download and install it.')


class DriverTooOldError(Error):
    '''An error due to using this module with an older version of the NI-FAKE driver runtime.'''

    def __init__(self):
        super(DriverTooOldError, self).__init__('A function was not found in the NI-FAKE runtime. Please visit http://www.ni.com/downloads/drivers/ to download a newer version and install it.')


class DriverTooNewError(Error):
    '''An error due to the NI-FAKE driver runtime being too new for this module.'''

    def __init__(self):
        super(DriverTooNewError, self).__init__('The NI-FAKE runtime returned an unexpected value. This can occur if it is too new for the nifake Python module. Upgrade the nifake Python module.')


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

    Helper function for handling errors returned by nifake.Library.
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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/nifake/grpc_session_options.py sha256=f411161ac541ba8d15c97eb076abb38d9d2b9b42f8ae65e97c75bc5ec00d0ca4 bytes=3452 -->
## FILE: generated/nifake/nifake/grpc_session_options.py

- repository: `ni/nimi-python`
- source_path: `generated/nifake/nifake/grpc_session_options.py`
- sha256: `f411161ac541ba8d15c97eb076abb38d9d2b9b42f8ae65e97c75bc5ec00d0ca4`
- bytes: 3452

````python
# -*- coding: utf-8 -*-
# This file was generated

from enum import IntEnum


# This constant specifies the gRPC package and service used by this API.
# Customers can pass this value to the MeasurementLink discovery service to resolve the server instance that provides this interface.
GRPC_SERVICE_INTERFACE_NAME = 'nifake_grpc.NiFake'

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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/nifake/nidevice_pb2.py sha256=9a935a95cbe830099345438b27f1460989b073de2e873f43cb394ac0df4ced54 bytes=2009 -->
## FILE: generated/nifake/nifake/nidevice_pb2.py

- repository: `ni/nimi-python`
- source_path: `generated/nifake/nifake/nidevice_pb2.py`
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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/nifake/nidevice_pb2_grpc.py sha256=d686e804f171693117b7d030ec4023f205c70c234c8590f6557aa8702f65fe09 bytes=159 -->
## FILE: generated/nifake/nifake/nidevice_pb2_grpc.py

- repository: `ni/nimi-python`
- source_path: `generated/nifake/nifake/nidevice_pb2_grpc.py`
- sha256: `d686e804f171693117b7d030ec4023f205c70c234c8590f6557aa8702f65fe09`
- bytes: 159

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/nifake/nifake_pb2.py sha256=80023dca1aa37370dd211313ee24a1f4bcb15a1389dd2518182bb153e3e7ef4e bytes=81908 -->
## FILE: generated/nifake/nifake/nifake_pb2.py

- repository: `ni/nimi-python`
- source_path: `generated/nifake/nifake/nifake_pb2.py`
- sha256: `80023dca1aa37370dd211313ee24a1f4bcb15a1389dd2518182bb153e3e7ef4e`
- bytes: 81908

````python
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nifake.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import session_pb2 as session__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cnifake.proto\x12\x0bnifake_grpc\x1a\rsession.proto\"=\n\x10\x46\x61keCustomStruct\x12\x12\n\nstruct_int\x18\x01 \x01(\x11\x12\x15\n\rstruct_double\x18\x02 \x01(\x01\"\xa0\x01\n\x19\x43ustomStructNestedTypedef\x12;\n\x14struct_custom_struct\x18\x01 \x01(\x0b\x32\x1d.nifake_grpc.FakeCustomStruct\x12\x46\n\x1cstruct_custom_struct_typedef\x18\x02 \x01(\x0b\x32 .nifake_grpc.CustomStructTypedef\"@\n\x13\x43ustomStructTypedef\x12\x12\n\nstruct_int\x18\x01 \x01(\x11\x12\x15\n\rstruct_double\x18\x02 \x01(\x01\"6\n\x13NIComplexI16_struct\x12\x0c\n\x04real\x18\x01 \x01(\x11\x12\x11\n\timaginary\x18\x02 \x01(\x11\"9\n\x16NIComplexNumber_struct\x12\x0c\n\x04real\x18\x01 \x01(\x01\x12\x11\n\timaginary\x18\x02 \x01(\x01\"<\n\x19NIComplexNumberF32_struct\x12\x0c\n\x04real\x18\x01 \x01(\x02\x12\x11\n\timaginary\x18\x02 \x01(\x02\"J\n\x0fStringAndTurtle\x12\x12\n\nstring_arg\x18\x01 \x01(\t\x12#\n\x06turtle\x18\x02 \x01(\x0e\x32\x13.nifake_grpc.Turtle\"%\n\x0f\x43ustomNamedType\x12\x12\n\nstring_arg\x18\x01 \x01(\t\"2\n\x0c\x41\x62ortRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\x1f\n\rAbortResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"`\n\x1e\x42oolArrayOutputFunctionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x1a\n\x12number_of_elements\x18\x02 \x01(\x11\"C\n\x1f\x42oolArrayOutputFunctionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08\x61n_array\x18\x02 \x03(\x08\"2\n\x0c\x43loseRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\x1f\n\rCloseResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"`\n\x1e\x45numArrayOutputFunctionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x1a\n\x12number_of_elements\x18\x02 \x01(\x11\"n\n\x1f\x45numArrayOutputFunctionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12%\n\x08\x61n_array\x18\x02 \x03(\x0e\x32\x13.nifake_grpc.Turtle\x12\x14\n\x0c\x61n_array_raw\x18\x03 \x03(\x11\"\x9c\x01\n$EnumInputFunctionWithDefaultsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\'\n\x08\x61_turtle\x18\x02 \x01(\x0e\x32\x13.nifake_grpc.TurtleH\x00\x12\x16\n\x0c\x61_turtle_raw\x18\x03 \x01(\x11H\x00\x42\x0f\n\ra_turtle_enum\"7\n%EnumInputFunctionWithDefaultsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xce\x01\n0StringValuedEnumInputFunctionWithDefaultsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12=\n\x17\x61_mobile_os_name_mapped\x18\x02 \x01(\x0e\x32\x1a.nifake_grpc.MobileOSNamesH\x00\x12\x1e\n\x14\x61_mobile_os_name_raw\x18\x03 \x01(\tH\x00\x42\x17\n\x15\x61_mobile_os_name_enum\"C\n1StringValuedEnumInputFunctionWithDefaultsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"M\n\x13\x45rrorMessageRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x12\n\nerror_code\x18\x02 \x01(\x11\"=\n\x14\x45rrorMessageResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t\"U\n\x14\x46\x65tchWaveformRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x19\n\x11number_of_samples\x18\x02 \x01(\x11\"`\n\x15\x46\x65tchWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rwaveform_data\x18\x02 \x03(\x01\x12 \n\x18\x61\x63tual_number_of_samples\x18\x03 \x01(\x11\"8\n\x12GetABooleanRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"8\n\x13GetABooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\ta_boolean\x18\x02 \x01(\x08\"7\n\x11GetANumberRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"6\n\x12GetANumberResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08\x61_number\x18\x02 \x01(\x11\"I\n#GetAStringOfFixedMaximumSizeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"H\n$GetAStringOfFixedMaximumSizeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08\x61_string\x18\x02 \x01(\t\"C\n\x1dGetAnIviDanceCharArrayRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"D\n\x1eGetAnIviDanceCharArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nchar_array\x18\x02 \x01(\t\"B\n\x1cGetArrayUsingIviDanceRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"B\n\x1dGetArrayUsingIviDanceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\tarray_out\x18\x02 \x03(\x01\"\x8c\x01\n\x1cGetAttributeViBooleanRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifake_grpc.NiFakeAttribute\"H\n\x1dGetAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0f\x61ttribute_value\x18\x02 \x01(\x08\"\x8a\x01\n\x1aGetAttributeViInt32Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifake_grpc.NiFakeAttribute\"F\n\x1bGetAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0f\x61ttribute_value\x18\x02 \x01(\x11\"\x8a\x01\n\x1aGetAttributeViInt64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifake_grpc.NiFakeAttribute\"F\n\x1bGetAttributeViInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0f\x61ttribute_value\x18\x02 \x01(\x03\"\x8b\x01\n\x1bGetAttributeViReal64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifake_grpc.NiFakeAttribute\"G\n\x1cGetAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0f\x61ttribute_value\x18\x02 \x01(\x01\"\x8c\x01\n\x1cGetAttributeViSessionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifake_grpc.NiFakeAttribute\"`\n\x1dGetAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12/\n\x0f\x61ttribute_value\x18\x02 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\x8b\x01\n\x1bGetAttributeViStringRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifake_grpc.NiFakeAttribute\"G\n\x1cGetAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0f\x61ttribute_value\x18\x02 \x01(\t\"P\n\x18GetCalDateAndTimeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x10\n\x08\x63\x61l_type\x18\x02 \x01(\x11\"s\n\x19GetCalDateAndTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05month\x18\x02 \x01(\x11\x12\x0b\n\x03\x64\x61y\x18\x03 \x01(\x11\x12\x0c\n\x04year\x18\x04 \x01(\x11\x12\x0c\n\x04hour\x18\x05 \x01(\x11\x12\x0e\n\x06minute\x18\x06 \x01(\x11\";\n\x15GetCalIntervalRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"8\n\x16GetCalIntervalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0e\n\x06months\x18\x02 \x01(\x11\"9\n\x13GetEnumValueRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"w\n\x14GetEnumValueResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\na_quantity\x18\x02 \x01(\x11\x12%\n\x08\x61_turtle\x18\x03 \x01(\x0e\x32\x13.nifake_grpc.Turtle\x12\x14\n\x0c\x61_turtle_raw\x18\x04 \x01(\x11\"5\n\x0fGetErrorRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"K\n\x10GetErrorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nerror_code\x18\x02 \x01(\x11\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"\xd3\x01\n\x16InitWithOptionsRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x10\n\x08id_query\x18\x03 \x01(\x08\x12\x14\n\x0creset_device\x18\x04 \x01(\x08\x12\x15\n\roption_string\x18\x05 \x01(\t\x12M\n\x17initialization_behavior\x18\x06 \x01(\x0e\x32,.nidevice_grpc.SessionInitializationBehavior\"n\n\x17InitWithOptionsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\"\n\x02vi\x18\x02 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x1f\n\x17new_session_initialized\x18\x03 \x01(\x08\"\x9a\x01\n\x19MultipleArrayTypesRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x19\n\x11output_array_size\x18\x02 \x01(\x11\x12\x1d\n\x15input_array_of_floats\x18\x03 \x03(\x01\x12\x1f\n\x17input_array_of_integers\x18\x04 \x03(\x11\"h\n\x1aMultipleArrayTypesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x14\n\x0coutput_array\x18\x02 \x03(\x01\x12$\n\x1coutput_array_of_fixed_length\x18\x03 \x03(\x01\"\x87\x01\n\x1dMultipleArraysSameSizeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0f\n\x07values1\x18\x02 \x03(\x01\x12\x0f\n\x07values2\x18\x03 \x03(\x01\x12\x0f\n\x07values3\x18\x04 \x03(\x01\x12\x0f\n\x07values4\x18\x05 \x03(\x01\"0\n\x1eMultipleArraysSameSizeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"r\n\"MultipleArraysDifferentSizeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0cvalues_array\x18\x02 \x03(\x01\x12\x12\n\ndata_array\x18\x03 \x03(\x11\"5\n#MultipleArraysDifferentSizeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"_\n#MixedIviDanceAndLenMechanismRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0cinput_values\x18\x02 \x03(\x01\"L\n$MixedIviDanceAndLenMechanismResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x14\n\x0coutput_array\x18\x02 \x03(\x11\"O\n\x17OneInputFunctionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x10\n\x08\x61_number\x18\x02 \x01(\x11\"*\n\x18OneInputFunctionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xe4\x02\n!ParametersAreMultipleTypesRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\ta_boolean\x18\x02 \x01(\x08\x12\x10\n\x08\x61n_int32\x18\x03 \x01(\x11\x12\x10\n\x08\x61n_int64\x18\x04 \x01(\x03\x12*\n\x0b\x61n_int_enum\x18\x05 \x01(\x0e\x32\x13.nifake_grpc.TurtleH\x00\x12\x19\n\x0f\x61n_int_enum_raw\x18\x06 \x01(\x11H\x00\x12\x0f\n\x07\x61_float\x18\x07 \x01(\x01\x12\x35\n\x13\x61_float_enum_mapped\x18\x08 \x01(\x0e\x32\x16.nifake_grpc.FloatEnumH\x01\x12\x1a\n\x10\x61_float_enum_raw\x18\t \x01(\x01H\x01\x12\x10\n\x08\x61_string\x18\n \x01(\tB\x12\n\x10\x61n_int_enum_enumB\x13\n\x11\x61_float_enum_enum\"4\n\"ParametersAreMultipleTypesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"F\n PoorlyNamedSimpleFunctionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"3\n!PoorlyNamedSimpleFunctionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"G\n\x0bReadRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0cmaximum_time\x18\x02 \x01(\x01\"/\n\x0cReadResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07reading\x18\x02 \x01(\x01\"h\n\x16ReadFromChannelRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x14\n\x0cmaximum_time\x18\x03 \x01(\x11\":\n\x17ReadFromChannelResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07reading\x18\x02 \x01(\x01\"D\n\x1eReturnANumberAndAStringRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"U\n\x1fReturnANumberAndAStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08\x61_number\x18\x02 \x01(\x11\x12\x10\n\x08\x61_string\x18\x03 \x01(\t\"T\n\x1aReturnMultipleTypesRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x12\n\narray_size\x18\x02 \x01(\x11\"\xab\x02\n\x1bReturnMultipleTypesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\ta_boolean\x18\x02 \x01(\x08\x12\x10\n\x08\x61n_int32\x18\x03 \x01(\x11\x12\x10\n\x08\x61n_int64\x18\x04 \x01(\x03\x12(\n\x0b\x61n_int_enum\x18\x05 \x01(\x0e\x32\x13.nifake_grpc.Turtle\x12\x17\n\x0f\x61n_int_enum_raw\x18\x06 \x01(\x11\x12\x0f\n\x07\x61_float\x18\x07 \x01(\x01\x12\x33\n\x13\x61_float_enum_mapped\x18\x08 \x01(\x0e\x32\x16.nifake_grpc.FloatEnum\x12\x18\n\x10\x61_float_enum_raw\x18\t \x01(\x01\x12\x10\n\x08\x61n_array\x18\n \x03(\x01\x12\x10\n\x08\x61_string\x18\x0b \x01(\t\"\xa5\x01\n\x1cSetAttributeViBooleanRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifake_grpc.NiFakeAttribute\x12\x17\n\x0f\x61ttribute_value\x18\x04 \x01(\x08\"/\n\x1dSetAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x85\x02\n\x1aSetAttributeViInt32Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifake_grpc.NiFakeAttribute\x12\x42\n\x0f\x61ttribute_value\x18\x04 \x01(\x0e\x32\'.nifake_grpc.NiFakeInt32AttributeValuesH\x00\x12\x1d\n\x13\x61ttribute_value_raw\x18\x05 \x01(\x11H\x00\x42\x16\n\x14\x61ttribute_value_enum\"-\n\x1bSetAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xa7\x01\n\x1aSetAttributeViInt64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifake_grpc.NiFakeAttribute\x12\x1b\n\x13\x61ttribute_value_raw\x18\x04 \x01(\x03\"-\n\x1bSetAttributeViInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xd9\x02\n\x1bSetAttributeViReal64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifake_grpc.NiFakeAttribute\x12\x43\n\x0f\x61ttribute_value\x18\x04 \x01(\x0e\x32(.nifake_grpc.NiFakeReal64AttributeValuesH\x00\x12P\n\x16\x61ttribute_value_mapped\x18\x05 \x01(\x0e\x32..nifake_grpc.NiFakeReal64AttributeValuesMappedH\x00\x12\x1d\n\x13\x61ttribute_value_raw\x18\x06 \x01(\x01H\x00\x42\x16\n\x14\x61ttribute_value_enum\".\n\x1cSetAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xa8\x01\n\x1bSetAttributeViStringRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifake_grpc.NiFakeAttribute\x12\x1b\n\x13\x61ttribute_value_raw\x18\x04 \x01(\t\".\n\x1cSetAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"a\n\x17TwoInputFunctionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x10\n\x08\x61_number\x18\x02 \x01(\x01\x12\x10\n\x08\x61_string\x18\x03 \x01(\t\"*\n\x18TwoInputFunctionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"J\n\x15Use64BitNumberRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\r\n\x05input\x18\x02 \x01(\x03\"8\n\x16Use64BitNumberResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0e\n\x06output\x18\x02 \x01(\x03\"L\n\x14WriteWaveformRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x10\n\x08waveform\x18\x02 \x03(\x01\"\'\n\x15WriteWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x8b\x01\n#WriteWaveformNumpyComplex128Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12@\n\x13waveform_data_array\x18\x02 \x03(\x0b\x32#.nifake_grpc.NIComplexNumber_struct\"6\n$WriteWaveformNumpyComplex128Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x8d\x01\n\"WriteWaveformNumpyComplex64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x43\n\x13waveform_data_array\x18\x02 \x03(\x0b\x32&.nifake_grpc.NIComplexNumberF32_struct\"5\n#WriteWaveformNumpyComplex64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x93\x01\n.WriteWaveformNumpyComplexInterleavedI16Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12=\n\x13waveform_data_array\x18\x02 \x03(\x0b\x32 .nifake_grpc.NIComplexI16_struct\"A\n/WriteWaveformNumpyComplexInterleavedI16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"e\n\x14SetCustomTypeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12)\n\x02\x63s\x18\x02 \x01(\x0b\x32\x1d.nifake_grpc.FakeCustomStruct\"\'\n\x15SetCustomTypeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"j\n\x19SetCustomTypeArrayRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12)\n\x02\x63s\x18\x02 \x03(\x0b\x32\x1d.nifake_grpc.FakeCustomStruct\",\n\x1aSetCustomTypeArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\":\n\x14GetCustomTypeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"R\n\x15GetCustomTypeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12)\n\x02\x63s\x18\x02 \x01(\x0b\x32\x1d.nifake_grpc.FakeCustomStruct\"[\n\x19GetCustomTypeArrayRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x1a\n\x12number_of_elements\x18\x02 \x01(\x11\"W\n\x1aGetCustomTypeArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12)\n\x02\x63s\x18\x02 \x03(\x0b\x32\x1d.nifake_grpc.FakeCustomStruct\"[\n#GetAnIviDanceWithATwistArrayRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x10\n\x08\x61_string\x18\x02 \x01(\t\"^\n$GetAnIviDanceWithATwistArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\tarray_out\x18\x02 \x03(\x11\x12\x13\n\x0b\x61\x63tual_size\x18\x03 \x01(\x11\"J\n$GetAnIviDanceWithATwistStringRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"^\n%GetAnIviDanceWithATwistStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08\x61_string\x18\x02 \x01(\t\x12\x13\n\x0b\x61\x63tual_size\x18\x03 \x01(\x11\"N\n\x17\x44oubleAllTheNumsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0f\n\x07numbers\x18\x02 \x03(\x01\"*\n\x18\x44oubleAllTheNumsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"[\n%AcceptListOfDurationsInSecondsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0e\n\x06\x64\x65lays\x18\x02 \x03(\x01\"8\n&AcceptListOfDurationsInSecondsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"D\n\x1eReturnDurationInSecondsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"D\n\x1fReturnDurationInSecondsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\ttimedelta\x18\x02 \x01(\x01\"g\n%ReturnListOfDurationsInSecondsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x1a\n\x12number_of_elements\x18\x02 \x01(\x11\"L\n&ReturnListOfDurationsInSecondsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\ntimedeltas\x18\x02 \x03(\x01\"9\n\x13\x43onfigureAbcRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"&\n\x14\x43onfigureAbcResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x8d\x02\n\x15\x43onfigureEnumsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x30\n\x0csample_count\x18\x02 \x01(\x0e\x32\x18.nifake_grpc.SampleCountH\x00\x12\x1a\n\x10sample_count_raw\x18\x03 \x01(\x11H\x00\x12\x36\n\x0fsample_interval\x18\x04 \x01(\x0e\x32\x1b.nifake_grpc.SampleIntervalH\x01\x12\x1d\n\x13sample_interval_raw\x18\x05 \x01(\x01H\x01\x42\x13\n\x11sample_count_enumB\x16\n\x14sample_interval_enum\"(\n\x16\x43onfigureEnumsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"Q\n+ExportAttributeConfigurationBufferExRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"U\n,ExportAttributeConfigurationBufferExResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rconfiguration\x18\x02 \x01(\x0c\"h\n+ImportAttributeConfigurationBufferExRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x15\n\rconfiguration\x18\x02 \x01(\x0c\">\n,ImportAttributeConfigurationBufferExResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"x\n\x1a\x46\x65tchWithCustomSizeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x1b\n\x13number_of_waveforms\x18\x02 \x01(\x11\x12\x19\n\x11number_of_samples\x18\x03 \x01(\x11\"D\n\x1b\x46\x65tchWithCustomSizeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rwaveform_data\x18\x02 \x03(\x01\"\xbf\x01\n)GetParameterWithOverriddenGrpcNameRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x31\n\x12\x65num_parameter_raw\x18\x02 \x01(\x0e\x32\x13.nifake_grpc.TurtleH\x00\x12 \n\x16\x65num_parameter_raw_raw\x18\x03 \x01(\x11H\x00\x42\x19\n\x17\x65num_parameter_raw_enum\"Z\n*GetParameterWithOverriddenGrpcNameResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1c\n\x14overridden_parameter\x18\x02 \x01(\x11\"`\n:IviDanceWithTwistWithMultipleArraysAndOneBufferSizeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\x9a\x01\n;IviDanceWithTwistWithMultipleArraysAndOneBufferSizeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0e\n\x06\x61rray1\x18\x02 \x03(\x11\x12\x0e\n\x06\x61rray2\x18\x03 \x03(\x11\x12\x0e\n\x06\x61rray3\x18\x04 \x03(\x11\x12\x1b\n\x13\x61\x63tual_num_elements\x18\x05 \x01(\x11\"M\n\'FunctionWithOverriddenGrpcName2xRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\":\n(FunctionWithOverriddenGrpcName2xResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xa9\x01\n>FunctionWith3dNumpyArrayOfNumpyComplex128InputParameterRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x43\n\x16multidimensional_array\x18\x02 \x03(\x0b\x32#.nifake_grpc.NIComplexNumber_struct\"Q\n?FunctionWith3dNumpyArrayOfNumpyComplex128InputParameterResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"c\n&StringValuedEnumNoEnumGeneratedRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x15\n\ra_string_enum\x18\x02 \x01(\t\"9\n\'StringValuedEnumNoEnumGeneratedResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"P\n*IviDanceWithATwistCalculatedSizeOutRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\x8e\x01\n+IviDanceWithATwistCalculatedSizeOutResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x03(\r\x12\x1c\n\x14\x61\x63tual_num_waveforms\x18\x03 \x01(\x11\x12#\n\x1b\x61\x63tual_samples_per_waveform\x18\x04 \x01(\x11\"f\n)ImportAttributeConfigurationBufferRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x15\n\rconfiguration\x18\x02 \x01(\x0c\"<\n*ImportAttributeConfigurationBufferResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"O\n)ExportAttributeConfigurationBufferRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"S\n*ExportAttributeConfigurationBufferResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rconfiguration\x18\x02 \x01(\x0c\"B\n\x12\x43ontrol4022Request\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x15\n\rconfiguration\x18\x02 \x01(\x11\"%\n\x13\x43ontrol4022Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"c\n\x1b\x41\x63\x63\x65ptViSessionArrayRequest\x12\x15\n\rsession_count\x18\x01 \x01(\r\x12-\n\rsession_array\x18\x02 \x03(\x0b\x32\x16.nidevice_grpc.Session\".\n\x1c\x41\x63\x63\x65ptViSessionArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"W\n\x1a\x41\x63\x63\x65ptViUInt32ArrayRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x15\n\ru_int32_array\x18\x02 \x03(\r\"-\n\x1b\x41\x63\x63\x65ptViUInt32ArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"q\n\x1d\x42oolArrayInputFunctionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x1a\n\x12number_of_elements\x18\x02 \x01(\x11\x12\x10\n\x08\x61n_array\x18\x03 \x03(\x08\"0\n\x1e\x42oolArrayInputFunctionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"H\n\x12\x43loseExtCalRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\x11\"%\n\x13\x43loseExtCalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"E\n\x1f\x43ommandWithReservedParamRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"2\n CommandWithReservedParamResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"Z\n\x1e\x43reateConfigurationListRequest\x12\x38\n\x12list_attribute_ids\x18\x01 \x03(\x0e\x32\x1c.nifake_grpc.NiFakeAttribute\"1\n\x1f\x43reateConfigurationListResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"k\n\"CustomNestedStructRoundtripRequest\x12\x45\n\x15nested_custom_type_in\x18\x01 \x01(\x0b\x32&.nifake_grpc.CustomStructNestedTypedef\"}\n#CustomNestedStructRoundtripResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x46\n\x16nested_custom_type_out\x18\x02 \x01(\x0b\x32&.nifake_grpc.CustomStructNestedTypedef\"\x1f\n\x1dGetBitfieldAsEnumArrayRequest\"o\n\x1eGetBitfieldAsEnumArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x0b\x66lags_array\x18\x02 \x03(\x0e\x32\x15.nifake_grpc.Bitfield\x12\x11\n\tflags_raw\x18\x03 \x01(\x03\"U\n/GetAnIviDanceWithATwistArrayOfCustomTypeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\x89\x01\n0GetAnIviDanceWithATwistArrayOfCustomTypeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x30\n\tarray_out\x18\x02 \x03(\x0b\x32\x1d.nifake_grpc.FakeCustomStruct\x12\x13\n\x0b\x61\x63tual_size\x18\x03 \x01(\x11\"D\n1GetAnIviDanceWithATwistArrayWithInputArrayRequest\x12\x0f\n\x07\x64\x61ta_in\x18\x01 \x03(\x11\"l\n2GetAnIviDanceWithATwistArrayWithInputArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\tarray_out\x18\x02 \x03(\x11\x12\x13\n\x0b\x61\x63tual_size\x18\x03 \x01(\x11\")\n\'GetAnIviDanceWithATwistByteArrayRequest\"b\n(GetAnIviDanceWithATwistByteArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\tarray_out\x18\x02 \x01(\x0c\x12\x13\n\x0b\x61\x63tual_size\x18\x03 \x01(\x11\"/\n-GetAnIviDanceWithATwistStringStrlenBugRequest\"i\n.GetAnIviDanceWithATwistStringStrlenBugResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nstring_out\x18\x02 \x01(\t\x12\x13\n\x0b\x61\x63tual_size\x18\x03 \x01(\x11\"F\n GetArraySizeForCustomCodeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"E\n!GetArraySizeForCustomCodeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08size_out\x18\x02 \x01(\x11\"W\n\x1eGetArrayViUInt8WithEnumRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tarray_len\x18\x02 \x01(\x11\"\x8b\x01\n\x1fGetArrayViUInt8WithEnumResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x39\n\x11u_int8_enum_array\x18\x02 \x03(\x0e\x32\x1e.nifake_grpc.GrpcColorOverride\x12\x1d\n\x15u_int8_enum_array_raw\x18\x03 \x01(\x0c\"7\n\x11GetViUInt8Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"<\n\x12GetViUInt8Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x16\n\x0e\x61_uint8_number\x18\x02 \x01(\r\"O\n\x16GetViInt32ArrayRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tarray_len\x18\x02 \x01(\x11\">\n\x17GetViInt32ArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0bint32_array\x18\x02 \x03(\x11\"P\n\x17GetViUInt32ArrayRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tarray_len\x18\x02 \x01(\x11\"A\n\x18GetViUInt32ArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\ru_int32_array\x18\x02 \x03(\r\"\x92\x01\n(MethodUsingEnumWithGrpcNameValuesRequest\x12\x39\n\nusing_enum\x18\x01 \x01(\x0e\x32#.nifake_grpc.EnumWithGrpcNameValuesH\x00\x12\x18\n\x0eusing_enum_raw\x18\x02 \x01(\x11H\x00\x42\x11\n\x0fusing_enum_enum\";\n)MethodUsingEnumWithGrpcNameValuesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"$\n\"MethodWithGetLastErrorParamRequest\"M\n#MethodWithGetLastErrorParamResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x16\n\nlast_error\x18\x02 \x01(\tB\x02\x18\x01\"6\n\x1eMethodWithGrpcOnlyParamRequest\x12\x14\n\x0csimple_param\x18\x01 \x01(\x11\"J\n\x1fMethodWithGrpcOnlyParamResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fgrpc_only_param\x18\x02 \x01(\x11\"-\n+MethodUsingWholeAndFractionalNumbersRequest\"\xf1\x01\n,MethodUsingWholeAndFractionalNumbersResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x35\n\x0cwhole_number\x18\x02 \x01(\x0e\x32\x1f.nifake_grpc.DecimalWholeNumber\x12\x18\n\x10whole_number_raw\x18\x03 \x01(\x11\x12\x41\n\x18\x66ractional_number_mapped\x18\x04 \x01(\x0e\x32\x1f.nifake_grpc.DecimalMixedNumber\x12\x1d\n\x15\x66ractional_number_raw\x18\x05 \x01(\x01\"&\n$MethodUsingWholeMappedNumbersRequest\"\x95\x01\n%MethodUsingWholeMappedNumbersResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x42\n\x13whole_number_mapped\x18\x02 \x01(\x0e\x32%.nifake_grpc.DecimalWholeNumberMapped\x12\x18\n\x10whole_number_raw\x18\x03 \x01(\x01\";\n MethodWithGrpcFieldNumberRequest\x12\x17\n\x0f\x61ttribute_value\x18\x05 \x01(\x11\"3\n!MethodWithGrpcFieldNumberResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\">\n#MethodWithProtoOnlyParameterRequest\x12\x17\n\x0f\x61ttribute_value\x18\x01 \x01(\x11\"6\n$MethodWithProtoOnlyParameterResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\"\n ReadDataWithInOutIviTwistRequest\"V\n!ReadDataWithInOutIviTwistResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x03(\x11\x12\x13\n\x0b\x62uffer_size\x18\x03 \x01(\x11\".\n,ReadDataWithMultipleIviTwistParamSetsRequest\"\x9b\x01\n-ReadDataWithMultipleIviTwistParamSetsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\tarray_out\x18\x02 \x03(\x11\x12\x13\n\x0b\x61\x63tual_size\x18\x03 \x01(\x11\x12\x17\n\x0fother_array_out\x18\x04 \x03(\x11\x12\x19\n\x11other_actual_size\x18\x05 \x01(\x11\"^\n\x11InitExtCalRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x1c\n\x14\x63\x61libration_password\x18\x03 \x01(\t\"H\n\x12InitExtCalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\"\n\x02vi\x18\x02 \x01(\x0b\x32\x16.nidevice_grpc.Session\"|\n\x16InitWithVarArgsRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x35\n\x0fname_and_turtle\x18\x03 \x03(\x0b\x32\x1c.nifake_grpc.StringAndTurtle\"M\n\x17InitWithVarArgsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\"\n\x02vi\x18\x02 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\xc3\x01\n)MultipleArraysSameSizeWithOptionalRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0f\n\x07values1\x18\x02 \x03(\x01\x12\x0f\n\x07values2\x18\x03 \x03(\x01\x12\x0f\n\x07values3\x18\x04 \x03(\x01\x12\x0f\n\x07values4\x18\x05 \x03(\x01\x12.\n\x07values5\x18\x06 \x03(\x0b\x32\x1d.nifake_grpc.FakeCustomStruct\"<\n*MultipleArraysSameSizeWithOptionalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"l\n UseATwoDimensionParameterRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\r\n\x05\x61rray\x18\x02 \x03(\x11\x12\x15\n\rarray_lengths\x18\x03 \x03(\x11\"3\n!UseATwoDimensionParameterResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"t\n ViUInt8ArrayInputFunctionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x1a\n\x12number_of_elements\x18\x02 \x01(\x11\x12\x10\n\x08\x61n_array\x18\x03 \x01(\x0c\"3\n!ViUInt8ArrayInputFunctionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"c\n!ViUInt8ArrayOutputFunctionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x1a\n\x12number_of_elements\x18\x02 \x01(\x11\"F\n\"ViUInt8ArrayOutputFunctionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08\x61n_array\x18\x02 \x01(\x0c\"X\n ViInt16ArrayInputFunctionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x10\n\x08\x61n_array\x18\x02 \x03(\x11\"3\n!ViInt16ArrayInputFunctionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05*\x9e\x05\n\x0fNiFakeAttribute\x12 \n\x1cNIFAKE_ATTRIBUTE_UNSPECIFIED\x10\x00\x12&\n NIFAKE_ATTRIBUTE_READ_WRITE_BOOL\x10\xc0\x84=\x12(\n\"NIFAKE_ATTRIBUTE_READ_WRITE_DOUBLE\x10\xc1\x84=\x12(\n\"NIFAKE_ATTRIBUTE_READ_WRITE_STRING\x10\xc2\x84=\x12\'\n!NIFAKE_ATTRIBUTE_READ_WRITE_COLOR\x10\xc3\x84=\x12)\n#NIFAKE_ATTRIBUTE_READ_WRITE_INTEGER\x10\xc4\x84=\x12/\n)NIFAKE_ATTRIBUTE_FLOAT_ENUM_NAME_OVERRIDE\x10\xc5\x84=\x12\'\n!NIFAKE_ATTRIBUTE_READ_WRITE_INT64\x10\xc6\x84=\x12\x37\n1NIFAKE_ATTRIBUTE_READ_WRITE_DOUBLE_WITH_CONVERTER\x10\xc7\x84=\x12\x38\n2NIFAKE_ATTRIBUTE_READ_WRITE_INTEGER_WITH_CONVERTER\x10\xc8\x84=\x12\x41\n;NIFAKE_ATTRIBUTE_READ_WRITE_DOUBLE_WITH_REPEATED_CAPABILITY\x10\xc9\x84=\x12<\n6NIFAKE_ATTRIBUTE_READ_WRITE_STRING_REPEATED_CAPABILITY\x10\xca\x84=\x12#\n\x1dNIFAKE_ATTRIBUTE_SAMPLE_COUNT\x10\xcc\x84=\x12&\n NIFAKE_ATTRIBUTE_SAMPLE_INTERVAL\x10\xcd\x84=*\xb2\x01\n\x11GrpcColorOverride\x12#\n\x1fGRPC_COLOR_OVERRIDE_UNSPECIFIED\x10\x00\x12\x1b\n\x17GRPC_COLOR_OVERRIDE_RED\x10\x01\x12\x1c\n\x18GRPC_COLOR_OVERRIDE_BLUE\x10\x02\x12\x1e\n\x1aGRPC_COLOR_OVERRIDE_YELLOW\x10\x05\x12\x1d\n\x19GRPC_COLOR_OVERRIDE_BLACK\x10**\xc8\x01\n\tFloatEnum\x12\x1a\n\x16\x46LOAT_ENUM_UNSPECIFIED\x10\x00\x12\x1f\n\x1b\x46LOAT_ENUM_THREE_POINT_FIVE\x10\x01\x12\x1e\n\x1a\x46LOAT_ENUM_FOUR_POINT_FIVE\x10\x02\x12\x1e\n\x1a\x46LOAT_ENUM_FIVE_POINT_FIVE\x10\x03\x12\x1d\n\x19\x46LOAT_ENUM_SIX_POINT_FIVE\x10\x04\x12\x1f\n\x1b\x46LOAT_ENUM_SEVEN_POINT_FIVE\x10\x05*`\n\x06Turtle\x12\x13\n\x0fTURTLE_LEONARDO\x10\x00\x12\x14\n\x10TURTLE_DONATELLO\x10\x01\x12\x12\n\x0eTURTLE_RAPHAEL\x10\x02\x12\x17\n\x13TURTLE_MICHELANGELO\x10\x03*\x80\x01\n\rMobileOSNames\x12\x1f\n\x1bMOBILE_OS_NAMES_UNSPECIFIED\x10\x00\x12\x1b\n\x17MOBILE_OS_NAMES_ANDROID\x10\x01\x12\x17\n\x13MOBILE_OS_NAMES_IOS\x10\x02\x12\x18\n\x14MOBILE_OS_NAMES_NONE\x10\x03*x\n\x08\x42itfield\x12\x18\n\x14\x42ITFIELD_UNSPECIFIED\x10\x00\x12\x13\n\x0f\x42ITFIELD_FLAG_A\x10\x01\x12\x13\n\x0f\x42ITFIELD_FLAG_B\x10\x02\x12\x13\n\x0f\x42ITFIELD_FLAG_C\x10\x04\x12\x13\n\x0f\x42ITFIELD_FLAG_D\x10\x08*\x88\x01\n\x12\x44\x65\x63imalWholeNumber\x12\x1d\n\x19\x44\x45\x43IMAL_WHOLE_NUMBER_ZERO\x10\x00\x12.\n!DECIMAL_WHOLE_NUMBER_NEGATIVE_ONE\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12#\n\x1f\x44\x45\x43IMAL_WHOLE_NUMBER_TWENTY_TWO\x10\x16*\xc7\x01\n\x18\x44\x65\x63imalWholeNumberMapped\x12+\n\'DECIMAL_WHOLE_NUMBER_MAPPED_UNSPECIFIED\x10\x00\x12$\n DECIMAL_WHOLE_NUMBER_MAPPED_ZERO\x10\x01\x12,\n(DECIMAL_WHOLE_NUMBER_MAPPED_NEGATIVE_ONE\x10\x02\x12*\n&DECIMAL_WHOLE_NUMBER_MAPPED_TWENTY_TWO\x10\x03*\xd7\x02\n\x12\x44\x65\x63imalMixedNumber\x12$\n DECIMAL_MIXED_NUMBER_UNSPECIFIED\x10\x00\x12#\n\x1f\x44\x45\x43IMAL_MIXED_NUMBER_TWENTY_TWO\x10\x01\x12&\n\"DECIMAL_MIXED_NUMBER_TWO_POINT_TWO\x10\x02\x12\'\n#DECIMAL_MIXED_NUMBER_NEGATIVE_THREE\x10\x03\x12#\n\x1f\x44\x45\x43IMAL_MIXED_NUMBER_MAX_INT_32\x10\x04\x12,\n(DECIMAL_MIXED_NUMBER_MAX_INT_32_PLUS_ONE\x10\x05\x12#\n\x1f\x44\x45\x43IMAL_MIXED_NUMBER_MIN_INT_32\x10\x06\x12-\n)DECIMAL_MIXED_NUMBER_MIN_INT_32_MINUS_ONE\x10\x07*\x9e\x01\n\x16\x45numWithGrpcNameValues\x12*\n&ENUM_WITH_GRPC_NAME_VALUES_UNSPECIFIED\x10\x00\x12\x34\n0ENUM_WITH_GRPC_NAME_VALUES_ALTERED_GRPC_NAME_ONE\x10\x01\x12\"\n\x1e\x45NUM_WITH_GRPC_NAME_VALUES_TWO\x10\x02*5\n\x0bSampleCount\x12&\n\"SAMPLE_COUNT_SAMPLE_COUNT_INFINITE\x10\x00*Z\n\x0eSampleInterval\x12\x1f\n\x1bSAMPLE_INTERVAL_UNSPECIFIED\x10\x00\x12\'\n\x1aSAMPLE_INTERVAL_AUTO_DELAY\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01*\xa1\x02\n\x1aNiFakeInt32AttributeValues\x12\x1c\n\x18NIFAKE_INT32_UNSPECIFIED\x10\x00\x12(\n$NIFAKE_INT32_GRPC_COLOR_OVERRIDE_RED\x10\x01\x12)\n%NIFAKE_INT32_GRPC_COLOR_OVERRIDE_BLUE\x10\x02\x12+\n\'NIFAKE_INT32_GRPC_COLOR_OVERRIDE_YELLOW\x10\x05\x12*\n&NIFAKE_INT32_GRPC_COLOR_OVERRIDE_BLACK\x10*\x12\x33\n/NIFAKE_INT32_SAMPLE_COUNT_SAMPLE_COUNT_INFINITE\x10\x00\x1a\x02\x10\x01*s\n\x1bNiFakeReal64AttributeValues\x12\x1d\n\x19NIFAKE_REAL64_UNSPECIFIED\x10\x00\x12\x35\n(NIFAKE_REAL64_SAMPLE_INTERVAL_AUTO_DELAY\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01*\xb0\x02\n!NiFakeReal64AttributeValuesMapped\x12$\n NIFAKE_REAL64_MAPPED_UNSPECIFIED\x10\x00\x12-\n)NIFAKE_REAL64_FLOAT_ENUM_THREE_POINT_FIVE\x10\x01\x12,\n(NIFAKE_REAL64_FLOAT_ENUM_FOUR_POINT_FIVE\x10\x02\x12,\n(NIFAKE_REAL64_FLOAT_ENUM_FIVE_POINT_FIVE\x10\x03\x12+\n\'NIFAKE_REAL64_FLOAT_ENUM_SIX_POINT_FIVE\x10\x04\x12-\n)NIFAKE_REAL64_FLOAT_ENUM_SEVEN_POINT_FIVE\x10\x05\x32\xad_\n\x06NiFake\x12>\n\x05\x41\x62ort\x12\x19.nifake_grpc.AbortRequest\x1a\x1a.nifake_grpc.AbortResponse\x12t\n\x17\x42oolArrayOutputFunction\x12+.nifake_grpc.BoolArrayOutputFunctionRequest\x1a,.nifake_grpc.BoolArrayOutputFunctionResponse\x12>\n\x05\x43lose\x12\x19.nifake_grpc.CloseRequest\x1a\x1a.nifake_grpc.CloseResponse\x12t\n\x17\x45numArrayOutputFunction\x12+.nifake_grpc.EnumArrayOutputFunctionRequest\x1a,.nifake_grpc.EnumArrayOutputFunctionResponse\x12\x86\x01\n\x1d\x45numInputFunctionWithDefaults\x12\x31.nifake_grpc.EnumInputFunctionWithDefaultsRequest\x1a\x32.nifake_grpc.EnumInputFunctionWithDefaultsResponse\x12\xaa\x01\n)StringValuedEnumInputFunctionWithDefaults\x12=.nifake_grpc.StringValuedEnumInputFunctionWithDefaultsRequest\x1a>.nifake_grpc.StringValuedEnumInputFunctionWithDefaultsResponse\x12S\n\x0c\x45rrorMessage\x12 .nifake_grpc.ErrorMessageRequest\x1a!.nifake_grpc.ErrorMessageResponse\x12V\n\rFetchWaveform\x12!.nifake_grpc.FetchWaveformRequest\x1a\".nifake_grpc.FetchWaveformResponse\x12P\n\x0bGetABoolean\x12\x1f.nifake_grpc.GetABooleanRequest\x1a .nifake_grpc.GetABooleanResponse\x12M\n\nGetANumber\x12\x1e.nifake_grpc.GetANumberRequest\x1a\x1f.nifake_grpc.GetANumberResponse\x12\x83\x01\n\x1cGetAStringOfFixedMaximumSize\x12\x30.nifake_grpc.GetAStringOfFixedMaximumSizeRequest\x1a\x31.nifake_grpc.GetAStringOfFixedMaximumSizeResponse\x12q\n\x16GetAnIviDanceCharArray\x12*.nifake_grpc.GetAnIviDanceCharArrayRequest\x1a+.nifake_grpc.GetAnIviDanceCharArrayResponse\x12n\n\x15GetArrayUsingIviDance\x12).nifake_grpc.GetArrayUsingIviDanceRequest\x1a*.nifake_grpc.GetArrayUsingIviDanceResponse\x12n\n\x15GetAttributeViBoolean\x12).nifake_grpc.GetAttributeViBooleanRequest\x1a*.nifake_grpc.GetAttributeViBooleanResponse\x12h\n\x13GetAttributeViInt32\x12\'.nifake_grpc.GetAttributeViInt32Request\x1a(.nifake_grpc.GetAttributeViInt32Response\x12h\n\x13GetAttributeViInt64\x12\'.nifake_grpc.GetAttributeViInt64Request\x1a(.nifake_grpc.GetAttributeViInt64Response\x12k\n\x14GetAttributeViReal64\x12(.nifake_grpc.GetAttributeViReal64Request\x1a).nifake_grpc.GetAttributeViReal64Response\x12n\n\x15GetAttributeViSession\x12).nifake_grpc.GetAttributeViSessionRequest\x1a*.nifake_grpc.GetAttributeViSessionResponse\x12k\n\x14GetAttributeViString\x12(.nifake_grpc.GetAttributeViStringRequest\x1a).nifake_grpc.GetAttributeViStringResponse\x12\x62\n\x11GetCalDateAndTime\x12%.nifake_grpc.GetCalDateAndTimeRequest\x1a&.nifake_grpc.GetCalDateAndTimeResponse\x12Y\n\x0eGetCalInterval\x12\".nifake_grpc.GetCalIntervalRequest\x1a#.nifake_grpc.GetCalIntervalResponse\x12S\n\x0cGetEnumValue\x12 .nifake_grpc.GetEnumValueRequest\x1a!.nifake_grpc.GetEnumValueResponse\x12G\n\x08GetError\x12\x1c.nifake_grpc.GetErrorRequest\x1a\x1d.nifake_grpc.GetErrorResponse\x12\\\n\x0fInitWithOptions\x12#.nifake_grpc.InitWithOptionsRequest\x1a$.nifake_grpc.InitWithOptionsResponse\x12\x65\n\x12MultipleArrayTypes\x12&.nifake_grpc.MultipleArrayTypesRequest\x1a\'.nifake_grpc.MultipleArrayTypesResponse\x12q\n\x16MultipleArraysSameSize\x12*.nifake_grpc.MultipleArraysSameSizeRequest\x1a+.nifake_grpc.MultipleArraysSameSizeResponse\x12\x80\x01\n\x1bMultipleArraysDifferentSize\x12/.nifake_grpc.MultipleArraysDifferentSizeRequest\x1a\x30.nifake_grpc.MultipleArraysDifferentSizeResponse\x12\x83\x01\n\x1cMixedIviDanceAndLenMechanism\x12\x30.nifake_grpc.MixedIviDanceAndLenMechanismRequest\x1a\x31.nifake_grpc.MixedIviDanceAndLenMechanismResponse\x12_\n\x10OneInputFunction\x12$.nifake_grpc.OneInputFunctionRequest\x1a%.nifake_grpc.OneInputFunctionResponse\x12}\n\x1aParametersAreMultipleTypes\x12..nifake_grpc.ParametersAreMultipleTypesRequest\x1a/.nifake_grpc.ParametersAreMultipleTypesResponse\x12z\n\x19PoorlyNamedSimpleFunction\x12-.nifake_grpc.PoorlyNamedSimpleFunctionRequest\x1a..nifake_grpc.PoorlyNamedSimpleFunctionResponse\x12;\n\x04Read\x12\x18.nifake_grpc.ReadRequest\x1a\x19.nifake_grpc.ReadResponse\x12\\\n\x0fReadFromChannel\x12#.nifake_grpc.ReadFromChannelRequest\x1a$.nifake_grpc.ReadFromChannelResponse\x12t\n\x17ReturnANumberAndAString\x12+.nifake_grpc.ReturnANumberAndAStringRequest\x1a,.nifake_grpc.ReturnANumberAndAStringResponse\x12h\n\x13ReturnMultipleTypes\x12\'.nifake_grpc.ReturnMultipleTypesRequest\x1a(.nifake_grpc.ReturnMultipleTypesResponse\x12n\n\x15SetAttributeViBoolean\x12).nifake_grpc.SetAttributeViBooleanRequest\x1a*.nifake_grpc.SetAttributeViBooleanResponse\x12h\n\x13SetAttributeViInt32\x12\'.nifake_grpc.SetAttributeViInt32Request\x1a(.nifake_grpc.SetAttributeViInt32Response\x12h\n\x13SetAttributeViInt64\x12\'.nifake_grpc.SetAttributeViInt64Request\x1a(.nifake_grpc.SetAttributeViInt64Response\x12k\n\x14SetAttributeViReal64\x12(.nifake_grpc.SetAttributeViReal64Request\x1a).nifake_grpc.SetAttributeViReal64Response\x12k\n\x14SetAttributeViString\x12(.nifake_grpc.SetAttributeViStringRequest\x1a).nifake_grpc.SetAttributeViStringResponse\x12_\n\x10TwoInputFunction\x12$.nifake_grpc.TwoInputFunctionRequest\x1a%.nifake_grpc.TwoInputFunctionResponse\x12Y\n\x0eUse64BitNumber\x12\".nifake_grpc.Use64BitNumberRequest\x1a#.nifake_grpc.Use64BitNumberResponse\x12V\n\rWriteWaveform\x12!.nifake_grpc.WriteWaveformRequest\x1a\".nifake_grpc.WriteWaveformResponse\x12\x83\x01\n\x1cWriteWaveformNumpyComplex128\x12\x30.nifake_grpc.WriteWaveformNumpyComplex128Request\x1a\x31.nifake_grpc.WriteWaveformNumpyComplex128Response\x12\x80\x01\n\x1bWriteWaveformNumpyComplex64\x12/.nifake_grpc.WriteWaveformNumpyComplex64Request\x1a\x30.nifake_grpc.WriteWaveformNumpyComplex64Response\x12\xa4\x01\n\'WriteWaveformNumpyComplexInterleavedI16\x12;.nifake_grpc.WriteWaveformNumpyComplexInterleavedI16Request\x1a<.nifake_grpc.WriteWaveformNumpyComplexInterleavedI16Response\x12V\n\rSetCustomType\x12!.nifake_grpc.SetCustomTypeRequest\x1a\".nifake_grpc.SetCustomTypeResponse\x12\x65\n\x12SetCustomTypeArray\x12&.nifake_grpc.SetCustomTypeArrayRequest\x1a\'.nifake_grpc.SetCustomTypeArrayResponse\x12V\n\rGetCustomType\x12!.nifake_grpc.GetCustomTypeRequest\x1a\".nifake_grpc.GetCustomTypeResponse\x12\x65\n\x12GetCustomTypeArray\x12&.nifake_grpc.GetCustomTypeArrayRequest\x1a\'.nifake_grpc.GetCustomTypeArrayResponse\x12\x83\x01\n\x1cGetAnIviDanceWithATwistArray\x12\x30.nifake_grpc.GetAnIviDanceWithATwistArrayRequest\x1a\x31.nifake_grpc.GetAnIviDanceWithATwistArrayResponse\x12\x86\x01\n\x1dGetAnIviDanceWithATwistString\x12\x31.nifake_grpc.GetAnIviDanceWithATwistStringRequest\x1a\x32.nifake_grpc.GetAnIviDanceWithATwistStringResponse\x12_\n\x10\x44oubleAllTheNums\x12$.nifake_grpc.DoubleAllTheNumsRequest\x1a%.nifake_grpc.DoubleAllTheNumsResponse\x12\x89\x01\n\x1e\x41\x63\x63\x65ptListOfDurationsInSeconds\x12\x32.nifake_grpc.AcceptListOfDurationsInSecondsRequest\x1a\x33.nifake_grpc.AcceptListOfDurationsInSecondsResponse\x12t\n\x17ReturnDurationInSeconds\x12+.nifake_grpc.ReturnDurationInSecondsRequest\x1a,.nifake_grpc.ReturnDurationInSecondsResponse\x12\x89\x01\n\x1eReturnListOfDurationsInSeconds\x12\x32.nifake_grpc.ReturnListOfDurationsInSecondsRequest\x1a\x33.nifake_grpc.ReturnListOfDurationsInSecondsResponse\x12S\n\x0c\x43onfigureAbc\x12 .nifake_grpc.ConfigureAbcRequest\x1a!.nifake_grpc.ConfigureAbcResponse\x12Y\n\x0e\x43onfigureEnums\x12\".nifake_grpc.ConfigureEnumsRequest\x1a#.nifake_grpc.ConfigureEnumsResponse\x12\x9b\x01\n$ExportAttributeConfigurationBufferEx\x12\x38.nifake_grpc.ExportAttributeConfigurationBufferExRequest\x1a\x39.nifake_grpc.ExportAttributeConfigurationBufferExResponse\x12\x9b\x01\n$ImportAttributeConfigurationBufferEx\x12\x38.nifake_grpc.ImportAttributeConfigurationBufferExRequest\x1a\x39.nifake_grpc.ImportAttributeConfigurationBufferExResponse\x12h\n\x13\x46\x65tchWithCustomSize\x12\'.nifake_grpc.FetchWithCustomSizeRequest\x1a(.nifake_grpc.FetchWithCustomSizeResponse\x12\x95\x01\n\"GetParameterWithOverriddenGrpcName\x12\x36.nifake_grpc.GetParameterWithOverriddenGrpcNameRequest\x1a\x37.nifake_grpc.GetParameterWithOverriddenGrpcNameResponse\x12\xc8\x01\n3IviDanceWithTwistWithMultipleArraysAndOneBufferSize\x12G.nifake_grpc.IviDanceWithTwistWithMultipleArraysAndOneBufferSizeRequest\x1aH.nifake_grpc.IviDanceWithTwistWithMultipleArraysAndOneBufferSizeResponse\x12\x8f\x01\n FunctionWithOverriddenGrpcName2x\x12\x34.nifake_grpc.FunctionWithOverriddenGrpcName2xRequest\x1a\x35.nifake_grpc.FunctionWithOverriddenGrpcName2xResponse\x12\xd4\x01\n7FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter\x12K.nifake_grpc.FunctionWith3dNumpyArrayOfNumpyComplex128InputParameterRequest\x1aL.nifake_grpc.FunctionWith3dNumpyArrayOfNumpyComplex128InputParameterResponse\x12\x8c\x01\n\x1fStringValuedEnumNoEnumGenerated\x12\x33.nifake_grpc.StringValuedEnumNoEnumGeneratedRequest\x1a\x34.nifake_grpc.StringValuedEnumNoEnumGeneratedResponse\x12\x98\x01\n#IviDanceWithATwistCalculatedSizeOut\x12\x37.nifake_grpc.IviDanceWithATwistCalculatedSizeOutRequest\x1a\x38.nifake_grpc.IviDanceWithATwistCalculatedSizeOutResponse\x12\x95\x01\n\"ImportAttributeConfigurationBuffer\x12\x36.nifake_grpc.ImportAttributeConfigurationBufferRequest\x1a\x37.nifake_grpc.ImportAttributeConfigurationBufferResponse\x12\x95\x01\n\"ExportAttributeConfigurationBuffer\x12\x36.nifake_grpc.ExportAttributeConfigurationBufferRequest\x1a\x37.nifake_grpc.ExportAttributeConfigurationBufferResponse\x12P\n\x0b\x43ontrol4022\x12\x1f.nifake_grpc.Control4022Request\x1a .nifake_grpc.Control4022Response\x12k\n\x14\x41\x63\x63\x65ptViSessionArray\x12(.nifake_grpc.AcceptViSessionArrayRequest\x1a).nifake_grpc.AcceptViSessionArrayResponse\x12h\n\x13\x41\x63\x63\x65ptViUInt32Array\x12\'.nifake_grpc.AcceptViUInt32ArrayRequest\x1a(.nifake_grpc.AcceptViUInt32ArrayResponse\x12q\n\x16\x42oolArrayInputFunction\x12*.nifake_grpc.BoolArrayInputFunctionRequest\x1a+.nifake_grpc.BoolArrayInputFunctionResponse\x12P\n\x0b\x43loseExtCal\x12\x1f.nifake_grpc.CloseExtCalRequest\x1a .nifake_grpc.CloseExtCalResponse\x12w\n\x18\x43ommandWithReservedParam\x12,.nifake_grpc.CommandWithReservedParamRequest\x1a-.nifake_grpc.CommandWithReservedParamResponse\x12t\n\x17\x43reateConfigurationList\x12+.nifake_grpc.CreateConfigurationListRequest\x1a,.nifake_grpc.CreateConfigurationListResponse\x12\x80\x01\n\x1b\x43ustomNestedStructRoundtrip\x12/.nifake_grpc.CustomNestedStructRoundtripRequest\x1a\x30.nifake_grpc.CustomNestedStructRoundtripResponse\x12q\n\x16GetBitfieldAsEnumArray\x12*.nifake_grpc.GetBitfieldAsEnumArrayRequest\x1a+.nifake_grpc.GetBitfieldAsEnumArrayResponse\x12\xa7\x01\n(GetAnIviDanceWithATwistArrayOfCustomType\x12<.nifake_grpc.GetAnIviDanceWithATwistArrayOfCustomTypeRequest\x1a=.nifake_grpc.GetAnIviDanceWithATwistArrayOfCustomTypeResponse\x12\xad\x01\n*GetAnIviDanceWithATwistArrayWithInputArray\x12>.nifake_grpc.GetAnIviDanceWithATwistArrayWithInputArrayRequest\x1a?.nifake_grpc.GetAnIviDanceWithATwistArrayWithInputArrayResponse\x12\x8f\x01\n GetAnIviDanceWithATwistByteArray\x12\x34.nifake_grpc.GetAnIviDanceWithATwistByteArrayRequest\x1a\x35.nifake_grpc.GetAnIviDanceWithATwistByteArrayResponse\x12\xa1\x01\n&GetAnIviDanceWithATwistStringStrlenBug\x12:.nifake_grpc.GetAnIviDanceWithATwistStringStrlenBugRequest\x1a;.nifake_grpc.GetAnIviDanceWithATwistStringStrlenBugResponse\x12z\n\x19GetArraySizeForCustomCode\x12-.nifake_grpc.GetArraySizeForCustomCodeRequest\x1a..nifake_grpc.GetArraySizeForCustomCodeResponse\x12t\n\x17GetArrayViUInt8WithEnum\x12+.nifake_grpc.GetArrayViUInt8WithEnumRequest\x1a,.nifake_grpc.GetArrayViUInt8WithEnumResponse\x12M\n\nGetViUInt8\x12\x1e.nifake_grpc.GetViUInt8Request\x1a\x1f.nifake_grpc.GetViUInt8Response\x12\\\n\x0fGetViInt32Array\x12#.nifake_grpc.GetViInt32ArrayRequest\x1a$.nifake_grpc.GetViInt32ArrayResponse\x12_\n\x10GetViUInt32Array\x12$.nifake_grpc.GetViUInt32ArrayRequest\x1a%.nifake_grpc.GetViUInt32ArrayResponse\x12\x92\x01\n!MethodUsingEnumWithGrpcNameValues\x12\x35.nifake_grpc.MethodUsingEnumWithGrpcNameValuesRequest\x1a\x36.nifake_grpc.MethodUsingEnumWithGrpcNameValuesResponse\x12\x80\x01\n\x1bMethodWithGetLastErrorParam\x12/.nifake_grpc.MethodWithGetLastErrorParamRequest\x1a\x30.nifake_grpc.MethodWithGetLastErrorParamResponse\x12t\n\x17MethodWithGrpcOnlyParam\x12+.nifake_grpc.MethodWithGrpcOnlyParamRequest\x1a,.nifake_grpc.MethodWithGrpcOnlyParamResponse\x12\x9b\x01\n$MethodUsingWholeAndFractionalNumbers\x12\x38.nifake_grpc.MethodUsingWholeAndFractionalNumbersRequest\x1a\x39.nifake_grpc.MethodUsingWholeAndFractionalNumbersResponse\x12\x86\x01\n\x1dMethodUsingWholeMappedNumbers\x12\x31.nifake_grpc.MethodUsingWholeMappedNumbersRequest\x1a\x32.nifake_grpc.MethodUsingWholeMappedNumbersResponse\x12z\n\x19MethodWithGrpcFieldNumber\x12-.nifake_grpc.MethodWithGrpcFieldNumberRequest\x1a..nifake_grpc.MethodWithGrpcFieldNumberResponse\x12\x83\x01\n\x1cMethodWithProtoOnlyParameter\x12\x30.nifake_grpc.MethodWithProtoOnlyParameterRequest\x1a\x31.nifake_grpc.MethodWithProtoOnlyParameterResponse\x12z\n\x19ReadDataWithInOutIviTwist\x12-.nifake_grpc.ReadDataWithInOutIviTwistRequest\x1a..nifake_grpc.ReadDataWithInOutIviTwistResponse\x12\x9e\x01\n%ReadDataWithMultipleIviTwistParamSets\x12\x39.nifake_grpc.ReadDataWithMultipleIviTwistParamSetsRequest\x1a:.nifake_grpc.ReadDataWithMultipleIviTwistParamSetsResponse\x12M\n\nInitExtCal\x12\x1e.nifake_grpc.InitExtCalRequest\x1a\x1f.nifake_grpc.InitExtCalResponse\x12\\\n\x0fInitWithVarArgs\x12#.nifake_grpc.InitWithVarArgsRequest\x1a$.nifake_grpc.InitWithVarArgsResponse\x12\x95\x01\n\"MultipleArraysSameSizeWithOptional\x12\x36.nifake_grpc.MultipleArraysSameSizeWithOptionalRequest\x1a\x37.nifake_grpc.MultipleArraysSameSizeWithOptionalResponse\x12z\n\x19UseATwoDimensionParameter\x12-.nifake_grpc.UseATwoDimensionParameterRequest\x1a..nifake_grpc.UseATwoDimensionParameterResponse\x12z\n\x19ViUInt8ArrayInputFunction\x12-.nifake_grpc.ViUInt8ArrayInputFunctionRequest\x1a..nifake_grpc.ViUInt8ArrayInputFunctionResponse\x12}\n\x1aViUInt8ArrayOutputFunction\x12..nifake_grpc.ViUInt8ArrayOutputFunctionRequest\x1a/.nifake_grpc.ViUInt8ArrayOutputFunctionResponse\x12z\n\x19ViInt16ArrayInputFunction\x12-.nifake_grpc.ViInt16ArrayInputFunctionRequest\x1a..nifake_grpc.ViInt16ArrayInputFunctionResponseB<\n\x10\x63om.ni.grpc.fakeB\x06NiFakeP\x01\xaa\x02\x1dNationalInstruments.Grpc.Fakeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nifake_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\020com.ni.grpc.fakeB\006NiFakeP\001\252\002\035NationalInstruments.Grpc.Fake'
  _NIFAKEINT32ATTRIBUTEVALUES._options = None
  _NIFAKEINT32ATTRIBUTEVALUES._serialized_options = b'\020\001'
  _METHODWITHGETLASTERRORPARAMRESPONSE.fields_by_name['last_error']._options = None
  _METHODWITHGETLASTERRORPARAMRESPONSE.fields_by_name['last_error']._serialized_options = b'\030\001'
  _globals['_NIFAKEATTRIBUTE']._serialized_start=19367
  _globals['_NIFAKEATTRIBUTE']._serialized_end=20037
  _globals['_GRPCCOLOROVERRIDE']._serialized_start=20040
  _globals['_GRPCCOLOROVERRIDE']._serialized_end=20218
  _globals['_FLOATENUM']._serialized_start=20221
  _globals['_FLOATENUM']._serialized_end=20421
  _globals['_TURTLE']._serialized_start=20423
  _globals['_TURTLE']._serialized_end=20519
  _globals['_MOBILEOSNAMES']._serialized_start=20522
  _globals['_MOBILEOSNAMES']._serialized_end=20650
  _globals['_BITFIELD']._serialized_start=20652
  _globals['_BITFIELD']._serialized_end=20772
  _globals['_DECIMALWHOLENUMBER']._serialized_start=20775
  _globals['_DECIMALWHOLENUMBER']._serialized_end=20911
  _globals['_DECIMALWHOLENUMBERMAPPED']._serialized_start=20914
  _globals['_DECIMALWHOLENUMBERMAPPED']._serialized_end=21113
  _globals['_DECIMALMIXEDNUMBER']._serialized_start=21116
  _globals['_DECIMALMIXEDNUMBER']._serialized_end=21459
  _globals['_ENUMWITHGRPCNAMEVALUES']._serialized_start=21462
  _globals['_ENUMWITHGRPCNAMEVALUES']._serialized_end=21620
  _globals['_SAMPLECOUNT']._serialized_start=21622
  _globals['_SAMPLECOUNT']._serialized_end=21675
  _globals['_SAMPLEINTERVAL']._serialized_start=21677
  _globals['_SAMPLEINTERVAL']._serialized_end=21767
  _globals['_NIFAKEINT32ATTRIBUTEVALUES']._serialized_start=21770
  _globals['_NIFAKEINT32ATTRIBUTEVALUES']._serialized_end=22059
  _globals['_NIFAKEREAL64ATTRIBUTEVALUES']._serialized_start=22061
  _globals['_NIFAKEREAL64ATTRIBUTEVALUES']._serialized_end=22176
  _globals['_NIFAKEREAL64ATTRIBUTEVALUESMAPPED']._serialized_start=22179
  _globals['_NIFAKEREAL64ATTRIBUTEVALUESMAPPED']._serialized_end=22483
  _globals['_FAKECUSTOMSTRUCT']._serialized_start=44
  _globals['_FAKECUSTOMSTRUCT']._serialized_end=105
  _globals['_CUSTOMSTRUCTNESTEDTYPEDEF']._serialized_start=108
  _globals['_CUSTOMSTRUCTNESTEDTYPEDEF']._serialized_end=268
  _globals['_CUSTOMSTRUCTTYPEDEF']._serialized_start=270
  _globals['_CUSTOMSTRUCTTYPEDEF']._serialized_end=334
  _globals['_NICOMPLEXI16_STRUCT']._serialized_start=336
  _globals['_NICOMPLEXI16_STRUCT']._serialized_end=390
  _globals['_NICOMPLEXNUMBER_STRUCT']._serialized_start=392
  _globals['_NICOMPLEXNUMBER_STRUCT']._serialized_end=449
  _globals['_NICOMPLEXNUMBERF32_STRUCT']._serialized_start=451
  _globals['_NICOMPLEXNUMBERF32_STRUCT']._serialized_end=511
  _globals['_STRINGANDTURTLE']._serialized_start=513
  _globals['_STRINGANDTURTLE']._serialized_end=587
  _globals['_CUSTOMNAMEDTYPE']._serialized_start=589
  _globals['_CUSTOMNAMEDTYPE']._serialized_end=626
  _globals['_ABORTREQUEST']._serialized_start=628
  _globals['_ABORTREQUEST']._serialized_end=678
  _globals['_ABORTRESPONSE']._serialized_start=680
  _globals['_ABORTRESPONSE']._serialized_end=711
  _globals['_BOOLARRAYOUTPUTFUNCTIONREQUEST']._serialized_start=713
  _globals['_BOOLARRAYOUTPUTFUNCTIONREQUEST']._serialized_end=809
  _globals['_BOOLARRAYOUTPUTFUNCTIONRESPONSE']._serialized_start=811
  _globals['_BOOLARRAYOUTPUTFUNCTIONRESPONSE']._serialized_end=878
  _globals['_CLOSEREQUEST']._serialized_start=880
  _globals['_CLOSEREQUEST']._serialized_end=930
  _globals['_CLOSERESPONSE']._serialized_start=932
  _globals['_CLOSERESPONSE']._serialized_end=963
  _globals['_ENUMARRAYOUTPUTFUNCTIONREQUEST']._serialized_start=965
  _globals['_ENUMARRAYOUTPUTFUNCTIONREQUEST']._serialized_end=1061
  _globals['_ENUMARRAYOUTPUTFUNCTIONRESPONSE']._serialized_start=1063
  _globals['_ENUMARRAYOUTPUTFUNCTIONRESPONSE']._serialized_end=1173
  _globals['_ENUMINPUTFUNCTIONWITHDEFAULTSREQUEST']._serialized_start=1176
  _globals['_ENUMINPUTFUNCTIONWITHDEFAULTSREQUEST']._serialized_end=1332
  _globals['_ENUMINPUTFUNCTIONWITHDEFAULTSRESPONSE']._serialized_start=1334
  _globals['_ENUMINPUTFUNCTIONWITHDEFAULTSRESPONSE']._serialized_end=1389
  _globals['_STRINGVALUEDENUMINPUTFUNCTIONWITHDEFAULTSREQUEST']._serialized_start=1392
  _globals['_STRINGVALUEDENUMINPUTFUNCTIONWITHDEFAULTSREQUEST']._serialized_end=1598
  _globals['_STRINGVALUEDENUMINPUTFUNCTIONWITHDEFAULTSRESPONSE']._serialized_start=1600
  _globals['_STRINGVALUEDENUMINPUTFUNCTIONWITHDEFAULTSRESPONSE']._serialized_end=1667
  _globals['_ERRORMESSAGEREQUEST']._serialized_start=1669
  _globals['_ERRORMESSAGEREQUEST']._serialized_end=1746
  _globals['_ERRORMESSAGERESPONSE']._serialized_start=1748
  _globals['_ERRORMESSAGERESPONSE']._serialized_end=1809
  _globals['_FETCHWAVEFORMREQUEST']._serialized_start=1811
  _globals['_FETCHWAVEFORMREQUEST']._serialized_end=1896
  _globals['_FETCHWAVEFORMRESPONSE']._serialized_start=1898
  _globals['_FETCHWAVEFORMRESPONSE']._serialized_end=1994
  _globals['_GETABOOLEANREQUEST']._serialized_start=1996
  _globals['_GETABOOLEANREQUEST']._serialized_end=2052
  _globals['_GETABOOLEANRESPONSE']._serialized_start=2054
  _globals['_GETABOOLEANRESPONSE']._serialized_end=2110
  _globals['_GETANUMBERREQUEST']._serialized_start=2112
  _globals['_GETANUMBERREQUEST']._serialized_end=2167
  _globals['_GETANUMBERRESPONSE']._serialized_start=2169
  _globals['_GETANUMBERRESPONSE']._serialized_end=2223
  _globals['_GETASTRINGOFFIXEDMAXIMUMSIZEREQUEST']._serialized_start=2225
  _globals['_GETASTRINGOFFIXEDMAXIMUMSIZEREQUEST']._serialized_end=2298
  _globals['_GETASTRINGOFFIXEDMAXIMUMSIZERESPONSE']._serialized_start=2300
  _globals['_GETASTRINGOFFIXEDMAXIMUMSIZERESPONSE']._serialized_end=2372
  _globals['_GETANIVIDANCECHARARRAYREQUEST']._serialized_start=2374
  _globals['_GETANIVIDANCECHARARRAYREQUEST']._serialized_end=2441
  _globals['_GETANIVIDANCECHARARRAYRESPONSE']._serialized_start=2443
  _globals['_GETANIVIDANCECHARARRAYRESPONSE']._serialized_end=2511
  _globals['_GETARRAYUSINGIVIDANCEREQUEST']._serialized_start=2513
  _globals['_GETARRAYUSINGIVIDANCEREQUEST']._serialized_end=2579
  _globals['_GETARRAYUSINGIVIDANCERESPONSE']._serialized_start=2581
  _globals['_GETARRAYUSINGIVIDANCERESPONSE']._serialized_end=2647
  _globals['_GETATTRIBUTEVIBOOLEANREQUEST']._serialized_start=2650
  _globals['_GETATTRIBUTEVIBOOLEANREQUEST']._serialized_end=2790
  _globals['_GETATTRIBUTEVIBOOLEANRESPONSE']._serialized_start=2792
  _globals['_GETATTRIBUTEVIBOOLEANRESPONSE']._serialized_end=2864
  _globals['_GETATTRIBUTEVIINT32REQUEST']._serialized_start=2867
  _globals['_GETATTRIBUTEVIINT32REQUEST']._serialized_end=3005
  _globals['_GETATTRIBUTEVIINT32RESPONSE']._serialized_start=3007
  _globals['_GETATTRIBUTEVIINT32RESPONSE']._serialized_end=3077
  _globals['_GETATTRIBUTEVIINT64REQUEST']._serialized_start=3080
  _globals['_GETATTRIBUTEVIINT64REQUEST']._serialized_end=3218
  _globals['_GETATTRIBUTEVIINT64RESPONSE']._serialized_start=3220
  _globals['_GETATTRIBUTEVIINT64RESPONSE']._serialized_end=3290
  _globals['_GETATTRIBUTEVIREAL64REQUEST']._serialized_start=3293
  _globals['_GETATTRIBUTEVIREAL64REQUEST']._serialized_end=3432
  _globals['_GETATTRIBUTEVIREAL64RESPONSE']._serialized_start=3434
  _globals['_GETATTRIBUTEVIREAL64RESPONSE']._serialized_end=3505
  _globals['_GETATTRIBUTEVISESSIONREQUEST']._serialized_start=3508
  _globals['_GETATTRIBUTEVISESSIONREQUEST']._serialized_end=3648
  _globals['_GETATTRIBUTEVISESSIONRESPONSE']._serialized_start=3650
  _globals['_GETATTRIBUTEVISESSIONRESPONSE']._serialized_end=3746
  _globals['_GETATTRIBUTEVISTRINGREQUEST']._serialized_start=3749
  _globals['_GETATTRIBUTEVISTRINGREQUEST']._serialized_end=3888
  _globals['_GETATTRIBUTEVISTRINGRESPONSE']._serialized_start=3890
  _globals['_GETATTRIBUTEVISTRINGRESPONSE']._serialized_end=3961
  _globals['_GETCALDATEANDTIMEREQUEST']._serialized_start=3963
  _globals['_GETCALDATEANDTIMEREQUEST']._serialized_end=4043
  _globals['_GETCALDATEANDTIMERESPONSE']._serialized_start=4045
  _globals['_GETCALDATEANDTIMERESPONSE']._serialized_end=4160
  _globals['_GETCALINTERVALREQUEST']._serialized_start=4162
  _globals['_GETCALINTERVALREQUEST']._serialized_end=4221
  _globals['_GETCALINTERVALRESPONSE']._serialized_start=4223
  _globals['_GETCALINTERVALRESPONSE']._serialized_end=4279
  _globals['_GETENUMVALUEREQUEST']._serialized_start=4281
  _globals['_GETENUMVALUEREQUEST']._serialized_end=4338
  _globals['_GETENUMVALUERESPONSE']._serialized_start=4340
  _globals['_GETENUMVALUERESPONSE']._serialized_end=4459
  _globals['_GETERRORREQUEST']._serialized_start=4461
  _globals['_GETERRORREQUEST']._serialized_end=4514
  _globals['_GETERRORRESPONSE']._serialized_start=4516
  _globals['_GETERRORRESPONSE']._serialized_end=4591
  _globals['_INITWITHOPTIONSREQUEST']._serialized_start=4594
  _globals['_INITWITHOPTIONSREQUEST']._serialized_end=4805
  _globals['_INITWITHOPTIONSRESPONSE']._serialized_start=4807
  _globals['_INITWITHOPTIONSRESPONSE']._serialized_end=4917
  _globals['_MULTIPLEARRAYTYPESREQUEST']._serialized_start=4920
  _globals['_MULTIPLEARRAYTYPESREQUEST']._serialized_end=5074
  _globals['_MULTIPLEARRAYTYPESRESPONSE']._serialized_start=5076
  _globals['_MULTIPLEARRAYTYPESRESPONSE']._serialized_end=5180
  _globals['_MULTIPLEARRAYSSAMESIZEREQUEST']._serialized_start=5183
  _globals['_MULTIPLEARRAYSSAMESIZEREQUEST']._serialized_end=5318
  _globals['_MULTIPLEARRAYSSAMESIZERESPONSE']._serialized_start=5320
  _globals['_MULTIPLEARRAYSSAMESIZERESPONSE']._serialized_end=5368
  _globals['_MULTIPLEARRAYSDIFFERENTSIZEREQUEST']._serialized_start=5370
  _globals['_MULTIPLEARRAYSDIFFERENTSIZEREQUEST']._serialized_end=5484
  _globals['_MULTIPLEARRAYSDIFFERENTSIZERESPONSE']._serialized_start=5486
  _globals['_MULTIPLEARRAYSDIFFERENTSIZERESPONSE']._serialized_end=5539
  _globals['_MIXEDIVIDANCEANDLENMECHANISMREQUEST']._serialized_start=5541
  _globals['_MIXEDIVIDANCEANDLENMECHANISMREQUEST']._serialized_end=5636
  _globals['_MIXEDIVIDANCEANDLENMECHANISMRESPONSE']._serialized_start=5638
  _globals['_MIXEDIVIDANCEANDLENMECHANISMRESPONSE']._serialized_end=5714
  _globals['_ONEINPUTFUNCTIONREQUEST']._serialized_start=5716
  _globals['_ONEINPUTFUNCTIONREQUEST']._serialized_end=5795
  _globals['_ONEINPUTFUNCTIONRESPONSE']._serialized_start=5797
  _globals['_ONEINPUTFUNCTIONRESPONSE']._serialized_end=5839
  _globals['_PARAMETERSAREMULTIPLETYPESREQUEST']._serialized_start=5842
  _globals['_PARAMETERSAREMULTIPLETYPESREQUEST']._serialized_end=6198
  _globals['_PARAMETERSAREMULTIPLETYPESRESPONSE']._serialized_start=6200
  _globals['_PARAMETERSAREMULTIPLETYPESRESPONSE']._serialized_end=6252
  _globals['_POORLYNAMEDSIMPLEFUNCTIONREQUEST']._serialized_start=6254
  _globals['_POORLYNAMEDSIMPLEFUNCTIONREQUEST']._serialized_end=6324
  _globals['_POORLYNAMEDSIMPLEFUNCTIONRESPONSE']._serialized_start=6326
  _globals['_POORLYNAMEDSIMPLEFUNCTIONRESPONSE']._serialized_end=6377
  _globals['_READREQUEST']._serialized_start=6379
  _globals['_READREQUEST']._serialized_end=6450
  _globals['_READRESPONSE']._serialized_start=6452
  _globals['_READRESPONSE']._serialized_end=6499
  _globals['_READFROMCHANNELREQUEST']._serialized_start=6501
  _globals['_READFROMCHANNELREQUEST']._serialized_end=6605
  _globals['_READFROMCHANNELRESPONSE']._serialized_start=6607
  _globals['_READFROMCHANNELRESPONSE']._serialized_end=6665
  _globals['_RETURNANUMBERANDASTRINGREQUEST']._serialized_start=6667
  _globals['_RETURNANUMBERANDASTRINGREQUEST']._serialized_end=6735
  _globals['_RETURNANUMBERANDASTRINGRESPONSE']._serialized_start=6737
  _globals['_RETURNANUMBERANDASTRINGRESPONSE']._serialized_end=6822
  _globals['_RETURNMULTIPLETYPESREQUEST']._serialized_start=6824
  _globals['_RETURNMULTIPLETYPESREQUEST']._serialized_end=6908
  _globals['_RETURNMULTIPLETYPESRESPONSE']._serialized_start=6911
  _globals['_RETURNMULTIPLETYPESRESPONSE']._serialized_end=7210
  _globals['_SETATTRIBUTEVIBOOLEANREQUEST']._serialized_start=7213
  _globals['_SETATTRIBUTEVIBOOLEANREQUEST']._serialized_end=7378
  _globals['_SETATTRIBUTEVIBOOLEANRESPONSE']._serialized_start=7380
  _globals['_SETATTRIBUTEVIBOOLEANRESPONSE']._serialized_end=7427
  _globals['_SETATTRIBUTEVIINT32REQUEST']._serialized_start=7430
  _globals['_SETATTRIBUTEVIINT32REQUEST']._serialized_end=7691
  _globals['_SETATTRIBUTEVIINT32RESPONSE']._serialized_start=7693
  _globals['_SETATTRIBUTEVIINT32RESPONSE']._serialized_end=7738
  _globals['_SETATTRIBUTEVIINT64REQUEST']._serialized_start=7741
  _globals['_SETATTRIBUTEVIINT64REQUEST']._serialized_end=7908
  _globals['_SETATTRIBUTEVIINT64RESPONSE']._serialized_start=7910
  _globals['_SETATTRIBUTEVIINT64RESPONSE']._serialized_end=7955
  _globals['_SETATTRIBUTEVIREAL64REQUEST']._serialized_start=7958
  _globals['_SETATTRIBUTEVIREAL64REQUEST']._serialized_end=8303
  _globals['_SETATTRIBUTEVIREAL64RESPONSE']._serialized_start=8305
  _globals['_SETATTRIBUTEVIREAL64RESPONSE']._serialized_end=8351
  _globals['_SETATTRIBUTEVISTRINGREQUEST']._serialized_start=8354
  _globals['_SETATTRIBUTEVISTRINGREQUEST']._serialized_end=8522
  _globals['_SETATTRIBUTEVISTRINGRESPONSE']._serialized_start=8524
  _globals['_SETATTRIBUTEVISTRINGRESPONSE']._serialized_end=8570
  _globals['_TWOINPUTFUNCTIONREQUEST']._serialized_start=8572
  _globals['_TWOINPUTFUNCTIONREQUEST']._serialized_end=8669
  _globals['_TWOINPUTFUNCTIONRESPONSE']._serialized_start=8671
  _globals['_TWOINPUTFUNCTIONRESPONSE']._serialized_end=8713
  _globals['_USE64BITNUMBERREQUEST']._serialized_start=8715
  _globals['_USE64BITNUMBERREQUEST']._serialized_end=8789
  _globals['_USE64BITNUMBERRESPONSE']._serialized_start=8791
  _globals['_USE64BITNUMBERRESPONSE']._serialized_end=8847
  _globals['_WRITEWAVEFORMREQUEST']._serialized_start=8849
  _globals['_WRITEWAVEFORMREQUEST']._serialized_end=8925
  _globals['_WRITEWAVEFORMRESPONSE']._serialized_start=8927
  _globals['_WRITEWAVEFORMRESPONSE']._serialized_end=8966
  _globals['_WRITEWAVEFORMNUMPYCOMPLEX128REQUEST']._serialized_start=8969
  _globals['_WRITEWAVEFORMNUMPYCOMPLEX128REQUEST']._serialized_end=9108
  _globals['_WRITEWAVEFORMNUMPYCOMPLEX128RESPONSE']._serialized_start=9110
  _globals['_WRITEWAVEFORMNUMPYCOMPLEX128RESPONSE']._serialized_end=9164
  _globals['_WRITEWAVEFORMNUMPYCOMPLEX64REQUEST']._serialized_start=9167
  _globals['_WRITEWAVEFORMNUMPYCOMPLEX64REQUEST']._serialized_end=9308
  _globals['_WRITEWAVEFORMNUMPYCOMPLEX64RESPONSE']._serialized_start=9310
  _globals['_WRITEWAVEFORMNUMPYCOMPLEX64RESPONSE']._serialized_end=9363
  _globals['_WRITEWAVEFORMNUMPYCOMPLEXINTERLEAVEDI16REQUEST']._serialized_start=9366
  _globals['_WRITEWAVEFORMNUMPYCOMPLEXINTERLEAVEDI16REQUEST']._serialized_end=9513
  _globals['_WRITEWAVEFORMNUMPYCOMPLEXINTERLEAVEDI16RESPONSE']._serialized_start=9515
  _globals['_WRITEWAVEFORMNUMPYCOMPLEXINTERLEAVEDI16RESPONSE']._serialized_end=9580
  _globals['_SETCUSTOMTYPEREQUEST']._serialized_start=9582
  _globals['_SETCUSTOMTYPEREQUEST']._serialized_end=9683
  _globals['_SETCUSTOMTYPERESPONSE']._serialized_start=9685
  _globals['_SETCUSTOMTYPERESPONSE']._serialized_end=9724
  _globals['_SETCUSTOMTYPEARRAYREQUEST']._serialized_start=9726
  _globals['_SETCUSTOMTYPEARRAYREQUEST']._serialized_end=9832
  _globals['_SETCUSTOMTYPEARRAYRESPONSE']._serialized_start=9834
  _globals['_SETCUSTOMTYPEARRAYRESPONSE']._serialized_end=9878
  _globals['_GETCUSTOMTYPEREQUEST']._serialized_start=9880
  _globals['_GETCUSTOMTYPEREQUEST']._serialized_end=9938
  _globals['_GETCUSTOMTYPERESPONSE']._serialized_start=9940
  _globals['_GETCUSTOMTYPERESPONSE']._serialized_end=10022
  _globals['_GETCUSTOMTYPEARRAYREQUEST']._serialized_start=10024
  _globals['_GETCUSTOMTYPEARRAYREQUEST']._serialized_end=10115
  _globals['_GETCUSTOMTYPEARRAYRESPONSE']._serialized_start=10117
  _globals['_GETCUSTOMTYPEARRAYRESPONSE']._serialized_end=10204
  _globals['_GETANIVIDANCEWITHATWISTARRAYREQUEST']._serialized_start=10206
  _globals['_GETANIVIDANCEWITHATWISTARRAYREQUEST']._serialized_end=10297
  _globals['_GETANIVIDANCEWITHATWISTARRAYRESPONSE']._serialized_start=10299
  _globals['_GETANIVIDANCEWITHATWISTARRAYRESPONSE']._serialized_end=10393
  _globals['_GETANIVIDANCEWITHATWISTSTRINGREQUEST']._serialized_start=10395
  _globals['_GETANIVIDANCEWITHATWISTSTRINGREQUEST']._serialized_end=10469
  _globals['_GETANIVIDANCEWITHATWISTSTRINGRESPONSE']._serialized_start=10471
  _globals['_GETANIVIDANCEWITHATWISTSTRINGRESPONSE']._serialized_end=10565
  _globals['_DOUBLEALLTHENUMSREQUEST']._serialized_start=10567
  _globals['_DOUBLEALLTHENUMSREQUEST']._serialized_end=10645
  _globals['_DOUBLEALLTHENUMSRESPONSE']._serialized_start=10647
  _globals['_DOUBLEALLTHENUMSRESPONSE']._serialized_end=10689
  _globals['_ACCEPTLISTOFDURATIONSINSECONDSREQUEST']._serialized_start=10691
  _globals['_ACCEPTLISTOFDURATIONSINSECONDSREQUEST']._serialized_end=10782
  _globals['_ACCEPTLISTOFDURATIONSINSECONDSRESPONSE']._serialized_start=10784
  _globals['_ACCEPTLISTOFDURATIONSINSECONDSRESPONSE']._serialized_end=10840
  _globals['_RETURNDURATIONINSECONDSREQUEST']._serialized_start=10842
  _globals['_RETURNDURATIONINSECONDSREQUEST']._serialized_end=10910
  _globals['_RETURNDURATIONINSECONDSRESPONSE']._serialized_start=10912
  _globals['_RETURNDURATIONINSECONDSRESPONSE']._serialized_end=10980
  _globals['_RETURNLISTOFDURATIONSINSECONDSREQUEST']._serialized_start=10982
  _globals['_RETURNLISTOFDURATIONSINSECONDSREQUEST']._serialized_end=11085
  _globals['_RETURNLISTOFDURATIONSINSECONDSRESPONSE']._serialized_start=11087
  _globals['_RETURNLISTOFDURATIONSINSECONDSRESPONSE']._serialized_end=11163
  _globals['_CONFIGUREABCREQUEST']._serialized_start=11165
  _globals['_CONFIGUREABCREQUEST']._serialized_end=11222
  _globals['_CONFIGUREABCRESPONSE']._serialized_start=11224
  _globals['_CONFIGUREABCRESPONSE']._serialized_end=11262
  _globals['_CONFIGUREENUMSREQUEST']._serialized_start=11265
  _globals['_CONFIGUREENUMSREQUEST']._serialized_end=11534
  _globals['_CONFIGUREENUMSRESPONSE']._serialized_start=11536
  _globals['_CONFIGUREENUMSRESPONSE']._serialized_end=11576
  _globals['_EXPORTATTRIBUTECONFIGURATIONBUFFEREXREQUEST']._serialized_start=11578
  _globals['_EXPORTATTRIBUTECONFIGURATIONBUFFEREXREQUEST']._serialized_end=11659
  _globals['_EXPORTATTRIBUTECONFIGURATIONBUFFEREXRESPONSE']._serialized_start=11661
  _globals['_EXPORTATTRIBUTECONFIGURATIONBUFFEREXRESPONSE']._serialized_end=11746
  _globals['_IMPORTATTRIBUTECONFIGURATIONBUFFEREXREQUEST']._serialized_start=11748
  _globals['_IMPORTATTRIBUTECONFIGURATIONBUFFEREXREQUEST']._serialized_end=11852
  _globals['_IMPORTATTRIBUTECONFIGURATIONBUFFEREXRESPONSE']._serialized_start=11854
  _globals['_IMPORTATTRIBUTECONFIGURATIONBUFFEREXRESPONSE']._serialized_end=11916
  _globals['_FETCHWITHCUSTOMSIZEREQUEST']._serialized_start=11918
  _globals['_FETCHWITHCUSTOMSIZEREQUEST']._serialized_end=12038
  _globals['_FETCHWITHCUSTOMSIZERESPONSE']._serialized_start=12040
  _globals['_FETCHWITHCUSTOMSIZERESPONSE']._serialized_end=12108
  _globals['_GETPARAMETERWITHOVERRIDDENGRPCNAMEREQUEST']._serialized_start=12111
  _globals['_GETPARAMETERWITHOVERRIDDENGRPCNAMEREQUEST']._serialized_end=12302
  _globals['_GETPARAMETERWITHOVERRIDDENGRPCNAMERESPONSE']._serialized_start=12304
  _globals['_GETPARAMETERWITHOVERRIDDENGRPCNAMERESPONSE']._serialized_end=12394
  _globals['_IVIDANCEWITHTWISTWITHMULTIPLEARRAYSANDONEBUFFERSIZEREQUEST']._serialized_start=12396
  _globals['_IVIDANCEWITHTWISTWITHMULTIPLEARRAYSANDONEBUFFERSIZEREQUEST']._serialized_end=12492
  _globals['_IVIDANCEWITHTWISTWITHMULTIPLEARRAYSANDONEBUFFERSIZERESPONSE']._serialized_start=12495
  _globals['_IVIDANCEWITHTWISTWITHMULTIPLEARRAYSANDONEBUFFERSIZERESPONSE']._serialized_end=12649
  _globals['_FUNCTIONWITHOVERRIDDENGRPCNAME2XREQUEST']._serialized_start=12651
  _globals['_FUNCTIONWITHOVERRIDDENGRPCNAME2XREQUEST']._serialized_end=12728
  _globals['_FUNCTIONWITHOVERRIDDENGRPCNAME2XRESPONSE']._serialized_start=12730
  _globals['_FUNCTIONWITHOVERRIDDENGRPCNAME2XRESPONSE']._serialized_end=12788
  _globals['_FUNCTIONWITH3DNUMPYARRAYOFNUMPYCOMPLEX128INPUTPARAMETERREQUEST']._serialized_start=12791
  _globals['_FUNCTIONWITH3DNUMPYARRAYOFNUMPYCOMPLEX128INPUTPARAMETERREQUEST']._serialized_end=12960
  _globals['_FUNCTIONWITH3DNUMPYARRAYOFNUMPYCOMPLEX128INPUTPARAMETERRESPONSE']._serialized_start=12962
  _globals['_FUNCTIONWITH3DNUMPYARRAYOFNUMPYCOMPLEX128INPUTPARAMETERRESPONSE']._serialized_end=13043
  _globals['_STRINGVALUEDENUMNOENUMGENERATEDREQUEST']._serialized_start=13045
  _globals['_STRINGVALUEDENUMNOENUMGENERATEDREQUEST']._serialized_end=13144
  _globals['_STRINGVALUEDENUMNOENUMGENERATEDRESPONSE']._serialized_start=13146
  _globals['_STRINGVALUEDENUMNOENUMGENERATEDRESPONSE']._serialized_end=13203
  _globals['_IVIDANCEWITHATWISTCALCULATEDSIZEOUTREQUEST']._serialized_start=13205
  _globals['_IVIDANCEWITHATWISTCALCULATEDSIZEOUTREQUEST']._serialized_end=13285
  _globals['_IVIDANCEWITHATWISTCALCULATEDSIZEOUTRESPONSE']._serialized_start=13288
  _globals['_IVIDANCEWITHATWISTCALCULATEDSIZEOUTRESPONSE']._serialized_end=13430
  _globals['_IMPORTATTRIBUTECONFIGURATIONBUFFERREQUEST']._serialized_start=13432
  _globals['_IMPORTATTRIBUTECONFIGURATIONBUFFERREQUEST']._serialized_end=13534
  _globals['_IMPORTATTRIBUTECONFIGURATIONBUFFERRESPONSE']._serialized_start=13536
  _globals['_IMPORTATTRIBUTECONFIGURATIONBUFFERRESPONSE']._serialized_end=13596
  _globals['_EXPORTATTRIBUTECONFIGURATIONBUFFERREQUEST']._serialized_start=13598
  _globals['_EXPORTATTRIBUTECONFIGURATIONBUFFERREQUEST']._serialized_end=13677
  _globals['_EXPORTATTRIBUTECONFIGURATIONBUFFERRESPONSE']._serialized_start=13679
  _globals['_EXPORTATTRIBUTECONFIGURATIONBUFFERRESPONSE']._serialized_end=13762
  _globals['_CONTROL4022REQUEST']._serialized_start=13764
  _globals['_CONTROL4022REQUEST']._serialized_end=13830
  _globals['_CONTROL4022RESPONSE']._serialized_start=13832
  _globals['_CONTROL4022RESPONSE']._serialized_end=13869
  _globals['_ACCEPTVISESSIONARRAYREQUEST']._serialized_start=13871
  _globals['_ACCEPTVISESSIONARRAYREQUEST']._serialized_end=13970
  _globals['_ACCEPTVISESSIONARRAYRESPONSE']._serialized_start=13972
  _globals['_ACCEPTVISESSIONARRAYRESPONSE']._serialized_end=14018
  _globals['_ACCEPTVIUINT32ARRAYREQUEST']._serialized_start=14020
  _globals['_ACCEPTVIUINT32ARRAYREQUEST']._serialized_end=14107
  _globals['_ACCEPTVIUINT32ARRAYRESPONSE']._serialized_start=14109
  _globals['_ACCEPTVIUINT32ARRAYRESPONSE']._serialized_end=14154
  _globals['_BOOLARRAYINPUTFUNCTIONREQUEST']._serialized_start=14156
  _globals['_BOOLARRAYINPUTFUNCTIONREQUEST']._serialized_end=14269
  _globals['_BOOLARRAYINPUTFUNCTIONRESPONSE']._serialized_start=14271
  _globals['_BOOLARRAYINPUTFUNCTIONRESPONSE']._serialized_end=14319
  _globals['_CLOSEEXTCALREQUEST']._serialized_start=14321
  _globals['_CLOSEEXTCALREQUEST']._serialized_end=14393
  _globals['_CLOSEEXTCALRESPONSE']._serialized_start=14395
  _globals['_CLOSEEXTCALRESPONSE']._serialized_end=14432
  _globals['_COMMANDWITHRESERVEDPARAMREQUEST']._serialized_start=14434
  _globals['_COMMANDWITHRESERVEDPARAMREQUEST']._serialized_end=14503
  _globals['_COMMANDWITHRESERVEDPARAMRESPONSE']._serialized_start=14505
  _globals['_COMMANDWITHRESERVEDPARAMRESPONSE']._serialized_end=14555
  _globals['_CREATECONFIGURATIONLISTREQUEST']._serialized_start=14557
  _globals['_CREATECONFIGURATIONLISTREQUEST']._serialized_end=14647
  _globals['_CREATECONFIGURATIONLISTRESPONSE']._serialized_start=14649
  _globals['_CREATECONFIGURATIONLISTRESPONSE']._serialized_end=14698
  _globals['_CUSTOMNESTEDSTRUCTROUNDTRIPREQUEST']._serialized_start=14700
  _globals['_CUSTOMNESTEDSTRUCTROUNDTRIPREQUEST']._serialized_end=14807
  _globals['_CUSTOMNESTEDSTRUCTROUNDTRIPRESPONSE']._serialized_start=14809
  _globals['_CUSTOMNESTEDSTRUCTROUNDTRIPRESPONSE']._serialized_end=14934
  _globals['_GETBITFIELDASENUMARRAYREQUEST']._serialized_start=14936
  _globals['_GETBITFIELDASENUMARRAYREQUEST']._serialized_end=14967
  _globals['_GETBITFIELDASENUMARRAYRESPONSE']._serialized_start=14969
  _globals['_GETBITFIELDASENUMARRAYRESPONSE']._serialized_end=15080
  _globals['_GETANIVIDANCEWITHATWISTARRAYOFCUSTOMTYPEREQUEST']._serialized_start=15082
  _globals['_GETANIVIDANCEWITHATWISTARRAYOFCUSTOMTYPEREQUEST']._serialized_end=15167
  _globals['_GETANIVIDANCEWITHATWISTARRAYOFCUSTOMTYPERESPONSE']._serialized_start=15170
  _globals['_GETANIVIDANCEWITHATWISTARRAYOFCUSTOMTYPERESPONSE']._serialized_end=15307
  _globals['_GETANIVIDANCEWITHATWISTARRAYWITHINPUTARRAYREQUEST']._serialized_start=15309
  _globals['_GETANIVIDANCEWITHATWISTARRAYWITHINPUTARRAYREQUEST']._serialized_end=15377
  _globals['_GETANIVIDANCEWITHATWISTARRAYWITHINPUTARRAYRESPONSE']._serialized_start=15379
  _globals['_GETANIVIDANCEWITHATWISTARRAYWITHINPUTARRAYRESPONSE']._serialized_end=15487
  _globals['_GETANIVIDANCEWITHATWISTBYTEARRAYREQUEST']._serialized_start=15489
  _globals['_GETANIVIDANCEWITHATWISTBYTEARRAYREQUEST']._serialized_end=15530
  _globals['_GETANIVIDANCEWITHATWISTBYTEARRAYRESPONSE']._serialized_start=15532
  _globals['_GETANIVIDANCEWITHATWISTBYTEARRAYRESPONSE']._serialized_end=15630
  _globals['_GETANIVIDANCEWITHATWISTSTRINGSTRLENBUGREQUEST']._serialized_start=15632
  _globals['_GETANIVIDANCEWITHATWISTSTRINGSTRLENBUGREQUEST']._serialized_end=15679
  _globals['_GETANIVIDANCEWITHATWISTSTRINGSTRLENBUGRESPONSE']._serialized_start=15681
  _globals['_GETANIVIDANCEWITHATWISTSTRINGSTRLENBUGRESPONSE']._serialized_end=15786
  _globals['_GETARRAYSIZEFORCUSTOMCODEREQUEST']._serialized_start=15788
  _globals['_GETARRAYSIZEFORCUSTOMCODEREQUEST']._serialized_end=15858
  _globals['_GETARRAYSIZEFORCUSTOMCODERESPONSE']._serialized_start=15860
  _globals['_GETARRAYSIZEFORCUSTOMCODERESPONSE']._serialized_end=15929
  _globals['_GETARRAYVIUINT8WITHENUMREQUEST']._serialized_start=15931
  _globals['_GETARRAYVIUINT8WITHENUMREQUEST']._serialized_end=16018
  _globals['_GETARRAYVIUINT8WITHENUMRESPONSE']._serialized_start=16021
  _globals['_GETARRAYVIUINT8WITHENUMRESPONSE']._serialized_end=16160
  _globals['_GETVIUINT8REQUEST']._serialized_start=16162
  _globals['_GETVIUINT8REQUEST']._serialized_end=16217
  _globals['_GETVIUINT8RESPONSE']._serialized_start=16219
  _globals['_GETVIUINT8RESPONSE']._serialized_end=16279
  _globals['_GETVIINT32ARRAYREQUEST']._serialized_start=16281
  _globals['_GETVIINT32ARRAYREQUEST']._serialized_end=16360
  _globals['_GETVIINT32ARRAYRESPONSE']._serialized_start=16362
  _globals['_GETVIINT32ARRAYRESPONSE']._serialized_end=16424
  _globals['_GETVIUINT32ARRAYREQUEST']._serialized_start=16426
  _globals['_GETVIUINT32ARRAYREQUEST']._serialized_end=16506
  _globals['_GETVIUINT32ARRAYRESPONSE']._serialized_start=16508
  _globals['_GETVIUINT32ARRAYRESPONSE']._serialized_end=16573
  _globals['_METHODUSINGENUMWITHGRPCNAMEVALUESREQUEST']._serialized_start=16576
  _globals['_METHODUSINGENUMWITHGRPCNAMEVALUESREQUEST']._serialized_end=16722
  _globals['_METHODUSINGENUMWITHGRPCNAMEVALUESRESPONSE']._serialized_start=16724
  _globals['_METHODUSINGENUMWITHGRPCNAMEVALUESRESPONSE']._serialized_end=16783
  _globals['_METHODWITHGETLASTERRORPARAMREQUEST']._serialized_start=16785
  _globals['_METHODWITHGETLASTERRORPARAMREQUEST']._serialized_end=16821
  _globals['_METHODWITHGETLASTERRORPARAMRESPONSE']._serialized_start=16823
  _globals['_METHODWITHGETLASTERRORPARAMRESPONSE']._serialized_end=16900
  _globals['_METHODWITHGRPCONLYPARAMREQUEST']._serialized_start=16902
  _globals['_METHODWITHGRPCONLYPARAMREQUEST']._serialized_end=16956
  _globals['_METHODWITHGRPCONLYPARAMRESPONSE']._serialized_start=16958
  _globals['_METHODWITHGRPCONLYPARAMRESPONSE']._serialized_end=17032
  _globals['_METHODUSINGWHOLEANDFRACTIONALNUMBERSREQUEST']._serialized_start=17034
  _globals['_METHODUSINGWHOLEANDFRACTIONALNUMBERSREQUEST']._serialized_end=17079
  _globals['_METHODUSINGWHOLEANDFRACTIONALNUMBERSRESPONSE']._serialized_start=17082
  _globals['_METHODUSINGWHOLEANDFRACTIONALNUMBERSRESPONSE']._serialized_end=17323
  _globals['_METHODUSINGWHOLEMAPPEDNUMBERSREQUEST']._serialized_start=17325
  _globals['_METHODUSINGWHOLEMAPPEDNUMBERSREQUEST']._serialized_end=17363
  _globals['_METHODUSINGWHOLEMAPPEDNUMBERSRESPONSE']._serialized_start=17366
  _globals['_METHODUSINGWHOLEMAPPEDNUMBERSRESPONSE']._serialized_end=17515
  _globals['_METHODWITHGRPCFIELDNUMBERREQUEST']._serialized_start=17517
  _globals['_METHODWITHGRPCFIELDNUMBERREQUEST']._serialized_end=17576
  _globals['_METHODWITHGRPCFIELDNUMBERRESPONSE']._serialized_start=17578
  _globals['_METHODWITHGRPCFIELDNUMBERRESPONSE']._serialized_end=17629
  _globals['_METHODWITHPROTOONLYPARAMETERREQUEST']._serialized_start=17631
  _globals['_METHODWITHPROTOONLYPARAMETERREQUEST']._serialized_end=17693
  _globals['_METHODWITHPROTOONLYPARAMETERRESPONSE']._serialized_start=17695
  _globals['_METHODWITHPROTOONLYPARAMETERRESPONSE']._serialized_end=17749
  _globals['_READDATAWITHINOUTIVITWISTREQUEST']._serialized_start=17751
  _globals['_READDATAWITHINOUTIVITWISTREQUEST']._serialized_end=17785
  _globals['_READDATAWITHINOUTIVITWISTRESPONSE']._serialized_start=17787
  _globals['_READDATAWITHINOUTIVITWISTRESPONSE']._serialized_end=17873
  _globals['_READDATAWITHMULTIPLEIVITWISTPARAMSETSREQUEST']._serialized_start=17875
  _globals['_READDATAWITHMULTIPLEIVITWISTPARAMSETSREQUEST']._serialized_end=17921
  _globals['_READDATAWITHMULTIPLEIVITWISTPARAMSETSRESPONSE']._serialized_start=17924
  _globals['_READDATAWITHMULTIPLEIVITWISTPARAMSETSRESPONSE']._serialized_end=18079
  _globals['_INITEXTCALREQUEST']._serialized_start=18081
  _globals['_INITEXTCALREQUEST']._serialized_end=18175
  _globals['_INITEXTCALRESPONSE']._serialized_start=18177
  _globals['_INITEXTCALRESPONSE']._serialized_end=18249
  _globals['_INITWITHVARARGSREQUEST']._serialized_start=18251
  _globals['_INITWITHVARARGSREQUEST']._serialized_end=18375
  _globals['_INITWITHVARARGSRESPONSE']._serialized_start=18377
  _globals['_INITWITHVARARGSRESPONSE']._serialized_end=18454
  _globals['_MULTIPLEARRAYSSAMESIZEWITHOPTIONALREQUEST']._serialized_start=18457
  _globals['_MULTIPLEARRAYSSAMESIZEWITHOPTIONALREQUEST']._serialized_end=18652
  _globals['_MULTIPLEARRAYSSAMESIZEWITHOPTIONALRESPONSE']._serialized_start=18654
  _globals['_MULTIPLEARRAYSSAMESIZEWITHOPTIONALRESPONSE']._serialized_end=18714
  _globals['_USEATWODIMENSIONPARAMETERREQUEST']._serialized_start=18716
  _globals['_USEATWODIMENSIONPARAMETERREQUEST']._serialized_end=18824
  _globals['_USEATWODIMENSIONPARAMETERRESPONSE']._serialized_start=18826
  _globals['_USEATWODIMENSIONPARAMETERRESPONSE']._serialized_end=18877
  _globals['_VIUINT8ARRAYINPUTFUNCTIONREQUEST']._serialized_start=18879
  _globals['_VIUINT8ARRAYINPUTFUNCTIONREQUEST']._serialized_end=18995
  _globals['_VIUINT8ARRAYINPUTFUNCTIONRESPONSE']._serialized_start=18997
  _globals['_VIUINT8ARRAYINPUTFUNCTIONRESPONSE']._serialized_end=19048
  _globals['_VIUINT8ARRAYOUTPUTFUNCTIONREQUEST']._serialized_start=19050
  _globals['_VIUINT8ARRAYOUTPUTFUNCTIONREQUEST']._serialized_end=19149
  _globals['_VIUINT8ARRAYOUTPUTFUNCTIONRESPONSE']._serialized_start=19151
  _globals['_VIUINT8ARRAYOUTPUTFUNCTIONRESPONSE']._serialized_end=19221
  _globals['_VIINT16ARRAYINPUTFUNCTIONREQUEST']._serialized_start=19223
  _globals['_VIINT16ARRAYINPUTFUNCTIONREQUEST']._serialized_end=19311
  _globals['_VIINT16ARRAYINPUTFUNCTIONRESPONSE']._serialized_start=19313
  _globals['_VIINT16ARRAYINPUTFUNCTIONRESPONSE']._serialized_end=19364
  _globals['_NIFAKE']._serialized_start=22486
  _globals['_NIFAKE']._serialized_end=34691
# @@protoc_insertion_point(module_scope)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/nifake/nifake_pb2_grpc.py sha256=c069a48939077a9f4519e4e316fd2057d681c3471bca9a183bc076eaecf0b0aa bytes=173990 -->
## FILE: generated/nifake/nifake/nifake_pb2_grpc.py

- repository: `ni/nimi-python`
- source_path: `generated/nifake/nifake/nifake_pb2_grpc.py`
- sha256: `c069a48939077a9f4519e4e316fd2057d681c3471bca9a183bc076eaecf0b0aa`
- bytes: 173990

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import nifake_pb2 as nifake__pb2


class NiFakeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Abort = channel.unary_unary(
                '/nifake_grpc.NiFake/Abort',
                request_serializer=nifake__pb2.AbortRequest.SerializeToString,
                response_deserializer=nifake__pb2.AbortResponse.FromString,
                )
        self.BoolArrayOutputFunction = channel.unary_unary(
                '/nifake_grpc.NiFake/BoolArrayOutputFunction',
                request_serializer=nifake__pb2.BoolArrayOutputFunctionRequest.SerializeToString,
                response_deserializer=nifake__pb2.BoolArrayOutputFunctionResponse.FromString,
                )
        self.Close = channel.unary_unary(
                '/nifake_grpc.NiFake/Close',
                request_serializer=nifake__pb2.CloseRequest.SerializeToString,
                response_deserializer=nifake__pb2.CloseResponse.FromString,
                )
        self.EnumArrayOutputFunction = channel.unary_unary(
                '/nifake_grpc.NiFake/EnumArrayOutputFunction',
                request_serializer=nifake__pb2.EnumArrayOutputFunctionRequest.SerializeToString,
                response_deserializer=nifake__pb2.EnumArrayOutputFunctionResponse.FromString,
                )
        self.EnumInputFunctionWithDefaults = channel.unary_unary(
                '/nifake_grpc.NiFake/EnumInputFunctionWithDefaults',
                request_serializer=nifake__pb2.EnumInputFunctionWithDefaultsRequest.SerializeToString,
                response_deserializer=nifake__pb2.EnumInputFunctionWithDefaultsResponse.FromString,
                )
        self.StringValuedEnumInputFunctionWithDefaults = channel.unary_unary(
                '/nifake_grpc.NiFake/StringValuedEnumInputFunctionWithDefaults',
                request_serializer=nifake__pb2.StringValuedEnumInputFunctionWithDefaultsRequest.SerializeToString,
                response_deserializer=nifake__pb2.StringValuedEnumInputFunctionWithDefaultsResponse.FromString,
                )
        self.ErrorMessage = channel.unary_unary(
                '/nifake_grpc.NiFake/ErrorMessage',
                request_serializer=nifake__pb2.ErrorMessageRequest.SerializeToString,
                response_deserializer=nifake__pb2.ErrorMessageResponse.FromString,
                )
        self.FetchWaveform = channel.unary_unary(
                '/nifake_grpc.NiFake/FetchWaveform',
                request_serializer=nifake__pb2.FetchWaveformRequest.SerializeToString,
                response_deserializer=nifake__pb2.FetchWaveformResponse.FromString,
                )
        self.GetABoolean = channel.unary_unary(
                '/nifake_grpc.NiFake/GetABoolean',
                request_serializer=nifake__pb2.GetABooleanRequest.SerializeToString,
                response_deserializer=nifake__pb2.GetABooleanResponse.FromString,
                )
        self.GetANumber = channel.unary_unary(
                '/nifake_grpc.NiFake/GetANumber',
                request_serializer=nifake__pb2.GetANumberRequest.SerializeToString,
                response_deserializer=nifake__pb2.GetANumberResponse.FromString,
                )
        self.GetAStringOfFixedMaximumSize = channel.unary_unary(
                '/nifake_grpc.NiFake/GetAStringOfFixedMaximumSize',
                request_serializer=nifake__pb2.GetAStringOfFixedMaximumSizeRequest.SerializeToString,
                response_deserializer=nifake__pb2.GetAStringOfFixedMaximumSizeResponse.FromString,
                )
        self.GetAnIviDanceCharArray = channel.unary_unary(
                '/nifake_grpc.NiFake/GetAnIviDanceCharArray',
                request_serializer=nifake__pb2.GetAnIviDanceCharArrayRequest.SerializeToString,
                response_deserializer=nifake__pb2.GetAnIviDanceCharArrayResponse.FromString,
                )
        self.GetArrayUsingIviDance = channel.unary_unary(
                '/nifake_grpc.NiFake/GetArrayUsingIviDance',
                request_serializer=nifake__pb2.GetArrayUsingIviDanceRequest.SerializeToString,
                response_deserializer=nifake__pb2.GetArrayUsingIviDanceResponse.FromString,
                )
        self.GetAttributeViBoolean = channel.unary_unary(
                '/nifake_grpc.NiFake/GetAttributeViBoolean',
                request_serializer=nifake__pb2.GetAttributeViBooleanRequest.SerializeToString,
                response_deserializer=nifake__pb2.GetAttributeViBooleanResponse.FromString,
                )
        self.GetAttributeViInt32 = channel.unary_unary(
                '/nifake_grpc.NiFake/GetAttributeViInt32',
                request_serializer=nifake__pb2.GetAttributeViInt32Request.SerializeToString,
                response_deserializer=nifake__pb2.GetAttributeViInt32Response.FromString,
                )
        self.GetAttributeViInt64 = channel.unary_unary(
                '/nifake_grpc.NiFake/GetAttributeViInt64',
                request_serializer=nifake__pb2.GetAttributeViInt64Request.SerializeToString,
                response_deserializer=nifake__pb2.GetAttributeViInt64Response.FromString,
                )
        self.GetAttributeViReal64 = channel.unary_unary(
                '/nifake_grpc.NiFake/GetAttributeViReal64',
                request_serializer=nifake__pb2.GetAttributeViReal64Request.SerializeToString,
                response_deserializer=nifake__pb2.GetAttributeViReal64Response.FromString,
                )
        self.GetAttributeViSession = channel.unary_unary(
                '/nifake_grpc.NiFake/GetAttributeViSession',
                request_serializer=nifake__pb2.GetAttributeViSessionRequest.SerializeToString,
                response_deserializer=nifake__pb2.GetAttributeViSessionResponse.FromString,
                )
        self.GetAttributeViString = channel.unary_unary(
                '/nifake_grpc.NiFake/GetAttributeViString',
                request_serializer=nifake__pb2.GetAttributeViStringRequest.SerializeToString,
                response_deserializer=nifake__pb2.GetAttributeViStringResponse.FromString,
                )
        self.GetCalDateAndTime = channel.unary_unary(
                '/nifake_grpc.NiFake/GetCalDateAndTime',
                request_serializer=nifake__pb2.GetCalDateAndTimeRequest.SerializeToString,
                response_deserializer=nifake__pb2.GetCalDateAndTimeResponse.FromString,
                )
        self.GetCalInterval = channel.unary_unary(
                '/nifake_grpc.NiFake/GetCalInterval',
                request_serializer=nifake__pb2.GetCalIntervalRequest.SerializeToString,
                response_deserializer=nifake__pb2.GetCalIntervalResponse.FromString,
                )
        self.GetEnumValue = channel.unary_unary(
                '/nifake_grpc.NiFake/GetEnumValue',
                request_serializer=nifake__pb2.GetEnumValueRequest.SerializeToString,
                response_deserializer=nifake__pb2.GetEnumValueResponse.FromString,
                )
        self.GetError = channel.unary_unary(
                '/nifake_grpc.NiFake/GetError',
                request_serializer=nifake__pb2.GetErrorRequest.SerializeToString,
                response_deserializer=nifake__pb2.GetErrorResponse.FromString,
                )
        self.InitWithOptions = channel.unary_unary(
                '/nifake_grpc.NiFake/InitWithOptions',
                request_serializer=nifake__pb2.InitWithOptionsRequest.SerializeToString,
                response_deserializer=nifake__pb2.InitWithOptionsResponse.FromString,
                )
        self.MultipleArrayTypes = channel.unary_unary(
                '/nifake_grpc.NiFake/MultipleArrayTypes',
                request_serializer=nifake__pb2.MultipleArrayTypesRequest.SerializeToString,
                response_deserializer=nifake__pb2.MultipleArrayTypesResponse.FromString,
                )
        self.MultipleArraysSameSize = channel.unary_unary(
                '/nifake_grpc.NiFake/MultipleArraysSameSize',
                request_serializer=nifake__pb2.MultipleArraysSameSizeRequest.SerializeToString,
                response_deserializer=nifake__pb2.MultipleArraysSameSizeResponse.FromString,
                )
        self.MultipleArraysDifferentSize = channel.unary_unary(
                '/nifake_grpc.NiFake/MultipleArraysDifferentSize',
                request_serializer=nifake__pb2.MultipleArraysDifferentSizeRequest.SerializeToString,
                response_deserializer=nifake__pb2.MultipleArraysDifferentSizeResponse.FromString,
                )
        self.MixedIviDanceAndLenMechanism = channel.unary_unary(
                '/nifake_grpc.NiFake/MixedIviDanceAndLenMechanism',
                request_serializer=nifake__pb2.MixedIviDanceAndLenMechanismRequest.SerializeToString,
                response_deserializer=nifake__pb2.MixedIviDanceAndLenMechanismResponse.FromString,
                )
        self.OneInputFunction = channel.unary_unary(
                '/nifake_grpc.NiFake/OneInputFunction',
                request_serializer=nifake__pb2.OneInputFunctionRequest.SerializeToString,
                response_deserializer=nifake__pb2.OneInputFunctionResponse.FromString,
                )
        self.ParametersAreMultipleTypes = channel.unary_unary(
                '/nifake_grpc.NiFake/ParametersAreMultipleTypes',
                request_serializer=nifake__pb2.ParametersAreMultipleTypesRequest.SerializeToString,
                response_deserializer=nifake__pb2.ParametersAreMultipleTypesResponse.FromString,
                )
        self.PoorlyNamedSimpleFunction = channel.unary_unary(
                '/nifake_grpc.NiFake/PoorlyNamedSimpleFunction',
                request_serializer=nifake__pb2.PoorlyNamedSimpleFunctionRequest.SerializeToString,
                response_deserializer=nifake__pb2.PoorlyNamedSimpleFunctionResponse.FromString,
                )
        self.Read = channel.unary_unary(
                '/nifake_grpc.NiFake/Read',
                request_serializer=nifake__pb2.ReadRequest.SerializeToString,
                response_deserializer=nifake__pb2.ReadResponse.FromString,
                )
        self.ReadFromChannel = channel.unary_unary(
                '/nifake_grpc.NiFake/ReadFromChannel',
                request_serializer=nifake__pb2.ReadFromChannelRequest.SerializeToString,
                response_deserializer=nifake__pb2.ReadFromChannelResponse.FromString,
                )
        self.ReturnANumberAndAString = channel.unary_unary(
                '/nifake_grpc.NiFake/ReturnANumberAndAString',
                request_serializer=nifake__pb2.ReturnANumberAndAStringRequest.SerializeToString,
                response_deserializer=nifake__pb2.ReturnANumberAndAStringResponse.FromString,
                )
        self.ReturnMultipleTypes = channel.unary_unary(
                '/nifake_grpc.NiFake/ReturnMultipleTypes',
                request_serializer=nifake__pb2.ReturnMultipleTypesRequest.SerializeToString,
                response_deserializer=nifake__pb2.ReturnMultipleTypesResponse.FromString,
                )
        self.SetAttributeViBoolean = channel.unary_unary(
                '/nifake_grpc.NiFake/SetAttributeViBoolean',
                request_serializer=nifake__pb2.SetAttributeViBooleanRequest.SerializeToString,
                response_deserializer=nifake__pb2.SetAttributeViBooleanResponse.FromString,
                )
        self.SetAttributeViInt32 = channel.unary_unary(
                '/nifake_grpc.NiFake/SetAttributeViInt32',
                request_serializer=nifake__pb2.SetAttributeViInt32Request.SerializeToString,
                response_deserializer=nifake__pb2.SetAttributeViInt32Response.FromString,
                )
        self.SetAttributeViInt64 = channel.unary_unary(
                '/nifake_grpc.NiFake/SetAttributeViInt64',
                request_serializer=nifake__pb2.SetAttributeViInt64Request.SerializeToString,
                response_deserializer=nifake__pb2.SetAttributeViInt64Response.FromString,
                )
        self.SetAttributeViReal64 = channel.unary_unary(
                '/nifake_grpc.NiFake/SetAttributeViReal64',
                request_serializer=nifake__pb2.SetAttributeViReal64Request.SerializeToString,
                response_deserializer=nifake__pb2.SetAttributeViReal64Response.FromString,
                )
        self.SetAttributeViString = channel.unary_unary(
                '/nifake_grpc.NiFake/SetAttributeViString',
                request_serializer=nifake__pb2.SetAttributeViStringRequest.SerializeToString,
                response_deserializer=nifake__pb2.SetAttributeViStringResponse.FromString,
                )
        self.TwoInputFunction = channel.unary_unary(
                '/nifake_grpc.NiFake/TwoInputFunction',
                request_serializer=nifake__pb2.TwoInputFunctionRequest.SerializeToString,
                response_deserializer=nifake__pb2.TwoInputFunctionResponse.FromString,
                )
        self.Use64BitNumber = channel.unary_unary(
                '/nifake_grpc.NiFake/Use64BitNumber',
                request_serializer=nifake__pb2.Use64BitNumberRequest.SerializeToString,
                response_deserializer=nifake__pb2.Use64BitNumberResponse.FromString,
                )
        self.WriteWaveform = channel.unary_unary(
                '/nifake_grpc.NiFake/WriteWaveform',
                request_serializer=nifake__pb2.WriteWaveformRequest.SerializeToString,
                response_deserializer=nifake__pb2.WriteWaveformResponse.FromString,
                )
        self.WriteWaveformNumpyComplex128 = channel.unary_unary(
                '/nifake_grpc.NiFake/WriteWaveformNumpyComplex128',
                request_serializer=nifake__pb2.WriteWaveformNumpyComplex128Request.SerializeToString,
                response_deserializer=nifake__pb2.WriteWaveformNumpyComplex128Response.FromString,
                )
        self.WriteWaveformNumpyComplex64 = channel.unary_unary(
                '/nifake_grpc.NiFake/WriteWaveformNumpyComplex64',
                request_serializer=nifake__pb2.WriteWaveformNumpyComplex64Request.SerializeToString,
                response_deserializer=nifake__pb2.WriteWaveformNumpyComplex64Response.FromString,
                )
        self.WriteWaveformNumpyComplexInterleavedI16 = channel.unary_unary(
                '/nifake_grpc.NiFake/WriteWaveformNumpyComplexInterleavedI16',
                request_serializer=nifake__pb2.WriteWaveformNumpyComplexInterleavedI16Request.SerializeToString,
                response_deserializer=nifake__pb2.WriteWaveformNumpyComplexInterleavedI16Response.FromString,
                )
        self.SetCustomType = channel.unary_unary(
                '/nifake_grpc.NiFake/SetCustomType',
                request_serializer=nifake__pb2.SetCustomTypeRequest.SerializeToString,
                response_deserializer=nifake__pb2.SetCustomTypeResponse.FromString,
                )
        self.SetCustomTypeArray = channel.unary_unary(
                '/nifake_grpc.NiFake/SetCustomTypeArray',
                request_serializer=nifake__pb2.SetCustomTypeArrayRequest.SerializeToString,
                response_deserializer=nifake__pb2.SetCustomTypeArrayResponse.FromString,
                )
        self.GetCustomType = channel.unary_unary(
                '/nifake_grpc.NiFake/GetCustomType',
                request_serializer=nifake__pb2.GetCustomTypeRequest.SerializeToString,
                response_deserializer=nifake__pb2.GetCustomTypeResponse.FromString,
                )
        self.GetCustomTypeArray = channel.unary_unary(
                '/nifake_grpc.NiFake/GetCustomTypeArray',
                request_serializer=nifake__pb2.GetCustomTypeArrayRequest.SerializeToString,
                response_deserializer=nifake__pb2.GetCustomTypeArrayResponse.FromString,
                )
        self.GetAnIviDanceWithATwistArray = channel.unary_unary(
                '/nifake_grpc.NiFake/GetAnIviDanceWithATwistArray',
                request_serializer=nifake__pb2.GetAnIviDanceWithATwistArrayRequest.SerializeToString,
                response_deserializer=nifake__pb2.GetAnIviDanceWithATwistArrayResponse.FromString,
                )
        self.GetAnIviDanceWithATwistString = channel.unary_unary(
                '/nifake_grpc.NiFake/GetAnIviDanceWithATwistString',
                request_serializer=nifake__pb2.GetAnIviDanceWithATwistStringRequest.SerializeToString,
                response_deserializer=nifake__pb2.GetAnIviDanceWithATwistStringResponse.FromString,
                )
        self.DoubleAllTheNums = channel.unary_unary(
                '/nifake_grpc.NiFake/DoubleAllTheNums',
                request_serializer=nifake__pb2.DoubleAllTheNumsRequest.SerializeToString,
                response_deserializer=nifake__pb2.DoubleAllTheNumsResponse.FromString,
                )
        self.AcceptListOfDurationsInSeconds = channel.unary_unary(
                '/nifake_grpc.NiFake/AcceptListOfDurationsInSeconds',
                request_serializer=nifake__pb2.AcceptListOfDurationsInSecondsRequest.SerializeToString,
                response_deserializer=nifake__pb2.AcceptListOfDurationsInSecondsResponse.FromString,
                )
        self.ReturnDurationInSeconds = channel.unary_unary(
                '/nifake_grpc.NiFake/ReturnDurationInSeconds',
                request_serializer=nifake__pb2.ReturnDurationInSecondsRequest.SerializeToString,
                response_deserializer=nifake__pb2.ReturnDurationInSecondsResponse.FromString,
                )
        self.ReturnListOfDurationsInSeconds = channel.unary_unary(
                '/nifake_grpc.NiFake/ReturnListOfDurationsInSeconds',
                request_serializer=nifake__pb2.ReturnListOfDurationsInSecondsRequest.SerializeToString,
                response_deserializer=nifake__pb2.ReturnListOfDurationsInSecondsResponse.FromString,
                )
        self.ConfigureAbc = channel.unary_unary(
                '/nifake_grpc.NiFake/ConfigureAbc',
                request_serializer=nifake__pb2.ConfigureAbcRequest.SerializeToString,
                response_deserializer=nifake__pb2.ConfigureAbcResponse.FromString,
                )
        self.ConfigureEnums = channel.unary_unary(
                '/nifake_grpc.NiFake/ConfigureEnums',
                request_serializer=nifake__pb2.ConfigureEnumsRequest.SerializeToString,
                response_deserializer=nifake__pb2.ConfigureEnumsResponse.FromString,
                )
        self.ExportAttributeConfigurationBufferEx = channel.unary_unary(
                '/nifake_grpc.NiFake/ExportAttributeConfigurationBufferEx',
                request_serializer=nifake__pb2.ExportAttributeConfigurationBufferExRequest.SerializeToString,
                response_deserializer=nifake__pb2.ExportAttributeConfigurationBufferExResponse.FromString,
                )
        self.ImportAttributeConfigurationBufferEx = channel.unary_unary(
                '/nifake_grpc.NiFake/ImportAttributeConfigurationBufferEx',
                request_serializer=nifake__pb2.ImportAttributeConfigurationBufferExRequest.SerializeToString,
                response_deserializer=nifake__pb2.ImportAttributeConfigurationBufferExResponse.FromString,
                )
        self.FetchWithCustomSize = channel.unary_unary(
                '/nifake_grpc.NiFake/FetchWithCustomSize',
                request_serializer=nifake__pb2.FetchWithCustomSizeRequest.SerializeToString,
                response_deserializer=nifake__pb2.FetchWithCustomSizeResponse.FromString,
                )
        self.GetParameterWithOverriddenGrpcName = channel.unary_unary(
                '/nifake_grpc.NiFake/GetParameterWithOverriddenGrpcName',
                request_serializer=nifake__pb2.GetParameterWithOverriddenGrpcNameRequest.SerializeToString,
                response_deserializer=nifake__pb2.GetParameterWithOverriddenGrpcNameResponse.FromString,
                )
        self.IviDanceWithTwistWithMultipleArraysAndOneBufferSize = channel.unary_unary(
                '/nifake_grpc.NiFake/IviDanceWithTwistWithMultipleArraysAndOneBufferSize',
                request_serializer=nifake__pb2.IviDanceWithTwistWithMultipleArraysAndOneBufferSizeRequest.SerializeToString,
                response_deserializer=nifake__pb2.IviDanceWithTwistWithMultipleArraysAndOneBufferSizeResponse.FromString,
                )
        self.FunctionWithOverriddenGrpcName2x = channel.unary_unary(
                '/nifake_grpc.NiFake/FunctionWithOverriddenGrpcName2x',
                request_serializer=nifake__pb2.FunctionWithOverriddenGrpcName2xRequest.SerializeToString,
                response_deserializer=nifake__pb2.FunctionWithOverriddenGrpcName2xResponse.FromString,
                )
        self.FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter = channel.unary_unary(
                '/nifake_grpc.NiFake/FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter',
                request_serializer=nifake__pb2.FunctionWith3dNumpyArrayOfNumpyComplex128InputParameterRequest.SerializeToString,
                response_deserializer=nifake__pb2.FunctionWith3dNumpyArrayOfNumpyComplex128InputParameterResponse.FromString,
                )
        self.StringValuedEnumNoEnumGenerated = channel.unary_unary(
                '/nifake_grpc.NiFake/StringValuedEnumNoEnumGenerated',
                request_serializer=nifake__pb2.StringValuedEnumNoEnumGeneratedRequest.SerializeToString,
                response_deserializer=nifake__pb2.StringValuedEnumNoEnumGeneratedResponse.FromString,
                )
        self.IviDanceWithATwistCalculatedSizeOut = channel.unary_unary(
                '/nifake_grpc.NiFake/IviDanceWithATwistCalculatedSizeOut',
                request_serializer=nifake__pb2.IviDanceWithATwistCalculatedSizeOutRequest.SerializeToString,
                response_deserializer=nifake__pb2.IviDanceWithATwistCalculatedSizeOutResponse.FromString,
                )
        self.ImportAttributeConfigurationBuffer = channel.unary_unary(
                '/nifake_grpc.NiFake/ImportAttributeConfigurationBuffer',
                request_serializer=nifake__pb2.ImportAttributeConfigurationBufferRequest.SerializeToString,
                response_deserializer=nifake__pb2.ImportAttributeConfigurationBufferResponse.FromString,
                )
        self.ExportAttributeConfigurationBuffer = channel.unary_unary(
                '/nifake_grpc.NiFake/ExportAttributeConfigurationBuffer',
                request_serializer=nifake__pb2.ExportAttributeConfigurationBufferRequest.SerializeToString,
                response_deserializer=nifake__pb2.ExportAttributeConfigurationBufferResponse.FromString,
                )
        self.Control4022 = channel.unary_unary(
                '/nifake_grpc.NiFake/Control4022',
                request_serializer=nifake__pb2.Control4022Request.SerializeToString,
                response_deserializer=nifake__pb2.Control4022Response.FromString,
                )
        self.AcceptViSessionArray = channel.unary_unary(
                '/nifake_grpc.NiFake/AcceptViSessionArray',
                request_serializer=nifake__pb2.AcceptViSessionArrayRequest.SerializeToString,
                response_deserializer=nifake__pb2.AcceptViSessionArrayResponse.FromString,
                )
        self.AcceptViUInt32Array = channel.unary_unary(
                '/nifake_grpc.NiFake/AcceptViUInt32Array',
                request_serializer=nifake__pb2.AcceptViUInt32ArrayRequest.SerializeToString,
                response_deserializer=nifake__pb2.AcceptViUInt32ArrayResponse.FromString,
                )
        self.BoolArrayInputFunction = channel.unary_unary(
                '/nifake_grpc.NiFake/BoolArrayInputFunction',
                request_serializer=nifake__pb2.BoolArrayInputFunctionRequest.SerializeToString,
                response_deserializer=nifake__pb2.BoolArrayInputFunctionResponse.FromString,
                )
        self.CloseExtCal = channel.unary_unary(
                '/nifake_grpc.NiFake/CloseExtCal',
                request_serializer=nifake__pb2.CloseExtCalRequest.SerializeToString,
                response_deserializer=nifake__pb2.CloseExtCalResponse.FromString,
                )
        self.CommandWithReservedParam = channel.unary_unary(
                '/nifake_grpc.NiFake/CommandWithReservedParam',
                request_serializer=nifake__pb2.CommandWithReservedParamRequest.SerializeToString,
                response_deserializer=nifake__pb2.CommandWithReservedParamResponse.FromString,
                )
        self.CreateConfigurationList = channel.unary_unary(
                '/nifake_grpc.NiFake/CreateConfigurationList',
                request_serializer=nifake__pb2.CreateConfigurationListRequest.SerializeToString,
                response_deserializer=nifake__pb2.CreateConfigurationListResponse.FromString,
                )
        self.CustomNestedStructRoundtrip = channel.unary_unary(
                '/nifake_grpc.NiFake/CustomNestedStructRoundtrip',
                request_serializer=nifake__pb2.CustomNestedStructRoundtripRequest.SerializeToString,
                response_deserializer=nifake__pb2.CustomNestedStructRoundtripResponse.FromString,
                )
        self.GetBitfieldAsEnumArray = channel.unary_unary(
                '/nifake_grpc.NiFake/GetBitfieldAsEnumArray',
                request_serializer=nifake__pb2.GetBitfieldAsEnumArrayRequest.SerializeToString,
                response_deserializer=nifake__pb2.GetBitfieldAsEnumArrayResponse.FromString,
                )
        self.GetAnIviDanceWithATwistArrayOfCustomType = channel.unary_unary(
                '/nifake_grpc.NiFake/GetAnIviDanceWithATwistArrayOfCustomType',
                request_serializer=nifake__pb2.GetAnIviDanceWithATwistArrayOfCustomTypeRequest.SerializeToString,
                response_deserializer=nifake__pb2.GetAnIviDanceWithATwistArrayOfCustomTypeResponse.FromString,
                )
        self.GetAnIviDanceWithATwistArrayWithInputArray = channel.unary_unary(
                '/nifake_grpc.NiFake/GetAnIviDanceWithATwistArrayWithInputArray',
                request_serializer=nifake__pb2.GetAnIviDanceWithATwistArrayWithInputArrayRequest.SerializeToString,
                response_deserializer=nifake__pb2.GetAnIviDanceWithATwistArrayWithInputArrayResponse.FromString,
                )
        self.GetAnIviDanceWithATwistByteArray = channel.unary_unary(
                '/nifake_grpc.NiFake/GetAnIviDanceWithATwistByteArray',
                request_serializer=nifake__pb2.GetAnIviDanceWithATwistByteArrayRequest.SerializeToString,
                response_deserializer=nifake__pb2.GetAnIviDanceWithATwistByteArrayResponse.FromString,
                )
        self.GetAnIviDanceWithATwistStringStrlenBug = channel.unary_unary(
                '/nifake_grpc.NiFake/GetAnIviDanceWithATwistStringStrlenBug',
                request_serializer=nifake__pb2.GetAnIviDanceWithATwistStringStrlenBugRequest.SerializeToString,
                response_deserializer=nifake__pb2.GetAnIviDanceWithATwistStringStrlenBugResponse.FromString,
                )
        self.GetArraySizeForCustomCode = channel.unary_unary(
                '/nifake_grpc.NiFake/GetArraySizeForCustomCode',
                request_serializer=nifake__pb2.GetArraySizeForCustomCodeRequest.SerializeToString,
                response_deserializer=nifake__pb2.GetArraySizeForCustomCodeResponse.FromString,
                )
        self.GetArrayViUInt8WithEnum = channel.unary_unary(
                '/nifake_grpc.NiFake/GetArrayViUInt8WithEnum',
                request_serializer=nifake__pb2.GetArrayViUInt8WithEnumRequest.SerializeToString,
                response_deserializer=nifake__pb2.GetArrayViUInt8WithEnumResponse.FromString,
                )
        self.GetViUInt8 = channel.unary_unary(
                '/nifake_grpc.NiFake/GetViUInt8',
                request_serializer=nifake__pb2.GetViUInt8Request.SerializeToString,
                response_deserializer=nifake__pb2.GetViUInt8Response.FromString,
                )
        self.GetViInt32Array = channel.unary_unary(
                '/nifake_grpc.NiFake/GetViInt32Array',
                request_serializer=nifake__pb2.GetViInt32ArrayRequest.SerializeToString,
                response_deserializer=nifake__pb2.GetViInt32ArrayResponse.FromString,
                )
        self.GetViUInt32Array = channel.unary_unary(
                '/nifake_grpc.NiFake/GetViUInt32Array',
                request_serializer=nifake__pb2.GetViUInt32ArrayRequest.SerializeToString,
                response_deserializer=nifake__pb2.GetViUInt32ArrayResponse.FromString,
                )
        self.MethodUsingEnumWithGrpcNameValues = channel.unary_unary(
                '/nifake_grpc.NiFake/MethodUsingEnumWithGrpcNameValues',
                request_serializer=nifake__pb2.MethodUsingEnumWithGrpcNameValuesRequest.SerializeToString,
                response_deserializer=nifake__pb2.MethodUsingEnumWithGrpcNameValuesResponse.FromString,
                )
        self.MethodWithGetLastErrorParam = channel.unary_unary(
                '/nifake_grpc.NiFake/MethodWithGetLastErrorParam',
                request_serializer=nifake__pb2.MethodWithGetLastErrorParamRequest.SerializeToString,
                response_deserializer=nifake__pb2.MethodWithGetLastErrorParamResponse.FromString,
                )
        self.MethodWithGrpcOnlyParam = channel.unary_unary(
                '/nifake_grpc.NiFake/MethodWithGrpcOnlyParam',
                request_serializer=nifake__pb2.MethodWithGrpcOnlyParamRequest.SerializeToString,
                response_deserializer=nifake__pb2.MethodWithGrpcOnlyParamResponse.FromString,
                )
        self.MethodUsingWholeAndFractionalNumbers = channel.unary_unary(
                '/nifake_grpc.NiFake/MethodUsingWholeAndFractionalNumbers',
                request_serializer=nifake__pb2.MethodUsingWholeAndFractionalNumbersRequest.SerializeToString,
                response_deserializer=nifake__pb2.MethodUsingWholeAndFractionalNumbersResponse.FromString,
                )
        self.MethodUsingWholeMappedNumbers = channel.unary_unary(
                '/nifake_grpc.NiFake/MethodUsingWholeMappedNumbers',
                request_serializer=nifake__pb2.MethodUsingWholeMappedNumbersRequest.SerializeToString,
                response_deserializer=nifake__pb2.MethodUsingWholeMappedNumbersResponse.FromString,
                )
        self.MethodWithGrpcFieldNumber = channel.unary_unary(
                '/nifake_grpc.NiFake/MethodWithGrpcFieldNumber',
                request_serializer=nifake__pb2.MethodWithGrpcFieldNumberRequest.SerializeToString,
                response_deserializer=nifake__pb2.MethodWithGrpcFieldNumberResponse.FromString,
                )
        self.MethodWithProtoOnlyParameter = channel.unary_unary(
                '/nifake_grpc.NiFake/MethodWithProtoOnlyParameter',
                request_serializer=nifake__pb2.MethodWithProtoOnlyParameterRequest.SerializeToString,
                response_deserializer=nifake__pb2.MethodWithProtoOnlyParameterResponse.FromString,
                )
        self.ReadDataWithInOutIviTwist = channel.unary_unary(
                '/nifake_grpc.NiFake/ReadDataWithInOutIviTwist',
                request_serializer=nifake__pb2.ReadDataWithInOutIviTwistRequest.SerializeToString,
                response_deserializer=nifake__pb2.ReadDataWithInOutIviTwistResponse.FromString,
                )
        self.ReadDataWithMultipleIviTwistParamSets = channel.unary_unary(
                '/nifake_grpc.NiFake/ReadDataWithMultipleIviTwistParamSets',
                request_serializer=nifake__pb2.ReadDataWithMultipleIviTwistParamSetsRequest.SerializeToString,
                response_deserializer=nifake__pb2.ReadDataWithMultipleIviTwistParamSetsResponse.FromString,
                )
        self.InitExtCal = channel.unary_unary(
                '/nifake_grpc.NiFake/InitExtCal',
                request_serializer=nifake__pb2.InitExtCalRequest.SerializeToString,
                response_deserializer=nifake__pb2.InitExtCalResponse.FromString,
                )
        self.InitWithVarArgs = channel.unary_unary(
                '/nifake_grpc.NiFake/InitWithVarArgs',
                request_serializer=nifake__pb2.InitWithVarArgsRequest.SerializeToString,
                response_deserializer=nifake__pb2.InitWithVarArgsResponse.FromString,
                )
        self.MultipleArraysSameSizeWithOptional = channel.unary_unary(
                '/nifake_grpc.NiFake/MultipleArraysSameSizeWithOptional',
                request_serializer=nifake__pb2.MultipleArraysSameSizeWithOptionalRequest.SerializeToString,
                response_deserializer=nifake__pb2.MultipleArraysSameSizeWithOptionalResponse.FromString,
                )
        self.UseATwoDimensionParameter = channel.unary_unary(
                '/nifake_grpc.NiFake/UseATwoDimensionParameter',
                request_serializer=nifake__pb2.UseATwoDimensionParameterRequest.SerializeToString,
                response_deserializer=nifake__pb2.UseATwoDimensionParameterResponse.FromString,
                )
        self.ViUInt8ArrayInputFunction = channel.unary_unary(
                '/nifake_grpc.NiFake/ViUInt8ArrayInputFunction',
                request_serializer=nifake__pb2.ViUInt8ArrayInputFunctionRequest.SerializeToString,
                response_deserializer=nifake__pb2.ViUInt8ArrayInputFunctionResponse.FromString,
                )
        self.ViUInt8ArrayOutputFunction = channel.unary_unary(
                '/nifake_grpc.NiFake/ViUInt8ArrayOutputFunction',
                request_serializer=nifake__pb2.ViUInt8ArrayOutputFunctionRequest.SerializeToString,
                response_deserializer=nifake__pb2.ViUInt8ArrayOutputFunctionResponse.FromString,
                )
        self.ViInt16ArrayInputFunction = channel.unary_unary(
                '/nifake_grpc.NiFake/ViInt16ArrayInputFunction',
                request_serializer=nifake__pb2.ViInt16ArrayInputFunctionRequest.SerializeToString,
                response_deserializer=nifake__pb2.ViInt16ArrayInputFunctionResponse.FromString,
                )


class NiFakeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Abort(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BoolArrayOutputFunction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Close(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnumArrayOutputFunction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnumInputFunctionWithDefaults(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StringValuedEnumInputFunctionWithDefaults(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ErrorMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FetchWaveform(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetABoolean(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetANumber(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAStringOfFixedMaximumSize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAnIviDanceCharArray(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetArrayUsingIviDance(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttributeViBoolean(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttributeViInt32(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttributeViInt64(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttributeViReal64(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttributeViSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttributeViString(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCalDateAndTime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCalInterval(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEnumValue(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetError(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InitWithOptions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MultipleArrayTypes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MultipleArraysSameSize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MultipleArraysDifferentSize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MixedIviDanceAndLenMechanism(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OneInputFunction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ParametersAreMultipleTypes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PoorlyNamedSimpleFunction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadFromChannel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReturnANumberAndAString(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReturnMultipleTypes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAttributeViBoolean(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAttributeViInt32(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAttributeViInt64(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAttributeViReal64(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAttributeViString(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TwoInputFunction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Use64BitNumber(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteWaveform(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteWaveformNumpyComplex128(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteWaveformNumpyComplex64(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteWaveformNumpyComplexInterleavedI16(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetCustomType(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetCustomTypeArray(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCustomType(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCustomTypeArray(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAnIviDanceWithATwistArray(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAnIviDanceWithATwistString(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DoubleAllTheNums(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AcceptListOfDurationsInSeconds(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReturnDurationInSeconds(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReturnListOfDurationsInSeconds(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureAbc(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureEnums(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExportAttributeConfigurationBufferEx(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ImportAttributeConfigurationBufferEx(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FetchWithCustomSize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetParameterWithOverriddenGrpcName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IviDanceWithTwistWithMultipleArraysAndOneBufferSize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FunctionWithOverriddenGrpcName2x(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StringValuedEnumNoEnumGenerated(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IviDanceWithATwistCalculatedSizeOut(self, request, context):
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

    def Control4022(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AcceptViSessionArray(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AcceptViUInt32Array(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BoolArrayInputFunction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloseExtCal(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CommandWithReservedParam(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateConfigurationList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CustomNestedStructRoundtrip(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBitfieldAsEnumArray(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAnIviDanceWithATwistArrayOfCustomType(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAnIviDanceWithATwistArrayWithInputArray(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAnIviDanceWithATwistByteArray(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAnIviDanceWithATwistStringStrlenBug(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetArraySizeForCustomCode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetArrayViUInt8WithEnum(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetViUInt8(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetViInt32Array(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetViUInt32Array(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MethodUsingEnumWithGrpcNameValues(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MethodWithGetLastErrorParam(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MethodWithGrpcOnlyParam(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MethodUsingWholeAndFractionalNumbers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MethodUsingWholeMappedNumbers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MethodWithGrpcFieldNumber(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MethodWithProtoOnlyParameter(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadDataWithInOutIviTwist(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadDataWithMultipleIviTwistParamSets(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InitExtCal(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InitWithVarArgs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MultipleArraysSameSizeWithOptional(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UseATwoDimensionParameter(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ViUInt8ArrayInputFunction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ViUInt8ArrayOutputFunction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ViInt16ArrayInputFunction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NiFakeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Abort': grpc.unary_unary_rpc_method_handler(
                    servicer.Abort,
                    request_deserializer=nifake__pb2.AbortRequest.FromString,
                    response_serializer=nifake__pb2.AbortResponse.SerializeToString,
            ),
            'BoolArrayOutputFunction': grpc.unary_unary_rpc_method_handler(
                    servicer.BoolArrayOutputFunction,
                    request_deserializer=nifake__pb2.BoolArrayOutputFunctionRequest.FromString,
                    response_serializer=nifake__pb2.BoolArrayOutputFunctionResponse.SerializeToString,
            ),
            'Close': grpc.unary_unary_rpc_method_handler(
                    servicer.Close,
                    request_deserializer=nifake__pb2.CloseRequest.FromString,
                    response_serializer=nifake__pb2.CloseResponse.SerializeToString,
            ),
            'EnumArrayOutputFunction': grpc.unary_unary_rpc_method_handler(
                    servicer.EnumArrayOutputFunction,
                    request_deserializer=nifake__pb2.EnumArrayOutputFunctionRequest.FromString,
                    response_serializer=nifake__pb2.EnumArrayOutputFunctionResponse.SerializeToString,
            ),
            'EnumInputFunctionWithDefaults': grpc.unary_unary_rpc_method_handler(
                    servicer.EnumInputFunctionWithDefaults,
                    request_deserializer=nifake__pb2.EnumInputFunctionWithDefaultsRequest.FromString,
                    response_serializer=nifake__pb2.EnumInputFunctionWithDefaultsResponse.SerializeToString,
            ),
            'StringValuedEnumInputFunctionWithDefaults': grpc.unary_unary_rpc_method_handler(
                    servicer.StringValuedEnumInputFunctionWithDefaults,
                    request_deserializer=nifake__pb2.StringValuedEnumInputFunctionWithDefaultsRequest.FromString,
                    response_serializer=nifake__pb2.StringValuedEnumInputFunctionWithDefaultsResponse.SerializeToString,
            ),
            'ErrorMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.ErrorMessage,
                    request_deserializer=nifake__pb2.ErrorMessageRequest.FromString,
                    response_serializer=nifake__pb2.ErrorMessageResponse.SerializeToString,
            ),
            'FetchWaveform': grpc.unary_unary_rpc_method_handler(
                    servicer.FetchWaveform,
                    request_deserializer=nifake__pb2.FetchWaveformRequest.FromString,
                    response_serializer=nifake__pb2.FetchWaveformResponse.SerializeToString,
            ),
            'GetABoolean': grpc.unary_unary_rpc_method_handler(
                    servicer.GetABoolean,
                    request_deserializer=nifake__pb2.GetABooleanRequest.FromString,
                    response_serializer=nifake__pb2.GetABooleanResponse.SerializeToString,
            ),
            'GetANumber': grpc.unary_unary_rpc_method_handler(
                    servicer.GetANumber,
                    request_deserializer=nifake__pb2.GetANumberRequest.FromString,
                    response_serializer=nifake__pb2.GetANumberResponse.SerializeToString,
            ),
            'GetAStringOfFixedMaximumSize': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAStringOfFixedMaximumSize,
                    request_deserializer=nifake__pb2.GetAStringOfFixedMaximumSizeRequest.FromString,
                    response_serializer=nifake__pb2.GetAStringOfFixedMaximumSizeResponse.SerializeToString,
            ),
            'GetAnIviDanceCharArray': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAnIviDanceCharArray,
                    request_deserializer=nifake__pb2.GetAnIviDanceCharArrayRequest.FromString,
                    response_serializer=nifake__pb2.GetAnIviDanceCharArrayResponse.SerializeToString,
            ),
            'GetArrayUsingIviDance': grpc.unary_unary_rpc_method_handler(
                    servicer.GetArrayUsingIviDance,
                    request_deserializer=nifake__pb2.GetArrayUsingIviDanceRequest.FromString,
                    response_serializer=nifake__pb2.GetArrayUsingIviDanceResponse.SerializeToString,
            ),
            'GetAttributeViBoolean': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViBoolean,
                    request_deserializer=nifake__pb2.GetAttributeViBooleanRequest.FromString,
                    response_serializer=nifake__pb2.GetAttributeViBooleanResponse.SerializeToString,
            ),
            'GetAttributeViInt32': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViInt32,
                    request_deserializer=nifake__pb2.GetAttributeViInt32Request.FromString,
                    response_serializer=nifake__pb2.GetAttributeViInt32Response.SerializeToString,
            ),
            'GetAttributeViInt64': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViInt64,
                    request_deserializer=nifake__pb2.GetAttributeViInt64Request.FromString,
                    response_serializer=nifake__pb2.GetAttributeViInt64Response.SerializeToString,
            ),
            'GetAttributeViReal64': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViReal64,
                    request_deserializer=nifake__pb2.GetAttributeViReal64Request.FromString,
                    response_serializer=nifake__pb2.GetAttributeViReal64Response.SerializeToString,
            ),
            'GetAttributeViSession': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViSession,
                    request_deserializer=nifake__pb2.GetAttributeViSessionRequest.FromString,
                    response_serializer=nifake__pb2.GetAttributeViSessionResponse.SerializeToString,
            ),
            'GetAttributeViString': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViString,
                    request_deserializer=nifake__pb2.GetAttributeViStringRequest.FromString,
                    response_serializer=nifake__pb2.GetAttributeViStringResponse.SerializeToString,
            ),
            'GetCalDateAndTime': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCalDateAndTime,
                    request_deserializer=nifake__pb2.GetCalDateAndTimeRequest.FromString,
                    response_serializer=nifake__pb2.GetCalDateAndTimeResponse.SerializeToString,
            ),
            'GetCalInterval': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCalInterval,
                    request_deserializer=nifake__pb2.GetCalIntervalRequest.FromString,
                    response_serializer=nifake__pb2.GetCalIntervalResponse.SerializeToString,
            ),
            'GetEnumValue': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEnumValue,
                    request_deserializer=nifake__pb2.GetEnumValueRequest.FromString,
                    response_serializer=nifake__pb2.GetEnumValueResponse.SerializeToString,
            ),
            'GetError': grpc.unary_unary_rpc_method_handler(
                    servicer.GetError,
                    request_deserializer=nifake__pb2.GetErrorRequest.FromString,
                    response_serializer=nifake__pb2.GetErrorResponse.SerializeToString,
            ),
            'InitWithOptions': grpc.unary_unary_rpc_method_handler(
                    servicer.InitWithOptions,
                    request_deserializer=nifake__pb2.InitWithOptionsRequest.FromString,
                    response_serializer=nifake__pb2.InitWithOptionsResponse.SerializeToString,
            ),
            'MultipleArrayTypes': grpc.unary_unary_rpc_method_handler(
                    servicer.MultipleArrayTypes,
                    request_deserializer=nifake__pb2.MultipleArrayTypesRequest.FromString,
                    response_serializer=nifake__pb2.MultipleArrayTypesResponse.SerializeToString,
            ),
            'MultipleArraysSameSize': grpc.unary_unary_rpc_method_handler(
                    servicer.MultipleArraysSameSize,
                    request_deserializer=nifake__pb2.MultipleArraysSameSizeRequest.FromString,
                    response_serializer=nifake__pb2.MultipleArraysSameSizeResponse.SerializeToString,
            ),
            'MultipleArraysDifferentSize': grpc.unary_unary_rpc_method_handler(
                    servicer.MultipleArraysDifferentSize,
                    request_deserializer=nifake__pb2.MultipleArraysDifferentSizeRequest.FromString,
                    response_serializer=nifake__pb2.MultipleArraysDifferentSizeResponse.SerializeToString,
            ),
            'MixedIviDanceAndLenMechanism': grpc.unary_unary_rpc_method_handler(
                    servicer.MixedIviDanceAndLenMechanism,
                    request_deserializer=nifake__pb2.MixedIviDanceAndLenMechanismRequest.FromString,
                    response_serializer=nifake__pb2.MixedIviDanceAndLenMechanismResponse.SerializeToString,
            ),
            'OneInputFunction': grpc.unary_unary_rpc_method_handler(
                    servicer.OneInputFunction,
                    request_deserializer=nifake__pb2.OneInputFunctionRequest.FromString,
                    response_serializer=nifake__pb2.OneInputFunctionResponse.SerializeToString,
            ),
            'ParametersAreMultipleTypes': grpc.unary_unary_rpc_method_handler(
                    servicer.ParametersAreMultipleTypes,
                    request_deserializer=nifake__pb2.ParametersAreMultipleTypesRequest.FromString,
                    response_serializer=nifake__pb2.ParametersAreMultipleTypesResponse.SerializeToString,
            ),
            'PoorlyNamedSimpleFunction': grpc.unary_unary_rpc_method_handler(
                    servicer.PoorlyNamedSimpleFunction,
                    request_deserializer=nifake__pb2.PoorlyNamedSimpleFunctionRequest.FromString,
                    response_serializer=nifake__pb2.PoorlyNamedSimpleFunctionResponse.SerializeToString,
            ),
            'Read': grpc.unary_unary_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=nifake__pb2.ReadRequest.FromString,
                    response_serializer=nifake__pb2.ReadResponse.SerializeToString,
            ),
            'ReadFromChannel': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadFromChannel,
                    request_deserializer=nifake__pb2.ReadFromChannelRequest.FromString,
                    response_serializer=nifake__pb2.ReadFromChannelResponse.SerializeToString,
            ),
            'ReturnANumberAndAString': grpc.unary_unary_rpc_method_handler(
                    servicer.ReturnANumberAndAString,
                    request_deserializer=nifake__pb2.ReturnANumberAndAStringRequest.FromString,
                    response_serializer=nifake__pb2.ReturnANumberAndAStringResponse.SerializeToString,
            ),
            'ReturnMultipleTypes': grpc.unary_unary_rpc_method_handler(
                    servicer.ReturnMultipleTypes,
                    request_deserializer=nifake__pb2.ReturnMultipleTypesRequest.FromString,
                    response_serializer=nifake__pb2.ReturnMultipleTypesResponse.SerializeToString,
            ),
            'SetAttributeViBoolean': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttributeViBoolean,
                    request_deserializer=nifake__pb2.SetAttributeViBooleanRequest.FromString,
                    response_serializer=nifake__pb2.SetAttributeViBooleanResponse.SerializeToString,
            ),
            'SetAttributeViInt32': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttributeViInt32,
                    request_deserializer=nifake__pb2.SetAttributeViInt32Request.FromString,
                    response_serializer=nifake__pb2.SetAttributeViInt32Response.SerializeToString,
            ),
            'SetAttributeViInt64': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttributeViInt64,
                    request_deserializer=nifake__pb2.SetAttributeViInt64Request.FromString,
                    response_serializer=nifake__pb2.SetAttributeViInt64Response.SerializeToString,
            ),
            'SetAttributeViReal64': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttributeViReal64,
                    request_deserializer=nifake__pb2.SetAttributeViReal64Request.FromString,
                    response_serializer=nifake__pb2.SetAttributeViReal64Response.SerializeToString,
            ),
            'SetAttributeViString': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttributeViString,
                    request_deserializer=nifake__pb2.SetAttributeViStringRequest.FromString,
                    response_serializer=nifake__pb2.SetAttributeViStringResponse.SerializeToString,
            ),
            'TwoInputFunction': grpc.unary_unary_rpc_method_handler(
                    servicer.TwoInputFunction,
                    request_deserializer=nifake__pb2.TwoInputFunctionRequest.FromString,
                    response_serializer=nifake__pb2.TwoInputFunctionResponse.SerializeToString,
            ),
            'Use64BitNumber': grpc.unary_unary_rpc_method_handler(
                    servicer.Use64BitNumber,
                    request_deserializer=nifake__pb2.Use64BitNumberRequest.FromString,
                    response_serializer=nifake__pb2.Use64BitNumberResponse.SerializeToString,
            ),
            'WriteWaveform': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteWaveform,
                    request_deserializer=nifake__pb2.WriteWaveformRequest.FromString,
                    response_serializer=nifake__pb2.WriteWaveformResponse.SerializeToString,
            ),
            'WriteWaveformNumpyComplex128': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteWaveformNumpyComplex128,
                    request_deserializer=nifake__pb2.WriteWaveformNumpyComplex128Request.FromString,
                    response_serializer=nifake__pb2.WriteWaveformNumpyComplex128Response.SerializeToString,
            ),
            'WriteWaveformNumpyComplex64': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteWaveformNumpyComplex64,
                    request_deserializer=nifake__pb2.WriteWaveformNumpyComplex64Request.FromString,
                    response_serializer=nifake__pb2.WriteWaveformNumpyComplex64Response.SerializeToString,
            ),
            'WriteWaveformNumpyComplexInterleavedI16': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteWaveformNumpyComplexInterleavedI16,
                    request_deserializer=nifake__pb2.WriteWaveformNumpyComplexInterleavedI16Request.FromString,
                    response_serializer=nifake__pb2.WriteWaveformNumpyComplexInterleavedI16Response.SerializeToString,
            ),
            'SetCustomType': grpc.unary_unary_rpc_method_handler(
                    servicer.SetCustomType,
                    request_deserializer=nifake__pb2.SetCustomTypeRequest.FromString,
                    response_serializer=nifake__pb2.SetCustomTypeResponse.SerializeToString,
            ),
            'SetCustomTypeArray': grpc.unary_unary_rpc_method_handler(
                    servicer.SetCustomTypeArray,
                    request_deserializer=nifake__pb2.SetCustomTypeArrayRequest.FromString,
                    response_serializer=nifake__pb2.SetCustomTypeArrayResponse.SerializeToString,
            ),
            'GetCustomType': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCustomType,
                    request_deserializer=nifake__pb2.GetCustomTypeRequest.FromString,
                    response_serializer=nifake__pb2.GetCustomTypeResponse.SerializeToString,
            ),
            'GetCustomTypeArray': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCustomTypeArray,
                    request_deserializer=nifake__pb2.GetCustomTypeArrayRequest.FromString,
                    response_serializer=nifake__pb2.GetCustomTypeArrayResponse.SerializeToString,
            ),
            'GetAnIviDanceWithATwistArray': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAnIviDanceWithATwistArray,
                    request_deserializer=nifake__pb2.GetAnIviDanceWithATwistArrayRequest.FromString,
                    response_serializer=nifake__pb2.GetAnIviDanceWithATwistArrayResponse.SerializeToString,
            ),
            'GetAnIviDanceWithATwistString': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAnIviDanceWithATwistString,
                    request_deserializer=nifake__pb2.GetAnIviDanceWithATwistStringRequest.FromString,
                    response_serializer=nifake__pb2.GetAnIviDanceWithATwistStringResponse.SerializeToString,
            ),
            'DoubleAllTheNums': grpc.unary_unary_rpc_method_handler(
                    servicer.DoubleAllTheNums,
                    request_deserializer=nifake__pb2.DoubleAllTheNumsRequest.FromString,
                    response_serializer=nifake__pb2.DoubleAllTheNumsResponse.SerializeToString,
            ),
            'AcceptListOfDurationsInSeconds': grpc.unary_unary_rpc_method_handler(
                    servicer.AcceptListOfDurationsInSeconds,
                    request_deserializer=nifake__pb2.AcceptListOfDurationsInSecondsRequest.FromString,
                    response_serializer=nifake__pb2.AcceptListOfDurationsInSecondsResponse.SerializeToString,
            ),
            'ReturnDurationInSeconds': grpc.unary_unary_rpc_method_handler(
                    servicer.ReturnDurationInSeconds,
                    request_deserializer=nifake__pb2.ReturnDurationInSecondsRequest.FromString,
                    response_serializer=nifake__pb2.ReturnDurationInSecondsResponse.SerializeToString,
            ),
            'ReturnListOfDurationsInSeconds': grpc.unary_unary_rpc_method_handler(
                    servicer.ReturnListOfDurationsInSeconds,
                    request_deserializer=nifake__pb2.ReturnListOfDurationsInSecondsRequest.FromString,
                    response_serializer=nifake__pb2.ReturnListOfDurationsInSecondsResponse.SerializeToString,
            ),
            'ConfigureAbc': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureAbc,
                    request_deserializer=nifake__pb2.ConfigureAbcRequest.FromString,
                    response_serializer=nifake__pb2.ConfigureAbcResponse.SerializeToString,
            ),
            'ConfigureEnums': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureEnums,
                    request_deserializer=nifake__pb2.ConfigureEnumsRequest.FromString,
                    response_serializer=nifake__pb2.ConfigureEnumsResponse.SerializeToString,
            ),
            'ExportAttributeConfigurationBufferEx': grpc.unary_unary_rpc_method_handler(
                    servicer.ExportAttributeConfigurationBufferEx,
                    request_deserializer=nifake__pb2.ExportAttributeConfigurationBufferExRequest.FromString,
                    response_serializer=nifake__pb2.ExportAttributeConfigurationBufferExResponse.SerializeToString,
            ),
            'ImportAttributeConfigurationBufferEx': grpc.unary_unary_rpc_method_handler(
                    servicer.ImportAttributeConfigurationBufferEx,
                    request_deserializer=nifake__pb2.ImportAttributeConfigurationBufferExRequest.FromString,
                    response_serializer=nifake__pb2.ImportAttributeConfigurationBufferExResponse.SerializeToString,
            ),
            'FetchWithCustomSize': grpc.unary_unary_rpc_method_handler(
                    servicer.FetchWithCustomSize,
                    request_deserializer=nifake__pb2.FetchWithCustomSizeRequest.FromString,
                    response_serializer=nifake__pb2.FetchWithCustomSizeResponse.SerializeToString,
            ),
            'GetParameterWithOverriddenGrpcName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetParameterWithOverriddenGrpcName,
                    request_deserializer=nifake__pb2.GetParameterWithOverriddenGrpcNameRequest.FromString,
                    response_serializer=nifake__pb2.GetParameterWithOverriddenGrpcNameResponse.SerializeToString,
            ),
            'IviDanceWithTwistWithMultipleArraysAndOneBufferSize': grpc.unary_unary_rpc_method_handler(
                    servicer.IviDanceWithTwistWithMultipleArraysAndOneBufferSize,
                    request_deserializer=nifake__pb2.IviDanceWithTwistWithMultipleArraysAndOneBufferSizeRequest.FromString,
                    response_serializer=nifake__pb2.IviDanceWithTwistWithMultipleArraysAndOneBufferSizeResponse.SerializeToString,
            ),
            'FunctionWithOverriddenGrpcName2x': grpc.unary_unary_rpc_method_handler(
                    servicer.FunctionWithOverriddenGrpcName2x,
                    request_deserializer=nifake__pb2.FunctionWithOverriddenGrpcName2xRequest.FromString,
                    response_serializer=nifake__pb2.FunctionWithOverriddenGrpcName2xResponse.SerializeToString,
            ),
            'FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter': grpc.unary_unary_rpc_method_handler(
                    servicer.FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter,
                    request_deserializer=nifake__pb2.FunctionWith3dNumpyArrayOfNumpyComplex128InputParameterRequest.FromString,
                    response_serializer=nifake__pb2.FunctionWith3dNumpyArrayOfNumpyComplex128InputParameterResponse.SerializeToString,
            ),
            'StringValuedEnumNoEnumGenerated': grpc.unary_unary_rpc_method_handler(
                    servicer.StringValuedEnumNoEnumGenerated,
                    request_deserializer=nifake__pb2.StringValuedEnumNoEnumGeneratedRequest.FromString,
                    response_serializer=nifake__pb2.StringValuedEnumNoEnumGeneratedResponse.SerializeToString,
            ),
            'IviDanceWithATwistCalculatedSizeOut': grpc.unary_unary_rpc_method_handler(
                    servicer.IviDanceWithATwistCalculatedSizeOut,
                    request_deserializer=nifake__pb2.IviDanceWithATwistCalculatedSizeOutRequest.FromString,
                    response_serializer=nifake__pb2.IviDanceWithATwistCalculatedSizeOutResponse.SerializeToString,
            ),
            'ImportAttributeConfigurationBuffer': grpc.unary_unary_rpc_method_handler(
                    servicer.ImportAttributeConfigurationBuffer,
                    request_deserializer=nifake__pb2.ImportAttributeConfigurationBufferRequest.FromString,
                    response_serializer=nifake__pb2.ImportAttributeConfigurationBufferResponse.SerializeToString,
            ),
            'ExportAttributeConfigurationBuffer': grpc.unary_unary_rpc_method_handler(
                    servicer.ExportAttributeConfigurationBuffer,
                    request_deserializer=nifake__pb2.ExportAttributeConfigurationBufferRequest.FromString,
                    response_serializer=nifake__pb2.ExportAttributeConfigurationBufferResponse.SerializeToString,
            ),
            'Control4022': grpc.unary_unary_rpc_method_handler(
                    servicer.Control4022,
                    request_deserializer=nifake__pb2.Control4022Request.FromString,
                    response_serializer=nifake__pb2.Control4022Response.SerializeToString,
            ),
            'AcceptViSessionArray': grpc.unary_unary_rpc_method_handler(
                    servicer.AcceptViSessionArray,
                    request_deserializer=nifake__pb2.AcceptViSessionArrayRequest.FromString,
                    response_serializer=nifake__pb2.AcceptViSessionArrayResponse.SerializeToString,
            ),
            'AcceptViUInt32Array': grpc.unary_unary_rpc_method_handler(
                    servicer.AcceptViUInt32Array,
                    request_deserializer=nifake__pb2.AcceptViUInt32ArrayRequest.FromString,
                    response_serializer=nifake__pb2.AcceptViUInt32ArrayResponse.SerializeToString,
            ),
            'BoolArrayInputFunction': grpc.unary_unary_rpc_method_handler(
                    servicer.BoolArrayInputFunction,
                    request_deserializer=nifake__pb2.BoolArrayInputFunctionRequest.FromString,
                    response_serializer=nifake__pb2.BoolArrayInputFunctionResponse.SerializeToString,
            ),
            'CloseExtCal': grpc.unary_unary_rpc_method_handler(
                    servicer.CloseExtCal,
                    request_deserializer=nifake__pb2.CloseExtCalRequest.FromString,
                    response_serializer=nifake__pb2.CloseExtCalResponse.SerializeToString,
            ),
            'CommandWithReservedParam': grpc.unary_unary_rpc_method_handler(
                    servicer.CommandWithReservedParam,
                    request_deserializer=nifake__pb2.CommandWithReservedParamRequest.FromString,
                    response_serializer=nifake__pb2.CommandWithReservedParamResponse.SerializeToString,
            ),
            'CreateConfigurationList': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateConfigurationList,
                    request_deserializer=nifake__pb2.CreateConfigurationListRequest.FromString,
                    response_serializer=nifake__pb2.CreateConfigurationListResponse.SerializeToString,
            ),
            'CustomNestedStructRoundtrip': grpc.unary_unary_rpc_method_handler(
                    servicer.CustomNestedStructRoundtrip,
                    request_deserializer=nifake__pb2.CustomNestedStructRoundtripRequest.FromString,
                    response_serializer=nifake__pb2.CustomNestedStructRoundtripResponse.SerializeToString,
            ),
            'GetBitfieldAsEnumArray': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBitfieldAsEnumArray,
                    request_deserializer=nifake__pb2.GetBitfieldAsEnumArrayRequest.FromString,
                    response_serializer=nifake__pb2.GetBitfieldAsEnumArrayResponse.SerializeToString,
            ),
            'GetAnIviDanceWithATwistArrayOfCustomType': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAnIviDanceWithATwistArrayOfCustomType,
                    request_deserializer=nifake__pb2.GetAnIviDanceWithATwistArrayOfCustomTypeRequest.FromString,
                    response_serializer=nifake__pb2.GetAnIviDanceWithATwistArrayOfCustomTypeResponse.SerializeToString,
            ),
            'GetAnIviDanceWithATwistArrayWithInputArray': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAnIviDanceWithATwistArrayWithInputArray,
                    request_deserializer=nifake__pb2.GetAnIviDanceWithATwistArrayWithInputArrayRequest.FromString,
                    response_serializer=nifake__pb2.GetAnIviDanceWithATwistArrayWithInputArrayResponse.SerializeToString,
            ),
            'GetAnIviDanceWithATwistByteArray': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAnIviDanceWithATwistByteArray,
                    request_deserializer=nifake__pb2.GetAnIviDanceWithATwistByteArrayRequest.FromString,
                    response_serializer=nifake__pb2.GetAnIviDanceWithATwistByteArrayResponse.SerializeToString,
            ),
            'GetAnIviDanceWithATwistStringStrlenBug': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAnIviDanceWithATwistStringStrlenBug,
                    request_deserializer=nifake__pb2.GetAnIviDanceWithATwistStringStrlenBugRequest.FromString,
                    response_serializer=nifake__pb2.GetAnIviDanceWithATwistStringStrlenBugResponse.SerializeToString,
            ),
            'GetArraySizeForCustomCode': grpc.unary_unary_rpc_method_handler(
                    servicer.GetArraySizeForCustomCode,
                    request_deserializer=nifake__pb2.GetArraySizeForCustomCodeRequest.FromString,
                    response_serializer=nifake__pb2.GetArraySizeForCustomCodeResponse.SerializeToString,
            ),
            'GetArrayViUInt8WithEnum': grpc.unary_unary_rpc_method_handler(
                    servicer.GetArrayViUInt8WithEnum,
                    request_deserializer=nifake__pb2.GetArrayViUInt8WithEnumRequest.FromString,
                    response_serializer=nifake__pb2.GetArrayViUInt8WithEnumResponse.SerializeToString,
            ),
            'GetViUInt8': grpc.unary_unary_rpc_method_handler(
                    servicer.GetViUInt8,
                    request_deserializer=nifake__pb2.GetViUInt8Request.FromString,
                    response_serializer=nifake__pb2.GetViUInt8Response.SerializeToString,
            ),
            'GetViInt32Array': grpc.unary_unary_rpc_method_handler(
                    servicer.GetViInt32Array,
                    request_deserializer=nifake__pb2.GetViInt32ArrayRequest.FromString,
                    response_serializer=nifake__pb2.GetViInt32ArrayResponse.SerializeToString,
            ),
            'GetViUInt32Array': grpc.unary_unary_rpc_method_handler(
                    servicer.GetViUInt32Array,
                    request_deserializer=nifake__pb2.GetViUInt32ArrayRequest.FromString,
                    response_serializer=nifake__pb2.GetViUInt32ArrayResponse.SerializeToString,
            ),
            'MethodUsingEnumWithGrpcNameValues': grpc.unary_unary_rpc_method_handler(
                    servicer.MethodUsingEnumWithGrpcNameValues,
                    request_deserializer=nifake__pb2.MethodUsingEnumWithGrpcNameValuesRequest.FromString,
                    response_serializer=nifake__pb2.MethodUsingEnumWithGrpcNameValuesResponse.SerializeToString,
            ),
            'MethodWithGetLastErrorParam': grpc.unary_unary_rpc_method_handler(
                    servicer.MethodWithGetLastErrorParam,
                    request_deserializer=nifake__pb2.MethodWithGetLastErrorParamRequest.FromString,
                    response_serializer=nifake__pb2.MethodWithGetLastErrorParamResponse.SerializeToString,
            ),
            'MethodWithGrpcOnlyParam': grpc.unary_unary_rpc_method_handler(
                    servicer.MethodWithGrpcOnlyParam,
                    request_deserializer=nifake__pb2.MethodWithGrpcOnlyParamRequest.FromString,
                    response_serializer=nifake__pb2.MethodWithGrpcOnlyParamResponse.SerializeToString,
            ),
            'MethodUsingWholeAndFractionalNumbers': grpc.unary_unary_rpc_method_handler(
                    servicer.MethodUsingWholeAndFractionalNumbers,
                    request_deserializer=nifake__pb2.MethodUsingWholeAndFractionalNumbersRequest.FromString,
                    response_serializer=nifake__pb2.MethodUsingWholeAndFractionalNumbersResponse.SerializeToString,
            ),
            'MethodUsingWholeMappedNumbers': grpc.unary_unary_rpc_method_handler(
                    servicer.MethodUsingWholeMappedNumbers,
                    request_deserializer=nifake__pb2.MethodUsingWholeMappedNumbersRequest.FromString,
                    response_serializer=nifake__pb2.MethodUsingWholeMappedNumbersResponse.SerializeToString,
            ),
            'MethodWithGrpcFieldNumber': grpc.unary_unary_rpc_method_handler(
                    servicer.MethodWithGrpcFieldNumber,
                    request_deserializer=nifake__pb2.MethodWithGrpcFieldNumberRequest.FromString,
                    response_serializer=nifake__pb2.MethodWithGrpcFieldNumberResponse.SerializeToString,
            ),
            'MethodWithProtoOnlyParameter': grpc.unary_unary_rpc_method_handler(
                    servicer.MethodWithProtoOnlyParameter,
                    request_deserializer=nifake__pb2.MethodWithProtoOnlyParameterRequest.FromString,
                    response_serializer=nifake__pb2.MethodWithProtoOnlyParameterResponse.SerializeToString,
            ),
            'ReadDataWithInOutIviTwist': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadDataWithInOutIviTwist,
                    request_deserializer=nifake__pb2.ReadDataWithInOutIviTwistRequest.FromString,
                    response_serializer=nifake__pb2.ReadDataWithInOutIviTwistResponse.SerializeToString,
            ),
            'ReadDataWithMultipleIviTwistParamSets': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadDataWithMultipleIviTwistParamSets,
                    request_deserializer=nifake__pb2.ReadDataWithMultipleIviTwistParamSetsRequest.FromString,
                    response_serializer=nifake__pb2.ReadDataWithMultipleIviTwistParamSetsResponse.SerializeToString,
            ),
            'InitExtCal': grpc.unary_unary_rpc_method_handler(
                    servicer.InitExtCal,
                    request_deserializer=nifake__pb2.InitExtCalRequest.FromString,
                    response_serializer=nifake__pb2.InitExtCalResponse.SerializeToString,
            ),
            'InitWithVarArgs': grpc.unary_unary_rpc_method_handler(
                    servicer.InitWithVarArgs,
                    request_deserializer=nifake__pb2.InitWithVarArgsRequest.FromString,
                    response_serializer=nifake__pb2.InitWithVarArgsResponse.SerializeToString,
            ),
            'MultipleArraysSameSizeWithOptional': grpc.unary_unary_rpc_method_handler(
                    servicer.MultipleArraysSameSizeWithOptional,
                    request_deserializer=nifake__pb2.MultipleArraysSameSizeWithOptionalRequest.FromString,
                    response_serializer=nifake__pb2.MultipleArraysSameSizeWithOptionalResponse.SerializeToString,
            ),
            'UseATwoDimensionParameter': grpc.unary_unary_rpc_method_handler(
                    servicer.UseATwoDimensionParameter,
                    request_deserializer=nifake__pb2.UseATwoDimensionParameterRequest.FromString,
                    response_serializer=nifake__pb2.UseATwoDimensionParameterResponse.SerializeToString,
            ),
            'ViUInt8ArrayInputFunction': grpc.unary_unary_rpc_method_handler(
                    servicer.ViUInt8ArrayInputFunction,
                    request_deserializer=nifake__pb2.ViUInt8ArrayInputFunctionRequest.FromString,
                    response_serializer=nifake__pb2.ViUInt8ArrayInputFunctionResponse.SerializeToString,
            ),
            'ViUInt8ArrayOutputFunction': grpc.unary_unary_rpc_method_handler(
                    servicer.ViUInt8ArrayOutputFunction,
                    request_deserializer=nifake__pb2.ViUInt8ArrayOutputFunctionRequest.FromString,
                    response_serializer=nifake__pb2.ViUInt8ArrayOutputFunctionResponse.SerializeToString,
            ),
            'ViInt16ArrayInputFunction': grpc.unary_unary_rpc_method_handler(
                    servicer.ViInt16ArrayInputFunction,
                    request_deserializer=nifake__pb2.ViInt16ArrayInputFunctionRequest.FromString,
                    response_serializer=nifake__pb2.ViInt16ArrayInputFunctionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'nifake_grpc.NiFake', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NiFake(object):
    """Missing associated documentation comment in .proto file."""

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
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/Abort',
            nifake__pb2.AbortRequest.SerializeToString,
            nifake__pb2.AbortResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BoolArrayOutputFunction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/BoolArrayOutputFunction',
            nifake__pb2.BoolArrayOutputFunctionRequest.SerializeToString,
            nifake__pb2.BoolArrayOutputFunctionResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/Close',
            nifake__pb2.CloseRequest.SerializeToString,
            nifake__pb2.CloseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EnumArrayOutputFunction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/EnumArrayOutputFunction',
            nifake__pb2.EnumArrayOutputFunctionRequest.SerializeToString,
            nifake__pb2.EnumArrayOutputFunctionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EnumInputFunctionWithDefaults(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/EnumInputFunctionWithDefaults',
            nifake__pb2.EnumInputFunctionWithDefaultsRequest.SerializeToString,
            nifake__pb2.EnumInputFunctionWithDefaultsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StringValuedEnumInputFunctionWithDefaults(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/StringValuedEnumInputFunctionWithDefaults',
            nifake__pb2.StringValuedEnumInputFunctionWithDefaultsRequest.SerializeToString,
            nifake__pb2.StringValuedEnumInputFunctionWithDefaultsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ErrorMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/ErrorMessage',
            nifake__pb2.ErrorMessageRequest.SerializeToString,
            nifake__pb2.ErrorMessageResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/FetchWaveform',
            nifake__pb2.FetchWaveformRequest.SerializeToString,
            nifake__pb2.FetchWaveformResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetABoolean(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetABoolean',
            nifake__pb2.GetABooleanRequest.SerializeToString,
            nifake__pb2.GetABooleanResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetANumber(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetANumber',
            nifake__pb2.GetANumberRequest.SerializeToString,
            nifake__pb2.GetANumberResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAStringOfFixedMaximumSize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetAStringOfFixedMaximumSize',
            nifake__pb2.GetAStringOfFixedMaximumSizeRequest.SerializeToString,
            nifake__pb2.GetAStringOfFixedMaximumSizeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAnIviDanceCharArray(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetAnIviDanceCharArray',
            nifake__pb2.GetAnIviDanceCharArrayRequest.SerializeToString,
            nifake__pb2.GetAnIviDanceCharArrayResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetArrayUsingIviDance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetArrayUsingIviDance',
            nifake__pb2.GetArrayUsingIviDanceRequest.SerializeToString,
            nifake__pb2.GetArrayUsingIviDanceResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetAttributeViBoolean',
            nifake__pb2.GetAttributeViBooleanRequest.SerializeToString,
            nifake__pb2.GetAttributeViBooleanResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetAttributeViInt32',
            nifake__pb2.GetAttributeViInt32Request.SerializeToString,
            nifake__pb2.GetAttributeViInt32Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAttributeViInt64(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetAttributeViInt64',
            nifake__pb2.GetAttributeViInt64Request.SerializeToString,
            nifake__pb2.GetAttributeViInt64Response.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetAttributeViReal64',
            nifake__pb2.GetAttributeViReal64Request.SerializeToString,
            nifake__pb2.GetAttributeViReal64Response.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetAttributeViSession',
            nifake__pb2.GetAttributeViSessionRequest.SerializeToString,
            nifake__pb2.GetAttributeViSessionResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetAttributeViString',
            nifake__pb2.GetAttributeViStringRequest.SerializeToString,
            nifake__pb2.GetAttributeViStringResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetCalDateAndTime',
            nifake__pb2.GetCalDateAndTimeRequest.SerializeToString,
            nifake__pb2.GetCalDateAndTimeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCalInterval(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetCalInterval',
            nifake__pb2.GetCalIntervalRequest.SerializeToString,
            nifake__pb2.GetCalIntervalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEnumValue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetEnumValue',
            nifake__pb2.GetEnumValueRequest.SerializeToString,
            nifake__pb2.GetEnumValueResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetError',
            nifake__pb2.GetErrorRequest.SerializeToString,
            nifake__pb2.GetErrorResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/InitWithOptions',
            nifake__pb2.InitWithOptionsRequest.SerializeToString,
            nifake__pb2.InitWithOptionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MultipleArrayTypes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/MultipleArrayTypes',
            nifake__pb2.MultipleArrayTypesRequest.SerializeToString,
            nifake__pb2.MultipleArrayTypesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MultipleArraysSameSize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/MultipleArraysSameSize',
            nifake__pb2.MultipleArraysSameSizeRequest.SerializeToString,
            nifake__pb2.MultipleArraysSameSizeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MultipleArraysDifferentSize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/MultipleArraysDifferentSize',
            nifake__pb2.MultipleArraysDifferentSizeRequest.SerializeToString,
            nifake__pb2.MultipleArraysDifferentSizeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MixedIviDanceAndLenMechanism(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/MixedIviDanceAndLenMechanism',
            nifake__pb2.MixedIviDanceAndLenMechanismRequest.SerializeToString,
            nifake__pb2.MixedIviDanceAndLenMechanismResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OneInputFunction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/OneInputFunction',
            nifake__pb2.OneInputFunctionRequest.SerializeToString,
            nifake__pb2.OneInputFunctionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ParametersAreMultipleTypes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/ParametersAreMultipleTypes',
            nifake__pb2.ParametersAreMultipleTypesRequest.SerializeToString,
            nifake__pb2.ParametersAreMultipleTypesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PoorlyNamedSimpleFunction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/PoorlyNamedSimpleFunction',
            nifake__pb2.PoorlyNamedSimpleFunctionRequest.SerializeToString,
            nifake__pb2.PoorlyNamedSimpleFunctionResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/Read',
            nifake__pb2.ReadRequest.SerializeToString,
            nifake__pb2.ReadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadFromChannel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/ReadFromChannel',
            nifake__pb2.ReadFromChannelRequest.SerializeToString,
            nifake__pb2.ReadFromChannelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReturnANumberAndAString(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/ReturnANumberAndAString',
            nifake__pb2.ReturnANumberAndAStringRequest.SerializeToString,
            nifake__pb2.ReturnANumberAndAStringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReturnMultipleTypes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/ReturnMultipleTypes',
            nifake__pb2.ReturnMultipleTypesRequest.SerializeToString,
            nifake__pb2.ReturnMultipleTypesResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/SetAttributeViBoolean',
            nifake__pb2.SetAttributeViBooleanRequest.SerializeToString,
            nifake__pb2.SetAttributeViBooleanResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/SetAttributeViInt32',
            nifake__pb2.SetAttributeViInt32Request.SerializeToString,
            nifake__pb2.SetAttributeViInt32Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAttributeViInt64(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/SetAttributeViInt64',
            nifake__pb2.SetAttributeViInt64Request.SerializeToString,
            nifake__pb2.SetAttributeViInt64Response.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/SetAttributeViReal64',
            nifake__pb2.SetAttributeViReal64Request.SerializeToString,
            nifake__pb2.SetAttributeViReal64Response.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/SetAttributeViString',
            nifake__pb2.SetAttributeViStringRequest.SerializeToString,
            nifake__pb2.SetAttributeViStringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TwoInputFunction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/TwoInputFunction',
            nifake__pb2.TwoInputFunctionRequest.SerializeToString,
            nifake__pb2.TwoInputFunctionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Use64BitNumber(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/Use64BitNumber',
            nifake__pb2.Use64BitNumberRequest.SerializeToString,
            nifake__pb2.Use64BitNumberResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteWaveform(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/WriteWaveform',
            nifake__pb2.WriteWaveformRequest.SerializeToString,
            nifake__pb2.WriteWaveformResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteWaveformNumpyComplex128(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/WriteWaveformNumpyComplex128',
            nifake__pb2.WriteWaveformNumpyComplex128Request.SerializeToString,
            nifake__pb2.WriteWaveformNumpyComplex128Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteWaveformNumpyComplex64(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/WriteWaveformNumpyComplex64',
            nifake__pb2.WriteWaveformNumpyComplex64Request.SerializeToString,
            nifake__pb2.WriteWaveformNumpyComplex64Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteWaveformNumpyComplexInterleavedI16(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/WriteWaveformNumpyComplexInterleavedI16',
            nifake__pb2.WriteWaveformNumpyComplexInterleavedI16Request.SerializeToString,
            nifake__pb2.WriteWaveformNumpyComplexInterleavedI16Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetCustomType(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/SetCustomType',
            nifake__pb2.SetCustomTypeRequest.SerializeToString,
            nifake__pb2.SetCustomTypeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetCustomTypeArray(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/SetCustomTypeArray',
            nifake__pb2.SetCustomTypeArrayRequest.SerializeToString,
            nifake__pb2.SetCustomTypeArrayResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCustomType(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetCustomType',
            nifake__pb2.GetCustomTypeRequest.SerializeToString,
            nifake__pb2.GetCustomTypeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCustomTypeArray(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetCustomTypeArray',
            nifake__pb2.GetCustomTypeArrayRequest.SerializeToString,
            nifake__pb2.GetCustomTypeArrayResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAnIviDanceWithATwistArray(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetAnIviDanceWithATwistArray',
            nifake__pb2.GetAnIviDanceWithATwistArrayRequest.SerializeToString,
            nifake__pb2.GetAnIviDanceWithATwistArrayResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAnIviDanceWithATwistString(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetAnIviDanceWithATwistString',
            nifake__pb2.GetAnIviDanceWithATwistStringRequest.SerializeToString,
            nifake__pb2.GetAnIviDanceWithATwistStringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DoubleAllTheNums(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/DoubleAllTheNums',
            nifake__pb2.DoubleAllTheNumsRequest.SerializeToString,
            nifake__pb2.DoubleAllTheNumsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AcceptListOfDurationsInSeconds(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/AcceptListOfDurationsInSeconds',
            nifake__pb2.AcceptListOfDurationsInSecondsRequest.SerializeToString,
            nifake__pb2.AcceptListOfDurationsInSecondsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReturnDurationInSeconds(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/ReturnDurationInSeconds',
            nifake__pb2.ReturnDurationInSecondsRequest.SerializeToString,
            nifake__pb2.ReturnDurationInSecondsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReturnListOfDurationsInSeconds(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/ReturnListOfDurationsInSeconds',
            nifake__pb2.ReturnListOfDurationsInSecondsRequest.SerializeToString,
            nifake__pb2.ReturnListOfDurationsInSecondsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureAbc(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/ConfigureAbc',
            nifake__pb2.ConfigureAbcRequest.SerializeToString,
            nifake__pb2.ConfigureAbcResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureEnums(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/ConfigureEnums',
            nifake__pb2.ConfigureEnumsRequest.SerializeToString,
            nifake__pb2.ConfigureEnumsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExportAttributeConfigurationBufferEx(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/ExportAttributeConfigurationBufferEx',
            nifake__pb2.ExportAttributeConfigurationBufferExRequest.SerializeToString,
            nifake__pb2.ExportAttributeConfigurationBufferExResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ImportAttributeConfigurationBufferEx(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/ImportAttributeConfigurationBufferEx',
            nifake__pb2.ImportAttributeConfigurationBufferExRequest.SerializeToString,
            nifake__pb2.ImportAttributeConfigurationBufferExResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FetchWithCustomSize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/FetchWithCustomSize',
            nifake__pb2.FetchWithCustomSizeRequest.SerializeToString,
            nifake__pb2.FetchWithCustomSizeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetParameterWithOverriddenGrpcName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetParameterWithOverriddenGrpcName',
            nifake__pb2.GetParameterWithOverriddenGrpcNameRequest.SerializeToString,
            nifake__pb2.GetParameterWithOverriddenGrpcNameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IviDanceWithTwistWithMultipleArraysAndOneBufferSize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/IviDanceWithTwistWithMultipleArraysAndOneBufferSize',
            nifake__pb2.IviDanceWithTwistWithMultipleArraysAndOneBufferSizeRequest.SerializeToString,
            nifake__pb2.IviDanceWithTwistWithMultipleArraysAndOneBufferSizeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FunctionWithOverriddenGrpcName2x(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/FunctionWithOverriddenGrpcName2x',
            nifake__pb2.FunctionWithOverriddenGrpcName2xRequest.SerializeToString,
            nifake__pb2.FunctionWithOverriddenGrpcName2xResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter',
            nifake__pb2.FunctionWith3dNumpyArrayOfNumpyComplex128InputParameterRequest.SerializeToString,
            nifake__pb2.FunctionWith3dNumpyArrayOfNumpyComplex128InputParameterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StringValuedEnumNoEnumGenerated(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/StringValuedEnumNoEnumGenerated',
            nifake__pb2.StringValuedEnumNoEnumGeneratedRequest.SerializeToString,
            nifake__pb2.StringValuedEnumNoEnumGeneratedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IviDanceWithATwistCalculatedSizeOut(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/IviDanceWithATwistCalculatedSizeOut',
            nifake__pb2.IviDanceWithATwistCalculatedSizeOutRequest.SerializeToString,
            nifake__pb2.IviDanceWithATwistCalculatedSizeOutResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/ImportAttributeConfigurationBuffer',
            nifake__pb2.ImportAttributeConfigurationBufferRequest.SerializeToString,
            nifake__pb2.ImportAttributeConfigurationBufferResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/ExportAttributeConfigurationBuffer',
            nifake__pb2.ExportAttributeConfigurationBufferRequest.SerializeToString,
            nifake__pb2.ExportAttributeConfigurationBufferResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Control4022(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/Control4022',
            nifake__pb2.Control4022Request.SerializeToString,
            nifake__pb2.Control4022Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AcceptViSessionArray(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/AcceptViSessionArray',
            nifake__pb2.AcceptViSessionArrayRequest.SerializeToString,
            nifake__pb2.AcceptViSessionArrayResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AcceptViUInt32Array(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/AcceptViUInt32Array',
            nifake__pb2.AcceptViUInt32ArrayRequest.SerializeToString,
            nifake__pb2.AcceptViUInt32ArrayResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BoolArrayInputFunction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/BoolArrayInputFunction',
            nifake__pb2.BoolArrayInputFunctionRequest.SerializeToString,
            nifake__pb2.BoolArrayInputFunctionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CloseExtCal(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/CloseExtCal',
            nifake__pb2.CloseExtCalRequest.SerializeToString,
            nifake__pb2.CloseExtCalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CommandWithReservedParam(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/CommandWithReservedParam',
            nifake__pb2.CommandWithReservedParamRequest.SerializeToString,
            nifake__pb2.CommandWithReservedParamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateConfigurationList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/CreateConfigurationList',
            nifake__pb2.CreateConfigurationListRequest.SerializeToString,
            nifake__pb2.CreateConfigurationListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CustomNestedStructRoundtrip(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/CustomNestedStructRoundtrip',
            nifake__pb2.CustomNestedStructRoundtripRequest.SerializeToString,
            nifake__pb2.CustomNestedStructRoundtripResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBitfieldAsEnumArray(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetBitfieldAsEnumArray',
            nifake__pb2.GetBitfieldAsEnumArrayRequest.SerializeToString,
            nifake__pb2.GetBitfieldAsEnumArrayResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAnIviDanceWithATwistArrayOfCustomType(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetAnIviDanceWithATwistArrayOfCustomType',
            nifake__pb2.GetAnIviDanceWithATwistArrayOfCustomTypeRequest.SerializeToString,
            nifake__pb2.GetAnIviDanceWithATwistArrayOfCustomTypeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAnIviDanceWithATwistArrayWithInputArray(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetAnIviDanceWithATwistArrayWithInputArray',
            nifake__pb2.GetAnIviDanceWithATwistArrayWithInputArrayRequest.SerializeToString,
            nifake__pb2.GetAnIviDanceWithATwistArrayWithInputArrayResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAnIviDanceWithATwistByteArray(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetAnIviDanceWithATwistByteArray',
            nifake__pb2.GetAnIviDanceWithATwistByteArrayRequest.SerializeToString,
            nifake__pb2.GetAnIviDanceWithATwistByteArrayResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAnIviDanceWithATwistStringStrlenBug(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetAnIviDanceWithATwistStringStrlenBug',
            nifake__pb2.GetAnIviDanceWithATwistStringStrlenBugRequest.SerializeToString,
            nifake__pb2.GetAnIviDanceWithATwistStringStrlenBugResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetArraySizeForCustomCode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetArraySizeForCustomCode',
            nifake__pb2.GetArraySizeForCustomCodeRequest.SerializeToString,
            nifake__pb2.GetArraySizeForCustomCodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetArrayViUInt8WithEnum(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetArrayViUInt8WithEnum',
            nifake__pb2.GetArrayViUInt8WithEnumRequest.SerializeToString,
            nifake__pb2.GetArrayViUInt8WithEnumResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetViUInt8(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetViUInt8',
            nifake__pb2.GetViUInt8Request.SerializeToString,
            nifake__pb2.GetViUInt8Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetViInt32Array(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetViInt32Array',
            nifake__pb2.GetViInt32ArrayRequest.SerializeToString,
            nifake__pb2.GetViInt32ArrayResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetViUInt32Array(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/GetViUInt32Array',
            nifake__pb2.GetViUInt32ArrayRequest.SerializeToString,
            nifake__pb2.GetViUInt32ArrayResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MethodUsingEnumWithGrpcNameValues(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/MethodUsingEnumWithGrpcNameValues',
            nifake__pb2.MethodUsingEnumWithGrpcNameValuesRequest.SerializeToString,
            nifake__pb2.MethodUsingEnumWithGrpcNameValuesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MethodWithGetLastErrorParam(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/MethodWithGetLastErrorParam',
            nifake__pb2.MethodWithGetLastErrorParamRequest.SerializeToString,
            nifake__pb2.MethodWithGetLastErrorParamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MethodWithGrpcOnlyParam(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/MethodWithGrpcOnlyParam',
            nifake__pb2.MethodWithGrpcOnlyParamRequest.SerializeToString,
            nifake__pb2.MethodWithGrpcOnlyParamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MethodUsingWholeAndFractionalNumbers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/MethodUsingWholeAndFractionalNumbers',
            nifake__pb2.MethodUsingWholeAndFractionalNumbersRequest.SerializeToString,
            nifake__pb2.MethodUsingWholeAndFractionalNumbersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MethodUsingWholeMappedNumbers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/MethodUsingWholeMappedNumbers',
            nifake__pb2.MethodUsingWholeMappedNumbersRequest.SerializeToString,
            nifake__pb2.MethodUsingWholeMappedNumbersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MethodWithGrpcFieldNumber(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/MethodWithGrpcFieldNumber',
            nifake__pb2.MethodWithGrpcFieldNumberRequest.SerializeToString,
            nifake__pb2.MethodWithGrpcFieldNumberResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MethodWithProtoOnlyParameter(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/MethodWithProtoOnlyParameter',
            nifake__pb2.MethodWithProtoOnlyParameterRequest.SerializeToString,
            nifake__pb2.MethodWithProtoOnlyParameterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadDataWithInOutIviTwist(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/ReadDataWithInOutIviTwist',
            nifake__pb2.ReadDataWithInOutIviTwistRequest.SerializeToString,
            nifake__pb2.ReadDataWithInOutIviTwistResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadDataWithMultipleIviTwistParamSets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/ReadDataWithMultipleIviTwistParamSets',
            nifake__pb2.ReadDataWithMultipleIviTwistParamSetsRequest.SerializeToString,
            nifake__pb2.ReadDataWithMultipleIviTwistParamSetsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InitExtCal(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/InitExtCal',
            nifake__pb2.InitExtCalRequest.SerializeToString,
            nifake__pb2.InitExtCalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InitWithVarArgs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/InitWithVarArgs',
            nifake__pb2.InitWithVarArgsRequest.SerializeToString,
            nifake__pb2.InitWithVarArgsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MultipleArraysSameSizeWithOptional(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/MultipleArraysSameSizeWithOptional',
            nifake__pb2.MultipleArraysSameSizeWithOptionalRequest.SerializeToString,
            nifake__pb2.MultipleArraysSameSizeWithOptionalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UseATwoDimensionParameter(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/UseATwoDimensionParameter',
            nifake__pb2.UseATwoDimensionParameterRequest.SerializeToString,
            nifake__pb2.UseATwoDimensionParameterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ViUInt8ArrayInputFunction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/ViUInt8ArrayInputFunction',
            nifake__pb2.ViUInt8ArrayInputFunctionRequest.SerializeToString,
            nifake__pb2.ViUInt8ArrayInputFunctionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ViUInt8ArrayOutputFunction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/ViUInt8ArrayOutputFunction',
            nifake__pb2.ViUInt8ArrayOutputFunctionRequest.SerializeToString,
            nifake__pb2.ViUInt8ArrayOutputFunctionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ViInt16ArrayInputFunction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifake_grpc.NiFake/ViInt16ArrayInputFunction',
            nifake__pb2.ViInt16ArrayInputFunctionRequest.SerializeToString,
            nifake__pb2.ViInt16ArrayInputFunctionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/nifake/session.py sha256=336ed2acc2922ab1b78825e814582f4675e1ad087099bf2cbc7de3f8791537bc bytes=66466 -->
## FILE: generated/nifake/nifake/session.py

- repository: `ni/nimi-python`
- source_path: `generated/nifake/nifake/session.py`
- sha256: `336ed2acc2922ab1b78825e814582f4675e1ad087099bf2cbc7de3f8791537bc`
- bytes: 66466

````python
# -*- coding: utf-8 -*-
# This file was generated
import array  # noqa: F401
# Used by @ivi_synchronized
from functools import wraps

import nifake._attributes as _attributes
import nifake._converters as _converters
import nifake._library_interpreter as _library_interpreter
import nifake.enums as enums
import nifake.errors as errors

import nifake.custom_struct as custom_struct  # noqa: F401

import nifake.custom_struct_typedef as custom_struct_typedef  # noqa: F401

import nifake.custom_struct_nested_typedef as custom_struct_nested_typedef  # noqa: F401

import hightime
import nitclk

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
    '''Base class for all NI-FAKE sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    float_enum = _attributes.AttributeEnum(_attributes.AttributeViReal64, enums.FloatEnum, 1000005)
    '''Type: enums.FloatEnum

    A property with an enum that is also a float
    '''
    read_write_bool = _attributes.AttributeViBoolean(1000000)
    '''Type: bool

    A property of type bool with read/write access.
    '''
    read_write_color = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.Color, 1000003)
    '''Type: enums.Color

    A property of type Color with read/write access.
    '''
    read_write_comma_separated_string = _attributes.AttributeViStringCommaSeparated(1000015)
    '''Type: str

    A property of type comma separated string with read/write access.
    '''
    read_write_double = _attributes.AttributeViReal64(1000001)
    '''Type: float

    A property of type float with read/write access.
    '''
    read_write_double_with_converter = _attributes.AttributeViReal64TimeDeltaSeconds(1000007)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Property in seconds
    '''
    read_write_double_with_repeated_capability = _attributes.AttributeViReal64(1000009)
    '''Type: float

    Tip:
    This property can be set/get on specific channels within your :py:class:`nifake.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].read_write_double_with_repeated_capability`

    To set/get on all channels, you can call the property directly on the :py:class:`nifake.Session`.

    Example: :py:attr:`my_session.read_write_double_with_repeated_capability`
    '''
    read_write_enum_with_converter = _attributes.AttributeEnumWithConverter(_attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EnumWithConverter, 1000011), _converters.convert_from_enum_with_converter_enum, _converters.convert_to_enum_with_converter_enum)
    read_write_int64 = _attributes.AttributeViInt64(1000006)
    '''Type: int

    A property of type 64-bit integer with read/write access.
    '''
    read_write_integer = _attributes.AttributeViInt32(1000004)
    '''Type: int

    A property of type integer with read/write access.
    '''
    read_write_integer_with_converter = _attributes.AttributeViInt32TimeDeltaMilliseconds(1000008)
    '''Type: hightime.timedelta, datetime.timedelta, or int in milliseconds

    Property in milliseconds
    '''
    read_write_integer_with_month_converter = _attributes.AttributeViInt32TimeDeltaMonths(1000014)
    '''Type: hightime.timedelta, datetime.timedelta, or int in months

    Property in months
    '''
    read_write_string = _attributes.AttributeViString(1000002)
    '''Type: str

    A property of type string with read/write access.
    '''
    read_write_string_repeated_capability = _attributes.AttributeViStringRepeatedCapability(1000010)
    '''Type: Any repeated capability type, as defined in nimi-python:
        - str
        - str - Comma delimited list
        - str - Range (using '-' or ':')
        - int
        - Basic sequence types (list, tuple, range, slice) of other supported types

    A property with read/write access, that represents a repeated capability

    Tip:
    This property can be set/get on specific instruments within your :py:class:`nifake.Session` instance.
    Use Python index notation on the repeated capabilities container instruments to specify a subset.

    Example: :py:attr:`my_session.instruments[ ... ].read_write_string_repeated_capability`

    To set/get on all instruments, you can call the property directly on the :py:class:`nifake.Session`.

    Example: :py:attr:`my_session.read_write_string_repeated_capability`
    '''
    sample_count = _attributes.AttributeViInt32(1000012)
    sample_interval = _attributes.AttributeViReal64(1000013)

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
        self.sites = _RepeatedCapabilities(self, 'site', repeated_capability_list)
        self.instruments = _RepeatedCapabilities(self, '', repeated_capability_list)

        # Finally, set _is_frozen to True which is used to prevent clients from accidentally adding
        # members when trying to set a property with a typo.
        self._is_frozen = freeze_it

    def __repr__(self):
        return '{0}.{1}({2})'.format('nifake', self.__class__.__name__, self._param_list)

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("'{0}' object has no attribute '{1}'".format(type(self).__name__, key))
        object.__setattr__(self, key, value)

    ''' These are code-generated '''

    @ivi_synchronized
    def function_with_repeated_capability_type(self):
        r'''function_with_repeated_capability_type

        A method with a parameter that specifies repeated_capability_type.

        Tip:
        This method can be called on specific sites within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].function_with_repeated_capability_type`

        To call the method on all sites, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session.function_with_repeated_capability_type`
        '''
        self._interpreter.function_with_repeated_capability_type(self._repeated_capability)

    @ivi_synchronized
    def _get_attribute_vi_boolean(self, attribute_id):
        r'''_get_attribute_vi_boolean

        Queries the value of a ViBoolean property.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_boolean`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (bool): Returns the value of the property.

        '''
        attribute_value = self._interpreter.get_attribute_vi_boolean(self._repeated_capability, attribute_id)
        return attribute_value

    @ivi_synchronized
    def _get_attribute_vi_int32(self, attribute_id):
        r'''_get_attribute_vi_int32

        Queries the value of a ViInt32 property.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int32`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (int): Returns the value of the property.

        '''
        attribute_value = self._interpreter.get_attribute_vi_int32(self._repeated_capability, attribute_id)
        return attribute_value

    @ivi_synchronized
    def _get_attribute_vi_int64(self, attribute_id):
        r'''_get_attribute_vi_int64

        Queries the value of a ViInt64 property.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int64`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (int): Returns the value of the property.

        '''
        attribute_value = self._interpreter.get_attribute_vi_int64(self._repeated_capability, attribute_id)
        return attribute_value

    @ivi_synchronized
    def _get_attribute_vi_real64(self, attribute_id):
        r'''_get_attribute_vi_real64

        Queries the value of a ViReal property.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_real64`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (float): Returns the value of the property.

        '''
        attribute_value = self._interpreter.get_attribute_vi_real64(self._repeated_capability, attribute_id)
        return attribute_value

    @ivi_synchronized
    def _get_attribute_vi_string(self, attribute_id):
        r'''_get_attribute_vi_string

        Queries the value of a ViBoolean property.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_string`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (str): Returns the value of the property.

        '''
        attribute_value = self._interpreter.get_attribute_vi_string(self._repeated_capability, attribute_id)
        return attribute_value

    @ivi_synchronized
    def _get_channel_names(self, indices):
        r'''_get_channel_names

        Returns a list of channel names for the given channel indices.

        Args:
            indices (basic sequence types or str or int): Index list for the channels in the session. Valid values are from zero to the total number of channels in the session minus one. The index string can be one of the following formats:

                -   A comma-separated list—for example, "0,2,3,1"
                -   A range using a hyphen—for example, "0-3"
                -   A range using a colon—for example, "0:3 "

                You can combine comma-separated lists and ranges that use a hyphen or colon. Both out-of-order and repeated indices are supported ("2,3,0," "1,2,2,3"). White space characters, including spaces, tabs, feeds, and carriage returns, are allowed between characters. Ranges can be incrementing or decrementing.


        Returns:
            names (list of str): The channel name(s) at the specified indices.

        '''
        indices = _converters.convert_repeated_capabilities_without_prefix(indices)
        names = self._interpreter.get_channel_names(indices)
        return _converters.convert_comma_separated_string_to_list(names)

    def lock(self):
        '''lock

        Obtains a multithread lock on the device session. Before doing so, the
        software waits until all other execution threads release their locks
        on the device session.

        Other threads may have obtained a lock on this session for the
        following reasons:

            -  The application called the lock method.
            -  A call to NI-FAKE locked the session.
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
            lock (context manager): When used in a with statement, nifake.Session.lock acts as
            a context manager and unlock will be called when the with block is exited
        '''
        self._interpreter.lock()  # We do not call this in the context manager so that this function can
        # act standalone as well and let the client call unlock() explicitly. If they do use the context manager,
        # that will handle the unlock for them
        return _Lock(self)

    @ivi_synchronized
    def get_channel_names(self, indices):
        '''get_channel_names

        Returns a list of channel names for the given channel indices.

        Args:
            indices (basic sequence types or str or int): Index list for the channels in the session. Valid values are from zero to the total number of channels in the session minus one. The index string can be one of the following formats:

                -   A comma-separated list—for example, "0,2,3,1"
                -   A range using a hyphen—for example, "0-3"
                -   A range using a colon—for example, "0:3 "

                You can combine comma-separated lists and ranges that use a hyphen or colon. Both out-of-order and repeated indices are supported ("2,3,0," "1,2,2,3"). White space characters, including spaces, tabs, feeds, and carriage returns, are allowed between characters. Ranges can be incrementing or decrementing.


        Returns:
            names (list of str): The channel name(s) at the specified indices.

        '''
        return self._get_channel_names(indices)

    @ivi_synchronized
    def read_from_channel(self, maximum_time):
        r'''read_from_channel

        Acquires a single measurement and returns the measured value.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].read_from_channel`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session.read_from_channel`

        Args:
            maximum_time (hightime.timedelta): Specifies the **maximum_time** allowed in milliseconds.


        Returns:
            reading (float): The measured value.

        '''
        maximum_time = _converters.convert_timedelta_to_milliseconds_int32(maximum_time)
        reading = self._interpreter.read_from_channel(self._repeated_capability, maximum_time)
        return reading

    @ivi_synchronized
    def _set_attribute_vi_boolean(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_boolean

        This method sets the value of a ViBoolean property.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

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

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int32`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (int): Pass the value that you want to set the property to.

        '''
        self._interpreter.set_attribute_vi_int32(self._repeated_capability, attribute_id, attribute_value)

    @ivi_synchronized
    def _set_attribute_vi_int64(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_int64

        This method sets the value of a ViInt64 property.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int64`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (int): Pass the value that you want to set the property to.

        '''
        self._interpreter.set_attribute_vi_int64(self._repeated_capability, attribute_id, attribute_value)

    @ivi_synchronized
    def _set_attribute_vi_real64(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_real64

        This method sets the value of a ViReal64 property.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

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

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

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

        Takes the errorCode returned by a functiona and returns it as a user-readable string.

        Args:
            error_code (int): The errorCode returned from the instrument.


        Returns:
            error_message (str): The error information formatted into a string.

        '''
        error_message = self._interpreter.error_message(error_code)
        return error_message


class Session(_SessionBase):
    '''An NI-FAKE session to a fake MI driver whose sole purpose is to test nimi-python code generation'''

    def __init__(self, resource_name, options={}, id_query=False, reset_device=False, *, grpc_options=None):
        r'''An NI-FAKE session to a fake MI driver whose sole purpose is to test nimi-python code generation

        Creates a new IVI instrument driver session.

        Args:
            resource_name (str): Caution: This is just some string.

                Contains the **resource_name** of the device to initialize.

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

            id_query (bool): NI-FAKE is probably not needed.

                +----------------+---+------------------+
                | True (default) | 1 | Perform ID Query |
                +----------------+---+------------------+
                | False          | 0 | Skip ID Query    |
                +----------------+---+------------------+

            reset_device (bool): Specifies whether to reset

                +----------------+---+--------------+
                | True (default) | 1 | Reset Device |
                +----------------+---+--------------+
                | False          | 0 | Don't Reset  |
                +----------------+---+--------------+

            grpc_options (nifake.grpc_session_options.GrpcSessionOptions): MeasurementLink gRPC session options


        Returns:
            session (nifake.Session): A session object representing the device.

        '''
        if grpc_options:
            import nifake._grpc_stub_interpreter as _grpc_stub_interpreter
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
        self._interpreter.set_session_handle(self._init_with_options(resource_name, options, id_query, reset_device))

        # NI-TClk does not work over NI gRPC Device Server
        if not grpc_options:
            self.tclk = nitclk.SessionReference(self._interpreter.get_session_handle())

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("resource_name=" + pp.pformat(resource_name))
        param_list.append("options=" + pp.pformat(options))
        param_list.append("reset_device=" + pp.pformat(reset_device))
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

        Initiates a thingie.

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

        Aborts a previously initiated thingie.
        '''
        self._interpreter.abort()

    @ivi_synchronized
    def accept_list_of_durations_in_seconds(self, delays):
        r'''accept_list_of_durations_in_seconds

        Accepts list of hightime.timedelta or datetime.timedelta or float instances representing time delays.

        Args:
            delays (hightime.timedelta, datetime.timedelta, or float in seconds): A collection of time delay values.

        '''
        delays = _converters.convert_timedeltas_to_seconds_real64(delays)
        self._interpreter.accept_list_of_durations_in_seconds(delays)

    @ivi_synchronized
    def bool_array_output_function(self, number_of_elements):
        r'''bool_array_output_function

        This method returns an array of booleans.

        Args:
            number_of_elements (int): Number of elements in the array.


        Returns:
            an_array (list of bool): Contains an array of booleans

        '''
        an_array = self._interpreter.bool_array_output_function(number_of_elements)
        return an_array

    @ivi_synchronized
    def configure_abc(self):
        r'''configure_abc

        TBD
        '''
        self._interpreter.configure_abc()

    @ivi_synchronized
    def custom_nested_struct_roundtrip(self, nested_custom_type_in):
        r'''custom_nested_struct_roundtrip

        TBD

        Args:
            nested_custom_type_in (CustomStructNestedTypedef):


        Returns:
            nested_custom_type_out (CustomStructNestedTypedef):

        '''
        nested_custom_type_out = self._interpreter.custom_nested_struct_roundtrip(nested_custom_type_in)
        return nested_custom_type_out

    @ivi_synchronized
    def double_all_the_nums(self, numbers):
        r'''double_all_the_nums

        Test for buffer with converter

        Args:
            numbers (list of float): numbers is an array of numbers we want to double.

        '''
        numbers = _converters.convert_double_each_element(numbers)
        self._interpreter.double_all_the_nums(numbers)

    @ivi_synchronized
    def enum_array_output_function(self, number_of_elements):
        r'''enum_array_output_function

        This method returns an array of enums, stored as 16 bit integers under the hood.

        Args:
            number_of_elements (int): Number of elements in the array.


        Returns:
            an_array (list of enums.Turtle): Contains an array of enums, stored as 16 bit integers under the hood

        '''
        an_array = self._interpreter.enum_array_output_function(number_of_elements)
        return an_array

    @ivi_synchronized
    def enum_input_function_with_defaults(self, a_turtle=enums.Turtle.LEONARDO):
        r'''enum_input_function_with_defaults

        This method takes one parameter other than the session, which happens to be an enum and has a default value.

        Args:
            a_turtle (enums.Turtle): Indicates a ninja turtle

                +---+---------------+
                | 0 | Leonardo      |
                +---+---------------+
                | 1 | Donatello     |
                +---+---------------+
                | 2 | Raphael       |
                +---+---------------+
                | 3 | Mich elangelo |
                +---+---------------+

        '''
        if type(a_turtle) is not enums.Turtle:
            raise TypeError('Parameter a_turtle must be of type ' + str(enums.Turtle))
        self._interpreter.enum_input_function_with_defaults(a_turtle)

    @ivi_synchronized
    def export_attribute_configuration_buffer(self):
        r'''export_attribute_configuration_buffer

        Export configuration buffer.

        Returns:
            configuration (bytes):

        '''
        configuration = self._interpreter.export_attribute_configuration_buffer()
        return _converters.convert_to_bytes(configuration)

    @ivi_synchronized
    def fetch_waveform(self, number_of_samples):
        r'''fetch_waveform

        Returns waveform data.

        Args:
            number_of_samples (int): Number of samples to return


        Returns:
            waveform_data (array.array("d")): Samples fetched from the device. Array should be numberOfSamples big.

        '''
        waveform_data = self._interpreter.fetch_waveform(number_of_samples)
        return waveform_data

    @ivi_synchronized
    def fetch_waveform_into(self, waveform_data):
        r'''fetch_waveform_into

        Returns waveform data.

        Args:
            waveform_data (numpy.array(dtype=numpy.float64)): Samples fetched from the device. Array should be numberOfSamples big.

        '''
        import numpy

        if type(waveform_data) is not numpy.ndarray:
            raise TypeError('waveform_data must be {0}, is {1}'.format(numpy.ndarray, type(waveform_data)))
        if numpy.isfortran(waveform_data) is True:
            raise TypeError('waveform_data must be in C-order')
        if waveform_data.dtype is not numpy.dtype('float64'):
            raise TypeError('waveform_data must be numpy.ndarray of dtype=float64, is ' + str(waveform_data.dtype))
        self._interpreter.fetch_waveform_into(waveform_data)

    def function_with_3d_numpy_array_of_numpy_complex128_input_parameter(self, multidimensional_array):
        r'''function_with_3d_numpy_array_of_numpy_complex128_input_parameter

        Method that takes a 3D numpy array of numpy complex128 as an input parameter.

        Args:
            multidimensional_array (numpy.array(dtype=numpy.complex128)): Specifies the 3D array of numpy complex numbers to write.

        '''
        import numpy

        if type(multidimensional_array) is not numpy.ndarray:
            raise TypeError('multidimensional_array must be {0}, is {1}'.format(numpy.ndarray, type(multidimensional_array)))
        if numpy.isfortran(multidimensional_array) is True:
            raise TypeError('multidimensional_array must be in C-order')
        if multidimensional_array.dtype is not numpy.dtype('complex128'):
            raise TypeError('multidimensional_array must be numpy.ndarray of dtype=complex128, is ' + str(multidimensional_array.dtype))
        if multidimensional_array.ndim != 3:
            raise TypeError('multidimensional_array must be numpy.ndarray of dimension=3, is ' + str(multidimensional_array.ndim))
        self._interpreter.function_with_3d_numpy_array_of_numpy_complex128_input_parameter(multidimensional_array)

    @ivi_synchronized
    def function_with_intflag_parameter(self, flag):
        r'''function_with_intflag_parameter

        Calls a method that takes a flag parameter which can be OR'd from multiple enum values.

        Args:
            flag (enums.IntFlagEnum): A flag parameter that can be a combination (bitwise OR) of IntFlagEnum values.

        '''
        if type(flag) is not enums.IntFlagEnum:
            raise TypeError('Parameter flag must be of type ' + str(enums.IntFlagEnum))
        self._interpreter.function_with_intflag_parameter(flag)

    @ivi_synchronized
    def get_a_boolean(self):
        r'''get_a_boolean

        Returns a boolean.

        Note: This method rules!

        Returns:
            a_boolean (bool): Contains a boolean.

        '''
        a_boolean = self._interpreter.get_a_boolean()
        return a_boolean

    @ivi_synchronized
    def get_a_number(self):
        r'''get_a_number

        Returns a number.

        Note: This method rules!

        Returns:
            a_number (int): Contains a number.

        '''
        a_number = self._interpreter.get_a_number()
        return a_number

    @ivi_synchronized
    def get_a_string_of_fixed_maximum_size(self):
        r'''get_a_string_of_fixed_maximum_size

        Illustrates returning a string of fixed size.

        Returns:
            a_string (str): String comes back here. Buffer must be 256 big.

        '''
        a_string = self._interpreter.get_a_string_of_fixed_maximum_size()
        return a_string

    @ivi_synchronized
    def get_a_string_using_python_code(self, a_number):
        r'''get_a_string_using_python_code

        Returns a number and a string.

        Note: This method rules!

        Args:
            a_number (int): Contains a number.


        Returns:
            a_string (str): Contains a string of length aNumber.

        '''
        a_string = self._interpreter.get_a_string_using_python_code(a_number)
        return a_string

    @ivi_synchronized
    def get_an_ivi_dance_char_array(self):
        r'''get_an_ivi_dance_char_array

        TBD

        Returns:
            char_array (str):

        '''
        char_array = self._interpreter.get_an_ivi_dance_char_array()
        return char_array

    @ivi_synchronized
    def get_an_ivi_dance_with_a_twist_string(self):
        r'''get_an_ivi_dance_with_a_twist_string

        TBD

        Returns:
            a_string (str):

        '''
        a_string = self._interpreter.get_an_ivi_dance_with_a_twist_string()
        return a_string

    @ivi_synchronized
    def get_array_for_python_code_custom_type(self):
        r'''get_array_for_python_code_custom_type

        This method returns an array for use in python-code size mechanism.

        Returns:
            array_out (list of CustomStruct): Array of custom type using python-code size mechanism

        '''
        array_out = self._interpreter.get_array_for_python_code_custom_type()
        return array_out

    @ivi_synchronized
    def get_array_for_python_code_double(self):
        r'''get_array_for_python_code_double

        This method returns an array for use in python-code size mechanism.

        Returns:
            array_out (list of float): Array of double using python-code size mechanism

        '''
        array_out = self._interpreter.get_array_for_python_code_double()
        return array_out

    @ivi_synchronized
    def get_array_size_for_python_code(self):
        r'''get_array_size_for_python_code

        This method returns the size of the array for use in python-code size mechanism.

        Returns:
            size_out (int): Size of array

        '''
        size_out = self._interpreter.get_array_size_for_python_code()
        return size_out

    @ivi_synchronized
    def get_array_using_ivi_dance(self):
        r'''get_array_using_ivi_dance

        This method returns an array of float whose size is determined with the IVI dance.

        Returns:
            array_out (list of float): The array returned by this method

        '''
        array_out = self._interpreter.get_array_using_ivi_dance()
        return array_out

    @ivi_synchronized
    def _get_cal_date_and_time(self, cal_type):
        r'''_get_cal_date_and_time

        Returns the date and time of the last calibration performed.

        Args:
            cal_type (int): Specifies the type of calibration performed (external or self-calibration).


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
    def get_cal_interval(self):
        r'''get_cal_interval

        Returns the recommended maximum interval, in **months**, between external calibrations.

        Returns:
            months (hightime.timedelta): Specifies the recommended maximum interval, in **months**, between external calibrations.

        '''
        months = self._interpreter.get_cal_interval()
        return _converters.convert_month_to_timedelta(months)

    @ivi_synchronized
    def get_custom_type(self):
        r'''get_custom_type

        This method returns a custom type.

        Returns:
            cs (CustomStruct): Set using custom type

        '''
        cs = self._interpreter.get_custom_type()
        return cs

    @ivi_synchronized
    def get_custom_type_array(self, number_of_elements):
        r'''get_custom_type_array

        This method returns a custom type.

        Args:
            number_of_elements (int): Number of elements in the array.


        Returns:
            cs (list of CustomStruct): Get using custom type

        '''
        cs = self._interpreter.get_custom_type_array(number_of_elements)
        return cs

    @ivi_synchronized
    def get_custom_type_typedef(self):
        r'''get_custom_type_typedef

        This method returns a custom type with typedef and a custom type with nested typedef.

        Returns:
            cst (CustomStructTypedef): An object of a custom type with typedef

            csnt (CustomStructNestedTypedef): An object of a custom type with nested typedef

        '''
        cst, csnt = self._interpreter.get_custom_type_typedef()
        return cst, csnt

    @ivi_synchronized
    def get_enum_value(self):
        r'''get_enum_value

        Returns an enum value

        Note: Splinter is not supported.

        Returns:
            a_quantity (int): This is an amount.

                Note: The amount will be between -2^31 and (2^31-1)

            a_turtle (enums.Turtle): Indicates a ninja turtle

                +---+---------------+
                | 0 | Leonardo      |
                +---+---------------+
                | 1 | Donatello     |
                +---+---------------+
                | 2 | Raphael       |
                +---+---------------+
                | 3 | Mich elangelo |
                +---+---------------+

        '''
        a_quantity, a_turtle = self._interpreter.get_enum_value()
        return a_quantity, a_turtle

    @ivi_synchronized
    def get_cal_date_and_time(self, cal_type):
        '''get_cal_date_and_time

        Returns the date and time of the last calibration performed.

        Args:
            cal_type (int): Specifies the type of calibration performed (external or self-calibration).


        Returns:
            last_cal_datetime (hightime.datetime): Indicates date and time of the last calibration.

        '''
        month, day, year, hour, minute = self._get_cal_date_and_time(cal_type)
        return hightime.datetime(year, month, day, hour, minute)

    @ivi_synchronized
    def get_parameter_with_overridden_grpc_name(self, enum_parameter):
        r'''get_parameter_with_overridden_grpc_name

        TBD

        Args:
            enum_parameter (enums.Turtle):


        Returns:
            original_parameter (int):

        '''
        if type(enum_parameter) is not enums.Turtle:
            raise TypeError('Parameter enum_parameter must be of type ' + str(enums.Turtle))
        original_parameter = self._interpreter.get_parameter_with_overridden_grpc_name(enum_parameter)
        return original_parameter

    @ivi_synchronized
    def import_attribute_configuration_buffer(self, configuration):
        r'''import_attribute_configuration_buffer

        Import configuration buffer.

        Args:
            configuration (bytes):

        '''
        configuration = _converters.convert_to_bytes(configuration)
        self._interpreter.import_attribute_configuration_buffer(configuration)

    @ivi_synchronized
    def import_attribute_configuration_buffer_ex(self, configuration):
        r'''import_attribute_configuration_buffer_ex

        TBD

        Args:
            configuration (list of ViAddr):

        '''
        self._interpreter.import_attribute_configuration_buffer_ex(configuration)

    def _init_with_options(self, resource_name, option_string, id_query=False, reset_device=False):
        r'''_init_with_options

        Creates a new IVI instrument driver session.

        Args:
            resource_name (str): Caution: This is just some string.

                Contains the **resource_name** of the device to initialize.

            option_string (dict): Some options

            id_query (bool): NI-FAKE is probably not needed.

                +----------------+---+------------------+
                | True (default) | 1 | Perform ID Query |
                +----------------+---+------------------+
                | False          | 0 | Skip ID Query    |
                +----------------+---+------------------+

            reset_device (bool): Specifies whether to reset

                +----------------+---+--------------+
                | True (default) | 1 | Reset Device |
                +----------------+---+--------------+
                | False          | 0 | Don't Reset  |
                +----------------+---+--------------+


        Returns:
            vi (int): Returns a ViSession handle that you use.

        '''
        option_string = _converters.convert_init_with_options_dictionary(option_string)
        vi = self._interpreter.init_with_options(resource_name, id_query, reset_device, option_string)
        return vi

    @ivi_synchronized
    def _initiate(self):
        r'''_initiate

        Initiates a thingie.
        '''
        self._interpreter.initiate()

    @ivi_synchronized
    def method_using_whole_and_fractional_numbers(self):
        r'''method_using_whole_and_fractional_numbers

        TBD

        Returns:
            whole_number (int):

            fractional_number (float):

        '''
        whole_number, fractional_number = self._interpreter.method_using_whole_and_fractional_numbers()
        return whole_number, fractional_number

    @ivi_synchronized
    def method_with_grpc_only_param(self, simple_param):
        r'''method_with_grpc_only_param

        TBD

        Args:
            simple_param (int):

        '''
        self._interpreter.method_with_grpc_only_param(simple_param)

    @ivi_synchronized
    def method_with_proto_only_parameter(self, attribute_value):
        r'''method_with_proto_only_parameter

        TBD

        Args:
            attribute_value (int):

        '''
        self._interpreter.method_with_proto_only_parameter(attribute_value)

    @ivi_synchronized
    def mixed_ivi_dance_and_len_mechanism(self, input_values):
        r'''mixed_ivi_dance_and_len_mechanism

        Test method with mixed size mechanisms: one len-sized input array and one IVI-dance output array.

        Args:
            input_values (list of float): Input array of doubles using len size mechanism.


        Returns:
            output_array (list of int): Output array using IVI-dance size mechanism.

        '''
        output_array = self._interpreter.mixed_ivi_dance_and_len_mechanism(input_values)
        return output_array

    @ivi_synchronized
    def multiple_array_types(self, output_array_size, input_array_of_floats, input_array_of_integers=None):
        r'''multiple_array_types

        Receives and returns multiple types of arrays.

        Args:
            output_array_size (int): Size of the array that will be returned.

            input_array_of_floats (list of float): Array of floats

            input_array_of_integers (list of int): Array of integers. Optional. If passed in then size must match that of inputArrayOfFloats.


        Returns:
            output_array (list of float): Array that will be returned.

                Note: The size must be at least outputArraySize.

            output_array_of_fixed_length (list of float): An array of doubles with fixed size.

        '''
        if input_array_of_integers is not None and len(input_array_of_integers) != len(input_array_of_floats):  # case S160
            raise ValueError("Length of input_array_of_integers and input_array_of_floats parameters do not match.")  # case S160
        output_array, output_array_of_fixed_length = self._interpreter.multiple_array_types(output_array_size, input_array_of_floats, input_array_of_integers)
        return output_array, output_array_of_fixed_length

    @ivi_synchronized
    def multiple_arrays_different_size(self, values_array, data_array):
        r'''multiple_arrays_different_size

        Test method with multiple arrays that have different size parameters. This tests the length handling mechanism where different array parameters can reference different size parameters.

        Args:
            values_array (list of float): Array of double values with its own size parameter.

            data_array (list of int): Array of integer values with a different size parameter.

        '''
        self._interpreter.multiple_arrays_different_size(values_array, data_array)

    @ivi_synchronized
    def multiple_arrays_same_size(self, values1, values2, values3, values4):
        r'''multiple_arrays_same_size

        Method to test multiple arrays that use the same size

        Args:
            values1 (list of float): Array 1 of same size.

            values2 (list of float): Array 2 of same size.

            values3 (list of float): Array 3 of same size.

            values4 (list of float): Array 4 of same size.

        '''
        if values2 is not None and len(values2) != len(values1):  # case S160
            raise ValueError("Length of values2 and values1 parameters do not match.")  # case S160
        if values3 is not None and len(values3) != len(values1):  # case S160
            raise ValueError("Length of values3 and values1 parameters do not match.")  # case S160
        if values4 is not None and len(values4) != len(values1):  # case S160
            raise ValueError("Length of values4 and values1 parameters do not match.")  # case S160
        self._interpreter.multiple_arrays_same_size(values1, values2, values3, values4)

    @ivi_synchronized
    def one_input_function(self, a_number):
        r'''one_input_function

        This method takes one parameter other than the session.

        Args:
            a_number (int): Contains a number

        '''
        self._interpreter.one_input_function(a_number)

    @ivi_synchronized
    def parameters_are_multiple_types(self, a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, a_string):
        r'''parameters_are_multiple_types

        Has parameters of multiple types.

        Args:
            a_boolean (bool): Contains a boolean.

            an_int32 (int): Contains a 32-bit integer.

            an_int64 (int): Contains a 64-bit integer.

            an_int_enum (enums.Turtle): Indicates a ninja turtle

                +---+---------------+
                | 0 | Leonardo      |
                +---+---------------+
                | 1 | Donatello     |
                +---+---------------+
                | 2 | Raphael       |
                +---+---------------+
                | 3 | Mich elangelo |
                +---+---------------+

            a_float (float): The measured value.

            a_float_enum (enums.FloatEnum): A float enum.

            a_string (str): An IVI dance string.

        '''
        if type(an_int_enum) is not enums.Turtle:
            raise TypeError('Parameter an_int_enum must be of type ' + str(enums.Turtle))
        if type(a_float_enum) is not enums.FloatEnum:
            raise TypeError('Parameter a_float_enum must be of type ' + str(enums.FloatEnum))
        self._interpreter.parameters_are_multiple_types(a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, a_string)

    @ivi_synchronized
    def simple_function(self):
        r'''simple_function

        This method takes no parameters other than the session.
        '''
        self._interpreter.simple_function()

    @ivi_synchronized
    def read(self, maximum_time):
        r'''read

        Acquires a single measurement and returns the measured value.

        Args:
            maximum_time (hightime.timedelta): Specifies the **maximum_time** allowed in seconds.


        Returns:
            reading (float): The measured value.

        '''
        maximum_time = _converters.convert_timedelta_to_seconds_real64(maximum_time)
        reading = self._interpreter.read(maximum_time)
        return reading

    @ivi_synchronized
    def return_a_number_and_a_string(self):
        r'''return_a_number_and_a_string

        Returns a number and a string.

        Note: This method rules!

        Returns:
            a_number (int): Contains a number.

            a_string (str): Contains a string. Buffer must be 256 bytes or larger.

        '''
        a_number, a_string = self._interpreter.return_a_number_and_a_string()
        return a_number, a_string

    @ivi_synchronized
    def return_duration_in_seconds(self):
        r'''return_duration_in_seconds

        Returns a hightime.timedelta instance.

        Returns:
            timedelta (hightime.timedelta): Duration in seconds.

        '''
        timedelta = self._interpreter.return_duration_in_seconds()
        return _converters.convert_seconds_real64_to_timedelta(timedelta)

    @ivi_synchronized
    def return_list_of_durations_in_seconds(self, number_of_elements):
        r'''return_list_of_durations_in_seconds

        Returns a list of hightime.timedelta instances.

        Args:
            number_of_elements (int): Number of elements in output.


        Returns:
            timedeltas (hightime.timedelta): Contains a list of hightime.timedelta instances.

        '''
        timedeltas = self._interpreter.return_list_of_durations_in_seconds(number_of_elements)
        return _converters.convert_seconds_real64_to_timedeltas(timedeltas)

    @ivi_synchronized
    def return_multiple_types(self, array_size):
        r'''return_multiple_types

        Returns multiple types.

        Args:
            array_size (int): Number of measurements to acquire.


        Returns:
            a_boolean (bool): Contains a boolean.

            an_int32 (int): Contains a 32-bit integer.

            an_int64 (int): Contains a 64-bit integer.

            an_int_enum (enums.Turtle): Indicates a ninja turtle

                +---+---------------+
                | 0 | Leonardo      |
                +---+---------------+
                | 1 | Donatello     |
                +---+---------------+
                | 2 | Raphael       |
                +---+---------------+
                | 3 | Mich elangelo |
                +---+---------------+

            a_float (float): The measured value.

            a_float_enum (enums.FloatEnum): A float enum.

            an_array (list of float): An array of measurement values.

                Note: The size must be at least arraySize.

            a_string (str): An IVI dance string.

        '''
        a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, an_array, a_string = self._interpreter.return_multiple_types(array_size)
        return a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, an_array, a_string

    @ivi_synchronized
    def set_custom_type(self, cs):
        r'''set_custom_type

        This method takes a custom type.

        Args:
            cs (CustomStruct): Set using custom type

        '''
        self._interpreter.set_custom_type(cs)

    @ivi_synchronized
    def set_custom_type_array(self, cs):
        r'''set_custom_type_array

        This method takes an array of custom types.

        Args:
            cs (list of CustomStruct): Set using custom type

        '''
        self._interpreter.set_custom_type_array(cs)

    @ivi_synchronized
    def string_valued_enum_input_function_with_defaults(self, a_mobile_os_name=enums.MobileOSNames.ANDROID):
        r'''string_valued_enum_input_function_with_defaults

        This method takes one parameter other than the session, which happens to be a string-valued enum and has a default value.

        Args:
            a_mobile_os_name (enums.MobileOSNames): Indicates a Mobile OS

                +---------+---------+
                | ANDROID | Android |
                +---------+---------+
                | IOS     | iOS     |
                +---------+---------+
                | NONE    | None    |
                +---------+---------+

        '''
        if type(a_mobile_os_name) is not enums.MobileOSNames:
            raise TypeError('Parameter a_mobile_os_name must be of type ' + str(enums.MobileOSNames))
        self._interpreter.string_valued_enum_input_function_with_defaults(a_mobile_os_name)

    @ivi_synchronized
    def two_input_function(self, a_number, a_string):
        r'''two_input_function

        This method takes two parameters other than the session.

        Args:
            a_number (float): Contains a number

            a_string (str): Contains a string

        '''
        self._interpreter.two_input_function(a_number, a_string)

    @ivi_synchronized
    def use64_bit_number(self, input):
        r'''use64_bit_number

        Returns a number and a string.

        Note: This method rules!

        Args:
            input (int): A big number on its way in.


        Returns:
            output (int): A big number on its way out.

        '''
        output = self._interpreter.use64_bit_number(input)
        return output

    @ivi_synchronized
    def write_waveform(self, waveform):
        r'''write_waveform

        Writes waveform to the driver

        Args:
            waveform (array.array("d")): Waveform data.

        '''
        self._interpreter.write_waveform(waveform)

    @ivi_synchronized
    def write_waveform_numpy(self, waveform):
        r'''write_waveform_numpy

        Writes waveform to the driver

        Args:
            waveform (numpy.array(dtype=numpy.float64)): Waveform data.

        '''
        import numpy

        if type(waveform) is not numpy.ndarray:
            raise TypeError('waveform must be {0}, is {1}'.format(numpy.ndarray, type(waveform)))
        if numpy.isfortran(waveform) is True:
            raise TypeError('waveform must be in C-order')
        if waveform.dtype is not numpy.dtype('float64'):
            raise TypeError('waveform must be numpy.ndarray of dtype=float64, is ' + str(waveform.dtype))
        if waveform.ndim != 1:
            raise TypeError('waveform must be numpy.ndarray of dimension=1, is ' + str(waveform.ndim))
        self._interpreter.write_waveform_numpy(waveform)

    @ivi_synchronized
    def write_waveform_numpy_complex128(self, waveform_data_array):
        r'''write_waveform_numpy_complex128

        A method that writes a waveform of numpy complex128 samples.

        Args:
            waveform_data_array (numpy.array(dtype=numpy.complex128)): Specifies the array of data to load into the waveform.

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
        self._interpreter.write_waveform_numpy_complex128(waveform_data_array)

    @ivi_synchronized
    def write_waveform_numpy_complex64(self, waveform_data_array):
        r'''write_waveform_numpy_complex64

        A method that writes a waveform of numpy complex64 samples.

        Args:
            waveform_data_array (numpy.array(dtype=numpy.complex64)): Specifies the array of data to load into the waveform.

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
        self._interpreter.write_waveform_numpy_complex64(waveform_data_array)

    @ivi_synchronized
    def write_waveform_numpy_complex_interleaved_i16(self, waveform_data_array):
        r'''write_waveform_numpy_complex_interleaved_i16

        A method that writes a waveform of numpy complex i16 samples.

        Args:
            waveform_data_array (numpy.array(dtype=numpy.int16)): Specifies the array of data to load into the waveform.

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
        self._interpreter.write_waveform_numpy_complex_interleaved_i16(waveform_data_array)

    def _close(self):
        r'''_close

        Closes the specified session and deallocates resources that it reserved.
        '''
        self._interpreter.close()

    @ivi_synchronized
    def self_test(self):
        '''self_test

        Performs a self-test
        '''
        code, msg = self._self_test()
        if code:
            raise errors.SelfTestError(code, msg)
        return None

    @ivi_synchronized
    def _self_test(self):
        r'''_self_test

        Performs a self-test.

        Returns:
            self_test_result (int): Contains the value returned from the instrument self-test. Zero indicates success.

            self_test_message (str): This parameter contains the string returned from the instrument self-test. The array must contain at least 256 elements.

        '''
        self_test_result, self_test_message = self._interpreter.self_test()
        return self_test_result, self_test_message
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/nifake/unit_tests/_matchers.py sha256=78120809c3501d31347714ce8130130dd43c5aeb07948695292e6ca4e9f6246f bytes=14043 -->
## FILE: generated/nifake/nifake/unit_tests/_matchers.py

- repository: `ni/nimi-python`
- source_path: `generated/nifake/nifake/unit_tests/_matchers.py`
- sha256: `78120809c3501d31347714ce8130130dd43c5aeb07948695292e6ca4e9f6246f`
- bytes: 14043

````python
# -*- coding: utf-8 -*-
# This file was generated
'''Matcher classes used by unit tests in order to set mock expectations.
These work well with our visatype definitions.
'''

import ctypes
import nifake._complextype as _complextype
import nifake._visatype as _visatype
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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/nifake/unit_tests/_mock_helper.py sha256=cd06f983ad422bcdf8a0cbdb1bfd7b6199d65c923b802d8bd8006b8056160f4b bytes=75831 -->
## FILE: generated/nifake/nifake/unit_tests/_mock_helper.py

- repository: `ni/nimi-python`
- source_path: `generated/nifake/nifake/unit_tests/_mock_helper.py`
- sha256: `cd06f983ad422bcdf8a0cbdb1bfd7b6199d65c923b802d8bd8006b8056160f4b`
- bytes: 75831

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
        self._defaults['AcceptListOfDurationsInSeconds'] = {}
        self._defaults['AcceptListOfDurationsInSeconds']['return'] = 0
        self._defaults['BoolArrayOutputFunction'] = {}
        self._defaults['BoolArrayOutputFunction']['return'] = 0
        self._defaults['BoolArrayOutputFunction']['anArray'] = None
        self._defaults['ConfigureABC'] = {}
        self._defaults['ConfigureABC']['return'] = 0
        self._defaults['CustomNestedStructRoundtrip'] = {}
        self._defaults['CustomNestedStructRoundtrip']['return'] = 0
        self._defaults['CustomNestedStructRoundtrip']['nestedCustomTypeOut'] = None
        self._defaults['DoubleAllTheNums'] = {}
        self._defaults['DoubleAllTheNums']['return'] = 0
        self._defaults['EnumArrayOutputFunction'] = {}
        self._defaults['EnumArrayOutputFunction']['return'] = 0
        self._defaults['EnumArrayOutputFunction']['anArray'] = None
        self._defaults['EnumInputFunctionWithDefaults'] = {}
        self._defaults['EnumInputFunctionWithDefaults']['return'] = 0
        self._defaults['ExportAttributeConfigurationBuffer'] = {}
        self._defaults['ExportAttributeConfigurationBuffer']['return'] = 0
        self._defaults['ExportAttributeConfigurationBuffer']['configuration'] = None
        self._defaults['FetchWaveform'] = {}
        self._defaults['FetchWaveform']['return'] = 0
        self._defaults['FetchWaveform']['waveformData'] = None
        self._defaults['FetchWaveform']['actualNumberOfSamples'] = None
        self._defaults['FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter'] = {}
        self._defaults['FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter']['return'] = 0
        self._defaults['FunctionWithIntflagParameter'] = {}
        self._defaults['FunctionWithIntflagParameter']['return'] = 0
        self._defaults['FunctionWithRepeatedCapabilityType'] = {}
        self._defaults['FunctionWithRepeatedCapabilityType']['return'] = 0
        self._defaults['GetABoolean'] = {}
        self._defaults['GetABoolean']['return'] = 0
        self._defaults['GetABoolean']['aBoolean'] = None
        self._defaults['GetANumber'] = {}
        self._defaults['GetANumber']['return'] = 0
        self._defaults['GetANumber']['aNumber'] = None
        self._defaults['GetAStringOfFixedMaximumSize'] = {}
        self._defaults['GetAStringOfFixedMaximumSize']['return'] = 0
        self._defaults['GetAStringOfFixedMaximumSize']['aString'] = None
        self._defaults['GetAStringUsingPythonCode'] = {}
        self._defaults['GetAStringUsingPythonCode']['return'] = 0
        self._defaults['GetAStringUsingPythonCode']['aString'] = None
        self._defaults['GetAnIviDanceCharArray'] = {}
        self._defaults['GetAnIviDanceCharArray']['return'] = 0
        self._defaults['GetAnIviDanceCharArray']['charArray'] = None
        self._defaults['GetAnIviDanceWithATwistString'] = {}
        self._defaults['GetAnIviDanceWithATwistString']['return'] = 0
        self._defaults['GetAnIviDanceWithATwistString']['actualSize'] = None
        self._defaults['GetAnIviDanceWithATwistString']['aString'] = None
        self._defaults['GetArrayForPythonCodeCustomType'] = {}
        self._defaults['GetArrayForPythonCodeCustomType']['return'] = 0
        self._defaults['GetArrayForPythonCodeCustomType']['arrayOut'] = None
        self._defaults['GetArrayForPythonCodeDouble'] = {}
        self._defaults['GetArrayForPythonCodeDouble']['return'] = 0
        self._defaults['GetArrayForPythonCodeDouble']['arrayOut'] = None
        self._defaults['GetArraySizeForPythonCode'] = {}
        self._defaults['GetArraySizeForPythonCode']['return'] = 0
        self._defaults['GetArraySizeForPythonCode']['sizeOut'] = None
        self._defaults['GetArrayUsingIviDance'] = {}
        self._defaults['GetArrayUsingIviDance']['return'] = 0
        self._defaults['GetArrayUsingIviDance']['arrayOut'] = None
        self._defaults['GetAttributeViBoolean'] = {}
        self._defaults['GetAttributeViBoolean']['return'] = 0
        self._defaults['GetAttributeViBoolean']['attributeValue'] = None
        self._defaults['GetAttributeViInt32'] = {}
        self._defaults['GetAttributeViInt32']['return'] = 0
        self._defaults['GetAttributeViInt32']['attributeValue'] = None
        self._defaults['GetAttributeViInt64'] = {}
        self._defaults['GetAttributeViInt64']['return'] = 0
        self._defaults['GetAttributeViInt64']['attributeValue'] = None
        self._defaults['GetAttributeViReal64'] = {}
        self._defaults['GetAttributeViReal64']['return'] = 0
        self._defaults['GetAttributeViReal64']['attributeValue'] = None
        self._defaults['GetAttributeViString'] = {}
        self._defaults['GetAttributeViString']['return'] = 0
        self._defaults['GetAttributeViString']['attributeValue'] = None
        self._defaults['GetCalDateAndTime'] = {}
        self._defaults['GetCalDateAndTime']['return'] = 0
        self._defaults['GetCalDateAndTime']['month'] = None
        self._defaults['GetCalDateAndTime']['day'] = None
        self._defaults['GetCalDateAndTime']['year'] = None
        self._defaults['GetCalDateAndTime']['hour'] = None
        self._defaults['GetCalDateAndTime']['minute'] = None
        self._defaults['GetCalInterval'] = {}
        self._defaults['GetCalInterval']['return'] = 0
        self._defaults['GetCalInterval']['months'] = None
        self._defaults['GetChannelNames'] = {}
        self._defaults['GetChannelNames']['return'] = 0
        self._defaults['GetChannelNames']['names'] = None
        self._defaults['GetCustomType'] = {}
        self._defaults['GetCustomType']['return'] = 0
        self._defaults['GetCustomType']['cs'] = None
        self._defaults['GetCustomTypeArray'] = {}
        self._defaults['GetCustomTypeArray']['return'] = 0
        self._defaults['GetCustomTypeArray']['cs'] = None
        self._defaults['GetCustomTypeTypedef'] = {}
        self._defaults['GetCustomTypeTypedef']['return'] = 0
        self._defaults['GetCustomTypeTypedef']['cst'] = None
        self._defaults['GetCustomTypeTypedef']['csnt'] = None
        self._defaults['GetEnumValue'] = {}
        self._defaults['GetEnumValue']['return'] = 0
        self._defaults['GetEnumValue']['aQuantity'] = None
        self._defaults['GetEnumValue']['aTurtle'] = None
        self._defaults['GetError'] = {}
        self._defaults['GetError']['return'] = 0
        self._defaults['GetError']['errorCode'] = None
        self._defaults['GetError']['description'] = None
        self._defaults['GetParameterWithOverriddenGrpcName'] = {}
        self._defaults['GetParameterWithOverriddenGrpcName']['return'] = 0
        self._defaults['GetParameterWithOverriddenGrpcName']['originalParameter'] = None
        self._defaults['ImportAttributeConfigurationBuffer'] = {}
        self._defaults['ImportAttributeConfigurationBuffer']['return'] = 0
        self._defaults['ImportAttributeConfigurationBufferEx'] = {}
        self._defaults['ImportAttributeConfigurationBufferEx']['return'] = 0
        self._defaults['InitWithOptions'] = {}
        self._defaults['InitWithOptions']['return'] = 0
        self._defaults['InitWithOptions']['vi'] = None
        self._defaults['Initiate'] = {}
        self._defaults['Initiate']['return'] = 0
        self._defaults['LockSession'] = {}
        self._defaults['LockSession']['return'] = 0
        self._defaults['LockSession']['callerHasLock'] = None
        self._defaults['MethodUsingWholeAndFractionalNumbers'] = {}
        self._defaults['MethodUsingWholeAndFractionalNumbers']['return'] = 0
        self._defaults['MethodUsingWholeAndFractionalNumbers']['wholeNumber'] = None
        self._defaults['MethodUsingWholeAndFractionalNumbers']['fractionalNumber'] = None
        self._defaults['MethodWithGrpcOnlyParam'] = {}
        self._defaults['MethodWithGrpcOnlyParam']['return'] = 0
        self._defaults['MethodWithProtoOnlyParameter'] = {}
        self._defaults['MethodWithProtoOnlyParameter']['return'] = 0
        self._defaults['MixedIviDanceAndLenMechanism'] = {}
        self._defaults['MixedIviDanceAndLenMechanism']['return'] = 0
        self._defaults['MixedIviDanceAndLenMechanism']['outputArray'] = None
        self._defaults['MultipleArrayTypes'] = {}
        self._defaults['MultipleArrayTypes']['return'] = 0
        self._defaults['MultipleArrayTypes']['outputArray'] = None
        self._defaults['MultipleArrayTypes']['outputArrayOfFixedLength'] = None
        self._defaults['MultipleArraysDifferentSize'] = {}
        self._defaults['MultipleArraysDifferentSize']['return'] = 0
        self._defaults['MultipleArraysSameSize'] = {}
        self._defaults['MultipleArraysSameSize']['return'] = 0
        self._defaults['OneInputFunction'] = {}
        self._defaults['OneInputFunction']['return'] = 0
        self._defaults['ParametersAreMultipleTypes'] = {}
        self._defaults['ParametersAreMultipleTypes']['return'] = 0
        self._defaults['PoorlyNamedSimpleFunction'] = {}
        self._defaults['PoorlyNamedSimpleFunction']['return'] = 0
        self._defaults['Read'] = {}
        self._defaults['Read']['return'] = 0
        self._defaults['Read']['reading'] = None
        self._defaults['ReadFromChannel'] = {}
        self._defaults['ReadFromChannel']['return'] = 0
        self._defaults['ReadFromChannel']['reading'] = None
        self._defaults['ReturnANumberAndAString'] = {}
        self._defaults['ReturnANumberAndAString']['return'] = 0
        self._defaults['ReturnANumberAndAString']['aNumber'] = None
        self._defaults['ReturnANumberAndAString']['aString'] = None
        self._defaults['ReturnDurationInSeconds'] = {}
        self._defaults['ReturnDurationInSeconds']['return'] = 0
        self._defaults['ReturnDurationInSeconds']['timedelta'] = None
        self._defaults['ReturnListOfDurationsInSeconds'] = {}
        self._defaults['ReturnListOfDurationsInSeconds']['return'] = 0
        self._defaults['ReturnListOfDurationsInSeconds']['timedeltas'] = None
        self._defaults['ReturnMultipleTypes'] = {}
        self._defaults['ReturnMultipleTypes']['return'] = 0
        self._defaults['ReturnMultipleTypes']['aBoolean'] = None
        self._defaults['ReturnMultipleTypes']['anInt32'] = None
        self._defaults['ReturnMultipleTypes']['anInt64'] = None
        self._defaults['ReturnMultipleTypes']['anIntEnum'] = None
        self._defaults['ReturnMultipleTypes']['aFloat'] = None
        self._defaults['ReturnMultipleTypes']['aFloatEnum'] = None
        self._defaults['ReturnMultipleTypes']['anArray'] = None
        self._defaults['ReturnMultipleTypes']['aString'] = None
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
        self._defaults['SetCustomType'] = {}
        self._defaults['SetCustomType']['return'] = 0
        self._defaults['SetCustomTypeArray'] = {}
        self._defaults['SetCustomTypeArray']['return'] = 0
        self._defaults['SetRuntimeEnvironment'] = {}
        self._defaults['SetRuntimeEnvironment']['return'] = 0
        self._defaults['StringValuedEnumInputFunctionWithDefaults'] = {}
        self._defaults['StringValuedEnumInputFunctionWithDefaults']['return'] = 0
        self._defaults['TwoInputFunction'] = {}
        self._defaults['TwoInputFunction']['return'] = 0
        self._defaults['UnlockSession'] = {}
        self._defaults['UnlockSession']['return'] = 0
        self._defaults['UnlockSession']['callerHasLock'] = None
        self._defaults['Use64BitNumber'] = {}
        self._defaults['Use64BitNumber']['return'] = 0
        self._defaults['Use64BitNumber']['output'] = None
        self._defaults['WriteWaveform'] = {}
        self._defaults['WriteWaveform']['return'] = 0
        self._defaults['WriteWaveformNumpyComplex128'] = {}
        self._defaults['WriteWaveformNumpyComplex128']['return'] = 0
        self._defaults['WriteWaveformNumpyComplex64'] = {}
        self._defaults['WriteWaveformNumpyComplex64']['return'] = 0
        self._defaults['WriteWaveformNumpyComplexInterleavedI16'] = {}
        self._defaults['WriteWaveformNumpyComplexInterleavedI16']['return'] = 0
        self._defaults['close'] = {}
        self._defaults['close']['return'] = 0
        self._defaults['error_message'] = {}
        self._defaults['error_message']['return'] = 0
        self._defaults['error_message']['errorMessage'] = None
        self._defaults['self_test'] = {}
        self._defaults['self_test']['return'] = 0
        self._defaults['self_test']['selfTestResult'] = None
        self._defaults['self_test']['selfTestMessage'] = None

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

    def niFake_Abort(self, vi):  # noqa: N802
        if self._defaults['Abort']['return'] != 0:
            return self._defaults['Abort']['return']
        return self._defaults['Abort']['return']

    def niFake_AcceptListOfDurationsInSeconds(self, vi, count, delays):  # noqa: N802
        if self._defaults['AcceptListOfDurationsInSeconds']['return'] != 0:
            return self._defaults['AcceptListOfDurationsInSeconds']['return']
        return self._defaults['AcceptListOfDurationsInSeconds']['return']

    def niFake_BoolArrayOutputFunction(self, vi, number_of_elements, an_array):  # noqa: N802
        if self._defaults['BoolArrayOutputFunction']['return'] != 0:
            return self._defaults['BoolArrayOutputFunction']['return']
        # an_array
        if self._defaults['BoolArrayOutputFunction']['anArray'] is None:
            raise MockFunctionCallError("niFake_BoolArrayOutputFunction", param='anArray')
        test_value = self._defaults['BoolArrayOutputFunction']['anArray']
        try:
            an_array_ref = an_array.contents
        except AttributeError:
            an_array_ref = an_array
        assert len(an_array_ref) >= len(test_value)
        for i in range(len(test_value)):
            an_array_ref[i] = test_value[i]
        return self._defaults['BoolArrayOutputFunction']['return']

    def niFake_ConfigureABC(self, vi):  # noqa: N802
        if self._defaults['ConfigureABC']['return'] != 0:
            return self._defaults['ConfigureABC']['return']
        return self._defaults['ConfigureABC']['return']

    def niFake_CustomNestedStructRoundtrip(self, nested_custom_type_in, nested_custom_type_out):  # noqa: N802
        if self._defaults['CustomNestedStructRoundtrip']['return'] != 0:
            return self._defaults['CustomNestedStructRoundtrip']['return']
        # nested_custom_type_out
        if self._defaults['CustomNestedStructRoundtrip']['nestedCustomTypeOut'] is None:
            raise MockFunctionCallError("niFake_CustomNestedStructRoundtrip", param='nestedCustomTypeOut')
        for field in self._defaults['CustomNestedStructRoundtrip']['nested_custom_type_out']._fields_:
            field_name = field[0]
            setattr(nested_custom_type_out.contents, field_name, getattr(self._defaults['CustomNestedStructRoundtrip']['nested_custom_type_out'], field_name))
        return self._defaults['CustomNestedStructRoundtrip']['return']

    def niFake_DoubleAllTheNums(self, vi, number_count, numbers):  # noqa: N802
        if self._defaults['DoubleAllTheNums']['return'] != 0:
            return self._defaults['DoubleAllTheNums']['return']
        return self._defaults['DoubleAllTheNums']['return']

    def niFake_EnumArrayOutputFunction(self, vi, number_of_elements, an_array):  # noqa: N802
        if self._defaults['EnumArrayOutputFunction']['return'] != 0:
            return self._defaults['EnumArrayOutputFunction']['return']
        # an_array
        if self._defaults['EnumArrayOutputFunction']['anArray'] is None:
            raise MockFunctionCallError("niFake_EnumArrayOutputFunction", param='anArray')
        test_value = self._defaults['EnumArrayOutputFunction']['anArray']
        try:
            an_array_ref = an_array.contents
        except AttributeError:
            an_array_ref = an_array
        assert len(an_array_ref) >= len(test_value)
        for i in range(len(test_value)):
            an_array_ref[i] = test_value[i]
        return self._defaults['EnumArrayOutputFunction']['return']

    def niFake_EnumInputFunctionWithDefaults(self, vi, a_turtle):  # noqa: N802
        if self._defaults['EnumInputFunctionWithDefaults']['return'] != 0:
            return self._defaults['EnumInputFunctionWithDefaults']['return']
        return self._defaults['EnumInputFunctionWithDefaults']['return']

    def niFake_ExportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration):  # noqa: N802
        if self._defaults['ExportAttributeConfigurationBuffer']['return'] != 0:
            return self._defaults['ExportAttributeConfigurationBuffer']['return']
        # configuration
        if self._defaults['ExportAttributeConfigurationBuffer']['configuration'] is None:
            raise MockFunctionCallError("niFake_ExportAttributeConfigurationBuffer", param='configuration')
        if size_in_bytes.value == 0:
            return len(self._defaults['ExportAttributeConfigurationBuffer']['configuration'])
        try:
            configuration_ref = configuration.contents
        except AttributeError:
            configuration_ref = configuration
        for i in range(len(self._defaults['ExportAttributeConfigurationBuffer']['configuration'])):
            configuration_ref[i] = self._defaults['ExportAttributeConfigurationBuffer']['configuration'][i]
        return self._defaults['ExportAttributeConfigurationBuffer']['return']

    def niFake_FetchWaveform(self, vi, number_of_samples, waveform_data, actual_number_of_samples):  # noqa: N802
        if self._defaults['FetchWaveform']['return'] != 0:
            return self._defaults['FetchWaveform']['return']
        # waveform_data
        if self._defaults['FetchWaveform']['waveformData'] is None:
            raise MockFunctionCallError("niFake_FetchWaveform", param='waveformData')
        test_value = self._defaults['FetchWaveform']['waveformData']
        try:
            waveform_data_ref = waveform_data.contents
        except AttributeError:
            waveform_data_ref = waveform_data
        assert len(waveform_data_ref) >= len(test_value)
        for i in range(len(test_value)):
            waveform_data_ref[i] = test_value[i]
        # actual_number_of_samples
        if self._defaults['FetchWaveform']['actualNumberOfSamples'] is None:
            raise MockFunctionCallError("niFake_FetchWaveform", param='actualNumberOfSamples')
        if actual_number_of_samples is not None:
            actual_number_of_samples.contents.value = self._defaults['FetchWaveform']['actualNumberOfSamples']
        return self._defaults['FetchWaveform']['return']

    def niFake_FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter(self, vi, multidimensional_array):  # noqa: N802
        if self._defaults['FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter']['return'] != 0:
            return self._defaults['FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter']['return']
        return self._defaults['FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter']['return']

    def niFake_FunctionWithIntflagParameter(self, vi, flag):  # noqa: N802
        if self._defaults['FunctionWithIntflagParameter']['return'] != 0:
            return self._defaults['FunctionWithIntflagParameter']['return']
        return self._defaults['FunctionWithIntflagParameter']['return']

    def niFake_FunctionWithRepeatedCapabilityType(self, vi, site_list):  # noqa: N802
        if self._defaults['FunctionWithRepeatedCapabilityType']['return'] != 0:
            return self._defaults['FunctionWithRepeatedCapabilityType']['return']
        return self._defaults['FunctionWithRepeatedCapabilityType']['return']

    def niFake_GetABoolean(self, vi, a_boolean):  # noqa: N802
        if self._defaults['GetABoolean']['return'] != 0:
            return self._defaults['GetABoolean']['return']
        # a_boolean
        if self._defaults['GetABoolean']['aBoolean'] is None:
            raise MockFunctionCallError("niFake_GetABoolean", param='aBoolean')
        if a_boolean is not None:
            a_boolean.contents.value = self._defaults['GetABoolean']['aBoolean']
        return self._defaults['GetABoolean']['return']

    def niFake_GetANumber(self, vi, a_number):  # noqa: N802
        if self._defaults['GetANumber']['return'] != 0:
            return self._defaults['GetANumber']['return']
        # a_number
        if self._defaults['GetANumber']['aNumber'] is None:
            raise MockFunctionCallError("niFake_GetANumber", param='aNumber')
        if a_number is not None:
            a_number.contents.value = self._defaults['GetANumber']['aNumber']
        return self._defaults['GetANumber']['return']

    def niFake_GetAStringOfFixedMaximumSize(self, vi, a_string):  # noqa: N802
        if self._defaults['GetAStringOfFixedMaximumSize']['return'] != 0:
            return self._defaults['GetAStringOfFixedMaximumSize']['return']
        # a_string
        if self._defaults['GetAStringOfFixedMaximumSize']['aString'] is None:
            raise MockFunctionCallError("niFake_GetAStringOfFixedMaximumSize", param='aString')
        test_value = self._defaults['GetAStringOfFixedMaximumSize']['aString']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(a_string) >= len(test_value)
        for i in range(len(test_value)):
            a_string[i] = test_value[i]
        return self._defaults['GetAStringOfFixedMaximumSize']['return']

    def niFake_GetAStringUsingPythonCode(self, vi, a_number, a_string):  # noqa: N802
        if self._defaults['GetAStringUsingPythonCode']['return'] != 0:
            return self._defaults['GetAStringUsingPythonCode']['return']
        # a_string
        if self._defaults['GetAStringUsingPythonCode']['aString'] is None:
            raise MockFunctionCallError("niFake_GetAStringUsingPythonCode", param='aString')
        test_value = self._defaults['GetAStringUsingPythonCode']['aString']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(a_string) >= len(test_value)
        for i in range(len(test_value)):
            a_string[i] = test_value[i]
        return self._defaults['GetAStringUsingPythonCode']['return']

    def niFake_GetAnIviDanceCharArray(self, vi, buffer_size, char_array):  # noqa: N802
        if self._defaults['GetAnIviDanceCharArray']['return'] != 0:
            return self._defaults['GetAnIviDanceCharArray']['return']
        # char_array
        if self._defaults['GetAnIviDanceCharArray']['charArray'] is None:
            raise MockFunctionCallError("niFake_GetAnIviDanceCharArray", param='charArray')
        if buffer_size.value == 0:
            return len(self._defaults['GetAnIviDanceCharArray']['charArray'])
        char_array.value = self._defaults['GetAnIviDanceCharArray']['charArray'].encode('ascii')
        return self._defaults['GetAnIviDanceCharArray']['return']

    def niFake_GetAnIviDanceWithATwistString(self, vi, buffer_size, a_string, actual_size):  # noqa: N802
        if self._defaults['GetAnIviDanceWithATwistString']['return'] != 0:
            return self._defaults['GetAnIviDanceWithATwistString']['return']
        # actual_size
        if self._defaults['GetAnIviDanceWithATwistString']['actualSize'] is None:
            raise MockFunctionCallError("niFake_GetAnIviDanceWithATwistString", param='actualSize')
        if actual_size is not None:
            actual_size.contents.value = self._defaults['GetAnIviDanceWithATwistString']['actualSize']
        # a_string
        if self._defaults['GetAnIviDanceWithATwistString']['aString'] is None:
            raise MockFunctionCallError("niFake_GetAnIviDanceWithATwistString", param='aString')
        if buffer_size.value == 0:
            return len(self._defaults['GetAnIviDanceWithATwistString']['aString'])
        a_string.value = self._defaults['GetAnIviDanceWithATwistString']['aString'].encode('ascii')
        return self._defaults['GetAnIviDanceWithATwistString']['return']

    def niFake_GetArrayForPythonCodeCustomType(self, vi, number_of_elements, array_out):  # noqa: N802
        if self._defaults['GetArrayForPythonCodeCustomType']['return'] != 0:
            return self._defaults['GetArrayForPythonCodeCustomType']['return']
        # array_out
        if self._defaults['GetArrayForPythonCodeCustomType']['arrayOut'] is None:
            raise MockFunctionCallError("niFake_GetArrayForPythonCodeCustomType", param='arrayOut')
        test_value = self._defaults['GetArrayForPythonCodeCustomType']['arrayOut']
        try:
            array_out_ref = array_out.contents
        except AttributeError:
            array_out_ref = array_out
        assert len(array_out_ref) >= len(test_value)
        for i in range(len(test_value)):
            array_out_ref[i] = test_value[i]
        return self._defaults['GetArrayForPythonCodeCustomType']['return']

    def niFake_GetArrayForPythonCodeDouble(self, vi, number_of_elements, array_out):  # noqa: N802
        if self._defaults['GetArrayForPythonCodeDouble']['return'] != 0:
            return self._defaults['GetArrayForPythonCodeDouble']['return']
        # array_out
        if self._defaults['GetArrayForPythonCodeDouble']['arrayOut'] is None:
            raise MockFunctionCallError("niFake_GetArrayForPythonCodeDouble", param='arrayOut')
        test_value = self._defaults['GetArrayForPythonCodeDouble']['arrayOut']
        try:
            array_out_ref = array_out.contents
        except AttributeError:
            array_out_ref = array_out
        assert len(array_out_ref) >= len(test_value)
        for i in range(len(test_value)):
            array_out_ref[i] = test_value[i]
        return self._defaults['GetArrayForPythonCodeDouble']['return']

    def niFake_GetArraySizeForPythonCode(self, vi, size_out):  # noqa: N802
        if self._defaults['GetArraySizeForPythonCode']['return'] != 0:
            return self._defaults['GetArraySizeForPythonCode']['return']
        # size_out
        if self._defaults['GetArraySizeForPythonCode']['sizeOut'] is None:
            raise MockFunctionCallError("niFake_GetArraySizeForPythonCode", param='sizeOut')
        if size_out is not None:
            size_out.contents.value = self._defaults['GetArraySizeForPythonCode']['sizeOut']
        return self._defaults['GetArraySizeForPythonCode']['return']

    def niFake_GetArrayUsingIviDance(self, vi, array_size, array_out):  # noqa: N802
        if self._defaults['GetArrayUsingIviDance']['return'] != 0:
            return self._defaults['GetArrayUsingIviDance']['return']
        # array_out
        if self._defaults['GetArrayUsingIviDance']['arrayOut'] is None:
            raise MockFunctionCallError("niFake_GetArrayUsingIviDance", param='arrayOut')
        if array_size.value == 0:
            return len(self._defaults['GetArrayUsingIviDance']['arrayOut'])
        try:
            array_out_ref = array_out.contents
        except AttributeError:
            array_out_ref = array_out
        for i in range(len(self._defaults['GetArrayUsingIviDance']['arrayOut'])):
            array_out_ref[i] = self._defaults['GetArrayUsingIviDance']['arrayOut'][i]
        return self._defaults['GetArrayUsingIviDance']['return']

    def niFake_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViBoolean']['return'] != 0:
            return self._defaults['GetAttributeViBoolean']['return']
        # attribute_value
        if self._defaults['GetAttributeViBoolean']['attributeValue'] is None:
            raise MockFunctionCallError("niFake_GetAttributeViBoolean", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViBoolean']['attributeValue']
        return self._defaults['GetAttributeViBoolean']['return']

    def niFake_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViInt32']['return'] != 0:
            return self._defaults['GetAttributeViInt32']['return']
        # attribute_value
        if self._defaults['GetAttributeViInt32']['attributeValue'] is None:
            raise MockFunctionCallError("niFake_GetAttributeViInt32", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViInt32']['attributeValue']
        return self._defaults['GetAttributeViInt32']['return']

    def niFake_GetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViInt64']['return'] != 0:
            return self._defaults['GetAttributeViInt64']['return']
        # attribute_value
        if self._defaults['GetAttributeViInt64']['attributeValue'] is None:
            raise MockFunctionCallError("niFake_GetAttributeViInt64", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViInt64']['attributeValue']
        return self._defaults['GetAttributeViInt64']['return']

    def niFake_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViReal64']['return'] != 0:
            return self._defaults['GetAttributeViReal64']['return']
        # attribute_value
        if self._defaults['GetAttributeViReal64']['attributeValue'] is None:
            raise MockFunctionCallError("niFake_GetAttributeViReal64", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViReal64']['attributeValue']
        return self._defaults['GetAttributeViReal64']['return']

    def niFake_GetAttributeViString(self, vi, channel_name, attribute_id, buffer_size, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViString']['return'] != 0:
            return self._defaults['GetAttributeViString']['return']
        # attribute_value
        if self._defaults['GetAttributeViString']['attributeValue'] is None:
            raise MockFunctionCallError("niFake_GetAttributeViString", param='attributeValue')
        if buffer_size.value == 0:
            return len(self._defaults['GetAttributeViString']['attributeValue'])
        attribute_value.value = self._defaults['GetAttributeViString']['attributeValue'].encode('ascii')
        return self._defaults['GetAttributeViString']['return']

    def niFake_GetCalDateAndTime(self, vi, cal_type, month, day, year, hour, minute):  # noqa: N802
        if self._defaults['GetCalDateAndTime']['return'] != 0:
            return self._defaults['GetCalDateAndTime']['return']
        # month
        if self._defaults['GetCalDateAndTime']['month'] is None:
            raise MockFunctionCallError("niFake_GetCalDateAndTime", param='month')
        if month is not None:
            month.contents.value = self._defaults['GetCalDateAndTime']['month']
        # day
        if self._defaults['GetCalDateAndTime']['day'] is None:
            raise MockFunctionCallError("niFake_GetCalDateAndTime", param='day')
        if day is not None:
            day.contents.value = self._defaults['GetCalDateAndTime']['day']
        # year
        if self._defaults['GetCalDateAndTime']['year'] is None:
            raise MockFunctionCallError("niFake_GetCalDateAndTime", param='year')
        if year is not None:
            year.contents.value = self._defaults['GetCalDateAndTime']['year']
        # hour
        if self._defaults['GetCalDateAndTime']['hour'] is None:
            raise MockFunctionCallError("niFake_GetCalDateAndTime", param='hour')
        if hour is not None:
            hour.contents.value = self._defaults['GetCalDateAndTime']['hour']
        # minute
        if self._defaults['GetCalDateAndTime']['minute'] is None:
            raise MockFunctionCallError("niFake_GetCalDateAndTime", param='minute')
        if minute is not None:
            minute.contents.value = self._defaults['GetCalDateAndTime']['minute']
        return self._defaults['GetCalDateAndTime']['return']

    def niFake_GetCalInterval(self, vi, months):  # noqa: N802
        if self._defaults['GetCalInterval']['return'] != 0:
            return self._defaults['GetCalInterval']['return']
        # months
        if self._defaults['GetCalInterval']['months'] is None:
            raise MockFunctionCallError("niFake_GetCalInterval", param='months')
        if months is not None:
            months.contents.value = self._defaults['GetCalInterval']['months']
        return self._defaults['GetCalInterval']['return']

    def niFake_GetChannelNames(self, vi, indices, name_size, names):  # noqa: N802
        if self._defaults['GetChannelNames']['return'] != 0:
            return self._defaults['GetChannelNames']['return']
        # names
        if self._defaults['GetChannelNames']['names'] is None:
            raise MockFunctionCallError("niFake_GetChannelNames", param='names')
        if name_size.value == 0:
            return len(self._defaults['GetChannelNames']['names'])
        names.value = self._defaults['GetChannelNames']['names'].encode('ascii')
        return self._defaults['GetChannelNames']['return']

    def niFake_GetCustomType(self, vi, cs):  # noqa: N802
        if self._defaults['GetCustomType']['return'] != 0:
            return self._defaults['GetCustomType']['return']
        # cs
        if self._defaults['GetCustomType']['cs'] is None:
            raise MockFunctionCallError("niFake_GetCustomType", param='cs')
        for field in self._defaults['GetCustomType']['cs']._fields_:
            field_name = field[0]
            setattr(cs.contents, field_name, getattr(self._defaults['GetCustomType']['cs'], field_name))
        return self._defaults['GetCustomType']['return']

    def niFake_GetCustomTypeArray(self, vi, number_of_elements, cs):  # noqa: N802
        if self._defaults['GetCustomTypeArray']['return'] != 0:
            return self._defaults['GetCustomTypeArray']['return']
        # cs
        if self._defaults['GetCustomTypeArray']['cs'] is None:
            raise MockFunctionCallError("niFake_GetCustomTypeArray", param='cs')
        test_value = self._defaults['GetCustomTypeArray']['cs']
        try:
            cs_ref = cs.contents
        except AttributeError:
            cs_ref = cs
        assert len(cs_ref) >= len(test_value)
        for i in range(len(test_value)):
            cs_ref[i] = test_value[i]
        return self._defaults['GetCustomTypeArray']['return']

    def niFake_GetCustomTypeTypedef(self, vi, cst, csnt):  # noqa: N802
        if self._defaults['GetCustomTypeTypedef']['return'] != 0:
            return self._defaults['GetCustomTypeTypedef']['return']
        # cst
        if self._defaults['GetCustomTypeTypedef']['cst'] is None:
            raise MockFunctionCallError("niFake_GetCustomTypeTypedef", param='cst')
        for field in self._defaults['GetCustomTypeTypedef']['cst']._fields_:
            field_name = field[0]
            setattr(cst.contents, field_name, getattr(self._defaults['GetCustomTypeTypedef']['cst'], field_name))
        # csnt
        if self._defaults['GetCustomTypeTypedef']['csnt'] is None:
            raise MockFunctionCallError("niFake_GetCustomTypeTypedef", param='csnt')
        for field in self._defaults['GetCustomTypeTypedef']['csnt']._fields_:
            field_name = field[0]
            setattr(csnt.contents, field_name, getattr(self._defaults['GetCustomTypeTypedef']['csnt'], field_name))
        return self._defaults['GetCustomTypeTypedef']['return']

    def niFake_GetEnumValue(self, vi, a_quantity, a_turtle):  # noqa: N802
        if self._defaults['GetEnumValue']['return'] != 0:
            return self._defaults['GetEnumValue']['return']
        # a_quantity
        if self._defaults['GetEnumValue']['aQuantity'] is None:
            raise MockFunctionCallError("niFake_GetEnumValue", param='aQuantity')
        if a_quantity is not None:
            a_quantity.contents.value = self._defaults['GetEnumValue']['aQuantity']
        # a_turtle
        if self._defaults['GetEnumValue']['aTurtle'] is None:
            raise MockFunctionCallError("niFake_GetEnumValue", param='aTurtle')
        if a_turtle is not None:
            a_turtle.contents.value = self._defaults['GetEnumValue']['aTurtle']
        return self._defaults['GetEnumValue']['return']

    def niFake_GetError(self, vi, error_code, buffer_size, description):  # noqa: N802
        if self._defaults['GetError']['return'] != 0:
            return self._defaults['GetError']['return']
        # error_code
        if self._defaults['GetError']['errorCode'] is None:
            raise MockFunctionCallError("niFake_GetError", param='errorCode')
        if error_code is not None:
            error_code.contents.value = self._defaults['GetError']['errorCode']
        # description
        if self._defaults['GetError']['description'] is None:
            raise MockFunctionCallError("niFake_GetError", param='description')
        if buffer_size.value == 0:
            return len(self._defaults['GetError']['description'])
        description.value = self._defaults['GetError']['description'].encode('ascii')
        return self._defaults['GetError']['return']

    def niFake_GetParameterWithOverriddenGrpcName(self, vi, original_parameter, enum_parameter):  # noqa: N802
        if self._defaults['GetParameterWithOverriddenGrpcName']['return'] != 0:
            return self._defaults['GetParameterWithOverriddenGrpcName']['return']
        # original_parameter
        if self._defaults['GetParameterWithOverriddenGrpcName']['originalParameter'] is None:
            raise MockFunctionCallError("niFake_GetParameterWithOverriddenGrpcName", param='originalParameter')
        if original_parameter is not None:
            original_parameter.contents.value = self._defaults['GetParameterWithOverriddenGrpcName']['originalParameter']
        return self._defaults['GetParameterWithOverriddenGrpcName']['return']

    def niFake_ImportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration):  # noqa: N802
        if self._defaults['ImportAttributeConfigurationBuffer']['return'] != 0:
            return self._defaults['ImportAttributeConfigurationBuffer']['return']
        return self._defaults['ImportAttributeConfigurationBuffer']['return']

    def niFake_ImportAttributeConfigurationBufferEx(self, vi, size, configuration):  # noqa: N802
        if self._defaults['ImportAttributeConfigurationBufferEx']['return'] != 0:
            return self._defaults['ImportAttributeConfigurationBufferEx']['return']
        return self._defaults['ImportAttributeConfigurationBufferEx']['return']

    def niFake_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi):  # noqa: N802
        if self._defaults['InitWithOptions']['return'] != 0:
            return self._defaults['InitWithOptions']['return']
        # vi
        if self._defaults['InitWithOptions']['vi'] is None:
            raise MockFunctionCallError("niFake_InitWithOptions", param='vi')
        if vi is not None:
            vi.contents.value = self._defaults['InitWithOptions']['vi']
        return self._defaults['InitWithOptions']['return']

    def niFake_Initiate(self, vi):  # noqa: N802
        if self._defaults['Initiate']['return'] != 0:
            return self._defaults['Initiate']['return']
        return self._defaults['Initiate']['return']

    def niFake_LockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['LockSession']['return'] != 0:
            return self._defaults['LockSession']['return']
        # caller_has_lock
        if self._defaults['LockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niFake_LockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['LockSession']['callerHasLock']
        return self._defaults['LockSession']['return']

    def niFake_MethodUsingWholeAndFractionalNumbers(self, whole_number, fractional_number):  # noqa: N802
        if self._defaults['MethodUsingWholeAndFractionalNumbers']['return'] != 0:
            return self._defaults['MethodUsingWholeAndFractionalNumbers']['return']
        # whole_number
        if self._defaults['MethodUsingWholeAndFractionalNumbers']['wholeNumber'] is None:
            raise MockFunctionCallError("niFake_MethodUsingWholeAndFractionalNumbers", param='wholeNumber')
        if whole_number is not None:
            whole_number.contents.value = self._defaults['MethodUsingWholeAndFractionalNumbers']['wholeNumber']
        # fractional_number
        if self._defaults['MethodUsingWholeAndFractionalNumbers']['fractionalNumber'] is None:
            raise MockFunctionCallError("niFake_MethodUsingWholeAndFractionalNumbers", param='fractionalNumber')
        if fractional_number is not None:
            fractional_number.contents.value = self._defaults['MethodUsingWholeAndFractionalNumbers']['fractionalNumber']
        return self._defaults['MethodUsingWholeAndFractionalNumbers']['return']

    def niFake_MethodWithGrpcOnlyParam(self, simple_param):  # noqa: N802
        if self._defaults['MethodWithGrpcOnlyParam']['return'] != 0:
            return self._defaults['MethodWithGrpcOnlyParam']['return']
        return self._defaults['MethodWithGrpcOnlyParam']['return']

    def niFake_MethodWithProtoOnlyParameter(self, attribute_value):  # noqa: N802
        if self._defaults['MethodWithProtoOnlyParameter']['return'] != 0:
            return self._defaults['MethodWithProtoOnlyParameter']['return']
        return self._defaults['MethodWithProtoOnlyParameter']['return']

    def niFake_MixedIviDanceAndLenMechanism(self, vi, input_values, input_values_size, output_size, output_array):  # noqa: N802
        if self._defaults['MixedIviDanceAndLenMechanism']['return'] != 0:
            return self._defaults['MixedIviDanceAndLenMechanism']['return']
        # output_array
        if self._defaults['MixedIviDanceAndLenMechanism']['outputArray'] is None:
            raise MockFunctionCallError("niFake_MixedIviDanceAndLenMechanism", param='outputArray')
        if output_size.value == 0:
            return len(self._defaults['MixedIviDanceAndLenMechanism']['outputArray'])
        try:
            output_array_ref = output_array.contents
        except AttributeError:
            output_array_ref = output_array
        for i in range(len(self._defaults['MixedIviDanceAndLenMechanism']['outputArray'])):
            output_array_ref[i] = self._defaults['MixedIviDanceAndLenMechanism']['outputArray'][i]
        return self._defaults['MixedIviDanceAndLenMechanism']['return']

    def niFake_MultipleArrayTypes(self, vi, output_array_size, output_array, output_array_of_fixed_length, input_array_sizes, input_array_of_floats, input_array_of_integers):  # noqa: N802
        if self._defaults['MultipleArrayTypes']['return'] != 0:
            return self._defaults['MultipleArrayTypes']['return']
        # output_array
        if self._defaults['MultipleArrayTypes']['outputArray'] is None:
            raise MockFunctionCallError("niFake_MultipleArrayTypes", param='outputArray')
        test_value = self._defaults['MultipleArrayTypes']['outputArray']
        try:
            output_array_ref = output_array.contents
        except AttributeError:
            output_array_ref = output_array
        assert len(output_array_ref) >= len(test_value)
        for i in range(len(test_value)):
            output_array_ref[i] = test_value[i]
        # output_array_of_fixed_length
        if self._defaults['MultipleArrayTypes']['outputArrayOfFixedLength'] is None:
            raise MockFunctionCallError("niFake_MultipleArrayTypes", param='outputArrayOfFixedLength')
        test_value = self._defaults['MultipleArrayTypes']['outputArrayOfFixedLength']
        try:
            output_array_of_fixed_length_ref = output_array_of_fixed_length.contents
        except AttributeError:
            output_array_of_fixed_length_ref = output_array_of_fixed_length
        assert len(output_array_of_fixed_length_ref) >= len(test_value)
        for i in range(len(test_value)):
            output_array_of_fixed_length_ref[i] = test_value[i]
        return self._defaults['MultipleArrayTypes']['return']

    def niFake_MultipleArraysDifferentSize(self, vi, values_array, values_array_size, data_array, data_array_size):  # noqa: N802
        if self._defaults['MultipleArraysDifferentSize']['return'] != 0:
            return self._defaults['MultipleArraysDifferentSize']['return']
        return self._defaults['MultipleArraysDifferentSize']['return']

    def niFake_MultipleArraysSameSize(self, vi, values1, values2, values3, values4, size):  # noqa: N802
        if self._defaults['MultipleArraysSameSize']['return'] != 0:
            return self._defaults['MultipleArraysSameSize']['return']
        return self._defaults['MultipleArraysSameSize']['return']

    def niFake_OneInputFunction(self, vi, a_number):  # noqa: N802
        if self._defaults['OneInputFunction']['return'] != 0:
            return self._defaults['OneInputFunction']['return']
        return self._defaults['OneInputFunction']['return']

    def niFake_ParametersAreMultipleTypes(self, vi, a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, a_string):  # noqa: N802
        if self._defaults['ParametersAreMultipleTypes']['return'] != 0:
            return self._defaults['ParametersAreMultipleTypes']['return']
        return self._defaults['ParametersAreMultipleTypes']['return']

    def niFake_PoorlyNamedSimpleFunction(self, vi):  # noqa: N802
        if self._defaults['PoorlyNamedSimpleFunction']['return'] != 0:
            return self._defaults['PoorlyNamedSimpleFunction']['return']
        return self._defaults['PoorlyNamedSimpleFunction']['return']

    def niFake_Read(self, vi, maximum_time, reading):  # noqa: N802
        if self._defaults['Read']['return'] != 0:
            return self._defaults['Read']['return']
        # reading
        if self._defaults['Read']['reading'] is None:
            raise MockFunctionCallError("niFake_Read", param='reading')
        if reading is not None:
            reading.contents.value = self._defaults['Read']['reading']
        return self._defaults['Read']['return']

    def niFake_ReadFromChannel(self, vi, channel_name, maximum_time, reading):  # noqa: N802
        if self._defaults['ReadFromChannel']['return'] != 0:
            return self._defaults['ReadFromChannel']['return']
        # reading
        if self._defaults['ReadFromChannel']['reading'] is None:
            raise MockFunctionCallError("niFake_ReadFromChannel", param='reading')
        if reading is not None:
            reading.contents.value = self._defaults['ReadFromChannel']['reading']
        return self._defaults['ReadFromChannel']['return']

    def niFake_ReturnANumberAndAString(self, vi, a_number, a_string):  # noqa: N802
        if self._defaults['ReturnANumberAndAString']['return'] != 0:
            return self._defaults['ReturnANumberAndAString']['return']
        # a_number
        if self._defaults['ReturnANumberAndAString']['aNumber'] is None:
            raise MockFunctionCallError("niFake_ReturnANumberAndAString", param='aNumber')
        if a_number is not None:
            a_number.contents.value = self._defaults['ReturnANumberAndAString']['aNumber']
        # a_string
        if self._defaults['ReturnANumberAndAString']['aString'] is None:
            raise MockFunctionCallError("niFake_ReturnANumberAndAString", param='aString')
        test_value = self._defaults['ReturnANumberAndAString']['aString']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(a_string) >= len(test_value)
        for i in range(len(test_value)):
            a_string[i] = test_value[i]
        return self._defaults['ReturnANumberAndAString']['return']

    def niFake_ReturnDurationInSeconds(self, vi, timedelta):  # noqa: N802
        if self._defaults['ReturnDurationInSeconds']['return'] != 0:
            return self._defaults['ReturnDurationInSeconds']['return']
        # timedelta
        if self._defaults['ReturnDurationInSeconds']['timedelta'] is None:
            raise MockFunctionCallError("niFake_ReturnDurationInSeconds", param='timedelta')
        if timedelta is not None:
            timedelta.contents.value = self._defaults['ReturnDurationInSeconds']['timedelta']
        return self._defaults['ReturnDurationInSeconds']['return']

    def niFake_ReturnListOfDurationsInSeconds(self, vi, number_of_elements, timedeltas):  # noqa: N802
        if self._defaults['ReturnListOfDurationsInSeconds']['return'] != 0:
            return self._defaults['ReturnListOfDurationsInSeconds']['return']
        # timedeltas
        if self._defaults['ReturnListOfDurationsInSeconds']['timedeltas'] is None:
            raise MockFunctionCallError("niFake_ReturnListOfDurationsInSeconds", param='timedeltas')
        test_value = self._defaults['ReturnListOfDurationsInSeconds']['timedeltas']
        try:
            timedeltas_ref = timedeltas.contents
        except AttributeError:
            timedeltas_ref = timedeltas
        assert len(timedeltas_ref) >= len(test_value)
        for i in range(len(test_value)):
            timedeltas_ref[i] = test_value[i]
        return self._defaults['ReturnListOfDurationsInSeconds']['return']

    def niFake_ReturnMultipleTypes(self, vi, a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, array_size, an_array, string_size, a_string):  # noqa: N802
        if self._defaults['ReturnMultipleTypes']['return'] != 0:
            return self._defaults['ReturnMultipleTypes']['return']
        # a_boolean
        if self._defaults['ReturnMultipleTypes']['aBoolean'] is None:
            raise MockFunctionCallError("niFake_ReturnMultipleTypes", param='aBoolean')
        if a_boolean is not None:
            a_boolean.contents.value = self._defaults['ReturnMultipleTypes']['aBoolean']
        # an_int32
        if self._defaults['ReturnMultipleTypes']['anInt32'] is None:
            raise MockFunctionCallError("niFake_ReturnMultipleTypes", param='anInt32')
        if an_int32 is not None:
            an_int32.contents.value = self._defaults['ReturnMultipleTypes']['anInt32']
        # an_int64
        if self._defaults['ReturnMultipleTypes']['anInt64'] is None:
            raise MockFunctionCallError("niFake_ReturnMultipleTypes", param='anInt64')
        if an_int64 is not None:
            an_int64.contents.value = self._defaults['ReturnMultipleTypes']['anInt64']
        # an_int_enum
        if self._defaults['ReturnMultipleTypes']['anIntEnum'] is None:
            raise MockFunctionCallError("niFake_ReturnMultipleTypes", param='anIntEnum')
        if an_int_enum is not None:
            an_int_enum.contents.value = self._defaults['ReturnMultipleTypes']['anIntEnum']
        # a_float
        if self._defaults['ReturnMultipleTypes']['aFloat'] is None:
            raise MockFunctionCallError("niFake_ReturnMultipleTypes", param='aFloat')
        if a_float is not None:
            a_float.contents.value = self._defaults['ReturnMultipleTypes']['aFloat']
        # a_float_enum
        if self._defaults['ReturnMultipleTypes']['aFloatEnum'] is None:
            raise MockFunctionCallError("niFake_ReturnMultipleTypes", param='aFloatEnum')
        if a_float_enum is not None:
            a_float_enum.contents.value = self._defaults['ReturnMultipleTypes']['aFloatEnum']
        # an_array
        if self._defaults['ReturnMultipleTypes']['anArray'] is None:
            raise MockFunctionCallError("niFake_ReturnMultipleTypes", param='anArray')
        test_value = self._defaults['ReturnMultipleTypes']['anArray']
        try:
            an_array_ref = an_array.contents
        except AttributeError:
            an_array_ref = an_array
        assert len(an_array_ref) >= len(test_value)
        for i in range(len(test_value)):
            an_array_ref[i] = test_value[i]
        # a_string
        if self._defaults['ReturnMultipleTypes']['aString'] is None:
            raise MockFunctionCallError("niFake_ReturnMultipleTypes", param='aString')
        if string_size.value == 0:
            return len(self._defaults['ReturnMultipleTypes']['aString'])
        a_string.value = self._defaults['ReturnMultipleTypes']['aString'].encode('ascii')
        return self._defaults['ReturnMultipleTypes']['return']

    def niFake_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViBoolean']['return'] != 0:
            return self._defaults['SetAttributeViBoolean']['return']
        return self._defaults['SetAttributeViBoolean']['return']

    def niFake_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViInt32']['return'] != 0:
            return self._defaults['SetAttributeViInt32']['return']
        return self._defaults['SetAttributeViInt32']['return']

    def niFake_SetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViInt64']['return'] != 0:
            return self._defaults['SetAttributeViInt64']['return']
        return self._defaults['SetAttributeViInt64']['return']

    def niFake_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViReal64']['return'] != 0:
            return self._defaults['SetAttributeViReal64']['return']
        return self._defaults['SetAttributeViReal64']['return']

    def niFake_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViString']['return'] != 0:
            return self._defaults['SetAttributeViString']['return']
        return self._defaults['SetAttributeViString']['return']

    def niFake_SetCustomType(self, vi, cs):  # noqa: N802
        if self._defaults['SetCustomType']['return'] != 0:
            return self._defaults['SetCustomType']['return']
        return self._defaults['SetCustomType']['return']

    def niFake_SetCustomTypeArray(self, vi, number_of_elements, cs):  # noqa: N802
        if self._defaults['SetCustomTypeArray']['return'] != 0:
            return self._defaults['SetCustomTypeArray']['return']
        return self._defaults['SetCustomTypeArray']['return']

    def niFake_SetRuntimeEnvironment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        if self._defaults['SetRuntimeEnvironment']['return'] != 0:
            return self._defaults['SetRuntimeEnvironment']['return']
        return self._defaults['SetRuntimeEnvironment']['return']

    def niFake_StringValuedEnumInputFunctionWithDefaults(self, vi, a_mobile_os_name):  # noqa: N802
        if self._defaults['StringValuedEnumInputFunctionWithDefaults']['return'] != 0:
            return self._defaults['StringValuedEnumInputFunctionWithDefaults']['return']
        return self._defaults['StringValuedEnumInputFunctionWithDefaults']['return']

    def niFake_TwoInputFunction(self, vi, a_number, a_string):  # noqa: N802
        if self._defaults['TwoInputFunction']['return'] != 0:
            return self._defaults['TwoInputFunction']['return']
        return self._defaults['TwoInputFunction']['return']

    def niFake_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['UnlockSession']['return'] != 0:
            return self._defaults['UnlockSession']['return']
        # caller_has_lock
        if self._defaults['UnlockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niFake_UnlockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['UnlockSession']['callerHasLock']
        return self._defaults['UnlockSession']['return']

    def niFake_Use64BitNumber(self, vi, input, output):  # noqa: N802
        if self._defaults['Use64BitNumber']['return'] != 0:
            return self._defaults['Use64BitNumber']['return']
        # output
        if self._defaults['Use64BitNumber']['output'] is None:
            raise MockFunctionCallError("niFake_Use64BitNumber", param='output')
        if output is not None:
            output.contents.value = self._defaults['Use64BitNumber']['output']
        return self._defaults['Use64BitNumber']['return']

    def niFake_WriteWaveform(self, vi, number_of_samples, waveform):  # noqa: N802
        if self._defaults['WriteWaveform']['return'] != 0:
            return self._defaults['WriteWaveform']['return']
        return self._defaults['WriteWaveform']['return']

    def niFake_WriteWaveformNumpyComplex128(self, vi, number_of_samples, waveform_data_array):  # noqa: N802
        if self._defaults['WriteWaveformNumpyComplex128']['return'] != 0:
            return self._defaults['WriteWaveformNumpyComplex128']['return']
        return self._defaults['WriteWaveformNumpyComplex128']['return']

    def niFake_WriteWaveformNumpyComplex64(self, vi, number_of_samples, waveform_data_array):  # noqa: N802
        if self._defaults['WriteWaveformNumpyComplex64']['return'] != 0:
            return self._defaults['WriteWaveformNumpyComplex64']['return']
        return self._defaults['WriteWaveformNumpyComplex64']['return']

    def niFake_WriteWaveformNumpyComplexInterleavedI16(self, vi, number_of_samples, waveform_data_array):  # noqa: N802
        if self._defaults['WriteWaveformNumpyComplexInterleavedI16']['return'] != 0:
            return self._defaults['WriteWaveformNumpyComplexInterleavedI16']['return']
        return self._defaults['WriteWaveformNumpyComplexInterleavedI16']['return']

    def niFake_close(self, vi):  # noqa: N802
        if self._defaults['close']['return'] != 0:
            return self._defaults['close']['return']
        return self._defaults['close']['return']

    def niFake_error_message(self, vi, error_code, error_message):  # noqa: N802
        if self._defaults['error_message']['return'] != 0:
            return self._defaults['error_message']['return']
        # error_message
        if self._defaults['error_message']['errorMessage'] is None:
            raise MockFunctionCallError("niFake_error_message", param='errorMessage')
        test_value = self._defaults['error_message']['errorMessage']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(error_message) >= len(test_value)
        for i in range(len(test_value)):
            error_message[i] = test_value[i]
        return self._defaults['error_message']['return']

    def niFake_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        if self._defaults['self_test']['return'] != 0:
            return self._defaults['self_test']['return']
        # self_test_result
        if self._defaults['self_test']['selfTestResult'] is None:
            raise MockFunctionCallError("niFake_self_test", param='selfTestResult')
        if self_test_result is not None:
            self_test_result.contents.value = self._defaults['self_test']['selfTestResult']
        # self_test_message
        if self._defaults['self_test']['selfTestMessage'] is None:
            raise MockFunctionCallError("niFake_self_test", param='selfTestMessage')
        test_value = self._defaults['self_test']['selfTestMessage']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(self_test_message) >= len(test_value)
        for i in range(len(test_value)):
            self_test_message[i] = test_value[i]
        return self._defaults['self_test']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niFake_Abort.side_effect = MockFunctionCallError("niFake_Abort")
        mock_library.niFake_Abort.return_value = 0
        mock_library.niFake_AcceptListOfDurationsInSeconds.side_effect = MockFunctionCallError("niFake_AcceptListOfDurationsInSeconds")
        mock_library.niFake_AcceptListOfDurationsInSeconds.return_value = 0
        mock_library.niFake_BoolArrayOutputFunction.side_effect = MockFunctionCallError("niFake_BoolArrayOutputFunction")
        mock_library.niFake_BoolArrayOutputFunction.return_value = 0
        mock_library.niFake_ConfigureABC.side_effect = MockFunctionCallError("niFake_ConfigureABC")
        mock_library.niFake_ConfigureABC.return_value = 0
        mock_library.niFake_CustomNestedStructRoundtrip.side_effect = MockFunctionCallError("niFake_CustomNestedStructRoundtrip")
        mock_library.niFake_CustomNestedStructRoundtrip.return_value = 0
        mock_library.niFake_DoubleAllTheNums.side_effect = MockFunctionCallError("niFake_DoubleAllTheNums")
        mock_library.niFake_DoubleAllTheNums.return_value = 0
        mock_library.niFake_EnumArrayOutputFunction.side_effect = MockFunctionCallError("niFake_EnumArrayOutputFunction")
        mock_library.niFake_EnumArrayOutputFunction.return_value = 0
        mock_library.niFake_EnumInputFunctionWithDefaults.side_effect = MockFunctionCallError("niFake_EnumInputFunctionWithDefaults")
        mock_library.niFake_EnumInputFunctionWithDefaults.return_value = 0
        mock_library.niFake_ExportAttributeConfigurationBuffer.side_effect = MockFunctionCallError("niFake_ExportAttributeConfigurationBuffer")
        mock_library.niFake_ExportAttributeConfigurationBuffer.return_value = 0
        mock_library.niFake_FetchWaveform.side_effect = MockFunctionCallError("niFake_FetchWaveform")
        mock_library.niFake_FetchWaveform.return_value = 0
        mock_library.niFake_FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter.side_effect = MockFunctionCallError("niFake_FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter")
        mock_library.niFake_FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter.return_value = 0
        mock_library.niFake_FunctionWithIntflagParameter.side_effect = MockFunctionCallError("niFake_FunctionWithIntflagParameter")
        mock_library.niFake_FunctionWithIntflagParameter.return_value = 0
        mock_library.niFake_FunctionWithRepeatedCapabilityType.side_effect = MockFunctionCallError("niFake_FunctionWithRepeatedCapabilityType")
        mock_library.niFake_FunctionWithRepeatedCapabilityType.return_value = 0
        mock_library.niFake_GetABoolean.side_effect = MockFunctionCallError("niFake_GetABoolean")
        mock_library.niFake_GetABoolean.return_value = 0
        mock_library.niFake_GetANumber.side_effect = MockFunctionCallError("niFake_GetANumber")
        mock_library.niFake_GetANumber.return_value = 0
        mock_library.niFake_GetAStringOfFixedMaximumSize.side_effect = MockFunctionCallError("niFake_GetAStringOfFixedMaximumSize")
        mock_library.niFake_GetAStringOfFixedMaximumSize.return_value = 0
        mock_library.niFake_GetAStringUsingPythonCode.side_effect = MockFunctionCallError("niFake_GetAStringUsingPythonCode")
        mock_library.niFake_GetAStringUsingPythonCode.return_value = 0
        mock_library.niFake_GetAnIviDanceCharArray.side_effect = MockFunctionCallError("niFake_GetAnIviDanceCharArray")
        mock_library.niFake_GetAnIviDanceCharArray.return_value = 0
        mock_library.niFake_GetAnIviDanceWithATwistString.side_effect = MockFunctionCallError("niFake_GetAnIviDanceWithATwistString")
        mock_library.niFake_GetAnIviDanceWithATwistString.return_value = 0
        mock_library.niFake_GetArrayForPythonCodeCustomType.side_effect = MockFunctionCallError("niFake_GetArrayForPythonCodeCustomType")
        mock_library.niFake_GetArrayForPythonCodeCustomType.return_value = 0
        mock_library.niFake_GetArrayForPythonCodeDouble.side_effect = MockFunctionCallError("niFake_GetArrayForPythonCodeDouble")
        mock_library.niFake_GetArrayForPythonCodeDouble.return_value = 0
        mock_library.niFake_GetArraySizeForPythonCode.side_effect = MockFunctionCallError("niFake_GetArraySizeForPythonCode")
        mock_library.niFake_GetArraySizeForPythonCode.return_value = 0
        mock_library.niFake_GetArrayUsingIviDance.side_effect = MockFunctionCallError("niFake_GetArrayUsingIviDance")
        mock_library.niFake_GetArrayUsingIviDance.return_value = 0
        mock_library.niFake_GetAttributeViBoolean.side_effect = MockFunctionCallError("niFake_GetAttributeViBoolean")
        mock_library.niFake_GetAttributeViBoolean.return_value = 0
        mock_library.niFake_GetAttributeViInt32.side_effect = MockFunctionCallError("niFake_GetAttributeViInt32")
        mock_library.niFake_GetAttributeViInt32.return_value = 0
        mock_library.niFake_GetAttributeViInt64.side_effect = MockFunctionCallError("niFake_GetAttributeViInt64")
        mock_library.niFake_GetAttributeViInt64.return_value = 0
        mock_library.niFake_GetAttributeViReal64.side_effect = MockFunctionCallError("niFake_GetAttributeViReal64")
        mock_library.niFake_GetAttributeViReal64.return_value = 0
        mock_library.niFake_GetAttributeViString.side_effect = MockFunctionCallError("niFake_GetAttributeViString")
        mock_library.niFake_GetAttributeViString.return_value = 0
        mock_library.niFake_GetCalDateAndTime.side_effect = MockFunctionCallError("niFake_GetCalDateAndTime")
        mock_library.niFake_GetCalDateAndTime.return_value = 0
        mock_library.niFake_GetCalInterval.side_effect = MockFunctionCallError("niFake_GetCalInterval")
        mock_library.niFake_GetCalInterval.return_value = 0
        mock_library.niFake_GetChannelNames.side_effect = MockFunctionCallError("niFake_GetChannelNames")
        mock_library.niFake_GetChannelNames.return_value = 0
        mock_library.niFake_GetCustomType.side_effect = MockFunctionCallError("niFake_GetCustomType")
        mock_library.niFake_GetCustomType.return_value = 0
        mock_library.niFake_GetCustomTypeArray.side_effect = MockFunctionCallError("niFake_GetCustomTypeArray")
        mock_library.niFake_GetCustomTypeArray.return_value = 0
        mock_library.niFake_GetCustomTypeTypedef.side_effect = MockFunctionCallError("niFake_GetCustomTypeTypedef")
        mock_library.niFake_GetCustomTypeTypedef.return_value = 0
        mock_library.niFake_GetEnumValue.side_effect = MockFunctionCallError("niFake_GetEnumValue")
        mock_library.niFake_GetEnumValue.return_value = 0
        mock_library.niFake_GetError.side_effect = MockFunctionCallError("niFake_GetError")
        mock_library.niFake_GetError.return_value = 0
        mock_library.niFake_GetParameterWithOverriddenGrpcName.side_effect = MockFunctionCallError("niFake_GetParameterWithOverriddenGrpcName")
        mock_library.niFake_GetParameterWithOverriddenGrpcName.return_value = 0
        mock_library.niFake_ImportAttributeConfigurationBuffer.side_effect = MockFunctionCallError("niFake_ImportAttributeConfigurationBuffer")
        mock_library.niFake_ImportAttributeConfigurationBuffer.return_value = 0
        mock_library.niFake_ImportAttributeConfigurationBufferEx.side_effect = MockFunctionCallError("niFake_ImportAttributeConfigurationBufferEx")
        mock_library.niFake_ImportAttributeConfigurationBufferEx.return_value = 0
        mock_library.niFake_InitWithOptions.side_effect = MockFunctionCallError("niFake_InitWithOptions")
        mock_library.niFake_InitWithOptions.return_value = 0
        mock_library.niFake_Initiate.side_effect = MockFunctionCallError("niFake_Initiate")
        mock_library.niFake_Initiate.return_value = 0
        mock_library.niFake_LockSession.side_effect = MockFunctionCallError("niFake_LockSession")
        mock_library.niFake_LockSession.return_value = 0
        mock_library.niFake_MethodUsingWholeAndFractionalNumbers.side_effect = MockFunctionCallError("niFake_MethodUsingWholeAndFractionalNumbers")
        mock_library.niFake_MethodUsingWholeAndFractionalNumbers.return_value = 0
        mock_library.niFake_MethodWithGrpcOnlyParam.side_effect = MockFunctionCallError("niFake_MethodWithGrpcOnlyParam")
        mock_library.niFake_MethodWithGrpcOnlyParam.return_value = 0
        mock_library.niFake_MethodWithProtoOnlyParameter.side_effect = MockFunctionCallError("niFake_MethodWithProtoOnlyParameter")
        mock_library.niFake_MethodWithProtoOnlyParameter.return_value = 0
        mock_library.niFake_MixedIviDanceAndLenMechanism.side_effect = MockFunctionCallError("niFake_MixedIviDanceAndLenMechanism")
        mock_library.niFake_MixedIviDanceAndLenMechanism.return_value = 0
        mock_library.niFake_MultipleArrayTypes.side_effect = MockFunctionCallError("niFake_MultipleArrayTypes")
        mock_library.niFake_MultipleArrayTypes.return_value = 0
        mock_library.niFake_MultipleArraysDifferentSize.side_effect = MockFunctionCallError("niFake_MultipleArraysDifferentSize")
        mock_library.niFake_MultipleArraysDifferentSize.return_value = 0
        mock_library.niFake_MultipleArraysSameSize.side_effect = MockFunctionCallError("niFake_MultipleArraysSameSize")
        mock_library.niFake_MultipleArraysSameSize.return_value = 0
        mock_library.niFake_OneInputFunction.side_effect = MockFunctionCallError("niFake_OneInputFunction")
        mock_library.niFake_OneInputFunction.return_value = 0
        mock_library.niFake_ParametersAreMultipleTypes.side_effect = MockFunctionCallError("niFake_ParametersAreMultipleTypes")
        mock_library.niFake_ParametersAreMultipleTypes.return_value = 0
        mock_library.niFake_PoorlyNamedSimpleFunction.side_effect = MockFunctionCallError("niFake_PoorlyNamedSimpleFunction")
        mock_library.niFake_PoorlyNamedSimpleFunction.return_value = 0
        mock_library.niFake_Read.side_effect = MockFunctionCallError("niFake_Read")
        mock_library.niFake_Read.return_value = 0
        mock_library.niFake_ReadFromChannel.side_effect = MockFunctionCallError("niFake_ReadFromChannel")
        mock_library.niFake_ReadFromChannel.return_value = 0
        mock_library.niFake_ReturnANumberAndAString.side_effect = MockFunctionCallError("niFake_ReturnANumberAndAString")
        mock_library.niFake_ReturnANumberAndAString.return_value = 0
        mock_library.niFake_ReturnDurationInSeconds.side_effect = MockFunctionCallError("niFake_ReturnDurationInSeconds")
        mock_library.niFake_ReturnDurationInSeconds.return_value = 0
        mock_library.niFake_ReturnListOfDurationsInSeconds.side_effect = MockFunctionCallError("niFake_ReturnListOfDurationsInSeconds")
        mock_library.niFake_ReturnListOfDurationsInSeconds.return_value = 0
        mock_library.niFake_ReturnMultipleTypes.side_effect = MockFunctionCallError("niFake_ReturnMultipleTypes")
        mock_library.niFake_ReturnMultipleTypes.return_value = 0
        mock_library.niFake_SetAttributeViBoolean.side_effect = MockFunctionCallError("niFake_SetAttributeViBoolean")
        mock_library.niFake_SetAttributeViBoolean.return_value = 0
        mock_library.niFake_SetAttributeViInt32.side_effect = MockFunctionCallError("niFake_SetAttributeViInt32")
        mock_library.niFake_SetAttributeViInt32.return_value = 0
        mock_library.niFake_SetAttributeViInt64.side_effect = MockFunctionCallError("niFake_SetAttributeViInt64")
        mock_library.niFake_SetAttributeViInt64.return_value = 0
        mock_library.niFake_SetAttributeViReal64.side_effect = MockFunctionCallError("niFake_SetAttributeViReal64")
        mock_library.niFake_SetAttributeViReal64.return_value = 0
        mock_library.niFake_SetAttributeViString.side_effect = MockFunctionCallError("niFake_SetAttributeViString")
        mock_library.niFake_SetAttributeViString.return_value = 0
        mock_library.niFake_SetCustomType.side_effect = MockFunctionCallError("niFake_SetCustomType")
        mock_library.niFake_SetCustomType.return_value = 0
        mock_library.niFake_SetCustomTypeArray.side_effect = MockFunctionCallError("niFake_SetCustomTypeArray")
        mock_library.niFake_SetCustomTypeArray.return_value = 0
        mock_library.niFake_SetRuntimeEnvironment.side_effect = MockFunctionCallError("niFake_SetRuntimeEnvironment")
        mock_library.niFake_SetRuntimeEnvironment.return_value = 0
        mock_library.niFake_StringValuedEnumInputFunctionWithDefaults.side_effect = MockFunctionCallError("niFake_StringValuedEnumInputFunctionWithDefaults")
        mock_library.niFake_StringValuedEnumInputFunctionWithDefaults.return_value = 0
        mock_library.niFake_TwoInputFunction.side_effect = MockFunctionCallError("niFake_TwoInputFunction")
        mock_library.niFake_TwoInputFunction.return_value = 0
        mock_library.niFake_UnlockSession.side_effect = MockFunctionCallError("niFake_UnlockSession")
        mock_library.niFake_UnlockSession.return_value = 0
        mock_library.niFake_Use64BitNumber.side_effect = MockFunctionCallError("niFake_Use64BitNumber")
        mock_library.niFake_Use64BitNumber.return_value = 0
        mock_library.niFake_WriteWaveform.side_effect = MockFunctionCallError("niFake_WriteWaveform")
        mock_library.niFake_WriteWaveform.return_value = 0
        mock_library.niFake_WriteWaveformNumpyComplex128.side_effect = MockFunctionCallError("niFake_WriteWaveformNumpyComplex128")
        mock_library.niFake_WriteWaveformNumpyComplex128.return_value = 0
        mock_library.niFake_WriteWaveformNumpyComplex64.side_effect = MockFunctionCallError("niFake_WriteWaveformNumpyComplex64")
        mock_library.niFake_WriteWaveformNumpyComplex64.return_value = 0
        mock_library.niFake_WriteWaveformNumpyComplexInterleavedI16.side_effect = MockFunctionCallError("niFake_WriteWaveformNumpyComplexInterleavedI16")
        mock_library.niFake_WriteWaveformNumpyComplexInterleavedI16.return_value = 0
        mock_library.niFake_close.side_effect = MockFunctionCallError("niFake_close")
        mock_library.niFake_close.return_value = 0
        mock_library.niFake_error_message.side_effect = MockFunctionCallError("niFake_error_message")
        mock_library.niFake_error_message.return_value = 0
        mock_library.niFake_self_test.side_effect = MockFunctionCallError("niFake_self_test")
        mock_library.niFake_self_test.return_value = 0
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/nifake/unit_tests/test_converters.py sha256=51960a6e9bda494a06bdc5a6e01d947bad9b2366139564cb7d5679afd7fb6f64 bytes=22272 -->
## FILE: generated/nifake/nifake/unit_tests/test_converters.py

- repository: `ni/nimi-python`
- source_path: `generated/nifake/nifake/unit_tests/test_converters.py`
- sha256: `51960a6e9bda494a06bdc5a6e01d947bad9b2366139564cb7d5679afd7fb6f64`
- bytes: 22272

````python
import nifake._converters as _converters
import nifake.errors as errors

import hightime
import pytest


def test_convert_init_with_options_dictionary():
    assert _converters.convert_init_with_options_dictionary('') == ''
    assert _converters.convert_init_with_options_dictionary('Simulate=1') == 'Simulate=1'
    assert _converters.convert_init_with_options_dictionary({'Simulate': True, }) == 'Simulate=1'
    assert _converters.convert_init_with_options_dictionary({'Simulate': False, }) == 'Simulate=0'
    assert _converters.convert_init_with_options_dictionary({'Simulate': True, 'Cache': False}) == 'Cache=0,Simulate=1'
    assert _converters.convert_init_with_options_dictionary({'DriverSetup': {'Model': '5162 (4CH)', 'Bitfile': 'CustomProcessing'}}) == 'DriverSetup=Bitfile:CustomProcessing;Model:5162 (4CH)'
    assert _converters.convert_init_with_options_dictionary({'Simulate': True, 'DriverSetup': {'Model': '5162 (4CH)', 'Bitfile': 'CustomProcessing'}}) == 'DriverSetup=Bitfile:CustomProcessing;Model:5162 (4CH),Simulate=1'
    assert _converters.convert_init_with_options_dictionary({'simulate': True, 'cache': False}) == 'Cache=0,Simulate=1'
    assert _converters.convert_init_with_options_dictionary({'driver_setup': {'Model': '5162 (4CH)', 'Bitfile': 'CustomProcessing'}}) == 'DriverSetup=Bitfile:CustomProcessing;Model:5162 (4CH)'
    assert _converters.convert_init_with_options_dictionary({'simulate': True, 'driver_setup': {'Model': '5162 (4CH)', 'Bitfile': 'CustomProcessing'}}) == 'DriverSetup=Bitfile:CustomProcessing;Model:5162 (4CH),Simulate=1'


# Tests - time
def test_convert_timedelta_to_seconds_double():
    test_result = _converters.convert_timedelta_to_seconds_real64(hightime.timedelta(seconds=10))
    assert test_result == 10.0
    test_result = _converters.convert_timedelta_to_seconds_real64(hightime.timedelta(nanoseconds=-0.5))
    assert test_result == pytest.approx(-5e-10)
    test_result = _converters.convert_timedelta_to_seconds_real64(10.5)
    assert test_result == 10.5
    test_result = _converters.convert_timedelta_to_seconds_real64(-1)
    assert test_result == -1


def test_convert_timedelta_to_milliseconds_int32():
    test_result = _converters.convert_timedelta_to_milliseconds_int32(hightime.timedelta(seconds=10))
    assert test_result == 10000
    test_result = _converters.convert_timedelta_to_milliseconds_int32(hightime.timedelta(seconds=-5))
    assert test_result == -5000
    test_result = _converters.convert_timedelta_to_milliseconds_int32(10.5)
    assert test_result == 10500
    test_result = _converters.convert_timedelta_to_milliseconds_int32(-1)
    assert test_result == -1000


def test_convert_timedeltas_to_seconds_real64():
    time_values = [10.5, -5e-10]
    test_result = _converters.convert_timedeltas_to_seconds_real64(time_values)
    assert all([actual == pytest.approx(expected) for actual, expected in zip(test_result, time_values)])
    test_input = [hightime.timedelta(seconds=10.5), hightime.timedelta(nanoseconds=-0.5)]
    test_result = _converters.convert_timedeltas_to_seconds_real64(test_input)
    assert all([actual == pytest.approx(expected) for actual, expected in zip(test_result, time_values)])


def test_convert_timedelta_to_months_int32():
    # 1 month = 60*60*24*30.4167 seconds = 2628002.88 seconds
    seconds_per_month = 60 * 60 * 24 * 30.4167
    test_result = _converters.convert_timedelta_to_months_int32(hightime.timedelta(seconds=seconds_per_month))
    assert test_result == 1
    test_result = _converters.convert_timedelta_to_months_int32(hightime.timedelta(seconds=-5 * seconds_per_month))
    assert test_result == -5
    test_result = _converters.convert_timedelta_to_months_int32(seconds_per_month * 2)
    assert test_result == 2
    test_result = _converters.convert_timedelta_to_months_int32(-seconds_per_month)
    assert test_result == -1


def test_convert_seconds_real64_to_timedelta():
    time_value = -5e-10
    test_result = _converters.convert_seconds_real64_to_timedelta(time_value)
    assert test_result.total_seconds() == pytest.approx(time_value)
    assert isinstance(test_result, hightime.timedelta)


def test_convert_seconds_real64_to_timedeltas():
    time_values = [10.5, -5e-10]
    test_result = _converters.convert_seconds_real64_to_timedeltas(time_values)
    assert all([actual.total_seconds() == pytest.approx(expected) for actual, expected in zip(test_result, time_values)])
    assert all([isinstance(x, hightime.timedelta) for x in test_result])


# Tests - repeated capabilities
def test_repeated_capabilities_string_channel():
    test_result_list = _converters.convert_repeated_capabilities('0')
    assert test_result_list == ['0']
    test_result_list = _converters.convert_repeated_capabilities('r0')
    assert test_result_list == ['r0']
    test_result_list = _converters.convert_repeated_capabilities('0,1')
    assert test_result_list == ['0', '1']


def test_repeated_capabilities_string_prefix():
    test_result_list = _converters.convert_repeated_capabilities('0', prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0']


def test_repeated_capabilities_list_channel():
    test_result_list = _converters.convert_repeated_capabilities(['0'])
    assert test_result_list == ['0']
    test_result_list = _converters.convert_repeated_capabilities(['r0'])
    assert test_result_list == ['r0']
    test_result_list = _converters.convert_repeated_capabilities(['0', '1'])
    assert test_result_list == ['0', '1']
    test_result_list = _converters.convert_repeated_capabilities([0, 1])
    assert test_result_list == ['0', '1']
    test_result_list = _converters.convert_repeated_capabilities([0, 1, '3'])
    assert test_result_list == ['0', '1', '3']


def test_repeated_capabilities_list_prefix():
    test_result_list = _converters.convert_repeated_capabilities(['ScriptTrigger0', 'ScriptTrigger1'], prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities(['0'], prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0']
    test_result_list = _converters.convert_repeated_capabilities(['0', '1'], prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities([0, 1], prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']


def test_repeated_capabilities_tuple_channel():
    test_result_list = _converters.convert_repeated_capabilities(('0'))
    assert test_result_list == ['0']
    test_result_list = _converters.convert_repeated_capabilities(('0,1'))
    assert test_result_list == ['0', '1']
    test_result_list = _converters.convert_repeated_capabilities(('0', '1'))
    assert test_result_list == ['0', '1']
    test_result_list = _converters.convert_repeated_capabilities((0, 1))
    assert test_result_list == ['0', '1']
    test_result_list = _converters.convert_repeated_capabilities((0, 1, '3'))
    assert test_result_list == ['0', '1', '3']


def test_repeated_capabilities_tuple_prefix():
    test_result_list = _converters.convert_repeated_capabilities(('ScriptTrigger0,ScriptTrigger1'), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities(('0'), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0']
    test_result_list = _converters.convert_repeated_capabilities(('0', '1'), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities((0, 1), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']


def test_repeated_capabilities_unicode():
    test_result_list = _converters.convert_repeated_capabilities(u'ScriptTrigger0,ScriptTrigger1', prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities(u'ScriptTrigger0,ScriptTrigger1', prefix=u'ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities('ScriptTrigger0,ScriptTrigger1', prefix=u'ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']


def test_repeated_capabilities_raw():
    test_result_list = _converters.convert_repeated_capabilities(r'ScriptTrigger0,ScriptTrigger1', prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities(r'ScriptTrigger0,ScriptTrigger1', prefix=r'ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities('ScriptTrigger0,ScriptTrigger1', prefix=r'ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities(r'ScriptTrigger0,ScriptTrigger1', prefix=u'ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities(r'ScriptTrigger0,ScriptTrigger1', prefix=r'ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities(u'ScriptTrigger0,ScriptTrigger1', prefix=r'ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']


def test_repeated_capabilities_slice_channel():
    test_result_list = _converters.convert_repeated_capabilities(slice(0, 1))
    assert test_result_list == ['0']
    test_result_list = _converters.convert_repeated_capabilities(slice(0, 2))
    assert test_result_list == ['0', '1']
    test_result_list = _converters.convert_repeated_capabilities(slice(None, 2))
    assert test_result_list == ['0', '1']


def test_repeated_capabilities_mixed_channel():
    test_result_list = _converters.convert_repeated_capabilities((slice(0, 1), '2', [4, '5-6'], '7-9', '11:14', '16, 17'))
    assert test_result_list == ['0', '2', '4', '5', '6', '7', '8', '9', '11', '12', '13', '14', '16', '17']
    test_result_list = _converters.convert_repeated_capabilities([slice(0, 1), '2', [4, '5-6'], '7-9', '11:14', '16, 17'])
    assert test_result_list == ['0', '2', '4', '5', '6', '7', '8', '9', '11', '12', '13', '14', '16', '17']


def test_repeated_capabilities_mixed_prefix():
    test_result_list = _converters.convert_repeated_capabilities((slice(0, 1), '2', [4, '5-6'], '7-9', '11:14', '16, 17'), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger2', 'ScriptTrigger4', 'ScriptTrigger5', 'ScriptTrigger6', 'ScriptTrigger7', 'ScriptTrigger8', 'ScriptTrigger9', 'ScriptTrigger11', 'ScriptTrigger12', 'ScriptTrigger13', 'ScriptTrigger14', 'ScriptTrigger16', 'ScriptTrigger17']
    test_result_list = _converters.convert_repeated_capabilities([slice(0, 1), '2', [4, '5-6'], '7-9', '11:14', '16, 17'], prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger2', 'ScriptTrigger4', 'ScriptTrigger5', 'ScriptTrigger6', 'ScriptTrigger7', 'ScriptTrigger8', 'ScriptTrigger9', 'ScriptTrigger11', 'ScriptTrigger12', 'ScriptTrigger13', 'ScriptTrigger14', 'ScriptTrigger16', 'ScriptTrigger17']


def test_invalid_repeated_capabilities():
    try:
        _converters.convert_repeated_capabilities('6-8-10')
        assert False
    except errors.InvalidRepeatedCapabilityError:
        pass
    try:
        _converters.convert_repeated_capabilities(['5', '6-8-10'])
        assert False
    except errors.InvalidRepeatedCapabilityError:
        pass
    try:
        _converters.convert_repeated_capabilities(('5', '6-8-10'))
        assert False
    except errors.InvalidRepeatedCapabilityError:
        pass
    try:
        _converters.convert_repeated_capabilities('5,6-8-10')
        assert False
    except errors.InvalidRepeatedCapabilityError:
        pass
    try:
        _converters.convert_repeated_capabilities(5.0)
        assert False
    except errors.InvalidRepeatedCapabilityError:
        pass
    try:
        _converters.convert_repeated_capabilities([5.0, '0'])
        assert False
    except errors.InvalidRepeatedCapabilityError:
        pass
    try:
        _converters.convert_repeated_capabilities((5.0, '0'))
        assert False
    except errors.InvalidRepeatedCapabilityError:
        pass


def test_repeated_capabilities_slice_prefix():
    test_result_list = _converters.convert_repeated_capabilities(slice(0, 1), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0']
    test_result_list = _converters.convert_repeated_capabilities(slice(0, 2), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']
    test_result_list = _converters.convert_repeated_capabilities(slice(None, 2), prefix='ScriptTrigger')
    assert test_result_list == ['ScriptTrigger0', 'ScriptTrigger1']


def test_repeated_capabilities_without_prefix():
    test_result = _converters.convert_repeated_capabilities_without_prefix((slice(0, 1), '2', [4, '5-6'], '7-9', '11:14', '16, 17'))
    assert test_result == '0,2,4,5,6,7,8,9,11,12,13,14,16,17'


def test_repeated_capabilities_string_resource_name():
    test_result_list = _converters.convert_repeated_capabilities_without_prefix('Dev1')
    assert test_result_list == 'Dev1'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix('Dev1,Dev2')
    assert test_result_list == 'Dev1,Dev2'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix('Dev1/0')
    assert test_result_list == 'Dev1/0'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix('Dev1/0:1, Dev2/0-1')
    assert test_result_list == 'Dev1/0:1,Dev2/0-1'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix('Dev1, Dev2/0-2')
    assert test_result_list == 'Dev1,Dev2/0-2'


def test_repeated_capabilities_list_resource_name():
    test_result_list = _converters.convert_repeated_capabilities_without_prefix(['Dev1'])
    assert test_result_list == 'Dev1'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix(['Dev1', 'Dev2'])
    assert test_result_list == 'Dev1,Dev2'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix(['Dev1/0'])
    assert test_result_list == 'Dev1/0'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix(['Dev1/0:1', 'Dev2/0-1'])
    assert test_result_list == 'Dev1/0:1,Dev2/0-1'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix(['Dev1', 'Dev2/0-2'])
    assert test_result_list == 'Dev1,Dev2/0-2'


def test_repeated_capabilities_tuple_resource_name():
    test_result_list = _converters.convert_repeated_capabilities_without_prefix(('Dev1'))
    assert test_result_list == 'Dev1'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix(('Dev1', 'Dev2'))
    assert test_result_list == 'Dev1,Dev2'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix(('Dev1/0'))
    assert test_result_list == 'Dev1/0'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix(('Dev1/0:1', 'Dev2/0-1'))
    assert test_result_list == 'Dev1/0:1,Dev2/0-1'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix(('Dev1', 'Dev2/0-2'))
    assert test_result_list == 'Dev1,Dev2/0-2'


def test_repeated_capabilities_mixed_resource_name():
    test_result_list = _converters.convert_repeated_capabilities_without_prefix(['Dev1', ('Dev2/0', 'Dev2/1'), ['Dev3/0:1', 'Dev4/1:2'], 'Dev5/1'])
    assert test_result_list == 'Dev1,Dev2/0,Dev2/1,Dev3/0:1,Dev4/1:2,Dev5/1'


def test_repeated_capabilities_invalid_resource_names():
    test_result_list = _converters.convert_repeated_capabilities_without_prefix('/')
    assert test_result_list == '/'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix('Dev/')
    assert test_result_list == 'Dev/'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix('Dev,')
    assert test_result_list == 'Dev,'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix('Dev/1/1,')
    assert test_result_list == 'Dev/1/1,'
    test_result_list = _converters.convert_repeated_capabilities_without_prefix('0/1:2,')
    assert test_result_list == '0/1:2,'


def test_expand_channel_string_non_fully_qualified_channel_names():
    test_result_list = _converters.expand_channel_string('1', ['0', '1', '2', '3'])
    assert test_result_list == ['1']
    test_result_list = _converters.expand_channel_string('0-2', ['0', '1', '2', '3'])
    assert test_result_list == ['0', '1', '2']
    test_result_list = _converters.expand_channel_string('0:2', ['0', '1', '2', '3'])
    assert test_result_list == ['0', '1', '2']
    test_result_list = _converters.expand_channel_string('0:2,4', ['0', '1', '2', '3', '4', '5'])
    assert test_result_list == ['0', '1', '2', '4']
    test_result_list = _converters.expand_channel_string('4,1:2', ['1', '2', '4'])
    assert test_result_list == ['4', '1', '2']
    test_result_list = _converters.expand_channel_string(' 1 : 2 , 4 ', ['1', '2', '4'])
    assert test_result_list == ['1', '2', '4']


def test_expand_channel_string_fully_qualified_channel_names():
    test_result_list = _converters.expand_channel_string(
        '2:3,0',
        ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/3']
    )
    assert test_result_list == ['Dev1/2', 'Dev1/3', 'Dev1/0']
    test_result_list = _converters.expand_channel_string(
        'Dev1/1',
        ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/3']
    )
    assert test_result_list == ['Dev1/1']
    test_result_list = _converters.expand_channel_string(
        'Dev1/0-2',
        ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/3']
    )
    assert test_result_list == ['Dev1/0', 'Dev1/1', 'Dev1/2']
    test_result_list = _converters.expand_channel_string(
        'Dev1/0:2',
        ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/3']
    )
    assert test_result_list == ['Dev1/0', 'Dev1/1', 'Dev1/2']
    test_result_list = _converters.expand_channel_string(
        'Dev1/0:2,4',
        ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/4']
    )
    assert test_result_list == ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/4']
    test_result_list = _converters.expand_channel_string(
        '4,Dev1/1:2',
        ['Dev1/1', 'Dev1/2', 'Dev1/4']
    )
    assert test_result_list == ['Dev1/4', 'Dev1/1', 'Dev1/2']
    test_result_list = _converters.expand_channel_string(
        'Dev1/4,Dev1/2,Dev1/3',
        ['Dev1/2', 'Dev1/3', 'Dev1/4']
    )
    assert test_result_list == ['Dev1/4', 'Dev1/2', 'Dev1/3']
    test_result_list = _converters.expand_channel_string(
        'Dev1/1,Dev2/2',
        ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/3', 'Dev2/0', 'Dev2/1', 'Dev2/2', 'Dev2/3']
    )
    assert test_result_list == ['Dev1/1', 'Dev2/2']
    test_result_list = _converters.expand_channel_string(
        ' Dev1 / 1 : 2 , 4 ',
        ['Dev1/1', 'Dev1/2', 'Dev1/4']
    )
    assert test_result_list == ['Dev1/1', 'Dev1/2', 'Dev1/4']
    test_result_list = _converters.expand_channel_string(
        'DEV1/0-1    , Dev1/3',
        ['dev1/0', 'dev1/1', 'dev1/2', 'dev1/3']
    )
    assert test_result_list == ['dev1/0', 'dev1/1', 'dev1/3']


def test_convert_chained_repeated_capability_to_parts_three_parts():
    chained_rep_cap = ('site0/test/PinA,site0/test/PinB,site0/test/PinC,'
                       'site1/test/PinA,site1/test/PinB,site1/test/PinC')
    rep_cap_list = _converters.convert_chained_repeated_capability_to_parts(chained_rep_cap)
    assert rep_cap_list == ['site0,site1', 'test', 'PinA,PinB,PinC']


def test_convert_chained_repeated_capability_to_parts_single_part():
    rep_cap_list = _converters.convert_chained_repeated_capability_to_parts('site0, site1')
    assert rep_cap_list == ['site0,site1']


def test_convert_chained_repeated_capability_to_parts_empty_string():
    rep_cap_list = _converters.convert_chained_repeated_capability_to_parts('')
    assert rep_cap_list == ['']


def test_string_to_list_channel():
    test_result = _converters._convert_repeated_capabilities('r0', '')
    assert test_result == ['r0']
    test_result = _converters._convert_repeated_capabilities(['0-2'], '')
    assert test_result == ['0', '1', '2']
    test_result = _converters._convert_repeated_capabilities(['3:7'], '')
    assert test_result == ['3', '4', '5', '6', '7']
    test_result = _converters._convert_repeated_capabilities(['2-0'], '')
    assert test_result == ['2', '1', '0']
    test_result = _converters._convert_repeated_capabilities(['2:0'], '')
    assert test_result == ['2', '1', '0']


def test_string_to_list_prefix():
    test_result = _converters._convert_repeated_capabilities(['ScriptTrigger3-ScriptTrigger7'], 'ScriptTrigger')
    assert test_result == ['3', '4', '5', '6', '7']
    test_result = _converters._convert_repeated_capabilities(['ScriptTrigger3:ScriptTrigger7'], 'ScriptTrigger')
    assert test_result == ['3', '4', '5', '6', '7']
    test_result = _converters._convert_repeated_capabilities(['ScriptTrigger2-ScriptTrigger0'], 'ScriptTrigger')
    assert test_result == ['2', '1', '0']
    test_result = _converters._convert_repeated_capabilities(['ScriptTrigger2:ScriptTrigger0'], 'ScriptTrigger')
    assert test_result == ['2', '1', '0']


def test_convert_comma_separated_string_to_list():
    out_list = _converters.convert_comma_separated_string_to_list(' PinA ,  PinB , PinC  ')
    assert out_list == ['PinA', 'PinB', 'PinC']


def test_convert_list_to_comma_separated_string():
    out_string = _converters.convert_list_to_comma_separated_string(['PinA', 'PinB', 'PinC'])
    assert out_string == 'PinA,PinB,PinC'


def test_convert_list_to_comma_separated_string_invalid_input():
    with pytest.raises(TypeError) as error_info:
        _converters.convert_list_to_comma_separated_string('PinA,PinB,PinC')
    assert str(error_info.value) == 'Input must be a list or tuple of str'
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/nifake/unit_tests/test_grpc.py sha256=0052a2984291996f78a37bdb936492ba4b4d3b28f2a38b6ba0ffbdf3340a7677 bytes=55634 -->
## FILE: generated/nifake/nifake/unit_tests/test_grpc.py

- repository: `ni/nimi-python`
- source_path: `generated/nifake/nifake/unit_tests/test_grpc.py`
- sha256: `0052a2984291996f78a37bdb936492ba4b4d3b28f2a38b6ba0ffbdf3340a7677`
- bytes: 55634

````python
import array
import collections
import grpc
import math
import nifake
import nifake.errors
import numpy
import pytest
import session_pb2
import warnings

from unittest.mock import MagicMock
from unittest.mock import patch

import _mock_helper

GRPC_SESSION_OBJECT_FOR_TEST = session_pb2.Session(name="TestSession", id=42)


Metadatum = collections.namedtuple('Metadatum', ('key', 'value'))


class MyRpcError(grpc.RpcError):
    def __init__(self, error_code, error_message, grpc_error=grpc.StatusCode.UNKNOWN):
        super().__init__()
        self._grpc_error = grpc_error
        self._error_code = error_code
        self._error_message = error_message

    def code(self):
        return self._grpc_error

    def details(self):
        return self._error_message

    def trailing_metadata(self):
        if self._error_code is None:
            return []
        else:
            return [Metadatum('ni-error', str(self._error_code))]


class TestGrpcStubInterpreter:

    class PatchedGrpcTypes:
        def __init__(self):
            for f in dir(nifake._grpc_stub_interpreter.grpc_types):
                if f.endswith('Request'):
                    real_func = getattr(nifake._grpc_stub_interpreter.grpc_types, f)
                    error_func = _mock_helper.MockFunctionCallError(f)
                    setattr(self, f, MagicMock(spec_set=real_func, side_effect=error_func))
                else:
                    setattr(self, f, getattr(nifake._grpc_stub_interpreter.grpc_types, f))

    class PatchedGrpcStub(nifake._grpc_stub_interpreter.nifake_grpc.NiFakeServicer):
        def _sample_func(self, request, metadata=None):
            pass

        def __init__(self):
            for f in dir(self):
                if not f.startswith('_') and f not in {'get_session_handle', 'set_session_handle'}:
                    error_func = _mock_helper.MockFunctionCallError(f)
                    setattr(self, f, MagicMock(spec_set=self._sample_func, side_effect=error_func))

        def __call__(self, grpc_channel):
            self._grpc_channel = grpc_channel
            return self

    def setup_method(self, method):
        self.patched_grpc_types = self.PatchedGrpcTypes()
        self.patched_grpc_stub = self.PatchedGrpcStub()
        self.real_grpc_types = nifake._grpc_stub_interpreter.grpc_types
        self.grpc_types_patch = patch('nifake._grpc_stub_interpreter.grpc_types', self.patched_grpc_types)
        self.grpc_stub_patch = patch('nifake._grpc_stub_interpreter.nifake_grpc.NiFakeStub', side_effect=self.patched_grpc_stub)
        self.grpc_types_patch.start()
        self.grpc_stub_patch.start()

        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        self.get_ctypes_pointer_for_buffer_side_effect_items = []

    def teardown_method(self, method):
        self.grpc_stub_patch.stop()
        self.grpc_types_patch.stop()

    def _get_initialized_stub_interpreter(self, grpc_channel=object()):
        session_options = nifake.GrpcSessionOptions(grpc_channel, '', initialization_behavior=nifake.SessionInitializationBehavior.AUTO)
        interpreter = nifake._grpc_stub_interpreter.GrpcStubInterpreter(session_options)
        assert interpreter._client is self.patched_grpc_stub
        assert interpreter.get_session_handle().id == 0
        assert interpreter.get_session_handle().name == ""
        assert self.patched_grpc_stub._grpc_channel is grpc_channel
        interpreter.set_session_handle(GRPC_SESSION_OBJECT_FOR_TEST)
        return interpreter

    def _check_fields(self, response_class, **kwargs):
        fields = dict(kwargs)
        response_fields = {x.name: x for x in response_class.DESCRIPTOR.fields}

        unexpected_fields = set(fields) - set(response_fields)
        assert not unexpected_fields, 'Unexpected fields: ' + str(list(sorted(unexpected_fields)))

        for f in response_fields:
            if f.endswith('_raw') and f[:-4] in response_fields:
                fields.setdefault(f, fields[f[:-4]])
                fields.setdefault(f[:-4], fields[f])

        missing_fields = set(response_fields) - set(fields)
        assert not missing_fields, 'Missing fields: ' + str(list(sorted(missing_fields)))

        for field, value in fields.items():
            rf = response_fields[field]
            field_type = rf.type
            if field_type == rf.TYPE_ENUM:
                if (field + '_raw') not in fields:
                    assert field.endswith('_mapped')
                    raw_field = field.rpartition('_mapped')[0] + '_raw'
                    assert raw_field in fields
                    assert kwargs.get(raw_field)
                    if rf.label == rf.LABEL_REPEATED:
                        assert len(kwargs[raw_field]) == len(value)
                expected_py_type = int
            elif field_type == rf.TYPE_BOOL:
                expected_py_type = bool
            elif field_type == rf.TYPE_STRING:
                expected_py_type = str
            elif field_type == rf.TYPE_BYTES:
                expected_py_type = bytes
            elif field_type in {rf.TYPE_DOUBLE, rf.TYPE_FLOAT}:
                expected_py_type = float
            elif field_type in {rf.TYPE_INT32, rf.TYPE_INT64, rf.TYPE_FIXED64, rf.TYPE_FIXED32}:
                expected_py_type = int
            elif field_type in {rf.TYPE_UINT32, rf.TYPE_UINT64}:
                expected_py_type = int
            elif field_type in {rf.TYPE_SINT32, rf.TYPE_SINT64, rf.TYPE_SFIXED32, rf.TYPE_SFIXED64}:
                expected_py_type = int
            elif field_type == rf.TYPE_MESSAGE:
                expected_py_type = object
            elif field_type == rf.TYPE_GROUP:
                assert False, 'GROUP types not yet supported here'
            else:
                assert False, f'Unknown type {field_type}'

            if rf.label == rf.LABEL_REPEATED:
                for x in value:
                    assert isinstance(x, expected_py_type)
            else:
                assert isinstance(value, expected_py_type), (field, field_type)

        return fields

    def _set_side_effect(self, function_name, side_effect=None, **kwargs):
        if side_effect is None:
            kwargs.setdefault('status', 0)
            response_class = getattr(self.real_grpc_types, function_name + 'Response')
            kwargs = self._check_fields(response_class, **kwargs)
            side_effect = [response_class(**kwargs)]
        else:
            assert not kwargs, 'Do not use both side_effect and kwargs'

        request_object = object()
        getattr(self.patched_grpc_types, function_name + 'Request').side_effect = [request_object]
        getattr(self.patched_grpc_stub, function_name).side_effect = side_effect
        return request_object

    def _assert_call(self, function_name, request_object, metadata=None):
        func = getattr(self.patched_grpc_stub, function_name)
        func.assert_called_once_with(request_object, metadata=metadata)
        return getattr(self.patched_grpc_types, function_name + 'Request')

    # gRPC errors

    def test_server_unavailable(self):
        library_func = 'InitWithOptions'
        grpc_error = grpc.StatusCode.UNAVAILABLE
        expected_error_message = 'Failed to connect to server'
        self._set_side_effect(library_func, side_effect=MyRpcError(None, '', grpc_error=grpc_error))
        grpc_options = nifake.GrpcSessionOptions(object(), '', initialization_behavior=nifake.SessionInitializationBehavior.AUTO)
        interpreter = nifake._grpc_stub_interpreter.GrpcStubInterpreter(grpc_options)
        try:
            interpreter.init_with_options('dev1', False, False, '')
            assert False
        except nifake.Error as e:
            assert e.rpc_code == grpc_error
            assert e.description == expected_error_message
            assert str(e) == f'StatusCode.UNAVAILABLE: {expected_error_message}'

    def test_function_not_implemented(self):
        library_func = 'PoorlyNamedSimpleFunction'
        grpc_error = grpc.StatusCode.UNIMPLEMENTED
        expected_error_message_intro = 'This operation is not supported'
        self._set_side_effect(library_func, side_effect=MyRpcError(None, '', grpc_error=grpc_error))
        interpreter = self._get_initialized_stub_interpreter()
        try:
            interpreter.simple_function()
            assert False
        except nifake.Error as e:
            assert e.rpc_code == grpc_error
            assert e.description.startswith(expected_error_message_intro)
            assert str(e).startswith(f'StatusCode.UNIMPLEMENTED: {expected_error_message_intro}')

    # Methods

    def test_api_key_sent_to_init(self):
        library_func = 'InitWithOptions'
        expected_metadata = (('ni-api-key', nifake.MEASUREMENTLINK_23Q1_NIMI_PYTHON_API_KEY),)
        from session_pb2 import Session as GrpcSession
        grpc_session_object = GrpcSession(id=42, name='')
        response_object = self._set_side_effect(library_func, new_session_initialized=True, vi=grpc_session_object)
        init_behavior = nifake.SessionInitializationBehavior.AUTO
        grpc_options = nifake.GrpcSessionOptions(object(), '', initialization_behavior=init_behavior)
        interpreter = nifake._grpc_stub_interpreter.GrpcStubInterpreter(grpc_options)
        interpreter.init_with_options('dev1', False, False, '')
        self._assert_call(library_func, response_object, metadata=expected_metadata).assert_called_once_with(
            resource_name='dev1', id_query=False, reset_device=False, option_string='', session_name='', initialization_behavior=init_behavior,
        )

    def test_new_session_already_exists(self):
        library_func = 'InitWithOptions'
        session_name = 'existing_session'
        error_message = "Cannot initialize '" + session_name + "' when a session already exists."
        grpc_error = grpc.StatusCode.ALREADY_EXISTS
        self._set_side_effect(library_func, side_effect=MyRpcError(None, error_message, grpc_error=grpc_error))
        init_behavior = nifake.SessionInitializationBehavior.INITIALIZE_SERVER_SESSION
        grpc_options = nifake.GrpcSessionOptions(object(), session_name, initialization_behavior=init_behavior)
        interpreter = nifake._grpc_stub_interpreter.GrpcStubInterpreter(grpc_options)
        try:
            interpreter.init_with_options('dev1', False, False, '')
            assert False
        except nifake.Error as e:
            assert e.rpc_code == grpc_error
            assert e.description == error_message
            assert str(e) == f'StatusCode.ALREADY_EXISTS: {error_message}'

    def test_attach_to_non_existent_session(self):
        library_func = 'InitWithOptions'
        session_name = 'non_existent_session'
        error_message = "Cannot attach to '" + session_name + "' because a session has not been initialized."
        grpc_error = grpc.StatusCode.FAILED_PRECONDITION
        self._set_side_effect(library_func, side_effect=MyRpcError(None, error_message, grpc_error=grpc_error))
        init_behavior = nifake.SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION
        grpc_options = nifake.GrpcSessionOptions(object(), session_name, initialization_behavior=init_behavior)
        interpreter = nifake._grpc_stub_interpreter.GrpcStubInterpreter(grpc_options)
        try:
            interpreter.init_with_options('dev1', False, False, '')
            assert False
        except nifake.Error as e:
            assert e.rpc_code == grpc_error
            assert e.description == error_message
            assert str(e) == f'StatusCode.FAILED_PRECONDITION: {error_message}'

    @pytest.mark.timeout(2)
    def test_lock_unlock(self):
        # Note: this is purely local; don't set up any grpc mocks
        interpreter = self._get_initialized_stub_interpreter()
        interpreter.lock()
        interpreter.lock()  # ensure recurive locking is allowed
        interpreter.unlock()
        interpreter.unlock()

    def test_simple_function(self):
        library_func = 'PoorlyNamedSimpleFunction'
        response_object = self._set_side_effect(library_func)
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.simple_function() is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    def test_get_a_number(self):
        library_func = 'GetANumber'
        test_number = 16
        response_object = self._set_side_effect(library_func, a_number=test_number)
        interpreter = self._get_initialized_stub_interpreter()
        test_result = interpreter.get_a_number()
        assert isinstance(test_result, int)
        assert test_result == test_number
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    def test_one_input_function(self):
        library_func = 'OneInputFunction'
        test_number = 1
        response_object = self._set_side_effect(library_func)
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.one_input_function(test_number) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, a_number=test_number
        )

    def test_vi_int_64_function(self):
        library_func = 'Use64BitNumber'
        input_value = 2 ** 40
        output_value = 2 ** 41
        response_object = self._set_side_effect(library_func, output=output_value)
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.use64_bit_number(input_value) == output_value
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, input=input_value
        )

    def test_two_input_function(self):
        library_func = 'TwoInputFunction'
        test_number = 1.5
        test_string = 'test'
        response_object = self._set_side_effect(library_func)
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.two_input_function(test_number, test_string) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, a_number=test_number, a_string=test_string
        )

    def test_get_enum_value(self):
        library_func = 'GetEnumValue'
        test_number = 1
        test_turtle = nifake.Turtle.LEONARDO
        response_object = self._set_side_effect(library_func, a_quantity=test_number, a_turtle=test_turtle.value)
        interpreter = self._get_initialized_stub_interpreter()
        test_result_number, test_result_enum = interpreter.get_enum_value()
        assert isinstance(test_result_number, int)
        assert test_result_number == test_number
        assert isinstance(test_result_enum, nifake.Turtle)
        assert test_result_enum == test_turtle
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    def test_get_a_list_enums(self):
        library_func = 'EnumArrayOutputFunction'
        test_list = [1, 1, 0]
        response_object = self._set_side_effect(library_func, an_array=test_list)
        interpreter = self._get_initialized_stub_interpreter()
        test_result = interpreter.enum_array_output_function(len(test_list))
        assert len(test_list) == len(test_result)
        for expected_value, actual_value in zip(test_list, test_result):
            assert isinstance(actual_value, nifake.Turtle)
            assert actual_value.value == expected_value
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, number_of_elements=len(test_list)
        )

    def test_get_a_boolean(self):
        library_func = 'GetABoolean'
        response_object = self._set_side_effect(library_func, a_boolean=True)
        interpreter = self._get_initialized_stub_interpreter()
        test_result = interpreter.get_a_boolean()
        assert test_result is True
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    def test_get_a_list_booleans(self):
        library_func = 'BoolArrayOutputFunction'
        test_list = [True, True, False]
        response_object = self._set_side_effect(library_func, an_array=test_list)
        interpreter = self._get_initialized_stub_interpreter()
        test_result = interpreter.bool_array_output_function(len(test_list))
        assert len(test_list) == len(test_result)
        for expected_value, actual_value in zip(test_list, test_result):
            assert actual_value is expected_value
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, number_of_elements=len(test_list)
        )

    def test_single_point_read_nan(self):
        library_func = 'Read'
        test_maximum_time_s = 10.0
        test_reading = float('NaN')
        response_object = self._set_side_effect(library_func, reading=test_reading)
        interpreter = self._get_initialized_stub_interpreter()
        assert math.isnan(interpreter.read(test_maximum_time_s))
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, maximum_time=test_maximum_time_s
        )

    def test_fetch_waveform(self):
        library_func = 'FetchWaveform'
        expected_waveform_list = [1.0, 0.1, 42.0, 0.42]
        response_object = self._set_side_effect(library_func, waveform_data=expected_waveform_list, actual_number_of_samples=len(expected_waveform_list))
        interpreter = self._get_initialized_stub_interpreter()
        actual_waveform = interpreter.fetch_waveform(len(expected_waveform_list))
        assert isinstance(actual_waveform[0], float)
        assert len(actual_waveform) == len(expected_waveform_list)
        for i in range(len(actual_waveform)):
            assert actual_waveform[i] == expected_waveform_list[i]
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, number_of_samples=len(expected_waveform_list)
        )

    def test_fetch_waveform_into(self):
        interpreter = self._get_initialized_stub_interpreter()
        waveform = numpy.empty(4, numpy.float64)
        try:
            interpreter.fetch_waveform_into(waveform)
            assert False
        except NotImplementedError:
            pass

    def test_write_waveform(self):
        library_func = 'WriteWaveform'
        expected_waveform = [1.1, 2.2, 3.3, 4.4]
        expected_array = array.array('d', expected_waveform)
        interpreter = self._get_initialized_stub_interpreter()
        response_object = self._set_side_effect(library_func)
        assert interpreter.write_waveform(expected_array) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, waveform=expected_array
        )

    def test_write_waveform_numpy(self):
        waveform = numpy.array([1.1, 2.2, 3.3, 4.4], order='C')
        interpreter = self._get_initialized_stub_interpreter()
        try:
            interpreter.write_waveform_numpy(waveform)
            assert False
        except NotImplementedError:
            pass

    def test_write_waveform_numpy_complex128(self):
        library_func = 'WriteWaveformNumpyComplex128'
        waveform = numpy.array([1.0 + 2.0j, 3.0 + 4.0j, 5.0 + 6.0j], dtype=numpy.complex128)
        grpc_waveform = [
            nifake._grpc_stub_interpreter.grpc_complex_types.NIComplexNumber(real=value.real, imaginary=value.imag)
            for value in waveform.ravel()
        ]
        response_object = self._set_side_effect(library_func)
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.write_waveform_numpy_complex128(waveform) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            waveform_data_array=grpc_waveform,
        )

    def test_write_waveform_numpy_complex64(self):
        library_func = 'WriteWaveformNumpyComplex64'
        waveform = numpy.array([1.0 + 2.0j, 3.0 + 4.0j, 5.0 + 6.0j], dtype=numpy.complex64)
        grpc_waveform = [
            nifake._grpc_stub_interpreter.grpc_complex_types.NIComplexNumberF32(real=value.real, imaginary=value.imag)
            for value in waveform.ravel()
        ]
        response_object = self._set_side_effect(library_func)
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.write_waveform_numpy_complex64(waveform) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            waveform_data_array=grpc_waveform,
        )

    def test_write_waveform_numpy_complex_interleaved_i16(self):
        library_func = 'WriteWaveformNumpyComplexInterleavedI16'
        waveform = numpy.array([32767, 0, 123, -456], dtype=numpy.int16)
        assert len(waveform) % 2 == 0
        grpc_waveform = [
            nifake._grpc_stub_interpreter.grpc_complex_types.NIComplexI16(real=waveform[i], imaginary=waveform[i + 1])
            for i in range(0, len(waveform), 2)
        ]
        assert len(grpc_waveform) == len(waveform) // 2
        response_object = self._set_side_effect(library_func)
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.write_waveform_numpy_complex_interleaved_i16(waveform) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            waveform_data_array=grpc_waveform,
        )

    def test_function_with_3d_numpy_array_of_numpy_complex128_input_parameter(self):
        library_func = 'FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter'
        array_3d = numpy.array(
            [[[1.0 + 2.0j, 3.0 + 4.0j], [5.0 + 6.0j, 7.0 + 8.0j]], [[9.0 + 10.0j, 11.0 + 12.0j], [13.0 + 14.0j, 15.0 + 16.0j]]],
            dtype=numpy.complex128,
        )
        grpc_array = [
            nifake._grpc_stub_interpreter.grpc_complex_types.NIComplexNumber(real=value.real, imaginary=value.imag)
            for value in array_3d.ravel()
        ]
        response_object = self._set_side_effect(library_func)
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.function_with_3d_numpy_array_of_numpy_complex128_input_parameter(array_3d) is None
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            multidimensional_array=grpc_array,
        )

    def test_return_multiple_types(self):
        library_func = 'ReturnMultipleTypes'
        boolean_val = True
        int32_val = 32
        int64_val = 6000000000
        expected_enum_val = nifake.Turtle.LEONARDO
        enum_val = nifake._grpc_stub_interpreter.grpc_types.Turtle.TURTLE_LEONARDO
        float_val = 1.23
        expected_float_enum_val = nifake.FloatEnum.SIX_POINT_FIVE
        float_enum_val = nifake._grpc_stub_interpreter.grpc_types.FloatEnum.FLOAT_ENUM_SIX_POINT_FIVE
        raw_float_enum_val = 6.5
        array_val = [0.0, 1.0, 2.0]
        array_size = len(array_val)
        string_val = 'Testing is fun?'
        response_object = self._set_side_effect(
            library_func,
            a_boolean=boolean_val,
            an_int32=int32_val,
            an_int64=int64_val,
            an_int_enum=enum_val,
            a_float=float_val,
            a_float_enum_mapped=float_enum_val,
            a_float_enum_raw=raw_float_enum_val,
            an_array=array_val,
            a_string=string_val,
        )
        interpreter = self._get_initialized_stub_interpreter()
        result_boolean, result_int32, result_int64, result_enum, result_float, result_float_enum, result_array, result_string = interpreter.return_multiple_types(array_size)
        assert result_boolean == boolean_val
        assert isinstance(result_boolean, bool)
        assert result_int32 == int32_val
        assert isinstance(result_int32, int)
        assert result_int64 == int64_val
        assert isinstance(result_int64, int)
        assert result_enum == expected_enum_val
        assert isinstance(result_enum, nifake.Turtle)
        assert result_float == float_val
        assert isinstance(result_float, float)
        assert result_float_enum == expected_float_enum_val
        assert isinstance(result_float_enum, nifake.FloatEnum)
        assert result_array == array_val
        # assert `list` duck typing (in reality, it's a google._upb._message.RepeatedScalarContainer
        assert isinstance(result_array, collections.abc.Sequence)
        assert isinstance(result_array[0], float)
        assert result_string == string_val
        assert isinstance(result_string, str)
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, array_size=array_size
        )

    def test_multiple_array_types(self):
        library_func = 'MultipleArrayTypes'
        expected_output_array = [0.2, 0.4]
        expected_output_array_of_fixed_length = [-6.0, -7.0, -8.0]
        output_array_size = len(expected_output_array)
        input_array_of_integers = [1, 2]
        input_array_of_floats = [-1.0, -2.0]
        response_object = self._set_side_effect(
            library_func,
            output_array=expected_output_array,
            output_array_of_fixed_length=expected_output_array_of_fixed_length,
        )
        interpreter = self._get_initialized_stub_interpreter()
        output_array, output_array_of_fixed_length = interpreter.multiple_array_types(output_array_size, input_array_of_floats, input_array_of_integers)
        assert output_array == output_array
        assert expected_output_array_of_fixed_length == output_array_of_fixed_length
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            output_array_size=output_array_size,
            input_array_of_floats=input_array_of_floats,
            input_array_of_integers=input_array_of_integers,
        )

    def test_multiple_array_types_none_input(self):
        library_func = 'MultipleArrayTypes'
        expected_output_array = [0.2, 0.4]
        expected_output_array_of_fixed_length = [-6.0, -7.0, -8.0]
        output_array_size = len(expected_output_array)
        input_array_of_floats = [0.1, 0.2]
        response_object = self._set_side_effect(
            library_func,
            output_array=expected_output_array,
            output_array_of_fixed_length=expected_output_array_of_fixed_length,
        )
        interpreter = self._get_initialized_stub_interpreter()
        output_array, output_array_of_fixed_length = interpreter.multiple_array_types(output_array_size, input_array_of_floats, None)
        assert output_array == output_array
        assert expected_output_array_of_fixed_length == output_array_of_fixed_length
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            output_array_size=output_array_size,
            input_array_of_floats=input_array_of_floats,
            input_array_of_integers=None,
        )

    def test_multiple_arrays_same_size(self):
        library_func = 'MultipleArraysSameSize'
        input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
        input_array_of_floats2 = [0.410, 0.420, 0.430, 0.440]
        input_array_of_floats3 = [4.100, 4.200, 4.300, 4.400]
        input_array_of_floats4 = [41.00, 42.00, 43.00, 44.00]
        response_object = self._set_side_effect(library_func)
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.multiple_arrays_same_size(input_array_of_floats1, input_array_of_floats2, input_array_of_floats3, input_array_of_floats4) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            values1=input_array_of_floats1,
            values2=input_array_of_floats2,
            values3=input_array_of_floats3,
            values4=input_array_of_floats4,
        )

    def test_multiple_arrays_same_size_none_input(self):
        library_func = 'MultipleArraysSameSize'
        response_object = self._set_side_effect(library_func)
        input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.multiple_arrays_same_size(input_array_of_floats1, None, None, None) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            values1=input_array_of_floats1,
            values2=None,
            values3=None,
            values4=None,
        )

    def test_multiple_arrays_different_size(self):
        library_func = 'MultipleArraysDifferentSize'
        response_object = self._set_side_effect(library_func)
        values_array = [1.1, 2.2, 3.3]
        data_array = [10, 20, 30, 40, 50]
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.multiple_arrays_different_size(values_array, data_array) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            values_array=values_array,
            data_array=data_array,
        )

    def test_multiple_arrays_different_size_none_input(self):
        library_func = 'MultipleArraysDifferentSize'
        response_object = self._set_side_effect(library_func)
        values_array = [1.1, 2.2, 3.3]
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.multiple_arrays_different_size(values_array, None) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            values_array=values_array,
            data_array=None,
        )

    def test_mixed_ivi_dance_and_len_mechanism(self):
        library_func = 'MixedIviDanceAndLenMechanism'
        input_values = [1.1, 2.2, 3.3]
        expected_output = [4, 5]
        response_object = self._set_side_effect(library_func, output_array=expected_output)
        interpreter = self._get_initialized_stub_interpreter()
        result_array = interpreter.mixed_ivi_dance_and_len_mechanism(input_values)
        assert result_array == expected_output
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            input_values=input_values,
        )

    def test_multiple_arrays_same_size_wrong_size(self):
        library_func = 'MultipleArraysSameSize'
        # grpc-device server checks this server-side and errors with ::grpc::INVALID_ARGUMENT
        self._set_side_effect(library_func, side_effect=MyRpcError(
            None,
            'The sizes of linked repeated fields [values1, values2, values3, values4] do not match',
            grpc_error=grpc.StatusCode.INVALID_ARGUMENT,
        ))
        input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
        input_array_of_floats2 = [0.410, 0.420, 0.430]
        input_array_of_floats3 = [4.100, 4.200, 4.300, 4.400]
        input_array_of_floats4 = [41.00, 42.00, 43.00, 44.00]
        interpreter = self._get_initialized_stub_interpreter()
        try:
            assert interpreter.multiple_arrays_same_size(input_array_of_floats1, input_array_of_floats2, input_array_of_floats3, input_array_of_floats4) is None  # no outputs
            assert False
        except ValueError:
            pass

    def test_parameters_are_multiple_types(self):
        library_func = 'ParametersAreMultipleTypes'
        response_object = self._set_side_effect(library_func)
        boolean_val = True
        int32_val = 32
        int64_val = 6000000000
        enum_val = nifake.Turtle.LEONARDO
        float_val = 1.23
        float_enum_val = nifake.FloatEnum.SIX_POINT_FIVE
        string_val = 'Testing is fun?'
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.parameters_are_multiple_types(boolean_val, int32_val, int64_val, enum_val, float_val, float_enum_val, string_val) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            a_boolean=boolean_val,
            an_int32=int32_val,
            an_int64=int64_val,
            an_int_enum_raw=enum_val.value,
            a_float=float_val,
            a_float_enum_raw=float_enum_val.value,
            a_string=string_val,
        )

    def test_method_with_error(self):
        library_func = 'PoorlyNamedSimpleFunction'
        test_error_code = -42
        test_error_desc = 'The answer to the ultimate question'
        self._set_side_effect(library_func, side_effect=MyRpcError(test_error_code, test_error_desc))
        interpreter = self._get_initialized_stub_interpreter()
        try:
            assert interpreter.simple_function() is None  # no outputs
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc

    def test_call_not_enough_parameters_error(self):
        interpreter = self._get_initialized_stub_interpreter()
        try:
            assert interpreter.multiple_array_types(10) is None  # no outputs
            assert False
        except TypeError:
            pass

    def test_invalid_method_call_wrong_type_error(self):
        interpreter = self._get_initialized_stub_interpreter()
        try:
            assert interpreter.multiple_array_types('potato', [0.0, 0.1, 0.2]) is None  # no outputs
            assert False
        except TypeError:
            pass

    def test_method_with_warning(self):
        # We want to capture all of our warnings, not just the first one
        warnings.filterwarnings('always', category=nifake.DriverWarning)

        library_func = 'PoorlyNamedSimpleFunction'
        test_error_code = 42
        test_error_desc = 'The answer to the ultimate question, only positive'
        response_object = self._set_side_effect(library_func, status=test_error_code)
        error_response_object = self._set_side_effect('ErrorMessage', error_message=test_error_desc)
        interpreter = self._get_initialized_stub_interpreter()
        with warnings.catch_warnings(record=True) as w:
            assert interpreter.simple_function() is None  # no outputs
            assert len(w) == 1
            assert issubclass(w[0].category, nifake.DriverWarning)
            assert test_error_desc in str(w[0].message)
            assert f'Warning {test_error_code} occurred.' in str(w[0].message)
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)
        self._assert_call('ErrorMessage', error_response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, error_code=test_error_code
        )

    def test_read_with_warning(self):
        # We want to capture all of our warnings, not just the first one
        warnings.filterwarnings('always', category=nifake.DriverWarning)

        library_func = 'Read'
        test_maximum_time_s = 10.0
        test_reading = float('nan')
        test_error_code = 42
        test_error_desc = 'The answer to the ultimate question, only positive'
        response_object = self._set_side_effect(library_func, status=test_error_code, reading=test_reading)
        error_response_object = self._set_side_effect('ErrorMessage', error_message=test_error_desc)
        interpreter = self._get_initialized_stub_interpreter()
        with warnings.catch_warnings(record=True) as w:
            assert math.isnan(interpreter.read(test_maximum_time_s))
            assert len(w) == 1
            assert issubclass(w[0].category, nifake.DriverWarning)
            assert test_error_desc in str(w[0].message)
            assert f'Warning {test_error_code} occurred.' in str(w[0].message)
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, maximum_time=test_maximum_time_s
        )
        self._assert_call('ErrorMessage', error_response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, error_code=test_error_code
        )

    # Retrieving buffers and strings

    def test_get_a_string_of_fixed_maximum_size(self):
        library_func = 'GetAStringOfFixedMaximumSize'
        test_string = 'A string no larger than the max size of 256 allowed by the function.'
        response_object = self._set_side_effect(library_func, a_string=test_string)
        interpreter = self._get_initialized_stub_interpreter()
        returned_string = interpreter.get_a_string_of_fixed_maximum_size()
        assert returned_string == test_string
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    def test_return_a_number_and_a_string(self):
        library_func = 'ReturnANumberAndAString'
        test_string = 'this string'
        test_number = 13
        response_object = self._set_side_effect(library_func, a_string=test_string, a_number=test_number)
        interpreter = self._get_initialized_stub_interpreter()
        returned_number, returned_string = interpreter.return_a_number_and_a_string()
        assert returned_string == test_string
        assert returned_number == test_number
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    def test_get_an_ivi_dance_char_array(self):
        library_func = 'GetAnIviDanceCharArray'
        string_val = 'Testing is fun?'
        response_object = self._set_side_effect(library_func, char_array=string_val)
        interpreter = self._get_initialized_stub_interpreter()
        result_string = interpreter.get_an_ivi_dance_char_array()
        assert result_string == string_val
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    def test_get_string_ivi_dance_error(self):
        library_func = 'GetAttributeViString'
        read_write_string_attribute_id = 1000002
        test_error_code = -1234
        test_error_desc = 'ascending order'
        self._set_side_effect(library_func, side_effect=MyRpcError(test_error_code, test_error_desc))
        interpreter = self._get_initialized_stub_interpreter()
        try:
            assert interpreter.get_attribute_vi_string('', read_write_string_attribute_id) is None  # no outputs
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc

    def test_get_an_ivi_dance_with_a_twist_string(self):
        library_func = 'GetAnIviDanceWithATwistString'
        string_val = 'Testing is fun?'
        response_object = self._set_side_effect(library_func, a_string=string_val, actual_size=len(string_val))
        interpreter = self._get_initialized_stub_interpreter()
        result_string = interpreter.get_an_ivi_dance_with_a_twist_string()
        assert result_string == string_val
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    def test_get_array_using_ivi_dance(self):
        library_func = 'GetArrayUsingIviDance'
        response_object = self._set_side_effect(library_func, array_out=[1.1, 2.2])
        interpreter = self._get_initialized_stub_interpreter()
        result_array = interpreter.get_array_using_ivi_dance()
        assert result_array == [1.1, 2.2]
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    # Attributes

    def test_get_attribute_int32(self):
        library_func = 'GetAttributeViInt32'
        attribute_id = 1000004
        test_number = 3
        response_object = self._set_side_effect(library_func, attribute_value=test_number)
        interpreter = self._get_initialized_stub_interpreter()
        attr_int = interpreter.get_attribute_vi_int32('', attribute_id)
        assert attr_int == test_number
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, channel_name='', attribute_id=attribute_id
        )

    def test_set_attribute_int32(self):
        library_func = 'SetAttributeViInt32'
        response_object = self._set_side_effect(library_func)
        attribute_id = 1000004
        test_number = -10
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.set_attribute_vi_int32('', attribute_id, test_number) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            channel_name='',
            attribute_id=attribute_id,
            attribute_value_raw=test_number,
        )

    def test_get_attribute_real64(self):
        library_func = 'GetAttributeViReal64'
        attribute_id = 1000001
        test_number = 1.5
        response_object = self._set_side_effect(library_func, attribute_value=test_number)
        interpreter = self._get_initialized_stub_interpreter()
        attr_double = interpreter.get_attribute_vi_real64('', attribute_id)
        assert attr_double == test_number
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, channel_name='', attribute_id=attribute_id
        )

    def test_set_attribute_real64(self):
        library_func = 'SetAttributeViReal64'
        response_object = self._set_side_effect(library_func)
        attribute_id = 1000001
        test_number = 10.1
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.set_attribute_vi_real64('', attribute_id, test_number) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            channel_name='',
            attribute_id=attribute_id,
            attribute_value_raw=test_number,
        )

    def test_get_attribute_string(self):
        library_func = 'GetAttributeViString'
        attribute_id = 1000002
        string = 'Testing is fun?'
        response_object = self._set_side_effect(library_func, attribute_value=string)
        interpreter = self._get_initialized_stub_interpreter()
        attr_string = interpreter.get_attribute_vi_string('', attribute_id)
        assert attr_string == string
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, channel_name='', attribute_id=attribute_id
        )

    def test_set_attribute_string(self):
        library_func = 'SetAttributeViString'
        response_object = self._set_side_effect(library_func)
        attribute_id = 1000002
        attrib_string = 'This is test string'
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.set_attribute_vi_string('', attribute_id, attrib_string) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            channel_name='',
            attribute_id=attribute_id,
            attribute_value_raw='This is test string',
        )

    def test_get_attribute_boolean(self):
        library_func = 'GetAttributeViBoolean'
        attribute_id = 1000000
        response_object = self._set_side_effect(library_func, attribute_value=True)
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.get_attribute_vi_boolean('', attribute_id)
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, channel_name='', attribute_id=attribute_id
        )

    def test_set_attribute_boolean(self):
        library_func = 'SetAttributeViBoolean'
        response_object = self._set_side_effect(library_func)
        attribute_id = 1000000
        attrib_bool = True
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.set_attribute_vi_boolean('', attribute_id, attrib_bool) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, channel_name='', attribute_id=attribute_id, attribute_value=True
        )

    def test_get_attribute_int64(self):
        library_func = 'GetAttributeViInt64'
        attribute_id = 1000006
        test_number = 6000000000
        response_object = self._set_side_effect(library_func, attribute_value=test_number)
        interpreter = self._get_initialized_stub_interpreter()
        attr_int = interpreter.get_attribute_vi_int64('', attribute_id)
        assert attr_int == test_number
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, channel_name='', attribute_id=attribute_id
        )

    def test_set_attribute_int64(self):
        library_func = 'SetAttributeViInt64'
        response_object = self._set_side_effect(library_func)
        attribute_id = 1000006
        test_number = -6000000000
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.set_attribute_vi_int64('', attribute_id, test_number) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            channel_name='',
            attribute_id=attribute_id,
            attribute_value_raw=test_number,
        )

    # Error descriptions

    def test_error_message_returns_error(self):
        # We want to capture all of our warnings, not just the first one
        warnings.filterwarnings('always', category=nifake.DriverWarning)

        test_error_code = 42
        library_func = 'PoorlyNamedSimpleFunction'
        response_object = self._set_side_effect(library_func, status=test_error_code)
        error_msg_response_object = self._set_side_effect('ErrorMessage', side_effect=MyRpcError(-3, 'ErrorMessage failed'))
        interpreter = self._get_initialized_stub_interpreter()
        with warnings.catch_warnings(record=True) as w:
            assert interpreter.simple_function() is None  # no outputs
            assert len(w) == 1
            assert issubclass(w[0].category, nifake.DriverWarning)
            assert 'Failed to retrieve error description.' in str(w[0].message)
            assert f'Warning {test_error_code} occurred.' in str(w[0].message)
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)
        self._assert_call('ErrorMessage', error_msg_response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST, error_code=test_error_code)

    # Custom types

    def test_set_custom_type(self):
        library_func = 'SetCustomType'
        response_object = self._set_side_effect(library_func)
        cs = nifake.CustomStruct(struct_int=42, struct_double=4.2)
        grpc_cs = nifake._grpc_stub_interpreter.grpc_types.FakeCustomStruct(struct_int=42, struct_double=4.2)
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.set_custom_type(cs) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, cs=grpc_cs
        )

    def test_get_custom_type(self):
        library_func = 'GetCustomType'
        expected_cs = nifake.CustomStruct(struct_int=42, struct_double=4.2)
        grpc_cs = nifake._grpc_stub_interpreter.grpc_types.FakeCustomStruct(struct_int=42, struct_double=4.2)
        response_object = self._set_side_effect(library_func, cs=grpc_cs)
        interpreter = self._get_initialized_stub_interpreter()
        cs = interpreter.get_custom_type()
        assert cs.struct_int == expected_cs.struct_int
        assert cs.struct_double == expected_cs.struct_double
        assert isinstance(cs, type(expected_cs))
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    def test_set_custom_type_array(self):
        library_func = 'SetCustomTypeArray'
        response_object = self._set_side_effect(library_func)
        cs = [nifake.CustomStruct(struct_int=42, struct_double=4.2), nifake.CustomStruct(struct_int=43, struct_double=4.3), nifake.CustomStruct(struct_int=42, struct_double=4.3)]
        grpc_cs = [nifake._grpc_stub_interpreter.grpc_types.FakeCustomStruct(struct_int=42, struct_double=4.2), nifake._grpc_stub_interpreter.grpc_types.FakeCustomStruct(struct_int=43, struct_double=4.3), nifake._grpc_stub_interpreter.grpc_types.FakeCustomStruct(struct_int=42, struct_double=4.3)]
        interpreter = self._get_initialized_stub_interpreter()
        assert interpreter.set_custom_type_array(cs) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, cs=grpc_cs
        )

    def test_get_custom_type_array(self):
        library_func = 'GetCustomTypeArray'
        cs = [nifake.CustomStruct(struct_int=42, struct_double=4.2), nifake.CustomStruct(struct_int=43, struct_double=4.3), nifake.CustomStruct(struct_int=42, struct_double=4.3)]
        grpc_cs = [nifake._grpc_stub_interpreter.grpc_types.FakeCustomStruct(struct_int=42, struct_double=4.2), nifake._grpc_stub_interpreter.grpc_types.FakeCustomStruct(struct_int=43, struct_double=4.3), nifake._grpc_stub_interpreter.grpc_types.FakeCustomStruct(struct_int=42, struct_double=4.3)]
        response_object = self._set_side_effect(library_func, cs=grpc_cs)
        interpreter = self._get_initialized_stub_interpreter()
        cs_test = interpreter.get_custom_type_array(len(cs))
        assert len(cs_test) == len(cs)
        for actual, expected in zip(cs_test, cs):
            assert actual.struct_int == expected.struct_int
            assert actual.struct_double == expected.struct_double
            assert isinstance(actual, type(expected))
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, number_of_elements=len(cs)
        )

    def test_get_custom_type_typedef(self):
        library_func = 'CustomNestedStructRoundtrip'
        csnt = nifake.CustomStructNestedTypedef(
            struct_custom_struct=nifake.CustomStruct(struct_int=43, struct_double=4.3),
            struct_custom_struct_typedef=nifake.CustomStructTypedef(struct_int=44, struct_double=4.4)
        )
        grpc_csnt = nifake._grpc_stub_interpreter.grpc_types.CustomStructNestedTypedef(
            struct_custom_struct=nifake._grpc_stub_interpreter.grpc_types.FakeCustomStruct(struct_int=43, struct_double=4.3),
            struct_custom_struct_typedef=nifake._grpc_stub_interpreter.grpc_types.CustomStructTypedef(struct_int=44, struct_double=4.4)
        )
        response_object = self._set_side_effect(library_func, nested_custom_type_out=grpc_csnt)
        interpreter = self._get_initialized_stub_interpreter()
        csnt_test = interpreter.custom_nested_struct_roundtrip(nested_custom_type_in=csnt)
        assert csnt_test.struct_custom_struct.struct_int == csnt.struct_custom_struct.struct_int
        assert csnt_test.struct_custom_struct.struct_double == csnt.struct_custom_struct.struct_double
        assert csnt_test.struct_custom_struct_typedef.struct_int == csnt.struct_custom_struct_typedef.struct_int
        assert csnt_test.struct_custom_struct_typedef.struct_double == csnt.struct_custom_struct_typedef.struct_double
        assert isinstance(csnt_test.struct_custom_struct, type(csnt.struct_custom_struct))
        assert isinstance(csnt_test.struct_custom_struct_typedef, type(csnt.struct_custom_struct_typedef))
        assert isinstance(csnt_test, type(csnt))
        request_object = self._assert_call(library_func, response_object)
        request_object.assert_called_once()
        call = request_object.call_args_list[0]
        assert len(call) == 2
        call_args, call_kwargs = call
        assert not call_args
        assert 'nested_custom_type_in' in call_kwargs
        sent_csnt = call_kwargs['nested_custom_type_in']
        assert sent_csnt.struct_custom_struct.struct_int == grpc_csnt.struct_custom_struct.struct_int
        assert sent_csnt.struct_custom_struct.struct_double == grpc_csnt.struct_custom_struct.struct_double
        assert sent_csnt.struct_custom_struct_typedef.struct_int == grpc_csnt.struct_custom_struct_typedef.struct_int
        assert sent_csnt.struct_custom_struct_typedef.struct_double == grpc_csnt.struct_custom_struct_typedef.struct_double
        assert isinstance(sent_csnt.struct_custom_struct, type(grpc_csnt.struct_custom_struct))
        assert isinstance(sent_csnt.struct_custom_struct_typedef, type(grpc_csnt.struct_custom_struct_typedef))
        assert isinstance(sent_csnt, type(grpc_csnt))

    def test_get_cal_date_time(self):
        library_func = 'GetCalDateAndTime'
        month = 12
        day = 30
        year = 1988
        hour = 10
        minute = 15
        response_object = self._set_side_effect(
            library_func, month=month, day=day, year=year, hour=hour, minute=minute
        )
        interpreter = self._get_initialized_stub_interpreter()
        last_cal = interpreter.get_cal_date_and_time(0)
        assert (month, day, year, hour, minute) == last_cal
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, cal_type=0
        )

    # Import/Export functions

    def test_import_attribute_configuration_buffer(self):
        library_func = 'ImportAttributeConfigurationBuffer'
        configuration = b'abcd'
        interpreter = self._get_initialized_stub_interpreter()
        response_object = self._set_side_effect(library_func)
        assert interpreter.import_attribute_configuration_buffer(configuration) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, configuration=configuration
        )

    def test_missing_function(self):
        library_func = 'Abort'
        self._set_side_effect(library_func, side_effect=MyRpcError(None, 'not found', grpc_error=grpc.StatusCode.NOT_FOUND))
        interpreter = self._get_initialized_stub_interpreter()
        try:
            interpreter.abort()
            assert False
        except nifake.errors.DriverTooOldError as e:
            message = e.args[0]
            assert message == 'A function was not found in the NI-FAKE runtime. Please visit http://www.ni.com/downloads/drivers/ to download a newer version and install it.'
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/nifake/unit_tests/test_library_interpreter.py sha256=a4286dfd1f62fd504566c117bc95f8b60c3a994c92c414b169ca76ae85b9f332 bytes=67532 -->
## FILE: generated/nifake/nifake/unit_tests/test_library_interpreter.py

- repository: `ni/nimi-python`
- source_path: `generated/nifake/nifake/unit_tests/test_library_interpreter.py`
- sha256: `a4286dfd1f62fd504566c117bc95f8b60c3a994c92c414b169ca76ae85b9f332`
- bytes: 67532

````python
import array
import ctypes
import math
import nifake
import nifake.errors
import numpy
import pytest
import warnings

from unittest.mock import call
from unittest.mock import MagicMock
from unittest.mock import patch

import _matchers
import _mock_helper

SESSION_NUM_FOR_TEST = 42


class TestLibraryInterpreter:

    class PatchedLibrary(nifake._library.Library):
        def __init__(self, ctypes_library):
            super().__init__(ctypes_library)

            for f in dir(self):
                if f.startswith("niFake_") and not f.endswith("_cfunc"):
                    setattr(self, f, MagicMock())

    def setup_method(self, method):
        self.patched_library = self.PatchedLibrary(None)
        self.patched_library_singleton_get = patch('nifake._library_interpreter._library_singleton.get', return_value=self.patched_library)
        self.patched_library_singleton_get.start()

        self.side_effects_helper = _mock_helper.SideEffectsHelper()
        self.side_effects_helper.set_side_effects_and_return_values(self.patched_library)
        self.patched_library.niFake_SetRuntimeEnvironment.side_effect = self.side_effects_helper.niFake_SetRuntimeEnvironment

        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        self.get_ctypes_pointer_for_buffer_side_effect_items = []

    def teardown_method(self, method):
        self.patched_library_singleton_get.stop()

    def get_initialized_library_interpreter(self):
        interpreter = nifake._library_interpreter.LibraryInterpreter('windows-1251')
        interpreter._vi = SESSION_NUM_FOR_TEST
        return interpreter

    def niFake_read_warning(self, vi, maximum_time, reading):  # noqa: N802
        reading.contents.value = self.reading
        return self.error_code_return

    def get_ctypes_pointer_for_buffer_side_effect(self, value, library_type=None):
        ret_val = self.get_ctypes_pointer_for_buffer_side_effect_items[self.get_ctypes_pointer_for_buffer_side_effect_count]
        self.get_ctypes_pointer_for_buffer_side_effect_count += 1
        return ret_val

    # Methods

    def test_simple_function(self):
        self.patched_library.niFake_PoorlyNamedSimpleFunction.side_effect = self.side_effects_helper.niFake_PoorlyNamedSimpleFunction
        interpreter = self.get_initialized_library_interpreter()
        interpreter.simple_function()
        self.patched_library.niFake_PoorlyNamedSimpleFunction.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

    def test_get_a_number(self):
        test_number = 16
        self.patched_library.niFake_GetANumber.side_effect = self.side_effects_helper.niFake_GetANumber
        self.side_effects_helper['GetANumber']['aNumber'] = test_number
        interpreter = self.get_initialized_library_interpreter()
        test_result = interpreter.get_a_number()
        assert isinstance(test_result, int)
        assert test_result == test_number
        self.patched_library.niFake_GetANumber.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt16PointerMatcher())

    def test_one_input_function(self):
        test_number = 1
        self.patched_library.niFake_OneInputFunction.side_effect = self.side_effects_helper.niFake_OneInputFunction
        interpreter = self.get_initialized_library_interpreter()
        interpreter.one_input_function(test_number)
        self.patched_library.niFake_OneInputFunction.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(test_number))

    def test_vi_int_64_function(self):
        input_value = 2 ** 40
        output_value = 2 ** 41
        self.patched_library.niFake_Use64BitNumber.side_effect = self.side_effects_helper.niFake_Use64BitNumber
        self.side_effects_helper['Use64BitNumber']['output'] = output_value
        interpreter = self.get_initialized_library_interpreter()
        assert interpreter.use64_bit_number(input_value) == output_value
        self.patched_library.niFake_Use64BitNumber.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt64Matcher(input_value), _matchers.ViInt64PointerMatcher())

    def test_two_input_function(self):
        test_number = 1.5
        test_string = 'test'
        self.patched_library.niFake_TwoInputFunction.side_effect = self.side_effects_helper.niFake_TwoInputFunction
        interpreter = self.get_initialized_library_interpreter()
        interpreter.two_input_function(test_number, test_string)
        self.patched_library.niFake_TwoInputFunction.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViReal64Matcher(test_number), _matchers.ViStringMatcher(test_string))

    def test_get_enum_value(self):
        test_number = 1
        test_turtle = nifake.Turtle.LEONARDO
        self.patched_library.niFake_GetEnumValue.side_effect = self.side_effects_helper.niFake_GetEnumValue
        self.side_effects_helper['GetEnumValue']['aQuantity'] = test_number
        self.side_effects_helper['GetEnumValue']['aTurtle'] = 0
        interpreter = self.get_initialized_library_interpreter()
        test_result_number, test_result_enum = interpreter.get_enum_value()
        assert isinstance(test_result_number, int)
        assert test_result_number == test_number
        assert isinstance(test_result_enum, nifake.Turtle)
        assert test_result_enum == test_turtle
        self.patched_library.niFake_GetEnumValue.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32PointerMatcher(), _matchers.ViInt16PointerMatcher())

    def test_get_a_list_enums(self):
        self.patched_library.niFake_EnumArrayOutputFunction.side_effect = self.side_effects_helper.niFake_EnumArrayOutputFunction
        test_list = [1, 1, 0]
        self.side_effects_helper['EnumArrayOutputFunction']['anArray'] = test_list
        interpreter = self.get_initialized_library_interpreter()
        test_result = interpreter.enum_array_output_function(len(test_list))
        assert len(test_list) == len(test_result)
        for expected_value, actual_value in zip(test_list, test_result):
            assert isinstance(actual_value, nifake.Turtle)
            assert actual_value.value == expected_value
        self.patched_library.niFake_EnumArrayOutputFunction.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(test_list)), _matchers.ViInt16BufferMatcher(len(test_list)))

    def test_get_a_boolean(self):
        self.patched_library.niFake_GetABoolean.side_effect = self.side_effects_helper.niFake_GetABoolean
        self.side_effects_helper['GetABoolean']['aBoolean'] = 1
        interpreter = self.get_initialized_library_interpreter()
        test_result = interpreter.get_a_boolean()
        assert isinstance(test_result, bool)
        assert test_result
        self.patched_library.niFake_GetABoolean.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViBooleanPointerMatcher())

    def test_get_a_list_booleans(self):
        self.patched_library.niFake_BoolArrayOutputFunction.side_effect = self.side_effects_helper.niFake_BoolArrayOutputFunction
        test_list = [1, 1, 0]
        self.side_effects_helper['BoolArrayOutputFunction']['anArray'] = test_list
        interpreter = self.get_initialized_library_interpreter()
        test_result = interpreter.bool_array_output_function(len(test_list))
        assert len(test_list) == len(test_result)
        for expected_value, actual_value in zip(test_list, test_result):
            assert isinstance(actual_value, bool)
            assert actual_value == bool(expected_value)
        self.patched_library.niFake_BoolArrayOutputFunction.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(test_list)), _matchers.ViBooleanBufferMatcher(len(test_list)))

    def test_single_point_read_nan(self):
        test_maximum_time_s = 10.0
        test_reading = float('NaN')
        self.patched_library.niFake_Read.side_effect = self.side_effects_helper.niFake_Read
        self.side_effects_helper['Read']['reading'] = test_reading
        interpreter = self.get_initialized_library_interpreter()
        assert math.isnan(interpreter.read(test_maximum_time_s))

    def test_fetch_waveform(self):
        expected_waveform_list = [1.0, 0.1, 42, .42]
        self.patched_library.niFake_FetchWaveform.side_effect = self.side_effects_helper.niFake_FetchWaveform
        self.side_effects_helper['FetchWaveform']['waveformData'] = expected_waveform_list
        self.side_effects_helper['FetchWaveform']['actualNumberOfSamples'] = len(expected_waveform_list)

        # Because we are mocking _get_ctypes_pointer_for_buffer() we don't end up using the array allocated in the function call. Instead, we will allocate the arrays here
        # and have the mock return them. These are the ones that are actually filled in by the function.
        expected_waveform = array.array('d', [0]) * len(expected_waveform_list)
        expected_waveform_ctypes = ctypes.cast(expected_waveform.buffer_info()[0], ctypes.POINTER(nifake._visatype.ViReal64 * len(expected_waveform_list)))

        interpreter = self.get_initialized_library_interpreter()
        self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_waveform_ctypes]
        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        self.patched_library.niFake_WriteWaveform.side_effect = self.side_effects_helper.niFake_WriteWaveform
        with patch('nifake._library_interpreter._get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
            # Because we have mocked away _get_ctypes_pointer_for_buffer(), we ignore the return values here and look at our already allocated arrays to make
            # sure they are filled in correctly
            interpreter.fetch_waveform(len(expected_waveform_list))
        assert isinstance(expected_waveform[0], float)
        assert len(expected_waveform) == len(expected_waveform_list)
        for i in range(len(expected_waveform)):
            assert expected_waveform[i] == expected_waveform_list[i]
        self.patched_library.niFake_FetchWaveform.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(expected_waveform)), _matchers.ViReal64BufferMatcher(expected_waveform), _matchers.ViInt32PointerMatcher())

    def test_fetch_waveform_into(self):
        expected_waveform = [1.0, 0.1, 42, .42]
        self.patched_library.niFake_FetchWaveform.side_effect = self.side_effects_helper.niFake_FetchWaveform
        self.side_effects_helper['FetchWaveform']['waveformData'] = expected_waveform
        self.side_effects_helper['FetchWaveform']['actualNumberOfSamples'] = len(expected_waveform)
        interpreter = self.get_initialized_library_interpreter()
        waveform = numpy.empty(len(expected_waveform), numpy.float64)
        interpreter.fetch_waveform_into(waveform)
        assert numpy.array_equal(waveform, expected_waveform)
        self.patched_library.niFake_FetchWaveform.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(expected_waveform)), _matchers.ViReal64BufferMatcher(expected_waveform), _matchers.ViInt32PointerMatcher())

    def test_write_waveform(self):
        expected_waveform = [1.1, 2.2, 3.3, 4.4]
        expected_array = array.array('d', expected_waveform)
        interpreter = self.get_initialized_library_interpreter()
        self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_waveform]
        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        self.patched_library.niFake_WriteWaveform.side_effect = self.side_effects_helper.niFake_WriteWaveform
        with patch('nifake._library_interpreter._get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
            interpreter.write_waveform(expected_array)
        self.patched_library.niFake_WriteWaveform.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(expected_waveform)), _matchers.ViReal64BufferMatcher(expected_array))

    def test_write_waveform_numpy(self):
        expected_waveform = numpy.array([1.1, 2.2, 3.3, 4.4], order='C')
        self.patched_library.niFake_WriteWaveform.side_effect = self.side_effects_helper.niFake_WriteWaveform
        interpreter = self.get_initialized_library_interpreter()
        interpreter.write_waveform_numpy(expected_waveform)
        self.patched_library.niFake_WriteWaveform.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(expected_waveform)), _matchers.ViReal64BufferMatcher(expected_waveform))

    def test_return_multiple_types(self):
        self.patched_library.niFake_ReturnMultipleTypes.side_effect = self.side_effects_helper.niFake_ReturnMultipleTypes
        boolean_val = True
        int32_val = 32
        int64_val = 6000000000
        enum_val = nifake.Turtle.LEONARDO
        float_val = 1.23
        float_enum_val = nifake.FloatEnum.SIX_POINT_FIVE
        array_val = [0, 1, 2]
        array_size = len(array_val)
        string_val = 'Testing is fun?'
        self.side_effects_helper['ReturnMultipleTypes']['return'] = len(string_val)
        self.side_effects_helper['ReturnMultipleTypes']['aBoolean'] = boolean_val
        self.side_effects_helper['ReturnMultipleTypes']['anInt32'] = int32_val
        self.side_effects_helper['ReturnMultipleTypes']['anInt64'] = int64_val
        self.side_effects_helper['ReturnMultipleTypes']['anIntEnum'] = enum_val.value
        self.side_effects_helper['ReturnMultipleTypes']['aFloat'] = float_val
        self.side_effects_helper['ReturnMultipleTypes']['aFloatEnum'] = float_enum_val.value
        self.side_effects_helper['ReturnMultipleTypes']['anArray'] = array_val
        self.side_effects_helper['ReturnMultipleTypes']['aString'] = string_val
        self.side_effects_helper['ReturnMultipleTypes']['return'] = 0
        interpreter = self.get_initialized_library_interpreter()
        result_boolean, result_int32, result_int64, result_enum, result_float, result_float_enum, result_array, result_string = interpreter.return_multiple_types(array_size)
        assert result_boolean == boolean_val
        assert isinstance(result_boolean, bool)
        assert result_int32 == int32_val
        assert isinstance(result_int32, int)
        assert result_int64 == int64_val
        assert isinstance(result_int64, int)
        assert result_enum == enum_val
        assert isinstance(result_enum, nifake.Turtle)
        assert result_float == float_val
        assert isinstance(result_float, float)
        assert result_float_enum == float_enum_val
        assert isinstance(result_float_enum, nifake.FloatEnum)
        assert result_array == array_val
        assert isinstance(result_array, list)
        assert isinstance(result_array[0], float)
        assert result_string == string_val
        assert isinstance(result_string, str)
        assert self.patched_library.niFake_ReturnMultipleTypes.call_count == 2

    def test_multiple_array_types(self):
        self.patched_library.niFake_MultipleArrayTypes.side_effect = self.side_effects_helper.niFake_MultipleArrayTypes
        expected_output_array = [0.2, 0.4]
        expected_output_array_of_fixed_length = [-6, -7, -8]
        output_array_size = len(expected_output_array)
        input_array_of_integers = [1, 2]
        input_array_of_floats = [-1.0, -2.0]
        self.side_effects_helper['MultipleArrayTypes']['outputArray'] = expected_output_array
        self.side_effects_helper['MultipleArrayTypes']['outputArrayOfFixedLength'] = expected_output_array_of_fixed_length
        interpreter = self.get_initialized_library_interpreter()
        output_array, output_array_of_fixed_length = interpreter.multiple_array_types(output_array_size, input_array_of_floats, input_array_of_integers)
        assert output_array == output_array
        assert expected_output_array_of_fixed_length == output_array_of_fixed_length
        self.patched_library.niFake_MultipleArrayTypes.assert_called_once_with(
            _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
            _matchers.ViInt32Matcher(output_array_size),
            _matchers.ViReal64BufferMatcher(output_array_size),
            _matchers.ViReal64BufferMatcher(len(expected_output_array_of_fixed_length)),
            _matchers.ViInt32Matcher(len(input_array_of_integers)),
            _matchers.ViReal64BufferMatcher(input_array_of_floats),
            _matchers.ViInt16BufferMatcher(input_array_of_integers),
        )

    def test_multiple_array_types_none_input(self):
        self.patched_library.niFake_MultipleArrayTypes.side_effect = self.side_effects_helper.niFake_MultipleArrayTypes
        expected_output_array = [0.2, 0.4]
        expected_output_array_of_fixed_length = [-6, -7, -8]
        output_array_size = len(expected_output_array)
        input_array_of_floats = [0.1, 0.2]
        self.side_effects_helper['MultipleArrayTypes']['outputArray'] = expected_output_array
        self.side_effects_helper['MultipleArrayTypes']['outputArrayOfFixedLength'] = expected_output_array_of_fixed_length
        interpreter = self.get_initialized_library_interpreter()
        output_array, output_array_of_fixed_length = interpreter.multiple_array_types(output_array_size, input_array_of_floats, None)
        assert output_array == output_array
        assert expected_output_array_of_fixed_length == output_array_of_fixed_length
        self.patched_library.niFake_MultipleArrayTypes.assert_called_once_with(
            _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
            _matchers.ViInt32Matcher(output_array_size),
            _matchers.ViReal64BufferMatcher(output_array_size),
            _matchers.ViReal64BufferMatcher(len(expected_output_array_of_fixed_length)),
            _matchers.ViInt32Matcher(len(input_array_of_floats)),
            _matchers.ViReal64BufferMatcher(input_array_of_floats),
            None
        )

    def test_multiple_arrays_same_size(self):
        self.patched_library.niFake_MultipleArraysSameSize.side_effect = self.side_effects_helper.niFake_MultipleArraysSameSize
        input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
        input_array_of_floats2 = [0.410, 0.420, 0.430, 0.440]
        input_array_of_floats3 = [4.100, 4.200, 4.300, 4.400]
        input_array_of_floats4 = [41.00, 42.00, 43.00, 44.00]
        interpreter = self.get_initialized_library_interpreter()
        interpreter.multiple_arrays_same_size(input_array_of_floats1, input_array_of_floats2, input_array_of_floats3, input_array_of_floats4)
        self.patched_library.niFake_MultipleArraysSameSize.assert_called_once_with(
            _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
            _matchers.ViReal64BufferMatcher(input_array_of_floats1),
            _matchers.ViReal64BufferMatcher(input_array_of_floats2),
            _matchers.ViReal64BufferMatcher(input_array_of_floats3),
            _matchers.ViReal64BufferMatcher(input_array_of_floats4),
            _matchers.ViInt32Matcher(len(input_array_of_floats1)),
        )

    def test_multiple_arrays_same_size_none_input(self):
        self.patched_library.niFake_MultipleArraysSameSize.side_effect = self.side_effects_helper.niFake_MultipleArraysSameSize
        input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
        interpreter = self.get_initialized_library_interpreter()
        interpreter.multiple_arrays_same_size(input_array_of_floats1, None, None, None)
        self.patched_library.niFake_MultipleArraysSameSize.assert_called_once_with(
            _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
            _matchers.ViReal64BufferMatcher(input_array_of_floats1),
            None,
            None,
            None,
            _matchers.ViInt32Matcher(len(input_array_of_floats1)),
        )

    def test_multiple_arrays_different_size(self):
        self.patched_library.niFake_MultipleArraysDifferentSize.side_effect = self.side_effects_helper.niFake_MultipleArraysDifferentSize
        values_array = [1.1, 2.2, 3.3]
        data_array = [10, 20, 30, 40, 50]
        interpreter = self.get_initialized_library_interpreter()
        interpreter.multiple_arrays_different_size(values_array, data_array)
        self.patched_library.niFake_MultipleArraysDifferentSize.assert_called_once_with(
            _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
            _matchers.ViReal64BufferMatcher(values_array),
            _matchers.ViInt32Matcher(len(values_array)),
            _matchers.ViInt32BufferMatcher(data_array),
            _matchers.ViInt32Matcher(len(data_array)),
        )

    def test_multiple_arrays_different_size_none_input(self):
        self.patched_library.niFake_MultipleArraysDifferentSize.side_effect = self.side_effects_helper.niFake_MultipleArraysDifferentSize
        values_array = [1.1, 2.2, 3.3]
        interpreter = self.get_initialized_library_interpreter()
        interpreter.multiple_arrays_different_size(values_array, None)
        self.patched_library.niFake_MultipleArraysDifferentSize.assert_called_once_with(
            _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
            _matchers.ViReal64BufferMatcher(values_array),
            _matchers.ViInt32Matcher(len(values_array)),
            None,
            _matchers.ViInt32Matcher(0),
        )

    def test_mixed_ivi_dance_and_len_mechanism(self):
        self.patched_library.niFake_MixedIviDanceAndLenMechanism.side_effect = self.side_effects_helper.niFake_MixedIviDanceAndLenMechanism
        expected_output = [4, 5]
        self.side_effects_helper['MixedIviDanceAndLenMechanism']['outputArray'] = expected_output
        interpreter = self.get_initialized_library_interpreter()
        result_array = interpreter.mixed_ivi_dance_and_len_mechanism([1.1])
        assert result_array == expected_output
        assert self.patched_library.niFake_MixedIviDanceAndLenMechanism.call_count == 2

    def test_parameters_are_multiple_types(self):
        self.patched_library.niFake_ParametersAreMultipleTypes.side_effect = self.side_effects_helper.niFake_ParametersAreMultipleTypes
        boolean_val = True
        int32_val = 32
        int64_val = 6000000000
        enum_val = nifake.Turtle.LEONARDO
        float_val = 1.23
        float_enum_val = nifake.FloatEnum.SIX_POINT_FIVE
        string_val = 'Testing is fun?'
        interpreter = self.get_initialized_library_interpreter()
        interpreter.parameters_are_multiple_types(boolean_val, int32_val, int64_val, enum_val, float_val, float_enum_val, string_val)
        self.patched_library.niFake_ParametersAreMultipleTypes.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViBooleanMatcher(boolean_val), _matchers.ViInt32Matcher(int32_val), _matchers.ViInt64Matcher(int64_val), _matchers.ViInt16Matcher(enum_val.value), _matchers.ViReal64Matcher(float_val), _matchers.ViReal64Matcher(float_enum_val.value), _matchers.ViStringMatcher(string_val))

    def test_method_with_error(self):
        test_error_code = -42
        test_error_desc = "The answer to the ultimate question"
        self.patched_library.niFake_PoorlyNamedSimpleFunction.side_effect = self.side_effects_helper.niFake_PoorlyNamedSimpleFunction
        self.side_effects_helper['PoorlyNamedSimpleFunction']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        interpreter = self.get_initialized_library_interpreter()
        try:
            interpreter.simple_function()
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc

    def test_call_not_enough_parameters_error(self):
        interpreter = self.get_initialized_library_interpreter()
        try:
            interpreter.multiple_array_types(10)
            assert False
        except TypeError:
            pass

    def test_invalid_method_call_wrong_type_error(self):
        interpreter = self.get_initialized_library_interpreter()
        try:
            interpreter.multiple_array_types('potato', [0.0, 0.1, 0.2])
            assert False
        except TypeError:
            pass

    def test_method_with_warning(self):
        # We want to capture all of our warnings, not just the first one
        warnings.filterwarnings("always", category=nifake.DriverWarning)

        test_error_code = 42
        test_error_desc = "The answer to the ultimate question, only positive"
        self.patched_library.niFake_PoorlyNamedSimpleFunction.side_effect = self.side_effects_helper.niFake_PoorlyNamedSimpleFunction
        self.side_effects_helper['PoorlyNamedSimpleFunction']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        interpreter = self.get_initialized_library_interpreter()
        with warnings.catch_warnings(record=True) as w:
            interpreter.simple_function()
            assert len(w) == 1
            assert issubclass(w[0].category, nifake.DriverWarning)
            assert test_error_desc in str(w[0].message)
            assert f'Warning {test_error_code} occurred.' in str(w[0].message)

    def test_read_with_warning(self):
        # We want to capture all of our warnings, not just the first one
        warnings.filterwarnings("always", category=nifake.DriverWarning)

        test_maximum_time_s = 10.0
        test_reading = float('nan')
        test_error_code = 42
        test_error_desc = "The answer to the ultimate question, only positive"
        self.patched_library.niFake_Read.side_effect = self.niFake_read_warning
        self.error_code_return = test_error_code
        self.reading = test_reading
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        interpreter = self.get_initialized_library_interpreter()
        with warnings.catch_warnings(record=True) as w:
            assert math.isnan(interpreter.read(test_maximum_time_s))
            assert len(w) == 1
            assert issubclass(w[0].category, nifake.DriverWarning)
            assert test_error_desc in str(w[0].message)
            assert f'Warning {test_error_code} occurred.' in str(w[0].message)

    def test_library_interpreter_always_uses_same_library_instance(self):
        interpreter1 = self.get_initialized_library_interpreter()
        interpreter2 = self.get_initialized_library_interpreter()
        assert interpreter1 is not interpreter2
        assert interpreter1._library is interpreter2._library

    def test_set_runtime_environment_is_called_once_if_present(self):
        nifake._library_interpreter._was_runtime_environment_set = None
        self.get_initialized_library_interpreter()
        self.get_initialized_library_interpreter()
        self.patched_library.niFake_SetRuntimeEnvironment.assert_called_once()

    def test_set_runtime_environment_not_present_in_driver_runtime(self):
        class TypesLibrary:
            item = ""

        nifake._library_interpreter._was_runtime_environment_set = None
        self.patched_library._library = TypesLibrary()
        interpreter = self.get_initialized_library_interpreter()
        with pytest.raises(nifake.errors.DriverTooOldError):
            interpreter._library._get_library_function('niFake_SetRuntimeEnvironment')

    # Retrieving buffers and strings

    def test_get_a_string_of_fixed_maximum_size(self):
        test_string = "A string no larger than the max size of 256 allowed by the function."
        self.patched_library.niFake_GetAStringOfFixedMaximumSize.side_effect = self.side_effects_helper.niFake_GetAStringOfFixedMaximumSize
        self.side_effects_helper['GetAStringOfFixedMaximumSize']['aString'] = test_string
        interpreter = self.get_initialized_library_interpreter()
        returned_string = interpreter.get_a_string_of_fixed_maximum_size()
        assert returned_string == test_string
        self.patched_library.niFake_GetAStringOfFixedMaximumSize.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViCharBufferMatcher(256))

    def test_get_a_string_of_size_python_code(self):
        test_size = 4
        expected_string_size = test_size - 1
        test_string = "A string that is larger than test_size."
        expected_string = test_string[:expected_string_size]
        self.patched_library.niFake_GetAStringUsingPythonCode.side_effect = self.side_effects_helper.niFake_GetAStringUsingPythonCode
        self.side_effects_helper['GetAStringUsingPythonCode']['aString'] = expected_string
        interpreter = self.get_initialized_library_interpreter()
        returned_string = interpreter.get_a_string_using_python_code(test_size)
        assert returned_string == expected_string
        self.patched_library.niFake_GetAStringUsingPythonCode.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt16Matcher(test_size), _matchers.ViCharBufferMatcher(test_size))

    def test_return_a_number_and_a_string(self):
        test_string = "this string"
        test_number = 13
        self.patched_library.niFake_ReturnANumberAndAString.side_effect = self.side_effects_helper.niFake_ReturnANumberAndAString
        self.side_effects_helper['ReturnANumberAndAString']['aString'] = test_string
        self.side_effects_helper['ReturnANumberAndAString']['aNumber'] = test_number
        interpreter = self.get_initialized_library_interpreter()
        returned_number, returned_string = interpreter.return_a_number_and_a_string()
        assert returned_string == test_string
        assert returned_number == test_number
        self.patched_library.niFake_ReturnANumberAndAString.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt16PointerMatcher(), _matchers.ViCharBufferMatcher(256))

    def test_get_an_ivi_dance_char_array(self):
        self.patched_library.niFake_GetAnIviDanceCharArray.side_effect = self.side_effects_helper.niFake_GetAnIviDanceCharArray
        string_val = 'Testing is fun?'
        self.side_effects_helper['GetAnIviDanceCharArray']['charArray'] = string_val
        interpreter = self.get_initialized_library_interpreter()
        result_string = interpreter.get_an_ivi_dance_char_array()
        assert result_string == string_val
        calls = [
            call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(0), None),
            call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(string_val)), _matchers.ViCharBufferMatcher(len(string_val)))
        ]
        self.patched_library.niFake_GetAnIviDanceCharArray.assert_has_calls(calls)
        assert self.patched_library.niFake_GetAnIviDanceCharArray.call_count == 2

    def test_get_string_ivi_dance_error(self):
        read_write_string_attribute_id = 1000002
        test_error_code = -1234
        test_error_desc = "ascending order"
        self.patched_library.niFake_GetAttributeViString.side_effect = self.side_effects_helper.niFake_GetAttributeViString
        self.side_effects_helper['GetAttributeViString']['attributeValue'] = 'Testing is fun?'
        self.side_effects_helper['GetAttributeViString']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = test_error_code
        self.side_effects_helper['GetError']['description'] = test_error_desc
        interpreter = self.get_initialized_library_interpreter()
        try:
            interpreter.get_attribute_vi_string('', read_write_string_attribute_id)
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc

    def test_get_an_ivi_dance_with_a_twist_string(self):
        self.patched_library.niFake_GetAnIviDanceWithATwistString.side_effect = self.side_effects_helper.niFake_GetAnIviDanceWithATwistString
        string_val = 'Testing is fun?'
        self.side_effects_helper['GetAnIviDanceWithATwistString']['aString'] = string_val
        self.side_effects_helper['GetAnIviDanceWithATwistString']['actualSize'] = len(string_val)
        interpreter = self.get_initialized_library_interpreter()
        result_string = interpreter.get_an_ivi_dance_with_a_twist_string()
        assert result_string == string_val
        calls = [
            call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(0), None, _matchers.ViInt32PointerMatcher()),
            call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(string_val)), _matchers.ViCharBufferMatcher(len(string_val)), _matchers.ViInt32PointerMatcher())
        ]
        self.patched_library.niFake_GetAnIviDanceWithATwistString.assert_has_calls(calls)
        assert self.patched_library.niFake_GetAnIviDanceWithATwistString.call_count == 2

    def test_get_array_using_ivi_dance(self):
        self.patched_library.niFake_GetArrayUsingIviDance.side_effect = self.side_effects_helper.niFake_GetArrayUsingIviDance
        self.side_effects_helper['GetArrayUsingIviDance']['arrayOut'] = [1.1, 2.2]
        interpreter = self.get_initialized_library_interpreter()
        result_array = interpreter.get_array_using_ivi_dance()
        assert result_array == [1.1, 2.2]

    # Attributes

    def test_get_attribute_int32(self):
        self.patched_library.niFake_GetAttributeViInt32.side_effect = self.side_effects_helper.niFake_GetAttributeViInt32
        attribute_id = 1000004
        test_number = 3
        self.side_effects_helper['GetAttributeViInt32']['attributeValue'] = test_number
        interpreter = self.get_initialized_library_interpreter()
        attr_int = interpreter.get_attribute_vi_int32('', attribute_id)
        assert attr_int == test_number
        self.patched_library.niFake_GetAttributeViInt32.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt32PointerMatcher())

    def test_set_attribute_int32(self):
        self.patched_library.niFake_SetAttributeViInt32.side_effect = self.side_effects_helper.niFake_SetAttributeViInt32
        attribute_id = 1000004
        test_number = -10
        interpreter = self.get_initialized_library_interpreter()
        interpreter.set_attribute_vi_int32('', attribute_id, test_number)
        self.patched_library.niFake_SetAttributeViInt32.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt32Matcher(test_number))

    def test_get_attribute_real64(self):
        self.patched_library.niFake_GetAttributeViReal64.side_effect = self.side_effects_helper.niFake_GetAttributeViReal64
        attribute_id = 1000001
        test_number = 1.5
        self.side_effects_helper['GetAttributeViReal64']['attributeValue'] = test_number
        interpreter = self.get_initialized_library_interpreter()
        attr_double = interpreter.get_attribute_vi_real64('', attribute_id)
        assert attr_double == test_number
        self.patched_library.niFake_GetAttributeViReal64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViReal64PointerMatcher())

    def test_set_attribute_real64(self):
        self.patched_library.niFake_SetAttributeViReal64.side_effect = self.side_effects_helper.niFake_SetAttributeViReal64
        attribute_id = 1000001
        test_number = 10.1
        interpreter = self.get_initialized_library_interpreter()
        interpreter.set_attribute_vi_real64('', attribute_id, test_number)
        self.patched_library.niFake_SetAttributeViReal64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViReal64Matcher(test_number))

    def test_get_attribute_string(self):
        self.patched_library.niFake_GetAttributeViString.side_effect = self.side_effects_helper.niFake_GetAttributeViString
        attribute_id = 1000002
        string = 'Testing is fun?'
        self.side_effects_helper['GetAttributeViString']['attributeValue'] = string
        interpreter = self.get_initialized_library_interpreter()
        attr_string = interpreter.get_attribute_vi_string('', attribute_id)
        assert attr_string == string
        calls = [
            call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(1000002), _matchers.ViInt32Matcher(0), None),
            call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt32Matcher(15), _matchers.ViCharBufferMatcher(len(string)))
        ]
        self.patched_library.niFake_GetAttributeViString.assert_has_calls(calls)
        assert self.patched_library.niFake_GetAttributeViString.call_count == 2

    def test_set_attribute_string(self):
        self.patched_library.niFake_SetAttributeViString.side_effect = self.side_effects_helper.niFake_SetAttributeViString
        attribute_id = 1000002
        attrib_string = 'This is test string'
        interpreter = self.get_initialized_library_interpreter()
        interpreter.set_attribute_vi_string('', attribute_id, attrib_string)
        self.patched_library.niFake_SetAttributeViString.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViStringMatcher('This is test string'))

    def test_get_attribute_boolean(self):
        self.patched_library.niFake_GetAttributeViBoolean.side_effect = self.side_effects_helper.niFake_GetAttributeViBoolean
        attribute_id = 1000000
        self.side_effects_helper['GetAttributeViBoolean']['attributeValue'] = 1
        interpreter = self.get_initialized_library_interpreter()
        assert interpreter.get_attribute_vi_boolean('', attribute_id)
        self.patched_library.niFake_GetAttributeViBoolean.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViBooleanPointerMatcher())

    def test_set_attribute_boolean(self):
        self.patched_library.niFake_SetAttributeViBoolean.side_effect = self.side_effects_helper.niFake_SetAttributeViBoolean
        attribute_id = 1000000
        attrib_bool = True
        interpreter = self.get_initialized_library_interpreter()
        interpreter.set_attribute_vi_boolean('', attribute_id, attrib_bool)
        self.patched_library.niFake_SetAttributeViBoolean.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViBooleanMatcher(True))

    def test_get_attribute_int64(self):
        self.patched_library.niFake_GetAttributeViInt64.side_effect = self.side_effects_helper.niFake_GetAttributeViInt64
        attribute_id = 1000006
        test_number = 6000000000
        self.side_effects_helper['GetAttributeViInt64']['attributeValue'] = test_number
        interpreter = self.get_initialized_library_interpreter()
        attr_int = interpreter.get_attribute_vi_int64('', attribute_id)
        assert attr_int == test_number
        self.patched_library.niFake_GetAttributeViInt64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt64PointerMatcher())

    def test_set_attribute_int64(self):
        self.patched_library.niFake_SetAttributeViInt64.side_effect = self.side_effects_helper.niFake_SetAttributeViInt64
        attribute_id = 1000006
        test_number = -6000000000
        interpreter = self.get_initialized_library_interpreter()
        interpreter.set_attribute_vi_int64('', attribute_id, test_number)
        self.patched_library.niFake_SetAttributeViInt64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt64Matcher(test_number))

    # Error descriptions

    def test_get_error_returns_mismatched_error_code(self):
        test_error_code = -42
        test_error_desc = "The answer to the ultimate question, only positive"
        wrong_error_code = 54
        wrong_error_desc = "What is six times nine"
        self.patched_library.niFake_PoorlyNamedSimpleFunction.side_effect = self.side_effects_helper.niFake_PoorlyNamedSimpleFunction
        self.side_effects_helper['PoorlyNamedSimpleFunction']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = wrong_error_code
        self.side_effects_helper['GetError']['description'] = wrong_error_desc
        self.patched_library.niFake_error_message.side_effect = self.side_effects_helper.niFake_error_message
        self.side_effects_helper['error_message']['errorMessage'] = test_error_desc
        interpreter = self.get_initialized_library_interpreter()
        try:
            interpreter.simple_function()
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc
        self.patched_library.niFake_PoorlyNamedSimpleFunction.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))
        self.patched_library.niFake_error_message.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(test_error_code), _matchers.ViCharBufferMatcher(256))

    def test_get_error_and_error_message_returns_error(self):
        test_error_code = -42
        self.patched_library.niFake_PoorlyNamedSimpleFunction.side_effect = self.side_effects_helper.niFake_PoorlyNamedSimpleFunction
        self.side_effects_helper['PoorlyNamedSimpleFunction']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = -1
        self.side_effects_helper['GetError']['description'] = "Shouldn't get this"
        self.side_effects_helper['GetError']['return'] = -2
        self.patched_library.niFake_error_message.side_effect = self.side_effects_helper.niFake_error_message
        self.side_effects_helper['error_message']['errorMessage'] = "Also shouldn't get this"
        self.side_effects_helper['error_message']['return'] = -3
        interpreter = self.get_initialized_library_interpreter()
        try:
            interpreter.simple_function()
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == 'Failed to retrieve error description.'

    def test_get_error_description_error_message_error(self):
        test_error_code = -42
        test_error_desc = "The answer to the ultimate question"
        self.patched_library.niFake_PoorlyNamedSimpleFunction.side_effect = self.side_effects_helper.niFake_PoorlyNamedSimpleFunction
        self.side_effects_helper['PoorlyNamedSimpleFunction']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = -1
        self.side_effects_helper['GetError']['description'] = "Shouldn't get this"
        self.side_effects_helper['GetError']['return'] = -2
        self.patched_library.niFake_error_message.side_effect = self.side_effects_helper.niFake_error_message
        self.side_effects_helper['error_message']['errorMessage'] = test_error_desc
        interpreter = self.get_initialized_library_interpreter()
        try:
            interpreter.simple_function()
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc
        self.patched_library.niFake_error_message.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(test_error_code), _matchers.ViCharBufferMatcher(256))

    def test_get_error_description_error_message_after_session_reset(self):
        test_error_code = -42
        test_error_desc = "The answer to the ultimate question"
        self.patched_library.niFake_PoorlyNamedSimpleFunction.side_effect = self.side_effects_helper.niFake_PoorlyNamedSimpleFunction
        self.side_effects_helper['PoorlyNamedSimpleFunction']['return'] = test_error_code
        self.patched_library.niFake_GetError.side_effect = self.side_effects_helper.niFake_GetError
        self.side_effects_helper['GetError']['errorCode'] = -1
        self.side_effects_helper['GetError']['description'] = "Shouldn't get this"
        self.side_effects_helper['GetError']['return'] = -2
        self.side_effects_helper['error_message']['errorMessage'] = test_error_desc

        def error_message_side_effect(vi, error_code, error_message_buf):
            if vi.value == SESSION_NUM_FOR_TEST:
                return -3
            return self.side_effects_helper.niFake_error_message(vi, error_code, error_message_buf)

        self.patched_library.niFake_error_message.side_effect = error_message_side_effect
        interpreter = self.get_initialized_library_interpreter()
        try:
            interpreter.simple_function()
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc
        assert self.patched_library.niFake_error_message.call_count == 2
        self.patched_library.niFake_error_message.assert_has_calls([
            call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(test_error_code), _matchers.ViCharBufferMatcher(256)),
            call(_matchers.ViSessionMatcher(0), _matchers.ViInt32Matcher(test_error_code), _matchers.ViCharBufferMatcher(256)),
        ])

    # Custom types

    def test_set_custom_type(self):
        self.patched_library.niFake_SetCustomType.side_effect = self.side_effects_helper.niFake_SetCustomType
        cs = nifake.CustomStruct(struct_int=42, struct_double=4.2)
        interpreter = self.get_initialized_library_interpreter()
        interpreter.set_custom_type(cs)
        self.patched_library.niFake_SetCustomType.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.CustomTypeMatcher(nifake.struct_CustomStruct, nifake.struct_CustomStruct(cs)))

    def test_get_custom_type(self):
        self.patched_library.niFake_GetCustomType.side_effect = self.side_effects_helper.niFake_GetCustomType
        cs_ctype = nifake.struct_CustomStruct(struct_int=42, struct_double=4.2)
        self.side_effects_helper['GetCustomType']['cs'] = cs_ctype
        interpreter = self.get_initialized_library_interpreter()
        cs = interpreter.get_custom_type()
        assert cs.struct_int == cs_ctype.struct_int
        assert cs.struct_double == cs_ctype.struct_double

    def test_set_custom_type_array(self):
        self.patched_library.niFake_SetCustomTypeArray.side_effect = self.side_effects_helper.niFake_SetCustomTypeArray
        cs = [nifake.CustomStruct(struct_int=42, struct_double=4.2), nifake.CustomStruct(struct_int=43, struct_double=4.3), nifake.CustomStruct(struct_int=42, struct_double=4.3)]
        cs_ctype = (nifake.struct_CustomStruct * len(cs))(*[nifake.struct_CustomStruct(c) for c in cs])
        interpreter = self.get_initialized_library_interpreter()
        interpreter.set_custom_type_array(cs)
        self.patched_library.niFake_SetCustomTypeArray.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(cs)), _matchers.CustomTypeBufferMatcher(nifake.struct_CustomStruct, cs_ctype))

    def test_get_custom_type_array(self):
        self.patched_library.niFake_GetCustomTypeArray.side_effect = self.side_effects_helper.niFake_GetCustomTypeArray
        cs = [nifake.CustomStruct(struct_int=42, struct_double=4.2), nifake.CustomStruct(struct_int=43, struct_double=4.3), nifake.CustomStruct(struct_int=42, struct_double=4.3)]
        cs_ctype = (nifake.struct_CustomStruct * len(cs))(*[nifake.struct_CustomStruct(c) for c in cs])
        self.side_effects_helper['GetCustomTypeArray']['cs'] = cs_ctype
        interpreter = self.get_initialized_library_interpreter()
        cs_test = interpreter.get_custom_type_array(len(cs_ctype))
        assert len(cs_test) == len(cs_ctype)
        for actual, expected in zip(cs_test, cs):
            assert actual.struct_int == expected.struct_int
            assert actual.struct_double == expected.struct_double

    def test_get_custom_type_typedef(self):
        self.patched_library.niFake_GetCustomTypeTypedef.side_effect = self.side_effects_helper.niFake_GetCustomTypeTypedef
        cst = nifake.CustomStructTypedef(struct_int=42, struct_double=4.2)
        cst_ctype = nifake.struct_CustomStructTypedef(cst)
        csnt = nifake.CustomStructNestedTypedef(
            struct_custom_struct=nifake.CustomStruct(struct_int=43, struct_double=4.3),
            struct_custom_struct_typedef=nifake.CustomStructTypedef(struct_int=44, struct_double=4.4)
        )
        csnt_ctype = nifake.struct_CustomStructNestedTypedef(csnt)
        self.side_effects_helper['GetCustomTypeTypedef']['cst'] = cst_ctype
        self.side_effects_helper['GetCustomTypeTypedef']['csnt'] = csnt_ctype
        interpreter = self.get_initialized_library_interpreter()
        cst_test, csnt_test = interpreter.get_custom_type_typedef()
        assert cst_test.struct_int == cst.struct_int
        assert cst_test.struct_double == cst.struct_double
        assert csnt_test.struct_custom_struct.struct_int == csnt.struct_custom_struct.struct_int
        assert csnt_test.struct_custom_struct.struct_double == csnt.struct_custom_struct.struct_double
        assert csnt_test.struct_custom_struct_typedef.struct_int == csnt.struct_custom_struct_typedef.struct_int
        assert csnt_test.struct_custom_struct_typedef.struct_double == csnt.struct_custom_struct_typedef.struct_double

    # python-code size mechanism

    def test_get_array_using_python_code_double(self):
        import nifake._visatype
        self.patched_library.niFake_GetArraySizeForPythonCode.side_effect = self.side_effects_helper.niFake_GetArraySizeForPythonCode
        self.patched_library.niFake_GetArrayForPythonCodeDouble.side_effect = self.side_effects_helper.niFake_GetArrayForPythonCodeDouble
        array_out = [42.0, 43.0, 44.0]
        array_out_ctype = (nifake._visatype.ViReal64 * len(array_out))(*array_out)
        self.side_effects_helper['GetArraySizeForPythonCode']['sizeOut'] = len(array_out)
        self.side_effects_helper['GetArrayForPythonCodeDouble']['arrayOut'] = array_out_ctype
        interpreter = self.get_initialized_library_interpreter()
        array_out_test = interpreter.get_array_for_python_code_double()
        assert len(array_out_test) == len(array_out)
        for actual, expected in zip(array_out_test, array_out):
            assert actual == expected

    def test_get_array_using_python_code_custom_type(self):
        import nifake._visatype
        self.patched_library.niFake_GetArraySizeForPythonCode.side_effect = self.side_effects_helper.niFake_GetArraySizeForPythonCode
        self.patched_library.niFake_GetArrayForPythonCodeCustomType.side_effect = self.side_effects_helper.niFake_GetArrayForPythonCodeCustomType
        cs = [nifake.CustomStruct(struct_int=42, struct_double=4.2), nifake.CustomStruct(struct_int=43, struct_double=4.3), nifake.CustomStruct(struct_int=42, struct_double=4.3)]
        cs_ctype = (nifake.struct_CustomStruct * len(cs))(*[nifake.struct_CustomStruct(c) for c in cs])
        self.side_effects_helper['GetArraySizeForPythonCode']['sizeOut'] = len(cs)
        self.side_effects_helper['GetArrayForPythonCodeCustomType']['arrayOut'] = cs_ctype
        interpreter = self.get_initialized_library_interpreter()
        cs_test = interpreter.get_array_for_python_code_custom_type()
        assert len(cs_test) == len(cs)
        for actual, expected in zip(cs_test, cs):
            assert actual.struct_int == expected.struct_int
            assert actual.struct_double == expected.struct_double

    def test_get_cal_date_time(self):
        self.patched_library.niFake_GetCalDateAndTime.side_effect = self.side_effects_helper.niFake_GetCalDateAndTime
        month = 12
        day = 30
        year = 1988
        hour = 10
        minute = 15
        self.side_effects_helper['GetCalDateAndTime']['return'] = 0
        self.side_effects_helper['GetCalDateAndTime']['month'] = month
        self.side_effects_helper['GetCalDateAndTime']['day'] = day
        self.side_effects_helper['GetCalDateAndTime']['year'] = year
        self.side_effects_helper['GetCalDateAndTime']['hour'] = hour
        self.side_effects_helper['GetCalDateAndTime']['minute'] = minute
        interpreter = self.get_initialized_library_interpreter()
        last_cal = interpreter.get_cal_date_and_time(0)
        assert (month, day, year, hour, minute) == last_cal

    # Import/Export functions

    def test_import_attribute_configuration_buffer_list_i8(self):
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.side_effect = self.side_effects_helper.niFake_ImportAttributeConfigurationBuffer
        expected_list = [ord('a'), ord('b'), ord('c'), ord('d')]
        configuration = expected_list
        interpreter = self.get_initialized_library_interpreter()
        self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        with patch('nifake._library_interpreter._get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
            interpreter.import_attribute_configuration_buffer(configuration)
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(configuration)), _matchers.ViInt8BufferMatcher(expected_list))

    def test_import_attribute_configuration_buffer_bytes(self):
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.side_effect = self.side_effects_helper.niFake_ImportAttributeConfigurationBuffer
        expected_list = [ord('a'), ord('b'), ord('c'), ord('d')]
        configuration = b'abcd'
        interpreter = self.get_initialized_library_interpreter()
        self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        with patch('nifake._library_interpreter._get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
            interpreter.import_attribute_configuration_buffer(configuration)
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(configuration)), _matchers.ViInt8BufferMatcher(expected_list))

    def test_import_attribute_configuration_buffer_bytearray(self):
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.side_effect = self.side_effects_helper.niFake_ImportAttributeConfigurationBuffer
        expected_list = [ord('a'), ord('b'), ord('c'), ord('d')]
        configuration = bytearray(b'abcd')
        interpreter = self.get_initialized_library_interpreter()
        self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        with patch('nifake._library_interpreter._get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
            interpreter.import_attribute_configuration_buffer(configuration)
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(configuration)), _matchers.ViInt8BufferMatcher(expected_list))

    def test_import_attribute_configuration_buffer_array_bytes(self):
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.side_effect = self.side_effects_helper.niFake_ImportAttributeConfigurationBuffer
        expected_list = [ord('a'), ord('b'), ord('c'), ord('d')]
        configuration = array.array('b', b'abcd')
        interpreter = self.get_initialized_library_interpreter()
        self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        with patch('nifake._library_interpreter._get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
            interpreter.import_attribute_configuration_buffer(configuration)
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(configuration)), _matchers.ViInt8BufferMatcher(expected_list))

    def test_import_attribute_configuration_buffer_str(self):
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.side_effect = self.side_effects_helper.niFake_ImportAttributeConfigurationBuffer
        expected_list = [ord('a'), ord('b'), ord('c'), ord('d')]
        configuration = 'abcd'
        interpreter = self.get_initialized_library_interpreter()
        self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        with patch('nifake._library_interpreter._get_ctypes_pointer_for_buffer', side_effect=self.get_ctypes_pointer_for_buffer_side_effect):
            interpreter.import_attribute_configuration_buffer(configuration)
        self.patched_library.niFake_ImportAttributeConfigurationBuffer.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViInt32Matcher(len(configuration)), _matchers.ViInt8BufferMatcher(expected_list))

    def test_write_waveform_numpy_complex128_valid_input(self):
        from nifake._complextype import NIComplexNumber

        waveform_data = numpy.full(1000, 0.707 + 0.707j, dtype=numpy.complex128)
        number_of_samples = len(waveform_data)

        waveform_data_ctypes = (NIComplexNumber * number_of_samples)(
            *[NIComplexNumber(real=0.707, imag=0.707) for _ in range(number_of_samples)]
        )
        waveform_data_pointer = ctypes.cast(waveform_data_ctypes, ctypes.POINTER(NIComplexNumber))
        self.patched_library.niFake_WriteWaveformNumpyComplex128.side_effect = self.side_effects_helper.niFake_WriteWaveformNumpyComplex128
        interpreter = self.get_initialized_library_interpreter()
        interpreter.write_waveform_numpy_complex128(waveform_data)
        self.patched_library.niFake_WriteWaveformNumpyComplex128.assert_called_once_with(
            _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
            _matchers.ViInt32Matcher(number_of_samples),
            _matchers.NIComplexNumberPointerMatcher(waveform_data_pointer, number_of_samples)
        )

    def test_write_waveform_numpy_complex64_valid_input(self):
        from nifake._complextype import NIComplexNumberF32

        waveform_data = numpy.full(1000, 0.707 + 0.707j, dtype=numpy.complex64)
        number_of_samples = len(waveform_data)

        waveform_data_ctypes = (NIComplexNumberF32 * number_of_samples)(
            *[NIComplexNumberF32(real=0.707, imag=0.707) for _ in range(number_of_samples)]
        )
        waveform_data_pointer = ctypes.cast(waveform_data_ctypes, ctypes.POINTER(NIComplexNumberF32))
        self.patched_library.niFake_WriteWaveformNumpyComplex64.side_effect = self.side_effects_helper.niFake_WriteWaveformNumpyComplex64
        interpreter = self.get_initialized_library_interpreter()
        interpreter.write_waveform_numpy_complex64(waveform_data)
        self.patched_library.niFake_WriteWaveformNumpyComplex64.assert_called_once_with(
            _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
            _matchers.ViInt32Matcher(number_of_samples),
            _matchers.NIComplexNumberF32PointerMatcher(waveform_data_pointer, number_of_samples)
        )

    def test_write_waveform_numpy_complex_interleaved_i16_valid_input(self):
        from nifake._complextype import NIComplexI16

        waveform_data = numpy.array([32767, 0] * 1000, dtype=numpy.int16)
        number_of_samples = len(waveform_data) // 2
        waveform_data_ctypes = (NIComplexI16 * number_of_samples)(
            *[NIComplexI16(real=32767, imag=0) for _ in range(number_of_samples)]
        )
        waveform_data_pointer = ctypes.cast(waveform_data_ctypes, ctypes.POINTER(NIComplexI16))
        self.patched_library.niFake_WriteWaveformNumpyComplexInterleavedI16.side_effect = self.side_effects_helper.niFake_WriteWaveformNumpyComplexInterleavedI16
        interpreter = self.get_initialized_library_interpreter()
        interpreter.write_waveform_numpy_complex_interleaved_i16(waveform_data)
        self.patched_library.niFake_WriteWaveformNumpyComplexInterleavedI16.assert_called_once_with(
            _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
            _matchers.ViInt32Matcher(number_of_samples),
            _matchers.NIComplexI16PointerMatcher(waveform_data_pointer, number_of_samples)
        )

    def test_write_3d_numpy_array_of_numpy_complex128(self):
        from nifake._complextype import NIComplexNumber

        array_3d = numpy.full((2, 3, 4), 1.0 + 2.0j, dtype=numpy.complex128)
        number_of_samples = array_3d.size
        flattened_array = array_3d.flatten()
        complex_array = (NIComplexNumber * len(flattened_array))()
        for i, value in enumerate(flattened_array):
            complex_array[i] = NIComplexNumber(value.real, value.imag)
        flattened_array_ptr = ctypes.cast(complex_array, ctypes.POINTER(NIComplexNumber))
        self.patched_library.niFake_FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter.side_effect = self.side_effects_helper.niFake_FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter
        interpreter = self.get_initialized_library_interpreter()
        interpreter.function_with_3d_numpy_array_of_numpy_complex128_input_parameter(array_3d)
        self.patched_library.niFake_FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter.assert_called_once_with(
            _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST),
            _matchers.NIComplexNumberPointerMatcher(flattened_array_ptr, number_of_samples)
        )

    def test_no_memorycopy_with_multi_dimensional_numpy_complex128_array(self):
        array_3d = numpy.full((2, 3, 4), 1.0 + 2.0j, dtype=numpy.complex128)
        self.patched_library.niFake_FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter.side_effect = self.side_effects_helper.niFake_FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter
        interpreter = self.get_initialized_library_interpreter()
        interpreter.function_with_3d_numpy_array_of_numpy_complex128_input_parameter(array_3d)
        args, kwargs = self.patched_library.niFake_FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter.call_args
        actual_pointer = args[1]
        input_address = array_3d.__array_interface__['data'][0]
        address_passed_to_library = ctypes.addressof(actual_pointer.contents)
        assert input_address == address_passed_to_library, f"Addresses do NOT match: input_address={input_address}, address_passed_to_library={address_passed_to_library}"

    def test_no_memorycopy_with_numpy_complex64_array(self):
        array_1d = numpy.full(1000, 0.707 + 0.707j, dtype=numpy.complex64)
        self.patched_library.niFake_WriteWaveformNumpyComplex64.side_effect = (
            self.side_effects_helper.niFake_WriteWaveformNumpyComplex64
        )
        interpreter = self.get_initialized_library_interpreter()
        interpreter.write_waveform_numpy_complex64(array_1d)
        args, kwargs = self.patched_library.niFake_WriteWaveformNumpyComplex64.call_args
        actual_pointer = args[2]
        input_address = array_1d.__array_interface__['data'][0]
        address_passed_to_library = ctypes.addressof(actual_pointer.contents)
        assert input_address == address_passed_to_library, (
            f"Addresses do NOT match: input_address={input_address}, address_passed_to_library={address_passed_to_library}"
        )

    def test_matcher_prints(self):
        assert _matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST).__repr__() == "ViSessionMatcher(" + str(nifake._visatype.ViSession) + ", 42)"
        assert _matchers.ViAttrMatcher(SESSION_NUM_FOR_TEST).__repr__() == "ViAttrMatcher(" + str(nifake._visatype.ViAttr) + ", 42)"
        assert _matchers.ViInt32Matcher(4).__repr__() == "ViInt32Matcher(" + str(nifake._visatype.ViInt32) + ", 4)"
        assert _matchers.ViStringMatcher('0-24').__repr__() == "ViStringMatcher('0-24')"
        assert _matchers.ViReal64Matcher(-42.0).__repr__() == "ViReal64Matcher(" + str(nifake._visatype.ViReal64) + ", -42.0)"
        assert _matchers.ViReal64PointerMatcher().__repr__() == "ViReal64PointerMatcher(" + str(nifake._visatype.ViReal64) + ")"
        assert _matchers.ViInt32PointerMatcher().__repr__() == "ViInt32PointerMatcher(" + str(nifake._visatype.ViInt32) + ")"
        cs = [nifake.CustomStruct(struct_int=42, struct_double=4.2), nifake.CustomStruct(struct_int=43, struct_double=4.3), nifake.CustomStruct(struct_int=42, struct_double=4.3)]
        cs_ctype = (nifake.struct_CustomStruct * len(cs))(*[nifake.struct_CustomStruct(c) for c in cs])
        assert _matchers.CustomTypeMatcher(nifake.struct_CustomStruct, nifake.struct_CustomStruct(cs[0])).__repr__() == "CustomTypeMatcher(<class 'nifake.custom_struct.struct_CustomStruct'>, struct_CustomStruct(data=None, struct_int=42, struct_double=4.2))"
        assert _matchers.CustomTypeBufferMatcher(nifake.struct_CustomStruct, cs_ctype).__repr__() == "CustomTypeBufferMatcher(<class 'nifake.custom_struct.struct_CustomStruct'>, [struct_CustomStruct(data=None, struct_int=42, struct_double=4.2), struct_CustomStruct(data=None, struct_int=43, struct_double=4.3), struct_CustomStruct(data=None, struct_int=42, struct_double=4.3)])"
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/nifake/unit_tests/test_library_singleton.py sha256=118b5ad6e0656d0db8e69ce148a6e1aee5574e4a0fbfedb41efe621e76d747ae bytes=208 -->
## FILE: generated/nifake/nifake/unit_tests/test_library_singleton.py

- repository: `ni/nimi-python`
- source_path: `generated/nifake/nifake/unit_tests/test_library_singleton.py`
- sha256: `118b5ad6e0656d0db8e69ce148a6e1aee5574e4a0fbfedb41efe621e76d747ae`
- bytes: 208

````python
import nifake
import pytest


def test_driver_runtime_not_installed_raises_driver_not_installed_error():
    with pytest.raises(nifake.errors.DriverNotInstalledError):
        nifake._library_singleton.get()
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/nifake/unit_tests/test_session.py sha256=27c8aa0fd32c7af6de4defb174955f1bf63a8a9ecfbbe5d79b88fc34a1986449 bytes=51612 -->
## FILE: generated/nifake/nifake/unit_tests/test_session.py

- repository: `ni/nimi-python`
- source_path: `generated/nifake/nifake/unit_tests/test_session.py`
- sha256: `27c8aa0fd32c7af6de4defb174955f1bf63a8a9ecfbbe5d79b88fc34a1986449`
- bytes: 51612

````python
import array
import datetime
import hightime
import nifake
import nifake.errors
import numpy
import pytest

from unittest.mock import MagicMock
from unittest.mock import patch

import _mock_helper

SESSION_NUM_FOR_TEST = 42
GRPC_SESSION_OBJECT_FOR_TEST = object()


class TestSession:

    class PatchedLibraryInterpreter(nifake._library_interpreter.LibraryInterpreter):
        def __init__(self, encoding):
            for f in dir(self):
                if not f.startswith("_") and f not in {'get_session_handle', 'set_session_handle'}:
                    setattr(self, f, MagicMock(spec_set=getattr(self, f), side_effect=_mock_helper.MockFunctionCallError(f)))

    def setup_method(self, method):
        self.patched_library_interpreter = self.PatchedLibraryInterpreter(None)
        self.patched_library_interpreter_ctor = patch('nifake.session._library_interpreter.LibraryInterpreter', return_value=self.patched_library_interpreter)
        self.patched_library_interpreter_ctor.start()

        # We don't actually call into the nitclk DLL, but we do need to mock the function since it is called
        self.tclk_patched_library_singleton_get = patch('nitclk._library_interpreter._library_singleton.get', return_value=None)
        self.tclk_patched_library_singleton_get.start()

        # We shouldn't call into grpc
        self.patched_grpc_interpreter = patch('nifake._grpc_stub_interpreter.GrpcStubInterpreter', side_effect=AssertionError('Called into grpc!'))
        self.patched_grpc_interpreter.start()

        def interpreter_init(*args, **kwargs):
            self.patched_library_interpreter._close_on_exit = True
            return SESSION_NUM_FOR_TEST

        self.patched_library_interpreter.init_with_options.side_effect = interpreter_init
        self.patched_library_interpreter.close.side_effect = [None]

        # Mock lock/unlock
        self.patched_library_interpreter.lock.side_effect = lambda *args: None
        self.patched_library_interpreter.unlock.side_effect = lambda *args: None

    def teardown_method(self, method):
        self.patched_grpc_interpreter.stop()
        self.patched_library_interpreter_ctor.stop()
        self.tclk_patched_library_singleton_get.stop()

    # Session management

    def test_init_with_options_and_close(self):
        session = nifake.Session('dev1')
        self.patched_library_interpreter.init_with_options.assert_called_once_with('dev1', False, False, '')
        assert session._interpreter._vi == SESSION_NUM_FOR_TEST
        session.close()
        self.patched_library_interpreter.close.assert_called_once_with()

    def test_init_with_options_nondefault_and_close(self):
        session = nifake.Session('FakeDevice', 'Some string', True, True)
        self.patched_library_interpreter.init_with_options.assert_called_once_with('FakeDevice', True, True, 'Some string')
        assert session._interpreter._vi == SESSION_NUM_FOR_TEST
        session.close()
        self.patched_library_interpreter.close.assert_called_once_with()

    def test_close(self):
        session = nifake.Session('dev1')
        assert session._interpreter._vi == SESSION_NUM_FOR_TEST
        session.close()
        self.patched_library_interpreter.close.assert_called_once_with()
        assert session._interpreter._vi == 0

    def test_session_context_manager(self):
        with nifake.Session('dev1') as session:
            assert isinstance(session, nifake.Session)
            self.patched_library_interpreter.init_with_options.assert_called_once_with('dev1', False, False, '')
            assert session._interpreter._vi == SESSION_NUM_FOR_TEST
        self.patched_library_interpreter.close.assert_called_once_with()
        assert session._interpreter._vi == 0

    def test_init_with_error(self):
        test_error_code = -1
        test_error_desc = 'Test'
        self.patched_library_interpreter.init_with_options.side_effect = nifake.errors.DriverError(test_error_code, test_error_desc)
        try:
            nifake.Session('dev1')
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc

    def test_close_with_error(self):
        test_error_code = -1
        test_error_desc = 'Test'
        session = nifake.Session('dev1')
        assert session._interpreter._vi == SESSION_NUM_FOR_TEST
        self.patched_library_interpreter.close.side_effect = nifake.errors.DriverError(test_error_code, test_error_desc)
        try:
            session.close()
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc
        self.patched_library_interpreter.close.assert_called_once_with()
        assert session._interpreter._vi == 0

    def test_session_context_manager_init_with_error(self):
        test_error_code = -1
        test_error_desc = 'Test'
        self.patched_library_interpreter.init_with_options.side_effect = nifake.errors.DriverError(test_error_code, test_error_desc)
        try:
            with nifake.Session('dev1') as session:
                assert isinstance(session, nifake.Session)
                assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc

    def test_session_context_manager_close_with_error(self):
        test_error_code = -1
        test_error_desc = 'Test'
        self.patched_library_interpreter.close.side_effect = nifake.errors.DriverError(test_error_code, test_error_desc)
        try:
            with nifake.Session('dev1') as session:
                assert isinstance(session, nifake.Session)
                assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc

    # Session locking

    def test_lock_session_none(self):
        with nifake.Session('dev1') as session:
            session.lock()
            self.patched_library_interpreter.lock.assert_called_once_with()

    def test_unlock_session_none(self):
        with nifake.Session('dev1') as session:
            session.unlock()
            self.patched_library_interpreter.unlock.assert_called_once_with()

    def test_lock_context_manager(self):
        with nifake.Session('dev1') as session:
            with session.lock():
                pass
            self.patched_library_interpreter.lock.assert_called_once_with()
            self.patched_library_interpreter.unlock.assert_called_once_with()

    def test_lock_context_manager_abnormal_exit(self):
        with nifake.Session('dev1') as session:
            try:
                with session.lock():
                    raise nifake.Error('Fake exception')
            except nifake.Error:
                pass
            self.patched_library_interpreter.lock.assert_called_once_with()
            self.patched_library_interpreter.unlock.assert_called_once_with()

    # Methods

    def test_self_test(self):
        test_error_code = 0
        self.patched_library_interpreter.self_test.side_effect = [(test_error_code, '')]
        with nifake.Session('dev1') as session:
            session.self_test()

    def test_self_test_fail(self):
        test_error_code = 1
        test_error_message = 'error message'
        self.patched_library_interpreter.self_test.side_effect = [(test_error_code, test_error_message)]
        with nifake.Session('dev1') as session:
            try:
                session.self_test()
                assert False
            except nifake.errors.SelfTestError as e:
                assert e.code == test_error_code
                assert e.message == test_error_message

    def test_acquisition_context_manager(self):
        self.patched_library_interpreter.initiate.side_effect = [None]
        self.patched_library_interpreter.abort.side_effect = [None]
        with nifake.Session('dev1') as session:
            with session.initiate():
                self.patched_library_interpreter.initiate.assert_called_once_with()
            self.patched_library_interpreter.abort.assert_called_once_with()
        self.patched_library_interpreter.close.assert_called_once_with()

    def test_acquisition_no_context_manager(self):
        self.patched_library_interpreter.initiate.side_effect = [None]
        self.patched_library_interpreter.abort.side_effect = [None]
        with nifake.Session('dev1') as session:
            session.initiate()
            self.patched_library_interpreter.initiate.assert_called_once_with()
            session.abort()
            self.patched_library_interpreter.abort.assert_called_once_with()
        self.patched_library_interpreter.close.assert_called_once_with()

    def test_single_point_read_timedelta(self):
        test_maximum_time_ns = 1    # nanoseconds
        test_maximum_time_s = 1e-9  # seconds
        test_maximum_time_timedelta = hightime.timedelta(nanoseconds=test_maximum_time_ns)
        test_reading = 5
        self.patched_library_interpreter.read.side_effect = [test_reading]
        with nifake.Session('dev1') as session:
            assert test_reading == session.read(test_maximum_time_timedelta)
            self.patched_library_interpreter.read.assert_called_once_with(test_maximum_time_s)

    def test_enum_input_function_with_defaults(self):
        default_turtle = nifake.Turtle.LEONARDO
        test_turtle = nifake.Turtle.DONATELLO
        self.patched_library_interpreter.enum_input_function_with_defaults.side_effect = [None, None]
        with nifake.Session('dev1') as session:
            session.enum_input_function_with_defaults()
            session.enum_input_function_with_defaults(test_turtle)
            from unittest.mock import call
            calls = [call(default_turtle), call(test_turtle)]
            self.patched_library_interpreter.enum_input_function_with_defaults.assert_has_calls(calls)

    def test_string_valued_enum_input_function_with_defaults(self):
        default_mobile_os_name = nifake.MobileOSNames.ANDROID
        test_mobile_os_name = nifake.MobileOSNames.IOS
        self.patched_library_interpreter.string_valued_enum_input_function_with_defaults.side_effect = [None, None]
        with nifake.Session('dev1') as session:
            session.string_valued_enum_input_function_with_defaults()
            session.string_valued_enum_input_function_with_defaults(test_mobile_os_name)
            from unittest.mock import call
            calls = [call(default_mobile_os_name), call(test_mobile_os_name)]
            self.patched_library_interpreter.string_valued_enum_input_function_with_defaults.assert_has_calls(calls)

    def test_fetch_waveform_into_wrong_type(self):
        length = 10
        with nifake.Session('dev1') as session:
            waveforms = [
                10,
                10.5,
                "Not a numpy.ndarray",
                range(length),
                [i + 0.0 for i in range(length)],
                numpy.empty(length, numpy.int32),
                numpy.empty(length, numpy.uint8)
            ]
            for w in waveforms:
                try:
                    session.fetch_waveform_into(w)
                    assert False
                except TypeError:
                    pass

    def test_parameters_are_multiple_types_error(self):
        boolean_val = True
        int32_val = 32
        int64_val = 6000000000
        enum_val = nifake.Turtle.LEONARDO
        float_val = 1.23
        float_enum_val = nifake.FloatEnum.SIX_POINT_FIVE
        string_val = 'Testing is fun?'
        with nifake.Session('dev1') as session:
            try:
                session.parameters_are_multiple_types(boolean_val, int32_val, int64_val, 123, float_val, float_enum_val, string_val)
                assert False
            except TypeError:
                pass
            try:
                session.parameters_are_multiple_types(boolean_val, int32_val, int64_val, enum_val, float_val, 0.123, string_val)
                assert False
            except TypeError:
                pass

    def test_error_with_rep_cap(self):
        test_error_code = -42
        test_error_desc = "The answer to the ultimate question"
        self.patched_library_interpreter.set_attribute_vi_real64.side_effect = nifake.errors.DriverError(test_error_code, test_error_desc)
        with nifake.Session('dev1') as session:
            try:
                session.channels['100'].read_write_double = 5.0
                assert False
            except nifake.Error as e:
                assert e.code == test_error_code
                assert e.description == test_error_desc

    def test_call_not_enough_parameters_error(self):
        with nifake.Session('dev1') as session:
            try:
                session.multiple_array_types(10)
                assert False
            except TypeError:
                pass

    def test_enum_input_function_with_defaults_bad_type_error(self):
        test_turtle = 123
        with nifake.Session('dev1') as session:
            try:
                session.enum_input_function_with_defaults(test_turtle)
                assert False
            except TypeError:
                pass

    def test_get_channel_names(self):
        channel_indices = [0, 3, 2]
        channel_indices_string = '0,3,2'
        expected_channel_names_string = 'ch0,ch3,ch2'
        expected_channel_names = ['ch0', 'ch3', 'ch2']
        self.patched_library_interpreter.get_channel_names.side_effect = [expected_channel_names_string]
        with nifake.Session('dev1') as session:
            channel_names_from_session = session.get_channel_names(channel_indices)
            assert channel_names_from_session == expected_channel_names
            self.patched_library_interpreter.get_channel_names.assert_called_once_with(channel_indices_string)

    # Repeated Capabilities

    def test_repeated_capability_method_on_session_timedelta(self):
        test_maximum_time_ms = 10     # milliseconds
        test_maximum_time_timedelta = hightime.timedelta(milliseconds=test_maximum_time_ms)
        test_reading = 5
        self.patched_library_interpreter.read_from_channel.side_effect = [test_reading]
        with nifake.Session('dev1') as session:
            value = session.read_from_channel(test_maximum_time_timedelta)
        self.patched_library_interpreter.read_from_channel.assert_called_once_with('', test_maximum_time_ms)
        assert value == test_reading

    def test_repeated_capability_method_on_specific_channel(self):
        test_maximum_time_ms = 10     # milliseconds
        test_maximum_time = hightime.timedelta(milliseconds=test_maximum_time_ms)
        test_reading = 5
        self.patched_library_interpreter.read_from_channel.side_effect = [test_reading]
        with nifake.Session('dev1') as session:
            value = session.channels['3'].read_from_channel(test_maximum_time)
        self.patched_library_interpreter.read_from_channel.assert_called_once_with('3', test_maximum_time_ms)
        assert value == test_reading

    def test_device_method_not_exist_on_repeated_capability_error(self):
        with nifake.Session('dev1') as session:
            try:
                session.channels['3'].simple_function()
                assert False, 'Method has no repeated capability so it shouldn\'t exist on _RepeatedCapability'
            except AttributeError:
                pass

    def test_repeated_capabilities_list(self):
        with nifake.Session('dev1') as session:
            assert session.channels['r0']._repeated_capability_list == ['r0']

    def test_chained_repeated_capabilities_list(self):
        with nifake.Session('dev1') as session:
            assert session.sites[0, 1].channels[2, 3]._repeated_capability_list == ['site0/2', 'site0/3', 'site1/2', 'site1/3']

    def test_chained_repeated_capability_method_on_specific_channel(self):
        test_maximum_time_ms = 10     # milliseconds
        test_maximum_time = hightime.timedelta(milliseconds=test_maximum_time_ms)
        test_reading = 5
        self.patched_library_interpreter.read_from_channel.side_effect = [test_reading]
        with nifake.Session('dev1') as session:
            value = session.sites[0, 1].channels[2, 3].read_from_channel(test_maximum_time)
        self.patched_library_interpreter.read_from_channel.assert_called_once_with('site0/2,site0/3,site1/2,site1/3', test_maximum_time_ms)
        assert value == test_reading

    def test_function_with_repeated_capability_type(self):
        self.patched_library_interpreter.function_with_repeated_capability_type.side_effect = [None]
        with nifake.Session('dev1') as session:
            session.channels['0-3'].function_with_repeated_capability_type()
            self.patched_library_interpreter.function_with_repeated_capability_type.assert_called_once_with('0,1,2,3')

    # Attributes

    def test_get_attribute_int32(self):
        test_number = 3
        self.patched_library_interpreter.get_attribute_vi_int32.side_effect = [test_number]
        with nifake.Session('dev1') as session:
            attr_int = session.read_write_integer
            assert attr_int == test_number
            self.patched_library_interpreter.get_attribute_vi_int32.assert_called_once_with('', 1000004)

    def test_set_attribute_int32(self):
        self.patched_library_interpreter.set_attribute_vi_int32.side_effect = [None]
        attribute_id = 1000004
        test_number = -10
        with nifake.Session('dev1') as session:
            session.read_write_integer = test_number
            self.patched_library_interpreter.set_attribute_vi_int32.assert_called_once_with('', attribute_id, test_number)

    def test_get_attribute_int32_with_converter(self):
        attribute_id = 1000008
        test_number_ms = 3
        test_number_s = 0.003
        self.patched_library_interpreter.get_attribute_vi_int32.side_effect = [test_number_ms]
        with nifake.Session('dev1') as session:
            attr_timedelta = session.read_write_integer_with_converter
            assert attr_timedelta.total_seconds() == test_number_s
            self.patched_library_interpreter.get_attribute_vi_int32.assert_called_once_with('', attribute_id)

    def test_set_attribute_int32_with_converter(self):
        self.patched_library_interpreter.set_attribute_vi_int32.side_effect = [None]
        attribute_id = 1000008
        test_number_ms = -10000
        with nifake.Session('dev1') as session:
            session.read_write_integer_with_converter = hightime.timedelta(milliseconds=test_number_ms)
            self.patched_library_interpreter.set_attribute_vi_int32.assert_called_once_with('', attribute_id, test_number_ms)

    def test_get_attribute_int32_with_month_converter(self):
        attribute_id = 1000014
        test_number_months = 2
        test_number_s = 5256005.76
        self.patched_library_interpreter.get_attribute_vi_int32.side_effect = [test_number_months]
        with nifake.Session('dev1') as session:
            attr_timedelta = session.read_write_integer_with_month_converter
            assert attr_timedelta.total_seconds() == test_number_s
            self.patched_library_interpreter.get_attribute_vi_int32.assert_called_once_with('', attribute_id)

    def test_set_attribute_int32_with_month_converter(self):
        self.patched_library_interpreter.set_attribute_vi_int32.side_effect = [None]
        attribute_id = 1000014
        test_number_months = 3
        with nifake.Session('dev1') as session:
            session.read_write_integer_with_month_converter = hightime.timedelta(seconds=60 * 60 * 24 * 30.4167 * test_number_months)
            self.patched_library_interpreter.set_attribute_vi_int32.assert_called_once_with('', attribute_id, test_number_months)

    def test_get_attribute_real64(self):
        attribute_id = 1000001
        test_number = 1.5
        self.patched_library_interpreter.get_attribute_vi_real64.side_effect = [test_number]
        with nifake.Session('dev1') as session:
            attr_double = session.read_write_double
            assert attr_double == test_number
            self.patched_library_interpreter.get_attribute_vi_real64.assert_called_once_with('', attribute_id)

    def test_set_attribute_real64(self):
        self.patched_library_interpreter.set_attribute_vi_real64.side_effect = [None]
        attribute_id = 1000001
        test_number = 10.1
        with nifake.Session('dev1') as session:
            session.read_write_double = test_number
            self.patched_library_interpreter.set_attribute_vi_real64.assert_called_once_with('', attribute_id, test_number)

    def test_get_attribute_real64_with_converter(self):
        attribute_id = 1000007
        test_number = 1e-9
        self.patched_library_interpreter.get_attribute_vi_real64.side_effect = [test_number]
        with nifake.Session('dev1') as session:
            attr_timedelta = session.read_write_double_with_converter
            assert attr_timedelta.total_seconds() == test_number
            self.patched_library_interpreter.get_attribute_vi_real64.assert_called_once_with('', attribute_id)

    def test_set_attribute_real64_with_converter(self):
        self.patched_library_interpreter.set_attribute_vi_real64.side_effect = [None]
        attribute_id = 1000007
        test_number = 1e-9
        with nifake.Session('dev1') as session:
            session.read_write_double_with_converter = hightime.timedelta(nanoseconds=1)
            self.patched_library_interpreter.set_attribute_vi_real64.assert_called_once_with('', attribute_id, test_number)

    def test_get_attribute_string(self):
        string = 'Testing is fun?'
        self.patched_library_interpreter.get_attribute_vi_string.side_effect = [string]
        attribute_id = 1000002
        with nifake.Session('dev1') as session:
            attr_string = session.read_write_string
            assert attr_string == string
            self.patched_library_interpreter.get_attribute_vi_string.assert_called_once_with('', attribute_id)

    def test_set_attribute_string(self):
        self.patched_library_interpreter.set_attribute_vi_string.side_effect = [None]
        attribute_id = 1000002
        attrib_string = 'This is test string'
        with nifake.Session('dev1') as session:
            session.read_write_string = attrib_string
            self.patched_library_interpreter.set_attribute_vi_string.assert_called_once_with('', attribute_id, 'This is test string')

    def test_get_attribute_comma_separated_string(self):
        comma_separated_string = 'PinA,PinB,PinC'
        expected_list = ['PinA', 'PinB', 'PinC']
        self.patched_library_interpreter.get_attribute_vi_string.side_effect = [comma_separated_string]
        attribute_id = 1000015
        with nifake.Session('dev1') as session:
            attr_list = session.read_write_comma_separated_string
            assert attr_list == expected_list
            self.patched_library_interpreter.get_attribute_vi_string.assert_called_once_with('', attribute_id)

    def test_set_attribute_comma_separated_string(self):
        self.patched_library_interpreter.set_attribute_vi_string.side_effect = [None]
        attribute_id = 1000015
        attrib_list = ['PinA', 'PinB', 'PinC']
        expected_string = 'PinA,PinB,PinC'
        with nifake.Session('dev1') as session:
            session.read_write_comma_separated_string = attrib_list
            self.patched_library_interpreter.set_attribute_vi_string.assert_called_once_with('', attribute_id, expected_string)

    def test_get_attribute_string_with_converter(self):
        string = 'not that interesting'
        self.patched_library_interpreter.get_attribute_vi_string.side_effect = [string]
        attribute_id = 1000010
        with nifake.Session('dev1') as session:
            attr_string = session.read_write_string_repeated_capability
            assert attr_string == string
            self.patched_library_interpreter.get_attribute_vi_string.assert_called_once_with('', attribute_id)

    def test_set_attribute_string_with_converter(self):
        self.patched_library_interpreter.set_attribute_vi_string.side_effect = [None]
        attribute_id = 1000010
        with nifake.Session('dev1') as session:
            session.read_write_string_repeated_capability = 42
            self.patched_library_interpreter.set_attribute_vi_string.assert_called_once_with('', attribute_id, '42')

    def test_get_attribute_boolean(self):
        self.patched_library_interpreter.get_attribute_vi_boolean.side_effect = [1]
        attribute_id = 1000000
        with nifake.Session('dev1') as session:
            assert session.read_write_bool
            self.patched_library_interpreter.get_attribute_vi_boolean.assert_called_once_with('', attribute_id)

    def test_set_attribute_boolean(self):
        self.patched_library_interpreter.set_attribute_vi_boolean.side_effect = [None]
        attribute_id = 1000000
        attrib_bool = True
        with nifake.Session('dev1') as session:
            session.read_write_bool = attrib_bool
            self.patched_library_interpreter.set_attribute_vi_boolean.assert_called_once_with('', attribute_id, True)

    def test_get_attribute_enum_int32(self):
        self.patched_library_interpreter.get_attribute_vi_int32.side_effect = [nifake.Color.BLUE]
        with nifake.Session('dev1') as session:
            assert session.read_write_color == nifake.Color.BLUE
            attribute_id = 1000003
            self.patched_library_interpreter.get_attribute_vi_int32.assert_called_once_with('', attribute_id)

    def test_set_attribute_enum_int32(self):
        self.patched_library_interpreter.set_attribute_vi_int32.side_effect = [None]
        enum_value = nifake.Color.RED
        with nifake.Session('dev1') as session:
            session.read_write_color = enum_value
            attribute_id = 1000003
            self.patched_library_interpreter.set_attribute_vi_int32.assert_called_once_with('', attribute_id, enum_value.value)

    def test_get_attribute_enum_real64(self):
        enum_value = nifake.FloatEnum.SIX_POINT_FIVE
        self.patched_library_interpreter.get_attribute_vi_real64.side_effect = [enum_value]
        with nifake.Session('dev1') as session:
            assert session.float_enum == enum_value
            attribute_id = 1000005
            self.patched_library_interpreter.get_attribute_vi_real64.assert_called_once_with('', attribute_id)

    def test_set_attribute_enum_real64(self):
        self.patched_library_interpreter.set_attribute_vi_real64.side_effect = [None]
        enum_value = nifake.FloatEnum.FIVE_POINT_FIVE
        with nifake.Session('dev1') as session:
            session.float_enum = enum_value
            attribute_id = 1000005
            self.patched_library_interpreter.set_attribute_vi_real64.assert_called_once_with('', attribute_id, enum_value.value)

    def test_get_attribute_enum_with_converter(self):
        enum_value = nifake.EnumWithConverter.RED
        converted_value = True
        self.patched_library_interpreter.get_attribute_vi_int32.side_effect = [enum_value]
        with nifake.Session('dev1') as session:
            assert session.read_write_enum_with_converter == converted_value
            attribute_id = 1000011
            self.patched_library_interpreter.get_attribute_vi_int32.assert_called_once_with('', attribute_id)

    def test_get_attribute_enum_with_converter_invalid_value_from_driver(self):
        invalid_value_from_driver = 0
        expected_error_message = 'The NI-FAKE runtime returned an unexpected value. This can occur if it is too new for the nifake Python module. Upgrade the nifake Python module.'
        self.patched_library_interpreter.get_attribute_vi_int32.side_effect = [invalid_value_from_driver]
        with nifake.Session('dev1') as session:
            try:
                session.read_write_enum_with_converter
                assert False
            except nifake.errors.DriverTooNewError as actual_error:
                actual_error_message = actual_error.args[0]
                assert actual_error_message == expected_error_message
            attribute_id = 1000011
            self.patched_library_interpreter.get_attribute_vi_int32.assert_called_once_with('', attribute_id)

    def test_set_attribute_enum_with_converter(self):
        enum_value = nifake.EnumWithConverter.RED
        converted_value = True
        self.patched_library_interpreter.set_attribute_vi_int32.side_effect = [None]
        with nifake.Session('dev1') as session:
            session.read_write_enum_with_converter = converted_value
            attribute_id = 1000011
            self.patched_library_interpreter.set_attribute_vi_int32.assert_called_once_with('', attribute_id, enum_value.value)

    def test_set_attribute_enum_with_converter_invalid_input(self):
        invalid_input_value = 'invalid'
        expected_error_description = "Invalid value: invalid"
        self.patched_library_interpreter.set_attribute_vi_int32.side_effect = [None]
        with nifake.Session('dev1') as session:
            try:
                session.read_write_enum_with_converter = invalid_input_value
                assert False
            except ValueError as actual_error:
                actual_error_message = actual_error.args[0]
                assert actual_error_message == expected_error_description
            assert not self.patched_library_interpreter.set_attribute_vi_int32.called

    def test_get_attribute_channel(self):
        test_number = 100
        self.patched_library_interpreter.get_attribute_vi_int32.side_effect = [test_number]
        attribute_id = 1000004
        with nifake.Session('dev1') as session:
            attr_int = session.channels[['0', '1']].read_write_integer
            assert attr_int == test_number
            self.patched_library_interpreter.get_attribute_vi_int32.assert_called_once_with('0,1', attribute_id)

    def test_set_attribute_channel(self):
        self.patched_library_interpreter.set_attribute_vi_real64.side_effect = [None]
        attribute_id = 1000001
        test_number = 0.001
        with nifake.Session('dev1') as session:
            session.channels[range(24)].read_write_double = test_number
            self.patched_library_interpreter.set_attribute_vi_real64.assert_called_once_with('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23', attribute_id, test_number)

    def test_get_attribute_int64(self):
        attribute_id = 1000006
        test_number = 6000000000
        self.patched_library_interpreter.get_attribute_vi_int64.side_effect = [test_number]
        with nifake.Session('dev1') as session:
            attr_int = session.read_write_int64
            assert attr_int == test_number
            self.patched_library_interpreter.get_attribute_vi_int64.assert_called_once_with('', attribute_id)

    def test_set_attribute_int64(self):
        self.patched_library_interpreter.set_attribute_vi_int64.side_effect = [None]
        attribute_id = 1000006
        test_number = -6000000000
        with nifake.Session('dev1') as session:
            session.read_write_int64 = test_number
            self.patched_library_interpreter.set_attribute_vi_int64.assert_called_once_with('', attribute_id, test_number)

    def test_get_attribute_error(self):
        test_error_code = -123
        test_error_desc = "ascending order"
        self.patched_library_interpreter.get_attribute_vi_real64.side_effect = nifake.errors.DriverError(test_error_code, test_error_desc)
        with nifake.Session('dev1') as session:
            try:
                session.read_write_double
                assert False
            except nifake.Error as e:
                assert e.code == test_error_code
                assert e.description == test_error_desc

    def test_set_attribute_error(self):
        attribute_id = 1000001
        test_error_code = -1
        test_error_desc = 'Test'
        self.patched_library_interpreter.set_attribute_vi_real64.side_effect = nifake.errors.DriverError(test_error_code, test_error_desc)
        with nifake.Session('dev1') as session:
            try:
                session.read_write_double = -42.0
                assert False
            except nifake.Error as e:
                assert e.code == test_error_code
                assert e.description == test_error_desc
                self.patched_library_interpreter.set_attribute_vi_real64.assert_called_once_with('', attribute_id, -42.0)

    def test_add_properties_to_session_error_set(self):
        with nifake.Session('dev1') as session:
            try:
                session.non_existent_property = 5
                assert False
            except AttributeError as e:
                assert str(e) == "'Session' object has no attribute 'non_existent_property'"

    def test_add_properties_to_session_error_get(self):
        with nifake.Session('dev1') as session:
            try:
                value = session.non_existent_property  # noqa: F841
                assert False
            except AttributeError as e:
                assert str(e) == "'Session' object has no attribute 'non_existent_property'"

    def test_add_properties_to_repeated_capability_error_set(self):
        with nifake.Session('dev1') as session:
            try:
                session.channels['0'].non_existent_property = 5
                assert False
            except AttributeError as e:
                assert str(e) == "'_SessionBase' object has no attribute 'non_existent_property'"

    def test_add_properties_to_repeated_capability_error_get(self):
        with nifake.Session('dev1') as session:
            try:
                value = session.channels['0'].non_existent_property  # noqa: F841
                assert False
            except AttributeError as e:
                assert str(e) == "'_SessionBase' object has no attribute 'non_existent_property'"

    def test_set_enum_attribute_int32_error(self):
        with nifake.Session('dev1') as session:
            try:
                session.read_write_color = 5
            except TypeError as e:
                assert str(e) == 'must be Color not int'

    def test_set_wrong_enum_attribute_int32_error(self):
        with nifake.Session('dev1') as session:
            try:
                session.read_write_color = nifake.FloatEnum.SIX_POINT_FIVE
            except TypeError as e:
                assert str(e) == 'must be Color not FloatEnum'

    def test_multiple_arrays_same_size_wrong_size_2(self):
        with nifake.Session('dev1') as session:
            input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
            input_array_of_floats2 = [0.410, 0.420, 0.430]
            input_array_of_floats3 = [4.100, 4.200, 4.300, 4.400]
            input_array_of_floats4 = [41.00, 42.00, 43.00, 44.00]
            try:
                session.multiple_arrays_same_size(input_array_of_floats1, input_array_of_floats2, input_array_of_floats3, input_array_of_floats4)
            except ValueError:
                pass

    def test_multiple_arrays_same_size_wrong_size_3(self):
        with nifake.Session('dev1') as session:
            input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
            input_array_of_floats2 = [0.410, 0.420, 0.430, 0.440]
            input_array_of_floats3 = [4.100, 4.200, 4.400]
            input_array_of_floats4 = [41.00, 42.00, 43.00, 44.00]
            try:
                session.multiple_arrays_same_size(input_array_of_floats1, input_array_of_floats2, input_array_of_floats3, input_array_of_floats4)
            except ValueError:
                pass

    def test_multiple_arrays_same_size_wrong_size_4(self):
        with nifake.Session('dev1') as session:
            input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
            input_array_of_floats2 = [0.410, 0.420, 0.430, 0.440]
            input_array_of_floats3 = [4.100, 4.200, 4.300, 4.400]
            input_array_of_floats4 = [41.00, 42.00, 43.00, 44.00, 45.00]
            try:
                session.multiple_arrays_same_size(input_array_of_floats1, input_array_of_floats2, input_array_of_floats3, input_array_of_floats4)
            except ValueError:
                pass

    def test_multiple_arrays_different_size_none_input(self):
        values_array = [1.1, 2.2, 3.3]
        self.patched_library_interpreter.multiple_arrays_different_size.side_effect = [None]
        with nifake.Session('dev1') as session:
            assert session.multiple_arrays_different_size(values_array, None) is None
            self.patched_library_interpreter.multiple_arrays_different_size.assert_called_once_with(values_array, None)

    def test_get_cal_date_time(self):
        month = 12
        day = 30
        year = 1988
        hour = 10
        minute = 15
        self.patched_library_interpreter.get_cal_date_and_time.side_effect = [(month, day, year, hour, minute)]
        with nifake.Session('dev1') as session:
            last_cal = session.get_cal_date_and_time(0)
            assert isinstance(last_cal, hightime.datetime)
            assert hightime.datetime(year, month, day, hour, minute) == last_cal

    def test_get_cal_interval(self):
        self.patched_library_interpreter.get_cal_interval.side_effect = [24]
        with nifake.Session('dev1') as session:
            last_cal = session.get_cal_interval()
            assert isinstance(last_cal, hightime.timedelta)
            assert 730 == last_cal.days

    # Import/Export functions - Invalid types

    def test_import_attribute_configuration_buffer_list_i8_big(self):
        expected_list = [ord('a') * 100, ord('b') * 100, ord('c') * 100, ord('d') * 100]
        configuration = expected_list
        with nifake.Session('dev1') as session:
            self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
            self.get_ctypes_pointer_for_buffer_side_effect_count = 0
            try:
                session.import_attribute_configuration_buffer(configuration)
                assert False
            except ValueError:
                pass

    def test_import_attribute_configuration_buffer_list_i8_float(self):
        expected_list = [ord('a') * 1.0, ord('b') * 1.0, ord('c') * 1.0, ord('d') * 1.0]
        configuration = expected_list
        with nifake.Session('dev1') as session:
            self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
            self.get_ctypes_pointer_for_buffer_side_effect_count = 0
            try:
                session.import_attribute_configuration_buffer(configuration)
                assert False
            except TypeError:
                pass

    def test_import_attribute_configuration_buffer_list_i8_big_float(self):
        expected_list = [ord('a') * 100.0, ord('b') * 100.0, ord('c') * 100.0, ord('d') * 100.0]
        configuration = expected_list
        with nifake.Session('dev1') as session:
            self.get_ctypes_pointer_for_buffer_side_effect_items = [expected_list]
            self.get_ctypes_pointer_for_buffer_side_effect_count = 0
            try:
                session.import_attribute_configuration_buffer(configuration)
                assert False
            except TypeError:
                pass

    def test_export_attribute_configuration_buffer(self):
        expected_buffer_list = [ord('a'), ord('b'), ord('c'), ord('d'), ]
        self.patched_library_interpreter.export_attribute_configuration_buffer.side_effect = [expected_buffer_list]
        with nifake.Session('dev1') as session:
            actual_configuration = session.export_attribute_configuration_buffer()
            assert type(actual_configuration) is bytes
            assert actual_configuration == bytes(expected_buffer_list)
        self.patched_library_interpreter.export_attribute_configuration_buffer.assert_called_once_with()

    def test_channel_on_session(self):
        with nifake.Session('dev1') as session:
            try:
                session['100'].read_write_double = 5.0
                assert False
            except TypeError:
                pass

    def test_function_name(self):
        with nifake.Session('dev1') as session:
            # Pick a function that uses @ivi_synchronized
            assert session.bool_array_output_function.__name__ == 'bool_array_output_function'
            # Pick several functions that do not use @ivi_synchronized to make sure they don't break in the future
            assert session.lock.__name__ == 'lock'
            assert session._error_message.__name__ == '_error_message'
            assert session.initiate.__name__ == 'initiate'
            # Cannot use session.<property>.__name__ since that invokes the get attribute value and the returned value
            # (string, int, float) don't have __name__ properties

    def test_buffer_converter(self):
        self.patched_library_interpreter.double_all_the_nums.side_effect = [None]
        nums = [1, 2, 3, 4.2]
        nums_x2 = [x * 2 for x in nums]
        with nifake.Session('dev1') as session:
            session.double_all_the_nums(nums)
            self.patched_library_interpreter.double_all_the_nums.assert_called_once_with(nums_x2)

    def test_nitclk_integration(self):
        with nifake.Session('dev1') as session:
            assert str(type(session.tclk)) == "<class 'nitclk.session.SessionReference'>"

    def test_accept_list_of_time_values_as_floats(self):
        self.patched_library_interpreter.accept_list_of_durations_in_seconds.side_effect = [None]
        delays = [-1.5, 2.0]
        with nifake.Session('dev1') as session:
            session.accept_list_of_durations_in_seconds(delays)
            self.patched_library_interpreter.accept_list_of_durations_in_seconds.assert_called_once_with(delays)

    def test_accept_array_of_time_values_as_floats(self):
        self.patched_library_interpreter.accept_list_of_durations_in_seconds.side_effect = [None]
        time_values = [-1.5, 2.0]
        delays = array.array('d', time_values)
        with nifake.Session('dev1') as session:
            session.accept_list_of_durations_in_seconds(delays)
            self.patched_library_interpreter.accept_list_of_durations_in_seconds.assert_called_once_with(time_values)

    def test_accept_list_of_time_values_as_timedelta_instances(self):
        self.patched_library_interpreter.accept_list_of_durations_in_seconds.side_effect = [None]
        time_values = [-1.5, 2e-9]
        delays = [datetime.timedelta(seconds=-1.5), hightime.timedelta(nanoseconds=2)]
        with nifake.Session('dev1') as session:
            session.accept_list_of_durations_in_seconds(delays)
            self.patched_library_interpreter.accept_list_of_durations_in_seconds.assert_called_once_with(time_values)

    def test_return_timedelta(self):
        time_value = -1.5
        expected_timedelta = hightime.timedelta(seconds=time_value)
        self.patched_library_interpreter.return_duration_in_seconds.side_effect = [time_value]
        with nifake.Session('dev1') as session:
            returned_timedelta = session.return_duration_in_seconds()
            assert returned_timedelta == expected_timedelta
            self.patched_library_interpreter.return_duration_in_seconds.assert_called_once_with()

    def test_return_timedeltas(self):
        time_values = [-1.5, 2.0]
        expected_timedeltas = [hightime.timedelta(seconds=i) for i in time_values]
        self.patched_library_interpreter.return_list_of_durations_in_seconds.side_effect = [time_values]
        with nifake.Session('dev1') as session:
            returned_timedeltas = session.return_list_of_durations_in_seconds(len(expected_timedeltas))
            assert len(returned_timedeltas) == len(expected_timedeltas)
            assert returned_timedeltas == expected_timedeltas
            self.patched_library_interpreter.return_list_of_durations_in_seconds.assert_called_once_with(len(time_values))

    def test_with_valid_intflag_parameter(self):
        flags = nifake.IntFlagEnum.E | nifake.IntFlagEnum.A
        self.patched_library_interpreter.function_with_intflag_parameter.side_effect = None
        self.patched_library_interpreter.function_with_intflag_parameter.return_value = None
        with nifake.Session('dev1') as session:
            session.function_with_intflag_parameter(flags)
        self.patched_library_interpreter.function_with_intflag_parameter.assert_called_once_with(1073741825)

    def test_with_intflag_parameter_invalid(self):
        invalid_flag = 5
        with nifake.Session('dev1') as session:
            try:
                session.function_with_intflag_parameter(invalid_flag)
                assert False
            except TypeError:
                pass

    def test_session_write_waveform_numpy_complex64_invalid_dtype(self):
        invalid_waveform_data = numpy.full(10, 1.0 + 1.0j, dtype=numpy.complex128)
        expected_error_message = "waveform_data_array must be numpy.ndarray of dtype=complex64, is complex128"
        with nifake.Session('dev1') as session:
            with pytest.raises(TypeError) as exc_info:
                session.write_waveform_numpy_complex64(invalid_waveform_data)
            assert str(exc_info.value) == expected_error_message

    def test_session_write_waveform_numpy_complex128_invalid_dtype(self):
        invalid_waveform_data = numpy.full(10, 1.0 + 1.0j, dtype=numpy.complex64)
        expected_error_message = "waveform_data_array must be numpy.ndarray of dtype=complex128, is complex64"
        with nifake.Session('dev1') as session:
            with pytest.raises(TypeError) as exc_info:
                session.write_waveform_numpy_complex128(invalid_waveform_data)
            assert str(exc_info.value) == expected_error_message

    def test_session_write_waveform_numpy_complex_interleaved_i16_invalid_dtype(self):
        invalid_waveform_data = numpy.full(10, 1.0 + 1.0j, dtype=numpy.complex64)
        expected_error_message = "waveform_data_array must be numpy.ndarray of dtype=int16, is complex64"
        with nifake.Session('dev1') as session:
            with pytest.raises(TypeError) as exc_info:
                session.write_waveform_numpy_complex_interleaved_i16(invalid_waveform_data)
            assert str(exc_info.value) == expected_error_message


class TestGrpcSession:

    class PatchedGrpcInterpreter(nifake._grpc_stub_interpreter.GrpcStubInterpreter):
        def __init__(self, grpc_options):
            for f in dir(self):
                if not f.startswith("_") and f not in {'get_session_handle', 'set_session_handle'}:
                    setattr(self, f, MagicMock(spec_set=getattr(self, f), side_effect=_mock_helper.MockFunctionCallError(f)))

    def setup_method(self, method):
        self.patched_grpc_interpreter = self.PatchedGrpcInterpreter(None)
        self.patched_grpc_constructor = patch('nifake._grpc_stub_interpreter.GrpcStubInterpreter', return_value=self.patched_grpc_interpreter)
        self.patched_grpc_constructor.start()

        # We don't actually call into the nitclk DLL, but we do need to mock the function since it is called
        self.tclk_patched_library_singleton_get = patch('nitclk._library_interpreter._library_singleton.get', return_value=None)
        self.tclk_patched_library_singleton_get.start()

        def interpreter_init(*args, **kwargs):
            self.patched_grpc_interpreter._close_on_exit = True
            return GRPC_SESSION_OBJECT_FOR_TEST

        self.patched_grpc_interpreter.init_with_options.side_effect = interpreter_init
        self.patched_grpc_interpreter._close_on_exit = True
        self.patched_grpc_interpreter.close.side_effect = [None]

        # Mock lock/unlock
        self.patched_grpc_interpreter.lock.side_effect = lambda *args: None
        self.patched_grpc_interpreter.unlock.side_effect = lambda *args: None

    def teardown_method(self, method):
        self.patched_grpc_constructor.stop()
        self.tclk_patched_library_singleton_get.stop()

    # Session management

    def test_init_with_options_and_close(self):
        session = nifake.Session('dev1', grpc_options=nifake.GrpcSessionOptions(object(), ''))
        self.patched_grpc_interpreter.init_with_options.assert_called_once_with('dev1', False, False, '')
        assert session._interpreter._vi == GRPC_SESSION_OBJECT_FOR_TEST
        session.close()
        self.patched_grpc_interpreter.close.assert_called_once_with()

    # Session locking

    def test_lock_session_none(self):
        with nifake.Session('dev1', grpc_options=nifake.GrpcSessionOptions(object(), '')) as session:
            session.lock()
            self.patched_grpc_interpreter.lock.assert_called_once_with()

    def test_unlock_session_none(self):
        with nifake.Session('dev1', grpc_options=nifake.GrpcSessionOptions(object(), '')) as session:
            session.unlock()
            self.patched_grpc_interpreter.unlock.assert_called_once_with()

    def test_lock_context_manager(self):
        with nifake.Session('dev1', grpc_options=nifake.GrpcSessionOptions(object(), '')) as session:
            with session.lock():
                pass
            self.patched_grpc_interpreter.lock.assert_called_once_with()
            self.patched_grpc_interpreter.unlock.assert_called_once_with()

    def test_lock_context_manager_abnormal_exit(self):
        with nifake.Session('dev1', grpc_options=nifake.GrpcSessionOptions(object(), '')) as session:
            try:
                with session.lock():
                    raise nifake.Error('Fake exception')
            except nifake.Error:
                pass
            self.patched_grpc_interpreter.lock.assert_called_once_with()
            self.patched_grpc_interpreter.unlock.assert_called_once_with()

    # Methods

    def test_self_test(self):
        test_error_code = 0
        self.patched_grpc_interpreter.self_test.side_effect = [(test_error_code, '')]
        with nifake.Session('dev1', grpc_options=nifake.GrpcSessionOptions(object(), '')) as session:
            session.self_test()

    def test_export_attribute_configuration_buffer(self):
        expected_buffer = b'abcd'
        self.patched_grpc_interpreter.export_attribute_configuration_buffer.side_effect = [expected_buffer]
        with nifake.Session('dev1', grpc_options=nifake.GrpcSessionOptions(object(), '')) as session:
            actual_configuration = session.export_attribute_configuration_buffer()
            assert type(actual_configuration) is bytes
            assert actual_configuration == bytes(expected_buffer)
        self.patched_grpc_interpreter.export_attribute_configuration_buffer.assert_called_once_with()

    # Attributes

    def test_get_attribute_int32(self):
        test_number = 3
        self.patched_grpc_interpreter.get_attribute_vi_int32.side_effect = [test_number]
        with nifake.Session('dev1', grpc_options=nifake.GrpcSessionOptions(object(), '')) as session:
            attr_int = session.read_write_integer
            assert attr_int == test_number
            self.patched_grpc_interpreter.get_attribute_vi_int32.assert_called_once_with('', 1000004)


# not session tests per se
def test_diagnostic_information():
    info = nifake.print_diagnostic_information()
    assert isinstance(info, dict)


def test_dunder_version():
    print(f'Version = {nifake.__version__}')
    assert type(nifake.__version__) is str
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/nifake/VERSION sha256=5f2df6d86b73b1668c81b8c2b11cfa05ed74b6c42453c2bd4badfc93a2d47b0d bytes=13 -->
## FILE: generated/nifake/nifake/VERSION

- repository: `ni/nimi-python`
- source_path: `generated/nifake/nifake/VERSION`
- sha256: `5f2df6d86b73b1668c81b8c2b11cfa05ed74b6c42453c2bd4badfc93a2d47b0d`
- bytes: 13

````text
1.4.10.dev0
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/README.rst sha256=b8b0d44a22d213d39c85595d803949cc87d19569932b3845387533181fb94301 bytes=1327 -->
## FILE: generated/nifake/README.rst

- repository: `ni/nimi-python`
- source_path: `generated/nifake/README.rst`
- sha256: `b8b0d44a22d213d39c85595d803949cc87d19569932b3845387533181fb94301`
- bytes: 1327

````rst
This is the MIT license: http://www.opensource.org/licenses/mit-license.php

Copyright (c) 2017-2022, National Instruments Corporation.
NI-Digital Pattern Driver, NI-DMM, NI-DCPower, NI-FGEN, NI-RFSG, NI-SCOPE, NI-SWITCH, NI Switch Executive,
NI-ModInst, NI-TClk are trademarks of National Instruments.

Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files (the "Software"), to deal in the Software
without restriction, including without limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons
to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/setup.py sha256=af94a742c028a28eda83da288c878fe6e02515164c83c61b8e7ec857ecaaa96e bytes=1841 -->
## FILE: generated/nifake/setup.py

- repository: `ni/nimi-python`
- source_path: `generated/nifake/setup.py`
- sha256: `af94a742c028a28eda83da288c878fe6e02515164c83c61b8e7ec857ecaaa96e`
- bytes: 1841

````python
#!/usr/bin/python
# This file was generated


from setuptools import setup


pypi_name = 'nifake'


def read_contents(file_to_read):
    with open(file_to_read, 'r') as f:
        return f.read()


setup(
    name=pypi_name,
    zip_safe=True,
    version='1.4.10.dev0',
    description='NI-FAKE Python API',
    long_description=read_contents('README.rst'),
    long_description_content_type='text/x-rst',
    author='NI',
    author_email="opensource@ni.com",
    url="https://github.com/ni/nimi-python",
    maintainer="NI",
    maintainer_email="opensource@ni.com",
    keywords=['nifake'],
    license='MIT',
    include_package_data=True,
    packages=['nifake'],
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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifake/tox-system_tests.ini sha256=d459da504b1881522e672ffbbd0d0597a6072915c192bec20b50c793a9739815 bytes=3058 -->
## FILE: generated/nifake/tox-system_tests.ini

- repository: `ni/nimi-python`
- source_path: `generated/nifake/tox-system_tests.ini`
- sha256: `d459da504b1881522e672ffbbd0d0597a6072915c192bec20b50c793a9739815`
- bytes: 3058

````ini
# Tox (http://tox.testrun.org/) is a tool for running tests
# in multiple virtualenvs. This configuration file will run the
# test suite on all supported python versions. To use it, "pip install tox"
# and then run "tox -c tox-system_tests.ini" from the driver directory. (generated/nifake)
[tox]
envlist = py{310,311,312,313,314}-nifake-wheel_dep,py{310,311,312,313,314}-nifake-system_tests, py314-nifake-coverage
skip_missing_interpreters=True
ignore_basepython_conflict=True
# We put the .tox directory outside of the Jenkins workspace so that it isn't wiped with the rest of the repo
toxworkdir = ../../../.tox

[testenv]
description =
    nifake-wheel_dep: Build the nitclk wheel because we use it in nifake tests
    nifake-system_tests: Run nifake system tests (requires NI-FAKE runtime to be installed)
    nifake-coverage: Prepare coverage report for upload to codecov.io  # upload handled by GitHub Actions

changedir =
    nifake-wheel_dep: ../nitclk
    nifake-system_tests: .
    nifake-coverage: .

commands =
    nifake-wheel_dep: python -m build --wheel

    # --disable-pip-version-check prevents pip from telling us we need to upgrade pip, since we are doing that now
    nifake-system_tests: python -m pip install --disable-pip-version-check --upgrade pip
    nifake-system_tests: python ../../tools/install_local_wheel.py --driver nitclk --start-path ../..
    nifake-system_tests: python -c "import nifake; nifake.print_diagnostic_information()"
    nifake-system_tests: coverage run --rcfile=../../tools/coverage_system_tests.rc --source nifake --parallel-mode -m pytest ../../src/nifake/examples --junitxml=../junit/junit-nifake-{envname}-examples-{env:BITNESS:64}.xml {posargs}
    nifake-system_tests: coverage run --rcfile=../../tools/coverage_system_tests.rc --source nifake --parallel-mode -m pytest ../../src/nifake/system_tests -c tox-system_tests.ini --junitxml=../junit/junit-nifake-{envname}-{env:BITNESS:64}.xml --durations=5 {posargs}

    nifake-coverage: coverage combine --rcfile=../../tools/coverage_system_tests.rc ./
    # Create the report to upload
    nifake-coverage: coverage xml -i --rcfile=../../tools/coverage_system_tests.rc
    # Display the coverage results
    nifake-coverage: coverage report --rcfile=../../tools/coverage_system_tests.rc

deps =
    nifake-wheel_dep: build

    nifake-system_tests: pytest
    nifake-system_tests: coverage
    nifake-system_tests: numpy
    nifake-system_tests: hightime
    nifake-system_tests: fasteners
    nifake-system_tests: pytest-json
    nifake-system_tests: .[grpc]

    nifake-coverage: coverage

depends =
    nifake-coverage: py{310,311,312,313,314}-nifake-system_tests
    nifake-system_tests: py{310,311,312,313,314}-nifake-wheel_dep,

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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifgen/nifgen/__init__.py sha256=7c83959bfc4ab802a5ccba75a50f0d85a508c027bae3cb155828f52ba556cd34 bytes=3290 -->
## FILE: generated/nifgen/nifgen/__init__.py

- repository: `ni/nimi-python`
- source_path: `generated/nifgen/nifgen/__init__.py`
- sha256: `7c83959bfc4ab802a5ccba75a50f0d85a508c027bae3cb155828f52ba556cd34`
- bytes: 3290

````python
# -*- coding: utf-8 -*-
# This file was generated


__version__ = '1.4.10.dev0'

from nifgen.enums import *  # noqa: F403,F401,H303
from nifgen.errors import DriverWarning  # noqa: F401
from nifgen.errors import Error  # noqa: F401
from nifgen.grpc_session_options import *  # noqa: F403,F401,H303
from nifgen.session import Session  # noqa: F401


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
            driver_version_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\National Instruments\NI-FGEN\CurrentVersion")
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
    info['driver']['name'] = "NI-FGEN"
    info['driver']['version'] = driver_version
    info['module']['name'] = 'nifgen'
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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifgen/nifgen/_attributes.py sha256=d8a584f563cf68beef574de508b6279d12bdb8af6daa210010c716890eec9ba7 bytes=6175 -->
## FILE: generated/nifgen/nifgen/_attributes.py

- repository: `ni/nimi-python`
- source_path: `generated/nifgen/nifgen/_attributes.py`
- sha256: `d8a584f563cf68beef574de508b6279d12bdb8af6daa210010c716890eec9ba7`
- bytes: 6175

````python
# -*- coding: utf-8 -*-
# This file was generated
import nifgen._converters as _converters
import nifgen.errors as errors

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
    '''Class for attributes that use enums internally but are exposed in the nifgen Python module as something else, thus need conversion.'''

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
        from nifgen.session import SessionReference
        return SessionReference(session._get_attribute_vi_session(self._attribute_id))

    def __set__(self, session, value):
        session._set_attribute_vi_session(self._attribute_id, _converters.convert_to_nitclk_session_number(value))
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifgen/nifgen/_converters.py sha256=b588792a4ebd020c51eca2db07eb6347728cf74e4cd0ede516aa50028bac322b bytes=14621 -->
## FILE: generated/nifgen/nifgen/_converters.py

- repository: `ni/nimi-python`
- source_path: `generated/nifgen/nifgen/_converters.py`
- sha256: `b588792a4ebd020c51eca2db07eb6347728cf74e4cd0ede516aa50028bac322b`
- bytes: 14621

````python
# -*- coding: utf-8 -*-
# This file was generated
import nifgen._visatype as _visatype
import nifgen.errors as errors

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
