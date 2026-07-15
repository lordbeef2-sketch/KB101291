# NI OSS SOURCE SNAPSHOT: grpc-device

<!--NI_OSS_SNAPSHOT repo=ni/grpc-device commit=13c1d30177e5da4b0c444b2ceab74506ca3847fb -->

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidaqmx/functions_addon.py sha256=e64ba600b1cba1b4fadf97d6ed50cd8329c5ba27b29bd802778d7ecf830ccf38 bytes=13381 -->
## FILE: source/codegen/metadata/nidaqmx/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidaqmx/functions_addon.py`
- sha256: `e64ba600b1cba1b4fadf97d6ed50cd8329c5ba27b29bd802778d7ecf830ccf38`
- bytes: 13381

````python
functions_override_metadata = {
    'ReadAnalogWaveforms': {
        'returns': 'int32',
        'codegen_method': 'CustomCodeNoLibrary',
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'numSampsPerChan',
                'python_data_type': 'int',
                'python_description': '',
                'python_type_annotation': 'int',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'timeout',
                'python_data_type': 'float',
                'python_default_value': '10.0',
                'python_description': 'Specifies the time in seconds to wait for the device to respond before timing out.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'WaveformAttributeMode',
                'is_optional_in_python': True,
                'name': 'waveformAttributeMode',
                'python_data_type': 'WaveformAttributeMode',
                'python_default_value': 'WaveformAttributeMode.NONE',
                'python_description': 'Specifies which waveform attributes to return with the waveforms.',
                'python_type_annotation': 'Optional[nidaqmx.constants.WaveformAttributeMode]',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'is_optional_in_python': False,
                'name': 'waveforms',
                'python_data_type': 'object',
                'python_description': 'The waveforms read from the specified channels.',
                'python_type_annotation': 'List[object]',
                'type': 'repeated ni.protobuf.types.DoubleAnalogWaveform'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'out',
                'is_optional_in_python': False,
                'is_streaming_type': True,
                'name': 'sampsPerChanRead',
                'python_data_type': 'int',
                'python_description': '',
                'python_type_annotation': 'int',
                'return_on_error_key': 'ni-samps-per-chan-read',
                'type': 'int32'
            }
        ]
    },
    'ReadDigitalWaveforms': {
        'returns': 'int32',
        'codegen_method': 'CustomCodeNoLibrary',
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'numSampsPerChan',
                'python_data_type': 'int',
                'python_description': '',
                'python_type_annotation': 'int',
                'type': 'int32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'timeout',
                'python_data_type': 'float',
                'python_default_value': '10.0',
                'python_description': 'Specifies the time in seconds to wait for the device to respond before timing out.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'in',
                'enum': 'WaveformAttributeMode',
                'is_optional_in_python': True,
                'name': 'waveformAttributeMode',
                'python_data_type': 'WaveformAttributeMode',
                'python_default_value': 'WaveformAttributeMode.NONE',
                'python_description': 'Specifies which waveform attributes to return with the waveforms.',
                'python_type_annotation': 'Optional[nidaqmx.constants.WaveformAttributeMode]',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'is_optional_in_python': False,
                'name': 'waveforms',
                'python_data_type': 'object',
                'python_description': 'The waveforms read from the specified channels.',
                'python_type_annotation': 'List[object]',
                'type': 'repeated ni.protobuf.types.DigitalWaveform'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'out',
                'is_optional_in_python': False,
                'is_streaming_type': True,
                'name': 'sampsPerChanRead',
                'python_data_type': 'int',
                'python_description': '',
                'python_type_annotation': 'int',
                'return_on_error_key': 'ni-samps-per-chan-read',
                'type': 'int32'
            }
        ]
    },
    'WriteAnalogWaveforms': {
        'returns': 'int32',
        'codegen_method': 'CustomCodeNoLibrary',
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_bool',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'autoStart',
                'python_data_type': 'bool',
                'python_default_value': 'False',
                'python_description': 'Specifies whether to automatically start the task after writing.',
                'python_type_annotation': 'Optional[bool]',
                'type': 'bool32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'timeout',
                'python_data_type': 'float',
                'python_default_value': '10.0',
                'python_description': 'Specifies the time in seconds to wait for the device to respond before timing out.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'waveforms',
                'python_data_type': 'object',
                'python_description': 'The waveforms to write to the specified channels.',
                'python_type_annotation': 'List[object]',
                'type': 'repeated ni.protobuf.types.DoubleAnalogWaveform'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'out',
                'is_optional_in_python': False,
                'is_streaming_type': True,
                'name': 'sampsPerChanWritten',
                'python_data_type': 'int',
                'python_description': '',
                'python_type_annotation': 'int',
                'return_on_error_key': 'ni-samps-per-chan-written',
                'type': 'int32'
            }
        ]
    },
    'WriteDigitalWaveforms': {
        'returns': 'int32',
        'codegen_method': 'CustomCodeNoLibrary',
        'parameters': [
            {
                'ctypes_data_type': 'ctypes.TaskHandle',
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'task',
                'python_data_type': 'TaskHandle',
                'python_description': '',
                'python_type_annotation': 'TaskHandle',
                'type': 'TaskHandle'
            },
            {
                'ctypes_data_type': 'ctypes.c_bool',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'autoStart',
                'python_data_type': 'bool',
                'python_default_value': 'False',
                'python_description': 'Specifies whether to start the task automatically.',
                'python_type_annotation': 'Optional[bool]',
                'type': 'bool32'
            },
            {
                'ctypes_data_type': 'ctypes.c_double',
                'direction': 'in',
                'is_optional_in_python': True,
                'name': 'timeout',
                'python_data_type': 'float',
                'python_default_value': '10.0',
                'python_description': 'Specifies the time in seconds to wait for the device to respond before timing out.',
                'python_type_annotation': 'Optional[float]',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'is_optional_in_python': False,
                'name': 'waveforms',
                'python_data_type': 'object',
                'python_description': 'The waveforms to write to the specified channels.',
                'python_type_annotation': 'List[object]',
                'type': 'repeated ni.protobuf.types.DigitalWaveform'
            },
            {
                'ctypes_data_type': 'ctypes.c_int',
                'direction': 'out',
                'is_optional_in_python': False,
                'is_streaming_type': True,
                'name': 'sampsPerChanWritten',
                'python_data_type': 'int',
                'python_description': '',
                'python_type_annotation': 'int',
                'return_on_error_key': 'ni-samps-per-chan-written',
                'type': 'int32'
            }
        ]
    }
}

functions_validation_suppressions = {
    'WriteCtrFreq': {
        'parameters': {
            # size is determined by numSampsPerChan and how many channels are in the task
            'frequency': ['ARRAY_PARAMETER_NEEDS_SIZE'],
            'dutyCycle': ['ARRAY_PARAMETER_NEEDS_SIZE'],
        }
    },
    'WriteCtrTicks': {
        'parameters': {
            # size is determined by numSampsPerChan and how many channels are in the task
            'highTicks': ['ARRAY_PARAMETER_NEEDS_SIZE'],
            'lowTicks': ['ARRAY_PARAMETER_NEEDS_SIZE'],
        }
    },
    'WriteCtrTime': {
        'parameters': {
            # size is determined by numSampsPerChan and how many channels are in the task
            'highTime': ['ARRAY_PARAMETER_NEEDS_SIZE'],
            'lowTime': ['ARRAY_PARAMETER_NEEDS_SIZE'],
        }
    },
    'InternalWriteDigitalWaveform': {
        'parameters': {
            # size is determined by numSampsPerChan and how many channels are in the task
            'writeArray': ['ARRAY_PARAMETER_NEEDS_SIZE'],
        }
    },
    'ReadAnalogWaveforms': {
        'parameters': {
            # size is determined by the Read.ChannelsToRead property
            'waveforms': ['ARRAY_PARAMETER_NEEDS_SIZE']
        }
    },
    'ReadDigitalWaveforms': {
        'parameters': {
            # size is determined by the Read.ChannelsToRead property
            'waveforms': ['ARRAY_PARAMETER_NEEDS_SIZE']
        }
    },
    'WriteAnalogWaveforms': {
        'parameters': {
            # size is determined by the Write.NumChans property
            'waveforms': ['ARRAY_PARAMETER_NEEDS_SIZE']
        }
    },
    'WriteDigitalWaveforms': {
        'parameters': {
            # size is determined by the Write.NumChans property
            'waveforms': ['ARRAY_PARAMETER_NEEDS_SIZE']
        }
    }
}

# size is determined by numSampsPerChan and how many channels are in the task
for function in ['WriteAnalogF64', 'WriteBinaryI16', 'WriteBinaryI32', 'WriteBinaryU16',
 'WriteBinaryU32', 'WriteDigitalLines', 'WriteDigitalU16', 'WriteDigitalU32', 'WriteDigitalU8',
 'WriteRaw']:
    functions_validation_suppressions[function] = {
        'parameters': {
            'writeArray': ['ARRAY_PARAMETER_NEEDS_SIZE']
        }
    }
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidcpower/__init__.py sha256=3f3177b9bfb8b1928720894e2452fe8decbd6707df63967cc881e20a7f8fb45a bytes=589 -->
## FILE: source/codegen/metadata/nidcpower/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidcpower/__init__.py`
- sha256: `3f3177b9bfb8b1928720894e2452fe8decbd6707df63967cc881e20a7f8fb45a`
- bytes: 589

````python
from .functions import functions
from .functions_addon import functions_override_metadata
from .attributes import attributes
from .attributes_addon import attributes_override_metadata
from .enums import enums
from .enums_addon import enums_override_metadata
from .config import config

metadata = {
    "functions" : functions,
    "attributes" : attributes,
    "enums" : enums,
    "config" : config
}

metadata['functions'].update(functions_override_metadata)
metadata['attributes'].update(attributes_override_metadata)
metadata['enums'].update(enums_override_metadata)
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidcpower/attributes.py sha256=60d83b40408747adb645816ba3505df1ae6afa193ce73318d9e63c5cdbf0f0a5 bytes=44650 -->
## FILE: source/codegen/metadata/nidcpower/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidcpower/attributes.py`
- sha256: `60d83b40408747adb645816ba3505df1ae6afa193ce73318d9e63c5cdbf0f0a5`
- bytes: 44650

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-DCPower API metadata version 23.0.0f517
attributes = {
    1050002: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'RANGE_CHECK',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050003: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'QUERY_INSTRUMENT_STATUS',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050004: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'CACHE',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050005: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'SIMULATE',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050006: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'RECORD_COERCIONS',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050007: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'DRIVER_SETUP',
        'resettable': False,
        'type': 'ViString'
    },
    1050021: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'INTERCHANGE_CHECK',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050203: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'CHANNEL_COUNT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050302: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SPECIFIC_DRIVER_PREFIX',
        'resettable': False,
        'type': 'ViString'
    },
    1050304: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'resettable': False,
        'type': 'ViString'
    },
    1050305: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'LOGICAL_NAME',
        'resettable': False,
        'type': 'ViString'
    },
    1050327: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'resettable': False,
        'type': 'ViString'
    },
    1050401: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'GROUP_CAPABILITIES',
        'resettable': False,
        'type': 'ViString'
    },
    1050510: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'resettable': False,
        'type': 'ViString'
    },
    1050511: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'INSTRUMENT_MANUFACTURER',
        'resettable': False,
        'type': 'ViString'
    },
    1050512: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'INSTRUMENT_MODEL',
        'resettable': False,
        'type': 'ViString'
    },
    1050513: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'resettable': False,
        'type': 'ViString'
    },
    1050514: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SPECIFIC_DRIVER_DESCRIPTION',
        'resettable': False,
        'type': 'ViString'
    },
    1050515: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050516: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050551: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SPECIFIC_DRIVER_REVISION',
        'resettable': False,
        'type': 'ViString'
    },
    1150000: {
        'codegen_method': 'public',
        'enum': 'PowerSource',
        'grpc_type': 'sint32',
        'name': 'POWER_SOURCE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150001: {
        'codegen_method': 'public',
        'enum': 'PowerSourceInUse',
        'grpc_type': 'sint32',
        'name': 'POWER_SOURCE_IN_USE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150002: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'AUXILIARY_POWER_SOURCE_AVAILABLE',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150003: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'SAMPLES_TO_AVERAGE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150004: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'CURRENT_LIMIT_RANGE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150005: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'VOLTAGE_LEVEL_RANGE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150006: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'RESET_AVERAGE_BEFORE_MEASUREMENT',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150007: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'OVERRANGING_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150008: {
        'codegen_method': 'public',
        'enum': 'OutputFunction',
        'grpc_type': 'sint32',
        'name': 'OUTPUT_FUNCTION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150009: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'CURRENT_LEVEL',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150010: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'VOLTAGE_LIMIT',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150011: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'CURRENT_LEVEL_RANGE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150012: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'VOLTAGE_LIMIT_RANGE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150013: {
        'codegen_method': 'public',
        'enum': 'Sense',
        'grpc_type': 'sint32',
        'name': 'SENSE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150014: {
        'codegen_method': 'public',
        'enum': 'OutputCapacitance',
        'grpc_type': 'sint32',
        'name': 'OUTPUT_CAPACITANCE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150015: {
        'codegen_method': 'public',
        'enum': 'AutoZero',
        'grpc_type': 'sint32',
        'name': 'VOLTAGE_LEVEL_AUTORANGE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150016: {
        'codegen_method': 'public',
        'enum': 'AutoZero',
        'grpc_type': 'sint32',
        'name': 'CURRENT_LIMIT_AUTORANGE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150017: {
        'codegen_method': 'public',
        'enum': 'AutoZero',
        'grpc_type': 'sint32',
        'name': 'CURRENT_LEVEL_AUTORANGE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150018: {
        'codegen_method': 'public',
        'enum': 'AutoZero',
        'grpc_type': 'sint32',
        'name': 'VOLTAGE_LIMIT_AUTORANGE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150020: {
        'codegen_method': 'public',
        'enum': 'PowerLineFrequencies',
        'grpc_type': 'double',
        'name': 'POWER_LINE_FREQUENCY',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150021: {
        'codegen_method': 'public',
        'enum': 'TriggerType',
        'grpc_type': 'sint32',
        'name': 'START_TRIGGER_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150022: {
        'codegen_method': 'public',
        'enum': 'DigitalEdge',
        'grpc_type': 'sint32',
        'name': 'DIGITAL_EDGE_START_TRIGGER_EDGE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150023: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    1150024: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'EXPORTED_START_TRIGGER_OUTPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    1150025: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'SEQUENCE_LOOP_COUNT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150026: {
        'codegen_method': 'public',
        'enum': 'TriggerType',
        'grpc_type': 'sint32',
        'name': 'SEQUENCE_ADVANCE_TRIGGER_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150027: {
        'codegen_method': 'public',
        'enum': 'DigitalEdge',
        'grpc_type': 'sint32',
        'name': 'DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150028: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_INPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    1150029: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'EXPORTED_SEQUENCE_ADVANCE_TRIGGER_OUTPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    1150030: {
        'codegen_method': 'public',
        'enum': 'TriggerType',
        'grpc_type': 'sint32',
        'name': 'SOURCE_TRIGGER_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150031: {
        'codegen_method': 'public',
        'enum': 'DigitalEdge',
        'grpc_type': 'sint32',
        'name': 'DIGITAL_EDGE_SOURCE_TRIGGER_EDGE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150032: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'DIGITAL_EDGE_SOURCE_TRIGGER_INPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    1150033: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    1150034: {
        'codegen_method': 'public',
        'enum': 'TriggerType',
        'grpc_type': 'sint32',
        'name': 'MEASURE_TRIGGER_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150035: {
        'codegen_method': 'public',
        'enum': 'DigitalEdge',
        'grpc_type': 'sint32',
        'name': 'DIGITAL_EDGE_MEASURE_TRIGGER_EDGE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150036: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'DIGITAL_EDGE_MEASURE_TRIGGER_INPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    1150037: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'EXPORTED_MEASURE_TRIGGER_OUTPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    1150038: {
        'codegen_method': 'public',
        'enum': 'Polarity',
        'grpc_type': 'sint32',
        'name': 'SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_POLARITY',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150039: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_WIDTH',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150040: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    1150041: {
        'codegen_method': 'public',
        'enum': 'Polarity',
        'grpc_type': 'sint32',
        'name': 'SOURCE_COMPLETE_EVENT_PULSE_POLARITY',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150042: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'SOURCE_COMPLETE_EVENT_PULSE_WIDTH',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150043: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SOURCE_COMPLETE_EVENT_OUTPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    1150044: {
        'codegen_method': 'public',
        'enum': 'Polarity',
        'grpc_type': 'sint32',
        'name': 'MEASURE_COMPLETE_EVENT_PULSE_POLARITY',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150045: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MEASURE_COMPLETE_EVENT_PULSE_WIDTH',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150046: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MEASURE_COMPLETE_EVENT_DELAY',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150047: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'MEASURE_COMPLETE_EVENT_OUTPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    1150048: {
        'codegen_method': 'public',
        'enum': 'Polarity',
        'grpc_type': 'sint32',
        'name': 'SEQUENCE_ENGINE_DONE_EVENT_PULSE_POLARITY',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150049: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'SEQUENCE_ENGINE_DONE_EVENT_PULSE_WIDTH',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150050: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    1150051: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'SOURCE_DELAY',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150054: {
        'codegen_method': 'public',
        'enum': 'SourceMode',
        'grpc_type': 'sint32',
        'name': 'SOURCE_MODE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150055: {
        'codegen_method': 'public',
        'enum': 'AutoZero',
        'grpc_type': 'sint32',
        'name': 'AUTO_ZERO',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150056: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'FETCH_BACKLOG',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150057: {
        'codegen_method': 'public',
        'enum': 'MeasureWhen',
        'grpc_type': 'sint32',
        'name': 'MEASURE_WHEN',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150058: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'APERTURE_TIME',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150059: {
        'codegen_method': 'public',
        'enum': 'ApertureTimeUnits',
        'grpc_type': 'sint32',
        'name': 'APERTURE_TIME_UNITS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150060: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'OUTPUT_CONNECTED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150061: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OUTPUT_RESISTANCE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150062: {
        'codegen_method': 'public',
        'enum': 'TransientResponse',
        'grpc_type': 'sint32',
        'name': 'TRANSIENT_RESPONSE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150063: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'MEASURE_RECORD_LENGTH',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150064: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'MEASURE_RECORD_LENGTH_IS_FINITE',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150065: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MEASURE_RECORD_DELTA_TIME',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150066: {
        'codegen_method': 'public',
        'enum': 'DCNoiseRejection',
        'grpc_type': 'sint32',
        'name': 'DC_NOISE_REJECTION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150067: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'VOLTAGE_GAIN_BANDWIDTH',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150068: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'VOLTAGE_COMPENSATION_FREQUENCY',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150069: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'VOLTAGE_POLE_ZERO_RATIO',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150070: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'CURRENT_GAIN_BANDWIDTH',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150071: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'CURRENT_COMPENSATION_FREQUENCY',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150072: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'CURRENT_POLE_ZERO_RATIO',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150073: {
        'codegen_method': 'public',
        'enum': 'SelfCalibrationPersistence',
        'grpc_type': 'sint32',
        'name': 'SELF_CALIBRATION_PERSISTENCE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150074: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'ACTIVE_ADVANCED_SEQUENCE',
        'resettable': False,
        'type': 'ViString'
    },
    1150075: {
        'codegen_method': 'public',
        'grpc_type': 'int64',
        'name': 'ACTIVE_ADVANCED_SEQUENCE_STEP',
        'resettable': False,
        'type': 'ViInt64'
    },
    1150077: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'MEASURE_BUFFER_SIZE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150078: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'SEQUENCE_LOOP_COUNT_IS_FINITE',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150079: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'SUPPORT_OUTPUT_DMA',
        'resettable': False,
        'type': 'bool'
    },
    1150080: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PULSE_VOLTAGE_LEVEL',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150081: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PULSE_CURRENT_LIMIT',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150082: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PULSE_BIAS_VOLTAGE_LEVEL',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150083: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PULSE_BIAS_CURRENT_LIMIT',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150084: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PULSE_VOLTAGE_LEVEL_RANGE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150085: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PULSE_CURRENT_LIMIT_RANGE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150086: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PULSE_CURRENT_LEVEL',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150087: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PULSE_VOLTAGE_LIMIT',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150088: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PULSE_BIAS_CURRENT_LEVEL',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150089: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PULSE_BIAS_VOLTAGE_LIMIT',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150090: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PULSE_CURRENT_LEVEL_RANGE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150091: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PULSE_VOLTAGE_LIMIT_RANGE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150092: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PULSE_BIAS_DELAY',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150093: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PULSE_ON_TIME',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150094: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PULSE_OFF_TIME',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150095: {
        'codegen_method': 'public',
        'enum': 'TriggerType',
        'grpc_type': 'sint32',
        'name': 'PULSE_TRIGGER_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150096: {
        'codegen_method': 'public',
        'enum': 'DigitalEdge',
        'grpc_type': 'sint32',
        'name': 'DIGITAL_EDGE_PULSE_TRIGGER_EDGE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150097: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'DIGITAL_EDGE_PULSE_TRIGGER_INPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    1150098: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'EXPORTED_PULSE_TRIGGER_OUTPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    1150099: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'PULSE_COMPLETE_EVENT_OUTPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    1150100: {
        'codegen_method': 'public',
        'enum': 'Polarity',
        'grpc_type': 'sint32',
        'name': 'PULSE_COMPLETE_EVENT_PULSE_POLARITY',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150101: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PULSE_COMPLETE_EVENT_PULSE_WIDTH',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150102: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'READY_FOR_PULSE_TRIGGER_EVENT_OUTPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    1150103: {
        'codegen_method': 'public',
        'enum': 'Polarity',
        'grpc_type': 'sint32',
        'name': 'READY_FOR_PULSE_TRIGGER_EVENT_PULSE_POLARITY',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150104: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'READY_FOR_PULSE_TRIGGER_EVENT_PULSE_WIDTH',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150105: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'INTERLOCK_INPUT_OPEN',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150110: {
        'codegen_method': 'public',
        'grpc_type': 'int64',
        'name': 'INSTRUMENT_API_SESSION_HANDLE',
        'resettable': False,
        'type': 'ViInt64'
    },
    1150111: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'WAS_SESSION_OPENED_BY_INITIALIZE_WITH_INDEPENDENT_CHANNELS',
        'resettable': False,
        'type': 'bool'
    },
    1150152: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SERIAL_NUMBER',
        'resettable': False,
        'type': 'ViString'
    },
    1150184: {
        'codegen_method': 'public',
        'enum': 'ComplianceLimitSymmetry',
        'grpc_type': 'sint32',
        'name': 'COMPLIANCE_LIMIT_SYMMETRY',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150185: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'VOLTAGE_LIMIT_HIGH',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150186: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'VOLTAGE_LIMIT_LOW',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150187: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'CURRENT_LIMIT_HIGH',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150188: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'CURRENT_LIMIT_LOW',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150189: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PULSE_VOLTAGE_LIMIT_HIGH',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150190: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PULSE_VOLTAGE_LIMIT_LOW',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150191: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PULSE_BIAS_VOLTAGE_LIMIT_HIGH',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150192: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PULSE_BIAS_VOLTAGE_LIMIT_LOW',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150193: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PULSE_CURRENT_LIMIT_HIGH',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150194: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PULSE_CURRENT_LIMIT_LOW',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150195: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PULSE_BIAS_CURRENT_LIMIT_HIGH',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150196: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PULSE_BIAS_CURRENT_LIMIT_LOW',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150198: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'SEQUENCE_STEP_DELTA_TIME',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150199: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'SEQUENCE_STEP_DELTA_TIME_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150200: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OCP_ERROR_PERCENTAGE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150205: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'ACTUAL_POWER_ALLOCATION',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150206: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'REQUESTED_POWER_ALLOCATION',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150207: {
        'codegen_method': 'public',
        'enum': 'PowerAllocationMode',
        'grpc_type': 'sint32',
        'name': 'POWER_ALLOCATION_MODE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150208: {
        'codegen_method': 'public',
        'enum': 'InstrumentMode',
        'grpc_type': 'sint32',
        'name': 'INSTRUMENT_MODE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150209: {
        'codegen_method': 'public',
        'enum': 'LCRStimulusFunction',
        'grpc_type': 'sint32',
        'name': 'LCR_STIMULUS_FUNCTION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150210: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'LCR_FREQUENCY',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150211: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'LCR_VOLTAGE_AMPLITUDE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150212: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'LCR_CURRENT_AMPLITUDE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150213: {
        'codegen_method': 'public',
        'enum': 'LCRDCBiasSource',
        'grpc_type': 'sint32',
        'name': 'LCR_DC_BIAS_SOURCE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150214: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'LCR_DC_BIAS_VOLTAGE_LEVEL',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150215: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'LCR_DC_BIAS_CURRENT_LEVEL',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150216: {
        'codegen_method': 'public',
        'enum': 'LCRImpedanceAutoRange',
        'grpc_type': 'sint32',
        'name': 'LCR_IMPEDANCE_AUTO_RANGE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150217: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'LCR_IMPEDANCE_RANGE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150218: {
        'codegen_method': 'public',
        'enum': 'LCRMeasurementTime',
        'grpc_type': 'sint32',
        'name': 'LCR_MEASUREMENT_TIME',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150220: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'LCR_OPEN_COMPENSATION_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150221: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'LCR_SHORT_COMPENSATION_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150222: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'LCR_LOAD_COMPENSATION_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150223: {
        'codegen_method': 'public',
        'enum': 'LCROpenShortLoadCompensationDataSource',
        'grpc_type': 'sint32',
        'name': 'LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150235: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'OUTPUT_CUTOFF_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150236: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_HIGH',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150237: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_HIGH',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150238: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_LOW',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150239: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_LOW',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150240: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'OUTPUT_CUTOFF_CURRENT_OVERRANGE_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150244: {
        'codegen_method': 'public',
        'enum': 'AutoZero',
        'grpc_type': 'sint32',
        'name': 'AUTORANGE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150245: {
        'codegen_method': 'public',
        'enum': 'AutorangeBehavior',
        'grpc_type': 'sint32',
        'name': 'AUTORANGE_BEHAVIOR',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150246: {
        'codegen_method': 'public',
        'enum': 'AutorangeApertureTimeMode',
        'grpc_type': 'sint32',
        'name': 'AUTORANGE_APERTURE_TIME_MODE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150247: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'AUTORANGE_MINIMUM_APERTURE_TIME',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150248: {
        'codegen_method': 'public',
        'enum': 'ApertureTimeUnits',
        'grpc_type': 'sint32',
        'name': 'AUTORANGE_MINIMUM_APERTURE_TIME_UNITS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150249: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'MERGED_CHANNELS',
        'resettable': False,
        'type': 'ViString'
    },
    1150255: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'AUTORANGE_MINIMUM_CURRENT_RANGE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150256: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'AUTORANGE_MINIMUM_VOLTAGE_RANGE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150257: {
        'codegen_method': 'public',
        'enum': 'AutorangeThresholdMode',
        'grpc_type': 'sint32',
        'name': 'AUTORANGE_THRESHOLD_MODE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150258: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'LCR_CUSTOM_MEASUREMENT_TIME',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150259: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'ACTUAL_VOLTAGE_RANGE_FOR_LAST_FETCH',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150260: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'ACTUAL_CURRENT_RANGE_FOR_LAST_FETCH',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150261: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'LCR_OPEN_CONDUCTANCE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150262: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'LCR_OPEN_SUSCEPTANCE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150263: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'LCR_SHORT_RESISTANCE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150264: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'LCR_SHORT_REACTANCE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150265: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'LCR_VOLTAGE_RANGE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150266: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'LCR_DC_BIAS_VOLTAGE_RANGE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150267: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'LCR_CURRENT_RANGE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150268: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'LCR_MEASURED_LOAD_RESISTANCE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150269: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'LCR_MEASURED_LOAD_REACTANCE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150270: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'LCR_ACTUAL_LOAD_RESISTANCE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150271: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'LCR_ACTUAL_LOAD_REACTANCE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150274: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'LCR_DC_BIAS_CURRENT_RANGE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150275: {
        'codegen_method': 'public',
        'enum': 'TriggerType',
        'grpc_type': 'sint32',
        'name': 'SHUTDOWN_TRIGGER_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150276: {
        'codegen_method': 'public',
        'enum': 'DigitalEdge',
        'grpc_type': 'sint32',
        'name': 'DIGITAL_EDGE_SHUTDOWN_TRIGGER_EDGE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150277: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'DIGITAL_EDGE_SHUTDOWN_TRIGGER_INPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    1150278: {
        'codegen_method': 'public',
        'enum': 'CableLength',
        'grpc_type': 'sint32',
        'name': 'CABLE_LENGTH',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150290: {
        'codegen_method': 'public',
        'enum': 'LCRAutomaticLevelControl',
        'grpc_type': 'sint32',
        'name': 'LCR_AUTOMATIC_LEVEL_CONTROL',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150291: {
        'codegen_method': 'public',
        'enum': 'LCRAutomaticLevelControl',
        'grpc_type': 'sint32',
        'name': 'LCR_DC_BIAS_AUTOMATIC_LEVEL_CONTROL',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150292: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_LOW',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150293: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_LOW',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150294: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_HIGH',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150295: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_HIGH',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150299: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'LCR_SHORT_CUSTOM_CABLE_COMPENSATION_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150300: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OUTPUT_CUTOFF_DELAY',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150302: {
        'codegen_method': 'public',
        'enum': 'IsolationState',
        'grpc_type': 'sint32',
        'name': 'ISOLATION_STATE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150314: {
        'codegen_method': 'public',
        'enum': 'ApertureTimeAutoMode',
        'grpc_type': 'sint32',
        'name': 'APERTURE_TIME_AUTO_MODE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150315: {
        'codegen_method': 'public',
        'enum': 'LCRSourceDelayMode',
        'grpc_type': 'sint32',
        'name': 'LCR_SOURCE_DELAY_MODE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150318: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'LCR_LOAD_RESISTANCE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150319: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'LCR_LOAD_INDUCTANCE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150320: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'LCR_LOAD_CAPACITANCE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150321: {
        'codegen_method': 'public',
        'enum': 'LCRImpedanceRangeSource',
        'grpc_type': 'sint32',
        'name': 'LCR_IMPEDANCE_RANGE_SOURCE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150322: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'AUTORANGE_MAXIMUM_DELAY_AFTER_RANGE_CHANGE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250001: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'VOLTAGE_LEVEL',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250002: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'OVP_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1250003: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OVP_LIMIT',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250004: {
        'codegen_method': 'public',
        'enum': 'CurrentLimitBehavior',
        'grpc_type': 'sint32',
        'name': 'CURRENT_LIMIT_BEHAVIOR',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250005: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'CURRENT_LIMIT',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250006: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'OUTPUT_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidcpower/attributes_addon.py sha256=cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f bytes=207 -->
## FILE: source/codegen/metadata/nidcpower/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidcpower/attributes_addon.py`
- sha256: `cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f`
- bytes: 207

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidcpower/config.py sha256=e2ceeb6d2101974854d3ea8f121b4e81a4abd3cfd5d22e64f2f97f6ee1017c23 bytes=6106 -->
## FILE: source/codegen/metadata/nidcpower/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidcpower/config.py`
- sha256: `e2ceeb6d2101974854d3ea8f121b4e81a4abd3cfd5d22e64f2f97f6ee1017c23`
- bytes: 6106

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-DCPower API metadata version 23.0.0f517
config = {
    'additional_headers': {
        'custom/ivi_errors.h': [
            'service.cpp'
        ]
    },
    'api_version': '23.0.0f517',
    'c_function_prefix': 'niDCPower_',
    'c_header': 'nidcpower.h',
    'close_function': 'Close',
    'csharp_namespace': 'NationalInstruments.Grpc.DCPower',
    'custom_types': [
        {
            'fields': [
                {
                    'grpc_type': 'double',
                    'name': 'frequency',
                    'type': 'ViReal64'
                },
                {
                    'grpc_type': 'sint32',
                    'name': 'referenceValueType',
                    'type': 'ViInt32'
                },
                {
                    'grpc_type': 'double',
                    'name': 'referenceValueA',
                    'type': 'ViReal64'
                },
                {
                    'grpc_type': 'double',
                    'name': 'referenceValueB',
                    'type': 'ViReal64'
                }
            ],
            'grpc_name': 'NILCRLoadCompensationSpot',
            'name': 'NILCRLoadCompensationSpot_struct'
        },
        {
            'fields': [
                {
                    'grpc_type': 'double',
                    'name': 'Vdc',
                    'type': 'ViReal64'
                },
                {
                    'grpc_type': 'double',
                    'name': 'Idc',
                    'type': 'ViReal64'
                },
                {
                    'grpc_type': 'double',
                    'name': 'stimulusFrequency',
                    'type': 'ViReal64'
                },
                {
                    'grpc_type': 'nidevice_grpc.NIComplexNumber',
                    'name': 'ACVoltage',
                    'type': 'struct NIComplexNumber_struct'
                },
                {
                    'grpc_type': 'nidevice_grpc.NIComplexNumber',
                    'name': 'ACCurrent',
                    'type': 'struct NIComplexNumber_struct'
                },
                {
                    'grpc_type': 'nidevice_grpc.NIComplexNumber',
                    'name': 'Z',
                    'type': 'struct NIComplexNumber_struct'
                },
                {
                    'grpc_type': 'double',
                    'name': 'ZMagnitude',
                    'type': 'ViReal64'
                },
                {
                    'grpc_type': 'double',
                    'name': 'ZPhase',
                    'type': 'ViReal64'
                },
                {
                    'grpc_type': 'nidevice_grpc.NIComplexNumber',
                    'name': 'Y',
                    'type': 'struct NIComplexNumber_struct'
                },
                {
                    'grpc_type': 'double',
                    'name': 'YMagnitude',
                    'type': 'ViReal64'
                },
                {
                    'grpc_type': 'double',
                    'name': 'YPhase',
                    'type': 'ViReal64'
                },
                {
                    'grpc_type': 'double',
                    'name': 'Ls',
                    'type': 'ViReal64'
                },
                {
                    'grpc_type': 'double',
                    'name': 'Cs',
                    'type': 'ViReal64'
                },
                {
                    'grpc_type': 'double',
                    'name': 'Rs',
                    'type': 'ViReal64'
                },
                {
                    'grpc_type': 'double',
                    'name': 'Lp',
                    'type': 'ViReal64'
                },
                {
                    'grpc_type': 'double',
                    'name': 'Cp',
                    'type': 'ViReal64'
                },
                {
                    'grpc_type': 'double',
                    'name': 'Rp',
                    'type': 'ViReal64'
                },
                {
                    'grpc_type': 'double',
                    'name': 'D',
                    'type': 'ViReal64'
                },
                {
                    'grpc_type': 'double',
                    'name': 'Q',
                    'type': 'ViReal64'
                },
                {
                    'grpc_type': 'uint32',
                    'name': 'measurementMode',
                    'type': 'ViUInt16'
                },
                {
                    'grpc_type': 'bool',
                    'name': 'dcInCompliance',
                    'type': 'ViBoolean'
                },
                {
                    'grpc_type': 'bool',
                    'name': 'acInCompliance',
                    'type': 'ViBoolean'
                },
                {
                    'grpc_type': 'bool',
                    'name': 'unbalanced',
                    'type': 'ViBoolean'
                }
            ],
            'grpc_name': 'NILCRMeasurement',
            'name': 'NILCRMeasurement_struct'
        }
    ],
    'driver_name': 'NI-DCPower',
    'java_package': 'com.ni.grpc.dcpower',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nidcpower',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'nidcpower_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'nidcpower_64.dll',
                'type': 'cdll'
            }
        }
    },
    'linux_rt_support': True,
    'module_name': 'nidcpower',
    'namespace_component': 'nidcpower',
    'service_class_prefix': 'NiDCPower',
    'session_handle_parameter_name': 'vi',
    'status_ok': 'status >= 0'
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidcpower/config_addon.py sha256=abf413baa866d858086e8dee0672b89a95d3c86014763be60855b1472e9e80e0 bytes=226 -->
## FILE: source/codegen/metadata/nidcpower/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidcpower/config_addon.py`
- sha256: `abf413baa866d858086e8dee0672b89a95d3c86014763be60855b1472e9e80e0`
- bytes: 226

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.4.dev0',
    'latest_runtime_version_tested_against': '20.6.0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidcpower/enums.py sha256=3e6bf5275a89ac9356d97902c1c40c7cc861037ebfa240b131098dbc3b4e3260 bytes=33578 -->
## FILE: source/codegen/metadata/nidcpower/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidcpower/enums.py`
- sha256: `3e6bf5275a89ac9356d97902c1c40c7cc861037ebfa240b131098dbc3b4e3260`
- bytes: 33578

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-DCPower API metadata version 23.0.0f517
enums = {
    'ApertureTimeAutoMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_APERTURE_TIME_AUTO_MODE_OFF',
                'value': 1135
            },
            {
                'name': 'NIDCPOWER_VAL_APERTURE_TIME_AUTO_MODE_SHORT',
                'value': 1136
            },
            {
                'name': 'NIDCPOWER_VAL_APERTURE_TIME_AUTO_MODE_NORMAL',
                'value': 1137
            },
            {
                'name': 'NIDCPOWER_VAL_APERTURE_TIME_AUTO_MODE_LONG',
                'value': 1138
            }
        ]
    },
    'ApertureTimeUnits': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_SECONDS',
                'value': 1028
            },
            {
                'name': 'NIDCPOWER_VAL_POWER_LINE_CYCLES',
                'value': 1029
            }
        ]
    },
    'AutoZero': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_OFF',
                'value': 0
            },
            {
                'name': 'NIDCPOWER_VAL_ON',
                'value': 1
            },
            {
                'name': 'NIDCPOWER_VAL_ONCE',
                'value': 1024
            }
        ]
    },
    'AutorangeApertureTimeMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_APERTURE_TIME_AUTO',
                'value': 1110
            },
            {
                'name': 'NIDCPOWER_VAL_APERTURE_TIME_CUSTOM',
                'value': 1111
            }
        ]
    },
    'AutorangeBehavior': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_RANGE_UP_TO_LIMIT_THEN_DOWN',
                'value': 1107
            },
            {
                'name': 'NIDCPOWER_VAL_RANGE_UP',
                'value': 1108
            },
            {
                'name': 'NIDCPOWER_VAL_RANGE_UP_AND_DOWN',
                'value': 1109
            }
        ]
    },
    'AutorangeThresholdMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_THRESHOLD_MODE_NORMAL',
                'value': 1112
            },
            {
                'name': 'NIDCPOWER_VAL_THRESHOLD_MODE_FAST_STEP',
                'value': 1113
            },
            {
                'name': 'NIDCPOWER_VAL_THRESHOLD_MODE_HIGH_HYSTERESIS',
                'value': 1114
            },
            {
                'name': 'NIDCPOWER_VAL_THRESHOLD_MODE_MEDIUM_HYSTERESIS',
                'value': 1115
            },
            {
                'name': 'NIDCPOWER_VAL_THRESHOLD_MODE_HOLD',
                'value': 1116
            }
        ]
    },
    'CableLength': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_ZERO_M',
                'value': 1121
            },
            {
                'name': 'NIDCPOWER_VAL_NI_STANDARD_1M',
                'value': 1122
            },
            {
                'name': 'NIDCPOWER_VAL_NI_STANDARD_2M',
                'value': 1123
            },
            {
                'name': 'NIDCPOWER_VAL_NI_STANDARD_4M',
                'value': 1124
            },
            {
                'name': 'NIDCPOWER_VAL_CUSTOM_ONBOARD_STORAGE',
                'value': 1125
            },
            {
                'name': 'NIDCPOWER_VAL_CUSTOM_AS_CONFIGURED',
                'value': 1126
            },
            {
                'name': 'NIDCPOWER_VAL_NI_STANDARD_TRIAXIAL_1M',
                'value': 1139
            },
            {
                'name': 'NIDCPOWER_VAL_NI_STANDARD_TRIAXIAL_2M',
                'value': 1140
            },
            {
                'name': 'NIDCPOWER_VAL_NI_STANDARD_TRIAXIAL_4M',
                'value': 1141
            }
        ]
    },
    'ComplianceLimitSymmetry': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_SYMMETRIC',
                'value': 0
            },
            {
                'name': 'NIDCPOWER_VAL_ASYMMETRIC',
                'value': 1
            }
        ]
    },
    'CurrentLimitBehavior': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_CURRENT_REGULATE',
                'value': 0
            },
            {
                'name': 'NIDCPOWER_VAL_CURRENT_TRIP',
                'value': 1
            }
        ]
    },
    'DCNoiseRejection': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_DC_NOISE_REJECTION_SECOND_ORDER',
                'value': 1043
            },
            {
                'name': 'NIDCPOWER_VAL_DC_NOISE_REJECTION_NORMAL',
                'value': 1044
            }
        ]
    },
    'DigitalEdge': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_RISING',
                'value': 1016
            },
            {
                'name': 'NIDCPOWER_VAL_FALLING',
                'value': 1017
            }
        ]
    },
    'Event': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_SOURCE_COMPLETE',
                'value': 1030
            },
            {
                'name': 'NIDCPOWER_VAL_MEASURE_COMPLETE',
                'value': 1031
            },
            {
                'name': 'NIDCPOWER_VAL_SEQUENCE_ITERATION_COMPLETE',
                'value': 1032
            },
            {
                'name': 'NIDCPOWER_VAL_SEQUENCE_ENGINE_DONE',
                'value': 1033
            },
            {
                'name': 'NIDCPOWER_VAL_PULSE_COMPLETE',
                'value': 1051
            },
            {
                'name': 'NIDCPOWER_VAL_READY_FOR_PULSE_TRIGGER',
                'value': 1052
            }
        ]
    },
    'ExportSignal': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_SOURCE_COMPLETE_EVENT',
                'value': 1030
            },
            {
                'name': 'NIDCPOWER_VAL_MEASURE_COMPLETE_EVENT',
                'value': 1031
            },
            {
                'name': 'NIDCPOWER_VAL_SEQUENCE_ITERATION_COMPLETE_EVENT',
                'value': 1032
            },
            {
                'name': 'NIDCPOWER_VAL_SEQUENCE_ENGINE_DONE_EVENT',
                'value': 1033
            },
            {
                'name': 'NIDCPOWER_VAL_PULSE_COMPLETE_EVENT',
                'value': 1051
            },
            {
                'name': 'NIDCPOWER_VAL_READY_FOR_PULSE_TRIGGER_EVENT',
                'value': 1052
            },
            {
                'name': 'NIDCPOWER_VAL_START_TRIGGER',
                'value': 1034
            },
            {
                'name': 'NIDCPOWER_VAL_SOURCE_TRIGGER',
                'value': 1035
            },
            {
                'name': 'NIDCPOWER_VAL_MEASURE_TRIGGER',
                'value': 1036
            },
            {
                'name': 'NIDCPOWER_VAL_SEQUENCE_ADVANCE_TRIGGER',
                'value': 1037
            },
            {
                'name': 'NIDCPOWER_VAL_PULSE_TRIGGER',
                'value': 1053
            },
            {
                'name': 'NIDCPOWER_VAL_SHUTDOWN_TRIGGER',
                'value': 1118
            }
        ]
    },
    'InstrumentMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_SMU_PS',
                'value': 1061
            },
            {
                'name': 'NIDCPOWER_VAL_LCR',
                'value': 1062
            }
        ]
    },
    'IsolationState': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_ISOLATED',
                'value': 1128
            },
            {
                'name': 'NIDCPOWER_VAL_NON_ISOLATED',
                'value': 1129
            }
        ]
    },
    'LCRAutomaticLevelControl': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_OFF',
                'value': 0
            },
            {
                'name': 'NIDCPOWER_VAL_ON',
                'value': 1
            }
        ]
    },
    'LCRCompensationType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_OPEN_COMPENSATION',
                'value': 1130
            },
            {
                'name': 'NIDCPOWER_VAL_SHORT_COMPENSATION',
                'value': 1131
            },
            {
                'name': 'NIDCPOWER_VAL_LOAD_COMPENSATION',
                'value': 1132
            },
            {
                'name': 'NIDCPOWER_VAL_OPEN_CUSTOM_CABLE_COMPENSATION',
                'value': 1133
            },
            {
                'name': 'NIDCPOWER_VAL_SHORT_CUSTOM_CABLE_COMPENSATION',
                'value': 1134
            }
        ]
    },
    'LCRDCBiasSource': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_DC_BIAS_OFF',
                'value': 1065
            },
            {
                'name': 'NIDCPOWER_VAL_DC_BIAS_VOLTAGE',
                'value': 1066
            },
            {
                'name': 'NIDCPOWER_VAL_DC_BIAS_CURRENT',
                'value': 1067
            }
        ]
    },
    'LCRImpedanceAutoRange': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_AUTO_RANGE_OFF',
                'value': 1068
            },
            {
                'name': 'NIDCPOWER_VAL_AUTO_RANGE_ON',
                'value': 1070
            }
        ]
    },
    'LCRImpedanceRangeSource': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_LCR_IMPEDANCE_RANGE',
                'value': 1142
            },
            {
                'name': 'NIDCPOWER_VAL_LCR_LOAD_CONFIGURATION',
                'value': 1143
            }
        ]
    },
    'LCRMeasurementTime': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_MEASUREMENT_TIME_SHORT',
                'value': 1071
            },
            {
                'name': 'NIDCPOWER_VAL_MEASUREMENT_TIME_MEDIUM',
                'value': 1072
            },
            {
                'name': 'NIDCPOWER_VAL_MEASUREMENT_TIME_LONG',
                'value': 1073
            },
            {
                'name': 'NIDCPOWER_VAL_MEASUREMENT_TIME_CUSTOM',
                'value': 1117
            }
        ]
    },
    'LCROpenShortLoadCompensationDataSource': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_ONBOARD_STORAGE',
                'value': 1074
            },
            {
                'name': 'NIDCPOWER_VAL_AS_DEFINED',
                'value': 1075
            },
            {
                'name': 'NIDCPOWER_VAL_AS_CONFIGURED',
                'value': 1146
            }
        ]
    },
    'LCRSourceDelayMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_LCR_SOURCE_DELAY_MODE_AUTOMATIC',
                'value': 1144
            },
            {
                'name': 'NIDCPOWER_VAL_LCR_SOURCE_DELAY_MODE_MANUAL',
                'value': 1145
            }
        ]
    },
    'LCRStimulusFunction': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_AC_VOLTAGE',
                'value': 1063
            },
            {
                'name': 'NIDCPOWER_VAL_AC_CURRENT',
                'value': 1064
            }
        ]
    },
    'MeasureWhen': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE',
                'value': 1025
            },
            {
                'name': 'NIDCPOWER_VAL_ON_DEMAND',
                'value': 1026
            },
            {
                'name': 'NIDCPOWER_VAL_ON_MEASURE_TRIGGER',
                'value': 1027
            }
        ]
    },
    'MeasurementTypes': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_MEASURE_CURRENT',
                'value': 0
            },
            {
                'name': 'NIDCPOWER_VAL_MEASURE_VOLTAGE',
                'value': 1
            }
        ]
    },
    'NiDCPowerInt32AttributeValues': {
        'enum-value-prefix': 'NIDCPOWER_INT32',
        'generate-mappings': False,
        'values': [
            {
                'name': 'APERTURE_TIME_AUTO_MODE_VAL_APERTURE_TIME_AUTO_MODE_OFF',
                'value': 1135
            },
            {
                'name': 'APERTURE_TIME_AUTO_MODE_VAL_APERTURE_TIME_AUTO_MODE_SHORT',
                'value': 1136
            },
            {
                'name': 'APERTURE_TIME_AUTO_MODE_VAL_APERTURE_TIME_AUTO_MODE_NORMAL',
                'value': 1137
            },
            {
                'name': 'APERTURE_TIME_AUTO_MODE_VAL_APERTURE_TIME_AUTO_MODE_LONG',
                'value': 1138
            },
            {
                'name': 'APERTURE_TIME_UNITS_VAL_SECONDS',
                'value': 1028
            },
            {
                'name': 'APERTURE_TIME_UNITS_VAL_POWER_LINE_CYCLES',
                'value': 1029
            },
            {
                'name': 'AUTO_ZERO_VAL_OFF',
                'value': 0
            },
            {
                'name': 'AUTO_ZERO_VAL_ON',
                'value': 1
            },
            {
                'name': 'AUTO_ZERO_VAL_ONCE',
                'value': 1024
            },
            {
                'name': 'AUTORANGE_APERTURE_TIME_MODE_VAL_APERTURE_TIME_AUTO',
                'value': 1110
            },
            {
                'name': 'AUTORANGE_APERTURE_TIME_MODE_VAL_APERTURE_TIME_CUSTOM',
                'value': 1111
            },
            {
                'name': 'AUTORANGE_BEHAVIOR_VAL_RANGE_UP_TO_LIMIT_THEN_DOWN',
                'value': 1107
            },
            {
                'name': 'AUTORANGE_BEHAVIOR_VAL_RANGE_UP',
                'value': 1108
            },
            {
                'name': 'AUTORANGE_BEHAVIOR_VAL_RANGE_UP_AND_DOWN',
                'value': 1109
            },
            {
                'name': 'AUTORANGE_THRESHOLD_MODE_VAL_THRESHOLD_MODE_NORMAL',
                'value': 1112
            },
            {
                'name': 'AUTORANGE_THRESHOLD_MODE_VAL_THRESHOLD_MODE_FAST_STEP',
                'value': 1113
            },
            {
                'name': 'AUTORANGE_THRESHOLD_MODE_VAL_THRESHOLD_MODE_HIGH_HYSTERESIS',
                'value': 1114
            },
            {
                'name': 'AUTORANGE_THRESHOLD_MODE_VAL_THRESHOLD_MODE_MEDIUM_HYSTERESIS',
                'value': 1115
            },
            {
                'name': 'AUTORANGE_THRESHOLD_MODE_VAL_THRESHOLD_MODE_HOLD',
                'value': 1116
            },
            {
                'name': 'CABLE_LENGTH_VAL_ZERO_M',
                'value': 1121
            },
            {
                'name': 'CABLE_LENGTH_VAL_NI_STANDARD_1M',
                'value': 1122
            },
            {
                'name': 'CABLE_LENGTH_VAL_NI_STANDARD_2M',
                'value': 1123
            },
            {
                'name': 'CABLE_LENGTH_VAL_NI_STANDARD_4M',
                'value': 1124
            },
            {
                'name': 'CABLE_LENGTH_VAL_CUSTOM_ONBOARD_STORAGE',
                'value': 1125
            },
            {
                'name': 'CABLE_LENGTH_VAL_CUSTOM_AS_CONFIGURED',
                'value': 1126
            },
            {
                'name': 'CABLE_LENGTH_VAL_NI_STANDARD_TRIAXIAL_1M',
                'value': 1139
            },
            {
                'name': 'CABLE_LENGTH_VAL_NI_STANDARD_TRIAXIAL_2M',
                'value': 1140
            },
            {
                'name': 'CABLE_LENGTH_VAL_NI_STANDARD_TRIAXIAL_4M',
                'value': 1141
            },
            {
                'name': 'COMPLIANCE_LIMIT_SYMMETRY_VAL_SYMMETRIC',
                'value': 0
            },
            {
                'name': 'COMPLIANCE_LIMIT_SYMMETRY_VAL_ASYMMETRIC',
                'value': 1
            },
            {
                'name': 'CURRENT_LIMIT_BEHAVIOR_VAL_CURRENT_REGULATE',
                'value': 0
            },
            {
                'name': 'CURRENT_LIMIT_BEHAVIOR_VAL_CURRENT_TRIP',
                'value': 1
            },
            {
                'name': 'DC_NOISE_REJECTION_VAL_DC_NOISE_REJECTION_SECOND_ORDER',
                'value': 1043
            },
            {
                'name': 'DC_NOISE_REJECTION_VAL_DC_NOISE_REJECTION_NORMAL',
                'value': 1044
            },
            {
                'name': 'DIGITAL_EDGE_VAL_RISING',
                'value': 1016
            },
            {
                'name': 'DIGITAL_EDGE_VAL_FALLING',
                'value': 1017
            },
            {
                'name': 'INSTRUMENT_MODE_VAL_SMU_PS',
                'value': 1061
            },
            {
                'name': 'INSTRUMENT_MODE_VAL_LCR',
                'value': 1062
            },
            {
                'name': 'ISOLATION_STATE_VAL_ISOLATED',
                'value': 1128
            },
            {
                'name': 'ISOLATION_STATE_VAL_NON_ISOLATED',
                'value': 1129
            },
            {
                'name': 'LCR_AUTOMATIC_LEVEL_CONTROL_VAL_OFF',
                'value': 0
            },
            {
                'name': 'LCR_AUTOMATIC_LEVEL_CONTROL_VAL_ON',
                'value': 1
            },
            {
                'name': 'LCRDC_BIAS_SOURCE_VAL_DC_BIAS_OFF',
                'value': 1065
            },
            {
                'name': 'LCRDC_BIAS_SOURCE_VAL_DC_BIAS_VOLTAGE',
                'value': 1066
            },
            {
                'name': 'LCRDC_BIAS_SOURCE_VAL_DC_BIAS_CURRENT',
                'value': 1067
            },
            {
                'name': 'LCR_IMPEDANCE_AUTO_RANGE_VAL_AUTO_RANGE_OFF',
                'value': 1068
            },
            {
                'name': 'LCR_IMPEDANCE_AUTO_RANGE_VAL_AUTO_RANGE_ON',
                'value': 1070
            },
            {
                'name': 'LCR_IMPEDANCE_RANGE_SOURCE_VAL_LCR_IMPEDANCE_RANGE',
                'value': 1142
            },
            {
                'name': 'LCR_IMPEDANCE_RANGE_SOURCE_VAL_LCR_LOAD_CONFIGURATION',
                'value': 1143
            },
            {
                'name': 'LCR_MEASUREMENT_TIME_VAL_MEASUREMENT_TIME_SHORT',
                'value': 1071
            },
            {
                'name': 'LCR_MEASUREMENT_TIME_VAL_MEASUREMENT_TIME_MEDIUM',
                'value': 1072
            },
            {
                'name': 'LCR_MEASUREMENT_TIME_VAL_MEASUREMENT_TIME_LONG',
                'value': 1073
            },
            {
                'name': 'LCR_MEASUREMENT_TIME_VAL_MEASUREMENT_TIME_CUSTOM',
                'value': 1117
            },
            {
                'name': 'LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE_VAL_ONBOARD_STORAGE',
                'value': 1074
            },
            {
                'name': 'LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE_VAL_AS_DEFINED',
                'value': 1075
            },
            {
                'name': 'LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE_VAL_AS_CONFIGURED',
                'value': 1146
            },
            {
                'name': 'LCR_SOURCE_DELAY_MODE_VAL_LCR_SOURCE_DELAY_MODE_AUTOMATIC',
                'value': 1144
            },
            {
                'name': 'LCR_SOURCE_DELAY_MODE_VAL_LCR_SOURCE_DELAY_MODE_MANUAL',
                'value': 1145
            },
            {
                'name': 'LCR_STIMULUS_FUNCTION_VAL_AC_VOLTAGE',
                'value': 1063
            },
            {
                'name': 'LCR_STIMULUS_FUNCTION_VAL_AC_CURRENT',
                'value': 1064
            },
            {
                'name': 'MEASURE_WHEN_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE',
                'value': 1025
            },
            {
                'name': 'MEASURE_WHEN_VAL_ON_DEMAND',
                'value': 1026
            },
            {
                'name': 'MEASURE_WHEN_VAL_ON_MEASURE_TRIGGER',
                'value': 1027
            },
            {
                'name': 'OUTPUT_CAPACITANCE_VAL_LOW',
                'value': 1010
            },
            {
                'name': 'OUTPUT_CAPACITANCE_VAL_HIGH',
                'value': 1011
            },
            {
                'name': 'OUTPUT_FUNCTION_VAL_DC_VOLTAGE',
                'value': 1006
            },
            {
                'name': 'OUTPUT_FUNCTION_VAL_DC_CURRENT',
                'value': 1007
            },
            {
                'name': 'OUTPUT_FUNCTION_VAL_PULSE_VOLTAGE',
                'value': 1049
            },
            {
                'name': 'OUTPUT_FUNCTION_VAL_PULSE_CURRENT',
                'value': 1050
            },
            {
                'name': 'POLARITY_VAL_ACTIVE_HIGH',
                'value': 1018
            },
            {
                'name': 'POLARITY_VAL_ACTIVE_LOW',
                'value': 1019
            },
            {
                'name': 'POWER_ALLOCATION_MODE_VAL_DISABLED',
                'value': 1058
            },
            {
                'name': 'POWER_ALLOCATION_MODE_VAL_AUTOMATIC',
                'value': 1059
            },
            {
                'name': 'POWER_ALLOCATION_MODE_VAL_MANUAL',
                'value': 1060
            },
            {
                'name': 'POWER_SOURCE_VAL_INTERNAL',
                'value': 1003
            },
            {
                'name': 'POWER_SOURCE_VAL_AUXILIARY',
                'value': 1004
            },
            {
                'name': 'POWER_SOURCE_VAL_AUTOMATIC',
                'value': 1005
            },
            {
                'name': 'POWER_SOURCE_IN_USE_VAL_INTERNAL',
                'value': 1003
            },
            {
                'name': 'POWER_SOURCE_IN_USE_VAL_AUXILIARY',
                'value': 1004
            },
            {
                'name': 'SELF_CALIBRATION_PERSISTENCE_VAL_KEEP_IN_MEMORY',
                'value': 1045
            },
            {
                'name': 'SELF_CALIBRATION_PERSISTENCE_VAL_WRITE_TO_EEPROM',
                'value': 1046
            },
            {
                'name': 'SENSE_VAL_LOCAL',
                'value': 1008
            },
            {
                'name': 'SENSE_VAL_REMOTE',
                'value': 1009
            },
            {
                'name': 'SOURCE_MODE_VAL_SINGLE_POINT',
                'value': 1020
            },
            {
                'name': 'SOURCE_MODE_VAL_SEQUENCE',
                'value': 1021
            },
            {
                'name': 'TRANSIENT_RESPONSE_VAL_NORMAL',
                'value': 1038
            },
            {
                'name': 'TRANSIENT_RESPONSE_VAL_FAST',
                'value': 1039
            },
            {
                'name': 'TRANSIENT_RESPONSE_VAL_SLOW',
                'value': 1041
            },
            {
                'name': 'TRANSIENT_RESPONSE_VAL_CUSTOM',
                'value': 1042
            },
            {
                'name': 'TRIGGER_TYPE_VAL_NONE',
                'value': 1012
            },
            {
                'name': 'TRIGGER_TYPE_VAL_DIGITAL_EDGE',
                'value': 1014
            },
            {
                'name': 'TRIGGER_TYPE_VAL_SOFTWARE_EDGE',
                'value': 1015
            }
        ]
    },
    'NiDCPowerReal64AttributeValues': {
        'enum-value-prefix': 'NIDCPOWER_REAL64',
        'generate-mappings': False,
        'values': [
            {
                'name': 'POWER_LINE_FREQUENCIES_VAL_50_HERTZ',
                'value': 50
            },
            {
                'name': 'POWER_LINE_FREQUENCIES_VAL_60_HERTZ',
                'value': 60
            }
        ]
    },
    'OutputCapacitance': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_LOW',
                'value': 1010
            },
            {
                'name': 'NIDCPOWER_VAL_HIGH',
                'value': 1011
            }
        ]
    },
    'OutputCutoffReason': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_ALL',
                'value': -1
            },
            {
                'name': 'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_OUTPUT_HIGH',
                'value': 1
            },
            {
                'name': 'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_OUTPUT_LOW',
                'value': 2
            },
            {
                'name': 'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_MEASURE_HIGH',
                'value': 4
            },
            {
                'name': 'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_MEASURE_LOW',
                'value': 8
            },
            {
                'name': 'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_CHANGE_HIGH',
                'value': 16
            },
            {
                'name': 'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_CHANGE_LOW',
                'value': 32
            },
            {
                'name': 'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_CHANGE_HIGH',
                'value': 64
            },
            {
                'name': 'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_CHANGE_LOW',
                'value': 128
            }
        ]
    },
    'OutputFunction': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_DC_VOLTAGE',
                'value': 1006
            },
            {
                'name': 'NIDCPOWER_VAL_DC_CURRENT',
                'value': 1007
            },
            {
                'name': 'NIDCPOWER_VAL_PULSE_VOLTAGE',
                'value': 1049
            },
            {
                'name': 'NIDCPOWER_VAL_PULSE_CURRENT',
                'value': 1050
            }
        ]
    },
    'OutputStates': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_OUTPUT_CONSTANT_VOLTAGE',
                'value': 0
            },
            {
                'name': 'NIDCPOWER_VAL_OUTPUT_CONSTANT_CURRENT',
                'value': 1
            },
            {
                'name': 'NIDCPOWER_VAL_OUTPUT_OVER_VOLTAGE',
                'value': 2
            },
            {
                'name': 'NIDCPOWER_VAL_OUTPUT_OVER_CURRENT',
                'value': 3
            },
            {
                'name': 'NIDCPOWER_VAL_OUTPUT_UNREGULATED',
                'value': 4
            }
        ]
    },
    'Polarity': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_ACTIVE_HIGH',
                'value': 1018
            },
            {
                'name': 'NIDCPOWER_VAL_ACTIVE_LOW',
                'value': 1019
            }
        ]
    },
    'PowerAllocationMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_DISABLED',
                'value': 1058
            },
            {
                'name': 'NIDCPOWER_VAL_AUTOMATIC',
                'value': 1059
            },
            {
                'name': 'NIDCPOWER_VAL_MANUAL',
                'value': 1060
            }
        ]
    },
    'PowerLineFrequencies': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_50_HERTZ',
                'value': 50
            },
            {
                'name': 'NIDCPOWER_VAL_60_HERTZ',
                'value': 60
            }
        ]
    },
    'PowerSource': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_INTERNAL',
                'value': 1003
            },
            {
                'name': 'NIDCPOWER_VAL_AUXILIARY',
                'value': 1004
            },
            {
                'name': 'NIDCPOWER_VAL_AUTOMATIC',
                'value': 1005
            }
        ]
    },
    'PowerSourceInUse': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_INTERNAL',
                'value': 1003
            },
            {
                'name': 'NIDCPOWER_VAL_AUXILIARY',
                'value': 1004
            }
        ]
    },
    'SelfCalibrationPersistence': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_KEEP_IN_MEMORY',
                'value': 1045
            },
            {
                'name': 'NIDCPOWER_VAL_WRITE_TO_EEPROM',
                'value': 1046
            }
        ]
    },
    'SendSoftwareEdgeTriggerType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_START',
                'value': 1034
            },
            {
                'name': 'NIDCPOWER_VAL_SOURCE',
                'value': 1035
            },
            {
                'name': 'NIDCPOWER_VAL_MEASURE',
                'value': 1036
            },
            {
                'name': 'NIDCPOWER_VAL_SEQUENCE_ADVANCE',
                'value': 1037
            },
            {
                'name': 'NIDCPOWER_VAL_PULSE',
                'value': 1053
            },
            {
                'name': 'NIDCPOWER_VAL_SHUTDOWN',
                'value': 1118
            }
        ]
    },
    'Sense': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_LOCAL',
                'value': 1008
            },
            {
                'name': 'NIDCPOWER_VAL_REMOTE',
                'value': 1009
            }
        ]
    },
    'SourceMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_SINGLE_POINT',
                'value': 1020
            },
            {
                'name': 'NIDCPOWER_VAL_SEQUENCE',
                'value': 1021
            }
        ]
    },
    'TransientResponse': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_NORMAL',
                'value': 1038
            },
            {
                'name': 'NIDCPOWER_VAL_FAST',
                'value': 1039
            },
            {
                'name': 'NIDCPOWER_VAL_SLOW',
                'value': 1041
            },
            {
                'name': 'NIDCPOWER_VAL_CUSTOM',
                'value': 1042
            }
        ]
    },
    'TriggerType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDCPOWER_VAL_NONE',
                'value': 1012
            },
            {
                'name': 'NIDCPOWER_VAL_DIGITAL_EDGE',
                'value': 1014
            },
            {
                'name': 'NIDCPOWER_VAL_SOFTWARE_EDGE',
                'value': 1015
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidcpower/enums_addon.py sha256=9f25172e660fd7e043e0a5b4bbd8669084c5cf552aa295713232ee352147b900 bytes=192 -->
## FILE: source/codegen/metadata/nidcpower/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidcpower/enums_addon.py`
- sha256: `9f25172e660fd7e043e0a5b4bbd8669084c5cf552aa295713232ee352147b900`
- bytes: 192

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidcpower/functions.py sha256=08b812ff7bde8702ab79e169803207966332713c6af71375b6a02cb053a6601f bytes=132392 -->
## FILE: source/codegen/metadata/nidcpower/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidcpower/functions.py`
- sha256: `08b812ff7bde8702ab79e169803207966332713c6af71375b6a02cb053a6601f`
- bytes: 132392

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-DCPower API metadata version 23.0.0f517
functions = {
    'Abort': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'AbortWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalSelfCalibrate': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearError': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearInterchangeWarnings': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearLatchedOutputCutoffState': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'outputCutoffReason',
                'direction': 'in',
                'enum': 'OutputCutoffReason',
                'grpc_type': 'sint32',
                'name': 'outputCutoffReason',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'Close': {
        'cname': 'niDCPower_close',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'Commit': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'CommitWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureApertureTime': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'apertureTime',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'apertureTime',
                'type': 'ViReal64'
            },
            {
                'cppName': 'units',
                'direction': 'in',
                'enum': 'ApertureTimeUnits',
                'grpc_type': 'sint32',
                'name': 'units',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureAutoZero': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'autoZero',
                'direction': 'in',
                'enum': 'AutoZero',
                'grpc_type': 'sint32',
                'name': 'autoZero',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureCurrentLevel': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'level',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'level',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureCurrentLevelRange': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'range',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'range',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureCurrentLimit': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'behavior',
                'direction': 'in',
                'enum': 'CurrentLimitBehavior',
                'grpc_type': 'sint32',
                'name': 'behavior',
                'type': 'ViInt32'
            },
            {
                'cppName': 'limit',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'limit',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureCurrentLimitRange': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'range',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'range',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeMeasureTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'inputTerminal',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'inputTerminal',
                'type': 'ViConstString'
            },
            {
                'cppName': 'edge',
                'direction': 'in',
                'enum': 'DigitalEdge',
                'grpc_type': 'sint32',
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeMeasureTriggerWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'inputTerminal',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'inputTerminal',
                'type': 'ViConstString'
            },
            {
                'cppName': 'edge',
                'direction': 'in',
                'enum': 'DigitalEdge',
                'grpc_type': 'sint32',
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgePulseTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'inputTerminal',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'inputTerminal',
                'type': 'ViConstString'
            },
            {
                'cppName': 'edge',
                'direction': 'in',
                'enum': 'DigitalEdge',
                'grpc_type': 'sint32',
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgePulseTriggerWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'inputTerminal',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'inputTerminal',
                'type': 'ViConstString'
            },
            {
                'cppName': 'edge',
                'direction': 'in',
                'enum': 'DigitalEdge',
                'grpc_type': 'sint32',
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeSequenceAdvanceTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'inputTerminal',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'inputTerminal',
                'type': 'ViConstString'
            },
            {
                'cppName': 'edge',
                'direction': 'in',
                'enum': 'DigitalEdge',
                'grpc_type': 'sint32',
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'inputTerminal',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'inputTerminal',
                'type': 'ViConstString'
            },
            {
                'cppName': 'edge',
                'direction': 'in',
                'enum': 'DigitalEdge',
                'grpc_type': 'sint32',
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeShutdownTriggerWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'inputTerminal',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'inputTerminal',
                'type': 'ViConstString'
            },
            {
                'cppName': 'edge',
                'direction': 'in',
                'enum': 'DigitalEdge',
                'grpc_type': 'sint32',
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeSourceTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'inputTerminal',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'inputTerminal',
                'type': 'ViConstString'
            },
            {
                'cppName': 'edge',
                'direction': 'in',
                'enum': 'DigitalEdge',
                'grpc_type': 'sint32',
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeSourceTriggerWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'inputTerminal',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'inputTerminal',
                'type': 'ViConstString'
            },
            {
                'cppName': 'edge',
                'direction': 'in',
                'enum': 'DigitalEdge',
                'grpc_type': 'sint32',
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeStartTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'inputTerminal',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'inputTerminal',
                'type': 'ViConstString'
            },
            {
                'cppName': 'edge',
                'direction': 'in',
                'enum': 'DigitalEdge',
                'grpc_type': 'sint32',
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeStartTriggerWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'inputTerminal',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'inputTerminal',
                'type': 'ViConstString'
            },
            {
                'cppName': 'edge',
                'direction': 'in',
                'enum': 'DigitalEdge',
                'grpc_type': 'sint32',
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureLCRCustomCableCompensation': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'customCableCompensationDataSize',
                'determine_size_from': [
                    'customCableCompensationData'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'customCableCompensationDataSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'customCableCompensationData',
                'direction': 'in',
                'grpc_type': 'bytes',
                'name': 'customCableCompensationData',
                'size': {
                    'mechanism': 'len',
                    'value': 'customCableCompensationDataSize'
                },
                'type': 'ViInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureOutputEnabled': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'enabled',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'enabled',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureOutputFunction': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'function',
                'direction': 'in',
                'enum': 'OutputFunction',
                'grpc_type': 'sint32',
                'name': 'function',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureOutputResistance': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'resistance',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'resistance',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureOvp': {
        'cname': 'niDCPower_ConfigureOVP',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'enabled',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'enabled',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'limit',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'limit',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePowerLineFrequency': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'powerlineFrequency',
                'direction': 'in',
                'enum': 'PowerLineFrequencies',
                'grpc_type': 'double',
                'name': 'powerlineFrequency',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePulseBiasCurrentLevel': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'level',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'level',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePulseBiasCurrentLimit': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'limit',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'limit',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePulseBiasVoltageLevel': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'level',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'level',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePulseBiasVoltageLimit': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'limit',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'limit',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePulseCurrentLevel': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'level',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'level',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePulseCurrentLevelRange': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'range',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'range',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePulseCurrentLimit': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'limit',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'limit',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePulseCurrentLimitRange': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'range',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'range',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePulseVoltageLevel': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'level',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'level',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePulseVoltageLevelRange': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'range',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'range',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePulseVoltageLimit': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'limit',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'limit',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePulseVoltageLimitRange': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'range',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'range',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSense': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'sense',
                'direction': 'in',
                'enum': 'Sense',
                'grpc_type': 'sint32',
                'name': 'sense',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgeMeasureTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgeMeasureTriggerWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgePulseTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgePulseTriggerWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgeSequenceAdvanceTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgeShutdownTriggerWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgeSourceTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgeSourceTriggerWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgeStartTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgeStartTriggerWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSourceMode': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'sourceMode',
                'direction': 'in',
                'enum': 'SourceMode',
                'grpc_type': 'sint32',
                'name': 'sourceMode',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSourceModeWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'sourceMode',
                'direction': 'in',
                'enum': 'SourceMode',
                'grpc_type': 'sint32',
                'name': 'sourceMode',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureVoltageLevel': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'level',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'level',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureVoltageLevelRange': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'range',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'range',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureVoltageLimit': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'limit',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'limit',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureVoltageLimitRange': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'range',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'range',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateAdvancedSequence': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'sequenceName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'sequenceName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeIdCount',
                'determine_size_from': [
                    'attributeIds'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'attributeIdCount',
                'type': 'ViInt32'
            },
            {
                'cppName': 'attributeIds',
                'direction': 'in',
                'grpc_type': 'repeated sint32',
                'name': 'attributeIds',
                'size': {
                    'mechanism': 'len',
                    'value': 'attributeIdCount'
                },
                'type': 'ViInt32[]'
            },
            {
                'cppName': 'setAsActiveSequence',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'setAsActiveSequence',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateAdvancedSequenceCommitStepWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'setAsActiveStep',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'setAsActiveStep',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateAdvancedSequenceStep': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'setAsActiveStep',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'setAsActiveStep',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateAdvancedSequenceStepWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'setAsActiveStep',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'setAsActiveStep',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateAdvancedSequenceWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'sequenceName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'sequenceName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeIdCount',
                'determine_size_from': [
                    'attributeIds'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'attributeIdCount',
                'type': 'ViInt32'
            },
            {
                'cppName': 'attributeIds',
                'direction': 'in',
                'grpc_type': 'repeated sint32',
                'name': 'attributeIds',
                'size': {
                    'mechanism': 'len',
                    'value': 'attributeIdCount'
                },
                'type': 'ViInt32[]'
            },
            {
                'cppName': 'setAsActiveSequence',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'setAsActiveSequence',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'DeleteAdvancedSequence': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'sequenceName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'sequenceName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DeleteAdvancedSequenceWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'sequenceName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'sequenceName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'Disable': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisablePulseTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisablePulseTriggerWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableSequenceAdvanceTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableSequenceAdvanceTriggerWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableShutdownTriggerWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableSourceTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableSourceTriggerWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableStartTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableStartTriggerWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ErrorMessage': {
        'cname': 'niDCPower_error_message',
        'codegen_method': 'public',
        'is_error_handling': True,
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorCode',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'cppName': 'errorMessage',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ErrorQuery': {
        'cname': 'niDCPower_error_query',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorCode',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'errorCode',
                'type': 'ViInt32'
            },
            {
                'cppName': 'errorMessage',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributeConfigurationBuffer': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'size',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'cppName': 'configuration',
                'direction': 'out',
                'grpc_type': 'bytes',
                'name': 'configuration',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'ViInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributeConfigurationFile': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'filePath',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportSignal': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'signal',
                'direction': 'in',
                'enum': 'ExportSignal',
                'grpc_type': 'sint32',
                'name': 'signal',
                'type': 'ViInt32'
            },
            {
                'cppName': 'signalIdentifier',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'signalIdentifier',
                'type': 'ViConstString'
            },
            {
                'cppName': 'outputTerminal',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'outputTerminal',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportSignalWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'signal',
                'direction': 'in',
                'enum': 'ExportSignal',
                'grpc_type': 'sint32',
                'name': 'signal',
                'type': 'ViInt32'
            },
            {
                'cppName': 'signalIdentifier',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'signalIdentifier',
                'type': 'ViConstString'
            },
            {
                'cppName': 'outputTerminal',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'outputTerminal',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchMultiple': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'timeout',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'cppName': 'count',
                'direction': 'in',
                'grpc_type': 'sint32',
                'is_size_param': True,
                'name': 'count',
                'type': 'ViInt32'
            },
            {
                'cppName': 'voltageMeasurements',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'voltageMeasurements',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'count'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'currentMeasurements',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'currentMeasurements',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'count'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'inCompliance',
                'direction': 'out',
                'grpc_type': 'repeated bool',
                'name': 'inCompliance',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'count'
                },
                'type': 'ViBoolean[]'
            },
            {
                'cppName': 'actualCount',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualCount',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchMultipleLCR': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'timeout',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'cppName': 'count',
                'direction': 'in',
                'grpc_type': 'sint32',
                'is_size_param': True,
                'name': 'count',
                'type': 'ViInt32'
            },
            {
                'cppName': 'measurements',
                'direction': 'out',
                'grpc_type': 'repeated NILCRMeasurement',
                'name': 'measurements',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'count'
                },
                'type': 'struct NILCRMeasurement_struct[]'
            },
            {
                'cppName': 'actualCount',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualCount',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiDCPowerAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt32': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiDCPowerAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiDCPowerAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'out',
                'grpc_type': 'int64',
                'name': 'attributeValue',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViReal64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiDCPowerAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViSession': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiDCPowerAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'attributeValue',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiDCPowerAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'attributeValue',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetChannelName': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'index',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'index',
                'type': 'ViInt32'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'channelName',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'channelName',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetChannelNameFromString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'index',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'index',
                'type': 'ViConstString'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'channelName',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'channelName',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetError': {
        'codegen_method': 'public',
        'is_error_handling': True,
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'code',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'code',
                'type': 'ViStatus'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'description',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'description',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetExtCalLastDateAndTime': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'year',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'cppName': 'month',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'cppName': 'day',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'day',
                'type': 'ViInt32'
            },
            {
                'cppName': 'hour',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'hour',
                'type': 'ViInt32'
            },
            {
                'cppName': 'minute',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'minute',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetExtCalLastTemp': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'temperature',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetExtCalRecommendedInterval': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'months',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'months',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetLCRCompensationLastDateAndTime': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'compensationType',
                'direction': 'in',
                'enum': 'LCRCompensationType',
                'grpc_type': 'sint32',
                'name': 'compensationType',
                'type': 'ViInt32'
            },
            {
                'cppName': 'year',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'cppName': 'month',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'cppName': 'day',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'day',
                'type': 'ViInt32'
            },
            {
                'cppName': 'hour',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'hour',
                'type': 'ViInt32'
            },
            {
                'cppName': 'minute',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'minute',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetLCRCustomCableCompensationData': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'customCableCompensationDataSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'customCableCompensationDataSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'customCableCompensationData',
                'direction': 'out',
                'grpc_type': 'bytes',
                'name': 'customCableCompensationData',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'customCableCompensationDataSize'
                },
                'type': 'ViInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetNextCoercionRecord': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'coercionRecord',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'coercionRecord',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetNextInterchangeWarning': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'interchangeWarning',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'interchangeWarning',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSelfCalLastDateAndTime': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'year',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'cppName': 'month',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'cppName': 'day',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'day',
                'type': 'ViInt32'
            },
            {
                'cppName': 'hour',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'hour',
                'type': 'ViInt32'
            },
            {
                'cppName': 'minute',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'minute',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSelfCalLastTemp': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'temperature',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributeConfigurationBuffer': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'size',
                'determine_size_from': [
                    'configuration'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'cppName': 'configuration',
                'direction': 'in',
                'grpc_type': 'bytes',
                'name': 'configuration',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributeConfigurationFile': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'filePath',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitializeWithChannels': {
        'codegen_method': 'public',
        'init_method': True,
        'parameters': [
            {
                'cppName': 'resourceName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'cppName': 'channels',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channels',
                'type': 'ViConstString'
            },
            {
                'cppName': 'reset',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'reset',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'optionString',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'optionString',
                'type': 'ViConstString'
            },
            {
                'cppName': 'vi',
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorMessage',
                'direction': 'out',
                'get_last_error': 'deprecated',
                'grpc_type': 'string',
                'name': 'errorMessage',
                'type': 'ViChar[]'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'ViInt32'
            },
            {
                'cppName': 'newSessionInitialized',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'newSessionInitialized',
                'proto_only': True,
                'type': 'bool'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitializeWithIndependentChannels': {
        'codegen_method': 'public',
        'init_method': True,
        'parameters': [
            {
                'cppName': 'resourceName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'cppName': 'reset',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'reset',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'optionString',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'optionString',
                'type': 'ViConstString'
            },
            {
                'cppName': 'vi',
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorMessage',
                'direction': 'out',
                'get_last_error': 'deprecated',
                'grpc_type': 'string',
                'name': 'errorMessage',
                'type': 'ViChar[]'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'ViInt32'
            },
            {
                'cppName': 'newSessionInitialized',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'newSessionInitialized',
                'proto_only': True,
                'type': 'bool'
            }
        ],
        'returns': 'ViStatus'
    },
    'Initiate': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitiateWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'InvalidateAllAttributes': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'LockSession': {
        'codegen_method': 'private',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'callerHasLock',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'Measure': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'measurementType',
                'direction': 'in',
                'enum': 'MeasurementTypes',
                'grpc_type': 'sint32',
                'name': 'measurementType',
                'type': 'ViInt32'
            },
            {
                'cppName': 'measurement',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'measurement',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'MeasureMultiple': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'voltageMeasurements',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'voltageMeasurements',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'number_of_channels'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'currentMeasurements',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'currentMeasurements',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'number_of_channels'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'MeasureMultipleLCR': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'measurements',
                'direction': 'out',
                'grpc_type': 'repeated NILCRMeasurement',
                'name': 'measurements',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'number_of_channels'
                },
                'type': 'struct NILCRMeasurement_struct[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ParseChannelCount': {
        'codegen_method': 'private',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelsString',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelsString',
                'type': 'ViConstString'
            },
            {
                'cppName': 'numberOfChannels',
                'direction': 'out',
                'grpc_type': 'uint32',
                'name': 'numberOfChannels',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'PerformLCRLoadCompensation': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'numCompensationSpots',
                'determine_size_from': [
                    'compensationSpots'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'numCompensationSpots',
                'type': 'ViInt32'
            },
            {
                'cppName': 'compensationSpots',
                'direction': 'in',
                'grpc_type': 'repeated NILCRLoadCompensationSpot',
                'name': 'compensationSpots',
                'size': {
                    'mechanism': 'len',
                    'value': 'numCompensationSpots'
                },
                'type': 'struct NILCRLoadCompensationSpot_struct[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'PerformLCROpenCompensation': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'numFrequencies',
                'determine_size_from': [
                    'additionalFrequencies'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'numFrequencies',
                'type': 'ViInt32'
            },
            {
                'cppName': 'additionalFrequencies',
                'direction': 'in',
                'grpc_type': 'repeated double',
                'name': 'additionalFrequencies',
                'size': {
                    'mechanism': 'len',
                    'value': 'numFrequencies'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'PerformLCROpenCustomCableCompensation': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'PerformLCRShortCompensation': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'numFrequencies',
                'determine_size_from': [
                    'additionalFrequencies'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'numFrequencies',
                'type': 'ViInt32'
            },
            {
                'cppName': 'additionalFrequencies',
                'direction': 'in',
                'grpc_type': 'repeated double',
                'name': 'additionalFrequencies',
                'size': {
                    'mechanism': 'len',
                    'value': 'numFrequencies'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'PerformLCRShortCustomCableCompensation': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'QueryInCompliance': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'inCompliance',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'inCompliance',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'QueryLatchedOutputCutoffState': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'outputCutoffReason',
                'direction': 'in',
                'enum': 'OutputCutoffReason',
                'grpc_type': 'sint32',
                'name': 'outputCutoffReason',
                'type': 'ViInt32'
            },
            {
                'cppName': 'outputCutoffState',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'outputCutoffState',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'QueryMaxCurrentLimit': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'voltageLevel',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'voltageLevel',
                'type': 'ViReal64'
            },
            {
                'cppName': 'maxCurrentLimit',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'maxCurrentLimit',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'QueryMaxVoltageLevel': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'currentLimit',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'currentLimit',
                'type': 'ViReal64'
            },
            {
                'cppName': 'maxVoltageLevel',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'maxVoltageLevel',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'QueryMinCurrentLimit': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'voltageLevel',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'voltageLevel',
                'type': 'ViReal64'
            },
            {
                'cppName': 'minCurrentLimit',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'minCurrentLimit',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'QueryOutputState': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'outputState',
                'direction': 'in',
                'enum': 'OutputStates',
                'grpc_type': 'sint32',
                'name': 'outputState',
                'type': 'ViInt32'
            },
            {
                'cppName': 'inState',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'inState',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadCurrentTemperature': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'temperature',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'Reset': {
        'cname': 'niDCPower_reset',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetDevice': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetInterchangeCheck': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetWithDefaults': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'RevisionQuery': {
        'cname': 'niDCPower_revision_query',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'instrumentDriverRevision',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'instrumentDriverRevision',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            },
            {
                'cppName': 'firmwareRevision',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'firmwareRevision',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'SelfTest': {
        'cname': 'niDCPower_self_test',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'selfTestResult',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'selfTestResult',
                'type': 'ViInt16'
            },
            {
                'cppName': 'selfTestMessage',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'selfTestMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'SendSoftwareEdgeTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'trigger',
                'direction': 'in',
                'enum': 'SendSoftwareEdgeTriggerType',
                'grpc_type': 'sint32',
                'name': 'trigger',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SendSoftwareEdgeTriggerWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'trigger',
                'direction': 'in',
                'enum': 'SendSoftwareEdgeTriggerType',
                'grpc_type': 'sint32',
                'name': 'trigger',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViBoolean': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiDCPowerAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt32': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiDCPowerAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'enum': 'NiDCPowerInt32AttributeValues',
                'grpc_type': 'sint32',
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiDCPowerAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_type': 'int64',
                'name': 'attribute_value_raw',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViReal64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiDCPowerAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'enum': 'NiDCPowerReal64AttributeValues',
                'grpc_type': 'double',
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViSession': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiDCPowerAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'attributeValue',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiDCPowerAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'attribute_value_raw',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetSequence': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'values',
                'direction': 'in',
                'grpc_type': 'repeated double',
                'name': 'values',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'sourceDelays',
                'direction': 'in',
                'grpc_type': 'repeated double',
                'name': 'sourceDelays',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'size',
                'determine_size_from': [
                    'values',
                    'sourceDelays'
                ],
                'direction': 'in',
                'grpc_type': 'uint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'size',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'UnlockSession': {
        'codegen_method': 'private',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'callerHasLock',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'WaitForEvent': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'eventId',
                'direction': 'in',
                'enum': 'Event',
                'grpc_type': 'sint32',
                'name': 'eventId',
                'type': 'ViInt32'
            },
            {
                'cppName': 'timeout',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'timeout',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'WaitForEventWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'eventId',
                'direction': 'in',
                'enum': 'Event',
                'grpc_type': 'sint32',
                'name': 'eventId',
                'type': 'ViInt32'
            },
            {
                'cppName': 'timeout',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'timeout',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidcpower/functions_addon.py sha256=f16f35823540a2624fa32e1e0397051ddbccfa1c7ae5d82e7413cef5b3c75708 bytes=1312 -->
## FILE: source/codegen/metadata/nidcpower/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidcpower/functions_addon.py`
- sha256: `f16f35823540a2624fa32e1e0397051ddbccfa1c7ae5d82e7413cef5b3c75708`
- bytes: 1312

````python
# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
    'SetRuntimeEnvironment': {
        'codegen_method': 'private',
        'parameters': [
            {
                'cppName': 'environment',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'environment',
                'type': 'ViConstString'
            },
            {
                'cppName': 'environmentVersion',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'environmentVersion',
                'type': 'ViConstString'
            },
            {
                'cppName': 'reserved1',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'reserved1',
                'type': 'ViConstString'
            },
            {
                'cppName': 'reserved2',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'reserved2',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidcpower/nidcpower.proto sha256=11e639b2932fa7c549166059717dc38b1598f7a1300c1ca3415da7154e8c1b90 bytes=74741 -->
## FILE: source/codegen/metadata/nidcpower/nidcpower.proto

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidcpower/nidcpower.proto`
- sha256: `11e639b2932fa7c549166059717dc38b1598f7a1300c1ca3415da7154e8c1b90`
- bytes: 74741

````protobuf

//---------------------------------------------------------------------
// This file is generated from NI-DCPower API metadata version 23.0.0f517
//---------------------------------------------------------------------
// Proto file for the NI-DCPower Metadata
//---------------------------------------------------------------------
syntax = "proto3";

option java_multiple_files = true;
option java_package = "com.ni.grpc.dcpower";
option java_outer_classname = "NiDCPower";
option csharp_namespace = "NationalInstruments.Grpc.DCPower";

package nidcpower_grpc;

import "nidevice.proto";
import "session.proto";

service NiDCPower {
  rpc Abort(AbortRequest) returns (AbortResponse);
  rpc AbortWithChannels(AbortWithChannelsRequest) returns (AbortWithChannelsResponse);
  rpc CalSelfCalibrate(CalSelfCalibrateRequest) returns (CalSelfCalibrateResponse);
  rpc ClearError(ClearErrorRequest) returns (ClearErrorResponse);
  rpc ClearInterchangeWarnings(ClearInterchangeWarningsRequest) returns (ClearInterchangeWarningsResponse);
  rpc ClearLatchedOutputCutoffState(ClearLatchedOutputCutoffStateRequest) returns (ClearLatchedOutputCutoffStateResponse);
  rpc Close(CloseRequest) returns (CloseResponse);
  rpc Commit(CommitRequest) returns (CommitResponse);
  rpc CommitWithChannels(CommitWithChannelsRequest) returns (CommitWithChannelsResponse);
  rpc ConfigureApertureTime(ConfigureApertureTimeRequest) returns (ConfigureApertureTimeResponse);
  rpc ConfigureAutoZero(ConfigureAutoZeroRequest) returns (ConfigureAutoZeroResponse);
  rpc ConfigureCurrentLevel(ConfigureCurrentLevelRequest) returns (ConfigureCurrentLevelResponse);
  rpc ConfigureCurrentLevelRange(ConfigureCurrentLevelRangeRequest) returns (ConfigureCurrentLevelRangeResponse);
  rpc ConfigureCurrentLimit(ConfigureCurrentLimitRequest) returns (ConfigureCurrentLimitResponse);
  rpc ConfigureCurrentLimitRange(ConfigureCurrentLimitRangeRequest) returns (ConfigureCurrentLimitRangeResponse);
  rpc ConfigureDigitalEdgeMeasureTrigger(ConfigureDigitalEdgeMeasureTriggerRequest) returns (ConfigureDigitalEdgeMeasureTriggerResponse);
  rpc ConfigureDigitalEdgeMeasureTriggerWithChannels(ConfigureDigitalEdgeMeasureTriggerWithChannelsRequest) returns (ConfigureDigitalEdgeMeasureTriggerWithChannelsResponse);
  rpc ConfigureDigitalEdgePulseTrigger(ConfigureDigitalEdgePulseTriggerRequest) returns (ConfigureDigitalEdgePulseTriggerResponse);
  rpc ConfigureDigitalEdgePulseTriggerWithChannels(ConfigureDigitalEdgePulseTriggerWithChannelsRequest) returns (ConfigureDigitalEdgePulseTriggerWithChannelsResponse);
  rpc ConfigureDigitalEdgeSequenceAdvanceTrigger(ConfigureDigitalEdgeSequenceAdvanceTriggerRequest) returns (ConfigureDigitalEdgeSequenceAdvanceTriggerResponse);
  rpc ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannels(ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannelsRequest) returns (ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannelsResponse);
  rpc ConfigureDigitalEdgeShutdownTriggerWithChannels(ConfigureDigitalEdgeShutdownTriggerWithChannelsRequest) returns (ConfigureDigitalEdgeShutdownTriggerWithChannelsResponse);
  rpc ConfigureDigitalEdgeSourceTrigger(ConfigureDigitalEdgeSourceTriggerRequest) returns (ConfigureDigitalEdgeSourceTriggerResponse);
  rpc ConfigureDigitalEdgeSourceTriggerWithChannels(ConfigureDigitalEdgeSourceTriggerWithChannelsRequest) returns (ConfigureDigitalEdgeSourceTriggerWithChannelsResponse);
  rpc ConfigureDigitalEdgeStartTrigger(ConfigureDigitalEdgeStartTriggerRequest) returns (ConfigureDigitalEdgeStartTriggerResponse);
  rpc ConfigureDigitalEdgeStartTriggerWithChannels(ConfigureDigitalEdgeStartTriggerWithChannelsRequest) returns (ConfigureDigitalEdgeStartTriggerWithChannelsResponse);
  rpc ConfigureLCRCustomCableCompensation(ConfigureLCRCustomCableCompensationRequest) returns (ConfigureLCRCustomCableCompensationResponse);
  rpc ConfigureOutputEnabled(ConfigureOutputEnabledRequest) returns (ConfigureOutputEnabledResponse);
  rpc ConfigureOutputFunction(ConfigureOutputFunctionRequest) returns (ConfigureOutputFunctionResponse);
  rpc ConfigureOutputResistance(ConfigureOutputResistanceRequest) returns (ConfigureOutputResistanceResponse);
  rpc ConfigureOvp(ConfigureOvpRequest) returns (ConfigureOvpResponse);
  rpc ConfigurePowerLineFrequency(ConfigurePowerLineFrequencyRequest) returns (ConfigurePowerLineFrequencyResponse);
  rpc ConfigurePulseBiasCurrentLevel(ConfigurePulseBiasCurrentLevelRequest) returns (ConfigurePulseBiasCurrentLevelResponse);
  rpc ConfigurePulseBiasCurrentLimit(ConfigurePulseBiasCurrentLimitRequest) returns (ConfigurePulseBiasCurrentLimitResponse);
  rpc ConfigurePulseBiasVoltageLevel(ConfigurePulseBiasVoltageLevelRequest) returns (ConfigurePulseBiasVoltageLevelResponse);
  rpc ConfigurePulseBiasVoltageLimit(ConfigurePulseBiasVoltageLimitRequest) returns (ConfigurePulseBiasVoltageLimitResponse);
  rpc ConfigurePulseCurrentLevel(ConfigurePulseCurrentLevelRequest) returns (ConfigurePulseCurrentLevelResponse);
  rpc ConfigurePulseCurrentLevelRange(ConfigurePulseCurrentLevelRangeRequest) returns (ConfigurePulseCurrentLevelRangeResponse);
  rpc ConfigurePulseCurrentLimit(ConfigurePulseCurrentLimitRequest) returns (ConfigurePulseCurrentLimitResponse);
  rpc ConfigurePulseCurrentLimitRange(ConfigurePulseCurrentLimitRangeRequest) returns (ConfigurePulseCurrentLimitRangeResponse);
  rpc ConfigurePulseVoltageLevel(ConfigurePulseVoltageLevelRequest) returns (ConfigurePulseVoltageLevelResponse);
  rpc ConfigurePulseVoltageLevelRange(ConfigurePulseVoltageLevelRangeRequest) returns (ConfigurePulseVoltageLevelRangeResponse);
  rpc ConfigurePulseVoltageLimit(ConfigurePulseVoltageLimitRequest) returns (ConfigurePulseVoltageLimitResponse);
  rpc ConfigurePulseVoltageLimitRange(ConfigurePulseVoltageLimitRangeRequest) returns (ConfigurePulseVoltageLimitRangeResponse);
  rpc ConfigureSense(ConfigureSenseRequest) returns (ConfigureSenseResponse);
  rpc ConfigureSoftwareEdgeMeasureTrigger(ConfigureSoftwareEdgeMeasureTriggerRequest) returns (ConfigureSoftwareEdgeMeasureTriggerResponse);
  rpc ConfigureSoftwareEdgeMeasureTriggerWithChannels(ConfigureSoftwareEdgeMeasureTriggerWithChannelsRequest) returns (ConfigureSoftwareEdgeMeasureTriggerWithChannelsResponse);
  rpc ConfigureSoftwareEdgePulseTrigger(ConfigureSoftwareEdgePulseTriggerRequest) returns (ConfigureSoftwareEdgePulseTriggerResponse);
  rpc ConfigureSoftwareEdgePulseTriggerWithChannels(ConfigureSoftwareEdgePulseTriggerWithChannelsRequest) returns (ConfigureSoftwareEdgePulseTriggerWithChannelsResponse);
  rpc ConfigureSoftwareEdgeSequenceAdvanceTrigger(ConfigureSoftwareEdgeSequenceAdvanceTriggerRequest) returns (ConfigureSoftwareEdgeSequenceAdvanceTriggerResponse);
  rpc ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannels(ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannelsRequest) returns (ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannelsResponse);
  rpc ConfigureSoftwareEdgeShutdownTriggerWithChannels(ConfigureSoftwareEdgeShutdownTriggerWithChannelsRequest) returns (ConfigureSoftwareEdgeShutdownTriggerWithChannelsResponse);
  rpc ConfigureSoftwareEdgeSourceTrigger(ConfigureSoftwareEdgeSourceTriggerRequest) returns (ConfigureSoftwareEdgeSourceTriggerResponse);
  rpc ConfigureSoftwareEdgeSourceTriggerWithChannels(ConfigureSoftwareEdgeSourceTriggerWithChannelsRequest) returns (ConfigureSoftwareEdgeSourceTriggerWithChannelsResponse);
  rpc ConfigureSoftwareEdgeStartTrigger(ConfigureSoftwareEdgeStartTriggerRequest) returns (ConfigureSoftwareEdgeStartTriggerResponse);
  rpc ConfigureSoftwareEdgeStartTriggerWithChannels(ConfigureSoftwareEdgeStartTriggerWithChannelsRequest) returns (ConfigureSoftwareEdgeStartTriggerWithChannelsResponse);
  rpc ConfigureSourceMode(ConfigureSourceModeRequest) returns (ConfigureSourceModeResponse);
  rpc ConfigureSourceModeWithChannels(ConfigureSourceModeWithChannelsRequest) returns (ConfigureSourceModeWithChannelsResponse);
  rpc ConfigureVoltageLevel(ConfigureVoltageLevelRequest) returns (ConfigureVoltageLevelResponse);
  rpc ConfigureVoltageLevelRange(ConfigureVoltageLevelRangeRequest) returns (ConfigureVoltageLevelRangeResponse);
  rpc ConfigureVoltageLimit(ConfigureVoltageLimitRequest) returns (ConfigureVoltageLimitResponse);
  rpc ConfigureVoltageLimitRange(ConfigureVoltageLimitRangeRequest) returns (ConfigureVoltageLimitRangeResponse);
  rpc CreateAdvancedSequence(CreateAdvancedSequenceRequest) returns (CreateAdvancedSequenceResponse);
  rpc CreateAdvancedSequenceCommitStepWithChannels(CreateAdvancedSequenceCommitStepWithChannelsRequest) returns (CreateAdvancedSequenceCommitStepWithChannelsResponse);
  rpc CreateAdvancedSequenceStep(CreateAdvancedSequenceStepRequest) returns (CreateAdvancedSequenceStepResponse);
  rpc CreateAdvancedSequenceStepWithChannels(CreateAdvancedSequenceStepWithChannelsRequest) returns (CreateAdvancedSequenceStepWithChannelsResponse);
  rpc CreateAdvancedSequenceWithChannels(CreateAdvancedSequenceWithChannelsRequest) returns (CreateAdvancedSequenceWithChannelsResponse);
  rpc DeleteAdvancedSequence(DeleteAdvancedSequenceRequest) returns (DeleteAdvancedSequenceResponse);
  rpc DeleteAdvancedSequenceWithChannels(DeleteAdvancedSequenceWithChannelsRequest) returns (DeleteAdvancedSequenceWithChannelsResponse);
  rpc Disable(DisableRequest) returns (DisableResponse);
  rpc DisablePulseTrigger(DisablePulseTriggerRequest) returns (DisablePulseTriggerResponse);
  rpc DisablePulseTriggerWithChannels(DisablePulseTriggerWithChannelsRequest) returns (DisablePulseTriggerWithChannelsResponse);
  rpc DisableSequenceAdvanceTrigger(DisableSequenceAdvanceTriggerRequest) returns (DisableSequenceAdvanceTriggerResponse);
  rpc DisableSequenceAdvanceTriggerWithChannels(DisableSequenceAdvanceTriggerWithChannelsRequest) returns (DisableSequenceAdvanceTriggerWithChannelsResponse);
  rpc DisableShutdownTriggerWithChannels(DisableShutdownTriggerWithChannelsRequest) returns (DisableShutdownTriggerWithChannelsResponse);
  rpc DisableSourceTrigger(DisableSourceTriggerRequest) returns (DisableSourceTriggerResponse);
  rpc DisableSourceTriggerWithChannels(DisableSourceTriggerWithChannelsRequest) returns (DisableSourceTriggerWithChannelsResponse);
  rpc DisableStartTrigger(DisableStartTriggerRequest) returns (DisableStartTriggerResponse);
  rpc DisableStartTriggerWithChannels(DisableStartTriggerWithChannelsRequest) returns (DisableStartTriggerWithChannelsResponse);
  rpc ErrorMessage(ErrorMessageRequest) returns (ErrorMessageResponse);
  rpc ErrorQuery(ErrorQueryRequest) returns (ErrorQueryResponse);
  rpc ExportAttributeConfigurationBuffer(ExportAttributeConfigurationBufferRequest) returns (ExportAttributeConfigurationBufferResponse);
  rpc ExportAttributeConfigurationFile(ExportAttributeConfigurationFileRequest) returns (ExportAttributeConfigurationFileResponse);
  rpc ExportSignal(ExportSignalRequest) returns (ExportSignalResponse);
  rpc ExportSignalWithChannels(ExportSignalWithChannelsRequest) returns (ExportSignalWithChannelsResponse);
  rpc FetchMultiple(FetchMultipleRequest) returns (FetchMultipleResponse);
  rpc FetchMultipleLCR(FetchMultipleLCRRequest) returns (FetchMultipleLCRResponse);
  rpc GetAttributeViBoolean(GetAttributeViBooleanRequest) returns (GetAttributeViBooleanResponse);
  rpc GetAttributeViInt32(GetAttributeViInt32Request) returns (GetAttributeViInt32Response);
  rpc GetAttributeViInt64(GetAttributeViInt64Request) returns (GetAttributeViInt64Response);
  rpc GetAttributeViReal64(GetAttributeViReal64Request) returns (GetAttributeViReal64Response);
  rpc GetAttributeViSession(GetAttributeViSessionRequest) returns (GetAttributeViSessionResponse);
  rpc GetAttributeViString(GetAttributeViStringRequest) returns (GetAttributeViStringResponse);
  rpc GetChannelName(GetChannelNameRequest) returns (GetChannelNameResponse);
  rpc GetChannelNameFromString(GetChannelNameFromStringRequest) returns (GetChannelNameFromStringResponse);
  rpc GetError(GetErrorRequest) returns (GetErrorResponse);
  rpc GetExtCalLastDateAndTime(GetExtCalLastDateAndTimeRequest) returns (GetExtCalLastDateAndTimeResponse);
  rpc GetExtCalLastTemp(GetExtCalLastTempRequest) returns (GetExtCalLastTempResponse);
  rpc GetExtCalRecommendedInterval(GetExtCalRecommendedIntervalRequest) returns (GetExtCalRecommendedIntervalResponse);
  rpc GetLCRCompensationLastDateAndTime(GetLCRCompensationLastDateAndTimeRequest) returns (GetLCRCompensationLastDateAndTimeResponse);
  rpc GetLCRCustomCableCompensationData(GetLCRCustomCableCompensationDataRequest) returns (GetLCRCustomCableCompensationDataResponse);
  rpc GetNextCoercionRecord(GetNextCoercionRecordRequest) returns (GetNextCoercionRecordResponse);
  rpc GetNextInterchangeWarning(GetNextInterchangeWarningRequest) returns (GetNextInterchangeWarningResponse);
  rpc GetSelfCalLastDateAndTime(GetSelfCalLastDateAndTimeRequest) returns (GetSelfCalLastDateAndTimeResponse);
  rpc GetSelfCalLastTemp(GetSelfCalLastTempRequest) returns (GetSelfCalLastTempResponse);
  rpc ImportAttributeConfigurationBuffer(ImportAttributeConfigurationBufferRequest) returns (ImportAttributeConfigurationBufferResponse);
  rpc ImportAttributeConfigurationFile(ImportAttributeConfigurationFileRequest) returns (ImportAttributeConfigurationFileResponse);
  rpc InitializeWithChannels(InitializeWithChannelsRequest) returns (InitializeWithChannelsResponse);
  rpc InitializeWithIndependentChannels(InitializeWithIndependentChannelsRequest) returns (InitializeWithIndependentChannelsResponse);
  rpc Initiate(InitiateRequest) returns (InitiateResponse);
  rpc InitiateWithChannels(InitiateWithChannelsRequest) returns (InitiateWithChannelsResponse);
  rpc InvalidateAllAttributes(InvalidateAllAttributesRequest) returns (InvalidateAllAttributesResponse);
  rpc Measure(MeasureRequest) returns (MeasureResponse);
  rpc MeasureMultiple(MeasureMultipleRequest) returns (MeasureMultipleResponse);
  rpc MeasureMultipleLCR(MeasureMultipleLCRRequest) returns (MeasureMultipleLCRResponse);
  rpc PerformLCRLoadCompensation(PerformLCRLoadCompensationRequest) returns (PerformLCRLoadCompensationResponse);
  rpc PerformLCROpenCompensation(PerformLCROpenCompensationRequest) returns (PerformLCROpenCompensationResponse);
  rpc PerformLCROpenCustomCableCompensation(PerformLCROpenCustomCableCompensationRequest) returns (PerformLCROpenCustomCableCompensationResponse);
  rpc PerformLCRShortCompensation(PerformLCRShortCompensationRequest) returns (PerformLCRShortCompensationResponse);
  rpc PerformLCRShortCustomCableCompensation(PerformLCRShortCustomCableCompensationRequest) returns (PerformLCRShortCustomCableCompensationResponse);
  rpc QueryInCompliance(QueryInComplianceRequest) returns (QueryInComplianceResponse);
  rpc QueryLatchedOutputCutoffState(QueryLatchedOutputCutoffStateRequest) returns (QueryLatchedOutputCutoffStateResponse);
  rpc QueryMaxCurrentLimit(QueryMaxCurrentLimitRequest) returns (QueryMaxCurrentLimitResponse);
  rpc QueryMaxVoltageLevel(QueryMaxVoltageLevelRequest) returns (QueryMaxVoltageLevelResponse);
  rpc QueryMinCurrentLimit(QueryMinCurrentLimitRequest) returns (QueryMinCurrentLimitResponse);
  rpc QueryOutputState(QueryOutputStateRequest) returns (QueryOutputStateResponse);
  rpc ReadCurrentTemperature(ReadCurrentTemperatureRequest) returns (ReadCurrentTemperatureResponse);
  rpc Reset(ResetRequest) returns (ResetResponse);
  rpc ResetDevice(ResetDeviceRequest) returns (ResetDeviceResponse);
  rpc ResetInterchangeCheck(ResetInterchangeCheckRequest) returns (ResetInterchangeCheckResponse);
  rpc ResetWithChannels(ResetWithChannelsRequest) returns (ResetWithChannelsResponse);
  rpc ResetWithDefaults(ResetWithDefaultsRequest) returns (ResetWithDefaultsResponse);
  rpc RevisionQuery(RevisionQueryRequest) returns (RevisionQueryResponse);
  rpc SelfTest(SelfTestRequest) returns (SelfTestResponse);
  rpc SendSoftwareEdgeTrigger(SendSoftwareEdgeTriggerRequest) returns (SendSoftwareEdgeTriggerResponse);
  rpc SendSoftwareEdgeTriggerWithChannels(SendSoftwareEdgeTriggerWithChannelsRequest) returns (SendSoftwareEdgeTriggerWithChannelsResponse);
  rpc SetAttributeViBoolean(SetAttributeViBooleanRequest) returns (SetAttributeViBooleanResponse);
  rpc SetAttributeViInt32(SetAttributeViInt32Request) returns (SetAttributeViInt32Response);
  rpc SetAttributeViInt64(SetAttributeViInt64Request) returns (SetAttributeViInt64Response);
  rpc SetAttributeViReal64(SetAttributeViReal64Request) returns (SetAttributeViReal64Response);
  rpc SetAttributeViSession(SetAttributeViSessionRequest) returns (SetAttributeViSessionResponse);
  rpc SetAttributeViString(SetAttributeViStringRequest) returns (SetAttributeViStringResponse);
  rpc SetSequence(SetSequenceRequest) returns (SetSequenceResponse);
  rpc WaitForEvent(WaitForEventRequest) returns (WaitForEventResponse);
  rpc WaitForEventWithChannels(WaitForEventWithChannelsRequest) returns (WaitForEventWithChannelsResponse);
}

enum NiDCPowerAttribute {
  NIDCPOWER_ATTRIBUTE_UNSPECIFIED = 0;
  NIDCPOWER_ATTRIBUTE_RANGE_CHECK = 1050002;
  NIDCPOWER_ATTRIBUTE_QUERY_INSTRUMENT_STATUS = 1050003;
  NIDCPOWER_ATTRIBUTE_CACHE = 1050004;
  NIDCPOWER_ATTRIBUTE_SIMULATE = 1050005;
  NIDCPOWER_ATTRIBUTE_RECORD_COERCIONS = 1050006;
  NIDCPOWER_ATTRIBUTE_DRIVER_SETUP = 1050007;
  NIDCPOWER_ATTRIBUTE_INTERCHANGE_CHECK = 1050021;
  NIDCPOWER_ATTRIBUTE_CHANNEL_COUNT = 1050203;
  NIDCPOWER_ATTRIBUTE_SPECIFIC_DRIVER_PREFIX = 1050302;
  NIDCPOWER_ATTRIBUTE_IO_RESOURCE_DESCRIPTOR = 1050304;
  NIDCPOWER_ATTRIBUTE_LOGICAL_NAME = 1050305;
  NIDCPOWER_ATTRIBUTE_SUPPORTED_INSTRUMENT_MODELS = 1050327;
  NIDCPOWER_ATTRIBUTE_GROUP_CAPABILITIES = 1050401;
  NIDCPOWER_ATTRIBUTE_INSTRUMENT_FIRMWARE_REVISION = 1050510;
  NIDCPOWER_ATTRIBUTE_INSTRUMENT_MANUFACTURER = 1050511;
  NIDCPOWER_ATTRIBUTE_INSTRUMENT_MODEL = 1050512;
  NIDCPOWER_ATTRIBUTE_SPECIFIC_DRIVER_VENDOR = 1050513;
  NIDCPOWER_ATTRIBUTE_SPECIFIC_DRIVER_DESCRIPTION = 1050514;
  NIDCPOWER_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION = 1050515;
  NIDCPOWER_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION = 1050516;
  NIDCPOWER_ATTRIBUTE_SPECIFIC_DRIVER_REVISION = 1050551;
  NIDCPOWER_ATTRIBUTE_POWER_SOURCE = 1150000;
  NIDCPOWER_ATTRIBUTE_POWER_SOURCE_IN_USE = 1150001;
  NIDCPOWER_ATTRIBUTE_AUXILIARY_POWER_SOURCE_AVAILABLE = 1150002;
  NIDCPOWER_ATTRIBUTE_SAMPLES_TO_AVERAGE = 1150003;
  NIDCPOWER_ATTRIBUTE_CURRENT_LIMIT_RANGE = 1150004;
  NIDCPOWER_ATTRIBUTE_VOLTAGE_LEVEL_RANGE = 1150005;
  NIDCPOWER_ATTRIBUTE_RESET_AVERAGE_BEFORE_MEASUREMENT = 1150006;
  NIDCPOWER_ATTRIBUTE_OVERRANGING_ENABLED = 1150007;
  NIDCPOWER_ATTRIBUTE_OUTPUT_FUNCTION = 1150008;
  NIDCPOWER_ATTRIBUTE_CURRENT_LEVEL = 1150009;
  NIDCPOWER_ATTRIBUTE_VOLTAGE_LIMIT = 1150010;
  NIDCPOWER_ATTRIBUTE_CURRENT_LEVEL_RANGE = 1150011;
  NIDCPOWER_ATTRIBUTE_VOLTAGE_LIMIT_RANGE = 1150012;
  NIDCPOWER_ATTRIBUTE_SENSE = 1150013;
  NIDCPOWER_ATTRIBUTE_OUTPUT_CAPACITANCE = 1150014;
  NIDCPOWER_ATTRIBUTE_VOLTAGE_LEVEL_AUTORANGE = 1150015;
  NIDCPOWER_ATTRIBUTE_CURRENT_LIMIT_AUTORANGE = 1150016;
  NIDCPOWER_ATTRIBUTE_CURRENT_LEVEL_AUTORANGE = 1150017;
  NIDCPOWER_ATTRIBUTE_VOLTAGE_LIMIT_AUTORANGE = 1150018;
  NIDCPOWER_ATTRIBUTE_POWER_LINE_FREQUENCY = 1150020;
  NIDCPOWER_ATTRIBUTE_START_TRIGGER_TYPE = 1150021;
  NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_START_TRIGGER_EDGE = 1150022;
  NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL = 1150023;
  NIDCPOWER_ATTRIBUTE_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL = 1150024;
  NIDCPOWER_ATTRIBUTE_SEQUENCE_LOOP_COUNT = 1150025;
  NIDCPOWER_ATTRIBUTE_SEQUENCE_ADVANCE_TRIGGER_TYPE = 1150026;
  NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE = 1150027;
  NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_INPUT_TERMINAL = 1150028;
  NIDCPOWER_ATTRIBUTE_EXPORTED_SEQUENCE_ADVANCE_TRIGGER_OUTPUT_TERMINAL = 1150029;
  NIDCPOWER_ATTRIBUTE_SOURCE_TRIGGER_TYPE = 1150030;
  NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_SOURCE_TRIGGER_EDGE = 1150031;
  NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_SOURCE_TRIGGER_INPUT_TERMINAL = 1150032;
  NIDCPOWER_ATTRIBUTE_EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINAL = 1150033;
  NIDCPOWER_ATTRIBUTE_MEASURE_TRIGGER_TYPE = 1150034;
  NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_MEASURE_TRIGGER_EDGE = 1150035;
  NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_MEASURE_TRIGGER_INPUT_TERMINAL = 1150036;
  NIDCPOWER_ATTRIBUTE_EXPORTED_MEASURE_TRIGGER_OUTPUT_TERMINAL = 1150037;
  NIDCPOWER_ATTRIBUTE_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_POLARITY = 1150038;
  NIDCPOWER_ATTRIBUTE_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_WIDTH = 1150039;
  NIDCPOWER_ATTRIBUTE_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_TERMINAL = 1150040;
  NIDCPOWER_ATTRIBUTE_SOURCE_COMPLETE_EVENT_PULSE_POLARITY = 1150041;
  NIDCPOWER_ATTRIBUTE_SOURCE_COMPLETE_EVENT_PULSE_WIDTH = 1150042;
  NIDCPOWER_ATTRIBUTE_SOURCE_COMPLETE_EVENT_OUTPUT_TERMINAL = 1150043;
  NIDCPOWER_ATTRIBUTE_MEASURE_COMPLETE_EVENT_PULSE_POLARITY = 1150044;
  NIDCPOWER_ATTRIBUTE_MEASURE_COMPLETE_EVENT_PULSE_WIDTH = 1150045;
  NIDCPOWER_ATTRIBUTE_MEASURE_COMPLETE_EVENT_DELAY = 1150046;
  NIDCPOWER_ATTRIBUTE_MEASURE_COMPLETE_EVENT_OUTPUT_TERMINAL = 1150047;
  NIDCPOWER_ATTRIBUTE_SEQUENCE_ENGINE_DONE_EVENT_PULSE_POLARITY = 1150048;
  NIDCPOWER_ATTRIBUTE_SEQUENCE_ENGINE_DONE_EVENT_PULSE_WIDTH = 1150049;
  NIDCPOWER_ATTRIBUTE_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_TERMINAL = 1150050;
  NIDCPOWER_ATTRIBUTE_SOURCE_DELAY = 1150051;
  NIDCPOWER_ATTRIBUTE_SOURCE_MODE = 1150054;
  NIDCPOWER_ATTRIBUTE_AUTO_ZERO = 1150055;
  NIDCPOWER_ATTRIBUTE_FETCH_BACKLOG = 1150056;
  NIDCPOWER_ATTRIBUTE_MEASURE_WHEN = 1150057;
  NIDCPOWER_ATTRIBUTE_APERTURE_TIME = 1150058;
  NIDCPOWER_ATTRIBUTE_APERTURE_TIME_UNITS = 1150059;
  NIDCPOWER_ATTRIBUTE_OUTPUT_CONNECTED = 1150060;
  NIDCPOWER_ATTRIBUTE_OUTPUT_RESISTANCE = 1150061;
  NIDCPOWER_ATTRIBUTE_TRANSIENT_RESPONSE = 1150062;
  NIDCPOWER_ATTRIBUTE_MEASURE_RECORD_LENGTH = 1150063;
  NIDCPOWER_ATTRIBUTE_MEASURE_RECORD_LENGTH_IS_FINITE = 1150064;
  NIDCPOWER_ATTRIBUTE_MEASURE_RECORD_DELTA_TIME = 1150065;
  NIDCPOWER_ATTRIBUTE_DC_NOISE_REJECTION = 1150066;
  NIDCPOWER_ATTRIBUTE_VOLTAGE_GAIN_BANDWIDTH = 1150067;
  NIDCPOWER_ATTRIBUTE_VOLTAGE_COMPENSATION_FREQUENCY = 1150068;
  NIDCPOWER_ATTRIBUTE_VOLTAGE_POLE_ZERO_RATIO = 1150069;
  NIDCPOWER_ATTRIBUTE_CURRENT_GAIN_BANDWIDTH = 1150070;
  NIDCPOWER_ATTRIBUTE_CURRENT_COMPENSATION_FREQUENCY = 1150071;
  NIDCPOWER_ATTRIBUTE_CURRENT_POLE_ZERO_RATIO = 1150072;
  NIDCPOWER_ATTRIBUTE_SELF_CALIBRATION_PERSISTENCE = 1150073;
  NIDCPOWER_ATTRIBUTE_ACTIVE_ADVANCED_SEQUENCE = 1150074;
  NIDCPOWER_ATTRIBUTE_ACTIVE_ADVANCED_SEQUENCE_STEP = 1150075;
  NIDCPOWER_ATTRIBUTE_MEASURE_BUFFER_SIZE = 1150077;
  NIDCPOWER_ATTRIBUTE_SEQUENCE_LOOP_COUNT_IS_FINITE = 1150078;
  NIDCPOWER_ATTRIBUTE_SUPPORT_OUTPUT_DMA = 1150079;
  NIDCPOWER_ATTRIBUTE_PULSE_VOLTAGE_LEVEL = 1150080;
  NIDCPOWER_ATTRIBUTE_PULSE_CURRENT_LIMIT = 1150081;
  NIDCPOWER_ATTRIBUTE_PULSE_BIAS_VOLTAGE_LEVEL = 1150082;
  NIDCPOWER_ATTRIBUTE_PULSE_BIAS_CURRENT_LIMIT = 1150083;
  NIDCPOWER_ATTRIBUTE_PULSE_VOLTAGE_LEVEL_RANGE = 1150084;
  NIDCPOWER_ATTRIBUTE_PULSE_CURRENT_LIMIT_RANGE = 1150085;
  NIDCPOWER_ATTRIBUTE_PULSE_CURRENT_LEVEL = 1150086;
  NIDCPOWER_ATTRIBUTE_PULSE_VOLTAGE_LIMIT = 1150087;
  NIDCPOWER_ATTRIBUTE_PULSE_BIAS_CURRENT_LEVEL = 1150088;
  NIDCPOWER_ATTRIBUTE_PULSE_BIAS_VOLTAGE_LIMIT = 1150089;
  NIDCPOWER_ATTRIBUTE_PULSE_CURRENT_LEVEL_RANGE = 1150090;
  NIDCPOWER_ATTRIBUTE_PULSE_VOLTAGE_LIMIT_RANGE = 1150091;
  NIDCPOWER_ATTRIBUTE_PULSE_BIAS_DELAY = 1150092;
  NIDCPOWER_ATTRIBUTE_PULSE_ON_TIME = 1150093;
  NIDCPOWER_ATTRIBUTE_PULSE_OFF_TIME = 1150094;
  NIDCPOWER_ATTRIBUTE_PULSE_TRIGGER_TYPE = 1150095;
  NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_PULSE_TRIGGER_EDGE = 1150096;
  NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_PULSE_TRIGGER_INPUT_TERMINAL = 1150097;
  NIDCPOWER_ATTRIBUTE_EXPORTED_PULSE_TRIGGER_OUTPUT_TERMINAL = 1150098;
  NIDCPOWER_ATTRIBUTE_PULSE_COMPLETE_EVENT_OUTPUT_TERMINAL = 1150099;
  NIDCPOWER_ATTRIBUTE_PULSE_COMPLETE_EVENT_PULSE_POLARITY = 1150100;
  NIDCPOWER_ATTRIBUTE_PULSE_COMPLETE_EVENT_PULSE_WIDTH = 1150101;
  NIDCPOWER_ATTRIBUTE_READY_FOR_PULSE_TRIGGER_EVENT_OUTPUT_TERMINAL = 1150102;
  NIDCPOWER_ATTRIBUTE_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_POLARITY = 1150103;
  NIDCPOWER_ATTRIBUTE_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_WIDTH = 1150104;
  NIDCPOWER_ATTRIBUTE_INTERLOCK_INPUT_OPEN = 1150105;
  NIDCPOWER_ATTRIBUTE_INSTRUMENT_API_SESSION_HANDLE = 1150110;
  NIDCPOWER_ATTRIBUTE_WAS_SESSION_OPENED_BY_INITIALIZE_WITH_INDEPENDENT_CHANNELS = 1150111;
  NIDCPOWER_ATTRIBUTE_SERIAL_NUMBER = 1150152;
  NIDCPOWER_ATTRIBUTE_COMPLIANCE_LIMIT_SYMMETRY = 1150184;
  NIDCPOWER_ATTRIBUTE_VOLTAGE_LIMIT_HIGH = 1150185;
  NIDCPOWER_ATTRIBUTE_VOLTAGE_LIMIT_LOW = 1150186;
  NIDCPOWER_ATTRIBUTE_CURRENT_LIMIT_HIGH = 1150187;
  NIDCPOWER_ATTRIBUTE_CURRENT_LIMIT_LOW = 1150188;
  NIDCPOWER_ATTRIBUTE_PULSE_VOLTAGE_LIMIT_HIGH = 1150189;
  NIDCPOWER_ATTRIBUTE_PULSE_VOLTAGE_LIMIT_LOW = 1150190;
  NIDCPOWER_ATTRIBUTE_PULSE_BIAS_VOLTAGE_LIMIT_HIGH = 1150191;
  NIDCPOWER_ATTRIBUTE_PULSE_BIAS_VOLTAGE_LIMIT_LOW = 1150192;
  NIDCPOWER_ATTRIBUTE_PULSE_CURRENT_LIMIT_HIGH = 1150193;
  NIDCPOWER_ATTRIBUTE_PULSE_CURRENT_LIMIT_LOW = 1150194;
  NIDCPOWER_ATTRIBUTE_PULSE_BIAS_CURRENT_LIMIT_HIGH = 1150195;
  NIDCPOWER_ATTRIBUTE_PULSE_BIAS_CURRENT_LIMIT_LOW = 1150196;
  NIDCPOWER_ATTRIBUTE_SEQUENCE_STEP_DELTA_TIME = 1150198;
  NIDCPOWER_ATTRIBUTE_SEQUENCE_STEP_DELTA_TIME_ENABLED = 1150199;
  NIDCPOWER_ATTRIBUTE_OCP_ERROR_PERCENTAGE = 1150200;
  NIDCPOWER_ATTRIBUTE_ACTUAL_POWER_ALLOCATION = 1150205;
  NIDCPOWER_ATTRIBUTE_REQUESTED_POWER_ALLOCATION = 1150206;
  NIDCPOWER_ATTRIBUTE_POWER_ALLOCATION_MODE = 1150207;
  NIDCPOWER_ATTRIBUTE_INSTRUMENT_MODE = 1150208;
  NIDCPOWER_ATTRIBUTE_LCR_STIMULUS_FUNCTION = 1150209;
  NIDCPOWER_ATTRIBUTE_LCR_FREQUENCY = 1150210;
  NIDCPOWER_ATTRIBUTE_LCR_VOLTAGE_AMPLITUDE = 1150211;
  NIDCPOWER_ATTRIBUTE_LCR_CURRENT_AMPLITUDE = 1150212;
  NIDCPOWER_ATTRIBUTE_LCR_DC_BIAS_SOURCE = 1150213;
  NIDCPOWER_ATTRIBUTE_LCR_DC_BIAS_VOLTAGE_LEVEL = 1150214;
  NIDCPOWER_ATTRIBUTE_LCR_DC_BIAS_CURRENT_LEVEL = 1150215;
  NIDCPOWER_ATTRIBUTE_LCR_IMPEDANCE_AUTO_RANGE = 1150216;
  NIDCPOWER_ATTRIBUTE_LCR_IMPEDANCE_RANGE = 1150217;
  NIDCPOWER_ATTRIBUTE_LCR_MEASUREMENT_TIME = 1150218;
  NIDCPOWER_ATTRIBUTE_LCR_OPEN_COMPENSATION_ENABLED = 1150220;
  NIDCPOWER_ATTRIBUTE_LCR_SHORT_COMPENSATION_ENABLED = 1150221;
  NIDCPOWER_ATTRIBUTE_LCR_LOAD_COMPENSATION_ENABLED = 1150222;
  NIDCPOWER_ATTRIBUTE_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE = 1150223;
  NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_ENABLED = 1150235;
  NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_HIGH = 1150236;
  NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_HIGH = 1150237;
  NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_LOW = 1150238;
  NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_LOW = 1150239;
  NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_CURRENT_OVERRANGE_ENABLED = 1150240;
  NIDCPOWER_ATTRIBUTE_AUTORANGE = 1150244;
  NIDCPOWER_ATTRIBUTE_AUTORANGE_BEHAVIOR = 1150245;
  NIDCPOWER_ATTRIBUTE_AUTORANGE_APERTURE_TIME_MODE = 1150246;
  NIDCPOWER_ATTRIBUTE_AUTORANGE_MINIMUM_APERTURE_TIME = 1150247;
  NIDCPOWER_ATTRIBUTE_AUTORANGE_MINIMUM_APERTURE_TIME_UNITS = 1150248;
  NIDCPOWER_ATTRIBUTE_MERGED_CHANNELS = 1150249;
  NIDCPOWER_ATTRIBUTE_AUTORANGE_MINIMUM_CURRENT_RANGE = 1150255;
  NIDCPOWER_ATTRIBUTE_AUTORANGE_MINIMUM_VOLTAGE_RANGE = 1150256;
  NIDCPOWER_ATTRIBUTE_AUTORANGE_THRESHOLD_MODE = 1150257;
  NIDCPOWER_ATTRIBUTE_LCR_CUSTOM_MEASUREMENT_TIME = 1150258;
  NIDCPOWER_ATTRIBUTE_ACTUAL_VOLTAGE_RANGE_FOR_LAST_FETCH = 1150259;
  NIDCPOWER_ATTRIBUTE_ACTUAL_CURRENT_RANGE_FOR_LAST_FETCH = 1150260;
  NIDCPOWER_ATTRIBUTE_LCR_OPEN_CONDUCTANCE = 1150261;
  NIDCPOWER_ATTRIBUTE_LCR_OPEN_SUSCEPTANCE = 1150262;
  NIDCPOWER_ATTRIBUTE_LCR_SHORT_RESISTANCE = 1150263;
  NIDCPOWER_ATTRIBUTE_LCR_SHORT_REACTANCE = 1150264;
  NIDCPOWER_ATTRIBUTE_LCR_VOLTAGE_RANGE = 1150265;
  NIDCPOWER_ATTRIBUTE_LCR_DC_BIAS_VOLTAGE_RANGE = 1150266;
  NIDCPOWER_ATTRIBUTE_LCR_CURRENT_RANGE = 1150267;
  NIDCPOWER_ATTRIBUTE_LCR_MEASURED_LOAD_RESISTANCE = 1150268;
  NIDCPOWER_ATTRIBUTE_LCR_MEASURED_LOAD_REACTANCE = 1150269;
  NIDCPOWER_ATTRIBUTE_LCR_ACTUAL_LOAD_RESISTANCE = 1150270;
  NIDCPOWER_ATTRIBUTE_LCR_ACTUAL_LOAD_REACTANCE = 1150271;
  NIDCPOWER_ATTRIBUTE_LCR_DC_BIAS_CURRENT_RANGE = 1150274;
  NIDCPOWER_ATTRIBUTE_SHUTDOWN_TRIGGER_TYPE = 1150275;
  NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_SHUTDOWN_TRIGGER_EDGE = 1150276;
  NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_SHUTDOWN_TRIGGER_INPUT_TERMINAL = 1150277;
  NIDCPOWER_ATTRIBUTE_CABLE_LENGTH = 1150278;
  NIDCPOWER_ATTRIBUTE_LCR_AUTOMATIC_LEVEL_CONTROL = 1150290;
  NIDCPOWER_ATTRIBUTE_LCR_DC_BIAS_AUTOMATIC_LEVEL_CONTROL = 1150291;
  NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_LOW = 1150292;
  NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_LOW = 1150293;
  NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_HIGH = 1150294;
  NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_HIGH = 1150295;
  NIDCPOWER_ATTRIBUTE_LCR_SHORT_CUSTOM_CABLE_COMPENSATION_ENABLED = 1150299;
  NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_DELAY = 1150300;
  NIDCPOWER_ATTRIBUTE_ISOLATION_STATE = 1150302;
  NIDCPOWER_ATTRIBUTE_APERTURE_TIME_AUTO_MODE = 1150314;
  NIDCPOWER_ATTRIBUTE_LCR_SOURCE_DELAY_MODE = 1150315;
  NIDCPOWER_ATTRIBUTE_LCR_LOAD_RESISTANCE = 1150318;
  NIDCPOWER_ATTRIBUTE_LCR_LOAD_INDUCTANCE = 1150319;
  NIDCPOWER_ATTRIBUTE_LCR_LOAD_CAPACITANCE = 1150320;
  NIDCPOWER_ATTRIBUTE_LCR_IMPEDANCE_RANGE_SOURCE = 1150321;
  NIDCPOWER_ATTRIBUTE_AUTORANGE_MAXIMUM_DELAY_AFTER_RANGE_CHANGE = 1150322;
  NIDCPOWER_ATTRIBUTE_VOLTAGE_LEVEL = 1250001;
  NIDCPOWER_ATTRIBUTE_OVP_ENABLED = 1250002;
  NIDCPOWER_ATTRIBUTE_OVP_LIMIT = 1250003;
  NIDCPOWER_ATTRIBUTE_CURRENT_LIMIT_BEHAVIOR = 1250004;
  NIDCPOWER_ATTRIBUTE_CURRENT_LIMIT = 1250005;
  NIDCPOWER_ATTRIBUTE_OUTPUT_ENABLED = 1250006;
}

enum ApertureTimeUnits {
  APERTURE_TIME_UNITS_UNSPECIFIED = 0;
  APERTURE_TIME_UNITS_NIDCPOWER_VAL_SECONDS = 1028;
  APERTURE_TIME_UNITS_NIDCPOWER_VAL_POWER_LINE_CYCLES = 1029;
}

enum AutoZero {
  AUTO_ZERO_NIDCPOWER_VAL_OFF = 0;
  AUTO_ZERO_NIDCPOWER_VAL_ON = 1;
  AUTO_ZERO_NIDCPOWER_VAL_ONCE = 1024;
}

enum CurrentLimitBehavior {
  CURRENT_LIMIT_BEHAVIOR_NIDCPOWER_VAL_CURRENT_REGULATE = 0;
  CURRENT_LIMIT_BEHAVIOR_NIDCPOWER_VAL_CURRENT_TRIP = 1;
}

enum DigitalEdge {
  DIGITAL_EDGE_UNSPECIFIED = 0;
  DIGITAL_EDGE_NIDCPOWER_VAL_RISING = 1016;
  DIGITAL_EDGE_NIDCPOWER_VAL_FALLING = 1017;
}

enum Event {
  EVENT_UNSPECIFIED = 0;
  EVENT_NIDCPOWER_VAL_SOURCE_COMPLETE = 1030;
  EVENT_NIDCPOWER_VAL_MEASURE_COMPLETE = 1031;
  EVENT_NIDCPOWER_VAL_SEQUENCE_ITERATION_COMPLETE = 1032;
  EVENT_NIDCPOWER_VAL_SEQUENCE_ENGINE_DONE = 1033;
  EVENT_NIDCPOWER_VAL_PULSE_COMPLETE = 1051;
  EVENT_NIDCPOWER_VAL_READY_FOR_PULSE_TRIGGER = 1052;
}

enum ExportSignal {
  EXPORT_SIGNAL_UNSPECIFIED = 0;
  EXPORT_SIGNAL_NIDCPOWER_VAL_SOURCE_COMPLETE_EVENT = 1030;
  EXPORT_SIGNAL_NIDCPOWER_VAL_MEASURE_COMPLETE_EVENT = 1031;
  EXPORT_SIGNAL_NIDCPOWER_VAL_SEQUENCE_ITERATION_COMPLETE_EVENT = 1032;
  EXPORT_SIGNAL_NIDCPOWER_VAL_SEQUENCE_ENGINE_DONE_EVENT = 1033;
  EXPORT_SIGNAL_NIDCPOWER_VAL_PULSE_COMPLETE_EVENT = 1051;
  EXPORT_SIGNAL_NIDCPOWER_VAL_READY_FOR_PULSE_TRIGGER_EVENT = 1052;
  EXPORT_SIGNAL_NIDCPOWER_VAL_START_TRIGGER = 1034;
  EXPORT_SIGNAL_NIDCPOWER_VAL_SOURCE_TRIGGER = 1035;
  EXPORT_SIGNAL_NIDCPOWER_VAL_MEASURE_TRIGGER = 1036;
  EXPORT_SIGNAL_NIDCPOWER_VAL_SEQUENCE_ADVANCE_TRIGGER = 1037;
  EXPORT_SIGNAL_NIDCPOWER_VAL_PULSE_TRIGGER = 1053;
  EXPORT_SIGNAL_NIDCPOWER_VAL_SHUTDOWN_TRIGGER = 1118;
}

enum LCRCompensationType {
  LCR_COMPENSATION_TYPE_UNSPECIFIED = 0;
  LCR_COMPENSATION_TYPE_NIDCPOWER_VAL_OPEN_COMPENSATION = 1130;
  LCR_COMPENSATION_TYPE_NIDCPOWER_VAL_SHORT_COMPENSATION = 1131;
  LCR_COMPENSATION_TYPE_NIDCPOWER_VAL_LOAD_COMPENSATION = 1132;
  LCR_COMPENSATION_TYPE_NIDCPOWER_VAL_OPEN_CUSTOM_CABLE_COMPENSATION = 1133;
  LCR_COMPENSATION_TYPE_NIDCPOWER_VAL_SHORT_CUSTOM_CABLE_COMPENSATION = 1134;
}

enum MeasurementTypes {
  MEASUREMENT_TYPES_NIDCPOWER_VAL_MEASURE_CURRENT = 0;
  MEASUREMENT_TYPES_NIDCPOWER_VAL_MEASURE_VOLTAGE = 1;
}

enum NiDCPowerInt32AttributeValues {
  option allow_alias = true;
  NIDCPOWER_INT32_UNSPECIFIED = 0;
  NIDCPOWER_INT32_APERTURE_TIME_AUTO_MODE_VAL_APERTURE_TIME_AUTO_MODE_OFF = 1135;
  NIDCPOWER_INT32_APERTURE_TIME_AUTO_MODE_VAL_APERTURE_TIME_AUTO_MODE_SHORT = 1136;
  NIDCPOWER_INT32_APERTURE_TIME_AUTO_MODE_VAL_APERTURE_TIME_AUTO_MODE_NORMAL = 1137;
  NIDCPOWER_INT32_APERTURE_TIME_AUTO_MODE_VAL_APERTURE_TIME_AUTO_MODE_LONG = 1138;
  NIDCPOWER_INT32_APERTURE_TIME_UNITS_VAL_SECONDS = 1028;
  NIDCPOWER_INT32_APERTURE_TIME_UNITS_VAL_POWER_LINE_CYCLES = 1029;
  NIDCPOWER_INT32_AUTO_ZERO_VAL_OFF = 0;
  NIDCPOWER_INT32_AUTO_ZERO_VAL_ON = 1;
  NIDCPOWER_INT32_AUTO_ZERO_VAL_ONCE = 1024;
  NIDCPOWER_INT32_AUTORANGE_APERTURE_TIME_MODE_VAL_APERTURE_TIME_AUTO = 1110;
  NIDCPOWER_INT32_AUTORANGE_APERTURE_TIME_MODE_VAL_APERTURE_TIME_CUSTOM = 1111;
  NIDCPOWER_INT32_AUTORANGE_BEHAVIOR_VAL_RANGE_UP_TO_LIMIT_THEN_DOWN = 1107;
  NIDCPOWER_INT32_AUTORANGE_BEHAVIOR_VAL_RANGE_UP = 1108;
  NIDCPOWER_INT32_AUTORANGE_BEHAVIOR_VAL_RANGE_UP_AND_DOWN = 1109;
  NIDCPOWER_INT32_AUTORANGE_THRESHOLD_MODE_VAL_THRESHOLD_MODE_NORMAL = 1112;
  NIDCPOWER_INT32_AUTORANGE_THRESHOLD_MODE_VAL_THRESHOLD_MODE_FAST_STEP = 1113;
  NIDCPOWER_INT32_AUTORANGE_THRESHOLD_MODE_VAL_THRESHOLD_MODE_HIGH_HYSTERESIS = 1114;
  NIDCPOWER_INT32_AUTORANGE_THRESHOLD_MODE_VAL_THRESHOLD_MODE_MEDIUM_HYSTERESIS = 1115;
  NIDCPOWER_INT32_AUTORANGE_THRESHOLD_MODE_VAL_THRESHOLD_MODE_HOLD = 1116;
  NIDCPOWER_INT32_CABLE_LENGTH_VAL_ZERO_M = 1121;
  NIDCPOWER_INT32_CABLE_LENGTH_VAL_NI_STANDARD_1M = 1122;
  NIDCPOWER_INT32_CABLE_LENGTH_VAL_NI_STANDARD_2M = 1123;
  NIDCPOWER_INT32_CABLE_LENGTH_VAL_NI_STANDARD_4M = 1124;
  NIDCPOWER_INT32_CABLE_LENGTH_VAL_CUSTOM_ONBOARD_STORAGE = 1125;
  NIDCPOWER_INT32_CABLE_LENGTH_VAL_CUSTOM_AS_CONFIGURED = 1126;
  NIDCPOWER_INT32_CABLE_LENGTH_VAL_NI_STANDARD_TRIAXIAL_1M = 1139;
  NIDCPOWER_INT32_CABLE_LENGTH_VAL_NI_STANDARD_TRIAXIAL_2M = 1140;
  NIDCPOWER_INT32_CABLE_LENGTH_VAL_NI_STANDARD_TRIAXIAL_4M = 1141;
  NIDCPOWER_INT32_COMPLIANCE_LIMIT_SYMMETRY_VAL_SYMMETRIC = 0;
  NIDCPOWER_INT32_COMPLIANCE_LIMIT_SYMMETRY_VAL_ASYMMETRIC = 1;
  NIDCPOWER_INT32_CURRENT_LIMIT_BEHAVIOR_VAL_CURRENT_REGULATE = 0;
  NIDCPOWER_INT32_CURRENT_LIMIT_BEHAVIOR_VAL_CURRENT_TRIP = 1;
  NIDCPOWER_INT32_DC_NOISE_REJECTION_VAL_DC_NOISE_REJECTION_SECOND_ORDER = 1043;
  NIDCPOWER_INT32_DC_NOISE_REJECTION_VAL_DC_NOISE_REJECTION_NORMAL = 1044;
  NIDCPOWER_INT32_DIGITAL_EDGE_VAL_RISING = 1016;
  NIDCPOWER_INT32_DIGITAL_EDGE_VAL_FALLING = 1017;
  NIDCPOWER_INT32_INSTRUMENT_MODE_VAL_SMU_PS = 1061;
  NIDCPOWER_INT32_INSTRUMENT_MODE_VAL_LCR = 1062;
  NIDCPOWER_INT32_ISOLATION_STATE_VAL_ISOLATED = 1128;
  NIDCPOWER_INT32_ISOLATION_STATE_VAL_NON_ISOLATED = 1129;
  NIDCPOWER_INT32_LCR_AUTOMATIC_LEVEL_CONTROL_VAL_OFF = 0;
  NIDCPOWER_INT32_LCR_AUTOMATIC_LEVEL_CONTROL_VAL_ON = 1;
  NIDCPOWER_INT32_LCRDC_BIAS_SOURCE_VAL_DC_BIAS_OFF = 1065;
  NIDCPOWER_INT32_LCRDC_BIAS_SOURCE_VAL_DC_BIAS_VOLTAGE = 1066;
  NIDCPOWER_INT32_LCRDC_BIAS_SOURCE_VAL_DC_BIAS_CURRENT = 1067;
  NIDCPOWER_INT32_LCR_IMPEDANCE_AUTO_RANGE_VAL_AUTO_RANGE_OFF = 1068;
  NIDCPOWER_INT32_LCR_IMPEDANCE_AUTO_RANGE_VAL_AUTO_RANGE_ON = 1070;
  NIDCPOWER_INT32_LCR_IMPEDANCE_RANGE_SOURCE_VAL_LCR_IMPEDANCE_RANGE = 1142;
  NIDCPOWER_INT32_LCR_IMPEDANCE_RANGE_SOURCE_VAL_LCR_LOAD_CONFIGURATION = 1143;
  NIDCPOWER_INT32_LCR_MEASUREMENT_TIME_VAL_MEASUREMENT_TIME_SHORT = 1071;
  NIDCPOWER_INT32_LCR_MEASUREMENT_TIME_VAL_MEASUREMENT_TIME_MEDIUM = 1072;
  NIDCPOWER_INT32_LCR_MEASUREMENT_TIME_VAL_MEASUREMENT_TIME_LONG = 1073;
  NIDCPOWER_INT32_LCR_MEASUREMENT_TIME_VAL_MEASUREMENT_TIME_CUSTOM = 1117;
  NIDCPOWER_INT32_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE_VAL_ONBOARD_STORAGE = 1074;
  NIDCPOWER_INT32_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE_VAL_AS_DEFINED = 1075;
  NIDCPOWER_INT32_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE_VAL_AS_CONFIGURED = 1146;
  NIDCPOWER_INT32_LCR_SOURCE_DELAY_MODE_VAL_LCR_SOURCE_DELAY_MODE_AUTOMATIC = 1144;
  NIDCPOWER_INT32_LCR_SOURCE_DELAY_MODE_VAL_LCR_SOURCE_DELAY_MODE_MANUAL = 1145;
  NIDCPOWER_INT32_LCR_STIMULUS_FUNCTION_VAL_AC_VOLTAGE = 1063;
  NIDCPOWER_INT32_LCR_STIMULUS_FUNCTION_VAL_AC_CURRENT = 1064;
  NIDCPOWER_INT32_MEASURE_WHEN_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE = 1025;
  NIDCPOWER_INT32_MEASURE_WHEN_VAL_ON_DEMAND = 1026;
  NIDCPOWER_INT32_MEASURE_WHEN_VAL_ON_MEASURE_TRIGGER = 1027;
  NIDCPOWER_INT32_OUTPUT_CAPACITANCE_VAL_LOW = 1010;
  NIDCPOWER_INT32_OUTPUT_CAPACITANCE_VAL_HIGH = 1011;
  NIDCPOWER_INT32_OUTPUT_FUNCTION_VAL_DC_VOLTAGE = 1006;
  NIDCPOWER_INT32_OUTPUT_FUNCTION_VAL_DC_CURRENT = 1007;
  NIDCPOWER_INT32_OUTPUT_FUNCTION_VAL_PULSE_VOLTAGE = 1049;
  NIDCPOWER_INT32_OUTPUT_FUNCTION_VAL_PULSE_CURRENT = 1050;
  NIDCPOWER_INT32_POLARITY_VAL_ACTIVE_HIGH = 1018;
  NIDCPOWER_INT32_POLARITY_VAL_ACTIVE_LOW = 1019;
  NIDCPOWER_INT32_POWER_ALLOCATION_MODE_VAL_DISABLED = 1058;
  NIDCPOWER_INT32_POWER_ALLOCATION_MODE_VAL_AUTOMATIC = 1059;
  NIDCPOWER_INT32_POWER_ALLOCATION_MODE_VAL_MANUAL = 1060;
  NIDCPOWER_INT32_POWER_SOURCE_VAL_INTERNAL = 1003;
  NIDCPOWER_INT32_POWER_SOURCE_VAL_AUXILIARY = 1004;
  NIDCPOWER_INT32_POWER_SOURCE_VAL_AUTOMATIC = 1005;
  NIDCPOWER_INT32_POWER_SOURCE_IN_USE_VAL_INTERNAL = 1003;
  NIDCPOWER_INT32_POWER_SOURCE_IN_USE_VAL_AUXILIARY = 1004;
  NIDCPOWER_INT32_SELF_CALIBRATION_PERSISTENCE_VAL_KEEP_IN_MEMORY = 1045;
  NIDCPOWER_INT32_SELF_CALIBRATION_PERSISTENCE_VAL_WRITE_TO_EEPROM = 1046;
  NIDCPOWER_INT32_SENSE_VAL_LOCAL = 1008;
  NIDCPOWER_INT32_SENSE_VAL_REMOTE = 1009;
  NIDCPOWER_INT32_SOURCE_MODE_VAL_SINGLE_POINT = 1020;
  NIDCPOWER_INT32_SOURCE_MODE_VAL_SEQUENCE = 1021;
  NIDCPOWER_INT32_TRANSIENT_RESPONSE_VAL_NORMAL = 1038;
  NIDCPOWER_INT32_TRANSIENT_RESPONSE_VAL_FAST = 1039;
  NIDCPOWER_INT32_TRANSIENT_RESPONSE_VAL_SLOW = 1041;
  NIDCPOWER_INT32_TRANSIENT_RESPONSE_VAL_CUSTOM = 1042;
  NIDCPOWER_INT32_TRIGGER_TYPE_VAL_NONE = 1012;
  NIDCPOWER_INT32_TRIGGER_TYPE_VAL_DIGITAL_EDGE = 1014;
  NIDCPOWER_INT32_TRIGGER_TYPE_VAL_SOFTWARE_EDGE = 1015;
}

enum NiDCPowerReal64AttributeValues {
  NIDCPOWER_REAL64_UNSPECIFIED = 0;
  NIDCPOWER_REAL64_POWER_LINE_FREQUENCIES_VAL_50_HERTZ = 50;
  NIDCPOWER_REAL64_POWER_LINE_FREQUENCIES_VAL_60_HERTZ = 60;
}

enum OutputCutoffReason {
  OUTPUT_CUTOFF_REASON_UNSPECIFIED = 0;
  OUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_ALL = -1;
  OUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_OUTPUT_HIGH = 1;
  OUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_OUTPUT_LOW = 2;
  OUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_MEASURE_HIGH = 4;
  OUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_MEASURE_LOW = 8;
  OUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_CHANGE_HIGH = 16;
  OUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_CHANGE_LOW = 32;
  OUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_CHANGE_HIGH = 64;
  OUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_CHANGE_LOW = 128;
}

enum OutputFunction {
  OUTPUT_FUNCTION_UNSPECIFIED = 0;
  OUTPUT_FUNCTION_NIDCPOWER_VAL_DC_VOLTAGE = 1006;
  OUTPUT_FUNCTION_NIDCPOWER_VAL_DC_CURRENT = 1007;
  OUTPUT_FUNCTION_NIDCPOWER_VAL_PULSE_VOLTAGE = 1049;
  OUTPUT_FUNCTION_NIDCPOWER_VAL_PULSE_CURRENT = 1050;
}

enum OutputStates {
  OUTPUT_STATES_NIDCPOWER_VAL_OUTPUT_CONSTANT_VOLTAGE = 0;
  OUTPUT_STATES_NIDCPOWER_VAL_OUTPUT_CONSTANT_CURRENT = 1;
  OUTPUT_STATES_NIDCPOWER_VAL_OUTPUT_OVER_VOLTAGE = 2;
  OUTPUT_STATES_NIDCPOWER_VAL_OUTPUT_OVER_CURRENT = 3;
  OUTPUT_STATES_NIDCPOWER_VAL_OUTPUT_UNREGULATED = 4;
}

enum PowerLineFrequencies {
  POWER_LINE_FREQUENCIES_UNSPECIFIED = 0;
  POWER_LINE_FREQUENCIES_NIDCPOWER_VAL_50_HERTZ = 50;
  POWER_LINE_FREQUENCIES_NIDCPOWER_VAL_60_HERTZ = 60;
}

enum SendSoftwareEdgeTriggerType {
  SEND_SOFTWARE_EDGE_TRIGGER_TYPE_UNSPECIFIED = 0;
  SEND_SOFTWARE_EDGE_TRIGGER_TYPE_NIDCPOWER_VAL_START = 1034;
  SEND_SOFTWARE_EDGE_TRIGGER_TYPE_NIDCPOWER_VAL_SOURCE = 1035;
  SEND_SOFTWARE_EDGE_TRIGGER_TYPE_NIDCPOWER_VAL_MEASURE = 1036;
  SEND_SOFTWARE_EDGE_TRIGGER_TYPE_NIDCPOWER_VAL_SEQUENCE_ADVANCE = 1037;
  SEND_SOFTWARE_EDGE_TRIGGER_TYPE_NIDCPOWER_VAL_PULSE = 1053;
  SEND_SOFTWARE_EDGE_TRIGGER_TYPE_NIDCPOWER_VAL_SHUTDOWN = 1118;
}

enum Sense {
  SENSE_UNSPECIFIED = 0;
  SENSE_NIDCPOWER_VAL_LOCAL = 1008;
  SENSE_NIDCPOWER_VAL_REMOTE = 1009;
}

enum SourceMode {
  SOURCE_MODE_UNSPECIFIED = 0;
  SOURCE_MODE_NIDCPOWER_VAL_SINGLE_POINT = 1020;
  SOURCE_MODE_NIDCPOWER_VAL_SEQUENCE = 1021;
}

message NILCRLoadCompensationSpot {
  double frequency = 1;
  sint32 reference_value_type = 2;
  double reference_value_a = 3;
  double reference_value_b = 4;
}

message NILCRMeasurement {
  double vdc = 1;
  double idc = 2;
  double stimulus_frequency = 3;
  nidevice_grpc.NIComplexNumber ac_voltage = 4;
  nidevice_grpc.NIComplexNumber ac_current = 5;
  nidevice_grpc.NIComplexNumber z = 6;
  double z_magnitude = 7;
  double z_phase = 8;
  nidevice_grpc.NIComplexNumber y = 9;
  double y_magnitude = 10;
  double y_phase = 11;
  double ls = 12;
  double cs = 13;
  double rs = 14;
  double lp = 15;
  double cp = 16;
  double rp = 17;
  double d = 18;
  double q = 19;
  uint32 measurement_mode = 20;
  bool dc_in_compliance = 21;
  bool ac_in_compliance = 22;
  bool unbalanced = 23;
}

message AbortRequest {
  nidevice_grpc.Session vi = 1;
}

message AbortResponse {
  int32 status = 1;
}

message AbortWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message AbortWithChannelsResponse {
  int32 status = 1;
}

message CalSelfCalibrateRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message CalSelfCalibrateResponse {
  int32 status = 1;
}

message ClearErrorRequest {
  nidevice_grpc.Session vi = 1;
}

message ClearErrorResponse {
  int32 status = 1;
}

message ClearInterchangeWarningsRequest {
  nidevice_grpc.Session vi = 1;
}

message ClearInterchangeWarningsResponse {
  int32 status = 1;
}

message ClearLatchedOutputCutoffStateRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  oneof output_cutoff_reason_enum {
    OutputCutoffReason output_cutoff_reason = 3;
    sint32 output_cutoff_reason_raw = 4;
  }
}

message ClearLatchedOutputCutoffStateResponse {
  int32 status = 1;
}

message CloseRequest {
  nidevice_grpc.Session vi = 1;
}

message CloseResponse {
  int32 status = 1;
}

message CommitRequest {
  nidevice_grpc.Session vi = 1;
}

message CommitResponse {
  int32 status = 1;
}

message CommitWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message CommitWithChannelsResponse {
  int32 status = 1;
}

message ConfigureApertureTimeRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double aperture_time = 3;
  oneof units_enum {
    ApertureTimeUnits units = 4;
    sint32 units_raw = 5;
  }
}

message ConfigureApertureTimeResponse {
  int32 status = 1;
}

message ConfigureAutoZeroRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  oneof auto_zero_enum {
    AutoZero auto_zero = 3;
    sint32 auto_zero_raw = 4;
  }
}

message ConfigureAutoZeroResponse {
  int32 status = 1;
}

message ConfigureCurrentLevelRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double level = 3;
}

message ConfigureCurrentLevelResponse {
  int32 status = 1;
}

message ConfigureCurrentLevelRangeRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double range = 3;
}

message ConfigureCurrentLevelRangeResponse {
  int32 status = 1;
}

message ConfigureCurrentLimitRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  oneof behavior_enum {
    CurrentLimitBehavior behavior = 3;
    sint32 behavior_raw = 4;
  }
  double limit = 5;
}

message ConfigureCurrentLimitResponse {
  int32 status = 1;
}

message ConfigureCurrentLimitRangeRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double range = 3;
}

message ConfigureCurrentLimitRangeResponse {
  int32 status = 1;
}

message ConfigureDigitalEdgeMeasureTriggerRequest {
  nidevice_grpc.Session vi = 1;
  string input_terminal = 2;
  oneof edge_enum {
    DigitalEdge edge = 3;
    sint32 edge_raw = 4;
  }
}

message ConfigureDigitalEdgeMeasureTriggerResponse {
  int32 status = 1;
}

message ConfigureDigitalEdgeMeasureTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string input_terminal = 3;
  oneof edge_enum {
    DigitalEdge edge = 4;
    sint32 edge_raw = 5;
  }
}

message ConfigureDigitalEdgeMeasureTriggerWithChannelsResponse {
  int32 status = 1;
}

message ConfigureDigitalEdgePulseTriggerRequest {
  nidevice_grpc.Session vi = 1;
  string input_terminal = 2;
  oneof edge_enum {
    DigitalEdge edge = 3;
    sint32 edge_raw = 4;
  }
}

message ConfigureDigitalEdgePulseTriggerResponse {
  int32 status = 1;
}

message ConfigureDigitalEdgePulseTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string input_terminal = 3;
  oneof edge_enum {
    DigitalEdge edge = 4;
    sint32 edge_raw = 5;
  }
}

message ConfigureDigitalEdgePulseTriggerWithChannelsResponse {
  int32 status = 1;
}

message ConfigureDigitalEdgeSequenceAdvanceTriggerRequest {
  nidevice_grpc.Session vi = 1;
  string input_terminal = 2;
  oneof edge_enum {
    DigitalEdge edge = 3;
    sint32 edge_raw = 4;
  }
}

message ConfigureDigitalEdgeSequenceAdvanceTriggerResponse {
  int32 status = 1;
}

message ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string input_terminal = 3;
  oneof edge_enum {
    DigitalEdge edge = 4;
    sint32 edge_raw = 5;
  }
}

message ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannelsResponse {
  int32 status = 1;
}

message ConfigureDigitalEdgeShutdownTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string input_terminal = 3;
  oneof edge_enum {
    DigitalEdge edge = 4;
    sint32 edge_raw = 5;
  }
}

message ConfigureDigitalEdgeShutdownTriggerWithChannelsResponse {
  int32 status = 1;
}

message ConfigureDigitalEdgeSourceTriggerRequest {
  nidevice_grpc.Session vi = 1;
  string input_terminal = 2;
  oneof edge_enum {
    DigitalEdge edge = 3;
    sint32 edge_raw = 4;
  }
}

message ConfigureDigitalEdgeSourceTriggerResponse {
  int32 status = 1;
}

message ConfigureDigitalEdgeSourceTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string input_terminal = 3;
  oneof edge_enum {
    DigitalEdge edge = 4;
    sint32 edge_raw = 5;
  }
}

message ConfigureDigitalEdgeSourceTriggerWithChannelsResponse {
  int32 status = 1;
}

message ConfigureDigitalEdgeStartTriggerRequest {
  nidevice_grpc.Session vi = 1;
  string input_terminal = 2;
  oneof edge_enum {
    DigitalEdge edge = 3;
    sint32 edge_raw = 4;
  }
}

message ConfigureDigitalEdgeStartTriggerResponse {
  int32 status = 1;
}

message ConfigureDigitalEdgeStartTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string input_terminal = 3;
  oneof edge_enum {
    DigitalEdge edge = 4;
    sint32 edge_raw = 5;
  }
}

message ConfigureDigitalEdgeStartTriggerWithChannelsResponse {
  int32 status = 1;
}

message ConfigureLCRCustomCableCompensationRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  bytes custom_cable_compensation_data = 3;
}

message ConfigureLCRCustomCableCompensationResponse {
  int32 status = 1;
}

message ConfigureOutputEnabledRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  bool enabled = 3;
}

message ConfigureOutputEnabledResponse {
  int32 status = 1;
}

message ConfigureOutputFunctionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  oneof function_enum {
    OutputFunction function = 3;
    sint32 function_raw = 4;
  }
}

message ConfigureOutputFunctionResponse {
  int32 status = 1;
}

message ConfigureOutputResistanceRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double resistance = 3;
}

message ConfigureOutputResistanceResponse {
  int32 status = 1;
}

message ConfigureOvpRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  bool enabled = 3;
  double limit = 4;
}

message ConfigureOvpResponse {
  int32 status = 1;
}

message ConfigurePowerLineFrequencyRequest {
  nidevice_grpc.Session vi = 1;
  oneof powerline_frequency_enum {
    PowerLineFrequencies powerline_frequency = 2;
    double powerline_frequency_raw = 3;
  }
}

message ConfigurePowerLineFrequencyResponse {
  int32 status = 1;
}

message ConfigurePulseBiasCurrentLevelRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double level = 3;
}

message ConfigurePulseBiasCurrentLevelResponse {
  int32 status = 1;
}

message ConfigurePulseBiasCurrentLimitRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double limit = 3;
}

message ConfigurePulseBiasCurrentLimitResponse {
  int32 status = 1;
}

message ConfigurePulseBiasVoltageLevelRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double level = 3;
}

message ConfigurePulseBiasVoltageLevelResponse {
  int32 status = 1;
}

message ConfigurePulseBiasVoltageLimitRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double limit = 3;
}

message ConfigurePulseBiasVoltageLimitResponse {
  int32 status = 1;
}

message ConfigurePulseCurrentLevelRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double level = 3;
}

message ConfigurePulseCurrentLevelResponse {
  int32 status = 1;
}

message ConfigurePulseCurrentLevelRangeRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double range = 3;
}

message ConfigurePulseCurrentLevelRangeResponse {
  int32 status = 1;
}

message ConfigurePulseCurrentLimitRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double limit = 3;
}

message ConfigurePulseCurrentLimitResponse {
  int32 status = 1;
}

message ConfigurePulseCurrentLimitRangeRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double range = 3;
}

message ConfigurePulseCurrentLimitRangeResponse {
  int32 status = 1;
}

message ConfigurePulseVoltageLevelRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double level = 3;
}

message ConfigurePulseVoltageLevelResponse {
  int32 status = 1;
}

message ConfigurePulseVoltageLevelRangeRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double range = 3;
}

message ConfigurePulseVoltageLevelRangeResponse {
  int32 status = 1;
}

message ConfigurePulseVoltageLimitRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double limit = 3;
}

message ConfigurePulseVoltageLimitResponse {
  int32 status = 1;
}

message ConfigurePulseVoltageLimitRangeRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double range = 3;
}

message ConfigurePulseVoltageLimitRangeResponse {
  int32 status = 1;
}

message ConfigureSenseRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  oneof sense_enum {
    Sense sense = 3;
    sint32 sense_raw = 4;
  }
}

message ConfigureSenseResponse {
  int32 status = 1;
}

message ConfigureSoftwareEdgeMeasureTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message ConfigureSoftwareEdgeMeasureTriggerResponse {
  int32 status = 1;
}

message ConfigureSoftwareEdgeMeasureTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message ConfigureSoftwareEdgeMeasureTriggerWithChannelsResponse {
  int32 status = 1;
}

message ConfigureSoftwareEdgePulseTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message ConfigureSoftwareEdgePulseTriggerResponse {
  int32 status = 1;
}

message ConfigureSoftwareEdgePulseTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message ConfigureSoftwareEdgePulseTriggerWithChannelsResponse {
  int32 status = 1;
}

message ConfigureSoftwareEdgeSequenceAdvanceTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message ConfigureSoftwareEdgeSequenceAdvanceTriggerResponse {
  int32 status = 1;
}

message ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannelsResponse {
  int32 status = 1;
}

message ConfigureSoftwareEdgeShutdownTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message ConfigureSoftwareEdgeShutdownTriggerWithChannelsResponse {
  int32 status = 1;
}

message ConfigureSoftwareEdgeSourceTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message ConfigureSoftwareEdgeSourceTriggerResponse {
  int32 status = 1;
}

message ConfigureSoftwareEdgeSourceTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message ConfigureSoftwareEdgeSourceTriggerWithChannelsResponse {
  int32 status = 1;
}

message ConfigureSoftwareEdgeStartTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message ConfigureSoftwareEdgeStartTriggerResponse {
  int32 status = 1;
}

message ConfigureSoftwareEdgeStartTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message ConfigureSoftwareEdgeStartTriggerWithChannelsResponse {
  int32 status = 1;
}

message ConfigureSourceModeRequest {
  nidevice_grpc.Session vi = 1;
  oneof source_mode_enum {
    SourceMode source_mode = 2;
    sint32 source_mode_raw = 3;
  }
}

message ConfigureSourceModeResponse {
  int32 status = 1;
}

message ConfigureSourceModeWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  oneof source_mode_enum {
    SourceMode source_mode = 3;
    sint32 source_mode_raw = 4;
  }
}

message ConfigureSourceModeWithChannelsResponse {
  int32 status = 1;
}

message ConfigureVoltageLevelRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double level = 3;
}

message ConfigureVoltageLevelResponse {
  int32 status = 1;
}

message ConfigureVoltageLevelRangeRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double range = 3;
}

message ConfigureVoltageLevelRangeResponse {
  int32 status = 1;
}

message ConfigureVoltageLimitRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double limit = 3;
}

message ConfigureVoltageLimitResponse {
  int32 status = 1;
}

message ConfigureVoltageLimitRangeRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double range = 3;
}

message ConfigureVoltageLimitRangeResponse {
  int32 status = 1;
}

message CreateAdvancedSequenceRequest {
  nidevice_grpc.Session vi = 1;
  string sequence_name = 2;
  repeated sint32 attribute_ids = 3;
  bool set_as_active_sequence = 4;
}

message CreateAdvancedSequenceResponse {
  int32 status = 1;
}

message CreateAdvancedSequenceCommitStepWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  bool set_as_active_step = 3;
}

message CreateAdvancedSequenceCommitStepWithChannelsResponse {
  int32 status = 1;
}

message CreateAdvancedSequenceStepRequest {
  nidevice_grpc.Session vi = 1;
  bool set_as_active_step = 2;
}

message CreateAdvancedSequenceStepResponse {
  int32 status = 1;
}

message CreateAdvancedSequenceStepWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  bool set_as_active_step = 3;
}

message CreateAdvancedSequenceStepWithChannelsResponse {
  int32 status = 1;
}

message CreateAdvancedSequenceWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string sequence_name = 3;
  repeated sint32 attribute_ids = 4;
  bool set_as_active_sequence = 5;
}

message CreateAdvancedSequenceWithChannelsResponse {
  int32 status = 1;
}

message DeleteAdvancedSequenceRequest {
  nidevice_grpc.Session vi = 1;
  string sequence_name = 2;
}

message DeleteAdvancedSequenceResponse {
  int32 status = 1;
}

message DeleteAdvancedSequenceWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string sequence_name = 3;
}

message DeleteAdvancedSequenceWithChannelsResponse {
  int32 status = 1;
}

message DisableRequest {
  nidevice_grpc.Session vi = 1;
}

message DisableResponse {
  int32 status = 1;
}

message DisablePulseTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message DisablePulseTriggerResponse {
  int32 status = 1;
}

message DisablePulseTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message DisablePulseTriggerWithChannelsResponse {
  int32 status = 1;
}

message DisableSequenceAdvanceTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message DisableSequenceAdvanceTriggerResponse {
  int32 status = 1;
}

message DisableSequenceAdvanceTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message DisableSequenceAdvanceTriggerWithChannelsResponse {
  int32 status = 1;
}

message DisableShutdownTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message DisableShutdownTriggerWithChannelsResponse {
  int32 status = 1;
}

message DisableSourceTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message DisableSourceTriggerResponse {
  int32 status = 1;
}

message DisableSourceTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message DisableSourceTriggerWithChannelsResponse {
  int32 status = 1;
}

message DisableStartTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message DisableStartTriggerResponse {
  int32 status = 1;
}

message DisableStartTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message DisableStartTriggerWithChannelsResponse {
  int32 status = 1;
}

message ErrorMessageRequest {
  nidevice_grpc.Session vi = 1;
  sint32 error_code = 2;
}

message ErrorMessageResponse {
  int32 status = 1;
  string error_message = 2;
}

message ErrorQueryRequest {
  nidevice_grpc.Session vi = 1;
}

message ErrorQueryResponse {
  int32 status = 1;
  sint32 error_code = 2;
  string error_message = 3;
}

message ExportAttributeConfigurationBufferRequest {
  nidevice_grpc.Session vi = 1;
}

message ExportAttributeConfigurationBufferResponse {
  int32 status = 1;
  bytes configuration = 2;
}

message ExportAttributeConfigurationFileRequest {
  nidevice_grpc.Session vi = 1;
  string file_path = 2;
}

message ExportAttributeConfigurationFileResponse {
  int32 status = 1;
}

message ExportSignalRequest {
  nidevice_grpc.Session vi = 1;
  oneof signal_enum {
    ExportSignal signal = 2;
    sint32 signal_raw = 3;
  }
  string signal_identifier = 4;
  string output_terminal = 5;
}

message ExportSignalResponse {
  int32 status = 1;
}

message ExportSignalWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  oneof signal_enum {
    ExportSignal signal = 3;
    sint32 signal_raw = 4;
  }
  string signal_identifier = 5;
  string output_terminal = 6;
}

message ExportSignalWithChannelsResponse {
  int32 status = 1;
}

message FetchMultipleRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double timeout = 3;
  sint32 count = 4;
}

message FetchMultipleResponse {
  int32 status = 1;
  repeated double voltage_measurements = 2;
  repeated double current_measurements = 3;
  repeated bool in_compliance = 4;
  sint32 actual_count = 5;
}

message FetchMultipleLCRRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double timeout = 3;
  sint32 count = 4;
}

message FetchMultipleLCRResponse {
  int32 status = 1;
  repeated NILCRMeasurement measurements = 2;
  sint32 actual_count = 3;
}

message GetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDCPowerAttribute attribute_id = 3;
}

message GetAttributeViBooleanResponse {
  int32 status = 1;
  bool attribute_value = 2;
}

message GetAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDCPowerAttribute attribute_id = 3;
}

message GetAttributeViInt32Response {
  int32 status = 1;
  sint32 attribute_value = 2;
}

message GetAttributeViInt64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDCPowerAttribute attribute_id = 3;
}

message GetAttributeViInt64Response {
  int32 status = 1;
  int64 attribute_value = 2;
}

message GetAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDCPowerAttribute attribute_id = 3;
}

message GetAttributeViReal64Response {
  int32 status = 1;
  double attribute_value = 2;
}

message GetAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDCPowerAttribute attribute_id = 3;
}

message GetAttributeViSessionResponse {
  int32 status = 1;
  nidevice_grpc.Session attribute_value = 2;
}

message GetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDCPowerAttribute attribute_id = 3;
}

message GetAttributeViStringResponse {
  int32 status = 1;
  string attribute_value = 2;
}

message GetChannelNameRequest {
  nidevice_grpc.Session vi = 1;
  sint32 index = 2;
}

message GetChannelNameResponse {
  int32 status = 1;
  string channel_name = 2;
}

message GetChannelNameFromStringRequest {
  nidevice_grpc.Session vi = 1;
  string index = 2;
}

message GetChannelNameFromStringResponse {
  int32 status = 1;
  string channel_name = 2;
}

message GetErrorRequest {
  nidevice_grpc.Session vi = 1;
}

message GetErrorResponse {
  int32 status = 1;
  sint32 code = 2;
  string description = 3;
}

message GetExtCalLastDateAndTimeRequest {
  nidevice_grpc.Session vi = 1;
}

message GetExtCalLastDateAndTimeResponse {
  int32 status = 1;
  sint32 year = 2;
  sint32 month = 3;
  sint32 day = 4;
  sint32 hour = 5;
  sint32 minute = 6;
}

message GetExtCalLastTempRequest {
  nidevice_grpc.Session vi = 1;
}

message GetExtCalLastTempResponse {
  int32 status = 1;
  double temperature = 2;
}

message GetExtCalRecommendedIntervalRequest {
  nidevice_grpc.Session vi = 1;
}

message GetExtCalRecommendedIntervalResponse {
  int32 status = 1;
  sint32 months = 2;
}

message GetLCRCompensationLastDateAndTimeRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  oneof compensation_type_enum {
    LCRCompensationType compensation_type = 3;
    sint32 compensation_type_raw = 4;
  }
}

message GetLCRCompensationLastDateAndTimeResponse {
  int32 status = 1;
  sint32 year = 2;
  sint32 month = 3;
  sint32 day = 4;
  sint32 hour = 5;
  sint32 minute = 6;
}

message GetLCRCustomCableCompensationDataRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message GetLCRCustomCableCompensationDataResponse {
  int32 status = 1;
  bytes custom_cable_compensation_data = 2;
}

message GetNextCoercionRecordRequest {
  nidevice_grpc.Session vi = 1;
}

message GetNextCoercionRecordResponse {
  int32 status = 1;
  string coercion_record = 2;
}

message GetNextInterchangeWarningRequest {
  nidevice_grpc.Session vi = 1;
}

message GetNextInterchangeWarningResponse {
  int32 status = 1;
  string interchange_warning = 2;
}

message GetSelfCalLastDateAndTimeRequest {
  nidevice_grpc.Session vi = 1;
}

message GetSelfCalLastDateAndTimeResponse {
  int32 status = 1;
  sint32 year = 2;
  sint32 month = 3;
  sint32 day = 4;
  sint32 hour = 5;
  sint32 minute = 6;
}

message GetSelfCalLastTempRequest {
  nidevice_grpc.Session vi = 1;
}

message GetSelfCalLastTempResponse {
  int32 status = 1;
  double temperature = 2;
}

message ImportAttributeConfigurationBufferRequest {
  nidevice_grpc.Session vi = 1;
  bytes configuration = 2;
}

message ImportAttributeConfigurationBufferResponse {
  int32 status = 1;
}

message ImportAttributeConfigurationFileRequest {
  nidevice_grpc.Session vi = 1;
  string file_path = 2;
}

message ImportAttributeConfigurationFileResponse {
  int32 status = 1;
}

message InitializeWithChannelsRequest {
  string session_name = 1;
  string resource_name = 2;
  string channels = 3;
  bool reset = 4;
  string option_string = 5;
  nidevice_grpc.SessionInitializationBehavior initialization_behavior = 6;
}

message InitializeWithChannelsResponse {
  int32 status = 1;
  nidevice_grpc.Session vi = 2;
  string error_message = 3 [deprecated = true];
  bool new_session_initialized = 4;
}

message InitializeWithIndependentChannelsRequest {
  string session_name = 1;
  string resource_name = 2;
  bool reset = 3;
  string option_string = 4;
  nidevice_grpc.SessionInitializationBehavior initialization_behavior = 5;
}

message InitializeWithIndependentChannelsResponse {
  int32 status = 1;
  nidevice_grpc.Session vi = 2;
  string error_message = 3 [deprecated = true];
  bool new_session_initialized = 4;
}

message InitiateRequest {
  nidevice_grpc.Session vi = 1;
}

message InitiateResponse {
  int32 status = 1;
}

message InitiateWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message InitiateWithChannelsResponse {
  int32 status = 1;
}

message InvalidateAllAttributesRequest {
  nidevice_grpc.Session vi = 1;
}

message InvalidateAllAttributesResponse {
  int32 status = 1;
}

message MeasureRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  oneof measurement_type_enum {
    MeasurementTypes measurement_type = 3;
    sint32 measurement_type_raw = 4;
  }
}

message MeasureResponse {
  int32 status = 1;
  double measurement = 2;
}

message MeasureMultipleRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message MeasureMultipleResponse {
  int32 status = 1;
  repeated double voltage_measurements = 2;
  repeated double current_measurements = 3;
}

message MeasureMultipleLCRRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message MeasureMultipleLCRResponse {
  int32 status = 1;
  repeated NILCRMeasurement measurements = 2;
}

message PerformLCRLoadCompensationRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  repeated NILCRLoadCompensationSpot compensation_spots = 3;
}

message PerformLCRLoadCompensationResponse {
  int32 status = 1;
}

message PerformLCROpenCompensationRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  repeated double additional_frequencies = 3;
}

message PerformLCROpenCompensationResponse {
  int32 status = 1;
}

message PerformLCROpenCustomCableCompensationRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message PerformLCROpenCustomCableCompensationResponse {
  int32 status = 1;
}

message PerformLCRShortCompensationRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  repeated double additional_frequencies = 3;
}

message PerformLCRShortCompensationResponse {
  int32 status = 1;
}

message PerformLCRShortCustomCableCompensationRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message PerformLCRShortCustomCableCompensationResponse {
  int32 status = 1;
}

message QueryInComplianceRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message QueryInComplianceResponse {
  int32 status = 1;
  bool in_compliance = 2;
}

message QueryLatchedOutputCutoffStateRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  oneof output_cutoff_reason_enum {
    OutputCutoffReason output_cutoff_reason = 3;
    sint32 output_cutoff_reason_raw = 4;
  }
}

message QueryLatchedOutputCutoffStateResponse {
  int32 status = 1;
  bool output_cutoff_state = 2;
}

message QueryMaxCurrentLimitRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double voltage_level = 3;
}

message QueryMaxCurrentLimitResponse {
  int32 status = 1;
  double max_current_limit = 2;
}

message QueryMaxVoltageLevelRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double current_limit = 3;
}

message QueryMaxVoltageLevelResponse {
  int32 status = 1;
  double max_voltage_level = 2;
}

message QueryMinCurrentLimitRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double voltage_level = 3;
}

message QueryMinCurrentLimitResponse {
  int32 status = 1;
  double min_current_limit = 2;
}

message QueryOutputStateRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  oneof output_state_enum {
    OutputStates output_state = 3;
    sint32 output_state_raw = 4;
  }
}

message QueryOutputStateResponse {
  int32 status = 1;
  bool in_state = 2;
}

message ReadCurrentTemperatureRequest {
  nidevice_grpc.Session vi = 1;
}

message ReadCurrentTemperatureResponse {
  int32 status = 1;
  double temperature = 2;
}

message ResetRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetResponse {
  int32 status = 1;
}

message ResetDeviceRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetDeviceResponse {
  int32 status = 1;
}

message ResetInterchangeCheckRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetInterchangeCheckResponse {
  int32 status = 1;
}

message ResetWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message ResetWithChannelsResponse {
  int32 status = 1;
}

message ResetWithDefaultsRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetWithDefaultsResponse {
  int32 status = 1;
}

message RevisionQueryRequest {
  nidevice_grpc.Session vi = 1;
}

message RevisionQueryResponse {
  int32 status = 1;
  string instrument_driver_revision = 2;
  string firmware_revision = 3;
}

message SelfTestRequest {
  nidevice_grpc.Session vi = 1;
}

message SelfTestResponse {
  int32 status = 1;
  sint32 self_test_result = 2;
  string self_test_message = 3;
}

message SendSoftwareEdgeTriggerRequest {
  nidevice_grpc.Session vi = 1;
  oneof trigger_enum {
    SendSoftwareEdgeTriggerType trigger = 2;
    sint32 trigger_raw = 3;
  }
}

message SendSoftwareEdgeTriggerResponse {
  int32 status = 1;
}

message SendSoftwareEdgeTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  oneof trigger_enum {
    SendSoftwareEdgeTriggerType trigger = 3;
    sint32 trigger_raw = 4;
  }
}

message SendSoftwareEdgeTriggerWithChannelsResponse {
  int32 status = 1;
}

message SetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDCPowerAttribute attribute_id = 3;
  bool attribute_value = 4;
}

message SetAttributeViBooleanResponse {
  int32 status = 1;
}

message SetAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDCPowerAttribute attribute_id = 3;
  oneof attribute_value_enum {
    NiDCPowerInt32AttributeValues attribute_value = 4;
    sint32 attribute_value_raw = 5;
  }
}

message SetAttributeViInt32Response {
  int32 status = 1;
}

message SetAttributeViInt64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDCPowerAttribute attribute_id = 3;
  int64 attribute_value_raw = 4;
}

message SetAttributeViInt64Response {
  int32 status = 1;
}

message SetAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDCPowerAttribute attribute_id = 3;
  oneof attribute_value_enum {
    NiDCPowerReal64AttributeValues attribute_value = 4;
    double attribute_value_raw = 5;
  }
}

message SetAttributeViReal64Response {
  int32 status = 1;
}

message SetAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDCPowerAttribute attribute_id = 3;
  nidevice_grpc.Session attribute_value = 4;
}

message SetAttributeViSessionResponse {
  int32 status = 1;
}

message SetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDCPowerAttribute attribute_id = 3;
  string attribute_value_raw = 4;
}

message SetAttributeViStringResponse {
  int32 status = 1;
}

message SetSequenceRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  repeated double values = 3;
  repeated double source_delays = 4;
}

message SetSequenceResponse {
  int32 status = 1;
}

message WaitForEventRequest {
  nidevice_grpc.Session vi = 1;
  oneof event_id_enum {
    Event event_id = 2;
    sint32 event_id_raw = 3;
  }
  double timeout = 4;
}

message WaitForEventResponse {
  int32 status = 1;
}

message WaitForEventWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  oneof event_id_enum {
    Event event_id = 3;
    sint32 event_id_raw = 4;
  }
  double timeout = 5;
}

message WaitForEventWithChannelsResponse {
  int32 status = 1;
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidcpower/README.md sha256=0f4491618d784982270eb1af29452a2f4d826d6743e5d147d3b03fd089a2827f bytes=212 -->
## FILE: source/codegen/metadata/nidcpower/README.md

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidcpower/README.md`
- sha256: `0f4491618d784982270eb1af29452a2f4d826d6743e5d147d3b03fd089a2827f`
- bytes: 212

````markdown
# Updating

To update this metadata folder. Find the nidcpower_grpc_device export and copy the contents of its metadata folder here.

# More info

Refer to source/codegen/metadata/Imported_From_Hapigen.md
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidigitalpattern/__init__.py sha256=951f156600c0e02d198b387303dbe8ddd9b655db9cff81388f7f53034b17e17c bytes=730 -->
## FILE: source/codegen/metadata/nidigitalpattern/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidigitalpattern/__init__.py`
- sha256: `951f156600c0e02d198b387303dbe8ddd9b655db9cff81388f7f53034b17e17c`
- bytes: 730

````python
from .functions import functions
from .functions_addon import functions_override_metadata
from .functions_addon import functions_validation_suppressions
from .attributes import attributes
from .attributes_addon import attributes_override_metadata
from .enums import enums
from .enums_addon import enums_override_metadata
from .config import config

metadata = {
    "functions" : functions,
    "functions_validation_suppressions": functions_validation_suppressions,
    "attributes" : attributes,
    "enums" : enums,
    "config" : config
}

metadata['functions'].update(functions_override_metadata)
metadata['attributes'].update(attributes_override_metadata)
metadata['enums'].update(enums_override_metadata)
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidigitalpattern/attributes.py sha256=9dff543765dbee6f2da3b4e05c2ee1c0b968a39fd9d570ae5516e5ef3a5b07bc bytes=17742 -->
## FILE: source/codegen/metadata/nidigitalpattern/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidigitalpattern/attributes.py`
- sha256: `9dff543765dbee6f2da3b4e05c2ee1c0b968a39fd9d570ae5516e5ef3a5b07bc`
- bytes: 17742

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-Digital Pattern Driver API metadata version 23.0.0f112
attributes = {
    1050002: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'RANGE_CHECK',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1050003: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'QUERY_INSTRUMENT_STATUS',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1050004: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'CACHE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1050005: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'SIMULATE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1050006: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'RECORD_COERCIONS',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1050007: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'DRIVER_SETUP',
        'resettable': False,
        'type': 'ViString'
    },
    1050021: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'INTERCHANGE_CHECK',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1050203: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'CHANNEL_COUNT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050302: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SPECIFIC_DRIVER_PREFIX',
        'resettable': False,
        'type': 'ViString'
    },
    1050304: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'resettable': False,
        'type': 'ViString'
    },
    1050305: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'LOGICAL_NAME',
        'resettable': False,
        'type': 'ViString'
    },
    1050327: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'resettable': False,
        'type': 'ViString'
    },
    1050401: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'GROUP_CAPABILITIES',
        'resettable': False,
        'type': 'ViString'
    },
    1050510: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'resettable': False,
        'type': 'ViString'
    },
    1050511: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'INSTRUMENT_MANUFACTURER',
        'resettable': False,
        'type': 'ViString'
    },
    1050512: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'INSTRUMENT_MODEL',
        'resettable': False,
        'type': 'ViString'
    },
    1050513: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'resettable': False,
        'type': 'ViString'
    },
    1050514: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SPECIFIC_DRIVER_DESCRIPTION',
        'resettable': False,
        'type': 'ViString'
    },
    1050515: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050516: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050551: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SPECIFIC_DRIVER_REVISION',
        'resettable': False,
        'type': 'ViString'
    },
    1150001: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SERIAL_NUMBER',
        'resettable': False,
        'type': 'ViString'
    },
    1150004: {
        'codegen_method': 'public',
        'enum': 'SelectedFunction',
        'grpc_type': 'sint32',
        'name': 'SELECTED_FUNCTION',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150006: {
        'codegen_method': 'public',
        'enum': 'TerminationMode',
        'grpc_type': 'sint32',
        'name': 'TERMINATION_MODE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150007: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'VIL',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150008: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'VIH',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150009: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'VOL',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150010: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'VOH',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150011: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'VTERM',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150012: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'ACTIVE_LOAD_IOL',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150013: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'ACTIVE_LOAD_IOH',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150014: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'ACTIVE_LOAD_VCOM',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150015: {
        'codegen_method': 'public',
        'enum': 'PpmuOutputFunction',
        'grpc_type': 'sint32',
        'name': 'PPMU_OUTPUT_FUNCTION',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150016: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PPMU_VOLTAGE_LEVEL',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150017: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PPMU_CURRENT_LIMIT_RANGE',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150019: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PPMU_CURRENT_LEVEL',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150020: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PPMU_CURRENT_LEVEL_RANGE',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150021: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PPMU_VOLTAGE_LIMIT_LOW',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150022: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PPMU_VOLTAGE_LIMIT_HIGH',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150023: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'START_LABEL',
        'resettable': True,
        'type': 'ViString'
    },
    1150029: {
        'codegen_method': 'public',
        'enum': 'TriggerType',
        'grpc_type': 'sint32',
        'name': 'START_TRIGGER_TYPE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150030: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'DIGITAL_EDGE_START_TRIGGER_SOURCE',
        'resettable': True,
        'type': 'ViString'
    },
    1150031: {
        'codegen_method': 'public',
        'enum': 'DigitalEdge',
        'grpc_type': 'sint32',
        'name': 'DIGITAL_EDGE_START_TRIGGER_EDGE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150032: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'EXPORTED_START_TRIGGER_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150033: {
        'codegen_method': 'public',
        'enum': 'TriggerType',
        'grpc_type': 'sint32',
        'name': 'CONDITIONAL_JUMP_TRIGGER_TYPE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150034: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'DIGITAL_EDGE_CONDITIONAL_JUMP_TRIGGER_SOURCE',
        'resettable': True,
        'type': 'ViString'
    },
    1150035: {
        'codegen_method': 'public',
        'enum': 'DigitalEdge',
        'grpc_type': 'sint32',
        'name': 'DIGITAL_EDGE_CONDITIONAL_JUMP_TRIGGER_EDGE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150036: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'EXPORTED_CONDITIONAL_JUMP_TRIGGER_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150037: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PPMU_APERTURE_TIME',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150038: {
        'codegen_method': 'public',
        'enum': 'PpmuApertureTimeUnits',
        'grpc_type': 'sint32',
        'name': 'PPMU_APERTURE_TIME_UNITS',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150039: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'START_TRIGGER_TERMINAL_NAME',
        'resettable': False,
        'type': 'ViString'
    },
    1150040: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'CONDITIONAL_JUMP_TRIGGER_TERMINAL_NAME',
        'resettable': False,
        'type': 'ViString'
    },
    1150041: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'EXPORTED_PATTERN_OPCODE_EVENT_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150042: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'PATTERN_OPCODE_EVENT_TERMINAL_NAME',
        'resettable': False,
        'type': 'ViString'
    },
    1150043: {
        'codegen_method': 'public',
        'enum': 'HistoryRamTriggerType',
        'grpc_type': 'sint32',
        'name': 'HISTORY_RAM_TRIGGER_TYPE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150044: {
        'codegen_method': 'public',
        'grpc_type': 'int64',
        'name': 'CYCLE_NUMBER_HISTORY_RAM_TRIGGER_CYCLE_NUMBER',
        'resettable': True,
        'type': 'ViInt64'
    },
    1150045: {
        'codegen_method': 'public',
        'grpc_type': 'int64',
        'name': 'PATTERN_LABEL_HISTORY_RAM_TRIGGER_CYCLE_OFFSET',
        'resettable': True,
        'type': 'ViInt64'
    },
    1150046: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'PATTERN_LABEL_HISTORY_RAM_TRIGGER_LABEL',
        'resettable': True,
        'type': 'ViString'
    },
    1150047: {
        'codegen_method': 'public',
        'enum': 'HistoryRamCyclesToAcquire',
        'grpc_type': 'sint32',
        'name': 'HISTORY_RAM_CYCLES_TO_ACQUIRE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150048: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'HISTORY_RAM_PRETRIGGER_SAMPLES',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150051: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'TDR_OFFSET',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150052: {
        'codegen_method': 'public',
        'grpc_type': 'int64',
        'name': 'PATTERN_LABEL_HISTORY_RAM_TRIGGER_VECTOR_OFFSET',
        'resettable': True,
        'type': 'ViInt64'
    },
    1150054: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PPMU_CURRENT_LIMIT',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150055: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'PPMU_CURRENT_LIMIT_SUPPORTED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150059: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SEQUENCER_FLAG_TERMINAL_NAME',
        'resettable': False,
        'type': 'ViString'
    },
    1150060: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'MASK_COMPARE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150062: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'HALT_ON_KEEP_ALIVE_OPCODE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150063: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'IS_KEEP_ALIVE_ACTIVE',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150064: {
        'codegen_method': 'public',
        'enum': 'PpmuCurrentLimitBehavior',
        'grpc_type': 'sint32',
        'name': 'PPMU_CURRENT_LIMIT_BEHAVIOR',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150069: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'FREQUENCY_COUNTER_MEASUREMENT_TIME',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150071: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'TIMING_ABSOLUTE_DELAY_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150072: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'TIMING_ABSOLUTE_DELAY',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150073: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'CLOCK_GENERATOR_FREQUENCY',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150074: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'CLOCK_GENERATOR_IS_RUNNING',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150076: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'PPMU_ALLOW_EXTENDED_VOLTAGE_RANGE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150077: {
        'codegen_method': 'public',
        'enum': 'HistoryRamMaxSamplesToAcquirePerSite',
        'grpc_type': 'sint32',
        'name': 'HISTORY_RAM_MAX_SAMPLES_TO_ACQUIRE_PER_SITE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150078: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'HISTORY_RAM_NUMBER_OF_SAMPLES_IS_FINITE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150079: {
        'codegen_method': 'public',
        'grpc_type': 'int64',
        'name': 'HISTORY_RAM_BUFFER_SIZE_PER_SITE',
        'resettable': True,
        'type': 'ViInt64'
    },
    1150081: {
        'codegen_method': 'public',
        'enum': 'TdrEndpointTermination',
        'grpc_type': 'sint32',
        'name': 'TDR_ENDPOINT_TERMINATION',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150084: {
        'codegen_method': 'public',
        'enum': 'FrequencyMeasurementMode',
        'grpc_type': 'sint32',
        'name': 'FREQUENCY_COUNTER_MEASUREMENT_MODE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150085: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'FREQUENCY_COUNTER_HYSTERESIS_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150086: {
        'codegen_method': 'public',
        'enum': 'TriggerType',
        'grpc_type': 'sint32',
        'name': 'RIO_TRIGGER_TYPE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150087: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'DIGITAL_EDGE_RIO_TRIGGER_SOURCE',
        'resettable': True,
        'type': 'ViString'
    },
    1150088: {
        'codegen_method': 'public',
        'enum': 'DigitalEdge',
        'grpc_type': 'sint32',
        'name': 'DIGITAL_EDGE_RIO_TRIGGER_EDGE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150089: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'RIO_TRIGGER_TERMINAL_NAME',
        'resettable': False,
        'type': 'ViString'
    },
    1150090: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'EXPORTED_RIO_EVENT_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150091: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'RIO_EVENT_TERMINAL_NAME',
        'resettable': False,
        'type': 'ViString'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidigitalpattern/attributes_addon.py sha256=cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f bytes=207 -->
## FILE: source/codegen/metadata/nidigitalpattern/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidigitalpattern/attributes_addon.py`
- sha256: `cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f`
- bytes: 207

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidigitalpattern/config.py sha256=d9b7c4521758f17eaf605b1d83cbcc69e07ea1199faba2748db6d193ab708855 bytes=1241 -->
## FILE: source/codegen/metadata/nidigitalpattern/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidigitalpattern/config.py`
- sha256: `d9b7c4521758f17eaf605b1d83cbcc69e07ea1199faba2748db6d193ab708855`
- bytes: 1241

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-Digital Pattern Driver API metadata version 23.0.0f112
config = {
    'additional_headers': {
        'custom/ivi_errors.h': [
            'service.cpp'
        ]
    },
    'api_version': '23.0.0f112',
    'c_function_prefix': 'niDigital_',
    'c_header': 'niDigital.h',
    'close_function': 'Close',
    'csharp_namespace': 'NationalInstruments.Grpc.Digital',
    'custom_types': [
    ],
    'driver_name': 'NI-Digital Pattern Driver',
    'java_package': 'com.ni.grpc.nidigital',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nidigital',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niDigital_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niDigital_64.dll',
                'type': 'cdll'
            }
        }
    },
    'linux_rt_support': False,
    'module_name': 'nidigitalpattern',
    'namespace_component': 'nidigitalpattern',
    'service_class_prefix': 'NiDigital',
    'session_handle_parameter_name': 'vi',
    'status_ok': 'status >= 0'
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidigitalpattern/config_addon.py sha256=2b0bf1d77be054a9e7a301b3e7ce0ff0a7a1db34ed78f5eb34cbd370c46e3df3 bytes=427 -->
## FILE: source/codegen/metadata/nidigitalpattern/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidigitalpattern/config_addon.py`
- sha256: `2b0bf1d77be054a9e7a301b3e7ce0ff0a7a1db34ed78f5eb34cbd370c46e3df3`
- bytes: 427

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.0.1.dev0',
    'latest_runtime_version_tested_against': '20.6.0',
    'custom_types': [
        {
            'ctypes_type': '',
            'file_name': 'history_ram_cycle_information',
            'python_name': 'HistoryRAMCycleInformation'
        }
    ],
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidigitalpattern/enums.py sha256=8ec0649d421e6d53dfef6d530a49432dd0ba24ea4505b62e1ee9b90262574a3c bytes=13722 -->
## FILE: source/codegen/metadata/nidigitalpattern/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidigitalpattern/enums.py`
- sha256: `8ec0649d421e6d53dfef6d530a49432dd0ba24ea4505b62e1ee9b90262574a3c`
- bytes: 13722

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-Digital Pattern Driver API metadata version 23.0.0f112
enums = {
    'BitOrder': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDIGITAL_VAL_MSB_FIRST',
                'value': 2500
            },
            {
                'name': 'NIDIGITAL_VAL_LSB_FIRST',
                'value': 2501
            }
        ]
    },
    'DigitalEdge': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDIGITAL_VAL_RISING_EDGE',
                'value': 1800
            },
            {
                'name': 'NIDIGITAL_VAL_FALLING_EDGE',
                'value': 1801
            }
        ]
    },
    'DriveFormat': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDIGITAL_VAL_NR',
                'value': 1500
            },
            {
                'name': 'NIDIGITAL_VAL_RL',
                'value': 1501
            },
            {
                'name': 'NIDIGITAL_VAL_RH',
                'value': 1502
            },
            {
                'name': 'NIDIGITAL_VAL_SBC',
                'value': 1503
            }
        ]
    },
    'ExportSignal': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDIGITAL_VAL_START_TRIGGER',
                'value': 2000
            },
            {
                'name': 'NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER',
                'value': 2001
            },
            {
                'name': 'NIDIGITAL_VAL_PATTERN_OPCODE_EVENT',
                'value': 2002
            },
            {
                'name': 'NIDIGITAL_VAL_REF_CLOCK',
                'value': 2003
            },
            {
                'name': 'NIDIGITAL_VAL_RIO_EVENT',
                'value': 2004
            }
        ]
    },
    'FrequencyMeasurementMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDIGITAL_VAL_BANKED',
                'value': 3700
            },
            {
                'name': 'NIDIGITAL_VAL_PARALLEL',
                'value': 3701
            }
        ]
    },
    'HistoryRamCyclesToAcquire': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDIGITAL_VAL_FAILED_CYCLES',
                'value': 2303
            },
            {
                'name': 'NIDIGITAL_VAL_ALL_CYCLES',
                'value': 2304
            }
        ]
    },
    'HistoryRamMaxSamplesToAcquirePerSite': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDIGITAL_VAL_ACQUIRE_ALL_SAMPLES',
                'value': -1
            }
        ]
    },
    'HistoryRamTriggerType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDIGITAL_VAL_FIRST_FAILURE',
                'value': 2200
            },
            {
                'name': 'NIDIGITAL_VAL_CYCLE_NUMBER',
                'value': 2201
            },
            {
                'name': 'NIDIGITAL_VAL_PATTERN_LABEL',
                'value': 2202
            }
        ]
    },
    'NiDigitalInt32AttributeValues': {
        'enum-value-prefix': 'NIDIGITAL_INT32',
        'generate-mappings': False,
        'values': [
            {
                'name': 'DIGITAL_EDGE_VAL_RISING_EDGE',
                'value': 1800
            },
            {
                'name': 'DIGITAL_EDGE_VAL_FALLING_EDGE',
                'value': 1801
            },
            {
                'name': 'FREQUENCY_MEASUREMENT_MODE_VAL_BANKED',
                'value': 3700
            },
            {
                'name': 'FREQUENCY_MEASUREMENT_MODE_VAL_PARALLEL',
                'value': 3701
            },
            {
                'name': 'HISTORY_RAM_CYCLES_TO_ACQUIRE_VAL_FAILED_CYCLES',
                'value': 2303
            },
            {
                'name': 'HISTORY_RAM_CYCLES_TO_ACQUIRE_VAL_ALL_CYCLES',
                'value': 2304
            },
            {
                'name': 'HISTORY_RAM_MAX_SAMPLES_TO_ACQUIRE_PER_SITE_VAL_ACQUIRE_ALL_SAMPLES',
                'value': -1
            },
            {
                'name': 'HISTORY_RAM_TRIGGER_TYPE_VAL_FIRST_FAILURE',
                'value': 2200
            },
            {
                'name': 'HISTORY_RAM_TRIGGER_TYPE_VAL_CYCLE_NUMBER',
                'value': 2201
            },
            {
                'name': 'HISTORY_RAM_TRIGGER_TYPE_VAL_PATTERN_LABEL',
                'value': 2202
            },
            {
                'name': 'PPMU_APERTURE_TIME_UNITS_VAL_SECONDS',
                'value': 2100
            },
            {
                'name': 'PPMU_CURRENT_LIMIT_BEHAVIOR_VAL_CURRENT_REGULATE',
                'value': 3100
            },
            {
                'name': 'PPMU_OUTPUT_FUNCTION_VAL_DC_VOLTAGE',
                'value': 1300
            },
            {
                'name': 'PPMU_OUTPUT_FUNCTION_VAL_DC_CURRENT',
                'value': 1301
            },
            {
                'name': 'SELECTED_FUNCTION_VAL_DIGITAL',
                'value': 1100
            },
            {
                'name': 'SELECTED_FUNCTION_VAL_PPMU',
                'value': 1101
            },
            {
                'name': 'SELECTED_FUNCTION_VAL_OFF',
                'value': 1102
            },
            {
                'name': 'SELECTED_FUNCTION_VAL_DISCONNECT',
                'value': 1103
            },
            {
                'name': 'SELECTED_FUNCTION_VAL_RIO',
                'value': 1104
            },
            {
                'name': 'TDR_ENDPOINT_TERMINATION_VAL_TDR_TO_OPEN',
                'value': 3600
            },
            {
                'name': 'TDR_ENDPOINT_TERMINATION_VAL_TDR_TO_SHORT_TO_GROUND',
                'value': 3601
            },
            {
                'name': 'TERMINATION_MODE_VAL_ACTIVE_LOAD',
                'value': 1200
            },
            {
                'name': 'TERMINATION_MODE_VAL_VTERM',
                'value': 1201
            },
            {
                'name': 'TERMINATION_MODE_VAL_HIGH_Z',
                'value': 1202
            },
            {
                'name': 'TRIGGER_TYPE_VAL_NONE',
                'value': 1700
            },
            {
                'name': 'TRIGGER_TYPE_VAL_DIGITAL_EDGE',
                'value': 1701
            },
            {
                'name': 'TRIGGER_TYPE_VAL_SOFTWARE',
                'value': 1702
            }
        ]
    },
    'PinState': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDIGITAL_VAL_0',
                'value': 0
            },
            {
                'name': 'NIDIGITAL_VAL_1',
                'value': 1
            },
            {
                'name': 'NIDIGITAL_VAL_L',
                'value': 3
            },
            {
                'name': 'NIDIGITAL_VAL_H',
                'value': 4
            },
            {
                'name': 'NIDIGITAL_VAL_X',
                'value': 5
            },
            {
                'name': 'NIDIGITAL_VAL_M',
                'value': 6
            },
            {
                'name': 'NIDIGITAL_VAL_V',
                'value': 7
            },
            {
                'name': 'NIDIGITAL_VAL_D',
                'value': 8
            },
            {
                'name': 'NIDIGITAL_VAL_E',
                'value': 9
            },
            {
                'name': 'NIDIGITAL_VAL_NOT_A_PIN_STATE',
                'value': 254
            },
            {
                'name': 'NIDIGITAL_VAL_PIN_STATE_NOT_ACQUIRED',
                'value': 255
            }
        ]
    },
    'PpmuApertureTimeUnits': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDIGITAL_VAL_SECONDS',
                'value': 2100
            }
        ]
    },
    'PpmuCurrentLimitBehavior': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDIGITAL_VAL_CURRENT_REGULATE',
                'value': 3100
            }
        ]
    },
    'PpmuMeasurementType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDIGITAL_VAL_MEASURE_CURRENT',
                'value': 2400
            },
            {
                'name': 'NIDIGITAL_VAL_MEASURE_VOLTAGE',
                'value': 2401
            }
        ]
    },
    'PpmuOutputFunction': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDIGITAL_VAL_DC_VOLTAGE',
                'value': 1300
            },
            {
                'name': 'NIDIGITAL_VAL_DC_CURRENT',
                'value': 1301
            }
        ]
    },
    'SelectedFunction': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDIGITAL_VAL_DIGITAL',
                'value': 1100
            },
            {
                'name': 'NIDIGITAL_VAL_PPMU',
                'value': 1101
            },
            {
                'name': 'NIDIGITAL_VAL_OFF',
                'value': 1102
            },
            {
                'name': 'NIDIGITAL_VAL_DISCONNECT',
                'value': 1103
            },
            {
                'name': 'NIDIGITAL_VAL_RIO',
                'value': 1104
            }
        ]
    },
    'SiteResultType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDIGITAL_VAL_PASS_FAIL',
                'value': 3300
            },
            {
                'name': 'NIDIGITAL_VAL_CAPTURE_WAVEFORM',
                'value': 3301
            }
        ]
    },
    'SoftwareTrigger': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDIGITAL_VAL_START_TRIGGER',
                'value': 2000
            },
            {
                'name': 'NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER',
                'value': 2001
            }
        ]
    },
    'SourceDataMapping': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDIGITAL_VAL_BROADCAST',
                'value': 2600
            },
            {
                'name': 'NIDIGITAL_VAL_SITE_UNIQUE',
                'value': 2601
            }
        ]
    },
    'TdrEndpointTermination': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDIGITAL_VAL_TDR_TO_OPEN',
                'value': 3600
            },
            {
                'name': 'NIDIGITAL_VAL_TDR_TO_SHORT_TO_GROUND',
                'value': 3601
            }
        ]
    },
    'TerminationMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDIGITAL_VAL_ACTIVE_LOAD',
                'value': 1200
            },
            {
                'name': 'NIDIGITAL_VAL_VTERM',
                'value': 1201
            },
            {
                'name': 'NIDIGITAL_VAL_HIGH_Z',
                'value': 1202
            }
        ]
    },
    'TimeSetEdgeType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDIGITAL_VAL_DRIVE_ON',
                'value': 2800
            },
            {
                'name': 'NIDIGITAL_VAL_DRIVE_DATA',
                'value': 2801
            },
            {
                'name': 'NIDIGITAL_VAL_DRIVE_RETURN',
                'value': 2802
            },
            {
                'name': 'NIDIGITAL_VAL_DRIVE_OFF',
                'value': 2803
            },
            {
                'name': 'NIDIGITAL_VAL_COMPARE_STROBE',
                'value': 2804
            },
            {
                'name': 'NIDIGITAL_VAL_DRIVE_DATA2',
                'value': 2805
            },
            {
                'name': 'NIDIGITAL_VAL_DRIVE_RETURN2',
                'value': 2806
            },
            {
                'name': 'NIDIGITAL_VAL_COMPARE_STROBE2',
                'value': 2807
            }
        ]
    },
    'TriggerType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDIGITAL_VAL_NONE',
                'value': 1700
            },
            {
                'name': 'NIDIGITAL_VAL_DIGITAL_EDGE',
                'value': 1701
            },
            {
                'name': 'NIDIGITAL_VAL_SOFTWARE',
                'value': 1702
            }
        ]
    },
    'WriteStaticPinState': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDIGITAL_VAL_0',
                'value': 0
            },
            {
                'name': 'NIDIGITAL_VAL_1',
                'value': 1
            },
            {
                'name': 'NIDIGITAL_VAL_X',
                'value': 5
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidigitalpattern/enums_addon.py sha256=ac06c73354b9c04f0145a994373cc801d22779eab924afbba804b47e50fca14e bytes=190 -->
## FILE: source/codegen/metadata/nidigitalpattern/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidigitalpattern/enums_addon.py`
- sha256: `ac06c73354b9c04f0145a994373cc801d22779eab924afbba804b47e50fca14e`
- bytes: 190

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidigitalpattern/functions.py sha256=87ecf823cf7103632759827e7512cba9325fd147378c4b0ecc842ddfc09a4cfd bytes=139711 -->
## FILE: source/codegen/metadata/nidigitalpattern/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidigitalpattern/functions.py`
- sha256: `87ecf823cf7103632759827e7512cba9325fd147378c4b0ecc842ddfc09a4cfd`
- bytes: 139711

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-Digital Pattern Driver API metadata version 23.0.0f112
functions = {
    'Abort': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'AbortKeepAlive': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ApplyLevelsAndTiming': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'siteList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'siteList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'levelsSheet',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'levelsSheet',
                'type': 'ViConstString'
            },
            {
                'cppName': 'timingSheet',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'timingSheet',
                'type': 'ViConstString'
            },
            {
                'cppName': 'initialStateHighPins',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'initialStateHighPins',
                'type': 'ViConstString'
            },
            {
                'cppName': 'initialStateLowPins',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'initialStateLowPins',
                'type': 'ViConstString'
            },
            {
                'cppName': 'initialStateTristatePins',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'initialStateTristatePins',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ApplyTDROffsets': {
        'cname': 'niDigital_ApplyTDROffsets',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'numOffsets',
                'determine_size_from': [
                    'offsets'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'numOffsets',
                'type': 'ViInt32'
            },
            {
                'cppName': 'offsets',
                'direction': 'in',
                'grpc_type': 'repeated double',
                'name': 'offsets',
                'size': {
                    'mechanism': 'len',
                    'value': 'numOffsets'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'BurstPattern': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'siteList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'siteList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'startLabel',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'startLabel',
                'type': 'ViConstString'
            },
            {
                'cppName': 'selectDigitalFunction',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'selectDigitalFunction',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'waitUntilDone',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'waitUntilDone',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'timeout',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'timeout',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'BurstPatternSynchronized': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'sessionCount',
                'direction': 'in',
                'grpc_type': 'uint32',
                'is_size_param': True,
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'cppName': 'sessions',
                'direction': 'in',
                'grpc_type': 'repeated nidevice_grpc.Session',
                'name': 'sessions',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]'
            },
            {
                'cppName': 'siteList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'siteList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'startLabel',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'startLabel',
                'type': 'ViConstString'
            },
            {
                'cppName': 'selectDigitalFunction',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'selectDigitalFunction',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'waitUntilDone',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'waitUntilDone',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'timeout',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'timeout',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearError': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClockGeneratorAbort': {
        'cname': 'niDigital_ClockGenerator_Abort',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClockGeneratorGenerateClock': {
        'cname': 'niDigital_ClockGenerator_GenerateClock',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'frequency',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'frequency',
                'type': 'ViReal64'
            },
            {
                'cppName': 'selectDigitalFunction',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'selectDigitalFunction',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClockGeneratorInitiate': {
        'cname': 'niDigital_ClockGenerator_Initiate',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'Close': {
        'cname': 'niDigital_close',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'Commit': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureActiveLoadLevels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'iol',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'iol',
                'type': 'ViReal64'
            },
            {
                'cppName': 'ioh',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'ioh',
                'type': 'ViReal64'
            },
            {
                'cppName': 'vcom',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'vcom',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureCycleNumberHistoryRAMTrigger': {
        'cname': 'niDigital_ConfigureCycleNumberHistoryRAMTrigger',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'cycleNumber',
                'direction': 'in',
                'grpc_type': 'int64',
                'name': 'cycleNumber',
                'type': 'ViInt64'
            },
            {
                'cppName': 'pretriggerSamples',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'pretriggerSamples',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeConditionalJumpTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'triggerIdentifier',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'triggerIdentifier',
                'type': 'ViConstString'
            },
            {
                'cppName': 'source',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'source',
                'type': 'ViConstString'
            },
            {
                'cppName': 'edge',
                'direction': 'in',
                'enum': 'DigitalEdge',
                'grpc_type': 'sint32',
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeStartTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'source',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'source',
                'type': 'ViConstString'
            },
            {
                'cppName': 'edge',
                'direction': 'in',
                'enum': 'DigitalEdge',
                'grpc_type': 'sint32',
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureFirstFailureHistoryRAMTrigger': {
        'cname': 'niDigital_ConfigureFirstFailureHistoryRAMTrigger',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'pretriggerSamples',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'pretriggerSamples',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureHistoryRAMCyclesToAcquire': {
        'cname': 'niDigital_ConfigureHistoryRAMCyclesToAcquire',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'cyclesToAcquire',
                'direction': 'in',
                'enum': 'HistoryRamCyclesToAcquire',
                'grpc_type': 'sint32',
                'name': 'cyclesToAcquire',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePatternBurstSites': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'siteList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'siteList',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePatternLabelHistoryRAMTrigger': {
        'cname': 'niDigital_ConfigurePatternLabelHistoryRAMTrigger',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'label',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'label',
                'type': 'ViConstString'
            },
            {
                'cppName': 'vectorOffset',
                'direction': 'in',
                'grpc_type': 'int64',
                'name': 'vectorOffset',
                'type': 'ViInt64'
            },
            {
                'cppName': 'cycleOffset',
                'direction': 'in',
                'grpc_type': 'int64',
                'name': 'cycleOffset',
                'type': 'ViInt64'
            },
            {
                'cppName': 'pretriggerSamples',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'pretriggerSamples',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgeConditionalJumpTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'triggerIdentifier',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'triggerIdentifier',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgeStartTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureStartLabel': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'label',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'label',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTerminationMode': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'mode',
                'direction': 'in',
                'enum': 'TerminationMode',
                'grpc_type': 'sint32',
                'name': 'mode',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTimeSetCompareEdgesStrobe': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'pinList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'pinList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'timeSet',
                'direction': 'in',
                'grpc_name': 'time_set_name',
                'grpc_type': 'string',
                'name': 'timeSet',
                'type': 'ViConstString'
            },
            {
                'cppName': 'strobeEdge',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'strobeEdge',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTimeSetCompareEdgesStrobe2x': {
        'cname': 'niDigital_ConfigureTimeSetCompareEdgesStrobe2x',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'pinList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'pinList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'timeSet',
                'direction': 'in',
                'grpc_name': 'time_set_name',
                'grpc_type': 'string',
                'name': 'timeSet',
                'type': 'ViConstString'
            },
            {
                'cppName': 'strobeEdge',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'strobeEdge',
                'type': 'ViReal64'
            },
            {
                'cppName': 'strobe2Edge',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'strobe2Edge',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTimeSetDriveEdges': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'pinList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'pinList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'timeSet',
                'direction': 'in',
                'grpc_name': 'time_set_name',
                'grpc_type': 'string',
                'name': 'timeSet',
                'type': 'ViConstString'
            },
            {
                'cppName': 'format',
                'direction': 'in',
                'enum': 'DriveFormat',
                'grpc_type': 'sint32',
                'name': 'format',
                'type': 'ViInt32'
            },
            {
                'cppName': 'driveOnEdge',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'driveOnEdge',
                'type': 'ViReal64'
            },
            {
                'cppName': 'driveDataEdge',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'driveDataEdge',
                'type': 'ViReal64'
            },
            {
                'cppName': 'driveReturnEdge',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'driveReturnEdge',
                'type': 'ViReal64'
            },
            {
                'cppName': 'driveOffEdge',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'driveOffEdge',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTimeSetDriveEdges2x': {
        'cname': 'niDigital_ConfigureTimeSetDriveEdges2x',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'pinList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'pinList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'timeSet',
                'direction': 'in',
                'grpc_name': 'time_set_name',
                'grpc_type': 'string',
                'name': 'timeSet',
                'type': 'ViConstString'
            },
            {
                'cppName': 'format',
                'direction': 'in',
                'enum': 'DriveFormat',
                'grpc_type': 'sint32',
                'name': 'format',
                'type': 'ViInt32'
            },
            {
                'cppName': 'driveOnEdge',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'driveOnEdge',
                'type': 'ViReal64'
            },
            {
                'cppName': 'driveDataEdge',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'driveDataEdge',
                'type': 'ViReal64'
            },
            {
                'cppName': 'driveReturnEdge',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'driveReturnEdge',
                'type': 'ViReal64'
            },
            {
                'cppName': 'driveOffEdge',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'driveOffEdge',
                'type': 'ViReal64'
            },
            {
                'cppName': 'driveData2Edge',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'driveData2Edge',
                'type': 'ViReal64'
            },
            {
                'cppName': 'driveReturn2Edge',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'driveReturn2Edge',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTimeSetDriveFormat': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'pinList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'pinList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'timeSet',
                'direction': 'in',
                'grpc_name': 'time_set_name',
                'grpc_type': 'string',
                'name': 'timeSet',
                'type': 'ViConstString'
            },
            {
                'cppName': 'driveFormat',
                'direction': 'in',
                'enum': 'DriveFormat',
                'grpc_type': 'sint32',
                'name': 'driveFormat',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTimeSetEdge': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'pinList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'pinList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'timeSet',
                'direction': 'in',
                'grpc_name': 'time_set_name',
                'grpc_type': 'string',
                'name': 'timeSet',
                'type': 'ViConstString'
            },
            {
                'cppName': 'edge',
                'direction': 'in',
                'enum': 'TimeSetEdgeType',
                'grpc_type': 'sint32',
                'name': 'edge',
                'type': 'ViInt32'
            },
            {
                'cppName': 'time',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'time',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTimeSetEdgeMultiplier': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'pinList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'pinList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'timeSet',
                'direction': 'in',
                'grpc_name': 'time_set_name',
                'grpc_type': 'string',
                'name': 'timeSet',
                'type': 'ViConstString'
            },
            {
                'cppName': 'edgeMultiplier',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'edgeMultiplier',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTimeSetPeriod': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'timeSet',
                'direction': 'in',
                'grpc_name': 'time_set_name',
                'grpc_type': 'string',
                'name': 'timeSet',
                'type': 'ViConstString'
            },
            {
                'cppName': 'period',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'period',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureVoltageLevels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'vil',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'vil',
                'type': 'ViReal64'
            },
            {
                'cppName': 'vih',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'vih',
                'type': 'ViReal64'
            },
            {
                'cppName': 'vol',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'vol',
                'type': 'ViReal64'
            },
            {
                'cppName': 'voh',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'voh',
                'type': 'ViReal64'
            },
            {
                'cppName': 'vterm',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'vterm',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateCaptureWaveformFromFileDigicapture': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'waveformName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'waveformFilePath',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'waveformFilePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateCaptureWaveformParallel': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'pinList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'pinList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'waveformName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'waveformName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateCaptureWaveformSerial': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'pinList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'pinList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'waveformName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'sampleWidth',
                'direction': 'in',
                'grpc_type': 'uint32',
                'name': 'sampleWidth',
                'type': 'ViUInt32'
            },
            {
                'cppName': 'bitOrder',
                'direction': 'in',
                'enum': 'BitOrder',
                'grpc_type': 'sint32',
                'name': 'bitOrder',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateChannelMap': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'numSites',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'numSites',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreatePinGroup': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'pinGroupName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'pinGroupName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'pinList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'pinList',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreatePinMap': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'dutPinList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'dutPinList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'systemPinList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'systemPinList',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateSourceWaveformFromFileTDMS': {
        'cname': 'niDigital_CreateSourceWaveformFromFileTDMS',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'waveformName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'waveformFilePath',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'waveformFilePath',
                'type': 'ViConstString'
            },
            {
                'cppName': 'writeWaveformData',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'writeWaveformData',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateSourceWaveformParallel': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'pinList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'pinList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'waveformName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'dataMapping',
                'direction': 'in',
                'enum': 'SourceDataMapping',
                'grpc_type': 'sint32',
                'name': 'dataMapping',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateSourceWaveformSerial': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'pinList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'pinList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'waveformName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'dataMapping',
                'direction': 'in',
                'enum': 'SourceDataMapping',
                'grpc_type': 'sint32',
                'name': 'dataMapping',
                'type': 'ViInt32'
            },
            {
                'cppName': 'sampleWidth',
                'direction': 'in',
                'grpc_type': 'uint32',
                'name': 'sampleWidth',
                'type': 'ViUInt32'
            },
            {
                'cppName': 'bitOrder',
                'direction': 'in',
                'enum': 'BitOrder',
                'grpc_type': 'sint32',
                'name': 'bitOrder',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateTimeSet': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'name',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'name',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DeleteAllTimeSets': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableConditionalJumpTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'triggerIdentifier',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'triggerIdentifier',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableSites': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'siteList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'siteList',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableStartTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'EnableMatchFailCombination': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'sessionCount',
                'direction': 'in',
                'grpc_type': 'uint32',
                'is_size_param': True,
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'cppName': 'sessions',
                'direction': 'in',
                'grpc_type': 'repeated nidevice_grpc.Session',
                'name': 'sessions',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]'
            },
            {
                'cppName': 'syncSession',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'syncSession',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'EnableSites': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'siteList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'siteList',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'EndChannelMap': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ErrorMessage': {
        'cname': 'niDigital_error_message',
        'codegen_method': 'public',
        'is_error_handling': True,
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorCode',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'cppName': 'errorMessage',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportSignal': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'signal',
                'direction': 'in',
                'enum': 'ExportSignal',
                'grpc_type': 'sint32',
                'name': 'signal',
                'type': 'ViInt32'
            },
            {
                'cppName': 'signalIdentifier',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'signalIdentifier',
                'type': 'ViConstString'
            },
            {
                'cppName': 'outputTerminal',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'outputTerminal',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchCaptureWaveformU32': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'siteList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'siteList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'waveformName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'samplesToRead',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'samplesToRead',
                'type': 'ViInt32'
            },
            {
                'cppName': 'timeout',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'cppName': 'dataBufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'dataBufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'data',
                'direction': 'out',
                'grpc_type': 'repeated uint32',
                'name': 'data',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dataBufferSize',
                    'value_twist': 'actualNumWaveforms'
                },
                'type': 'ViUInt32[]'
            },
            {
                'cppName': 'actualNumWaveforms',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualNumWaveforms',
                'type': 'ViInt32'
            },
            {
                'cppName': 'actualSamplesPerWaveform',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualSamplesPerWaveform',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchHistoryRAMCycleInformation': {
        'cname': 'niDigital_FetchHistoryRAMCycleInformation',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'site',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'site',
                'type': 'ViConstString'
            },
            {
                'cppName': 'sampleIndex',
                'direction': 'in',
                'grpc_type': 'int64',
                'name': 'sampleIndex',
                'type': 'ViInt64'
            },
            {
                'cppName': 'patternIndex',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'patternIndex',
                'type': 'ViInt32'
            },
            {
                'cppName': 'timeSetIndex',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'timeSetIndex',
                'type': 'ViInt32'
            },
            {
                'cppName': 'vectorNumber',
                'direction': 'out',
                'grpc_type': 'int64',
                'name': 'vectorNumber',
                'type': 'ViInt64'
            },
            {
                'cppName': 'cycleNumber',
                'direction': 'out',
                'grpc_type': 'int64',
                'name': 'cycleNumber',
                'type': 'ViInt64'
            },
            {
                'cppName': 'numDutCycles',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'numDutCycles',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchHistoryRAMCyclePinData': {
        'cname': 'niDigital_FetchHistoryRAMCyclePinData',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'site',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'site',
                'type': 'ViConstString'
            },
            {
                'cppName': 'pinList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'pinList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'sampleIndex',
                'direction': 'in',
                'grpc_type': 'int64',
                'name': 'sampleIndex',
                'type': 'ViInt64'
            },
            {
                'cppName': 'dutCycleIndex',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'dutCycleIndex',
                'type': 'ViInt32'
            },
            {
                'cppName': 'pinDataBufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'pinDataBufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'expectedPinStates',
                'direction': 'out',
                'enum': 'PinState',
                'grpc_type': 'bytes',
                'name': 'expectedPinStates',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'pinDataBufferSize',
                    'value_twist': 'actualNumPinData'
                },
                'type': 'ViUInt8[]'
            },
            {
                'cppName': 'actualPinStates',
                'direction': 'out',
                'enum': 'PinState',
                'grpc_type': 'bytes',
                'name': 'actualPinStates',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'pinDataBufferSize',
                    'value_twist': 'actualNumPinData'
                },
                'type': 'ViUInt8[]'
            },
            {
                'cppName': 'perPinPassFail',
                'direction': 'out',
                'grpc_type': 'repeated bool',
                'name': 'perPinPassFail',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'pinDataBufferSize',
                    'value_twist': 'actualNumPinData'
                },
                'type': 'ViBoolean[]'
            },
            {
                'cppName': 'actualNumPinData',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualNumPinData',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchHistoryRAMScanCycleNumber': {
        'cname': 'niDigital_FetchHistoryRAMScanCycleNumber',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'site',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'site',
                'type': 'ViConstString'
            },
            {
                'cppName': 'sampleIndex',
                'direction': 'in',
                'grpc_type': 'int64',
                'name': 'sampleIndex',
                'type': 'ViInt64'
            },
            {
                'cppName': 'scanCycleNumber',
                'direction': 'out',
                'grpc_type': 'int64',
                'name': 'scanCycleNumber',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'FrequencyCounterConfigureMeasurementMode': {
        'cname': 'niDigital_FrequencyCounter_ConfigureMeasurementMode',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'measurementmode',
                'direction': 'in',
                'enum': 'FrequencyMeasurementMode',
                'grpc_name': 'measurement_mode',
                'grpc_type': 'sint32',
                'name': 'measurementmode',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'FrequencyCounterConfigureMeasurementTime': {
        'cname': 'niDigital_FrequencyCounter_ConfigureMeasurementTime',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'measurementTime',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'measurementTime',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'FrequencyCounterMeasureFrequency': {
        'cname': 'niDigital_FrequencyCounter_MeasureFrequency',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'frequenciesBufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'frequenciesBufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'frequencies',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'frequencies',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'frequenciesBufferSize',
                    'value_twist': 'actualNumFrequencies'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'actualNumFrequencies',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualNumFrequencies',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attribute',
                'direction': 'in',
                'grpc_type': 'NiDigitalAttribute',
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'value',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt32': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attribute',
                'direction': 'in',
                'grpc_type': 'NiDigitalAttribute',
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'value',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attribute',
                'direction': 'in',
                'grpc_type': 'NiDigitalAttribute',
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'out',
                'grpc_type': 'int64',
                'name': 'value',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViReal64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attribute',
                'direction': 'in',
                'grpc_type': 'NiDigitalAttribute',
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'value',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViSession': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_name': 'channel_list',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attribute',
                'direction': 'in',
                'grpc_type': 'NiDigitalAttribute',
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'value',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attribute',
                'direction': 'in',
                'grpc_type': 'NiDigitalAttribute',
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'value',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetChannelName': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'index',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'index',
                'type': 'ViInt32'
            },
            {
                'cppName': 'nameBufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'nameBufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'name',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'name',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'nameBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetChannelNameFromString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'index',
                'direction': 'in',
                'grpc_name': 'indices',
                'grpc_type': 'string',
                'name': 'index',
                'type': 'ViConstString'
            },
            {
                'cppName': 'nameBufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'nameBufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'name',
                'direction': 'out',
                'grpc_name': 'names',
                'grpc_type': 'string',
                'name': 'name',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'nameBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetError': {
        'codegen_method': 'public',
        'is_error_handling': True,
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorCode',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'cppName': 'errorDescriptionBufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'errorDescriptionBufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'errorDescription',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'errorDescription',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'errorDescriptionBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetFailCount': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'failureCount',
                'direction': 'out',
                'grpc_type': 'repeated int64',
                'name': 'failureCount',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualNumRead'
                },
                'type': 'ViInt64[]'
            },
            {
                'cppName': 'actualNumRead',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualNumRead',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetHistoryRAMSampleCount': {
        'cname': 'niDigital_GetHistoryRAMSampleCount',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'site',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'site',
                'type': 'ViConstString'
            },
            {
                'cppName': 'sampleCount',
                'direction': 'out',
                'grpc_type': 'int64',
                'name': 'sampleCount',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetPatternName': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'patternIndex',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'patternIndex',
                'type': 'ViInt32'
            },
            {
                'cppName': 'nameBufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'nameBufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'name',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'name',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'nameBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetPatternPinIndexes': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'startLabel',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'startLabel',
                'type': 'ViConstString'
            },
            {
                'cppName': 'pinIndexesBufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'pinIndexesBufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'pinIndexes',
                'direction': 'out',
                'grpc_type': 'repeated sint32',
                'name': 'pinIndexes',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'pinIndexesBufferSize',
                    'value_twist': 'actualNumPins'
                },
                'type': 'ViInt32[]'
            },
            {
                'cppName': 'actualNumPins',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualNumPins',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetPatternPinList': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'startLabel',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'startLabel',
                'type': 'ViConstString'
            },
            {
                'cppName': 'pinListBufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'pinListBufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'pinList',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'pinList',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'pinListBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetPinName': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'pinIndex',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'pinIndex',
                'type': 'ViInt32'
            },
            {
                'cppName': 'nameBufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'nameBufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'name',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'name',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'nameBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetPinResultsPinInformation': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'pinIndexes',
                'direction': 'out',
                'grpc_type': 'repeated sint32',
                'name': 'pinIndexes',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualNumValues'
                },
                'type': 'ViInt32[]'
            },
            {
                'cppName': 'siteNumbers',
                'direction': 'out',
                'grpc_type': 'repeated sint32',
                'name': 'siteNumbers',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualNumValues'
                },
                'type': 'ViInt32[]'
            },
            {
                'cppName': 'channelIndexes',
                'direction': 'out',
                'grpc_type': 'repeated sint32',
                'name': 'channelIndexes',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualNumValues'
                },
                'type': 'ViInt32[]'
            },
            {
                'cppName': 'actualNumValues',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualNumValues',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSitePassFail': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'siteList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'siteList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'passFailBufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'passFailBufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'passFail',
                'direction': 'out',
                'grpc_type': 'repeated bool',
                'name': 'passFail',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'passFailBufferSize',
                    'value_twist': 'actualNumSites'
                },
                'type': 'ViBoolean[]'
            },
            {
                'cppName': 'actualNumSites',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualNumSites',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSiteResultsSiteNumbers': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'siteList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'siteList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'siteResultType',
                'direction': 'in',
                'enum': 'SiteResultType',
                'grpc_type': 'sint32',
                'name': 'siteResultType',
                'type': 'ViInt32'
            },
            {
                'cppName': 'siteNumbersBufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'siteNumbersBufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'siteNumbers',
                'direction': 'out',
                'grpc_type': 'repeated sint32',
                'name': 'siteNumbers',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'siteNumbersBufferSize',
                    'value_twist': 'actualNumSiteNumbers'
                },
                'type': 'ViInt32[]'
            },
            {
                'cppName': 'actualNumSiteNumbers',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualNumSiteNumbers',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetTimeSetDriveFormat': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'pin',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'pin',
                'type': 'ViConstString'
            },
            {
                'cppName': 'timeSet',
                'direction': 'in',
                'grpc_name': 'time_set_name',
                'grpc_type': 'string',
                'name': 'timeSet',
                'type': 'ViConstString'
            },
            {
                'cppName': 'format',
                'direction': 'out',
                'enum': 'DriveFormat',
                'grpc_type': 'sint32',
                'name': 'format',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetTimeSetEdge': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'pin',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'pin',
                'type': 'ViConstString'
            },
            {
                'cppName': 'timeSet',
                'direction': 'in',
                'grpc_name': 'time_set_name',
                'grpc_type': 'string',
                'name': 'timeSet',
                'type': 'ViConstString'
            },
            {
                'cppName': 'edge',
                'direction': 'in',
                'enum': 'TimeSetEdgeType',
                'grpc_type': 'sint32',
                'name': 'edge',
                'type': 'ViInt32'
            },
            {
                'cppName': 'time',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'time',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetTimeSetEdgeMultiplier': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'pin',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'pin',
                'type': 'ViConstString'
            },
            {
                'cppName': 'timeSet',
                'direction': 'in',
                'grpc_name': 'time_set_name',
                'grpc_type': 'string',
                'name': 'timeSet',
                'type': 'ViConstString'
            },
            {
                'cppName': 'edgeMultiplier',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'edgeMultiplier',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetTimeSetName': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'timeSetIndex',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'timeSetIndex',
                'type': 'ViInt32'
            },
            {
                'cppName': 'nameBufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'nameBufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'name',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'name',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'nameBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetTimeSetPeriod': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'timeSet',
                'direction': 'in',
                'grpc_name': 'time_set_name',
                'grpc_type': 'string',
                'name': 'timeSet',
                'type': 'ViConstString'
            },
            {
                'cppName': 'period',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'period',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'Init': {
        'cname': 'niDigital_init',
        'codegen_method': 'public',
        'init_method': True,
        'parameters': [
            {
                'cppName': 'resourceName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'resourceName',
                'type': 'ViString'
            },
            {
                'cppName': 'idQuery',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'idQuery',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'resetDevice',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'newVi',
                'direction': 'out',
                'grpc_name': 'vi',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'newVi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorMessage',
                'direction': 'out',
                'get_last_error': 'deprecated',
                'grpc_type': 'string',
                'name': 'errorMessage',
                'type': 'ViChar[]'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'ViInt32'
            },
            {
                'cppName': 'newSessionInitialized',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'newSessionInitialized',
                'proto_only': True,
                'type': 'bool'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitWithOptions': {
        'codegen_method': 'public',
        'init_method': True,
        'parameters': [
            {
                'cppName': 'resourceName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'resourceName',
                'type': 'ViString'
            },
            {
                'cppName': 'idQuery',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'idQuery',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'resetDevice',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'optionString',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'optionString',
                'type': 'ViConstString'
            },
            {
                'cppName': 'newVi',
                'direction': 'out',
                'grpc_name': 'vi',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'newVi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorMessage',
                'direction': 'out',
                'get_last_error': 'deprecated',
                'grpc_type': 'string',
                'name': 'errorMessage',
                'type': 'ViChar[]'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'ViInt32'
            },
            {
                'cppName': 'newSessionInitialized',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'newSessionInitialized',
                'proto_only': True,
                'type': 'bool'
            }
        ],
        'returns': 'ViStatus'
    },
    'Initiate': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'IsDone': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'done',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'done',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'IsSiteEnabled': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'site',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'site',
                'type': 'ViConstString'
            },
            {
                'cppName': 'enable',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'enable',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'LoadLevels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'levelsFilePath',
                'direction': 'in',
                'grpc_name': 'file_path',
                'grpc_type': 'string',
                'name': 'levelsFilePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'LoadPattern': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'filePath',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'LoadPinMap': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'pinMapFilePath',
                'direction': 'in',
                'grpc_name': 'file_path',
                'grpc_type': 'string',
                'name': 'pinMapFilePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'LoadSpecifications': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'specificationsFilePath',
                'direction': 'in',
                'grpc_name': 'file_path',
                'grpc_type': 'string',
                'name': 'specificationsFilePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'LoadTiming': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'timingFilePath',
                'direction': 'in',
                'grpc_name': 'file_path',
                'grpc_type': 'string',
                'name': 'timingFilePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'LockSession': {
        'codegen_method': 'private',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'callerHasLock',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'MapPinToChannel': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'pin',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'pin',
                'type': 'ViConstString'
            },
            {
                'cppName': 'site',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'site',
                'type': 'ViInt32'
            },
            {
                'cppName': 'channel',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channel',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'PPMUConfigureApertureTime': {
        'cname': 'niDigital_PPMU_ConfigureApertureTime',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'apertureTime',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'apertureTime',
                'type': 'ViReal64'
            },
            {
                'cppName': 'units',
                'direction': 'in',
                'enum': 'PpmuApertureTimeUnits',
                'grpc_type': 'sint32',
                'name': 'units',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'PPMUConfigureCurrentLevel': {
        'cname': 'niDigital_PPMU_ConfigureCurrentLevel',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'currentLevel',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'currentLevel',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'PPMUConfigureCurrentLevelRange': {
        'cname': 'niDigital_PPMU_ConfigureCurrentLevelRange',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'range',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'range',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'PPMUConfigureCurrentLimit': {
        'cname': 'niDigital_PPMU_ConfigureCurrentLimit',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'behavior',
                'direction': 'in',
                'enum': 'PpmuCurrentLimitBehavior',
                'grpc_type': 'sint32',
                'name': 'behavior',
                'type': 'ViInt32'
            },
            {
                'cppName': 'limit',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'limit',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'PPMUConfigureCurrentLimitRange': {
        'cname': 'niDigital_PPMU_ConfigureCurrentLimitRange',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'range',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'range',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'PPMUConfigureOutputFunction': {
        'cname': 'niDigital_PPMU_ConfigureOutputFunction',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'outputFunction',
                'direction': 'in',
                'enum': 'PpmuOutputFunction',
                'grpc_type': 'sint32',
                'name': 'outputFunction',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'PPMUConfigureVoltageLevel': {
        'cname': 'niDigital_PPMU_ConfigureVoltageLevel',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'voltageLevel',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'voltageLevel',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'PPMUConfigureVoltageLimits': {
        'cname': 'niDigital_PPMU_ConfigureVoltageLimits',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'lowerVoltageLimit',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'lowerVoltageLimit',
                'type': 'ViReal64'
            },
            {
                'cppName': 'upperVoltageLimit',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'upperVoltageLimit',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'PPMUMeasure': {
        'cname': 'niDigital_PPMU_Measure',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'measurementType',
                'direction': 'in',
                'enum': 'PpmuMeasurementType',
                'grpc_type': 'sint32',
                'name': 'measurementType',
                'type': 'ViInt32'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'measurements',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'measurements',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualNumRead'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'actualNumRead',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualNumRead',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'PPMUSource': {
        'cname': 'niDigital_PPMU_Source',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadSequencerFlag': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'flag',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'flag',
                'type': 'ViConstString'
            },
            {
                'cppName': 'value',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'value',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadSequencerRegister': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'reg',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'reg',
                'type': 'ViConstString'
            },
            {
                'cppName': 'value',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'value',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadStatic': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'data',
                'direction': 'out',
                'enum': 'PinState',
                'grpc_type': 'bytes',
                'name': 'data',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualNumRead'
                },
                'type': 'ViUInt8[]'
            },
            {
                'cppName': 'actualNumRead',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualNumRead',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'Reset': {
        'cname': 'niDigital_reset',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetAttribute': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiDigitalAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetDevice': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SelectFunction': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'function',
                'direction': 'in',
                'enum': 'SelectedFunction',
                'grpc_type': 'sint32',
                'name': 'function',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SelfCalibrate': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SelfTest': {
        'cname': 'niDigital_self_test',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'testResult',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'testResult',
                'type': 'ViInt16'
            },
            {
                'cppName': 'testMessage',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'testMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 2048
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'SendSoftwareEdgeTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'trigger',
                'direction': 'in',
                'enum': 'SoftwareTrigger',
                'grpc_type': 'sint32',
                'name': 'trigger',
                'type': 'ViInt32'
            },
            {
                'cppName': 'triggerIdentifier',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'triggerIdentifier',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViBoolean': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attribute',
                'direction': 'in',
                'grpc_type': 'NiDigitalAttribute',
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'value',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt32': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attribute',
                'direction': 'in',
                'grpc_type': 'NiDigitalAttribute',
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'in',
                'enum': 'NiDigitalInt32AttributeValues',
                'grpc_type': 'sint32',
                'name': 'value',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attribute',
                'direction': 'in',
                'grpc_type': 'NiDigitalAttribute',
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'in',
                'grpc_type': 'int64',
                'name': 'value_raw',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViReal64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attribute',
                'direction': 'in',
                'grpc_type': 'NiDigitalAttribute',
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'value_raw',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViSession': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_name': 'channel_list',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attribute',
                'direction': 'in',
                'grpc_type': 'NiDigitalAttribute',
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'value',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attribute',
                'direction': 'in',
                'grpc_type': 'NiDigitalAttribute',
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'value_raw',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'TDR': {
        'cname': 'niDigital_TDR',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'applyOffsets',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'applyOffsets',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'offsetsBufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'offsetsBufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'offsets',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'offsets',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'offsetsBufferSize',
                    'value_twist': 'actualNumOffsets'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'actualNumOffsets',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualNumOffsets',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'UnloadAllPatterns': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'unloadKeepAlivePattern',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'unloadKeepAlivePattern',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'UnloadSpecifications': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'specificationsFilePath',
                'direction': 'in',
                'grpc_name': 'file_path',
                'grpc_type': 'string',
                'name': 'specificationsFilePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'UnlockSession': {
        'codegen_method': 'private',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'callerHasLock',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'WaitUntilDone': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'timeout',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'timeout',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteSequencerFlag': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'flag',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'flag',
                'type': 'ViConstString'
            },
            {
                'cppName': 'value',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'value',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteSequencerFlagSynchronized': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'sessionCount',
                'direction': 'in',
                'grpc_type': 'uint32',
                'is_size_param': True,
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'cppName': 'sessions',
                'direction': 'in',
                'grpc_type': 'repeated nidevice_grpc.Session',
                'name': 'sessions',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]'
            },
            {
                'cppName': 'flag',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'flag',
                'type': 'ViConstString'
            },
            {
                'cppName': 'value',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'value',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteSequencerRegister': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'reg',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'reg',
                'type': 'ViConstString'
            },
            {
                'cppName': 'value',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'value',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteSourceWaveformBroadcastU32': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'waveformName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'waveformSize',
                'determine_size_from': [
                    'waveformData'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'waveformData',
                'direction': 'in',
                'grpc_type': 'repeated uint32',
                'name': 'waveformData',
                'size': {
                    'mechanism': 'len',
                    'value': 'waveformSize'
                },
                'type': 'ViUInt32[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteSourceWaveformDataFromFileTDMS': {
        'cname': 'niDigital_WriteSourceWaveformDataFromFileTDMS',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'waveformName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'waveformFilePath',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'waveformFilePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteSourceWaveformSiteUniqueU32': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'siteList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'siteList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'waveformName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'numWaveforms',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'numWaveforms',
                'type': 'ViInt32'
            },
            {
                'cppName': 'samplesPerWaveform',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'samplesPerWaveform',
                'type': 'ViInt32'
            },
            {
                'cppName': 'waveformData',
                'direction': 'in',
                'grpc_type': 'repeated uint32',
                'name': 'waveformData',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'ViUInt32[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteStatic': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'state',
                'direction': 'in',
                'enum': 'WriteStaticPinState',
                'grpc_type': 'uint32',
                'name': 'state',
                'type': 'ViUInt8'
            }
        ],
        'returns': 'ViStatus'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidigitalpattern/functions_addon.py sha256=a5f4e6e98b3259dac34d9003a636d68e248a27d8a22b0f4d2b3a7d77d538c541 bytes=24921 -->
## FILE: source/codegen/metadata/nidigitalpattern/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidigitalpattern/functions_addon.py`
- sha256: `a5f4e6e98b3259dac34d9003a636d68e248a27d8a22b0f4d2b3a7d77d538c541`
- bytes: 24921

````python
# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
    'SetRuntimeEnvironment': {
        'codegen_method': 'private',
        'parameters': [
            {
                'cppName': 'environment',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'environment',
                'type': 'ViConstString'
            },
            {
                'cppName': 'environmentVersion',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'environmentVersion',
                'type': 'ViConstString'
            },
            {
                'cppName': 'reserved1',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'reserved1',
                'type': 'ViConstString'
            },
            {
                'cppName': 'reserved2',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'reserved2',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
}

functions_validation_suppressions = {
}

for function_name in ['BurstPatternSynchronized', 'EnableMatchFailCombination', 'WriteSequencerFlagSynchronized']:
    functions_validation_suppressions[function_name] = {
        "parameters": {
            # We shipped this way, fixing it would be a breaking change
            "sessions": ["INPUT_ARRAY_SHOULD_NOT_HAVE_PASSED_IN_SIZE"]
        }
    }

functions_additional_burst_pattern = {
    'FancyBurstPattern': {
        'python_name': 'burst_pattern',
        'codegen_method': 'python-only',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_burst_pattern',
            }
        ],
        'documentation': {
            'description': """\nUses the start_label you specify to burst the pattern on the sites you specify. If you
specify wait_until_done as True, waits for the burst to complete, and returns comparison results for each site.

Digital pins retain their state at the end of a pattern burst until the first vector of the pattern burst, a call to
niDigital_WriteStatic, or a call to niDigital_ApplyLevelsAndTiming.

"""
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'sites',
                'name': 'siteList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pattern name or exported pattern label from which to start bursting the pattern.'
                },
                'name': 'startLabel',
                'type': 'ViConstString'
            },
            {
                'default_value': True,
                'direction': 'in',
                'documentation': {
                    'description': 'A Boolean that specifies whether to select the digital method for the pins in the pattern prior to bursting.'
                },
                'name': 'selectDigitalFunction',
                'type': 'ViBoolean'
            },
            {
                'default_value': True,
                'direction': 'in',
                'documentation': {
                    'description': 'A Boolean that indicates whether to wait until the bursting is complete.'
                },
                'name': 'waitUntilDone',
                'type': 'ViBoolean'
            },
            {
                'default_value': 'hightime.timedelta(seconds=10.0)',
                'direction': 'in',
                'documentation': {
                    'description': 'Maximum time (in seconds) allowed for this method to complete. If this method does not complete within this time interval, this method returns an error.'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds',
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nDictionary where each key is a site number and value is pass/fail,\nif wait_until_done is specified as True. Else, None.\n'
                },
                'name': 'passFail',
                'size': {
                    'mechanism': 'python-code',
                    'value': None
                },
                'type': 'ViBoolean',
                'type_in_documentation': '{ int: bool, int: bool, ... }',
            },
        ],
    },
}

functions_additional_write_source_waveform_site_unique = {
    'FancyWriteSourceWaveformSiteUnique': {
        'python_name': 'write_source_waveform_site_unique',
        'codegen_method': 'python-only',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_write_source_waveform_site_unique',
            }
        ],
        'documentation': {
            'description': 'Writes one waveform per site. Use this write function if you set the parameter of the create source waveform function to Site Unique.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The name to assign to the waveform. Use the waveform_name with source_start opcode in your pattern.\n'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nDictionary where each key is a site number and value is a collection of samples to use as source data\n'
                },
                'name': 'waveform_data',
                'type': 'ViUInt32',  # This type is ignored since this function isn't code generated
                'type_in_documentation': '{ int: basic sequence of unsigned int, int: basic sequence of unsigned int, ... }',
            },
        ],
    },
}

functions_additional_get_pin_results_pin_information = {
    'FancyGetPinResultsPinInformation': {
        'python_name': 'get_pin_results_pin_information',
        'codegen_method': 'python-only',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_get_pin_results_pin_information',
            }
        ],
        'documentation': {
            'description': 'Returns the pin names, site numbers, and channel names that correspond to per-pin data read from the digital pattern instrument. The function returns pin information in the same order as values read using the niDigital_ReadStatic function, niDigital_PPMU_Measure function, and niDigital_GetFailCount function. Use this function to match values the previously listed functions return with pins, sites, and instrument channels.',
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nList of named tuples with fields:\n\n- **pin_name** (str)\n- **site_number** (int)\n- **channel_name** (str)\n'
                },
                'name': 'pin_info',
                'python_type': 'PinInfo',
                'size': {
                    'mechanism': 'python-code',
                    'value': None
                },
                'type': 'ViInt32[]'
            }
        ],
    },
}

functions_additional_get_site_pass_fail = {
    'FancyGetSitePassFail': {
        'python_name': 'get_site_pass_fail',
        'codegen_method': 'python-only',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_get_site_pass_fail',
            }
        ],
        'documentation': {
            'description': '\nReturns dictionary where each key is a site number and value is pass/fail\n\n',
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'sites',
                'name': 'siteList',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nDictionary where each key is a site number and value is pass/fail\n'
                },
                'name': 'passFail',
                'size': {
                    'mechanism': 'python-code',
                    'value': None
                },
                'type': 'ViBoolean',
                'type_in_documentation': '{ int: bool, int: bool, ... }',
            },
        ],
    },
}

functions_additional_fetch_capture_waveform = {
    'FancyFetchCaptureWaveform': {
        'python_name': 'fetch_capture_waveform',
        'codegen_method': 'python-only',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_fetch_capture_waveform',
            }
        ],
       'documentation': {
            'description': '\nReturns dictionary where each key is a site number and value is a collection of digital states representing capture waveform data\n\n',
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'sites',
                'name': 'siteList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Waveform name you create with the create capture waveform function. Use the waveform_name parameter with capture_start opcode in your pattern.',
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of samples to fetch.',
                },
                'name': 'samplesToRead',
                'type': 'ViInt32'
            },
            {
                'default_value': 'hightime.timedelta(seconds=10.0)',
                'direction': 'in',
                'documentation': {
                    'description': 'Maximum time (in seconds) allowed for this function to complete. If this function does not complete within this time interval, this function returns an error.',
                },
                'name': 'timeout',
                'type': 'ViReal64',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds',
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nDictionary where each key is a site number and value is a collection of digital states representing capture waveform data\n'
                },
                'name': 'waveform',
                'size': {
                    'mechanism': 'python-code',
                    'value': None
                },
                'type': 'ViUInt32',
                'type_in_documentation': '{ int: memoryview of array.array of unsigned int, int: memoryview of array.array of unsigned int, ... }',
            },
        ],
    },
}

functions_additional_fetch_history_ram_cycle_information = {
    'FancyFetchHistoryRAMCycleInformation': {
        'python_name': 'fetch_history_ram_cycle_information',
        'codegen_method': 'python-only',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_fetch_history_ram_cycle_information',
            }
        ],
        'documentation': {
            'description': """\nReturns the pattern information acquired for the specified cycles.
            
If the pattern is using the edge multiplier feature, cycle numbers represent tester cycles, each of which may
consist of multiple DUT cycles. When using pins with mixed edge multipliers, pins may return
NIDIGITAL_VAL_PIN_STATE_NOT_ACQUIRED for DUT cycles where those pins do not have edges defined.

Site number on which to retrieve pattern information must be specified via sites repeated capability.
The method returns an error if more than one site is specified.

Pins for which to retrieve pattern information must be specified via pins repeated capability.
If pins are not specified, pin list from the pattern containing the start label is used. Call
niDigital_GetPatternPinList with the start label to retrieve the pins associated with the pattern burst:

.. code:: python

 session.sites[0].pins['PinA', 'PinB'].fetch_history_ram_cycle_information(0, -1)
""",
            'note': """\nBefore bursting a pattern, you must configure the History RAM trigger and specify which cycles to acquire. 

NIDIGITAL_ATTR_HISTORY_RAM_TRIGGER_TYPE should be used to specify the trigger condition on which History RAM
starts acquiring pattern information.

If History RAM trigger is configured as NIDIGITAL_VAL_CYCLE_NUMBER,
NIDIGITAL_ATTR_CYCLE_NUMBER_HISTORY_RAM_TRIGGER_CYCLE_NUMBER should be used to specify the cycle number on which
History RAM starts acquiring pattern information.

If History RAM trigger is configured as NIDIGITAL_VAL_PATTERN_LABEL,
NIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_LABEL should be used to specify the pattern label from which to
start acquiring pattern information. 
NIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_VECTOR_OFFSET should be used to specify the number of vectors
following the specified pattern label from which to start acquiring pattern information. 
NIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_CYCLE_OFFSET should be used to specify the number of cycles
following the specified pattern label and vector offset from which to start acquiring pattern information.

For all History RAM trigger conditions, NIDIGITAL_ATTR_HISTORY_RAM_PRETRIGGER_SAMPLES should be used to specify
the number of samples to acquire before the trigger conditions are met. If you configure History RAM to only
acquire failed cycles, you must set NIDIGITAL_ATTR_HISTORY_RAM_PRETRIGGER_SAMPLES to 0. 

NIDIGITAL_ATTR_HISTORY_RAM_CYCLES_TO_ACQUIRE should be used to specify which cycles History RAM acquires after
the trigger conditions are met.
""",
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Site on which to retrieve History RAM data. The method returns an error if more than one site is specified.'
                },
                'is_repeated_capability': True,
                'repeated_capability_type': 'sites',
                'name': 'site',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pins for which to retrieve History RAM data. If empty, the pin list from the pattern\ncontaining the start label is used. Call niDigital_GetPatternPinList with the start\nlabel to retrieve the pins associated with the pattern burst.'
                },
                'is_repeated_capability': True,
                'repeated_capability_type': 'pins',
                'name': 'pinList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Sample index from which to start fetching pattern information.'
                },
                'name': 'position',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of samples to fetch. A value of -1 specifies to fetch all available samples.'
                },
                'name': 'samples_to_read',
                'type': 'ViInt64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': """Returns a list of class instances with
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
   will have a value of NIDIGITAL_VAL_PIN_STATE_NOT_ACQUIRED.
   Length of the outer list will be equal to the value of edge multiplier for the given vector.
   Length of the inner list will be equal to the number of pins requested.
-  **actual_pin_states** (list of list of enums.PinState) Pin states acquired by History RAM in the
   order specified in the pin list. Pins without defined edges in the specified DUT cycle will have a
   value of NIDIGITAL_VAL_PIN_STATE_NOT_ACQUIRED.
   Length of the outer list will be equal to the value of edge multiplier for the given vector.
   Length of the inner list will be equal to the number of pins requested.
-  **per_pin_pass_fail** (list of list of bool) Pass fail information for pins in the order specified in
   the pin list. Pins without defined edges in the specified DUT cycle will have a value of pass (True).
   Length of the outer list will be equal to the value of edge multiplier for the given vector.
   Length of the inner list will be equal to the number of pins requested.
"""
                },
                'name': 'history_ram_cycle_information',
                'size': {
                    'mechanism': 'python-code',
                    'value': None
                },
                'type': 'HistoryRAMCycleInformation[]'
            }
        ],
    },
}

functions_additional_load_specifications_levels_and_timing = {
    'FancyLoadSpecificationsLevelsAndTiming': {
        'python_name': 'load_specifications_levels_and_timing',
        'codegen_method': 'python-only',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_load_specifications_levels_and_timing',
            }
        ],
        'documentation': {
            'description': """\nLoads settings in specifications, levels, and timing sheets. These settings are not
applied to the digital pattern instrument until niDigital_ApplyLevelsAndTiming is called.

If the levels and timing sheets contains formulas, they are evaluated at load time.
If the formulas refer to variables, the specifications sheets that define those
variables must be loaded either first, or at the same time as the levels and timing sheets.

"""
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': '\nAbsolute file path of one or more specifications files.\n'
                },
                'name': 'specificationsFilePaths',
                'type': 'ViConstString[]',  # Value is unused, but required by code generator
                'type_in_documentation': 'str or basic sequence of str',
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': '\nAbsolute file path of one or more levels sheet files.\n'
                },
                'name': 'levelsFilePaths',
                'type': 'ViConstString[]',  # Value is unused, but required by code generator
                'type_in_documentation': 'str or basic sequence of str',
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': '\nAbsolute file path of one or more timing sheet files.\n'
                },
                'name': 'timingFilePaths',
                'type': 'ViConstString[]',  # Value is unused, but required by code generator
                'type_in_documentation': 'str or basic sequence of str',
            },
        ],
    },
}

functions_additional_unload_specifications = {
    'FancyUnloadSpecifications': {
        'python_name': 'unload_specifications',
        'codegen_method': 'python-only',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_unload_specifications',
            }
        ],
        'documentation': {
            'description': """\nUnloads the given specifications sheets present in the previously loaded
specifications files that you select.

You must call niDigital_FancyLoadSpecificationsLevelsAndTiming to reload the files with updated
specifications values. You must then call niDigital_ApplyLevelsAndTiming in order to apply
the levels and timing values that reference the updated specifications values.

"""
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nAbsolute file path of one or more loaded specifications files.\n'
                },
                'name': 'filePaths',
                'type': 'ViConstString[]',  # Value is unused, but required by code generator
                'type_in_documentation': 'str or basic sequence of str',
            },
        ],
    },
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidigitalpattern/nidigitalpattern.proto sha256=2bf0e18a930d562715c6a1fe16c87a39f9be0402c5081b42d70a8737d34c0467 bytes=54672 -->
## FILE: source/codegen/metadata/nidigitalpattern/nidigitalpattern.proto

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidigitalpattern/nidigitalpattern.proto`
- sha256: `2bf0e18a930d562715c6a1fe16c87a39f9be0402c5081b42d70a8737d34c0467`
- bytes: 54672

````protobuf

//---------------------------------------------------------------------
// This file is generated from NI-Digital Pattern Driver API metadata version 23.0.0f112
//---------------------------------------------------------------------
// Proto file for the NI-Digital Pattern Driver Metadata
//---------------------------------------------------------------------
syntax = "proto3";

option java_multiple_files = true;
option java_package = "com.ni.grpc.nidigital";
option java_outer_classname = "NiDigital";
option csharp_namespace = "NationalInstruments.Grpc.Digital";

package nidigitalpattern_grpc;

import "session.proto";

service NiDigital {
  rpc Abort(AbortRequest) returns (AbortResponse);
  rpc AbortKeepAlive(AbortKeepAliveRequest) returns (AbortKeepAliveResponse);
  rpc ApplyLevelsAndTiming(ApplyLevelsAndTimingRequest) returns (ApplyLevelsAndTimingResponse);
  rpc ApplyTDROffsets(ApplyTDROffsetsRequest) returns (ApplyTDROffsetsResponse);
  rpc BurstPattern(BurstPatternRequest) returns (BurstPatternResponse);
  rpc BurstPatternSynchronized(BurstPatternSynchronizedRequest) returns (BurstPatternSynchronizedResponse);
  rpc ClearError(ClearErrorRequest) returns (ClearErrorResponse);
  rpc ClockGeneratorAbort(ClockGeneratorAbortRequest) returns (ClockGeneratorAbortResponse);
  rpc ClockGeneratorGenerateClock(ClockGeneratorGenerateClockRequest) returns (ClockGeneratorGenerateClockResponse);
  rpc ClockGeneratorInitiate(ClockGeneratorInitiateRequest) returns (ClockGeneratorInitiateResponse);
  rpc Close(CloseRequest) returns (CloseResponse);
  rpc Commit(CommitRequest) returns (CommitResponse);
  rpc ConfigureActiveLoadLevels(ConfigureActiveLoadLevelsRequest) returns (ConfigureActiveLoadLevelsResponse);
  rpc ConfigureCycleNumberHistoryRAMTrigger(ConfigureCycleNumberHistoryRAMTriggerRequest) returns (ConfigureCycleNumberHistoryRAMTriggerResponse);
  rpc ConfigureDigitalEdgeConditionalJumpTrigger(ConfigureDigitalEdgeConditionalJumpTriggerRequest) returns (ConfigureDigitalEdgeConditionalJumpTriggerResponse);
  rpc ConfigureDigitalEdgeStartTrigger(ConfigureDigitalEdgeStartTriggerRequest) returns (ConfigureDigitalEdgeStartTriggerResponse);
  rpc ConfigureFirstFailureHistoryRAMTrigger(ConfigureFirstFailureHistoryRAMTriggerRequest) returns (ConfigureFirstFailureHistoryRAMTriggerResponse);
  rpc ConfigureHistoryRAMCyclesToAcquire(ConfigureHistoryRAMCyclesToAcquireRequest) returns (ConfigureHistoryRAMCyclesToAcquireResponse);
  rpc ConfigurePatternBurstSites(ConfigurePatternBurstSitesRequest) returns (ConfigurePatternBurstSitesResponse);
  rpc ConfigurePatternLabelHistoryRAMTrigger(ConfigurePatternLabelHistoryRAMTriggerRequest) returns (ConfigurePatternLabelHistoryRAMTriggerResponse);
  rpc ConfigureSoftwareEdgeConditionalJumpTrigger(ConfigureSoftwareEdgeConditionalJumpTriggerRequest) returns (ConfigureSoftwareEdgeConditionalJumpTriggerResponse);
  rpc ConfigureSoftwareEdgeStartTrigger(ConfigureSoftwareEdgeStartTriggerRequest) returns (ConfigureSoftwareEdgeStartTriggerResponse);
  rpc ConfigureStartLabel(ConfigureStartLabelRequest) returns (ConfigureStartLabelResponse);
  rpc ConfigureTerminationMode(ConfigureTerminationModeRequest) returns (ConfigureTerminationModeResponse);
  rpc ConfigureTimeSetCompareEdgesStrobe(ConfigureTimeSetCompareEdgesStrobeRequest) returns (ConfigureTimeSetCompareEdgesStrobeResponse);
  rpc ConfigureTimeSetCompareEdgesStrobe2x(ConfigureTimeSetCompareEdgesStrobe2xRequest) returns (ConfigureTimeSetCompareEdgesStrobe2xResponse);
  rpc ConfigureTimeSetDriveEdges(ConfigureTimeSetDriveEdgesRequest) returns (ConfigureTimeSetDriveEdgesResponse);
  rpc ConfigureTimeSetDriveEdges2x(ConfigureTimeSetDriveEdges2xRequest) returns (ConfigureTimeSetDriveEdges2xResponse);
  rpc ConfigureTimeSetDriveFormat(ConfigureTimeSetDriveFormatRequest) returns (ConfigureTimeSetDriveFormatResponse);
  rpc ConfigureTimeSetEdge(ConfigureTimeSetEdgeRequest) returns (ConfigureTimeSetEdgeResponse);
  rpc ConfigureTimeSetEdgeMultiplier(ConfigureTimeSetEdgeMultiplierRequest) returns (ConfigureTimeSetEdgeMultiplierResponse);
  rpc ConfigureTimeSetPeriod(ConfigureTimeSetPeriodRequest) returns (ConfigureTimeSetPeriodResponse);
  rpc ConfigureVoltageLevels(ConfigureVoltageLevelsRequest) returns (ConfigureVoltageLevelsResponse);
  rpc CreateCaptureWaveformFromFileDigicapture(CreateCaptureWaveformFromFileDigicaptureRequest) returns (CreateCaptureWaveformFromFileDigicaptureResponse);
  rpc CreateCaptureWaveformParallel(CreateCaptureWaveformParallelRequest) returns (CreateCaptureWaveformParallelResponse);
  rpc CreateCaptureWaveformSerial(CreateCaptureWaveformSerialRequest) returns (CreateCaptureWaveformSerialResponse);
  rpc CreateChannelMap(CreateChannelMapRequest) returns (CreateChannelMapResponse);
  rpc CreatePinGroup(CreatePinGroupRequest) returns (CreatePinGroupResponse);
  rpc CreatePinMap(CreatePinMapRequest) returns (CreatePinMapResponse);
  rpc CreateSourceWaveformFromFileTDMS(CreateSourceWaveformFromFileTDMSRequest) returns (CreateSourceWaveformFromFileTDMSResponse);
  rpc CreateSourceWaveformParallel(CreateSourceWaveformParallelRequest) returns (CreateSourceWaveformParallelResponse);
  rpc CreateSourceWaveformSerial(CreateSourceWaveformSerialRequest) returns (CreateSourceWaveformSerialResponse);
  rpc CreateTimeSet(CreateTimeSetRequest) returns (CreateTimeSetResponse);
  rpc DeleteAllTimeSets(DeleteAllTimeSetsRequest) returns (DeleteAllTimeSetsResponse);
  rpc DisableConditionalJumpTrigger(DisableConditionalJumpTriggerRequest) returns (DisableConditionalJumpTriggerResponse);
  rpc DisableSites(DisableSitesRequest) returns (DisableSitesResponse);
  rpc DisableStartTrigger(DisableStartTriggerRequest) returns (DisableStartTriggerResponse);
  rpc EnableMatchFailCombination(EnableMatchFailCombinationRequest) returns (EnableMatchFailCombinationResponse);
  rpc EnableSites(EnableSitesRequest) returns (EnableSitesResponse);
  rpc EndChannelMap(EndChannelMapRequest) returns (EndChannelMapResponse);
  rpc ErrorMessage(ErrorMessageRequest) returns (ErrorMessageResponse);
  rpc ExportSignal(ExportSignalRequest) returns (ExportSignalResponse);
  rpc FetchCaptureWaveformU32(FetchCaptureWaveformU32Request) returns (FetchCaptureWaveformU32Response);
  rpc FetchHistoryRAMCycleInformation(FetchHistoryRAMCycleInformationRequest) returns (FetchHistoryRAMCycleInformationResponse);
  rpc FetchHistoryRAMCyclePinData(FetchHistoryRAMCyclePinDataRequest) returns (FetchHistoryRAMCyclePinDataResponse);
  rpc FetchHistoryRAMScanCycleNumber(FetchHistoryRAMScanCycleNumberRequest) returns (FetchHistoryRAMScanCycleNumberResponse);
  rpc FrequencyCounterConfigureMeasurementMode(FrequencyCounterConfigureMeasurementModeRequest) returns (FrequencyCounterConfigureMeasurementModeResponse);
  rpc FrequencyCounterConfigureMeasurementTime(FrequencyCounterConfigureMeasurementTimeRequest) returns (FrequencyCounterConfigureMeasurementTimeResponse);
  rpc FrequencyCounterMeasureFrequency(FrequencyCounterMeasureFrequencyRequest) returns (FrequencyCounterMeasureFrequencyResponse);
  rpc GetAttributeViBoolean(GetAttributeViBooleanRequest) returns (GetAttributeViBooleanResponse);
  rpc GetAttributeViInt32(GetAttributeViInt32Request) returns (GetAttributeViInt32Response);
  rpc GetAttributeViInt64(GetAttributeViInt64Request) returns (GetAttributeViInt64Response);
  rpc GetAttributeViReal64(GetAttributeViReal64Request) returns (GetAttributeViReal64Response);
  rpc GetAttributeViSession(GetAttributeViSessionRequest) returns (GetAttributeViSessionResponse);
  rpc GetAttributeViString(GetAttributeViStringRequest) returns (GetAttributeViStringResponse);
  rpc GetChannelName(GetChannelNameRequest) returns (GetChannelNameResponse);
  rpc GetChannelNameFromString(GetChannelNameFromStringRequest) returns (GetChannelNameFromStringResponse);
  rpc GetError(GetErrorRequest) returns (GetErrorResponse);
  rpc GetFailCount(GetFailCountRequest) returns (GetFailCountResponse);
  rpc GetHistoryRAMSampleCount(GetHistoryRAMSampleCountRequest) returns (GetHistoryRAMSampleCountResponse);
  rpc GetPatternName(GetPatternNameRequest) returns (GetPatternNameResponse);
  rpc GetPatternPinIndexes(GetPatternPinIndexesRequest) returns (GetPatternPinIndexesResponse);
  rpc GetPatternPinList(GetPatternPinListRequest) returns (GetPatternPinListResponse);
  rpc GetPinName(GetPinNameRequest) returns (GetPinNameResponse);
  rpc GetPinResultsPinInformation(GetPinResultsPinInformationRequest) returns (GetPinResultsPinInformationResponse);
  rpc GetSitePassFail(GetSitePassFailRequest) returns (GetSitePassFailResponse);
  rpc GetSiteResultsSiteNumbers(GetSiteResultsSiteNumbersRequest) returns (GetSiteResultsSiteNumbersResponse);
  rpc GetTimeSetDriveFormat(GetTimeSetDriveFormatRequest) returns (GetTimeSetDriveFormatResponse);
  rpc GetTimeSetEdge(GetTimeSetEdgeRequest) returns (GetTimeSetEdgeResponse);
  rpc GetTimeSetEdgeMultiplier(GetTimeSetEdgeMultiplierRequest) returns (GetTimeSetEdgeMultiplierResponse);
  rpc GetTimeSetName(GetTimeSetNameRequest) returns (GetTimeSetNameResponse);
  rpc GetTimeSetPeriod(GetTimeSetPeriodRequest) returns (GetTimeSetPeriodResponse);
  rpc Init(InitRequest) returns (InitResponse);
  rpc InitWithOptions(InitWithOptionsRequest) returns (InitWithOptionsResponse);
  rpc Initiate(InitiateRequest) returns (InitiateResponse);
  rpc IsDone(IsDoneRequest) returns (IsDoneResponse);
  rpc IsSiteEnabled(IsSiteEnabledRequest) returns (IsSiteEnabledResponse);
  rpc LoadLevels(LoadLevelsRequest) returns (LoadLevelsResponse);
  rpc LoadPattern(LoadPatternRequest) returns (LoadPatternResponse);
  rpc LoadPinMap(LoadPinMapRequest) returns (LoadPinMapResponse);
  rpc LoadSpecifications(LoadSpecificationsRequest) returns (LoadSpecificationsResponse);
  rpc LoadTiming(LoadTimingRequest) returns (LoadTimingResponse);
  rpc MapPinToChannel(MapPinToChannelRequest) returns (MapPinToChannelResponse);
  rpc PPMUConfigureApertureTime(PPMUConfigureApertureTimeRequest) returns (PPMUConfigureApertureTimeResponse);
  rpc PPMUConfigureCurrentLevel(PPMUConfigureCurrentLevelRequest) returns (PPMUConfigureCurrentLevelResponse);
  rpc PPMUConfigureCurrentLevelRange(PPMUConfigureCurrentLevelRangeRequest) returns (PPMUConfigureCurrentLevelRangeResponse);
  rpc PPMUConfigureCurrentLimit(PPMUConfigureCurrentLimitRequest) returns (PPMUConfigureCurrentLimitResponse);
  rpc PPMUConfigureCurrentLimitRange(PPMUConfigureCurrentLimitRangeRequest) returns (PPMUConfigureCurrentLimitRangeResponse);
  rpc PPMUConfigureOutputFunction(PPMUConfigureOutputFunctionRequest) returns (PPMUConfigureOutputFunctionResponse);
  rpc PPMUConfigureVoltageLevel(PPMUConfigureVoltageLevelRequest) returns (PPMUConfigureVoltageLevelResponse);
  rpc PPMUConfigureVoltageLimits(PPMUConfigureVoltageLimitsRequest) returns (PPMUConfigureVoltageLimitsResponse);
  rpc PPMUMeasure(PPMUMeasureRequest) returns (PPMUMeasureResponse);
  rpc PPMUSource(PPMUSourceRequest) returns (PPMUSourceResponse);
  rpc ReadSequencerFlag(ReadSequencerFlagRequest) returns (ReadSequencerFlagResponse);
  rpc ReadSequencerRegister(ReadSequencerRegisterRequest) returns (ReadSequencerRegisterResponse);
  rpc ReadStatic(ReadStaticRequest) returns (ReadStaticResponse);
  rpc Reset(ResetRequest) returns (ResetResponse);
  rpc ResetAttribute(ResetAttributeRequest) returns (ResetAttributeResponse);
  rpc ResetDevice(ResetDeviceRequest) returns (ResetDeviceResponse);
  rpc SelectFunction(SelectFunctionRequest) returns (SelectFunctionResponse);
  rpc SelfCalibrate(SelfCalibrateRequest) returns (SelfCalibrateResponse);
  rpc SelfTest(SelfTestRequest) returns (SelfTestResponse);
  rpc SendSoftwareEdgeTrigger(SendSoftwareEdgeTriggerRequest) returns (SendSoftwareEdgeTriggerResponse);
  rpc SetAttributeViBoolean(SetAttributeViBooleanRequest) returns (SetAttributeViBooleanResponse);
  rpc SetAttributeViInt32(SetAttributeViInt32Request) returns (SetAttributeViInt32Response);
  rpc SetAttributeViInt64(SetAttributeViInt64Request) returns (SetAttributeViInt64Response);
  rpc SetAttributeViReal64(SetAttributeViReal64Request) returns (SetAttributeViReal64Response);
  rpc SetAttributeViSession(SetAttributeViSessionRequest) returns (SetAttributeViSessionResponse);
  rpc SetAttributeViString(SetAttributeViStringRequest) returns (SetAttributeViStringResponse);
  rpc TDR(TDRRequest) returns (TDRResponse);
  rpc UnloadAllPatterns(UnloadAllPatternsRequest) returns (UnloadAllPatternsResponse);
  rpc UnloadSpecifications(UnloadSpecificationsRequest) returns (UnloadSpecificationsResponse);
  rpc WaitUntilDone(WaitUntilDoneRequest) returns (WaitUntilDoneResponse);
  rpc WriteSequencerFlag(WriteSequencerFlagRequest) returns (WriteSequencerFlagResponse);
  rpc WriteSequencerFlagSynchronized(WriteSequencerFlagSynchronizedRequest) returns (WriteSequencerFlagSynchronizedResponse);
  rpc WriteSequencerRegister(WriteSequencerRegisterRequest) returns (WriteSequencerRegisterResponse);
  rpc WriteSourceWaveformBroadcastU32(WriteSourceWaveformBroadcastU32Request) returns (WriteSourceWaveformBroadcastU32Response);
  rpc WriteSourceWaveformDataFromFileTDMS(WriteSourceWaveformDataFromFileTDMSRequest) returns (WriteSourceWaveformDataFromFileTDMSResponse);
  rpc WriteSourceWaveformSiteUniqueU32(WriteSourceWaveformSiteUniqueU32Request) returns (WriteSourceWaveformSiteUniqueU32Response);
  rpc WriteStatic(WriteStaticRequest) returns (WriteStaticResponse);
}

enum NiDigitalAttribute {
  NIDIGITAL_ATTRIBUTE_UNSPECIFIED = 0;
  NIDIGITAL_ATTRIBUTE_RANGE_CHECK = 1050002;
  NIDIGITAL_ATTRIBUTE_QUERY_INSTRUMENT_STATUS = 1050003;
  NIDIGITAL_ATTRIBUTE_CACHE = 1050004;
  NIDIGITAL_ATTRIBUTE_SIMULATE = 1050005;
  NIDIGITAL_ATTRIBUTE_RECORD_COERCIONS = 1050006;
  NIDIGITAL_ATTRIBUTE_DRIVER_SETUP = 1050007;
  NIDIGITAL_ATTRIBUTE_INTERCHANGE_CHECK = 1050021;
  NIDIGITAL_ATTRIBUTE_CHANNEL_COUNT = 1050203;
  NIDIGITAL_ATTRIBUTE_SPECIFIC_DRIVER_PREFIX = 1050302;
  NIDIGITAL_ATTRIBUTE_IO_RESOURCE_DESCRIPTOR = 1050304;
  NIDIGITAL_ATTRIBUTE_LOGICAL_NAME = 1050305;
  NIDIGITAL_ATTRIBUTE_SUPPORTED_INSTRUMENT_MODELS = 1050327;
  NIDIGITAL_ATTRIBUTE_GROUP_CAPABILITIES = 1050401;
  NIDIGITAL_ATTRIBUTE_INSTRUMENT_FIRMWARE_REVISION = 1050510;
  NIDIGITAL_ATTRIBUTE_INSTRUMENT_MANUFACTURER = 1050511;
  NIDIGITAL_ATTRIBUTE_INSTRUMENT_MODEL = 1050512;
  NIDIGITAL_ATTRIBUTE_SPECIFIC_DRIVER_VENDOR = 1050513;
  NIDIGITAL_ATTRIBUTE_SPECIFIC_DRIVER_DESCRIPTION = 1050514;
  NIDIGITAL_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION = 1050515;
  NIDIGITAL_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION = 1050516;
  NIDIGITAL_ATTRIBUTE_SPECIFIC_DRIVER_REVISION = 1050551;
  NIDIGITAL_ATTRIBUTE_SERIAL_NUMBER = 1150001;
  NIDIGITAL_ATTRIBUTE_SELECTED_FUNCTION = 1150004;
  NIDIGITAL_ATTRIBUTE_TERMINATION_MODE = 1150006;
  NIDIGITAL_ATTRIBUTE_VIL = 1150007;
  NIDIGITAL_ATTRIBUTE_VIH = 1150008;
  NIDIGITAL_ATTRIBUTE_VOL = 1150009;
  NIDIGITAL_ATTRIBUTE_VOH = 1150010;
  NIDIGITAL_ATTRIBUTE_VTERM = 1150011;
  NIDIGITAL_ATTRIBUTE_ACTIVE_LOAD_IOL = 1150012;
  NIDIGITAL_ATTRIBUTE_ACTIVE_LOAD_IOH = 1150013;
  NIDIGITAL_ATTRIBUTE_ACTIVE_LOAD_VCOM = 1150014;
  NIDIGITAL_ATTRIBUTE_PPMU_OUTPUT_FUNCTION = 1150015;
  NIDIGITAL_ATTRIBUTE_PPMU_VOLTAGE_LEVEL = 1150016;
  NIDIGITAL_ATTRIBUTE_PPMU_CURRENT_LIMIT_RANGE = 1150017;
  NIDIGITAL_ATTRIBUTE_PPMU_CURRENT_LEVEL = 1150019;
  NIDIGITAL_ATTRIBUTE_PPMU_CURRENT_LEVEL_RANGE = 1150020;
  NIDIGITAL_ATTRIBUTE_PPMU_VOLTAGE_LIMIT_LOW = 1150021;
  NIDIGITAL_ATTRIBUTE_PPMU_VOLTAGE_LIMIT_HIGH = 1150022;
  NIDIGITAL_ATTRIBUTE_START_LABEL = 1150023;
  NIDIGITAL_ATTRIBUTE_START_TRIGGER_TYPE = 1150029;
  NIDIGITAL_ATTRIBUTE_DIGITAL_EDGE_START_TRIGGER_SOURCE = 1150030;
  NIDIGITAL_ATTRIBUTE_DIGITAL_EDGE_START_TRIGGER_EDGE = 1150031;
  NIDIGITAL_ATTRIBUTE_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL = 1150032;
  NIDIGITAL_ATTRIBUTE_CONDITIONAL_JUMP_TRIGGER_TYPE = 1150033;
  NIDIGITAL_ATTRIBUTE_DIGITAL_EDGE_CONDITIONAL_JUMP_TRIGGER_SOURCE = 1150034;
  NIDIGITAL_ATTRIBUTE_DIGITAL_EDGE_CONDITIONAL_JUMP_TRIGGER_EDGE = 1150035;
  NIDIGITAL_ATTRIBUTE_EXPORTED_CONDITIONAL_JUMP_TRIGGER_OUTPUT_TERMINAL = 1150036;
  NIDIGITAL_ATTRIBUTE_PPMU_APERTURE_TIME = 1150037;
  NIDIGITAL_ATTRIBUTE_PPMU_APERTURE_TIME_UNITS = 1150038;
  NIDIGITAL_ATTRIBUTE_START_TRIGGER_TERMINAL_NAME = 1150039;
  NIDIGITAL_ATTRIBUTE_CONDITIONAL_JUMP_TRIGGER_TERMINAL_NAME = 1150040;
  NIDIGITAL_ATTRIBUTE_EXPORTED_PATTERN_OPCODE_EVENT_OUTPUT_TERMINAL = 1150041;
  NIDIGITAL_ATTRIBUTE_PATTERN_OPCODE_EVENT_TERMINAL_NAME = 1150042;
  NIDIGITAL_ATTRIBUTE_HISTORY_RAM_TRIGGER_TYPE = 1150043;
  NIDIGITAL_ATTRIBUTE_CYCLE_NUMBER_HISTORY_RAM_TRIGGER_CYCLE_NUMBER = 1150044;
  NIDIGITAL_ATTRIBUTE_PATTERN_LABEL_HISTORY_RAM_TRIGGER_CYCLE_OFFSET = 1150045;
  NIDIGITAL_ATTRIBUTE_PATTERN_LABEL_HISTORY_RAM_TRIGGER_LABEL = 1150046;
  NIDIGITAL_ATTRIBUTE_HISTORY_RAM_CYCLES_TO_ACQUIRE = 1150047;
  NIDIGITAL_ATTRIBUTE_HISTORY_RAM_PRETRIGGER_SAMPLES = 1150048;
  NIDIGITAL_ATTRIBUTE_TDR_OFFSET = 1150051;
  NIDIGITAL_ATTRIBUTE_PATTERN_LABEL_HISTORY_RAM_TRIGGER_VECTOR_OFFSET = 1150052;
  NIDIGITAL_ATTRIBUTE_PPMU_CURRENT_LIMIT = 1150054;
  NIDIGITAL_ATTRIBUTE_PPMU_CURRENT_LIMIT_SUPPORTED = 1150055;
  NIDIGITAL_ATTRIBUTE_SEQUENCER_FLAG_TERMINAL_NAME = 1150059;
  NIDIGITAL_ATTRIBUTE_MASK_COMPARE = 1150060;
  NIDIGITAL_ATTRIBUTE_HALT_ON_KEEP_ALIVE_OPCODE = 1150062;
  NIDIGITAL_ATTRIBUTE_IS_KEEP_ALIVE_ACTIVE = 1150063;
  NIDIGITAL_ATTRIBUTE_PPMU_CURRENT_LIMIT_BEHAVIOR = 1150064;
  NIDIGITAL_ATTRIBUTE_FREQUENCY_COUNTER_MEASUREMENT_TIME = 1150069;
  NIDIGITAL_ATTRIBUTE_TIMING_ABSOLUTE_DELAY_ENABLED = 1150071;
  NIDIGITAL_ATTRIBUTE_TIMING_ABSOLUTE_DELAY = 1150072;
  NIDIGITAL_ATTRIBUTE_CLOCK_GENERATOR_FREQUENCY = 1150073;
  NIDIGITAL_ATTRIBUTE_CLOCK_GENERATOR_IS_RUNNING = 1150074;
  NIDIGITAL_ATTRIBUTE_PPMU_ALLOW_EXTENDED_VOLTAGE_RANGE = 1150076;
  NIDIGITAL_ATTRIBUTE_HISTORY_RAM_MAX_SAMPLES_TO_ACQUIRE_PER_SITE = 1150077;
  NIDIGITAL_ATTRIBUTE_HISTORY_RAM_NUMBER_OF_SAMPLES_IS_FINITE = 1150078;
  NIDIGITAL_ATTRIBUTE_HISTORY_RAM_BUFFER_SIZE_PER_SITE = 1150079;
  NIDIGITAL_ATTRIBUTE_TDR_ENDPOINT_TERMINATION = 1150081;
  NIDIGITAL_ATTRIBUTE_FREQUENCY_COUNTER_MEASUREMENT_MODE = 1150084;
  NIDIGITAL_ATTRIBUTE_FREQUENCY_COUNTER_HYSTERESIS_ENABLED = 1150085;
  NIDIGITAL_ATTRIBUTE_RIO_TRIGGER_TYPE = 1150086;
  NIDIGITAL_ATTRIBUTE_DIGITAL_EDGE_RIO_TRIGGER_SOURCE = 1150087;
  NIDIGITAL_ATTRIBUTE_DIGITAL_EDGE_RIO_TRIGGER_EDGE = 1150088;
  NIDIGITAL_ATTRIBUTE_RIO_TRIGGER_TERMINAL_NAME = 1150089;
  NIDIGITAL_ATTRIBUTE_EXPORTED_RIO_EVENT_OUTPUT_TERMINAL = 1150090;
  NIDIGITAL_ATTRIBUTE_RIO_EVENT_TERMINAL_NAME = 1150091;
}

enum BitOrder {
  BIT_ORDER_UNSPECIFIED = 0;
  BIT_ORDER_NIDIGITAL_VAL_MSB_FIRST = 2500;
  BIT_ORDER_NIDIGITAL_VAL_LSB_FIRST = 2501;
}

enum DigitalEdge {
  DIGITAL_EDGE_UNSPECIFIED = 0;
  DIGITAL_EDGE_NIDIGITAL_VAL_RISING_EDGE = 1800;
  DIGITAL_EDGE_NIDIGITAL_VAL_FALLING_EDGE = 1801;
}

enum DriveFormat {
  DRIVE_FORMAT_UNSPECIFIED = 0;
  DRIVE_FORMAT_NIDIGITAL_VAL_NR = 1500;
  DRIVE_FORMAT_NIDIGITAL_VAL_RL = 1501;
  DRIVE_FORMAT_NIDIGITAL_VAL_RH = 1502;
  DRIVE_FORMAT_NIDIGITAL_VAL_SBC = 1503;
}

enum ExportSignal {
  EXPORT_SIGNAL_UNSPECIFIED = 0;
  EXPORT_SIGNAL_NIDIGITAL_VAL_START_TRIGGER = 2000;
  EXPORT_SIGNAL_NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER = 2001;
  EXPORT_SIGNAL_NIDIGITAL_VAL_PATTERN_OPCODE_EVENT = 2002;
  EXPORT_SIGNAL_NIDIGITAL_VAL_REF_CLOCK = 2003;
  EXPORT_SIGNAL_NIDIGITAL_VAL_RIO_EVENT = 2004;
}

enum FrequencyMeasurementMode {
  FREQUENCY_MEASUREMENT_MODE_UNSPECIFIED = 0;
  FREQUENCY_MEASUREMENT_MODE_NIDIGITAL_VAL_BANKED = 3700;
  FREQUENCY_MEASUREMENT_MODE_NIDIGITAL_VAL_PARALLEL = 3701;
}

enum HistoryRamCyclesToAcquire {
  HISTORY_RAM_CYCLES_TO_ACQUIRE_UNSPECIFIED = 0;
  HISTORY_RAM_CYCLES_TO_ACQUIRE_NIDIGITAL_VAL_FAILED_CYCLES = 2303;
  HISTORY_RAM_CYCLES_TO_ACQUIRE_NIDIGITAL_VAL_ALL_CYCLES = 2304;
}

enum NiDigitalInt32AttributeValues {
  NIDIGITAL_INT32_UNSPECIFIED = 0;
  NIDIGITAL_INT32_DIGITAL_EDGE_VAL_RISING_EDGE = 1800;
  NIDIGITAL_INT32_DIGITAL_EDGE_VAL_FALLING_EDGE = 1801;
  NIDIGITAL_INT32_FREQUENCY_MEASUREMENT_MODE_VAL_BANKED = 3700;
  NIDIGITAL_INT32_FREQUENCY_MEASUREMENT_MODE_VAL_PARALLEL = 3701;
  NIDIGITAL_INT32_HISTORY_RAM_CYCLES_TO_ACQUIRE_VAL_FAILED_CYCLES = 2303;
  NIDIGITAL_INT32_HISTORY_RAM_CYCLES_TO_ACQUIRE_VAL_ALL_CYCLES = 2304;
  NIDIGITAL_INT32_HISTORY_RAM_MAX_SAMPLES_TO_ACQUIRE_PER_SITE_VAL_ACQUIRE_ALL_SAMPLES = -1;
  NIDIGITAL_INT32_HISTORY_RAM_TRIGGER_TYPE_VAL_FIRST_FAILURE = 2200;
  NIDIGITAL_INT32_HISTORY_RAM_TRIGGER_TYPE_VAL_CYCLE_NUMBER = 2201;
  NIDIGITAL_INT32_HISTORY_RAM_TRIGGER_TYPE_VAL_PATTERN_LABEL = 2202;
  NIDIGITAL_INT32_PPMU_APERTURE_TIME_UNITS_VAL_SECONDS = 2100;
  NIDIGITAL_INT32_PPMU_CURRENT_LIMIT_BEHAVIOR_VAL_CURRENT_REGULATE = 3100;
  NIDIGITAL_INT32_PPMU_OUTPUT_FUNCTION_VAL_DC_VOLTAGE = 1300;
  NIDIGITAL_INT32_PPMU_OUTPUT_FUNCTION_VAL_DC_CURRENT = 1301;
  NIDIGITAL_INT32_SELECTED_FUNCTION_VAL_DIGITAL = 1100;
  NIDIGITAL_INT32_SELECTED_FUNCTION_VAL_PPMU = 1101;
  NIDIGITAL_INT32_SELECTED_FUNCTION_VAL_OFF = 1102;
  NIDIGITAL_INT32_SELECTED_FUNCTION_VAL_DISCONNECT = 1103;
  NIDIGITAL_INT32_SELECTED_FUNCTION_VAL_RIO = 1104;
  NIDIGITAL_INT32_TDR_ENDPOINT_TERMINATION_VAL_TDR_TO_OPEN = 3600;
  NIDIGITAL_INT32_TDR_ENDPOINT_TERMINATION_VAL_TDR_TO_SHORT_TO_GROUND = 3601;
  NIDIGITAL_INT32_TERMINATION_MODE_VAL_ACTIVE_LOAD = 1200;
  NIDIGITAL_INT32_TERMINATION_MODE_VAL_VTERM = 1201;
  NIDIGITAL_INT32_TERMINATION_MODE_VAL_HIGH_Z = 1202;
  NIDIGITAL_INT32_TRIGGER_TYPE_VAL_NONE = 1700;
  NIDIGITAL_INT32_TRIGGER_TYPE_VAL_DIGITAL_EDGE = 1701;
  NIDIGITAL_INT32_TRIGGER_TYPE_VAL_SOFTWARE = 1702;
}

enum PinState {
  PIN_STATE_NIDIGITAL_VAL_0 = 0;
  PIN_STATE_NIDIGITAL_VAL_1 = 1;
  PIN_STATE_NIDIGITAL_VAL_L = 3;
  PIN_STATE_NIDIGITAL_VAL_H = 4;
  PIN_STATE_NIDIGITAL_VAL_X = 5;
  PIN_STATE_NIDIGITAL_VAL_M = 6;
  PIN_STATE_NIDIGITAL_VAL_V = 7;
  PIN_STATE_NIDIGITAL_VAL_D = 8;
  PIN_STATE_NIDIGITAL_VAL_E = 9;
  PIN_STATE_NIDIGITAL_VAL_NOT_A_PIN_STATE = 254;
  PIN_STATE_NIDIGITAL_VAL_PIN_STATE_NOT_ACQUIRED = 255;
}

enum PpmuApertureTimeUnits {
  PPMU_APERTURE_TIME_UNITS_UNSPECIFIED = 0;
  PPMU_APERTURE_TIME_UNITS_NIDIGITAL_VAL_SECONDS = 2100;
}

enum PpmuCurrentLimitBehavior {
  PPMU_CURRENT_LIMIT_BEHAVIOR_UNSPECIFIED = 0;
  PPMU_CURRENT_LIMIT_BEHAVIOR_NIDIGITAL_VAL_CURRENT_REGULATE = 3100;
}

enum PpmuMeasurementType {
  PPMU_MEASUREMENT_TYPE_UNSPECIFIED = 0;
  PPMU_MEASUREMENT_TYPE_NIDIGITAL_VAL_MEASURE_CURRENT = 2400;
  PPMU_MEASUREMENT_TYPE_NIDIGITAL_VAL_MEASURE_VOLTAGE = 2401;
}

enum PpmuOutputFunction {
  PPMU_OUTPUT_FUNCTION_UNSPECIFIED = 0;
  PPMU_OUTPUT_FUNCTION_NIDIGITAL_VAL_DC_VOLTAGE = 1300;
  PPMU_OUTPUT_FUNCTION_NIDIGITAL_VAL_DC_CURRENT = 1301;
}

enum SelectedFunction {
  SELECTED_FUNCTION_UNSPECIFIED = 0;
  SELECTED_FUNCTION_NIDIGITAL_VAL_DIGITAL = 1100;
  SELECTED_FUNCTION_NIDIGITAL_VAL_PPMU = 1101;
  SELECTED_FUNCTION_NIDIGITAL_VAL_OFF = 1102;
  SELECTED_FUNCTION_NIDIGITAL_VAL_DISCONNECT = 1103;
  SELECTED_FUNCTION_NIDIGITAL_VAL_RIO = 1104;
}

enum SiteResultType {
  SITE_RESULT_TYPE_UNSPECIFIED = 0;
  SITE_RESULT_TYPE_NIDIGITAL_VAL_PASS_FAIL = 3300;
  SITE_RESULT_TYPE_NIDIGITAL_VAL_CAPTURE_WAVEFORM = 3301;
}

enum SoftwareTrigger {
  SOFTWARE_TRIGGER_UNSPECIFIED = 0;
  SOFTWARE_TRIGGER_NIDIGITAL_VAL_START_TRIGGER = 2000;
  SOFTWARE_TRIGGER_NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER = 2001;
}

enum SourceDataMapping {
  SOURCE_DATA_MAPPING_UNSPECIFIED = 0;
  SOURCE_DATA_MAPPING_NIDIGITAL_VAL_BROADCAST = 2600;
  SOURCE_DATA_MAPPING_NIDIGITAL_VAL_SITE_UNIQUE = 2601;
}

enum TerminationMode {
  TERMINATION_MODE_UNSPECIFIED = 0;
  TERMINATION_MODE_NIDIGITAL_VAL_ACTIVE_LOAD = 1200;
  TERMINATION_MODE_NIDIGITAL_VAL_VTERM = 1201;
  TERMINATION_MODE_NIDIGITAL_VAL_HIGH_Z = 1202;
}

enum TimeSetEdgeType {
  TIME_SET_EDGE_TYPE_UNSPECIFIED = 0;
  TIME_SET_EDGE_TYPE_NIDIGITAL_VAL_DRIVE_ON = 2800;
  TIME_SET_EDGE_TYPE_NIDIGITAL_VAL_DRIVE_DATA = 2801;
  TIME_SET_EDGE_TYPE_NIDIGITAL_VAL_DRIVE_RETURN = 2802;
  TIME_SET_EDGE_TYPE_NIDIGITAL_VAL_DRIVE_OFF = 2803;
  TIME_SET_EDGE_TYPE_NIDIGITAL_VAL_COMPARE_STROBE = 2804;
  TIME_SET_EDGE_TYPE_NIDIGITAL_VAL_DRIVE_DATA2 = 2805;
  TIME_SET_EDGE_TYPE_NIDIGITAL_VAL_DRIVE_RETURN2 = 2806;
  TIME_SET_EDGE_TYPE_NIDIGITAL_VAL_COMPARE_STROBE2 = 2807;
}

enum WriteStaticPinState {
  WRITE_STATIC_PIN_STATE_NIDIGITAL_VAL_0 = 0;
  WRITE_STATIC_PIN_STATE_NIDIGITAL_VAL_1 = 1;
  WRITE_STATIC_PIN_STATE_NIDIGITAL_VAL_X = 5;
}

message AbortRequest {
  nidevice_grpc.Session vi = 1;
}

message AbortResponse {
  int32 status = 1;
}

message AbortKeepAliveRequest {
  nidevice_grpc.Session vi = 1;
}

message AbortKeepAliveResponse {
  int32 status = 1;
}

message ApplyLevelsAndTimingRequest {
  nidevice_grpc.Session vi = 1;
  string site_list = 2;
  string levels_sheet = 3;
  string timing_sheet = 4;
  string initial_state_high_pins = 5;
  string initial_state_low_pins = 6;
  string initial_state_tristate_pins = 7;
}

message ApplyLevelsAndTimingResponse {
  int32 status = 1;
}

message ApplyTDROffsetsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  repeated double offsets = 3;
}

message ApplyTDROffsetsResponse {
  int32 status = 1;
}

message BurstPatternRequest {
  nidevice_grpc.Session vi = 1;
  string site_list = 2;
  string start_label = 3;
  bool select_digital_function = 4;
  bool wait_until_done = 5;
  double timeout = 6;
}

message BurstPatternResponse {
  int32 status = 1;
}

message BurstPatternSynchronizedRequest {
  uint32 session_count = 1;
  repeated nidevice_grpc.Session sessions = 2;
  string site_list = 3;
  string start_label = 4;
  bool select_digital_function = 5;
  bool wait_until_done = 6;
  double timeout = 7;
}

message BurstPatternSynchronizedResponse {
  int32 status = 1;
}

message ClearErrorRequest {
  nidevice_grpc.Session vi = 1;
}

message ClearErrorResponse {
  int32 status = 1;
}

message ClockGeneratorAbortRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
}

message ClockGeneratorAbortResponse {
  int32 status = 1;
}

message ClockGeneratorGenerateClockRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double frequency = 3;
  bool select_digital_function = 4;
}

message ClockGeneratorGenerateClockResponse {
  int32 status = 1;
}

message ClockGeneratorInitiateRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
}

message ClockGeneratorInitiateResponse {
  int32 status = 1;
}

message CloseRequest {
  nidevice_grpc.Session vi = 1;
}

message CloseResponse {
  int32 status = 1;
}

message CommitRequest {
  nidevice_grpc.Session vi = 1;
}

message CommitResponse {
  int32 status = 1;
}

message ConfigureActiveLoadLevelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double iol = 3;
  double ioh = 4;
  double vcom = 5;
}

message ConfigureActiveLoadLevelsResponse {
  int32 status = 1;
}

message ConfigureCycleNumberHistoryRAMTriggerRequest {
  nidevice_grpc.Session vi = 1;
  int64 cycle_number = 2;
  sint32 pretrigger_samples = 3;
}

message ConfigureCycleNumberHistoryRAMTriggerResponse {
  int32 status = 1;
}

message ConfigureDigitalEdgeConditionalJumpTriggerRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_identifier = 2;
  string source = 3;
  oneof edge_enum {
    DigitalEdge edge = 4;
    sint32 edge_raw = 5;
  }
}

message ConfigureDigitalEdgeConditionalJumpTriggerResponse {
  int32 status = 1;
}

message ConfigureDigitalEdgeStartTriggerRequest {
  nidevice_grpc.Session vi = 1;
  string source = 2;
  oneof edge_enum {
    DigitalEdge edge = 3;
    sint32 edge_raw = 4;
  }
}

message ConfigureDigitalEdgeStartTriggerResponse {
  int32 status = 1;
}

message ConfigureFirstFailureHistoryRAMTriggerRequest {
  nidevice_grpc.Session vi = 1;
  sint32 pretrigger_samples = 2;
}

message ConfigureFirstFailureHistoryRAMTriggerResponse {
  int32 status = 1;
}

message ConfigureHistoryRAMCyclesToAcquireRequest {
  nidevice_grpc.Session vi = 1;
  oneof cycles_to_acquire_enum {
    HistoryRamCyclesToAcquire cycles_to_acquire = 2;
    sint32 cycles_to_acquire_raw = 3;
  }
}

message ConfigureHistoryRAMCyclesToAcquireResponse {
  int32 status = 1;
}

message ConfigurePatternBurstSitesRequest {
  nidevice_grpc.Session vi = 1;
  string site_list = 2;
}

message ConfigurePatternBurstSitesResponse {
  int32 status = 1;
}

message ConfigurePatternLabelHistoryRAMTriggerRequest {
  nidevice_grpc.Session vi = 1;
  string label = 2;
  int64 vector_offset = 3;
  int64 cycle_offset = 4;
  sint32 pretrigger_samples = 5;
}

message ConfigurePatternLabelHistoryRAMTriggerResponse {
  int32 status = 1;
}

message ConfigureSoftwareEdgeConditionalJumpTriggerRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_identifier = 2;
}

message ConfigureSoftwareEdgeConditionalJumpTriggerResponse {
  int32 status = 1;
}

message ConfigureSoftwareEdgeStartTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message ConfigureSoftwareEdgeStartTriggerResponse {
  int32 status = 1;
}

message ConfigureStartLabelRequest {
  nidevice_grpc.Session vi = 1;
  string label = 2;
}

message ConfigureStartLabelResponse {
  int32 status = 1;
}

message ConfigureTerminationModeRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  oneof mode_enum {
    TerminationMode mode = 3;
    sint32 mode_raw = 4;
  }
}

message ConfigureTerminationModeResponse {
  int32 status = 1;
}

message ConfigureTimeSetCompareEdgesStrobeRequest {
  nidevice_grpc.Session vi = 1;
  string pin_list = 2;
  string time_set_name = 3;
  double strobe_edge = 4;
}

message ConfigureTimeSetCompareEdgesStrobeResponse {
  int32 status = 1;
}

message ConfigureTimeSetCompareEdgesStrobe2xRequest {
  nidevice_grpc.Session vi = 1;
  string pin_list = 2;
  string time_set_name = 3;
  double strobe_edge = 4;
  double strobe2_edge = 5;
}

message ConfigureTimeSetCompareEdgesStrobe2xResponse {
  int32 status = 1;
}

message ConfigureTimeSetDriveEdgesRequest {
  nidevice_grpc.Session vi = 1;
  string pin_list = 2;
  string time_set_name = 3;
  oneof format_enum {
    DriveFormat format = 4;
    sint32 format_raw = 5;
  }
  double drive_on_edge = 6;
  double drive_data_edge = 7;
  double drive_return_edge = 8;
  double drive_off_edge = 9;
}

message ConfigureTimeSetDriveEdgesResponse {
  int32 status = 1;
}

message ConfigureTimeSetDriveEdges2xRequest {
  nidevice_grpc.Session vi = 1;
  string pin_list = 2;
  string time_set_name = 3;
  oneof format_enum {
    DriveFormat format = 4;
    sint32 format_raw = 5;
  }
  double drive_on_edge = 6;
  double drive_data_edge = 7;
  double drive_return_edge = 8;
  double drive_off_edge = 9;
  double drive_data2_edge = 10;
  double drive_return2_edge = 11;
}

message ConfigureTimeSetDriveEdges2xResponse {
  int32 status = 1;
}

message ConfigureTimeSetDriveFormatRequest {
  nidevice_grpc.Session vi = 1;
  string pin_list = 2;
  string time_set_name = 3;
  oneof drive_format_enum {
    DriveFormat drive_format = 4;
    sint32 drive_format_raw = 5;
  }
}

message ConfigureTimeSetDriveFormatResponse {
  int32 status = 1;
}

message ConfigureTimeSetEdgeRequest {
  nidevice_grpc.Session vi = 1;
  string pin_list = 2;
  string time_set_name = 3;
  oneof edge_enum {
    TimeSetEdgeType edge = 4;
    sint32 edge_raw = 5;
  }
  double time = 6;
}

message ConfigureTimeSetEdgeResponse {
  int32 status = 1;
}

message ConfigureTimeSetEdgeMultiplierRequest {
  nidevice_grpc.Session vi = 1;
  string pin_list = 2;
  string time_set_name = 3;
  sint32 edge_multiplier = 4;
}

message ConfigureTimeSetEdgeMultiplierResponse {
  int32 status = 1;
}

message ConfigureTimeSetPeriodRequest {
  nidevice_grpc.Session vi = 1;
  string time_set_name = 2;
  double period = 3;
}

message ConfigureTimeSetPeriodResponse {
  int32 status = 1;
}

message ConfigureVoltageLevelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double vil = 3;
  double vih = 4;
  double vol = 5;
  double voh = 6;
  double vterm = 7;
}

message ConfigureVoltageLevelsResponse {
  int32 status = 1;
}

message CreateCaptureWaveformFromFileDigicaptureRequest {
  nidevice_grpc.Session vi = 1;
  string waveform_name = 2;
  string waveform_file_path = 3;
}

message CreateCaptureWaveformFromFileDigicaptureResponse {
  int32 status = 1;
}

message CreateCaptureWaveformParallelRequest {
  nidevice_grpc.Session vi = 1;
  string pin_list = 2;
  string waveform_name = 3;
}

message CreateCaptureWaveformParallelResponse {
  int32 status = 1;
}

message CreateCaptureWaveformSerialRequest {
  nidevice_grpc.Session vi = 1;
  string pin_list = 2;
  string waveform_name = 3;
  uint32 sample_width = 4;
  oneof bit_order_enum {
    BitOrder bit_order = 5;
    sint32 bit_order_raw = 6;
  }
}

message CreateCaptureWaveformSerialResponse {
  int32 status = 1;
}

message CreateChannelMapRequest {
  nidevice_grpc.Session vi = 1;
  sint32 num_sites = 2;
}

message CreateChannelMapResponse {
  int32 status = 1;
}

message CreatePinGroupRequest {
  nidevice_grpc.Session vi = 1;
  string pin_group_name = 2;
  string pin_list = 3;
}

message CreatePinGroupResponse {
  int32 status = 1;
}

message CreatePinMapRequest {
  nidevice_grpc.Session vi = 1;
  string dut_pin_list = 2;
  string system_pin_list = 3;
}

message CreatePinMapResponse {
  int32 status = 1;
}

message CreateSourceWaveformFromFileTDMSRequest {
  nidevice_grpc.Session vi = 1;
  string waveform_name = 2;
  string waveform_file_path = 3;
  bool write_waveform_data = 4;
}

message CreateSourceWaveformFromFileTDMSResponse {
  int32 status = 1;
}

message CreateSourceWaveformParallelRequest {
  nidevice_grpc.Session vi = 1;
  string pin_list = 2;
  string waveform_name = 3;
  oneof data_mapping_enum {
    SourceDataMapping data_mapping = 4;
    sint32 data_mapping_raw = 5;
  }
}

message CreateSourceWaveformParallelResponse {
  int32 status = 1;
}

message CreateSourceWaveformSerialRequest {
  nidevice_grpc.Session vi = 1;
  string pin_list = 2;
  string waveform_name = 3;
  oneof data_mapping_enum {
    SourceDataMapping data_mapping = 4;
    sint32 data_mapping_raw = 5;
  }
  uint32 sample_width = 6;
  oneof bit_order_enum {
    BitOrder bit_order = 7;
    sint32 bit_order_raw = 8;
  }
}

message CreateSourceWaveformSerialResponse {
  int32 status = 1;
}

message CreateTimeSetRequest {
  nidevice_grpc.Session vi = 1;
  string name = 2;
}

message CreateTimeSetResponse {
  int32 status = 1;
}

message DeleteAllTimeSetsRequest {
  nidevice_grpc.Session vi = 1;
}

message DeleteAllTimeSetsResponse {
  int32 status = 1;
}

message DisableConditionalJumpTriggerRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_identifier = 2;
}

message DisableConditionalJumpTriggerResponse {
  int32 status = 1;
}

message DisableSitesRequest {
  nidevice_grpc.Session vi = 1;
  string site_list = 2;
}

message DisableSitesResponse {
  int32 status = 1;
}

message DisableStartTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message DisableStartTriggerResponse {
  int32 status = 1;
}

message EnableMatchFailCombinationRequest {
  uint32 session_count = 1;
  repeated nidevice_grpc.Session sessions = 2;
  nidevice_grpc.Session sync_session = 3;
}

message EnableMatchFailCombinationResponse {
  int32 status = 1;
}

message EnableSitesRequest {
  nidevice_grpc.Session vi = 1;
  string site_list = 2;
}

message EnableSitesResponse {
  int32 status = 1;
}

message EndChannelMapRequest {
  nidevice_grpc.Session vi = 1;
}

message EndChannelMapResponse {
  int32 status = 1;
}

message ErrorMessageRequest {
  nidevice_grpc.Session vi = 1;
  sint32 error_code = 2;
}

message ErrorMessageResponse {
  int32 status = 1;
  string error_message = 2;
}

message ExportSignalRequest {
  nidevice_grpc.Session vi = 1;
  oneof signal_enum {
    ExportSignal signal = 2;
    sint32 signal_raw = 3;
  }
  string signal_identifier = 4;
  string output_terminal = 5;
}

message ExportSignalResponse {
  int32 status = 1;
}

message FetchCaptureWaveformU32Request {
  nidevice_grpc.Session vi = 1;
  string site_list = 2;
  string waveform_name = 3;
  sint32 samples_to_read = 4;
  double timeout = 5;
}

message FetchCaptureWaveformU32Response {
  int32 status = 1;
  repeated uint32 data = 2;
  sint32 actual_num_waveforms = 3;
  sint32 actual_samples_per_waveform = 4;
}

message FetchHistoryRAMCycleInformationRequest {
  nidevice_grpc.Session vi = 1;
  string site = 2;
  int64 sample_index = 3;
}

message FetchHistoryRAMCycleInformationResponse {
  int32 status = 1;
  sint32 pattern_index = 2;
  sint32 time_set_index = 3;
  int64 vector_number = 4;
  int64 cycle_number = 5;
  sint32 num_dut_cycles = 6;
}

message FetchHistoryRAMCyclePinDataRequest {
  nidevice_grpc.Session vi = 1;
  string site = 2;
  string pin_list = 3;
  int64 sample_index = 4;
  sint32 dut_cycle_index = 5;
}

message FetchHistoryRAMCyclePinDataResponse {
  int32 status = 1;
  repeated PinState expected_pin_states = 2;
  bytes expected_pin_states_raw = 3;
  repeated PinState actual_pin_states = 4;
  bytes actual_pin_states_raw = 5;
  repeated bool per_pin_pass_fail = 6;
  sint32 actual_num_pin_data = 7;
}

message FetchHistoryRAMScanCycleNumberRequest {
  nidevice_grpc.Session vi = 1;
  string site = 2;
  int64 sample_index = 3;
}

message FetchHistoryRAMScanCycleNumberResponse {
  int32 status = 1;
  int64 scan_cycle_number = 2;
}

message FrequencyCounterConfigureMeasurementModeRequest {
  nidevice_grpc.Session vi = 1;
  oneof measurement_mode_enum {
    FrequencyMeasurementMode measurement_mode = 2;
    sint32 measurement_mode_raw = 3;
  }
}

message FrequencyCounterConfigureMeasurementModeResponse {
  int32 status = 1;
}

message FrequencyCounterConfigureMeasurementTimeRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double measurement_time = 3;
}

message FrequencyCounterConfigureMeasurementTimeResponse {
  int32 status = 1;
}

message FrequencyCounterMeasureFrequencyRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
}

message FrequencyCounterMeasureFrequencyResponse {
  int32 status = 1;
  repeated double frequencies = 2;
  sint32 actual_num_frequencies = 3;
}

message GetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDigitalAttribute attribute = 3;
}

message GetAttributeViBooleanResponse {
  int32 status = 1;
  bool value = 2;
}

message GetAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDigitalAttribute attribute = 3;
}

message GetAttributeViInt32Response {
  int32 status = 1;
  sint32 value = 2;
}

message GetAttributeViInt64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDigitalAttribute attribute = 3;
}

message GetAttributeViInt64Response {
  int32 status = 1;
  int64 value = 2;
}

message GetAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDigitalAttribute attribute = 3;
}

message GetAttributeViReal64Response {
  int32 status = 1;
  double value = 2;
}

message GetAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiDigitalAttribute attribute = 3;
}

message GetAttributeViSessionResponse {
  int32 status = 1;
  nidevice_grpc.Session value = 2;
}

message GetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDigitalAttribute attribute = 3;
}

message GetAttributeViStringResponse {
  int32 status = 1;
  string value = 2;
}

message GetChannelNameRequest {
  nidevice_grpc.Session vi = 1;
  sint32 index = 2;
}

message GetChannelNameResponse {
  int32 status = 1;
  string name = 2;
}

message GetChannelNameFromStringRequest {
  nidevice_grpc.Session vi = 1;
  string indices = 2;
}

message GetChannelNameFromStringResponse {
  int32 status = 1;
  string names = 2;
}

message GetErrorRequest {
  nidevice_grpc.Session vi = 1;
}

message GetErrorResponse {
  int32 status = 1;
  sint32 error_code = 2;
  string error_description = 3;
}

message GetFailCountRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
}

message GetFailCountResponse {
  int32 status = 1;
  repeated int64 failure_count = 2;
  sint32 actual_num_read = 3;
}

message GetHistoryRAMSampleCountRequest {
  nidevice_grpc.Session vi = 1;
  string site = 2;
}

message GetHistoryRAMSampleCountResponse {
  int32 status = 1;
  int64 sample_count = 2;
}

message GetPatternNameRequest {
  nidevice_grpc.Session vi = 1;
  sint32 pattern_index = 2;
}

message GetPatternNameResponse {
  int32 status = 1;
  string name = 2;
}

message GetPatternPinIndexesRequest {
  nidevice_grpc.Session vi = 1;
  string start_label = 2;
}

message GetPatternPinIndexesResponse {
  int32 status = 1;
  repeated sint32 pin_indexes = 2;
  sint32 actual_num_pins = 3;
}

message GetPatternPinListRequest {
  nidevice_grpc.Session vi = 1;
  string start_label = 2;
}

message GetPatternPinListResponse {
  int32 status = 1;
  string pin_list = 2;
}

message GetPinNameRequest {
  nidevice_grpc.Session vi = 1;
  sint32 pin_index = 2;
}

message GetPinNameResponse {
  int32 status = 1;
  string name = 2;
}

message GetPinResultsPinInformationRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
}

message GetPinResultsPinInformationResponse {
  int32 status = 1;
  repeated sint32 pin_indexes = 2;
  repeated sint32 site_numbers = 3;
  repeated sint32 channel_indexes = 4;
  sint32 actual_num_values = 5;
}

message GetSitePassFailRequest {
  nidevice_grpc.Session vi = 1;
  string site_list = 2;
}

message GetSitePassFailResponse {
  int32 status = 1;
  repeated bool pass_fail = 2;
  sint32 actual_num_sites = 3;
}

message GetSiteResultsSiteNumbersRequest {
  nidevice_grpc.Session vi = 1;
  string site_list = 2;
  oneof site_result_type_enum {
    SiteResultType site_result_type = 3;
    sint32 site_result_type_raw = 4;
  }
}

message GetSiteResultsSiteNumbersResponse {
  int32 status = 1;
  repeated sint32 site_numbers = 2;
  sint32 actual_num_site_numbers = 3;
}

message GetTimeSetDriveFormatRequest {
  nidevice_grpc.Session vi = 1;
  string pin = 2;
  string time_set_name = 3;
}

message GetTimeSetDriveFormatResponse {
  int32 status = 1;
  DriveFormat format = 2;
  sint32 format_raw = 3;
}

message GetTimeSetEdgeRequest {
  nidevice_grpc.Session vi = 1;
  string pin = 2;
  string time_set_name = 3;
  oneof edge_enum {
    TimeSetEdgeType edge = 4;
    sint32 edge_raw = 5;
  }
}

message GetTimeSetEdgeResponse {
  int32 status = 1;
  double time = 2;
}

message GetTimeSetEdgeMultiplierRequest {
  nidevice_grpc.Session vi = 1;
  string pin = 2;
  string time_set_name = 3;
}

message GetTimeSetEdgeMultiplierResponse {
  int32 status = 1;
  sint32 edge_multiplier = 2;
}

message GetTimeSetNameRequest {
  nidevice_grpc.Session vi = 1;
  sint32 time_set_index = 2;
}

message GetTimeSetNameResponse {
  int32 status = 1;
  string name = 2;
}

message GetTimeSetPeriodRequest {
  nidevice_grpc.Session vi = 1;
  string time_set_name = 2;
}

message GetTimeSetPeriodResponse {
  int32 status = 1;
  double period = 2;
}

message InitRequest {
  string session_name = 1;
  string resource_name = 2;
  bool id_query = 3;
  bool reset_device = 4;
  nidevice_grpc.SessionInitializationBehavior initialization_behavior = 5;
}

message InitResponse {
  int32 status = 1;
  nidevice_grpc.Session vi = 2;
  string error_message = 3 [deprecated = true];
  bool new_session_initialized = 4;
}

message InitWithOptionsRequest {
  string session_name = 1;
  string resource_name = 2;
  bool id_query = 3;
  bool reset_device = 4;
  string option_string = 5;
  nidevice_grpc.SessionInitializationBehavior initialization_behavior = 6;
}

message InitWithOptionsResponse {
  int32 status = 1;
  nidevice_grpc.Session vi = 2;
  string error_message = 3 [deprecated = true];
  bool new_session_initialized = 4;
}

message InitiateRequest {
  nidevice_grpc.Session vi = 1;
}

message InitiateResponse {
  int32 status = 1;
}

message IsDoneRequest {
  nidevice_grpc.Session vi = 1;
}

message IsDoneResponse {
  int32 status = 1;
  bool done = 2;
}

message IsSiteEnabledRequest {
  nidevice_grpc.Session vi = 1;
  string site = 2;
}

message IsSiteEnabledResponse {
  int32 status = 1;
  bool enable = 2;
}

message LoadLevelsRequest {
  nidevice_grpc.Session vi = 1;
  string file_path = 2;
}

message LoadLevelsResponse {
  int32 status = 1;
}

message LoadPatternRequest {
  nidevice_grpc.Session vi = 1;
  string file_path = 2;
}

message LoadPatternResponse {
  int32 status = 1;
}

message LoadPinMapRequest {
  nidevice_grpc.Session vi = 1;
  string file_path = 2;
}

message LoadPinMapResponse {
  int32 status = 1;
}

message LoadSpecificationsRequest {
  nidevice_grpc.Session vi = 1;
  string file_path = 2;
}

message LoadSpecificationsResponse {
  int32 status = 1;
}

message LoadTimingRequest {
  nidevice_grpc.Session vi = 1;
  string file_path = 2;
}

message LoadTimingResponse {
  int32 status = 1;
}

message MapPinToChannelRequest {
  nidevice_grpc.Session vi = 1;
  string pin = 2;
  sint32 site = 3;
  string channel = 4;
}

message MapPinToChannelResponse {
  int32 status = 1;
}

message PPMUConfigureApertureTimeRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double aperture_time = 3;
  oneof units_enum {
    PpmuApertureTimeUnits units = 4;
    sint32 units_raw = 5;
  }
}

message PPMUConfigureApertureTimeResponse {
  int32 status = 1;
}

message PPMUConfigureCurrentLevelRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double current_level = 3;
}

message PPMUConfigureCurrentLevelResponse {
  int32 status = 1;
}

message PPMUConfigureCurrentLevelRangeRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double range = 3;
}

message PPMUConfigureCurrentLevelRangeResponse {
  int32 status = 1;
}

message PPMUConfigureCurrentLimitRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  oneof behavior_enum {
    PpmuCurrentLimitBehavior behavior = 3;
    sint32 behavior_raw = 4;
  }
  double limit = 5;
}

message PPMUConfigureCurrentLimitResponse {
  int32 status = 1;
}

message PPMUConfigureCurrentLimitRangeRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double range = 3;
}

message PPMUConfigureCurrentLimitRangeResponse {
  int32 status = 1;
}

message PPMUConfigureOutputFunctionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  oneof output_function_enum {
    PpmuOutputFunction output_function = 3;
    sint32 output_function_raw = 4;
  }
}

message PPMUConfigureOutputFunctionResponse {
  int32 status = 1;
}

message PPMUConfigureVoltageLevelRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double voltage_level = 3;
}

message PPMUConfigureVoltageLevelResponse {
  int32 status = 1;
}

message PPMUConfigureVoltageLimitsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double lower_voltage_limit = 3;
  double upper_voltage_limit = 4;
}

message PPMUConfigureVoltageLimitsResponse {
  int32 status = 1;
}

message PPMUMeasureRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  oneof measurement_type_enum {
    PpmuMeasurementType measurement_type = 3;
    sint32 measurement_type_raw = 4;
  }
}

message PPMUMeasureResponse {
  int32 status = 1;
  repeated double measurements = 2;
  sint32 actual_num_read = 3;
}

message PPMUSourceRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
}

message PPMUSourceResponse {
  int32 status = 1;
}

message ReadSequencerFlagRequest {
  nidevice_grpc.Session vi = 1;
  string flag = 2;
}

message ReadSequencerFlagResponse {
  int32 status = 1;
  bool value = 2;
}

message ReadSequencerRegisterRequest {
  nidevice_grpc.Session vi = 1;
  string reg = 2;
}

message ReadSequencerRegisterResponse {
  int32 status = 1;
  sint32 value = 2;
}

message ReadStaticRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
}

message ReadStaticResponse {
  int32 status = 1;
  repeated PinState data = 2;
  bytes data_raw = 3;
  sint32 actual_num_read = 4;
}

message ResetRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetResponse {
  int32 status = 1;
}

message ResetAttributeRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDigitalAttribute attribute_id = 3;
}

message ResetAttributeResponse {
  int32 status = 1;
}

message ResetDeviceRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetDeviceResponse {
  int32 status = 1;
}

message SelectFunctionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  oneof function_enum {
    SelectedFunction function = 3;
    sint32 function_raw = 4;
  }
}

message SelectFunctionResponse {
  int32 status = 1;
}

message SelfCalibrateRequest {
  nidevice_grpc.Session vi = 1;
}

message SelfCalibrateResponse {
  int32 status = 1;
}

message SelfTestRequest {
  nidevice_grpc.Session vi = 1;
}

message SelfTestResponse {
  int32 status = 1;
  sint32 test_result = 2;
  string test_message = 3;
}

message SendSoftwareEdgeTriggerRequest {
  nidevice_grpc.Session vi = 1;
  oneof trigger_enum {
    SoftwareTrigger trigger = 2;
    sint32 trigger_raw = 3;
  }
  string trigger_identifier = 4;
}

message SendSoftwareEdgeTriggerResponse {
  int32 status = 1;
}

message SetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDigitalAttribute attribute = 3;
  bool value = 4;
}

message SetAttributeViBooleanResponse {
  int32 status = 1;
}

message SetAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDigitalAttribute attribute = 3;
  oneof value_enum {
    NiDigitalInt32AttributeValues value = 4;
    sint32 value_raw = 5;
  }
}

message SetAttributeViInt32Response {
  int32 status = 1;
}

message SetAttributeViInt64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDigitalAttribute attribute = 3;
  int64 value_raw = 4;
}

message SetAttributeViInt64Response {
  int32 status = 1;
}

message SetAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDigitalAttribute attribute = 3;
  double value_raw = 4;
}

message SetAttributeViReal64Response {
  int32 status = 1;
}

message SetAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiDigitalAttribute attribute = 3;
  nidevice_grpc.Session value = 4;
}

message SetAttributeViSessionResponse {
  int32 status = 1;
}

message SetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDigitalAttribute attribute = 3;
  string value_raw = 4;
}

message SetAttributeViStringResponse {
  int32 status = 1;
}

message TDRRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  bool apply_offsets = 3;
}

message TDRResponse {
  int32 status = 1;
  repeated double offsets = 2;
  sint32 actual_num_offsets = 3;
}

message UnloadAllPatternsRequest {
  nidevice_grpc.Session vi = 1;
  bool unload_keep_alive_pattern = 2;
}

message UnloadAllPatternsResponse {
  int32 status = 1;
}

message UnloadSpecificationsRequest {
  nidevice_grpc.Session vi = 1;
  string file_path = 2;
}

message UnloadSpecificationsResponse {
  int32 status = 1;
}

message WaitUntilDoneRequest {
  nidevice_grpc.Session vi = 1;
  double timeout = 2;
}

message WaitUntilDoneResponse {
  int32 status = 1;
}

message WriteSequencerFlagRequest {
  nidevice_grpc.Session vi = 1;
  string flag = 2;
  bool value = 3;
}

message WriteSequencerFlagResponse {
  int32 status = 1;
}

message WriteSequencerFlagSynchronizedRequest {
  uint32 session_count = 1;
  repeated nidevice_grpc.Session sessions = 2;
  string flag = 3;
  bool value = 4;
}

message WriteSequencerFlagSynchronizedResponse {
  int32 status = 1;
}

message WriteSequencerRegisterRequest {
  nidevice_grpc.Session vi = 1;
  string reg = 2;
  sint32 value = 3;
}

message WriteSequencerRegisterResponse {
  int32 status = 1;
}

message WriteSourceWaveformBroadcastU32Request {
  nidevice_grpc.Session vi = 1;
  string waveform_name = 2;
  repeated uint32 waveform_data = 3;
}

message WriteSourceWaveformBroadcastU32Response {
  int32 status = 1;
}

message WriteSourceWaveformDataFromFileTDMSRequest {
  nidevice_grpc.Session vi = 1;
  string waveform_name = 2;
  string waveform_file_path = 3;
}

message WriteSourceWaveformDataFromFileTDMSResponse {
  int32 status = 1;
}

message WriteSourceWaveformSiteUniqueU32Request {
  nidevice_grpc.Session vi = 1;
  string site_list = 2;
  string waveform_name = 3;
  sint32 num_waveforms = 4;
  sint32 samples_per_waveform = 5;
  repeated uint32 waveform_data = 6;
}

message WriteSourceWaveformSiteUniqueU32Response {
  int32 status = 1;
}

message WriteStaticRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  oneof state_enum {
    WriteStaticPinState state = 3;
    uint32 state_raw = 4;
  }
}

message WriteStaticResponse {
  int32 status = 1;
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidigitalpattern/README.md sha256=c22aa3ce73c1a511a9f42eaff389302947b9712eb599bb5b844f43deb67d2ed3 bytes=212 -->
## FILE: source/codegen/metadata/nidigitalpattern/README.md

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidigitalpattern/README.md`
- sha256: `c22aa3ce73c1a511a9f42eaff389302947b9712eb599bb5b844f43deb67d2ed3`
- bytes: 212

````markdown
# Updating

To update this metadata folder. Find the nidigital_grpc_device export and copy the contents of its metadata folder here.

# More info

Refer to source/codegen/metadata/Imported_From_Hapigen.md
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidmm/__init__.py sha256=3f3177b9bfb8b1928720894e2452fe8decbd6707df63967cc881e20a7f8fb45a bytes=589 -->
## FILE: source/codegen/metadata/nidmm/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidmm/__init__.py`
- sha256: `3f3177b9bfb8b1928720894e2452fe8decbd6707df63967cc881e20a7f8fb45a`
- bytes: 589

````python
from .functions import functions
from .functions_addon import functions_override_metadata
from .attributes import attributes
from .attributes_addon import attributes_override_metadata
from .enums import enums
from .enums_addon import enums_override_metadata
from .config import config

metadata = {
    "functions" : functions,
    "attributes" : attributes,
    "enums" : enums,
    "config" : config
}

metadata['functions'].update(functions_override_metadata)
metadata['attributes'].update(attributes_override_metadata)
metadata['enums'].update(enums_override_metadata)
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidmm/attributes.py sha256=68b68284ba6da1d21480d1d3d6d0b62e2795881172f5d6ad8f80114e13b0e6b7 bytes=17223 -->
## FILE: source/codegen/metadata/nidmm/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidmm/attributes.py`
- sha256: `68b68284ba6da1d21480d1d3d6d0b62e2795881172f5d6ad8f80114e13b0e6b7`
- bytes: 17223

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-DMM API metadata version 26.0.0d90
attributes = {
    1050002: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'RANGE_CHECK',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050003: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'QUERY_INSTRUMENT_STATUS',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050004: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'CACHE',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050005: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'SIMULATE',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050006: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'RECORD_COERCIONS',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050007: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'DRIVER_SETUP',
        'resettable': False,
        'type': 'ViString'
    },
    1050021: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'INTERCHANGE_CHECK',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050203: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'CHANNEL_COUNT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050302: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SPECIFIC_DRIVER_PREFIX',
        'resettable': False,
        'type': 'ViString'
    },
    1050304: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'resettable': False,
        'type': 'ViString'
    },
    1050305: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'LOGICAL_NAME',
        'resettable': False,
        'type': 'ViString'
    },
    1050322: {
        'codegen_method': 'public',
        'grpc_type': 'nidevice_grpc.Session',
        'name': 'IO_SESSION',
        'resettable': False,
        'type': 'ViSession'
    },
    1050327: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'resettable': False,
        'type': 'ViString'
    },
    1050401: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'GROUP_CAPABILITIES',
        'resettable': False,
        'type': 'ViString'
    },
    1050510: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'resettable': False,
        'type': 'ViString'
    },
    1050511: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'INSTRUMENT_MANUFACTURER',
        'resettable': False,
        'type': 'ViString'
    },
    1050512: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'INSTRUMENT_MODEL',
        'resettable': False,
        'type': 'ViString'
    },
    1050513: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'resettable': False,
        'type': 'ViString'
    },
    1050514: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SPECIFIC_DRIVER_DESCRIPTION',
        'resettable': False,
        'type': 'ViString'
    },
    1050515: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050516: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050519: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050520: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050551: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SPECIFIC_DRIVER_REVISION',
        'resettable': False,
        'type': 'ViString'
    },
    1150002: {
        'codegen_method': 'public',
        'enum': 'MeasurementDestinationSlope',
        'grpc_type': 'sint32',
        'name': 'MEAS_DEST_SLOPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150003: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'SHUNT_VALUE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150010: {
        'codegen_method': 'public',
        'enum': 'SampleTrigSlope',
        'grpc_type': 'sint32',
        'name': 'SAMPLE_TRIGGER_SLOPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150014: {
        'codegen_method': 'public',
        'enum': 'OperationMode',
        'grpc_type': 'sint32',
        'name': 'OPERATION_MODE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150018: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'WAVEFORM_RATE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150019: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'WAVEFORM_POINTS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150022: {
        'codegen_method': 'public',
        'enum': 'AdcCalibration',
        'grpc_type': 'sint32',
        'name': 'ADC_CALIBRATION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150023: {
        'codegen_method': 'public',
        'enum': 'CompensatedOhms',
        'grpc_type': 'sint32',
        'name': 'OFFSET_COMP_OHMS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150025: {
        'codegen_method': 'public',
        'enum': 'CurrentSource',
        'grpc_type': 'double',
        'name': 'CURRENT_SOURCE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150026: {
        'codegen_method': 'public',
        'enum': 'DcNoiseRejection',
        'grpc_type': 'sint32',
        'name': 'DC_NOISE_REJECTION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150027: {
        'codegen_method': 'public',
        'enum': 'WaveformCoupling',
        'grpc_type': 'sint32',
        'name': 'WAVEFORM_COUPLING',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150028: {
        'codegen_method': 'public',
        'enum': 'SettleTime',
        'grpc_type': 'double',
        'name': 'SETTLE_TIME',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150029: {
        'codegen_method': 'public',
        'enum': 'InputResistance',
        'grpc_type': 'double',
        'name': 'INPUT_RESISTANCE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150032: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'NUMBER_OF_AVERAGES',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150034: {
        'codegen_method': 'public',
        'enum': 'Latency',
        'grpc_type': 'sint32',
        'name': 'LATENCY',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150037: {
        'codegen_method': 'public',
        'enum': 'BufferSize',
        'grpc_type': 'sint32',
        'name': 'BUFFER_SIZE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150044: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'FREQ_VOLTAGE_AUTO_RANGE_VALUE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150045: {
        'codegen_method': 'public',
        'enum': 'CableCompensationType',
        'grpc_type': 'sint32',
        'name': 'CABLE_COMP_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150046: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'SHORT_CABLE_COMP_REACTANCE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150047: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'SHORT_CABLE_COMP_RESISTANCE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150048: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OPEN_CABLE_COMP_SUSCEPTANCE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150049: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OPEN_CABLE_COMP_CONDUCTANCE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150052: {
        'codegen_method': 'public',
        'enum': 'LcCalculationModel',
        'grpc_type': 'sint32',
        'name': 'LC_CALCULATION_MODEL',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150053: {
        'codegen_method': 'public',
        'enum': 'DcBias',
        'grpc_type': 'sint32',
        'name': 'DC_BIAS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150054: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SERIAL_NUMBER',
        'resettable': False,
        'type': 'ViString'
    },
    1150055: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'LC_NUMBER_MEAS_TO_AVERAGE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150061: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'CONFIG_PRODUCT_NUMBER',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150120: {
        'codegen_method': 'public',
        'enum': 'RtdType',
        'grpc_type': 'sint32',
        'name': 'TEMP_RTD_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150121: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'TEMP_RTD_A',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150122: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'TEMP_RTD_B',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150123: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'TEMP_RTD_C',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150124: {
        'codegen_method': 'public',
        'enum': 'ThermistorType',
        'grpc_type': 'sint32',
        'name': 'TEMP_THERMISTOR_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150125: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'TEMP_THERMISTOR_A',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150126: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'TEMP_THERMISTOR_B',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150127: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'TEMP_THERMISTOR_C',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250001: {
        'codegen_method': 'public',
        'enum': 'Function',
        'grpc_type': 'sint32',
        'name': 'FUNCTION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250002: {
        'codegen_method': 'public',
        'enum': 'Range',
        'grpc_type': 'double',
        'name': 'RANGE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250003: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'RESOLUTION_DIGITS',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250004: {
        'codegen_method': 'public',
        'enum': 'TriggerSource',
        'grpc_type': 'sint32',
        'name': 'TRIGGER_SOURCE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250005: {
        'codegen_method': 'public',
        'enum': 'TriggerDelays',
        'grpc_type': 'double',
        'name': 'TRIGGER_DELAY',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250006: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'AC_MIN_FREQ',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250007: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'AC_MAX_FREQ',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250008: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'RESOLUTION_ABSOLUTE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250101: {
        'codegen_method': 'public',
        'enum': 'FrequencyVoltageRange',
        'grpc_type': 'double',
        'name': 'FREQ_VOLTAGE_RANGE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250201: {
        'codegen_method': 'public',
        'enum': 'TransducerType',
        'grpc_type': 'sint32',
        'name': 'TEMP_TRANSDUCER_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250231: {
        'codegen_method': 'public',
        'enum': 'ThermocoupleType',
        'grpc_type': 'sint32',
        'name': 'TEMP_TC_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250232: {
        'codegen_method': 'public',
        'enum': 'ThermocoupleReferenceJunctionType',
        'grpc_type': 'sint32',
        'name': 'TEMP_TC_REF_JUNC_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250233: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'TEMP_TC_FIXED_REF_JUNC',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250242: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'TEMP_RTD_RES',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250301: {
        'codegen_method': 'public',
        'enum': 'SampleCount',
        'grpc_type': 'sint32',
        'name': 'SAMPLE_COUNT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250302: {
        'codegen_method': 'public',
        'enum': 'SampleTrigger',
        'grpc_type': 'sint32',
        'name': 'SAMPLE_TRIGGER',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250303: {
        'codegen_method': 'public',
        'enum': 'SampleInterval',
        'grpc_type': 'double',
        'name': 'SAMPLE_INTERVAL',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250304: {
        'codegen_method': 'public',
        'enum': 'TriggerCount',
        'grpc_type': 'sint32',
        'name': 'TRIGGER_COUNT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250305: {
        'codegen_method': 'public',
        'enum': 'MeasurementCompleteDest',
        'grpc_type': 'sint32',
        'name': 'MEAS_COMPLETE_DEST',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250321: {
        'codegen_method': 'public',
        'enum': 'ApertureTime',
        'grpc_type': 'double',
        'name': 'APERTURE_TIME',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250322: {
        'codegen_method': 'public',
        'enum': 'ApertureTimeUnits',
        'grpc_type': 'sint32',
        'name': 'APERTURE_TIME_UNITS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250331: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'AUTO_RANGE_VALUE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250332: {
        'codegen_method': 'public',
        'enum': 'AutoZero',
        'grpc_type': 'sint32',
        'name': 'AUTO_ZERO',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250333: {
        'codegen_method': 'public',
        'enum': 'PowerLineFrequencies',
        'grpc_type': 'double',
        'name': 'POWERLINE_FREQ',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250334: {
        'codegen_method': 'public',
        'enum': 'TriggerSlope',
        'grpc_type': 'sint32',
        'name': 'TRIGGER_SLOPE',
        'resettable': False,
        'type': 'ViInt32'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidmm/attributes_addon.py sha256=cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f bytes=207 -->
## FILE: source/codegen/metadata/nidmm/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidmm/attributes_addon.py`
- sha256: `cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f`
- bytes: 207

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidmm/config.py sha256=f2136c1ffc1c1ac238c372ac5ac127de8b83cf066bbb951b24e1aa71304b230f bytes=1144 -->
## FILE: source/codegen/metadata/nidmm/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidmm/config.py`
- sha256: `f2136c1ffc1c1ac238c372ac5ac127de8b83cf066bbb951b24e1aa71304b230f`
- bytes: 1144

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-DMM API metadata version 26.0.0d90
config = {
    'additional_headers': {
        'custom/ivi_errors.h': [
            'service.cpp'
        ]
    },
    'api_version': '26.0.0d90',
    'c_function_prefix': 'niDMM_',
    'c_header': 'nidmm.h',
    'close_function': 'Close',
    'csharp_namespace': 'NationalInstruments.Grpc.Dmm',
    'custom_types': [
    ],
    'driver_name': 'NI-DMM',
    'java_package': 'com.ni.grpc.dmm',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nidmm',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'nidmm_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'nidmm_64.dll',
                'type': 'cdll'
            }
        }
    },
    'linux_rt_support': True,
    'module_name': 'nidmm',
    'namespace_component': 'nidmm',
    'service_class_prefix': 'NiDmm',
    'session_handle_parameter_name': 'vi',
    'status_ok': 'status >= 0'
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidmm/config_addon.py sha256=e1412555b082de48219c38a9909c95c4479751fa77895b6c7fdd61b9f2485186 bytes=226 -->
## FILE: source/codegen/metadata/nidmm/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidmm/config_addon.py`
- sha256: `e1412555b082de48219c38a9909c95c4479751fa77895b6c7fdd61b9f2485186`
- bytes: 226

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.4.dev0',
    'latest_runtime_version_tested_against': '20.5.0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidmm/enums.py sha256=20ea12908e3a5b68213ee2c0db0789041f4e484dccc1bea9fe0ed407e6fd1ec5 bytes=39199 -->
## FILE: source/codegen/metadata/nidmm/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidmm/enums.py`
- sha256: `20ea12908e3a5b68213ee2c0db0789041f4e484dccc1bea9fe0ed407e6fd1ec5`
- bytes: 39199

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-DMM API metadata version 26.0.0d90
enums = {
    'AcquisitionStatus': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_RUNNING_ANTICOLLISION',
                'value': 0
            },
            {
                'name': 'NIDMM_VAL_FINISHED_WITH_BACKLOG',
                'value': 1
            },
            {
                'name': 'NIDMM_VAL_FINISHED_WITH_NO_BACKLOG',
                'value': 2
            },
            {
                'name': 'NIDMM_VAL_PAUSED',
                'value': 3
            },
            {
                'name': 'NIDMM_VAL_NO_ACQUISITION_IN_PROGRESS',
                'value': 4
            }
        ]
    },
    'AdcCalibration': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_ADC_CALIBRATION_OFF',
                'value': 0
            },
            {
                'name': 'NIDMM_VAL_ADC_CALIBRATION_AUTO',
                'value': -1
            },
            {
                'name': 'NIDMM_VAL_ADC_CALIBRATION_ON',
                'value': 1
            }
        ]
    },
    'ApertureTime': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_APERTURE_TIME_AUTO',
                'value': -1
            },
            {
                'name': 'NIDMM_VAL_1_PLC',
                'value': 1
            },
            {
                'name': 'NIDMM_VAL_5_PLC',
                'value': 5
            },
            {
                'name': 'NIDMM_VAL_6_PLC',
                'value': 6
            },
            {
                'name': 'NIDMM_VAL_10_PLC',
                'value': 10
            },
            {
                'name': 'NIDMM_VAL_12_PLC',
                'value': 12
            },
            {
                'name': 'NIDMM_VAL_100_PLC',
                'value': 100
            },
            {
                'name': 'NIDMM_VAL_120_PLC',
                'value': 120
            }
        ]
    },
    'ApertureTimeUnits': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_SECONDS',
                'value': 0
            },
            {
                'name': 'NIDMM_VAL_POWER_LINE_CYCLES',
                'value': 1
            }
        ]
    },
    'AutoZero': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_AUTO_ZERO_OFF',
                'value': 0
            },
            {
                'name': 'NIDMM_VAL_AUTO_ZERO_AUTO',
                'value': -1
            },
            {
                'name': 'NIDMM_VAL_AUTO_ZERO_ON',
                'value': 1
            },
            {
                'name': 'NIDMM_VAL_AUTO_ZERO_ONCE',
                'value': 2
            }
        ]
    },
    'BufferSize': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_BUFFER_SIZE_AUTO',
                'value': -1
            }
        ]
    },
    'CableCompensationType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_CABLE_COMP_NONE',
                'value': 0
            },
            {
                'name': 'NIDMM_VAL_CABLE_COMP_OPEN',
                'value': 1
            },
            {
                'name': 'NIDMM_VAL_CABLE_COMP_SHORT',
                'value': 2
            },
            {
                'name': 'NIDMM_VAL_CABLE_COMP_OPEN_AND_SHORT',
                'value': 3
            }
        ]
    },
    'CalibrationType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_INTERNAL_AREA',
                'value': 0
            },
            {
                'name': 'NIDMM_VAL_EXTERNAL_AREA',
                'value': 1
            }
        ]
    },
    'CompensatedOhms': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_OFFSET_COMP_OHMS_OFF',
                'value': 0
            },
            {
                'name': 'NIDMM_VAL_OFFSET_COMP_OHMS_ON',
                'value': 1
            }
        ]
    },
    'ControlCommit': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_CONTROL_COMMIT',
                'value': 0
            }
        ]
    },
    'CurrentSource': {
        'codegen_method': 'public',
        'generate-mappings': True,
        'values': [
            {
                'name': 'NIDMM_VAL_1_MICROAMP',
                'value': 1e-06
            },
            {
                'name': 'NIDMM_VAL_10_MICROAMP',
                'value': 1e-05
            },
            {
                'name': 'NIDMM_VAL_100_MICROAMP',
                'value': 0.0001
            },
            {
                'name': 'NIDMM_VAL_1_MILLIAMP',
                'value': 0.001
            }
        ]
    },
    'DcBias': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_DC_BIAS_OFF',
                'value': 0
            },
            {
                'name': 'NIDMM_VAL_DC_BIAS_ON',
                'value': 1
            }
        ]
    },
    'DcNoiseRejection': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_DCNR_NORMAL',
                'value': 0
            },
            {
                'name': 'NIDMM_VAL_DCNR_AUTO',
                'value': -1
            },
            {
                'name': 'NIDMM_VAL_DCNR_SECOND_ORDER',
                'value': 1
            },
            {
                'name': 'NIDMM_VAL_DCNR_HIGH_ORDER',
                'value': 2
            }
        ]
    },
    'FrequencyVoltageRange': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_AUTO_RANGE_ON',
                'value': -1
            },
            {
                'name': 'NIDMM_VAL_AUTO_RANGE_OFF',
                'value': -2
            }
        ]
    },
    'Function': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_DC_VOLTS',
                'value': 1
            },
            {
                'name': 'NIDMM_VAL_AC_VOLTS',
                'value': 2
            },
            {
                'name': 'NIDMM_VAL_DC_CURRENT',
                'value': 3
            },
            {
                'name': 'NIDMM_VAL_AC_CURRENT',
                'value': 4
            },
            {
                'name': 'NIDMM_VAL_2_WIRE_RES',
                'value': 5
            },
            {
                'name': 'NIDMM_VAL_4_WIRE_RES',
                'value': 101
            },
            {
                'name': 'NIDMM_VAL_FREQ',
                'value': 104
            },
            {
                'name': 'NIDMM_VAL_PERIOD',
                'value': 105
            },
            {
                'name': 'NIDMM_VAL_TEMPERATURE',
                'value': 108
            },
            {
                'name': 'NIDMM_VAL_AC_VOLTS_DC_COUPLED',
                'value': 1001
            },
            {
                'name': 'NIDMM_VAL_DIODE',
                'value': 1002
            },
            {
                'name': 'NIDMM_VAL_WAVEFORM_VOLTAGE',
                'value': 1003
            },
            {
                'name': 'NIDMM_VAL_WAVEFORM_CURRENT',
                'value': 1004
            },
            {
                'name': 'NIDMM_VAL_CAPACITANCE',
                'value': 1005
            },
            {
                'name': 'NIDMM_VAL_INDUCTANCE',
                'value': 1006
            }
        ]
    },
    'InputResistance': {
        'codegen_method': 'public',
        'generate-mappings': True,
        'values': [
            {
                'name': 'NIDMM_VAL_RESISTANCE_NA',
                'value': 0
            },
            {
                'name': 'NIDMM_VAL_1_MEGAOHM',
                'value': 1000000
            },
            {
                'name': 'NIDMM_VAL_10_MEGAOHM',
                'value': 10000000
            },
            {
                'name': 'NIDMM_VAL_GREATER_THAN_10_GIGAOHM',
                'value': 10000000000.0
            }
        ]
    },
    'Latency': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_LATENCY_AUTO',
                'value': -1
            }
        ]
    },
    'LcCalculationModel': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_CALC_MODEL_SERIES',
                'value': 0
            },
            {
                'name': 'NIDMM_VAL_CALC_MODEL_AUTO',
                'value': -1
            },
            {
                'name': 'NIDMM_VAL_CALC_MODEL_PARALLEL',
                'value': 1
            }
        ]
    },
    'MeasurementCompleteDest': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_NONE',
                'value': -1
            },
            {
                'name': 'NIDMM_VAL_EXTERNAL',
                'value': 2
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG0',
                'value': 111
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG1',
                'value': 112
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG2',
                'value': 113
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG3',
                'value': 114
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG4',
                'value': 115
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG5',
                'value': 116
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG6',
                'value': 117
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG7',
                'value': 118
            },
            {
                'name': 'NIDMM_VAL_LBR_TRIG0',
                'value': 1003
            }
        ]
    },
    'MeasurementDestinationSlope': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_POSITIVE',
                'value': 0
            },
            {
                'name': 'NIDMM_VAL_NEGATIVE',
                'value': 1
            }
        ]
    },
    'NiDmmInt32AttributeValues': {
        'enum-value-prefix': 'NIDMM_INT32',
        'generate-mappings': False,
        'values': [
            {
                'name': 'ADC_CALIBRATION_VAL_ADC_CALIBRATION_OFF',
                'value': 0
            },
            {
                'name': 'ADC_CALIBRATION_VAL_ADC_CALIBRATION_AUTO',
                'value': -1
            },
            {
                'name': 'ADC_CALIBRATION_VAL_ADC_CALIBRATION_ON',
                'value': 1
            },
            {
                'name': 'APERTURE_TIME_UNITS_VAL_SECONDS',
                'value': 0
            },
            {
                'name': 'APERTURE_TIME_UNITS_VAL_POWER_LINE_CYCLES',
                'value': 1
            },
            {
                'name': 'AUTO_ZERO_VAL_AUTO_ZERO_OFF',
                'value': 0
            },
            {
                'name': 'AUTO_ZERO_VAL_AUTO_ZERO_AUTO',
                'value': -1
            },
            {
                'name': 'AUTO_ZERO_VAL_AUTO_ZERO_ON',
                'value': 1
            },
            {
                'name': 'AUTO_ZERO_VAL_AUTO_ZERO_ONCE',
                'value': 2
            },
            {
                'name': 'BUFFER_SIZE_VAL_BUFFER_SIZE_AUTO',
                'value': -1
            },
            {
                'name': 'CABLE_COMPENSATION_TYPE_VAL_CABLE_COMP_NONE',
                'value': 0
            },
            {
                'name': 'CABLE_COMPENSATION_TYPE_VAL_CABLE_COMP_OPEN',
                'value': 1
            },
            {
                'name': 'CABLE_COMPENSATION_TYPE_VAL_CABLE_COMP_SHORT',
                'value': 2
            },
            {
                'name': 'CABLE_COMPENSATION_TYPE_VAL_CABLE_COMP_OPEN_AND_SHORT',
                'value': 3
            },
            {
                'name': 'COMPENSATED_OHMS_VAL_OFFSET_COMP_OHMS_OFF',
                'value': 0
            },
            {
                'name': 'COMPENSATED_OHMS_VAL_OFFSET_COMP_OHMS_ON',
                'value': 1
            },
            {
                'name': 'DC_BIAS_VAL_DC_BIAS_OFF',
                'value': 0
            },
            {
                'name': 'DC_BIAS_VAL_DC_BIAS_ON',
                'value': 1
            },
            {
                'name': 'DC_NOISE_REJECTION_VAL_DCNR_NORMAL',
                'value': 0
            },
            {
                'name': 'DC_NOISE_REJECTION_VAL_DCNR_AUTO',
                'value': -1
            },
            {
                'name': 'DC_NOISE_REJECTION_VAL_DCNR_SECOND_ORDER',
                'value': 1
            },
            {
                'name': 'DC_NOISE_REJECTION_VAL_DCNR_HIGH_ORDER',
                'value': 2
            },
            {
                'name': 'FUNCTION_VAL_DC_VOLTS',
                'value': 1
            },
            {
                'name': 'FUNCTION_VAL_AC_VOLTS',
                'value': 2
            },
            {
                'name': 'FUNCTION_VAL_DC_CURRENT',
                'value': 3
            },
            {
                'name': 'FUNCTION_VAL_AC_CURRENT',
                'value': 4
            },
            {
                'name': 'FUNCTION_VAL_2_WIRE_RES',
                'value': 5
            },
            {
                'name': 'FUNCTION_VAL_4_WIRE_RES',
                'value': 101
            },
            {
                'name': 'FUNCTION_VAL_FREQ',
                'value': 104
            },
            {
                'name': 'FUNCTION_VAL_PERIOD',
                'value': 105
            },
            {
                'name': 'FUNCTION_VAL_TEMPERATURE',
                'value': 108
            },
            {
                'name': 'FUNCTION_VAL_AC_VOLTS_DC_COUPLED',
                'value': 1001
            },
            {
                'name': 'FUNCTION_VAL_DIODE',
                'value': 1002
            },
            {
                'name': 'FUNCTION_VAL_WAVEFORM_VOLTAGE',
                'value': 1003
            },
            {
                'name': 'FUNCTION_VAL_WAVEFORM_CURRENT',
                'value': 1004
            },
            {
                'name': 'FUNCTION_VAL_CAPACITANCE',
                'value': 1005
            },
            {
                'name': 'FUNCTION_VAL_INDUCTANCE',
                'value': 1006
            },
            {
                'name': 'LATENCY_VAL_LATENCY_AUTO',
                'value': -1
            },
            {
                'name': 'LC_CALCULATION_MODEL_VAL_CALC_MODEL_SERIES',
                'value': 0
            },
            {
                'name': 'LC_CALCULATION_MODEL_VAL_CALC_MODEL_AUTO',
                'value': -1
            },
            {
                'name': 'LC_CALCULATION_MODEL_VAL_CALC_MODEL_PARALLEL',
                'value': 1
            },
            {
                'name': 'MEASUREMENT_COMPLETE_DEST_VAL_NONE',
                'value': -1
            },
            {
                'name': 'MEASUREMENT_COMPLETE_DEST_VAL_EXTERNAL',
                'value': 2
            },
            {
                'name': 'MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG0',
                'value': 111
            },
            {
                'name': 'MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG1',
                'value': 112
            },
            {
                'name': 'MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG2',
                'value': 113
            },
            {
                'name': 'MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG3',
                'value': 114
            },
            {
                'name': 'MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG4',
                'value': 115
            },
            {
                'name': 'MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG5',
                'value': 116
            },
            {
                'name': 'MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG6',
                'value': 117
            },
            {
                'name': 'MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG7',
                'value': 118
            },
            {
                'name': 'MEASUREMENT_COMPLETE_DEST_VAL_LBR_TRIG0',
                'value': 1003
            },
            {
                'name': 'MEASUREMENT_DESTINATION_SLOPE_VAL_POSITIVE',
                'value': 0
            },
            {
                'name': 'MEASUREMENT_DESTINATION_SLOPE_VAL_NEGATIVE',
                'value': 1
            },
            {
                'name': 'OPERATION_MODE_VAL_IVIDMM_MODE',
                'value': 0
            },
            {
                'name': 'OPERATION_MODE_VAL_WAVEFORM_MODE',
                'value': 1
            },
            {
                'name': 'RTD_TYPE_VAL_TEMP_RTD_CUSTOM',
                'value': 0
            },
            {
                'name': 'RTD_TYPE_VAL_TEMP_RTD_PT3750',
                'value': 1
            },
            {
                'name': 'RTD_TYPE_VAL_TEMP_RTD_PT3851',
                'value': 2
            },
            {
                'name': 'RTD_TYPE_VAL_TEMP_RTD_PT3911',
                'value': 3
            },
            {
                'name': 'RTD_TYPE_VAL_TEMP_RTD_PT3916',
                'value': 4
            },
            {
                'name': 'RTD_TYPE_VAL_TEMP_RTD_PT3920',
                'value': 5
            },
            {
                'name': 'RTD_TYPE_VAL_TEMP_RTD_PT3928',
                'value': 6
            },
            {
                'name': 'SAMPLE_COUNT_VAL_SAMPLE_COUNT_INFINITE',
                'value': 0
            },
            {
                'name': 'SAMPLE_TRIG_SLOPE_VAL_POSITIVE',
                'value': 0
            },
            {
                'name': 'SAMPLE_TRIG_SLOPE_VAL_NEGATIVE',
                'value': 1
            },
            {
                'name': 'SAMPLE_TRIGGER_VAL_IMMEDIATE',
                'value': 1
            },
            {
                'name': 'SAMPLE_TRIGGER_VAL_EXTERNAL',
                'value': 2
            },
            {
                'name': 'SAMPLE_TRIGGER_VAL_SOFTWARE_TRIG',
                'value': 3
            },
            {
                'name': 'SAMPLE_TRIGGER_VAL_INTERVAL',
                'value': 10
            },
            {
                'name': 'SAMPLE_TRIGGER_VAL_PXI_TRIG0',
                'value': 111
            },
            {
                'name': 'SAMPLE_TRIGGER_VAL_PXI_TRIG1',
                'value': 112
            },
            {
                'name': 'SAMPLE_TRIGGER_VAL_PXI_TRIG2',
                'value': 113
            },
            {
                'name': 'SAMPLE_TRIGGER_VAL_PXI_TRIG3',
                'value': 114
            },
            {
                'name': 'SAMPLE_TRIGGER_VAL_PXI_TRIG4',
                'value': 115
            },
            {
                'name': 'SAMPLE_TRIGGER_VAL_PXI_TRIG5',
                'value': 116
            },
            {
                'name': 'SAMPLE_TRIGGER_VAL_PXI_TRIG6',
                'value': 117
            },
            {
                'name': 'SAMPLE_TRIGGER_VAL_PXI_TRIG7',
                'value': 118
            },
            {
                'name': 'SAMPLE_TRIGGER_VAL_PXI_STAR',
                'value': 131
            },
            {
                'name': 'SAMPLE_TRIGGER_VAL_AUX_TRIG1',
                'value': 1001
            },
            {
                'name': 'SAMPLE_TRIGGER_VAL_LBR_TRIG1',
                'value': 1004
            },
            {
                'name': 'THERMISTOR_TYPE_VAL_TEMP_THERMISTOR_CUSTOM',
                'value': 0
            },
            {
                'name': 'THERMISTOR_TYPE_VAL_TEMP_THERMISTOR_44004',
                'value': 1
            },
            {
                'name': 'THERMISTOR_TYPE_VAL_TEMP_THERMISTOR_44006',
                'value': 2
            },
            {
                'name': 'THERMISTOR_TYPE_VAL_TEMP_THERMISTOR_44007',
                'value': 3
            },
            {
                'name': 'THERMOCOUPLE_REFERENCE_JUNCTION_TYPE_VAL_TEMP_REF_JUNC_FIXED',
                'value': 2
            },
            {
                'name': 'THERMOCOUPLE_TYPE_VAL_TEMP_TC_B',
                'value': 1
            },
            {
                'name': 'THERMOCOUPLE_TYPE_VAL_TEMP_TC_E',
                'value': 4
            },
            {
                'name': 'THERMOCOUPLE_TYPE_VAL_TEMP_TC_J',
                'value': 6
            },
            {
                'name': 'THERMOCOUPLE_TYPE_VAL_TEMP_TC_K',
                'value': 7
            },
            {
                'name': 'THERMOCOUPLE_TYPE_VAL_TEMP_TC_N',
                'value': 8
            },
            {
                'name': 'THERMOCOUPLE_TYPE_VAL_TEMP_TC_R',
                'value': 9
            },
            {
                'name': 'THERMOCOUPLE_TYPE_VAL_TEMP_TC_S',
                'value': 10
            },
            {
                'name': 'THERMOCOUPLE_TYPE_VAL_TEMP_TC_T',
                'value': 11
            },
            {
                'name': 'TRANSDUCER_TYPE_VAL_THERMOCOUPLE',
                'value': 1
            },
            {
                'name': 'TRANSDUCER_TYPE_VAL_THERMISTOR',
                'value': 2
            },
            {
                'name': 'TRANSDUCER_TYPE_VAL_2_WIRE_RTD',
                'value': 3
            },
            {
                'name': 'TRANSDUCER_TYPE_VAL_4_WIRE_RTD',
                'value': 4
            },
            {
                'name': 'TRIGGER_COUNT_VAL_TRIG_COUNT_INFINITE',
                'value': 0
            },
            {
                'name': 'TRIGGER_SLOPE_VAL_POSITIVE',
                'value': 0
            },
            {
                'name': 'TRIGGER_SLOPE_VAL_NEGATIVE',
                'value': 1
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_IMMEDIATE',
                'value': 1
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_EXTERNAL',
                'value': 2
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_SOFTWARE_TRIG',
                'value': 3
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_PXI_TRIG0',
                'value': 111
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_PXI_TRIG1',
                'value': 112
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_PXI_TRIG2',
                'value': 113
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_PXI_TRIG3',
                'value': 114
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_PXI_TRIG4',
                'value': 115
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_PXI_TRIG5',
                'value': 116
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_PXI_TRIG6',
                'value': 117
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_PXI_TRIG7',
                'value': 118
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_PXI_STAR',
                'value': 131
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_AUX_TRIG1',
                'value': 1001
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_LBR_TRIG1',
                'value': 1004
            },
            {
                'name': 'WAVEFORM_COUPLING_VAL_WAVEFORM_COUPLING_AC',
                'value': 0
            },
            {
                'name': 'WAVEFORM_COUPLING_VAL_WAVEFORM_COUPLING_DC',
                'value': 1
            }
        ]
    },
    'NiDmmReal64AttributeValues': {
        'enum-value-prefix': 'NIDMM_REAL64',
        'generate-mappings': False,
        'values': [
            {
                'name': 'APERTURE_TIME_VAL_APERTURE_TIME_AUTO',
                'value': -1
            },
            {
                'name': 'APERTURE_TIME_VAL_1_PLC',
                'value': 1
            },
            {
                'name': 'APERTURE_TIME_VAL_5_PLC',
                'value': 5
            },
            {
                'name': 'APERTURE_TIME_VAL_6_PLC',
                'value': 6
            },
            {
                'name': 'APERTURE_TIME_VAL_10_PLC',
                'value': 10
            },
            {
                'name': 'APERTURE_TIME_VAL_12_PLC',
                'value': 12
            },
            {
                'name': 'APERTURE_TIME_VAL_100_PLC',
                'value': 100
            },
            {
                'name': 'APERTURE_TIME_VAL_120_PLC',
                'value': 120
            },
            {
                'name': 'FREQUENCY_VOLTAGE_RANGE_VAL_AUTO_RANGE_ON',
                'value': -1
            },
            {
                'name': 'FREQUENCY_VOLTAGE_RANGE_VAL_AUTO_RANGE_OFF',
                'value': -2
            },
            {
                'name': 'POWER_LINE_FREQUENCIES_VAL_50_HERTZ',
                'value': 50
            },
            {
                'name': 'POWER_LINE_FREQUENCIES_VAL_60_HERTZ',
                'value': 60
            },
            {
                'name': 'RANGE_VAL_AUTO_RANGE_ON',
                'value': -1
            },
            {
                'name': 'RANGE_VAL_AUTO_RANGE_OFF',
                'value': -2
            },
            {
                'name': 'RANGE_VAL_AUTO_RANGE_ONCE',
                'value': -3
            },
            {
                'name': 'SAMPLE_INTERVAL_VAL_AUTO_DELAY',
                'value': -1
            },
            {
                'name': 'SETTLE_TIME_VAL_SETTLE_TIME_AUTO',
                'value': -1
            },
            {
                'name': 'TRIGGER_DELAYS_VAL_AUTO_DELAY',
                'value': -1
            },
            {
                'name': 'TRIGGER_DELAYS_VAL_AUTO_DELAY_ON',
                'value': -1
            },
            {
                'name': 'TRIGGER_DELAYS_VAL_AUTO_DELAY_OFF',
                'value': -2
            }
        ]
    },
    'NiDmmReal64AttributeValuesMapped': {
        'enum-value-prefix': 'NIDMM_REAL64',
        'generate-mappings': True,
        'values': [
            {
                'name': 'CURRENT_SOURCE_VAL_1_MICROAMP',
                'value': 1e-06
            },
            {
                'name': 'CURRENT_SOURCE_VAL_10_MICROAMP',
                'value': 1e-05
            },
            {
                'name': 'CURRENT_SOURCE_VAL_100_MICROAMP',
                'value': 0.0001
            },
            {
                'name': 'CURRENT_SOURCE_VAL_1_MILLIAMP',
                'value': 0.001
            },
            {
                'name': 'INPUT_RESISTANCE_VAL_RESISTANCE_NA',
                'value': 0
            },
            {
                'name': 'INPUT_RESISTANCE_VAL_1_MEGAOHM',
                'value': 1000000
            },
            {
                'name': 'INPUT_RESISTANCE_VAL_10_MEGAOHM',
                'value': 10000000
            },
            {
                'name': 'INPUT_RESISTANCE_VAL_GREATER_THAN_10_GIGAOHM',
                'value': 10000000000.0
            }
        ]
    },
    'OperationMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_IVIDMM_MODE',
                'value': 0
            },
            {
                'name': 'NIDMM_VAL_WAVEFORM_MODE',
                'value': 1
            }
        ]
    },
    'PowerLineFrequencies': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_50_HERTZ',
                'value': 50
            },
            {
                'name': 'NIDMM_VAL_60_HERTZ',
                'value': 60
            }
        ]
    },
    'Range': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_AUTO_RANGE_ON',
                'value': -1
            },
            {
                'name': 'NIDMM_VAL_AUTO_RANGE_OFF',
                'value': -2
            },
            {
                'name': 'NIDMM_VAL_AUTO_RANGE_ONCE',
                'value': -3
            }
        ]
    },
    'RtdType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_TEMP_RTD_CUSTOM',
                'value': 0
            },
            {
                'name': 'NIDMM_VAL_TEMP_RTD_PT3750',
                'value': 1
            },
            {
                'name': 'NIDMM_VAL_TEMP_RTD_PT3851',
                'value': 2
            },
            {
                'name': 'NIDMM_VAL_TEMP_RTD_PT3911',
                'value': 3
            },
            {
                'name': 'NIDMM_VAL_TEMP_RTD_PT3916',
                'value': 4
            },
            {
                'name': 'NIDMM_VAL_TEMP_RTD_PT3920',
                'value': 5
            },
            {
                'name': 'NIDMM_VAL_TEMP_RTD_PT3928',
                'value': 6
            }
        ]
    },
    'SampleCount': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_SAMPLE_COUNT_INFINITE',
                'value': 0
            }
        ]
    },
    'SampleInterval': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_AUTO_DELAY',
                'value': -1
            }
        ]
    },
    'SampleTrigSlope': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_POSITIVE',
                'value': 0
            },
            {
                'name': 'NIDMM_VAL_NEGATIVE',
                'value': 1
            }
        ]
    },
    'SampleTrigger': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_IMMEDIATE',
                'value': 1
            },
            {
                'name': 'NIDMM_VAL_EXTERNAL',
                'value': 2
            },
            {
                'name': 'NIDMM_VAL_SOFTWARE_TRIG',
                'value': 3
            },
            {
                'name': 'NIDMM_VAL_INTERVAL',
                'value': 10
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG0',
                'value': 111
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG1',
                'value': 112
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG2',
                'value': 113
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG3',
                'value': 114
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG4',
                'value': 115
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG5',
                'value': 116
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG6',
                'value': 117
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG7',
                'value': 118
            },
            {
                'name': 'NIDMM_VAL_PXI_STAR',
                'value': 131
            },
            {
                'name': 'NIDMM_VAL_AUX_TRIG1',
                'value': 1001
            },
            {
                'name': 'NIDMM_VAL_LBR_TRIG1',
                'value': 1004
            }
        ]
    },
    'SettleTime': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_SETTLE_TIME_AUTO',
                'value': -1
            }
        ]
    },
    'ThermistorType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_TEMP_THERMISTOR_CUSTOM',
                'value': 0
            },
            {
                'name': 'NIDMM_VAL_TEMP_THERMISTOR_44004',
                'value': 1
            },
            {
                'name': 'NIDMM_VAL_TEMP_THERMISTOR_44006',
                'value': 2
            },
            {
                'name': 'NIDMM_VAL_TEMP_THERMISTOR_44007',
                'value': 3
            }
        ]
    },
    'ThermocoupleReferenceJunctionType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_TEMP_REF_JUNC_FIXED',
                'value': 2
            }
        ]
    },
    'ThermocoupleType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_TEMP_TC_B',
                'value': 1
            },
            {
                'name': 'NIDMM_VAL_TEMP_TC_E',
                'value': 4
            },
            {
                'name': 'NIDMM_VAL_TEMP_TC_J',
                'value': 6
            },
            {
                'name': 'NIDMM_VAL_TEMP_TC_K',
                'value': 7
            },
            {
                'name': 'NIDMM_VAL_TEMP_TC_N',
                'value': 8
            },
            {
                'name': 'NIDMM_VAL_TEMP_TC_R',
                'value': 9
            },
            {
                'name': 'NIDMM_VAL_TEMP_TC_S',
                'value': 10
            },
            {
                'name': 'NIDMM_VAL_TEMP_TC_T',
                'value': 11
            }
        ]
    },
    'TimeLimit': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_TIME_LIMIT_AUTO',
                'value': -1
            }
        ]
    },
    'TransducerType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_THERMOCOUPLE',
                'value': 1
            },
            {
                'name': 'NIDMM_VAL_THERMISTOR',
                'value': 2
            },
            {
                'name': 'NIDMM_VAL_2_WIRE_RTD',
                'value': 3
            },
            {
                'name': 'NIDMM_VAL_4_WIRE_RTD',
                'value': 4
            }
        ]
    },
    'TriggerCount': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_TRIG_COUNT_INFINITE',
                'value': 0
            }
        ]
    },
    'TriggerDelays': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_AUTO_DELAY',
                'value': -1
            },
            {
                'name': 'NIDMM_VAL_AUTO_DELAY_ON',
                'value': -1
            },
            {
                'name': 'NIDMM_VAL_AUTO_DELAY_OFF',
                'value': -2
            }
        ]
    },
    'TriggerSlope': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_POSITIVE',
                'value': 0
            },
            {
                'name': 'NIDMM_VAL_NEGATIVE',
                'value': 1
            }
        ]
    },
    'TriggerSource': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_IMMEDIATE',
                'value': 1
            },
            {
                'name': 'NIDMM_VAL_EXTERNAL',
                'value': 2
            },
            {
                'name': 'NIDMM_VAL_SOFTWARE_TRIG',
                'value': 3
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG0',
                'value': 111
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG1',
                'value': 112
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG2',
                'value': 113
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG3',
                'value': 114
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG4',
                'value': 115
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG5',
                'value': 116
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG6',
                'value': 117
            },
            {
                'name': 'NIDMM_VAL_PXI_TRIG7',
                'value': 118
            },
            {
                'name': 'NIDMM_VAL_PXI_STAR',
                'value': 131
            },
            {
                'name': 'NIDMM_VAL_AUX_TRIG1',
                'value': 1001
            },
            {
                'name': 'NIDMM_VAL_LBR_TRIG1',
                'value': 1004
            }
        ]
    },
    'WaveformCoupling': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_WAVEFORM_COUPLING_AC',
                'value': 0
            },
            {
                'name': 'NIDMM_VAL_WAVEFORM_COUPLING_DC',
                'value': 1
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidmm/enums_addon.py sha256=9f25172e660fd7e043e0a5b4bbd8669084c5cf552aa295713232ee352147b900 bytes=192 -->
## FILE: source/codegen/metadata/nidmm/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidmm/enums_addon.py`
- sha256: `9f25172e660fd7e043e0a5b4bbd8669084c5cf552aa295713232ee352147b900`
- bytes: 192

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidmm/functions.py sha256=578662d2d9a9fb437261751b909911811bbb886117a0bb808c822a71deac40d1 bytes=77935 -->
## FILE: source/codegen/metadata/nidmm/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidmm/functions.py`
- sha256: `578662d2d9a9fb437261751b909911811bbb886117a0bb808c822a71deac40d1`
- bytes: 77935

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-DMM API metadata version 26.0.0d90
functions = {
    'Abort': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViBoolean': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiDmmAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViInt32': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiDmmAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'enum': 'NiDmmInt32AttributeValues',
                'grpc_type': 'sint32',
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViReal64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiDmmAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'enum': 'NiDmmReal64AttributeValues',
                'grpc_field_number': '4',
                'grpc_mapped_field_number': '6',
                'grpc_raw_field_number': '5',
                'grpc_type': 'double',
                'mapped-enum': 'NiDmmReal64AttributeValuesMapped',
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViSession': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiDmmAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'attributeValue',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiDmmAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'attribute_value_raw',
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearError': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearInterchangeWarnings': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'Close': {
        'cname': 'niDMM_close',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureACBandwidth': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'acMinimumFrequencyHz',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'acMinimumFrequencyHz',
                'type': 'ViReal64'
            },
            {
                'cppName': 'acMaximumFrequencyHz',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'acMaximumFrequencyHz',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureADCCalibration': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'adcCalibration',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'adcCalibration',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureAutoZeroMode': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'autoZeroMode',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'autoZeroMode',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureCableCompType': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'cableCompType',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'cableCompType',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureCurrentSource': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'currentSource',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'currentSource',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureFixedRefJunction': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'fixedReferenceJunction',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'fixedReferenceJunction',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureFrequencyVoltageRange': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'voltageRange',
                'direction': 'in',
                'enum': 'FrequencyVoltageRange',
                'grpc_type': 'double',
                'name': 'voltageRange',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureMeasCompleteDest': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'measCompleteDestination',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'measCompleteDestination',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureMeasCompleteSlope': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'measCompleteSlope',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'measCompleteSlope',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureMeasurementAbsolute': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'measurementFunction',
                'direction': 'in',
                'enum': 'Function',
                'grpc_type': 'sint32',
                'name': 'measurementFunction',
                'type': 'ViInt32'
            },
            {
                'cppName': 'range',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'cppName': 'resolutionAbsolute',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'resolutionAbsolute',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureMeasurementDigits': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'measurementFunction',
                'direction': 'in',
                'enum': 'Function',
                'grpc_type': 'sint32',
                'name': 'measurementFunction',
                'type': 'ViInt32'
            },
            {
                'cppName': 'range',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'cppName': 'resolutionDigits',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'resolutionDigits',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureMultiPoint': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'triggerCount',
                'direction': 'in',
                'enum': 'TriggerCount',
                'grpc_type': 'sint32',
                'name': 'triggerCount',
                'type': 'ViInt32'
            },
            {
                'cppName': 'sampleCount',
                'direction': 'in',
                'enum': 'SampleCount',
                'grpc_type': 'sint32',
                'name': 'sampleCount',
                'type': 'ViInt32'
            },
            {
                'cppName': 'sampleTrigger',
                'direction': 'in',
                'enum': 'SampleTrigger',
                'grpc_type': 'sint32',
                'name': 'sampleTrigger',
                'type': 'ViInt32'
            },
            {
                'cppName': 'sampleInterval',
                'direction': 'in',
                'enum': 'SampleInterval',
                'grpc_type': 'double',
                'name': 'sampleInterval',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureOffsetCompOhms': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'offsetCompOhms',
                'direction': 'in',
                'enum': 'CompensatedOhms',
                'grpc_type': 'sint32',
                'name': 'offsetCompOhms',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureOpenCableCompValues': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'conductance',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'conductance',
                'type': 'ViReal64'
            },
            {
                'cppName': 'susceptance',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'susceptance',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePowerLineFrequency': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'powerLineFrequencyHz',
                'direction': 'in',
                'enum': 'PowerLineFrequencies',
                'grpc_type': 'double',
                'name': 'powerLineFrequencyHz',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureRTDCustom': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'rtdA',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'rtdA',
                'type': 'ViReal64'
            },
            {
                'cppName': 'rtdB',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'rtdB',
                'type': 'ViReal64'
            },
            {
                'cppName': 'rtdC',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'rtdC',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureRTDType': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'rtdType',
                'direction': 'in',
                'enum': 'RtdType',
                'grpc_type': 'sint32',
                'name': 'rtdType',
                'type': 'ViInt32'
            },
            {
                'cppName': 'rtdResistance',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'rtdResistance',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSampleTriggerSlope': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'sampleTriggerSlope',
                'direction': 'in',
                'enum': 'SampleTrigSlope',
                'grpc_type': 'sint32',
                'name': 'sampleTriggerSlope',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureShortCableCompValues': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'resistance',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'resistance',
                'type': 'ViReal64'
            },
            {
                'cppName': 'reactance',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'reactance',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureThermistorCustom': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'thermistorA',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'thermistorA',
                'type': 'ViReal64'
            },
            {
                'cppName': 'thermistorB',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'thermistorB',
                'type': 'ViReal64'
            },
            {
                'cppName': 'thermistorC',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'thermistorC',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureThermistorType': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'thermistorType',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'thermistorType',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureThermocouple': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'thermocoupleType',
                'direction': 'in',
                'enum': 'ThermocoupleType',
                'grpc_type': 'sint32',
                'name': 'thermocoupleType',
                'type': 'ViInt32'
            },
            {
                'cppName': 'referenceJunctionType',
                'direction': 'in',
                'enum': 'ThermocoupleReferenceJunctionType',
                'grpc_type': 'sint32',
                'name': 'referenceJunctionType',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTransducerType': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'transducerType',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'transducerType',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'triggerSource',
                'direction': 'in',
                'enum': 'TriggerSource',
                'grpc_type': 'sint32',
                'name': 'triggerSource',
                'type': 'ViInt32'
            },
            {
                'cppName': 'triggerDelay',
                'direction': 'in',
                'enum': 'TriggerDelays',
                'grpc_type': 'double',
                'name': 'triggerDelay',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerSlope': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'triggerSlope',
                'direction': 'in',
                'enum': 'TriggerSlope',
                'grpc_type': 'sint32',
                'name': 'triggerSlope',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureWaveformAcquisition': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'measurementFunction',
                'direction': 'in',
                'enum': 'Function',
                'grpc_type': 'sint32',
                'name': 'measurementFunction',
                'type': 'ViInt32'
            },
            {
                'cppName': 'range',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'cppName': 'rate',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'rate',
                'type': 'ViReal64'
            },
            {
                'cppName': 'waveformPoints',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'waveformPoints',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureWaveformCoupling': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'waveformCoupling',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'waveformCoupling',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'Control': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'controlAction',
                'direction': 'in',
                'enum': 'ControlCommit',
                'grpc_type': 'sint32',
                'name': 'controlAction',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'Disable': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributeConfigurationBuffer': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'size',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'cppName': 'configuration',
                'direction': 'out',
                'grpc_type': 'bytes',
                'name': 'configuration',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'ViInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributeConfigurationFile': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'filePath',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'Fetch': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'maximumTime',
                'direction': 'in',
                'enum': 'TimeLimit',
                'grpc_type': 'sint32',
                'name': 'maximumTime',
                'type': 'ViInt32'
            },
            {
                'cppName': 'reading',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'reading',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchMultiPoint': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'maximumTime',
                'direction': 'in',
                'enum': 'TimeLimit',
                'grpc_type': 'sint32',
                'name': 'maximumTime',
                'type': 'ViInt32'
            },
            {
                'cppName': 'arraySize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'is_size_param': True,
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'readingArray',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'readingArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySize'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'actualNumberOfPoints',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchWaveform': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'maximumTime',
                'direction': 'in',
                'enum': 'TimeLimit',
                'grpc_type': 'sint32',
                'name': 'maximumTime',
                'type': 'ViInt32'
            },
            {
                'cppName': 'arraySize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'is_size_param': True,
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'waveformArray',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'waveformArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySize'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'actualNumberOfPoints',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetApertureTimeInfo': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'apertureTime',
                'direction': 'out',
                'enum': 'ApertureTime',
                'grpc_type': 'double',
                'name': 'apertureTime',
                'type': 'ViReal64'
            },
            {
                'cppName': 'apertureTimeUnits',
                'direction': 'out',
                'enum': 'ApertureTimeUnits',
                'grpc_type': 'sint32',
                'name': 'apertureTimeUnits',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiDmmAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt32': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiDmmAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViReal64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiDmmAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViSession': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiDmmAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'attributeValue',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiDmmAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'attributeValue',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAutoRangeValue': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'actualRange',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'actualRange',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetCalDateAndTime': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'calType',
                'direction': 'in',
                'enum': 'CalibrationType',
                'grpc_type': 'sint32',
                'name': 'calType',
                'type': 'ViInt32'
            },
            {
                'cppName': 'month',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'cppName': 'day',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'day',
                'type': 'ViInt32'
            },
            {
                'cppName': 'year',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'cppName': 'hour',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'hour',
                'type': 'ViInt32'
            },
            {
                'cppName': 'minute',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'minute',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetChannelName': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'index',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'index',
                'type': 'ViInt32'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'channelString',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'channelString',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetDevTemp': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'options',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'options',
                'type': 'ViString'
            },
            {
                'cppName': 'temperature',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetError': {
        'codegen_method': 'public',
        'is_error_handling': True,
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorCode',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'description',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'description',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetErrorMessage': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorCode',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'errorMessage',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetExtCalRecommendedInterval': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'months',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'months',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetLastCalTemp': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'calType',
                'direction': 'in',
                'enum': 'CalibrationType',
                'grpc_type': 'sint32',
                'name': 'calType',
                'type': 'ViInt32'
            },
            {
                'cppName': 'temperature',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetMeasurementPeriod': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'period',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'period',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSelfCalSupported': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'selfCalSupported',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'selfCalSupported',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributeConfigurationBuffer': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'size',
                'determine_size_from': [
                    'configuration'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'cppName': 'configuration',
                'direction': 'in',
                'grpc_type': 'bytes',
                'name': 'configuration',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributeConfigurationFile': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'filePath',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'Init': {
        'cname': 'niDMM_init',
        'codegen_method': 'public',
        'init_method': True,
        'parameters': [
            {
                'cppName': 'resourceName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'resourceName',
                'type': 'ViString'
            },
            {
                'cppName': 'idQuery',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'idQuery',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'resetDevice',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'vi',
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorMessage',
                'direction': 'out',
                'get_last_error': 'deprecated',
                'grpc_type': 'string',
                'name': 'errorMessage',
                'type': 'ViChar[]'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'ViInt32'
            },
            {
                'cppName': 'newSessionInitialized',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'newSessionInitialized',
                'proto_only': True,
                'type': 'bool'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitWithOptions': {
        'codegen_method': 'public',
        'init_method': True,
        'parameters': [
            {
                'cppName': 'resourceName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'resourceName',
                'type': 'ViString'
            },
            {
                'cppName': 'idQuery',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'idQuery',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'resetDevice',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'optionString',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'optionString',
                'type': 'ViString'
            },
            {
                'cppName': 'vi',
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorMessage',
                'direction': 'out',
                'get_last_error': 'deprecated',
                'grpc_type': 'string',
                'name': 'errorMessage',
                'type': 'ViChar[]'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'ViInt32'
            },
            {
                'cppName': 'newSessionInitialized',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'newSessionInitialized',
                'proto_only': True,
                'type': 'bool'
            }
        ],
        'returns': 'ViStatus'
    },
    'Initiate': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'InvalidateAllAttributes': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'IsOverRange': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'measurementValue',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'measurementValue',
                'type': 'ViReal64'
            },
            {
                'cppName': 'isOverRange',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'isOverRange',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'IsUnderRange': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'measurementValue',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'measurementValue',
                'type': 'ViReal64'
            },
            {
                'cppName': 'isUnderRange',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'isUnderRange',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'LockSession': {
        'codegen_method': 'private',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'callerHasLock',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'PerformOpenCableComp': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'conductance',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'conductance',
                'type': 'ViReal64'
            },
            {
                'cppName': 'susceptance',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'susceptance',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'PerformShortCableComp': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'resistance',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'resistance',
                'type': 'ViReal64'
            },
            {
                'cppName': 'reactance',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'reactance',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'Read': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'maximumTime',
                'direction': 'in',
                'enum': 'TimeLimit',
                'grpc_type': 'sint32',
                'name': 'maximumTime',
                'type': 'ViInt32'
            },
            {
                'cppName': 'reading',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'reading',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadMultiPoint': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'maximumTime',
                'direction': 'in',
                'enum': 'TimeLimit',
                'grpc_type': 'sint32',
                'name': 'maximumTime',
                'type': 'ViInt32'
            },
            {
                'cppName': 'arraySize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'is_size_param': True,
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'readingArray',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'readingArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySize'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'actualNumberOfPoints',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadStatus': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'acquisitionBacklog',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'acquisitionBacklog',
                'type': 'ViInt32'
            },
            {
                'cppName': 'acquisitionStatus',
                'direction': 'out',
                'enum': 'AcquisitionStatus',
                'grpc_type': 'sint32',
                'name': 'acquisitionStatus',
                'type': 'ViInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadWaveform': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'maximumTime',
                'direction': 'in',
                'enum': 'TimeLimit',
                'grpc_type': 'sint32',
                'name': 'maximumTime',
                'type': 'ViInt32'
            },
            {
                'cppName': 'arraySize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'is_size_param': True,
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'waveformArray',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'waveformArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySize'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'actualNumberOfPoints',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'Reset': {
        'cname': 'niDMM_reset',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetInterchangeCheck': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetWithDefaults': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'RevisionQuery': {
        'cname': 'niDMM_revision_query',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'instrumentDriverRevision',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'instrumentDriverRevision',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            },
            {
                'cppName': 'firmwareRevision',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'firmwareRevision',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'SelfCal': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SelfTest': {
        'cname': 'niDMM_self_test',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'selfTestResult',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'selfTestResult',
                'type': 'ViInt16'
            },
            {
                'cppName': 'selfTestMessage',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'selfTestMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'SendSoftwareTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViBoolean': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiDmmAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt32': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiDmmAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'enum': 'NiDmmInt32AttributeValues',
                'grpc_type': 'sint32',
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViReal64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiDmmAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'enum': 'NiDmmReal64AttributeValues',
                'grpc_field_number': '4',
                'grpc_mapped_field_number': '6',
                'grpc_raw_field_number': '5',
                'grpc_type': 'double',
                'mapped-enum': 'NiDmmReal64AttributeValuesMapped',
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViSession': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiDmmAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'attributeValue',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiDmmAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'attribute_value_raw',
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetRuntimeEnvironment': {
        'codegen_method': 'private',
        'parameters': [
            {
                'cppName': 'environment',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'environment',
                'type': 'ViConstString'
            },
            {
                'cppName': 'environmentVersion',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'environmentVersion',
                'type': 'ViConstString'
            },
            {
                'cppName': 'reserved1',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'reserved1',
                'type': 'ViConstString'
            },
            {
                'cppName': 'reserved2',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'reserved2',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'UnlockSession': {
        'codegen_method': 'private',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'callerHasLock',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidmm/functions_addon.py sha256=2baced8307d23f1fceb2b39befd2ea9702c4a8ea8094614a02db2ab889ce5f21 bytes=243 -->
## FILE: source/codegen/metadata/nidmm/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidmm/functions_addon.py`
- sha256: `2baced8307d23f1fceb2b39befd2ea9702c4a8ea8094614a02db2ab889ce5f21`
- bytes: 243

````python
# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidmm/nidmm.proto sha256=943f2ced8151366b0169aa953f1cd20242b9e53da342656fbc9fd0b8e8fb079e bytes=46053 -->
## FILE: source/codegen/metadata/nidmm/nidmm.proto

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidmm/nidmm.proto`
- sha256: `943f2ced8151366b0169aa953f1cd20242b9e53da342656fbc9fd0b8e8fb079e`
- bytes: 46053

````protobuf

//---------------------------------------------------------------------
// This file is generated from NI-DMM API metadata version 26.0.0d90
//---------------------------------------------------------------------
// Proto file for the NI-DMM Metadata
//---------------------------------------------------------------------
syntax = "proto3";

option java_multiple_files = true;
option java_package = "com.ni.grpc.dmm";
option java_outer_classname = "NiDmm";
option csharp_namespace = "NationalInstruments.Grpc.Dmm";

package nidmm_grpc;

import "session.proto";

service NiDmm {
  rpc Abort(AbortRequest) returns (AbortResponse);
  rpc CheckAttributeViBoolean(CheckAttributeViBooleanRequest) returns (CheckAttributeViBooleanResponse);
  rpc CheckAttributeViInt32(CheckAttributeViInt32Request) returns (CheckAttributeViInt32Response);
  rpc CheckAttributeViReal64(CheckAttributeViReal64Request) returns (CheckAttributeViReal64Response);
  rpc CheckAttributeViSession(CheckAttributeViSessionRequest) returns (CheckAttributeViSessionResponse);
  rpc CheckAttributeViString(CheckAttributeViStringRequest) returns (CheckAttributeViStringResponse);
  rpc ClearError(ClearErrorRequest) returns (ClearErrorResponse);
  rpc ClearInterchangeWarnings(ClearInterchangeWarningsRequest) returns (ClearInterchangeWarningsResponse);
  rpc Close(CloseRequest) returns (CloseResponse);
  rpc ConfigureACBandwidth(ConfigureACBandwidthRequest) returns (ConfigureACBandwidthResponse);
  rpc ConfigureADCCalibration(ConfigureADCCalibrationRequest) returns (ConfigureADCCalibrationResponse);
  rpc ConfigureAutoZeroMode(ConfigureAutoZeroModeRequest) returns (ConfigureAutoZeroModeResponse);
  rpc ConfigureCableCompType(ConfigureCableCompTypeRequest) returns (ConfigureCableCompTypeResponse);
  rpc ConfigureCurrentSource(ConfigureCurrentSourceRequest) returns (ConfigureCurrentSourceResponse);
  rpc ConfigureFixedRefJunction(ConfigureFixedRefJunctionRequest) returns (ConfigureFixedRefJunctionResponse);
  rpc ConfigureFrequencyVoltageRange(ConfigureFrequencyVoltageRangeRequest) returns (ConfigureFrequencyVoltageRangeResponse);
  rpc ConfigureMeasCompleteDest(ConfigureMeasCompleteDestRequest) returns (ConfigureMeasCompleteDestResponse);
  rpc ConfigureMeasCompleteSlope(ConfigureMeasCompleteSlopeRequest) returns (ConfigureMeasCompleteSlopeResponse);
  rpc ConfigureMeasurementAbsolute(ConfigureMeasurementAbsoluteRequest) returns (ConfigureMeasurementAbsoluteResponse);
  rpc ConfigureMeasurementDigits(ConfigureMeasurementDigitsRequest) returns (ConfigureMeasurementDigitsResponse);
  rpc ConfigureMultiPoint(ConfigureMultiPointRequest) returns (ConfigureMultiPointResponse);
  rpc ConfigureOffsetCompOhms(ConfigureOffsetCompOhmsRequest) returns (ConfigureOffsetCompOhmsResponse);
  rpc ConfigureOpenCableCompValues(ConfigureOpenCableCompValuesRequest) returns (ConfigureOpenCableCompValuesResponse);
  rpc ConfigurePowerLineFrequency(ConfigurePowerLineFrequencyRequest) returns (ConfigurePowerLineFrequencyResponse);
  rpc ConfigureRTDCustom(ConfigureRTDCustomRequest) returns (ConfigureRTDCustomResponse);
  rpc ConfigureRTDType(ConfigureRTDTypeRequest) returns (ConfigureRTDTypeResponse);
  rpc ConfigureSampleTriggerSlope(ConfigureSampleTriggerSlopeRequest) returns (ConfigureSampleTriggerSlopeResponse);
  rpc ConfigureShortCableCompValues(ConfigureShortCableCompValuesRequest) returns (ConfigureShortCableCompValuesResponse);
  rpc ConfigureThermistorCustom(ConfigureThermistorCustomRequest) returns (ConfigureThermistorCustomResponse);
  rpc ConfigureThermistorType(ConfigureThermistorTypeRequest) returns (ConfigureThermistorTypeResponse);
  rpc ConfigureThermocouple(ConfigureThermocoupleRequest) returns (ConfigureThermocoupleResponse);
  rpc ConfigureTransducerType(ConfigureTransducerTypeRequest) returns (ConfigureTransducerTypeResponse);
  rpc ConfigureTrigger(ConfigureTriggerRequest) returns (ConfigureTriggerResponse);
  rpc ConfigureTriggerSlope(ConfigureTriggerSlopeRequest) returns (ConfigureTriggerSlopeResponse);
  rpc ConfigureWaveformAcquisition(ConfigureWaveformAcquisitionRequest) returns (ConfigureWaveformAcquisitionResponse);
  rpc ConfigureWaveformCoupling(ConfigureWaveformCouplingRequest) returns (ConfigureWaveformCouplingResponse);
  rpc Control(ControlRequest) returns (ControlResponse);
  rpc Disable(DisableRequest) returns (DisableResponse);
  rpc ExportAttributeConfigurationBuffer(ExportAttributeConfigurationBufferRequest) returns (ExportAttributeConfigurationBufferResponse);
  rpc ExportAttributeConfigurationFile(ExportAttributeConfigurationFileRequest) returns (ExportAttributeConfigurationFileResponse);
  rpc Fetch(FetchRequest) returns (FetchResponse);
  rpc FetchMultiPoint(FetchMultiPointRequest) returns (FetchMultiPointResponse);
  rpc FetchWaveform(FetchWaveformRequest) returns (FetchWaveformResponse);
  rpc GetApertureTimeInfo(GetApertureTimeInfoRequest) returns (GetApertureTimeInfoResponse);
  rpc GetAttributeViBoolean(GetAttributeViBooleanRequest) returns (GetAttributeViBooleanResponse);
  rpc GetAttributeViInt32(GetAttributeViInt32Request) returns (GetAttributeViInt32Response);
  rpc GetAttributeViReal64(GetAttributeViReal64Request) returns (GetAttributeViReal64Response);
  rpc GetAttributeViSession(GetAttributeViSessionRequest) returns (GetAttributeViSessionResponse);
  rpc GetAttributeViString(GetAttributeViStringRequest) returns (GetAttributeViStringResponse);
  rpc GetAutoRangeValue(GetAutoRangeValueRequest) returns (GetAutoRangeValueResponse);
  rpc GetCalDateAndTime(GetCalDateAndTimeRequest) returns (GetCalDateAndTimeResponse);
  rpc GetChannelName(GetChannelNameRequest) returns (GetChannelNameResponse);
  rpc GetDevTemp(GetDevTempRequest) returns (GetDevTempResponse);
  rpc GetError(GetErrorRequest) returns (GetErrorResponse);
  rpc GetErrorMessage(GetErrorMessageRequest) returns (GetErrorMessageResponse);
  rpc GetExtCalRecommendedInterval(GetExtCalRecommendedIntervalRequest) returns (GetExtCalRecommendedIntervalResponse);
  rpc GetLastCalTemp(GetLastCalTempRequest) returns (GetLastCalTempResponse);
  rpc GetMeasurementPeriod(GetMeasurementPeriodRequest) returns (GetMeasurementPeriodResponse);
  rpc GetSelfCalSupported(GetSelfCalSupportedRequest) returns (GetSelfCalSupportedResponse);
  rpc ImportAttributeConfigurationBuffer(ImportAttributeConfigurationBufferRequest) returns (ImportAttributeConfigurationBufferResponse);
  rpc ImportAttributeConfigurationFile(ImportAttributeConfigurationFileRequest) returns (ImportAttributeConfigurationFileResponse);
  rpc Init(InitRequest) returns (InitResponse);
  rpc InitWithOptions(InitWithOptionsRequest) returns (InitWithOptionsResponse);
  rpc Initiate(InitiateRequest) returns (InitiateResponse);
  rpc InvalidateAllAttributes(InvalidateAllAttributesRequest) returns (InvalidateAllAttributesResponse);
  rpc IsOverRange(IsOverRangeRequest) returns (IsOverRangeResponse);
  rpc IsUnderRange(IsUnderRangeRequest) returns (IsUnderRangeResponse);
  rpc PerformOpenCableComp(PerformOpenCableCompRequest) returns (PerformOpenCableCompResponse);
  rpc PerformShortCableComp(PerformShortCableCompRequest) returns (PerformShortCableCompResponse);
  rpc Read(ReadRequest) returns (ReadResponse);
  rpc ReadMultiPoint(ReadMultiPointRequest) returns (ReadMultiPointResponse);
  rpc ReadStatus(ReadStatusRequest) returns (ReadStatusResponse);
  rpc ReadWaveform(ReadWaveformRequest) returns (ReadWaveformResponse);
  rpc Reset(ResetRequest) returns (ResetResponse);
  rpc ResetInterchangeCheck(ResetInterchangeCheckRequest) returns (ResetInterchangeCheckResponse);
  rpc ResetWithDefaults(ResetWithDefaultsRequest) returns (ResetWithDefaultsResponse);
  rpc RevisionQuery(RevisionQueryRequest) returns (RevisionQueryResponse);
  rpc SelfCal(SelfCalRequest) returns (SelfCalResponse);
  rpc SelfTest(SelfTestRequest) returns (SelfTestResponse);
  rpc SendSoftwareTrigger(SendSoftwareTriggerRequest) returns (SendSoftwareTriggerResponse);
  rpc SetAttributeViBoolean(SetAttributeViBooleanRequest) returns (SetAttributeViBooleanResponse);
  rpc SetAttributeViInt32(SetAttributeViInt32Request) returns (SetAttributeViInt32Response);
  rpc SetAttributeViReal64(SetAttributeViReal64Request) returns (SetAttributeViReal64Response);
  rpc SetAttributeViSession(SetAttributeViSessionRequest) returns (SetAttributeViSessionResponse);
  rpc SetAttributeViString(SetAttributeViStringRequest) returns (SetAttributeViStringResponse);
}

enum NiDmmAttribute {
  NIDMM_ATTRIBUTE_UNSPECIFIED = 0;
  NIDMM_ATTRIBUTE_RANGE_CHECK = 1050002;
  NIDMM_ATTRIBUTE_QUERY_INSTRUMENT_STATUS = 1050003;
  NIDMM_ATTRIBUTE_CACHE = 1050004;
  NIDMM_ATTRIBUTE_SIMULATE = 1050005;
  NIDMM_ATTRIBUTE_RECORD_COERCIONS = 1050006;
  NIDMM_ATTRIBUTE_DRIVER_SETUP = 1050007;
  NIDMM_ATTRIBUTE_INTERCHANGE_CHECK = 1050021;
  NIDMM_ATTRIBUTE_CHANNEL_COUNT = 1050203;
  NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_PREFIX = 1050302;
  NIDMM_ATTRIBUTE_IO_RESOURCE_DESCRIPTOR = 1050304;
  NIDMM_ATTRIBUTE_LOGICAL_NAME = 1050305;
  NIDMM_ATTRIBUTE_IO_SESSION = 1050322;
  NIDMM_ATTRIBUTE_SUPPORTED_INSTRUMENT_MODELS = 1050327;
  NIDMM_ATTRIBUTE_GROUP_CAPABILITIES = 1050401;
  NIDMM_ATTRIBUTE_INSTRUMENT_FIRMWARE_REVISION = 1050510;
  NIDMM_ATTRIBUTE_INSTRUMENT_MANUFACTURER = 1050511;
  NIDMM_ATTRIBUTE_INSTRUMENT_MODEL = 1050512;
  NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_VENDOR = 1050513;
  NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_DESCRIPTION = 1050514;
  NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION = 1050515;
  NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION = 1050516;
  NIDMM_ATTRIBUTE_CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION = 1050519;
  NIDMM_ATTRIBUTE_CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION = 1050520;
  NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_REVISION = 1050551;
  NIDMM_ATTRIBUTE_MEAS_DEST_SLOPE = 1150002;
  NIDMM_ATTRIBUTE_SHUNT_VALUE = 1150003;
  NIDMM_ATTRIBUTE_SAMPLE_TRIGGER_SLOPE = 1150010;
  NIDMM_ATTRIBUTE_OPERATION_MODE = 1150014;
  NIDMM_ATTRIBUTE_WAVEFORM_RATE = 1150018;
  NIDMM_ATTRIBUTE_WAVEFORM_POINTS = 1150019;
  NIDMM_ATTRIBUTE_ADC_CALIBRATION = 1150022;
  NIDMM_ATTRIBUTE_OFFSET_COMP_OHMS = 1150023;
  NIDMM_ATTRIBUTE_CURRENT_SOURCE = 1150025;
  NIDMM_ATTRIBUTE_DC_NOISE_REJECTION = 1150026;
  NIDMM_ATTRIBUTE_WAVEFORM_COUPLING = 1150027;
  NIDMM_ATTRIBUTE_SETTLE_TIME = 1150028;
  NIDMM_ATTRIBUTE_INPUT_RESISTANCE = 1150029;
  NIDMM_ATTRIBUTE_NUMBER_OF_AVERAGES = 1150032;
  NIDMM_ATTRIBUTE_LATENCY = 1150034;
  NIDMM_ATTRIBUTE_BUFFER_SIZE = 1150037;
  NIDMM_ATTRIBUTE_FREQ_VOLTAGE_AUTO_RANGE_VALUE = 1150044;
  NIDMM_ATTRIBUTE_CABLE_COMP_TYPE = 1150045;
  NIDMM_ATTRIBUTE_SHORT_CABLE_COMP_REACTANCE = 1150046;
  NIDMM_ATTRIBUTE_SHORT_CABLE_COMP_RESISTANCE = 1150047;
  NIDMM_ATTRIBUTE_OPEN_CABLE_COMP_SUSCEPTANCE = 1150048;
  NIDMM_ATTRIBUTE_OPEN_CABLE_COMP_CONDUCTANCE = 1150049;
  NIDMM_ATTRIBUTE_LC_CALCULATION_MODEL = 1150052;
  NIDMM_ATTRIBUTE_DC_BIAS = 1150053;
  NIDMM_ATTRIBUTE_SERIAL_NUMBER = 1150054;
  NIDMM_ATTRIBUTE_LC_NUMBER_MEAS_TO_AVERAGE = 1150055;
  NIDMM_ATTRIBUTE_CONFIG_PRODUCT_NUMBER = 1150061;
  NIDMM_ATTRIBUTE_TEMP_RTD_TYPE = 1150120;
  NIDMM_ATTRIBUTE_TEMP_RTD_A = 1150121;
  NIDMM_ATTRIBUTE_TEMP_RTD_B = 1150122;
  NIDMM_ATTRIBUTE_TEMP_RTD_C = 1150123;
  NIDMM_ATTRIBUTE_TEMP_THERMISTOR_TYPE = 1150124;
  NIDMM_ATTRIBUTE_TEMP_THERMISTOR_A = 1150125;
  NIDMM_ATTRIBUTE_TEMP_THERMISTOR_B = 1150126;
  NIDMM_ATTRIBUTE_TEMP_THERMISTOR_C = 1150127;
  NIDMM_ATTRIBUTE_FUNCTION = 1250001;
  NIDMM_ATTRIBUTE_RANGE = 1250002;
  NIDMM_ATTRIBUTE_RESOLUTION_DIGITS = 1250003;
  NIDMM_ATTRIBUTE_TRIGGER_SOURCE = 1250004;
  NIDMM_ATTRIBUTE_TRIGGER_DELAY = 1250005;
  NIDMM_ATTRIBUTE_AC_MIN_FREQ = 1250006;
  NIDMM_ATTRIBUTE_AC_MAX_FREQ = 1250007;
  NIDMM_ATTRIBUTE_RESOLUTION_ABSOLUTE = 1250008;
  NIDMM_ATTRIBUTE_FREQ_VOLTAGE_RANGE = 1250101;
  NIDMM_ATTRIBUTE_TEMP_TRANSDUCER_TYPE = 1250201;
  NIDMM_ATTRIBUTE_TEMP_TC_TYPE = 1250231;
  NIDMM_ATTRIBUTE_TEMP_TC_REF_JUNC_TYPE = 1250232;
  NIDMM_ATTRIBUTE_TEMP_TC_FIXED_REF_JUNC = 1250233;
  NIDMM_ATTRIBUTE_TEMP_RTD_RES = 1250242;
  NIDMM_ATTRIBUTE_SAMPLE_COUNT = 1250301;
  NIDMM_ATTRIBUTE_SAMPLE_TRIGGER = 1250302;
  NIDMM_ATTRIBUTE_SAMPLE_INTERVAL = 1250303;
  NIDMM_ATTRIBUTE_TRIGGER_COUNT = 1250304;
  NIDMM_ATTRIBUTE_MEAS_COMPLETE_DEST = 1250305;
  NIDMM_ATTRIBUTE_APERTURE_TIME = 1250321;
  NIDMM_ATTRIBUTE_APERTURE_TIME_UNITS = 1250322;
  NIDMM_ATTRIBUTE_AUTO_RANGE_VALUE = 1250331;
  NIDMM_ATTRIBUTE_AUTO_ZERO = 1250332;
  NIDMM_ATTRIBUTE_POWERLINE_FREQ = 1250333;
  NIDMM_ATTRIBUTE_TRIGGER_SLOPE = 1250334;
}

enum AcquisitionStatus {
  ACQUISITION_STATUS_NIDMM_VAL_RUNNING_ANTICOLLISION = 0;
  ACQUISITION_STATUS_NIDMM_VAL_FINISHED_WITH_BACKLOG = 1;
  ACQUISITION_STATUS_NIDMM_VAL_FINISHED_WITH_NO_BACKLOG = 2;
  ACQUISITION_STATUS_NIDMM_VAL_PAUSED = 3;
  ACQUISITION_STATUS_NIDMM_VAL_NO_ACQUISITION_IN_PROGRESS = 4;
}

enum ApertureTime {
  APERTURE_TIME_UNSPECIFIED = 0;
  APERTURE_TIME_NIDMM_VAL_APERTURE_TIME_AUTO = -1;
  APERTURE_TIME_NIDMM_VAL_1_PLC = 1;
  APERTURE_TIME_NIDMM_VAL_5_PLC = 5;
  APERTURE_TIME_NIDMM_VAL_6_PLC = 6;
  APERTURE_TIME_NIDMM_VAL_10_PLC = 10;
  APERTURE_TIME_NIDMM_VAL_12_PLC = 12;
  APERTURE_TIME_NIDMM_VAL_100_PLC = 100;
  APERTURE_TIME_NIDMM_VAL_120_PLC = 120;
}

enum ApertureTimeUnits {
  APERTURE_TIME_UNITS_NIDMM_VAL_SECONDS = 0;
  APERTURE_TIME_UNITS_NIDMM_VAL_POWER_LINE_CYCLES = 1;
}

enum CalibrationType {
  CALIBRATION_TYPE_NIDMM_VAL_INTERNAL_AREA = 0;
  CALIBRATION_TYPE_NIDMM_VAL_EXTERNAL_AREA = 1;
}

enum CompensatedOhms {
  COMPENSATED_OHMS_NIDMM_VAL_OFFSET_COMP_OHMS_OFF = 0;
  COMPENSATED_OHMS_NIDMM_VAL_OFFSET_COMP_OHMS_ON = 1;
}

enum ControlCommit {
  CONTROL_COMMIT_NIDMM_VAL_CONTROL_COMMIT = 0;
}

enum FrequencyVoltageRange {
  FREQUENCY_VOLTAGE_RANGE_UNSPECIFIED = 0;
  FREQUENCY_VOLTAGE_RANGE_NIDMM_VAL_AUTO_RANGE_ON = -1;
  FREQUENCY_VOLTAGE_RANGE_NIDMM_VAL_AUTO_RANGE_OFF = -2;
}

enum Function {
  FUNCTION_UNSPECIFIED = 0;
  FUNCTION_NIDMM_VAL_DC_VOLTS = 1;
  FUNCTION_NIDMM_VAL_AC_VOLTS = 2;
  FUNCTION_NIDMM_VAL_DC_CURRENT = 3;
  FUNCTION_NIDMM_VAL_AC_CURRENT = 4;
  FUNCTION_NIDMM_VAL_2_WIRE_RES = 5;
  FUNCTION_NIDMM_VAL_4_WIRE_RES = 101;
  FUNCTION_NIDMM_VAL_FREQ = 104;
  FUNCTION_NIDMM_VAL_PERIOD = 105;
  FUNCTION_NIDMM_VAL_TEMPERATURE = 108;
  FUNCTION_NIDMM_VAL_AC_VOLTS_DC_COUPLED = 1001;
  FUNCTION_NIDMM_VAL_DIODE = 1002;
  FUNCTION_NIDMM_VAL_WAVEFORM_VOLTAGE = 1003;
  FUNCTION_NIDMM_VAL_WAVEFORM_CURRENT = 1004;
  FUNCTION_NIDMM_VAL_CAPACITANCE = 1005;
  FUNCTION_NIDMM_VAL_INDUCTANCE = 1006;
}

enum NiDmmInt32AttributeValues {
  option allow_alias = true;
  NIDMM_INT32_UNSPECIFIED = 0;
  NIDMM_INT32_ADC_CALIBRATION_VAL_ADC_CALIBRATION_OFF = 0;
  NIDMM_INT32_ADC_CALIBRATION_VAL_ADC_CALIBRATION_AUTO = -1;
  NIDMM_INT32_ADC_CALIBRATION_VAL_ADC_CALIBRATION_ON = 1;
  NIDMM_INT32_APERTURE_TIME_UNITS_VAL_SECONDS = 0;
  NIDMM_INT32_APERTURE_TIME_UNITS_VAL_POWER_LINE_CYCLES = 1;
  NIDMM_INT32_AUTO_ZERO_VAL_AUTO_ZERO_OFF = 0;
  NIDMM_INT32_AUTO_ZERO_VAL_AUTO_ZERO_AUTO = -1;
  NIDMM_INT32_AUTO_ZERO_VAL_AUTO_ZERO_ON = 1;
  NIDMM_INT32_AUTO_ZERO_VAL_AUTO_ZERO_ONCE = 2;
  NIDMM_INT32_BUFFER_SIZE_VAL_BUFFER_SIZE_AUTO = -1;
  NIDMM_INT32_CABLE_COMPENSATION_TYPE_VAL_CABLE_COMP_NONE = 0;
  NIDMM_INT32_CABLE_COMPENSATION_TYPE_VAL_CABLE_COMP_OPEN = 1;
  NIDMM_INT32_CABLE_COMPENSATION_TYPE_VAL_CABLE_COMP_SHORT = 2;
  NIDMM_INT32_CABLE_COMPENSATION_TYPE_VAL_CABLE_COMP_OPEN_AND_SHORT = 3;
  NIDMM_INT32_COMPENSATED_OHMS_VAL_OFFSET_COMP_OHMS_OFF = 0;
  NIDMM_INT32_COMPENSATED_OHMS_VAL_OFFSET_COMP_OHMS_ON = 1;
  NIDMM_INT32_DC_BIAS_VAL_DC_BIAS_OFF = 0;
  NIDMM_INT32_DC_BIAS_VAL_DC_BIAS_ON = 1;
  NIDMM_INT32_DC_NOISE_REJECTION_VAL_DCNR_NORMAL = 0;
  NIDMM_INT32_DC_NOISE_REJECTION_VAL_DCNR_AUTO = -1;
  NIDMM_INT32_DC_NOISE_REJECTION_VAL_DCNR_SECOND_ORDER = 1;
  NIDMM_INT32_DC_NOISE_REJECTION_VAL_DCNR_HIGH_ORDER = 2;
  NIDMM_INT32_FUNCTION_VAL_DC_VOLTS = 1;
  NIDMM_INT32_FUNCTION_VAL_AC_VOLTS = 2;
  NIDMM_INT32_FUNCTION_VAL_DC_CURRENT = 3;
  NIDMM_INT32_FUNCTION_VAL_AC_CURRENT = 4;
  NIDMM_INT32_FUNCTION_VAL_2_WIRE_RES = 5;
  NIDMM_INT32_FUNCTION_VAL_4_WIRE_RES = 101;
  NIDMM_INT32_FUNCTION_VAL_FREQ = 104;
  NIDMM_INT32_FUNCTION_VAL_PERIOD = 105;
  NIDMM_INT32_FUNCTION_VAL_TEMPERATURE = 108;
  NIDMM_INT32_FUNCTION_VAL_AC_VOLTS_DC_COUPLED = 1001;
  NIDMM_INT32_FUNCTION_VAL_DIODE = 1002;
  NIDMM_INT32_FUNCTION_VAL_WAVEFORM_VOLTAGE = 1003;
  NIDMM_INT32_FUNCTION_VAL_WAVEFORM_CURRENT = 1004;
  NIDMM_INT32_FUNCTION_VAL_CAPACITANCE = 1005;
  NIDMM_INT32_FUNCTION_VAL_INDUCTANCE = 1006;
  NIDMM_INT32_LATENCY_VAL_LATENCY_AUTO = -1;
  NIDMM_INT32_LC_CALCULATION_MODEL_VAL_CALC_MODEL_SERIES = 0;
  NIDMM_INT32_LC_CALCULATION_MODEL_VAL_CALC_MODEL_AUTO = -1;
  NIDMM_INT32_LC_CALCULATION_MODEL_VAL_CALC_MODEL_PARALLEL = 1;
  NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_NONE = -1;
  NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_EXTERNAL = 2;
  NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG0 = 111;
  NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG1 = 112;
  NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG2 = 113;
  NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG3 = 114;
  NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG4 = 115;
  NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG5 = 116;
  NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG6 = 117;
  NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG7 = 118;
  NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_LBR_TRIG0 = 1003;
  NIDMM_INT32_MEASUREMENT_DESTINATION_SLOPE_VAL_POSITIVE = 0;
  NIDMM_INT32_MEASUREMENT_DESTINATION_SLOPE_VAL_NEGATIVE = 1;
  NIDMM_INT32_OPERATION_MODE_VAL_IVIDMM_MODE = 0;
  NIDMM_INT32_OPERATION_MODE_VAL_WAVEFORM_MODE = 1;
  NIDMM_INT32_RTD_TYPE_VAL_TEMP_RTD_CUSTOM = 0;
  NIDMM_INT32_RTD_TYPE_VAL_TEMP_RTD_PT3750 = 1;
  NIDMM_INT32_RTD_TYPE_VAL_TEMP_RTD_PT3851 = 2;
  NIDMM_INT32_RTD_TYPE_VAL_TEMP_RTD_PT3911 = 3;
  NIDMM_INT32_RTD_TYPE_VAL_TEMP_RTD_PT3916 = 4;
  NIDMM_INT32_RTD_TYPE_VAL_TEMP_RTD_PT3920 = 5;
  NIDMM_INT32_RTD_TYPE_VAL_TEMP_RTD_PT3928 = 6;
  NIDMM_INT32_SAMPLE_COUNT_VAL_SAMPLE_COUNT_INFINITE = 0;
  NIDMM_INT32_SAMPLE_TRIG_SLOPE_VAL_POSITIVE = 0;
  NIDMM_INT32_SAMPLE_TRIG_SLOPE_VAL_NEGATIVE = 1;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_IMMEDIATE = 1;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_EXTERNAL = 2;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_SOFTWARE_TRIG = 3;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_INTERVAL = 10;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG0 = 111;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG1 = 112;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG2 = 113;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG3 = 114;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG4 = 115;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG5 = 116;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG6 = 117;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG7 = 118;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_STAR = 131;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_AUX_TRIG1 = 1001;
  NIDMM_INT32_SAMPLE_TRIGGER_VAL_LBR_TRIG1 = 1004;
  NIDMM_INT32_THERMISTOR_TYPE_VAL_TEMP_THERMISTOR_CUSTOM = 0;
  NIDMM_INT32_THERMISTOR_TYPE_VAL_TEMP_THERMISTOR_44004 = 1;
  NIDMM_INT32_THERMISTOR_TYPE_VAL_TEMP_THERMISTOR_44006 = 2;
  NIDMM_INT32_THERMISTOR_TYPE_VAL_TEMP_THERMISTOR_44007 = 3;
  NIDMM_INT32_THERMOCOUPLE_REFERENCE_JUNCTION_TYPE_VAL_TEMP_REF_JUNC_FIXED = 2;
  NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_B = 1;
  NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_E = 4;
  NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_J = 6;
  NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_K = 7;
  NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_N = 8;
  NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_R = 9;
  NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_S = 10;
  NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_T = 11;
  NIDMM_INT32_TRANSDUCER_TYPE_VAL_THERMOCOUPLE = 1;
  NIDMM_INT32_TRANSDUCER_TYPE_VAL_THERMISTOR = 2;
  NIDMM_INT32_TRANSDUCER_TYPE_VAL_2_WIRE_RTD = 3;
  NIDMM_INT32_TRANSDUCER_TYPE_VAL_4_WIRE_RTD = 4;
  NIDMM_INT32_TRIGGER_COUNT_VAL_TRIG_COUNT_INFINITE = 0;
  NIDMM_INT32_TRIGGER_SLOPE_VAL_POSITIVE = 0;
  NIDMM_INT32_TRIGGER_SLOPE_VAL_NEGATIVE = 1;
  NIDMM_INT32_TRIGGER_SOURCE_VAL_IMMEDIATE = 1;
  NIDMM_INT32_TRIGGER_SOURCE_VAL_EXTERNAL = 2;
  NIDMM_INT32_TRIGGER_SOURCE_VAL_SOFTWARE_TRIG = 3;
  NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG0 = 111;
  NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG1 = 112;
  NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG2 = 113;
  NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG3 = 114;
  NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG4 = 115;
  NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG5 = 116;
  NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG6 = 117;
  NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG7 = 118;
  NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_STAR = 131;
  NIDMM_INT32_TRIGGER_SOURCE_VAL_AUX_TRIG1 = 1001;
  NIDMM_INT32_TRIGGER_SOURCE_VAL_LBR_TRIG1 = 1004;
  NIDMM_INT32_WAVEFORM_COUPLING_VAL_WAVEFORM_COUPLING_AC = 0;
  NIDMM_INT32_WAVEFORM_COUPLING_VAL_WAVEFORM_COUPLING_DC = 1;
}

enum NiDmmReal64AttributeValues {
  option allow_alias = true;
  NIDMM_REAL64_UNSPECIFIED = 0;
  NIDMM_REAL64_APERTURE_TIME_VAL_APERTURE_TIME_AUTO = -1;
  NIDMM_REAL64_APERTURE_TIME_VAL_1_PLC = 1;
  NIDMM_REAL64_APERTURE_TIME_VAL_5_PLC = 5;
  NIDMM_REAL64_APERTURE_TIME_VAL_6_PLC = 6;
  NIDMM_REAL64_APERTURE_TIME_VAL_10_PLC = 10;
  NIDMM_REAL64_APERTURE_TIME_VAL_12_PLC = 12;
  NIDMM_REAL64_APERTURE_TIME_VAL_100_PLC = 100;
  NIDMM_REAL64_APERTURE_TIME_VAL_120_PLC = 120;
  NIDMM_REAL64_FREQUENCY_VOLTAGE_RANGE_VAL_AUTO_RANGE_ON = -1;
  NIDMM_REAL64_FREQUENCY_VOLTAGE_RANGE_VAL_AUTO_RANGE_OFF = -2;
  NIDMM_REAL64_POWER_LINE_FREQUENCIES_VAL_50_HERTZ = 50;
  NIDMM_REAL64_POWER_LINE_FREQUENCIES_VAL_60_HERTZ = 60;
  NIDMM_REAL64_RANGE_VAL_AUTO_RANGE_ON = -1;
  NIDMM_REAL64_RANGE_VAL_AUTO_RANGE_OFF = -2;
  NIDMM_REAL64_RANGE_VAL_AUTO_RANGE_ONCE = -3;
  NIDMM_REAL64_SAMPLE_INTERVAL_VAL_AUTO_DELAY = -1;
  NIDMM_REAL64_SETTLE_TIME_VAL_SETTLE_TIME_AUTO = -1;
  NIDMM_REAL64_TRIGGER_DELAYS_VAL_AUTO_DELAY = -1;
  NIDMM_REAL64_TRIGGER_DELAYS_VAL_AUTO_DELAY_ON = -1;
  NIDMM_REAL64_TRIGGER_DELAYS_VAL_AUTO_DELAY_OFF = -2;
}

enum NiDmmReal64AttributeValuesMapped {
  NIDMM_REAL64_MAPPED_UNSPECIFIED = 0;
  NIDMM_REAL64_CURRENT_SOURCE_VAL_1_MICROAMP = 1;
  NIDMM_REAL64_CURRENT_SOURCE_VAL_10_MICROAMP = 2;
  NIDMM_REAL64_CURRENT_SOURCE_VAL_100_MICROAMP = 3;
  NIDMM_REAL64_CURRENT_SOURCE_VAL_1_MILLIAMP = 4;
  NIDMM_REAL64_INPUT_RESISTANCE_VAL_RESISTANCE_NA = 5;
  NIDMM_REAL64_INPUT_RESISTANCE_VAL_1_MEGAOHM = 6;
  NIDMM_REAL64_INPUT_RESISTANCE_VAL_10_MEGAOHM = 7;
  NIDMM_REAL64_INPUT_RESISTANCE_VAL_GREATER_THAN_10_GIGAOHM = 8;
}

enum PowerLineFrequencies {
  POWER_LINE_FREQUENCIES_UNSPECIFIED = 0;
  POWER_LINE_FREQUENCIES_NIDMM_VAL_50_HERTZ = 50;
  POWER_LINE_FREQUENCIES_NIDMM_VAL_60_HERTZ = 60;
}

enum RtdType {
  RTD_TYPE_NIDMM_VAL_TEMP_RTD_CUSTOM = 0;
  RTD_TYPE_NIDMM_VAL_TEMP_RTD_PT3750 = 1;
  RTD_TYPE_NIDMM_VAL_TEMP_RTD_PT3851 = 2;
  RTD_TYPE_NIDMM_VAL_TEMP_RTD_PT3911 = 3;
  RTD_TYPE_NIDMM_VAL_TEMP_RTD_PT3916 = 4;
  RTD_TYPE_NIDMM_VAL_TEMP_RTD_PT3920 = 5;
  RTD_TYPE_NIDMM_VAL_TEMP_RTD_PT3928 = 6;
}

enum SampleCount {
  SAMPLE_COUNT_NIDMM_VAL_SAMPLE_COUNT_INFINITE = 0;
}

enum SampleInterval {
  SAMPLE_INTERVAL_UNSPECIFIED = 0;
  SAMPLE_INTERVAL_NIDMM_VAL_AUTO_DELAY = -1;
}

enum SampleTrigSlope {
  SAMPLE_TRIG_SLOPE_NIDMM_VAL_POSITIVE = 0;
  SAMPLE_TRIG_SLOPE_NIDMM_VAL_NEGATIVE = 1;
}

enum SampleTrigger {
  SAMPLE_TRIGGER_UNSPECIFIED = 0;
  SAMPLE_TRIGGER_NIDMM_VAL_IMMEDIATE = 1;
  SAMPLE_TRIGGER_NIDMM_VAL_EXTERNAL = 2;
  SAMPLE_TRIGGER_NIDMM_VAL_SOFTWARE_TRIG = 3;
  SAMPLE_TRIGGER_NIDMM_VAL_INTERVAL = 10;
  SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG0 = 111;
  SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG1 = 112;
  SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG2 = 113;
  SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG3 = 114;
  SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG4 = 115;
  SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG5 = 116;
  SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG6 = 117;
  SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG7 = 118;
  SAMPLE_TRIGGER_NIDMM_VAL_PXI_STAR = 131;
  SAMPLE_TRIGGER_NIDMM_VAL_AUX_TRIG1 = 1001;
  SAMPLE_TRIGGER_NIDMM_VAL_LBR_TRIG1 = 1004;
}

enum ThermocoupleReferenceJunctionType {
  THERMOCOUPLE_REFERENCE_JUNCTION_TYPE_UNSPECIFIED = 0;
  THERMOCOUPLE_REFERENCE_JUNCTION_TYPE_NIDMM_VAL_TEMP_REF_JUNC_FIXED = 2;
}

enum ThermocoupleType {
  THERMOCOUPLE_TYPE_UNSPECIFIED = 0;
  THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_B = 1;
  THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_E = 4;
  THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_J = 6;
  THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_K = 7;
  THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_N = 8;
  THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_R = 9;
  THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_S = 10;
  THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_T = 11;
}

enum TimeLimit {
  TIME_LIMIT_UNSPECIFIED = 0;
  TIME_LIMIT_NIDMM_VAL_TIME_LIMIT_AUTO = -1;
}

enum TriggerCount {
  TRIGGER_COUNT_NIDMM_VAL_TRIG_COUNT_INFINITE = 0;
}

enum TriggerDelays {
  option allow_alias = true;
  TRIGGER_DELAYS_UNSPECIFIED = 0;
  TRIGGER_DELAYS_NIDMM_VAL_AUTO_DELAY = -1;
  TRIGGER_DELAYS_NIDMM_VAL_AUTO_DELAY_ON = -1;
  TRIGGER_DELAYS_NIDMM_VAL_AUTO_DELAY_OFF = -2;
}

enum TriggerSlope {
  TRIGGER_SLOPE_NIDMM_VAL_POSITIVE = 0;
  TRIGGER_SLOPE_NIDMM_VAL_NEGATIVE = 1;
}

enum TriggerSource {
  TRIGGER_SOURCE_UNSPECIFIED = 0;
  TRIGGER_SOURCE_NIDMM_VAL_IMMEDIATE = 1;
  TRIGGER_SOURCE_NIDMM_VAL_EXTERNAL = 2;
  TRIGGER_SOURCE_NIDMM_VAL_SOFTWARE_TRIG = 3;
  TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG0 = 111;
  TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG1 = 112;
  TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG2 = 113;
  TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG3 = 114;
  TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG4 = 115;
  TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG5 = 116;
  TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG6 = 117;
  TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG7 = 118;
  TRIGGER_SOURCE_NIDMM_VAL_PXI_STAR = 131;
  TRIGGER_SOURCE_NIDMM_VAL_AUX_TRIG1 = 1001;
  TRIGGER_SOURCE_NIDMM_VAL_LBR_TRIG1 = 1004;
}

message AbortRequest {
  nidevice_grpc.Session vi = 1;
}

message AbortResponse {
  int32 status = 1;
}

message CheckAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
  bool attribute_value = 4;
}

message CheckAttributeViBooleanResponse {
  int32 status = 1;
}

message CheckAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
  oneof attribute_value_enum {
    NiDmmInt32AttributeValues attribute_value = 4;
    sint32 attribute_value_raw = 5;
  }
}

message CheckAttributeViInt32Response {
  int32 status = 1;
}

message CheckAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
  oneof attribute_value_enum {
    NiDmmReal64AttributeValues attribute_value = 4;
    double attribute_value_raw = 5;
    NiDmmReal64AttributeValuesMapped attribute_value_mapped = 6;
  }
}

message CheckAttributeViReal64Response {
  int32 status = 1;
}

message CheckAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
  nidevice_grpc.Session attribute_value = 4;
}

message CheckAttributeViSessionResponse {
  int32 status = 1;
}

message CheckAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
  string attribute_value_raw = 4;
}

message CheckAttributeViStringResponse {
  int32 status = 1;
}

message ClearErrorRequest {
  nidevice_grpc.Session vi = 1;
}

message ClearErrorResponse {
  int32 status = 1;
}

message ClearInterchangeWarningsRequest {
  nidevice_grpc.Session vi = 1;
}

message ClearInterchangeWarningsResponse {
  int32 status = 1;
}

message CloseRequest {
  nidevice_grpc.Session vi = 1;
}

message CloseResponse {
  int32 status = 1;
}

message ConfigureACBandwidthRequest {
  nidevice_grpc.Session vi = 1;
  double ac_minimum_frequency_hz = 2;
  double ac_maximum_frequency_hz = 3;
}

message ConfigureACBandwidthResponse {
  int32 status = 1;
}

message ConfigureADCCalibrationRequest {
  nidevice_grpc.Session vi = 1;
  sint32 adc_calibration = 2;
}

message ConfigureADCCalibrationResponse {
  int32 status = 1;
}

message ConfigureAutoZeroModeRequest {
  nidevice_grpc.Session vi = 1;
  sint32 auto_zero_mode = 2;
}

message ConfigureAutoZeroModeResponse {
  int32 status = 1;
}

message ConfigureCableCompTypeRequest {
  nidevice_grpc.Session vi = 1;
  sint32 cable_comp_type = 2;
}

message ConfigureCableCompTypeResponse {
  int32 status = 1;
}

message ConfigureCurrentSourceRequest {
  nidevice_grpc.Session vi = 1;
  double current_source = 2;
}

message ConfigureCurrentSourceResponse {
  int32 status = 1;
}

message ConfigureFixedRefJunctionRequest {
  nidevice_grpc.Session vi = 1;
  double fixed_reference_junction = 2;
}

message ConfigureFixedRefJunctionResponse {
  int32 status = 1;
}

message ConfigureFrequencyVoltageRangeRequest {
  nidevice_grpc.Session vi = 1;
  oneof voltage_range_enum {
    FrequencyVoltageRange voltage_range = 2;
    double voltage_range_raw = 3;
  }
}

message ConfigureFrequencyVoltageRangeResponse {
  int32 status = 1;
}

message ConfigureMeasCompleteDestRequest {
  nidevice_grpc.Session vi = 1;
  sint32 meas_complete_destination = 2;
}

message ConfigureMeasCompleteDestResponse {
  int32 status = 1;
}

message ConfigureMeasCompleteSlopeRequest {
  nidevice_grpc.Session vi = 1;
  sint32 meas_complete_slope = 2;
}

message ConfigureMeasCompleteSlopeResponse {
  int32 status = 1;
}

message ConfigureMeasurementAbsoluteRequest {
  nidevice_grpc.Session vi = 1;
  oneof measurement_function_enum {
    Function measurement_function = 2;
    sint32 measurement_function_raw = 3;
  }
  double range = 4;
  double resolution_absolute = 5;
}

message ConfigureMeasurementAbsoluteResponse {
  int32 status = 1;
}

message ConfigureMeasurementDigitsRequest {
  nidevice_grpc.Session vi = 1;
  oneof measurement_function_enum {
    Function measurement_function = 2;
    sint32 measurement_function_raw = 3;
  }
  double range = 4;
  double resolution_digits = 5;
}

message ConfigureMeasurementDigitsResponse {
  int32 status = 1;
}

message ConfigureMultiPointRequest {
  nidevice_grpc.Session vi = 1;
  oneof trigger_count_enum {
    TriggerCount trigger_count = 2;
    sint32 trigger_count_raw = 3;
  }
  oneof sample_count_enum {
    SampleCount sample_count = 4;
    sint32 sample_count_raw = 5;
  }
  oneof sample_trigger_enum {
    SampleTrigger sample_trigger = 6;
    sint32 sample_trigger_raw = 7;
  }
  oneof sample_interval_enum {
    SampleInterval sample_interval = 8;
    double sample_interval_raw = 9;
  }
}

message ConfigureMultiPointResponse {
  int32 status = 1;
}

message ConfigureOffsetCompOhmsRequest {
  nidevice_grpc.Session vi = 1;
  oneof offset_comp_ohms_enum {
    CompensatedOhms offset_comp_ohms = 2;
    sint32 offset_comp_ohms_raw = 3;
  }
}

message ConfigureOffsetCompOhmsResponse {
  int32 status = 1;
}

message ConfigureOpenCableCompValuesRequest {
  nidevice_grpc.Session vi = 1;
  double conductance = 2;
  double susceptance = 3;
}

message ConfigureOpenCableCompValuesResponse {
  int32 status = 1;
}

message ConfigurePowerLineFrequencyRequest {
  nidevice_grpc.Session vi = 1;
  oneof power_line_frequency_hz_enum {
    PowerLineFrequencies power_line_frequency_hz = 2;
    double power_line_frequency_hz_raw = 3;
  }
}

message ConfigurePowerLineFrequencyResponse {
  int32 status = 1;
}

message ConfigureRTDCustomRequest {
  nidevice_grpc.Session vi = 1;
  double rtd_a = 2;
  double rtd_b = 3;
  double rtd_c = 4;
}

message ConfigureRTDCustomResponse {
  int32 status = 1;
}

message ConfigureRTDTypeRequest {
  nidevice_grpc.Session vi = 1;
  oneof rtd_type_enum {
    RtdType rtd_type = 2;
    sint32 rtd_type_raw = 3;
  }
  double rtd_resistance = 4;
}

message ConfigureRTDTypeResponse {
  int32 status = 1;
}

message ConfigureSampleTriggerSlopeRequest {
  nidevice_grpc.Session vi = 1;
  oneof sample_trigger_slope_enum {
    SampleTrigSlope sample_trigger_slope = 2;
    sint32 sample_trigger_slope_raw = 3;
  }
}

message ConfigureSampleTriggerSlopeResponse {
  int32 status = 1;
}

message ConfigureShortCableCompValuesRequest {
  nidevice_grpc.Session vi = 1;
  double resistance = 2;
  double reactance = 3;
}

message ConfigureShortCableCompValuesResponse {
  int32 status = 1;
}

message ConfigureThermistorCustomRequest {
  nidevice_grpc.Session vi = 1;
  double thermistor_a = 2;
  double thermistor_b = 3;
  double thermistor_c = 4;
}

message ConfigureThermistorCustomResponse {
  int32 status = 1;
}

message ConfigureThermistorTypeRequest {
  nidevice_grpc.Session vi = 1;
  sint32 thermistor_type = 2;
}

message ConfigureThermistorTypeResponse {
  int32 status = 1;
}

message ConfigureThermocoupleRequest {
  nidevice_grpc.Session vi = 1;
  oneof thermocouple_type_enum {
    ThermocoupleType thermocouple_type = 2;
    sint32 thermocouple_type_raw = 3;
  }
  oneof reference_junction_type_enum {
    ThermocoupleReferenceJunctionType reference_junction_type = 4;
    sint32 reference_junction_type_raw = 5;
  }
}

message ConfigureThermocoupleResponse {
  int32 status = 1;
}

message ConfigureTransducerTypeRequest {
  nidevice_grpc.Session vi = 1;
  sint32 transducer_type = 2;
}

message ConfigureTransducerTypeResponse {
  int32 status = 1;
}

message ConfigureTriggerRequest {
  nidevice_grpc.Session vi = 1;
  oneof trigger_source_enum {
    TriggerSource trigger_source = 2;
    sint32 trigger_source_raw = 3;
  }
  oneof trigger_delay_enum {
    TriggerDelays trigger_delay = 4;
    double trigger_delay_raw = 5;
  }
}

message ConfigureTriggerResponse {
  int32 status = 1;
}

message ConfigureTriggerSlopeRequest {
  nidevice_grpc.Session vi = 1;
  oneof trigger_slope_enum {
    TriggerSlope trigger_slope = 2;
    sint32 trigger_slope_raw = 3;
  }
}

message ConfigureTriggerSlopeResponse {
  int32 status = 1;
}

message ConfigureWaveformAcquisitionRequest {
  nidevice_grpc.Session vi = 1;
  oneof measurement_function_enum {
    Function measurement_function = 2;
    sint32 measurement_function_raw = 3;
  }
  double range = 4;
  double rate = 5;
  sint32 waveform_points = 6;
}

message ConfigureWaveformAcquisitionResponse {
  int32 status = 1;
}

message ConfigureWaveformCouplingRequest {
  nidevice_grpc.Session vi = 1;
  sint32 waveform_coupling = 2;
}

message ConfigureWaveformCouplingResponse {
  int32 status = 1;
}

message ControlRequest {
  nidevice_grpc.Session vi = 1;
  oneof control_action_enum {
    ControlCommit control_action = 2;
    sint32 control_action_raw = 3;
  }
}

message ControlResponse {
  int32 status = 1;
}

message DisableRequest {
  nidevice_grpc.Session vi = 1;
}

message DisableResponse {
  int32 status = 1;
}

message ExportAttributeConfigurationBufferRequest {
  nidevice_grpc.Session vi = 1;
}

message ExportAttributeConfigurationBufferResponse {
  int32 status = 1;
  bytes configuration = 2;
}

message ExportAttributeConfigurationFileRequest {
  nidevice_grpc.Session vi = 1;
  string file_path = 2;
}

message ExportAttributeConfigurationFileResponse {
  int32 status = 1;
}

message FetchRequest {
  nidevice_grpc.Session vi = 1;
  oneof maximum_time_enum {
    TimeLimit maximum_time = 2;
    sint32 maximum_time_raw = 3;
  }
}

message FetchResponse {
  int32 status = 1;
  double reading = 2;
}

message FetchMultiPointRequest {
  nidevice_grpc.Session vi = 1;
  oneof maximum_time_enum {
    TimeLimit maximum_time = 2;
    sint32 maximum_time_raw = 3;
  }
  sint32 array_size = 4;
}

message FetchMultiPointResponse {
  int32 status = 1;
  repeated double reading_array = 2;
  sint32 actual_number_of_points = 3;
}

message FetchWaveformRequest {
  nidevice_grpc.Session vi = 1;
  oneof maximum_time_enum {
    TimeLimit maximum_time = 2;
    sint32 maximum_time_raw = 3;
  }
  sint32 array_size = 4;
}

message FetchWaveformResponse {
  int32 status = 1;
  repeated double waveform_array = 2;
  sint32 actual_number_of_points = 3;
}

message GetApertureTimeInfoRequest {
  nidevice_grpc.Session vi = 1;
}

message GetApertureTimeInfoResponse {
  int32 status = 1;
  ApertureTime aperture_time = 2;
  double aperture_time_raw = 3;
  ApertureTimeUnits aperture_time_units = 4;
  sint32 aperture_time_units_raw = 5;
}

message GetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
}

message GetAttributeViBooleanResponse {
  int32 status = 1;
  bool attribute_value = 2;
}

message GetAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
}

message GetAttributeViInt32Response {
  int32 status = 1;
  sint32 attribute_value = 2;
}

message GetAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
}

message GetAttributeViReal64Response {
  int32 status = 1;
  double attribute_value = 2;
}

message GetAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
}

message GetAttributeViSessionResponse {
  int32 status = 1;
  nidevice_grpc.Session attribute_value = 2;
}

message GetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
}

message GetAttributeViStringResponse {
  int32 status = 1;
  string attribute_value = 2;
}

message GetAutoRangeValueRequest {
  nidevice_grpc.Session vi = 1;
}

message GetAutoRangeValueResponse {
  int32 status = 1;
  double actual_range = 2;
}

message GetCalDateAndTimeRequest {
  nidevice_grpc.Session vi = 1;
  oneof cal_type_enum {
    CalibrationType cal_type = 2;
    sint32 cal_type_raw = 3;
  }
}

message GetCalDateAndTimeResponse {
  int32 status = 1;
  sint32 month = 2;
  sint32 day = 3;
  sint32 year = 4;
  sint32 hour = 5;
  sint32 minute = 6;
}

message GetChannelNameRequest {
  nidevice_grpc.Session vi = 1;
  sint32 index = 2;
}

message GetChannelNameResponse {
  int32 status = 1;
  string channel_string = 2;
}

message GetDevTempRequest {
  nidevice_grpc.Session vi = 1;
  string options = 2;
}

message GetDevTempResponse {
  int32 status = 1;
  double temperature = 2;
}

message GetErrorRequest {
  nidevice_grpc.Session vi = 1;
}

message GetErrorResponse {
  int32 status = 1;
  sint32 error_code = 2;
  string description = 3;
}

message GetErrorMessageRequest {
  nidevice_grpc.Session vi = 1;
  sint32 error_code = 2;
}

message GetErrorMessageResponse {
  int32 status = 1;
  string error_message = 2;
}

message GetExtCalRecommendedIntervalRequest {
  nidevice_grpc.Session vi = 1;
}

message GetExtCalRecommendedIntervalResponse {
  int32 status = 1;
  sint32 months = 2;
}

message GetLastCalTempRequest {
  nidevice_grpc.Session vi = 1;
  oneof cal_type_enum {
    CalibrationType cal_type = 2;
    sint32 cal_type_raw = 3;
  }
}

message GetLastCalTempResponse {
  int32 status = 1;
  double temperature = 2;
}

message GetMeasurementPeriodRequest {
  nidevice_grpc.Session vi = 1;
}

message GetMeasurementPeriodResponse {
  int32 status = 1;
  double period = 2;
}

message GetSelfCalSupportedRequest {
  nidevice_grpc.Session vi = 1;
}

message GetSelfCalSupportedResponse {
  int32 status = 1;
  bool self_cal_supported = 2;
}

message ImportAttributeConfigurationBufferRequest {
  nidevice_grpc.Session vi = 1;
  bytes configuration = 2;
}

message ImportAttributeConfigurationBufferResponse {
  int32 status = 1;
}

message ImportAttributeConfigurationFileRequest {
  nidevice_grpc.Session vi = 1;
  string file_path = 2;
}

message ImportAttributeConfigurationFileResponse {
  int32 status = 1;
}

message InitRequest {
  string session_name = 1;
  string resource_name = 2;
  bool id_query = 3;
  bool reset_device = 4;
  nidevice_grpc.SessionInitializationBehavior initialization_behavior = 5;
}

message InitResponse {
  int32 status = 1;
  nidevice_grpc.Session vi = 2;
  string error_message = 3 [deprecated = true];
  bool new_session_initialized = 4;
}

message InitWithOptionsRequest {
  string session_name = 1;
  string resource_name = 2;
  bool id_query = 3;
  bool reset_device = 4;
  string option_string = 5;
  nidevice_grpc.SessionInitializationBehavior initialization_behavior = 6;
}

message InitWithOptionsResponse {
  int32 status = 1;
  nidevice_grpc.Session vi = 2;
  string error_message = 3 [deprecated = true];
  bool new_session_initialized = 4;
}

message InitiateRequest {
  nidevice_grpc.Session vi = 1;
}

message InitiateResponse {
  int32 status = 1;
}

message InvalidateAllAttributesRequest {
  nidevice_grpc.Session vi = 1;
}

message InvalidateAllAttributesResponse {
  int32 status = 1;
}

message IsOverRangeRequest {
  nidevice_grpc.Session vi = 1;
  double measurement_value = 2;
}

message IsOverRangeResponse {
  int32 status = 1;
  bool is_over_range = 2;
}

message IsUnderRangeRequest {
  nidevice_grpc.Session vi = 1;
  double measurement_value = 2;
}

message IsUnderRangeResponse {
  int32 status = 1;
  bool is_under_range = 2;
}

message PerformOpenCableCompRequest {
  nidevice_grpc.Session vi = 1;
}

message PerformOpenCableCompResponse {
  int32 status = 1;
  double conductance = 2;
  double susceptance = 3;
}

message PerformShortCableCompRequest {
  nidevice_grpc.Session vi = 1;
}

message PerformShortCableCompResponse {
  int32 status = 1;
  double resistance = 2;
  double reactance = 3;
}

message ReadRequest {
  nidevice_grpc.Session vi = 1;
  oneof maximum_time_enum {
    TimeLimit maximum_time = 2;
    sint32 maximum_time_raw = 3;
  }
}

message ReadResponse {
  int32 status = 1;
  double reading = 2;
}

message ReadMultiPointRequest {
  nidevice_grpc.Session vi = 1;
  oneof maximum_time_enum {
    TimeLimit maximum_time = 2;
    sint32 maximum_time_raw = 3;
  }
  sint32 array_size = 4;
}

message ReadMultiPointResponse {
  int32 status = 1;
  repeated double reading_array = 2;
  sint32 actual_number_of_points = 3;
}

message ReadStatusRequest {
  nidevice_grpc.Session vi = 1;
}

message ReadStatusResponse {
  int32 status = 1;
  sint32 acquisition_backlog = 2;
  AcquisitionStatus acquisition_status = 3;
  sint32 acquisition_status_raw = 4;
}

message ReadWaveformRequest {
  nidevice_grpc.Session vi = 1;
  oneof maximum_time_enum {
    TimeLimit maximum_time = 2;
    sint32 maximum_time_raw = 3;
  }
  sint32 array_size = 4;
}

message ReadWaveformResponse {
  int32 status = 1;
  repeated double waveform_array = 2;
  sint32 actual_number_of_points = 3;
}

message ResetRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetResponse {
  int32 status = 1;
}

message ResetInterchangeCheckRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetInterchangeCheckResponse {
  int32 status = 1;
}

message ResetWithDefaultsRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetWithDefaultsResponse {
  int32 status = 1;
}

message RevisionQueryRequest {
  nidevice_grpc.Session vi = 1;
}

message RevisionQueryResponse {
  int32 status = 1;
  string instrument_driver_revision = 2;
  string firmware_revision = 3;
}

message SelfCalRequest {
  nidevice_grpc.Session vi = 1;
}

message SelfCalResponse {
  int32 status = 1;
}

message SelfTestRequest {
  nidevice_grpc.Session vi = 1;
}

message SelfTestResponse {
  int32 status = 1;
  sint32 self_test_result = 2;
  string self_test_message = 3;
}

message SendSoftwareTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message SendSoftwareTriggerResponse {
  int32 status = 1;
}

message SetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
  bool attribute_value = 4;
}

message SetAttributeViBooleanResponse {
  int32 status = 1;
}

message SetAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
  oneof attribute_value_enum {
    NiDmmInt32AttributeValues attribute_value = 4;
    sint32 attribute_value_raw = 5;
  }
}

message SetAttributeViInt32Response {
  int32 status = 1;
}

message SetAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
  oneof attribute_value_enum {
    NiDmmReal64AttributeValues attribute_value = 4;
    double attribute_value_raw = 5;
    NiDmmReal64AttributeValuesMapped attribute_value_mapped = 6;
  }
}

message SetAttributeViReal64Response {
  int32 status = 1;
}

message SetAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
  nidevice_grpc.Session attribute_value = 4;
}

message SetAttributeViSessionResponse {
  int32 status = 1;
}

message SetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDmmAttribute attribute_id = 3;
  string attribute_value_raw = 4;
}

message SetAttributeViStringResponse {
  int32 status = 1;
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidmm/README.md sha256=618dd065fc8d736d7869c0006438e3a90e37f0975a1c844fd3a55a375eb1532f bytes=208 -->
## FILE: source/codegen/metadata/nidmm/README.md

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidmm/README.md`
- sha256: `618dd065fc8d736d7869c0006438e3a90e37f0975a1c844fd3a55a375eb1532f`
- bytes: 208

````markdown
# Updating

To update this metadata folder. Find the nidmm_grpc_device export and copy the contents of its metadata folder here.

# More info

Refer to source/codegen/metadata/Imported_From_Hapigen.md
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidmm_restricted/__init__.py sha256=9f2093ddaaf188e3d37c1fccce6ee28dbb56756ec05683fd6d89597b24b732f8 bytes=244 -->
## FILE: source/codegen/metadata/nidmm_restricted/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidmm_restricted/__init__.py`
- sha256: `9f2093ddaaf188e3d37c1fccce6ee28dbb56756ec05683fd6d89597b24b732f8`
- bytes: 244

````python
from .functions import functions
from .attributes import attributes
from .enums import enums
from .config import config

metadata = {
    "functions": functions,
    "attributes": attributes,
    "enums": enums,
    "config": config
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidmm_restricted/attributes.py sha256=3f55827ece9f75b85d8da8a9a93a54dc6028407339e16a885b6ae3e113e93c6d bytes=113 -->
## FILE: source/codegen/metadata/nidmm_restricted/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidmm_restricted/attributes.py`
- sha256: `3f55827ece9f75b85d8da8a9a93a54dc6028407339e16a885b6ae3e113e93c6d`
- bytes: 113

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-DMM API metadata version 26.0.0d90
attributes = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidmm_restricted/attributes_addon.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: source/codegen/metadata/nidmm_restricted/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidmm_restricted/attributes_addon.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidmm_restricted/config.py sha256=2c02a247fa879e419cbcf57e32f5fcf0c7570450a379465cb148c4f1d3689d2d bytes=1232 -->
## FILE: source/codegen/metadata/nidmm_restricted/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidmm_restricted/config.py`
- sha256: `2c02a247fa879e419cbcf57e32f5fcf0c7570450a379465cb148c4f1d3689d2d`
- bytes: 1232

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-DMM API metadata version 26.0.0d90
config = {
    'additional_headers': {
        'custom/ivi_errors.h': [
            'service.cpp'
        ]
    },
    'api_version': '26.0.0d90',
    'c_function_prefix': 'niDMM_',
    'c_header': 'nidmm.h',
    'close_function': None,
    'csharp_namespace': 'NationalInstruments.Grpc.DmmRestricted',
    'custom_types': [
    ],
    'driver_name': 'NI-DMM-RESTRICTED',
    'is_restricted': True,
    'java_package': 'com.ni.grpc.dmmrestricted',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nidmm',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'nidmm_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'nidmm_64.dll',
                'type': 'cdll'
            }
        }
    },
    'linux_rt_support': True,
    'module_name': 'nidmm_restricted',
    'namespace_component': 'nidmm_restricted',
    'service_class_prefix': 'NiDmmRestricted',
    'session_handle_parameter_name': 'vi',
    'status_ok': 'status >= 0'
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidmm_restricted/config_addon.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: source/codegen/metadata/nidmm_restricted/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidmm_restricted/config_addon.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidmm_restricted/enums.py sha256=a3e6005d63797cb2135cca6362435cd188c23db9e0220d460a4cff2ce74e5f73 bytes=1379 -->
## FILE: source/codegen/metadata/nidmm_restricted/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidmm_restricted/enums.py`
- sha256: `a3e6005d63797cb2135cca6362435cd188c23db9e0220d460a4cff2ce74e5f73`
- bytes: 1379

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-DMM API metadata version 26.0.0d90
enums = {
    'AcquisitionStatus': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_RUNNING_ANTICOLLISION',
                'value': 0
            },
            {
                'name': 'NIDMM_VAL_FINISHED_WITH_BACKLOG',
                'value': 1
            },
            {
                'name': 'NIDMM_VAL_FINISHED_WITH_NO_BACKLOG',
                'value': 2
            },
            {
                'name': 'NIDMM_VAL_PAUSED',
                'value': 3
            },
            {
                'name': 'NIDMM_VAL_NO_ACQUISITION_IN_PROGRESS',
                'value': 4
            }
        ]
    },
    'PrivilegeLevel': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIDMM_VAL_NO_PRIVILEGE',
                'value': 0
            },
            {
                'name': 'NIDMM_VAL_MONITOR_PRIVILEGE',
                'value': 1
            },
            {
                'name': 'NIDMM_VAL_REVOKABLE_CONTROL_PRIVILEGE',
                'value': 2
            },
            {
                'name': 'NIDMM_VAL_NON_REVOKABLE_CONTROL_PRIVILEGE',
                'value': 3
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidmm_restricted/enums_addon.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: source/codegen/metadata/nidmm_restricted/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidmm_restricted/enums_addon.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidmm_restricted/functions.py sha256=6e2b60fa78639ee5f547bc2268eb972b9565baaa8580d167094669ff27cb987d bytes=8016 -->
## FILE: source/codegen/metadata/nidmm_restricted/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidmm_restricted/functions.py`
- sha256: `6e2b60fa78639ee5f547bc2268eb972b9565baaa8580d167094669ff27cb987d`
- bytes: 8016

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-DMM API metadata version 26.0.0d90
functions = {
    'AttributeWasSetByUser': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'repCapName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'repCapName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'int32',
                'name': 'attributeId',
                'type': 'ViAttr'
            }
        ],
        'returns': 'ViBoolean'
    },
    'CachedReadStatus': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'acqBacklog',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'acqBacklog',
                'type': 'ViInt32'
            },
            {
                'cppName': 'acqStatus',
                'direction': 'out',
                'enum': 'AcquisitionStatus',
                'grpc_type': 'sint32',
                'name': 'acqStatus',
                'type': 'ViInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchMultiPointWithCaching': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'maxTime',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'maxTime',
                'type': 'ViInt32'
            },
            {
                'cppName': 'arraySize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'is_size_param': True,
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'readingArray',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'readingArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySize'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'actualPts',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualPts',
                'type': 'ViInt32'
            },
            {
                'cppName': 'isMonitoring',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'isMonitoring',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetError': {
        'codegen_method': 'private',
        'is_error_handling': True,
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorCode',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'description',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'description',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetErrorMessage': {
        'codegen_method': 'private',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorCode',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'errorMessage',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetOpenSessionsInformation': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'cppName': 'resourceName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'cppName': 'infoJson',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'infoJson',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'bufferSizeNeededInBytes'
                },
                'type': 'ViChar[]'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'uint64',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViUInt64'
            },
            {
                'cppName': 'bufferSizeNeededInBytes',
                'direction': 'out',
                'grpc_type': 'uint64',
                'name': 'bufferSizeNeededInBytes',
                'type': 'ViUInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'RequestPrivilege': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'privilegeLevel',
                'direction': 'in',
                'enum': 'PrivilegeLevel',
                'grpc_type': 'sint32',
                'name': 'privilegeLevel',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nidmm_restricted/functions_addon.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: source/codegen/metadata/nidmm_restricted/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nidmm_restricted/functions_addon.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake/__init__.py sha256=951f156600c0e02d198b387303dbe8ddd9b655db9cff81388f7f53034b17e17c bytes=730 -->
## FILE: source/codegen/metadata/nifake/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake/__init__.py`
- sha256: `951f156600c0e02d198b387303dbe8ddd9b655db9cff81388f7f53034b17e17c`
- bytes: 730

````python
from .functions import functions
from .functions_addon import functions_override_metadata
from .functions_addon import functions_validation_suppressions
from .attributes import attributes
from .attributes_addon import attributes_override_metadata
from .enums import enums
from .enums_addon import enums_override_metadata
from .config import config

metadata = {
    "functions" : functions,
    "functions_validation_suppressions": functions_validation_suppressions,
    "attributes" : attributes,
    "enums" : enums,
    "config" : config
}

metadata['functions'].update(functions_override_metadata)
metadata['attributes'].update(attributes_override_metadata)
metadata['enums'].update(enums_override_metadata)
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake/attributes.py sha256=a37bb124a2b943712847f870116a022aa00469bc72626ea4a16d43c4fbda811e bytes=2769 -->
## FILE: source/codegen/metadata/nifake/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake/attributes.py`
- sha256: `a37bb124a2b943712847f870116a022aa00469bc72626ea4a16d43c4fbda811e`
- bytes: 2769

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-FAKE API metadata version 26.5.0d5
attributes = {
    1000000: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'READ_WRITE_BOOL',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1000001: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'READ_WRITE_DOUBLE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1000002: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'READ_WRITE_STRING',
        'resettable': False,
        'type': 'ViString'
    },
    1000003: {
        'codegen_method': 'public',
        'enum': 'GrpcColorOverride',
        'grpc_type': 'sint32',
        'name': 'READ_WRITE_COLOR',
        'resettable': False,
        'type': 'ViInt32'
    },
    1000004: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'READ_WRITE_INTEGER',
        'resettable': True,
        'type': 'ViInt32'
    },
    1000005: {
        'codegen_method': 'public',
        'enum': 'FloatEnum',
        'grpc_type': 'double',
        'name': 'FLOAT_ENUM_NAME_OVERRIDE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1000006: {
        'codegen_method': 'public',
        'grpc_type': 'int64',
        'name': 'READ_WRITE_INT64',
        'resettable': False,
        'type': 'ViInt64'
    },
    1000007: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'READ_WRITE_DOUBLE_WITH_CONVERTER',
        'resettable': False,
        'type': 'ViReal64'
    },
    1000008: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'READ_WRITE_INTEGER_WITH_CONVERTER',
        'resettable': False,
        'type': 'ViInt32'
    },
    1000009: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'READ_WRITE_DOUBLE_WITH_REPEATED_CAPABILITY',
        'resettable': False,
        'type': 'ViReal64'
    },
    1000010: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'READ_WRITE_STRING_REPEATED_CAPABILITY',
        'resettable': False,
        'type': 'ViString'
    },
    1000012: {
        'codegen_method': 'public',
        'enum': 'SampleCount',
        'grpc_type': 'sint32',
        'name': 'SAMPLE_COUNT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1000013: {
        'codegen_method': 'public',
        'enum': 'SampleInterval',
        'grpc_type': 'double',
        'name': 'SAMPLE_INTERVAL',
        'resettable': False,
        'type': 'ViReal64'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake/attributes_addon.py sha256=cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f bytes=207 -->
## FILE: source/codegen/metadata/nifake/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake/attributes_addon.py`
- sha256: `cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f`
- bytes: 207

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake/config.py sha256=e2f3ba86a6843b2a5700309bbd6346fc1ddb422ff5b206c92ff2d9688109f5c1 bytes=4947 -->
## FILE: source/codegen/metadata/nifake/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake/config.py`
- sha256: `e2f3ba86a6843b2a5700309bbd6346fc1ddb422ff5b206c92ff2d9688109f5c1`
- bytes: 4947

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-FAKE API metadata version 26.5.0d5
config = {
    'additional_headers': {
    },
    'api_version': '26.5.0d5',
    'c_function_prefix': 'niFake_',
    'c_header': 'niFake.h',
    'close_function': 'Close',
    'csharp_namespace': 'NationalInstruments.Grpc.Fake',
    'custom_types': [
        {
            'fields': [
                {
                    'grpc_type': 'sint32',
                    'name': 'structInt',
                    'type': 'ViInt32'
                },
                {
                    'grpc_type': 'double',
                    'name': 'structDouble',
                    'type': 'ViReal64'
                }
            ],
            'grpc_name': 'FakeCustomStruct',
            'name': 'CustomStruct'
        },
        {
            'fields': [
                {
                    'grpc_type': 'FakeCustomStruct',
                    'name': 'structCustomStruct',
                    'type': 'struct CustomStruct'
                },
                {
                    'grpc_type': 'CustomStructTypedef',
                    'name': 'structCustomStructTypedef',
                    'type': 'struct CustomStructTypedef_struct'
                }
            ],
            'grpc_name': 'CustomStructNestedTypedef',
            'name': 'CustomStructNestedTypedef_struct'
        },
        {
            'fields': [
                {
                    'grpc_type': 'sint32',
                    'name': 'structInt',
                    'type': 'ViInt32'
                },
                {
                    'grpc_type': 'double',
                    'name': 'structDouble',
                    'type': 'ViReal64'
                }
            ],
            'grpc_name': 'CustomStructTypedef',
            'name': 'CustomStructTypedef_struct'
        },
        {
            'fields': [
                {
                    'grpc_type': 'sint32',
                    'name': 'real',
                    'type': 'ViInt16'
                },
                {
                    'grpc_type': 'sint32',
                    'name': 'imaginary',
                    'type': 'ViInt16'
                }
            ],
            'grpc_name': 'NIComplexI16_struct',
            'name': 'NiComplexI16'
        },
        {
            'fields': [
                {
                    'grpc_type': 'double',
                    'name': 'real',
                    'type': 'ViReal64'
                },
                {
                    'grpc_type': 'double',
                    'name': 'imaginary',
                    'type': 'ViReal64'
                }
            ],
            'grpc_name': 'NIComplexNumber_struct',
            'name': 'NiComplexNumber'
        },
        {
            'fields': [
                {
                    'grpc_type': 'float',
                    'name': 'real',
                    'type': 'ViReal32'
                },
                {
                    'grpc_type': 'float',
                    'name': 'imaginary',
                    'type': 'ViReal32'
                }
            ],
            'grpc_name': 'NIComplexNumberF32_struct',
            'name': 'NiComplexNumberF32'
        },
        {
            'fields': [
                {
                    'grpc_type': 'string',
                    'name': 'stringArg',
                    'type': 'ViConstString'
                },
                {
                    'coerced': True,
                    'enum': 'Turtle',
                    'grpc_type': 'Turtle',
                    'name': 'turtle',
                    'type': 'ViInt16'
                }
            ],
            'grpc_name': 'StringAndTurtle',
            'name': 'StringAndTurtle'
        },
        {
            'fields': [
                {
                    'grpc_type': 'string',
                    'name': 'stringArg',
                    'type': 'ViConstString'
                }
            ],
            'grpc_name': 'CustomNamedType',
            'name': 'namedType_custom'
        }
    ],
    'driver_name': 'NI-FAKE',
    'java_package': 'com.ni.grpc.fake',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nifake',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'nifake_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'nifake_64.dll',
                'type': 'cdll'
            }
        }
    },
    'linux_rt_support': False,
    'module_name': 'nifake',
    'namespace_component': 'nifake',
    'service_class_prefix': 'NiFake',
    'session_handle_parameter_name': 'vi',
    'status_ok': 'status >= 0'
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake/config_addon.py sha256=e6b1ac77e5483d879a9918d233d21e26e9a461e36a1d51d0341004417cbec305 bytes=170 -->
## FILE: source/codegen/metadata/nifake/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake/config_addon.py`
- sha256: `e6b1ac77e5483d879a9918d233d21e26e9a461e36a1d51d0341004417cbec305`
- bytes: 170

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.3.dev0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake/enums.py sha256=29cff2a4f20253c84b7f6b3fe0d6fe575abad35148a09ceb9c712e7d43fe3c62 bytes=6835 -->
## FILE: source/codegen/metadata/nifake/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake/enums.py`
- sha256: `29cff2a4f20253c84b7f6b3fe0d6fe575abad35148a09ceb9c712e7d43fe3c62`
- bytes: 6835

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-FAKE API metadata version 26.5.0d5
enums = {
    'Bitfield': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'FLAG_A',
                'value': 1
            },
            {
                'name': 'FLAG_B',
                'value': 2
            },
            {
                'name': 'FLAG_C',
                'value': 4
            },
            {
                'name': 'FLAG_D',
                'value': 8
            }
        ]
    },
    'DecimalMixedNumber': {
        'codegen_method': 'public',
        'generate-mappings': True,
        'values': [
            {
                'name': 'TWENTY_TWO',
                'value': 22
            },
            {
                'name': 'TWO_POINT_TWO',
                'value': 2.2
            },
            {
                'name': 'NEGATIVE_THREE',
                'value': -3
            },
            {
                'name': 'MAX_INT_32',
                'value': 2147483647
            },
            {
                'name': 'MAX_INT_32_PLUS_ONE',
                'value': 2147483648.0
            },
            {
                'name': 'MIN_INT_32',
                'value': -2147483648
            },
            {
                'name': 'MIN_INT_32_MINUS_ONE',
                'value': -2147483649.0
            }
        ]
    },
    'DecimalWholeNumber': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'ZERO',
                'value': 0
            },
            {
                'name': 'NEGATIVE_ONE',
                'value': -1
            },
            {
                'name': 'TWENTY_TWO',
                'value': 22
            }
        ]
    },
    'DecimalWholeNumberMapped': {
        'codegen_method': 'public',
        'generate-mappings': True,
        'values': [
            {
                'name': 'ZERO',
                'value': 0.0
            },
            {
                'name': 'NEGATIVE_ONE',
                'value': -1.0
            },
            {
                'name': 'TWENTY_TWO',
                'value': 22.0
            }
        ]
    },
    'EnumWithGrpcNameValues': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'ALTERED_GRPC_NAME_ONE',
                'value': 1
            },
            {
                'name': 'TWO',
                'value': 2
            }
        ]
    },
    'FloatEnum': {
        'codegen_method': 'public',
        'generate-mappings': True,
        'values': [
            {
                'name': 'THREE_POINT_FIVE',
                'value': 3.5
            },
            {
                'name': 'FOUR_POINT_FIVE',
                'value': 4.5
            },
            {
                'name': 'FIVE_POINT_FIVE',
                'value': 5.5
            },
            {
                'name': 'SIX_POINT_FIVE',
                'value': 6.5
            },
            {
                'name': 'SEVEN_POINT_FIVE',
                'value': 7.5
            }
        ]
    },
    'GrpcColorOverride': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'RED',
                'value': 1
            },
            {
                'name': 'BLUE',
                'value': 2
            },
            {
                'name': 'YELLOW',
                'value': 5
            },
            {
                'name': 'BLACK',
                'value': 42
            }
        ]
    },
    'MobileOSNames': {
        'codegen_method': 'public',
        'generate-mappings': True,
        'values': [
            {
                'name': 'ANDROID',
                'value': 'Android'
            },
            {
                'name': 'IOS',
                'value': 'iOS'
            },
            {
                'name': 'NONE',
                'value': 'None'
            }
        ]
    },
    'NiFakeInt32AttributeValues': {
        'enum-value-prefix': 'NIFAKE_INT32',
        'generate-mappings': False,
        'values': [
            {
                'name': 'GRPC_COLOR_OVERRIDE_RED',
                'value': 1
            },
            {
                'name': 'GRPC_COLOR_OVERRIDE_BLUE',
                'value': 2
            },
            {
                'name': 'GRPC_COLOR_OVERRIDE_YELLOW',
                'value': 5
            },
            {
                'name': 'GRPC_COLOR_OVERRIDE_BLACK',
                'value': 42
            },
            {
                'name': 'SAMPLE_COUNT_SAMPLE_COUNT_INFINITE',
                'value': 0
            }
        ]
    },
    'NiFakeReal64AttributeValues': {
        'enum-value-prefix': 'NIFAKE_REAL64',
        'generate-mappings': False,
        'values': [
            {
                'name': 'SAMPLE_INTERVAL_AUTO_DELAY',
                'value': -1
            }
        ]
    },
    'NiFakeReal64AttributeValuesMapped': {
        'enum-value-prefix': 'NIFAKE_REAL64',
        'generate-mappings': True,
        'values': [
            {
                'name': 'FLOAT_ENUM_THREE_POINT_FIVE',
                'value': 3.5
            },
            {
                'name': 'FLOAT_ENUM_FOUR_POINT_FIVE',
                'value': 4.5
            },
            {
                'name': 'FLOAT_ENUM_FIVE_POINT_FIVE',
                'value': 5.5
            },
            {
                'name': 'FLOAT_ENUM_SIX_POINT_FIVE',
                'value': 6.5
            },
            {
                'name': 'FLOAT_ENUM_SEVEN_POINT_FIVE',
                'value': 7.5
            }
        ]
    },
    'SampleCount': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'SAMPLE_COUNT_INFINITE',
                'value': 0
            }
        ]
    },
    'SampleInterval': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'AUTO_DELAY',
                'value': -1
            }
        ]
    },
    'Turtle': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'LEONARDO',
                'value': 0
            },
            {
                'name': 'DONATELLO',
                'value': 1
            },
            {
                'name': 'RAPHAEL',
                'value': 2
            },
            {
                'name': 'MICHELANGELO',
                'value': 3
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake/enums_addon.py sha256=9f25172e660fd7e043e0a5b4bbd8669084c5cf552aa295713232ee352147b900 bytes=192 -->
## FILE: source/codegen/metadata/nifake/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake/enums_addon.py`
- sha256: `9f25172e660fd7e043e0a5b4bbd8669084c5cf552aa295713232ee352147b900`
- bytes: 192

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake/functions.py sha256=bcc4411d65cc2a322ca192b28216bfb4fcee853a8bd140feaefdb63e4b3b76c5 bytes=105575 -->
## FILE: source/codegen/metadata/nifake/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake/functions.py`
- sha256: `bcc4411d65cc2a322ca192b28216bfb4fcee853a8bd140feaefdb63e4b3b76c5`
- bytes: 105575

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-FAKE API metadata version 26.5.0d5
functions = {
    'Abort': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'AcceptListOfDurationsInSeconds': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'count',
                'determine_size_from': [
                    'delays'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'count',
                'type': 'ViInt32'
            },
            {
                'cppName': 'delays',
                'direction': 'in',
                'grpc_type': 'repeated double',
                'name': 'delays',
                'size': {
                    'mechanism': 'len',
                    'value': 'count'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'AcceptViSessionArray': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'sessionCount',
                'direction': 'in',
                'grpc_type': 'uint32',
                'is_size_param': True,
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'cppName': 'sessionArray',
                'direction': 'in',
                'grpc_type': 'repeated nidevice_grpc.Session',
                'name': 'sessionArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'AcceptViUInt32Array': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'arrayLen',
                'determine_size_from': [
                    'uInt32Array'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'arrayLen',
                'type': 'ViInt32'
            },
            {
                'cppName': 'uInt32Array',
                'direction': 'in',
                'grpc_type': 'repeated uint32',
                'name': 'uInt32Array',
                'size': {
                    'mechanism': 'len',
                    'value': 'arrayLen'
                },
                'type': 'ViUInt32[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'BoolArrayInputFunction': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'numberOfElements',
                'direction': 'in',
                'grpc_type': 'sint32',
                'is_size_param': True,
                'name': 'numberOfElements',
                'type': 'ViInt32'
            },
            {
                'cppName': 'anArray',
                'direction': 'in',
                'grpc_type': 'repeated bool',
                'name': 'anArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'ViBoolean[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'BoolArrayOutputFunction': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'numberOfElements',
                'direction': 'in',
                'grpc_type': 'sint32',
                'is_size_param': True,
                'name': 'numberOfElements',
                'type': 'ViInt32'
            },
            {
                'cppName': 'anArray',
                'direction': 'out',
                'grpc_type': 'repeated bool',
                'name': 'anArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'ViBoolean[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearError': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'Close': {
        'cname': 'niFake_close',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'CloseExtCal': {
        'codegen_method': 'public',
        'custom_close_method': True,
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'action',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'action',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CommandWithReservedParam': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'reserved',
                'direction': 'in',
                'grpc_type': 'bool',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureAbc': {
        'cname': 'niFake_ConfigureABC',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureEnums': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'sampleCount',
                'direction': 'in',
                'enum': 'SampleCount',
                'grpc_type': 'sint32',
                'name': 'sampleCount',
                'type': 'ViInt32'
            },
            {
                'cppName': 'sampleInterval',
                'direction': 'in',
                'enum': 'SampleInterval',
                'grpc_type': 'double',
                'name': 'sampleInterval',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'Control4022': {
        'cname': 'niFake_4022Control',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'resourceName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'resourceName',
                'type': 'ViString'
            },
            {
                'cppName': 'configuration',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'configuration',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateConfigurationList': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'numberOfListAttributes',
                'determine_size_from': [
                    'listAttributeIds'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'numberOfListAttributes',
                'type': 'ViInt32'
            },
            {
                'cppName': 'listAttributeIds',
                'direction': 'in',
                'grpc_type': 'repeated NiFakeAttribute',
                'name': 'listAttributeIds',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfListAttributes'
                },
                'type': 'ViAttr[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'CustomNestedStructRoundtrip': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'nestedCustomTypeIn',
                'direction': 'in',
                'grpc_type': 'CustomStructNestedTypedef',
                'name': 'nestedCustomTypeIn',
                'type': 'struct CustomStructNestedTypedef_struct'
            },
            {
                'cppName': 'nestedCustomTypeOut',
                'direction': 'out',
                'grpc_type': 'CustomStructNestedTypedef',
                'name': 'nestedCustomTypeOut',
                'type': 'struct CustomStructNestedTypedef_struct'
            }
        ],
        'returns': 'ViStatus'
    },
    'DoubleAllTheNums': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'numberCount',
                'determine_size_from': [
                    'numbers'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'numberCount',
                'type': 'ViInt32'
            },
            {
                'cppName': 'numbers',
                'direction': 'in',
                'grpc_type': 'repeated double',
                'name': 'numbers',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberCount'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'EnumArrayOutputFunction': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'numberOfElements',
                'direction': 'in',
                'grpc_type': 'sint32',
                'is_size_param': True,
                'name': 'numberOfElements',
                'type': 'ViInt32'
            },
            {
                'cppName': 'anArray',
                'direction': 'out',
                'enum': 'Turtle',
                'grpc_type': 'repeated sint32',
                'name': 'anArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'ViInt16[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'EnumInputFunctionWithDefaults': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'aTurtle',
                'direction': 'in',
                'enum': 'Turtle',
                'grpc_type': 'sint32',
                'name': 'aTurtle',
                'type': 'ViInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'ErrorMessage': {
        'cname': 'niFake_error_message',
        'codegen_method': 'public',
        'is_error_handling': True,
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorCode',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'cppName': 'errorMessage',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributeConfigurationBuffer': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'sizeInBytes',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'sizeInBytes',
                'type': 'ViInt32'
            },
            {
                'cppName': 'configuration',
                'direction': 'out',
                'grpc_type': 'bytes',
                'name': 'configuration',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'sizeInBytes'
                },
                'type': 'ViInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributeConfigurationBufferEx': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'size',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'cppName': 'configuration',
                'direction': 'out',
                'grpc_type': 'bytes',
                'name': 'configuration',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'ViInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchWaveform': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'numberOfSamples',
                'direction': 'in',
                'grpc_type': 'sint32',
                'is_size_param': True,
                'name': 'numberOfSamples',
                'type': 'ViInt32'
            },
            {
                'cppName': 'waveformData',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'waveformData',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfSamples'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'actualNumberOfSamples',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualNumberOfSamples',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchWithCustomSize': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'numberOfWaveforms',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'numberOfWaveforms',
                'type': 'ViInt32'
            },
            {
                'cppName': 'numberOfSamples',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'numberOfSamples',
                'type': 'ViInt32'
            },
            {
                'cppName': 'waveformData',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'waveformData',
                'size': {
                    'mechanism': 'custom-code',
                    'value': '(number_of_samples * number_of_waveforms)'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FunctionWithOverriddenGrpcName2x': {
        'cname': 'niFake_FunctionWithOverriddenGrpcName2x',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetABoolean': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'aBoolean',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'aBoolean',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetANumber': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'aNumber',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'aNumber',
                'type': 'ViInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAStringOfFixedMaximumSize': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'aString',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'aString',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAnIviDanceCharArray': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'charArray',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'charArray',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAnIviDanceWithATwistArray': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'aString',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'aString',
                'type': 'ViConstString'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'arrayOut',
                'direction': 'out',
                'grpc_type': 'repeated sint32',
                'name': 'arrayOut',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualSize'
                },
                'type': 'ViInt32[]'
            },
            {
                'cppName': 'actualSize',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAnIviDanceWithATwistArrayOfCustomType': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'arrayOut',
                'direction': 'out',
                'grpc_type': 'repeated FakeCustomStruct',
                'name': 'arrayOut',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualSize'
                },
                'type': 'struct CustomStruct[]'
            },
            {
                'cppName': 'actualSize',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAnIviDanceWithATwistArrayWithInputArray': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'dataIn',
                'direction': 'in',
                'grpc_type': 'repeated sint32',
                'name': 'dataIn',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySizeIn'
                },
                'type': 'ViInt32[]'
            },
            {
                'cppName': 'arraySizeIn',
                'determine_size_from': [
                    'dataIn'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'arraySizeIn',
                'type': 'ViInt32'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'arrayOut',
                'direction': 'out',
                'grpc_type': 'repeated sint32',
                'name': 'arrayOut',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualSize'
                },
                'type': 'ViInt32[]'
            },
            {
                'cppName': 'actualSize',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAnIviDanceWithATwistByteArray': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'arrayOut',
                'direction': 'out',
                'grpc_type': 'bytes',
                'name': 'arrayOut',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualSize'
                },
                'type': 'ViInt8[]'
            },
            {
                'cppName': 'actualSize',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAnIviDanceWithATwistString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'aString',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'aString',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualSize'
                },
                'type': 'ViChar[]'
            },
            {
                'cppName': 'actualSize',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAnIviDanceWithATwistStringStrlenBug': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'stringOut',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'stringOut',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'tags': [
                        'strlen-bug'
                    ],
                    'value': 'bufferSize',
                    'value_twist': 'actualSize'
                },
                'type': 'ViChar[]'
            },
            {
                'cppName': 'actualSize',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetArraySizeForCustomCode': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'sizeOut',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'sizeOut',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetArrayUsingIviDance': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'arraySize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'arrayOut',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'arrayOut',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetArrayViUInt8WithEnum': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'arrayLen',
                'direction': 'in',
                'grpc_type': 'sint32',
                'is_size_param': True,
                'name': 'arrayLen',
                'type': 'ViInt32'
            },
            {
                'cppName': 'uInt8EnumArray',
                'direction': 'out',
                'enum': 'GrpcColorOverride',
                'grpc_type': 'bytes',
                'name': 'uInt8EnumArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arrayLen'
                },
                'type': 'ViUInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFakeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt32': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFakeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFakeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'out',
                'grpc_type': 'int64',
                'name': 'attributeValue',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViReal64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFakeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViSession': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFakeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'attributeValue',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFakeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'attributeValue',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetBitfieldAsEnumArray': {
        'codegen_method': 'public',
        'parameters': [
            {
                'bitfield_as_enum_array': 'Bitfield',
                'cppName': 'flags',
                'direction': 'out',
                'grpc_type': 'int64',
                'name': 'flags',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetCalDateAndTime': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'calType',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'calType',
                'type': 'ViInt32'
            },
            {
                'cppName': 'month',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'cppName': 'day',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'day',
                'type': 'ViInt32'
            },
            {
                'cppName': 'year',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'cppName': 'hour',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'hour',
                'type': 'ViInt32'
            },
            {
                'cppName': 'minute',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'minute',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetCalInterval': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'months',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'months',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetCustomType': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'cs',
                'direction': 'out',
                'grpc_type': 'FakeCustomStruct',
                'name': 'cs',
                'type': 'struct CustomStruct'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetCustomTypeArray': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'numberOfElements',
                'direction': 'in',
                'grpc_type': 'sint32',
                'is_size_param': True,
                'name': 'numberOfElements',
                'type': 'ViInt32'
            },
            {
                'cppName': 'cs',
                'direction': 'out',
                'grpc_type': 'repeated FakeCustomStruct',
                'name': 'cs',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'struct CustomStruct[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetEnumValue': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'aQuantity',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'aQuantity',
                'type': 'ViInt32'
            },
            {
                'cppName': 'aTurtle',
                'direction': 'out',
                'enum': 'Turtle',
                'grpc_type': 'sint32',
                'name': 'aTurtle',
                'type': 'ViInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetError': {
        'codegen_method': 'public',
        'is_error_handling': True,
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorCode',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'description',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'description',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetParameterWithOverriddenGrpcName': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'originalParameter',
                'direction': 'out',
                'grpc_name': 'overridden_parameter',
                'grpc_type': 'sint32',
                'name': 'originalParameter',
                'type': 'ViInt16'
            },
            {
                'cppName': 'enumParameter',
                'direction': 'in',
                'enum': 'Turtle',
                'grpc_name': 'enum_parameter_raw',
                'grpc_type': 'sint32',
                'name': 'enumParameter',
                'type': 'ViInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetViInt32Array': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'arrayLen',
                'direction': 'in',
                'grpc_type': 'sint32',
                'is_size_param': True,
                'name': 'arrayLen',
                'type': 'ViInt32'
            },
            {
                'cppName': 'int32Array',
                'direction': 'out',
                'grpc_type': 'repeated sint32',
                'name': 'int32Array',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arrayLen'
                },
                'type': 'ViInt32[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetViUInt32Array': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'arrayLen',
                'direction': 'in',
                'grpc_type': 'sint32',
                'is_size_param': True,
                'name': 'arrayLen',
                'type': 'ViInt32'
            },
            {
                'cppName': 'uInt32Array',
                'direction': 'out',
                'grpc_type': 'repeated uint32',
                'name': 'uInt32Array',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arrayLen'
                },
                'type': 'ViUInt32[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetViUInt8': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'aUint8Number',
                'direction': 'out',
                'grpc_type': 'uint32',
                'name': 'aUint8Number',
                'type': 'ViUInt8'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributeConfigurationBuffer': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'sizeInBytes',
                'determine_size_from': [
                    'configuration'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'sizeInBytes',
                'type': 'ViInt32'
            },
            {
                'cppName': 'configuration',
                'direction': 'in',
                'grpc_type': 'bytes',
                'name': 'configuration',
                'size': {
                    'mechanism': 'len',
                    'value': 'sizeInBytes'
                },
                'type': 'ViInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributeConfigurationBufferEx': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'size',
                'determine_size_from': [
                    'configuration'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'cppName': 'configuration',
                'direction': 'in',
                'grpc_type': 'bytes',
                'name': 'configuration',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitExtCal': {
        'codegen_method': 'public',
        'custom_close': 'CloseExtCal(id, 0)',
        'init_method': True,
        'parameters': [
            {
                'cppName': 'resourceName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'cppName': 'calibrationPassword',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'calibrationPassword',
                'type': 'ViString'
            },
            {
                'cppName': 'vi',
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitWithOptions': {
        'codegen_method': 'public',
        'init_method': True,
        'parameters': [
            {
                'cppName': 'resourceName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'resourceName',
                'type': 'ViString'
            },
            {
                'cppName': 'idQuery',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'idQuery',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'resetDevice',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'optionString',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'optionString',
                'type': 'ViConstString'
            },
            {
                'cppName': 'vi',
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'ViInt32'
            },
            {
                'cppName': 'newSessionInitialized',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'newSessionInitialized',
                'proto_only': True,
                'type': 'bool'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitWithVarArgs': {
        'codegen_method': 'public',
        'init_method': True,
        'parameters': [
            {
                'cppName': 'resourceName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'cppName': 'vi',
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'stringArg',
                'direction': 'in',
                'grpc_type': 'string',
                'include_in_proto': False,
                'name': 'stringArg',
                'repeating_argument': True,
                'type': 'ViConstString'
            },
            {
                'cppName': 'turtle',
                'direction': 'in',
                'enum': 'Turtle',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'name': 'turtle',
                'repeating_argument': True,
                'type': 'ViInt16'
            },
            {
                'cppName': 'nameAndTurtle',
                'direction': 'in',
                'grpc_type': 'repeated StringAndTurtle',
                'is_compound_type': True,
                'max_length': 3,
                'name': 'nameAndTurtle',
                'repeated_var_args': True,
                'type': '...'
            }
        ],
        'returns': 'ViStatus'
    },
    'Initiate': {
        'codegen_method': 'private',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'IviDanceWithATwistCalculatedSizeOut': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'dataBufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'dataBufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'data',
                'direction': 'out',
                'grpc_type': 'repeated uint32',
                'name': 'data',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dataBufferSize',
                    'value_twist': 'actualNumWaveforms'
                },
                'type': 'ViUInt32[]'
            },
            {
                'cppName': 'actualNumWaveforms',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualNumWaveforms',
                'type': 'ViInt32'
            },
            {
                'cppName': 'actualSamplesPerWaveform',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualSamplesPerWaveform',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'IviDanceWithTwistWithMultipleArraysAndOneBufferSize': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'numElements',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'numElements',
                'type': 'ViInt32'
            },
            {
                'cppName': 'array1',
                'direction': 'out',
                'grpc_type': 'repeated sint32',
                'name': 'array1',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'numElements',
                    'value_twist': 'actualNumElements'
                },
                'type': 'ViInt32[]'
            },
            {
                'cppName': 'array2',
                'direction': 'out',
                'grpc_type': 'repeated sint32',
                'name': 'array2',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'numElements',
                    'value_twist': 'actualNumElements'
                },
                'type': 'ViInt32[]'
            },
            {
                'cppName': 'array3',
                'direction': 'out',
                'grpc_type': 'repeated sint32',
                'name': 'array3',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'numElements',
                    'value_twist': 'actualNumElements'
                },
                'type': 'ViInt32[]'
            },
            {
                'cppName': 'actualNumElements',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualNumElements',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'MethodUsingEnumWithGrpcNameValues': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'usingEnum',
                'direction': 'in',
                'enum': 'EnumWithGrpcNameValues',
                'grpc_type': 'sint32',
                'name': 'usingEnum',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'MethodUsingWholeAndFractionalNumbers': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'wholeNumber',
                'direction': 'out',
                'enum': 'DecimalWholeNumber',
                'grpc_type': 'sint32',
                'name': 'wholeNumber',
                'type': 'ViInt32'
            },
            {
                'cppName': 'fractionalNumber',
                'direction': 'out',
                'grpc_type': 'double',
                'mapped-enum': 'DecimalMixedNumber',
                'name': 'fractionalNumber',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'MethodUsingWholeMappedNumbers': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'wholeNumber',
                'direction': 'out',
                'grpc_type': 'double',
                'mapped-enum': 'DecimalWholeNumberMapped',
                'name': 'wholeNumber',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'MethodWithGetLastErrorParam': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'lastError',
                'direction': 'out',
                'get_last_error': 'deprecated',
                'grpc_type': 'string',
                'name': 'lastError',
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'MethodWithGrpcFieldNumber': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_field_number': '5',
                'grpc_mapped_field_number': '6',
                'grpc_raw_field_number': '4',
                'grpc_type': 'sint32',
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'MethodWithGrpcOnlyParam': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'simpleParam',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'simpleParam',
                'type': 'ViInt32'
            },
            {
                'cppName': 'grpcOnlyParam',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'grpcOnlyParam',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'MethodWithProtoOnlyParameter': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'attributeValue',
                'proto_only': True,
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'MultipleArrayTypes': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'outputArraySize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'is_size_param': True,
                'name': 'outputArraySize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'outputArray',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'outputArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'outputArraySize'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'outputArrayOfFixedLength',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'outputArrayOfFixedLength',
                'size': {
                    'mechanism': 'fixed',
                    'value': 3
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'inputArraySizes',
                'determine_size_from': [
                    'inputArrayOfFloats',
                    'inputArrayOfIntegers'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'inputArraySizes',
                'type': 'ViInt32'
            },
            {
                'cppName': 'inputArrayOfFloats',
                'direction': 'in',
                'grpc_type': 'repeated double',
                'name': 'inputArrayOfFloats',
                'size': {
                    'mechanism': 'len',
                    'value': 'inputArraySizes'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'inputArrayOfIntegers',
                'direction': 'in',
                'grpc_type': 'repeated sint32',
                'name': 'inputArrayOfIntegers',
                'size': {
                    'mechanism': 'len',
                    'value': 'inputArraySizes'
                },
                'type': 'ViInt16[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'MultipleArraysSameSize': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'values1',
                'direction': 'in',
                'grpc_type': 'repeated double',
                'name': 'values1',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'values2',
                'direction': 'in',
                'grpc_type': 'repeated double',
                'name': 'values2',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'values3',
                'direction': 'in',
                'grpc_type': 'repeated double',
                'name': 'values3',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'values4',
                'direction': 'in',
                'grpc_type': 'repeated double',
                'name': 'values4',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'size',
                'determine_size_from': [
                    'values1',
                    'values2',
                    'values3',
                    'values4'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'size',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'MultipleArraysSameSizeWithOptional': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'values1',
                'direction': 'in',
                'grpc_type': 'repeated double',
                'name': 'values1',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'values2',
                'direction': 'in',
                'grpc_type': 'repeated double',
                'name': 'values2',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'values3',
                'direction': 'in',
                'grpc_type': 'repeated double',
                'name': 'values3',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'values4',
                'direction': 'in',
                'grpc_type': 'repeated double',
                'name': 'values4',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'values5',
                'direction': 'in',
                'grpc_type': 'repeated FakeCustomStruct',
                'name': 'values5',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'size'
                },
                'type': 'struct CustomStruct[]'
            },
            {
                'cppName': 'size',
                'determine_size_from': [
                    'values1',
                    'values2',
                    'values3',
                    'values4',
                    'values5'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': True,
                'name': 'size',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'OneInputFunction': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'aNumber',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'aNumber',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ParametersAreMultipleTypes': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'aBoolean',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'aBoolean',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'anInt32',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'anInt32',
                'type': 'ViInt32'
            },
            {
                'cppName': 'anInt64',
                'direction': 'in',
                'grpc_type': 'int64',
                'name': 'anInt64',
                'type': 'ViInt64'
            },
            {
                'cppName': 'anIntEnum',
                'direction': 'in',
                'enum': 'Turtle',
                'grpc_type': 'sint32',
                'name': 'anIntEnum',
                'type': 'ViInt16'
            },
            {
                'cppName': 'aFloat',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'aFloat',
                'type': 'ViReal64'
            },
            {
                'cppName': 'aFloatEnum',
                'direction': 'in',
                'grpc_type': 'double',
                'mapped-enum': 'FloatEnum',
                'name': 'aFloatEnum',
                'type': 'ViReal64'
            },
            {
                'cppName': 'aString',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'aString',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'PoorlyNamedSimpleFunction': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'Read': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'maximumTime',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'maximumTime',
                'type': 'ViReal64'
            },
            {
                'cppName': 'reading',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'reading',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadDataWithInOutIviTwist': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'data',
                'direction': 'out',
                'grpc_type': 'repeated sint32',
                'name': 'data',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'bufferSize'
                },
                'type': 'ViInt32[]'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'out',
                'grpc_type': 'sint32',
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadDataWithMultipleIviTwistParamSets': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'arrayOut',
                'direction': 'out',
                'grpc_type': 'repeated sint32',
                'name': 'arrayOut',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualSize'
                },
                'type': 'ViInt32[]'
            },
            {
                'cppName': 'actualSize',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'actualSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'otherBufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'otherBufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'otherArrayOut',
                'direction': 'out',
                'grpc_type': 'repeated sint32',
                'name': 'otherArrayOut',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'otherBufferSize',
                    'value_twist': 'otherActualSize'
                },
                'type': 'ViInt32[]'
            },
            {
                'cppName': 'otherActualSize',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'otherActualSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadFromChannel': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'maximumTime',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'maximumTime',
                'type': 'ViInt32'
            },
            {
                'cppName': 'reading',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'reading',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReturnANumberAndAString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'aNumber',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'aNumber',
                'type': 'ViInt16'
            },
            {
                'cppName': 'aString',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'aString',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReturnDurationInSeconds': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'timedelta',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'timedelta',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReturnListOfDurationsInSeconds': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'numberOfElements',
                'direction': 'in',
                'grpc_type': 'sint32',
                'is_size_param': True,
                'name': 'numberOfElements',
                'type': 'ViInt32'
            },
            {
                'cppName': 'timedeltas',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'timedeltas',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReturnMultipleTypes': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'aBoolean',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'aBoolean',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'anInt32',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'anInt32',
                'type': 'ViInt32'
            },
            {
                'cppName': 'anInt64',
                'direction': 'out',
                'grpc_type': 'int64',
                'name': 'anInt64',
                'type': 'ViInt64'
            },
            {
                'cppName': 'anIntEnum',
                'direction': 'out',
                'enum': 'Turtle',
                'grpc_type': 'sint32',
                'name': 'anIntEnum',
                'type': 'ViInt16'
            },
            {
                'cppName': 'aFloat',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'aFloat',
                'type': 'ViReal64'
            },
            {
                'cppName': 'aFloatEnum',
                'direction': 'out',
                'grpc_type': 'double',
                'mapped-enum': 'FloatEnum',
                'name': 'aFloatEnum',
                'type': 'ViReal64'
            },
            {
                'cppName': 'arraySize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'is_size_param': True,
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'anArray',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'anArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySize'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'stringSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'stringSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'aString',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'aString',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'stringSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'SelfTest': {
        'cname': 'niFake_self_test',
        'codegen_method': 'private',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'selfTestResult',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'selfTestResult',
                'type': 'ViInt16'
            },
            {
                'cppName': 'selfTestMessage',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'selfTestMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViBoolean': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFakeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt32': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFakeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'enum': 'NiFakeInt32AttributeValues',
                'grpc_type': 'sint32',
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFakeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_type': 'int64',
                'name': 'attribute_value_raw',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViReal64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFakeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'enum': 'NiFakeReal64AttributeValues',
                'grpc_type': 'double',
                'mapped-enum': 'NiFakeReal64AttributeValuesMapped',
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFakeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'attribute_value_raw',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetCustomType': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'cs',
                'direction': 'in',
                'grpc_type': 'FakeCustomStruct',
                'name': 'cs',
                'type': 'struct CustomStruct'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetCustomTypeArray': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'numberOfElements',
                'determine_size_from': [
                    'cs'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'numberOfElements',
                'type': 'ViInt32'
            },
            {
                'cppName': 'cs',
                'direction': 'in',
                'grpc_type': 'repeated FakeCustomStruct',
                'name': 'cs',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfElements'
                },
                'type': 'struct CustomStruct[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetRuntimeEnvironment': {
        'codegen_method': 'private',
        'parameters': [
            {
                'cppName': 'environment',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'environment',
                'type': 'ViConstString'
            },
            {
                'cppName': 'environmentVersion',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'environmentVersion',
                'type': 'ViConstString'
            },
            {
                'cppName': 'reserved1',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'reserved1',
                'type': 'ViConstString'
            },
            {
                'cppName': 'reserved2',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'reserved2',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'StringValuedEnumInputFunctionWithDefaults': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'aMobileOSName',
                'direction': 'in',
                'grpc_type': 'string',
                'mapped-enum': 'MobileOSNames',
                'name': 'aMobileOSName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'StringValuedEnumNoEnumGenerated': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'aStringEnum',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'aStringEnum',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'TwoInputFunction': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'aNumber',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'aNumber',
                'type': 'ViReal64'
            },
            {
                'cppName': 'aString',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'aString',
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'Use64BitNumber': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'input',
                'direction': 'in',
                'grpc_type': 'int64',
                'name': 'input',
                'type': 'ViInt64'
            },
            {
                'cppName': 'output',
                'direction': 'out',
                'grpc_type': 'int64',
                'name': 'output',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'UseATwoDimensionParameter': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'array',
                'direction': 'in',
                'grpc_type': 'repeated sint32',
                'name': 'array',
                'size': {
                    'mechanism': 'two-dimension',
                    'value': 'arrayLengths'
                },
                'type': 'ViInt32[]'
            },
            {
                'cppName': 'arrayLengths',
                'direction': 'in',
                'grpc_type': 'repeated sint32',
                'name': 'arrayLengths',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'ViInt32[]'
            },
            {
                'cppName': 'arraySize',
                'determine_size_from': [
                    'arrayLengths'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'arraySize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ViInt16ArrayInputFunction': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'numberOfElements',
                'determine_size_from': [
                    'anArray'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'numberOfElements',
                'type': 'ViInt32'
            },
            {
                'cppName': 'anArray',
                'direction': 'in',
                'grpc_type': 'repeated sint32',
                'name': 'anArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfElements'
                },
                'type': 'ViInt16[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ViUInt8ArrayInputFunction': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'numberOfElements',
                'direction': 'in',
                'grpc_type': 'sint32',
                'is_size_param': True,
                'name': 'numberOfElements',
                'type': 'ViInt32'
            },
            {
                'cppName': 'anArray',
                'direction': 'in',
                'grpc_type': 'bytes',
                'name': 'anArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'ViUInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ViUInt8ArrayOutputFunction': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'numberOfElements',
                'direction': 'in',
                'grpc_type': 'sint32',
                'is_size_param': True,
                'name': 'numberOfElements',
                'type': 'ViInt32'
            },
            {
                'cppName': 'anArray',
                'direction': 'out',
                'grpc_type': 'bytes',
                'name': 'anArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'ViUInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteWaveform': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'numberOfSamples',
                'determine_size_from': [
                    'waveform'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'numberOfSamples',
                'type': 'ViInt32'
            },
            {
                'cppName': 'waveform',
                'direction': 'in',
                'grpc_type': 'repeated double',
                'name': 'waveform',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfSamples'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    }
}
````
