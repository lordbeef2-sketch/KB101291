# NI OSS SOURCE SNAPSHOT: nimi-python

<!--NI_OSS_SNAPSHOT repo=ni/nimi-python commit=6511f8025f072f7f7021953888b916bbdc31aa2a -->

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidcpower/nidcpower/unit_tests/_matchers.py sha256=7497d73de7de99f340dc1bbb481f7bca09fd5a44a098335a5c6b0b67d1ae1f8b bytes=12202 -->
## FILE: generated/nidcpower/nidcpower/unit_tests/_matchers.py

- repository: `ni/nimi-python`
- source_path: `generated/nidcpower/nidcpower/unit_tests/_matchers.py`
- sha256: `7497d73de7de99f340dc1bbb481f7bca09fd5a44a098335a5c6b0b67d1ae1f8b`
- bytes: 12202

````python
# -*- coding: utf-8 -*-
# This file was generated
'''Matcher classes used by unit tests in order to set mock expectations.
These work well with our visatype definitions.
'''

import ctypes
import nidcpower._visatype as _visatype
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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidcpower/nidcpower/unit_tests/_mock_helper.py sha256=3069ddbf154e69e61c168654eb291872ec416bfd1b87795092e836a57efd85d6 bytes=70249 -->
## FILE: generated/nidcpower/nidcpower/unit_tests/_mock_helper.py

- repository: `ni/nimi-python`
- source_path: `generated/nidcpower/nidcpower/unit_tests/_mock_helper.py`
- sha256: `3069ddbf154e69e61c168654eb291872ec416bfd1b87795092e836a57efd85d6`
- bytes: 70249

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
        self._defaults['AbortWithChannels'] = {}
        self._defaults['AbortWithChannels']['return'] = 0
        self._defaults['CalSelfCalibrate'] = {}
        self._defaults['CalSelfCalibrate']['return'] = 0
        self._defaults['ClearLatchedOutputCutoffState'] = {}
        self._defaults['ClearLatchedOutputCutoffState']['return'] = 0
        self._defaults['CommitWithChannels'] = {}
        self._defaults['CommitWithChannels']['return'] = 0
        self._defaults['ConfigureApertureTime'] = {}
        self._defaults['ConfigureApertureTime']['return'] = 0
        self._defaults['ConfigureLCRCompensation'] = {}
        self._defaults['ConfigureLCRCompensation']['return'] = 0
        self._defaults['ConfigureLCRCustomCableCompensation'] = {}
        self._defaults['ConfigureLCRCustomCableCompensation']['return'] = 0
        self._defaults['CreateAdvancedSequenceCommitStepWithChannels'] = {}
        self._defaults['CreateAdvancedSequenceCommitStepWithChannels']['return'] = 0
        self._defaults['CreateAdvancedSequenceStepWithChannels'] = {}
        self._defaults['CreateAdvancedSequenceStepWithChannels']['return'] = 0
        self._defaults['CreateAdvancedSequenceWithChannels'] = {}
        self._defaults['CreateAdvancedSequenceWithChannels']['return'] = 0
        self._defaults['DeleteAdvancedSequenceWithChannels'] = {}
        self._defaults['DeleteAdvancedSequenceWithChannels']['return'] = 0
        self._defaults['Disable'] = {}
        self._defaults['Disable']['return'] = 0
        self._defaults['ExportAttributeConfigurationBuffer'] = {}
        self._defaults['ExportAttributeConfigurationBuffer']['return'] = 0
        self._defaults['ExportAttributeConfigurationBuffer']['configuration'] = None
        self._defaults['ExportAttributeConfigurationFile'] = {}
        self._defaults['ExportAttributeConfigurationFile']['return'] = 0
        self._defaults['FancyInitialize'] = {}
        self._defaults['FancyInitialize']['return'] = 0
        self._defaults['FancyInitialize']['vi'] = None
        self._defaults['FetchMultiple'] = {}
        self._defaults['FetchMultiple']['return'] = 0
        self._defaults['FetchMultiple']['voltageMeasurements'] = None
        self._defaults['FetchMultiple']['currentMeasurements'] = None
        self._defaults['FetchMultiple']['inCompliance'] = None
        self._defaults['FetchMultiple']['actualCount'] = None
        self._defaults['FetchMultipleLCR'] = {}
        self._defaults['FetchMultipleLCR']['return'] = 0
        self._defaults['FetchMultipleLCR']['measurements'] = None
        self._defaults['FetchMultipleLCR']['actualCount'] = None
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
        self._defaults['GetChannelName'] = {}
        self._defaults['GetChannelName']['return'] = 0
        self._defaults['GetChannelName']['channelName'] = None
        self._defaults['GetChannelNameFromString'] = {}
        self._defaults['GetChannelNameFromString']['return'] = 0
        self._defaults['GetChannelNameFromString']['channelName'] = None
        self._defaults['GetError'] = {}
        self._defaults['GetError']['return'] = 0
        self._defaults['GetError']['code'] = None
        self._defaults['GetError']['description'] = None
        self._defaults['GetExtCalLastDateAndTime'] = {}
        self._defaults['GetExtCalLastDateAndTime']['return'] = 0
        self._defaults['GetExtCalLastDateAndTime']['year'] = None
        self._defaults['GetExtCalLastDateAndTime']['month'] = None
        self._defaults['GetExtCalLastDateAndTime']['day'] = None
        self._defaults['GetExtCalLastDateAndTime']['hour'] = None
        self._defaults['GetExtCalLastDateAndTime']['minute'] = None
        self._defaults['GetExtCalLastTemp'] = {}
        self._defaults['GetExtCalLastTemp']['return'] = 0
        self._defaults['GetExtCalLastTemp']['temperature'] = None
        self._defaults['GetExtCalRecommendedInterval'] = {}
        self._defaults['GetExtCalRecommendedInterval']['return'] = 0
        self._defaults['GetExtCalRecommendedInterval']['months'] = None
        self._defaults['GetLCRCompensationData'] = {}
        self._defaults['GetLCRCompensationData']['return'] = 0
        self._defaults['GetLCRCompensationData']['compensationData'] = None
        self._defaults['GetLCRCompensationLastDateAndTime'] = {}
        self._defaults['GetLCRCompensationLastDateAndTime']['return'] = 0
        self._defaults['GetLCRCompensationLastDateAndTime']['year'] = None
        self._defaults['GetLCRCompensationLastDateAndTime']['month'] = None
        self._defaults['GetLCRCompensationLastDateAndTime']['day'] = None
        self._defaults['GetLCRCompensationLastDateAndTime']['hour'] = None
        self._defaults['GetLCRCompensationLastDateAndTime']['minute'] = None
        self._defaults['GetLCRCustomCableCompensationData'] = {}
        self._defaults['GetLCRCustomCableCompensationData']['return'] = 0
        self._defaults['GetLCRCustomCableCompensationData']['customCableCompensationData'] = None
        self._defaults['GetSelfCalLastDateAndTime'] = {}
        self._defaults['GetSelfCalLastDateAndTime']['return'] = 0
        self._defaults['GetSelfCalLastDateAndTime']['year'] = None
        self._defaults['GetSelfCalLastDateAndTime']['month'] = None
        self._defaults['GetSelfCalLastDateAndTime']['day'] = None
        self._defaults['GetSelfCalLastDateAndTime']['hour'] = None
        self._defaults['GetSelfCalLastDateAndTime']['minute'] = None
        self._defaults['GetSelfCalLastTemp'] = {}
        self._defaults['GetSelfCalLastTemp']['return'] = 0
        self._defaults['GetSelfCalLastTemp']['temperature'] = None
        self._defaults['ImportAttributeConfigurationBuffer'] = {}
        self._defaults['ImportAttributeConfigurationBuffer']['return'] = 0
        self._defaults['ImportAttributeConfigurationFile'] = {}
        self._defaults['ImportAttributeConfigurationFile']['return'] = 0
        self._defaults['InitializeWithChannels'] = {}
        self._defaults['InitializeWithChannels']['return'] = 0
        self._defaults['InitializeWithChannels']['vi'] = None
        self._defaults['InitializeWithIndependentChannels'] = {}
        self._defaults['InitializeWithIndependentChannels']['return'] = 0
        self._defaults['InitializeWithIndependentChannels']['vi'] = None
        self._defaults['InitiateWithChannels'] = {}
        self._defaults['InitiateWithChannels']['return'] = 0
        self._defaults['LockSession'] = {}
        self._defaults['LockSession']['return'] = 0
        self._defaults['LockSession']['callerHasLock'] = None
        self._defaults['Measure'] = {}
        self._defaults['Measure']['return'] = 0
        self._defaults['Measure']['measurement'] = None
        self._defaults['MeasureMultiple'] = {}
        self._defaults['MeasureMultiple']['return'] = 0
        self._defaults['MeasureMultiple']['voltageMeasurements'] = None
        self._defaults['MeasureMultiple']['currentMeasurements'] = None
        self._defaults['MeasureMultipleLCR'] = {}
        self._defaults['MeasureMultipleLCR']['return'] = 0
        self._defaults['MeasureMultipleLCR']['measurements'] = None
        self._defaults['ParseChannelCount'] = {}
        self._defaults['ParseChannelCount']['return'] = 0
        self._defaults['ParseChannelCount']['numberOfChannels'] = None
        self._defaults['PerformLCRLoadCompensation'] = {}
        self._defaults['PerformLCRLoadCompensation']['return'] = 0
        self._defaults['PerformLCROpenCompensation'] = {}
        self._defaults['PerformLCROpenCompensation']['return'] = 0
        self._defaults['PerformLCROpenCustomCableCompensation'] = {}
        self._defaults['PerformLCROpenCustomCableCompensation']['return'] = 0
        self._defaults['PerformLCRShortCompensation'] = {}
        self._defaults['PerformLCRShortCompensation']['return'] = 0
        self._defaults['PerformLCRShortCustomCableCompensation'] = {}
        self._defaults['PerformLCRShortCustomCableCompensation']['return'] = 0
        self._defaults['QueryInCompliance'] = {}
        self._defaults['QueryInCompliance']['return'] = 0
        self._defaults['QueryInCompliance']['inCompliance'] = None
        self._defaults['QueryLatchedOutputCutoffState'] = {}
        self._defaults['QueryLatchedOutputCutoffState']['return'] = 0
        self._defaults['QueryLatchedOutputCutoffState']['outputCutoffState'] = None
        self._defaults['QueryMaxCurrentLimit'] = {}
        self._defaults['QueryMaxCurrentLimit']['return'] = 0
        self._defaults['QueryMaxCurrentLimit']['maxCurrentLimit'] = None
        self._defaults['QueryMaxVoltageLevel'] = {}
        self._defaults['QueryMaxVoltageLevel']['return'] = 0
        self._defaults['QueryMaxVoltageLevel']['maxVoltageLevel'] = None
        self._defaults['QueryMinCurrentLimit'] = {}
        self._defaults['QueryMinCurrentLimit']['return'] = 0
        self._defaults['QueryMinCurrentLimit']['minCurrentLimit'] = None
        self._defaults['QueryOutputState'] = {}
        self._defaults['QueryOutputState']['return'] = 0
        self._defaults['QueryOutputState']['inState'] = None
        self._defaults['ReadCurrentTemperature'] = {}
        self._defaults['ReadCurrentTemperature']['return'] = 0
        self._defaults['ReadCurrentTemperature']['temperature'] = None
        self._defaults['ResetDevice'] = {}
        self._defaults['ResetDevice']['return'] = 0
        self._defaults['ResetWithChannels'] = {}
        self._defaults['ResetWithChannels']['return'] = 0
        self._defaults['ResetWithDefaults'] = {}
        self._defaults['ResetWithDefaults']['return'] = 0
        self._defaults['SendSoftwareEdgeTriggerWithChannels'] = {}
        self._defaults['SendSoftwareEdgeTriggerWithChannels']['return'] = 0
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
        self._defaults['SetSequence'] = {}
        self._defaults['SetSequence']['return'] = 0
        self._defaults['UnlockSession'] = {}
        self._defaults['UnlockSession']['return'] = 0
        self._defaults['UnlockSession']['callerHasLock'] = None
        self._defaults['WaitForEventWithChannels'] = {}
        self._defaults['WaitForEventWithChannels']['return'] = 0
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

    def niDCPower_AbortWithChannels(self, vi, channel_name):  # noqa: N802
        if self._defaults['AbortWithChannels']['return'] != 0:
            return self._defaults['AbortWithChannels']['return']
        return self._defaults['AbortWithChannels']['return']

    def niDCPower_CalSelfCalibrate(self, vi, channel_name):  # noqa: N802
        if self._defaults['CalSelfCalibrate']['return'] != 0:
            return self._defaults['CalSelfCalibrate']['return']
        return self._defaults['CalSelfCalibrate']['return']

    def niDCPower_ClearLatchedOutputCutoffState(self, vi, channel_name, output_cutoff_reason):  # noqa: N802
        if self._defaults['ClearLatchedOutputCutoffState']['return'] != 0:
            return self._defaults['ClearLatchedOutputCutoffState']['return']
        return self._defaults['ClearLatchedOutputCutoffState']['return']

    def niDCPower_CommitWithChannels(self, vi, channel_name):  # noqa: N802
        if self._defaults['CommitWithChannels']['return'] != 0:
            return self._defaults['CommitWithChannels']['return']
        return self._defaults['CommitWithChannels']['return']

    def niDCPower_ConfigureApertureTime(self, vi, channel_name, aperture_time, units):  # noqa: N802
        if self._defaults['ConfigureApertureTime']['return'] != 0:
            return self._defaults['ConfigureApertureTime']['return']
        return self._defaults['ConfigureApertureTime']['return']

    def niDCPower_ConfigureLCRCompensation(self, vi, channel_name, compensation_data_size, compensation_data):  # noqa: N802
        if self._defaults['ConfigureLCRCompensation']['return'] != 0:
            return self._defaults['ConfigureLCRCompensation']['return']
        return self._defaults['ConfigureLCRCompensation']['return']

    def niDCPower_ConfigureLCRCustomCableCompensation(self, vi, channel_name, custom_cable_compensation_data_size, custom_cable_compensation_data):  # noqa: N802
        if self._defaults['ConfigureLCRCustomCableCompensation']['return'] != 0:
            return self._defaults['ConfigureLCRCustomCableCompensation']['return']
        return self._defaults['ConfigureLCRCustomCableCompensation']['return']

    def niDCPower_CreateAdvancedSequenceCommitStepWithChannels(self, vi, channel_name, set_as_active_step):  # noqa: N802
        if self._defaults['CreateAdvancedSequenceCommitStepWithChannels']['return'] != 0:
            return self._defaults['CreateAdvancedSequenceCommitStepWithChannels']['return']
        return self._defaults['CreateAdvancedSequenceCommitStepWithChannels']['return']

    def niDCPower_CreateAdvancedSequenceStepWithChannels(self, vi, channel_name, set_as_active_step):  # noqa: N802
        if self._defaults['CreateAdvancedSequenceStepWithChannels']['return'] != 0:
            return self._defaults['CreateAdvancedSequenceStepWithChannels']['return']
        return self._defaults['CreateAdvancedSequenceStepWithChannels']['return']

    def niDCPower_CreateAdvancedSequenceWithChannels(self, vi, channel_name, sequence_name, attribute_id_count, attribute_ids, set_as_active_sequence):  # noqa: N802
        if self._defaults['CreateAdvancedSequenceWithChannels']['return'] != 0:
            return self._defaults['CreateAdvancedSequenceWithChannels']['return']
        return self._defaults['CreateAdvancedSequenceWithChannels']['return']

    def niDCPower_DeleteAdvancedSequenceWithChannels(self, vi, channel_name, sequence_name):  # noqa: N802
        if self._defaults['DeleteAdvancedSequenceWithChannels']['return'] != 0:
            return self._defaults['DeleteAdvancedSequenceWithChannels']['return']
        return self._defaults['DeleteAdvancedSequenceWithChannels']['return']

    def niDCPower_Disable(self, vi):  # noqa: N802
        if self._defaults['Disable']['return'] != 0:
            return self._defaults['Disable']['return']
        return self._defaults['Disable']['return']

    def niDCPower_ExportAttributeConfigurationBuffer(self, vi, size, configuration):  # noqa: N802
        if self._defaults['ExportAttributeConfigurationBuffer']['return'] != 0:
            return self._defaults['ExportAttributeConfigurationBuffer']['return']
        # configuration
        if self._defaults['ExportAttributeConfigurationBuffer']['configuration'] is None:
            raise MockFunctionCallError("niDCPower_ExportAttributeConfigurationBuffer", param='configuration')
        if size.value == 0:
            return len(self._defaults['ExportAttributeConfigurationBuffer']['configuration'])
        try:
            configuration_ref = configuration.contents
        except AttributeError:
            configuration_ref = configuration
        for i in range(len(self._defaults['ExportAttributeConfigurationBuffer']['configuration'])):
            configuration_ref[i] = self._defaults['ExportAttributeConfigurationBuffer']['configuration'][i]
        return self._defaults['ExportAttributeConfigurationBuffer']['return']

    def niDCPower_ExportAttributeConfigurationFile(self, vi, file_path):  # noqa: N802
        if self._defaults['ExportAttributeConfigurationFile']['return'] != 0:
            return self._defaults['ExportAttributeConfigurationFile']['return']
        return self._defaults['ExportAttributeConfigurationFile']['return']

    def niDCPower_FancyInitialize(self, resource_name, channels, reset, option_string, vi, independent_channels):  # noqa: N802
        if self._defaults['FancyInitialize']['return'] != 0:
            return self._defaults['FancyInitialize']['return']
        # vi
        if self._defaults['FancyInitialize']['vi'] is None:
            raise MockFunctionCallError("niDCPower_FancyInitialize", param='vi')
        if vi is not None:
            vi.contents.value = self._defaults['FancyInitialize']['vi']
        return self._defaults['FancyInitialize']['return']

    def niDCPower_FetchMultiple(self, vi, channel_name, timeout, count, voltage_measurements, current_measurements, in_compliance, actual_count):  # noqa: N802
        if self._defaults['FetchMultiple']['return'] != 0:
            return self._defaults['FetchMultiple']['return']
        # voltage_measurements
        if self._defaults['FetchMultiple']['voltageMeasurements'] is None:
            raise MockFunctionCallError("niDCPower_FetchMultiple", param='voltageMeasurements')
        test_value = self._defaults['FetchMultiple']['voltageMeasurements']
        try:
            voltage_measurements_ref = voltage_measurements.contents
        except AttributeError:
            voltage_measurements_ref = voltage_measurements
        assert len(voltage_measurements_ref) >= len(test_value)
        for i in range(len(test_value)):
            voltage_measurements_ref[i] = test_value[i]
        # current_measurements
        if self._defaults['FetchMultiple']['currentMeasurements'] is None:
            raise MockFunctionCallError("niDCPower_FetchMultiple", param='currentMeasurements')
        test_value = self._defaults['FetchMultiple']['currentMeasurements']
        try:
            current_measurements_ref = current_measurements.contents
        except AttributeError:
            current_measurements_ref = current_measurements
        assert len(current_measurements_ref) >= len(test_value)
        for i in range(len(test_value)):
            current_measurements_ref[i] = test_value[i]
        # in_compliance
        if self._defaults['FetchMultiple']['inCompliance'] is None:
            raise MockFunctionCallError("niDCPower_FetchMultiple", param='inCompliance')
        test_value = self._defaults['FetchMultiple']['inCompliance']
        try:
            in_compliance_ref = in_compliance.contents
        except AttributeError:
            in_compliance_ref = in_compliance
        assert len(in_compliance_ref) >= len(test_value)
        for i in range(len(test_value)):
            in_compliance_ref[i] = test_value[i]
        # actual_count
        if self._defaults['FetchMultiple']['actualCount'] is None:
            raise MockFunctionCallError("niDCPower_FetchMultiple", param='actualCount')
        if actual_count is not None:
            actual_count.contents.value = self._defaults['FetchMultiple']['actualCount']
        return self._defaults['FetchMultiple']['return']

    def niDCPower_FetchMultipleLCR(self, vi, channel_name, timeout, count, measurements, actual_count):  # noqa: N802
        if self._defaults['FetchMultipleLCR']['return'] != 0:
            return self._defaults['FetchMultipleLCR']['return']
        # measurements
        if self._defaults['FetchMultipleLCR']['measurements'] is None:
            raise MockFunctionCallError("niDCPower_FetchMultipleLCR", param='measurements')
        test_value = self._defaults['FetchMultipleLCR']['measurements']
        try:
            measurements_ref = measurements.contents
        except AttributeError:
            measurements_ref = measurements
        assert len(measurements_ref) >= len(test_value)
        for i in range(len(test_value)):
            measurements_ref[i] = test_value[i]
        # actual_count
        if self._defaults['FetchMultipleLCR']['actualCount'] is None:
            raise MockFunctionCallError("niDCPower_FetchMultipleLCR", param='actualCount')
        if actual_count is not None:
            actual_count.contents.value = self._defaults['FetchMultipleLCR']['actualCount']
        return self._defaults['FetchMultipleLCR']['return']

    def niDCPower_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViBoolean']['return'] != 0:
            return self._defaults['GetAttributeViBoolean']['return']
        # attribute_value
        if self._defaults['GetAttributeViBoolean']['attributeValue'] is None:
            raise MockFunctionCallError("niDCPower_GetAttributeViBoolean", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViBoolean']['attributeValue']
        return self._defaults['GetAttributeViBoolean']['return']

    def niDCPower_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViInt32']['return'] != 0:
            return self._defaults['GetAttributeViInt32']['return']
        # attribute_value
        if self._defaults['GetAttributeViInt32']['attributeValue'] is None:
            raise MockFunctionCallError("niDCPower_GetAttributeViInt32", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViInt32']['attributeValue']
        return self._defaults['GetAttributeViInt32']['return']

    def niDCPower_GetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViInt64']['return'] != 0:
            return self._defaults['GetAttributeViInt64']['return']
        # attribute_value
        if self._defaults['GetAttributeViInt64']['attributeValue'] is None:
            raise MockFunctionCallError("niDCPower_GetAttributeViInt64", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViInt64']['attributeValue']
        return self._defaults['GetAttributeViInt64']['return']

    def niDCPower_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViReal64']['return'] != 0:
            return self._defaults['GetAttributeViReal64']['return']
        # attribute_value
        if self._defaults['GetAttributeViReal64']['attributeValue'] is None:
            raise MockFunctionCallError("niDCPower_GetAttributeViReal64", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViReal64']['attributeValue']
        return self._defaults['GetAttributeViReal64']['return']

    def niDCPower_GetAttributeViString(self, vi, channel_name, attribute_id, buffer_size, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViString']['return'] != 0:
            return self._defaults['GetAttributeViString']['return']
        # attribute_value
        if self._defaults['GetAttributeViString']['attributeValue'] is None:
            raise MockFunctionCallError("niDCPower_GetAttributeViString", param='attributeValue')
        if buffer_size.value == 0:
            return len(self._defaults['GetAttributeViString']['attributeValue'])
        attribute_value.value = self._defaults['GetAttributeViString']['attributeValue'].encode('ascii')
        return self._defaults['GetAttributeViString']['return']

    def niDCPower_GetChannelName(self, vi, index, buffer_size, channel_name):  # noqa: N802
        if self._defaults['GetChannelName']['return'] != 0:
            return self._defaults['GetChannelName']['return']
        # channel_name
        if self._defaults['GetChannelName']['channelName'] is None:
            raise MockFunctionCallError("niDCPower_GetChannelName", param='channelName')
        if buffer_size.value == 0:
            return len(self._defaults['GetChannelName']['channelName'])
        channel_name.value = self._defaults['GetChannelName']['channelName'].encode('ascii')
        return self._defaults['GetChannelName']['return']

    def niDCPower_GetChannelNameFromString(self, vi, indices, buffer_size, names):  # noqa: N802
        if self._defaults['GetChannelNameFromString']['return'] != 0:
            return self._defaults['GetChannelNameFromString']['return']
        # names
        if self._defaults['GetChannelNameFromString']['channelName'] is None:
            raise MockFunctionCallError("niDCPower_GetChannelNameFromString", param='channelName')
        if buffer_size.value == 0:
            return len(self._defaults['GetChannelNameFromString']['channelName'])
        names.value = self._defaults['GetChannelNameFromString']['channelName'].encode('ascii')
        return self._defaults['GetChannelNameFromString']['return']

    def niDCPower_GetError(self, vi, code, buffer_size, description):  # noqa: N802
        if self._defaults['GetError']['return'] != 0:
            return self._defaults['GetError']['return']
        # code
        if self._defaults['GetError']['code'] is None:
            raise MockFunctionCallError("niDCPower_GetError", param='code')
        if code is not None:
            code.contents.value = self._defaults['GetError']['code']
        # description
        if self._defaults['GetError']['description'] is None:
            raise MockFunctionCallError("niDCPower_GetError", param='description')
        if buffer_size.value == 0:
            return len(self._defaults['GetError']['description'])
        description.value = self._defaults['GetError']['description'].encode('ascii')
        return self._defaults['GetError']['return']

    def niDCPower_GetExtCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        if self._defaults['GetExtCalLastDateAndTime']['return'] != 0:
            return self._defaults['GetExtCalLastDateAndTime']['return']
        # year
        if self._defaults['GetExtCalLastDateAndTime']['year'] is None:
            raise MockFunctionCallError("niDCPower_GetExtCalLastDateAndTime", param='year')
        if year is not None:
            year.contents.value = self._defaults['GetExtCalLastDateAndTime']['year']
        # month
        if self._defaults['GetExtCalLastDateAndTime']['month'] is None:
            raise MockFunctionCallError("niDCPower_GetExtCalLastDateAndTime", param='month')
        if month is not None:
            month.contents.value = self._defaults['GetExtCalLastDateAndTime']['month']
        # day
        if self._defaults['GetExtCalLastDateAndTime']['day'] is None:
            raise MockFunctionCallError("niDCPower_GetExtCalLastDateAndTime", param='day')
        if day is not None:
            day.contents.value = self._defaults['GetExtCalLastDateAndTime']['day']
        # hour
        if self._defaults['GetExtCalLastDateAndTime']['hour'] is None:
            raise MockFunctionCallError("niDCPower_GetExtCalLastDateAndTime", param='hour')
        if hour is not None:
            hour.contents.value = self._defaults['GetExtCalLastDateAndTime']['hour']
        # minute
        if self._defaults['GetExtCalLastDateAndTime']['minute'] is None:
            raise MockFunctionCallError("niDCPower_GetExtCalLastDateAndTime", param='minute')
        if minute is not None:
            minute.contents.value = self._defaults['GetExtCalLastDateAndTime']['minute']
        return self._defaults['GetExtCalLastDateAndTime']['return']

    def niDCPower_GetExtCalLastTemp(self, vi, temperature):  # noqa: N802
        if self._defaults['GetExtCalLastTemp']['return'] != 0:
            return self._defaults['GetExtCalLastTemp']['return']
        # temperature
        if self._defaults['GetExtCalLastTemp']['temperature'] is None:
            raise MockFunctionCallError("niDCPower_GetExtCalLastTemp", param='temperature')
        if temperature is not None:
            temperature.contents.value = self._defaults['GetExtCalLastTemp']['temperature']
        return self._defaults['GetExtCalLastTemp']['return']

    def niDCPower_GetExtCalRecommendedInterval(self, vi, months):  # noqa: N802
        if self._defaults['GetExtCalRecommendedInterval']['return'] != 0:
            return self._defaults['GetExtCalRecommendedInterval']['return']
        # months
        if self._defaults['GetExtCalRecommendedInterval']['months'] is None:
            raise MockFunctionCallError("niDCPower_GetExtCalRecommendedInterval", param='months')
        if months is not None:
            months.contents.value = self._defaults['GetExtCalRecommendedInterval']['months']
        return self._defaults['GetExtCalRecommendedInterval']['return']

    def niDCPower_GetLCRCompensationData(self, vi, channel_name, compensation_data_size, compensation_data):  # noqa: N802
        if self._defaults['GetLCRCompensationData']['return'] != 0:
            return self._defaults['GetLCRCompensationData']['return']
        # compensation_data
        if self._defaults['GetLCRCompensationData']['compensationData'] is None:
            raise MockFunctionCallError("niDCPower_GetLCRCompensationData", param='compensationData')
        if compensation_data_size.value == 0:
            return len(self._defaults['GetLCRCompensationData']['compensationData'])
        try:
            compensation_data_ref = compensation_data.contents
        except AttributeError:
            compensation_data_ref = compensation_data
        for i in range(len(self._defaults['GetLCRCompensationData']['compensationData'])):
            compensation_data_ref[i] = self._defaults['GetLCRCompensationData']['compensationData'][i]
        return self._defaults['GetLCRCompensationData']['return']

    def niDCPower_GetLCRCompensationLastDateAndTime(self, vi, channel_name, compensation_type, year, month, day, hour, minute):  # noqa: N802
        if self._defaults['GetLCRCompensationLastDateAndTime']['return'] != 0:
            return self._defaults['GetLCRCompensationLastDateAndTime']['return']
        # year
        if self._defaults['GetLCRCompensationLastDateAndTime']['year'] is None:
            raise MockFunctionCallError("niDCPower_GetLCRCompensationLastDateAndTime", param='year')
        if year is not None:
            year.contents.value = self._defaults['GetLCRCompensationLastDateAndTime']['year']
        # month
        if self._defaults['GetLCRCompensationLastDateAndTime']['month'] is None:
            raise MockFunctionCallError("niDCPower_GetLCRCompensationLastDateAndTime", param='month')
        if month is not None:
            month.contents.value = self._defaults['GetLCRCompensationLastDateAndTime']['month']
        # day
        if self._defaults['GetLCRCompensationLastDateAndTime']['day'] is None:
            raise MockFunctionCallError("niDCPower_GetLCRCompensationLastDateAndTime", param='day')
        if day is not None:
            day.contents.value = self._defaults['GetLCRCompensationLastDateAndTime']['day']
        # hour
        if self._defaults['GetLCRCompensationLastDateAndTime']['hour'] is None:
            raise MockFunctionCallError("niDCPower_GetLCRCompensationLastDateAndTime", param='hour')
        if hour is not None:
            hour.contents.value = self._defaults['GetLCRCompensationLastDateAndTime']['hour']
        # minute
        if self._defaults['GetLCRCompensationLastDateAndTime']['minute'] is None:
            raise MockFunctionCallError("niDCPower_GetLCRCompensationLastDateAndTime", param='minute')
        if minute is not None:
            minute.contents.value = self._defaults['GetLCRCompensationLastDateAndTime']['minute']
        return self._defaults['GetLCRCompensationLastDateAndTime']['return']

    def niDCPower_GetLCRCustomCableCompensationData(self, vi, channel_name, custom_cable_compensation_data_size, custom_cable_compensation_data):  # noqa: N802
        if self._defaults['GetLCRCustomCableCompensationData']['return'] != 0:
            return self._defaults['GetLCRCustomCableCompensationData']['return']
        # custom_cable_compensation_data
        if self._defaults['GetLCRCustomCableCompensationData']['customCableCompensationData'] is None:
            raise MockFunctionCallError("niDCPower_GetLCRCustomCableCompensationData", param='customCableCompensationData')
        if custom_cable_compensation_data_size.value == 0:
            return len(self._defaults['GetLCRCustomCableCompensationData']['customCableCompensationData'])
        try:
            custom_cable_compensation_data_ref = custom_cable_compensation_data.contents
        except AttributeError:
            custom_cable_compensation_data_ref = custom_cable_compensation_data
        for i in range(len(self._defaults['GetLCRCustomCableCompensationData']['customCableCompensationData'])):
            custom_cable_compensation_data_ref[i] = self._defaults['GetLCRCustomCableCompensationData']['customCableCompensationData'][i]
        return self._defaults['GetLCRCustomCableCompensationData']['return']

    def niDCPower_GetSelfCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        if self._defaults['GetSelfCalLastDateAndTime']['return'] != 0:
            return self._defaults['GetSelfCalLastDateAndTime']['return']
        # year
        if self._defaults['GetSelfCalLastDateAndTime']['year'] is None:
            raise MockFunctionCallError("niDCPower_GetSelfCalLastDateAndTime", param='year')
        if year is not None:
            year.contents.value = self._defaults['GetSelfCalLastDateAndTime']['year']
        # month
        if self._defaults['GetSelfCalLastDateAndTime']['month'] is None:
            raise MockFunctionCallError("niDCPower_GetSelfCalLastDateAndTime", param='month')
        if month is not None:
            month.contents.value = self._defaults['GetSelfCalLastDateAndTime']['month']
        # day
        if self._defaults['GetSelfCalLastDateAndTime']['day'] is None:
            raise MockFunctionCallError("niDCPower_GetSelfCalLastDateAndTime", param='day')
        if day is not None:
            day.contents.value = self._defaults['GetSelfCalLastDateAndTime']['day']
        # hour
        if self._defaults['GetSelfCalLastDateAndTime']['hour'] is None:
            raise MockFunctionCallError("niDCPower_GetSelfCalLastDateAndTime", param='hour')
        if hour is not None:
            hour.contents.value = self._defaults['GetSelfCalLastDateAndTime']['hour']
        # minute
        if self._defaults['GetSelfCalLastDateAndTime']['minute'] is None:
            raise MockFunctionCallError("niDCPower_GetSelfCalLastDateAndTime", param='minute')
        if minute is not None:
            minute.contents.value = self._defaults['GetSelfCalLastDateAndTime']['minute']
        return self._defaults['GetSelfCalLastDateAndTime']['return']

    def niDCPower_GetSelfCalLastTemp(self, vi, temperature):  # noqa: N802
        if self._defaults['GetSelfCalLastTemp']['return'] != 0:
            return self._defaults['GetSelfCalLastTemp']['return']
        # temperature
        if self._defaults['GetSelfCalLastTemp']['temperature'] is None:
            raise MockFunctionCallError("niDCPower_GetSelfCalLastTemp", param='temperature')
        if temperature is not None:
            temperature.contents.value = self._defaults['GetSelfCalLastTemp']['temperature']
        return self._defaults['GetSelfCalLastTemp']['return']

    def niDCPower_ImportAttributeConfigurationBuffer(self, vi, size, configuration):  # noqa: N802
        if self._defaults['ImportAttributeConfigurationBuffer']['return'] != 0:
            return self._defaults['ImportAttributeConfigurationBuffer']['return']
        return self._defaults['ImportAttributeConfigurationBuffer']['return']

    def niDCPower_ImportAttributeConfigurationFile(self, vi, file_path):  # noqa: N802
        if self._defaults['ImportAttributeConfigurationFile']['return'] != 0:
            return self._defaults['ImportAttributeConfigurationFile']['return']
        return self._defaults['ImportAttributeConfigurationFile']['return']

    def niDCPower_InitializeWithChannels(self, resource_name, channels, reset, option_string, vi):  # noqa: N802
        if self._defaults['InitializeWithChannels']['return'] != 0:
            return self._defaults['InitializeWithChannels']['return']
        # vi
        if self._defaults['InitializeWithChannels']['vi'] is None:
            raise MockFunctionCallError("niDCPower_InitializeWithChannels", param='vi')
        if vi is not None:
            vi.contents.value = self._defaults['InitializeWithChannels']['vi']
        return self._defaults['InitializeWithChannels']['return']

    def niDCPower_InitializeWithIndependentChannels(self, resource_name, reset, option_string, vi):  # noqa: N802
        if self._defaults['InitializeWithIndependentChannels']['return'] != 0:
            return self._defaults['InitializeWithIndependentChannels']['return']
        # vi
        if self._defaults['InitializeWithIndependentChannels']['vi'] is None:
            raise MockFunctionCallError("niDCPower_InitializeWithIndependentChannels", param='vi')
        if vi is not None:
            vi.contents.value = self._defaults['InitializeWithIndependentChannels']['vi']
        return self._defaults['InitializeWithIndependentChannels']['return']

    def niDCPower_InitiateWithChannels(self, vi, channel_name):  # noqa: N802
        if self._defaults['InitiateWithChannels']['return'] != 0:
            return self._defaults['InitiateWithChannels']['return']
        return self._defaults['InitiateWithChannels']['return']

    def niDCPower_LockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['LockSession']['return'] != 0:
            return self._defaults['LockSession']['return']
        # caller_has_lock
        if self._defaults['LockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niDCPower_LockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['LockSession']['callerHasLock']
        return self._defaults['LockSession']['return']

    def niDCPower_Measure(self, vi, channel_name, measurement_type, measurement):  # noqa: N802
        if self._defaults['Measure']['return'] != 0:
            return self._defaults['Measure']['return']
        # measurement
        if self._defaults['Measure']['measurement'] is None:
            raise MockFunctionCallError("niDCPower_Measure", param='measurement')
        if measurement is not None:
            measurement.contents.value = self._defaults['Measure']['measurement']
        return self._defaults['Measure']['return']

    def niDCPower_MeasureMultiple(self, vi, channel_name, voltage_measurements, current_measurements):  # noqa: N802
        if self._defaults['MeasureMultiple']['return'] != 0:
            return self._defaults['MeasureMultiple']['return']
        # voltage_measurements
        if self._defaults['MeasureMultiple']['voltageMeasurements'] is None:
            raise MockFunctionCallError("niDCPower_MeasureMultiple", param='voltageMeasurements')
        test_value = self._defaults['MeasureMultiple']['voltageMeasurements']
        try:
            voltage_measurements_ref = voltage_measurements.contents
        except AttributeError:
            voltage_measurements_ref = voltage_measurements
        assert len(voltage_measurements_ref) >= len(test_value)
        for i in range(len(test_value)):
            voltage_measurements_ref[i] = test_value[i]
        # current_measurements
        if self._defaults['MeasureMultiple']['currentMeasurements'] is None:
            raise MockFunctionCallError("niDCPower_MeasureMultiple", param='currentMeasurements')
        test_value = self._defaults['MeasureMultiple']['currentMeasurements']
        try:
            current_measurements_ref = current_measurements.contents
        except AttributeError:
            current_measurements_ref = current_measurements
        assert len(current_measurements_ref) >= len(test_value)
        for i in range(len(test_value)):
            current_measurements_ref[i] = test_value[i]
        return self._defaults['MeasureMultiple']['return']

    def niDCPower_MeasureMultipleLCR(self, vi, channel_name, measurements):  # noqa: N802
        if self._defaults['MeasureMultipleLCR']['return'] != 0:
            return self._defaults['MeasureMultipleLCR']['return']
        # measurements
        if self._defaults['MeasureMultipleLCR']['measurements'] is None:
            raise MockFunctionCallError("niDCPower_MeasureMultipleLCR", param='measurements')
        test_value = self._defaults['MeasureMultipleLCR']['measurements']
        try:
            measurements_ref = measurements.contents
        except AttributeError:
            measurements_ref = measurements
        assert len(measurements_ref) >= len(test_value)
        for i in range(len(test_value)):
            measurements_ref[i] = test_value[i]
        return self._defaults['MeasureMultipleLCR']['return']

    def niDCPower_ParseChannelCount(self, vi, channels_string, number_of_channels):  # noqa: N802
        if self._defaults['ParseChannelCount']['return'] != 0:
            return self._defaults['ParseChannelCount']['return']
        # number_of_channels
        if self._defaults['ParseChannelCount']['numberOfChannels'] is None:
            raise MockFunctionCallError("niDCPower_ParseChannelCount", param='numberOfChannels')
        if number_of_channels is not None:
            number_of_channels.contents.value = self._defaults['ParseChannelCount']['numberOfChannels']
        return self._defaults['ParseChannelCount']['return']

    def niDCPower_PerformLCRLoadCompensation(self, vi, channel_name, num_compensation_spots, compensation_spots):  # noqa: N802
        if self._defaults['PerformLCRLoadCompensation']['return'] != 0:
            return self._defaults['PerformLCRLoadCompensation']['return']
        return self._defaults['PerformLCRLoadCompensation']['return']

    def niDCPower_PerformLCROpenCompensation(self, vi, channel_name, num_frequencies, additional_frequencies):  # noqa: N802
        if self._defaults['PerformLCROpenCompensation']['return'] != 0:
            return self._defaults['PerformLCROpenCompensation']['return']
        return self._defaults['PerformLCROpenCompensation']['return']

    def niDCPower_PerformLCROpenCustomCableCompensation(self, vi, channel_name):  # noqa: N802
        if self._defaults['PerformLCROpenCustomCableCompensation']['return'] != 0:
            return self._defaults['PerformLCROpenCustomCableCompensation']['return']
        return self._defaults['PerformLCROpenCustomCableCompensation']['return']

    def niDCPower_PerformLCRShortCompensation(self, vi, channel_name, num_frequencies, additional_frequencies):  # noqa: N802
        if self._defaults['PerformLCRShortCompensation']['return'] != 0:
            return self._defaults['PerformLCRShortCompensation']['return']
        return self._defaults['PerformLCRShortCompensation']['return']

    def niDCPower_PerformLCRShortCustomCableCompensation(self, vi, channel_name):  # noqa: N802
        if self._defaults['PerformLCRShortCustomCableCompensation']['return'] != 0:
            return self._defaults['PerformLCRShortCustomCableCompensation']['return']
        return self._defaults['PerformLCRShortCustomCableCompensation']['return']

    def niDCPower_QueryInCompliance(self, vi, channel_name, in_compliance):  # noqa: N802
        if self._defaults['QueryInCompliance']['return'] != 0:
            return self._defaults['QueryInCompliance']['return']
        # in_compliance
        if self._defaults['QueryInCompliance']['inCompliance'] is None:
            raise MockFunctionCallError("niDCPower_QueryInCompliance", param='inCompliance')
        if in_compliance is not None:
            in_compliance.contents.value = self._defaults['QueryInCompliance']['inCompliance']
        return self._defaults['QueryInCompliance']['return']

    def niDCPower_QueryLatchedOutputCutoffState(self, vi, channel_name, output_cutoff_reason, output_cutoff_state):  # noqa: N802
        if self._defaults['QueryLatchedOutputCutoffState']['return'] != 0:
            return self._defaults['QueryLatchedOutputCutoffState']['return']
        # output_cutoff_state
        if self._defaults['QueryLatchedOutputCutoffState']['outputCutoffState'] is None:
            raise MockFunctionCallError("niDCPower_QueryLatchedOutputCutoffState", param='outputCutoffState')
        if output_cutoff_state is not None:
            output_cutoff_state.contents.value = self._defaults['QueryLatchedOutputCutoffState']['outputCutoffState']
        return self._defaults['QueryLatchedOutputCutoffState']['return']

    def niDCPower_QueryMaxCurrentLimit(self, vi, channel_name, voltage_level, max_current_limit):  # noqa: N802
        if self._defaults['QueryMaxCurrentLimit']['return'] != 0:
            return self._defaults['QueryMaxCurrentLimit']['return']
        # max_current_limit
        if self._defaults['QueryMaxCurrentLimit']['maxCurrentLimit'] is None:
            raise MockFunctionCallError("niDCPower_QueryMaxCurrentLimit", param='maxCurrentLimit')
        if max_current_limit is not None:
            max_current_limit.contents.value = self._defaults['QueryMaxCurrentLimit']['maxCurrentLimit']
        return self._defaults['QueryMaxCurrentLimit']['return']

    def niDCPower_QueryMaxVoltageLevel(self, vi, channel_name, current_limit, max_voltage_level):  # noqa: N802
        if self._defaults['QueryMaxVoltageLevel']['return'] != 0:
            return self._defaults['QueryMaxVoltageLevel']['return']
        # max_voltage_level
        if self._defaults['QueryMaxVoltageLevel']['maxVoltageLevel'] is None:
            raise MockFunctionCallError("niDCPower_QueryMaxVoltageLevel", param='maxVoltageLevel')
        if max_voltage_level is not None:
            max_voltage_level.contents.value = self._defaults['QueryMaxVoltageLevel']['maxVoltageLevel']
        return self._defaults['QueryMaxVoltageLevel']['return']

    def niDCPower_QueryMinCurrentLimit(self, vi, channel_name, voltage_level, min_current_limit):  # noqa: N802
        if self._defaults['QueryMinCurrentLimit']['return'] != 0:
            return self._defaults['QueryMinCurrentLimit']['return']
        # min_current_limit
        if self._defaults['QueryMinCurrentLimit']['minCurrentLimit'] is None:
            raise MockFunctionCallError("niDCPower_QueryMinCurrentLimit", param='minCurrentLimit')
        if min_current_limit is not None:
            min_current_limit.contents.value = self._defaults['QueryMinCurrentLimit']['minCurrentLimit']
        return self._defaults['QueryMinCurrentLimit']['return']

    def niDCPower_QueryOutputState(self, vi, channel_name, output_state, in_state):  # noqa: N802
        if self._defaults['QueryOutputState']['return'] != 0:
            return self._defaults['QueryOutputState']['return']
        # in_state
        if self._defaults['QueryOutputState']['inState'] is None:
            raise MockFunctionCallError("niDCPower_QueryOutputState", param='inState')
        if in_state is not None:
            in_state.contents.value = self._defaults['QueryOutputState']['inState']
        return self._defaults['QueryOutputState']['return']

    def niDCPower_ReadCurrentTemperature(self, vi, temperature):  # noqa: N802
        if self._defaults['ReadCurrentTemperature']['return'] != 0:
            return self._defaults['ReadCurrentTemperature']['return']
        # temperature
        if self._defaults['ReadCurrentTemperature']['temperature'] is None:
            raise MockFunctionCallError("niDCPower_ReadCurrentTemperature", param='temperature')
        if temperature is not None:
            temperature.contents.value = self._defaults['ReadCurrentTemperature']['temperature']
        return self._defaults['ReadCurrentTemperature']['return']

    def niDCPower_ResetDevice(self, vi):  # noqa: N802
        if self._defaults['ResetDevice']['return'] != 0:
            return self._defaults['ResetDevice']['return']
        return self._defaults['ResetDevice']['return']

    def niDCPower_ResetWithChannels(self, vi, channel_name):  # noqa: N802
        if self._defaults['ResetWithChannels']['return'] != 0:
            return self._defaults['ResetWithChannels']['return']
        return self._defaults['ResetWithChannels']['return']

    def niDCPower_ResetWithDefaults(self, vi):  # noqa: N802
        if self._defaults['ResetWithDefaults']['return'] != 0:
            return self._defaults['ResetWithDefaults']['return']
        return self._defaults['ResetWithDefaults']['return']

    def niDCPower_SendSoftwareEdgeTriggerWithChannels(self, vi, channel_name, trigger):  # noqa: N802
        if self._defaults['SendSoftwareEdgeTriggerWithChannels']['return'] != 0:
            return self._defaults['SendSoftwareEdgeTriggerWithChannels']['return']
        return self._defaults['SendSoftwareEdgeTriggerWithChannels']['return']

    def niDCPower_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViBoolean']['return'] != 0:
            return self._defaults['SetAttributeViBoolean']['return']
        return self._defaults['SetAttributeViBoolean']['return']

    def niDCPower_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViInt32']['return'] != 0:
            return self._defaults['SetAttributeViInt32']['return']
        return self._defaults['SetAttributeViInt32']['return']

    def niDCPower_SetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViInt64']['return'] != 0:
            return self._defaults['SetAttributeViInt64']['return']
        return self._defaults['SetAttributeViInt64']['return']

    def niDCPower_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViReal64']['return'] != 0:
            return self._defaults['SetAttributeViReal64']['return']
        return self._defaults['SetAttributeViReal64']['return']

    def niDCPower_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViString']['return'] != 0:
            return self._defaults['SetAttributeViString']['return']
        return self._defaults['SetAttributeViString']['return']

    def niDCPower_SetRuntimeEnvironment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        if self._defaults['SetRuntimeEnvironment']['return'] != 0:
            return self._defaults['SetRuntimeEnvironment']['return']
        return self._defaults['SetRuntimeEnvironment']['return']

    def niDCPower_SetSequence(self, vi, channel_name, values, source_delays, size):  # noqa: N802
        if self._defaults['SetSequence']['return'] != 0:
            return self._defaults['SetSequence']['return']
        return self._defaults['SetSequence']['return']

    def niDCPower_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['UnlockSession']['return'] != 0:
            return self._defaults['UnlockSession']['return']
        # caller_has_lock
        if self._defaults['UnlockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niDCPower_UnlockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['UnlockSession']['callerHasLock']
        return self._defaults['UnlockSession']['return']

    def niDCPower_WaitForEventWithChannels(self, vi, channel_name, event_id, timeout):  # noqa: N802
        if self._defaults['WaitForEventWithChannels']['return'] != 0:
            return self._defaults['WaitForEventWithChannels']['return']
        return self._defaults['WaitForEventWithChannels']['return']

    def niDCPower_close(self, vi):  # noqa: N802
        if self._defaults['close']['return'] != 0:
            return self._defaults['close']['return']
        return self._defaults['close']['return']

    def niDCPower_error_message(self, vi, error_code, error_message):  # noqa: N802
        if self._defaults['error_message']['return'] != 0:
            return self._defaults['error_message']['return']
        # error_message
        if self._defaults['error_message']['errorMessage'] is None:
            raise MockFunctionCallError("niDCPower_error_message", param='errorMessage')
        test_value = self._defaults['error_message']['errorMessage']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(error_message) >= len(test_value)
        for i in range(len(test_value)):
            error_message[i] = test_value[i]
        return self._defaults['error_message']['return']

    def niDCPower_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        if self._defaults['self_test']['return'] != 0:
            return self._defaults['self_test']['return']
        # self_test_result
        if self._defaults['self_test']['selfTestResult'] is None:
            raise MockFunctionCallError("niDCPower_self_test", param='selfTestResult')
        if self_test_result is not None:
            self_test_result.contents.value = self._defaults['self_test']['selfTestResult']
        # self_test_message
        if self._defaults['self_test']['selfTestMessage'] is None:
            raise MockFunctionCallError("niDCPower_self_test", param='selfTestMessage')
        test_value = self._defaults['self_test']['selfTestMessage']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(self_test_message) >= len(test_value)
        for i in range(len(test_value)):
            self_test_message[i] = test_value[i]
        return self._defaults['self_test']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niDCPower_AbortWithChannels.side_effect = MockFunctionCallError("niDCPower_AbortWithChannels")
        mock_library.niDCPower_AbortWithChannels.return_value = 0
        mock_library.niDCPower_CalSelfCalibrate.side_effect = MockFunctionCallError("niDCPower_CalSelfCalibrate")
        mock_library.niDCPower_CalSelfCalibrate.return_value = 0
        mock_library.niDCPower_ClearLatchedOutputCutoffState.side_effect = MockFunctionCallError("niDCPower_ClearLatchedOutputCutoffState")
        mock_library.niDCPower_ClearLatchedOutputCutoffState.return_value = 0
        mock_library.niDCPower_CommitWithChannels.side_effect = MockFunctionCallError("niDCPower_CommitWithChannels")
        mock_library.niDCPower_CommitWithChannels.return_value = 0
        mock_library.niDCPower_ConfigureApertureTime.side_effect = MockFunctionCallError("niDCPower_ConfigureApertureTime")
        mock_library.niDCPower_ConfigureApertureTime.return_value = 0
        mock_library.niDCPower_ConfigureLCRCompensation.side_effect = MockFunctionCallError("niDCPower_ConfigureLCRCompensation")
        mock_library.niDCPower_ConfigureLCRCompensation.return_value = 0
        mock_library.niDCPower_ConfigureLCRCustomCableCompensation.side_effect = MockFunctionCallError("niDCPower_ConfigureLCRCustomCableCompensation")
        mock_library.niDCPower_ConfigureLCRCustomCableCompensation.return_value = 0
        mock_library.niDCPower_CreateAdvancedSequenceCommitStepWithChannels.side_effect = MockFunctionCallError("niDCPower_CreateAdvancedSequenceCommitStepWithChannels")
        mock_library.niDCPower_CreateAdvancedSequenceCommitStepWithChannels.return_value = 0
        mock_library.niDCPower_CreateAdvancedSequenceStepWithChannels.side_effect = MockFunctionCallError("niDCPower_CreateAdvancedSequenceStepWithChannels")
        mock_library.niDCPower_CreateAdvancedSequenceStepWithChannels.return_value = 0
        mock_library.niDCPower_CreateAdvancedSequenceWithChannels.side_effect = MockFunctionCallError("niDCPower_CreateAdvancedSequenceWithChannels")
        mock_library.niDCPower_CreateAdvancedSequenceWithChannels.return_value = 0
        mock_library.niDCPower_DeleteAdvancedSequenceWithChannels.side_effect = MockFunctionCallError("niDCPower_DeleteAdvancedSequenceWithChannels")
        mock_library.niDCPower_DeleteAdvancedSequenceWithChannels.return_value = 0
        mock_library.niDCPower_Disable.side_effect = MockFunctionCallError("niDCPower_Disable")
        mock_library.niDCPower_Disable.return_value = 0
        mock_library.niDCPower_ExportAttributeConfigurationBuffer.side_effect = MockFunctionCallError("niDCPower_ExportAttributeConfigurationBuffer")
        mock_library.niDCPower_ExportAttributeConfigurationBuffer.return_value = 0
        mock_library.niDCPower_ExportAttributeConfigurationFile.side_effect = MockFunctionCallError("niDCPower_ExportAttributeConfigurationFile")
        mock_library.niDCPower_ExportAttributeConfigurationFile.return_value = 0
        mock_library.niDCPower_FancyInitialize.side_effect = MockFunctionCallError("niDCPower_FancyInitialize")
        mock_library.niDCPower_FancyInitialize.return_value = 0
        mock_library.niDCPower_FetchMultiple.side_effect = MockFunctionCallError("niDCPower_FetchMultiple")
        mock_library.niDCPower_FetchMultiple.return_value = 0
        mock_library.niDCPower_FetchMultipleLCR.side_effect = MockFunctionCallError("niDCPower_FetchMultipleLCR")
        mock_library.niDCPower_FetchMultipleLCR.return_value = 0
        mock_library.niDCPower_GetAttributeViBoolean.side_effect = MockFunctionCallError("niDCPower_GetAttributeViBoolean")
        mock_library.niDCPower_GetAttributeViBoolean.return_value = 0
        mock_library.niDCPower_GetAttributeViInt32.side_effect = MockFunctionCallError("niDCPower_GetAttributeViInt32")
        mock_library.niDCPower_GetAttributeViInt32.return_value = 0
        mock_library.niDCPower_GetAttributeViInt64.side_effect = MockFunctionCallError("niDCPower_GetAttributeViInt64")
        mock_library.niDCPower_GetAttributeViInt64.return_value = 0
        mock_library.niDCPower_GetAttributeViReal64.side_effect = MockFunctionCallError("niDCPower_GetAttributeViReal64")
        mock_library.niDCPower_GetAttributeViReal64.return_value = 0
        mock_library.niDCPower_GetAttributeViString.side_effect = MockFunctionCallError("niDCPower_GetAttributeViString")
        mock_library.niDCPower_GetAttributeViString.return_value = 0
        mock_library.niDCPower_GetChannelName.side_effect = MockFunctionCallError("niDCPower_GetChannelName")
        mock_library.niDCPower_GetChannelName.return_value = 0
        mock_library.niDCPower_GetChannelNameFromString.side_effect = MockFunctionCallError("niDCPower_GetChannelNameFromString")
        mock_library.niDCPower_GetChannelNameFromString.return_value = 0
        mock_library.niDCPower_GetError.side_effect = MockFunctionCallError("niDCPower_GetError")
        mock_library.niDCPower_GetError.return_value = 0
        mock_library.niDCPower_GetExtCalLastDateAndTime.side_effect = MockFunctionCallError("niDCPower_GetExtCalLastDateAndTime")
        mock_library.niDCPower_GetExtCalLastDateAndTime.return_value = 0
        mock_library.niDCPower_GetExtCalLastTemp.side_effect = MockFunctionCallError("niDCPower_GetExtCalLastTemp")
        mock_library.niDCPower_GetExtCalLastTemp.return_value = 0
        mock_library.niDCPower_GetExtCalRecommendedInterval.side_effect = MockFunctionCallError("niDCPower_GetExtCalRecommendedInterval")
        mock_library.niDCPower_GetExtCalRecommendedInterval.return_value = 0
        mock_library.niDCPower_GetLCRCompensationData.side_effect = MockFunctionCallError("niDCPower_GetLCRCompensationData")
        mock_library.niDCPower_GetLCRCompensationData.return_value = 0
        mock_library.niDCPower_GetLCRCompensationLastDateAndTime.side_effect = MockFunctionCallError("niDCPower_GetLCRCompensationLastDateAndTime")
        mock_library.niDCPower_GetLCRCompensationLastDateAndTime.return_value = 0
        mock_library.niDCPower_GetLCRCustomCableCompensationData.side_effect = MockFunctionCallError("niDCPower_GetLCRCustomCableCompensationData")
        mock_library.niDCPower_GetLCRCustomCableCompensationData.return_value = 0
        mock_library.niDCPower_GetSelfCalLastDateAndTime.side_effect = MockFunctionCallError("niDCPower_GetSelfCalLastDateAndTime")
        mock_library.niDCPower_GetSelfCalLastDateAndTime.return_value = 0
        mock_library.niDCPower_GetSelfCalLastTemp.side_effect = MockFunctionCallError("niDCPower_GetSelfCalLastTemp")
        mock_library.niDCPower_GetSelfCalLastTemp.return_value = 0
        mock_library.niDCPower_ImportAttributeConfigurationBuffer.side_effect = MockFunctionCallError("niDCPower_ImportAttributeConfigurationBuffer")
        mock_library.niDCPower_ImportAttributeConfigurationBuffer.return_value = 0
        mock_library.niDCPower_ImportAttributeConfigurationFile.side_effect = MockFunctionCallError("niDCPower_ImportAttributeConfigurationFile")
        mock_library.niDCPower_ImportAttributeConfigurationFile.return_value = 0
        mock_library.niDCPower_InitializeWithChannels.side_effect = MockFunctionCallError("niDCPower_InitializeWithChannels")
        mock_library.niDCPower_InitializeWithChannels.return_value = 0
        mock_library.niDCPower_InitializeWithIndependentChannels.side_effect = MockFunctionCallError("niDCPower_InitializeWithIndependentChannels")
        mock_library.niDCPower_InitializeWithIndependentChannels.return_value = 0
        mock_library.niDCPower_InitiateWithChannels.side_effect = MockFunctionCallError("niDCPower_InitiateWithChannels")
        mock_library.niDCPower_InitiateWithChannels.return_value = 0
        mock_library.niDCPower_LockSession.side_effect = MockFunctionCallError("niDCPower_LockSession")
        mock_library.niDCPower_LockSession.return_value = 0
        mock_library.niDCPower_Measure.side_effect = MockFunctionCallError("niDCPower_Measure")
        mock_library.niDCPower_Measure.return_value = 0
        mock_library.niDCPower_MeasureMultiple.side_effect = MockFunctionCallError("niDCPower_MeasureMultiple")
        mock_library.niDCPower_MeasureMultiple.return_value = 0
        mock_library.niDCPower_MeasureMultipleLCR.side_effect = MockFunctionCallError("niDCPower_MeasureMultipleLCR")
        mock_library.niDCPower_MeasureMultipleLCR.return_value = 0
        mock_library.niDCPower_ParseChannelCount.side_effect = MockFunctionCallError("niDCPower_ParseChannelCount")
        mock_library.niDCPower_ParseChannelCount.return_value = 0
        mock_library.niDCPower_PerformLCRLoadCompensation.side_effect = MockFunctionCallError("niDCPower_PerformLCRLoadCompensation")
        mock_library.niDCPower_PerformLCRLoadCompensation.return_value = 0
        mock_library.niDCPower_PerformLCROpenCompensation.side_effect = MockFunctionCallError("niDCPower_PerformLCROpenCompensation")
        mock_library.niDCPower_PerformLCROpenCompensation.return_value = 0
        mock_library.niDCPower_PerformLCROpenCustomCableCompensation.side_effect = MockFunctionCallError("niDCPower_PerformLCROpenCustomCableCompensation")
        mock_library.niDCPower_PerformLCROpenCustomCableCompensation.return_value = 0
        mock_library.niDCPower_PerformLCRShortCompensation.side_effect = MockFunctionCallError("niDCPower_PerformLCRShortCompensation")
        mock_library.niDCPower_PerformLCRShortCompensation.return_value = 0
        mock_library.niDCPower_PerformLCRShortCustomCableCompensation.side_effect = MockFunctionCallError("niDCPower_PerformLCRShortCustomCableCompensation")
        mock_library.niDCPower_PerformLCRShortCustomCableCompensation.return_value = 0
        mock_library.niDCPower_QueryInCompliance.side_effect = MockFunctionCallError("niDCPower_QueryInCompliance")
        mock_library.niDCPower_QueryInCompliance.return_value = 0
        mock_library.niDCPower_QueryLatchedOutputCutoffState.side_effect = MockFunctionCallError("niDCPower_QueryLatchedOutputCutoffState")
        mock_library.niDCPower_QueryLatchedOutputCutoffState.return_value = 0
        mock_library.niDCPower_QueryMaxCurrentLimit.side_effect = MockFunctionCallError("niDCPower_QueryMaxCurrentLimit")
        mock_library.niDCPower_QueryMaxCurrentLimit.return_value = 0
        mock_library.niDCPower_QueryMaxVoltageLevel.side_effect = MockFunctionCallError("niDCPower_QueryMaxVoltageLevel")
        mock_library.niDCPower_QueryMaxVoltageLevel.return_value = 0
        mock_library.niDCPower_QueryMinCurrentLimit.side_effect = MockFunctionCallError("niDCPower_QueryMinCurrentLimit")
        mock_library.niDCPower_QueryMinCurrentLimit.return_value = 0
        mock_library.niDCPower_QueryOutputState.side_effect = MockFunctionCallError("niDCPower_QueryOutputState")
        mock_library.niDCPower_QueryOutputState.return_value = 0
        mock_library.niDCPower_ReadCurrentTemperature.side_effect = MockFunctionCallError("niDCPower_ReadCurrentTemperature")
        mock_library.niDCPower_ReadCurrentTemperature.return_value = 0
        mock_library.niDCPower_ResetDevice.side_effect = MockFunctionCallError("niDCPower_ResetDevice")
        mock_library.niDCPower_ResetDevice.return_value = 0
        mock_library.niDCPower_ResetWithChannels.side_effect = MockFunctionCallError("niDCPower_ResetWithChannels")
        mock_library.niDCPower_ResetWithChannels.return_value = 0
        mock_library.niDCPower_ResetWithDefaults.side_effect = MockFunctionCallError("niDCPower_ResetWithDefaults")
        mock_library.niDCPower_ResetWithDefaults.return_value = 0
        mock_library.niDCPower_SendSoftwareEdgeTriggerWithChannels.side_effect = MockFunctionCallError("niDCPower_SendSoftwareEdgeTriggerWithChannels")
        mock_library.niDCPower_SendSoftwareEdgeTriggerWithChannels.return_value = 0
        mock_library.niDCPower_SetAttributeViBoolean.side_effect = MockFunctionCallError("niDCPower_SetAttributeViBoolean")
        mock_library.niDCPower_SetAttributeViBoolean.return_value = 0
        mock_library.niDCPower_SetAttributeViInt32.side_effect = MockFunctionCallError("niDCPower_SetAttributeViInt32")
        mock_library.niDCPower_SetAttributeViInt32.return_value = 0
        mock_library.niDCPower_SetAttributeViInt64.side_effect = MockFunctionCallError("niDCPower_SetAttributeViInt64")
        mock_library.niDCPower_SetAttributeViInt64.return_value = 0
        mock_library.niDCPower_SetAttributeViReal64.side_effect = MockFunctionCallError("niDCPower_SetAttributeViReal64")
        mock_library.niDCPower_SetAttributeViReal64.return_value = 0
        mock_library.niDCPower_SetAttributeViString.side_effect = MockFunctionCallError("niDCPower_SetAttributeViString")
        mock_library.niDCPower_SetAttributeViString.return_value = 0
        mock_library.niDCPower_SetRuntimeEnvironment.side_effect = MockFunctionCallError("niDCPower_SetRuntimeEnvironment")
        mock_library.niDCPower_SetRuntimeEnvironment.return_value = 0
        mock_library.niDCPower_SetSequence.side_effect = MockFunctionCallError("niDCPower_SetSequence")
        mock_library.niDCPower_SetSequence.return_value = 0
        mock_library.niDCPower_UnlockSession.side_effect = MockFunctionCallError("niDCPower_UnlockSession")
        mock_library.niDCPower_UnlockSession.return_value = 0
        mock_library.niDCPower_WaitForEventWithChannels.side_effect = MockFunctionCallError("niDCPower_WaitForEventWithChannels")
        mock_library.niDCPower_WaitForEventWithChannels.return_value = 0
        mock_library.niDCPower_close.side_effect = MockFunctionCallError("niDCPower_close")
        mock_library.niDCPower_close.return_value = 0
        mock_library.niDCPower_error_message.side_effect = MockFunctionCallError("niDCPower_error_message")
        mock_library.niDCPower_error_message.return_value = 0
        mock_library.niDCPower_self_test.side_effect = MockFunctionCallError("niDCPower_self_test")
        mock_library.niDCPower_self_test.return_value = 0
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidcpower/nidcpower/unit_tests/test_nidcpower.py sha256=32baf6ad91b702f6b890098126c8c10796886a78be8180a5a2815317e9311dda bytes=13216 -->
## FILE: generated/nidcpower/nidcpower/unit_tests/test_nidcpower.py

- repository: `ni/nimi-python`
- source_path: `generated/nidcpower/nidcpower/unit_tests/test_nidcpower.py`
- sha256: `32baf6ad91b702f6b890098126c8c10796886a78be8180a5a2815317e9311dda`
- bytes: 13216

````python
import cmath
import platform
import pytest

import nidcpower


@pytest.mark.parametrize(
    "ctype_members, channel, expected_python_members, expected_python_str",
    [
        (
            # ctype_members
            {
                "vdc": 0.1,
                "idc": 0.001,
                "stimulus_frequency": 10_000.0,
                "ac_voltage_real": 1.0,
                "ac_voltage_imaginary": 0.1,
                "ac_current_real": 0.01,
                "ac_current_imaginary": 0.001,
                "z_real": 100.0,
                "z_imaginary": 10.0,
                "z_magnitude": 100.49876,
                "z_phase": 5.7105931375,
                "y_real": 0.0099009901,
                "y_imaginary": -0.00099009901,
                "y_magnitude": 0.0099503719,
                "y_phase": -5.7105931375,
                "ls": 10.0,
                "cs": 20.0,
                "rs": 90.0,
                "lp": 30.0,
                "cp": 40.0,
                "rp": 110.0,
                "d": 10.0,
                "q": 0.1,
                "measurement_mode": nidcpower.InstrumentMode.SMU_PS.value,
                "dc_in_compliance": True,
                "ac_in_compliance": True,
                "unbalanced": True,
            },
            # channel
            "Dev1/0",
            # expected_python_members
            {
                "channel": "Dev1/0",
                "vdc": 0.1,
                "idc": 0.001,
                "stimulus_frequency": 10_000.0,
                "ac_voltage": complex(1.0, 0.1),
                "ac_current": complex(0.01, 0.001),
                "z": complex(100.0, 10.0),
                "series_lcr": nidcpower.LCRMeasurement.LCR(
                    inductance=10.0,
                    capacitance=20.0,
                    resistance=90.0
                ),
                "parallel_lcr": nidcpower.LCRMeasurement.LCR(
                    inductance=30.0,
                    capacitance=40.0,
                    resistance=110.0
                ),
                "d": 10.0,
                "measurement_mode": nidcpower.InstrumentMode.SMU_PS,
                "dc_in_compliance": True,
                "ac_in_compliance": True,
                "unbalanced": True,
                # Derived properties
                "z_magnitude_and_phase": (100.49876, 5.7105931375),
                "y": complex(0.0099009901, -0.00099009901),
                "y_magnitude_and_phase": (0.0099503719, -5.7105931375),
                "q": 0.1
            },
            # expected_python_str
            (
                "Channel             : Dev1/0\n"
                "DC voltage          : 0.1 V\n"
                "DC current          : 0.001 A\n"
                "Stimulus frequency  : 10,000 Hz\n"
                "AC voltage          : 1+0.1j V RMS\n"
                "AC current          : 0.01+0.001j A RMS\n"
                "Impedance           : 100+10j Ω\n"
                "Impedance magnitude : 100.499 Ω\n"
                "Impedance phase     : 5.71059 °\n"
                "Admittance          : 0.00990099-0.000990099j S\n"
                "Admittance magnitude: 0.00995037 S\n"
                "Admittance phase    : -5.71059 °\n"
                "Series inductance   : 10 H\n"
                "Series capacitance  : 20 F\n"
                "Series resistance   : 90 Ω\n"
                "Parallel inductance : 30 H\n"
                "Parallel capacitance: 40 F\n"
                "Parallel resistance : 110 Ω\n"
                "Dissipation factor  : 10\n"
                "Quality factor      : 0.1\n"
                "Measurement mode    : SMU_PS\n"
                "DC in compliance    : True\n"
                "AC in compliance    : True\n"
                "Unbalanced          : True\n"
            )
        ),
        (
            # ctype_members
            {
                "vdc": 0.0,
                "idc": 0.0,
                "stimulus_frequency": 0.0,
                "ac_voltage_real": 0.0,
                "ac_voltage_imaginary": 0.0,
                "ac_current_real": 0.0,
                "ac_current_imaginary": 0.0,
                "z_real": 0.0,
                "z_imaginary": 0.0,
                "z_magnitude": 0.0,
                "z_phase": 0.0,
                "y_real": cmath.nan,
                "y_imaginary": cmath.nan,
                "y_magnitude": cmath.nan,
                "y_phase": cmath.nan,
                "ls": 0.0,
                "cs": 0.0,
                "rs": 0.0,
                "lp": 0.0,
                "cp": 0.0,
                "rp": 0.0,
                "d": 0.0,
                "q": cmath.nan,
                "measurement_mode": nidcpower.InstrumentMode.LCR.value,
                "dc_in_compliance": False,
                "ac_in_compliance": False,
                "unbalanced": False,
            },
            # channel
            "1",
            # expected_python_members
            {
                "channel": "1",
                "vdc": 0.0,
                "idc": 0.0,
                "stimulus_frequency": 0.0,
                "ac_voltage": complex(),
                "ac_current": complex(),
                "z": complex(),
                "series_lcr": nidcpower.LCRMeasurement.LCR(
                    inductance=0.0,
                    capacitance=0.0,
                    resistance=0.0
                ),
                "parallel_lcr": nidcpower.LCRMeasurement.LCR(
                    inductance=0.0,
                    capacitance=0.0,
                    resistance=0.0
                ),
                "d": 0.0,
                "measurement_mode": nidcpower.InstrumentMode.LCR,
                "dc_in_compliance": False,
                "ac_in_compliance": False,
                "unbalanced": False,
                # Derived properties
                "z_magnitude_and_phase": (0.0, 0.0),
                "y": complex(cmath.nan, cmath.nan),
                "y_magnitude_and_phase": (cmath.nan, cmath.nan),
                "q": cmath.nan
            },
            # expected_python_str
            (
                "Channel             : 1\n"
                "DC voltage          : 0 V\n"
                "DC current          : 0 A\n"
                "Stimulus frequency  : 0 Hz\n"
                "AC voltage          : 0+0j V RMS\n"
                "AC current          : 0+0j A RMS\n"
                "Impedance           : 0+0j Ω\n"
                "Impedance magnitude : 0 Ω\n"
                "Impedance phase     : 0 °\n"
                "Admittance          : nan+nanj S\n"
                "Admittance magnitude: nan S\n"
                "Admittance phase    : nan °\n"
                "Series inductance   : 0 H\n"
                "Series capacitance  : 0 F\n"
                "Series resistance   : 0 Ω\n"
                "Parallel inductance : 0 H\n"
                "Parallel capacitance: 0 F\n"
                "Parallel resistance : 0 Ω\n"
                "Dissipation factor  : 0\n"
                "Quality factor      : nan\n"
                "Measurement mode    : LCR\n"
                "DC in compliance    : False\n"
                "AC in compliance    : False\n"
                "Unbalanced          : False\n"
            )
        ),
    ]
)
def test_lcr_measurement(ctype_members, channel, expected_python_members, expected_python_str):
    ctype_instance = nidcpower.struct_NILCRMeasurement(**ctype_members)
    python_instance = nidcpower.LCRMeasurement(ctype_instance)
    python_instance.channel = channel
    for member in expected_python_members:
        assert getattr(python_instance, member) == pytest.approx(
            expected_python_members[member],
            nan_ok=True
        )
    assert str(python_instance) == expected_python_str


@pytest.mark.parametrize(
    "python_init_params, expected_repr, expected_str, expected_ctype_members",
    [
        (
            # python_init_params
            {
                "frequency": 200.0,
                "reference_value_type": nidcpower.LCRReferenceValueType.IMPEDANCE,
                "reference_value": complex(3.0, 4.0)
            },
            # expected_repr
            (
                "nidcpower.lcr_load_compensation_spot.LCRLoadCompensationSpot("
                "frequency=200.0, "
                "reference_value_type=nidcpower.enums.LCRReferenceValueType.IMPEDANCE, "
                "reference_value=(3+4j))"
            ),
            # expected_str
            (
                "Frequency        : 200 Hz\n"
                "Impedance        : 3+4j Ω\n"
            ),
            # expected_ctype_members
            {
                "frequency": 200.0,
                "reference_value_type": nidcpower.LCRReferenceValueType.IMPEDANCE.value,
                "reference_value_a": 3.0,
                "reference_value_b": 4.0
            }
        ),
        (
            # python_init_params
            {
                "frequency": 300.0,
                "reference_value_type": nidcpower.LCRReferenceValueType.IDEAL_CAPACITANCE,
                "reference_value": 5.0
            },
            # expected_repr
            (
                "nidcpower.lcr_load_compensation_spot.LCRLoadCompensationSpot("
                "frequency=300.0, "
                "reference_value_type=nidcpower.enums.LCRReferenceValueType.IDEAL_CAPACITANCE, "
                "reference_value=5.0)"
            ),
            # expected_str
            (
                "Frequency        : 300 Hz\n"
                "Ideal Capacitance: 5 F\n"
            ),
            # expected_ctype_members
            {
                "frequency": 300.0,
                "reference_value_type": nidcpower.LCRReferenceValueType.IDEAL_CAPACITANCE.value,
                "reference_value_a": 5.0,
                "reference_value_b": 0.0
            }
        ),
        (
            # python_init_params
            {
                "frequency": 400.0,
                "reference_value_type": nidcpower.LCRReferenceValueType.IDEAL_INDUCTANCE,
                "reference_value": 6.0
            },
            # expected_repr
            (
                "nidcpower.lcr_load_compensation_spot.LCRLoadCompensationSpot("
                "frequency=400.0, "
                "reference_value_type=nidcpower.enums.LCRReferenceValueType.IDEAL_INDUCTANCE, "
                "reference_value=6.0)"
            ),
            # expected_str
            (
                "Frequency        : 400 Hz\n"
                "Ideal Inductance : 6 H\n"
            ),
            # expected_ctype_members
            {
                "frequency": 400.0,
                "reference_value_type": nidcpower.LCRReferenceValueType.IDEAL_INDUCTANCE.value,
                "reference_value_a": 6.0,
                "reference_value_b": 0.0
            }
        ),
        (
            # python_init_params
            {
                "frequency": 500.0,
                "reference_value_type": nidcpower.LCRReferenceValueType.IDEAL_RESISTANCE,
                "reference_value": 7.0
            },
            # expected_repr
            (
                "nidcpower.lcr_load_compensation_spot.LCRLoadCompensationSpot("
                "frequency=500.0, "
                "reference_value_type=nidcpower.enums.LCRReferenceValueType.IDEAL_RESISTANCE, "
                "reference_value=7.0)"
            ),
            # expected_str
            (
                "Frequency        : 500 Hz\n"
                "Ideal Resistance : 7 Ω\n"
            ),
            # expected_ctype_members
            {
                "frequency": 500.0,
                "reference_value_type": nidcpower.LCRReferenceValueType.IDEAL_RESISTANCE.value,
                "reference_value_a": 7.0,
                "reference_value_b": 0.0
            },
        ),
    ],
)
def test_lcr_load_compensation_spot(
    python_init_params,
    expected_repr,
    expected_str,
    expected_ctype_members
):
    python_instance = nidcpower.LCRLoadCompensationSpot(**python_init_params)
    for member in python_init_params:
        assert getattr(python_instance, member) == pytest.approx(python_init_params[member])

    assert repr(python_instance) == expected_repr
    assert str(python_instance) == expected_str
    recreated_instance = eval(repr(python_instance))
    assert str(recreated_instance) == str(python_instance)

    ctype_instance = nidcpower.struct_NILCRLoadCompensationSpot(python_instance)
    for member in expected_ctype_members:
        assert getattr(ctype_instance, member) == pytest.approx(expected_ctype_members[member])


def test_lcr_load_compensation_spot_byte_packing_alignment():
    if (platform.system() == "Windows" and platform.architecture()[0] == "64bit") or \
            platform.system() == "Linux" or platform.system() == "Darwin":
        expected_bytes_len = 32
    else:
        expected_bytes_len = 28
    python_spot = nidcpower.LCRLoadCompensationSpot(
        frequency=1_000.0,
        reference_value_type=nidcpower.LCRReferenceValueType.IMPEDANCE,
        reference_value=complex(1.0, 2.0)
    )
    ctype_spot = nidcpower.struct_NILCRLoadCompensationSpot(python_spot)
    assert len(bytes(ctype_spot)) == expected_bytes_len
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidcpower/nidcpower/VERSION sha256=f77228f67c4bb301d51a96f4ec9b3ecb701476af4804f56d06cfef31790f0b46 bytes=12 -->
## FILE: generated/nidcpower/nidcpower/VERSION

- repository: `ni/nimi-python`
- source_path: `generated/nidcpower/nidcpower/VERSION`
- sha256: `f77228f67c4bb301d51a96f4ec9b3ecb701476af4804f56d06cfef31790f0b46`
- bytes: 12

````text
1.5.1.dev0
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidcpower/README.rst sha256=5aead267aa836912798c49390328efb86f8ee08fc6a4af5c52181685fd7919f6 bytes=8097 -->
## FILE: generated/nidcpower/README.rst

- repository: `ni/nimi-python`
- source_path: `generated/nidcpower/README.rst`
- sha256: `5aead267aa836912798c49390328efb86f8ee08fc6a4af5c52181685fd7919f6`
- bytes: 8097

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

The **nidcpower** module provides a Python API for NI-DCPower. The code is maintained in the Open Source repository for `nimi-python <https://github.com/ni/nimi-python>`_.

Support Policy
--------------
**nidcpower** supports all the Operating Systems supported by NI-DCPower.

It follows `Python Software Foundation <https://devguide.python.org/#status-of-python-branches>`_ support policy for different versions of CPython.

NI created and supports **nidcpower**.


NI-DCPower Python API Status
----------------------------

+-------------------------------+--------------------------+
| NI-DCPower (nidcpower)        |                          |
+===============================+==========================+
| Driver Version Tested Against | 2025 Q4 Patch 1          |
+-------------------------------+--------------------------+
| PyPI Version                  | |nidcpowerLatestVersion| |
+-------------------------------+--------------------------+
| Supported Python Version      | |nidcpowerPythonVersion| |
+-------------------------------+--------------------------+
| Documentation                 | |nidcpowerDocs|          |
+-------------------------------+--------------------------+
| Open Issues                   | |nidcpowerOpenIssues|    |
+-------------------------------+--------------------------+
| Open Pull Requests            | |nidcpowerOpenPRs|       |
+-------------------------------+--------------------------+


.. |nidcpowerLatestVersion| image:: http://img.shields.io/pypi/v/nidcpower.svg
    :alt: Latest NI-DCPower Version
    :target: http://pypi.python.org/pypi/nidcpower


.. |nidcpowerPythonVersion| image:: http://img.shields.io/pypi/pyversions/nidcpower.svg
    :alt: NI-DCPower supported Python versions
    :target: http://pypi.python.org/pypi/nidcpower


.. |nidcpowerDocs| image:: https://readthedocs.org/projects/nidcpower/badge/?version=latest
    :alt: NI-DCPower Python API Documentation Status
    :target: https://nidcpower.readthedocs.io/en/latest


.. |nidcpowerOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/nidcpower.svg
    :alt: Open Issues + Pull Requests for NI-DCPower
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Anidcpower


.. |nidcpowerOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/nidcpower.svg
    :alt: Pull Requests for NI-DCPower
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Anidcpower



.. _nidcpower_installation-section:

Installation
------------

As a prerequisite to using the **nidcpower** module, you must install the NI-DCPower runtime on your system. Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the driver runtime for your devices.

The nimi-python modules (i.e. for **NI-DCPower**) can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install nidcpower


Contributing
============

We welcome contributions! You can clone the project repository, build it, and install it by `following these instructions <https://github.com/ni/nimi-python/blob/master/CONTRIBUTING.md>`_.

Usage
------

The following is a basic example of using the **nidcpower** module to open a session to a Source Meter Unit and measure voltage and current.

.. code-block:: python

    import nidcpower
    # Configure the session.

    with nidcpower.Session(resource_name='PXI1Slot2/0') as session:
        session.measure_record_length = 20
        session.measure_record_length_is_finite = True
        session.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE
        session.voltage_level = 5.0

        session.commit()
        print('Effective measurement rate: {} S/s'.format(session.measure_record_delta_time / 1))

        samples_acquired = 0
        print('Channel           Num  Voltage    Current    In Compliance')
        row_format = '{0:15} {1:3d}    {2:8.6f}   {3:8.6f}   {4}'
        with session.initiate():
            channel_indices = '0-{}'.format(session.channel_count - 1)
            channels = session.get_channel_names(channel_indices)
            for i, channel_name in enumerate(channels):
                samples_acquired = 0
                while samples_acquired < 20:
                    measurements = session.channels[channel_name].fetch_multiple(count=session.fetch_backlog)
                    samples_acquired += len(measurements)
                    for i in range(len(measurements)):
                        print(row_format.format(channel_name, i, measurements[i].voltage, measurements[i].current, measurements[i].in_compliance))

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nidcpower/examples>`_

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

Documentation is available `here <http://nidcpower.readthedocs.io>`_.


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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidcpower/setup.py sha256=4fbc47e332c56bc564db3ea8b3cc951f0cfe91aea3591d71515764b399e6d78a bytes=1817 -->
## FILE: generated/nidcpower/setup.py

- repository: `ni/nimi-python`
- source_path: `generated/nidcpower/setup.py`
- sha256: `4fbc47e332c56bc564db3ea8b3cc951f0cfe91aea3591d71515764b399e6d78a`
- bytes: 1817

````python
#!/usr/bin/python
# This file was generated


from setuptools import setup


pypi_name = 'nidcpower'


def read_contents(file_to_read):
    with open(file_to_read, 'r') as f:
        return f.read()


setup(
    name=pypi_name,
    zip_safe=True,
    version='1.5.1.dev0',
    description='NI-DCPower Python API',
    long_description=read_contents('README.rst'),
    long_description_content_type='text/x-rst',
    author='NI',
    author_email="opensource@ni.com",
    url="https://github.com/ni/nimi-python",
    maintainer="NI",
    maintainer_email="opensource@ni.com",
    keywords=['nidcpower'],
    license='MIT',
    include_package_data=True,
    packages=['nidcpower'],
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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidcpower/tox-system_tests.ini sha256=b091ffb83bcf96d4d180ce0f3d9bee2e481f860c55dec03f802794055e8987db bytes=3503 -->
## FILE: generated/nidcpower/tox-system_tests.ini

- repository: `ni/nimi-python`
- source_path: `generated/nidcpower/tox-system_tests.ini`
- sha256: `b091ffb83bcf96d4d180ce0f3d9bee2e481f860c55dec03f802794055e8987db`
- bytes: 3503

````ini
# Tox (http://tox.testrun.org/) is a tool for running tests
# in multiple virtualenvs. This configuration file will run the
# test suite on all supported python versions. To use it, "pip install tox"
# and then run "tox -c tox-system_tests.ini" from the driver directory. (generated/nidcpower)
[tox]
envlist = py{310,311,312,313,314}-nidcpower-system_tests, py314-nidcpower-coverage
skip_missing_interpreters=True
ignore_basepython_conflict=True
# We put the .tox directory outside of the Jenkins workspace so that it isn't wiped with the rest of the repo
toxworkdir = ../../../.tox

[testenv]
description =
    nidcpower-system_tests: Run nidcpower system tests (requires NI-DCPower runtime to be installed)
    nidcpower-coverage: Prepare coverage report for upload to codecov.io  # upload handled by GitHub Actions

changedir =
    nidcpower-system_tests: .
    nidcpower-coverage: .

commands =
    # --disable-pip-version-check prevents pip from telling us we need to upgrade pip, since we are doing that now
    nidcpower-system_tests: python -m pip install --disable-pip-version-check --upgrade pip
    nidcpower-system_tests: python -c "import nidcpower; nidcpower.print_diagnostic_information()"
    nidcpower-system_tests: coverage run --rcfile=../../tools/coverage_system_tests.rc --source nidcpower --parallel-mode -m pytest ../../src/nidcpower/examples --junitxml=../junit/junit-nidcpower-{envname}-examples-{env:BITNESS:64}.xml {posargs}
    nidcpower-system_tests: coverage run --rcfile=../../tools/coverage_system_tests.rc --source nidcpower --parallel-mode -m pytest ../../src/nidcpower/system_tests -c tox-system_tests.ini --junitxml=../junit/junit-nidcpower-{envname}-{env:BITNESS:64}.xml --durations=5 {posargs}

    nidcpower-coverage: coverage combine --rcfile=../../tools/coverage_system_tests.rc ./
    # Create the report to upload
    nidcpower-coverage: coverage xml -i --rcfile=../../tools/coverage_system_tests.rc
    # Display the coverage results
    nidcpower-coverage: coverage report --rcfile=../../tools/coverage_system_tests.rc

deps =
    nidcpower-system_tests: pytest
    nidcpower-system_tests: coverage
    nidcpower-system_tests: numpy
    nidcpower-system_tests: hightime
    nidcpower-system_tests: fasteners
    nidcpower-system_tests: pytest-json
    nidcpower-system_tests: .[grpc]

    nidcpower-coverage: coverage

depends =
    nidcpower-coverage: py{310,311,312,313,314}-nidcpower-system_tests

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
markers = # Defines custom markers used by nidcpower system tests. Prevents PytestUnknownMarkWarning.
    include_legacy_session: Include a legacy session in nidcpower system tests.
    legacy_session_only: Exclude an independent channels session in nidcpower system tests.
    resource_name: Overrides the default resource_name argument in the nidcpower session fixture.
    channels: Overrides the default channels argument in the nidcpower session fixture.
    reset: Overrides the default reset argument in the nidcpower session fixture.
    options: Overrides the default options argument in the nidcpower session fixture.
    independent_channels: Overrides the default independent_channels argument in the nidcpower session fixture.
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidigital/nidigital/__init__.py sha256=a2ca6490bb91bc5140bac02112359467b6060b62443515ad369617683df24232 bytes=3438 -->
## FILE: generated/nidigital/nidigital/__init__.py

- repository: `ni/nimi-python`
- source_path: `generated/nidigital/nidigital/__init__.py`
- sha256: `a2ca6490bb91bc5140bac02112359467b6060b62443515ad369617683df24232`
- bytes: 3438

````python
# -*- coding: utf-8 -*-
# This file was generated


__version__ = '1.4.10.dev0'

from nidigital.enums import *  # noqa: F403,F401,H303
from nidigital.errors import DriverWarning  # noqa: F401
from nidigital.errors import Error  # noqa: F401
from nidigital.grpc_session_options import *  # noqa: F403,F401,H303
from nidigital.session import Session  # noqa: F401

from nidigital.history_ram_cycle_information import HistoryRAMCycleInformation  # noqa: F401


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
            driver_version_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\National Instruments\NI-Digital Pattern Driver\CurrentVersion")
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
    info['driver']['name'] = "NI-Digital Pattern Driver"
    info['driver']['version'] = driver_version
    info['module']['name'] = 'nidigital'
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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidigital/nidigital/_attributes.py sha256=cba3453114dbe81b02efa04bd48418792aec2987eb7bc1ceb253c309ccfad5ab bytes=6187 -->
## FILE: generated/nidigital/nidigital/_attributes.py

- repository: `ni/nimi-python`
- source_path: `generated/nidigital/nidigital/_attributes.py`
- sha256: `cba3453114dbe81b02efa04bd48418792aec2987eb7bc1ceb253c309ccfad5ab`
- bytes: 6187

````python
# -*- coding: utf-8 -*-
# This file was generated
import nidigital._converters as _converters
import nidigital.errors as errors

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
    '''Class for attributes that use enums internally but are exposed in the nidigital Python module as something else, thus need conversion.'''

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
        from nidigital.session import SessionReference
        return SessionReference(session._get_attribute_vi_session(self._attribute_id))

    def __set__(self, session, value):
        session._set_attribute_vi_session(self._attribute_id, _converters.convert_to_nitclk_session_number(value))
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidigital/nidigital/_converters.py sha256=f75068432314a888f052662a57f22094864c104e7bb356aada74ead7f30a7212 bytes=14627 -->
## FILE: generated/nidigital/nidigital/_converters.py

- repository: `ni/nimi-python`
- source_path: `generated/nidigital/nidigital/_converters.py`
- sha256: `f75068432314a888f052662a57f22094864c104e7bb356aada74ead7f30a7212`
- bytes: 14627

````python
# -*- coding: utf-8 -*-
# This file was generated
import nidigital._visatype as _visatype
import nidigital.errors as errors

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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidigital/nidigital/_grpc_stub_interpreter.py sha256=416c2dc3e740d107e69b084b1217a54ac47918a11b1d87848700830698a12dc1 bytes=29734 -->
## FILE: generated/nidigital/nidigital/_grpc_stub_interpreter.py

- repository: `ni/nimi-python`
- source_path: `generated/nidigital/nidigital/_grpc_stub_interpreter.py`
- sha256: `416c2dc3e740d107e69b084b1217a54ac47918a11b1d87848700830698a12dc1`
- bytes: 29734

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
from . import nidigitalpattern_pb2 as grpc_types
from . import nidigitalpattern_pb2_grpc as nidigital_grpc

from . import history_ram_cycle_information as history_ram_cycle_information  # noqa: F401


class GrpcStubInterpreter(object):
    '''Interpreter for interacting with a gRPC Stub class'''

    def __init__(self, grpc_options):
        self._grpc_options = grpc_options
        self._lock = threading.RLock()
        self._client = nidigital_grpc.NiDigitalStub(grpc_options.grpc_channel)
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

    def abort_keep_alive(self):  # noqa: N802
        self._invoke(
            self._client.AbortKeepAlive,
            grpc_types.AbortKeepAliveRequest(vi=self._vi),
        )

    def apply_levels_and_timing(self, site_list, levels_sheet, timing_sheet, initial_state_high_pins, initial_state_low_pins, initial_state_tristate_pins):  # noqa: N802
        self._invoke(
            self._client.ApplyLevelsAndTiming,
            grpc_types.ApplyLevelsAndTimingRequest(vi=self._vi, site_list=site_list, levels_sheet=levels_sheet, timing_sheet=timing_sheet, initial_state_high_pins=initial_state_high_pins, initial_state_low_pins=initial_state_low_pins, initial_state_tristate_pins=initial_state_tristate_pins),
        )

    def apply_tdr_offsets(self, channel_list, offsets):  # noqa: N802
        self._invoke(
            self._client.ApplyTDROffsets,
            grpc_types.ApplyTDROffsetsRequest(vi=self._vi, channel_list=channel_list, offsets=offsets),
        )

    def burst_pattern(self, site_list, start_label, select_digital_function, wait_until_done, timeout):  # noqa: N802
        self._invoke(
            self._client.BurstPattern,
            grpc_types.BurstPatternRequest(vi=self._vi, site_list=site_list, start_label=start_label, select_digital_function=select_digital_function, wait_until_done=wait_until_done, timeout=timeout),
        )

    def clock_generator_abort(self, channel_list):  # noqa: N802
        self._invoke(
            self._client.ClockGeneratorAbort,
            grpc_types.ClockGeneratorAbortRequest(vi=self._vi, channel_list=channel_list),
        )

    def clock_generator_generate_clock(self, channel_list, frequency, select_digital_function):  # noqa: N802
        self._invoke(
            self._client.ClockGeneratorGenerateClock,
            grpc_types.ClockGeneratorGenerateClockRequest(vi=self._vi, channel_list=channel_list, frequency=frequency, select_digital_function=select_digital_function),
        )

    def commit(self):  # noqa: N802
        self._invoke(
            self._client.Commit,
            grpc_types.CommitRequest(vi=self._vi),
        )

    def configure_active_load_levels(self, channel_list, iol, ioh, vcom):  # noqa: N802
        self._invoke(
            self._client.ConfigureActiveLoadLevels,
            grpc_types.ConfigureActiveLoadLevelsRequest(vi=self._vi, channel_list=channel_list, iol=iol, ioh=ioh, vcom=vcom),
        )

    def configure_pattern_burst_sites(self, site_list):  # noqa: N802
        self._invoke(
            self._client.ConfigurePatternBurstSites,
            grpc_types.ConfigurePatternBurstSitesRequest(vi=self._vi, site_list=site_list),
        )

    def configure_time_set_compare_edges_strobe(self, pin_list, time_set_name, strobe_edge):  # noqa: N802
        self._invoke(
            self._client.ConfigureTimeSetCompareEdgesStrobe,
            grpc_types.ConfigureTimeSetCompareEdgesStrobeRequest(vi=self._vi, pin_list=pin_list, time_set_name=time_set_name, strobe_edge=strobe_edge),
        )

    def configure_time_set_compare_edges_strobe2x(self, pin_list, time_set_name, strobe_edge, strobe2_edge):  # noqa: N802
        self._invoke(
            self._client.ConfigureTimeSetCompareEdgesStrobe2x,
            grpc_types.ConfigureTimeSetCompareEdgesStrobe2xRequest(vi=self._vi, pin_list=pin_list, time_set_name=time_set_name, strobe_edge=strobe_edge, strobe2_edge=strobe2_edge),
        )

    def configure_time_set_drive_edges(self, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge):  # noqa: N802
        self._invoke(
            self._client.ConfigureTimeSetDriveEdges,
            grpc_types.ConfigureTimeSetDriveEdgesRequest(vi=self._vi, pin_list=pin_list, time_set_name=time_set_name, format_raw=format.value, drive_on_edge=drive_on_edge, drive_data_edge=drive_data_edge, drive_return_edge=drive_return_edge, drive_off_edge=drive_off_edge),
        )

    def configure_time_set_drive_edges2x(self, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge, drive_data2_edge, drive_return2_edge):  # noqa: N802
        self._invoke(
            self._client.ConfigureTimeSetDriveEdges2x,
            grpc_types.ConfigureTimeSetDriveEdges2xRequest(vi=self._vi, pin_list=pin_list, time_set_name=time_set_name, format_raw=format.value, drive_on_edge=drive_on_edge, drive_data_edge=drive_data_edge, drive_return_edge=drive_return_edge, drive_off_edge=drive_off_edge, drive_data2_edge=drive_data2_edge, drive_return2_edge=drive_return2_edge),
        )

    def configure_time_set_drive_format(self, pin_list, time_set_name, drive_format):  # noqa: N802
        self._invoke(
            self._client.ConfigureTimeSetDriveFormat,
            grpc_types.ConfigureTimeSetDriveFormatRequest(vi=self._vi, pin_list=pin_list, time_set_name=time_set_name, drive_format_raw=drive_format.value),
        )

    def configure_time_set_edge(self, pin_list, time_set_name, edge, time):  # noqa: N802
        self._invoke(
            self._client.ConfigureTimeSetEdge,
            grpc_types.ConfigureTimeSetEdgeRequest(vi=self._vi, pin_list=pin_list, time_set_name=time_set_name, edge_raw=edge.value, time=time),
        )

    def configure_time_set_edge_multiplier(self, pin_list, time_set_name, edge_multiplier):  # noqa: N802
        self._invoke(
            self._client.ConfigureTimeSetEdgeMultiplier,
            grpc_types.ConfigureTimeSetEdgeMultiplierRequest(vi=self._vi, pin_list=pin_list, time_set_name=time_set_name, edge_multiplier=edge_multiplier),
        )

    def configure_time_set_period(self, time_set_name, period):  # noqa: N802
        self._invoke(
            self._client.ConfigureTimeSetPeriod,
            grpc_types.ConfigureTimeSetPeriodRequest(vi=self._vi, time_set_name=time_set_name, period=period),
        )

    def configure_voltage_levels(self, channel_list, vil, vih, vol, voh, vterm):  # noqa: N802
        self._invoke(
            self._client.ConfigureVoltageLevels,
            grpc_types.ConfigureVoltageLevelsRequest(vi=self._vi, channel_list=channel_list, vil=vil, vih=vih, vol=vol, voh=voh, vterm=vterm),
        )

    def create_capture_waveform_from_file_digicapture(self, waveform_name, waveform_file_path):  # noqa: N802
        self._invoke(
            self._client.CreateCaptureWaveformFromFileDigicapture,
            grpc_types.CreateCaptureWaveformFromFileDigicaptureRequest(vi=self._vi, waveform_name=waveform_name, waveform_file_path=waveform_file_path),
        )

    def create_capture_waveform_parallel(self, pin_list, waveform_name):  # noqa: N802
        self._invoke(
            self._client.CreateCaptureWaveformParallel,
            grpc_types.CreateCaptureWaveformParallelRequest(vi=self._vi, pin_list=pin_list, waveform_name=waveform_name),
        )

    def create_capture_waveform_serial(self, pin_list, waveform_name, sample_width, bit_order):  # noqa: N802
        self._invoke(
            self._client.CreateCaptureWaveformSerial,
            grpc_types.CreateCaptureWaveformSerialRequest(vi=self._vi, pin_list=pin_list, waveform_name=waveform_name, sample_width=sample_width, bit_order_raw=bit_order.value),
        )

    def create_source_waveform_from_file_tdms(self, waveform_name, waveform_file_path, write_waveform_data):  # noqa: N802
        self._invoke(
            self._client.CreateSourceWaveformFromFileTDMS,
            grpc_types.CreateSourceWaveformFromFileTDMSRequest(vi=self._vi, waveform_name=waveform_name, waveform_file_path=waveform_file_path, write_waveform_data=write_waveform_data),
        )

    def create_source_waveform_parallel(self, pin_list, waveform_name, data_mapping):  # noqa: N802
        self._invoke(
            self._client.CreateSourceWaveformParallel,
            grpc_types.CreateSourceWaveformParallelRequest(vi=self._vi, pin_list=pin_list, waveform_name=waveform_name, data_mapping_raw=data_mapping.value),
        )

    def create_source_waveform_serial(self, pin_list, waveform_name, data_mapping, sample_width, bit_order):  # noqa: N802
        self._invoke(
            self._client.CreateSourceWaveformSerial,
            grpc_types.CreateSourceWaveformSerialRequest(vi=self._vi, pin_list=pin_list, waveform_name=waveform_name, data_mapping_raw=data_mapping.value, sample_width=sample_width, bit_order_raw=bit_order.value),
        )

    def create_time_set(self, name):  # noqa: N802
        self._invoke(
            self._client.CreateTimeSet,
            grpc_types.CreateTimeSetRequest(vi=self._vi, name=name),
        )

    def delete_all_time_sets(self):  # noqa: N802
        self._invoke(
            self._client.DeleteAllTimeSets,
            grpc_types.DeleteAllTimeSetsRequest(vi=self._vi),
        )

    def disable_sites(self, site_list):  # noqa: N802
        self._invoke(
            self._client.DisableSites,
            grpc_types.DisableSitesRequest(vi=self._vi, site_list=site_list),
        )

    def enable_sites(self, site_list):  # noqa: N802
        self._invoke(
            self._client.EnableSites,
            grpc_types.EnableSitesRequest(vi=self._vi, site_list=site_list),
        )

    def fetch_capture_waveform(self, site_list, waveform_name, samples_to_read, timeout):  # noqa: N802
        response = self._invoke(
            self._client.FetchCaptureWaveformU32,
            grpc_types.FetchCaptureWaveformU32Request(vi=self._vi, site_list=site_list, waveform_name=waveform_name, samples_to_read=samples_to_read, timeout=timeout),
        )
        return bytes(response.data), response.actual_num_waveforms, response.actual_samples_per_waveform

    def fetch_history_ram_cycle_information(self, site, sample_index):  # noqa: N802
        response = self._invoke(
            self._client.FetchHistoryRAMCycleInformation,
            grpc_types.FetchHistoryRAMCycleInformationRequest(vi=self._vi, site=site, sample_index=sample_index),
        )
        return response.pattern_index, response.time_set_index, response.vector_number, response.cycle_number, response.num_dut_cycles

    def fetch_history_ram_cycle_pin_data(self, site, pin_list, sample_index, dut_cycle_index):  # noqa: N802
        response = self._invoke(
            self._client.FetchHistoryRAMCyclePinData,
            grpc_types.FetchHistoryRAMCyclePinDataRequest(vi=self._vi, site=site, pin_list=pin_list, sample_index=sample_index, dut_cycle_index=dut_cycle_index),
        )
        return [enums.PinState(x) for x in response.expected_pin_states_raw], [enums.PinState(x) for x in response.actual_pin_states_raw], response.per_pin_pass_fail

    def fetch_history_ram_scan_cycle_number(self, site, sample_index):  # noqa: N802
        response = self._invoke(
            self._client.FetchHistoryRAMScanCycleNumber,
            grpc_types.FetchHistoryRAMScanCycleNumberRequest(vi=self._vi, site=site, sample_index=sample_index),
        )
        return response.scan_cycle_number

    def frequency_counter_measure_frequency(self, channel_list):  # noqa: N802
        response = self._invoke(
            self._client.FrequencyCounterMeasureFrequency,
            grpc_types.FrequencyCounterMeasureFrequencyRequest(vi=self._vi, channel_list=channel_list),
        )
        return response.frequencies

    def get_attribute_vi_boolean(self, channel_name, attribute):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViBoolean,
            grpc_types.GetAttributeViBooleanRequest(vi=self._vi, channel_name=channel_name, attribute=attribute),
        )
        return response.value

    def get_attribute_vi_int32(self, channel_name, attribute):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViInt32,
            grpc_types.GetAttributeViInt32Request(vi=self._vi, channel_name=channel_name, attribute=attribute),
        )
        return response.value

    def get_attribute_vi_int64(self, channel_name, attribute):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViInt64,
            grpc_types.GetAttributeViInt64Request(vi=self._vi, channel_name=channel_name, attribute=attribute),
        )
        return response.value

    def get_attribute_vi_real64(self, channel_name, attribute):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViReal64,
            grpc_types.GetAttributeViReal64Request(vi=self._vi, channel_name=channel_name, attribute=attribute),
        )
        return response.value

    def get_attribute_vi_string(self, channel_name, attribute):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViString,
            grpc_types.GetAttributeViStringRequest(vi=self._vi, channel_name=channel_name, attribute=attribute),
        )
        return response.value

    def get_channel_names(self, indices):  # noqa: N802
        response = self._invoke(
            self._client.GetChannelNameFromString,
            grpc_types.GetChannelNameFromStringRequest(vi=self._vi, indices=indices),
        )
        return response.names

    def get_error(self):  # noqa: N802
        response = self._invoke(
            self._client.GetError,
            grpc_types.GetErrorRequest(vi=self._vi),
        )
        return response.error_code, response.error_description

    def get_fail_count(self, channel_list):  # noqa: N802
        response = self._invoke(
            self._client.GetFailCount,
            grpc_types.GetFailCountRequest(vi=self._vi, channel_list=channel_list),
        )
        return response.failure_count

    def get_history_ram_sample_count(self, site):  # noqa: N802
        response = self._invoke(
            self._client.GetHistoryRAMSampleCount,
            grpc_types.GetHistoryRAMSampleCountRequest(vi=self._vi, site=site),
        )
        return response.sample_count

    def get_pattern_name(self, pattern_index):  # noqa: N802
        response = self._invoke(
            self._client.GetPatternName,
            grpc_types.GetPatternNameRequest(vi=self._vi, pattern_index=pattern_index),
        )
        return response.name

    def get_pattern_pin_names(self, start_label):  # noqa: N802
        response = self._invoke(
            self._client.GetPatternPinList,
            grpc_types.GetPatternPinListRequest(vi=self._vi, start_label=start_label),
        )
        return response.pin_list

    def get_pin_name(self, pin_index):  # noqa: N802
        response = self._invoke(
            self._client.GetPinName,
            grpc_types.GetPinNameRequest(vi=self._vi, pin_index=pin_index),
        )
        return response.name

    def get_pin_results_pin_information(self, channel_list):  # noqa: N802
        response = self._invoke(
            self._client.GetPinResultsPinInformation,
            grpc_types.GetPinResultsPinInformationRequest(vi=self._vi, channel_list=channel_list),
        )
        return response.pin_indexes, response.site_numbers, response.channel_indexes

    def get_site_pass_fail(self, site_list):  # noqa: N802
        response = self._invoke(
            self._client.GetSitePassFail,
            grpc_types.GetSitePassFailRequest(vi=self._vi, site_list=site_list),
        )
        return response.pass_fail

    def get_site_results_site_numbers(self, site_list, site_result_type):  # noqa: N802
        response = self._invoke(
            self._client.GetSiteResultsSiteNumbers,
            grpc_types.GetSiteResultsSiteNumbersRequest(vi=self._vi, site_list=site_list, site_result_type_raw=site_result_type.value),
        )
        return response.site_numbers

    def get_time_set_drive_format(self, pin, time_set_name):  # noqa: N802
        response = self._invoke(
            self._client.GetTimeSetDriveFormat,
            grpc_types.GetTimeSetDriveFormatRequest(vi=self._vi, pin=pin, time_set_name=time_set_name),
        )
        return enums.DriveFormat(response.format_raw)

    def get_time_set_edge(self, pin, time_set_name, edge):  # noqa: N802
        response = self._invoke(
            self._client.GetTimeSetEdge,
            grpc_types.GetTimeSetEdgeRequest(vi=self._vi, pin=pin, time_set_name=time_set_name, edge_raw=edge.value),
        )
        return response.time

    def get_time_set_edge_multiplier(self, pin, time_set_name):  # noqa: N802
        response = self._invoke(
            self._client.GetTimeSetEdgeMultiplier,
            grpc_types.GetTimeSetEdgeMultiplierRequest(vi=self._vi, pin=pin, time_set_name=time_set_name),
        )
        return response.edge_multiplier

    def get_time_set_name(self, time_set_index):  # noqa: N802
        response = self._invoke(
            self._client.GetTimeSetName,
            grpc_types.GetTimeSetNameRequest(vi=self._vi, time_set_index=time_set_index),
        )
        return response.name

    def get_time_set_period(self, time_set_name):  # noqa: N802
        response = self._invoke(
            self._client.GetTimeSetPeriod,
            grpc_types.GetTimeSetPeriodRequest(vi=self._vi, time_set_name=time_set_name),
        )
        return response.period

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

    def is_done(self):  # noqa: N802
        response = self._invoke(
            self._client.IsDone,
            grpc_types.IsDoneRequest(vi=self._vi),
        )
        return response.done

    def is_site_enabled(self, site):  # noqa: N802
        response = self._invoke(
            self._client.IsSiteEnabled,
            grpc_types.IsSiteEnabledRequest(vi=self._vi, site=site),
        )
        return response.enable

    def load_levels(self, file_path):  # noqa: N802
        self._invoke(
            self._client.LoadLevels,
            grpc_types.LoadLevelsRequest(vi=self._vi, file_path=file_path),
        )

    def load_pattern(self, file_path):  # noqa: N802
        self._invoke(
            self._client.LoadPattern,
            grpc_types.LoadPatternRequest(vi=self._vi, file_path=file_path),
        )

    def load_pin_map(self, file_path):  # noqa: N802
        self._invoke(
            self._client.LoadPinMap,
            grpc_types.LoadPinMapRequest(vi=self._vi, file_path=file_path),
        )

    def load_specifications(self, file_path):  # noqa: N802
        self._invoke(
            self._client.LoadSpecifications,
            grpc_types.LoadSpecificationsRequest(vi=self._vi, file_path=file_path),
        )

    def load_timing(self, file_path):  # noqa: N802
        self._invoke(
            self._client.LoadTiming,
            grpc_types.LoadTimingRequest(vi=self._vi, file_path=file_path),
        )

    def lock(self):  # noqa: N802
        self._lock.acquire()

    def ppmu_measure(self, channel_list, measurement_type):  # noqa: N802
        response = self._invoke(
            self._client.PPMUMeasure,
            grpc_types.PPMUMeasureRequest(vi=self._vi, channel_list=channel_list, measurement_type_raw=measurement_type.value),
        )
        return response.measurements

    def ppmu_source(self, channel_list):  # noqa: N802
        self._invoke(
            self._client.PPMUSource,
            grpc_types.PPMUSourceRequest(vi=self._vi, channel_list=channel_list),
        )

    def read_sequencer_flag(self, flag):  # noqa: N802
        response = self._invoke(
            self._client.ReadSequencerFlag,
            grpc_types.ReadSequencerFlagRequest(vi=self._vi, flag=flag.value),
        )
        return response.value

    def read_sequencer_register(self, reg):  # noqa: N802
        response = self._invoke(
            self._client.ReadSequencerRegister,
            grpc_types.ReadSequencerRegisterRequest(vi=self._vi, reg=reg.value),
        )
        return response.value

    def read_static(self, channel_list):  # noqa: N802
        response = self._invoke(
            self._client.ReadStatic,
            grpc_types.ReadStaticRequest(vi=self._vi, channel_list=channel_list),
        )
        return [enums.PinState(x) for x in response.data_raw]

    def reset_device(self):  # noqa: N802
        self._invoke(
            self._client.ResetDevice,
            grpc_types.ResetDeviceRequest(vi=self._vi),
        )

    def self_calibrate(self):  # noqa: N802
        self._invoke(
            self._client.SelfCalibrate,
            grpc_types.SelfCalibrateRequest(vi=self._vi),
        )

    def send_software_edge_trigger(self, trigger, trigger_identifier):  # noqa: N802
        self._invoke(
            self._client.SendSoftwareEdgeTrigger,
            grpc_types.SendSoftwareEdgeTriggerRequest(vi=self._vi, trigger_raw=trigger.value, trigger_identifier=trigger_identifier),
        )

    def set_attribute_vi_boolean(self, channel_name, attribute, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViBoolean,
            grpc_types.SetAttributeViBooleanRequest(vi=self._vi, channel_name=channel_name, attribute=attribute, value=value),
        )

    def set_attribute_vi_int32(self, channel_name, attribute, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViInt32,
            grpc_types.SetAttributeViInt32Request(vi=self._vi, channel_name=channel_name, attribute=attribute, value_raw=value),
        )

    def set_attribute_vi_int64(self, channel_name, attribute, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViInt64,
            grpc_types.SetAttributeViInt64Request(vi=self._vi, channel_name=channel_name, attribute=attribute, value_raw=value),
        )

    def set_attribute_vi_real64(self, channel_name, attribute, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViReal64,
            grpc_types.SetAttributeViReal64Request(vi=self._vi, channel_name=channel_name, attribute=attribute, value_raw=value),
        )

    def set_attribute_vi_string(self, channel_name, attribute, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViString,
            grpc_types.SetAttributeViStringRequest(vi=self._vi, channel_name=channel_name, attribute=attribute, value_raw=value),
        )

    def set_runtime_environment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        raise NotImplementedError('set_runtime_environment is not supported over gRPC')

    def tdr(self, channel_list, apply_offsets):  # noqa: N802
        response = self._invoke(
            self._client.TDR,
            grpc_types.TDRRequest(vi=self._vi, channel_list=channel_list, apply_offsets=apply_offsets),
        )
        return response.offsets

    def unload_all_patterns(self, unload_keep_alive_pattern):  # noqa: N802
        self._invoke(
            self._client.UnloadAllPatterns,
            grpc_types.UnloadAllPatternsRequest(vi=self._vi, unload_keep_alive_pattern=unload_keep_alive_pattern),
        )

    def unload_specifications(self, file_path):  # noqa: N802
        self._invoke(
            self._client.UnloadSpecifications,
            grpc_types.UnloadSpecificationsRequest(vi=self._vi, file_path=file_path),
        )

    def unlock(self):  # noqa: N802
        self._lock.release()

    def wait_until_done(self, timeout):  # noqa: N802
        self._invoke(
            self._client.WaitUntilDone,
            grpc_types.WaitUntilDoneRequest(vi=self._vi, timeout=timeout),
        )

    def write_sequencer_flag(self, flag, value):  # noqa: N802
        self._invoke(
            self._client.WriteSequencerFlag,
            grpc_types.WriteSequencerFlagRequest(vi=self._vi, flag=flag.value, value=value),
        )

    def write_sequencer_register(self, reg, value):  # noqa: N802
        self._invoke(
            self._client.WriteSequencerRegister,
            grpc_types.WriteSequencerRegisterRequest(vi=self._vi, reg=reg.value, value=value),
        )

    def write_source_waveform_broadcast(self, waveform_name, waveform_data):  # noqa: N802
        self._invoke(
            self._client.WriteSourceWaveformBroadcastU32,
            grpc_types.WriteSourceWaveformBroadcastU32Request(vi=self._vi, waveform_name=waveform_name, waveform_data=waveform_data),
        )

    def write_source_waveform_data_from_file_tdms(self, waveform_name, waveform_file_path):  # noqa: N802
        self._invoke(
            self._client.WriteSourceWaveformDataFromFileTDMS,
            grpc_types.WriteSourceWaveformDataFromFileTDMSRequest(vi=self._vi, waveform_name=waveform_name, waveform_file_path=waveform_file_path),
        )

    def write_source_waveform_site_unique_u32(self, site_list, waveform_name, num_waveforms, samples_per_waveform, waveform_data):  # noqa: N802
        self._invoke(
            self._client.WriteSourceWaveformSiteUniqueU32,
            grpc_types.WriteSourceWaveformSiteUniqueU32Request(vi=self._vi, site_list=site_list, waveform_name=waveform_name, num_waveforms=num_waveforms, samples_per_waveform=samples_per_waveform, waveform_data=waveform_data),
        )

    def write_static(self, channel_list, state):  # noqa: N802
        self._invoke(
            self._client.WriteStatic,
            grpc_types.WriteStaticRequest(vi=self._vi, channel_list=channel_list, state_raw=state.value),
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
        return response.test_result, response.test_message
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidigital/nidigital/_library.py sha256=8dc05cc9f85ffcb176d9ae4187046a4ae043c4ec41745e5c0ff9c3105d8d67db bytes=67099 -->
## FILE: generated/nidigital/nidigital/_library.py

- repository: `ni/nimi-python`
- source_path: `generated/nidigital/nidigital/_library.py`
- sha256: `8dc05cc9f85ffcb176d9ae4187046a4ae043c4ec41745e5c0ff9c3105d8d67db`
- bytes: 67099

````python
# -*- coding: utf-8 -*-
# This file was generated

import ctypes
import nidigital.errors as errors
import threading

from nidigital._visatype import *  # noqa: F403,H303

import nidigital.history_ram_cycle_information as history_ram_cycle_information  # noqa: F401


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, ctypes_library):
        self._func_lock = threading.Lock()
        self._library = ctypes_library
        # We cache the cfunc object from the ctypes.CDLL object
        self.niDigital_Abort_cfunc = None
        self.niDigital_AbortKeepAlive_cfunc = None
        self.niDigital_ApplyLevelsAndTiming_cfunc = None
        self.niDigital_ApplyTDROffsets_cfunc = None
        self.niDigital_BurstPattern_cfunc = None
        self.niDigital_ClockGenerator_Abort_cfunc = None
        self.niDigital_ClockGenerator_GenerateClock_cfunc = None
        self.niDigital_Commit_cfunc = None
        self.niDigital_ConfigureActiveLoadLevels_cfunc = None
        self.niDigital_ConfigurePatternBurstSites_cfunc = None
        self.niDigital_ConfigureTimeSetCompareEdgesStrobe_cfunc = None
        self.niDigital_ConfigureTimeSetCompareEdgesStrobe2x_cfunc = None
        self.niDigital_ConfigureTimeSetDriveEdges_cfunc = None
        self.niDigital_ConfigureTimeSetDriveEdges2x_cfunc = None
        self.niDigital_ConfigureTimeSetDriveFormat_cfunc = None
        self.niDigital_ConfigureTimeSetEdge_cfunc = None
        self.niDigital_ConfigureTimeSetEdgeMultiplier_cfunc = None
        self.niDigital_ConfigureTimeSetPeriod_cfunc = None
        self.niDigital_ConfigureVoltageLevels_cfunc = None
        self.niDigital_CreateCaptureWaveformFromFileDigicapture_cfunc = None
        self.niDigital_CreateCaptureWaveformParallel_cfunc = None
        self.niDigital_CreateCaptureWaveformSerial_cfunc = None
        self.niDigital_CreateSourceWaveformFromFileTDMS_cfunc = None
        self.niDigital_CreateSourceWaveformParallel_cfunc = None
        self.niDigital_CreateSourceWaveformSerial_cfunc = None
        self.niDigital_CreateTimeSet_cfunc = None
        self.niDigital_DeleteAllTimeSets_cfunc = None
        self.niDigital_DisableSites_cfunc = None
        self.niDigital_EnableMatchFailCombination_cfunc = None
        self.niDigital_EnableSites_cfunc = None
        self.niDigital_FetchCaptureWaveformU32_cfunc = None
        self.niDigital_FetchHistoryRAMCycleInformation_cfunc = None
        self.niDigital_FetchHistoryRAMCyclePinData_cfunc = None
        self.niDigital_FetchHistoryRAMScanCycleNumber_cfunc = None
        self.niDigital_FrequencyCounter_MeasureFrequency_cfunc = None
        self.niDigital_GetAttributeViBoolean_cfunc = None
        self.niDigital_GetAttributeViInt32_cfunc = None
        self.niDigital_GetAttributeViInt64_cfunc = None
        self.niDigital_GetAttributeViReal64_cfunc = None
        self.niDigital_GetAttributeViString_cfunc = None
        self.niDigital_GetChannelNameFromString_cfunc = None
        self.niDigital_GetError_cfunc = None
        self.niDigital_GetFailCount_cfunc = None
        self.niDigital_GetHistoryRAMSampleCount_cfunc = None
        self.niDigital_GetPatternName_cfunc = None
        self.niDigital_GetPatternPinList_cfunc = None
        self.niDigital_GetPinName_cfunc = None
        self.niDigital_GetPinResultsPinInformation_cfunc = None
        self.niDigital_GetSitePassFail_cfunc = None
        self.niDigital_GetSiteResultsSiteNumbers_cfunc = None
        self.niDigital_GetTimeSetDriveFormat_cfunc = None
        self.niDigital_GetTimeSetEdge_cfunc = None
        self.niDigital_GetTimeSetEdgeMultiplier_cfunc = None
        self.niDigital_GetTimeSetName_cfunc = None
        self.niDigital_GetTimeSetPeriod_cfunc = None
        self.niDigital_InitWithOptions_cfunc = None
        self.niDigital_Initiate_cfunc = None
        self.niDigital_IsDone_cfunc = None
        self.niDigital_IsSiteEnabled_cfunc = None
        self.niDigital_LoadLevels_cfunc = None
        self.niDigital_LoadPattern_cfunc = None
        self.niDigital_LoadPinMap_cfunc = None
        self.niDigital_LoadSpecifications_cfunc = None
        self.niDigital_LoadTiming_cfunc = None
        self.niDigital_LockSession_cfunc = None
        self.niDigital_PPMU_Measure_cfunc = None
        self.niDigital_PPMU_Source_cfunc = None
        self.niDigital_ReadSequencerFlag_cfunc = None
        self.niDigital_ReadSequencerRegister_cfunc = None
        self.niDigital_ReadStatic_cfunc = None
        self.niDigital_ResetDevice_cfunc = None
        self.niDigital_SelfCalibrate_cfunc = None
        self.niDigital_SendSoftwareEdgeTrigger_cfunc = None
        self.niDigital_SetAttributeViBoolean_cfunc = None
        self.niDigital_SetAttributeViInt32_cfunc = None
        self.niDigital_SetAttributeViInt64_cfunc = None
        self.niDigital_SetAttributeViReal64_cfunc = None
        self.niDigital_SetAttributeViString_cfunc = None
        self.niDigital_SetRuntimeEnvironment_cfunc = None
        self.niDigital_TDR_cfunc = None
        self.niDigital_UnloadAllPatterns_cfunc = None
        self.niDigital_UnloadSpecifications_cfunc = None
        self.niDigital_UnlockSession_cfunc = None
        self.niDigital_WaitUntilDone_cfunc = None
        self.niDigital_WriteSequencerFlag_cfunc = None
        self.niDigital_WriteSequencerRegister_cfunc = None
        self.niDigital_WriteSourceWaveformBroadcastU32_cfunc = None
        self.niDigital_WriteSourceWaveformDataFromFileTDMS_cfunc = None
        self.niDigital_WriteSourceWaveformSiteUniqueU32_cfunc = None
        self.niDigital_WriteStatic_cfunc = None
        self.niDigital_close_cfunc = None
        self.niDigital_error_message_cfunc = None
        self.niDigital_reset_cfunc = None
        self.niDigital_self_test_cfunc = None

    def _get_library_function(self, name):
        try:
            function = getattr(self._library, name)
        except AttributeError as e:
            raise errors.DriverTooOldError() from e
        return function

    def niDigital_Abort(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDigital_Abort_cfunc is None:
                self.niDigital_Abort_cfunc = self._get_library_function('niDigital_Abort')
                self.niDigital_Abort_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDigital_Abort_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_Abort_cfunc(vi)

    def niDigital_AbortKeepAlive(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDigital_AbortKeepAlive_cfunc is None:
                self.niDigital_AbortKeepAlive_cfunc = self._get_library_function('niDigital_AbortKeepAlive')
                self.niDigital_AbortKeepAlive_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDigital_AbortKeepAlive_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_AbortKeepAlive_cfunc(vi)

    def niDigital_ApplyLevelsAndTiming(self, vi, site_list, levels_sheet, timing_sheet, initial_state_high_pins, initial_state_low_pins, initial_state_tristate_pins):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ApplyLevelsAndTiming_cfunc is None:
                self.niDigital_ApplyLevelsAndTiming_cfunc = self._get_library_function('niDigital_ApplyLevelsAndTiming')
                self.niDigital_ApplyLevelsAndTiming_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_ApplyLevelsAndTiming_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ApplyLevelsAndTiming_cfunc(vi, site_list, levels_sheet, timing_sheet, initial_state_high_pins, initial_state_low_pins, initial_state_tristate_pins)

    def niDigital_ApplyTDROffsets(self, vi, channel_list, num_offsets, offsets):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ApplyTDROffsets_cfunc is None:
                self.niDigital_ApplyTDROffsets_cfunc = self._get_library_function('niDigital_ApplyTDROffsets')
                self.niDigital_ApplyTDROffsets_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDigital_ApplyTDROffsets_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ApplyTDROffsets_cfunc(vi, channel_list, num_offsets, offsets)

    def niDigital_BurstPattern(self, vi, site_list, start_label, select_digital_function, wait_until_done, timeout):  # noqa: N802
        with self._func_lock:
            if self.niDigital_BurstPattern_cfunc is None:
                self.niDigital_BurstPattern_cfunc = self._get_library_function('niDigital_BurstPattern')
                self.niDigital_BurstPattern_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViBoolean, ViBoolean, ViReal64]  # noqa: F405
                self.niDigital_BurstPattern_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_BurstPattern_cfunc(vi, site_list, start_label, select_digital_function, wait_until_done, timeout)

    def niDigital_ClockGenerator_Abort(self, vi, channel_list):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ClockGenerator_Abort_cfunc is None:
                self.niDigital_ClockGenerator_Abort_cfunc = self._get_library_function('niDigital_ClockGenerator_Abort')
                self.niDigital_ClockGenerator_Abort_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_ClockGenerator_Abort_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ClockGenerator_Abort_cfunc(vi, channel_list)

    def niDigital_ClockGenerator_GenerateClock(self, vi, channel_list, frequency, select_digital_function):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ClockGenerator_GenerateClock_cfunc is None:
                self.niDigital_ClockGenerator_GenerateClock_cfunc = self._get_library_function('niDigital_ClockGenerator_GenerateClock')
                self.niDigital_ClockGenerator_GenerateClock_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViBoolean]  # noqa: F405
                self.niDigital_ClockGenerator_GenerateClock_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ClockGenerator_GenerateClock_cfunc(vi, channel_list, frequency, select_digital_function)

    def niDigital_Commit(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDigital_Commit_cfunc is None:
                self.niDigital_Commit_cfunc = self._get_library_function('niDigital_Commit')
                self.niDigital_Commit_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDigital_Commit_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_Commit_cfunc(vi)

    def niDigital_ConfigureActiveLoadLevels(self, vi, channel_list, iol, ioh, vcom):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ConfigureActiveLoadLevels_cfunc is None:
                self.niDigital_ConfigureActiveLoadLevels_cfunc = self._get_library_function('niDigital_ConfigureActiveLoadLevels')
                self.niDigital_ConfigureActiveLoadLevels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niDigital_ConfigureActiveLoadLevels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ConfigureActiveLoadLevels_cfunc(vi, channel_list, iol, ioh, vcom)

    def niDigital_ConfigurePatternBurstSites(self, vi, site_list):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ConfigurePatternBurstSites_cfunc is None:
                self.niDigital_ConfigurePatternBurstSites_cfunc = self._get_library_function('niDigital_ConfigurePatternBurstSites')
                self.niDigital_ConfigurePatternBurstSites_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_ConfigurePatternBurstSites_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ConfigurePatternBurstSites_cfunc(vi, site_list)

    def niDigital_ConfigureTimeSetCompareEdgesStrobe(self, vi, pin_list, time_set_name, strobe_edge):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ConfigureTimeSetCompareEdgesStrobe_cfunc is None:
                self.niDigital_ConfigureTimeSetCompareEdgesStrobe_cfunc = self._get_library_function('niDigital_ConfigureTimeSetCompareEdgesStrobe')
                self.niDigital_ConfigureTimeSetCompareEdgesStrobe_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViReal64]  # noqa: F405
                self.niDigital_ConfigureTimeSetCompareEdgesStrobe_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ConfigureTimeSetCompareEdgesStrobe_cfunc(vi, pin_list, time_set_name, strobe_edge)

    def niDigital_ConfigureTimeSetCompareEdgesStrobe2x(self, vi, pin_list, time_set_name, strobe_edge, strobe2_edge):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ConfigureTimeSetCompareEdgesStrobe2x_cfunc is None:
                self.niDigital_ConfigureTimeSetCompareEdgesStrobe2x_cfunc = self._get_library_function('niDigital_ConfigureTimeSetCompareEdgesStrobe2x')
                self.niDigital_ConfigureTimeSetCompareEdgesStrobe2x_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViReal64, ViReal64]  # noqa: F405
                self.niDigital_ConfigureTimeSetCompareEdgesStrobe2x_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ConfigureTimeSetCompareEdgesStrobe2x_cfunc(vi, pin_list, time_set_name, strobe_edge, strobe2_edge)

    def niDigital_ConfigureTimeSetDriveEdges(self, vi, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ConfigureTimeSetDriveEdges_cfunc is None:
                self.niDigital_ConfigureTimeSetDriveEdges_cfunc = self._get_library_function('niDigital_ConfigureTimeSetDriveEdges')
                self.niDigital_ConfigureTimeSetDriveEdges_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ViReal64, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niDigital_ConfigureTimeSetDriveEdges_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ConfigureTimeSetDriveEdges_cfunc(vi, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge)

    def niDigital_ConfigureTimeSetDriveEdges2x(self, vi, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge, drive_data2_edge, drive_return2_edge):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ConfigureTimeSetDriveEdges2x_cfunc is None:
                self.niDigital_ConfigureTimeSetDriveEdges2x_cfunc = self._get_library_function('niDigital_ConfigureTimeSetDriveEdges2x')
                self.niDigital_ConfigureTimeSetDriveEdges2x_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ViReal64, ViReal64, ViReal64, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niDigital_ConfigureTimeSetDriveEdges2x_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ConfigureTimeSetDriveEdges2x_cfunc(vi, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge, drive_data2_edge, drive_return2_edge)

    def niDigital_ConfigureTimeSetDriveFormat(self, vi, pin_list, time_set_name, drive_format):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ConfigureTimeSetDriveFormat_cfunc is None:
                self.niDigital_ConfigureTimeSetDriveFormat_cfunc = self._get_library_function('niDigital_ConfigureTimeSetDriveFormat')
                self.niDigital_ConfigureTimeSetDriveFormat_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niDigital_ConfigureTimeSetDriveFormat_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ConfigureTimeSetDriveFormat_cfunc(vi, pin_list, time_set_name, drive_format)

    def niDigital_ConfigureTimeSetEdge(self, vi, pin_list, time_set_name, edge, time):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ConfigureTimeSetEdge_cfunc is None:
                self.niDigital_ConfigureTimeSetEdge_cfunc = self._get_library_function('niDigital_ConfigureTimeSetEdge')
                self.niDigital_ConfigureTimeSetEdge_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ViReal64]  # noqa: F405
                self.niDigital_ConfigureTimeSetEdge_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ConfigureTimeSetEdge_cfunc(vi, pin_list, time_set_name, edge, time)

    def niDigital_ConfigureTimeSetEdgeMultiplier(self, vi, pin_list, time_set_name, edge_multiplier):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ConfigureTimeSetEdgeMultiplier_cfunc is None:
                self.niDigital_ConfigureTimeSetEdgeMultiplier_cfunc = self._get_library_function('niDigital_ConfigureTimeSetEdgeMultiplier')
                self.niDigital_ConfigureTimeSetEdgeMultiplier_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niDigital_ConfigureTimeSetEdgeMultiplier_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ConfigureTimeSetEdgeMultiplier_cfunc(vi, pin_list, time_set_name, edge_multiplier)

    def niDigital_ConfigureTimeSetPeriod(self, vi, time_set_name, period):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ConfigureTimeSetPeriod_cfunc is None:
                self.niDigital_ConfigureTimeSetPeriod_cfunc = self._get_library_function('niDigital_ConfigureTimeSetPeriod')
                self.niDigital_ConfigureTimeSetPeriod_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64]  # noqa: F405
                self.niDigital_ConfigureTimeSetPeriod_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ConfigureTimeSetPeriod_cfunc(vi, time_set_name, period)

    def niDigital_ConfigureVoltageLevels(self, vi, channel_list, vil, vih, vol, voh, vterm):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ConfigureVoltageLevels_cfunc is None:
                self.niDigital_ConfigureVoltageLevels_cfunc = self._get_library_function('niDigital_ConfigureVoltageLevels')
                self.niDigital_ConfigureVoltageLevels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niDigital_ConfigureVoltageLevels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ConfigureVoltageLevels_cfunc(vi, channel_list, vil, vih, vol, voh, vterm)

    def niDigital_CreateCaptureWaveformFromFileDigicapture(self, vi, waveform_name, waveform_file_path):  # noqa: N802
        with self._func_lock:
            if self.niDigital_CreateCaptureWaveformFromFileDigicapture_cfunc is None:
                self.niDigital_CreateCaptureWaveformFromFileDigicapture_cfunc = self._get_library_function('niDigital_CreateCaptureWaveformFromFileDigicapture')
                self.niDigital_CreateCaptureWaveformFromFileDigicapture_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_CreateCaptureWaveformFromFileDigicapture_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_CreateCaptureWaveformFromFileDigicapture_cfunc(vi, waveform_name, waveform_file_path)

    def niDigital_CreateCaptureWaveformParallel(self, vi, pin_list, waveform_name):  # noqa: N802
        with self._func_lock:
            if self.niDigital_CreateCaptureWaveformParallel_cfunc is None:
                self.niDigital_CreateCaptureWaveformParallel_cfunc = self._get_library_function('niDigital_CreateCaptureWaveformParallel')
                self.niDigital_CreateCaptureWaveformParallel_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_CreateCaptureWaveformParallel_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_CreateCaptureWaveformParallel_cfunc(vi, pin_list, waveform_name)

    def niDigital_CreateCaptureWaveformSerial(self, vi, pin_list, waveform_name, sample_width, bit_order):  # noqa: N802
        with self._func_lock:
            if self.niDigital_CreateCaptureWaveformSerial_cfunc is None:
                self.niDigital_CreateCaptureWaveformSerial_cfunc = self._get_library_function('niDigital_CreateCaptureWaveformSerial')
                self.niDigital_CreateCaptureWaveformSerial_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViUInt32, ViInt32]  # noqa: F405
                self.niDigital_CreateCaptureWaveformSerial_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_CreateCaptureWaveformSerial_cfunc(vi, pin_list, waveform_name, sample_width, bit_order)

    def niDigital_CreateSourceWaveformFromFileTDMS(self, vi, waveform_name, waveform_file_path, write_waveform_data):  # noqa: N802
        with self._func_lock:
            if self.niDigital_CreateSourceWaveformFromFileTDMS_cfunc is None:
                self.niDigital_CreateSourceWaveformFromFileTDMS_cfunc = self._get_library_function('niDigital_CreateSourceWaveformFromFileTDMS')
                self.niDigital_CreateSourceWaveformFromFileTDMS_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViBoolean]  # noqa: F405
                self.niDigital_CreateSourceWaveformFromFileTDMS_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_CreateSourceWaveformFromFileTDMS_cfunc(vi, waveform_name, waveform_file_path, write_waveform_data)

    def niDigital_CreateSourceWaveformParallel(self, vi, pin_list, waveform_name, data_mapping):  # noqa: N802
        with self._func_lock:
            if self.niDigital_CreateSourceWaveformParallel_cfunc is None:
                self.niDigital_CreateSourceWaveformParallel_cfunc = self._get_library_function('niDigital_CreateSourceWaveformParallel')
                self.niDigital_CreateSourceWaveformParallel_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niDigital_CreateSourceWaveformParallel_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_CreateSourceWaveformParallel_cfunc(vi, pin_list, waveform_name, data_mapping)

    def niDigital_CreateSourceWaveformSerial(self, vi, pin_list, waveform_name, data_mapping, sample_width, bit_order):  # noqa: N802
        with self._func_lock:
            if self.niDigital_CreateSourceWaveformSerial_cfunc is None:
                self.niDigital_CreateSourceWaveformSerial_cfunc = self._get_library_function('niDigital_CreateSourceWaveformSerial')
                self.niDigital_CreateSourceWaveformSerial_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ViUInt32, ViInt32]  # noqa: F405
                self.niDigital_CreateSourceWaveformSerial_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_CreateSourceWaveformSerial_cfunc(vi, pin_list, waveform_name, data_mapping, sample_width, bit_order)

    def niDigital_CreateTimeSet(self, vi, name):  # noqa: N802
        with self._func_lock:
            if self.niDigital_CreateTimeSet_cfunc is None:
                self.niDigital_CreateTimeSet_cfunc = self._get_library_function('niDigital_CreateTimeSet')
                self.niDigital_CreateTimeSet_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_CreateTimeSet_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_CreateTimeSet_cfunc(vi, name)

    def niDigital_DeleteAllTimeSets(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDigital_DeleteAllTimeSets_cfunc is None:
                self.niDigital_DeleteAllTimeSets_cfunc = self._get_library_function('niDigital_DeleteAllTimeSets')
                self.niDigital_DeleteAllTimeSets_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDigital_DeleteAllTimeSets_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_DeleteAllTimeSets_cfunc(vi)

    def niDigital_DisableSites(self, vi, site_list):  # noqa: N802
        with self._func_lock:
            if self.niDigital_DisableSites_cfunc is None:
                self.niDigital_DisableSites_cfunc = self._get_library_function('niDigital_DisableSites')
                self.niDigital_DisableSites_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_DisableSites_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_DisableSites_cfunc(vi, site_list)

    def niDigital_EnableMatchFailCombination(self, session_count, sessions, sync_session):  # noqa: N802
        with self._func_lock:
            if self.niDigital_EnableMatchFailCombination_cfunc is None:
                self.niDigital_EnableMatchFailCombination_cfunc = self._get_library_function('niDigital_EnableMatchFailCombination')
                self.niDigital_EnableMatchFailCombination_cfunc.argtypes = [ViUInt32, ctypes.POINTER(ViSession), ViSession]  # noqa: F405
                self.niDigital_EnableMatchFailCombination_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_EnableMatchFailCombination_cfunc(session_count, sessions, sync_session)

    def niDigital_EnableSites(self, vi, site_list):  # noqa: N802
        with self._func_lock:
            if self.niDigital_EnableSites_cfunc is None:
                self.niDigital_EnableSites_cfunc = self._get_library_function('niDigital_EnableSites')
                self.niDigital_EnableSites_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_EnableSites_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_EnableSites_cfunc(vi, site_list)

    def niDigital_FetchCaptureWaveformU32(self, vi, site_list, waveform_name, samples_to_read, timeout, data_buffer_size, data, actual_num_waveforms, actual_samples_per_waveform):  # noqa: N802
        with self._func_lock:
            if self.niDigital_FetchCaptureWaveformU32_cfunc is None:
                self.niDigital_FetchCaptureWaveformU32_cfunc = self._get_library_function('niDigital_FetchCaptureWaveformU32')
                self.niDigital_FetchCaptureWaveformU32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ViReal64, ViInt32, ctypes.POINTER(ViUInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_FetchCaptureWaveformU32_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_FetchCaptureWaveformU32_cfunc(vi, site_list, waveform_name, samples_to_read, timeout, data_buffer_size, data, actual_num_waveforms, actual_samples_per_waveform)

    def niDigital_FetchHistoryRAMCycleInformation(self, vi, site, sample_index, pattern_index, time_set_index, vector_number, cycle_number, num_dut_cycles):  # noqa: N802
        with self._func_lock:
            if self.niDigital_FetchHistoryRAMCycleInformation_cfunc is None:
                self.niDigital_FetchHistoryRAMCycleInformation_cfunc = self._get_library_function('niDigital_FetchHistoryRAMCycleInformation')
                self.niDigital_FetchHistoryRAMCycleInformation_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt64, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt64), ctypes.POINTER(ViInt64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_FetchHistoryRAMCycleInformation_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_FetchHistoryRAMCycleInformation_cfunc(vi, site, sample_index, pattern_index, time_set_index, vector_number, cycle_number, num_dut_cycles)

    def niDigital_FetchHistoryRAMCyclePinData(self, vi, site, pin_list, sample_index, dut_cycle_index, pin_data_buffer_size, expected_pin_states, actual_pin_states, per_pin_pass_fail, actual_num_pin_data):  # noqa: N802
        with self._func_lock:
            if self.niDigital_FetchHistoryRAMCyclePinData_cfunc is None:
                self.niDigital_FetchHistoryRAMCyclePinData_cfunc = self._get_library_function('niDigital_FetchHistoryRAMCyclePinData')
                self.niDigital_FetchHistoryRAMCyclePinData_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt64, ViInt32, ViInt32, ctypes.POINTER(ViUInt8), ctypes.POINTER(ViUInt8), ctypes.POINTER(ViBoolean), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_FetchHistoryRAMCyclePinData_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_FetchHistoryRAMCyclePinData_cfunc(vi, site, pin_list, sample_index, dut_cycle_index, pin_data_buffer_size, expected_pin_states, actual_pin_states, per_pin_pass_fail, actual_num_pin_data)

    def niDigital_FetchHistoryRAMScanCycleNumber(self, vi, site, sample_index, scan_cycle_number):  # noqa: N802
        with self._func_lock:
            if self.niDigital_FetchHistoryRAMScanCycleNumber_cfunc is None:
                self.niDigital_FetchHistoryRAMScanCycleNumber_cfunc = self._get_library_function('niDigital_FetchHistoryRAMScanCycleNumber')
                self.niDigital_FetchHistoryRAMScanCycleNumber_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt64, ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niDigital_FetchHistoryRAMScanCycleNumber_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_FetchHistoryRAMScanCycleNumber_cfunc(vi, site, sample_index, scan_cycle_number)

    def niDigital_FrequencyCounter_MeasureFrequency(self, vi, channel_list, frequencies_buffer_size, frequencies, actual_num_frequencies):  # noqa: N802
        with self._func_lock:
            if self.niDigital_FrequencyCounter_MeasureFrequency_cfunc is None:
                self.niDigital_FrequencyCounter_MeasureFrequency_cfunc = self._get_library_function('niDigital_FrequencyCounter_MeasureFrequency')
                self.niDigital_FrequencyCounter_MeasureFrequency_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_FrequencyCounter_MeasureFrequency_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_FrequencyCounter_MeasureFrequency_cfunc(vi, channel_list, frequencies_buffer_size, frequencies, actual_num_frequencies)

    def niDigital_GetAttributeViBoolean(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetAttributeViBoolean_cfunc is None:
                self.niDigital_GetAttributeViBoolean_cfunc = self._get_library_function('niDigital_GetAttributeViBoolean')
                self.niDigital_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDigital_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetAttributeViBoolean_cfunc(vi, channel_name, attribute, value)

    def niDigital_GetAttributeViInt32(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetAttributeViInt32_cfunc is None:
                self.niDigital_GetAttributeViInt32_cfunc = self._get_library_function('niDigital_GetAttributeViInt32')
                self.niDigital_GetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetAttributeViInt32_cfunc(vi, channel_name, attribute, value)

    def niDigital_GetAttributeViInt64(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetAttributeViInt64_cfunc is None:
                self.niDigital_GetAttributeViInt64_cfunc = self._get_library_function('niDigital_GetAttributeViInt64')
                self.niDigital_GetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niDigital_GetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetAttributeViInt64_cfunc(vi, channel_name, attribute, value)

    def niDigital_GetAttributeViReal64(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetAttributeViReal64_cfunc is None:
                self.niDigital_GetAttributeViReal64_cfunc = self._get_library_function('niDigital_GetAttributeViReal64')
                self.niDigital_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDigital_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetAttributeViReal64_cfunc(vi, channel_name, attribute, value)

    def niDigital_GetAttributeViString(self, vi, channel_name, attribute, buffer_size, value):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetAttributeViString_cfunc is None:
                self.niDigital_GetAttributeViString_cfunc = self._get_library_function('niDigital_GetAttributeViString')
                self.niDigital_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetAttributeViString_cfunc(vi, channel_name, attribute, buffer_size, value)

    def niDigital_GetChannelNameFromString(self, vi, indices, name_buffer_size, names):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetChannelNameFromString_cfunc is None:
                self.niDigital_GetChannelNameFromString_cfunc = self._get_library_function('niDigital_GetChannelNameFromString')
                self.niDigital_GetChannelNameFromString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_GetChannelNameFromString_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetChannelNameFromString_cfunc(vi, indices, name_buffer_size, names)

    def niDigital_GetError(self, vi, error_code, error_description_buffer_size, error_description):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetError_cfunc is None:
                self.niDigital_GetError_cfunc = self._get_library_function('niDigital_GetError')
                self.niDigital_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_GetError_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetError_cfunc(vi, error_code, error_description_buffer_size, error_description)

    def niDigital_GetFailCount(self, vi, channel_list, buffer_size, failure_count, actual_num_read):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetFailCount_cfunc is None:
                self.niDigital_GetFailCount_cfunc = self._get_library_function('niDigital_GetFailCount')
                self.niDigital_GetFailCount_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_GetFailCount_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetFailCount_cfunc(vi, channel_list, buffer_size, failure_count, actual_num_read)

    def niDigital_GetHistoryRAMSampleCount(self, vi, site, sample_count):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetHistoryRAMSampleCount_cfunc is None:
                self.niDigital_GetHistoryRAMSampleCount_cfunc = self._get_library_function('niDigital_GetHistoryRAMSampleCount')
                self.niDigital_GetHistoryRAMSampleCount_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niDigital_GetHistoryRAMSampleCount_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetHistoryRAMSampleCount_cfunc(vi, site, sample_count)

    def niDigital_GetPatternName(self, vi, pattern_index, name_buffer_size, name):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetPatternName_cfunc is None:
                self.niDigital_GetPatternName_cfunc = self._get_library_function('niDigital_GetPatternName')
                self.niDigital_GetPatternName_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_GetPatternName_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetPatternName_cfunc(vi, pattern_index, name_buffer_size, name)

    def niDigital_GetPatternPinList(self, vi, start_label, pin_list_buffer_size, pin_list):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetPatternPinList_cfunc is None:
                self.niDigital_GetPatternPinList_cfunc = self._get_library_function('niDigital_GetPatternPinList')
                self.niDigital_GetPatternPinList_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_GetPatternPinList_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetPatternPinList_cfunc(vi, start_label, pin_list_buffer_size, pin_list)

    def niDigital_GetPinName(self, vi, pin_index, name_buffer_size, name):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetPinName_cfunc is None:
                self.niDigital_GetPinName_cfunc = self._get_library_function('niDigital_GetPinName')
                self.niDigital_GetPinName_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_GetPinName_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetPinName_cfunc(vi, pin_index, name_buffer_size, name)

    def niDigital_GetPinResultsPinInformation(self, vi, channel_list, buffer_size, pin_indexes, site_numbers, channel_indexes, actual_num_values):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetPinResultsPinInformation_cfunc is None:
                self.niDigital_GetPinResultsPinInformation_cfunc = self._get_library_function('niDigital_GetPinResultsPinInformation')
                self.niDigital_GetPinResultsPinInformation_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_GetPinResultsPinInformation_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetPinResultsPinInformation_cfunc(vi, channel_list, buffer_size, pin_indexes, site_numbers, channel_indexes, actual_num_values)

    def niDigital_GetSitePassFail(self, vi, site_list, pass_fail_buffer_size, pass_fail, actual_num_sites):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetSitePassFail_cfunc is None:
                self.niDigital_GetSitePassFail_cfunc = self._get_library_function('niDigital_GetSitePassFail')
                self.niDigital_GetSitePassFail_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViBoolean), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_GetSitePassFail_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetSitePassFail_cfunc(vi, site_list, pass_fail_buffer_size, pass_fail, actual_num_sites)

    def niDigital_GetSiteResultsSiteNumbers(self, vi, site_list, site_result_type, site_numbers_buffer_size, site_numbers, actual_num_site_numbers):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetSiteResultsSiteNumbers_cfunc is None:
                self.niDigital_GetSiteResultsSiteNumbers_cfunc = self._get_library_function('niDigital_GetSiteResultsSiteNumbers')
                self.niDigital_GetSiteResultsSiteNumbers_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_GetSiteResultsSiteNumbers_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetSiteResultsSiteNumbers_cfunc(vi, site_list, site_result_type, site_numbers_buffer_size, site_numbers, actual_num_site_numbers)

    def niDigital_GetTimeSetDriveFormat(self, vi, pin, time_set_name, format):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetTimeSetDriveFormat_cfunc is None:
                self.niDigital_GetTimeSetDriveFormat_cfunc = self._get_library_function('niDigital_GetTimeSetDriveFormat')
                self.niDigital_GetTimeSetDriveFormat_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_GetTimeSetDriveFormat_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetTimeSetDriveFormat_cfunc(vi, pin, time_set_name, format)

    def niDigital_GetTimeSetEdge(self, vi, pin, time_set_name, edge, time):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetTimeSetEdge_cfunc is None:
                self.niDigital_GetTimeSetEdge_cfunc = self._get_library_function('niDigital_GetTimeSetEdge')
                self.niDigital_GetTimeSetEdge_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDigital_GetTimeSetEdge_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetTimeSetEdge_cfunc(vi, pin, time_set_name, edge, time)

    def niDigital_GetTimeSetEdgeMultiplier(self, vi, pin, time_set_name, edge_multiplier):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetTimeSetEdgeMultiplier_cfunc is None:
                self.niDigital_GetTimeSetEdgeMultiplier_cfunc = self._get_library_function('niDigital_GetTimeSetEdgeMultiplier')
                self.niDigital_GetTimeSetEdgeMultiplier_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_GetTimeSetEdgeMultiplier_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetTimeSetEdgeMultiplier_cfunc(vi, pin, time_set_name, edge_multiplier)

    def niDigital_GetTimeSetName(self, vi, time_set_index, name_buffer_size, name):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetTimeSetName_cfunc is None:
                self.niDigital_GetTimeSetName_cfunc = self._get_library_function('niDigital_GetTimeSetName')
                self.niDigital_GetTimeSetName_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_GetTimeSetName_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetTimeSetName_cfunc(vi, time_set_index, name_buffer_size, name)

    def niDigital_GetTimeSetPeriod(self, vi, time_set_name, period):  # noqa: N802
        with self._func_lock:
            if self.niDigital_GetTimeSetPeriod_cfunc is None:
                self.niDigital_GetTimeSetPeriod_cfunc = self._get_library_function('niDigital_GetTimeSetPeriod')
                self.niDigital_GetTimeSetPeriod_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDigital_GetTimeSetPeriod_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_GetTimeSetPeriod_cfunc(vi, time_set_name, period)

    def niDigital_InitWithOptions(self, resource_name, id_query, reset_device, option_string, new_vi):  # noqa: N802
        with self._func_lock:
            if self.niDigital_InitWithOptions_cfunc is None:
                self.niDigital_InitWithOptions_cfunc = self._get_library_function('niDigital_InitWithOptions')
                self.niDigital_InitWithOptions_cfunc.argtypes = [ctypes.POINTER(ViChar), ViBoolean, ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niDigital_InitWithOptions_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_InitWithOptions_cfunc(resource_name, id_query, reset_device, option_string, new_vi)

    def niDigital_Initiate(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDigital_Initiate_cfunc is None:
                self.niDigital_Initiate_cfunc = self._get_library_function('niDigital_Initiate')
                self.niDigital_Initiate_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDigital_Initiate_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_Initiate_cfunc(vi)

    def niDigital_IsDone(self, vi, done):  # noqa: N802
        with self._func_lock:
            if self.niDigital_IsDone_cfunc is None:
                self.niDigital_IsDone_cfunc = self._get_library_function('niDigital_IsDone')
                self.niDigital_IsDone_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDigital_IsDone_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_IsDone_cfunc(vi, done)

    def niDigital_IsSiteEnabled(self, vi, site, enable):  # noqa: N802
        with self._func_lock:
            if self.niDigital_IsSiteEnabled_cfunc is None:
                self.niDigital_IsSiteEnabled_cfunc = self._get_library_function('niDigital_IsSiteEnabled')
                self.niDigital_IsSiteEnabled_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDigital_IsSiteEnabled_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_IsSiteEnabled_cfunc(vi, site, enable)

    def niDigital_LoadLevels(self, vi, file_path):  # noqa: N802
        with self._func_lock:
            if self.niDigital_LoadLevels_cfunc is None:
                self.niDigital_LoadLevels_cfunc = self._get_library_function('niDigital_LoadLevels')
                self.niDigital_LoadLevels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_LoadLevels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_LoadLevels_cfunc(vi, file_path)

    def niDigital_LoadPattern(self, vi, file_path):  # noqa: N802
        with self._func_lock:
            if self.niDigital_LoadPattern_cfunc is None:
                self.niDigital_LoadPattern_cfunc = self._get_library_function('niDigital_LoadPattern')
                self.niDigital_LoadPattern_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_LoadPattern_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_LoadPattern_cfunc(vi, file_path)

    def niDigital_LoadPinMap(self, vi, file_path):  # noqa: N802
        with self._func_lock:
            if self.niDigital_LoadPinMap_cfunc is None:
                self.niDigital_LoadPinMap_cfunc = self._get_library_function('niDigital_LoadPinMap')
                self.niDigital_LoadPinMap_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_LoadPinMap_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_LoadPinMap_cfunc(vi, file_path)

    def niDigital_LoadSpecifications(self, vi, file_path):  # noqa: N802
        with self._func_lock:
            if self.niDigital_LoadSpecifications_cfunc is None:
                self.niDigital_LoadSpecifications_cfunc = self._get_library_function('niDigital_LoadSpecifications')
                self.niDigital_LoadSpecifications_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_LoadSpecifications_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_LoadSpecifications_cfunc(vi, file_path)

    def niDigital_LoadTiming(self, vi, file_path):  # noqa: N802
        with self._func_lock:
            if self.niDigital_LoadTiming_cfunc is None:
                self.niDigital_LoadTiming_cfunc = self._get_library_function('niDigital_LoadTiming')
                self.niDigital_LoadTiming_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_LoadTiming_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_LoadTiming_cfunc(vi, file_path)

    def niDigital_LockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niDigital_LockSession_cfunc is None:
                self.niDigital_LockSession_cfunc = self._get_library_function('niDigital_LockSession')
                self.niDigital_LockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDigital_LockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_LockSession_cfunc(vi, caller_has_lock)

    def niDigital_PPMU_Measure(self, vi, channel_list, measurement_type, buffer_size, measurements, actual_num_read):  # noqa: N802
        with self._func_lock:
            if self.niDigital_PPMU_Measure_cfunc is None:
                self.niDigital_PPMU_Measure_cfunc = self._get_library_function('niDigital_PPMU_Measure')
                self.niDigital_PPMU_Measure_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_PPMU_Measure_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_PPMU_Measure_cfunc(vi, channel_list, measurement_type, buffer_size, measurements, actual_num_read)

    def niDigital_PPMU_Source(self, vi, channel_list):  # noqa: N802
        with self._func_lock:
            if self.niDigital_PPMU_Source_cfunc is None:
                self.niDigital_PPMU_Source_cfunc = self._get_library_function('niDigital_PPMU_Source')
                self.niDigital_PPMU_Source_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_PPMU_Source_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_PPMU_Source_cfunc(vi, channel_list)

    def niDigital_ReadSequencerFlag(self, vi, flag, value):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ReadSequencerFlag_cfunc is None:
                self.niDigital_ReadSequencerFlag_cfunc = self._get_library_function('niDigital_ReadSequencerFlag')
                self.niDigital_ReadSequencerFlag_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDigital_ReadSequencerFlag_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ReadSequencerFlag_cfunc(vi, flag, value)

    def niDigital_ReadSequencerRegister(self, vi, reg, value):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ReadSequencerRegister_cfunc is None:
                self.niDigital_ReadSequencerRegister_cfunc = self._get_library_function('niDigital_ReadSequencerRegister')
                self.niDigital_ReadSequencerRegister_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_ReadSequencerRegister_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ReadSequencerRegister_cfunc(vi, reg, value)

    def niDigital_ReadStatic(self, vi, channel_list, buffer_size, data, actual_num_read):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ReadStatic_cfunc is None:
                self.niDigital_ReadStatic_cfunc = self._get_library_function('niDigital_ReadStatic')
                self.niDigital_ReadStatic_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViUInt8), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_ReadStatic_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ReadStatic_cfunc(vi, channel_list, buffer_size, data, actual_num_read)

    def niDigital_ResetDevice(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDigital_ResetDevice_cfunc is None:
                self.niDigital_ResetDevice_cfunc = self._get_library_function('niDigital_ResetDevice')
                self.niDigital_ResetDevice_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDigital_ResetDevice_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_ResetDevice_cfunc(vi)

    def niDigital_SelfCalibrate(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDigital_SelfCalibrate_cfunc is None:
                self.niDigital_SelfCalibrate_cfunc = self._get_library_function('niDigital_SelfCalibrate')
                self.niDigital_SelfCalibrate_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDigital_SelfCalibrate_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_SelfCalibrate_cfunc(vi)

    def niDigital_SendSoftwareEdgeTrigger(self, vi, trigger, trigger_identifier):  # noqa: N802
        with self._func_lock:
            if self.niDigital_SendSoftwareEdgeTrigger_cfunc is None:
                self.niDigital_SendSoftwareEdgeTrigger_cfunc = self._get_library_function('niDigital_SendSoftwareEdgeTrigger')
                self.niDigital_SendSoftwareEdgeTrigger_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_SendSoftwareEdgeTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_SendSoftwareEdgeTrigger_cfunc(vi, trigger, trigger_identifier)

    def niDigital_SetAttributeViBoolean(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niDigital_SetAttributeViBoolean_cfunc is None:
                self.niDigital_SetAttributeViBoolean_cfunc = self._get_library_function('niDigital_SetAttributeViBoolean')
                self.niDigital_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niDigital_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_SetAttributeViBoolean_cfunc(vi, channel_name, attribute, value)

    def niDigital_SetAttributeViInt32(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niDigital_SetAttributeViInt32_cfunc is None:
                self.niDigital_SetAttributeViInt32_cfunc = self._get_library_function('niDigital_SetAttributeViInt32')
                self.niDigital_SetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niDigital_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_SetAttributeViInt32_cfunc(vi, channel_name, attribute, value)

    def niDigital_SetAttributeViInt64(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niDigital_SetAttributeViInt64_cfunc is None:
                self.niDigital_SetAttributeViInt64_cfunc = self._get_library_function('niDigital_SetAttributeViInt64')
                self.niDigital_SetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt64]  # noqa: F405
                self.niDigital_SetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_SetAttributeViInt64_cfunc(vi, channel_name, attribute, value)

    def niDigital_SetAttributeViReal64(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niDigital_SetAttributeViReal64_cfunc is None:
                self.niDigital_SetAttributeViReal64_cfunc = self._get_library_function('niDigital_SetAttributeViReal64')
                self.niDigital_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niDigital_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_SetAttributeViReal64_cfunc(vi, channel_name, attribute, value)

    def niDigital_SetAttributeViString(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niDigital_SetAttributeViString_cfunc is None:
                self.niDigital_SetAttributeViString_cfunc = self._get_library_function('niDigital_SetAttributeViString')
                self.niDigital_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_SetAttributeViString_cfunc(vi, channel_name, attribute, value)

    def niDigital_SetRuntimeEnvironment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        with self._func_lock:
            if self.niDigital_SetRuntimeEnvironment_cfunc is None:
                self.niDigital_SetRuntimeEnvironment_cfunc = self._get_library_function('niDigital_SetRuntimeEnvironment')
                self.niDigital_SetRuntimeEnvironment_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_SetRuntimeEnvironment_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_SetRuntimeEnvironment_cfunc(environment, environment_version, reserved1, reserved2)

    def niDigital_TDR(self, vi, channel_list, apply_offsets, offsets_buffer_size, offsets, actual_num_offsets):  # noqa: N802
        with self._func_lock:
            if self.niDigital_TDR_cfunc is None:
                self.niDigital_TDR_cfunc = self._get_library_function('niDigital_TDR')
                self.niDigital_TDR_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViBoolean, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDigital_TDR_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_TDR_cfunc(vi, channel_list, apply_offsets, offsets_buffer_size, offsets, actual_num_offsets)

    def niDigital_UnloadAllPatterns(self, vi, unload_keep_alive_pattern):  # noqa: N802
        with self._func_lock:
            if self.niDigital_UnloadAllPatterns_cfunc is None:
                self.niDigital_UnloadAllPatterns_cfunc = self._get_library_function('niDigital_UnloadAllPatterns')
                self.niDigital_UnloadAllPatterns_cfunc.argtypes = [ViSession, ViBoolean]  # noqa: F405
                self.niDigital_UnloadAllPatterns_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_UnloadAllPatterns_cfunc(vi, unload_keep_alive_pattern)

    def niDigital_UnloadSpecifications(self, vi, file_path):  # noqa: N802
        with self._func_lock:
            if self.niDigital_UnloadSpecifications_cfunc is None:
                self.niDigital_UnloadSpecifications_cfunc = self._get_library_function('niDigital_UnloadSpecifications')
                self.niDigital_UnloadSpecifications_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_UnloadSpecifications_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_UnloadSpecifications_cfunc(vi, file_path)

    def niDigital_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niDigital_UnlockSession_cfunc is None:
                self.niDigital_UnlockSession_cfunc = self._get_library_function('niDigital_UnlockSession')
                self.niDigital_UnlockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDigital_UnlockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_UnlockSession_cfunc(vi, caller_has_lock)

    def niDigital_WaitUntilDone(self, vi, timeout):  # noqa: N802
        with self._func_lock:
            if self.niDigital_WaitUntilDone_cfunc is None:
                self.niDigital_WaitUntilDone_cfunc = self._get_library_function('niDigital_WaitUntilDone')
                self.niDigital_WaitUntilDone_cfunc.argtypes = [ViSession, ViReal64]  # noqa: F405
                self.niDigital_WaitUntilDone_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_WaitUntilDone_cfunc(vi, timeout)

    def niDigital_WriteSequencerFlag(self, vi, flag, value):  # noqa: N802
        with self._func_lock:
            if self.niDigital_WriteSequencerFlag_cfunc is None:
                self.niDigital_WriteSequencerFlag_cfunc = self._get_library_function('niDigital_WriteSequencerFlag')
                self.niDigital_WriteSequencerFlag_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViBoolean]  # noqa: F405
                self.niDigital_WriteSequencerFlag_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_WriteSequencerFlag_cfunc(vi, flag, value)

    def niDigital_WriteSequencerRegister(self, vi, reg, value):  # noqa: N802
        with self._func_lock:
            if self.niDigital_WriteSequencerRegister_cfunc is None:
                self.niDigital_WriteSequencerRegister_cfunc = self._get_library_function('niDigital_WriteSequencerRegister')
                self.niDigital_WriteSequencerRegister_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niDigital_WriteSequencerRegister_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_WriteSequencerRegister_cfunc(vi, reg, value)

    def niDigital_WriteSourceWaveformBroadcastU32(self, vi, waveform_name, waveform_size, waveform_data):  # noqa: N802
        with self._func_lock:
            if self.niDigital_WriteSourceWaveformBroadcastU32_cfunc is None:
                self.niDigital_WriteSourceWaveformBroadcastU32_cfunc = self._get_library_function('niDigital_WriteSourceWaveformBroadcastU32')
                self.niDigital_WriteSourceWaveformBroadcastU32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViUInt32)]  # noqa: F405
                self.niDigital_WriteSourceWaveformBroadcastU32_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_WriteSourceWaveformBroadcastU32_cfunc(vi, waveform_name, waveform_size, waveform_data)

    def niDigital_WriteSourceWaveformDataFromFileTDMS(self, vi, waveform_name, waveform_file_path):  # noqa: N802
        with self._func_lock:
            if self.niDigital_WriteSourceWaveformDataFromFileTDMS_cfunc is None:
                self.niDigital_WriteSourceWaveformDataFromFileTDMS_cfunc = self._get_library_function('niDigital_WriteSourceWaveformDataFromFileTDMS')
                self.niDigital_WriteSourceWaveformDataFromFileTDMS_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_WriteSourceWaveformDataFromFileTDMS_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_WriteSourceWaveformDataFromFileTDMS_cfunc(vi, waveform_name, waveform_file_path)

    def niDigital_WriteSourceWaveformSiteUniqueU32(self, vi, site_list, waveform_name, num_waveforms, samples_per_waveform, waveform_data):  # noqa: N802
        with self._func_lock:
            if self.niDigital_WriteSourceWaveformSiteUniqueU32_cfunc is None:
                self.niDigital_WriteSourceWaveformSiteUniqueU32_cfunc = self._get_library_function('niDigital_WriteSourceWaveformSiteUniqueU32')
                self.niDigital_WriteSourceWaveformSiteUniqueU32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ViInt32, ctypes.POINTER(ViUInt32)]  # noqa: F405
                self.niDigital_WriteSourceWaveformSiteUniqueU32_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_WriteSourceWaveformSiteUniqueU32_cfunc(vi, site_list, waveform_name, num_waveforms, samples_per_waveform, waveform_data)

    def niDigital_WriteStatic(self, vi, channel_list, state):  # noqa: N802
        with self._func_lock:
            if self.niDigital_WriteStatic_cfunc is None:
                self.niDigital_WriteStatic_cfunc = self._get_library_function('niDigital_WriteStatic')
                self.niDigital_WriteStatic_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViUInt8]  # noqa: F405
                self.niDigital_WriteStatic_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_WriteStatic_cfunc(vi, channel_list, state)

    def niDigital_close(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDigital_close_cfunc is None:
                self.niDigital_close_cfunc = self._get_library_function('niDigital_close')
                self.niDigital_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDigital_close_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_close_cfunc(vi)

    def niDigital_error_message(self, vi, error_code, error_message):  # noqa: N802
        with self._func_lock:
            if self.niDigital_error_message_cfunc is None:
                self.niDigital_error_message_cfunc = self._get_library_function('niDigital_error_message')
                self.niDigital_error_message_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_error_message_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_error_message_cfunc(vi, error_code, error_message)

    def niDigital_reset(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDigital_reset_cfunc is None:
                self.niDigital_reset_cfunc = self._get_library_function('niDigital_reset')
                self.niDigital_reset_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDigital_reset_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_reset_cfunc(vi)

    def niDigital_self_test(self, vi, test_result, test_message):  # noqa: N802
        with self._func_lock:
            if self.niDigital_self_test_cfunc is None:
                self.niDigital_self_test_cfunc = self._get_library_function('niDigital_self_test')
                self.niDigital_self_test_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDigital_self_test_cfunc.restype = ViStatus  # noqa: F405
        return self.niDigital_self_test_cfunc(vi, test_result, test_message)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidigital/nidigital/_library_interpreter.py sha256=5fc3712349fbb21dc71abbecfcfa5b3996d033a03cff8f2f8772b936356a0daa bytes=76275 -->
## FILE: generated/nidigital/nidigital/_library_interpreter.py

- repository: `ni/nimi-python`
- source_path: `generated/nidigital/nidigital/_library_interpreter.py`
- sha256: `5fc3712349fbb21dc71abbecfcfa5b3996d033a03cff8f2f8772b936356a0daa`
- bytes: 76275

````python
# -*- coding: utf-8 -*-
# This file was generated

import array
import ctypes
import hightime  # noqa: F401
import platform

import nidigital._library_singleton as _library_singleton
import nidigital._visatype as _visatype
import nidigital.enums as enums  # noqa: F401
import nidigital.errors as errors

import nidigital.history_ram_cycle_information as history_ram_cycle_information  # noqa: F401


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
        error_code = self._library.niDigital_Abort(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def abort_keep_alive(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_AbortKeepAlive(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def apply_levels_and_timing(self, site_list, levels_sheet, timing_sheet, initial_state_high_pins, initial_state_low_pins, initial_state_tristate_pins):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C010
        levels_sheet_ctype = ctypes.create_string_buffer(levels_sheet.encode(self._encoding))  # case C020
        timing_sheet_ctype = ctypes.create_string_buffer(timing_sheet.encode(self._encoding))  # case C020
        initial_state_high_pins_ctype = ctypes.create_string_buffer(initial_state_high_pins.encode(self._encoding))  # case C020
        initial_state_low_pins_ctype = ctypes.create_string_buffer(initial_state_low_pins.encode(self._encoding))  # case C020
        initial_state_tristate_pins_ctype = ctypes.create_string_buffer(initial_state_tristate_pins.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_ApplyLevelsAndTiming(vi_ctype, site_list_ctype, levels_sheet_ctype, timing_sheet_ctype, initial_state_high_pins_ctype, initial_state_low_pins_ctype, initial_state_tristate_pins_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def apply_tdr_offsets(self, channel_list, offsets):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        num_offsets_ctype = _visatype.ViInt32(0 if offsets is None else len(offsets))  # case S160
        offsets_ctype = _get_ctypes_pointer_for_buffer(value=offsets, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.niDigital_ApplyTDROffsets(vi_ctype, channel_list_ctype, num_offsets_ctype, offsets_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def burst_pattern(self, site_list, start_label, select_digital_function, wait_until_done, timeout):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C010
        start_label_ctype = ctypes.create_string_buffer(start_label.encode(self._encoding))  # case C020
        select_digital_function_ctype = _visatype.ViBoolean(select_digital_function)  # case S150
        wait_until_done_ctype = _visatype.ViBoolean(wait_until_done)  # case S150
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        error_code = self._library.niDigital_BurstPattern(vi_ctype, site_list_ctype, start_label_ctype, select_digital_function_ctype, wait_until_done_ctype, timeout_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clock_generator_abort(self, channel_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        error_code = self._library.niDigital_ClockGenerator_Abort(vi_ctype, channel_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clock_generator_generate_clock(self, channel_list, frequency, select_digital_function):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        frequency_ctype = _visatype.ViReal64(frequency)  # case S150
        select_digital_function_ctype = _visatype.ViBoolean(select_digital_function)  # case S150
        error_code = self._library.niDigital_ClockGenerator_GenerateClock(vi_ctype, channel_list_ctype, frequency_ctype, select_digital_function_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def commit(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_Commit(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_active_load_levels(self, channel_list, iol, ioh, vcom):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        iol_ctype = _visatype.ViReal64(iol)  # case S150
        ioh_ctype = _visatype.ViReal64(ioh)  # case S150
        vcom_ctype = _visatype.ViReal64(vcom)  # case S150
        error_code = self._library.niDigital_ConfigureActiveLoadLevels(vi_ctype, channel_list_ctype, iol_ctype, ioh_ctype, vcom_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_pattern_burst_sites(self, site_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C010
        error_code = self._library.niDigital_ConfigurePatternBurstSites(vi_ctype, site_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_time_set_compare_edges_strobe(self, pin_list, time_set_name, strobe_edge):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        strobe_edge_ctype = _visatype.ViReal64(strobe_edge)  # case S150
        error_code = self._library.niDigital_ConfigureTimeSetCompareEdgesStrobe(vi_ctype, pin_list_ctype, time_set_name_ctype, strobe_edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_time_set_compare_edges_strobe2x(self, pin_list, time_set_name, strobe_edge, strobe2_edge):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        strobe_edge_ctype = _visatype.ViReal64(strobe_edge)  # case S150
        strobe2_edge_ctype = _visatype.ViReal64(strobe2_edge)  # case S150
        error_code = self._library.niDigital_ConfigureTimeSetCompareEdgesStrobe2x(vi_ctype, pin_list_ctype, time_set_name_ctype, strobe_edge_ctype, strobe2_edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_time_set_drive_edges(self, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        format_ctype = _visatype.ViInt32(format.value)  # case S130
        drive_on_edge_ctype = _visatype.ViReal64(drive_on_edge)  # case S150
        drive_data_edge_ctype = _visatype.ViReal64(drive_data_edge)  # case S150
        drive_return_edge_ctype = _visatype.ViReal64(drive_return_edge)  # case S150
        drive_off_edge_ctype = _visatype.ViReal64(drive_off_edge)  # case S150
        error_code = self._library.niDigital_ConfigureTimeSetDriveEdges(vi_ctype, pin_list_ctype, time_set_name_ctype, format_ctype, drive_on_edge_ctype, drive_data_edge_ctype, drive_return_edge_ctype, drive_off_edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_time_set_drive_edges2x(self, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge, drive_data2_edge, drive_return2_edge):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        format_ctype = _visatype.ViInt32(format.value)  # case S130
        drive_on_edge_ctype = _visatype.ViReal64(drive_on_edge)  # case S150
        drive_data_edge_ctype = _visatype.ViReal64(drive_data_edge)  # case S150
        drive_return_edge_ctype = _visatype.ViReal64(drive_return_edge)  # case S150
        drive_off_edge_ctype = _visatype.ViReal64(drive_off_edge)  # case S150
        drive_data2_edge_ctype = _visatype.ViReal64(drive_data2_edge)  # case S150
        drive_return2_edge_ctype = _visatype.ViReal64(drive_return2_edge)  # case S150
        error_code = self._library.niDigital_ConfigureTimeSetDriveEdges2x(vi_ctype, pin_list_ctype, time_set_name_ctype, format_ctype, drive_on_edge_ctype, drive_data_edge_ctype, drive_return_edge_ctype, drive_off_edge_ctype, drive_data2_edge_ctype, drive_return2_edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_time_set_drive_format(self, pin_list, time_set_name, drive_format):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        drive_format_ctype = _visatype.ViInt32(drive_format.value)  # case S130
        error_code = self._library.niDigital_ConfigureTimeSetDriveFormat(vi_ctype, pin_list_ctype, time_set_name_ctype, drive_format_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_time_set_edge(self, pin_list, time_set_name, edge, time):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        edge_ctype = _visatype.ViInt32(edge.value)  # case S130
        time_ctype = _visatype.ViReal64(time)  # case S150
        error_code = self._library.niDigital_ConfigureTimeSetEdge(vi_ctype, pin_list_ctype, time_set_name_ctype, edge_ctype, time_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_time_set_edge_multiplier(self, pin_list, time_set_name, edge_multiplier):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        edge_multiplier_ctype = _visatype.ViInt32(edge_multiplier)  # case S150
        error_code = self._library.niDigital_ConfigureTimeSetEdgeMultiplier(vi_ctype, pin_list_ctype, time_set_name_ctype, edge_multiplier_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_time_set_period(self, time_set_name, period):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        period_ctype = _visatype.ViReal64(period)  # case S150
        error_code = self._library.niDigital_ConfigureTimeSetPeriod(vi_ctype, time_set_name_ctype, period_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_voltage_levels(self, channel_list, vil, vih, vol, voh, vterm):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        vil_ctype = _visatype.ViReal64(vil)  # case S150
        vih_ctype = _visatype.ViReal64(vih)  # case S150
        vol_ctype = _visatype.ViReal64(vol)  # case S150
        voh_ctype = _visatype.ViReal64(voh)  # case S150
        vterm_ctype = _visatype.ViReal64(vterm)  # case S150
        error_code = self._library.niDigital_ConfigureVoltageLevels(vi_ctype, channel_list_ctype, vil_ctype, vih_ctype, vol_ctype, voh_ctype, vterm_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_capture_waveform_from_file_digicapture(self, waveform_name, waveform_file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        waveform_file_path_ctype = ctypes.create_string_buffer(waveform_file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_CreateCaptureWaveformFromFileDigicapture(vi_ctype, waveform_name_ctype, waveform_file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_capture_waveform_parallel(self, pin_list, waveform_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_CreateCaptureWaveformParallel(vi_ctype, pin_list_ctype, waveform_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_capture_waveform_serial(self, pin_list, waveform_name, sample_width, bit_order):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        sample_width_ctype = _visatype.ViUInt32(sample_width)  # case S150
        bit_order_ctype = _visatype.ViInt32(bit_order.value)  # case S130
        error_code = self._library.niDigital_CreateCaptureWaveformSerial(vi_ctype, pin_list_ctype, waveform_name_ctype, sample_width_ctype, bit_order_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_source_waveform_from_file_tdms(self, waveform_name, waveform_file_path, write_waveform_data):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        waveform_file_path_ctype = ctypes.create_string_buffer(waveform_file_path.encode(self._encoding))  # case C020
        write_waveform_data_ctype = _visatype.ViBoolean(write_waveform_data)  # case S150
        error_code = self._library.niDigital_CreateSourceWaveformFromFileTDMS(vi_ctype, waveform_name_ctype, waveform_file_path_ctype, write_waveform_data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_source_waveform_parallel(self, pin_list, waveform_name, data_mapping):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        data_mapping_ctype = _visatype.ViInt32(data_mapping.value)  # case S130
        error_code = self._library.niDigital_CreateSourceWaveformParallel(vi_ctype, pin_list_ctype, waveform_name_ctype, data_mapping_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_source_waveform_serial(self, pin_list, waveform_name, data_mapping, sample_width, bit_order):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        data_mapping_ctype = _visatype.ViInt32(data_mapping.value)  # case S130
        sample_width_ctype = _visatype.ViUInt32(sample_width)  # case S150
        bit_order_ctype = _visatype.ViInt32(bit_order.value)  # case S130
        error_code = self._library.niDigital_CreateSourceWaveformSerial(vi_ctype, pin_list_ctype, waveform_name_ctype, data_mapping_ctype, sample_width_ctype, bit_order_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_time_set(self, name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        name_ctype = ctypes.create_string_buffer(name.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_CreateTimeSet(vi_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def delete_all_time_sets(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_DeleteAllTimeSets(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable_sites(self, site_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C010
        error_code = self._library.niDigital_DisableSites(vi_ctype, site_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def enable_match_fail_combination(self, sessions, sync_session):  # noqa: N802
        session_count_ctype = _visatype.ViUInt32(0 if sessions is None else len(sessions))  # case S160
        sessions_ctype = _get_ctypes_pointer_for_buffer(value=sessions, library_type=_visatype.ViSession)  # case B550
        sync_session_ctype = _visatype.ViSession(sync_session)  # case S110
        error_code = self._library.niDigital_EnableMatchFailCombination(session_count_ctype, sessions_ctype, sync_session_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def enable_sites(self, site_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C010
        error_code = self._library.niDigital_EnableSites(vi_ctype, site_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def fetch_capture_waveform(self, site_list, waveform_name, samples_to_read, timeout):
        # This is slightly modified codegen from the function
        # We cannot use codegen without major modifications to the code generator
        # This function uses two 'ivi-dance' parameters and then multiplies them together - see
        # the (modified) line below
        # Also, we want to return the two sizes that normally wouldn't be returned
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        samples_to_read_ctype = _visatype.ViInt32(samples_to_read)  # case S150
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        data_buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        data_ctype = None  # case B610
        actual_num_waveforms_ctype = _visatype.ViInt32()  # case S220
        actual_samples_per_waveform_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_FetchCaptureWaveformU32(vi_ctype, site_list_ctype, waveform_name_ctype, samples_to_read_ctype, timeout_ctype, data_buffer_size_ctype, data_ctype, None if actual_num_waveforms_ctype is None else (ctypes.pointer(actual_num_waveforms_ctype)), None if actual_samples_per_waveform_ctype is None else (ctypes.pointer(actual_samples_per_waveform_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        data_buffer_size_ctype = _visatype.ViInt32(actual_num_waveforms_ctype.value * actual_samples_per_waveform_ctype.value)  # case S200 (modified)
        data_size = actual_num_waveforms_ctype.value * actual_samples_per_waveform_ctype.value  # case B620 (modified)
        data_array = array.array("L", [0]) * data_size  # case B620
        data_ctype = _get_ctypes_pointer_for_buffer(value=data_array, library_type=_visatype.ViUInt32)  # case B620
        error_code = self._library.niDigital_FetchCaptureWaveformU32(vi_ctype, site_list_ctype, waveform_name_ctype, samples_to_read_ctype, timeout_ctype, data_buffer_size_ctype, data_ctype, None if actual_num_waveforms_ctype is None else (ctypes.pointer(actual_num_waveforms_ctype)), None if actual_samples_per_waveform_ctype is None else (ctypes.pointer(actual_samples_per_waveform_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return data_array, actual_num_waveforms_ctype.value, actual_samples_per_waveform_ctype.value  # (modified)

    def fetch_history_ram_cycle_information(self, site, sample_index):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_ctype = ctypes.create_string_buffer(site.encode(self._encoding))  # case C010
        sample_index_ctype = _visatype.ViInt64(sample_index)  # case S150
        pattern_index_ctype = _visatype.ViInt32()  # case S220
        time_set_index_ctype = _visatype.ViInt32()  # case S220
        vector_number_ctype = _visatype.ViInt64()  # case S220
        cycle_number_ctype = _visatype.ViInt64()  # case S220
        num_dut_cycles_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_FetchHistoryRAMCycleInformation(vi_ctype, site_ctype, sample_index_ctype, None if pattern_index_ctype is None else (ctypes.pointer(pattern_index_ctype)), None if time_set_index_ctype is None else (ctypes.pointer(time_set_index_ctype)), None if vector_number_ctype is None else (ctypes.pointer(vector_number_ctype)), None if cycle_number_ctype is None else (ctypes.pointer(cycle_number_ctype)), None if num_dut_cycles_ctype is None else (ctypes.pointer(num_dut_cycles_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(pattern_index_ctype.value), int(time_set_index_ctype.value), int(vector_number_ctype.value), int(cycle_number_ctype.value), int(num_dut_cycles_ctype.value)

    def fetch_history_ram_cycle_pin_data(self, site, pin_list, sample_index, dut_cycle_index):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_ctype = ctypes.create_string_buffer(site.encode(self._encoding))  # case C010
        pin_list_ctype = ctypes.create_string_buffer(pin_list.encode(self._encoding))  # case C020
        sample_index_ctype = _visatype.ViInt64(sample_index)  # case S150
        dut_cycle_index_ctype = _visatype.ViInt32(dut_cycle_index)  # case S150
        pin_data_buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        expected_pin_states_ctype = None  # case B610
        actual_pin_states_ctype = None  # case B610
        per_pin_pass_fail_ctype = None  # case B610
        actual_num_pin_data_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_FetchHistoryRAMCyclePinData(vi_ctype, site_ctype, pin_list_ctype, sample_index_ctype, dut_cycle_index_ctype, pin_data_buffer_size_ctype, expected_pin_states_ctype, actual_pin_states_ctype, per_pin_pass_fail_ctype, None if actual_num_pin_data_ctype is None else (ctypes.pointer(actual_num_pin_data_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        pin_data_buffer_size_ctype = _visatype.ViInt32(actual_num_pin_data_ctype.value)  # case S200
        expected_pin_states_size = actual_num_pin_data_ctype.value  # case B620
        expected_pin_states_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViUInt8, size=expected_pin_states_size)  # case B620
        actual_pin_states_size = actual_num_pin_data_ctype.value  # case B620
        actual_pin_states_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViUInt8, size=actual_pin_states_size)  # case B620
        per_pin_pass_fail_size = actual_num_pin_data_ctype.value  # case B620
        per_pin_pass_fail_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViBoolean, size=per_pin_pass_fail_size)  # case B620
        error_code = self._library.niDigital_FetchHistoryRAMCyclePinData(vi_ctype, site_ctype, pin_list_ctype, sample_index_ctype, dut_cycle_index_ctype, pin_data_buffer_size_ctype, expected_pin_states_ctype, actual_pin_states_ctype, per_pin_pass_fail_ctype, None if actual_num_pin_data_ctype is None else (ctypes.pointer(actual_num_pin_data_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [enums.PinState(expected_pin_states_ctype[i]) for i in range(pin_data_buffer_size_ctype.value)], [enums.PinState(actual_pin_states_ctype[i]) for i in range(pin_data_buffer_size_ctype.value)], [bool(per_pin_pass_fail_ctype[i]) for i in range(pin_data_buffer_size_ctype.value)]

    def fetch_history_ram_scan_cycle_number(self, site, sample_index):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_ctype = ctypes.create_string_buffer(site.encode(self._encoding))  # case C010
        sample_index_ctype = _visatype.ViInt64(sample_index)  # case S150
        scan_cycle_number_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niDigital_FetchHistoryRAMScanCycleNumber(vi_ctype, site_ctype, sample_index_ctype, None if scan_cycle_number_ctype is None else (ctypes.pointer(scan_cycle_number_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(scan_cycle_number_ctype.value)

    def frequency_counter_measure_frequency(self, channel_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        frequencies_buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        frequencies_ctype = None  # case B610
        actual_num_frequencies_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_FrequencyCounter_MeasureFrequency(vi_ctype, channel_list_ctype, frequencies_buffer_size_ctype, frequencies_ctype, None if actual_num_frequencies_ctype is None else (ctypes.pointer(actual_num_frequencies_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        frequencies_buffer_size_ctype = _visatype.ViInt32(actual_num_frequencies_ctype.value)  # case S200
        frequencies_size = actual_num_frequencies_ctype.value  # case B620
        frequencies_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=frequencies_size)  # case B620
        error_code = self._library.niDigital_FrequencyCounter_MeasureFrequency(vi_ctype, channel_list_ctype, frequencies_buffer_size_ctype, frequencies_ctype, None if actual_num_frequencies_ctype is None else (ctypes.pointer(actual_num_frequencies_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(frequencies_ctype[i]) for i in range(frequencies_buffer_size_ctype.value)]

    def get_attribute_vi_boolean(self, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDigital_GetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(value_ctype.value)

    def get_attribute_vi_int32(self, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_GetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def get_attribute_vi_int64(self, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niDigital_GetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def get_attribute_vi_real64(self, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDigital_GetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(value_ctype.value)

    def get_attribute_vi_string(self, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        value_ctype = None  # case C050
        error_code = self._library.niDigital_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_ctype, buffer_size_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        value_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDigital_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_ctype, buffer_size_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return value_ctype.value.decode(self._encoding)

    def get_channel_names(self, indices):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        indices_ctype = ctypes.create_string_buffer(indices.encode(self._encoding))  # case C020
        name_buffer_size_ctype = _visatype.ViInt32()  # case S170
        names_ctype = None  # case C050
        error_code = self._library.niDigital_GetChannelNameFromString(vi_ctype, indices_ctype, name_buffer_size_ctype, names_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        name_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        names_ctype = (_visatype.ViChar * name_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDigital_GetChannelNameFromString(vi_ctype, indices_ctype, name_buffer_size_ctype, names_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return names_ctype.value.decode(self._encoding)

    def get_error(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus()  # case S220
        error_description_buffer_size_ctype = _visatype.ViInt32()  # case S170
        error_description_ctype = None  # case C050
        error_code = self._library.niDigital_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        error_description_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        error_description_ctype = (_visatype.ViChar * error_description_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDigital_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), error_description_ctype.value.decode(self._encoding)

    def get_fail_count(self, channel_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        failure_count_ctype = None  # case B610
        actual_num_read_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_GetFailCount(vi_ctype, channel_list_ctype, buffer_size_ctype, failure_count_ctype, None if actual_num_read_ctype is None else (ctypes.pointer(actual_num_read_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(actual_num_read_ctype.value)  # case S200
        failure_count_size = actual_num_read_ctype.value  # case B620
        failure_count_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt64, size=failure_count_size)  # case B620
        error_code = self._library.niDigital_GetFailCount(vi_ctype, channel_list_ctype, buffer_size_ctype, failure_count_ctype, None if actual_num_read_ctype is None else (ctypes.pointer(actual_num_read_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [int(failure_count_ctype[i]) for i in range(buffer_size_ctype.value)]

    def get_history_ram_sample_count(self, site):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_ctype = ctypes.create_string_buffer(site.encode(self._encoding))  # case C010
        sample_count_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niDigital_GetHistoryRAMSampleCount(vi_ctype, site_ctype, None if sample_count_ctype is None else (ctypes.pointer(sample_count_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(sample_count_ctype.value)

    def get_pattern_name(self, pattern_index):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pattern_index_ctype = _visatype.ViInt32(pattern_index)  # case S150
        name_buffer_size_ctype = _visatype.ViInt32()  # case S170
        name_ctype = None  # case C050
        error_code = self._library.niDigital_GetPatternName(vi_ctype, pattern_index_ctype, name_buffer_size_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        name_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        name_ctype = (_visatype.ViChar * name_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDigital_GetPatternName(vi_ctype, pattern_index_ctype, name_buffer_size_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return name_ctype.value.decode(self._encoding)

    def get_pattern_pin_names(self, start_label):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        start_label_ctype = ctypes.create_string_buffer(start_label.encode(self._encoding))  # case C020
        pin_list_buffer_size_ctype = _visatype.ViInt32()  # case S170
        pin_list_ctype = None  # case C050
        error_code = self._library.niDigital_GetPatternPinList(vi_ctype, start_label_ctype, pin_list_buffer_size_ctype, pin_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        pin_list_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        pin_list_ctype = (_visatype.ViChar * pin_list_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDigital_GetPatternPinList(vi_ctype, start_label_ctype, pin_list_buffer_size_ctype, pin_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return pin_list_ctype.value.decode(self._encoding)

    def get_pin_name(self, pin_index):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_index_ctype = _visatype.ViInt32(pin_index)  # case S150
        name_buffer_size_ctype = _visatype.ViInt32()  # case S170
        name_ctype = None  # case C050
        error_code = self._library.niDigital_GetPinName(vi_ctype, pin_index_ctype, name_buffer_size_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        name_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        name_ctype = (_visatype.ViChar * name_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDigital_GetPinName(vi_ctype, pin_index_ctype, name_buffer_size_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return name_ctype.value.decode(self._encoding)

    def get_pin_results_pin_information(self, channel_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        pin_indexes_ctype = None  # case B610
        site_numbers_ctype = None  # case B610
        channel_indexes_ctype = None  # case B610
        actual_num_values_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_GetPinResultsPinInformation(vi_ctype, channel_list_ctype, buffer_size_ctype, pin_indexes_ctype, site_numbers_ctype, channel_indexes_ctype, None if actual_num_values_ctype is None else (ctypes.pointer(actual_num_values_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(actual_num_values_ctype.value)  # case S200
        pin_indexes_size = actual_num_values_ctype.value  # case B620
        pin_indexes_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=pin_indexes_size)  # case B620
        site_numbers_size = actual_num_values_ctype.value  # case B620
        site_numbers_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=site_numbers_size)  # case B620
        channel_indexes_size = actual_num_values_ctype.value  # case B620
        channel_indexes_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=channel_indexes_size)  # case B620
        error_code = self._library.niDigital_GetPinResultsPinInformation(vi_ctype, channel_list_ctype, buffer_size_ctype, pin_indexes_ctype, site_numbers_ctype, channel_indexes_ctype, None if actual_num_values_ctype is None else (ctypes.pointer(actual_num_values_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [int(pin_indexes_ctype[i]) for i in range(buffer_size_ctype.value)], [int(site_numbers_ctype[i]) for i in range(buffer_size_ctype.value)], [int(channel_indexes_ctype[i]) for i in range(buffer_size_ctype.value)]

    def get_site_pass_fail(self, site_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C010
        pass_fail_buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        pass_fail_ctype = None  # case B610
        actual_num_sites_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_GetSitePassFail(vi_ctype, site_list_ctype, pass_fail_buffer_size_ctype, pass_fail_ctype, None if actual_num_sites_ctype is None else (ctypes.pointer(actual_num_sites_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        pass_fail_buffer_size_ctype = _visatype.ViInt32(actual_num_sites_ctype.value)  # case S200
        pass_fail_size = actual_num_sites_ctype.value  # case B620
        pass_fail_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViBoolean, size=pass_fail_size)  # case B620
        error_code = self._library.niDigital_GetSitePassFail(vi_ctype, site_list_ctype, pass_fail_buffer_size_ctype, pass_fail_ctype, None if actual_num_sites_ctype is None else (ctypes.pointer(actual_num_sites_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [bool(pass_fail_ctype[i]) for i in range(pass_fail_buffer_size_ctype.value)]

    def get_site_results_site_numbers(self, site_list, site_result_type):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C010
        site_result_type_ctype = _visatype.ViInt32(site_result_type.value)  # case S130
        site_numbers_buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        site_numbers_ctype = None  # case B610
        actual_num_site_numbers_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_GetSiteResultsSiteNumbers(vi_ctype, site_list_ctype, site_result_type_ctype, site_numbers_buffer_size_ctype, site_numbers_ctype, None if actual_num_site_numbers_ctype is None else (ctypes.pointer(actual_num_site_numbers_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        site_numbers_buffer_size_ctype = _visatype.ViInt32(actual_num_site_numbers_ctype.value)  # case S200
        site_numbers_size = actual_num_site_numbers_ctype.value  # case B620
        site_numbers_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=site_numbers_size)  # case B620
        error_code = self._library.niDigital_GetSiteResultsSiteNumbers(vi_ctype, site_list_ctype, site_result_type_ctype, site_numbers_buffer_size_ctype, site_numbers_ctype, None if actual_num_site_numbers_ctype is None else (ctypes.pointer(actual_num_site_numbers_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [int(site_numbers_ctype[i]) for i in range(site_numbers_buffer_size_ctype.value)]

    def get_time_set_drive_format(self, pin, time_set_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_ctype = ctypes.create_string_buffer(pin.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        format_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_GetTimeSetDriveFormat(vi_ctype, pin_ctype, time_set_name_ctype, None if format_ctype is None else (ctypes.pointer(format_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return enums.DriveFormat(format_ctype.value)

    def get_time_set_edge(self, pin, time_set_name, edge):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_ctype = ctypes.create_string_buffer(pin.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        edge_ctype = _visatype.ViInt32(edge.value)  # case S130
        time_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDigital_GetTimeSetEdge(vi_ctype, pin_ctype, time_set_name_ctype, edge_ctype, None if time_ctype is None else (ctypes.pointer(time_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(time_ctype.value)

    def get_time_set_edge_multiplier(self, pin, time_set_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        pin_ctype = ctypes.create_string_buffer(pin.encode(self._encoding))  # case C010
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        edge_multiplier_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_GetTimeSetEdgeMultiplier(vi_ctype, pin_ctype, time_set_name_ctype, None if edge_multiplier_ctype is None else (ctypes.pointer(edge_multiplier_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(edge_multiplier_ctype.value)

    def get_time_set_name(self, time_set_index):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        time_set_index_ctype = _visatype.ViInt32(time_set_index)  # case S150
        name_buffer_size_ctype = _visatype.ViInt32()  # case S170
        name_ctype = None  # case C050
        error_code = self._library.niDigital_GetTimeSetName(vi_ctype, time_set_index_ctype, name_buffer_size_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        name_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        name_ctype = (_visatype.ViChar * name_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDigital_GetTimeSetName(vi_ctype, time_set_index_ctype, name_buffer_size_ctype, name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return name_ctype.value.decode(self._encoding)

    def get_time_set_period(self, time_set_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        time_set_name_ctype = ctypes.create_string_buffer(time_set_name.encode(self._encoding))  # case C020
        period_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDigital_GetTimeSetPeriod(vi_ctype, time_set_name_ctype, None if period_ctype is None else (ctypes.pointer(period_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(period_ctype.value)

    def init_with_options(self, resource_name, id_query, reset_device, option_string):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        id_query_ctype = _visatype.ViBoolean(id_query)  # case S150
        reset_device_ctype = _visatype.ViBoolean(reset_device)  # case S150
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case C020
        new_vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niDigital_InitWithOptions(resource_name_ctype, id_query_ctype, reset_device_ctype, option_string_ctype, None if new_vi_ctype is None else (ctypes.pointer(new_vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        self._close_on_exit = True
        return int(new_vi_ctype.value)

    def initiate(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_Initiate(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def is_done(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        done_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDigital_IsDone(vi_ctype, None if done_ctype is None else (ctypes.pointer(done_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(done_ctype.value)

    def is_site_enabled(self, site):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_ctype = ctypes.create_string_buffer(site.encode(self._encoding))  # case C010
        enable_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDigital_IsSiteEnabled(vi_ctype, site_ctype, None if enable_ctype is None else (ctypes.pointer(enable_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(enable_ctype.value)

    def load_levels(self, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_LoadLevels(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def load_pattern(self, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_LoadPattern(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def load_pin_map(self, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_LoadPinMap(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def load_specifications(self, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_LoadSpecifications(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def load_timing(self, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_LoadTiming(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def lock(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_LockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def ppmu_measure(self, channel_list, measurement_type):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        measurement_type_ctype = _visatype.ViInt32(measurement_type.value)  # case S130
        buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        measurements_ctype = None  # case B610
        actual_num_read_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_PPMU_Measure(vi_ctype, channel_list_ctype, measurement_type_ctype, buffer_size_ctype, measurements_ctype, None if actual_num_read_ctype is None else (ctypes.pointer(actual_num_read_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(actual_num_read_ctype.value)  # case S200
        measurements_size = actual_num_read_ctype.value  # case B620
        measurements_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=measurements_size)  # case B620
        error_code = self._library.niDigital_PPMU_Measure(vi_ctype, channel_list_ctype, measurement_type_ctype, buffer_size_ctype, measurements_ctype, None if actual_num_read_ctype is None else (ctypes.pointer(actual_num_read_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(measurements_ctype[i]) for i in range(buffer_size_ctype.value)]

    def ppmu_source(self, channel_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        error_code = self._library.niDigital_PPMU_Source(vi_ctype, channel_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def read_sequencer_flag(self, flag):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        flag_ctype = ctypes.create_string_buffer(flag.value.encode(self._encoding))  # case C030
        value_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDigital_ReadSequencerFlag(vi_ctype, flag_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(value_ctype.value)

    def read_sequencer_register(self, reg):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        reg_ctype = ctypes.create_string_buffer(reg.value.encode(self._encoding))  # case C030
        value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_ReadSequencerRegister(vi_ctype, reg_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def read_static(self, channel_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        data_ctype = None  # case B610
        actual_num_read_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_ReadStatic(vi_ctype, channel_list_ctype, buffer_size_ctype, data_ctype, None if actual_num_read_ctype is None else (ctypes.pointer(actual_num_read_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(actual_num_read_ctype.value)  # case S200
        data_size = actual_num_read_ctype.value  # case B620
        data_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViUInt8, size=data_size)  # case B620
        error_code = self._library.niDigital_ReadStatic(vi_ctype, channel_list_ctype, buffer_size_ctype, data_ctype, None if actual_num_read_ctype is None else (ctypes.pointer(actual_num_read_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [enums.PinState(data_ctype[i]) for i in range(buffer_size_ctype.value)]

    def reset_device(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_ResetDevice(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_calibrate(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_SelfCalibrate(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def send_software_edge_trigger(self, trigger, trigger_identifier):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_ctype = _visatype.ViInt32(trigger.value)  # case S130
        trigger_identifier_ctype = ctypes.create_string_buffer(trigger_identifier.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_SendSoftwareEdgeTrigger(vi_ctype, trigger_ctype, trigger_identifier_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_boolean(self, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViBoolean(value)  # case S150
        error_code = self._library.niDigital_SetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_int32(self, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViInt32(value)  # case S150
        error_code = self._library.niDigital_SetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_int64(self, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViInt64(value)  # case S150
        error_code = self._library.niDigital_SetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_real64(self, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViReal64(value)  # case S150
        error_code = self._library.niDigital_SetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_string(self, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = ctypes.create_string_buffer(value.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_SetAttributeViString(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_runtime_environment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        environment_ctype = ctypes.create_string_buffer(environment.encode(self._encoding))  # case C020
        environment_version_ctype = ctypes.create_string_buffer(environment_version.encode(self._encoding))  # case C020
        reserved1_ctype = ctypes.create_string_buffer(reserved1.encode(self._encoding))  # case C020
        reserved2_ctype = ctypes.create_string_buffer(reserved2.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_SetRuntimeEnvironment(environment_ctype, environment_version_ctype, reserved1_ctype, reserved2_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def tdr(self, channel_list, apply_offsets):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        apply_offsets_ctype = _visatype.ViBoolean(apply_offsets)  # case S150
        offsets_buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        offsets_ctype = None  # case B610
        actual_num_offsets_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDigital_TDR(vi_ctype, channel_list_ctype, apply_offsets_ctype, offsets_buffer_size_ctype, offsets_ctype, None if actual_num_offsets_ctype is None else (ctypes.pointer(actual_num_offsets_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        offsets_buffer_size_ctype = _visatype.ViInt32(actual_num_offsets_ctype.value)  # case S200
        offsets_size = actual_num_offsets_ctype.value  # case B620
        offsets_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=offsets_size)  # case B620
        error_code = self._library.niDigital_TDR(vi_ctype, channel_list_ctype, apply_offsets_ctype, offsets_buffer_size_ctype, offsets_ctype, None if actual_num_offsets_ctype is None else (ctypes.pointer(actual_num_offsets_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(offsets_ctype[i]) for i in range(offsets_buffer_size_ctype.value)]

    def unload_all_patterns(self, unload_keep_alive_pattern):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        unload_keep_alive_pattern_ctype = _visatype.ViBoolean(unload_keep_alive_pattern)  # case S150
        error_code = self._library.niDigital_UnloadAllPatterns(vi_ctype, unload_keep_alive_pattern_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unload_specifications(self, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_UnloadSpecifications(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_UnlockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def wait_until_done(self, timeout):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        error_code = self._library.niDigital_WaitUntilDone(vi_ctype, timeout_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_sequencer_flag(self, flag, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        flag_ctype = ctypes.create_string_buffer(flag.value.encode(self._encoding))  # case C030
        value_ctype = _visatype.ViBoolean(value)  # case S150
        error_code = self._library.niDigital_WriteSequencerFlag(vi_ctype, flag_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_sequencer_register(self, reg, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        reg_ctype = ctypes.create_string_buffer(reg.value.encode(self._encoding))  # case C030
        value_ctype = _visatype.ViInt32(value)  # case S150
        error_code = self._library.niDigital_WriteSequencerRegister(vi_ctype, reg_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_source_waveform_broadcast(self, waveform_name, waveform_data):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        waveform_size_ctype = _visatype.ViInt32(0 if waveform_data is None else len(waveform_data))  # case S160
        waveform_data_ctype = _get_ctypes_pointer_for_buffer(value=waveform_data, library_type=_visatype.ViUInt32)  # case B550
        error_code = self._library.niDigital_WriteSourceWaveformBroadcastU32(vi_ctype, waveform_name_ctype, waveform_size_ctype, waveform_data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_source_waveform_data_from_file_tdms(self, waveform_name, waveform_file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        waveform_file_path_ctype = ctypes.create_string_buffer(waveform_file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDigital_WriteSourceWaveformDataFromFileTDMS(vi_ctype, waveform_name_ctype, waveform_file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_source_waveform_site_unique_u32(self, site_list, waveform_name, num_waveforms, samples_per_waveform, waveform_data):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        site_list_ctype = ctypes.create_string_buffer(site_list.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        num_waveforms_ctype = _visatype.ViInt32(num_waveforms)  # case S150
        samples_per_waveform_ctype = _visatype.ViInt32(samples_per_waveform)  # case S150
        waveform_data_array = _convert_to_array(value=waveform_data, array_type="L")  # case B550
        waveform_data_ctype = _get_ctypes_pointer_for_buffer(value=waveform_data_array, library_type=_visatype.ViUInt32)  # case B550
        error_code = self._library.niDigital_WriteSourceWaveformSiteUniqueU32(vi_ctype, site_list_ctype, waveform_name_ctype, num_waveforms_ctype, samples_per_waveform_ctype, waveform_data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_static(self, channel_list, state):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        state_ctype = _visatype.ViUInt8(state.value)  # case S130
        error_code = self._library.niDigital_WriteStatic(vi_ctype, channel_list_ctype, state_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def close(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def error_message(self, error_code):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niDigital_error_message(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)

    def reset(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDigital_reset(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_test(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        test_result_ctype = _visatype.ViInt16()  # case S220
        test_message_ctype = (_visatype.ViChar * 2048)()  # case C070
        error_code = self._library.niDigital_self_test(vi_ctype, None if test_result_ctype is None else (ctypes.pointer(test_result_ctype)), test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(test_result_ctype.value), test_message_ctype.value.decode(self._encoding)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidigital/nidigital/_library_singleton.py sha256=777c9fe1d5c91ce8e6e4d940e92c8a1a53183fbc5589c422ce5d2c18439c1425 bytes=1711 -->
## FILE: generated/nidigital/nidigital/_library_singleton.py

- repository: `ni/nimi-python`
- source_path: `generated/nidigital/nidigital/_library_singleton.py`
- sha256: `777c9fe1d5c91ce8e6e4d940e92c8a1a53183fbc5589c422ce5d2c18439c1425`
- bytes: 1711

````python
# -*- coding: utf-8 -*-
# This file was generated

import platform

import ctypes
import ctypes.util
import nidigital._library as _library
import nidigital.errors as errors
import threading


_instance = None
_instance_lock = threading.Lock()
_library_info = {'Linux': {'64bit': {'name': 'nidigital', 'type': 'cdll'}},
                 'Windows': {'32bit': {'name': 'niDigital_32.dll', 'type': 'windll'},
                             '64bit': {'name': 'niDigital_64.dll', 'type': 'cdll'}}}


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

    Returns the library.Library singleton for nidigital.
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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidigital/nidigital/_visatype.py sha256=ac436ae1613f5e807cd16d2df951c7a502f37996234e4d324c5412b3633e1c92 bytes=662 -->
## FILE: generated/nidigital/nidigital/_visatype.py

- repository: `ni/nimi-python`
- source_path: `generated/nidigital/nidigital/_visatype.py`
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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidigital/nidigital/enums.py sha256=31280f1c83b0e0eb5b1cae696649a73878c571d9bded4a14605c0b1869883a46 bytes=7810 -->
## FILE: generated/nidigital/nidigital/enums.py

- repository: `ni/nimi-python`
- source_path: `generated/nidigital/nidigital/enums.py`
- sha256: `31280f1c83b0e0eb5b1cae696649a73878c571d9bded4a14605c0b1869883a46`
- bytes: 7810

````python
# -*- coding: utf-8 -*-
# This file was generated

from enum import Enum


class BitOrder(Enum):
    MSB = 2500
    r'''
    The most significant bit is first. The first bit is in the 2^n place, where n is the number of bits.
    '''
    LSB = 2501
    r'''
    The least significant bit is first. The first bit is in the 2^0 place.
    '''


class DigitalEdge(Enum):
    RISING = 1800
    r'''
    Asserts the trigger when the signal transitions from low level to high level.
    '''
    FALLING = 1801
    r'''
    Asserts the trigger when the signal transitions from high level to low level.
    '''


class DriveFormat(Enum):
    NR = 1500
    r'''
    Drive format remains at logic level after each bit.
    '''
    RL = 1501
    r'''
    Drive format returns to a logic level low after each bit.
    '''
    RH = 1502
    r'''
    Drive format returns to a logic level high after each bit.
    '''
    SBC = 1503
    r'''
    Drive format returns to the complement logic level of the bit after each bit.
    '''


class FrequencyMeasurementMode(Enum):
    BANKED = 3700
    r'''
    Frequency measurements are made serially for groups of channels associated with a single frequency counter for each group.

    Maximum frequency measured: 200 MHz.
    '''
    PARALLEL = 3701
    r'''
    Frequency measurements are made by multiple frequency counters in parallel.

    Maximum frequency measured: 100 MHz.
    '''


class HistoryRAMCyclesToAcquire(Enum):
    FAILED = 2303
    r'''
    Acquires failed cycles.
    '''
    ALL = 2304
    r'''
    Acquires all cycles.
    '''


class HistoryRAMTriggerType(Enum):
    FIRST_FAILURE = 2200
    r'''
    First Failure History RAM trigger
    '''
    CYCLE_NUMBER = 2201
    r'''
    Cycle Number History RAM trigger.
    '''
    PATTERN_LABEL = 2202
    r'''
    Pattern Label History RAM trigger
    '''


class PPMUApertureTimeUnits(Enum):
    SECONDS = 2100
    r'''
    Unit in seconds.
    '''


class PPMUCurrentLimitBehavior(Enum):
    REGULATE = 3100
    r'''
    Controls output current so that it does not exceed the current limit. Power continues to generate even if the current limit is reached.
    '''


class PPMUMeasurementType(Enum):
    CURRENT = 2400
    r'''
    The PPMU measures current.
    '''
    VOLTAGE = 2401
    r'''
    The PPMU measures voltage.
    '''


class PPMUOutputFunction(Enum):
    VOLTAGE = 1300
    r'''
    The PPMU forces voltage to the DUT.
    '''
    CURRENT = 1301
    r'''
    The PPMU forces current to the DUT.
    '''


class PinState(Enum):
    ZERO = 0
    r'''
    A digital state of 0.
    '''
    ONE = 1
    r'''
    A digital state of 1.
    '''
    L = 3
    r'''
    A digital state of L (low).
    '''
    H = 4
    r'''
    A digital state of H (high).
    '''
    X = 5
    r'''
    A digital state of X (non-drive state).
    '''
    M = 6
    r'''
    A digital state of M (midband).
    '''
    V = 7
    r'''
    A digital state of V (compare high or low, not midband; store results from capture functionality if configured).
    '''
    D = 8
    r'''
    A digital state of D (drive data from source functionality if configured).
    '''
    E = 9
    r'''
    A digital state of E (compare data from source functionality if configured).
    '''
    NOT_A_PIN_STATE = 254
    r'''
    Not a pin state is used for non-existent DUT cycles.
    '''
    PIN_STATE_NOT_ACQUIRED = 255
    r'''
    Pin state could not be acquired because none of the pins mapped to the instrument in a multi-instrument session had any failures.
    '''

    def __str__(self):
        return {
            'ZERO': '0',
            'ONE': '1',
            'NOT_A_PIN_STATE': 'Not a Pin State',
            'PIN_STATE_NOT_ACQUIRED': 'Pin State Not Acquired',
        }.get(self.name, self.name)


class SelectedFunction(Enum):
    DIGITAL = 1100
    r'''
    The pattern sequencer controls the specified pin(s). If a pattern is currently bursting, the pin immediately switches to bursting the pattern. This option disconnects the PPMU.
    '''
    PPMU = 1101
    r'''
    The PPMU controls the specified pin(s) and connects the PPMU. The pin driver is in a non-drive state, and the active load is disabled. The PPMU does not start sourcing or measuring until Source or Measure(PpmuMeasurementType) is called.
    '''
    OFF = 1102
    r'''
    Puts the digital driver in a non-drive state, disables the active load, disconnects the PPMU, and closes the I/O switch connecting the instrument channel.
    '''
    DISCONNECT = 1103
    r'''
    The I/O switch connecting the instrument channel is open to the I/O connector. If the PPMU is sourcing, it is stopped prior to opening the I/O switch.
    '''
    RIO = 1104
    r'''
    Yields control of the specified pin(s) to LabVIEW FPGA.
    '''


class SequencerFlag(Enum):
    FLAG0 = 'seqflag0'
    FLAG1 = 'seqflag1'
    FLAG2 = 'seqflag2'
    FLAG3 = 'seqflag3'


class SequencerRegister(Enum):
    REGISTER0 = 'reg0'
    REGISTER1 = 'reg1'
    REGISTER2 = 'reg2'
    REGISTER3 = 'reg3'
    REGISTER4 = 'reg4'
    REGISTER5 = 'reg5'
    REGISTER6 = 'reg6'
    REGISTER7 = 'reg7'
    REGISTER8 = 'reg8'
    REGISTER9 = 'reg9'
    REGISTER10 = 'reg10'
    REGISTER11 = 'reg11'
    REGISTER12 = 'reg12'
    REGISTER13 = 'reg13'
    REGISTER14 = 'reg14'
    REGISTER15 = 'reg15'


class _SiteResultType(Enum):
    PASS_FAIL = 3300
    r'''
    Pass/fail site result.
    '''
    CAPTURE_WAVEFORM = 3301
    r'''
    Capture waveform site result.
    '''


class SoftwareTrigger(Enum):
    START = 2000
    r'''
    Overrides the start trigger.
    '''
    CONDITIONAL_JUMP = 2001
    r'''
    Specifies to route a conditional jump trigger.
    '''


class SourceDataMapping(Enum):
    BROADCAST = 2600
    r'''
    Broadcasts the waveform you specify to all sites.
    '''
    SITE_UNIQUE = 2601
    r'''
    Sources unique waveform data to each site.
    '''


class TDREndpointTermination(Enum):
    OPEN = 3600
    r'''
    TDR channels are connected to an open circuit.
    '''
    SHORT_TO_GROUND = 3601
    r'''
    TDR channels are connected to a short to ground.
    '''


class TerminationMode(Enum):
    ACTIVE_LOAD = 1200
    r'''
    The active load provides a constant current to a commutating voltage (Vcom).
    '''
    VTERM = 1201
    r'''
    The pin driver drives Vterm.
    '''
    HIGH_Z = 1202
    r'''
    The pin driver is in a non-drive state (in a high-impedance state) and the active load is disabled.
    '''


class TimeSetEdgeType(Enum):
    DRIVE_ON = 2800
    r'''
    Specifies the drive on edge of the time set.
    '''
    DRIVE_DATA = 2801
    r'''
    Specifies the drive data edge of the time set.
    '''
    DRIVE_RETURN = 2802
    r'''
    Specifies the drive return edge of the time set.
    '''
    DRIVE_OFF = 2803
    r'''
    Specifies the drive off edge of the time set.
    '''
    COMPARE_STROBE = 2804
    r'''
    Specifies the compare strobe of the time set.
    '''
    DRIVE_DATA2 = 2805
    r'''
    Specifies the drive data 2 edge of the time set.
    '''
    DRIVE_RETURN2 = 2806
    r'''
    Specifies the drive return 2 edge of the time set.
    '''
    COMPARE_STROBE2 = 2807
    r'''
    Specifies the compare strobe 2 of the time set.
    '''


class TriggerType(Enum):
    NONE = 1700
    r'''
    Disables the start trigger.
    '''
    DIGITAL_EDGE = 1701
    r'''
    Digital edge trigger.
    '''
    SOFTWARE = 1702
    r'''
    Software start trigger.
    '''


class WriteStaticPinState(Enum):
    ZERO = 0
    r'''
    Specifies to drive low.
    '''
    ONE = 1
    r'''
    Specifies to drive high.
    '''
    X = 5
    r'''
    Specifies to not drive.
    '''

    def __str__(self):
        return {
            'ZERO': '0',
            'ONE': '1',
        }.get(self.name, self.name)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidigital/nidigital/errors.py sha256=ce3bb25b9b0683499a34b65e1c939975d721e367990e9de7ad0bb19540a22804 bytes=4502 -->
## FILE: generated/nidigital/nidigital/errors.py

- repository: `ni/nimi-python`
- source_path: `generated/nidigital/nidigital/errors.py`
- sha256: `ce3bb25b9b0683499a34b65e1c939975d721e367990e9de7ad0bb19540a22804`
- bytes: 4502

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
    '''Base error class for NI-Digital Pattern Driver'''

    def __init__(self, message):
        super(Error, self).__init__(message)


class DriverError(Error):
    '''An error originating from the NI-Digital Pattern Driver driver'''

    def __init__(self, code, description):
        assert _is_error(code), "Should not raise Error if code is not fatal."
        self.code = code
        self.description = description
        super(DriverError, self).__init__(str(self.code) + ": " + self.description)


class DriverWarning(Warning):
    '''A warning originating from the NI-Digital Pattern Driver driver'''

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
        super(DriverNotInstalledError, self).__init__('The NI-Digital Pattern Driver runtime could not be loaded. Make sure it is installed and its bitness matches that of your Python interpreter. Please visit http://www.ni.com/downloads/drivers/ to download and install it.')


class DriverTooOldError(Error):
    '''An error due to using this module with an older version of the NI-Digital Pattern Driver driver runtime.'''

    def __init__(self):
        super(DriverTooOldError, self).__init__('A function was not found in the NI-Digital Pattern Driver runtime. Please visit http://www.ni.com/downloads/drivers/ to download a newer version and install it.')


class DriverTooNewError(Error):
    '''An error due to the NI-Digital Pattern Driver driver runtime being too new for this module.'''

    def __init__(self):
        super(DriverTooNewError, self).__init__('The NI-Digital Pattern Driver runtime returned an unexpected value. This can occur if it is too new for the nidigital Python module. Upgrade the nidigital Python module.')


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

    Helper function for handling errors returned by nidigital.Library.
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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidigital/nidigital/grpc_session_options.py sha256=3ad9bb9d07fd0fcdaf29e94ff49c20dfdfa9cbbfd03ec92e2da53a671af6c431 bytes=3465 -->
## FILE: generated/nidigital/nidigital/grpc_session_options.py

- repository: `ni/nimi-python`
- source_path: `generated/nidigital/nidigital/grpc_session_options.py`
- sha256: `3ad9bb9d07fd0fcdaf29e94ff49c20dfdfa9cbbfd03ec92e2da53a671af6c431`
- bytes: 3465

````python
# -*- coding: utf-8 -*-
# This file was generated

from enum import IntEnum


# This constant specifies the gRPC package and service used by this API.
# Customers can pass this value to the MeasurementLink discovery service to resolve the server instance that provides this interface.
GRPC_SERVICE_INTERFACE_NAME = 'nidigitalpattern_grpc.NiDigital'

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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidigital/nidigital/history_ram_cycle_information.py sha256=03ca3bbe111135f4dda85bd70e50dae85821a13699a7998e72bc67f4724f61f2 bytes=2800 -->
## FILE: generated/nidigital/nidigital/history_ram_cycle_information.py

- repository: `ni/nimi-python`
- source_path: `generated/nidigital/nidigital/history_ram_cycle_information.py`
- sha256: `03ca3bbe111135f4dda85bd70e50dae85821a13699a7998e72bc67f4724f61f2`
- bytes: 2800

````python
class HistoryRAMCycleInformation:
    def __init__(self, pattern_name, time_set_name, vector_number, cycle_number, scan_cycle_number, expected_pin_states, actual_pin_states, per_pin_pass_fail):
        self.pattern_name = pattern_name
        self.time_set_name = time_set_name
        self.vector_number = vector_number
        self.cycle_number = cycle_number
        self.scan_cycle_number = scan_cycle_number
        self.expected_pin_states = expected_pin_states
        self.actual_pin_states = actual_pin_states
        self.per_pin_pass_fail = per_pin_pass_fail

    def __repr__(self):
        parameter_list = [
            f'pattern_name="{self.pattern_name}"',
            f'time_set_name="{self.time_set_name}"',
            f'vector_number={self.vector_number}',
            f'cycle_number={self.cycle_number}',
            f'scan_cycle_number={self.scan_cycle_number}',
            f'expected_pin_states={self._digital_states_representation(self.expected_pin_states)}',
            f'actual_pin_states={self._digital_states_representation(self.actual_pin_states)}',
            f'per_pin_pass_fail={self.per_pin_pass_fail}',
        ]

        return '{}.{}({})'.format(self.__class__.__module__, self.__class__.__qualname__, ', '.join(parameter_list))

    def __str__(self):
        # different format lines
        row_format_d = '{:<20}: {:,}\n'
        row_format_s = '{:<20}: {:}\n'

        string_representation = ''
        string_representation += row_format_s.format('Pattern Name', self.pattern_name)
        string_representation += row_format_s.format('Time Set Name', self.time_set_name)
        string_representation += row_format_d.format('Vector Number', self.vector_number)
        string_representation += row_format_d.format('Cycle Number', self.cycle_number)
        string_representation += row_format_d.format('Scan Cycle Number', self.scan_cycle_number)
        string_representation += row_format_s.format('Expected Pin States', self._digital_states_string(self.expected_pin_states))
        string_representation += row_format_s.format('Actual Pin States', self._digital_states_string(self.actual_pin_states))
        string_representation += row_format_s.format('Per Pin Pass Fail', self.per_pin_pass_fail)

        return string_representation

    @staticmethod
    def _digital_states_representation(states):
        states_representation = [[f'{i.__class__.__module__}.{i.__class__.__qualname__}.{i.name}' for i in j] for j in states]
        return '[{}]'.format(', '.join(['[{}]'.format(', '.join(i)) for i in states_representation]))

    @staticmethod
    def _digital_states_string(states):
        states_string = [[str(i) for i in j] for j in states]
        return '[{}]'.format(', '.join(['[{}]'.format(', '.join(i)) for i in states_string]))
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidigital/nidigital/nidevice_pb2.py sha256=9a935a95cbe830099345438b27f1460989b073de2e873f43cb394ac0df4ced54 bytes=2009 -->
## FILE: generated/nidigital/nidigital/nidevice_pb2.py

- repository: `ni/nimi-python`
- source_path: `generated/nidigital/nidigital/nidevice_pb2.py`
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

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidigital/nidigital/nidevice_pb2_grpc.py sha256=d686e804f171693117b7d030ec4023f205c70c234c8590f6557aa8702f65fe09 bytes=159 -->
## FILE: generated/nidigital/nidigital/nidevice_pb2_grpc.py

- repository: `ni/nimi-python`
- source_path: `generated/nidigital/nidigital/nidevice_pb2_grpc.py`
- sha256: `d686e804f171693117b7d030ec4023f205c70c234c8590f6557aa8702f65fe09`
- bytes: 159

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidigital/nidigital/nidigitalpattern_pb2.py sha256=f127a60b3883464fafd27a712539915b16899b1f34e5d9527a54c5be1ccfced5 bytes=112326 -->
## FILE: generated/nidigital/nidigital/nidigitalpattern_pb2.py

- repository: `ni/nimi-python`
- source_path: `generated/nidigital/nidigital/nidigitalpattern_pb2.py`
- sha256: `f127a60b3883464fafd27a712539915b16899b1f34e5d9527a54c5be1ccfced5`
- bytes: 112326

````python
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nidigitalpattern.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import session_pb2 as session__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16nidigitalpattern.proto\x12\x15nidigitalpattern_grpc\x1a\rsession.proto\"\xb1\x01\n\x0bInitRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x10\n\x08id_query\x18\x03 \x01(\x08\x12\x14\n\x0creset_device\x18\x04 \x01(\x08\x12M\n\x17initialization_behavior\x18\x05 \x01(\x0e\x32,.nidevice_grpc.SessionInitializationBehavior\"~\n\x0cInitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\"\n\x02vi\x18\x02 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x19\n\rerror_message\x18\x03 \x01(\tB\x02\x18\x01\x12\x1f\n\x17new_session_initialized\x18\x04 \x01(\x08\"\xd3\x01\n\x16InitWithOptionsRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x10\n\x08id_query\x18\x03 \x01(\x08\x12\x14\n\x0creset_device\x18\x04 \x01(\x08\x12\x15\n\roption_string\x18\x05 \x01(\t\x12M\n\x17initialization_behavior\x18\x06 \x01(\x0e\x32,.nidevice_grpc.SessionInitializationBehavior\"\x89\x01\n\x17InitWithOptionsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\"\n\x02vi\x18\x02 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x19\n\rerror_message\x18\x03 \x01(\tB\x02\x18\x01\x12\x1f\n\x17new_session_initialized\x18\x04 \x01(\x08\"2\n\x0c\x43loseRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\x1f\n\rCloseResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"2\n\x0cResetRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\x1f\n\rResetResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"8\n\x12ResetDeviceRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"%\n\x13ResetDeviceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"5\n\x0fSelfTestRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"M\n\x10SelfTestResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0btest_result\x18\x02 \x01(\x11\x12\x14\n\x0ctest_message\x18\x03 \x01(\t\"5\n\x0fGetErrorRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"Q\n\x10GetErrorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nerror_code\x18\x02 \x01(\x11\x12\x19\n\x11\x65rror_description\x18\x03 \x01(\t\"7\n\x11\x43learErrorRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"$\n\x12\x43learErrorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"M\n\x13\x45rrorMessageRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x12\n\nerror_code\x18\x02 \x01(\x11\"=\n\x14\x45rrorMessageResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t\":\n\x14SelfCalibrateRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\'\n\x15SelfCalibrateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x94\x01\n\x1aGetAttributeViInt32Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12<\n\tattribute\x18\x03 \x01(\x0e\x32).nidigitalpattern_grpc.NiDigitalAttribute\"<\n\x1bGetAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x11\"\x94\x01\n\x1aGetAttributeViInt64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12<\n\tattribute\x18\x03 \x01(\x0e\x32).nidigitalpattern_grpc.NiDigitalAttribute\"<\n\x1bGetAttributeViInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x03\"\x95\x01\n\x1bGetAttributeViReal64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12<\n\tattribute\x18\x03 \x01(\x0e\x32).nidigitalpattern_grpc.NiDigitalAttribute\"=\n\x1cGetAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01\"\x95\x01\n\x1bGetAttributeViStringRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12<\n\tattribute\x18\x03 \x01(\x0e\x32).nidigitalpattern_grpc.NiDigitalAttribute\"=\n\x1cGetAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t\"\x96\x01\n\x1cGetAttributeViSessionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_list\x18\x02 \x01(\t\x12<\n\tattribute\x18\x03 \x01(\x0e\x32).nidigitalpattern_grpc.NiDigitalAttribute\"V\n\x1dGetAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\x96\x01\n\x1cGetAttributeViBooleanRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12<\n\tattribute\x18\x03 \x01(\x0e\x32).nidigitalpattern_grpc.NiDigitalAttribute\">\n\x1dGetAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08\"\xfe\x01\n\x1aSetAttributeViInt32Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12<\n\tattribute\x18\x03 \x01(\x0e\x32).nidigitalpattern_grpc.NiDigitalAttribute\x12\x45\n\x05value\x18\x04 \x01(\x0e\x32\x34.nidigitalpattern_grpc.NiDigitalInt32AttributeValuesH\x00\x12\x13\n\tvalue_raw\x18\x05 \x01(\x11H\x00\x42\x0c\n\nvalue_enum\"-\n\x1bSetAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xa7\x01\n\x1aSetAttributeViInt64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12<\n\tattribute\x18\x03 \x01(\x0e\x32).nidigitalpattern_grpc.NiDigitalAttribute\x12\x11\n\tvalue_raw\x18\x04 \x01(\x03\"-\n\x1bSetAttributeViInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xa8\x01\n\x1bSetAttributeViReal64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12<\n\tattribute\x18\x03 \x01(\x0e\x32).nidigitalpattern_grpc.NiDigitalAttribute\x12\x11\n\tvalue_raw\x18\x04 \x01(\x01\".\n\x1cSetAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xa8\x01\n\x1bSetAttributeViStringRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12<\n\tattribute\x18\x03 \x01(\x0e\x32).nidigitalpattern_grpc.NiDigitalAttribute\x12\x11\n\tvalue_raw\x18\x04 \x01(\t\".\n\x1cSetAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xbd\x01\n\x1cSetAttributeViSessionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_list\x18\x02 \x01(\t\x12<\n\tattribute\x18\x03 \x01(\x0e\x32).nidigitalpattern_grpc.NiDigitalAttribute\x12%\n\x05value\x18\x04 \x01(\x0b\x32\x16.nidevice_grpc.Session\"/\n\x1dSetAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xa5\x01\n\x1cSetAttributeViBooleanRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12<\n\tattribute\x18\x03 \x01(\x0e\x32).nidigitalpattern_grpc.NiDigitalAttribute\x12\r\n\x05value\x18\x04 \x01(\x08\"/\n\x1dSetAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x92\x01\n\x15ResetAttributeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12?\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32).nidigitalpattern_grpc.NiDigitalAttribute\"(\n\x16ResetAttributeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"J\n\x11LoadPinMapRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tfile_path\x18\x02 \x01(\t\"$\n\x12LoadPinMapResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"K\n\x12\x45nableSitesRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tsite_list\x18\x02 \x01(\t\"%\n\x13\x45nableSitesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"L\n\x13\x44isableSitesRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tsite_list\x18\x02 \x01(\t\"&\n\x14\x44isableSitesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"H\n\x14IsSiteEnabledRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0c\n\x04site\x18\x02 \x01(\t\"7\n\x15IsSiteEnabledResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0e\n\x06\x65nable\x18\x02 \x01(\x08\"h\n\x13\x43reatePinMapRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x64ut_pin_list\x18\x02 \x01(\t\x12\x17\n\x0fsystem_pin_list\x18\x03 \x01(\t\"&\n\x14\x43reatePinMapResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"e\n\x15\x43reatePinGroupRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x16\n\x0epin_group_name\x18\x02 \x01(\t\x12\x10\n\x08pin_list\x18\x03 \x01(\t\"(\n\x16\x43reatePinGroupResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"P\n\x17\x43reateChannelMapRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tnum_sites\x18\x02 \x01(\x11\"*\n\x18\x43reateChannelMapResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"h\n\x16MapPinToChannelRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0b\n\x03pin\x18\x02 \x01(\t\x12\x0c\n\x04site\x18\x03 \x01(\x11\x12\x0f\n\x07\x63hannel\x18\x04 \x01(\t\")\n\x17MapPinToChannelResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\":\n\x14\x45ndChannelMapRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\'\n\x15\x45ndChannelMapResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"J\n\x11GetPinNameRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tpin_index\x18\x02 \x01(\x11\"2\n\x12GetPinNameResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"J\n\x15GetChannelNameRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\r\n\x05index\x18\x02 \x01(\x11\"6\n\x16GetChannelNameResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xb7\x01\n\x15SelectFunctionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_list\x18\x02 \x01(\t\x12;\n\x08\x66unction\x18\x03 \x01(\x0e\x32\'.nidigitalpattern_grpc.SelectedFunctionH\x00\x12\x16\n\x0c\x66unction_raw\x18\x04 \x01(\x11H\x00\x42\x0f\n\rfunction_enum\"(\n\x16SelectFunctionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"M\n\x11ReadStaticRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_list\x18\x02 \x01(\t\"~\n\x12ReadStaticResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12-\n\x04\x64\x61ta\x18\x02 \x03(\x0e\x32\x1f.nidigitalpattern_grpc.PinState\x12\x10\n\x08\x64\x61ta_raw\x18\x03 \x01(\x0c\x12\x17\n\x0f\x61\x63tual_num_read\x18\x04 \x01(\x11\"\xae\x01\n\x12WriteStaticRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_list\x18\x02 \x01(\t\x12;\n\x05state\x18\x03 \x01(\x0e\x32*.nidigitalpattern_grpc.WriteStaticPinStateH\x00\x12\x13\n\tstate_raw\x18\x04 \x01(\rH\x00\x42\x0c\n\nstate_enum\"%\n\x13WriteStaticResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x92\x01\n\"ClockGeneratorGenerateClockRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_list\x18\x02 \x01(\t\x12\x11\n\tfrequency\x18\x03 \x01(\x01\x12\x1f\n\x17select_digital_function\x18\x04 \x01(\x08\"5\n#ClockGeneratorGenerateClockResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"Y\n\x1d\x43lockGeneratorInitiateRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_list\x18\x02 \x01(\t\"0\n\x1e\x43lockGeneratorInitiateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"V\n\x1a\x43lockGeneratorAbortRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_list\x18\x02 \x01(\t\"-\n\x1b\x43lockGeneratorAbortResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"R\n\x19LoadSpecificationsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tfile_path\x18\x02 \x01(\t\",\n\x1aLoadSpecificationsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"T\n\x1bUnloadSpecificationsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tfile_path\x18\x02 \x01(\t\".\n\x1cUnloadSpecificationsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"J\n\x11LoadLevelsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tfile_path\x18\x02 \x01(\t\"$\n\x12LoadLevelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"J\n\x11LoadTimingRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tfile_path\x18\x02 \x01(\t\"$\n\x12LoadTimingResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xe6\x01\n\x1b\x41pplyLevelsAndTimingRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tsite_list\x18\x02 \x01(\t\x12\x14\n\x0clevels_sheet\x18\x03 \x01(\t\x12\x14\n\x0ctiming_sheet\x18\x04 \x01(\t\x12\x1f\n\x17initial_state_high_pins\x18\x05 \x01(\t\x12\x1e\n\x16initial_state_low_pins\x18\x06 \x01(\t\x12#\n\x1binitial_state_tristate_pins\x18\x07 \x01(\t\".\n\x1c\x41pplyLevelsAndTimingResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x9c\x01\n\x1d\x43onfigureVoltageLevelsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_list\x18\x02 \x01(\t\x12\x0b\n\x03vil\x18\x03 \x01(\x01\x12\x0b\n\x03vih\x18\x04 \x01(\x01\x12\x0b\n\x03vol\x18\x05 \x01(\x01\x12\x0b\n\x03voh\x18\x06 \x01(\x01\x12\r\n\x05vterm\x18\x07 \x01(\x01\"0\n\x1e\x43onfigureVoltageLevelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x84\x01\n ConfigureActiveLoadLevelsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_list\x18\x02 \x01(\t\x12\x0b\n\x03iol\x18\x03 \x01(\x01\x12\x0b\n\x03ioh\x18\x04 \x01(\x01\x12\x0c\n\x04vcom\x18\x05 \x01(\x01\"3\n!ConfigureActiveLoadLevelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xb4\x01\n\x1f\x43onfigureTerminationModeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_list\x18\x02 \x01(\t\x12\x36\n\x04mode\x18\x03 \x01(\x0e\x32&.nidigitalpattern_grpc.TerminationModeH\x00\x12\x12\n\x08mode_raw\x18\x04 \x01(\x11H\x00\x42\x0b\n\tmode_enum\"2\n ConfigureTerminationModeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"H\n\x14\x43reateTimeSetRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0c\n\x04name\x18\x02 \x01(\t\"\'\n\x15\x43reateTimeSetResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"j\n\x1d\x43onfigureTimeSetPeriodRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x15\n\rtime_set_name\x18\x02 \x01(\t\x12\x0e\n\x06period\x18\x03 \x01(\x01\"0\n\x1e\x43onfigureTimeSetPeriodResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xae\x02\n!ConfigureTimeSetDriveEdgesRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x10\n\x08pin_list\x18\x02 \x01(\t\x12\x15\n\rtime_set_name\x18\x03 \x01(\t\x12\x34\n\x06\x66ormat\x18\x04 \x01(\x0e\x32\".nidigitalpattern_grpc.DriveFormatH\x00\x12\x14\n\nformat_raw\x18\x05 \x01(\x11H\x00\x12\x15\n\rdrive_on_edge\x18\x06 \x01(\x01\x12\x17\n\x0f\x64rive_data_edge\x18\x07 \x01(\x01\x12\x19\n\x11\x64rive_return_edge\x18\x08 \x01(\x01\x12\x16\n\x0e\x64rive_off_edge\x18\t \x01(\x01\x42\r\n\x0b\x66ormat_enum\"4\n\"ConfigureTimeSetDriveEdgesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x8d\x01\n)ConfigureTimeSetCompareEdgesStrobeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x10\n\x08pin_list\x18\x02 \x01(\t\x12\x15\n\rtime_set_name\x18\x03 \x01(\t\x12\x13\n\x0bstrobe_edge\x18\x04 \x01(\x01\"<\n*ConfigureTimeSetCompareEdgesStrobeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xde\x01\n\"ConfigureTimeSetDriveFormatRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x10\n\x08pin_list\x18\x02 \x01(\t\x12\x15\n\rtime_set_name\x18\x03 \x01(\t\x12:\n\x0c\x64rive_format\x18\x04 \x01(\x0e\x32\".nidigitalpattern_grpc.DriveFormatH\x00\x12\x1a\n\x10\x64rive_format_raw\x18\x05 \x01(\x11H\x00\x42\x13\n\x11\x64rive_format_enum\"5\n#ConfigureTimeSetDriveFormatResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\">\n\x18\x44\x65leteAllTimeSetsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"+\n\x19\x44\x65leteAllTimeSetsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x8d\x01\n%ConfigureTimeSetEdgeMultiplierRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x10\n\x08pin_list\x18\x02 \x01(\t\x12\x15\n\rtime_set_name\x18\x03 \x01(\t\x12\x17\n\x0f\x65\x64ge_multiplier\x18\x04 \x01(\x11\"8\n&ConfigureTimeSetEdgeMultiplierResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xe6\x02\n#ConfigureTimeSetDriveEdges2xRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x10\n\x08pin_list\x18\x02 \x01(\t\x12\x15\n\rtime_set_name\x18\x03 \x01(\t\x12\x34\n\x06\x66ormat\x18\x04 \x01(\x0e\x32\".nidigitalpattern_grpc.DriveFormatH\x00\x12\x14\n\nformat_raw\x18\x05 \x01(\x11H\x00\x12\x15\n\rdrive_on_edge\x18\x06 \x01(\x01\x12\x17\n\x0f\x64rive_data_edge\x18\x07 \x01(\x01\x12\x19\n\x11\x64rive_return_edge\x18\x08 \x01(\x01\x12\x16\n\x0e\x64rive_off_edge\x18\t \x01(\x01\x12\x18\n\x10\x64rive_data2_edge\x18\n \x01(\x01\x12\x1a\n\x12\x64rive_return2_edge\x18\x0b \x01(\x01\x42\r\n\x0b\x66ormat_enum\"6\n$ConfigureTimeSetDriveEdges2xResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xa5\x01\n+ConfigureTimeSetCompareEdgesStrobe2xRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x10\n\x08pin_list\x18\x02 \x01(\t\x12\x15\n\rtime_set_name\x18\x03 \x01(\t\x12\x13\n\x0bstrobe_edge\x18\x04 \x01(\x01\x12\x14\n\x0cstrobe2_edge\x18\x05 \x01(\x01\">\n,ConfigureTimeSetCompareEdgesStrobe2xResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xd1\x01\n\x1b\x43onfigureTimeSetEdgeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x10\n\x08pin_list\x18\x02 \x01(\t\x12\x15\n\rtime_set_name\x18\x03 \x01(\t\x12\x36\n\x04\x65\x64ge\x18\x04 \x01(\x0e\x32&.nidigitalpattern_grpc.TimeSetEdgeTypeH\x00\x12\x12\n\x08\x65\x64ge_raw\x18\x05 \x01(\x11H\x00\x12\x0c\n\x04time\x18\x06 \x01(\x01\x42\x0b\n\tedge_enum\".\n\x1c\x43onfigureTimeSetEdgeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"T\n\x17GetTimeSetPeriodRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x15\n\rtime_set_name\x18\x02 \x01(\t\":\n\x18GetTimeSetPeriodResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0e\n\x06period\x18\x02 \x01(\x01\"\xb8\x01\n\x15GetTimeSetEdgeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0b\n\x03pin\x18\x02 \x01(\t\x12\x15\n\rtime_set_name\x18\x03 \x01(\t\x12\x36\n\x04\x65\x64ge\x18\x04 \x01(\x0e\x32&.nidigitalpattern_grpc.TimeSetEdgeTypeH\x00\x12\x12\n\x08\x65\x64ge_raw\x18\x05 \x01(\x11H\x00\x42\x0b\n\tedge_enum\"6\n\x16GetTimeSetEdgeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04time\x18\x02 \x01(\x01\"i\n\x1fGetTimeSetEdgeMultiplierRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0b\n\x03pin\x18\x02 \x01(\t\x12\x15\n\rtime_set_name\x18\x03 \x01(\t\"K\n GetTimeSetEdgeMultiplierResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0f\x65\x64ge_multiplier\x18\x02 \x01(\x11\"f\n\x1cGetTimeSetDriveFormatRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0b\n\x03pin\x18\x02 \x01(\t\x12\x15\n\rtime_set_name\x18\x03 \x01(\t\"w\n\x1dGetTimeSetDriveFormatResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x32\n\x06\x66ormat\x18\x02 \x01(\x0e\x32\".nidigitalpattern_grpc.DriveFormat\x12\x12\n\nformat_raw\x18\x03 \x01(\x11\"S\n\x15GetTimeSetNameRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x16\n\x0etime_set_index\x18\x02 \x01(\x11\"6\n\x16GetTimeSetNameResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"]\n\nTDRRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_list\x18\x02 \x01(\t\x12\x15\n\rapply_offsets\x18\x03 \x01(\x08\"J\n\x0bTDRResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07offsets\x18\x02 \x03(\x01\x12\x1a\n\x12\x61\x63tual_num_offsets\x18\x03 \x01(\x11\"c\n\x16\x41pplyTDROffsetsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_list\x18\x02 \x01(\t\x12\x0f\n\x07offsets\x18\x03 \x03(\x01\")\n\x17\x41pplyTDROffsetsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xdb\x01\n\"PPMUConfigureOutputFunctionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_list\x18\x02 \x01(\t\x12\x44\n\x0foutput_function\x18\x03 \x01(\x0e\x32).nidigitalpattern_grpc.PpmuOutputFunctionH\x00\x12\x1d\n\x13output_function_raw\x18\x04 \x01(\x11H\x00\x42\x16\n\x14output_function_enum\"5\n#PPMUConfigureOutputFunctionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xd5\x01\n PPMUConfigureApertureTimeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_list\x18\x02 \x01(\t\x12\x15\n\raperture_time\x18\x03 \x01(\x01\x12=\n\x05units\x18\x04 \x01(\x0e\x32,.nidigitalpattern_grpc.PpmuApertureTimeUnitsH\x00\x12\x13\n\tunits_raw\x18\x05 \x01(\x11H\x00\x42\x0c\n\nunits_enum\"3\n!PPMUConfigureApertureTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"s\n PPMUConfigureVoltageLevelRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_list\x18\x02 \x01(\t\x12\x15\n\rvoltage_level\x18\x03 \x01(\x01\"3\n!PPMUConfigureVoltageLevelResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xd9\x01\n PPMUConfigureCurrentLimitRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_list\x18\x02 \x01(\t\x12\x43\n\x08\x62\x65havior\x18\x03 \x01(\x0e\x32/.nidigitalpattern_grpc.PpmuCurrentLimitBehaviorH\x00\x12\x16\n\x0c\x62\x65havior_raw\x18\x04 \x01(\x11H\x00\x12\r\n\x05limit\x18\x05 \x01(\x01\x42\x0f\n\rbehavior_enum\"3\n!PPMUConfigureCurrentLimitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"p\n%PPMUConfigureCurrentLimitRangeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_list\x18\x02 \x01(\t\x12\r\n\x05range\x18\x03 \x01(\x01\"8\n&PPMUConfigureCurrentLimitRangeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"s\n PPMUConfigureCurrentLevelRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_list\x18\x02 \x01(\t\x12\x15\n\rcurrent_level\x18\x03 \x01(\x01\"3\n!PPMUConfigureCurrentLevelResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"p\n%PPMUConfigureCurrentLevelRangeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_list\x18\x02 \x01(\t\x12\r\n\x05range\x18\x03 \x01(\x01\"8\n&PPMUConfigureCurrentLevelRangeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x97\x01\n!PPMUConfigureVoltageLimitsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_list\x18\x02 \x01(\t\x12\x1b\n\x13lower_voltage_limit\x18\x03 \x01(\x01\x12\x1b\n\x13upper_voltage_limit\x18\x04 \x01(\x01\"4\n\"PPMUConfigureVoltageLimitsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"M\n\x11PPMUSourceRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_list\x18\x02 \x01(\t\"$\n\x12PPMUSourceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xcf\x01\n\x12PPMUMeasureRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_list\x18\x02 \x01(\t\x12\x46\n\x10measurement_type\x18\x03 \x01(\x0e\x32*.nidigitalpattern_grpc.PpmuMeasurementTypeH\x00\x12\x1e\n\x14measurement_type_raw\x18\x04 \x01(\x11H\x00\x42\x17\n\x15measurement_type_enum\"T\n\x13PPMUMeasureResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x14\n\x0cmeasurements\x18\x02 \x03(\x01\x12\x17\n\x0f\x61\x63tual_num_read\x18\x03 \x01(\x11\"K\n\x12LoadPatternRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tfile_path\x18\x02 \x01(\t\"%\n\x13LoadPatternResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"a\n\x18UnloadAllPatternsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12!\n\x19unload_keep_alive_pattern\x18\x02 \x01(\x08\"+\n\x19UnloadAllPatternsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"O\n\x1a\x43onfigureStartLabelRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\r\n\x05label\x18\x02 \x01(\t\"-\n\x1b\x43onfigureStartLabelResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"Z\n!ConfigurePatternBurstSitesRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tsite_list\x18\x02 \x01(\t\"4\n\"ConfigurePatternBurstSitesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"V\n\x1bGetPatternPinIndexesRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x13\n\x0bstart_label\x18\x02 \x01(\t\"\\\n\x1cGetPatternPinIndexesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0bpin_indexes\x18\x02 \x03(\x11\x12\x17\n\x0f\x61\x63tual_num_pins\x18\x03 \x01(\x11\"S\n\x18GetPatternPinListRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x13\n\x0bstart_label\x18\x02 \x01(\t\"=\n\x19GetPatternPinListResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08pin_list\x18\x02 \x01(\t\"R\n\x15GetPatternNameRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x15\n\rpattern_index\x18\x02 \x01(\x11\"6\n\x16GetPatternNameResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xac\x01\n\x13\x42urstPatternRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tsite_list\x18\x02 \x01(\t\x12\x13\n\x0bstart_label\x18\x03 \x01(\t\x12\x1f\n\x17select_digital_function\x18\x04 \x01(\x08\x12\x17\n\x0fwait_until_done\x18\x05 \x01(\x08\x12\x0f\n\x07timeout\x18\x06 \x01(\x01\"&\n\x14\x42urstPatternResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xd5\x01\n\x1f\x42urstPatternSynchronizedRequest\x12\x15\n\rsession_count\x18\x01 \x01(\r\x12(\n\x08sessions\x18\x02 \x03(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tsite_list\x18\x03 \x01(\t\x12\x13\n\x0bstart_label\x18\x04 \x01(\t\x12\x1f\n\x17select_digital_function\x18\x05 \x01(\x08\x12\x17\n\x0fwait_until_done\x18\x06 \x01(\x08\x12\x0f\n\x07timeout\x18\x07 \x01(\x01\"2\n BurstPatternSynchronizedResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"3\n\rCommitRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\" \n\x0e\x43ommitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"5\n\x0fInitiateRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\"\n\x10InitiateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"3\n\rIsDoneRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\".\n\x0eIsDoneResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04\x64one\x18\x02 \x01(\x08\"K\n\x14WaitUntilDoneRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0f\n\x07timeout\x18\x02 \x01(\x01\"\'\n\x15WaitUntilDoneResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"2\n\x0c\x41\x62ortRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\x1f\n\rAbortResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\";\n\x15\x41\x62ortKeepAliveRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"(\n\x16\x41\x62ortKeepAliveResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xab\x01\n-ConfigurePatternLabelHistoryRAMTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\r\n\x05label\x18\x02 \x01(\t\x12\x15\n\rvector_offset\x18\x03 \x01(\x03\x12\x14\n\x0c\x63ycle_offset\x18\x04 \x01(\x03\x12\x1a\n\x12pretrigger_samples\x18\x05 \x01(\x11\"@\n.ConfigurePatternLabelHistoryRAMTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x84\x01\n,ConfigureCycleNumberHistoryRAMTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63ycle_number\x18\x02 \x01(\x03\x12\x1a\n\x12pretrigger_samples\x18\x03 \x01(\x11\"?\n-ConfigureCycleNumberHistoryRAMTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"o\n-ConfigureFirstFailureHistoryRAMTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x1a\n\x12pretrigger_samples\x18\x02 \x01(\x11\"@\n.ConfigureFirstFailureHistoryRAMTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xd9\x01\n)ConfigureHistoryRAMCyclesToAcquireRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12M\n\x11\x63ycles_to_acquire\x18\x02 \x01(\x0e\x32\x30.nidigitalpattern_grpc.HistoryRamCyclesToAcquireH\x00\x12\x1f\n\x15\x63ycles_to_acquire_raw\x18\x03 \x01(\x11H\x00\x42\x18\n\x16\x63ycles_to_acquire_enum\"<\n*ConfigureHistoryRAMCyclesToAcquireResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"S\n\x1fGetHistoryRAMSampleCountRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0c\n\x04site\x18\x02 \x01(\t\"H\n GetHistoryRAMSampleCountResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x14\n\x0csample_count\x18\x02 \x01(\x03\"p\n&FetchHistoryRAMCycleInformationRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0c\n\x04site\x18\x02 \x01(\t\x12\x14\n\x0csample_index\x18\x03 \x01(\x03\"\xad\x01\n\'FetchHistoryRAMCycleInformationResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rpattern_index\x18\x02 \x01(\x11\x12\x16\n\x0etime_set_index\x18\x03 \x01(\x11\x12\x15\n\rvector_number\x18\x04 \x01(\x03\x12\x14\n\x0c\x63ycle_number\x18\x05 \x01(\x03\x12\x16\n\x0enum_dut_cycles\x18\x06 \x01(\x11\"\x97\x01\n\"FetchHistoryRAMCyclePinDataRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0c\n\x04site\x18\x02 \x01(\t\x12\x10\n\x08pin_list\x18\x03 \x01(\t\x12\x14\n\x0csample_index\x18\x04 \x01(\x03\x12\x17\n\x0f\x64ut_cycle_index\x18\x05 \x01(\x11\"\xa7\x02\n#FetchHistoryRAMCyclePinDataResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12<\n\x13\x65xpected_pin_states\x18\x02 \x03(\x0e\x32\x1f.nidigitalpattern_grpc.PinState\x12\x1f\n\x17\x65xpected_pin_states_raw\x18\x03 \x01(\x0c\x12:\n\x11\x61\x63tual_pin_states\x18\x04 \x03(\x0e\x32\x1f.nidigitalpattern_grpc.PinState\x12\x1d\n\x15\x61\x63tual_pin_states_raw\x18\x05 \x01(\x0c\x12\x19\n\x11per_pin_pass_fail\x18\x06 \x03(\x08\x12\x1b\n\x13\x61\x63tual_num_pin_data\x18\x07 \x01(\x11\"o\n%FetchHistoryRAMScanCycleNumberRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0c\n\x04site\x18\x02 \x01(\t\x12\x14\n\x0csample_index\x18\x03 \x01(\x03\"S\n&FetchHistoryRAMScanCycleNumberResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x19\n\x11scan_cycle_number\x18\x02 \x01(\x03\"\xe5\x01\n#CreateSourceWaveformParallelRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x10\n\x08pin_list\x18\x02 \x01(\t\x12\x15\n\rwaveform_name\x18\x03 \x01(\t\x12@\n\x0c\x64\x61ta_mapping\x18\x04 \x01(\x0e\x32(.nidigitalpattern_grpc.SourceDataMappingH\x00\x12\x1a\n\x10\x64\x61ta_mapping_raw\x18\x05 \x01(\x11H\x00\x42\x13\n\x11\x64\x61ta_mapping_enum\"6\n$CreateSourceWaveformParallelResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xda\x02\n!CreateSourceWaveformSerialRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x10\n\x08pin_list\x18\x02 \x01(\t\x12\x15\n\rwaveform_name\x18\x03 \x01(\t\x12@\n\x0c\x64\x61ta_mapping\x18\x04 \x01(\x0e\x32(.nidigitalpattern_grpc.SourceDataMappingH\x00\x12\x1a\n\x10\x64\x61ta_mapping_raw\x18\x05 \x01(\x11H\x00\x12\x14\n\x0csample_width\x18\x06 \x01(\r\x12\x34\n\tbit_order\x18\x07 \x01(\x0e\x32\x1f.nidigitalpattern_grpc.BitOrderH\x01\x12\x17\n\rbit_order_raw\x18\x08 \x01(\x11H\x01\x42\x13\n\x11\x64\x61ta_mapping_enumB\x10\n\x0e\x62it_order_enum\"4\n\"CreateSourceWaveformSerialResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x9d\x01\n\'CreateSourceWaveformFromFileTDMSRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x15\n\rwaveform_name\x18\x02 \x01(\t\x12\x1a\n\x12waveform_file_path\x18\x03 \x01(\t\x12\x1b\n\x13write_waveform_data\x18\x04 \x01(\x08\":\n(CreateSourceWaveformFromFileTDMSResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"z\n&WriteSourceWaveformBroadcastU32Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x15\n\rwaveform_name\x18\x02 \x01(\t\x12\x15\n\rwaveform_data\x18\x03 \x03(\r\"9\n\'WriteSourceWaveformBroadcastU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xc3\x01\n\'WriteSourceWaveformSiteUniqueU32Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tsite_list\x18\x02 \x01(\t\x12\x15\n\rwaveform_name\x18\x03 \x01(\t\x12\x15\n\rnum_waveforms\x18\x04 \x01(\x11\x12\x1c\n\x14samples_per_waveform\x18\x05 \x01(\x11\x12\x15\n\rwaveform_data\x18\x06 \x03(\r\":\n(WriteSourceWaveformSiteUniqueU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x83\x01\n*WriteSourceWaveformDataFromFileTDMSRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x15\n\rwaveform_name\x18\x02 \x01(\t\x12\x1a\n\x12waveform_file_path\x18\x03 \x01(\t\"=\n+WriteSourceWaveformDataFromFileTDMSResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"s\n$CreateCaptureWaveformParallelRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x10\n\x08pin_list\x18\x02 \x01(\t\x12\x15\n\rwaveform_name\x18\x03 \x01(\t\"7\n%CreateCaptureWaveformParallelResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xe8\x01\n\"CreateCaptureWaveformSerialRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x10\n\x08pin_list\x18\x02 \x01(\t\x12\x15\n\rwaveform_name\x18\x03 \x01(\t\x12\x14\n\x0csample_width\x18\x04 \x01(\r\x12\x34\n\tbit_order\x18\x05 \x01(\x0e\x32\x1f.nidigitalpattern_grpc.BitOrderH\x00\x12\x17\n\rbit_order_raw\x18\x06 \x01(\x11H\x00\x42\x10\n\x0e\x62it_order_enum\"5\n#CreateCaptureWaveformSerialResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x88\x01\n/CreateCaptureWaveformFromFileDigicaptureRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x15\n\rwaveform_name\x18\x02 \x01(\t\x12\x1a\n\x12waveform_file_path\x18\x03 \x01(\t\"B\n0CreateCaptureWaveformFromFileDigicaptureResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x98\x01\n\x1e\x46\x65tchCaptureWaveformU32Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tsite_list\x18\x02 \x01(\t\x12\x15\n\rwaveform_name\x18\x03 \x01(\t\x12\x17\n\x0fsamples_to_read\x18\x04 \x01(\x11\x12\x0f\n\x07timeout\x18\x05 \x01(\x01\"\x82\x01\n\x1f\x46\x65tchCaptureWaveformU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x03(\r\x12\x1c\n\x14\x61\x63tual_num_waveforms\x18\x03 \x01(\x11\x12#\n\x1b\x61\x63tual_samples_per_waveform\x18\x04 \x01(\x11\"\xc9\x01\n\x13\x45xportSignalRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x35\n\x06signal\x18\x02 \x01(\x0e\x32#.nidigitalpattern_grpc.ExportSignalH\x00\x12\x14\n\nsignal_raw\x18\x03 \x01(\x11H\x00\x12\x19\n\x11signal_identifier\x18\x04 \x01(\t\x12\x17\n\x0foutput_terminal\x18\x05 \x01(\tB\r\n\x0bsignal_enum\"&\n\x14\x45xportSignalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xb2\x01\n\'ConfigureDigitalEdgeStartTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0e\n\x06source\x18\x02 \x01(\t\x12\x32\n\x04\x65\x64ge\x18\x03 \x01(\x0e\x32\".nidigitalpattern_grpc.DigitalEdgeH\x00\x12\x12\n\x08\x65\x64ge_raw\x18\x04 \x01(\x11H\x00\x42\x0b\n\tedge_enum\":\n(ConfigureDigitalEdgeStartTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"N\n(ConfigureSoftwareEdgeStartTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\";\n)ConfigureSoftwareEdgeStartTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"@\n\x1a\x44isableStartTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"-\n\x1b\x44isableStartTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xd8\x01\n1ConfigureDigitalEdgeConditionalJumpTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x1a\n\x12trigger_identifier\x18\x02 \x01(\t\x12\x0e\n\x06source\x18\x03 \x01(\t\x12\x32\n\x04\x65\x64ge\x18\x04 \x01(\x0e\x32\".nidigitalpattern_grpc.DigitalEdgeH\x00\x12\x12\n\x08\x65\x64ge_raw\x18\x05 \x01(\x11H\x00\x42\x0b\n\tedge_enum\"D\n2ConfigureDigitalEdgeConditionalJumpTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"t\n2ConfigureSoftwareEdgeConditionalJumpTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x1a\n\x12trigger_identifier\x18\x02 \x01(\t\"E\n3ConfigureSoftwareEdgeConditionalJumpTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"f\n$DisableConditionalJumpTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x1a\n\x12trigger_identifier\x18\x02 \x01(\t\"7\n%DisableConditionalJumpTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xc2\x01\n\x1eSendSoftwareEdgeTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x39\n\x07trigger\x18\x02 \x01(\x0e\x32&.nidigitalpattern_grpc.SoftwareTriggerH\x00\x12\x15\n\x0btrigger_raw\x18\x03 \x01(\x11H\x00\x12\x1a\n\x12trigger_identifier\x18\x04 \x01(\tB\x0e\n\x0ctrigger_enum\"1\n\x1fSendSoftwareEdgeTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\\\n\x19WriteSequencerFlagRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0c\n\x04\x66lag\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x08\",\n\x1aWriteSequencerFlagResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x85\x01\n%WriteSequencerFlagSynchronizedRequest\x12\x15\n\rsession_count\x18\x01 \x01(\r\x12(\n\x08sessions\x18\x02 \x03(\x0b\x32\x16.nidevice_grpc.Session\x12\x0c\n\x04\x66lag\x18\x03 \x01(\t\x12\r\n\x05value\x18\x04 \x01(\x08\"8\n&WriteSequencerFlagSynchronizedResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"L\n\x18ReadSequencerFlagRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0c\n\x04\x66lag\x18\x02 \x01(\t\":\n\x19ReadSequencerFlagResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08\"_\n\x1dWriteSequencerRegisterRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0b\n\x03reg\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x11\"0\n\x1eWriteSequencerRegisterResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"O\n\x1cReadSequencerRegisterRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0b\n\x03reg\x18\x02 \x01(\t\">\n\x1dReadSequencerRegisterResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x11\"\x92\x01\n!EnableMatchFailCombinationRequest\x12\x15\n\rsession_count\x18\x01 \x01(\r\x12(\n\x08sessions\x18\x02 \x03(\x0b\x32\x16.nidevice_grpc.Session\x12,\n\x0csync_session\x18\x03 \x01(\x0b\x32\x16.nidevice_grpc.Session\"4\n\"EnableMatchFailCombinationResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"O\n\x16GetSitePassFailRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tsite_list\x18\x02 \x01(\t\"V\n\x17GetSitePassFailResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\tpass_fail\x18\x02 \x03(\x08\x12\x18\n\x10\x61\x63tual_num_sites\x18\x03 \x01(\x11\"O\n\x13GetFailCountRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_list\x18\x02 \x01(\t\"V\n\x14GetFailCountResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rfailure_count\x18\x02 \x03(\x03\x12\x17\n\x0f\x61\x63tual_num_read\x18\x03 \x01(\x11\"^\n\"GetPinResultsPinInformationRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_list\x18\x02 \x01(\t\"\x94\x01\n#GetPinResultsPinInformationResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0bpin_indexes\x18\x02 \x03(\x11\x12\x14\n\x0csite_numbers\x18\x03 \x03(\x11\x12\x17\n\x0f\x63hannel_indexes\x18\x04 \x03(\x11\x12\x19\n\x11\x61\x63tual_num_values\x18\x05 \x01(\x11\"\xd5\x01\n GetSiteResultsSiteNumbersRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tsite_list\x18\x02 \x01(\t\x12\x41\n\x10site_result_type\x18\x03 \x01(\x0e\x32%.nidigitalpattern_grpc.SiteResultTypeH\x00\x12\x1e\n\x14site_result_type_raw\x18\x04 \x01(\x11H\x00\x42\x17\n\x15site_result_type_enum\"j\n!GetSiteResultsSiteNumbersResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x14\n\x0csite_numbers\x18\x02 \x03(\x11\x12\x1f\n\x17\x61\x63tual_num_site_numbers\x18\x03 \x01(\x11\"\x85\x01\n/FrequencyCounterConfigureMeasurementTimeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_list\x18\x02 \x01(\t\x12\x18\n\x10measurement_time\x18\x03 \x01(\x01\"B\n0FrequencyCounterConfigureMeasurementTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xdb\x01\n/FrequencyCounterConfigureMeasurementModeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12K\n\x10measurement_mode\x18\x02 \x01(\x0e\x32/.nidigitalpattern_grpc.FrequencyMeasurementModeH\x00\x12\x1e\n\x14measurement_mode_raw\x18\x03 \x01(\x11H\x00\x42\x17\n\x15measurement_mode_enum\"B\n0FrequencyCounterConfigureMeasurementModeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"c\n\'FrequencyCounterMeasureFrequencyRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_list\x18\x02 \x01(\t\"o\n(FrequencyCounterMeasureFrequencyResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0b\x66requencies\x18\x02 \x03(\x01\x12\x1e\n\x16\x61\x63tual_num_frequencies\x18\x03 \x01(\x11\"V\n\x1fGetChannelNameFromStringRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0f\n\x07indices\x18\x02 \x01(\t\"A\n GetChannelNameFromStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05names\x18\x02 \x01(\t*\x8c$\n\x12NiDigitalAttribute\x12#\n\x1fNIDIGITAL_ATTRIBUTE_UNSPECIFIED\x10\x00\x12%\n\x1fNIDIGITAL_ATTRIBUTE_RANGE_CHECK\x10\x92\x8b@\x12\x31\n+NIDIGITAL_ATTRIBUTE_QUERY_INSTRUMENT_STATUS\x10\x93\x8b@\x12\x1f\n\x19NIDIGITAL_ATTRIBUTE_CACHE\x10\x94\x8b@\x12\"\n\x1cNIDIGITAL_ATTRIBUTE_SIMULATE\x10\x95\x8b@\x12*\n$NIDIGITAL_ATTRIBUTE_RECORD_COERCIONS\x10\x96\x8b@\x12&\n NIDIGITAL_ATTRIBUTE_DRIVER_SETUP\x10\x97\x8b@\x12+\n%NIDIGITAL_ATTRIBUTE_INTERCHANGE_CHECK\x10\xa5\x8b@\x12\'\n!NIDIGITAL_ATTRIBUTE_CHANNEL_COUNT\x10\xdb\x8c@\x12\x30\n*NIDIGITAL_ATTRIBUTE_SPECIFIC_DRIVER_PREFIX\x10\xbe\x8d@\x12\x30\n*NIDIGITAL_ATTRIBUTE_IO_RESOURCE_DESCRIPTOR\x10\xc0\x8d@\x12&\n NIDIGITAL_ATTRIBUTE_LOGICAL_NAME\x10\xc1\x8d@\x12\x35\n/NIDIGITAL_ATTRIBUTE_SUPPORTED_INSTRUMENT_MODELS\x10\xd7\x8d@\x12,\n&NIDIGITAL_ATTRIBUTE_GROUP_CAPABILITIES\x10\xa1\x8e@\x12\x36\n0NIDIGITAL_ATTRIBUTE_INSTRUMENT_FIRMWARE_REVISION\x10\x8e\x8f@\x12\x31\n+NIDIGITAL_ATTRIBUTE_INSTRUMENT_MANUFACTURER\x10\x8f\x8f@\x12\x30\n*NIDIGITAL_ATTRIBUTE_SPECIFIC_DRIVER_VENDOR\x10\x91\x8f@\x12\x35\n/NIDIGITAL_ATTRIBUTE_SPECIFIC_DRIVER_DESCRIPTION\x10\x92\x8f@\x12\x42\n<NIDIGITAL_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION\x10\x93\x8f@\x12\x42\n<NIDIGITAL_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION\x10\x94\x8f@\x12\x32\n,NIDIGITAL_ATTRIBUTE_SPECIFIC_DRIVER_REVISION\x10\xb7\x8f@\x12*\n$NIDIGITAL_ATTRIBUTE_INSTRUMENT_MODEL\x10\x90\x8f@\x12\'\n!NIDIGITAL_ATTRIBUTE_SERIAL_NUMBER\x10\xb1\x98\x46\x12+\n%NIDIGITAL_ATTRIBUTE_SELECTED_FUNCTION\x10\xb4\x98\x46\x12*\n$NIDIGITAL_ATTRIBUTE_TERMINATION_MODE\x10\xb6\x98\x46\x12\x1d\n\x17NIDIGITAL_ATTRIBUTE_VIL\x10\xb7\x98\x46\x12\x1d\n\x17NIDIGITAL_ATTRIBUTE_VIH\x10\xb8\x98\x46\x12\x1d\n\x17NIDIGITAL_ATTRIBUTE_VOL\x10\xb9\x98\x46\x12\x1d\n\x17NIDIGITAL_ATTRIBUTE_VOH\x10\xba\x98\x46\x12\x1f\n\x19NIDIGITAL_ATTRIBUTE_VTERM\x10\xbb\x98\x46\x12)\n#NIDIGITAL_ATTRIBUTE_ACTIVE_LOAD_IOL\x10\xbc\x98\x46\x12)\n#NIDIGITAL_ATTRIBUTE_ACTIVE_LOAD_IOH\x10\xbd\x98\x46\x12*\n$NIDIGITAL_ATTRIBUTE_ACTIVE_LOAD_VCOM\x10\xbe\x98\x46\x12.\n(NIDIGITAL_ATTRIBUTE_PPMU_OUTPUT_FUNCTION\x10\xbf\x98\x46\x12,\n&NIDIGITAL_ATTRIBUTE_PPMU_VOLTAGE_LEVEL\x10\xc0\x98\x46\x12\x32\n,NIDIGITAL_ATTRIBUTE_PPMU_CURRENT_LIMIT_RANGE\x10\xc1\x98\x46\x12,\n&NIDIGITAL_ATTRIBUTE_PPMU_CURRENT_LEVEL\x10\xc3\x98\x46\x12\x32\n,NIDIGITAL_ATTRIBUTE_PPMU_CURRENT_LEVEL_RANGE\x10\xc4\x98\x46\x12\x30\n*NIDIGITAL_ATTRIBUTE_PPMU_VOLTAGE_LIMIT_LOW\x10\xc5\x98\x46\x12\x31\n+NIDIGITAL_ATTRIBUTE_PPMU_VOLTAGE_LIMIT_HIGH\x10\xc6\x98\x46\x12%\n\x1fNIDIGITAL_ATTRIBUTE_START_LABEL\x10\xc7\x98\x46\x12,\n&NIDIGITAL_ATTRIBUTE_START_TRIGGER_TYPE\x10\xcd\x98\x46\x12;\n5NIDIGITAL_ATTRIBUTE_DIGITAL_EDGE_START_TRIGGER_SOURCE\x10\xce\x98\x46\x12\x39\n3NIDIGITAL_ATTRIBUTE_DIGITAL_EDGE_START_TRIGGER_EDGE\x10\xcf\x98\x46\x12@\n:NIDIGITAL_ATTRIBUTE_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL\x10\xd0\x98\x46\x12\x35\n/NIDIGITAL_ATTRIBUTE_START_TRIGGER_TERMINAL_NAME\x10\xd7\x98\x46\x12,\n&NIDIGITAL_ATTRIBUTE_PPMU_APERTURE_TIME\x10\xd5\x98\x46\x12\x32\n,NIDIGITAL_ATTRIBUTE_PPMU_APERTURE_TIME_UNITS\x10\xd6\x98\x46\x12G\nANIDIGITAL_ATTRIBUTE_EXPORTED_PATTERN_OPCODE_EVENT_OUTPUT_TERMINAL\x10\xd9\x98\x46\x12<\n6NIDIGITAL_ATTRIBUTE_PATTERN_OPCODE_EVENT_TERMINAL_NAME\x10\xda\x98\x46\x12\x32\n,NIDIGITAL_ATTRIBUTE_HISTORY_RAM_TRIGGER_TYPE\x10\xdb\x98\x46\x12G\nANIDIGITAL_ATTRIBUTE_CYCLE_NUMBER_HISTORY_RAM_TRIGGER_CYCLE_NUMBER\x10\xdc\x98\x46\x12H\nBNIDIGITAL_ATTRIBUTE_PATTERN_LABEL_HISTORY_RAM_TRIGGER_CYCLE_OFFSET\x10\xdd\x98\x46\x12\x41\n;NIDIGITAL_ATTRIBUTE_PATTERN_LABEL_HISTORY_RAM_TRIGGER_LABEL\x10\xde\x98\x46\x12\x37\n1NIDIGITAL_ATTRIBUTE_HISTORY_RAM_CYCLES_TO_ACQUIRE\x10\xdf\x98\x46\x12\x38\n2NIDIGITAL_ATTRIBUTE_HISTORY_RAM_PRETRIGGER_SAMPLES\x10\xe0\x98\x46\x12\x32\n,NIDIGITAL_ATTRIBUTE_TDR_ENDPOINT_TERMINATION\x10\x81\x99\x46\x12*\n$NIDIGITAL_ATTRIBUTE_RIO_TRIGGER_TYPE\x10\x86\x99\x46\x12\x39\n3NIDIGITAL_ATTRIBUTE_DIGITAL_EDGE_RIO_TRIGGER_SOURCE\x10\x87\x99\x46\x12\x37\n1NIDIGITAL_ATTRIBUTE_DIGITAL_EDGE_RIO_TRIGGER_EDGE\x10\x88\x99\x46\x12\x33\n-NIDIGITAL_ATTRIBUTE_RIO_TRIGGER_TERMINAL_NAME\x10\x89\x99\x46\x12<\n6NIDIGITAL_ATTRIBUTE_EXPORTED_RIO_EVENT_OUTPUT_TERMINAL\x10\x8a\x99\x46\x12\x31\n+NIDIGITAL_ATTRIBUTE_RIO_EVENT_TERMINAL_NAME\x10\x8b\x99\x46\x12$\n\x1eNIDIGITAL_ATTRIBUTE_TDR_OFFSET\x10\xe3\x98\x46\x12I\nCNIDIGITAL_ATTRIBUTE_PATTERN_LABEL_HISTORY_RAM_TRIGGER_VECTOR_OFFSET\x10\xe4\x98\x46\x12,\n&NIDIGITAL_ATTRIBUTE_PPMU_CURRENT_LIMIT\x10\xe6\x98\x46\x12\x36\n0NIDIGITAL_ATTRIBUTE_PPMU_CURRENT_LIMIT_SUPPORTED\x10\xe7\x98\x46\x12\x36\n0NIDIGITAL_ATTRIBUTE_SEQUENCER_FLAG_TERMINAL_NAME\x10\xeb\x98\x46\x12&\n NIDIGITAL_ATTRIBUTE_MASK_COMPARE\x10\xec\x98\x46\x12\x33\n-NIDIGITAL_ATTRIBUTE_HALT_ON_KEEP_ALIVE_OPCODE\x10\xee\x98\x46\x12.\n(NIDIGITAL_ATTRIBUTE_IS_KEEP_ALIVE_ACTIVE\x10\xef\x98\x46\x12\x35\n/NIDIGITAL_ATTRIBUTE_PPMU_CURRENT_LIMIT_BEHAVIOR\x10\xf0\x98\x46\x12<\n6NIDIGITAL_ATTRIBUTE_FREQUENCY_COUNTER_MEASUREMENT_TIME\x10\xf5\x98\x46\x12<\n6NIDIGITAL_ATTRIBUTE_FREQUENCY_COUNTER_MEASUREMENT_MODE\x10\x84\x99\x46\x12>\n8NIDIGITAL_ATTRIBUTE_FREQUENCY_COUNTER_HYSTERESIS_ENABLED\x10\x85\x99\x46\x12\x37\n1NIDIGITAL_ATTRIBUTE_TIMING_ABSOLUTE_DELAY_ENABLED\x10\xf7\x98\x46\x12/\n)NIDIGITAL_ATTRIBUTE_TIMING_ABSOLUTE_DELAY\x10\xf8\x98\x46\x12\x33\n-NIDIGITAL_ATTRIBUTE_CLOCK_GENERATOR_FREQUENCY\x10\xf9\x98\x46\x12\x34\n.NIDIGITAL_ATTRIBUTE_CLOCK_GENERATOR_IS_RUNNING\x10\xfa\x98\x46\x12;\n5NIDIGITAL_ATTRIBUTE_PPMU_ALLOW_EXTENDED_VOLTAGE_RANGE\x10\xfc\x98\x46\x12\x45\n?NIDIGITAL_ATTRIBUTE_HISTORY_RAM_MAX_SAMPLES_TO_ACQUIRE_PER_SITE\x10\xfd\x98\x46\x12\x41\n;NIDIGITAL_ATTRIBUTE_HISTORY_RAM_NUMBER_OF_SAMPLES_IS_FINITE\x10\xfe\x98\x46\x12:\n4NIDIGITAL_ATTRIBUTE_HISTORY_RAM_BUFFER_SIZE_PER_SITE\x10\xff\x98\x46\x12\x37\n1NIDIGITAL_ATTRIBUTE_CONDITIONAL_JUMP_TRIGGER_TYPE\x10\xd1\x98\x46\x12\x46\n@NIDIGITAL_ATTRIBUTE_DIGITAL_EDGE_CONDITIONAL_JUMP_TRIGGER_SOURCE\x10\xd2\x98\x46\x12\x44\n>NIDIGITAL_ATTRIBUTE_DIGITAL_EDGE_CONDITIONAL_JUMP_TRIGGER_EDGE\x10\xd3\x98\x46\x12K\nENIDIGITAL_ATTRIBUTE_EXPORTED_CONDITIONAL_JUMP_TRIGGER_OUTPUT_TERMINAL\x10\xd4\x98\x46\x12@\n:NIDIGITAL_ATTRIBUTE_CONDITIONAL_JUMP_TRIGGER_TERMINAL_NAME\x10\xd8\x98\x46*v\n\x15PpmuApertureTimeUnits\x12(\n$PPMU_APERTURE_TIME_UNITS_UNSPECIFIED\x10\x00\x12\x33\n.PPMU_APERTURE_TIME_UNITS_NIDIGITAL_VAL_SECONDS\x10\xb4\x10*u\n\x08\x42itOrder\x12\x19\n\x15\x42IT_ORDER_UNSPECIFIED\x10\x00\x12&\n!BIT_ORDER_NIDIGITAL_VAL_MSB_FIRST\x10\xc4\x13\x12&\n!BIT_ORDER_NIDIGITAL_VAL_LSB_FIRST\x10\xc5\x13*\x86\x01\n\x0b\x44igitalEdge\x12\x1c\n\x18\x44IGITAL_EDGE_UNSPECIFIED\x10\x00\x12+\n&DIGITAL_EDGE_NIDIGITAL_VAL_RISING_EDGE\x10\x88\x0e\x12,\n\'DIGITAL_EDGE_NIDIGITAL_VAL_FALLING_EDGE\x10\x89\x0e*\x84\x03\n\x08PinState\x12\x1d\n\x19PIN_STATE_NIDIGITAL_VAL_0\x10\x00\x12\x1d\n\x19PIN_STATE_NIDIGITAL_VAL_1\x10\x01\x12\x1d\n\x19PIN_STATE_NIDIGITAL_VAL_L\x10\x03\x12\x1d\n\x19PIN_STATE_NIDIGITAL_VAL_H\x10\x04\x12\x1d\n\x19PIN_STATE_NIDIGITAL_VAL_X\x10\x05\x12\x1d\n\x19PIN_STATE_NIDIGITAL_VAL_M\x10\x06\x12\x1d\n\x19PIN_STATE_NIDIGITAL_VAL_V\x10\x07\x12\x1d\n\x19PIN_STATE_NIDIGITAL_VAL_D\x10\x08\x12\x1d\n\x19PIN_STATE_NIDIGITAL_VAL_E\x10\t\x12,\n\'PIN_STATE_NIDIGITAL_VAL_NOT_A_PIN_STATE\x10\xfe\x01\x12\x33\n.PIN_STATE_NIDIGITAL_VAL_PIN_STATE_NOT_ACQUIRED\x10\xff\x01*\xbc\x01\n\x0b\x44riveFormat\x12\x1c\n\x18\x44RIVE_FORMAT_UNSPECIFIED\x10\x00\x12\"\n\x1d\x44RIVE_FORMAT_NIDIGITAL_VAL_NR\x10\xdc\x0b\x12\"\n\x1d\x44RIVE_FORMAT_NIDIGITAL_VAL_RL\x10\xdd\x0b\x12\"\n\x1d\x44RIVE_FORMAT_NIDIGITAL_VAL_RH\x10\xde\x0b\x12#\n\x1e\x44RIVE_FORMAT_NIDIGITAL_VAL_SBC\x10\xdf\x0b*\xc7\x01\n\x19HistoryRamCyclesToAcquire\x12-\n)HISTORY_RAM_CYCLES_TO_ACQUIRE_UNSPECIFIED\x10\x00\x12>\n9HISTORY_RAM_CYCLES_TO_ACQUIRE_NIDIGITAL_VAL_FAILED_CYCLES\x10\xff\x11\x12;\n6HISTORY_RAM_CYCLES_TO_ACQUIRE_NIDIGITAL_VAL_ALL_CYCLES\x10\x80\x12*\x88\x01\n\x18PpmuCurrentLimitBehavior\x12+\n\'PPMU_CURRENT_LIMIT_BEHAVIOR_UNSPECIFIED\x10\x00\x12?\n:PPMU_CURRENT_LIMIT_BEHAVIOR_NIDIGITAL_VAL_CURRENT_REGULATE\x10\x9c\x18*\xb0\x01\n\x13PpmuMeasurementType\x12%\n!PPMU_MEASUREMENT_TYPE_UNSPECIFIED\x10\x00\x12\x38\n3PPMU_MEASUREMENT_TYPE_NIDIGITAL_VAL_MEASURE_CURRENT\x10\xe0\x12\x12\x38\n3PPMU_MEASUREMENT_TYPE_NIDIGITAL_VAL_MEASURE_VOLTAGE\x10\xe1\x12*\xa2\x01\n\x12PpmuOutputFunction\x12$\n PPMU_OUTPUT_FUNCTION_UNSPECIFIED\x10\x00\x12\x32\n-PPMU_OUTPUT_FUNCTION_NIDIGITAL_VAL_DC_VOLTAGE\x10\x94\n\x12\x32\n-PPMU_OUTPUT_FUNCTION_NIDIGITAL_VAL_DC_CURRENT\x10\x95\n*\x93\x02\n\x10SelectedFunction\x12!\n\x1dSELECTED_FUNCTION_UNSPECIFIED\x10\x00\x12,\n\'SELECTED_FUNCTION_NIDIGITAL_VAL_DIGITAL\x10\xcc\x08\x12)\n$SELECTED_FUNCTION_NIDIGITAL_VAL_PPMU\x10\xcd\x08\x12(\n#SELECTED_FUNCTION_NIDIGITAL_VAL_OFF\x10\xce\x08\x12/\n*SELECTED_FUNCTION_NIDIGITAL_VAL_DISCONNECT\x10\xcf\x08\x12(\n#SELECTED_FUNCTION_NIDIGITAL_VAL_RIO\x10\xd0\x08*\xa7\x02\n\x0c\x45xportSignal\x12\x1d\n\x19\x45XPORT_SIGNAL_UNSPECIFIED\x10\x00\x12.\n)EXPORT_SIGNAL_NIDIGITAL_VAL_START_TRIGGER\x10\xd0\x0f\x12\x39\n4EXPORT_SIGNAL_NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER\x10\xd1\x0f\x12\x35\n0EXPORT_SIGNAL_NIDIGITAL_VAL_PATTERN_OPCODE_EVENT\x10\xd2\x0f\x12*\n%EXPORT_SIGNAL_NIDIGITAL_VAL_REF_CLOCK\x10\xd3\x0f\x12*\n%EXPORT_SIGNAL_NIDIGITAL_VAL_RIO_EVENT\x10\xd4\x0f*\x97\x01\n\x0eSiteResultType\x12 \n\x1cSITE_RESULT_TYPE_UNSPECIFIED\x10\x00\x12-\n(SITE_RESULT_TYPE_NIDIGITAL_VAL_PASS_FAIL\x10\xe4\x19\x12\x34\n/SITE_RESULT_TYPE_NIDIGITAL_VAL_CAPTURE_WAVEFORM\x10\xe5\x19*\xa4\x01\n\x0fSoftwareTrigger\x12 \n\x1cSOFTWARE_TRIGGER_UNSPECIFIED\x10\x00\x12\x31\n,SOFTWARE_TRIGGER_NIDIGITAL_VAL_START_TRIGGER\x10\xd0\x0f\x12<\n7SOFTWARE_TRIGGER_NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER\x10\xd1\x0f*\x9e\x01\n\x11SourceDataMapping\x12#\n\x1fSOURCE_DATA_MAPPING_UNSPECIFIED\x10\x00\x12\x30\n+SOURCE_DATA_MAPPING_NIDIGITAL_VAL_BROADCAST\x10\xa8\x14\x12\x32\n-SOURCE_DATA_MAPPING_NIDIGITAL_VAL_SITE_UNIQUE\x10\xa9\x14*\xbb\x01\n\x0fTerminationMode\x12 \n\x1cTERMINATION_MODE_UNSPECIFIED\x10\x00\x12/\n*TERMINATION_MODE_NIDIGITAL_VAL_ACTIVE_LOAD\x10\xb0\t\x12)\n$TERMINATION_MODE_NIDIGITAL_VAL_VTERM\x10\xb1\t\x12*\n%TERMINATION_MODE_NIDIGITAL_VAL_HIGH_Z\x10\xb2\t*\xd1\x03\n\x0fTimeSetEdgeType\x12\"\n\x1eTIME_SET_EDGE_TYPE_UNSPECIFIED\x10\x00\x12.\n)TIME_SET_EDGE_TYPE_NIDIGITAL_VAL_DRIVE_ON\x10\xf0\x15\x12\x30\n+TIME_SET_EDGE_TYPE_NIDIGITAL_VAL_DRIVE_DATA\x10\xf1\x15\x12\x32\n-TIME_SET_EDGE_TYPE_NIDIGITAL_VAL_DRIVE_RETURN\x10\xf2\x15\x12/\n*TIME_SET_EDGE_TYPE_NIDIGITAL_VAL_DRIVE_OFF\x10\xf3\x15\x12\x34\n/TIME_SET_EDGE_TYPE_NIDIGITAL_VAL_COMPARE_STROBE\x10\xf4\x15\x12\x31\n,TIME_SET_EDGE_TYPE_NIDIGITAL_VAL_DRIVE_DATA2\x10\xf5\x15\x12\x33\n.TIME_SET_EDGE_TYPE_NIDIGITAL_VAL_DRIVE_RETURN2\x10\xf6\x15\x12\x35\n0TIME_SET_EDGE_TYPE_NIDIGITAL_VAL_COMPARE_STROBE2\x10\xf7\x15*\xb4\x01\n\x18\x46requencyMeasurementMode\x12*\n&FREQUENCY_MEASUREMENT_MODE_UNSPECIFIED\x10\x00\x12\x34\n/FREQUENCY_MEASUREMENT_MODE_NIDIGITAL_VAL_BANKED\x10\xf4\x1c\x12\x36\n1FREQUENCY_MEASUREMENT_MODE_NIDIGITAL_VAL_PARALLEL\x10\xf5\x1c*\x99\x01\n\x13WriteStaticPinState\x12*\n&WRITE_STATIC_PIN_STATE_NIDIGITAL_VAL_0\x10\x00\x12*\n&WRITE_STATIC_PIN_STATE_NIDIGITAL_VAL_1\x10\x01\x12*\n&WRITE_STATIC_PIN_STATE_NIDIGITAL_VAL_X\x10\x05*\xf3\x0c\n\x1dNiDigitalInt32AttributeValues\x12\x1f\n\x1bNIDIGITAL_INT32_UNSPECIFIED\x10\x00\x12\x31\n,NIDIGITAL_INT32_DIGITAL_EDGE_VAL_RISING_EDGE\x10\x88\x0e\x12\x32\n-NIDIGITAL_INT32_DIGITAL_EDGE_VAL_FALLING_EDGE\x10\x89\x0e\x12:\n5NIDIGITAL_INT32_FREQUENCY_MEASUREMENT_MODE_VAL_BANKED\x10\xf4\x1c\x12<\n7NIDIGITAL_INT32_FREQUENCY_MEASUREMENT_MODE_VAL_PARALLEL\x10\xf5\x1c\x12\x44\n?NIDIGITAL_INT32_HISTORY_RAM_CYCLES_TO_ACQUIRE_VAL_FAILED_CYCLES\x10\xff\x11\x12\x41\n<NIDIGITAL_INT32_HISTORY_RAM_CYCLES_TO_ACQUIRE_VAL_ALL_CYCLES\x10\x80\x12\x12`\nSNIDIGITAL_INT32_HISTORY_RAM_MAX_SAMPLES_TO_ACQUIRE_PER_SITE_VAL_ACQUIRE_ALL_SAMPLES\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12?\n:NIDIGITAL_INT32_HISTORY_RAM_TRIGGER_TYPE_VAL_FIRST_FAILURE\x10\x98\x11\x12>\n9NIDIGITAL_INT32_HISTORY_RAM_TRIGGER_TYPE_VAL_CYCLE_NUMBER\x10\x99\x11\x12?\n:NIDIGITAL_INT32_HISTORY_RAM_TRIGGER_TYPE_VAL_PATTERN_LABEL\x10\x9a\x11\x12\x39\n4NIDIGITAL_INT32_PPMU_APERTURE_TIME_UNITS_VAL_SECONDS\x10\xb4\x10\x12\x45\n@NIDIGITAL_INT32_PPMU_CURRENT_LIMIT_BEHAVIOR_VAL_CURRENT_REGULATE\x10\x9c\x18\x12\x38\n3NIDIGITAL_INT32_PPMU_OUTPUT_FUNCTION_VAL_DC_VOLTAGE\x10\x94\n\x12\x38\n3NIDIGITAL_INT32_PPMU_OUTPUT_FUNCTION_VAL_DC_CURRENT\x10\x95\n\x12\x32\n-NIDIGITAL_INT32_SELECTED_FUNCTION_VAL_DIGITAL\x10\xcc\x08\x12/\n*NIDIGITAL_INT32_SELECTED_FUNCTION_VAL_PPMU\x10\xcd\x08\x12.\n)NIDIGITAL_INT32_SELECTED_FUNCTION_VAL_OFF\x10\xce\x08\x12\x35\n0NIDIGITAL_INT32_SELECTED_FUNCTION_VAL_DISCONNECT\x10\xcf\x08\x12.\n)NIDIGITAL_INT32_SELECTED_FUNCTION_VAL_RIO\x10\xd0\x08\x12=\n8NIDIGITAL_INT32_TDR_ENDPOINT_TERMINATION_VAL_TDR_TO_OPEN\x10\x90\x1c\x12H\nCNIDIGITAL_INT32_TDR_ENDPOINT_TERMINATION_VAL_TDR_TO_SHORT_TO_GROUND\x10\x91\x1c\x12\x35\n0NIDIGITAL_INT32_TERMINATION_MODE_VAL_ACTIVE_LOAD\x10\xb0\t\x12/\n*NIDIGITAL_INT32_TERMINATION_MODE_VAL_VTERM\x10\xb1\t\x12\x30\n+NIDIGITAL_INT32_TERMINATION_MODE_VAL_HIGH_Z\x10\xb2\t\x12*\n%NIDIGITAL_INT32_TRIGGER_TYPE_VAL_NONE\x10\xa4\r\x12\x32\n-NIDIGITAL_INT32_TRIGGER_TYPE_VAL_DIGITAL_EDGE\x10\xa5\r\x12.\n)NIDIGITAL_INT32_TRIGGER_TYPE_VAL_SOFTWARE\x10\xa6\r2\xd0\x85\x01\n\tNiDigital\x12O\n\x04Init\x12\".nidigitalpattern_grpc.InitRequest\x1a#.nidigitalpattern_grpc.InitResponse\x12p\n\x0fInitWithOptions\x12-.nidigitalpattern_grpc.InitWithOptionsRequest\x1a..nidigitalpattern_grpc.InitWithOptionsResponse\x12R\n\x05\x43lose\x12#.nidigitalpattern_grpc.CloseRequest\x1a$.nidigitalpattern_grpc.CloseResponse\x12R\n\x05Reset\x12#.nidigitalpattern_grpc.ResetRequest\x1a$.nidigitalpattern_grpc.ResetResponse\x12\x64\n\x0bResetDevice\x12).nidigitalpattern_grpc.ResetDeviceRequest\x1a*.nidigitalpattern_grpc.ResetDeviceResponse\x12[\n\x08SelfTest\x12&.nidigitalpattern_grpc.SelfTestRequest\x1a\'.nidigitalpattern_grpc.SelfTestResponse\x12[\n\x08GetError\x12&.nidigitalpattern_grpc.GetErrorRequest\x1a\'.nidigitalpattern_grpc.GetErrorResponse\x12\x61\n\nClearError\x12(.nidigitalpattern_grpc.ClearErrorRequest\x1a).nidigitalpattern_grpc.ClearErrorResponse\x12g\n\x0c\x45rrorMessage\x12*.nidigitalpattern_grpc.ErrorMessageRequest\x1a+.nidigitalpattern_grpc.ErrorMessageResponse\x12j\n\rSelfCalibrate\x12+.nidigitalpattern_grpc.SelfCalibrateRequest\x1a,.nidigitalpattern_grpc.SelfCalibrateResponse\x12|\n\x13GetAttributeViInt32\x12\x31.nidigitalpattern_grpc.GetAttributeViInt32Request\x1a\x32.nidigitalpattern_grpc.GetAttributeViInt32Response\x12|\n\x13GetAttributeViInt64\x12\x31.nidigitalpattern_grpc.GetAttributeViInt64Request\x1a\x32.nidigitalpattern_grpc.GetAttributeViInt64Response\x12\x7f\n\x14GetAttributeViReal64\x12\x32.nidigitalpattern_grpc.GetAttributeViReal64Request\x1a\x33.nidigitalpattern_grpc.GetAttributeViReal64Response\x12\x7f\n\x14GetAttributeViString\x12\x32.nidigitalpattern_grpc.GetAttributeViStringRequest\x1a\x33.nidigitalpattern_grpc.GetAttributeViStringResponse\x12\x82\x01\n\x15GetAttributeViSession\x12\x33.nidigitalpattern_grpc.GetAttributeViSessionRequest\x1a\x34.nidigitalpattern_grpc.GetAttributeViSessionResponse\x12\x82\x01\n\x15GetAttributeViBoolean\x12\x33.nidigitalpattern_grpc.GetAttributeViBooleanRequest\x1a\x34.nidigitalpattern_grpc.GetAttributeViBooleanResponse\x12|\n\x13SetAttributeViInt32\x12\x31.nidigitalpattern_grpc.SetAttributeViInt32Request\x1a\x32.nidigitalpattern_grpc.SetAttributeViInt32Response\x12|\n\x13SetAttributeViInt64\x12\x31.nidigitalpattern_grpc.SetAttributeViInt64Request\x1a\x32.nidigitalpattern_grpc.SetAttributeViInt64Response\x12\x7f\n\x14SetAttributeViReal64\x12\x32.nidigitalpattern_grpc.SetAttributeViReal64Request\x1a\x33.nidigitalpattern_grpc.SetAttributeViReal64Response\x12\x7f\n\x14SetAttributeViString\x12\x32.nidigitalpattern_grpc.SetAttributeViStringRequest\x1a\x33.nidigitalpattern_grpc.SetAttributeViStringResponse\x12\x82\x01\n\x15SetAttributeViSession\x12\x33.nidigitalpattern_grpc.SetAttributeViSessionRequest\x1a\x34.nidigitalpattern_grpc.SetAttributeViSessionResponse\x12\x82\x01\n\x15SetAttributeViBoolean\x12\x33.nidigitalpattern_grpc.SetAttributeViBooleanRequest\x1a\x34.nidigitalpattern_grpc.SetAttributeViBooleanResponse\x12m\n\x0eResetAttribute\x12,.nidigitalpattern_grpc.ResetAttributeRequest\x1a-.nidigitalpattern_grpc.ResetAttributeResponse\x12\x61\n\nLoadPinMap\x12(.nidigitalpattern_grpc.LoadPinMapRequest\x1a).nidigitalpattern_grpc.LoadPinMapResponse\x12\x64\n\x0b\x45nableSites\x12).nidigitalpattern_grpc.EnableSitesRequest\x1a*.nidigitalpattern_grpc.EnableSitesResponse\x12g\n\x0c\x44isableSites\x12*.nidigitalpattern_grpc.DisableSitesRequest\x1a+.nidigitalpattern_grpc.DisableSitesResponse\x12j\n\rIsSiteEnabled\x12+.nidigitalpattern_grpc.IsSiteEnabledRequest\x1a,.nidigitalpattern_grpc.IsSiteEnabledResponse\x12g\n\x0c\x43reatePinMap\x12*.nidigitalpattern_grpc.CreatePinMapRequest\x1a+.nidigitalpattern_grpc.CreatePinMapResponse\x12m\n\x0e\x43reatePinGroup\x12,.nidigitalpattern_grpc.CreatePinGroupRequest\x1a-.nidigitalpattern_grpc.CreatePinGroupResponse\x12s\n\x10\x43reateChannelMap\x12..nidigitalpattern_grpc.CreateChannelMapRequest\x1a/.nidigitalpattern_grpc.CreateChannelMapResponse\x12p\n\x0fMapPinToChannel\x12-.nidigitalpattern_grpc.MapPinToChannelRequest\x1a..nidigitalpattern_grpc.MapPinToChannelResponse\x12j\n\rEndChannelMap\x12+.nidigitalpattern_grpc.EndChannelMapRequest\x1a,.nidigitalpattern_grpc.EndChannelMapResponse\x12\x61\n\nGetPinName\x12(.nidigitalpattern_grpc.GetPinNameRequest\x1a).nidigitalpattern_grpc.GetPinNameResponse\x12m\n\x0eGetChannelName\x12,.nidigitalpattern_grpc.GetChannelNameRequest\x1a-.nidigitalpattern_grpc.GetChannelNameResponse\x12m\n\x0eSelectFunction\x12,.nidigitalpattern_grpc.SelectFunctionRequest\x1a-.nidigitalpattern_grpc.SelectFunctionResponse\x12\x61\n\nReadStatic\x12(.nidigitalpattern_grpc.ReadStaticRequest\x1a).nidigitalpattern_grpc.ReadStaticResponse\x12\x64\n\x0bWriteStatic\x12).nidigitalpattern_grpc.WriteStaticRequest\x1a*.nidigitalpattern_grpc.WriteStaticResponse\x12\x94\x01\n\x1b\x43lockGeneratorGenerateClock\x12\x39.nidigitalpattern_grpc.ClockGeneratorGenerateClockRequest\x1a:.nidigitalpattern_grpc.ClockGeneratorGenerateClockResponse\x12\x85\x01\n\x16\x43lockGeneratorInitiate\x12\x34.nidigitalpattern_grpc.ClockGeneratorInitiateRequest\x1a\x35.nidigitalpattern_grpc.ClockGeneratorInitiateResponse\x12|\n\x13\x43lockGeneratorAbort\x12\x31.nidigitalpattern_grpc.ClockGeneratorAbortRequest\x1a\x32.nidigitalpattern_grpc.ClockGeneratorAbortResponse\x12y\n\x12LoadSpecifications\x12\x30.nidigitalpattern_grpc.LoadSpecificationsRequest\x1a\x31.nidigitalpattern_grpc.LoadSpecificationsResponse\x12\x7f\n\x14UnloadSpecifications\x12\x32.nidigitalpattern_grpc.UnloadSpecificationsRequest\x1a\x33.nidigitalpattern_grpc.UnloadSpecificationsResponse\x12\x61\n\nLoadLevels\x12(.nidigitalpattern_grpc.LoadLevelsRequest\x1a).nidigitalpattern_grpc.LoadLevelsResponse\x12\x61\n\nLoadTiming\x12(.nidigitalpattern_grpc.LoadTimingRequest\x1a).nidigitalpattern_grpc.LoadTimingResponse\x12\x7f\n\x14\x41pplyLevelsAndTiming\x12\x32.nidigitalpattern_grpc.ApplyLevelsAndTimingRequest\x1a\x33.nidigitalpattern_grpc.ApplyLevelsAndTimingResponse\x12\x85\x01\n\x16\x43onfigureVoltageLevels\x12\x34.nidigitalpattern_grpc.ConfigureVoltageLevelsRequest\x1a\x35.nidigitalpattern_grpc.ConfigureVoltageLevelsResponse\x12\x8e\x01\n\x19\x43onfigureActiveLoadLevels\x12\x37.nidigitalpattern_grpc.ConfigureActiveLoadLevelsRequest\x1a\x38.nidigitalpattern_grpc.ConfigureActiveLoadLevelsResponse\x12\x8b\x01\n\x18\x43onfigureTerminationMode\x12\x36.nidigitalpattern_grpc.ConfigureTerminationModeRequest\x1a\x37.nidigitalpattern_grpc.ConfigureTerminationModeResponse\x12j\n\rCreateTimeSet\x12+.nidigitalpattern_grpc.CreateTimeSetRequest\x1a,.nidigitalpattern_grpc.CreateTimeSetResponse\x12\x85\x01\n\x16\x43onfigureTimeSetPeriod\x12\x34.nidigitalpattern_grpc.ConfigureTimeSetPeriodRequest\x1a\x35.nidigitalpattern_grpc.ConfigureTimeSetPeriodResponse\x12\x91\x01\n\x1a\x43onfigureTimeSetDriveEdges\x12\x38.nidigitalpattern_grpc.ConfigureTimeSetDriveEdgesRequest\x1a\x39.nidigitalpattern_grpc.ConfigureTimeSetDriveEdgesResponse\x12\xa9\x01\n\"ConfigureTimeSetCompareEdgesStrobe\x12@.nidigitalpattern_grpc.ConfigureTimeSetCompareEdgesStrobeRequest\x1a\x41.nidigitalpattern_grpc.ConfigureTimeSetCompareEdgesStrobeResponse\x12\x94\x01\n\x1b\x43onfigureTimeSetDriveFormat\x12\x39.nidigitalpattern_grpc.ConfigureTimeSetDriveFormatRequest\x1a:.nidigitalpattern_grpc.ConfigureTimeSetDriveFormatResponse\x12v\n\x11\x44\x65leteAllTimeSets\x12/.nidigitalpattern_grpc.DeleteAllTimeSetsRequest\x1a\x30.nidigitalpattern_grpc.DeleteAllTimeSetsResponse\x12\x9d\x01\n\x1e\x43onfigureTimeSetEdgeMultiplier\x12<.nidigitalpattern_grpc.ConfigureTimeSetEdgeMultiplierRequest\x1a=.nidigitalpattern_grpc.ConfigureTimeSetEdgeMultiplierResponse\x12\x97\x01\n\x1c\x43onfigureTimeSetDriveEdges2x\x12:.nidigitalpattern_grpc.ConfigureTimeSetDriveEdges2xRequest\x1a;.nidigitalpattern_grpc.ConfigureTimeSetDriveEdges2xResponse\x12\xaf\x01\n$ConfigureTimeSetCompareEdgesStrobe2x\x12\x42.nidigitalpattern_grpc.ConfigureTimeSetCompareEdgesStrobe2xRequest\x1a\x43.nidigitalpattern_grpc.ConfigureTimeSetCompareEdgesStrobe2xResponse\x12\x7f\n\x14\x43onfigureTimeSetEdge\x12\x32.nidigitalpattern_grpc.ConfigureTimeSetEdgeRequest\x1a\x33.nidigitalpattern_grpc.ConfigureTimeSetEdgeResponse\x12s\n\x10GetTimeSetPeriod\x12..nidigitalpattern_grpc.GetTimeSetPeriodRequest\x1a/.nidigitalpattern_grpc.GetTimeSetPeriodResponse\x12m\n\x0eGetTimeSetEdge\x12,.nidigitalpattern_grpc.GetTimeSetEdgeRequest\x1a-.nidigitalpattern_grpc.GetTimeSetEdgeResponse\x12\x8b\x01\n\x18GetTimeSetEdgeMultiplier\x12\x36.nidigitalpattern_grpc.GetTimeSetEdgeMultiplierRequest\x1a\x37.nidigitalpattern_grpc.GetTimeSetEdgeMultiplierResponse\x12\x82\x01\n\x15GetTimeSetDriveFormat\x12\x33.nidigitalpattern_grpc.GetTimeSetDriveFormatRequest\x1a\x34.nidigitalpattern_grpc.GetTimeSetDriveFormatResponse\x12m\n\x0eGetTimeSetName\x12,.nidigitalpattern_grpc.GetTimeSetNameRequest\x1a-.nidigitalpattern_grpc.GetTimeSetNameResponse\x12L\n\x03TDR\x12!.nidigitalpattern_grpc.TDRRequest\x1a\".nidigitalpattern_grpc.TDRResponse\x12p\n\x0f\x41pplyTDROffsets\x12-.nidigitalpattern_grpc.ApplyTDROffsetsRequest\x1a..nidigitalpattern_grpc.ApplyTDROffsetsResponse\x12\x94\x01\n\x1bPPMUConfigureOutputFunction\x12\x39.nidigitalpattern_grpc.PPMUConfigureOutputFunctionRequest\x1a:.nidigitalpattern_grpc.PPMUConfigureOutputFunctionResponse\x12\x8e\x01\n\x19PPMUConfigureApertureTime\x12\x37.nidigitalpattern_grpc.PPMUConfigureApertureTimeRequest\x1a\x38.nidigitalpattern_grpc.PPMUConfigureApertureTimeResponse\x12\x8e\x01\n\x19PPMUConfigureVoltageLevel\x12\x37.nidigitalpattern_grpc.PPMUConfigureVoltageLevelRequest\x1a\x38.nidigitalpattern_grpc.PPMUConfigureVoltageLevelResponse\x12\x8e\x01\n\x19PPMUConfigureCurrentLimit\x12\x37.nidigitalpattern_grpc.PPMUConfigureCurrentLimitRequest\x1a\x38.nidigitalpattern_grpc.PPMUConfigureCurrentLimitResponse\x12\x9d\x01\n\x1ePPMUConfigureCurrentLimitRange\x12<.nidigitalpattern_grpc.PPMUConfigureCurrentLimitRangeRequest\x1a=.nidigitalpattern_grpc.PPMUConfigureCurrentLimitRangeResponse\x12\x8e\x01\n\x19PPMUConfigureCurrentLevel\x12\x37.nidigitalpattern_grpc.PPMUConfigureCurrentLevelRequest\x1a\x38.nidigitalpattern_grpc.PPMUConfigureCurrentLevelResponse\x12\x9d\x01\n\x1ePPMUConfigureCurrentLevelRange\x12<.nidigitalpattern_grpc.PPMUConfigureCurrentLevelRangeRequest\x1a=.nidigitalpattern_grpc.PPMUConfigureCurrentLevelRangeResponse\x12\x91\x01\n\x1aPPMUConfigureVoltageLimits\x12\x38.nidigitalpattern_grpc.PPMUConfigureVoltageLimitsRequest\x1a\x39.nidigitalpattern_grpc.PPMUConfigureVoltageLimitsResponse\x12\x61\n\nPPMUSource\x12(.nidigitalpattern_grpc.PPMUSourceRequest\x1a).nidigitalpattern_grpc.PPMUSourceResponse\x12\x64\n\x0bPPMUMeasure\x12).nidigitalpattern_grpc.PPMUMeasureRequest\x1a*.nidigitalpattern_grpc.PPMUMeasureResponse\x12\x64\n\x0bLoadPattern\x12).nidigitalpattern_grpc.LoadPatternRequest\x1a*.nidigitalpattern_grpc.LoadPatternResponse\x12v\n\x11UnloadAllPatterns\x12/.nidigitalpattern_grpc.UnloadAllPatternsRequest\x1a\x30.nidigitalpattern_grpc.UnloadAllPatternsResponse\x12|\n\x13\x43onfigureStartLabel\x12\x31.nidigitalpattern_grpc.ConfigureStartLabelRequest\x1a\x32.nidigitalpattern_grpc.ConfigureStartLabelResponse\x12\x91\x01\n\x1a\x43onfigurePatternBurstSites\x12\x38.nidigitalpattern_grpc.ConfigurePatternBurstSitesRequest\x1a\x39.nidigitalpattern_grpc.ConfigurePatternBurstSitesResponse\x12\x7f\n\x14GetPatternPinIndexes\x12\x32.nidigitalpattern_grpc.GetPatternPinIndexesRequest\x1a\x33.nidigitalpattern_grpc.GetPatternPinIndexesResponse\x12v\n\x11GetPatternPinList\x12/.nidigitalpattern_grpc.GetPatternPinListRequest\x1a\x30.nidigitalpattern_grpc.GetPatternPinListResponse\x12m\n\x0eGetPatternName\x12,.nidigitalpattern_grpc.GetPatternNameRequest\x1a-.nidigitalpattern_grpc.GetPatternNameResponse\x12g\n\x0c\x42urstPattern\x12*.nidigitalpattern_grpc.BurstPatternRequest\x1a+.nidigitalpattern_grpc.BurstPatternResponse\x12\x8b\x01\n\x18\x42urstPatternSynchronized\x12\x36.nidigitalpattern_grpc.BurstPatternSynchronizedRequest\x1a\x37.nidigitalpattern_grpc.BurstPatternSynchronizedResponse\x12U\n\x06\x43ommit\x12$.nidigitalpattern_grpc.CommitRequest\x1a%.nidigitalpattern_grpc.CommitResponse\x12[\n\x08Initiate\x12&.nidigitalpattern_grpc.InitiateRequest\x1a\'.nidigitalpattern_grpc.InitiateResponse\x12U\n\x06IsDone\x12$.nidigitalpattern_grpc.IsDoneRequest\x1a%.nidigitalpattern_grpc.IsDoneResponse\x12j\n\rWaitUntilDone\x12+.nidigitalpattern_grpc.WaitUntilDoneRequest\x1a,.nidigitalpattern_grpc.WaitUntilDoneResponse\x12R\n\x05\x41\x62ort\x12#.nidigitalpattern_grpc.AbortRequest\x1a$.nidigitalpattern_grpc.AbortResponse\x12m\n\x0e\x41\x62ortKeepAlive\x12,.nidigitalpattern_grpc.AbortKeepAliveRequest\x1a-.nidigitalpattern_grpc.AbortKeepAliveResponse\x12\xb5\x01\n&ConfigurePatternLabelHistoryRAMTrigger\x12\x44.nidigitalpattern_grpc.ConfigurePatternLabelHistoryRAMTriggerRequest\x1a\x45.nidigitalpattern_grpc.ConfigurePatternLabelHistoryRAMTriggerResponse\x12\xb2\x01\n%ConfigureCycleNumberHistoryRAMTrigger\x12\x43.nidigitalpattern_grpc.ConfigureCycleNumberHistoryRAMTriggerRequest\x1a\x44.nidigitalpattern_grpc.ConfigureCycleNumberHistoryRAMTriggerResponse\x12\xb5\x01\n&ConfigureFirstFailureHistoryRAMTrigger\x12\x44.nidigitalpattern_grpc.ConfigureFirstFailureHistoryRAMTriggerRequest\x1a\x45.nidigitalpattern_grpc.ConfigureFirstFailureHistoryRAMTriggerResponse\x12\xa9\x01\n\"ConfigureHistoryRAMCyclesToAcquire\x12@.nidigitalpattern_grpc.ConfigureHistoryRAMCyclesToAcquireRequest\x1a\x41.nidigitalpattern_grpc.ConfigureHistoryRAMCyclesToAcquireResponse\x12\x8b\x01\n\x18GetHistoryRAMSampleCount\x12\x36.nidigitalpattern_grpc.GetHistoryRAMSampleCountRequest\x1a\x37.nidigitalpattern_grpc.GetHistoryRAMSampleCountResponse\x12\xa0\x01\n\x1f\x46\x65tchHistoryRAMCycleInformation\x12=.nidigitalpattern_grpc.FetchHistoryRAMCycleInformationRequest\x1a>.nidigitalpattern_grpc.FetchHistoryRAMCycleInformationResponse\x12\x94\x01\n\x1b\x46\x65tchHistoryRAMCyclePinData\x12\x39.nidigitalpattern_grpc.FetchHistoryRAMCyclePinDataRequest\x1a:.nidigitalpattern_grpc.FetchHistoryRAMCyclePinDataResponse\x12\x9d\x01\n\x1e\x46\x65tchHistoryRAMScanCycleNumber\x12<.nidigitalpattern_grpc.FetchHistoryRAMScanCycleNumberRequest\x1a=.nidigitalpattern_grpc.FetchHistoryRAMScanCycleNumberResponse\x12\x97\x01\n\x1c\x43reateSourceWaveformParallel\x12:.nidigitalpattern_grpc.CreateSourceWaveformParallelRequest\x1a;.nidigitalpattern_grpc.CreateSourceWaveformParallelResponse\x12\x91\x01\n\x1a\x43reateSourceWaveformSerial\x12\x38.nidigitalpattern_grpc.CreateSourceWaveformSerialRequest\x1a\x39.nidigitalpattern_grpc.CreateSourceWaveformSerialResponse\x12\xa3\x01\n CreateSourceWaveformFromFileTDMS\x12>.nidigitalpattern_grpc.CreateSourceWaveformFromFileTDMSRequest\x1a?.nidigitalpattern_grpc.CreateSourceWaveformFromFileTDMSResponse\x12\xa0\x01\n\x1fWriteSourceWaveformBroadcastU32\x12=.nidigitalpattern_grpc.WriteSourceWaveformBroadcastU32Request\x1a>.nidigitalpattern_grpc.WriteSourceWaveformBroadcastU32Response\x12\xa3\x01\n WriteSourceWaveformSiteUniqueU32\x12>.nidigitalpattern_grpc.WriteSourceWaveformSiteUniqueU32Request\x1a?.nidigitalpattern_grpc.WriteSourceWaveformSiteUniqueU32Response\x12\xac\x01\n#WriteSourceWaveformDataFromFileTDMS\x12\x41.nidigitalpattern_grpc.WriteSourceWaveformDataFromFileTDMSRequest\x1a\x42.nidigitalpattern_grpc.WriteSourceWaveformDataFromFileTDMSResponse\x12\x9a\x01\n\x1d\x43reateCaptureWaveformParallel\x12;.nidigitalpattern_grpc.CreateCaptureWaveformParallelRequest\x1a<.nidigitalpattern_grpc.CreateCaptureWaveformParallelResponse\x12\x94\x01\n\x1b\x43reateCaptureWaveformSerial\x12\x39.nidigitalpattern_grpc.CreateCaptureWaveformSerialRequest\x1a:.nidigitalpattern_grpc.CreateCaptureWaveformSerialResponse\x12\xbb\x01\n(CreateCaptureWaveformFromFileDigicapture\x12\x46.nidigitalpattern_grpc.CreateCaptureWaveformFromFileDigicaptureRequest\x1aG.nidigitalpattern_grpc.CreateCaptureWaveformFromFileDigicaptureResponse\x12\x88\x01\n\x17\x46\x65tchCaptureWaveformU32\x12\x35.nidigitalpattern_grpc.FetchCaptureWaveformU32Request\x1a\x36.nidigitalpattern_grpc.FetchCaptureWaveformU32Response\x12g\n\x0c\x45xportSignal\x12*.nidigitalpattern_grpc.ExportSignalRequest\x1a+.nidigitalpattern_grpc.ExportSignalResponse\x12\xa3\x01\n ConfigureDigitalEdgeStartTrigger\x12>.nidigitalpattern_grpc.ConfigureDigitalEdgeStartTriggerRequest\x1a?.nidigitalpattern_grpc.ConfigureDigitalEdgeStartTriggerResponse\x12\xa6\x01\n!ConfigureSoftwareEdgeStartTrigger\x12?.nidigitalpattern_grpc.ConfigureSoftwareEdgeStartTriggerRequest\x1a@.nidigitalpattern_grpc.ConfigureSoftwareEdgeStartTriggerResponse\x12|\n\x13\x44isableStartTrigger\x12\x31.nidigitalpattern_grpc.DisableStartTriggerRequest\x1a\x32.nidigitalpattern_grpc.DisableStartTriggerResponse\x12\xc1\x01\n*ConfigureDigitalEdgeConditionalJumpTrigger\x12H.nidigitalpattern_grpc.ConfigureDigitalEdgeConditionalJumpTriggerRequest\x1aI.nidigitalpattern_grpc.ConfigureDigitalEdgeConditionalJumpTriggerResponse\x12\xc4\x01\n+ConfigureSoftwareEdgeConditionalJumpTrigger\x12I.nidigitalpattern_grpc.ConfigureSoftwareEdgeConditionalJumpTriggerRequest\x1aJ.nidigitalpattern_grpc.ConfigureSoftwareEdgeConditionalJumpTriggerResponse\x12\x9a\x01\n\x1d\x44isableConditionalJumpTrigger\x12;.nidigitalpattern_grpc.DisableConditionalJumpTriggerRequest\x1a<.nidigitalpattern_grpc.DisableConditionalJumpTriggerResponse\x12\x88\x01\n\x17SendSoftwareEdgeTrigger\x12\x35.nidigitalpattern_grpc.SendSoftwareEdgeTriggerRequest\x1a\x36.nidigitalpattern_grpc.SendSoftwareEdgeTriggerResponse\x12y\n\x12WriteSequencerFlag\x12\x30.nidigitalpattern_grpc.WriteSequencerFlagRequest\x1a\x31.nidigitalpattern_grpc.WriteSequencerFlagResponse\x12\x9d\x01\n\x1eWriteSequencerFlagSynchronized\x12<.nidigitalpattern_grpc.WriteSequencerFlagSynchronizedRequest\x1a=.nidigitalpattern_grpc.WriteSequencerFlagSynchronizedResponse\x12v\n\x11ReadSequencerFlag\x12/.nidigitalpattern_grpc.ReadSequencerFlagRequest\x1a\x30.nidigitalpattern_grpc.ReadSequencerFlagResponse\x12\x85\x01\n\x16WriteSequencerRegister\x12\x34.nidigitalpattern_grpc.WriteSequencerRegisterRequest\x1a\x35.nidigitalpattern_grpc.WriteSequencerRegisterResponse\x12\x82\x01\n\x15ReadSequencerRegister\x12\x33.nidigitalpattern_grpc.ReadSequencerRegisterRequest\x1a\x34.nidigitalpattern_grpc.ReadSequencerRegisterResponse\x12\x91\x01\n\x1a\x45nableMatchFailCombination\x12\x38.nidigitalpattern_grpc.EnableMatchFailCombinationRequest\x1a\x39.nidigitalpattern_grpc.EnableMatchFailCombinationResponse\x12p\n\x0fGetSitePassFail\x12-.nidigitalpattern_grpc.GetSitePassFailRequest\x1a..nidigitalpattern_grpc.GetSitePassFailResponse\x12g\n\x0cGetFailCount\x12*.nidigitalpattern_grpc.GetFailCountRequest\x1a+.nidigitalpattern_grpc.GetFailCountResponse\x12\x94\x01\n\x1bGetPinResultsPinInformation\x12\x39.nidigitalpattern_grpc.GetPinResultsPinInformationRequest\x1a:.nidigitalpattern_grpc.GetPinResultsPinInformationResponse\x12\x8e\x01\n\x19GetSiteResultsSiteNumbers\x12\x37.nidigitalpattern_grpc.GetSiteResultsSiteNumbersRequest\x1a\x38.nidigitalpattern_grpc.GetSiteResultsSiteNumbersResponse\x12\xbb\x01\n(FrequencyCounterConfigureMeasurementTime\x12\x46.nidigitalpattern_grpc.FrequencyCounterConfigureMeasurementTimeRequest\x1aG.nidigitalpattern_grpc.FrequencyCounterConfigureMeasurementTimeResponse\x12\xbb\x01\n(FrequencyCounterConfigureMeasurementMode\x12\x46.nidigitalpattern_grpc.FrequencyCounterConfigureMeasurementModeRequest\x1aG.nidigitalpattern_grpc.FrequencyCounterConfigureMeasurementModeResponse\x12\xa3\x01\n FrequencyCounterMeasureFrequency\x12>.nidigitalpattern_grpc.FrequencyCounterMeasureFrequencyRequest\x1a?.nidigitalpattern_grpc.FrequencyCounterMeasureFrequencyResponse\x12\x8b\x01\n\x18GetChannelNameFromString\x12\x36.nidigitalpattern_grpc.GetChannelNameFromStringRequest\x1a\x37.nidigitalpattern_grpc.GetChannelNameFromStringResponseBG\n\x15\x63om.ni.grpc.nidigitalB\tNiDigitalP\x01\xaa\x02 NationalInstruments.Grpc.Digitalb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nidigitalpattern_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\025com.ni.grpc.nidigitalB\tNiDigitalP\001\252\002 NationalInstruments.Grpc.Digital'
  _INITRESPONSE.fields_by_name['error_message']._options = None
  _INITRESPONSE.fields_by_name['error_message']._serialized_options = b'\030\001'
  _INITWITHOPTIONSRESPONSE.fields_by_name['error_message']._options = None
  _INITWITHOPTIONSRESPONSE.fields_by_name['error_message']._serialized_options = b'\030\001'
  _globals['_NIDIGITALATTRIBUTE']._serialized_start=25129
  _globals['_NIDIGITALATTRIBUTE']._serialized_end=29749
  _globals['_PPMUAPERTURETIMEUNITS']._serialized_start=29751
  _globals['_PPMUAPERTURETIMEUNITS']._serialized_end=29869
  _globals['_BITORDER']._serialized_start=29871
  _globals['_BITORDER']._serialized_end=29988
  _globals['_DIGITALEDGE']._serialized_start=29991
  _globals['_DIGITALEDGE']._serialized_end=30125
  _globals['_PINSTATE']._serialized_start=30128
  _globals['_PINSTATE']._serialized_end=30516
  _globals['_DRIVEFORMAT']._serialized_start=30519
  _globals['_DRIVEFORMAT']._serialized_end=30707
  _globals['_HISTORYRAMCYCLESTOACQUIRE']._serialized_start=30710
  _globals['_HISTORYRAMCYCLESTOACQUIRE']._serialized_end=30909
  _globals['_PPMUCURRENTLIMITBEHAVIOR']._serialized_start=30912
  _globals['_PPMUCURRENTLIMITBEHAVIOR']._serialized_end=31048
  _globals['_PPMUMEASUREMENTTYPE']._serialized_start=31051
  _globals['_PPMUMEASUREMENTTYPE']._serialized_end=31227
  _globals['_PPMUOUTPUTFUNCTION']._serialized_start=31230
  _globals['_PPMUOUTPUTFUNCTION']._serialized_end=31392
  _globals['_SELECTEDFUNCTION']._serialized_start=31395
  _globals['_SELECTEDFUNCTION']._serialized_end=31670
  _globals['_EXPORTSIGNAL']._serialized_start=31673
  _globals['_EXPORTSIGNAL']._serialized_end=31968
  _globals['_SITERESULTTYPE']._serialized_start=31971
  _globals['_SITERESULTTYPE']._serialized_end=32122
  _globals['_SOFTWARETRIGGER']._serialized_start=32125
  _globals['_SOFTWARETRIGGER']._serialized_end=32289
  _globals['_SOURCEDATAMAPPING']._serialized_start=32292
  _globals['_SOURCEDATAMAPPING']._serialized_end=32450
  _globals['_TERMINATIONMODE']._serialized_start=32453
  _globals['_TERMINATIONMODE']._serialized_end=32640
  _globals['_TIMESETEDGETYPE']._serialized_start=32643
  _globals['_TIMESETEDGETYPE']._serialized_end=33108
  _globals['_FREQUENCYMEASUREMENTMODE']._serialized_start=33111
  _globals['_FREQUENCYMEASUREMENTMODE']._serialized_end=33291
  _globals['_WRITESTATICPINSTATE']._serialized_start=33294
  _globals['_WRITESTATICPINSTATE']._serialized_end=33447
  _globals['_NIDIGITALINT32ATTRIBUTEVALUES']._serialized_start=33450
  _globals['_NIDIGITALINT32ATTRIBUTEVALUES']._serialized_end=35101
  _globals['_INITREQUEST']._serialized_start=65
  _globals['_INITREQUEST']._serialized_end=242
  _globals['_INITRESPONSE']._serialized_start=244
  _globals['_INITRESPONSE']._serialized_end=370
  _globals['_INITWITHOPTIONSREQUEST']._serialized_start=373
  _globals['_INITWITHOPTIONSREQUEST']._serialized_end=584
  _globals['_INITWITHOPTIONSRESPONSE']._serialized_start=587
  _globals['_INITWITHOPTIONSRESPONSE']._serialized_end=724
  _globals['_CLOSEREQUEST']._serialized_start=726
  _globals['_CLOSEREQUEST']._serialized_end=776
  _globals['_CLOSERESPONSE']._serialized_start=778
  _globals['_CLOSERESPONSE']._serialized_end=809
  _globals['_RESETREQUEST']._serialized_start=811
  _globals['_RESETREQUEST']._serialized_end=861
  _globals['_RESETRESPONSE']._serialized_start=863
  _globals['_RESETRESPONSE']._serialized_end=894
  _globals['_RESETDEVICEREQUEST']._serialized_start=896
  _globals['_RESETDEVICEREQUEST']._serialized_end=952
  _globals['_RESETDEVICERESPONSE']._serialized_start=954
  _globals['_RESETDEVICERESPONSE']._serialized_end=991
  _globals['_SELFTESTREQUEST']._serialized_start=993
  _globals['_SELFTESTREQUEST']._serialized_end=1046
  _globals['_SELFTESTRESPONSE']._serialized_start=1048
  _globals['_SELFTESTRESPONSE']._serialized_end=1125
  _globals['_GETERRORREQUEST']._serialized_start=1127
  _globals['_GETERRORREQUEST']._serialized_end=1180
  _globals['_GETERRORRESPONSE']._serialized_start=1182
  _globals['_GETERRORRESPONSE']._serialized_end=1263
  _globals['_CLEARERRORREQUEST']._serialized_start=1265
  _globals['_CLEARERRORREQUEST']._serialized_end=1320
  _globals['_CLEARERRORRESPONSE']._serialized_start=1322
  _globals['_CLEARERRORRESPONSE']._serialized_end=1358
  _globals['_ERRORMESSAGEREQUEST']._serialized_start=1360
  _globals['_ERRORMESSAGEREQUEST']._serialized_end=1437
  _globals['_ERRORMESSAGERESPONSE']._serialized_start=1439
  _globals['_ERRORMESSAGERESPONSE']._serialized_end=1500
  _globals['_SELFCALIBRATEREQUEST']._serialized_start=1502
  _globals['_SELFCALIBRATEREQUEST']._serialized_end=1560
  _globals['_SELFCALIBRATERESPONSE']._serialized_start=1562
  _globals['_SELFCALIBRATERESPONSE']._serialized_end=1601
  _globals['_GETATTRIBUTEVIINT32REQUEST']._serialized_start=1604
  _globals['_GETATTRIBUTEVIINT32REQUEST']._serialized_end=1752
  _globals['_GETATTRIBUTEVIINT32RESPONSE']._serialized_start=1754
  _globals['_GETATTRIBUTEVIINT32RESPONSE']._serialized_end=1814
  _globals['_GETATTRIBUTEVIINT64REQUEST']._serialized_start=1817
  _globals['_GETATTRIBUTEVIINT64REQUEST']._serialized_end=1965
  _globals['_GETATTRIBUTEVIINT64RESPONSE']._serialized_start=1967
  _globals['_GETATTRIBUTEVIINT64RESPONSE']._serialized_end=2027
  _globals['_GETATTRIBUTEVIREAL64REQUEST']._serialized_start=2030
  _globals['_GETATTRIBUTEVIREAL64REQUEST']._serialized_end=2179
  _globals['_GETATTRIBUTEVIREAL64RESPONSE']._serialized_start=2181
  _globals['_GETATTRIBUTEVIREAL64RESPONSE']._serialized_end=2242
  _globals['_GETATTRIBUTEVISTRINGREQUEST']._serialized_start=2245
  _globals['_GETATTRIBUTEVISTRINGREQUEST']._serialized_end=2394
  _globals['_GETATTRIBUTEVISTRINGRESPONSE']._serialized_start=2396
  _globals['_GETATTRIBUTEVISTRINGRESPONSE']._serialized_end=2457
  _globals['_GETATTRIBUTEVISESSIONREQUEST']._serialized_start=2460
  _globals['_GETATTRIBUTEVISESSIONREQUEST']._serialized_end=2610
  _globals['_GETATTRIBUTEVISESSIONRESPONSE']._serialized_start=2612
  _globals['_GETATTRIBUTEVISESSIONRESPONSE']._serialized_end=2698
  _globals['_GETATTRIBUTEVIBOOLEANREQUEST']._serialized_start=2701
  _globals['_GETATTRIBUTEVIBOOLEANREQUEST']._serialized_end=2851
  _globals['_GETATTRIBUTEVIBOOLEANRESPONSE']._serialized_start=2853
  _globals['_GETATTRIBUTEVIBOOLEANRESPONSE']._serialized_end=2915
  _globals['_SETATTRIBUTEVIINT32REQUEST']._serialized_start=2918
  _globals['_SETATTRIBUTEVIINT32REQUEST']._serialized_end=3172
  _globals['_SETATTRIBUTEVIINT32RESPONSE']._serialized_start=3174
  _globals['_SETATTRIBUTEVIINT32RESPONSE']._serialized_end=3219
  _globals['_SETATTRIBUTEVIINT64REQUEST']._serialized_start=3222
  _globals['_SETATTRIBUTEVIINT64REQUEST']._serialized_end=3389
  _globals['_SETATTRIBUTEVIINT64RESPONSE']._serialized_start=3391
  _globals['_SETATTRIBUTEVIINT64RESPONSE']._serialized_end=3436
  _globals['_SETATTRIBUTEVIREAL64REQUEST']._serialized_start=3439
  _globals['_SETATTRIBUTEVIREAL64REQUEST']._serialized_end=3607
  _globals['_SETATTRIBUTEVIREAL64RESPONSE']._serialized_start=3609
  _globals['_SETATTRIBUTEVIREAL64RESPONSE']._serialized_end=3655
  _globals['_SETATTRIBUTEVISTRINGREQUEST']._serialized_start=3658
  _globals['_SETATTRIBUTEVISTRINGREQUEST']._serialized_end=3826
  _globals['_SETATTRIBUTEVISTRINGRESPONSE']._serialized_start=3828
  _globals['_SETATTRIBUTEVISTRINGRESPONSE']._serialized_end=3874
  _globals['_SETATTRIBUTEVISESSIONREQUEST']._serialized_start=3877
  _globals['_SETATTRIBUTEVISESSIONREQUEST']._serialized_end=4066
  _globals['_SETATTRIBUTEVISESSIONRESPONSE']._serialized_start=4068
  _globals['_SETATTRIBUTEVISESSIONRESPONSE']._serialized_end=4115
  _globals['_SETATTRIBUTEVIBOOLEANREQUEST']._serialized_start=4118
  _globals['_SETATTRIBUTEVIBOOLEANREQUEST']._serialized_end=4283
  _globals['_SETATTRIBUTEVIBOOLEANRESPONSE']._serialized_start=4285
  _globals['_SETATTRIBUTEVIBOOLEANRESPONSE']._serialized_end=4332
  _globals['_RESETATTRIBUTEREQUEST']._serialized_start=4335
  _globals['_RESETATTRIBUTEREQUEST']._serialized_end=4481
  _globals['_RESETATTRIBUTERESPONSE']._serialized_start=4483
  _globals['_RESETATTRIBUTERESPONSE']._serialized_end=4523
  _globals['_LOADPINMAPREQUEST']._serialized_start=4525
  _globals['_LOADPINMAPREQUEST']._serialized_end=4599
  _globals['_LOADPINMAPRESPONSE']._serialized_start=4601
  _globals['_LOADPINMAPRESPONSE']._serialized_end=4637
  _globals['_ENABLESITESREQUEST']._serialized_start=4639
  _globals['_ENABLESITESREQUEST']._serialized_end=4714
  _globals['_ENABLESITESRESPONSE']._serialized_start=4716
  _globals['_ENABLESITESRESPONSE']._serialized_end=4753
  _globals['_DISABLESITESREQUEST']._serialized_start=4755
  _globals['_DISABLESITESREQUEST']._serialized_end=4831
  _globals['_DISABLESITESRESPONSE']._serialized_start=4833
  _globals['_DISABLESITESRESPONSE']._serialized_end=4871
  _globals['_ISSITEENABLEDREQUEST']._serialized_start=4873
  _globals['_ISSITEENABLEDREQUEST']._serialized_end=4945
  _globals['_ISSITEENABLEDRESPONSE']._serialized_start=4947
  _globals['_ISSITEENABLEDRESPONSE']._serialized_end=5002
  _globals['_CREATEPINMAPREQUEST']._serialized_start=5004
  _globals['_CREATEPINMAPREQUEST']._serialized_end=5108
  _globals['_CREATEPINMAPRESPONSE']._serialized_start=5110
  _globals['_CREATEPINMAPRESPONSE']._serialized_end=5148
  _globals['_CREATEPINGROUPREQUEST']._serialized_start=5150
  _globals['_CREATEPINGROUPREQUEST']._serialized_end=5251
  _globals['_CREATEPINGROUPRESPONSE']._serialized_start=5253
  _globals['_CREATEPINGROUPRESPONSE']._serialized_end=5293
  _globals['_CREATECHANNELMAPREQUEST']._serialized_start=5295
  _globals['_CREATECHANNELMAPREQUEST']._serialized_end=5375
  _globals['_CREATECHANNELMAPRESPONSE']._serialized_start=5377
  _globals['_CREATECHANNELMAPRESPONSE']._serialized_end=5419
  _globals['_MAPPINTOCHANNELREQUEST']._serialized_start=5421
  _globals['_MAPPINTOCHANNELREQUEST']._serialized_end=5525
  _globals['_MAPPINTOCHANNELRESPONSE']._serialized_start=5527
  _globals['_MAPPINTOCHANNELRESPONSE']._serialized_end=5568
  _globals['_ENDCHANNELMAPREQUEST']._serialized_start=5570
  _globals['_ENDCHANNELMAPREQUEST']._serialized_end=5628
  _globals['_ENDCHANNELMAPRESPONSE']._serialized_start=5630
  _globals['_ENDCHANNELMAPRESPONSE']._serialized_end=5669
  _globals['_GETPINNAMEREQUEST']._serialized_start=5671
  _globals['_GETPINNAMEREQUEST']._serialized_end=5745
  _globals['_GETPINNAMERESPONSE']._serialized_start=5747
  _globals['_GETPINNAMERESPONSE']._serialized_end=5797
  _globals['_GETCHANNELNAMEREQUEST']._serialized_start=5799
  _globals['_GETCHANNELNAMEREQUEST']._serialized_end=5873
  _globals['_GETCHANNELNAMERESPONSE']._serialized_start=5875
  _globals['_GETCHANNELNAMERESPONSE']._serialized_end=5929
  _globals['_SELECTFUNCTIONREQUEST']._serialized_start=5932
  _globals['_SELECTFUNCTIONREQUEST']._serialized_end=6115
  _globals['_SELECTFUNCTIONRESPONSE']._serialized_start=6117
  _globals['_SELECTFUNCTIONRESPONSE']._serialized_end=6157
  _globals['_READSTATICREQUEST']._serialized_start=6159
  _globals['_READSTATICREQUEST']._serialized_end=6236
  _globals['_READSTATICRESPONSE']._serialized_start=6238
  _globals['_READSTATICRESPONSE']._serialized_end=6364
  _globals['_WRITESTATICREQUEST']._serialized_start=6367
  _globals['_WRITESTATICREQUEST']._serialized_end=6541
  _globals['_WRITESTATICRESPONSE']._serialized_start=6543
  _globals['_WRITESTATICRESPONSE']._serialized_end=6580
  _globals['_CLOCKGENERATORGENERATECLOCKREQUEST']._serialized_start=6583
  _globals['_CLOCKGENERATORGENERATECLOCKREQUEST']._serialized_end=6729
  _globals['_CLOCKGENERATORGENERATECLOCKRESPONSE']._serialized_start=6731
  _globals['_CLOCKGENERATORGENERATECLOCKRESPONSE']._serialized_end=6784
  _globals['_CLOCKGENERATORINITIATEREQUEST']._serialized_start=6786
  _globals['_CLOCKGENERATORINITIATEREQUEST']._serialized_end=6875
  _globals['_CLOCKGENERATORINITIATERESPONSE']._serialized_start=6877
  _globals['_CLOCKGENERATORINITIATERESPONSE']._serialized_end=6925
  _globals['_CLOCKGENERATORABORTREQUEST']._serialized_start=6927
  _globals['_CLOCKGENERATORABORTREQUEST']._serialized_end=7013
  _globals['_CLOCKGENERATORABORTRESPONSE']._serialized_start=7015
  _globals['_CLOCKGENERATORABORTRESPONSE']._serialized_end=7060
  _globals['_LOADSPECIFICATIONSREQUEST']._serialized_start=7062
  _globals['_LOADSPECIFICATIONSREQUEST']._serialized_end=7144
  _globals['_LOADSPECIFICATIONSRESPONSE']._serialized_start=7146
  _globals['_LOADSPECIFICATIONSRESPONSE']._serialized_end=7190
  _globals['_UNLOADSPECIFICATIONSREQUEST']._serialized_start=7192
  _globals['_UNLOADSPECIFICATIONSREQUEST']._serialized_end=7276
  _globals['_UNLOADSPECIFICATIONSRESPONSE']._serialized_start=7278
  _globals['_UNLOADSPECIFICATIONSRESPONSE']._serialized_end=7324
  _globals['_LOADLEVELSREQUEST']._serialized_start=7326
  _globals['_LOADLEVELSREQUEST']._serialized_end=7400
  _globals['_LOADLEVELSRESPONSE']._serialized_start=7402
  _globals['_LOADLEVELSRESPONSE']._serialized_end=7438
  _globals['_LOADTIMINGREQUEST']._serialized_start=7440
  _globals['_LOADTIMINGREQUEST']._serialized_end=7514
  _globals['_LOADTIMINGRESPONSE']._serialized_start=7516
  _globals['_LOADTIMINGRESPONSE']._serialized_end=7552
  _globals['_APPLYLEVELSANDTIMINGREQUEST']._serialized_start=7555
  _globals['_APPLYLEVELSANDTIMINGREQUEST']._serialized_end=7785
  _globals['_APPLYLEVELSANDTIMINGRESPONSE']._serialized_start=7787
  _globals['_APPLYLEVELSANDTIMINGRESPONSE']._serialized_end=7833
  _globals['_CONFIGUREVOLTAGELEVELSREQUEST']._serialized_start=7836
  _globals['_CONFIGUREVOLTAGELEVELSREQUEST']._serialized_end=7992
  _globals['_CONFIGUREVOLTAGELEVELSRESPONSE']._serialized_start=7994
  _globals['_CONFIGUREVOLTAGELEVELSRESPONSE']._serialized_end=8042
  _globals['_CONFIGUREACTIVELOADLEVELSREQUEST']._serialized_start=8045
  _globals['_CONFIGUREACTIVELOADLEVELSREQUEST']._serialized_end=8177
  _globals['_CONFIGUREACTIVELOADLEVELSRESPONSE']._serialized_start=8179
  _globals['_CONFIGUREACTIVELOADLEVELSRESPONSE']._serialized_end=8230
  _globals['_CONFIGURETERMINATIONMODEREQUEST']._serialized_start=8233
  _globals['_CONFIGURETERMINATIONMODEREQUEST']._serialized_end=8413
  _globals['_CONFIGURETERMINATIONMODERESPONSE']._serialized_start=8415
  _globals['_CONFIGURETERMINATIONMODERESPONSE']._serialized_end=8465
  _globals['_CREATETIMESETREQUEST']._serialized_start=8467
  _globals['_CREATETIMESETREQUEST']._serialized_end=8539
  _globals['_CREATETIMESETRESPONSE']._serialized_start=8541
  _globals['_CREATETIMESETRESPONSE']._serialized_end=8580
  _globals['_CONFIGURETIMESETPERIODREQUEST']._serialized_start=8582
  _globals['_CONFIGURETIMESETPERIODREQUEST']._serialized_end=8688
  _globals['_CONFIGURETIMESETPERIODRESPONSE']._serialized_start=8690
  _globals['_CONFIGURETIMESETPERIODRESPONSE']._serialized_end=8738
  _globals['_CONFIGURETIMESETDRIVEEDGESREQUEST']._serialized_start=8741
  _globals['_CONFIGURETIMESETDRIVEEDGESREQUEST']._serialized_end=9043
  _globals['_CONFIGURETIMESETDRIVEEDGESRESPONSE']._serialized_start=9045
  _globals['_CONFIGURETIMESETDRIVEEDGESRESPONSE']._serialized_end=9097
  _globals['_CONFIGURETIMESETCOMPAREEDGESSTROBEREQUEST']._serialized_start=9100
  _globals['_CONFIGURETIMESETCOMPAREEDGESSTROBEREQUEST']._serialized_end=9241
  _globals['_CONFIGURETIMESETCOMPAREEDGESSTROBERESPONSE']._serialized_start=9243
  _globals['_CONFIGURETIMESETCOMPAREEDGESSTROBERESPONSE']._serialized_end=9303
  _globals['_CONFIGURETIMESETDRIVEFORMATREQUEST']._serialized_start=9306
  _globals['_CONFIGURETIMESETDRIVEFORMATREQUEST']._serialized_end=9528
  _globals['_CONFIGURETIMESETDRIVEFORMATRESPONSE']._serialized_start=9530
  _globals['_CONFIGURETIMESETDRIVEFORMATRESPONSE']._serialized_end=9583
  _globals['_DELETEALLTIMESETSREQUEST']._serialized_start=9585
  _globals['_DELETEALLTIMESETSREQUEST']._serialized_end=9647
  _globals['_DELETEALLTIMESETSRESPONSE']._serialized_start=9649
  _globals['_DELETEALLTIMESETSRESPONSE']._serialized_end=9692
  _globals['_CONFIGURETIMESETEDGEMULTIPLIERREQUEST']._serialized_start=9695
  _globals['_CONFIGURETIMESETEDGEMULTIPLIERREQUEST']._serialized_end=9836
  _globals['_CONFIGURETIMESETEDGEMULTIPLIERRESPONSE']._serialized_start=9838
  _globals['_CONFIGURETIMESETEDGEMULTIPLIERRESPONSE']._serialized_end=9894
  _globals['_CONFIGURETIMESETDRIVEEDGES2XREQUEST']._serialized_start=9897
  _globals['_CONFIGURETIMESETDRIVEEDGES2XREQUEST']._serialized_end=10255
  _globals['_CONFIGURETIMESETDRIVEEDGES2XRESPONSE']._serialized_start=10257
  _globals['_CONFIGURETIMESETDRIVEEDGES2XRESPONSE']._serialized_end=10311
  _globals['_CONFIGURETIMESETCOMPAREEDGESSTROBE2XREQUEST']._serialized_start=10314
  _globals['_CONFIGURETIMESETCOMPAREEDGESSTROBE2XREQUEST']._serialized_end=10479
  _globals['_CONFIGURETIMESETCOMPAREEDGESSTROBE2XRESPONSE']._serialized_start=10481
  _globals['_CONFIGURETIMESETCOMPAREEDGESSTROBE2XRESPONSE']._serialized_end=10543
  _globals['_CONFIGURETIMESETEDGEREQUEST']._serialized_start=10546
  _globals['_CONFIGURETIMESETEDGEREQUEST']._serialized_end=10755
  _globals['_CONFIGURETIMESETEDGERESPONSE']._serialized_start=10757
  _globals['_CONFIGURETIMESETEDGERESPONSE']._serialized_end=10803
  _globals['_GETTIMESETPERIODREQUEST']._serialized_start=10805
  _globals['_GETTIMESETPERIODREQUEST']._serialized_end=10889
  _globals['_GETTIMESETPERIODRESPONSE']._serialized_start=10891
  _globals['_GETTIMESETPERIODRESPONSE']._serialized_end=10949
  _globals['_GETTIMESETEDGEREQUEST']._serialized_start=10952
  _globals['_GETTIMESETEDGEREQUEST']._serialized_end=11136
  _globals['_GETTIMESETEDGERESPONSE']._serialized_start=11138
  _globals['_GETTIMESETEDGERESPONSE']._serialized_end=11192
  _globals['_GETTIMESETEDGEMULTIPLIERREQUEST']._serialized_start=11194
  _globals['_GETTIMESETEDGEMULTIPLIERREQUEST']._serialized_end=11299
  _globals['_GETTIMESETEDGEMULTIPLIERRESPONSE']._serialized_start=11301
  _globals['_GETTIMESETEDGEMULTIPLIERRESPONSE']._serialized_end=11376
  _globals['_GETTIMESETDRIVEFORMATREQUEST']._serialized_start=11378
  _globals['_GETTIMESETDRIVEFORMATREQUEST']._serialized_end=11480
  _globals['_GETTIMESETDRIVEFORMATRESPONSE']._serialized_start=11482
  _globals['_GETTIMESETDRIVEFORMATRESPONSE']._serialized_end=11601
  _globals['_GETTIMESETNAMEREQUEST']._serialized_start=11603
  _globals['_GETTIMESETNAMEREQUEST']._serialized_end=11686
  _globals['_GETTIMESETNAMERESPONSE']._serialized_start=11688
  _globals['_GETTIMESETNAMERESPONSE']._serialized_end=11742
  _globals['_TDRREQUEST']._serialized_start=11744
  _globals['_TDRREQUEST']._serialized_end=11837
  _globals['_TDRRESPONSE']._serialized_start=11839
  _globals['_TDRRESPONSE']._serialized_end=11913
  _globals['_APPLYTDROFFSETSREQUEST']._serialized_start=11915
  _globals['_APPLYTDROFFSETSREQUEST']._serialized_end=12014
  _globals['_APPLYTDROFFSETSRESPONSE']._serialized_start=12016
  _globals['_APPLYTDROFFSETSRESPONSE']._serialized_end=12057
  _globals['_PPMUCONFIGUREOUTPUTFUNCTIONREQUEST']._serialized_start=12060
  _globals['_PPMUCONFIGUREOUTPUTFUNCTIONREQUEST']._serialized_end=12279
  _globals['_PPMUCONFIGUREOUTPUTFUNCTIONRESPONSE']._serialized_start=12281
  _globals['_PPMUCONFIGUREOUTPUTFUNCTIONRESPONSE']._serialized_end=12334
  _globals['_PPMUCONFIGUREAPERTURETIMEREQUEST']._serialized_start=12337
  _globals['_PPMUCONFIGUREAPERTURETIMEREQUEST']._serialized_end=12550
  _globals['_PPMUCONFIGUREAPERTURETIMERESPONSE']._serialized_start=12552
  _globals['_PPMUCONFIGUREAPERTURETIMERESPONSE']._serialized_end=12603
  _globals['_PPMUCONFIGUREVOLTAGELEVELREQUEST']._serialized_start=12605
  _globals['_PPMUCONFIGUREVOLTAGELEVELREQUEST']._serialized_end=12720
  _globals['_PPMUCONFIGUREVOLTAGELEVELRESPONSE']._serialized_start=12722
  _globals['_PPMUCONFIGUREVOLTAGELEVELRESPONSE']._serialized_end=12773
  _globals['_PPMUCONFIGURECURRENTLIMITREQUEST']._serialized_start=12776
  _globals['_PPMUCONFIGURECURRENTLIMITREQUEST']._serialized_end=12993
  _globals['_PPMUCONFIGURECURRENTLIMITRESPONSE']._serialized_start=12995
  _globals['_PPMUCONFIGURECURRENTLIMITRESPONSE']._serialized_end=13046
  _globals['_PPMUCONFIGURECURRENTLIMITRANGEREQUEST']._serialized_start=13048
  _globals['_PPMUCONFIGURECURRENTLIMITRANGEREQUEST']._serialized_end=13160
  _globals['_PPMUCONFIGURECURRENTLIMITRANGERESPONSE']._serialized_start=13162
  _globals['_PPMUCONFIGURECURRENTLIMITRANGERESPONSE']._serialized_end=13218
  _globals['_PPMUCONFIGURECURRENTLEVELREQUEST']._serialized_start=13220
  _globals['_PPMUCONFIGURECURRENTLEVELREQUEST']._serialized_end=13335
  _globals['_PPMUCONFIGURECURRENTLEVELRESPONSE']._serialized_start=13337
  _globals['_PPMUCONFIGURECURRENTLEVELRESPONSE']._serialized_end=13388
  _globals['_PPMUCONFIGURECURRENTLEVELRANGEREQUEST']._serialized_start=13390
  _globals['_PPMUCONFIGURECURRENTLEVELRANGEREQUEST']._serialized_end=13502
  _globals['_PPMUCONFIGURECURRENTLEVELRANGERESPONSE']._serialized_start=13504
  _globals['_PPMUCONFIGURECURRENTLEVELRANGERESPONSE']._serialized_end=13560
  _globals['_PPMUCONFIGUREVOLTAGELIMITSREQUEST']._serialized_start=13563
  _globals['_PPMUCONFIGUREVOLTAGELIMITSREQUEST']._serialized_end=13714
  _globals['_PPMUCONFIGUREVOLTAGELIMITSRESPONSE']._serialized_start=13716
  _globals['_PPMUCONFIGUREVOLTAGELIMITSRESPONSE']._serialized_end=13768
  _globals['_PPMUSOURCEREQUEST']._serialized_start=13770
  _globals['_PPMUSOURCEREQUEST']._serialized_end=13847
  _globals['_PPMUSOURCERESPONSE']._serialized_start=13849
  _globals['_PPMUSOURCERESPONSE']._serialized_end=13885
  _globals['_PPMUMEASUREREQUEST']._serialized_start=13888
  _globals['_PPMUMEASUREREQUEST']._serialized_end=14095
  _globals['_PPMUMEASURERESPONSE']._serialized_start=14097
  _globals['_PPMUMEASURERESPONSE']._serialized_end=14181
  _globals['_LOADPATTERNREQUEST']._serialized_start=14183
  _globals['_LOADPATTERNREQUEST']._serialized_end=14258
  _globals['_LOADPATTERNRESPONSE']._serialized_start=14260
  _globals['_LOADPATTERNRESPONSE']._serialized_end=14297
  _globals['_UNLOADALLPATTERNSREQUEST']._serialized_start=14299
  _globals['_UNLOADALLPATTERNSREQUEST']._serialized_end=14396
  _globals['_UNLOADALLPATTERNSRESPONSE']._serialized_start=14398
  _globals['_UNLOADALLPATTERNSRESPONSE']._serialized_end=14441
  _globals['_CONFIGURESTARTLABELREQUEST']._serialized_start=14443
  _globals['_CONFIGURESTARTLABELREQUEST']._serialized_end=14522
  _globals['_CONFIGURESTARTLABELRESPONSE']._serialized_start=14524
  _globals['_CONFIGURESTARTLABELRESPONSE']._serialized_end=14569
  _globals['_CONFIGUREPATTERNBURSTSITESREQUEST']._serialized_start=14571
  _globals['_CONFIGUREPATTERNBURSTSITESREQUEST']._serialized_end=14661
  _globals['_CONFIGUREPATTERNBURSTSITESRESPONSE']._serialized_start=14663
  _globals['_CONFIGUREPATTERNBURSTSITESRESPONSE']._serialized_end=14715
  _globals['_GETPATTERNPININDEXESREQUEST']._serialized_start=14717
  _globals['_GETPATTERNPININDEXESREQUEST']._serialized_end=14803
  _globals['_GETPATTERNPININDEXESRESPONSE']._serialized_start=14805
  _globals['_GETPATTERNPININDEXESRESPONSE']._serialized_end=14897
  _globals['_GETPATTERNPINLISTREQUEST']._serialized_start=14899
  _globals['_GETPATTERNPINLISTREQUEST']._serialized_end=14982
  _globals['_GETPATTERNPINLISTRESPONSE']._serialized_start=14984
  _globals['_GETPATTERNPINLISTRESPONSE']._serialized_end=15045
  _globals['_GETPATTERNNAMEREQUEST']._serialized_start=15047
  _globals['_GETPATTERNNAMEREQUEST']._serialized_end=15129
  _globals['_GETPATTERNNAMERESPONSE']._serialized_start=15131
  _globals['_GETPATTERNNAMERESPONSE']._serialized_end=15185
  _globals['_BURSTPATTERNREQUEST']._serialized_start=15188
  _globals['_BURSTPATTERNREQUEST']._serialized_end=15360
  _globals['_BURSTPATTERNRESPONSE']._serialized_start=15362
  _globals['_BURSTPATTERNRESPONSE']._serialized_end=15400
  _globals['_BURSTPATTERNSYNCHRONIZEDREQUEST']._serialized_start=15403
  _globals['_BURSTPATTERNSYNCHRONIZEDREQUEST']._serialized_end=15616
  _globals['_BURSTPATTERNSYNCHRONIZEDRESPONSE']._serialized_start=15618
  _globals['_BURSTPATTERNSYNCHRONIZEDRESPONSE']._serialized_end=15668
  _globals['_COMMITREQUEST']._serialized_start=15670
  _globals['_COMMITREQUEST']._serialized_end=15721
  _globals['_COMMITRESPONSE']._serialized_start=15723
  _globals['_COMMITRESPONSE']._serialized_end=15755
  _globals['_INITIATEREQUEST']._serialized_start=15757
  _globals['_INITIATEREQUEST']._serialized_end=15810
  _globals['_INITIATERESPONSE']._serialized_start=15812
  _globals['_INITIATERESPONSE']._serialized_end=15846
  _globals['_ISDONEREQUEST']._serialized_start=15848
  _globals['_ISDONEREQUEST']._serialized_end=15899
  _globals['_ISDONERESPONSE']._serialized_start=15901
  _globals['_ISDONERESPONSE']._serialized_end=15947
  _globals['_WAITUNTILDONEREQUEST']._serialized_start=15949
  _globals['_WAITUNTILDONEREQUEST']._serialized_end=16024
  _globals['_WAITUNTILDONERESPONSE']._serialized_start=16026
  _globals['_WAITUNTILDONERESPONSE']._serialized_end=16065
  _globals['_ABORTREQUEST']._serialized_start=16067
  _globals['_ABORTREQUEST']._serialized_end=16117
  _globals['_ABORTRESPONSE']._serialized_start=16119
  _globals['_ABORTRESPONSE']._serialized_end=16150
  _globals['_ABORTKEEPALIVEREQUEST']._serialized_start=16152
  _globals['_ABORTKEEPALIVEREQUEST']._serialized_end=16211
  _globals['_ABORTKEEPALIVERESPONSE']._serialized_start=16213
  _globals['_ABORTKEEPALIVERESPONSE']._serialized_end=16253
  _globals['_CONFIGUREPATTERNLABELHISTORYRAMTRIGGERREQUEST']._serialized_start=16256
  _globals['_CONFIGUREPATTERNLABELHISTORYRAMTRIGGERREQUEST']._serialized_end=16427
  _globals['_CONFIGUREPATTERNLABELHISTORYRAMTRIGGERRESPONSE']._serialized_start=16429
  _globals['_CONFIGUREPATTERNLABELHISTORYRAMTRIGGERRESPONSE']._serialized_end=16493
  _globals['_CONFIGURECYCLENUMBERHISTORYRAMTRIGGERREQUEST']._serialized_start=16496
  _globals['_CONFIGURECYCLENUMBERHISTORYRAMTRIGGERREQUEST']._serialized_end=16628
  _globals['_CONFIGURECYCLENUMBERHISTORYRAMTRIGGERRESPONSE']._serialized_start=16630
  _globals['_CONFIGURECYCLENUMBERHISTORYRAMTRIGGERRESPONSE']._serialized_end=16693
  _globals['_CONFIGUREFIRSTFAILUREHISTORYRAMTRIGGERREQUEST']._serialized_start=16695
  _globals['_CONFIGUREFIRSTFAILUREHISTORYRAMTRIGGERREQUEST']._serialized_end=16806
  _globals['_CONFIGUREFIRSTFAILUREHISTORYRAMTRIGGERRESPONSE']._serialized_start=16808
  _globals['_CONFIGUREFIRSTFAILUREHISTORYRAMTRIGGERRESPONSE']._serialized_end=16872
  _globals['_CONFIGUREHISTORYRAMCYCLESTOACQUIREREQUEST']._serialized_start=16875
  _globals['_CONFIGUREHISTORYRAMCYCLESTOACQUIREREQUEST']._serialized_end=17092
  _globals['_CONFIGUREHISTORYRAMCYCLESTOACQUIRERESPONSE']._serialized_start=17094
  _globals['_CONFIGUREHISTORYRAMCYCLESTOACQUIRERESPONSE']._serialized_end=17154
  _globals['_GETHISTORYRAMSAMPLECOUNTREQUEST']._serialized_start=17156
  _globals['_GETHISTORYRAMSAMPLECOUNTREQUEST']._serialized_end=17239
  _globals['_GETHISTORYRAMSAMPLECOUNTRESPONSE']._serialized_start=17241
  _globals['_GETHISTORYRAMSAMPLECOUNTRESPONSE']._serialized_end=17313
  _globals['_FETCHHISTORYRAMCYCLEINFORMATIONREQUEST']._serialized_start=17315
  _globals['_FETCHHISTORYRAMCYCLEINFORMATIONREQUEST']._serialized_end=17427
  _globals['_FETCHHISTORYRAMCYCLEINFORMATIONRESPONSE']._serialized_start=17430
  _globals['_FETCHHISTORYRAMCYCLEINFORMATIONRESPONSE']._serialized_end=17603
  _globals['_FETCHHISTORYRAMCYCLEPINDATAREQUEST']._serialized_start=17606
  _globals['_FETCHHISTORYRAMCYCLEPINDATAREQUEST']._serialized_end=17757
  _globals['_FETCHHISTORYRAMCYCLEPINDATARESPONSE']._serialized_start=17760
  _globals['_FETCHHISTORYRAMCYCLEPINDATARESPONSE']._serialized_end=18055
  _globals['_FETCHHISTORYRAMSCANCYCLENUMBERREQUEST']._serialized_start=18057
  _globals['_FETCHHISTORYRAMSCANCYCLENUMBERREQUEST']._serialized_end=18168
  _globals['_FETCHHISTORYRAMSCANCYCLENUMBERRESPONSE']._serialized_start=18170
  _globals['_FETCHHISTORYRAMSCANCYCLENUMBERRESPONSE']._serialized_end=18253
  _globals['_CREATESOURCEWAVEFORMPARALLELREQUEST']._serialized_start=18256
  _globals['_CREATESOURCEWAVEFORMPARALLELREQUEST']._serialized_end=18485
  _globals['_CREATESOURCEWAVEFORMPARALLELRESPONSE']._serialized_start=18487
  _globals['_CREATESOURCEWAVEFORMPARALLELRESPONSE']._serialized_end=18541
  _globals['_CREATESOURCEWAVEFORMSERIALREQUEST']._serialized_start=18544
  _globals['_CREATESOURCEWAVEFORMSERIALREQUEST']._serialized_end=18890
  _globals['_CREATESOURCEWAVEFORMSERIALRESPONSE']._serialized_start=18892
  _globals['_CREATESOURCEWAVEFORMSERIALRESPONSE']._serialized_end=18944
  _globals['_CREATESOURCEWAVEFORMFROMFILETDMSREQUEST']._serialized_start=18947
  _globals['_CREATESOURCEWAVEFORMFROMFILETDMSREQUEST']._serialized_end=19104
  _globals['_CREATESOURCEWAVEFORMFROMFILETDMSRESPONSE']._serialized_start=19106
  _globals['_CREATESOURCEWAVEFORMFROMFILETDMSRESPONSE']._serialized_end=19164
  _globals['_WRITESOURCEWAVEFORMBROADCASTU32REQUEST']._serialized_start=19166
  _globals['_WRITESOURCEWAVEFORMBROADCASTU32REQUEST']._serialized_end=19288
  _globals['_WRITESOURCEWAVEFORMBROADCASTU32RESPONSE']._serialized_start=19290
  _globals['_WRITESOURCEWAVEFORMBROADCASTU32RESPONSE']._serialized_end=19347
  _globals['_WRITESOURCEWAVEFORMSITEUNIQUEU32REQUEST']._serialized_start=19350
  _globals['_WRITESOURCEWAVEFORMSITEUNIQUEU32REQUEST']._serialized_end=19545
  _globals['_WRITESOURCEWAVEFORMSITEUNIQUEU32RESPONSE']._serialized_start=19547
  _globals['_WRITESOURCEWAVEFORMSITEUNIQUEU32RESPONSE']._serialized_end=19605
  _globals['_WRITESOURCEWAVEFORMDATAFROMFILETDMSREQUEST']._serialized_start=19608
  _globals['_WRITESOURCEWAVEFORMDATAFROMFILETDMSREQUEST']._serialized_end=19739
  _globals['_WRITESOURCEWAVEFORMDATAFROMFILETDMSRESPONSE']._serialized_start=19741
  _globals['_WRITESOURCEWAVEFORMDATAFROMFILETDMSRESPONSE']._serialized_end=19802
  _globals['_CREATECAPTUREWAVEFORMPARALLELREQUEST']._serialized_start=19804
  _globals['_CREATECAPTUREWAVEFORMPARALLELREQUEST']._serialized_end=19919
  _globals['_CREATECAPTUREWAVEFORMPARALLELRESPONSE']._serialized_start=19921
  _globals['_CREATECAPTUREWAVEFORMPARALLELRESPONSE']._serialized_end=19976
  _globals['_CREATECAPTUREWAVEFORMSERIALREQUEST']._serialized_start=19979
  _globals['_CREATECAPTUREWAVEFORMSERIALREQUEST']._serialized_end=20211
  _globals['_CREATECAPTUREWAVEFORMSERIALRESPONSE']._serialized_start=20213
  _globals['_CREATECAPTUREWAVEFORMSERIALRESPONSE']._serialized_end=20266
  _globals['_CREATECAPTUREWAVEFORMFROMFILEDIGICAPTUREREQUEST']._serialized_start=20269
  _globals['_CREATECAPTUREWAVEFORMFROMFILEDIGICAPTUREREQUEST']._serialized_end=20405
  _globals['_CREATECAPTUREWAVEFORMFROMFILEDIGICAPTURERESPONSE']._serialized_start=20407
  _globals['_CREATECAPTUREWAVEFORMFROMFILEDIGICAPTURERESPONSE']._serialized_end=20473
  _globals['_FETCHCAPTUREWAVEFORMU32REQUEST']._serialized_start=20476
  _globals['_FETCHCAPTUREWAVEFORMU32REQUEST']._serialized_end=20628
  _globals['_FETCHCAPTUREWAVEFORMU32RESPONSE']._serialized_start=20631
  _globals['_FETCHCAPTUREWAVEFORMU32RESPONSE']._serialized_end=20761
  _globals['_EXPORTSIGNALREQUEST']._serialized_start=20764
  _globals['_EXPORTSIGNALREQUEST']._serialized_end=20965
  _globals['_EXPORTSIGNALRESPONSE']._serialized_start=20967
  _globals['_EXPORTSIGNALRESPONSE']._serialized_end=21005
  _globals['_CONFIGUREDIGITALEDGESTARTTRIGGERREQUEST']._serialized_start=21008
  _globals['_CONFIGUREDIGITALEDGESTARTTRIGGERREQUEST']._serialized_end=21186
  _globals['_CONFIGUREDIGITALEDGESTARTTRIGGERRESPONSE']._serialized_start=21188
  _globals['_CONFIGUREDIGITALEDGESTARTTRIGGERRESPONSE']._serialized_end=21246
  _globals['_CONFIGURESOFTWAREEDGESTARTTRIGGERREQUEST']._serialized_start=21248
  _globals['_CONFIGURESOFTWAREEDGESTARTTRIGGERREQUEST']._serialized_end=21326
  _globals['_CONFIGURESOFTWAREEDGESTARTTRIGGERRESPONSE']._serialized_start=21328
  _globals['_CONFIGURESOFTWAREEDGESTARTTRIGGERRESPONSE']._serialized_end=21387
  _globals['_DISABLESTARTTRIGGERREQUEST']._serialized_start=21389
  _globals['_DISABLESTARTTRIGGERREQUEST']._serialized_end=21453
  _globals['_DISABLESTARTTRIGGERRESPONSE']._serialized_start=21455
  _globals['_DISABLESTARTTRIGGERRESPONSE']._serialized_end=21500
  _globals['_CONFIGUREDIGITALEDGECONDITIONALJUMPTRIGGERREQUEST']._serialized_start=21503
  _globals['_CONFIGUREDIGITALEDGECONDITIONALJUMPTRIGGERREQUEST']._serialized_end=21719
  _globals['_CONFIGUREDIGITALEDGECONDITIONALJUMPTRIGGERRESPONSE']._serialized_start=21721
  _globals['_CONFIGUREDIGITALEDGECONDITIONALJUMPTRIGGERRESPONSE']._serialized_end=21789
  _globals['_CONFIGURESOFTWAREEDGECONDITIONALJUMPTRIGGERREQUEST']._serialized_start=21791
  _globals['_CONFIGURESOFTWAREEDGECONDITIONALJUMPTRIGGERREQUEST']._serialized_end=21907
  _globals['_CONFIGURESOFTWAREEDGECONDITIONALJUMPTRIGGERRESPONSE']._serialized_start=21909
  _globals['_CONFIGURESOFTWAREEDGECONDITIONALJUMPTRIGGERRESPONSE']._serialized_end=21978
  _globals['_DISABLECONDITIONALJUMPTRIGGERREQUEST']._serialized_start=21980
  _globals['_DISABLECONDITIONALJUMPTRIGGERREQUEST']._serialized_end=22082
  _globals['_DISABLECONDITIONALJUMPTRIGGERRESPONSE']._serialized_start=22084
  _globals['_DISABLECONDITIONALJUMPTRIGGERRESPONSE']._serialized_end=22139
  _globals['_SENDSOFTWAREEDGETRIGGERREQUEST']._serialized_start=22142
  _globals['_SENDSOFTWAREEDGETRIGGERREQUEST']._serialized_end=22336
  _globals['_SENDSOFTWAREEDGETRIGGERRESPONSE']._serialized_start=22338
  _globals['_SENDSOFTWAREEDGETRIGGERRESPONSE']._serialized_end=22387
  _globals['_WRITESEQUENCERFLAGREQUEST']._serialized_start=22389
  _globals['_WRITESEQUENCERFLAGREQUEST']._serialized_end=22481
  _globals['_WRITESEQUENCERFLAGRESPONSE']._serialized_start=22483
  _globals['_WRITESEQUENCERFLAGRESPONSE']._serialized_end=22527
  _globals['_WRITESEQUENCERFLAGSYNCHRONIZEDREQUEST']._serialized_start=22530
  _globals['_WRITESEQUENCERFLAGSYNCHRONIZEDREQUEST']._serialized_end=22663
  _globals['_WRITESEQUENCERFLAGSYNCHRONIZEDRESPONSE']._serialized_start=22665
  _globals['_WRITESEQUENCERFLAGSYNCHRONIZEDRESPONSE']._serialized_end=22721
  _globals['_READSEQUENCERFLAGREQUEST']._serialized_start=22723
  _globals['_READSEQUENCERFLAGREQUEST']._serialized_end=22799
  _globals['_READSEQUENCERFLAGRESPONSE']._serialized_start=22801
  _globals['_READSEQUENCERFLAGRESPONSE']._serialized_end=22859
  _globals['_WRITESEQUENCERREGISTERREQUEST']._serialized_start=22861
  _globals['_WRITESEQUENCERREGISTERREQUEST']._serialized_end=22956
  _globals['_WRITESEQUENCERREGISTERRESPONSE']._serialized_start=22958
  _globals['_WRITESEQUENCERREGISTERRESPONSE']._serialized_end=23006
  _globals['_READSEQUENCERREGISTERREQUEST']._serialized_start=23008
  _globals['_READSEQUENCERREGISTERREQUEST']._serialized_end=23087
  _globals['_READSEQUENCERREGISTERRESPONSE']._serialized_start=23089
  _globals['_READSEQUENCERREGISTERRESPONSE']._serialized_end=23151
  _globals['_ENABLEMATCHFAILCOMBINATIONREQUEST']._serialized_start=23154
  _globals['_ENABLEMATCHFAILCOMBINATIONREQUEST']._serialized_end=23300
  _globals['_ENABLEMATCHFAILCOMBINATIONRESPONSE']._serialized_start=23302
  _globals['_ENABLEMATCHFAILCOMBINATIONRESPONSE']._serialized_end=23354
  _globals['_GETSITEPASSFAILREQUEST']._serialized_start=23356
  _globals['_GETSITEPASSFAILREQUEST']._serialized_end=23435
  _globals['_GETSITEPASSFAILRESPONSE']._serialized_start=23437
  _globals['_GETSITEPASSFAILRESPONSE']._serialized_end=23523
  _globals['_GETFAILCOUNTREQUEST']._serialized_start=23525
  _globals['_GETFAILCOUNTREQUEST']._serialized_end=23604
  _globals['_GETFAILCOUNTRESPONSE']._serialized_start=23606
  _globals['_GETFAILCOUNTRESPONSE']._serialized_end=23692
  _globals['_GETPINRESULTSPININFORMATIONREQUEST']._serialized_start=23694
  _globals['_GETPINRESULTSPININFORMATIONREQUEST']._serialized_end=23788
  _globals['_GETPINRESULTSPININFORMATIONRESPONSE']._serialized_start=23791
  _globals['_GETPINRESULTSPININFORMATIONRESPONSE']._serialized_end=23939
  _globals['_GETSITERESULTSSITENUMBERSREQUEST']._serialized_start=23942
  _globals['_GETSITERESULTSSITENUMBERSREQUEST']._serialized_end=24155
  _globals['_GETSITERESULTSSITENUMBERSRESPONSE']._serialized_start=24157
  _globals['_GETSITERESULTSSITENUMBERSRESPONSE']._serialized_end=24263
  _globals['_FREQUENCYCOUNTERCONFIGUREMEASUREMENTTIMEREQUEST']._serialized_start=24266
  _globals['_FREQUENCYCOUNTERCONFIGUREMEASUREMENTTIMEREQUEST']._serialized_end=24399
  _globals['_FREQUENCYCOUNTERCONFIGUREMEASUREMENTTIMERESPONSE']._serialized_start=24401
  _globals['_FREQUENCYCOUNTERCONFIGUREMEASUREMENTTIMERESPONSE']._serialized_end=24467
  _globals['_FREQUENCYCOUNTERCONFIGUREMEASUREMENTMODEREQUEST']._serialized_start=24470
  _globals['_FREQUENCYCOUNTERCONFIGUREMEASUREMENTMODEREQUEST']._serialized_end=24689
  _globals['_FREQUENCYCOUNTERCONFIGUREMEASUREMENTMODERESPONSE']._serialized_start=24691
  _globals['_FREQUENCYCOUNTERCONFIGUREMEASUREMENTMODERESPONSE']._serialized_end=24757
  _globals['_FREQUENCYCOUNTERMEASUREFREQUENCYREQUEST']._serialized_start=24759
  _globals['_FREQUENCYCOUNTERMEASUREFREQUENCYREQUEST']._serialized_end=24858
  _globals['_FREQUENCYCOUNTERMEASUREFREQUENCYRESPONSE']._serialized_start=24860
  _globals['_FREQUENCYCOUNTERMEASUREFREQUENCYRESPONSE']._serialized_end=24971
  _globals['_GETCHANNELNAMEFROMSTRINGREQUEST']._serialized_start=24973
  _globals['_GETCHANNELNAMEFROMSTRINGREQUEST']._serialized_end=25059
  _globals['_GETCHANNELNAMEFROMSTRINGRESPONSE']._serialized_start=25061
  _globals['_GETCHANNELNAMEFROMSTRINGRESPONSE']._serialized_end=25126
  _globals['_NIDIGITAL']._serialized_start=35105
  _globals['_NIDIGITAL']._serialized_end=52209
# @@protoc_insertion_point(module_scope)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidigital/nidigital/nidigitalpattern_pb2_grpc.py sha256=cf9c4ed9bf2987c32dc9a21eeab66fffbb3cea1473c76fcbeb2dc8c484456e37 bytes=226597 -->
## FILE: generated/nidigital/nidigital/nidigitalpattern_pb2_grpc.py

- repository: `ni/nimi-python`
- source_path: `generated/nidigital/nidigital/nidigitalpattern_pb2_grpc.py`
- sha256: `cf9c4ed9bf2987c32dc9a21eeab66fffbb3cea1473c76fcbeb2dc8c484456e37`
- bytes: 226597

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import nidigitalpattern_pb2 as nidigitalpattern__pb2


class NiDigitalStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Init = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/Init',
                request_serializer=nidigitalpattern__pb2.InitRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.InitResponse.FromString,
                )
        self.InitWithOptions = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/InitWithOptions',
                request_serializer=nidigitalpattern__pb2.InitWithOptionsRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.InitWithOptionsResponse.FromString,
                )
        self.Close = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/Close',
                request_serializer=nidigitalpattern__pb2.CloseRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.CloseResponse.FromString,
                )
        self.Reset = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/Reset',
                request_serializer=nidigitalpattern__pb2.ResetRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ResetResponse.FromString,
                )
        self.ResetDevice = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ResetDevice',
                request_serializer=nidigitalpattern__pb2.ResetDeviceRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ResetDeviceResponse.FromString,
                )
        self.SelfTest = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/SelfTest',
                request_serializer=nidigitalpattern__pb2.SelfTestRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.SelfTestResponse.FromString,
                )
        self.GetError = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/GetError',
                request_serializer=nidigitalpattern__pb2.GetErrorRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.GetErrorResponse.FromString,
                )
        self.ClearError = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ClearError',
                request_serializer=nidigitalpattern__pb2.ClearErrorRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ClearErrorResponse.FromString,
                )
        self.ErrorMessage = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ErrorMessage',
                request_serializer=nidigitalpattern__pb2.ErrorMessageRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ErrorMessageResponse.FromString,
                )
        self.SelfCalibrate = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/SelfCalibrate',
                request_serializer=nidigitalpattern__pb2.SelfCalibrateRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.SelfCalibrateResponse.FromString,
                )
        self.GetAttributeViInt32 = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/GetAttributeViInt32',
                request_serializer=nidigitalpattern__pb2.GetAttributeViInt32Request.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.GetAttributeViInt32Response.FromString,
                )
        self.GetAttributeViInt64 = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/GetAttributeViInt64',
                request_serializer=nidigitalpattern__pb2.GetAttributeViInt64Request.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.GetAttributeViInt64Response.FromString,
                )
        self.GetAttributeViReal64 = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/GetAttributeViReal64',
                request_serializer=nidigitalpattern__pb2.GetAttributeViReal64Request.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.GetAttributeViReal64Response.FromString,
                )
        self.GetAttributeViString = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/GetAttributeViString',
                request_serializer=nidigitalpattern__pb2.GetAttributeViStringRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.GetAttributeViStringResponse.FromString,
                )
        self.GetAttributeViSession = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/GetAttributeViSession',
                request_serializer=nidigitalpattern__pb2.GetAttributeViSessionRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.GetAttributeViSessionResponse.FromString,
                )
        self.GetAttributeViBoolean = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/GetAttributeViBoolean',
                request_serializer=nidigitalpattern__pb2.GetAttributeViBooleanRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.GetAttributeViBooleanResponse.FromString,
                )
        self.SetAttributeViInt32 = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/SetAttributeViInt32',
                request_serializer=nidigitalpattern__pb2.SetAttributeViInt32Request.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.SetAttributeViInt32Response.FromString,
                )
        self.SetAttributeViInt64 = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/SetAttributeViInt64',
                request_serializer=nidigitalpattern__pb2.SetAttributeViInt64Request.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.SetAttributeViInt64Response.FromString,
                )
        self.SetAttributeViReal64 = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/SetAttributeViReal64',
                request_serializer=nidigitalpattern__pb2.SetAttributeViReal64Request.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.SetAttributeViReal64Response.FromString,
                )
        self.SetAttributeViString = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/SetAttributeViString',
                request_serializer=nidigitalpattern__pb2.SetAttributeViStringRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.SetAttributeViStringResponse.FromString,
                )
        self.SetAttributeViSession = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/SetAttributeViSession',
                request_serializer=nidigitalpattern__pb2.SetAttributeViSessionRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.SetAttributeViSessionResponse.FromString,
                )
        self.SetAttributeViBoolean = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/SetAttributeViBoolean',
                request_serializer=nidigitalpattern__pb2.SetAttributeViBooleanRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.SetAttributeViBooleanResponse.FromString,
                )
        self.ResetAttribute = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ResetAttribute',
                request_serializer=nidigitalpattern__pb2.ResetAttributeRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ResetAttributeResponse.FromString,
                )
        self.LoadPinMap = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/LoadPinMap',
                request_serializer=nidigitalpattern__pb2.LoadPinMapRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.LoadPinMapResponse.FromString,
                )
        self.EnableSites = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/EnableSites',
                request_serializer=nidigitalpattern__pb2.EnableSitesRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.EnableSitesResponse.FromString,
                )
        self.DisableSites = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/DisableSites',
                request_serializer=nidigitalpattern__pb2.DisableSitesRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.DisableSitesResponse.FromString,
                )
        self.IsSiteEnabled = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/IsSiteEnabled',
                request_serializer=nidigitalpattern__pb2.IsSiteEnabledRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.IsSiteEnabledResponse.FromString,
                )
        self.CreatePinMap = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/CreatePinMap',
                request_serializer=nidigitalpattern__pb2.CreatePinMapRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.CreatePinMapResponse.FromString,
                )
        self.CreatePinGroup = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/CreatePinGroup',
                request_serializer=nidigitalpattern__pb2.CreatePinGroupRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.CreatePinGroupResponse.FromString,
                )
        self.CreateChannelMap = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/CreateChannelMap',
                request_serializer=nidigitalpattern__pb2.CreateChannelMapRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.CreateChannelMapResponse.FromString,
                )
        self.MapPinToChannel = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/MapPinToChannel',
                request_serializer=nidigitalpattern__pb2.MapPinToChannelRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.MapPinToChannelResponse.FromString,
                )
        self.EndChannelMap = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/EndChannelMap',
                request_serializer=nidigitalpattern__pb2.EndChannelMapRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.EndChannelMapResponse.FromString,
                )
        self.GetPinName = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/GetPinName',
                request_serializer=nidigitalpattern__pb2.GetPinNameRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.GetPinNameResponse.FromString,
                )
        self.GetChannelName = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/GetChannelName',
                request_serializer=nidigitalpattern__pb2.GetChannelNameRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.GetChannelNameResponse.FromString,
                )
        self.SelectFunction = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/SelectFunction',
                request_serializer=nidigitalpattern__pb2.SelectFunctionRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.SelectFunctionResponse.FromString,
                )
        self.ReadStatic = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ReadStatic',
                request_serializer=nidigitalpattern__pb2.ReadStaticRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ReadStaticResponse.FromString,
                )
        self.WriteStatic = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/WriteStatic',
                request_serializer=nidigitalpattern__pb2.WriteStaticRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.WriteStaticResponse.FromString,
                )
        self.ClockGeneratorGenerateClock = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ClockGeneratorGenerateClock',
                request_serializer=nidigitalpattern__pb2.ClockGeneratorGenerateClockRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ClockGeneratorGenerateClockResponse.FromString,
                )
        self.ClockGeneratorInitiate = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ClockGeneratorInitiate',
                request_serializer=nidigitalpattern__pb2.ClockGeneratorInitiateRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ClockGeneratorInitiateResponse.FromString,
                )
        self.ClockGeneratorAbort = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ClockGeneratorAbort',
                request_serializer=nidigitalpattern__pb2.ClockGeneratorAbortRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ClockGeneratorAbortResponse.FromString,
                )
        self.LoadSpecifications = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/LoadSpecifications',
                request_serializer=nidigitalpattern__pb2.LoadSpecificationsRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.LoadSpecificationsResponse.FromString,
                )
        self.UnloadSpecifications = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/UnloadSpecifications',
                request_serializer=nidigitalpattern__pb2.UnloadSpecificationsRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.UnloadSpecificationsResponse.FromString,
                )
        self.LoadLevels = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/LoadLevels',
                request_serializer=nidigitalpattern__pb2.LoadLevelsRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.LoadLevelsResponse.FromString,
                )
        self.LoadTiming = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/LoadTiming',
                request_serializer=nidigitalpattern__pb2.LoadTimingRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.LoadTimingResponse.FromString,
                )
        self.ApplyLevelsAndTiming = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ApplyLevelsAndTiming',
                request_serializer=nidigitalpattern__pb2.ApplyLevelsAndTimingRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ApplyLevelsAndTimingResponse.FromString,
                )
        self.ConfigureVoltageLevels = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ConfigureVoltageLevels',
                request_serializer=nidigitalpattern__pb2.ConfigureVoltageLevelsRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ConfigureVoltageLevelsResponse.FromString,
                )
        self.ConfigureActiveLoadLevels = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ConfigureActiveLoadLevels',
                request_serializer=nidigitalpattern__pb2.ConfigureActiveLoadLevelsRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ConfigureActiveLoadLevelsResponse.FromString,
                )
        self.ConfigureTerminationMode = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ConfigureTerminationMode',
                request_serializer=nidigitalpattern__pb2.ConfigureTerminationModeRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ConfigureTerminationModeResponse.FromString,
                )
        self.CreateTimeSet = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/CreateTimeSet',
                request_serializer=nidigitalpattern__pb2.CreateTimeSetRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.CreateTimeSetResponse.FromString,
                )
        self.ConfigureTimeSetPeriod = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ConfigureTimeSetPeriod',
                request_serializer=nidigitalpattern__pb2.ConfigureTimeSetPeriodRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ConfigureTimeSetPeriodResponse.FromString,
                )
        self.ConfigureTimeSetDriveEdges = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ConfigureTimeSetDriveEdges',
                request_serializer=nidigitalpattern__pb2.ConfigureTimeSetDriveEdgesRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ConfigureTimeSetDriveEdgesResponse.FromString,
                )
        self.ConfigureTimeSetCompareEdgesStrobe = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ConfigureTimeSetCompareEdgesStrobe',
                request_serializer=nidigitalpattern__pb2.ConfigureTimeSetCompareEdgesStrobeRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ConfigureTimeSetCompareEdgesStrobeResponse.FromString,
                )
        self.ConfigureTimeSetDriveFormat = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ConfigureTimeSetDriveFormat',
                request_serializer=nidigitalpattern__pb2.ConfigureTimeSetDriveFormatRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ConfigureTimeSetDriveFormatResponse.FromString,
                )
        self.DeleteAllTimeSets = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/DeleteAllTimeSets',
                request_serializer=nidigitalpattern__pb2.DeleteAllTimeSetsRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.DeleteAllTimeSetsResponse.FromString,
                )
        self.ConfigureTimeSetEdgeMultiplier = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ConfigureTimeSetEdgeMultiplier',
                request_serializer=nidigitalpattern__pb2.ConfigureTimeSetEdgeMultiplierRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ConfigureTimeSetEdgeMultiplierResponse.FromString,
                )
        self.ConfigureTimeSetDriveEdges2x = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ConfigureTimeSetDriveEdges2x',
                request_serializer=nidigitalpattern__pb2.ConfigureTimeSetDriveEdges2xRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ConfigureTimeSetDriveEdges2xResponse.FromString,
                )
        self.ConfigureTimeSetCompareEdgesStrobe2x = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ConfigureTimeSetCompareEdgesStrobe2x',
                request_serializer=nidigitalpattern__pb2.ConfigureTimeSetCompareEdgesStrobe2xRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ConfigureTimeSetCompareEdgesStrobe2xResponse.FromString,
                )
        self.ConfigureTimeSetEdge = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ConfigureTimeSetEdge',
                request_serializer=nidigitalpattern__pb2.ConfigureTimeSetEdgeRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ConfigureTimeSetEdgeResponse.FromString,
                )
        self.GetTimeSetPeriod = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/GetTimeSetPeriod',
                request_serializer=nidigitalpattern__pb2.GetTimeSetPeriodRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.GetTimeSetPeriodResponse.FromString,
                )
        self.GetTimeSetEdge = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/GetTimeSetEdge',
                request_serializer=nidigitalpattern__pb2.GetTimeSetEdgeRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.GetTimeSetEdgeResponse.FromString,
                )
        self.GetTimeSetEdgeMultiplier = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/GetTimeSetEdgeMultiplier',
                request_serializer=nidigitalpattern__pb2.GetTimeSetEdgeMultiplierRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.GetTimeSetEdgeMultiplierResponse.FromString,
                )
        self.GetTimeSetDriveFormat = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/GetTimeSetDriveFormat',
                request_serializer=nidigitalpattern__pb2.GetTimeSetDriveFormatRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.GetTimeSetDriveFormatResponse.FromString,
                )
        self.GetTimeSetName = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/GetTimeSetName',
                request_serializer=nidigitalpattern__pb2.GetTimeSetNameRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.GetTimeSetNameResponse.FromString,
                )
        self.TDR = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/TDR',
                request_serializer=nidigitalpattern__pb2.TDRRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.TDRResponse.FromString,
                )
        self.ApplyTDROffsets = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ApplyTDROffsets',
                request_serializer=nidigitalpattern__pb2.ApplyTDROffsetsRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ApplyTDROffsetsResponse.FromString,
                )
        self.PPMUConfigureOutputFunction = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/PPMUConfigureOutputFunction',
                request_serializer=nidigitalpattern__pb2.PPMUConfigureOutputFunctionRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.PPMUConfigureOutputFunctionResponse.FromString,
                )
        self.PPMUConfigureApertureTime = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/PPMUConfigureApertureTime',
                request_serializer=nidigitalpattern__pb2.PPMUConfigureApertureTimeRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.PPMUConfigureApertureTimeResponse.FromString,
                )
        self.PPMUConfigureVoltageLevel = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/PPMUConfigureVoltageLevel',
                request_serializer=nidigitalpattern__pb2.PPMUConfigureVoltageLevelRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.PPMUConfigureVoltageLevelResponse.FromString,
                )
        self.PPMUConfigureCurrentLimit = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/PPMUConfigureCurrentLimit',
                request_serializer=nidigitalpattern__pb2.PPMUConfigureCurrentLimitRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.PPMUConfigureCurrentLimitResponse.FromString,
                )
        self.PPMUConfigureCurrentLimitRange = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/PPMUConfigureCurrentLimitRange',
                request_serializer=nidigitalpattern__pb2.PPMUConfigureCurrentLimitRangeRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.PPMUConfigureCurrentLimitRangeResponse.FromString,
                )
        self.PPMUConfigureCurrentLevel = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/PPMUConfigureCurrentLevel',
                request_serializer=nidigitalpattern__pb2.PPMUConfigureCurrentLevelRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.PPMUConfigureCurrentLevelResponse.FromString,
                )
        self.PPMUConfigureCurrentLevelRange = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/PPMUConfigureCurrentLevelRange',
                request_serializer=nidigitalpattern__pb2.PPMUConfigureCurrentLevelRangeRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.PPMUConfigureCurrentLevelRangeResponse.FromString,
                )
        self.PPMUConfigureVoltageLimits = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/PPMUConfigureVoltageLimits',
                request_serializer=nidigitalpattern__pb2.PPMUConfigureVoltageLimitsRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.PPMUConfigureVoltageLimitsResponse.FromString,
                )
        self.PPMUSource = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/PPMUSource',
                request_serializer=nidigitalpattern__pb2.PPMUSourceRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.PPMUSourceResponse.FromString,
                )
        self.PPMUMeasure = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/PPMUMeasure',
                request_serializer=nidigitalpattern__pb2.PPMUMeasureRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.PPMUMeasureResponse.FromString,
                )
        self.LoadPattern = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/LoadPattern',
                request_serializer=nidigitalpattern__pb2.LoadPatternRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.LoadPatternResponse.FromString,
                )
        self.UnloadAllPatterns = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/UnloadAllPatterns',
                request_serializer=nidigitalpattern__pb2.UnloadAllPatternsRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.UnloadAllPatternsResponse.FromString,
                )
        self.ConfigureStartLabel = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ConfigureStartLabel',
                request_serializer=nidigitalpattern__pb2.ConfigureStartLabelRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ConfigureStartLabelResponse.FromString,
                )
        self.ConfigurePatternBurstSites = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ConfigurePatternBurstSites',
                request_serializer=nidigitalpattern__pb2.ConfigurePatternBurstSitesRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ConfigurePatternBurstSitesResponse.FromString,
                )
        self.GetPatternPinIndexes = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/GetPatternPinIndexes',
                request_serializer=nidigitalpattern__pb2.GetPatternPinIndexesRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.GetPatternPinIndexesResponse.FromString,
                )
        self.GetPatternPinList = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/GetPatternPinList',
                request_serializer=nidigitalpattern__pb2.GetPatternPinListRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.GetPatternPinListResponse.FromString,
                )
        self.GetPatternName = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/GetPatternName',
                request_serializer=nidigitalpattern__pb2.GetPatternNameRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.GetPatternNameResponse.FromString,
                )
        self.BurstPattern = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/BurstPattern',
                request_serializer=nidigitalpattern__pb2.BurstPatternRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.BurstPatternResponse.FromString,
                )
        self.BurstPatternSynchronized = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/BurstPatternSynchronized',
                request_serializer=nidigitalpattern__pb2.BurstPatternSynchronizedRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.BurstPatternSynchronizedResponse.FromString,
                )
        self.Commit = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/Commit',
                request_serializer=nidigitalpattern__pb2.CommitRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.CommitResponse.FromString,
                )
        self.Initiate = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/Initiate',
                request_serializer=nidigitalpattern__pb2.InitiateRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.InitiateResponse.FromString,
                )
        self.IsDone = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/IsDone',
                request_serializer=nidigitalpattern__pb2.IsDoneRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.IsDoneResponse.FromString,
                )
        self.WaitUntilDone = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/WaitUntilDone',
                request_serializer=nidigitalpattern__pb2.WaitUntilDoneRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.WaitUntilDoneResponse.FromString,
                )
        self.Abort = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/Abort',
                request_serializer=nidigitalpattern__pb2.AbortRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.AbortResponse.FromString,
                )
        self.AbortKeepAlive = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/AbortKeepAlive',
                request_serializer=nidigitalpattern__pb2.AbortKeepAliveRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.AbortKeepAliveResponse.FromString,
                )
        self.ConfigurePatternLabelHistoryRAMTrigger = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ConfigurePatternLabelHistoryRAMTrigger',
                request_serializer=nidigitalpattern__pb2.ConfigurePatternLabelHistoryRAMTriggerRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ConfigurePatternLabelHistoryRAMTriggerResponse.FromString,
                )
        self.ConfigureCycleNumberHistoryRAMTrigger = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ConfigureCycleNumberHistoryRAMTrigger',
                request_serializer=nidigitalpattern__pb2.ConfigureCycleNumberHistoryRAMTriggerRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ConfigureCycleNumberHistoryRAMTriggerResponse.FromString,
                )
        self.ConfigureFirstFailureHistoryRAMTrigger = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ConfigureFirstFailureHistoryRAMTrigger',
                request_serializer=nidigitalpattern__pb2.ConfigureFirstFailureHistoryRAMTriggerRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ConfigureFirstFailureHistoryRAMTriggerResponse.FromString,
                )
        self.ConfigureHistoryRAMCyclesToAcquire = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ConfigureHistoryRAMCyclesToAcquire',
                request_serializer=nidigitalpattern__pb2.ConfigureHistoryRAMCyclesToAcquireRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ConfigureHistoryRAMCyclesToAcquireResponse.FromString,
                )
        self.GetHistoryRAMSampleCount = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/GetHistoryRAMSampleCount',
                request_serializer=nidigitalpattern__pb2.GetHistoryRAMSampleCountRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.GetHistoryRAMSampleCountResponse.FromString,
                )
        self.FetchHistoryRAMCycleInformation = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/FetchHistoryRAMCycleInformation',
                request_serializer=nidigitalpattern__pb2.FetchHistoryRAMCycleInformationRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.FetchHistoryRAMCycleInformationResponse.FromString,
                )
        self.FetchHistoryRAMCyclePinData = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/FetchHistoryRAMCyclePinData',
                request_serializer=nidigitalpattern__pb2.FetchHistoryRAMCyclePinDataRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.FetchHistoryRAMCyclePinDataResponse.FromString,
                )
        self.FetchHistoryRAMScanCycleNumber = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/FetchHistoryRAMScanCycleNumber',
                request_serializer=nidigitalpattern__pb2.FetchHistoryRAMScanCycleNumberRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.FetchHistoryRAMScanCycleNumberResponse.FromString,
                )
        self.CreateSourceWaveformParallel = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/CreateSourceWaveformParallel',
                request_serializer=nidigitalpattern__pb2.CreateSourceWaveformParallelRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.CreateSourceWaveformParallelResponse.FromString,
                )
        self.CreateSourceWaveformSerial = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/CreateSourceWaveformSerial',
                request_serializer=nidigitalpattern__pb2.CreateSourceWaveformSerialRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.CreateSourceWaveformSerialResponse.FromString,
                )
        self.CreateSourceWaveformFromFileTDMS = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/CreateSourceWaveformFromFileTDMS',
                request_serializer=nidigitalpattern__pb2.CreateSourceWaveformFromFileTDMSRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.CreateSourceWaveformFromFileTDMSResponse.FromString,
                )
        self.WriteSourceWaveformBroadcastU32 = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/WriteSourceWaveformBroadcastU32',
                request_serializer=nidigitalpattern__pb2.WriteSourceWaveformBroadcastU32Request.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.WriteSourceWaveformBroadcastU32Response.FromString,
                )
        self.WriteSourceWaveformSiteUniqueU32 = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/WriteSourceWaveformSiteUniqueU32',
                request_serializer=nidigitalpattern__pb2.WriteSourceWaveformSiteUniqueU32Request.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.WriteSourceWaveformSiteUniqueU32Response.FromString,
                )
        self.WriteSourceWaveformDataFromFileTDMS = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/WriteSourceWaveformDataFromFileTDMS',
                request_serializer=nidigitalpattern__pb2.WriteSourceWaveformDataFromFileTDMSRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.WriteSourceWaveformDataFromFileTDMSResponse.FromString,
                )
        self.CreateCaptureWaveformParallel = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/CreateCaptureWaveformParallel',
                request_serializer=nidigitalpattern__pb2.CreateCaptureWaveformParallelRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.CreateCaptureWaveformParallelResponse.FromString,
                )
        self.CreateCaptureWaveformSerial = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/CreateCaptureWaveformSerial',
                request_serializer=nidigitalpattern__pb2.CreateCaptureWaveformSerialRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.CreateCaptureWaveformSerialResponse.FromString,
                )
        self.CreateCaptureWaveformFromFileDigicapture = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/CreateCaptureWaveformFromFileDigicapture',
                request_serializer=nidigitalpattern__pb2.CreateCaptureWaveformFromFileDigicaptureRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.CreateCaptureWaveformFromFileDigicaptureResponse.FromString,
                )
        self.FetchCaptureWaveformU32 = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/FetchCaptureWaveformU32',
                request_serializer=nidigitalpattern__pb2.FetchCaptureWaveformU32Request.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.FetchCaptureWaveformU32Response.FromString,
                )
        self.ExportSignal = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ExportSignal',
                request_serializer=nidigitalpattern__pb2.ExportSignalRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ExportSignalResponse.FromString,
                )
        self.ConfigureDigitalEdgeStartTrigger = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ConfigureDigitalEdgeStartTrigger',
                request_serializer=nidigitalpattern__pb2.ConfigureDigitalEdgeStartTriggerRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ConfigureDigitalEdgeStartTriggerResponse.FromString,
                )
        self.ConfigureSoftwareEdgeStartTrigger = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ConfigureSoftwareEdgeStartTrigger',
                request_serializer=nidigitalpattern__pb2.ConfigureSoftwareEdgeStartTriggerRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ConfigureSoftwareEdgeStartTriggerResponse.FromString,
                )
        self.DisableStartTrigger = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/DisableStartTrigger',
                request_serializer=nidigitalpattern__pb2.DisableStartTriggerRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.DisableStartTriggerResponse.FromString,
                )
        self.ConfigureDigitalEdgeConditionalJumpTrigger = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ConfigureDigitalEdgeConditionalJumpTrigger',
                request_serializer=nidigitalpattern__pb2.ConfigureDigitalEdgeConditionalJumpTriggerRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ConfigureDigitalEdgeConditionalJumpTriggerResponse.FromString,
                )
        self.ConfigureSoftwareEdgeConditionalJumpTrigger = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ConfigureSoftwareEdgeConditionalJumpTrigger',
                request_serializer=nidigitalpattern__pb2.ConfigureSoftwareEdgeConditionalJumpTriggerRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ConfigureSoftwareEdgeConditionalJumpTriggerResponse.FromString,
                )
        self.DisableConditionalJumpTrigger = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/DisableConditionalJumpTrigger',
                request_serializer=nidigitalpattern__pb2.DisableConditionalJumpTriggerRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.DisableConditionalJumpTriggerResponse.FromString,
                )
        self.SendSoftwareEdgeTrigger = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/SendSoftwareEdgeTrigger',
                request_serializer=nidigitalpattern__pb2.SendSoftwareEdgeTriggerRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.SendSoftwareEdgeTriggerResponse.FromString,
                )
        self.WriteSequencerFlag = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/WriteSequencerFlag',
                request_serializer=nidigitalpattern__pb2.WriteSequencerFlagRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.WriteSequencerFlagResponse.FromString,
                )
        self.WriteSequencerFlagSynchronized = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/WriteSequencerFlagSynchronized',
                request_serializer=nidigitalpattern__pb2.WriteSequencerFlagSynchronizedRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.WriteSequencerFlagSynchronizedResponse.FromString,
                )
        self.ReadSequencerFlag = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ReadSequencerFlag',
                request_serializer=nidigitalpattern__pb2.ReadSequencerFlagRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ReadSequencerFlagResponse.FromString,
                )
        self.WriteSequencerRegister = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/WriteSequencerRegister',
                request_serializer=nidigitalpattern__pb2.WriteSequencerRegisterRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.WriteSequencerRegisterResponse.FromString,
                )
        self.ReadSequencerRegister = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/ReadSequencerRegister',
                request_serializer=nidigitalpattern__pb2.ReadSequencerRegisterRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.ReadSequencerRegisterResponse.FromString,
                )
        self.EnableMatchFailCombination = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/EnableMatchFailCombination',
                request_serializer=nidigitalpattern__pb2.EnableMatchFailCombinationRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.EnableMatchFailCombinationResponse.FromString,
                )
        self.GetSitePassFail = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/GetSitePassFail',
                request_serializer=nidigitalpattern__pb2.GetSitePassFailRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.GetSitePassFailResponse.FromString,
                )
        self.GetFailCount = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/GetFailCount',
                request_serializer=nidigitalpattern__pb2.GetFailCountRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.GetFailCountResponse.FromString,
                )
        self.GetPinResultsPinInformation = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/GetPinResultsPinInformation',
                request_serializer=nidigitalpattern__pb2.GetPinResultsPinInformationRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.GetPinResultsPinInformationResponse.FromString,
                )
        self.GetSiteResultsSiteNumbers = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/GetSiteResultsSiteNumbers',
                request_serializer=nidigitalpattern__pb2.GetSiteResultsSiteNumbersRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.GetSiteResultsSiteNumbersResponse.FromString,
                )
        self.FrequencyCounterConfigureMeasurementTime = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/FrequencyCounterConfigureMeasurementTime',
                request_serializer=nidigitalpattern__pb2.FrequencyCounterConfigureMeasurementTimeRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.FrequencyCounterConfigureMeasurementTimeResponse.FromString,
                )
        self.FrequencyCounterConfigureMeasurementMode = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/FrequencyCounterConfigureMeasurementMode',
                request_serializer=nidigitalpattern__pb2.FrequencyCounterConfigureMeasurementModeRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.FrequencyCounterConfigureMeasurementModeResponse.FromString,
                )
        self.FrequencyCounterMeasureFrequency = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/FrequencyCounterMeasureFrequency',
                request_serializer=nidigitalpattern__pb2.FrequencyCounterMeasureFrequencyRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.FrequencyCounterMeasureFrequencyResponse.FromString,
                )
        self.GetChannelNameFromString = channel.unary_unary(
                '/nidigitalpattern_grpc.NiDigital/GetChannelNameFromString',
                request_serializer=nidigitalpattern__pb2.GetChannelNameFromStringRequest.SerializeToString,
                response_deserializer=nidigitalpattern__pb2.GetChannelNameFromStringResponse.FromString,
                )


class NiDigitalServicer(object):
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

    def Reset(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetDevice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SelfTest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetError(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearError(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ErrorMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SelfCalibrate(self, request, context):
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

    def GetAttributeViString(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttributeViSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttributeViBoolean(self, request, context):
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

    def SetAttributeViSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAttributeViBoolean(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetAttribute(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoadPinMap(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnableSites(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableSites(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IsSiteEnabled(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreatePinMap(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreatePinGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateChannelMap(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MapPinToChannel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EndChannelMap(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPinName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetChannelName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SelectFunction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadStatic(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteStatic(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClockGeneratorGenerateClock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClockGeneratorInitiate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClockGeneratorAbort(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoadSpecifications(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnloadSpecifications(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoadLevels(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoadTiming(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ApplyLevelsAndTiming(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureVoltageLevels(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureActiveLoadLevels(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureTerminationMode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateTimeSet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureTimeSetPeriod(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureTimeSetDriveEdges(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureTimeSetCompareEdgesStrobe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureTimeSetDriveFormat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAllTimeSets(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureTimeSetEdgeMultiplier(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureTimeSetDriveEdges2x(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureTimeSetCompareEdgesStrobe2x(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureTimeSetEdge(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTimeSetPeriod(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTimeSetEdge(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTimeSetEdgeMultiplier(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTimeSetDriveFormat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTimeSetName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TDR(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ApplyTDROffsets(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PPMUConfigureOutputFunction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PPMUConfigureApertureTime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PPMUConfigureVoltageLevel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PPMUConfigureCurrentLimit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PPMUConfigureCurrentLimitRange(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PPMUConfigureCurrentLevel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PPMUConfigureCurrentLevelRange(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PPMUConfigureVoltageLimits(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PPMUSource(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PPMUMeasure(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoadPattern(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnloadAllPatterns(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureStartLabel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigurePatternBurstSites(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPatternPinIndexes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPatternPinList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPatternName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BurstPattern(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BurstPatternSynchronized(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Commit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Initiate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IsDone(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WaitUntilDone(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Abort(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AbortKeepAlive(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigurePatternLabelHistoryRAMTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureCycleNumberHistoryRAMTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureFirstFailureHistoryRAMTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureHistoryRAMCyclesToAcquire(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetHistoryRAMSampleCount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FetchHistoryRAMCycleInformation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FetchHistoryRAMCyclePinData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FetchHistoryRAMScanCycleNumber(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateSourceWaveformParallel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateSourceWaveformSerial(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateSourceWaveformFromFileTDMS(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteSourceWaveformBroadcastU32(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteSourceWaveformSiteUniqueU32(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteSourceWaveformDataFromFileTDMS(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCaptureWaveformParallel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCaptureWaveformSerial(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCaptureWaveformFromFileDigicapture(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FetchCaptureWaveformU32(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExportSignal(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureDigitalEdgeStartTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureSoftwareEdgeStartTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableStartTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureDigitalEdgeConditionalJumpTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureSoftwareEdgeConditionalJumpTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableConditionalJumpTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendSoftwareEdgeTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteSequencerFlag(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteSequencerFlagSynchronized(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadSequencerFlag(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteSequencerRegister(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadSequencerRegister(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnableMatchFailCombination(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSitePassFail(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFailCount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPinResultsPinInformation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSiteResultsSiteNumbers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FrequencyCounterConfigureMeasurementTime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FrequencyCounterConfigureMeasurementMode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FrequencyCounterMeasureFrequency(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetChannelNameFromString(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NiDigitalServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Init': grpc.unary_unary_rpc_method_handler(
                    servicer.Init,
                    request_deserializer=nidigitalpattern__pb2.InitRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.InitResponse.SerializeToString,
            ),
            'InitWithOptions': grpc.unary_unary_rpc_method_handler(
                    servicer.InitWithOptions,
                    request_deserializer=nidigitalpattern__pb2.InitWithOptionsRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.InitWithOptionsResponse.SerializeToString,
            ),
            'Close': grpc.unary_unary_rpc_method_handler(
                    servicer.Close,
                    request_deserializer=nidigitalpattern__pb2.CloseRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.CloseResponse.SerializeToString,
            ),
            'Reset': grpc.unary_unary_rpc_method_handler(
                    servicer.Reset,
                    request_deserializer=nidigitalpattern__pb2.ResetRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ResetResponse.SerializeToString,
            ),
            'ResetDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetDevice,
                    request_deserializer=nidigitalpattern__pb2.ResetDeviceRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ResetDeviceResponse.SerializeToString,
            ),
            'SelfTest': grpc.unary_unary_rpc_method_handler(
                    servicer.SelfTest,
                    request_deserializer=nidigitalpattern__pb2.SelfTestRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.SelfTestResponse.SerializeToString,
            ),
            'GetError': grpc.unary_unary_rpc_method_handler(
                    servicer.GetError,
                    request_deserializer=nidigitalpattern__pb2.GetErrorRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.GetErrorResponse.SerializeToString,
            ),
            'ClearError': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearError,
                    request_deserializer=nidigitalpattern__pb2.ClearErrorRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ClearErrorResponse.SerializeToString,
            ),
            'ErrorMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.ErrorMessage,
                    request_deserializer=nidigitalpattern__pb2.ErrorMessageRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ErrorMessageResponse.SerializeToString,
            ),
            'SelfCalibrate': grpc.unary_unary_rpc_method_handler(
                    servicer.SelfCalibrate,
                    request_deserializer=nidigitalpattern__pb2.SelfCalibrateRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.SelfCalibrateResponse.SerializeToString,
            ),
            'GetAttributeViInt32': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViInt32,
                    request_deserializer=nidigitalpattern__pb2.GetAttributeViInt32Request.FromString,
                    response_serializer=nidigitalpattern__pb2.GetAttributeViInt32Response.SerializeToString,
            ),
            'GetAttributeViInt64': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViInt64,
                    request_deserializer=nidigitalpattern__pb2.GetAttributeViInt64Request.FromString,
                    response_serializer=nidigitalpattern__pb2.GetAttributeViInt64Response.SerializeToString,
            ),
            'GetAttributeViReal64': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViReal64,
                    request_deserializer=nidigitalpattern__pb2.GetAttributeViReal64Request.FromString,
                    response_serializer=nidigitalpattern__pb2.GetAttributeViReal64Response.SerializeToString,
            ),
            'GetAttributeViString': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViString,
                    request_deserializer=nidigitalpattern__pb2.GetAttributeViStringRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.GetAttributeViStringResponse.SerializeToString,
            ),
            'GetAttributeViSession': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViSession,
                    request_deserializer=nidigitalpattern__pb2.GetAttributeViSessionRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.GetAttributeViSessionResponse.SerializeToString,
            ),
            'GetAttributeViBoolean': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViBoolean,
                    request_deserializer=nidigitalpattern__pb2.GetAttributeViBooleanRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.GetAttributeViBooleanResponse.SerializeToString,
            ),
            'SetAttributeViInt32': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttributeViInt32,
                    request_deserializer=nidigitalpattern__pb2.SetAttributeViInt32Request.FromString,
                    response_serializer=nidigitalpattern__pb2.SetAttributeViInt32Response.SerializeToString,
            ),
            'SetAttributeViInt64': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttributeViInt64,
                    request_deserializer=nidigitalpattern__pb2.SetAttributeViInt64Request.FromString,
                    response_serializer=nidigitalpattern__pb2.SetAttributeViInt64Response.SerializeToString,
            ),
            'SetAttributeViReal64': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttributeViReal64,
                    request_deserializer=nidigitalpattern__pb2.SetAttributeViReal64Request.FromString,
                    response_serializer=nidigitalpattern__pb2.SetAttributeViReal64Response.SerializeToString,
            ),
            'SetAttributeViString': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttributeViString,
                    request_deserializer=nidigitalpattern__pb2.SetAttributeViStringRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.SetAttributeViStringResponse.SerializeToString,
            ),
            'SetAttributeViSession': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttributeViSession,
                    request_deserializer=nidigitalpattern__pb2.SetAttributeViSessionRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.SetAttributeViSessionResponse.SerializeToString,
            ),
            'SetAttributeViBoolean': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttributeViBoolean,
                    request_deserializer=nidigitalpattern__pb2.SetAttributeViBooleanRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.SetAttributeViBooleanResponse.SerializeToString,
            ),
            'ResetAttribute': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetAttribute,
                    request_deserializer=nidigitalpattern__pb2.ResetAttributeRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ResetAttributeResponse.SerializeToString,
            ),
            'LoadPinMap': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadPinMap,
                    request_deserializer=nidigitalpattern__pb2.LoadPinMapRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.LoadPinMapResponse.SerializeToString,
            ),
            'EnableSites': grpc.unary_unary_rpc_method_handler(
                    servicer.EnableSites,
                    request_deserializer=nidigitalpattern__pb2.EnableSitesRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.EnableSitesResponse.SerializeToString,
            ),
            'DisableSites': grpc.unary_unary_rpc_method_handler(
                    servicer.DisableSites,
                    request_deserializer=nidigitalpattern__pb2.DisableSitesRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.DisableSitesResponse.SerializeToString,
            ),
            'IsSiteEnabled': grpc.unary_unary_rpc_method_handler(
                    servicer.IsSiteEnabled,
                    request_deserializer=nidigitalpattern__pb2.IsSiteEnabledRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.IsSiteEnabledResponse.SerializeToString,
            ),
            'CreatePinMap': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePinMap,
                    request_deserializer=nidigitalpattern__pb2.CreatePinMapRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.CreatePinMapResponse.SerializeToString,
            ),
            'CreatePinGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePinGroup,
                    request_deserializer=nidigitalpattern__pb2.CreatePinGroupRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.CreatePinGroupResponse.SerializeToString,
            ),
            'CreateChannelMap': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateChannelMap,
                    request_deserializer=nidigitalpattern__pb2.CreateChannelMapRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.CreateChannelMapResponse.SerializeToString,
            ),
            'MapPinToChannel': grpc.unary_unary_rpc_method_handler(
                    servicer.MapPinToChannel,
                    request_deserializer=nidigitalpattern__pb2.MapPinToChannelRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.MapPinToChannelResponse.SerializeToString,
            ),
            'EndChannelMap': grpc.unary_unary_rpc_method_handler(
                    servicer.EndChannelMap,
                    request_deserializer=nidigitalpattern__pb2.EndChannelMapRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.EndChannelMapResponse.SerializeToString,
            ),
            'GetPinName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPinName,
                    request_deserializer=nidigitalpattern__pb2.GetPinNameRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.GetPinNameResponse.SerializeToString,
            ),
            'GetChannelName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetChannelName,
                    request_deserializer=nidigitalpattern__pb2.GetChannelNameRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.GetChannelNameResponse.SerializeToString,
            ),
            'SelectFunction': grpc.unary_unary_rpc_method_handler(
                    servicer.SelectFunction,
                    request_deserializer=nidigitalpattern__pb2.SelectFunctionRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.SelectFunctionResponse.SerializeToString,
            ),
            'ReadStatic': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadStatic,
                    request_deserializer=nidigitalpattern__pb2.ReadStaticRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ReadStaticResponse.SerializeToString,
            ),
            'WriteStatic': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteStatic,
                    request_deserializer=nidigitalpattern__pb2.WriteStaticRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.WriteStaticResponse.SerializeToString,
            ),
            'ClockGeneratorGenerateClock': grpc.unary_unary_rpc_method_handler(
                    servicer.ClockGeneratorGenerateClock,
                    request_deserializer=nidigitalpattern__pb2.ClockGeneratorGenerateClockRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ClockGeneratorGenerateClockResponse.SerializeToString,
            ),
            'ClockGeneratorInitiate': grpc.unary_unary_rpc_method_handler(
                    servicer.ClockGeneratorInitiate,
                    request_deserializer=nidigitalpattern__pb2.ClockGeneratorInitiateRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ClockGeneratorInitiateResponse.SerializeToString,
            ),
            'ClockGeneratorAbort': grpc.unary_unary_rpc_method_handler(
                    servicer.ClockGeneratorAbort,
                    request_deserializer=nidigitalpattern__pb2.ClockGeneratorAbortRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ClockGeneratorAbortResponse.SerializeToString,
            ),
            'LoadSpecifications': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadSpecifications,
                    request_deserializer=nidigitalpattern__pb2.LoadSpecificationsRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.LoadSpecificationsResponse.SerializeToString,
            ),
            'UnloadSpecifications': grpc.unary_unary_rpc_method_handler(
                    servicer.UnloadSpecifications,
                    request_deserializer=nidigitalpattern__pb2.UnloadSpecificationsRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.UnloadSpecificationsResponse.SerializeToString,
            ),
            'LoadLevels': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadLevels,
                    request_deserializer=nidigitalpattern__pb2.LoadLevelsRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.LoadLevelsResponse.SerializeToString,
            ),
            'LoadTiming': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadTiming,
                    request_deserializer=nidigitalpattern__pb2.LoadTimingRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.LoadTimingResponse.SerializeToString,
            ),
            'ApplyLevelsAndTiming': grpc.unary_unary_rpc_method_handler(
                    servicer.ApplyLevelsAndTiming,
                    request_deserializer=nidigitalpattern__pb2.ApplyLevelsAndTimingRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ApplyLevelsAndTimingResponse.SerializeToString,
            ),
            'ConfigureVoltageLevels': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureVoltageLevels,
                    request_deserializer=nidigitalpattern__pb2.ConfigureVoltageLevelsRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ConfigureVoltageLevelsResponse.SerializeToString,
            ),
            'ConfigureActiveLoadLevels': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureActiveLoadLevels,
                    request_deserializer=nidigitalpattern__pb2.ConfigureActiveLoadLevelsRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ConfigureActiveLoadLevelsResponse.SerializeToString,
            ),
            'ConfigureTerminationMode': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureTerminationMode,
                    request_deserializer=nidigitalpattern__pb2.ConfigureTerminationModeRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ConfigureTerminationModeResponse.SerializeToString,
            ),
            'CreateTimeSet': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTimeSet,
                    request_deserializer=nidigitalpattern__pb2.CreateTimeSetRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.CreateTimeSetResponse.SerializeToString,
            ),
            'ConfigureTimeSetPeriod': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureTimeSetPeriod,
                    request_deserializer=nidigitalpattern__pb2.ConfigureTimeSetPeriodRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ConfigureTimeSetPeriodResponse.SerializeToString,
            ),
            'ConfigureTimeSetDriveEdges': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureTimeSetDriveEdges,
                    request_deserializer=nidigitalpattern__pb2.ConfigureTimeSetDriveEdgesRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ConfigureTimeSetDriveEdgesResponse.SerializeToString,
            ),
            'ConfigureTimeSetCompareEdgesStrobe': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureTimeSetCompareEdgesStrobe,
                    request_deserializer=nidigitalpattern__pb2.ConfigureTimeSetCompareEdgesStrobeRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ConfigureTimeSetCompareEdgesStrobeResponse.SerializeToString,
            ),
            'ConfigureTimeSetDriveFormat': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureTimeSetDriveFormat,
                    request_deserializer=nidigitalpattern__pb2.ConfigureTimeSetDriveFormatRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ConfigureTimeSetDriveFormatResponse.SerializeToString,
            ),
            'DeleteAllTimeSets': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAllTimeSets,
                    request_deserializer=nidigitalpattern__pb2.DeleteAllTimeSetsRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.DeleteAllTimeSetsResponse.SerializeToString,
            ),
            'ConfigureTimeSetEdgeMultiplier': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureTimeSetEdgeMultiplier,
                    request_deserializer=nidigitalpattern__pb2.ConfigureTimeSetEdgeMultiplierRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ConfigureTimeSetEdgeMultiplierResponse.SerializeToString,
            ),
            'ConfigureTimeSetDriveEdges2x': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureTimeSetDriveEdges2x,
                    request_deserializer=nidigitalpattern__pb2.ConfigureTimeSetDriveEdges2xRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ConfigureTimeSetDriveEdges2xResponse.SerializeToString,
            ),
            'ConfigureTimeSetCompareEdgesStrobe2x': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureTimeSetCompareEdgesStrobe2x,
                    request_deserializer=nidigitalpattern__pb2.ConfigureTimeSetCompareEdgesStrobe2xRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ConfigureTimeSetCompareEdgesStrobe2xResponse.SerializeToString,
            ),
            'ConfigureTimeSetEdge': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureTimeSetEdge,
                    request_deserializer=nidigitalpattern__pb2.ConfigureTimeSetEdgeRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ConfigureTimeSetEdgeResponse.SerializeToString,
            ),
            'GetTimeSetPeriod': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTimeSetPeriod,
                    request_deserializer=nidigitalpattern__pb2.GetTimeSetPeriodRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.GetTimeSetPeriodResponse.SerializeToString,
            ),
            'GetTimeSetEdge': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTimeSetEdge,
                    request_deserializer=nidigitalpattern__pb2.GetTimeSetEdgeRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.GetTimeSetEdgeResponse.SerializeToString,
            ),
            'GetTimeSetEdgeMultiplier': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTimeSetEdgeMultiplier,
                    request_deserializer=nidigitalpattern__pb2.GetTimeSetEdgeMultiplierRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.GetTimeSetEdgeMultiplierResponse.SerializeToString,
            ),
            'GetTimeSetDriveFormat': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTimeSetDriveFormat,
                    request_deserializer=nidigitalpattern__pb2.GetTimeSetDriveFormatRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.GetTimeSetDriveFormatResponse.SerializeToString,
            ),
            'GetTimeSetName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTimeSetName,
                    request_deserializer=nidigitalpattern__pb2.GetTimeSetNameRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.GetTimeSetNameResponse.SerializeToString,
            ),
            'TDR': grpc.unary_unary_rpc_method_handler(
                    servicer.TDR,
                    request_deserializer=nidigitalpattern__pb2.TDRRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.TDRResponse.SerializeToString,
            ),
            'ApplyTDROffsets': grpc.unary_unary_rpc_method_handler(
                    servicer.ApplyTDROffsets,
                    request_deserializer=nidigitalpattern__pb2.ApplyTDROffsetsRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ApplyTDROffsetsResponse.SerializeToString,
            ),
            'PPMUConfigureOutputFunction': grpc.unary_unary_rpc_method_handler(
                    servicer.PPMUConfigureOutputFunction,
                    request_deserializer=nidigitalpattern__pb2.PPMUConfigureOutputFunctionRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.PPMUConfigureOutputFunctionResponse.SerializeToString,
            ),
            'PPMUConfigureApertureTime': grpc.unary_unary_rpc_method_handler(
                    servicer.PPMUConfigureApertureTime,
                    request_deserializer=nidigitalpattern__pb2.PPMUConfigureApertureTimeRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.PPMUConfigureApertureTimeResponse.SerializeToString,
            ),
            'PPMUConfigureVoltageLevel': grpc.unary_unary_rpc_method_handler(
                    servicer.PPMUConfigureVoltageLevel,
                    request_deserializer=nidigitalpattern__pb2.PPMUConfigureVoltageLevelRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.PPMUConfigureVoltageLevelResponse.SerializeToString,
            ),
            'PPMUConfigureCurrentLimit': grpc.unary_unary_rpc_method_handler(
                    servicer.PPMUConfigureCurrentLimit,
                    request_deserializer=nidigitalpattern__pb2.PPMUConfigureCurrentLimitRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.PPMUConfigureCurrentLimitResponse.SerializeToString,
            ),
            'PPMUConfigureCurrentLimitRange': grpc.unary_unary_rpc_method_handler(
                    servicer.PPMUConfigureCurrentLimitRange,
                    request_deserializer=nidigitalpattern__pb2.PPMUConfigureCurrentLimitRangeRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.PPMUConfigureCurrentLimitRangeResponse.SerializeToString,
            ),
            'PPMUConfigureCurrentLevel': grpc.unary_unary_rpc_method_handler(
                    servicer.PPMUConfigureCurrentLevel,
                    request_deserializer=nidigitalpattern__pb2.PPMUConfigureCurrentLevelRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.PPMUConfigureCurrentLevelResponse.SerializeToString,
            ),
            'PPMUConfigureCurrentLevelRange': grpc.unary_unary_rpc_method_handler(
                    servicer.PPMUConfigureCurrentLevelRange,
                    request_deserializer=nidigitalpattern__pb2.PPMUConfigureCurrentLevelRangeRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.PPMUConfigureCurrentLevelRangeResponse.SerializeToString,
            ),
            'PPMUConfigureVoltageLimits': grpc.unary_unary_rpc_method_handler(
                    servicer.PPMUConfigureVoltageLimits,
                    request_deserializer=nidigitalpattern__pb2.PPMUConfigureVoltageLimitsRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.PPMUConfigureVoltageLimitsResponse.SerializeToString,
            ),
            'PPMUSource': grpc.unary_unary_rpc_method_handler(
                    servicer.PPMUSource,
                    request_deserializer=nidigitalpattern__pb2.PPMUSourceRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.PPMUSourceResponse.SerializeToString,
            ),
            'PPMUMeasure': grpc.unary_unary_rpc_method_handler(
                    servicer.PPMUMeasure,
                    request_deserializer=nidigitalpattern__pb2.PPMUMeasureRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.PPMUMeasureResponse.SerializeToString,
            ),
            'LoadPattern': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadPattern,
                    request_deserializer=nidigitalpattern__pb2.LoadPatternRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.LoadPatternResponse.SerializeToString,
            ),
            'UnloadAllPatterns': grpc.unary_unary_rpc_method_handler(
                    servicer.UnloadAllPatterns,
                    request_deserializer=nidigitalpattern__pb2.UnloadAllPatternsRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.UnloadAllPatternsResponse.SerializeToString,
            ),
            'ConfigureStartLabel': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureStartLabel,
                    request_deserializer=nidigitalpattern__pb2.ConfigureStartLabelRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ConfigureStartLabelResponse.SerializeToString,
            ),
            'ConfigurePatternBurstSites': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigurePatternBurstSites,
                    request_deserializer=nidigitalpattern__pb2.ConfigurePatternBurstSitesRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ConfigurePatternBurstSitesResponse.SerializeToString,
            ),
            'GetPatternPinIndexes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPatternPinIndexes,
                    request_deserializer=nidigitalpattern__pb2.GetPatternPinIndexesRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.GetPatternPinIndexesResponse.SerializeToString,
            ),
            'GetPatternPinList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPatternPinList,
                    request_deserializer=nidigitalpattern__pb2.GetPatternPinListRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.GetPatternPinListResponse.SerializeToString,
            ),
            'GetPatternName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPatternName,
                    request_deserializer=nidigitalpattern__pb2.GetPatternNameRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.GetPatternNameResponse.SerializeToString,
            ),
            'BurstPattern': grpc.unary_unary_rpc_method_handler(
                    servicer.BurstPattern,
                    request_deserializer=nidigitalpattern__pb2.BurstPatternRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.BurstPatternResponse.SerializeToString,
            ),
            'BurstPatternSynchronized': grpc.unary_unary_rpc_method_handler(
                    servicer.BurstPatternSynchronized,
                    request_deserializer=nidigitalpattern__pb2.BurstPatternSynchronizedRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.BurstPatternSynchronizedResponse.SerializeToString,
            ),
            'Commit': grpc.unary_unary_rpc_method_handler(
                    servicer.Commit,
                    request_deserializer=nidigitalpattern__pb2.CommitRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.CommitResponse.SerializeToString,
            ),
            'Initiate': grpc.unary_unary_rpc_method_handler(
                    servicer.Initiate,
                    request_deserializer=nidigitalpattern__pb2.InitiateRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.InitiateResponse.SerializeToString,
            ),
            'IsDone': grpc.unary_unary_rpc_method_handler(
                    servicer.IsDone,
                    request_deserializer=nidigitalpattern__pb2.IsDoneRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.IsDoneResponse.SerializeToString,
            ),
            'WaitUntilDone': grpc.unary_unary_rpc_method_handler(
                    servicer.WaitUntilDone,
                    request_deserializer=nidigitalpattern__pb2.WaitUntilDoneRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.WaitUntilDoneResponse.SerializeToString,
            ),
            'Abort': grpc.unary_unary_rpc_method_handler(
                    servicer.Abort,
                    request_deserializer=nidigitalpattern__pb2.AbortRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.AbortResponse.SerializeToString,
            ),
            'AbortKeepAlive': grpc.unary_unary_rpc_method_handler(
                    servicer.AbortKeepAlive,
                    request_deserializer=nidigitalpattern__pb2.AbortKeepAliveRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.AbortKeepAliveResponse.SerializeToString,
            ),
            'ConfigurePatternLabelHistoryRAMTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigurePatternLabelHistoryRAMTrigger,
                    request_deserializer=nidigitalpattern__pb2.ConfigurePatternLabelHistoryRAMTriggerRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ConfigurePatternLabelHistoryRAMTriggerResponse.SerializeToString,
            ),
            'ConfigureCycleNumberHistoryRAMTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureCycleNumberHistoryRAMTrigger,
                    request_deserializer=nidigitalpattern__pb2.ConfigureCycleNumberHistoryRAMTriggerRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ConfigureCycleNumberHistoryRAMTriggerResponse.SerializeToString,
            ),
            'ConfigureFirstFailureHistoryRAMTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureFirstFailureHistoryRAMTrigger,
                    request_deserializer=nidigitalpattern__pb2.ConfigureFirstFailureHistoryRAMTriggerRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ConfigureFirstFailureHistoryRAMTriggerResponse.SerializeToString,
            ),
            'ConfigureHistoryRAMCyclesToAcquire': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureHistoryRAMCyclesToAcquire,
                    request_deserializer=nidigitalpattern__pb2.ConfigureHistoryRAMCyclesToAcquireRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ConfigureHistoryRAMCyclesToAcquireResponse.SerializeToString,
            ),
            'GetHistoryRAMSampleCount': grpc.unary_unary_rpc_method_handler(
                    servicer.GetHistoryRAMSampleCount,
                    request_deserializer=nidigitalpattern__pb2.GetHistoryRAMSampleCountRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.GetHistoryRAMSampleCountResponse.SerializeToString,
            ),
            'FetchHistoryRAMCycleInformation': grpc.unary_unary_rpc_method_handler(
                    servicer.FetchHistoryRAMCycleInformation,
                    request_deserializer=nidigitalpattern__pb2.FetchHistoryRAMCycleInformationRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.FetchHistoryRAMCycleInformationResponse.SerializeToString,
            ),
            'FetchHistoryRAMCyclePinData': grpc.unary_unary_rpc_method_handler(
                    servicer.FetchHistoryRAMCyclePinData,
                    request_deserializer=nidigitalpattern__pb2.FetchHistoryRAMCyclePinDataRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.FetchHistoryRAMCyclePinDataResponse.SerializeToString,
            ),
            'FetchHistoryRAMScanCycleNumber': grpc.unary_unary_rpc_method_handler(
                    servicer.FetchHistoryRAMScanCycleNumber,
                    request_deserializer=nidigitalpattern__pb2.FetchHistoryRAMScanCycleNumberRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.FetchHistoryRAMScanCycleNumberResponse.SerializeToString,
            ),
            'CreateSourceWaveformParallel': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateSourceWaveformParallel,
                    request_deserializer=nidigitalpattern__pb2.CreateSourceWaveformParallelRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.CreateSourceWaveformParallelResponse.SerializeToString,
            ),
            'CreateSourceWaveformSerial': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateSourceWaveformSerial,
                    request_deserializer=nidigitalpattern__pb2.CreateSourceWaveformSerialRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.CreateSourceWaveformSerialResponse.SerializeToString,
            ),
            'CreateSourceWaveformFromFileTDMS': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateSourceWaveformFromFileTDMS,
                    request_deserializer=nidigitalpattern__pb2.CreateSourceWaveformFromFileTDMSRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.CreateSourceWaveformFromFileTDMSResponse.SerializeToString,
            ),
            'WriteSourceWaveformBroadcastU32': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteSourceWaveformBroadcastU32,
                    request_deserializer=nidigitalpattern__pb2.WriteSourceWaveformBroadcastU32Request.FromString,
                    response_serializer=nidigitalpattern__pb2.WriteSourceWaveformBroadcastU32Response.SerializeToString,
            ),
            'WriteSourceWaveformSiteUniqueU32': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteSourceWaveformSiteUniqueU32,
                    request_deserializer=nidigitalpattern__pb2.WriteSourceWaveformSiteUniqueU32Request.FromString,
                    response_serializer=nidigitalpattern__pb2.WriteSourceWaveformSiteUniqueU32Response.SerializeToString,
            ),
            'WriteSourceWaveformDataFromFileTDMS': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteSourceWaveformDataFromFileTDMS,
                    request_deserializer=nidigitalpattern__pb2.WriteSourceWaveformDataFromFileTDMSRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.WriteSourceWaveformDataFromFileTDMSResponse.SerializeToString,
            ),
            'CreateCaptureWaveformParallel': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCaptureWaveformParallel,
                    request_deserializer=nidigitalpattern__pb2.CreateCaptureWaveformParallelRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.CreateCaptureWaveformParallelResponse.SerializeToString,
            ),
            'CreateCaptureWaveformSerial': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCaptureWaveformSerial,
                    request_deserializer=nidigitalpattern__pb2.CreateCaptureWaveformSerialRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.CreateCaptureWaveformSerialResponse.SerializeToString,
            ),
            'CreateCaptureWaveformFromFileDigicapture': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCaptureWaveformFromFileDigicapture,
                    request_deserializer=nidigitalpattern__pb2.CreateCaptureWaveformFromFileDigicaptureRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.CreateCaptureWaveformFromFileDigicaptureResponse.SerializeToString,
            ),
            'FetchCaptureWaveformU32': grpc.unary_unary_rpc_method_handler(
                    servicer.FetchCaptureWaveformU32,
                    request_deserializer=nidigitalpattern__pb2.FetchCaptureWaveformU32Request.FromString,
                    response_serializer=nidigitalpattern__pb2.FetchCaptureWaveformU32Response.SerializeToString,
            ),
            'ExportSignal': grpc.unary_unary_rpc_method_handler(
                    servicer.ExportSignal,
                    request_deserializer=nidigitalpattern__pb2.ExportSignalRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ExportSignalResponse.SerializeToString,
            ),
            'ConfigureDigitalEdgeStartTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureDigitalEdgeStartTrigger,
                    request_deserializer=nidigitalpattern__pb2.ConfigureDigitalEdgeStartTriggerRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ConfigureDigitalEdgeStartTriggerResponse.SerializeToString,
            ),
            'ConfigureSoftwareEdgeStartTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureSoftwareEdgeStartTrigger,
                    request_deserializer=nidigitalpattern__pb2.ConfigureSoftwareEdgeStartTriggerRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ConfigureSoftwareEdgeStartTriggerResponse.SerializeToString,
            ),
            'DisableStartTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.DisableStartTrigger,
                    request_deserializer=nidigitalpattern__pb2.DisableStartTriggerRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.DisableStartTriggerResponse.SerializeToString,
            ),
            'ConfigureDigitalEdgeConditionalJumpTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureDigitalEdgeConditionalJumpTrigger,
                    request_deserializer=nidigitalpattern__pb2.ConfigureDigitalEdgeConditionalJumpTriggerRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ConfigureDigitalEdgeConditionalJumpTriggerResponse.SerializeToString,
            ),
            'ConfigureSoftwareEdgeConditionalJumpTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureSoftwareEdgeConditionalJumpTrigger,
                    request_deserializer=nidigitalpattern__pb2.ConfigureSoftwareEdgeConditionalJumpTriggerRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ConfigureSoftwareEdgeConditionalJumpTriggerResponse.SerializeToString,
            ),
            'DisableConditionalJumpTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.DisableConditionalJumpTrigger,
                    request_deserializer=nidigitalpattern__pb2.DisableConditionalJumpTriggerRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.DisableConditionalJumpTriggerResponse.SerializeToString,
            ),
            'SendSoftwareEdgeTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.SendSoftwareEdgeTrigger,
                    request_deserializer=nidigitalpattern__pb2.SendSoftwareEdgeTriggerRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.SendSoftwareEdgeTriggerResponse.SerializeToString,
            ),
            'WriteSequencerFlag': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteSequencerFlag,
                    request_deserializer=nidigitalpattern__pb2.WriteSequencerFlagRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.WriteSequencerFlagResponse.SerializeToString,
            ),
            'WriteSequencerFlagSynchronized': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteSequencerFlagSynchronized,
                    request_deserializer=nidigitalpattern__pb2.WriteSequencerFlagSynchronizedRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.WriteSequencerFlagSynchronizedResponse.SerializeToString,
            ),
            'ReadSequencerFlag': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadSequencerFlag,
                    request_deserializer=nidigitalpattern__pb2.ReadSequencerFlagRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ReadSequencerFlagResponse.SerializeToString,
            ),
            'WriteSequencerRegister': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteSequencerRegister,
                    request_deserializer=nidigitalpattern__pb2.WriteSequencerRegisterRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.WriteSequencerRegisterResponse.SerializeToString,
            ),
            'ReadSequencerRegister': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadSequencerRegister,
                    request_deserializer=nidigitalpattern__pb2.ReadSequencerRegisterRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.ReadSequencerRegisterResponse.SerializeToString,
            ),
            'EnableMatchFailCombination': grpc.unary_unary_rpc_method_handler(
                    servicer.EnableMatchFailCombination,
                    request_deserializer=nidigitalpattern__pb2.EnableMatchFailCombinationRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.EnableMatchFailCombinationResponse.SerializeToString,
            ),
            'GetSitePassFail': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSitePassFail,
                    request_deserializer=nidigitalpattern__pb2.GetSitePassFailRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.GetSitePassFailResponse.SerializeToString,
            ),
            'GetFailCount': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFailCount,
                    request_deserializer=nidigitalpattern__pb2.GetFailCountRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.GetFailCountResponse.SerializeToString,
            ),
            'GetPinResultsPinInformation': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPinResultsPinInformation,
                    request_deserializer=nidigitalpattern__pb2.GetPinResultsPinInformationRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.GetPinResultsPinInformationResponse.SerializeToString,
            ),
            'GetSiteResultsSiteNumbers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSiteResultsSiteNumbers,
                    request_deserializer=nidigitalpattern__pb2.GetSiteResultsSiteNumbersRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.GetSiteResultsSiteNumbersResponse.SerializeToString,
            ),
            'FrequencyCounterConfigureMeasurementTime': grpc.unary_unary_rpc_method_handler(
                    servicer.FrequencyCounterConfigureMeasurementTime,
                    request_deserializer=nidigitalpattern__pb2.FrequencyCounterConfigureMeasurementTimeRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.FrequencyCounterConfigureMeasurementTimeResponse.SerializeToString,
            ),
            'FrequencyCounterConfigureMeasurementMode': grpc.unary_unary_rpc_method_handler(
                    servicer.FrequencyCounterConfigureMeasurementMode,
                    request_deserializer=nidigitalpattern__pb2.FrequencyCounterConfigureMeasurementModeRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.FrequencyCounterConfigureMeasurementModeResponse.SerializeToString,
            ),
            'FrequencyCounterMeasureFrequency': grpc.unary_unary_rpc_method_handler(
                    servicer.FrequencyCounterMeasureFrequency,
                    request_deserializer=nidigitalpattern__pb2.FrequencyCounterMeasureFrequencyRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.FrequencyCounterMeasureFrequencyResponse.SerializeToString,
            ),
            'GetChannelNameFromString': grpc.unary_unary_rpc_method_handler(
                    servicer.GetChannelNameFromString,
                    request_deserializer=nidigitalpattern__pb2.GetChannelNameFromStringRequest.FromString,
                    response_serializer=nidigitalpattern__pb2.GetChannelNameFromStringResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'nidigitalpattern_grpc.NiDigital', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NiDigital(object):
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
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/Init',
            nidigitalpattern__pb2.InitRequest.SerializeToString,
            nidigitalpattern__pb2.InitResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/InitWithOptions',
            nidigitalpattern__pb2.InitWithOptionsRequest.SerializeToString,
            nidigitalpattern__pb2.InitWithOptionsResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/Close',
            nidigitalpattern__pb2.CloseRequest.SerializeToString,
            nidigitalpattern__pb2.CloseResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/Reset',
            nidigitalpattern__pb2.ResetRequest.SerializeToString,
            nidigitalpattern__pb2.ResetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResetDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ResetDevice',
            nidigitalpattern__pb2.ResetDeviceRequest.SerializeToString,
            nidigitalpattern__pb2.ResetDeviceResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/SelfTest',
            nidigitalpattern__pb2.SelfTestRequest.SerializeToString,
            nidigitalpattern__pb2.SelfTestResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/GetError',
            nidigitalpattern__pb2.GetErrorRequest.SerializeToString,
            nidigitalpattern__pb2.GetErrorResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ClearError',
            nidigitalpattern__pb2.ClearErrorRequest.SerializeToString,
            nidigitalpattern__pb2.ClearErrorResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ErrorMessage',
            nidigitalpattern__pb2.ErrorMessageRequest.SerializeToString,
            nidigitalpattern__pb2.ErrorMessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SelfCalibrate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/SelfCalibrate',
            nidigitalpattern__pb2.SelfCalibrateRequest.SerializeToString,
            nidigitalpattern__pb2.SelfCalibrateResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/GetAttributeViInt32',
            nidigitalpattern__pb2.GetAttributeViInt32Request.SerializeToString,
            nidigitalpattern__pb2.GetAttributeViInt32Response.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/GetAttributeViInt64',
            nidigitalpattern__pb2.GetAttributeViInt64Request.SerializeToString,
            nidigitalpattern__pb2.GetAttributeViInt64Response.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/GetAttributeViReal64',
            nidigitalpattern__pb2.GetAttributeViReal64Request.SerializeToString,
            nidigitalpattern__pb2.GetAttributeViReal64Response.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/GetAttributeViString',
            nidigitalpattern__pb2.GetAttributeViStringRequest.SerializeToString,
            nidigitalpattern__pb2.GetAttributeViStringResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/GetAttributeViSession',
            nidigitalpattern__pb2.GetAttributeViSessionRequest.SerializeToString,
            nidigitalpattern__pb2.GetAttributeViSessionResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/GetAttributeViBoolean',
            nidigitalpattern__pb2.GetAttributeViBooleanRequest.SerializeToString,
            nidigitalpattern__pb2.GetAttributeViBooleanResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/SetAttributeViInt32',
            nidigitalpattern__pb2.SetAttributeViInt32Request.SerializeToString,
            nidigitalpattern__pb2.SetAttributeViInt32Response.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/SetAttributeViInt64',
            nidigitalpattern__pb2.SetAttributeViInt64Request.SerializeToString,
            nidigitalpattern__pb2.SetAttributeViInt64Response.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/SetAttributeViReal64',
            nidigitalpattern__pb2.SetAttributeViReal64Request.SerializeToString,
            nidigitalpattern__pb2.SetAttributeViReal64Response.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/SetAttributeViString',
            nidigitalpattern__pb2.SetAttributeViStringRequest.SerializeToString,
            nidigitalpattern__pb2.SetAttributeViStringResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/SetAttributeViSession',
            nidigitalpattern__pb2.SetAttributeViSessionRequest.SerializeToString,
            nidigitalpattern__pb2.SetAttributeViSessionResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/SetAttributeViBoolean',
            nidigitalpattern__pb2.SetAttributeViBooleanRequest.SerializeToString,
            nidigitalpattern__pb2.SetAttributeViBooleanResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResetAttribute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ResetAttribute',
            nidigitalpattern__pb2.ResetAttributeRequest.SerializeToString,
            nidigitalpattern__pb2.ResetAttributeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LoadPinMap(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/LoadPinMap',
            nidigitalpattern__pb2.LoadPinMapRequest.SerializeToString,
            nidigitalpattern__pb2.LoadPinMapResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EnableSites(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/EnableSites',
            nidigitalpattern__pb2.EnableSitesRequest.SerializeToString,
            nidigitalpattern__pb2.EnableSitesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisableSites(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/DisableSites',
            nidigitalpattern__pb2.DisableSitesRequest.SerializeToString,
            nidigitalpattern__pb2.DisableSitesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IsSiteEnabled(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/IsSiteEnabled',
            nidigitalpattern__pb2.IsSiteEnabledRequest.SerializeToString,
            nidigitalpattern__pb2.IsSiteEnabledResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreatePinMap(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/CreatePinMap',
            nidigitalpattern__pb2.CreatePinMapRequest.SerializeToString,
            nidigitalpattern__pb2.CreatePinMapResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreatePinGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/CreatePinGroup',
            nidigitalpattern__pb2.CreatePinGroupRequest.SerializeToString,
            nidigitalpattern__pb2.CreatePinGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateChannelMap(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/CreateChannelMap',
            nidigitalpattern__pb2.CreateChannelMapRequest.SerializeToString,
            nidigitalpattern__pb2.CreateChannelMapResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MapPinToChannel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/MapPinToChannel',
            nidigitalpattern__pb2.MapPinToChannelRequest.SerializeToString,
            nidigitalpattern__pb2.MapPinToChannelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EndChannelMap(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/EndChannelMap',
            nidigitalpattern__pb2.EndChannelMapRequest.SerializeToString,
            nidigitalpattern__pb2.EndChannelMapResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPinName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/GetPinName',
            nidigitalpattern__pb2.GetPinNameRequest.SerializeToString,
            nidigitalpattern__pb2.GetPinNameResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/GetChannelName',
            nidigitalpattern__pb2.GetChannelNameRequest.SerializeToString,
            nidigitalpattern__pb2.GetChannelNameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SelectFunction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/SelectFunction',
            nidigitalpattern__pb2.SelectFunctionRequest.SerializeToString,
            nidigitalpattern__pb2.SelectFunctionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadStatic(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ReadStatic',
            nidigitalpattern__pb2.ReadStaticRequest.SerializeToString,
            nidigitalpattern__pb2.ReadStaticResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteStatic(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/WriteStatic',
            nidigitalpattern__pb2.WriteStaticRequest.SerializeToString,
            nidigitalpattern__pb2.WriteStaticResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClockGeneratorGenerateClock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ClockGeneratorGenerateClock',
            nidigitalpattern__pb2.ClockGeneratorGenerateClockRequest.SerializeToString,
            nidigitalpattern__pb2.ClockGeneratorGenerateClockResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClockGeneratorInitiate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ClockGeneratorInitiate',
            nidigitalpattern__pb2.ClockGeneratorInitiateRequest.SerializeToString,
            nidigitalpattern__pb2.ClockGeneratorInitiateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClockGeneratorAbort(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ClockGeneratorAbort',
            nidigitalpattern__pb2.ClockGeneratorAbortRequest.SerializeToString,
            nidigitalpattern__pb2.ClockGeneratorAbortResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LoadSpecifications(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/LoadSpecifications',
            nidigitalpattern__pb2.LoadSpecificationsRequest.SerializeToString,
            nidigitalpattern__pb2.LoadSpecificationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnloadSpecifications(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/UnloadSpecifications',
            nidigitalpattern__pb2.UnloadSpecificationsRequest.SerializeToString,
            nidigitalpattern__pb2.UnloadSpecificationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LoadLevels(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/LoadLevels',
            nidigitalpattern__pb2.LoadLevelsRequest.SerializeToString,
            nidigitalpattern__pb2.LoadLevelsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LoadTiming(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/LoadTiming',
            nidigitalpattern__pb2.LoadTimingRequest.SerializeToString,
            nidigitalpattern__pb2.LoadTimingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ApplyLevelsAndTiming(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ApplyLevelsAndTiming',
            nidigitalpattern__pb2.ApplyLevelsAndTimingRequest.SerializeToString,
            nidigitalpattern__pb2.ApplyLevelsAndTimingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureVoltageLevels(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ConfigureVoltageLevels',
            nidigitalpattern__pb2.ConfigureVoltageLevelsRequest.SerializeToString,
            nidigitalpattern__pb2.ConfigureVoltageLevelsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureActiveLoadLevels(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ConfigureActiveLoadLevels',
            nidigitalpattern__pb2.ConfigureActiveLoadLevelsRequest.SerializeToString,
            nidigitalpattern__pb2.ConfigureActiveLoadLevelsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureTerminationMode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ConfigureTerminationMode',
            nidigitalpattern__pb2.ConfigureTerminationModeRequest.SerializeToString,
            nidigitalpattern__pb2.ConfigureTerminationModeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateTimeSet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/CreateTimeSet',
            nidigitalpattern__pb2.CreateTimeSetRequest.SerializeToString,
            nidigitalpattern__pb2.CreateTimeSetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureTimeSetPeriod(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ConfigureTimeSetPeriod',
            nidigitalpattern__pb2.ConfigureTimeSetPeriodRequest.SerializeToString,
            nidigitalpattern__pb2.ConfigureTimeSetPeriodResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureTimeSetDriveEdges(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ConfigureTimeSetDriveEdges',
            nidigitalpattern__pb2.ConfigureTimeSetDriveEdgesRequest.SerializeToString,
            nidigitalpattern__pb2.ConfigureTimeSetDriveEdgesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureTimeSetCompareEdgesStrobe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ConfigureTimeSetCompareEdgesStrobe',
            nidigitalpattern__pb2.ConfigureTimeSetCompareEdgesStrobeRequest.SerializeToString,
            nidigitalpattern__pb2.ConfigureTimeSetCompareEdgesStrobeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureTimeSetDriveFormat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ConfigureTimeSetDriveFormat',
            nidigitalpattern__pb2.ConfigureTimeSetDriveFormatRequest.SerializeToString,
            nidigitalpattern__pb2.ConfigureTimeSetDriveFormatResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteAllTimeSets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/DeleteAllTimeSets',
            nidigitalpattern__pb2.DeleteAllTimeSetsRequest.SerializeToString,
            nidigitalpattern__pb2.DeleteAllTimeSetsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureTimeSetEdgeMultiplier(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ConfigureTimeSetEdgeMultiplier',
            nidigitalpattern__pb2.ConfigureTimeSetEdgeMultiplierRequest.SerializeToString,
            nidigitalpattern__pb2.ConfigureTimeSetEdgeMultiplierResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureTimeSetDriveEdges2x(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ConfigureTimeSetDriveEdges2x',
            nidigitalpattern__pb2.ConfigureTimeSetDriveEdges2xRequest.SerializeToString,
            nidigitalpattern__pb2.ConfigureTimeSetDriveEdges2xResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureTimeSetCompareEdgesStrobe2x(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ConfigureTimeSetCompareEdgesStrobe2x',
            nidigitalpattern__pb2.ConfigureTimeSetCompareEdgesStrobe2xRequest.SerializeToString,
            nidigitalpattern__pb2.ConfigureTimeSetCompareEdgesStrobe2xResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureTimeSetEdge(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ConfigureTimeSetEdge',
            nidigitalpattern__pb2.ConfigureTimeSetEdgeRequest.SerializeToString,
            nidigitalpattern__pb2.ConfigureTimeSetEdgeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTimeSetPeriod(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/GetTimeSetPeriod',
            nidigitalpattern__pb2.GetTimeSetPeriodRequest.SerializeToString,
            nidigitalpattern__pb2.GetTimeSetPeriodResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTimeSetEdge(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/GetTimeSetEdge',
            nidigitalpattern__pb2.GetTimeSetEdgeRequest.SerializeToString,
            nidigitalpattern__pb2.GetTimeSetEdgeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTimeSetEdgeMultiplier(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/GetTimeSetEdgeMultiplier',
            nidigitalpattern__pb2.GetTimeSetEdgeMultiplierRequest.SerializeToString,
            nidigitalpattern__pb2.GetTimeSetEdgeMultiplierResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTimeSetDriveFormat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/GetTimeSetDriveFormat',
            nidigitalpattern__pb2.GetTimeSetDriveFormatRequest.SerializeToString,
            nidigitalpattern__pb2.GetTimeSetDriveFormatResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTimeSetName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/GetTimeSetName',
            nidigitalpattern__pb2.GetTimeSetNameRequest.SerializeToString,
            nidigitalpattern__pb2.GetTimeSetNameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TDR(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/TDR',
            nidigitalpattern__pb2.TDRRequest.SerializeToString,
            nidigitalpattern__pb2.TDRResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ApplyTDROffsets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ApplyTDROffsets',
            nidigitalpattern__pb2.ApplyTDROffsetsRequest.SerializeToString,
            nidigitalpattern__pb2.ApplyTDROffsetsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PPMUConfigureOutputFunction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/PPMUConfigureOutputFunction',
            nidigitalpattern__pb2.PPMUConfigureOutputFunctionRequest.SerializeToString,
            nidigitalpattern__pb2.PPMUConfigureOutputFunctionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PPMUConfigureApertureTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/PPMUConfigureApertureTime',
            nidigitalpattern__pb2.PPMUConfigureApertureTimeRequest.SerializeToString,
            nidigitalpattern__pb2.PPMUConfigureApertureTimeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PPMUConfigureVoltageLevel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/PPMUConfigureVoltageLevel',
            nidigitalpattern__pb2.PPMUConfigureVoltageLevelRequest.SerializeToString,
            nidigitalpattern__pb2.PPMUConfigureVoltageLevelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PPMUConfigureCurrentLimit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/PPMUConfigureCurrentLimit',
            nidigitalpattern__pb2.PPMUConfigureCurrentLimitRequest.SerializeToString,
            nidigitalpattern__pb2.PPMUConfigureCurrentLimitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PPMUConfigureCurrentLimitRange(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/PPMUConfigureCurrentLimitRange',
            nidigitalpattern__pb2.PPMUConfigureCurrentLimitRangeRequest.SerializeToString,
            nidigitalpattern__pb2.PPMUConfigureCurrentLimitRangeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PPMUConfigureCurrentLevel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/PPMUConfigureCurrentLevel',
            nidigitalpattern__pb2.PPMUConfigureCurrentLevelRequest.SerializeToString,
            nidigitalpattern__pb2.PPMUConfigureCurrentLevelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PPMUConfigureCurrentLevelRange(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/PPMUConfigureCurrentLevelRange',
            nidigitalpattern__pb2.PPMUConfigureCurrentLevelRangeRequest.SerializeToString,
            nidigitalpattern__pb2.PPMUConfigureCurrentLevelRangeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PPMUConfigureVoltageLimits(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/PPMUConfigureVoltageLimits',
            nidigitalpattern__pb2.PPMUConfigureVoltageLimitsRequest.SerializeToString,
            nidigitalpattern__pb2.PPMUConfigureVoltageLimitsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PPMUSource(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/PPMUSource',
            nidigitalpattern__pb2.PPMUSourceRequest.SerializeToString,
            nidigitalpattern__pb2.PPMUSourceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PPMUMeasure(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/PPMUMeasure',
            nidigitalpattern__pb2.PPMUMeasureRequest.SerializeToString,
            nidigitalpattern__pb2.PPMUMeasureResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LoadPattern(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/LoadPattern',
            nidigitalpattern__pb2.LoadPatternRequest.SerializeToString,
            nidigitalpattern__pb2.LoadPatternResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnloadAllPatterns(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/UnloadAllPatterns',
            nidigitalpattern__pb2.UnloadAllPatternsRequest.SerializeToString,
            nidigitalpattern__pb2.UnloadAllPatternsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureStartLabel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ConfigureStartLabel',
            nidigitalpattern__pb2.ConfigureStartLabelRequest.SerializeToString,
            nidigitalpattern__pb2.ConfigureStartLabelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigurePatternBurstSites(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ConfigurePatternBurstSites',
            nidigitalpattern__pb2.ConfigurePatternBurstSitesRequest.SerializeToString,
            nidigitalpattern__pb2.ConfigurePatternBurstSitesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPatternPinIndexes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/GetPatternPinIndexes',
            nidigitalpattern__pb2.GetPatternPinIndexesRequest.SerializeToString,
            nidigitalpattern__pb2.GetPatternPinIndexesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPatternPinList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/GetPatternPinList',
            nidigitalpattern__pb2.GetPatternPinListRequest.SerializeToString,
            nidigitalpattern__pb2.GetPatternPinListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPatternName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/GetPatternName',
            nidigitalpattern__pb2.GetPatternNameRequest.SerializeToString,
            nidigitalpattern__pb2.GetPatternNameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BurstPattern(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/BurstPattern',
            nidigitalpattern__pb2.BurstPatternRequest.SerializeToString,
            nidigitalpattern__pb2.BurstPatternResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BurstPatternSynchronized(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/BurstPatternSynchronized',
            nidigitalpattern__pb2.BurstPatternSynchronizedRequest.SerializeToString,
            nidigitalpattern__pb2.BurstPatternSynchronizedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Commit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/Commit',
            nidigitalpattern__pb2.CommitRequest.SerializeToString,
            nidigitalpattern__pb2.CommitResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/Initiate',
            nidigitalpattern__pb2.InitiateRequest.SerializeToString,
            nidigitalpattern__pb2.InitiateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IsDone(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/IsDone',
            nidigitalpattern__pb2.IsDoneRequest.SerializeToString,
            nidigitalpattern__pb2.IsDoneResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WaitUntilDone(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/WaitUntilDone',
            nidigitalpattern__pb2.WaitUntilDoneRequest.SerializeToString,
            nidigitalpattern__pb2.WaitUntilDoneResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/Abort',
            nidigitalpattern__pb2.AbortRequest.SerializeToString,
            nidigitalpattern__pb2.AbortResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AbortKeepAlive(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/AbortKeepAlive',
            nidigitalpattern__pb2.AbortKeepAliveRequest.SerializeToString,
            nidigitalpattern__pb2.AbortKeepAliveResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigurePatternLabelHistoryRAMTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ConfigurePatternLabelHistoryRAMTrigger',
            nidigitalpattern__pb2.ConfigurePatternLabelHistoryRAMTriggerRequest.SerializeToString,
            nidigitalpattern__pb2.ConfigurePatternLabelHistoryRAMTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureCycleNumberHistoryRAMTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ConfigureCycleNumberHistoryRAMTrigger',
            nidigitalpattern__pb2.ConfigureCycleNumberHistoryRAMTriggerRequest.SerializeToString,
            nidigitalpattern__pb2.ConfigureCycleNumberHistoryRAMTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureFirstFailureHistoryRAMTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ConfigureFirstFailureHistoryRAMTrigger',
            nidigitalpattern__pb2.ConfigureFirstFailureHistoryRAMTriggerRequest.SerializeToString,
            nidigitalpattern__pb2.ConfigureFirstFailureHistoryRAMTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureHistoryRAMCyclesToAcquire(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ConfigureHistoryRAMCyclesToAcquire',
            nidigitalpattern__pb2.ConfigureHistoryRAMCyclesToAcquireRequest.SerializeToString,
            nidigitalpattern__pb2.ConfigureHistoryRAMCyclesToAcquireResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetHistoryRAMSampleCount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/GetHistoryRAMSampleCount',
            nidigitalpattern__pb2.GetHistoryRAMSampleCountRequest.SerializeToString,
            nidigitalpattern__pb2.GetHistoryRAMSampleCountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FetchHistoryRAMCycleInformation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/FetchHistoryRAMCycleInformation',
            nidigitalpattern__pb2.FetchHistoryRAMCycleInformationRequest.SerializeToString,
            nidigitalpattern__pb2.FetchHistoryRAMCycleInformationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FetchHistoryRAMCyclePinData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/FetchHistoryRAMCyclePinData',
            nidigitalpattern__pb2.FetchHistoryRAMCyclePinDataRequest.SerializeToString,
            nidigitalpattern__pb2.FetchHistoryRAMCyclePinDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FetchHistoryRAMScanCycleNumber(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/FetchHistoryRAMScanCycleNumber',
            nidigitalpattern__pb2.FetchHistoryRAMScanCycleNumberRequest.SerializeToString,
            nidigitalpattern__pb2.FetchHistoryRAMScanCycleNumberResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateSourceWaveformParallel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/CreateSourceWaveformParallel',
            nidigitalpattern__pb2.CreateSourceWaveformParallelRequest.SerializeToString,
            nidigitalpattern__pb2.CreateSourceWaveformParallelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateSourceWaveformSerial(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/CreateSourceWaveformSerial',
            nidigitalpattern__pb2.CreateSourceWaveformSerialRequest.SerializeToString,
            nidigitalpattern__pb2.CreateSourceWaveformSerialResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateSourceWaveformFromFileTDMS(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/CreateSourceWaveformFromFileTDMS',
            nidigitalpattern__pb2.CreateSourceWaveformFromFileTDMSRequest.SerializeToString,
            nidigitalpattern__pb2.CreateSourceWaveformFromFileTDMSResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteSourceWaveformBroadcastU32(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/WriteSourceWaveformBroadcastU32',
            nidigitalpattern__pb2.WriteSourceWaveformBroadcastU32Request.SerializeToString,
            nidigitalpattern__pb2.WriteSourceWaveformBroadcastU32Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteSourceWaveformSiteUniqueU32(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/WriteSourceWaveformSiteUniqueU32',
            nidigitalpattern__pb2.WriteSourceWaveformSiteUniqueU32Request.SerializeToString,
            nidigitalpattern__pb2.WriteSourceWaveformSiteUniqueU32Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteSourceWaveformDataFromFileTDMS(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/WriteSourceWaveformDataFromFileTDMS',
            nidigitalpattern__pb2.WriteSourceWaveformDataFromFileTDMSRequest.SerializeToString,
            nidigitalpattern__pb2.WriteSourceWaveformDataFromFileTDMSResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateCaptureWaveformParallel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/CreateCaptureWaveformParallel',
            nidigitalpattern__pb2.CreateCaptureWaveformParallelRequest.SerializeToString,
            nidigitalpattern__pb2.CreateCaptureWaveformParallelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateCaptureWaveformSerial(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/CreateCaptureWaveformSerial',
            nidigitalpattern__pb2.CreateCaptureWaveformSerialRequest.SerializeToString,
            nidigitalpattern__pb2.CreateCaptureWaveformSerialResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateCaptureWaveformFromFileDigicapture(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/CreateCaptureWaveformFromFileDigicapture',
            nidigitalpattern__pb2.CreateCaptureWaveformFromFileDigicaptureRequest.SerializeToString,
            nidigitalpattern__pb2.CreateCaptureWaveformFromFileDigicaptureResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FetchCaptureWaveformU32(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/FetchCaptureWaveformU32',
            nidigitalpattern__pb2.FetchCaptureWaveformU32Request.SerializeToString,
            nidigitalpattern__pb2.FetchCaptureWaveformU32Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExportSignal(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ExportSignal',
            nidigitalpattern__pb2.ExportSignalRequest.SerializeToString,
            nidigitalpattern__pb2.ExportSignalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureDigitalEdgeStartTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ConfigureDigitalEdgeStartTrigger',
            nidigitalpattern__pb2.ConfigureDigitalEdgeStartTriggerRequest.SerializeToString,
            nidigitalpattern__pb2.ConfigureDigitalEdgeStartTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureSoftwareEdgeStartTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ConfigureSoftwareEdgeStartTrigger',
            nidigitalpattern__pb2.ConfigureSoftwareEdgeStartTriggerRequest.SerializeToString,
            nidigitalpattern__pb2.ConfigureSoftwareEdgeStartTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisableStartTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/DisableStartTrigger',
            nidigitalpattern__pb2.DisableStartTriggerRequest.SerializeToString,
            nidigitalpattern__pb2.DisableStartTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureDigitalEdgeConditionalJumpTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ConfigureDigitalEdgeConditionalJumpTrigger',
            nidigitalpattern__pb2.ConfigureDigitalEdgeConditionalJumpTriggerRequest.SerializeToString,
            nidigitalpattern__pb2.ConfigureDigitalEdgeConditionalJumpTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureSoftwareEdgeConditionalJumpTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ConfigureSoftwareEdgeConditionalJumpTrigger',
            nidigitalpattern__pb2.ConfigureSoftwareEdgeConditionalJumpTriggerRequest.SerializeToString,
            nidigitalpattern__pb2.ConfigureSoftwareEdgeConditionalJumpTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisableConditionalJumpTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/DisableConditionalJumpTrigger',
            nidigitalpattern__pb2.DisableConditionalJumpTriggerRequest.SerializeToString,
            nidigitalpattern__pb2.DisableConditionalJumpTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendSoftwareEdgeTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/SendSoftwareEdgeTrigger',
            nidigitalpattern__pb2.SendSoftwareEdgeTriggerRequest.SerializeToString,
            nidigitalpattern__pb2.SendSoftwareEdgeTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteSequencerFlag(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/WriteSequencerFlag',
            nidigitalpattern__pb2.WriteSequencerFlagRequest.SerializeToString,
            nidigitalpattern__pb2.WriteSequencerFlagResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteSequencerFlagSynchronized(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/WriteSequencerFlagSynchronized',
            nidigitalpattern__pb2.WriteSequencerFlagSynchronizedRequest.SerializeToString,
            nidigitalpattern__pb2.WriteSequencerFlagSynchronizedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadSequencerFlag(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ReadSequencerFlag',
            nidigitalpattern__pb2.ReadSequencerFlagRequest.SerializeToString,
            nidigitalpattern__pb2.ReadSequencerFlagResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteSequencerRegister(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/WriteSequencerRegister',
            nidigitalpattern__pb2.WriteSequencerRegisterRequest.SerializeToString,
            nidigitalpattern__pb2.WriteSequencerRegisterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadSequencerRegister(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/ReadSequencerRegister',
            nidigitalpattern__pb2.ReadSequencerRegisterRequest.SerializeToString,
            nidigitalpattern__pb2.ReadSequencerRegisterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EnableMatchFailCombination(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/EnableMatchFailCombination',
            nidigitalpattern__pb2.EnableMatchFailCombinationRequest.SerializeToString,
            nidigitalpattern__pb2.EnableMatchFailCombinationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSitePassFail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/GetSitePassFail',
            nidigitalpattern__pb2.GetSitePassFailRequest.SerializeToString,
            nidigitalpattern__pb2.GetSitePassFailResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFailCount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/GetFailCount',
            nidigitalpattern__pb2.GetFailCountRequest.SerializeToString,
            nidigitalpattern__pb2.GetFailCountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPinResultsPinInformation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/GetPinResultsPinInformation',
            nidigitalpattern__pb2.GetPinResultsPinInformationRequest.SerializeToString,
            nidigitalpattern__pb2.GetPinResultsPinInformationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSiteResultsSiteNumbers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/GetSiteResultsSiteNumbers',
            nidigitalpattern__pb2.GetSiteResultsSiteNumbersRequest.SerializeToString,
            nidigitalpattern__pb2.GetSiteResultsSiteNumbersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FrequencyCounterConfigureMeasurementTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/FrequencyCounterConfigureMeasurementTime',
            nidigitalpattern__pb2.FrequencyCounterConfigureMeasurementTimeRequest.SerializeToString,
            nidigitalpattern__pb2.FrequencyCounterConfigureMeasurementTimeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FrequencyCounterConfigureMeasurementMode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/FrequencyCounterConfigureMeasurementMode',
            nidigitalpattern__pb2.FrequencyCounterConfigureMeasurementModeRequest.SerializeToString,
            nidigitalpattern__pb2.FrequencyCounterConfigureMeasurementModeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FrequencyCounterMeasureFrequency(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/FrequencyCounterMeasureFrequency',
            nidigitalpattern__pb2.FrequencyCounterMeasureFrequencyRequest.SerializeToString,
            nidigitalpattern__pb2.FrequencyCounterMeasureFrequencyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetChannelNameFromString(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nidigitalpattern_grpc.NiDigital/GetChannelNameFromString',
            nidigitalpattern__pb2.GetChannelNameFromStringRequest.SerializeToString,
            nidigitalpattern__pb2.GetChannelNameFromStringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
````
