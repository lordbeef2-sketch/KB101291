# NI OSS SOURCE SNAPSHOT: nimi-python

<!--NI_OSS_SNAPSHOT repo=ni/nimi-python commit=6511f8025f072f7f7021953888b916bbdc31aa2a -->

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidcpower/metadata/functions.py sha256=bc28ca63dea639db9b649ccc6febbf1562b1277cf42088f92d89307e96d7f478 bytes=246358 -->
## FILE: src/nidcpower/metadata/functions.py

- repository: `ni/nimi-python`
- source_path: `src/nidcpower/metadata/functions.py`
- sha256: `bc28ca63dea639db9b649ccc6febbf1562b1277cf42088f92d89307e96d7f478`
- bytes: 246358

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-DCPower API metadata version 25.3.0f265
functions = {
    'AbortWithChannels': {
        'documentation': {
            'description': '\nTransitions the specified channel(s) from the Running state to the\nUncommitted state. If a sequence is running, it is stopped. Any\nconfiguration functions called after this function are not applied until\nthe niDCPower_InitiateWithChannels function is called. If power output is enabled\nwhen you call the niDCPower_AbortWithChannels function, the channels remain\nin their current state and continue providing power.\n\nUse the niDCPower_ConfigureOutputEnabled function to disable power\noutput on a per channel basis. Use the niDCPower_reset function to\ndisable output on all channels.\n\nRefer to the `Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in\nthe *NI DC Power Supplies and SMUs Help* for information about the\nspecific NI-DCPower software states.\n\n**Related Topics:**\n\n`Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__\n',
            'note': '\nNI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'python_name': 'abort',
        'returns': 'ViStatus'
    },
    'CalSelfCalibrate': {
        'documentation': {
            'description': '\nPerforms a self-calibration upon the specified channel(s).\n\nThis function disables the output, performs several internal\ncalculations, and updates calibration values. The updated calibration\nvalues are written to the device hardware if the\nNIDCPOWER_ATTR_SELF_CALIBRATION_PERSISTENCE attribute is set to\nNIDCPOWER_VAL_WRITE_TO_EEPROM. Refer to the\nNIDCPOWER_ATTR_SELF_CALIBRATION_PERSISTENCE attribute topic for more\ninformation about the settings for this attribute.\n\nWhen calling niDCPower_CalSelfCalibrate with the PXIe-4162/4163,\nspecify all channels of your PXIe-4162/4163 with the channelName input.\nYou cannot self-calibrate a subset of PXIe-4162/4163 channels.\n\nRefer to the\n`Self-Calibration <REPLACE_DRIVER_SPECIFIC_URL_1(selfcal)>`__ topic for\nmore information about this function.\n\n**Related Topics:**\n\n`Self-Calibration <REPLACE_DRIVER_SPECIFIC_URL_1(selfcal)>`__\n',
            'note': '\nNI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.\n\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'python_name': 'self_cal',
        'returns': 'ViStatus'
    },
    'ClearLatchedOutputCutoffState': {
        'documentation': {
            'description': 'Clears the state of an output cutoff that was engaged.\nTo clear the state for all output cutoff reasons, use NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_ALL.\n',
            'note': '\nNI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the reasons for which to clear the output cutoff state.\n',
                    'table_body': [
                        [
                            'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_ALL',
                            'Clears all output cutoff conditions'
                        ],
                        [
                            'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_OUTPUT_HIGH',
                            'Clears cutoffs caused when the output exceeded the high cutoff limit for voltage output'
                        ],
                        [
                            'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_OUTPUT_LOW',
                            'Clears cutoffs caused when the output fell below the low cutoff limit for voltage output'
                        ],
                        [
                            'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_MEASURE_HIGH',
                            'Clears cutoffs caused when the measured voltage exceeded the high cutoff limit for voltage output'
                        ],
                        [
                            'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_MEASURE_LOW',
                            'Clears cutoffs caused when the measured voltage fell below the low cutoff limit for voltage output'
                        ],
                        [
                            'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_MEASURE_HIGH',
                            'Clears cutoffs caused when the measured current exceeded the high cutoff limit for current output'
                        ],
                        [
                            'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_MEASURE_LOW',
                            'Clears cutoffs caused when the measured current fell below the low cutoff limit for current output'
                        ],
                        [
                            'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_CHANGE_HIGH',
                            'Clears cutoffs caused when the voltage slew rate increased beyond the positive change cutoff for voltage output'
                        ],
                        [
                            'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_CHANGE_LOW',
                            'Clears cutoffs caused when the voltage slew rate decreased beyond the negative change cutoff for voltage output'
                        ],
                        [
                            'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_CHANGE_HIGH',
                            'Clears cutoffs caused when the current slew rate increased beyond the positive change cutoff for current output'
                        ],
                        [
                            'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_CHANGE_LOW',
                            'Clears cutoffs caused when the voltage slew rate decreased beyond the negative change cutoff for current output'
                        ],
                        [
                            'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_SATURATED',
                            'Clears cutoffs caused when the measured current saturates the current range'
                        ]
                    ]
                },
                'enum': 'OutputCutoffReason',
                'name': 'outputCutoffReason',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CommitWithChannels': {
        'documentation': {
            'description': '\nApplies previously configured settings to the specified channel(s). Calling this\nfunction moves the NI-DCPower session from the Uncommitted state into\nthe Committed state. After calling this function, modifying any\nattribute reverts the NI-DCPower session to the Uncommitted state. Use\nthe niDCPower_InitiateWithChannels function to transition to the Running state.\nRefer to the `Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in\nthe *NI DC Power Supplies and SMUs Help* for details about the specific\nNI-DCPower software states.\n\n**Related Topics:**\n\n`Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'python_name': 'commit',
        'returns': 'ViStatus'
    },
    'ConfigureApertureTime': {
        'documentation': {
            'description': '\nConfigures the aperture time on the specified channel(s).\n\nThe supported values depend on the **units**. Refer to the *Aperture\nTime* topic for your device in the *NI DC Power Supplies and SMUs Help*\nfor more information. In general, devices support discrete\n**apertureTime** values, and if you configure **apertureTime** to some\nunsupported value, NI-DCPower coerces it up to the next supported value.\n\nRefer to the *Measurement Configuration and Timing* or *DC Noise\nRejection* topic for your device in the *NI DC Power Supplies and SMUs\nHelp* for more information about how to configure your measurements.\n\n**Related Topics:**\n\n`Aperture Time <REPLACE_DRIVER_SPECIFIC_URL_1(aperture)>`__\n',
            'note': '\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the aperture time. Refer to the *Aperture Time* topic for your\ndevice in the *NI DC Power Supplies and SMUs Help* for more information.\n'
                },
                'name': 'apertureTime',
                'type': 'ViReal64'
            },
            {
                'default_value': 'ApertureTimeUnits.SECONDS',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the units for **apertureTime**.\n**Defined Values**:\n',
                    'table_body': [
                        [
                            'NIDCPOWER_VAL_SECONDS',
                            'Specifies seconds.'
                        ],
                        [
                            'NIDCPOWER_VAL_POWER_LINE_CYCLES',
                            'Specifies Power Line Cycles.'
                        ]
                    ]
                },
                'enum': 'ApertureTimeUnits',
                'name': 'units',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureLCRCompensation': {
        'documentation': {
            'description': '\nApplies previously generated open, short, load, as well as open and short custom cable compensation data to LCR measurements.\n\nThis function applies open, short and load compensation data when you have set the NIDCPOWER_ATTR_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE property to NIDCPOWER_VAL_AS_CONFIGURED, and it also applies custom cable compensation data when you have set the NIDCPOWER_ATTR_CABLE_LENGTH property to NIDCPOWER_VAL_CUSTOM_AS_CONFIGURED.\n\nCall this function after you have obtained LCR compensation data.\n\nIf the NIDCPOWER_ATTR_LCR_SHORT_CUSTOM_CABLE_COMPENSATION_ENABLED property is set to VI_TRUE, you must generate data with both niDCPower_PerformLCROpenCustomCableCompensation and niDCPower_PerformLCRShortCustomCableCompensation; if VI_FALSE, you must only use niDCPower_PerformLCROpenCustomCableCompensation, and NI-DCPower uses default short data.\n\nCall niDCPower_GetLCRCompensationData and pass the **compensation data** to this function.\n',
            'note': '\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session.\n**vi** is obtained from the niDCPower_InitExtCal or niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {'\nSpecifies the channel(s) to which this configuration value applies.\nSpecify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies channels 0 and 2).\nA channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are performed sequentially based on the order specified in this parameter.\n'},
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe size of the **compensation data**\n'
                },
                'name': 'compensationDataSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe open, short and load compensation data to apply.\n'
                },
                'name': 'compensationData',
                'python_api_converter_name': 'convert_to_bytes',
                'python_type': 'bytes',
                'size': {
                    'mechanism': 'len',
                    'value': 'compensationDataSize'
                },
                'type': 'ViAddr[]',
                'type_in_documentation': 'bytes'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureLCRCustomCableCompensation': {
        'documentation': {
            'description': '\nThis function is deprecated. Use niDCPower_ConfigureLCRCompensation\ninstead.\n\nApplies previously generated open and short custom cable compensation data to LCR measurements.\n\nThis function applies custom cable compensation data when you have set NIDCPOWER_ATTR_CABLE_LENGTH property to NIDCPOWER_VAL_CUSTOM_AS_CONFIGURED.\n\nCall this function after you have obtained custom cable compensation data.\n\nIf NIDCPOWER_ATTR_LCR_SHORT_CUSTOM_CABLE_COMPENSATION_ENABLED property is set to VI_TRUE, you must generate data with both niDCPower_PerformLCROpenCustomCableCompensation and niDCPower_PerformLCRShortCustomCableCompensation;\nif VI_FALSE, you must only use niDCPower_PerformLCROpenCustomCableCompensation, and NI-DCPower uses default short data.\n\nCall niDCPower_GetLCRCustomCableCompensationData and pass the **custom cable compensation data** to this function.\n',
            'note': '\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session.\n**vi** is obtained from the niDCPower_InitExtCal or niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {'\nSpecifies the channel(s) to which this configuration value applies.\nSpecify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies channels 0 and 2).\nA channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are performed sequentially based on the order specified in this parameter.\n'},
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe size of the **custom cable compensation data**\n'
                },
                'name': 'customCableCompensationDataSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe open and short custom cable compensation data to apply.\n'
                },
                'name': 'customCableCompensationData',
                'python_api_converter_name': 'convert_to_bytes',
                'python_type': 'bytes',
                'size': {
                    'mechanism': 'len',
                    'value': 'customCableCompensationDataSize'
                },
                'type': 'ViAddr[]',
                'type_in_documentation': 'bytes'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateAdvancedSequenceCommitStepWithChannels': {
        'documentation': {
            'description': '\nCreates a Commit step in the Active advanced sequence. A Commit step\nconfigures channels to a user-defined known state before starting the advanced sequence.\nWhen a Commit step exists in the Active advanced sequence, you cannot\nset the output function to Pulse Voltage or Pulse Current in either\nthe Commit step (-1) or step 0. When you create an advanced sequence\nstep, each attribute you passed to the niDCPower_CreateAdvancedSequenceWithChannels\nfunction is reset to its default value for that step unless otherwise specified.\n\n**Support for this Function**\n\nYou must set the source mode to Sequence to use this function.\n\nUsing the niDCPower_SetSequence function with Advanced Sequence\nfunctions is unsupported.\n\n**Related Topics**:\n\n`Advanced Sequence\nMode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__\n\n`Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__\n\nniDCPower_CreateAdvancedSequenceWithChannels\n',
            'note': '\nNI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.\n\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'default_value': True,
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies whether the step created with this function is active in the Active advanced sequence.'
                },
                'name': 'setAsActiveStep',
                'type': 'ViBoolean'
            }
        ],
        'python_name': 'create_advanced_sequence_commit_step',
        'returns': 'ViStatus'
    },
    'CreateAdvancedSequenceStepWithChannels': {
        'documentation': {
            'description': '\nCreates a new advanced sequence step in the advanced sequence specified\nby the Active advanced sequence. When you create an advanced sequence\nstep, each attribute you passed to the niDCPower_CreateAdvancedSequenceWithChannels\nfunction is reset to its default value for that step unless otherwise\nspecified.\n\n**Support for this Function**\n\nYou must set the source mode to Sequence to use this function.\n\nUsing the niDCPower_SetSequence function with Advanced Sequence\nfunctions is unsupported.\n\n**Related Topics**:\n\n`Advanced Sequence\nMode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__\n\n`Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__\n\nniDCPower_CreateAdvancedSequenceWithChannels\n',
            'note': '\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'default_value': True,
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies whether the step created with this function is active in the Active advanced sequence.'
                },
                'name': 'setAsActiveStep',
                'type': 'ViBoolean'
            }
        ],
        'python_name': 'create_advanced_sequence_step',
        'returns': 'ViStatus'
    },
    'CreateAdvancedSequenceWithChannels': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nCreates an empty advanced sequence. Call the\nniDCPower_CreateAdvancedSequenceStepWithChannels function to add steps to the\nactive advanced sequence.\n\nYou can create multiple advanced sequences for a channel.\n\n**Support for this function**\n\nYou must set the source mode to Sequence to use this function.\n\nUsing the niDCPower_SetSequence function with Advanced Sequence\nfunctions is unsupported.\n\nUse this function in the Uncommitted or Committed programming states.\nRefer to the `Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in\nthe *NI DC Power Supplies and SMUs Help* for more information about\nNI-DCPower programming states.\n\n**Related Topics**:\n\n`Advanced Sequence\nMode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__\n\n`Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__\n\nniDCPower_CreateAdvancedSequenceStepWithChannels\n',
            'note': '\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'create_advanced_sequence',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the sequence to create.'
                },
                'name': 'sequenceName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of attributes in the attributeIDs array.'
                },
                'name': 'attributeIdCount',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the attributes you reconfigure per step in the advanced\nsequence. For more information about which attributes can be configured\nin an advanced sequence for each NI-DCPower device that supports advanced\nsequencing, search ni.com for Supported Properties by Device.\n'
                },
                'name': 'attributeIds',
                'size': {
                    'mechanism': 'len',
                    'value': 'attributeIdCount'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies that this current sequence is active.'
                },
                'name': 'setAsActiveSequence',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'DeleteAdvancedSequenceWithChannels': {
        'documentation': {
            'description': '\nDeletes a previously created advanced sequence and all the advanced\nsequence steps in the advanced sequence.\n\n**Support for this Function**\n\nYou must set the source mode to Sequence to use this function.\n\nUsing the niDCPower_SetSequence function with Advanced Sequence\nfunctions is unsupported.\n\n**Related Topics**:\n\n`Advanced Sequence\nMode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__\n\n`Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__\n',
            'note': '\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'specifies the name of the sequence to delete.'
                },
                'name': 'sequenceName',
                'type': 'ViConstString'
            }
        ],
        'python_name': 'delete_advanced_sequence',
        'returns': 'ViStatus'
    },
    'Disable': {
        'documentation': {
            'description': '\nThis function performs the same actions as the niDCPower_ResetWithChannels\nfunction, except that this function also immediately sets the\nNIDCPOWER_ATTR_OUTPUT_ENABLED attribute to VI_FALSE.\n\nThis function opens the output relay on devices that have an output\nrelay.\n',
            'note': '\nNI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributeConfigurationBuffer': {
        'documentation': {
            'description': '\nExports the attribute configuration of the session to the specified\nconfiguration buffer.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers and the same number of configured\nchannels.\n\nThis function verifies that the attributes you have configured for the\nsession are valid. If the configuration is invalid, NI‑DCPower returns\nan error.\n\n**Support for this Function**\n\nCalling this function in `Sequence Source\nMode <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ is unsupported.\n\n**Channel Mapping Behavior for Multichannel Sessions**\n\nWhen importing and exporting session attribute configurations between\nNI‑DCPower sessions that were initialized with different channels, the\nconfigurations of the exporting channels are mapped to the importing\nchannels in the order you specify in the **channelName** input to the\nniDCPower_InitializeWithChannels function.\n\nFor example, if your entry for **channelName** is 0,1 for the exporting\nsession and 1,2 for the importing session:\n\n-  The configuration exported from channel 0 is imported into channel 1.\n-  The configuration exported from channel 1 is imported into channel 2.\n\n**Related Topics:**\n\n`Using Properties and\nAttributes <REPLACE_DRIVER_SPECIFIC_URL_1(using_properties_and_attributes)>`__\n\n`Setting Properties and Attributes Before Reading\nThem <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__\n',
            'note': '\nThis function will return an error if the total number of channels\ninitialized for the exporting session is not equal to the total number\nof channels initialized for the importing session.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the size, in bytes, of the byte array to export. If you enter\n0, this function returns the needed size.\n'
                },
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nSpecifies the byte array buffer to be populated with the exported\nattribute configuration.\n'
                },
                'name': 'configuration',
                'python_api_converter_name': 'convert_to_bytes',
                'python_type': 'bytes',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'ViAddr[]',
                'type_in_documentation': 'bytes',
                'use_array': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributeConfigurationFile': {
        'documentation': {
            'description': '\nExports the attribute configuration of the session to the specified\nfile.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers and the same number of configured\nchannels.\n\nThis function verifies that the attributes you have configured for the\nsession are valid. If the configuration is invalid, NI‑DCPower returns\nan error.\n\n**Support for this Function**\n\nCalling this function in `Sequence Source\nMode <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ is unsupported.\n\n**Channel Mapping Behavior for Multichannel Sessions**\n\nWhen importing and exporting session attribute configurations between\nNI‑DCPower sessions that were initialized with different channels, the\nconfigurations of the exporting channels are mapped to the importing\nchannels in the order you specify in the **channelName** input to the\nniDCPower_InitializeWithChannels function.\n\nFor example, if your entry for **channelName** is 0,1 for the exporting\nsession and 1,2 for the importing session:\n\n-  The configuration exported from channel 0 is imported into channel 1.\n-  The configuration exported from channel 1 is imported into channel 2.\n\n**Related Topics:**\n\n`Using Properties and\nAttributes <REPLACE_DRIVER_SPECIFIC_URL_1(using_properties_and_attributes)>`__\n\n`Setting Properties and Attributes Before Reading\nThem <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__\n',
            'note': '\nThis function will return an error if the total number of channels\ninitialized for the exporting session is not equal to the total number\nof channels initialized for the importing session.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the absolute path to the file to contain the exported\nattribute configuration. If you specify an empty or relative path, this\nfunction returns an error.\n**Default file extension:** .nidcpowerconfig\n'
                },
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'FancyFetchMultiple': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nReturns a list of named tuples (Measurement) that were\npreviously taken and are stored in the NI-DCPower buffer. This function\nshould not be used when the NIDCPOWER_ATTR_MEASURE_WHEN attribute is\nset to NIDCPOWER_VAL_ON_DEMAND. You must first call\nniDCPower_InitiateWithChannels before calling this function.\n\nFields in Measurement:\n\n- **voltage** (float)\n- **current** (float)\n- **in_compliance** (bool)\n- **channel** (str)\n\n',
            'note': '\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_fetch_measure'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. **vi** is obtained from the niDCPower_InitializeWithChannels function.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of measurements to fetch.'
                },
                'name': 'count',
                'type': 'ViInt32'
            },
            {
                'default_value': 'hightime.timedelta(seconds=1.0)',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the maximum time allowed for this function to complete. If the function does not complete within this time interval, NI-DCPower returns an error.\nDefault value: 1.0 second\n',
                    'note': 'When setting the timeout interval, ensure you take into account any triggers so that the timeout interval is long enough for your application.'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nList of named tuples with fields:\n\n- **voltage** (float)\n- **current** (float)\n- **in_compliance** (bool)\n- **channel** (str)\n'
                },
                'name': 'measurements',
                'python_type': 'Measurement',
                'size': {
                    'mechanism': 'python-code',
                    'value': None
                },
                'type': 'ViReal64[]'
            }
        ],
        'python_name': 'fetch_multiple',
        'returns': 'ViStatus'
    },
    'FancyFetchMultipleLCR': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nReturns a list of previously measured LCRMeasurement instances on the specified channel that have been taken and stored in a buffer.\n\nTo use this function:\n\n-  Set NIDCPOWER_ATTR_MEASURE_WHEN property to NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE or NIDCPOWER_VAL_ON_MEASURE_TRIGGER\n-  Put the channel in the Running state (call niDCPower_InitiateWithChannels)\n',
            'note': '\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_fetch_measure_lcr'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session.\n**vi** is obtained from the niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value applies.\nSpecify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies channels 0 and 2).\nA channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are performed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViString'
            },
            {
                'default_value': 'hightime.timedelta(seconds=1.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the maximum time allowed for this function to complete, in seconds.\nIf the function does not complete within this time interval, NI-DCPower returns an error.\nDefault value: 1.0 second\n',
                    'note': '\nWhen setting the timeout interval, ensure you take into account any triggers so that the timeout interval is long enough for your application.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of measurements to fetch.\n'
                },
                'name': 'count',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nA list of LCRMeasurement instances.\n',
                    'table_body': [
                        [
                            'channel',
                            '',
                            'The channel name associated with this LCR measurement.'
                        ],
                        [
                            'vdc',
                            'float',
                            'The measured DC voltage, in volts.'
                        ],
                        [
                            'idc',
                            'float',
                            'The measured DC current, in amps.'
                        ],
                        [
                            'stimulus_frequency',
                            'float',
                            'The frequency of the LCR test signal, in Hz.'
                        ],
                        [
                            'ac_voltage',
                            'complex',
                            'The measured AC voltage, in volts RMS.'
                        ],
                        [
                            'ac_current',
                            'complex',
                            'The measured AC current, in amps RMS.'
                        ],
                        [
                            'z',
                            'complex',
                            'The complex impedance.'
                        ],
                        [
                            'z_magnitude_and_phase',
                            'tuple of float',
                            'The magnitude, in ohms, and phase angle, in degrees, of the complex impedance.'
                        ],
                        [
                            'y',
                            'complex',
                            'The complex admittance.'
                        ],
                        [
                            'y_magnitude_and_phase',
                            'tuple of float',
                            'The magnitude, in siemens, and phase angle, in degrees, of the complex admittance.'
                        ],
                        [
                            'series_lcr',
                            'LCR',
                            'The inductance, in henrys, the capacitance, in farads, and the resistance, in ohms, as measured using a series circuit model.'
                        ],
                        [
                            'parallel_lcr',
                            'LCR',
                            'The inductance, in henrys, the capacitance, in farads, and the resistance, in ohms, as measured using a parallel circuit model.'
                        ],
                        [
                            'd',
                            'float',
                            'The dissipation factor of the circuit. The dimensionless dissipation factor is directly proportional to how quickly an oscillating system loses energy. D is the reciprocal of Q, the quality factor.'
                        ],
                        [
                            'q',
                            'float',
                            'The quality factor of the circuit. The dimensionless quality factor is inversely proportional to the degree of damping in a system. Q is the reciprocal of D, the dissipation factor.'
                        ],
                        [
                            'measurement_mode',
                            'enums.InstrumentMode',
                            'The measurement mode: **SMU** - The channel(s) are operating as a power supply/SMU. **LCR** - The channel(s) are operating as an LCR meter.'
                        ],
                        [
                            'dc_in_compliance',
                            'bool',
                            'Indicates whether the output was in DC compliance at the time the measurement was taken.'
                        ],
                        [
                            'ac_in_compliance',
                            'bool',
                            'Indicates whether the output was in AC compliance at the time the measurement was taken.'
                        ],
                        [
                            'unbalanced',
                            'bool',
                            'Indicates whether the output was unbalanced at the time the measurement was taken.'
                        ]
                    ]
                },
                'name': 'measurements',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'count'
                },
                'type': 'NILCRMeasurement[]'
            }
        ],
        'python_name': 'fetch_multiple_lcr',
        'returns': 'ViStatus'
    },
    'FancyInitialize': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nCreates and returns a new NI-DCPower session to the instrument(s) and channel(s) specified\nin **resource name** to be used in all subsequent NI-DCPower function calls. With this function,\nyou can optionally set the initial state of the following session attributes:\n\n-  NIDCPOWER_ATTR_SIMULATE\n-  NIDCPOWER_ATTR_DRIVER_SETUP\n\nAfter calling this function, the specified channel or channels will be in the Uncommitted\nstate.\n\nTo place channel(s) in a known start-up state when creating a new session, set **reset** to\nVI_TRUE. This action is equivalent to using the niDCPower_ResetWithChannels function immediately after initializing the\nsession.\n\nTo open a session and leave the channel(s) in an existing configuration without passing\nthrough a transitional output state, set **reset** to VI_FALSE. Next, configure the channel(s)\nas in the previous session, change the desired settings, and then call the niDCPower_InitiateWithChannels function\nto write both settings.\n\n**Details of Independent Channel Operation**\n\nWith this function and channel-based NI-DCPower functions and attributes, you can use any\nchannels in the session independently. For example, you can initiate a subset of channels in\nthe session with niDCPower_InitiateWithChannels, and the other channels in the session remain in the Uncommitted\nstate.\n\nWhen you initialize with independent channels, each channel steps through the NI-DCPower\nprogramming state model independently of all other channels, and you can specify a subset of\nchannels for most operations.\n\n**Note** You can make concurrent calls to a session from multiple threads, but the session\nexecutes the calls one at a time. If you specify multiple channels for a function or attribute,\nthe session may perform the operation on multiple channels in parallel, though this is not\nguaranteed, and some operations may execute sequentially.\n'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_initialize'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **resource name** as seen in Measurement\n& Automation Explorer (MAX) or lsni, for example "PXI1Slot3" where "PXI1Slot3" is an\ninstrument\'s **resource name**. If independent_channels is False, **resource name**\ncan also be a logical IVI name.\n\nIf independent_channels is True, **resource name** can be names of the instrument(s)\nand the channel(s) to initialize. Specify the instrument(s) and channel(s) using the\nform "PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or\nPXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3", where "PXI1Slot3" and "PXI1Slot4" are\ninstrument resource names followed by channels. If you exclude a channels string\nafter an instrument resource name, all channels of the instrument(s) are included in\nthe session.\n'
                },
                'name': 'resourceName',
                'python_api_converter_name': 'convert_repeated_capabilities_without_prefix',
                'type': 'ViString',
                'type_in_documentation': 'str, list, tuple'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': '\nFor new applications, use the default value of None\nand specify the channels in **resource name**.\n\nSpecifies which channel(s) to include in a new session. Specify multiple\nchannels by using a channel list or a channel range. A channel list is a comma (,)\nseparated sequence of channel names (for example, 0,2 specifies channels 0 and 2).\nA channel range is a lower bound channel followed by a hyphen (-) or colon (:)\nfollowed by an upper bound channel (for example, 0-2 specifies channels 0, 1,\nand 2).\n\nIf independent_channels is False, this argument specifies which channels to include\nin a legacy synchronized channels session. If you do not specify any channels, by\ndefault all channels on the device are included in the session.\n\nIf independent_channels is True, this argument combines with **resource name** to\nspecify which channels to include in an independent channels session. Initializing\nan independent channels session with a channels argument is deprecated.\n'
                },
                'is_repeated_capability': False,
                'name': 'channels',
                'python_api_converter_name': 'convert_repeated_capabilities_without_prefix',
                'type': 'ViString',
                'type_in_documentation': 'str, list, range, tuple'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether to reset channel(s) during the initialization procedure.\n'
                },
                'name': 'reset',
                'type': 'ViBoolean'
            },
            {
                'default_value': '""',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the initial value of certain attributes for the session.\nThe syntax for **optionString** is a list of attributes with an assigned value where\n1 is VI_TRUE and 0 is VI_FALSE. For example:\n\nSimulate=0, DriverSetup=Model:<model number>; BoardType:<bus connector>\n\nTo simulate a multi-instrument session when independent_channels is True, set\nSimulate to 1 and list multiple instruments for DriverSetup. For example:\n\nSimulate=1, DriverSetup=ResourceName:<instrument name>; Model:<model number>;\nBoardType:<bus connector> & ResourceName:<resource name>; Model:<model number>;\nBoardType:<bus connector>\n\nYou do not have to specify a value for all the attributes. If you do not specify a\nvalue for an attribute, the default value is used.\n'
                },
                'name': 'optionString',
                'python_api_converter_name': 'convert_init_with_options_dictionary',
                'type': 'ViString',
                'type_in_documentation': 'dict'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a session handle that you use to identify the device in all\nsubsequent NI-DCPower function calls.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': True,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether to initialize the session with\nindependent channels. Set this argument to False on legacy applications or if you\nare unable to upgrade your NI-DCPower driver runtime to 20.6 or higher.\n'
                },
                'name': 'independentChannels',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'FancyMeasureMultiple': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nReturns a list of named tuples (Measurement) containing the measured voltage\nand current values on the specified channel(s). Each call to this function\nblocks other function calls until the measurements are returned from the device.\nThe order of the measurements returned in the array corresponds to the order\non the specified channel(s).\n\nFields in Measurement:\n\n- **voltage** (float)\n- **current** (float)\n- **in_compliance** (bool) - Always None\n- **channel** (str)\n\n',
            'note': '\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_fetch_measure'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. **vi** is obtained from the niDCPower_InitializeWithChannels function.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nList of named tuples with fields:\n\n- **voltage** (float)\n- **current** (float)\n- **in_compliance** (bool) - Always None\n- **channel** (str)\n'
                },
                'name': 'measurements',
                'python_type': 'Measurement',
                'size': {
                    'mechanism': 'python-code',
                    'value': None
                },
                'type': 'ViReal64[]'
            }
        ],
        'python_name': 'measure_multiple',
        'returns': 'ViStatus'
    },
    'FancyMeasureMultipleLCR': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nMeasures and returns a list of LCRMeasurement instances on the specified channel(s).\n\nTo use this function:\n\n-  Set NIDCPOWER_ATTR_INSTRUMENT_MODE property to NIDCPOWER_VAL_LCR\n-  Set NIDCPOWER_ATTR_MEASURE_WHEN property to NIDCPOWER_VAL_ON_DEMAND\n-  Put the channel(s) in the Running state (call niDCPower_InitiateWithChannels)\n',
            'note': '\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_fetch_measure_lcr'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session.\n**vi** is obtained from the niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value applies.\nSpecify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies channels 0 and 2).\nA channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are performed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nA list of LCRMeasurement instances.\n',
                    'table_body': [
                        [
                            'channel',
                            '',
                            'The channel name associated with this LCR measurement.'
                        ],
                        [
                            'vdc',
                            'float',
                            'The measured DC voltage, in volts.'
                        ],
                        [
                            'idc',
                            'float',
                            'The measured DC current, in amps.'
                        ],
                        [
                            'stimulus_frequency',
                            'float',
                            'The frequency of the LCR test signal, in Hz.'
                        ],
                        [
                            'ac_voltage',
                            'complex',
                            'The measured AC voltage, in volts RMS.'
                        ],
                        [
                            'ac_current',
                            'complex',
                            'The measured AC current, in amps RMS.'
                        ],
                        [
                            'z',
                            'complex',
                            'The complex impedance.'
                        ],
                        [
                            'z_magnitude_and_phase',
                            'tuple of float',
                            'The magnitude, in ohms, and phase angle, in degrees, of the complex impedance.'
                        ],
                        [
                            'y',
                            'complex',
                            'The complex admittance.'
                        ],
                        [
                            'y_magnitude_and_phase',
                            'tuple of float',
                            'The magnitude, in siemens, and phase angle, in degrees, of the complex admittance.'
                        ],
                        [
                            'series_lcr',
                            'LCR',
                            'The inductance, in henrys, the capacitance, in farads, and the resistance, in ohms, as measured using a series circuit model.'
                        ],
                        [
                            'parallel_lcr',
                            'LCR',
                            'The inductance, in henrys, the capacitance, in farads, and the resistance, in ohms, as measured using a parallel circuit model.'
                        ],
                        [
                            'd',
                            'float',
                            'The dissipation factor of the circuit. The dimensionless dissipation factor is directly proportional to how quickly an oscillating system loses energy. D is the reciprocal of Q, the quality factor.'
                        ],
                        [
                            'q',
                            'float',
                            'The quality factor of the circuit. The dimensionless quality factor is inversely proportional to the degree of damping in a system. Q is the reciprocal of D, the dissipation factor.'
                        ],
                        [
                            'measurement_mode',
                            'enums.InstrumentMode',
                            'The measurement mode: **SMU** - The channel(s) are operating as a power supply/SMU. **LCR** - The channel(s) are operating as an LCR meter.'
                        ],
                        [
                            'dc_in_compliance',
                            'bool',
                            'Indicates whether the output was in DC compliance at the time the measurement was taken.'
                        ],
                        [
                            'ac_in_compliance',
                            'bool',
                            'Indicates whether the output was in AC compliance at the time the measurement was taken.'
                        ],
                        [
                            'unbalanced',
                            'bool',
                            'Indicates whether the output was unbalanced at the time the measurement was taken.'
                        ]
                    ]
                },
                'name': 'measurements',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self.parse_channel_count(channel_name)'
                },
                'type': 'NILCRMeasurement[]'
            }
        ],
        'python_name': 'measure_multiple_lcr',
        'returns': 'ViStatus'
    },
    'FetchMultiple': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns an array of voltage measurements, an array of current\nmeasurements, and an array of compliance measurements that were\npreviously taken and are stored in the NI-DCPower buffer. This function\nshould not be used when the NIDCPOWER_ATTR_MEASURE_WHEN attribute is\nset to NIDCPOWER_VAL_ON_DEMAND. You must first call\nniDCPower_InitiateWithChannels before calling this function.\n\nRefer to the `Acquiring\nMeasurements <REPLACE_DRIVER_SPECIFIC_URL_1(acquiringmeasurements)>`__\nand `Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__ topics in\nthe *NI DC Power Supplies and SMUs Help* for more information about\nconfiguring this function.\n',
            'note': '\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'fetch_multiple',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the maximum time allowed for this function to complete, in\nseconds. If the function does not complete within this time interval,\nNI-DCPower returns an error.\n',
                    'note': '\nWhen setting the timeout interval, ensure you take into account any\ntriggers so that the timeout interval is long enough for your\napplication.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of measurements to fetch.'
                },
                'name': 'count',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array of voltage measurements. Ensure that sufficient space\nhas been allocated for the returned array.\n'
                },
                'name': 'voltageMeasurements',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'count'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array of current measurements. Ensure that sufficient space\nhas been allocated for the returned array.\n'
                },
                'name': 'currentMeasurements',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'count'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array of Boolean values indicating whether the output was in\ncompliance at the time the measurement was taken. Ensure that sufficient\nspace has been allocated for the returned array.\n'
                },
                'name': 'inCompliance',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'count'
                },
                'type': 'ViBoolean[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nIndicates the number of measured values actually retrieved from the\ndevice.\n'
                },
                'name': 'actualCount',
                'type': 'ViInt32',
                'use_in_python_api': False
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchMultipleLCR': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns a list of previously measured LCRMeasurement instances on the specified channel that have been taken and stored in a buffer.\n\nTo use this function:\n\n-  Set NIDCPOWER_ATTR_MEASURE_WHEN property to NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE or NIDCPOWER_VAL_ON_MEASURE_TRIGGER\n-  Put the channel in the Running state (call niDCPower_InitiateWithChannels)\n',
            'note': '\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session.\n**vi** is obtained from the niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value applies.\nSpecify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies channels 0 and 2).\nA channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are performed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'default_value': 'hightime.timedelta(seconds=1.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the maximum time allowed for this function to complete, in seconds.\nIf the function does not complete within this time interval, NI-DCPower returns an error.\n',
                    'note': '\nWhen setting the timeout interval, ensure you take into account any triggers so that the timeout interval is long enough for your application.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of measurements to fetch.\n'
                },
                'name': 'count',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nA list of LCRMeasurement instances.\n',
                    'table_body': [
                        [
                            'vdc',
                            'float',
                            'The measured DC voltage, in volts.'
                        ],
                        [
                            'idc',
                            'float',
                            'The measured DC current, in amps.'
                        ],
                        [
                            'stimulus_frequency',
                            'float',
                            'The frequency of the LCR test signal, in Hz.'
                        ],
                        [
                            'ac_voltage',
                            'complex',
                            'The measured AC voltage, in volts RMS.'
                        ],
                        [
                            'ac_current',
                            'complex',
                            'The measured AC current, in amps RMS.'
                        ],
                        [
                            'z',
                            'complex',
                            'The complex impedance.'
                        ],
                        [
                            'z_magnitude_and_phase',
                            'tuple of float',
                            'The magnitude, in ohms, and phase angle, in degrees, of the complex impedance.'
                        ],
                        [
                            'y',
                            'complex',
                            'The complex admittance.'
                        ],
                        [
                            'y_magnitude_and_phase',
                            'tuple of float',
                            'The magnitude, in siemens, and phase angle, in degrees, of the complex admittance.'
                        ],
                        [
                            'series_lcr',
                            'LCR',
                            'The inductance, in henrys, the capacitance, in farads, and the resistance, in ohms, as measured using a series circuit model.'
                        ],
                        [
                            'parallel_lcr',
                            'LCR',
                            'The inductance, in henrys, the capacitance, in farads, and the resistance, in ohms, as measured using a parallel circuit model.'
                        ],
                        [
                            'd',
                            'float',
                            'The dissipation factor of the circuit. The dimensionless dissipation factor is directly proportional to how quickly an oscillating system loses energy. D is the reciprocal of Q, the quality factor.'
                        ],
                        [
                            'q',
                            'float',
                            'The quality factor of the circuit. The dimensionless quality factor is inversely proportional to the degree of damping in a system. Q is the reciprocal of D, the dissipation factor.'
                        ],
                        [
                            'measurement_mode',
                            'enums.InstrumentMode',
                            'The measurement mode: **SMU** - The channel(s) are operating as a power supply/SMU. **LCR** - The channel(s) are operating as an LCR meter.'
                        ],
                        [
                            'dc_in_compliance',
                            'bool',
                            'Indicates whether the output was in DC compliance at the time the measurement was taken.'
                        ],
                        [
                            'ac_in_compliance',
                            'bool',
                            'Indicates whether the output was in AC compliance at the time the measurement was taken.'
                        ],
                        [
                            'unbalanced',
                            'bool',
                            'Indicates whether the output was unbalanced at the time the measurement was taken.'
                        ]
                    ]
                },
                'name': 'measurements',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'count'
                },
                'type': 'NILCRMeasurement[]'
            },
            {
                'direction': 'out',
                'name': 'actualCount',
                'type': 'ViInt32',
                'use_in_python_api': False
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\n| Queries the value of a ViBoolean attribute.\n| You can use this function to get the values of device-specific\n  attributes and inherent IVI attributes.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the ID of an attribute. From the function panel window, you\ncan use this control as follows.\n\n-  In the function panel window, click on the control or press **Enter**\n   or the spacebar to display a dialog box containing hierarchical list\n   of the available attributes. Help text is shown for each attribute.\n   Select an attribute by double-clicking on it or by selecting it and\n   then pressing **Enter**.\n-  A ring control at the top of the dialog box allows you to see all IVI\n   attributes or only the attributes of type ViBoolean. If you choose to\n   see all IVI attributes, the data types appear to the right of the\n   attribute names in the list box. Attributes with data types other\n   than ViBoolean are dim. If you select an attribute data type that is\n   dim, LabWindows/CVI transfers you to the function panel for the\n   corresponding function that is consistent with the data type.\n-  If you want to enter a variable name, press **Ctrl**\\ +\\ **T** to\n   change this ring control to a manual input box. If the attribute in\n   this ring control has named constants as valid values, you can view\n   the constants by moving to the value control and pressing **Enter**.\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Passes the address of a\nViBoolean variable.\nIf the attribute currently showing in the attribute ring control has\nconstants as valid values, you can view a list of the constants by\npressing **Enter** on this control. Select a value by double-clicking on\nit or by selecting it and then pressing **Enter**.\n'
                },
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt32': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\n| Queries the value of a ViInt32 attribute.\n| You can use this function to get the values of device-specific\n  attributes and inherent IVI attributes.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the ID of an attribute. From the function panel window, you\ncan use this control as follows.\n\n-  In the function panel window, click on the control or press **Enter**\n   or the spacebar to display a dialog box containing hierarchical list\n   of the available attributes. Help text is shown for each attribute.\n   Select an attribute by double-clicking on it or by selecting it and\n   then pressing **Enter**.\n-  A ring control at the top of the dialog box allows you to see all IVI\n   attributes or only the attributes of type ViInt32. If you choose to\n   see all IVI attributes, the data types appear to the right of the\n   attribute names in the list box. Attributes with data types other\n   than ViInt32 are dim. If you select an attribute data type that is\n   dim, LabWindows/CVI transfers you to the function panel for the\n   corresponding function that is consistent with the data type.\n-  If you want to enter a variable name, press **Ctrl**\\ +\\ **T** to\n   change this ring control to a manual input box. If the attribute in\n   this ring control has named constants as valid values, you can view\n   the constants by moving to the value control and pressing **Enter**.\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Passes the address of a\nViInt32 variable.\nIf the attribute currently showing in the attribute ring control has\nconstants as valid values, you can view a list of the constants by\npressing **Enter** on this control. Select a value by double-clicking on\nit or by selecting it and then pressing **Enter**.\n'
                },
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\n| Queries the value of a ViInt64 attribute.\n| You can use this function to get the values of device-specific\n  attributes and inherent IVI attributes.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the ID of an attribute. From the function panel window, you\ncan use this control as follows.\n\n-  In the function panel window, click on the control or press **Enter**\n   or the spacebar to display a dialog box containing hierarchical list\n   of the available attributes. Help text is shown for each attribute.\n   Select an attribute by double-clicking on it or by selecting it and\n   then pressing **Enter**.\n-  A ring control at the top of the dialog box allows you to see all IVI\n   attributes or only the attributes of type ViReal64. If you choose to\n   see all IVI attributes, the data types appear to the right of the\n   attribute names in the list box. Attributes with data types other\n   than ViReal64 are dim. If you select an attribute data type that is\n   dim, LabWindows/CVI transfers you to the function panel for the\n   corresponding function that is consistent with the data type.\n-  If you want to enter a variable name, press **Ctrl**\\ +\\ **T** to\n   change this ring control to a manual input box. If the attribute in\n   this ring control has named constants as valid values, you can view\n   the constants by moving to the value control and pressing **Enter**.\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Passes the address of a\nViReal64 variable.\nIf the attribute currently showing in the attribute ring control has\nconstants as valid values, you can view a list of the constants by\npressing **Enter** on this control. Select a value by double-clicking on\nit or by selecting it and then pressing **Enter**.\n'
                },
                'name': 'attributeValue',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\n| Queries the value of a ViReal64 attribute.\n| You can use this function to get the values of device-specific\n  attributes and inherent IVI attributes.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the ID of an attribute. From the function panel window, you\ncan use this control as follows.\n\n-  In the function panel window, click on the control or press **Enter**\n   or the spacebar to display a dialog box containing hierarchical list\n   of the available attributes. Help text is shown for each attribute.\n   Select an attribute by double-clicking on it or by selecting it and\n   then pressing **Enter**.\n-  A ring control at the top of the dialog box allows you to see all IVI\n   attributes or only the attributes of type ViReal64. If you choose to\n   see all IVI attributes, the data types appear to the right of the\n   attribute names in the list box. Attributes with data types other\n   than ViReal64 are dim. If you select an attribute data type that is\n   dim, LabWindows/CVI transfers you to the function panel for the\n   corresponding function that is consistent with the data type.\n-  If you want to enter a variable name, press **Ctrl**\\ +\\ **T** to\n   change this ring control to a manual input box. If the attribute in\n   this ring control has named constants as valid values, you can view\n   the constants by moving to the value control and pressing **Enter**.\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Passes the address of a\nViReal64 variable.\nIf the attribute currently showing in the attribute ring control has\nconstants as valid values, you can view a list of the constants by\npressing **Enter** on this control. Select a value by double-clicking on\nit or by selecting it and then pressing **Enter**.\n'
                },
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\n| Queries the value of a ViString attribute.\n| You can use this function to get the values of device-specific\n  attributes and inherent IVI attributes.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the ID of an attribute. From the function panel window, you\ncan use this control as follows.\n\n-  In the function panel window, click on the control or press or the\n   spacebar to display a dialog box containing hierarchical list of the\n   available attributes. Help text is shown for each attribute. Select\n   an attribute by double-clicking on it or by selecting it and then\n   pressing .\n-  A ring control at the top of the dialog box allows you to see all IVI\n   attributes or only the attributes of type ViString. If you choose to\n   see all IVI attributes, the data types appear to the right of the\n   attribute names in the list box. Attributes with data types other\n   than ViString are dimmed. If you select an attribute data type that\n   is dimmed, LabWindows/CVI transfers you to the function panel for the\n   corresponding function that is consistent with the data type.\n-  If you want to enter a variable name, press to change this ring\n   control to a manual input control. If the attribute in this ring\n   control has named constants as valid values, you can view the\n   constants by moving to the value control and pressing .\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPasses the number of bytes in the buffer and specifies the number of\nbytes in the ViChar array you specify for **value**. If the current\nvalue of **value**, including the terminating NUL byte, is larger than\nthe size you indicate in this parameter, the function copies (buffer\nsize - 1) bytes into the buffer, places an ASCII NUL byte at the end of\nthe buffer, and returns the buffer size you must pass to get the entire\nvalue. For example, if the value is 123456 and the buffer size is 4, the\nfunction places 123 into the buffer and returns 7.\nTo obtain the required buffer size, you can pass 0 for this attribute\nand VI_NULL for **value**. If you want the function to fill in the\nbuffer regardless of the number of bytes in the value, pass a negative\nnumber for this attribute.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe buffer in which the function returns the current value of the\nattribute. The buffer must be of type ViChar and have at least as many\nbytes as indicated in **bufSize**.\nIf the current value of the attribute, including the terminating NUL\nbyte, contains more bytes that you indicate in this attribute, the\nfunction copies (buffer size -1) bytes into the buffer, places an ASCII\nNUL byte at the end of the buffer, and returns the buffer size you must\npass to get the entire value. For example, if the value is 123456 and\nthe buffer size is 4, the function places 123 into the buffer and\nreturns 7.\nIf you specify 0 for **bufSize**, you can pass VI_NULL for this\nattribute.\nIf the attribute currently showing in the attribute ring control has\nconstants as valid values, you can view a list of the constants by\npressing on this control. Select a value by double-clicking on it or by\nselecting it and then pressing .\n'
                },
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
        'documentation': {
            'description': '\nRetrieves the output **channelName** that corresponds to the requested\n**index**. Use the NIDCPOWER_ATTR_CHANNEL_COUNT attribute to\ndetermine the upper bound of valid values for **index**.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies which channel name to return. The index values begin at\n1.\n'
                },
                'name': 'index',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of bytes in the ViChar array you specify for\n**channelName**. If the **channelName**, including the terminating NUL\nbyte, contains more bytes than you indicate in this attribute, the\nfunction copies (buffer size - 1) bytes into the buffer, places an ASCII\nNUL byte at the end of the buffer, and returns the buffer size you must\npass to get the entire value. For example, if the value is 123456 and\nthe buffer size is 4, the function places 123 into the buffer and\nreturns 7.\nIf you pass 0, you can pass VI_NULL for **channelName**.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the channel name that corresponds to **index**.'
                },
                'is_repeated_capability': False,
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
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns a list of channel names for the given channel indices.'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'get_channel_name_from_string',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Index list for the channels in the session. Valid values are from zero to the total number of channels in the session minus one. The index string can be one of the following formats:\n\n-   A comma-separated list—for example, "0,2,3,1"\n-   A range using a hyphen—for example, "0-3"\n-   A range using a colon—for example, "0:3 "\n\nYou can combine comma-separated lists and ranges that use a hyphen or colon. Both out-of-order and repeated indices are supported ("2,3,0", "1,2,2,3"). White space characters, including spaces, tabs, feeds, and carriage returns, are allowed between characters. Ranges can be incrementing or decrementing.\n'
                },
                'grpc_name': 'index',
                'name': 'index',
                'python_api_converter_name': 'convert_repeated_capabilities_without_prefix',
                'python_name': 'indices',
                'type': 'ViConstString',
                'type_in_documentation': 'basic sequence types, str, or int'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe number of elements in the ViChar array you specify for name.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The channel name(s) at the specified indices.'
                },
                'grpc_name': 'channel_name',
                'is_repeated_capability': False,
                'name': 'channelName',
                'python_api_converter_name': 'convert_comma_separated_string_to_list',
                'python_name': 'names',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]',
                'type_in_documentation': 'list of str'
            }
        ],
        'python_name': '_get_channel_names',
        'render_in_session_base': True,
        'returns': 'ViStatus'
    },
    'GetError': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\n| Retrieves and then clears the IVI error information for the session or\n  the current execution thread unless **bufferSize** is 0, in which case\n  the function does not clear the error information. By passing 0 for\n  the buffer size, you can ascertain the buffer size required to get the\n  entire error description string and then call the function again with\n  a sufficiently large buffer size.\n| If the user specifies a valid IVI session for **vi**, this function\n  retrieves and then clears the error information for the session. If\n  the user passes VI_NULL for **vi**, this function retrieves and then\n  clears the error information for the current execution thread. If\n  **vi** is an invalid session, the function does nothing and returns an\n  error. Normally, the error information describes the first error that\n  occurred since the user last called niDCPower_GetError or\n  niDCPower_ClearError.\n'
        },
        'included_in_proto': True,
        'is_error_handling': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'none'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the error code for the session or execution thread.'
                },
                'name': 'code',
                'type': 'ViStatus'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of bytes in the ViChar array you specify for\n**description**.\nIf the error description, including the terminating NUL byte, contains\nmore bytes than you indicate in this attribute, the function copies\n(buffer size - 1) bytes into the buffer, places an ASCII NUL byte at the\nend of the buffer, and returns the buffer size you must pass to get the\nentire value. For example, if the value is 123456 and the buffer size is\n4, the function places 123 into the buffer and returns 7.\nIf you pass 0 for this attribute, you can pass VI_NULL for\n**description**.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the error description for the IVI session or execution thread.\nIf there is no description, the function returns an empty string.\nThe buffer must contain at least as many elements as the value you\nspecify with **bufferSize**. If the error description, including the\nterminating NUL byte, contains more bytes than you indicate with\n**bufferSize**, the function copies (buffer size - 1) bytes into the\nbuffer, places an ASCII NUL byte at the end of the buffer, and returns\nthe buffer size you must pass to get the entire value. For example, if\nthe value is 123456 and the buffer size is 4, the function places 123\ninto the buffer and returns 7.\nIf you pass 0 for **bufferSize**, you can pass VI_NULL for this\nattribute.\n'
                },
                'name': 'description',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'GetExtCalLastDateAndTime': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns the date and time of the last successful calibration. The time\nreturned is 24-hour (military) local time; for example, if the device\nwas calibrated at 2:30 PM, this function returns 14 for **hours** and 30\nfor **minutes**.\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'get_ext_cal_last_date_and_time',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitExtCal or niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **year** the device was last calibrated.'
                },
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **month** in which the device was last calibrated.'
                },
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **day** on which the device was last calibrated.'
                },
                'name': 'day',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the **hour** (in 24-hour time) in which the device was last\ncalibrated.\n'
                },
                'name': 'hour',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **minute** in which the device was last calibrated.'
                },
                'name': 'minute',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetExtCalLastTemp': {
        'documentation': {
            'description': '\nReturns the onboard **temperature** of the device, in degrees Celsius,\nduring the last successful external calibration.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitExtCal or niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the onboard **temperature** of the device, in degrees Celsius,\nduring the last successful external calibration.\n'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetExtCalRecommendedInterval': {
        'documentation': {
            'description': '\nReturns the recommended maximum interval, in **months**, between\nexternal calibrations.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitExtCal or niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nSpecifies the recommended maximum interval, in **months**, between\nexternal calibrations.\n'
                },
                'name': 'months',
                'python_api_converter_name': 'convert_month_to_timedelta',
                'type': 'ViInt32',
                'type_in_documentation': 'hightime.timedelta'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetLCRCompensationData': {
        'documentation': {
            'description': '\nCollects previously generated open, short, load, and custom cable compensation data so you can then apply it to LCR measurements with niDCPower_ConfigureLCRCompensation.\n\nCall this function after you have obtained the compensation data of all types (open, short, load, open custom cable compensation, and short custom cable compensation) you want to apply to your measurements. Pass the **compensation data** to niDCPower_ConfigureLCRCompensation\n',
            'note': '\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session.\n**vi** is obtained from the niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value applies.\nSpecify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies channels 0 and 2).\nA channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are performed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'compensationDataSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe open, short, load, and custom cable compensation data to retrieve.\n'
                },
                'name': 'compensationData',
                'python_api_converter_name': 'convert_to_bytes',
                'python_type': 'bytes',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'compensationDataSize'
                },
                'type': 'ViAddr[]',
                'type_in_documentation': 'bytes',
                'use_array': True
            }
        ],
        'returns': 'ViStatus'
    },
    'GetLCRCompensationLastDateAndTime': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns the date and time the specified type of compensation data for LCR measurements was most recently generated.\nThe time returned is 24-hour (military) local time; for example, if the selected type of compensation data was generated at 2:30 PM, this function returns 14 for **hours** and 30 for **minutes**.\n',
            'note': '\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'get_lcr_compensation_last_date_and_time',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session.\n**vi** is obtained from the niDCPower_InitExtCal or niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value applies.\nSpecify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies channels 0 and 2).\nA channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are performed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the type of compensation for LCR measurements.\n'
                },
                'enum': 'LCRCompensationType',
                'name': 'compensationType',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the year of the relevant operation.\n'
                },
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the month of the relevant operation.\n'
                },
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the day of the relevant operation.\n'
                },
                'name': 'day',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the hour (in 24-hour time) of the relevant operation.\n'
                },
                'name': 'hour',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the minute of the relevant operation.\n'
                },
                'name': 'minute',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetLCRCustomCableCompensationData': {
        'documentation': {
            'description': '\nThis function is deprecated. Use niDCPower_GetLCRCompensationData\ninstead.\n\nCollects previously generated open and short custom cable compensation data so you can then apply it to LCR measurements with niDCPower_ConfigureLCRCustomCableCompensation.\n\nCall this function after you have obtained open and short custom cable compensation data. Pass the **custom cable compensation data** to niDCPower_ConfigureLCRCustomCableCompensation\n',
            'note': '\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session.\n**vi** is obtained from the niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value applies.\nSpecify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies channels 0 and 2).\nA channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are performed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'customCableCompensationDataSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe open and short custom cable compensation data to retrieve.\n'
                },
                'name': 'customCableCompensationData',
                'python_api_converter_name': 'convert_to_bytes',
                'python_type': 'bytes',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'customCableCompensationDataSize'
                },
                'type': 'ViAddr[]',
                'type_in_documentation': 'bytes',
                'use_array': True
            }
        ],
        'returns': 'ViStatus'
    },
    'GetLastExtCalLastDateAndTime': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Returns the date and time of the last successful calibration.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'datetime_wrappers'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. **vi** is obtained from the niDCPower_InitExtCal or niDCPower_InitializeWithChannels function.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates date and time of the last calibration.'
                },
                'name': 'lastCalDatetime',
                'type': 'hightime.datetime'
            }
        ],
        'python_name': 'get_ext_cal_last_date_and_time',
        'real_datetime_call': 'GetExtCalLastDateAndTime',
        'returns': 'ViStatus'
    },
    'GetLastLCRCompensationLastDateAndTime': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nReturns the date and time the specified type of compensation data for LCR measurements was most recently generated.\n',
            'note': '\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'datetime_wrappers'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session.\n**vi** is obtained from the niDCPower_InitExtCal or niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value applies.\nSpecify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies channels 0 and 2).\nA channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are performed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the type of compensation for LCR measurements.\n'
                },
                'enum': 'LCRCompensationType',
                'grpc_enum': None,
                'name': 'compensationType',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the date and time the specified type of compensation data for LCR measurements was most recently generated.\n'
                },
                'name': 'lastCompDatetime',
                'type': 'hightime.datetime'
            }
        ],
        'python_name': 'get_lcr_compensation_last_date_and_time',
        'real_datetime_call': 'GetLCRCompensationLastDateAndTime',
        'returns': 'ViStatus'
    },
    'GetLastSelfCalLastDateAndTime': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Returns the date and time of the oldest successful self-calibration from among the channels in the session.',
            'note': '\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'datetime_wrappers'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. **vi** is obtained from the niDCPower_InitExtCal or niDCPower_InitializeWithChannels function.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the date and time the device was last calibrated.'
                },
                'name': 'lastCalDatetime',
                'type': 'hightime.datetime'
            }
        ],
        'python_name': 'get_self_cal_last_date_and_time',
        'real_datetime_call': 'GetSelfCalLastDateAndTime',
        'returns': 'ViStatus'
    },
    'GetSelfCalLastDateAndTime': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns the date and time of the oldest successful self-calibration from\namong the channels in the session.\n\nThe time returned is 24-hour (military) local time; for example, if you\nhave a session using channels 1 and 2, and a self-calibration was\nperformed on channel 1 at 2:30 PM, and a self-calibration was performed\non channel 2 at 3:00 PM on the same day, this function returns 14 for\n**hours** and 30 for **minutes**.\n',
            'note': '\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'get_self_cal_last_date_and_time',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitExtCal or niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **year** the device was last calibrated.'
                },
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **month** in which the device was last calibrated.'
                },
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **day** on which the device was last calibrated.'
                },
                'name': 'day',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the **hour** (in 24-hour time) in which the device was last\ncalibrated.\n'
                },
                'name': 'hour',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **minute** in which the device was last calibrated.'
                },
                'name': 'minute',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSelfCalLastTemp': {
        'documentation': {
            'description': '\nReturns the onboard temperature of the device, in degrees Celsius,\nduring the oldest successful self-calibration from among the channels in\nthe session.\n\nFor example, if you have a session using channels 1 and 2, and you\nperform a self-calibration on channel 1 with a device temperature of 25\ndegrees Celsius at 2:00, and a self-calibration was performed on channel\n2 at 27 degrees Celsius at 3:00 on the same day, this function returns\n25 for the **temperature** parameter.\n',
            'note': '\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitExtCal or niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the onboard **temperature** of the device, in degrees Celsius,\nduring the oldest successful calibration.\n'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributeConfigurationBuffer': {
        'documentation': {
            'description': '\nImports an attribute configuration to the session from the specified\nconfiguration buffer.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers and the same number of configured\nchannels.\n\n**Support for this Function**\n\nCalling this function in `Sequence Source\nMode <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ is unsupported.\n\n**Channel Mapping Behavior for Multichannel Sessions**\n\nWhen importing and exporting session attribute configurations between\nNI‑DCPower sessions that were initialized with different channels, the\nconfigurations of the exporting channels are mapped to the importing\nchannels in the order you specify in the **channelName** input to the\nniDCPower_InitializeWithChannels function.\n\nFor example, if your entry for **channelName** is 0,1 for the exporting\nsession and 1,2 for the importing session:\n\n-  The configuration exported from channel 0 is imported into channel 1.\n-  The configuration exported from channel 1 is imported into channel 2.\n\n**Related Topics:**\n\n`Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__\n\n`Using Properties and\nAttributes <REPLACE_DRIVER_SPECIFIC_URL_1(using_properties_and_attributes)>`__\n\n`Setting Properties and Attributes Before Reading\nThem <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__\n',
            'note': '\nThis function will return an error if the total number of channels\ninitialized for the exporting session is not equal to the total number\nof channels initialized for the importing session.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the size, in bytes, of the byte array to import. If you enter\n0, this function returns the needed size.\n'
                },
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the byte array buffer that contains the attribute\nconfiguration to import.\n'
                },
                'name': 'configuration',
                'python_api_converter_name': 'convert_to_bytes',
                'python_type': 'bytes',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViAddr[]',
                'type_in_documentation': 'bytes'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributeConfigurationFile': {
        'documentation': {
            'description': '\nImports an attribute configuration to the session from the specified\nfile.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers and the same number of configured\nchannels.\n\n**Support for this Function**\n\nCalling this function in `Sequence Source\nMode <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ is unsupported.\n\n**Channel Mapping Behavior for Multichannel Sessions**\n\nWhen importing and exporting session attribute configurations between\nNI‑DCPower sessions that were initialized with different channels, the\nconfigurations of the exporting channels are mapped to the importing\nchannels in the order you specify in the **channelName** input to the\nniDCPower_InitializeWithChannels function.\n\nFor example, if your entry for **channelName** is 0,1 for the exporting\nsession and 1,2 for the importing session:\n\n-  The configuration exported from channel 0 is imported into channel 1.\n-  The configuration exported from channel 1 is imported into channel 2.\n\n**Related Topics:**\n\n`Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__\n\n`Using Properties and\nAttributes <REPLACE_DRIVER_SPECIFIC_URL_1(using_properties_and_attributes)>`__\n\n`Setting Properties and Attributes Before Reading\nThem <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__\n',
            'note': '\nThis function will return an error if the total number of channels\ninitialized for the exporting session is not equal to the total number\nof channels initialized for the importing session.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the absolute path to the file containing the attribute\nconfiguration to import. If you specify an empty or relative path, this\nfunction returns an error.\n**Default File Extension:** .nidcpowerconfig\n'
                },
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitializeWithChannels': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nCreates and returns a new NI-DCPower session to the instrument\nspecified in **resource name** to be used in all subsequent NI-DCPower\nfunction calls. With this function, you can optionally set the initial\nstate of the following session attributes:\n\n-  NIDCPOWER_ATTR_SIMULATE\n-  NIDCPOWER_ATTR_DRIVER_SETUP\n\nAfter calling this function, the session will be in the Uncommitted\nstate. Refer to the `Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic for\ndetails about specific software states.\n\nTo place the device in a known start-up state when creating a new\nsession, set **reset** to VI_TRUE. This action is equivalent to using\nthe niDCPower_ResetWithChannels function immediately after initializing the\nsession.\n\nTo open a session and leave the device in its existing configuration\nwithout passing through a transitional output state, set **reset** to\nVI_FALSE. Then configure the device as in the previous session,\nchanging only the desired settings, and then call the\nniDCPower_InitiateWithChannels function.\n\n**Related Topics:**\n\n`Programming States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': '__init__',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'initialization_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **resourceName** assigned by Measurement & Automation\nExplorer (MAX), for example "PXI1Slot3" where "PXI1Slot3" is an\ninstrument\'s **resourceName**. **resourceName** can also be a logical\nIVI name.\n'
                },
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies which channel(s) to include in a new session. Specify\nmultiple channels by using a channel list or a channel range. A channel\nlist is a comma (,) separated sequence of channel names (for example,\n0,2 specifies channels 0 and 2). A channel range is a lower bound\nchannel followed by a hyphen (-) or colon (:) followed by an upper bound\nchannel (for example, 0-2 specifies channels 0, 1, and 2). In the\nRunning state, multiple channel configurations are performed\nsequentially based on the order specified in this parameter. If you do\nnot specify any channels, by default all channels on the device are\nincluded in the session.\n'
                },
                'is_repeated_capability': False,
                'name': 'channels',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether to reset the device during the initialization\nprocedure.\n'
                },
                'name': 'reset',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the initial value of certain attributes for the session.\nThe syntax for **optionString** is a list of attributes with an assigned\nvalue where 1 is VI_TRUE and 0 is VI_FALSE. For example:\n\n"Simulate=0"\n\nYou do not have to specify a value for all the attributes. If you do not\nspecify a value for an attribute, the default value is used.\n\nFor more information about simulating a device, refer to `Simulating an\nInstrument <REPLACE_DRIVER_SPECIFIC_URL_1(simulate)>`__.\n'
                },
                'name': 'optionString',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a session handle that you use to identify the device in all\nsubsequent NI-DCPower function calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'InitializeWithIndependentChannels': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nCreates a new NI-DCPower session to the specified instrument(s) and channel(s) and returns a\nsession handle to be used in all subsequent NI-DCPower function calls.\n\nAfter calling this function, the specified channel or channels will be in the Uncommitted\nstate.\n\nWith this function and channel-based NI-DCPower functions and attributes, you can use any\nchannels in the session independently. For example, you can initiate a subset of channels in\nthe session with niDCPower_InitiateWithChannels, and the other channels in the session\nremain in the Uncommitted state.\n\n**Details of Independent Channel Operation**\n\nWhen you initialize with independent channels, each channel steps through the NI-DCPower\nprogramming state model independently of all other channels, and you can specify a subset\nof channels for most operations.\n\n**Note** You can make concurrent calls to a session from multiple threads, but the session\nexecutes the calls one at a time. If you specify multiple channels for a function or\nattribute, the session may perform the operation on multiple channels in parallel, though\nthis is not guaranteed, and some operations may execute sequentially.\n\n**Related Topics:**\n\n`Programming States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': '__init__',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'initialization_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the NI-DCPower resources to use in the session.\nNI-DCPower resources can be names of the instrument(s) assigned by Measurement &\nAutomation Explorer (MAX) and the channel(s) to initialize. Specify the\ninstrument(s) and channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3\nor PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are\ninstrument resource names and 0, 2, and 3 are channels.\n\nIf you pass "" for this control, all channels of the instrument(s) are included in\nthe session.\n'
                },
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether to reset channel(s) during the initialization procedure.\nThe default is VI_FALSE.\n\nTo place channel(s) in a known startup state when creating a new session, set\n**reset** to VI_TRUE. This action is equivalent to using the niDCPower_ResetWithChannels\nfunction immediately after initializing the session.\n\nTo open a session and leave the channel(s) in an existing configuration without\npassing through a transitional output state, set **reset** to VI_FALSE. Next, configure\nthe channel(s) as in the previous session, change the desired settings, and then\ncall the niDCPower_InitiateWithChannels function to write both settings.\n'
                },
                'name': 'reset',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the initial value of certain attributes for the session.\nThe syntax for **optionString** is a list of attributes with an assigned value where\n1 is VI_TRUE and 0 is VI_FALSE. For example:\n\nSimulate=0, DriverSetup=Model:<model number>; BoardType:<bus connector>\n\nTo simulate a multi-instrument session, set Simulate to 1 and list multiple\ninstruments for DriverSetup. For example:\n\nSimulate=1, DriverSetup=ResourceName:<instrument name>; Model:<model number>;\nBoardType:<bus connector> & ResourceName:<resource name>; Model:<model number>;\nBoardType:<bus connector>\n\nYou do not have to specify a value for all the attributes. If you do not specify a\nvalue for an attribute, the default value is used.\n\nFor more information about simulating a device, refer to `Simulating an\nInstrument <REPLACE_DRIVER_SPECIFIC_URL_1(simulate)>`__.\n'
                },
                'name': 'optionString',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a session handle that you use to identify the session in all\nsubsequent NI-DCPower function calls.'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'InitiateWithChannels': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nStarts generation or acquisition, causing the specified channel(s) to\nleave the Uncommitted state or Committed state and enter the Running\nstate. To return to the Uncommitted state call the niDCPower_AbortWithChannels\nfunction. Refer to the `Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in\nthe *NI DC Power Supplies and SMUs Help* for information about the\nspecific NI-DCPower software states.\n\n**Related Topics:**\n\n`Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'initiate',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'LockSession': {
        'documentation': {
            'description': '\n| Obtains a multithread lock on the device session. Before doing so, the\n  software waits until all other execution threads release their locks\n  on the device session.\n| Other threads may have obtained a lock on this session for the\n  following reasons:\n\n-  The application called the niDCPower_LockSession function.\n-  A call to NI-DCPower locked the session.\n-  A call to the IVI engine locked the session.\n-  After a call to the niDCPower_LockSession function returns\n   successfully, no other threads can access the device session until\n   you call the niDCPower_UnlockSession function.\n-  Use the niDCPower_LockSession function and the\n   niDCPower_UnlockSession function around a sequence of calls to\n   instrument driver functions if you require that the device retain its\n   settings through the end of the sequence.\n\nYou can safely make nested calls to the niDCPower_LockSession function\nwithin the same thread. To completely unlock the session, you must\nbalance each call to the niDCPower_LockSession function with a call to\nthe niDCPower_UnlockSession function. If, however, you use\n**Caller_Has_Lock** in all calls to the niDCPower_LockSession and\nniDCPower_UnlockSession function within a function, the IVI Library\nlocks the session only once within the function regardless of the number\nof calls you make to the niDCPower_LockSession function. This behavior\nallows you to call the niDCPower_UnlockSession function just once at\nthe end of the function.\n'
        },
        'included_in_proto': False,
        'method_templates': [
            {
                'documentation_filename': 'lock',
                'library_interpreter_filename': 'lock',
                'method_python_name_suffix': '',
                'session_filename': 'lock'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\n| This parameter is optional. If you do not want to use this parameter,\n  pass VI_NULL.\n| Use this parameter in complex functions to keep track of whether you\n  obtain a lock and therefore need to unlock the session. Pass the\n  address of a local ViBoolean variable. In the declaration of the local\n  variable, initialize it to VI_FALSE. Pass the address of the same\n  local variable to any other calls you make to the\n  niDCPower_LockSession function or the niDCPower_UnlockSession\n  function in the same function.\n| The parameter is an input/output parameter. The niDCPower_LockSession\n  and niDCPower_UnlockSession functions each inspect the current value\n  and take the following actions.\n\n-  If the value is VI_TRUE, the niDCPower_LockSession function does\n   not lock the session again.\n-  If the value is VI_FALSE, the niDCPower_LockSession function\n   obtains the lock and sets the value of the parameter to VI_TRUE.\n-  If the value is VI_FALSE, the niDCPower_UnlockSession function does\n   not attempt to unlock the session.\n-  If the value is VI_TRUE, the niDCPower_UnlockSession function\n   releases the lock and sets the value of the parameter to VI_FALSE.\n\n| Thus, you can, call the niDCPower_UnlockSession function at the end\n  of your function without worrying about whether you actually have the\n  lock, as shown in the following example.\n| ViStatus TestFunc (ViSession vi, ViInt32 flags)\n  {\n  ViStatus error = VI_SUCCESS;\n  ViBoolean haveLock = VI_FALSE;\n  if (flags & BIT_1)\n  {\n  viCheckErr( niDCPower_LockSession(vi, &haveLock;));\n  viCheckErr( TakeAction1(vi));\n  if (flags & BIT_2)\n  {\n  viCheckErr( niDCPower_UnlockSession(vi, &haveLock;));\n  viCheckErr( TakeAction2(vi));\n  viCheckErr( niDCPower_LockSession(vi, &haveLock;);\n  }\n  if (flags & BIT_3)\n  viCheckErr( TakeAction3(vi));\n  }\n  Error:\n  /\\*At this point, you cannot really be sure that you have the lock.\n  Fortunately, the haveLock variable takes care of that for you.\\*/\n  niDCPower_UnlockSession(vi, &haveLock;);\n  return error;\n| }\n'
                },
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'python_name': 'lock',
        'render_in_session_base': True,
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'Measure': {
        'documentation': {
            'description': '\nReturns the measured value of either the voltage or current on the\nspecified channel. Each call to this function blocks other\nfunction calls until the hardware returns the **measurement**. To\nmeasure multiple channels, use the niDCPower_MeasureMultiple\nfunction.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel to measure. Only one measurement at a time\nmay be made with the niDCPower_Measure function. Use the\nniDCPower_MeasureMultiple function to measure multiple channels.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether a voltage or current value is measured.\n**Defined Values**:\n',
                    'table_body': [
                        [
                            'NIDCPOWER_VAL_MEASURE_VOLTAGE',
                            'The device measures voltage.'
                        ],
                        [
                            'NIDCPOWER_VAL_MEASURE_CURRENT',
                            'The device measures current.'
                        ]
                    ]
                },
                'enum': 'MeasurementTypes',
                'name': 'measurementType',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the value of the measurement, either in volts for voltage or\namps for current.\n'
                },
                'name': 'measurement',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'MeasureMultiple': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns arrays of the measured voltage and current values on the\nspecified channel(s). Each call to this function blocks other\nfunction calls until the measurements are returned from the device. The\norder of the measurements returned in the array corresponds to the order\non the specified channel(s).\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'measure_multiple',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channels to measure. You can specify multiple\nchannels by using a channel list or a channel range. A channel list is a\ncomma (,) separated sequence of channel names (e.g. 0,2 specifies\nchannels 0 and 2). A channel range is a lower bound channel followed by\na hyphen (-) or colon (:) followed by an upper bound channel (e.g. 0-2\nspecifies channels 0, 1, and 2). If you do not specify a channel name,\nthe function uses all channels in the session.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array of voltage measurements. The measurements in the array\nare returned in the same order as the channels specified in\n**channelName**. Ensure that sufficient space has been allocated for the\nreturned array.\n'
                },
                'name': 'voltageMeasurements',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self.parse_channel_count(channel_name)'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array of current measurements. The measurements in the array\nare returned in the same order as the channels specified in\n**channelName**. Ensure that sufficient space has been allocated for the\nreturned array.\n'
                },
                'name': 'currentMeasurements',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self.parse_channel_count(channel_name)'
                },
                'type': 'ViReal64[]',
                'use_array': True
            }
        ],
        'returns': 'ViStatus'
    },
    'MeasureMultipleLCR': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nMeasures and returns a list of LCRMeasurement instances on the specified channel(s).\n\nTo use this function:\n\n-  Set NIDCPOWER_ATTR_INSTRUMENT_MODE property to NIDCPOWER_VAL_LCR\n-  Set NIDCPOWER_ATTR_MEASURE_WHEN property to NIDCPOWER_VAL_ON_DEMAND\n-  Put the channel(s) in the Running state (call niDCPower_InitiateWithChannels)\n',
            'note': '\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session.\n**vi** is obtained from the niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value applies.\nSpecify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies channels 0 and 2).\nA channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are performed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nA list of LCRMeasurement instances.\n',
                    'table_body': [
                        [
                            'vdc',
                            'float',
                            'The measured DC voltage, in volts.'
                        ],
                        [
                            'idc',
                            'float',
                            'The measured DC current, in amps.'
                        ],
                        [
                            'stimulus_frequency',
                            'float',
                            'The frequency of the LCR test signal, in Hz.'
                        ],
                        [
                            'ac_voltage',
                            'complex',
                            'The measured AC voltage, in volts RMS.'
                        ],
                        [
                            'ac_current',
                            'complex',
                            'The measured AC current, in amps RMS.'
                        ],
                        [
                            'z',
                            'complex',
                            'The complex impedance.'
                        ],
                        [
                            'z_magnitude_and_phase',
                            'tuple of float',
                            'The magnitude, in ohms, and phase angle, in degrees, of the complex impedance.'
                        ],
                        [
                            'y',
                            'complex',
                            'The complex admittance.'
                        ],
                        [
                            'y_magnitude_and_phase',
                            'tuple of float',
                            'The magnitude, in siemens, and phase angle, in degrees, of the complex admittance.'
                        ],
                        [
                            'series_lcr',
                            'LCR',
                            'The inductance, in henrys, the capacitance, in farads, and the resistance, in ohms, as measured using a series circuit model.'
                        ],
                        [
                            'parallel_lcr',
                            'LCR',
                            'The inductance, in henrys, the capacitance, in farads, and the resistance, in ohms, as measured using a parallel circuit model.'
                        ],
                        [
                            'd',
                            'float',
                            'The dissipation factor of the circuit. The dimensionless dissipation factor is directly proportional to how quickly an oscillating system loses energy. D is the reciprocal of Q, the quality factor.'
                        ],
                        [
                            'q',
                            'float',
                            'The quality factor of the circuit. The dimensionless quality factor is inversely proportional to the degree of damping in a system. Q is the reciprocal of D, the dissipation factor.'
                        ],
                        [
                            'measurement_mode',
                            'enums.InstrumentMode',
                            'The measurement mode: **SMU** - The channel(s) are operating as a power supply/SMU. **LCR** - The channel(s) are operating as an LCR meter.'
                        ],
                        [
                            'dc_in_compliance',
                            'bool',
                            'Indicates whether the output was in DC compliance at the time the measurement was taken.'
                        ],
                        [
                            'ac_in_compliance',
                            'bool',
                            'Indicates whether the output was in AC compliance at the time the measurement was taken.'
                        ],
                        [
                            'unbalanced',
                            'bool',
                            'Indicates whether the output was unbalanced at the time the measurement was taken.'
                        ]
                    ]
                },
                'name': 'measurements',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self.parse_channel_count(channel_name)'
                },
                'type': 'NILCRMeasurement[]',
                'use_array': False
            }
        ],
        'returns': 'ViStatus'
    },
    'ParseChannelCount': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the number of channels.'
        },
        'included_in_proto': False,
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelsString',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'name': 'numberOfChannels',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'PerformLCRLoadCompensation': {
        'documentation': {
            'description': '\nGenerates load compensation data for LCR measurements for the test spots you specify.\n\nYou must physically configure your LCR circuit with an appropriate reference load to use this function to generate valid load compensation data.\n\nWhen you call this function:\n\n-  The load compensation data is written to the onboard storage of the instrument. Onboard storage can contain only the most recent set of data.\n-  Most NI-DCPower attributes in the session are reset to their default values. Rewrite the values of any attributes you want to maintain.\n\nTo apply the load compensation data you generate with this function to your LCR measurements, set the NIDCPOWER_ATTR_LCR_LOAD_COMPENSATION_ENABLED property to VI_TRUE.\n\nLoad compensation data are generated only for those specific frequencies you define with this function; load compensation is not interpolated from the specific frequencies you define and applied to other frequencies.\n',
            'note': '\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session.\n**vi** is obtained from the niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value applies.\nSpecify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sfequence of channel names (for example, 0,2 specifies channels 0 and 2).\nA channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are performed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe number of elements defined in **compensation spots**.\n'
                },
                'name': 'numCompensationSpots',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nDefines the frequencies and DUT specifications to use for LCR load compensation.\n\nYou can specify <=1000 spot frequencies.\n',
                    'table_body': [
                        [
                            'frequency',
                            'The spot frequency, in Hz.'
                        ],
                        [
                            'reference_value_type',
                            'A known specification value of your DUT to use as the basis for load compensation.'
                        ],
                        [
                            'reference_value',
                            'A value that describes the **reference_value_type** specification. Use as indicated by the **reference_value_type** option you choose.'
                        ]
                    ]
                },
                'name': 'compensationSpots',
                'size': {
                    'mechanism': 'len',
                    'value': 'numCompensationSpots'
                },
                'type': 'NILCRLoadCompensationSpot[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'PerformLCROpenCompensation': {
        'documentation': {
            'description': '\nGenerates open compensation data for LCR measurements based on a default set of test frequencies and, optionally, additional frequencies you can specify.\n\nYou must physically configure an open LCR circuit to use this function to generate valid open compensation data.\n\nWhen you call this function:\n\n-  The open compensation data is written to the onboard storage of the instrument. Onboard storage can contain only the most recent set of data.\n-  Most NI-DCPower attributes in the session are reset to their default values. Rewrite the values of any attributes you want to maintain.\n\nTo apply the open compensation data you generate with this method to your LCR measurements, set the NIDCPOWER_ATTR_LCR_OPEN_COMPENSATION_ENABLED property to VI_TRUE.\n\nCorrections for frequencies other than the default frequencies or any additional frequencies you specify are interpolated.\n',
            'note': [
                '\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n',
                '\nDefault Open Compensation Frequencies:\nBy default, NI-DCPower uses the following frequencies for LCR open compensation:\n\n-  10 logarithmic steps at 1 kHz frequency decade\n-  10 logarithmic steps at 10 kHz frequency decade\n-  100 logarithmic steps at 100 kHz frequency decade\n-  100 logarithmic steps at 1 MHz frequency decade\n\nThe actual frequencies used depend on the bandwidth of your instrument.\n'
            ]
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session.\n**vi** is obtained from the niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value applies.\nSpecify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies channels 0 and 2).\nA channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are performed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe number of frequencies defined in **addtional frequencies**.\n'
                },
                'name': 'numFrequencies',
                'type': 'ViInt32'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': '\nDefines a further set of frequencies, in addition to the default frequencies, to perform the compensation for. You can specify <=200 additional frequencies.\n'
                },
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
        'documentation': {
            'description': '\nGenerates open custom cable compensation data for LCR measurements.\n\nTo use this function, you must physically configure an open LCR circuit to generate valid open custom cable compensation data.\n\nWhen you call this function:\n\n-  The open compensation data is written to the onboard storage of the instrument. Onboard storage can contain only the most recent set of data.\n-  Most NI-DCPower attributes in the session are reset to their default values. Rewrite the values of any attributes you want to maintain.\n',
            'note': '\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session.\n**vi** is obtained from the niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value applies.\nSpecify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies channels 0 and 2).\nA channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are performed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'PerformLCRShortCompensation': {
        'documentation': {
            'description': '\nGenerates short compensation data for LCR measurements based on a default set of test frequencies and, optionally, additional frequencies you can specify.\n\nYou must physically configure your LCR circuit with a short to use this function to generate valid short compensation data.\n\nWhen you call this function:\n\n-  The short compensation data is written to the onboard storage of the instrument. Onboard storage can contain only the most recent set of data.\n- Most NI-DCPower attributes in the session are reset to their default values. Rewrite the values of any attributes you want to maintain.\n\nTo apply the short compensation data you generate with this method to your LCR measurements, set the NIDCPOWER_ATTR_LCR_SHORT_COMPENSATION_ENABLED property to VI_TRUE.\n\nCorrections for frequencies other than the default frequencies or any additional frequencies you specify are interpolated.\n',
            'note': [
                '\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n',
                '\nDefault Short Compensation Frequencies:\nBy default, NI-DCPower uses the following frequencies for LCR short compensation:\n\n-  10 logarithmic steps at 1 kHz frequency decade\n-  10 logarithmic steps at 10 kHz frequency decade\n-  100 logarithmic steps at 100 kHz frequency decade\n-  100 logarithmic steps at 1 MHz frequency decade\n\nThe actual frequencies used depend on the bandwidth of your instrument.'
            ]
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session.\n**vi** is obtained from the niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value applies.\nSpecify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies channels 0 and 2).\nA channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are performed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe number of frequencies defined in **addtional frequencies**.\n'
                },
                'name': 'numFrequencies',
                'type': 'ViInt32'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': '\nDefines a further set of frequencies, in addition to the default frequencies, to perform the compensation for. You can specify <=200 additional frequencies.\n'
                },
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
        'documentation': {
            'description': '\nGenerates short custom cable compensation data for LCR measurements.\n\nTo use this function:\n\n-  You must physically configure your LCR circuit with a short to generate valid short custom cable compensation data.\n-  Set NIDCPOWER_ATTR_LCR_SHORT_CUSTOM_CABLE_COMPENSATION_ENABLED property to VI_TRUE \n\nWhen you call this function:\n\n-  The short compensation data is written to the onboard storage of the instrument. Onboard storage can contain only the most recent set of data.\n-  Most NI-DCPower properties in the session are reset to their default values. Rewrite the values of any properties you want to maintain.\n',
            'note': '\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session.\n**vi** is obtained from the niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value applies.\nSpecify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies channels 0 and 2).\nA channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are performed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'PublicGetChannelNameFromString': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nReturns a list of channel names for the given channel indices.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'get_channel_names'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIndex list for the channels in the session. Valid values are from zero to the total number of channels in the session minus one. The index string can be one of the following formats:\n\n-   A comma-separated list—for example, "0,2,3,1"\n-   A range using a hyphen—for example, "0-3"\n-   A range using a colon—for example, "0:3 "\n\nYou can combine comma-separated lists and ranges that use a hyphen or colon. Both out-of-order and repeated indices are supported ("2,3,0," "1,2,2,3"). White space characters, including spaces, tabs, feeds, and carriage returns, are allowed between characters. Ranges can be incrementing or decrementing.\n'
                },
                'grpc_name': 'index',
                'name': 'index',
                'python_api_converter_name': 'convert_repeated_capabilities_without_prefix',
                'python_name': 'indices',
                'type': 'ViString',
                'type_in_documentation': 'basic sequence types or str or int'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe number of elements in the ViChar array you specify for name.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The channel name(s) at the specified indices.'
                },
                'grpc_name': 'channel_name',
                'is_repeated_capability': False,
                'name': 'channelName',
                'python_api_converter_name': 'convert_comma_separated_string_to_list',
                'python_name': 'names',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViString',
                'type_in_documentation': 'list of str'
            }
        ],
        'python_name': 'get_channel_names',
        'returns': 'ViStatus'
    },
    'QueryInCompliance': {
        'documentation': {
            'description': '\nQueries the specified channel to determine if it is operating at the compliance limit.\n\nThe compliance limit is the current limit when the NIDCPOWER_ATTR_OUTPUT_FUNCTION property is set to NIDCPOWER_VAL_DC_VOLTAGE, NIDCPOWER_VAL_PULSE_VOLTAGE, NIDCPOWER_VAL_CONSTANT_RESISTANCE or NIDCPOWER_VAL_CONSTANT_POWER. If the output is operating at the compliance limit, the output reaches the current limit before the desired voltage, resistance or power level.\n\nThe compliance limit is the voltage limit when the NIDCPOWER_ATTR_OUTPUT_FUNCTION property is set to NIDCPOWER_VAL_DC_CURRENT or NIDCPOWER_VAL_PULSE_CURRENT. If the output is operating at the compliance limit, the output reaches the voltage limit before the desired current level.\n\nRefer to the NIDCPOWER_ATTR_OUTPUT_FUNCTION property for more information about the applicable properties to configure for each output function.\n',
            'note': '\nNI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel to query. Compliance status can only be\nqueried for one channel at a time.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns whether the device channel is in compliance.'
                },
                'name': 'inCompliance',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'QueryLatchedOutputCutoffState': {
        'documentation': {
            'description': '\nDiscovers if an output cutoff limit was exceeded for the specified reason. When an output cutoff is engaged, the output of the channel(s) is disconnected.\nIf a limit was exceeded, the state is latched until you clear it with the niDCPower_ClearLatchedOutputCutoffState function or the niDCPower_ResetWithChannels function.\n\noutputCutoffReason specifies the conditions for which an output is disconnected.\n',
            'note': '\nNI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies which output cutoff conditions to query.\n',
                    'table_body': [
                        [
                            'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_ALL',
                            'Any output cutoff condition was met'
                        ],
                        [
                            'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_OUTPUT_HIGH',
                            'The output exceeded the high cutoff limit for voltage output'
                        ],
                        [
                            'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_OUTPUT_LOW',
                            'The output fell below the low cutoff limit for voltage output'
                        ],
                        [
                            'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_MEASURE_HIGH',
                            'The measured voltage exceeded the high cutoff limit for voltage output'
                        ],
                        [
                            'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_MEASURE_LOW',
                            'The measured voltage fell below the low cutoff limit for voltage output'
                        ],
                        [
                            'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_MEASURE_HIGH',
                            'The measured current exceeded the high cutoff limit for current output'
                        ],
                        [
                            'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_MEASURE_LOW',
                            'The measured current fell below the low cutoff limit for current output'
                        ],
                        [
                            'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_CHANGE_HIGH',
                            'The voltage slew rate increased beyond the positive change cutoff for voltage output'
                        ],
                        [
                            'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_CHANGE_LOW',
                            'The voltage slew rate decreased beyond the negative change cutoff for voltage output'
                        ],
                        [
                            'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_CHANGE_HIGH',
                            'The current slew rate increased beyond the positive change cutoff for current output'
                        ],
                        [
                            'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_CHANGE_LOW',
                            'The current slew rate decreased beyond the negative change cutoff for current output'
                        ],
                        [
                            'NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_SATURATED',
                            'The measured current saturates the current range'
                        ]
                    ]
                },
                'enum': 'OutputCutoffReason',
                'name': 'outputCutoffReason',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies whether an output cutoff has engaged.\n',
                    'table_body': [
                        [
                            'VI_TRUE',
                            'An output cutoff has engaged for the conditions in **output cutoff reason**.'
                        ],
                        [
                            'VI_FALSE',
                            'No output cutoff has engaged.'
                        ]
                    ]
                },
                'name': 'outputCutoffState',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'QueryMaxCurrentLimit': {
        'documentation': {
            'description': '\nQueries the maximum current limit on a channel if the channel is set to the specified **voltageLevel**.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel to query. The maximum current limit may\nonly be queried for one channel at a time.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the voltage level to use when calculating the\n**maxCurrentLimit**.\n'
                },
                'name': 'voltageLevel',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the maximum current limit that can be set with the specified\n**voltageLevel**.\n'
                },
                'name': 'maxCurrentLimit',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'QueryMaxVoltageLevel': {
        'documentation': {
            'description': '\nQueries the maximum voltage level on a channel if the channel is set to the specified **currentLimit**.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel to query. The maximum voltage level may\nonly be queried for one channel at a time.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the current limit to use when calculating the\n**maxVoltageLevel**.\n'
                },
                'name': 'currentLimit',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the maximum voltage level that can be set on a channel\nwith the specified **currentLimit**.\n'
                },
                'name': 'maxVoltageLevel',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'QueryMinCurrentLimit': {
        'documentation': {
            'description': '\nQueries the minimum current limit on a channel if the channel is set to the specified **voltageLevel**.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel to query. The minimum current limit may\nonly be queried for one channel at a time.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the voltage level to use when calculating the\n**minCurrentLimit**.\n'
                },
                'name': 'voltageLevel',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the minimum current limit that can be set on a channel\nwith the specified **voltageLevel**.\n'
                },
                'name': 'minCurrentLimit',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'QueryOutputState': {
        'documentation': {
            'description': '\nQueries the specified channel to determine if the channel\nis currently in the state specified by **outputState**.\n\n**Related Topics:**\n\n`Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__\n',
            'note': '\nNI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel to query. The output state may only be\nqueried for one channel at a time.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output state of the channel that is being queried.\n**Defined Values**:\n',
                    'table_body': [
                        [
                            'NIDCPOWER_VAL_OUTPUT_CONSTANT_VOLTAGE',
                            'The channel maintains a constant voltage by adjusting the current.'
                        ],
                        [
                            'NIDCPOWER_VAL_OUTPUT_CONSTANT_CURRENT',
                            'The channel maintains a constant current by adjusting the voltage.'
                        ],
                        [
                            'NIDCPOWER_VAL_OUTPUT_INHIBITED',
                            'The channel is in the inhibited state.'
                        ]
                    ]
                },
                'enum': 'OutputStates',
                'name': 'outputState',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns whether the device channel is in the specified output\nstate.\n'
                },
                'name': 'inState',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadCurrentTemperature': {
        'documentation': {
            'description': '\nReturns the current onboard **temperature**, in degrees Celsius, of the\ndevice.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitExtCal or niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the onboard **temperature**, in degrees Celsius, of the device.'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetDevice': {
        'documentation': {
            'description': '\nResets the device to a known state. The function disables power\ngeneration, resets session attributes to their default values, clears\nerrors such as overtemperature and unexpected loss of auxiliary power,\ncommits the session attributes, and leaves the session in the\nUncommitted state. This function also performs a hard reset on the\ndevice and driver software. This function has the same functionality as\nusing reset in Measurement & Automation Explorer. Refer to the\n`Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic for\nmore information about NI-DCPower software states.\n\nThis will also open the output relay on devices that have an output\nrelay.\n',
            'note': '\nNI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetWithChannels': {
        'documentation': {
            'description': '\nResets the specified channel(s) to a known state. This function disables power\ngeneration, resets session attributes to their default values, commits\nthe session attributes, and leaves the session in the Uncommitted state.\nRefer to the `Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic for\nmore information about NI-DCPower software states.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'python_name': 'reset',
        'returns': 'ViStatus'
    },
    'ResetWithDefaults': {
        'documentation': {
            'description': "\nResets the device to a known state. This function disables power\ngeneration, resets session attributes to their default values, commits\nthe session attributes, and leaves the session in the\n`Running <javascript:LaunchHelp('NI_DC_Power_Supplies_Help.chm::/programmingStates.html#running')>`__\nstate. In addition to exhibiting the behavior of the niDCPower_ResetWithChannels\nfunction, this function can assign user-defined default values for\nconfigurable attributes from the IVI configuration.\n"
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SendSoftwareEdgeTriggerWithChannels': {
        'documentation': {
            'description': '\nAsserts the specified trigger. This function can override an external\nedge trigger.\n\n**Related Topics:**\n\n`Triggers <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__\n',
            'note': '\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies which trigger to assert.\n**Defined Values:**\n',
                    'table_body': [
                        [
                            'NIDCPOWER_VAL_START_TRIGGER',
                            'Asserts the Start trigger.'
                        ],
                        [
                            'NIDCPOWER_VAL_SOURCE_TRIGGER',
                            'Asserts the Source trigger.'
                        ],
                        [
                            'NIDCPOWER_VAL_MEASURE_TRIGGER',
                            'Asserts the Measure trigger.'
                        ],
                        [
                            'NIDCPOWER_VAL_SEQUENCE_ADVANCE_TRIGGER',
                            'Asserts the Sequence Advance trigger.'
                        ],
                        [
                            'NIDCPOWER_VAL_PULSE_TRIGGER',
                            'Asserts the Pulse trigger.'
                        ],
                        [
                            'NIDCPOWER_VAL_SHUTDOWN_TRIGGER',
                            'Asserts the Shutdown trigger.'
                        ]
                    ]
                },
                'enum': 'SendSoftwareEdgeTriggerType',
                'name': 'trigger',
                'type': 'ViInt32'
            }
        ],
        'python_name': 'send_software_edge_trigger',
        'returns': 'ViStatus'
    },
    'SetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\n| Sets the value of a ViBoolean attribute.\n| This is a low-level function that you can use to set the values of\n  device-specific attributes and inherent IVI attributes.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the ID of an attribute. From the function panel window, you\ncan use this control as follows.\n\n-  In the function panel window, click on the control or press **Enter**\n   or the spacebar to display a dialog box containing hierarchical list\n   of the available attributes. Attributes whose value cannot be set are\n   dim. Help text is shown for each attribute. Select an attribute by\n   double-clicking on it or by selecting it and then pressing **Enter**.\n-  Read-only attributes appear dim in the list box. If you select a\n   read-only attribute, an error message appears. A ring control at the\n   top of the dialog box allows you to see all IVI attributes or only\n   the attributes of type ViBoolean. If you choose to see all IVI\n   attributes, the data types appear to the right of the attribute names\n   in the list box. Attributes with data types other than ViBoolean are\n   dim. If you select an attribute data type that is dim, LabWindows/CVI\n   transfers you to the function panel for the corresponding function\n   that is consistent with the data type.\n-  If you want to enter a variable name, press **Ctrl**\\ +\\ **T** to\n   change this ring control to a manual input box. If the attribute in\n   this ring control has named constants as valid values, you can view\n   the constants by moving to the value control and pressing **Enter**.\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value to which you want to set the attribute. If the\nattribute currently showing in the attribute ring control has constants\nas valid values, you can view a list of the constants by pressing\n**Enter** on this control. Select a value by double-clicking on it or by\nselecting it and then pressing **Enter**.\n',
                    'note': '\nSome of the values might not be valid depending upon the current\nsettings of the device session.\n'
                },
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt32': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\n| Sets the value of a ViInt32 attribute.\n| This is a low-level function that you can use to set the values of\n  device-specific attributes and inherent IVI attributes.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the ID of an attribute. From the function panel window, you\ncan use this control as follows.\n\n-  In the function panel window, click on the control or press **Enter**\n   or the spacebar to display a dialog box containing hierarchical list\n   of the available attributes. Attributes whose value cannot be set are\n   dim. Help text is shown for each attribute. Select an attribute by\n   double-clicking on it or by selecting it and then pressing **Enter**.\n-  Read-only attributes appear dim in the list box. If you select a\n   read-only attribute, an error message appears. A ring control at the\n   top of the dialog box allows you to see all IVI attributes or only\n   the attributes of type ViInt32. If you choose to see all IVI\n   attributes, the data types appear to the right of the attribute names\n   in the list box. Attributes with data types other than ViInt32 are\n   dim. If you select an attribute data type that is dim, LabWindows/CVI\n   transfers you to the function panel for the corresponding function\n   that is consistent with the data type.\n-  If you want to enter a variable name, press **Ctrl**\\ +\\ **T** to\n   change this ring control to a manual input box. If the attribute in\n   this ring control has named constants as valid values, you can view\n   the constants by moving to the value control and pressing **Enter**.\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value to which you want to set the attribute. If the\nattribute currently showing in the attribute ring control has constants\nas valid values, you can view a list of the constants by pressing\n**Enter** on this control. Select a value by double-clicking on it or by\nselecting it and then pressing **Enter**.\n',
                    'note': '\nSome of the values might not be valid depending upon the current\nsettings of the device session.\n'
                },
                'grpc_enum': 'NiDCPowerInt32AttributeValues',
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\n| Sets the value of a ViInt64 attribute.\n| This is a low-level function that you can use to set the values of\n  device-specific attributes and inherent IVI attributes.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the ID of an attribute. From the function panel window, you\ncan use this control as follows.\n\n-  In the function panel window, click on the control or press **Enter**\n   or the spacebar to display a dialog box containing hierarchical list\n   of the available attributes. Attributes whose value cannot be set are\n   dim. Help text is shown for each attribute. Select an attribute by\n   double-clicking on it or by selecting it and then pressing **Enter**.\n-  Read-only attributes appear dim in the list box. If you select a\n   read-only attribute, an error message appears. A ring control at the\n   top of the dialog box allows you to see all IVI attributes or only\n   the attributes of type ViReal64. If you choose to see all IVI\n   attributes, the data types appear to the right of the attribute names\n   in the list box. Attributes with data types other than ViReal64 are\n   dim. If you select an attribute data type that is dim, LabWindows/CVI\n   transfers you to the function panel for the corresponding function\n   that is consistent with the data type.\n-  If you want to enter a variable name, press **Ctrl**\\ +\\ **T** to\n   change this ring control to a manual input box. If the attribute in\n   this ring control has named constants as valid values, you can view\n   the constants by moving to the value control and pressing **Enter**.\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value to which you want to set the attribute. If the\nattribute currently showing in the attribute ring control has constants\nas valid values, you can view a list of the constants by pressing\n**Enter** on this control. Select a value by double-clicking on it or by\nselecting it and then pressing **Enter**.\n',
                    'note': '\nSome of the values might not be valid depending upon the current\nsettings of the device session.\n'
                },
                'grpc_name': 'attribute_value_raw',
                'name': 'attributeValue',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\n| Sets the value of a ViReal64 attribute.\n| This is a low-level function that you can use to set the values of\n  device-specific attributes and inherent IVI attributes.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the ID of an attribute. From the function panel window, you\ncan use this control as follows.\n\n-  In the function panel window, click on the control or press **Enter**\n   or the spacebar to display a dialog box containing hierarchical list\n   of the available attributes. Attributes whose value cannot be set are\n   dim. Help text is shown for each attribute. Select an attribute by\n   double-clicking on it or by selecting it and then pressing **Enter**.\n-  Read-only attributes appear dim in the list box. If you select a\n   read-only attribute, an error message appears. A ring control at the\n   top of the dialog box allows you to see all IVI attributes or only\n   the attributes of type ViReal64. If you choose to see all IVI\n   attributes, the data types appear to the right of the attribute names\n   in the list box. Attributes with data types other than ViReal64 are\n   dim. If you select an attribute data type that is dim, LabWindows/CVI\n   transfers you to the function panel for the corresponding function\n   that is consistent with the data type.\n-  If you want to enter a variable name, press **Ctrl**\\ +\\ **T** to\n   change this ring control to a manual input box. If the attribute in\n   this ring control has named constants as valid values, you can view\n   the constants by moving to the value control and pressing **Enter**.\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value to which you want to set the attribute. If the\nattribute currently showing in the attribute ring control has constants\nas valid values, you can view a list of the constants by pressing\n**Enter** on this control. Select a value by double-clicking on it or by\nselecting it and then pressing **Enter**.\n',
                    'note': '\nSome of the values might not be valid depending upon the current\nsettings of the device session.\n'
                },
                'grpc_name': 'attribute_value_raw',
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\n| Sets the value of a ViString attribute.\n| This is a low-level function that you can use to set the values of\n  device-specific attributes and inherent IVI attributes.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the ID of an attribute. From the function panel window, you\ncan use this control as follows.\n\n-  In the function panel window, click on the control or press **Enter**\n   or the spacebar to display a dialog box containing hierarchical list\n   of the available attributes. Attributes whose value cannot be set are\n   dim. Help text is shown for each attribute. Select an attribute by\n   double-clicking on it or by selecting it and then pressing **Enter**.\n-  Read-only attributes appear dim in the list box. If you select a\n   read-only attribute, an error message appears. A ring control at the\n   top of the dialog box allows you to see all IVI attributes or only\n   the attributes of type ViString. If you choose to see all IVI\n   attributes, the data types appear to the right of the attribute names\n   in the list box. Attributes with data types other than ViString are\n   dim. If you select an attribute data type that is dim, LabWindows/CVI\n   transfers you to the function panel for the corresponding function\n   that is consistent with the data type.\n-  If you want to enter a variable name, press **Ctrl**\\ +\\ **T** to\n   change this ring control to a manual input box. If the attribute in\n   this ring control has named constants as valid values, you can view\n   the constants by moving to the value control and pressing **Enter**.\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value to which you want to set the attribute. If the\nattribute currently showing in the attribute ring control has constants\nas valid values, you can view a list of the constants by pressing\n**Enter** on this control. Select a value by double-clicking on it or by\nselecting it and then pressing **Enter**.\n',
                    'note': '\nSome of the values might not be valid depending upon the current\nsettings of the device session.\n'
                },
                'grpc_name': 'attribute_value_raw',
                'name': 'attributeValue',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetRuntimeEnvironment': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'TBD'
        },
        'included_in_proto': False,
        'method_templates': [
            {
                'documentation_filename': 'none',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'none'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'environment',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'environmentVersion',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'reserved1',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'reserved2',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetSequence': {
        'documentation': {
            'description': '\nConfigures a series of voltage, current, resistance or power outputs and corresponding source delays. The source mode must be set to NIDCPOWER_VAL_SEQUENCE for this function to take effect.\n\nRefer to the Configuring the Source Unit topic in the *NI DC Power Supplies and SMUs Help* for more information about how to configure your device.\n\nUse this function in the Uncommitted or Committed programming states.\nRefer to the Programming States topic in the *NI DC Power Supplies and SMUs Help* for more information about NI-DCPower programming states.\n\nUsing this function with Advanced Sequence functions for the same channel in the same session is not supported.\n',
            'note': '\nNI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.\n\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel to which this configuration value applies.\nYou can only set a sequence for one channel at a time.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the series of voltage, current, resistance or power levels, depending on the configured NIDCPOWER_ATTR_OUTPUT_FUNCTION.\n**Valid values**: The valid values for this parameter are defined by the voltage level range, current level range, constant resistance level range or constant power level range.\n'
                },
                'name': 'values',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the source delay that follows the configuration of each value\nin the sequence.\n**Valid Values**:\nThe valid values are between 0 and 167 seconds.\n'
                },
                'name': 'sourceDelays',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe number of elements in the Values and the Source Delays arrays. The\nValues and Source Delays arrays should have the same size.\n'
                },
                'name': 'size',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'UnlockSession': {
        'documentation': {
            'description': '\nReleases a lock that you acquired on an device session using\nniDCPower_LockSession. Refer to niDCPower_LockSession for additional\ninformation on session locks.\n'
        },
        'included_in_proto': False,
        'method_templates': [
            {
                'documentation_filename': 'unlock',
                'library_interpreter_filename': 'unlock',
                'method_python_name_suffix': '',
                'session_filename': 'unlock'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\n| This attribute is optional. If you do not want to use this attribute,\n  pass VI_NULL.\n| Use this attribute in complex functions to keep track of whether you\n  obtain a lock and therefore need to unlock the session.\n| Pass the address of a local ViBoolean variable. In the declaration of\n  the local variable, initialize it to VI_FALSE. Pass the address of\n  the same local variable to any other calls you make to\n  niDCPower_LockSession or niDCPower_UnlockSessionin the same\n  function.\n| The parameter is an input/output parameter. niDCPower_LockSession and\n  niDCPower_UnlockSessioneach inspect the current value and take the\n  following actions.\n\n-  If the value is VI_TRUE, niDCPower_LockSession does not lock the\n   session again.\n-  If the value is VI_FALSE, niDCPower_LockSession obtains the lock\n   and sets the value of the parameter to VI_TRUE.\n-  If the value is VI_FALSE, niDCPower_UnlockSessiondoes not attempt\n   to unlock the session.\n-  If the value is VI_TRUE, niDCPower_UnlockSessionreleases the lock\n   and sets the value of the parameter to VI_FALSE.\n\n| Thus, you can, call niDCPower_UnlockSession at the end of your\n  function without worrying about whether you actually have the lock, as\n  the following example shows.\n| ViStatus TestFunc (ViSession vi, ViInt32 flags)\n  {\n  ViStatus error = VI_SUCCESS;\n  ViBoolean haveLock = VI_FALSE;\n  if (flags & BIT_1)\n  {\n  viCheckErr( niDCPower_LockSession(vi, &haveLock;));\n  viCheckErr( TakeAction1(vi));\n  if (flags & BIT_2)\n  {\n  viCheckErr( niDCPower_UnlockSession(vi, &haveLock;));\n  viCheckErr( TakeAction2(vi));\n  viCheckErr( niDCPower_LockSession(vi, &haveLock;);\n  }\n  if (flags & BIT_3)\n  viCheckErr( TakeAction3(vi));\n  }\n  Error:\n  /\\*At this point, you cannot really be sure that you have the lock.\n  Fortunately, the haveLock variable takes care of that for you.\\*/\n  niDCPower_UnlockSession(vi, &haveLock;);\n  return error;\n  }\n'
                },
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'python_name': 'unlock',
        'render_in_session_base': True,
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'WaitForEventWithChannels': {
        'documentation': {
            'description': '\nWaits until the specified channel(s) have generated the specified event.\n\nThe session monitors whether each type of event has occurred at least\nonce since the last time this function or the niDCPower_InitiateWithChannels\nfunction were called. If an event has only been generated once and you\ncall this function successively, the function times out. Individual\nevents must be generated between separate calls of this function.\n',
            'note': '\nThis function is not supported on all devices. For more information about supported devices, search ni.com for Supported Functions by Device.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies which event to wait for.\n**Defined Values:**\n',
                    'table_body': [
                        [
                            'NIDCPOWER_VAL_SOURCE_COMPLETE_EVENT',
                            'Waits for the Source Complete event.'
                        ],
                        [
                            'NIDCPOWER_VAL_MEASURE_COMPLETE_EVENT',
                            'Waits for the Measure Complete event.'
                        ],
                        [
                            'NIDCPOWER_VAL_SEQUENCE_ITERATION_COMPLETE_EVENT',
                            'Waits for the Sequence Iteration Complete event.'
                        ],
                        [
                            'NIDCPOWER_VAL_SEQUENCE_ENGINE_DONE_EVENT',
                            'Waits for the Sequence Engine Done event.'
                        ],
                        [
                            'NIDCPOWER_VAL_PULSE_COMPLETE_EVENT',
                            'Waits for the Pulse Complete event.'
                        ],
                        [
                            'NIDCPOWER_VAL_READY_FOR_PULSE_TRIGGER_EVENT',
                            'Waits for the Ready for Pulse Trigger event.'
                        ]
                    ]
                },
                'enum': 'Event',
                'name': 'eventId',
                'type': 'ViInt32'
            },
            {
                'default_value': 'hightime.timedelta(seconds=10.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the maximum time allowed for this function to complete, in\nseconds. If the function does not complete within this time interval,\nNI-DCPower returns an error.\n',
                    'note': '\nWhen setting the timeout interval, ensure you take into account any\ntriggers so that the timeout interval is long enough for your\napplication.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'python_name': 'wait_for_event',
        'returns': 'ViStatus'
    },
    'close': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nCloses the session specified in **vi** and deallocates the resources\nthat NI-DCPower reserves. If power output is enabled when you call this\nfunction, the channels remain in their existing state and\ncontinue providing power. Use the niDCPower_ConfigureOutputEnabled\nfunction to disable power output on a per channel basis. Use the\nniDCPower_ResetWithChannels function to disable power output on all channel(s).\n\n**Related Topics:**\n\n`Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__\n',
            'note': '\nNI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.\n'
        },
        'grpc_name': 'Close',
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': '_close',
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'error_message': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nConverts a status code returned by an instrument driver function into a\nuser-readable string.\n'
        },
        'grpc_name': 'ErrorMessage',
        'included_in_proto': True,
        'is_error_handling': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **status** parameter that is returned from any of the\nNI-DCPower functions.\n'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the user-readable message string that corresponds to the status\ncode you specify.\nYou must pass a ViChar array with at least 256 bytes.\n'
                },
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'fancy_self_test': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nPerforms the device self-test routine and returns the test result(s).\nCalling this function implicitly calls the niDCPower_ResetWithChannels function.\n\nWhen calling niDCPower_self_test with the PXIe-4162/4163, specify all\nchannels of your PXIe-4162/4163 with the channels input of\nniDCPower_InitializeWithChannels. You cannot self test a subset of\nPXIe-4162/4163 channels.\n\nRaises `SelfTestError` on self test failure. Attributes on exception object:\n\n- code - failure code from driver\n- message - status message from driver\n',
            'table_body': [
                [
                    '0',
                    'Self test passed.'
                ],
                [
                    '1',
                    'Self test failed.'
                ]
            ],
            'table_header': [
                'Self-Test Code',
                'Description'
            ]
        },
        'grpc_name': 'FancySelfTest',
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_self_test'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. **vi** is obtained from the niDCPower_InitializeWithChannels function.'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': 'self_test',
        'returns': 'ViStatus'
    },
    'self_test': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nPerforms the device self-test routine and returns the test result(s).\nCalling this function implicitly calls the niDCPower_ResetWithChannels function.\n\nWhen calling niDCPower_self_test with the PXIe-4162/4163, specify all\nchannels of your PXIe-4162/4163 with the channels input of\nniDCPower_InitializeWithChannels. You cannot self test a subset of\nPXIe-4162/4163 channels.\n'
        },
        'grpc_name': 'SelfTest',
        'included_in_proto': True,
        'method_name_for_documentation': 'self_test',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the value result from the device self-test.',
                    'table_body': [
                        [
                            '0',
                            'Self test passed.'
                        ],
                        [
                            '1',
                            'Self test failed.'
                        ]
                    ],
                    'table_header': [
                        'Self-Test Code',
                        'Description'
                    ]
                },
                'name': 'selfTestResult',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the self-test result message. The size of this array must be at\nleast 256 bytes.\n'
                },
                'name': 'selfTestMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    }
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidcpower/metadata/functions_addon.py sha256=dc2781dcad682e2dfa73e8632950d700e8a00d63218d2f0b4e77dad40fd9db00 bytes=3989 -->
## FILE: src/nidcpower/metadata/functions_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nidcpower/metadata/functions_addon.py`
- sha256: `dc2781dcad682e2dfa73e8632950d700e8a00d63218d2f0b4e77dad40fd9db00`
- bytes: 3989

````python
# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
    # TODO (ni-jfitzger): delete this override once ConfigureLCRCompensation is in nidcpower.proto. See https://github.com/ni/nimi-python/issues/1920
    'ConfigureLCRCompensation': {
        'included_in_proto': False,
    },
    # TODO (ni-jfitzger): delete this override once GetLCRCompensationData is in nidcpower.proto. See https://github.com/ni/nimi-python/issues/1920
    'GetLCRCompensationData': {
        'included_in_proto': False,
    },
}

functions_additional_create_advanced_sequence = {
    'FancyCreateAdvancedSequence': {
        'codegen_method': 'python-only',
        'returns': 'ViStatus',
        'python_name': 'create_advanced_sequence',
        'method_templates': [
            { 'session_filename': 'fancy_advanced_sequence', 'library_interpreter_filename': 'none', 'documentation_filename': 'default_method', 'method_python_name_suffix': '', },
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session. **vi** is obtained from the niDCPower_InitExtCal or niDCPower_InitializeWithChannels function.',
                },
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'SequenceName',
                'type': 'ViString',
                'documentation': {
                    'description': 'Specifies the name of the sequence to create.'
                },
            },
            {
                'direction': 'in',
                'name': 'PropertyNames',
                'type': 'ViString[]',
                'documentation': {
                    'description': 'Specifies the names of the properties you reconfigure per step in the advanced sequence. For more information about properties that can be configured in an advanced sequence for each NI-DCPower device that supports advanced sequencing, search ni.com for Supported Properties by Device.',
                },
            },
            {
                'direction': 'in',
                'name': 'setAsActiveSequence',
                'type': 'ViBoolean',
                'default_value': True,
                'documentation': { 'description': 'Specifies that this current sequence is active.', },
            },
        ],
        'documentation':
        {
            'description': '\nCreates an empty advanced sequence. Call the\nniDCPower_CreateAdvancedSequenceStepWithChannels function to add steps to the\nactive advanced sequence.\n\nYou can create multiple advanced sequences in a session.\n\n**Support for this function**\n\nYou must set the source mode to Sequence to use this function.\n\nUsing the niDCPower_SetSequence function with Advanced Sequence\nfunctions is unsupported.\n\nUse this function in the Uncommitted or Committed programming states.\nRefer to the `Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in\nthe *NI DC Power Supplies and SMUs Help* for more information about\nNI-DCPower programming states.\n\n**Related Topics**:\n\n`Advanced Sequence\nMode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__\n\n`Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__\n\nniDCPower_CreateAdvancedSequenceStepWithChannels\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
    },
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidcpower/metadata/nidcpower.proto sha256=48d11e5a9bd5f5241379972671921da0573bfded96a5f0fc74dd42064cb17ac0 bytes=78341 -->
## FILE: src/nidcpower/metadata/nidcpower.proto

- repository: `ni/nimi-python`
- source_path: `src/nidcpower/metadata/nidcpower.proto`
- sha256: `48d11e5a9bd5f5241379972671921da0573bfded96a5f0fc74dd42064cb17ac0`
- bytes: 78341

````protobuf

//---------------------------------------------------------------------
// This file is generated from NI-DCPower API metadata version 25.3.0f265
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
  rpc InitializeWithChannels(InitializeWithChannelsRequest) returns (InitializeWithChannelsResponse);
  rpc Close(CloseRequest) returns (CloseResponse);
  rpc ConfigureSourceMode(ConfigureSourceModeRequest) returns (ConfigureSourceModeResponse);
  rpc ConfigureOutputFunction(ConfigureOutputFunctionRequest) returns (ConfigureOutputFunctionResponse);
  rpc ConfigureOutputEnabled(ConfigureOutputEnabledRequest) returns (ConfigureOutputEnabledResponse);
  rpc SetSequence(SetSequenceRequest) returns (SetSequenceResponse);
  rpc ConfigureVoltageLevel(ConfigureVoltageLevelRequest) returns (ConfigureVoltageLevelResponse);
  rpc ConfigureCurrentLimit(ConfigureCurrentLimitRequest) returns (ConfigureCurrentLimitResponse);
  rpc ConfigureVoltageLevelRange(ConfigureVoltageLevelRangeRequest) returns (ConfigureVoltageLevelRangeResponse);
  rpc ConfigureCurrentLimitRange(ConfigureCurrentLimitRangeRequest) returns (ConfigureCurrentLimitRangeResponse);
  rpc ConfigureOutputResistance(ConfigureOutputResistanceRequest) returns (ConfigureOutputResistanceResponse);
  rpc ConfigureCurrentLevel(ConfigureCurrentLevelRequest) returns (ConfigureCurrentLevelResponse);
  rpc ConfigureCurrentLevelRange(ConfigureCurrentLevelRangeRequest) returns (ConfigureCurrentLevelRangeResponse);
  rpc ConfigureVoltageLimit(ConfigureVoltageLimitRequest) returns (ConfigureVoltageLimitResponse);
  rpc ConfigureVoltageLimitRange(ConfigureVoltageLimitRangeRequest) returns (ConfigureVoltageLimitRangeResponse);
  rpc ConfigurePulseVoltageLevel(ConfigurePulseVoltageLevelRequest) returns (ConfigurePulseVoltageLevelResponse);
  rpc ConfigurePulseCurrentLimit(ConfigurePulseCurrentLimitRequest) returns (ConfigurePulseCurrentLimitResponse);
  rpc ConfigurePulseBiasVoltageLevel(ConfigurePulseBiasVoltageLevelRequest) returns (ConfigurePulseBiasVoltageLevelResponse);
  rpc ConfigurePulseBiasCurrentLimit(ConfigurePulseBiasCurrentLimitRequest) returns (ConfigurePulseBiasCurrentLimitResponse);
  rpc ConfigurePulseVoltageLevelRange(ConfigurePulseVoltageLevelRangeRequest) returns (ConfigurePulseVoltageLevelRangeResponse);
  rpc ConfigurePulseCurrentLimitRange(ConfigurePulseCurrentLimitRangeRequest) returns (ConfigurePulseCurrentLimitRangeResponse);
  rpc ConfigurePulseCurrentLevel(ConfigurePulseCurrentLevelRequest) returns (ConfigurePulseCurrentLevelResponse);
  rpc ConfigurePulseVoltageLimit(ConfigurePulseVoltageLimitRequest) returns (ConfigurePulseVoltageLimitResponse);
  rpc ConfigurePulseBiasCurrentLevel(ConfigurePulseBiasCurrentLevelRequest) returns (ConfigurePulseBiasCurrentLevelResponse);
  rpc ConfigurePulseBiasVoltageLimit(ConfigurePulseBiasVoltageLimitRequest) returns (ConfigurePulseBiasVoltageLimitResponse);
  rpc ConfigurePulseCurrentLevelRange(ConfigurePulseCurrentLevelRangeRequest) returns (ConfigurePulseCurrentLevelRangeResponse);
  rpc ConfigurePulseVoltageLimitRange(ConfigurePulseVoltageLimitRangeRequest) returns (ConfigurePulseVoltageLimitRangeResponse);
  rpc CreateAdvancedSequence(CreateAdvancedSequenceRequest) returns (CreateAdvancedSequenceResponse);
  rpc CreateAdvancedSequenceStep(CreateAdvancedSequenceStepRequest) returns (CreateAdvancedSequenceStepResponse);
  rpc DeleteAdvancedSequence(DeleteAdvancedSequenceRequest) returns (DeleteAdvancedSequenceResponse);
  rpc ConfigureApertureTime(ConfigureApertureTimeRequest) returns (ConfigureApertureTimeResponse);
  rpc ConfigureAutoZero(ConfigureAutoZeroRequest) returns (ConfigureAutoZeroResponse);
  rpc ConfigurePowerLineFrequency(ConfigurePowerLineFrequencyRequest) returns (ConfigurePowerLineFrequencyResponse);
  rpc ConfigureSense(ConfigureSenseRequest) returns (ConfigureSenseResponse);
  rpc Measure(MeasureRequest) returns (MeasureResponse);
  rpc MeasureMultiple(MeasureMultipleRequest) returns (MeasureMultipleResponse);
  rpc FetchMultiple(FetchMultipleRequest) returns (FetchMultipleResponse);
  rpc MeasureMultipleLCR(MeasureMultipleLCRRequest) returns (MeasureMultipleLCRResponse);
  rpc FetchMultipleLCR(FetchMultipleLCRRequest) returns (FetchMultipleLCRResponse);
  rpc QueryInCompliance(QueryInComplianceRequest) returns (QueryInComplianceResponse);
  rpc QueryOutputState(QueryOutputStateRequest) returns (QueryOutputStateResponse);
  rpc QueryLatchedOutputCutoffState(QueryLatchedOutputCutoffStateRequest) returns (QueryLatchedOutputCutoffStateResponse);
  rpc ClearLatchedOutputCutoffState(ClearLatchedOutputCutoffStateRequest) returns (ClearLatchedOutputCutoffStateResponse);
  rpc Commit(CommitRequest) returns (CommitResponse);
  rpc Initiate(InitiateRequest) returns (InitiateResponse);
  rpc Abort(AbortRequest) returns (AbortResponse);
  rpc QueryMaxCurrentLimit(QueryMaxCurrentLimitRequest) returns (QueryMaxCurrentLimitResponse);
  rpc QueryMaxVoltageLevel(QueryMaxVoltageLevelRequest) returns (QueryMaxVoltageLevelResponse);
  rpc QueryMinCurrentLimit(QueryMinCurrentLimitRequest) returns (QueryMinCurrentLimitResponse);
  rpc CalSelfCalibrate(CalSelfCalibrateRequest) returns (CalSelfCalibrateResponse);
  rpc GetExtCalRecommendedInterval(GetExtCalRecommendedIntervalRequest) returns (GetExtCalRecommendedIntervalResponse);
  rpc GetExtCalLastDateAndTime(GetExtCalLastDateAndTimeRequest) returns (GetExtCalLastDateAndTimeResponse);
  rpc ReadCurrentTemperature(ReadCurrentTemperatureRequest) returns (ReadCurrentTemperatureResponse);
  rpc GetExtCalLastTemp(GetExtCalLastTempRequest) returns (GetExtCalLastTempResponse);
  rpc GetSelfCalLastDateAndTime(GetSelfCalLastDateAndTimeRequest) returns (GetSelfCalLastDateAndTimeResponse);
  rpc GetSelfCalLastTemp(GetSelfCalLastTempRequest) returns (GetSelfCalLastTempResponse);
  rpc GetLCRCompensationLastDateAndTime(GetLCRCompensationLastDateAndTimeRequest) returns (GetLCRCompensationLastDateAndTimeResponse);
  rpc ConfigureDigitalEdgeStartTrigger(ConfigureDigitalEdgeStartTriggerRequest) returns (ConfigureDigitalEdgeStartTriggerResponse);
  rpc ConfigureSoftwareEdgeStartTrigger(ConfigureSoftwareEdgeStartTriggerRequest) returns (ConfigureSoftwareEdgeStartTriggerResponse);
  rpc DisableStartTrigger(DisableStartTriggerRequest) returns (DisableStartTriggerResponse);
  rpc ConfigureDigitalEdgeSequenceAdvanceTrigger(ConfigureDigitalEdgeSequenceAdvanceTriggerRequest) returns (ConfigureDigitalEdgeSequenceAdvanceTriggerResponse);
  rpc ConfigureSoftwareEdgeSequenceAdvanceTrigger(ConfigureSoftwareEdgeSequenceAdvanceTriggerRequest) returns (ConfigureSoftwareEdgeSequenceAdvanceTriggerResponse);
  rpc DisableSequenceAdvanceTrigger(DisableSequenceAdvanceTriggerRequest) returns (DisableSequenceAdvanceTriggerResponse);
  rpc ConfigureDigitalEdgeSourceTrigger(ConfigureDigitalEdgeSourceTriggerRequest) returns (ConfigureDigitalEdgeSourceTriggerResponse);
  rpc ConfigureSoftwareEdgeSourceTrigger(ConfigureSoftwareEdgeSourceTriggerRequest) returns (ConfigureSoftwareEdgeSourceTriggerResponse);
  rpc DisableSourceTrigger(DisableSourceTriggerRequest) returns (DisableSourceTriggerResponse);
  rpc ConfigureDigitalEdgeMeasureTrigger(ConfigureDigitalEdgeMeasureTriggerRequest) returns (ConfigureDigitalEdgeMeasureTriggerResponse);
  rpc ConfigureSoftwareEdgeMeasureTrigger(ConfigureSoftwareEdgeMeasureTriggerRequest) returns (ConfigureSoftwareEdgeMeasureTriggerResponse);
  rpc ConfigureDigitalEdgePulseTrigger(ConfigureDigitalEdgePulseTriggerRequest) returns (ConfigureDigitalEdgePulseTriggerResponse);
  rpc ConfigureSoftwareEdgePulseTrigger(ConfigureSoftwareEdgePulseTriggerRequest) returns (ConfigureSoftwareEdgePulseTriggerResponse);
  rpc DisablePulseTrigger(DisablePulseTriggerRequest) returns (DisablePulseTriggerResponse);
  rpc ExportSignal(ExportSignalRequest) returns (ExportSignalResponse);
  rpc SendSoftwareEdgeTrigger(SendSoftwareEdgeTriggerRequest) returns (SendSoftwareEdgeTriggerResponse);
  rpc WaitForEvent(WaitForEventRequest) returns (WaitForEventResponse);
  rpc Disable(DisableRequest) returns (DisableResponse);
  rpc Reset(ResetRequest) returns (ResetResponse);
  rpc ResetDevice(ResetDeviceRequest) returns (ResetDeviceResponse);
  rpc SelfTest(SelfTestRequest) returns (SelfTestResponse);
  rpc RevisionQuery(RevisionQueryRequest) returns (RevisionQueryResponse);
  rpc ResetWithDefaults(ResetWithDefaultsRequest) returns (ResetWithDefaultsResponse);
  rpc GetChannelName(GetChannelNameRequest) returns (GetChannelNameResponse);
  rpc GetChannelNameFromString(GetChannelNameFromStringRequest) returns (GetChannelNameFromStringResponse);
  rpc GetNextCoercionRecord(GetNextCoercionRecordRequest) returns (GetNextCoercionRecordResponse);
  rpc ClearInterchangeWarnings(ClearInterchangeWarningsRequest) returns (ClearInterchangeWarningsResponse);
  rpc ResetInterchangeCheck(ResetInterchangeCheckRequest) returns (ResetInterchangeCheckResponse);
  rpc GetNextInterchangeWarning(GetNextInterchangeWarningRequest) returns (GetNextInterchangeWarningResponse);
  rpc GetError(GetErrorRequest) returns (GetErrorResponse);
  rpc ClearError(ClearErrorRequest) returns (ClearErrorResponse);
  rpc ErrorMessage(ErrorMessageRequest) returns (ErrorMessageResponse);
  rpc SetAttributeViInt32(SetAttributeViInt32Request) returns (SetAttributeViInt32Response);
  rpc SetAttributeViInt64(SetAttributeViInt64Request) returns (SetAttributeViInt64Response);
  rpc SetAttributeViReal64(SetAttributeViReal64Request) returns (SetAttributeViReal64Response);
  rpc SetAttributeViString(SetAttributeViStringRequest) returns (SetAttributeViStringResponse);
  rpc SetAttributeViSession(SetAttributeViSessionRequest) returns (SetAttributeViSessionResponse);
  rpc SetAttributeViBoolean(SetAttributeViBooleanRequest) returns (SetAttributeViBooleanResponse);
  rpc GetAttributeViInt32(GetAttributeViInt32Request) returns (GetAttributeViInt32Response);
  rpc GetAttributeViInt64(GetAttributeViInt64Request) returns (GetAttributeViInt64Response);
  rpc GetAttributeViReal64(GetAttributeViReal64Request) returns (GetAttributeViReal64Response);
  rpc GetAttributeViString(GetAttributeViStringRequest) returns (GetAttributeViStringResponse);
  rpc GetAttributeViSession(GetAttributeViSessionRequest) returns (GetAttributeViSessionResponse);
  rpc GetAttributeViBoolean(GetAttributeViBooleanRequest) returns (GetAttributeViBooleanResponse);
  rpc ImportAttributeConfigurationFile(ImportAttributeConfigurationFileRequest) returns (ImportAttributeConfigurationFileResponse);
  rpc ExportAttributeConfigurationFile(ExportAttributeConfigurationFileRequest) returns (ExportAttributeConfigurationFileResponse);
  rpc ImportAttributeConfigurationBuffer(ImportAttributeConfigurationBufferRequest) returns (ImportAttributeConfigurationBufferResponse);
  rpc ExportAttributeConfigurationBuffer(ExportAttributeConfigurationBufferRequest) returns (ExportAttributeConfigurationBufferResponse);
  rpc PerformLCROpenCompensation(PerformLCROpenCompensationRequest) returns (PerformLCROpenCompensationResponse);
  rpc PerformLCRShortCompensation(PerformLCRShortCompensationRequest) returns (PerformLCRShortCompensationResponse);
  rpc PerformLCRLoadCompensation(PerformLCRLoadCompensationRequest) returns (PerformLCRLoadCompensationResponse);
  rpc ConfigureLCRCompensation(ConfigureLCRCompensationRequest) returns (ConfigureLCRCompensationResponse);
  rpc PerformLCROpenCustomCableCompensation(PerformLCROpenCustomCableCompensationRequest) returns (PerformLCROpenCustomCableCompensationResponse);
  rpc PerformLCRShortCustomCableCompensation(PerformLCRShortCustomCableCompensationRequest) returns (PerformLCRShortCustomCableCompensationResponse);
  rpc GetLCRCompensationData(GetLCRCompensationDataRequest) returns (GetLCRCompensationDataResponse);
  rpc InitializeWithIndependentChannels(InitializeWithIndependentChannelsRequest) returns (InitializeWithIndependentChannelsResponse);
  rpc ConfigureSourceModeWithChannels(ConfigureSourceModeWithChannelsRequest) returns (ConfigureSourceModeWithChannelsResponse);
  rpc CreateAdvancedSequenceWithChannels(CreateAdvancedSequenceWithChannelsRequest) returns (CreateAdvancedSequenceWithChannelsResponse);
  rpc CreateAdvancedSequenceStepWithChannels(CreateAdvancedSequenceStepWithChannelsRequest) returns (CreateAdvancedSequenceStepWithChannelsResponse);
  rpc CreateAdvancedSequenceCommitStepWithChannels(CreateAdvancedSequenceCommitStepWithChannelsRequest) returns (CreateAdvancedSequenceCommitStepWithChannelsResponse);
  rpc DeleteAdvancedSequenceWithChannels(DeleteAdvancedSequenceWithChannelsRequest) returns (DeleteAdvancedSequenceWithChannelsResponse);
  rpc CommitWithChannels(CommitWithChannelsRequest) returns (CommitWithChannelsResponse);
  rpc InitiateWithChannels(InitiateWithChannelsRequest) returns (InitiateWithChannelsResponse);
  rpc AbortWithChannels(AbortWithChannelsRequest) returns (AbortWithChannelsResponse);
  rpc ConfigureDigitalEdgeStartTriggerWithChannels(ConfigureDigitalEdgeStartTriggerWithChannelsRequest) returns (ConfigureDigitalEdgeStartTriggerWithChannelsResponse);
  rpc ConfigureSoftwareEdgeStartTriggerWithChannels(ConfigureSoftwareEdgeStartTriggerWithChannelsRequest) returns (ConfigureSoftwareEdgeStartTriggerWithChannelsResponse);
  rpc DisableStartTriggerWithChannels(DisableStartTriggerWithChannelsRequest) returns (DisableStartTriggerWithChannelsResponse);
  rpc ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannels(ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannelsRequest) returns (ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannelsResponse);
  rpc ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannels(ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannelsRequest) returns (ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannelsResponse);
  rpc DisableSequenceAdvanceTriggerWithChannels(DisableSequenceAdvanceTriggerWithChannelsRequest) returns (DisableSequenceAdvanceTriggerWithChannelsResponse);
  rpc ConfigureDigitalEdgeSourceTriggerWithChannels(ConfigureDigitalEdgeSourceTriggerWithChannelsRequest) returns (ConfigureDigitalEdgeSourceTriggerWithChannelsResponse);
  rpc ConfigureSoftwareEdgeSourceTriggerWithChannels(ConfigureSoftwareEdgeSourceTriggerWithChannelsRequest) returns (ConfigureSoftwareEdgeSourceTriggerWithChannelsResponse);
  rpc DisableSourceTriggerWithChannels(DisableSourceTriggerWithChannelsRequest) returns (DisableSourceTriggerWithChannelsResponse);
  rpc ConfigureDigitalEdgeMeasureTriggerWithChannels(ConfigureDigitalEdgeMeasureTriggerWithChannelsRequest) returns (ConfigureDigitalEdgeMeasureTriggerWithChannelsResponse);
  rpc ConfigureSoftwareEdgeMeasureTriggerWithChannels(ConfigureSoftwareEdgeMeasureTriggerWithChannelsRequest) returns (ConfigureSoftwareEdgeMeasureTriggerWithChannelsResponse);
  rpc ConfigureDigitalEdgePulseTriggerWithChannels(ConfigureDigitalEdgePulseTriggerWithChannelsRequest) returns (ConfigureDigitalEdgePulseTriggerWithChannelsResponse);
  rpc ConfigureSoftwareEdgePulseTriggerWithChannels(ConfigureSoftwareEdgePulseTriggerWithChannelsRequest) returns (ConfigureSoftwareEdgePulseTriggerWithChannelsResponse);
  rpc DisablePulseTriggerWithChannels(DisablePulseTriggerWithChannelsRequest) returns (DisablePulseTriggerWithChannelsResponse);
  rpc ConfigureDigitalEdgeShutdownTriggerWithChannels(ConfigureDigitalEdgeShutdownTriggerWithChannelsRequest) returns (ConfigureDigitalEdgeShutdownTriggerWithChannelsResponse);
  rpc ConfigureSoftwareEdgeShutdownTriggerWithChannels(ConfigureSoftwareEdgeShutdownTriggerWithChannelsRequest) returns (ConfigureSoftwareEdgeShutdownTriggerWithChannelsResponse);
  rpc DisableShutdownTriggerWithChannels(DisableShutdownTriggerWithChannelsRequest) returns (DisableShutdownTriggerWithChannelsResponse);
  rpc ExportSignalWithChannels(ExportSignalWithChannelsRequest) returns (ExportSignalWithChannelsResponse);
  rpc SendSoftwareEdgeTriggerWithChannels(SendSoftwareEdgeTriggerWithChannelsRequest) returns (SendSoftwareEdgeTriggerWithChannelsResponse);
  rpc WaitForEventWithChannels(WaitForEventWithChannelsRequest) returns (WaitForEventWithChannelsResponse);
  rpc ResetWithChannels(ResetWithChannelsRequest) returns (ResetWithChannelsResponse);
  rpc InvalidateAllAttributes(InvalidateAllAttributesRequest) returns (InvalidateAllAttributesResponse);
  rpc ConfigureOvp(ConfigureOvpRequest) returns (ConfigureOvpResponse);
  rpc ErrorQuery(ErrorQueryRequest) returns (ErrorQueryResponse);
  rpc GetLCRCustomCableCompensationData(GetLCRCustomCableCompensationDataRequest) returns (GetLCRCustomCableCompensationDataResponse);
  rpc ConfigureLCRCustomCableCompensation(ConfigureLCRCustomCableCompensationRequest) returns (ConfigureLCRCustomCableCompensationResponse);
}

enum NiDCPowerAttribute {
  NIDCPOWER_ATTRIBUTE_UNSPECIFIED = 0;
  NIDCPOWER_ATTRIBUTE_RANGE_CHECK = 1050002;
  NIDCPOWER_ATTRIBUTE_QUERY_INSTRUMENT_STATUS = 1050003;
  NIDCPOWER_ATTRIBUTE_CACHE = 1050004;
  NIDCPOWER_ATTRIBUTE_SIMULATE = 1050005;
  NIDCPOWER_ATTRIBUTE_RECORD_COERCIONS = 1050006;
  NIDCPOWER_ATTRIBUTE_INTERCHANGE_CHECK = 1050021;
  NIDCPOWER_ATTRIBUTE_CHANNEL_COUNT = 1050203;
  NIDCPOWER_ATTRIBUTE_SPECIFIC_DRIVER_PREFIX = 1050302;
  NIDCPOWER_ATTRIBUTE_SUPPORTED_INSTRUMENT_MODELS = 1050327;
  NIDCPOWER_ATTRIBUTE_GROUP_CAPABILITIES = 1050401;
  NIDCPOWER_ATTRIBUTE_INSTRUMENT_MANUFACTURER = 1050511;
  NIDCPOWER_ATTRIBUTE_INSTRUMENT_MODEL = 1050512;
  NIDCPOWER_ATTRIBUTE_INSTRUMENT_FIRMWARE_REVISION = 1050510;
  NIDCPOWER_ATTRIBUTE_SPECIFIC_DRIVER_REVISION = 1050551;
  NIDCPOWER_ATTRIBUTE_SPECIFIC_DRIVER_VENDOR = 1050513;
  NIDCPOWER_ATTRIBUTE_SPECIFIC_DRIVER_DESCRIPTION = 1050514;
  NIDCPOWER_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION = 1050515;
  NIDCPOWER_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION = 1050516;
  NIDCPOWER_ATTRIBUTE_SERIAL_NUMBER = 1150152;
  NIDCPOWER_ATTRIBUTE_LOGICAL_NAME = 1050305;
  NIDCPOWER_ATTRIBUTE_IO_RESOURCE_DESCRIPTOR = 1050304;
  NIDCPOWER_ATTRIBUTE_DRIVER_SETUP = 1050007;
  NIDCPOWER_ATTRIBUTE_SOURCE_MODE = 1150054;
  NIDCPOWER_ATTRIBUTE_OUTPUT_FUNCTION = 1150008;
  NIDCPOWER_ATTRIBUTE_OUTPUT_ENABLED = 1250006;
  NIDCPOWER_ATTRIBUTE_OUTPUT_CONNECTED = 1150060;
  NIDCPOWER_ATTRIBUTE_OUTPUT_RESISTANCE = 1150061;
  NIDCPOWER_ATTRIBUTE_TRANSIENT_RESPONSE = 1150062;
  NIDCPOWER_ATTRIBUTE_VOLTAGE_GAIN_BANDWIDTH = 1150067;
  NIDCPOWER_ATTRIBUTE_VOLTAGE_COMPENSATION_FREQUENCY = 1150068;
  NIDCPOWER_ATTRIBUTE_VOLTAGE_POLE_ZERO_RATIO = 1150069;
  NIDCPOWER_ATTRIBUTE_CURRENT_GAIN_BANDWIDTH = 1150070;
  NIDCPOWER_ATTRIBUTE_CURRENT_COMPENSATION_FREQUENCY = 1150071;
  NIDCPOWER_ATTRIBUTE_CURRENT_POLE_ZERO_RATIO = 1150072;
  NIDCPOWER_ATTRIBUTE_CONSTANT_RESISTANCE_GAIN_BANDWIDTH = 1150368;
  NIDCPOWER_ATTRIBUTE_CONSTANT_RESISTANCE_COMPENSATION_FREQUENCY = 1150366;
  NIDCPOWER_ATTRIBUTE_CONSTANT_RESISTANCE_POLE_ZERO_RATIO = 1150371;
  NIDCPOWER_ATTRIBUTE_CONSTANT_POWER_GAIN_BANDWIDTH = 1150362;
  NIDCPOWER_ATTRIBUTE_CONSTANT_POWER_COMPENSATION_FREQUENCY = 1150360;
  NIDCPOWER_ATTRIBUTE_CONSTANT_POWER_POLE_ZERO_RATIO = 1150365;
  NIDCPOWER_ATTRIBUTE_VOLTAGE_LEVEL = 1250001;
  NIDCPOWER_ATTRIBUTE_CURRENT_LIMIT = 1250005;
  NIDCPOWER_ATTRIBUTE_VOLTAGE_LEVEL_RANGE = 1150005;
  NIDCPOWER_ATTRIBUTE_CURRENT_LIMIT_RANGE = 1150004;
  NIDCPOWER_ATTRIBUTE_CURRENT_LIMIT_BEHAVIOR = 1250004;
  NIDCPOWER_ATTRIBUTE_VOLTAGE_LEVEL_AUTORANGE = 1150015;
  NIDCPOWER_ATTRIBUTE_CURRENT_LIMIT_AUTORANGE = 1150016;
  NIDCPOWER_ATTRIBUTE_CURRENT_LIMIT_HIGH = 1150187;
  NIDCPOWER_ATTRIBUTE_CURRENT_LIMIT_LOW = 1150188;
  NIDCPOWER_ATTRIBUTE_CURRENT_LEVEL = 1150009;
  NIDCPOWER_ATTRIBUTE_VOLTAGE_LIMIT = 1150010;
  NIDCPOWER_ATTRIBUTE_CURRENT_LEVEL_RANGE = 1150011;
  NIDCPOWER_ATTRIBUTE_VOLTAGE_LIMIT_RANGE = 1150012;
  NIDCPOWER_ATTRIBUTE_CURRENT_LEVEL_AUTORANGE = 1150017;
  NIDCPOWER_ATTRIBUTE_VOLTAGE_LIMIT_AUTORANGE = 1150018;
  NIDCPOWER_ATTRIBUTE_VOLTAGE_LIMIT_HIGH = 1150185;
  NIDCPOWER_ATTRIBUTE_VOLTAGE_LIMIT_LOW = 1150186;
  NIDCPOWER_ATTRIBUTE_CURRENT_LEVEL_RISING_SLEW_RATE = 1150343;
  NIDCPOWER_ATTRIBUTE_CURRENT_LEVEL_FALLING_SLEW_RATE = 1150344;
  NIDCPOWER_ATTRIBUTE_PULSE_VOLTAGE_LEVEL = 1150080;
  NIDCPOWER_ATTRIBUTE_PULSE_CURRENT_LIMIT = 1150081;
  NIDCPOWER_ATTRIBUTE_PULSE_BIAS_VOLTAGE_LEVEL = 1150082;
  NIDCPOWER_ATTRIBUTE_PULSE_BIAS_CURRENT_LIMIT = 1150083;
  NIDCPOWER_ATTRIBUTE_PULSE_VOLTAGE_LEVEL_RANGE = 1150084;
  NIDCPOWER_ATTRIBUTE_PULSE_CURRENT_LIMIT_RANGE = 1150085;
  NIDCPOWER_ATTRIBUTE_PULSE_CURRENT_LIMIT_HIGH = 1150193;
  NIDCPOWER_ATTRIBUTE_PULSE_CURRENT_LIMIT_LOW = 1150194;
  NIDCPOWER_ATTRIBUTE_PULSE_BIAS_CURRENT_LIMIT_HIGH = 1150195;
  NIDCPOWER_ATTRIBUTE_PULSE_BIAS_CURRENT_LIMIT_LOW = 1150196;
  NIDCPOWER_ATTRIBUTE_PULSE_CURRENT_LEVEL = 1150086;
  NIDCPOWER_ATTRIBUTE_PULSE_VOLTAGE_LIMIT = 1150087;
  NIDCPOWER_ATTRIBUTE_PULSE_BIAS_CURRENT_LEVEL = 1150088;
  NIDCPOWER_ATTRIBUTE_PULSE_BIAS_VOLTAGE_LIMIT = 1150089;
  NIDCPOWER_ATTRIBUTE_PULSE_CURRENT_LEVEL_RANGE = 1150090;
  NIDCPOWER_ATTRIBUTE_PULSE_VOLTAGE_LIMIT_RANGE = 1150091;
  NIDCPOWER_ATTRIBUTE_PULSE_VOLTAGE_LIMIT_HIGH = 1150189;
  NIDCPOWER_ATTRIBUTE_PULSE_VOLTAGE_LIMIT_LOW = 1150190;
  NIDCPOWER_ATTRIBUTE_PULSE_BIAS_VOLTAGE_LIMIT_HIGH = 1150191;
  NIDCPOWER_ATTRIBUTE_PULSE_BIAS_VOLTAGE_LIMIT_LOW = 1150192;
  NIDCPOWER_ATTRIBUTE_CONSTANT_RESISTANCE_LEVEL = 1150369;
  NIDCPOWER_ATTRIBUTE_CONSTANT_RESISTANCE_LEVEL_RANGE = 1150370;
  NIDCPOWER_ATTRIBUTE_CONSTANT_RESISTANCE_CURRENT_LIMIT = 1150367;
  NIDCPOWER_ATTRIBUTE_CONSTANT_POWER_LEVEL = 1150363;
  NIDCPOWER_ATTRIBUTE_CONSTANT_POWER_LEVEL_RANGE = 1150364;
  NIDCPOWER_ATTRIBUTE_CONSTANT_POWER_CURRENT_LIMIT = 1150361;
  NIDCPOWER_ATTRIBUTE_SOURCE_DELAY = 1150051;
  NIDCPOWER_ATTRIBUTE_OVERRANGING_ENABLED = 1150007;
  NIDCPOWER_ATTRIBUTE_OUTPUT_CAPACITANCE = 1150014;
  NIDCPOWER_ATTRIBUTE_SEQUENCE_LOOP_COUNT = 1150025;
  NIDCPOWER_ATTRIBUTE_SEQUENCE_LOOP_COUNT_IS_FINITE = 1150078;
  NIDCPOWER_ATTRIBUTE_COMPLIANCE_LIMIT_SYMMETRY = 1150184;
  NIDCPOWER_ATTRIBUTE_SEQUENCE_STEP_DELTA_TIME = 1150198;
  NIDCPOWER_ATTRIBUTE_SEQUENCE_STEP_DELTA_TIME_ENABLED = 1150199;
  NIDCPOWER_ATTRIBUTE_ACTUAL_POWER_ALLOCATION = 1150205;
  NIDCPOWER_ATTRIBUTE_REQUESTED_POWER_ALLOCATION = 1150206;
  NIDCPOWER_ATTRIBUTE_POWER_ALLOCATION_MODE = 1150207;
  NIDCPOWER_ATTRIBUTE_MERGED_CHANNELS = 1150249;
  NIDCPOWER_ATTRIBUTE_CONDUCTION_VOLTAGE_MODE = 1150350;
  NIDCPOWER_ATTRIBUTE_CONDUCTION_VOLTAGE_ON_THRESHOLD = 1150351;
  NIDCPOWER_ATTRIBUTE_CONDUCTION_VOLTAGE_OFF_THRESHOLD = 1150352;
  NIDCPOWER_ATTRIBUTE_OUTPUT_SHORTED = 1150372;
  NIDCPOWER_ATTRIBUTE_PULSE_BIAS_DELAY = 1150092;
  NIDCPOWER_ATTRIBUTE_PULSE_ON_TIME = 1150093;
  NIDCPOWER_ATTRIBUTE_PULSE_OFF_TIME = 1150094;
  NIDCPOWER_ATTRIBUTE_OVP_ENABLED = 1250002;
  NIDCPOWER_ATTRIBUTE_OVP_LIMIT = 1250003;
  NIDCPOWER_ATTRIBUTE_SENSE = 1150013;
  NIDCPOWER_ATTRIBUTE_AUTO_ZERO = 1150055;
  NIDCPOWER_ATTRIBUTE_APERTURE_TIME = 1150058;
  NIDCPOWER_ATTRIBUTE_APERTURE_TIME_UNITS = 1150059;
  NIDCPOWER_ATTRIBUTE_POWER_LINE_FREQUENCY = 1150020;
  NIDCPOWER_ATTRIBUTE_SAMPLES_TO_AVERAGE = 1150003;
  NIDCPOWER_ATTRIBUTE_FETCH_BACKLOG = 1150056;
  NIDCPOWER_ATTRIBUTE_APERTURE_TIME_AUTO_MODE = 1150314;
  NIDCPOWER_ATTRIBUTE_AUTORANGE = 1150244;
  NIDCPOWER_ATTRIBUTE_MEASURE_WHEN = 1150057;
  NIDCPOWER_ATTRIBUTE_RESET_AVERAGE_BEFORE_MEASUREMENT = 1150006;
  NIDCPOWER_ATTRIBUTE_MEASURE_RECORD_LENGTH = 1150063;
  NIDCPOWER_ATTRIBUTE_MEASURE_RECORD_LENGTH_IS_FINITE = 1150064;
  NIDCPOWER_ATTRIBUTE_MEASURE_RECORD_DELTA_TIME = 1150065;
  NIDCPOWER_ATTRIBUTE_DC_NOISE_REJECTION = 1150066;
  NIDCPOWER_ATTRIBUTE_SELF_CALIBRATION_PERSISTENCE = 1150073;
  NIDCPOWER_ATTRIBUTE_MEASURE_BUFFER_SIZE = 1150077;
  NIDCPOWER_ATTRIBUTE_AUTORANGE_BEHAVIOR = 1150245;
  NIDCPOWER_ATTRIBUTE_AUTORANGE_APERTURE_TIME_MODE = 1150246;
  NIDCPOWER_ATTRIBUTE_AUTORANGE_MINIMUM_APERTURE_TIME = 1150247;
  NIDCPOWER_ATTRIBUTE_AUTORANGE_MINIMUM_APERTURE_TIME_UNITS = 1150248;
  NIDCPOWER_ATTRIBUTE_AUTORANGE_MINIMUM_CURRENT_RANGE = 1150255;
  NIDCPOWER_ATTRIBUTE_AUTORANGE_MINIMUM_VOLTAGE_RANGE = 1150256;
  NIDCPOWER_ATTRIBUTE_AUTORANGE_THRESHOLD_MODE = 1150257;
  NIDCPOWER_ATTRIBUTE_AUTORANGE_MAXIMUM_DELAY_AFTER_RANGE_CHANGE = 1150322;
  NIDCPOWER_ATTRIBUTE_START_TRIGGER_TYPE = 1150021;
  NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_START_TRIGGER_EDGE = 1150022;
  NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL = 1150023;
  NIDCPOWER_ATTRIBUTE_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL = 1150024;
  NIDCPOWER_ATTRIBUTE_SOURCE_TRIGGER_TYPE = 1150030;
  NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_SOURCE_TRIGGER_EDGE = 1150031;
  NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_SOURCE_TRIGGER_INPUT_TERMINAL = 1150032;
  NIDCPOWER_ATTRIBUTE_EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINAL = 1150033;
  NIDCPOWER_ATTRIBUTE_MEASURE_TRIGGER_TYPE = 1150034;
  NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_MEASURE_TRIGGER_EDGE = 1150035;
  NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_MEASURE_TRIGGER_INPUT_TERMINAL = 1150036;
  NIDCPOWER_ATTRIBUTE_EXPORTED_MEASURE_TRIGGER_OUTPUT_TERMINAL = 1150037;
  NIDCPOWER_ATTRIBUTE_SEQUENCE_ADVANCE_TRIGGER_TYPE = 1150026;
  NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE = 1150027;
  NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_INPUT_TERMINAL = 1150028;
  NIDCPOWER_ATTRIBUTE_EXPORTED_SEQUENCE_ADVANCE_TRIGGER_OUTPUT_TERMINAL = 1150029;
  NIDCPOWER_ATTRIBUTE_SOURCE_COMPLETE_EVENT_OUTPUT_TERMINAL = 1150043;
  NIDCPOWER_ATTRIBUTE_SOURCE_COMPLETE_EVENT_PULSE_POLARITY = 1150041;
  NIDCPOWER_ATTRIBUTE_SOURCE_COMPLETE_EVENT_PULSE_WIDTH = 1150042;
  NIDCPOWER_ATTRIBUTE_MEASURE_COMPLETE_EVENT_OUTPUT_TERMINAL = 1150047;
  NIDCPOWER_ATTRIBUTE_MEASURE_COMPLETE_EVENT_DELAY = 1150046;
  NIDCPOWER_ATTRIBUTE_MEASURE_COMPLETE_EVENT_PULSE_POLARITY = 1150044;
  NIDCPOWER_ATTRIBUTE_MEASURE_COMPLETE_EVENT_PULSE_WIDTH = 1150045;
  NIDCPOWER_ATTRIBUTE_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_TERMINAL = 1150040;
  NIDCPOWER_ATTRIBUTE_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_POLARITY = 1150038;
  NIDCPOWER_ATTRIBUTE_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_WIDTH = 1150039;
  NIDCPOWER_ATTRIBUTE_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_TERMINAL = 1150050;
  NIDCPOWER_ATTRIBUTE_SEQUENCE_ENGINE_DONE_EVENT_PULSE_POLARITY = 1150048;
  NIDCPOWER_ATTRIBUTE_SEQUENCE_ENGINE_DONE_EVENT_PULSE_WIDTH = 1150049;
  NIDCPOWER_ATTRIBUTE_ACTIVE_ADVANCED_SEQUENCE = 1150074;
  NIDCPOWER_ATTRIBUTE_ACTIVE_ADVANCED_SEQUENCE_STEP = 1150075;
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
  NIDCPOWER_ATTRIBUTE_SHUTDOWN_TRIGGER_TYPE = 1150275;
  NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_SHUTDOWN_TRIGGER_EDGE = 1150276;
  NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_SHUTDOWN_TRIGGER_INPUT_TERMINAL = 1150277;
  NIDCPOWER_ATTRIBUTE_INTERLOCK_INPUT_OPEN = 1150105;
  NIDCPOWER_ATTRIBUTE_POWER_SOURCE = 1150000;
  NIDCPOWER_ATTRIBUTE_POWER_SOURCE_IN_USE = 1150001;
  NIDCPOWER_ATTRIBUTE_AUXILIARY_POWER_SOURCE_AVAILABLE = 1150002;
  NIDCPOWER_ATTRIBUTE_ISOLATION_STATE = 1150302;
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
  NIDCPOWER_ATTRIBUTE_LCR_CUSTOM_MEASUREMENT_TIME = 1150258;
  NIDCPOWER_ATTRIBUTE_LCR_OPEN_CONDUCTANCE = 1150261;
  NIDCPOWER_ATTRIBUTE_LCR_OPEN_SUSCEPTANCE = 1150262;
  NIDCPOWER_ATTRIBUTE_LCR_SHORT_RESISTANCE = 1150263;
  NIDCPOWER_ATTRIBUTE_LCR_SHORT_REACTANCE = 1150264;
  NIDCPOWER_ATTRIBUTE_LCR_VOLTAGE_RANGE = 1150265;
  NIDCPOWER_ATTRIBUTE_LCR_DC_BIAS_VOLTAGE_RANGE = 1150266;
  NIDCPOWER_ATTRIBUTE_LCR_CURRENT_RANGE = 1150267;
  NIDCPOWER_ATTRIBUTE_LCR_DC_BIAS_CURRENT_RANGE = 1150274;
  NIDCPOWER_ATTRIBUTE_LCR_MEASURED_LOAD_RESISTANCE = 1150268;
  NIDCPOWER_ATTRIBUTE_LCR_MEASURED_LOAD_REACTANCE = 1150269;
  NIDCPOWER_ATTRIBUTE_LCR_ACTUAL_LOAD_RESISTANCE = 1150270;
  NIDCPOWER_ATTRIBUTE_LCR_ACTUAL_LOAD_REACTANCE = 1150271;
  NIDCPOWER_ATTRIBUTE_CABLE_LENGTH = 1150278;
  NIDCPOWER_ATTRIBUTE_LCR_AUTOMATIC_LEVEL_CONTROL = 1150290;
  NIDCPOWER_ATTRIBUTE_LCR_DC_BIAS_AUTOMATIC_LEVEL_CONTROL = 1150291;
  NIDCPOWER_ATTRIBUTE_LCR_SHORT_CUSTOM_CABLE_COMPENSATION_ENABLED = 1150299;
  NIDCPOWER_ATTRIBUTE_LCR_AC_ELECTRICAL_CABLE_LENGTH_DELAY = 1150309;
  NIDCPOWER_ATTRIBUTE_LCR_SOURCE_DELAY_MODE = 1150315;
  NIDCPOWER_ATTRIBUTE_LCR_LOAD_RESISTANCE = 1150318;
  NIDCPOWER_ATTRIBUTE_LCR_LOAD_INDUCTANCE = 1150319;
  NIDCPOWER_ATTRIBUTE_LCR_LOAD_CAPACITANCE = 1150320;
  NIDCPOWER_ATTRIBUTE_LCR_IMPEDANCE_RANGE_SOURCE = 1150321;
  NIDCPOWER_ATTRIBUTE_LCR_DC_BIAS_TRANSIENT_RESPONSE = 1150347;
  NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_ENABLED = 1150235;
  NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_HIGH = 1150236;
  NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_HIGH = 1150237;
  NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_LOW = 1150238;
  NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_LOW = 1150239;
  NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_CURRENT_OVERRANGE_ENABLED = 1150240;
  NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_LOW = 1150292;
  NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_LOW = 1150293;
  NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_HIGH = 1150294;
  NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_HIGH = 1150295;
  NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_DELAY = 1150300;
  NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_VOLTAGE_MEASURE_LIMIT_HIGH = 1150357;
  NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_VOLTAGE_MEASURE_LIMIT_LOW = 1150358;
  NIDCPOWER_ATTRIBUTE_LCR_AC_DITHER_ENABLED = 1150348;
  NIDCPOWER_ATTRIBUTE_LCR_SOURCE_APERTURE_TIME = 1150349;
  NIDCPOWER_ATTRIBUTE_OCP_ERROR_PERCENTAGE = 1150200;
  NIDCPOWER_ATTRIBUTE_SUPPORT_OUTPUT_DMA = 1150079;
  NIDCPOWER_ATTRIBUTE_INSTRUMENT_API_SESSION_HANDLE = 1150110;
  NIDCPOWER_ATTRIBUTE_ACTUAL_VOLTAGE_RANGE_FOR_LAST_FETCH = 1150259;
  NIDCPOWER_ATTRIBUTE_ACTUAL_CURRENT_RANGE_FOR_LAST_FETCH = 1150260;
  NIDCPOWER_ATTRIBUTE_WAS_SESSION_OPENED_BY_INITIALIZE_WITH_INDEPENDENT_CHANNELS = 1150111;
}

enum CurrentLimitBehavior {
  CURRENT_LIMIT_BEHAVIOR_NIDCPOWER_VAL_CURRENT_REGULATE = 0;
  CURRENT_LIMIT_BEHAVIOR_NIDCPOWER_VAL_CURRENT_TRIP = 1;
}

enum OutputStates {
  OUTPUT_STATES_NIDCPOWER_VAL_OUTPUT_CONSTANT_VOLTAGE = 0;
  OUTPUT_STATES_NIDCPOWER_VAL_OUTPUT_CONSTANT_CURRENT = 1;
  OUTPUT_STATES_NIDCPOWER_VAL_OUTPUT_OVER_VOLTAGE = 2;
  OUTPUT_STATES_NIDCPOWER_VAL_OUTPUT_OVER_CURRENT = 3;
  OUTPUT_STATES_NIDCPOWER_VAL_OUTPUT_UNREGULATED = 4;
  OUTPUT_STATES_NIDCPOWER_VAL_OUTPUT_INHIBITED = 1163;
}

enum MeasurementTypes {
  MEASUREMENT_TYPES_NIDCPOWER_VAL_MEASURE_CURRENT = 0;
  MEASUREMENT_TYPES_NIDCPOWER_VAL_MEASURE_VOLTAGE = 1;
}

enum OutputFunction {
  OUTPUT_FUNCTION_UNSPECIFIED = 0;
  OUTPUT_FUNCTION_NIDCPOWER_VAL_DC_VOLTAGE = 1006;
  OUTPUT_FUNCTION_NIDCPOWER_VAL_DC_CURRENT = 1007;
  OUTPUT_FUNCTION_NIDCPOWER_VAL_PULSE_VOLTAGE = 1049;
  OUTPUT_FUNCTION_NIDCPOWER_VAL_PULSE_CURRENT = 1050;
  OUTPUT_FUNCTION_NIDCPOWER_VAL_CONSTANT_RESISTANCE = 1161;
  OUTPUT_FUNCTION_NIDCPOWER_VAL_CONSTANT_POWER = 1162;
}

enum Sense {
  SENSE_UNSPECIFIED = 0;
  SENSE_NIDCPOWER_VAL_LOCAL = 1008;
  SENSE_NIDCPOWER_VAL_REMOTE = 1009;
}

enum DigitalEdge {
  DIGITAL_EDGE_UNSPECIFIED = 0;
  DIGITAL_EDGE_NIDCPOWER_VAL_RISING = 1016;
  DIGITAL_EDGE_NIDCPOWER_VAL_FALLING = 1017;
}

enum SourceMode {
  SOURCE_MODE_UNSPECIFIED = 0;
  SOURCE_MODE_NIDCPOWER_VAL_SINGLE_POINT = 1020;
  SOURCE_MODE_NIDCPOWER_VAL_SEQUENCE = 1021;
}

enum AutoZero {
  AUTO_ZERO_NIDCPOWER_VAL_OFF = 0;
  AUTO_ZERO_NIDCPOWER_VAL_ONCE = 1024;
  AUTO_ZERO_NIDCPOWER_VAL_ON = 1;
}

enum PowerLineFrequencies {
  POWER_LINE_FREQUENCIES_UNSPECIFIED = 0;
  POWER_LINE_FREQUENCIES_NIDCPOWER_VAL_50_HERTZ = 50;
  POWER_LINE_FREQUENCIES_NIDCPOWER_VAL_60_HERTZ = 60;
}

enum ApertureTimeUnits {
  APERTURE_TIME_UNITS_UNSPECIFIED = 0;
  APERTURE_TIME_UNITS_NIDCPOWER_VAL_SECONDS = 1028;
  APERTURE_TIME_UNITS_NIDCPOWER_VAL_POWER_LINE_CYCLES = 1029;
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
  OUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_SATURATED = 256;
  OUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_SATURATED = 512;
  OUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_MEASURE_HIGH = 1024;
  OUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_MEASURE_LOW = 2048;
  OUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_SELF_TEST_MEASUREMENT_HIGH = 4096;
  OUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_SELF_TEST_MEASUREMENT_LOW = 8192;
}

enum LCRCompensationType {
  LCR_COMPENSATION_TYPE_UNSPECIFIED = 0;
  LCR_COMPENSATION_TYPE_NIDCPOWER_VAL_OPEN_COMPENSATION = 1130;
  LCR_COMPENSATION_TYPE_NIDCPOWER_VAL_SHORT_COMPENSATION = 1131;
  LCR_COMPENSATION_TYPE_NIDCPOWER_VAL_LOAD_COMPENSATION = 1132;
  LCR_COMPENSATION_TYPE_NIDCPOWER_VAL_OPEN_CUSTOM_CABLE_COMPENSATION = 1133;
  LCR_COMPENSATION_TYPE_NIDCPOWER_VAL_SHORT_CUSTOM_CABLE_COMPENSATION = 1134;
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

enum SendSoftwareEdgeTriggerType {
  SEND_SOFTWARE_EDGE_TRIGGER_TYPE_UNSPECIFIED = 0;
  SEND_SOFTWARE_EDGE_TRIGGER_TYPE_NIDCPOWER_VAL_START = 1034;
  SEND_SOFTWARE_EDGE_TRIGGER_TYPE_NIDCPOWER_VAL_SOURCE = 1035;
  SEND_SOFTWARE_EDGE_TRIGGER_TYPE_NIDCPOWER_VAL_MEASURE = 1036;
  SEND_SOFTWARE_EDGE_TRIGGER_TYPE_NIDCPOWER_VAL_SEQUENCE_ADVANCE = 1037;
  SEND_SOFTWARE_EDGE_TRIGGER_TYPE_NIDCPOWER_VAL_PULSE = 1053;
  SEND_SOFTWARE_EDGE_TRIGGER_TYPE_NIDCPOWER_VAL_SHUTDOWN = 1118;
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
  NIDCPOWER_INT32_AUTO_ZERO_VAL_ONCE = 1024;
  NIDCPOWER_INT32_AUTO_ZERO_VAL_ON = 1;
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
  NIDCPOWER_INT32_CABLE_LENGTH_VAL_NI_STANDARD_0_5M = 1153;
  NIDCPOWER_INT32_CABLE_LENGTH_VAL_NI_STANDARD_1M = 1122;
  NIDCPOWER_INT32_CABLE_LENGTH_VAL_NI_STANDARD_2M = 1123;
  NIDCPOWER_INT32_CABLE_LENGTH_VAL_NI_STANDARD_4M = 1124;
  NIDCPOWER_INT32_CABLE_LENGTH_VAL_NI_STANDARD_TRIAXIAL_1M = 1139;
  NIDCPOWER_INT32_CABLE_LENGTH_VAL_NI_STANDARD_TRIAXIAL_2M = 1140;
  NIDCPOWER_INT32_CABLE_LENGTH_VAL_NI_STANDARD_TRIAXIAL_4M = 1141;
  NIDCPOWER_INT32_CABLE_LENGTH_VAL_CUSTOM_ONBOARD_STORAGE = 1125;
  NIDCPOWER_INT32_CABLE_LENGTH_VAL_CUSTOM_AS_CONFIGURED = 1126;
  NIDCPOWER_INT32_COMPLIANCE_LIMIT_SYMMETRY_VAL_SYMMETRIC = 0;
  NIDCPOWER_INT32_COMPLIANCE_LIMIT_SYMMETRY_VAL_ASYMMETRIC = 1;
  NIDCPOWER_INT32_CONDUCTION_VOLTAGE_MODE_VAL_CONDUCTION_VOLTAGE_MODE_AUTOMATIC = 1155;
  NIDCPOWER_INT32_CONDUCTION_VOLTAGE_MODE_VAL_CONDUCTION_VOLTAGE_MODE_ENABLED = 1156;
  NIDCPOWER_INT32_CONDUCTION_VOLTAGE_MODE_VAL_CONDUCTION_VOLTAGE_MODE_DISABLED = 1157;
  NIDCPOWER_INT32_CURRENT_LIMIT_BEHAVIOR_VAL_CURRENT_REGULATE = 0;
  NIDCPOWER_INT32_CURRENT_LIMIT_BEHAVIOR_VAL_CURRENT_TRIP = 1;
  NIDCPOWER_INT32_DC_NOISE_REJECTION_VAL_DC_NOISE_REJECTION_SECOND_ORDER = 1043;
  NIDCPOWER_INT32_DC_NOISE_REJECTION_VAL_DC_NOISE_REJECTION_NORMAL = 1044;
  NIDCPOWER_INT32_DIGITAL_EDGE_VAL_RISING = 1016;
  NIDCPOWER_INT32_DIGITAL_EDGE_VAL_FALLING = 1017;
  NIDCPOWER_INT32_INSTRUMENT_MODE_VAL_SMU_PS = 1061;
  NIDCPOWER_INT32_INSTRUMENT_MODE_VAL_LCR = 1062;
  NIDCPOWER_INT32_INSTRUMENT_MODE_VAL_E_LOAD = 1154;
  NIDCPOWER_INT32_ISOLATION_STATE_VAL_ISOLATED = 1128;
  NIDCPOWER_INT32_ISOLATION_STATE_VAL_NON_ISOLATED = 1129;
  NIDCPOWER_INT32_LCR_AUTOMATIC_LEVEL_CONTROL_VAL_OFF = 0;
  NIDCPOWER_INT32_LCR_AUTOMATIC_LEVEL_CONTROL_VAL_ON = 1;
  NIDCPOWER_INT32_LCRDC_BIAS_SOURCE_VAL_DC_BIAS_OFF = 1065;
  NIDCPOWER_INT32_LCRDC_BIAS_SOURCE_VAL_DC_BIAS_VOLTAGE = 1066;
  NIDCPOWER_INT32_LCRDC_BIAS_SOURCE_VAL_DC_BIAS_CURRENT = 1067;
  NIDCPOWER_INT32_LCRDC_BIAS_TRANSIENT_RESPONSE_VAL_LCR_DC_BIAS_TRANSIENT_RESPONSE_NORMAL = 1151;
  NIDCPOWER_INT32_LCRDC_BIAS_TRANSIENT_RESPONSE_VAL_LCR_DC_BIAS_TRANSIENT_RESPONSE_CUSTOM = 1152;
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
  NIDCPOWER_INT32_OUTPUT_FUNCTION_VAL_CONSTANT_RESISTANCE = 1161;
  NIDCPOWER_INT32_OUTPUT_FUNCTION_VAL_CONSTANT_POWER = 1162;
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

message NILCRLoadCompensationSpot {
  double frequency = 1;
  sint32 reference_value_type = 2;
  double reference_value_a = 3;
  double reference_value_b = 4;
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

message CloseRequest {
  nidevice_grpc.Session vi = 1;
}

message CloseResponse {
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

message ConfigureOutputEnabledRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  bool enabled = 3;
}

message ConfigureOutputEnabledResponse {
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

message ConfigureVoltageLevelRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double level = 3;
}

message ConfigureVoltageLevelResponse {
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

message ConfigureVoltageLevelRangeRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double range = 3;
}

message ConfigureVoltageLevelRangeResponse {
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

message ConfigureOutputResistanceRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double resistance = 3;
}

message ConfigureOutputResistanceResponse {
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

message ConfigurePulseVoltageLevelRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double level = 3;
}

message ConfigurePulseVoltageLevelResponse {
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

message ConfigurePulseBiasVoltageLevelRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double level = 3;
}

message ConfigurePulseBiasVoltageLevelResponse {
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

message ConfigurePulseVoltageLevelRangeRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double range = 3;
}

message ConfigurePulseVoltageLevelRangeResponse {
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

message ConfigurePulseCurrentLevelRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double level = 3;
}

message ConfigurePulseCurrentLevelResponse {
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

message ConfigurePulseBiasCurrentLevelRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double level = 3;
}

message ConfigurePulseBiasCurrentLevelResponse {
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

message ConfigurePulseCurrentLevelRangeRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double range = 3;
}

message ConfigurePulseCurrentLevelRangeResponse {
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

message CreateAdvancedSequenceRequest {
  nidevice_grpc.Session vi = 1;
  string sequence_name = 2;
  repeated sint32 attribute_ids = 3;
  bool set_as_active_sequence = 4;
}

message CreateAdvancedSequenceResponse {
  int32 status = 1;
}

message CreateAdvancedSequenceStepRequest {
  nidevice_grpc.Session vi = 1;
  bool set_as_active_step = 2;
}

message CreateAdvancedSequenceStepResponse {
  int32 status = 1;
}

message DeleteAdvancedSequenceRequest {
  nidevice_grpc.Session vi = 1;
  string sequence_name = 2;
}

message DeleteAdvancedSequenceResponse {
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

message MeasureMultipleLCRRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message MeasureMultipleLCRResponse {
  int32 status = 1;
  repeated NILCRMeasurement measurements = 2;
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

message QueryInComplianceRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message QueryInComplianceResponse {
  int32 status = 1;
  bool in_compliance = 2;
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

message CommitRequest {
  nidevice_grpc.Session vi = 1;
}

message CommitResponse {
  int32 status = 1;
}

message InitiateRequest {
  nidevice_grpc.Session vi = 1;
}

message InitiateResponse {
  int32 status = 1;
}

message AbortRequest {
  nidevice_grpc.Session vi = 1;
}

message AbortResponse {
  int32 status = 1;
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

message CalSelfCalibrateRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message CalSelfCalibrateResponse {
  int32 status = 1;
}

message GetExtCalRecommendedIntervalRequest {
  nidevice_grpc.Session vi = 1;
}

message GetExtCalRecommendedIntervalResponse {
  int32 status = 1;
  sint32 months = 2;
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

message ReadCurrentTemperatureRequest {
  nidevice_grpc.Session vi = 1;
}

message ReadCurrentTemperatureResponse {
  int32 status = 1;
  double temperature = 2;
}

message GetExtCalLastTempRequest {
  nidevice_grpc.Session vi = 1;
}

message GetExtCalLastTempResponse {
  int32 status = 1;
  double temperature = 2;
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

message ConfigureSoftwareEdgeStartTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message ConfigureSoftwareEdgeStartTriggerResponse {
  int32 status = 1;
}

message DisableStartTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message DisableStartTriggerResponse {
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

message ConfigureSoftwareEdgeSequenceAdvanceTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message ConfigureSoftwareEdgeSequenceAdvanceTriggerResponse {
  int32 status = 1;
}

message DisableSequenceAdvanceTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message DisableSequenceAdvanceTriggerResponse {
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

message ConfigureSoftwareEdgeSourceTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message ConfigureSoftwareEdgeSourceTriggerResponse {
  int32 status = 1;
}

message DisableSourceTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message DisableSourceTriggerResponse {
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

message ConfigureSoftwareEdgeMeasureTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message ConfigureSoftwareEdgeMeasureTriggerResponse {
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

message ConfigureSoftwareEdgePulseTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message ConfigureSoftwareEdgePulseTriggerResponse {
  int32 status = 1;
}

message DisablePulseTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message DisablePulseTriggerResponse {
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

message DisableRequest {
  nidevice_grpc.Session vi = 1;
}

message DisableResponse {
  int32 status = 1;
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

message SelfTestRequest {
  nidevice_grpc.Session vi = 1;
}

message SelfTestResponse {
  int32 status = 1;
  sint32 self_test_result = 2;
  string self_test_message = 3;
}

message RevisionQueryRequest {
  nidevice_grpc.Session vi = 1;
}

message RevisionQueryResponse {
  int32 status = 1;
  string instrument_driver_revision = 2;
  string firmware_revision = 3;
}

message ResetWithDefaultsRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetWithDefaultsResponse {
  int32 status = 1;
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

message GetNextCoercionRecordRequest {
  nidevice_grpc.Session vi = 1;
}

message GetNextCoercionRecordResponse {
  int32 status = 1;
  string coercion_record = 2;
}

message ClearInterchangeWarningsRequest {
  nidevice_grpc.Session vi = 1;
}

message ClearInterchangeWarningsResponse {
  int32 status = 1;
}

message ResetInterchangeCheckRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetInterchangeCheckResponse {
  int32 status = 1;
}

message GetNextInterchangeWarningRequest {
  nidevice_grpc.Session vi = 1;
}

message GetNextInterchangeWarningResponse {
  int32 status = 1;
  string interchange_warning = 2;
}

message GetErrorRequest {
  nidevice_grpc.Session vi = 1;
}

message GetErrorResponse {
  int32 status = 1;
  sint32 code = 2;
  string description = 3;
}

message ClearErrorRequest {
  nidevice_grpc.Session vi = 1;
}

message ClearErrorResponse {
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

message SetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDCPowerAttribute attribute_id = 3;
  string attribute_value_raw = 4;
}

message SetAttributeViStringResponse {
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

message SetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDCPowerAttribute attribute_id = 3;
  bool attribute_value = 4;
}

message SetAttributeViBooleanResponse {
  int32 status = 1;
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

message GetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDCPowerAttribute attribute_id = 3;
}

message GetAttributeViStringResponse {
  int32 status = 1;
  string attribute_value = 2;
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

message GetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDCPowerAttribute attribute_id = 3;
}

message GetAttributeViBooleanResponse {
  int32 status = 1;
  bool attribute_value = 2;
}

message ImportAttributeConfigurationFileRequest {
  nidevice_grpc.Session vi = 1;
  string file_path = 2;
}

message ImportAttributeConfigurationFileResponse {
  int32 status = 1;
}

message ExportAttributeConfigurationFileRequest {
  nidevice_grpc.Session vi = 1;
  string file_path = 2;
}

message ExportAttributeConfigurationFileResponse {
  int32 status = 1;
}

message ImportAttributeConfigurationBufferRequest {
  nidevice_grpc.Session vi = 1;
  bytes configuration = 2;
}

message ImportAttributeConfigurationBufferResponse {
  int32 status = 1;
}

message ExportAttributeConfigurationBufferRequest {
  nidevice_grpc.Session vi = 1;
}

message ExportAttributeConfigurationBufferResponse {
  int32 status = 1;
  bytes configuration = 2;
}

message PerformLCROpenCompensationRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  repeated double additional_frequencies = 3;
}

message PerformLCROpenCompensationResponse {
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

message PerformLCRLoadCompensationRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  repeated NILCRLoadCompensationSpot compensation_spots = 3;
}

message PerformLCRLoadCompensationResponse {
  int32 status = 1;
}

message ConfigureLCRCompensationRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  bytes compensation_data = 3;
}

message ConfigureLCRCompensationResponse {
  int32 status = 1;
}

message PerformLCROpenCustomCableCompensationRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message PerformLCROpenCustomCableCompensationResponse {
  int32 status = 1;
}

message PerformLCRShortCustomCableCompensationRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message PerformLCRShortCustomCableCompensationResponse {
  int32 status = 1;
}

message GetLCRCompensationDataRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message GetLCRCompensationDataResponse {
  int32 status = 1;
  bytes compensation_data = 2;
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

message CreateAdvancedSequenceStepWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  bool set_as_active_step = 3;
}

message CreateAdvancedSequenceStepWithChannelsResponse {
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

message DeleteAdvancedSequenceWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string sequence_name = 3;
}

message DeleteAdvancedSequenceWithChannelsResponse {
  int32 status = 1;
}

message CommitWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message CommitWithChannelsResponse {
  int32 status = 1;
}

message InitiateWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message InitiateWithChannelsResponse {
  int32 status = 1;
}

message AbortWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message AbortWithChannelsResponse {
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

message ConfigureSoftwareEdgeStartTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message ConfigureSoftwareEdgeStartTriggerWithChannelsResponse {
  int32 status = 1;
}

message DisableStartTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message DisableStartTriggerWithChannelsResponse {
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

message ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannelsResponse {
  int32 status = 1;
}

message DisableSequenceAdvanceTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message DisableSequenceAdvanceTriggerWithChannelsResponse {
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

message ConfigureSoftwareEdgeSourceTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message ConfigureSoftwareEdgeSourceTriggerWithChannelsResponse {
  int32 status = 1;
}

message DisableSourceTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message DisableSourceTriggerWithChannelsResponse {
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

message ConfigureSoftwareEdgeMeasureTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message ConfigureSoftwareEdgeMeasureTriggerWithChannelsResponse {
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

message ConfigureSoftwareEdgePulseTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message ConfigureSoftwareEdgePulseTriggerWithChannelsResponse {
  int32 status = 1;
}

message DisablePulseTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message DisablePulseTriggerWithChannelsResponse {
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

message ConfigureSoftwareEdgeShutdownTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message ConfigureSoftwareEdgeShutdownTriggerWithChannelsResponse {
  int32 status = 1;
}

message DisableShutdownTriggerWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message DisableShutdownTriggerWithChannelsResponse {
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

message ResetWithChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message ResetWithChannelsResponse {
  int32 status = 1;
}

message InvalidateAllAttributesRequest {
  nidevice_grpc.Session vi = 1;
}

message InvalidateAllAttributesResponse {
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

message ErrorQueryRequest {
  nidevice_grpc.Session vi = 1;
}

message ErrorQueryResponse {
  int32 status = 1;
  sint32 error_code = 2;
  string error_message = 3;
}

message GetLCRCustomCableCompensationDataRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message GetLCRCustomCableCompensationDataResponse {
  int32 status = 1;
  bytes custom_cable_compensation_data = 2;
}

message ConfigureLCRCustomCableCompensationRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  bytes custom_cable_compensation_data = 3;
}

message ConfigureLCRCustomCableCompensationResponse {
  int32 status = 1;
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidcpower/nidcpower.mak sha256=a8f82458d296356c9a2aa3fdea5d635266fb8b8f6568e9a59471ab2fde352a46 bytes=440 -->
## FILE: src/nidcpower/nidcpower.mak

- repository: `ni/nimi-python`
- source_path: `src/nidcpower/nidcpower.mak`
- sha256: `a8f82458d296356c9a2aa3fdea5d635266fb8b8f6568e9a59471ab2fde352a46`
- bytes: 440

````makefile


include $(BUILD_HELPER_DIR)/defines.mak

MODULE_FILES_TO_GENERATE := $(DEFAULT_PY_FILES_TO_GENERATE)

MODULE_FILES_TO_COPY := $(DEFAULT_PY_FILES_TO_COPY)

RST_FILES_TO_GENERATE := $(DEFAULT_RST_FILES_TO_GENERATE)

SPHINX_CONF_PY := $(DEFAULT_SPHINX_CONF_PY)
READTHEDOCS_CONFIG := $(DEFAULT_READTHEDOCS_CONFIG)

CUSTOM_TYPES_TO_COPY += \
    lcr_load_compensation_spot.py \
    lcr_measurement.py \

include $(BUILD_HELPER_DIR)/rules.mak
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidcpower/system_tests/conftest.py sha256=fa9f27c37c7c684d0e8e8fc3a3aea95d287e82b9bd1133285b61228344fd6979 bytes=468 -->
## FILE: src/nidcpower/system_tests/conftest.py

- repository: `ni/nimi-python`
- source_path: `src/nidcpower/system_tests/conftest.py`
- sha256: `fa9f27c37c7c684d0e8e8fc3a3aea95d287e82b9bd1133285b61228344fd6979`
- bytes: 468

````python
import pytest


def pytest_collection_modifyitems(items):
    '''Ignores initializer deprecation warnings for all nidcpower system tests.'''
    for item in items:
        item.add_marker(pytest.mark.filterwarnings('ignore:Attempting to initialize an independent channels session with a channels argument.:DeprecationWarning'))
        item.add_marker(pytest.mark.filterwarnings('ignore:Initializing session without independent channels enabled.:DeprecationWarning'))
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidcpower/system_tests/grpc_server_config.json sha256=a653f4023a0251a570d59b74a76cd4158b9d30ab718a729ed4b1f78ceb1770f0 bytes=156 -->
## FILE: src/nidcpower/system_tests/grpc_server_config.json

- repository: `ni/nimi-python`
- source_path: `src/nidcpower/system_tests/grpc_server_config.json`
- sha256: `a653f4023a0251a570d59b74a76cd4158b9d30ab718a729ed4b1f78ceb1770f0`
- bytes: 156

````json
{
    "address": "[::1]",
    "port": 31760,
    "security" : {
       "server_cert": "",
       "server_key": "",
       "root_cert": ""
    }
 }
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidcpower/system_tests/test_system_nidcpower.py sha256=9116bb21124bb1878e858b918ab159ddeb86051833ba8ad7e63b8f20232e8ff6 bytes=52913 -->
## FILE: src/nidcpower/system_tests/test_system_nidcpower.py

- repository: `ni/nimi-python`
- source_path: `src/nidcpower/system_tests/test_system_nidcpower.py`
- sha256: `9116bb21124bb1878e858b918ab159ddeb86051833ba8ad7e63b8f20232e8ff6`
- bytes: 52913

````python
import os
import pathlib
import sys
import tempfile

import grpc
import hightime
import pytest

import nidcpower

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent / 'shared'))
import system_test_utilities  # noqa: E402


def pytest_generate_tests(metafunc):
    """Parametrizes the "session" fixture by examining the the markers set for a test.

    By default, the session fixture is parametrized so each test runs once with an Independent
    Channels session. To also run a test with a legacy Synchronized Channels session, decorate the
    test with the custom marker @pytest.mark.include_legacy_session. To run a test with only a
    legacy session, decorate the test with @pytest.mark.legacy_session_only.
    """

    if 'session' in metafunc.fixturenames:
        # fixtures can't be parametrized more than once. this approach prevents exclusive
        # markers from being set on the same test

        legacy_session_only = metafunc.definition.get_closest_marker('legacy_session_only')
        include_legacy_session = metafunc.definition.get_closest_marker('include_legacy_session')

        if legacy_session_only:
            metafunc.parametrize('session', [False], indirect=True)
        if include_legacy_session:
            metafunc.parametrize('session', [True, False], indirect=True)
        if not legacy_session_only and not include_legacy_session:
            metafunc.parametrize('session', [True], indirect=True)


class SystemTests:
    @pytest.fixture(scope='function')
    def session(self, request, session_creation_kwargs):
        """Creates an NI-DCPower Session.

        Markers can be used to override the default initializer arguments. For example,
        @pytest.mark.resource_name('4162/0') will override the default resource name.

        Available markers include:
            @pytest.mark.resource_name
            @pytest.mark.channels
            @pytest.mark.reset
            @pytest.mark.options
            @pytest.mark.independent_channels

        By default, all dependent tests will run once with an Independent Channels session. Dependent
        tests can override this behavior by using custom markers. Refer to the documentation in
        pytest_generate_tests for more information.
        """

        # set default values
        init_args = {
            'resource_name': '4162',
            'channels': '',
            'reset': False,
            'options': 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe',
            'independent_channels': request.param
        }

        # iterate through markers and update arguments
        for marker in request.node.iter_markers():
            if marker.name in init_args:  # only look at markers with valid argument names
                init_args[marker.name] = marker.args[0]  # assume single parameter in marker

        # initialize and yield session
        with nidcpower.Session(**init_args, **session_creation_kwargs) as simulated_session:
            yield simulated_session

    def test_self_test(self, session):
        session.self_test()

    # Workaround for driver runtime bug. See issue #1798 for details.
    @pytest.mark.legacy_session_only
    def test_self_cal(self, session):
        session.self_cal()

    def test_get_channel_name(self, session):
        name = session.get_channel_name(1)
        assert name == '4162/0'

    def test_get_channel_names(self, session):
        expected_string = [f'4162/{x}' for x in range(12)]
        channel_indices = ['0-1, 2, 3:4', 5, (6, 7), range(8, 10), slice(10, 12)]
        assert session.get_channel_names(channel_indices) == expected_string

    @pytest.mark.resource_name('Dev1/0-5,Dev2/0-5')
    def test_get_channel_names_multiple_instruments(self, session):
        expected_string = [f'{name}/{channel}' for name in ['Dev1', 'Dev2'] for channel in range(6)]
        channel_indices = ['0-1, 2, 3:4', 5, (6, 7), range(8, 10), slice(10, 12)]
        assert session.get_channel_names(channel_indices) == expected_string

    def test_get_attribute_string(self, session):
        model = session.instrument_model
        assert model == 'NI PXIe-4162'

    def test_error_message(self, session_creation_kwargs):
        with pytest.raises(nidcpower.Error) as e:
            # We pass in an invalid model name to force going to error_message
            with nidcpower.Session('4162', [0, 1], False, 'Simulate=1, DriverSetup=Model:invalid_model; BoardType:PXIe', **session_creation_kwargs):
                pass
        assert e.value.code == -1074134964
        # The option string parameter contains an entry with an unknown option value.

    def test_get_error(self, session):
        with pytest.raises(nidcpower.Error) as e:
            session.instrument_model = ''
        assert e.value.code == -1074135027
        # Error Description: Attribute is read-only.

    def test_get_self_cal_last_date_and_time(self, session):
        last_cal = session.get_self_cal_last_date_and_time()
        assert last_cal.year == 1940
        assert last_cal.month == 3
        assert last_cal.day == 1
        assert last_cal.hour == 0
        assert last_cal.minute == 0

    def test_get_self_cal_last_temp(self, session):
        temperature = session.get_self_cal_last_temp()
        assert temperature == 25.0

    def test_read_current_temperature(self, session):
        temperature = session.read_current_temperature()
        assert temperature == 25.0

    def test_reset_device(self, session):
        channel = session.channels['0']
        default_output_function = channel.output_function
        assert default_output_function == nidcpower.OutputFunction.DC_VOLTAGE
        channel.output_function = nidcpower.OutputFunction.DC_CURRENT
        session.reset_device()
        function_after_reset = channel.output_function
        assert function_after_reset == default_output_function

    def test_reset_with_default(self, session):
        channel = session.channels['0']
        assert channel.aperture_time_units == nidcpower.ApertureTimeUnits.SECONDS
        channel.aperture_time_units = nidcpower.ApertureTimeUnits.POWER_LINE_CYCLES
        session.reset_with_defaults()
        assert channel.aperture_time_units == nidcpower.ApertureTimeUnits.SECONDS

    def test_reset(self, session):
        channel = session.channels['0']
        assert channel.output_enabled is True
        channel.output_enabled = False
        session.reset()
        assert channel.output_enabled is True

    def test_disable(self, session):
        channel = session.channels['0']
        assert channel.output_enabled is True
        session.disable()
        assert channel.output_enabled is False

    @pytest.mark.channels('0')
    def test_measure(self, session):
        session.source_mode = nidcpower.SourceMode.SINGLE_POINT
        session.output_function = nidcpower.OutputFunction.DC_VOLTAGE
        session.voltage_level_range = 6
        session.voltage_level = 2
        with session.initiate():
            reading = session.measure(nidcpower.MeasurementTypes.VOLTAGE)
            assert session.query_in_compliance() is False
        assert reading == 2

    @pytest.mark.channels('0')
    def test_query_output_state(self, session):
        with session.initiate():
            assert session.query_output_state(nidcpower.OutputStates.CONSTANT_VOLTAGE) is True   # since default function is DCVolt when initiated output state for DC Volt\DC current should be True and False respectively
            assert session.query_output_state(nidcpower.OutputStates.CONSTANT_CURRENT) is False

    @pytest.mark.channels('0')
    def test_config_aperture_time(self, session):
        expected_default_aperture_time = 0.01666
        default_aperture_time = session.aperture_time
        assert session.aperture_time_units == nidcpower.ApertureTimeUnits.SECONDS
        default_aperture_time_in_range = abs(default_aperture_time - expected_default_aperture_time) <= max(1e-09 * max(abs(default_aperture_time), abs(expected_default_aperture_time)), 0.0)  # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
        assert default_aperture_time_in_range is True
        session.configure_aperture_time(5, nidcpower.ApertureTimeUnits.POWER_LINE_CYCLES)
        assert session.aperture_time_units == nidcpower.ApertureTimeUnits.POWER_LINE_CYCLES
        aperture_time = session.aperture_time
        expected_aperture_time = 5
        aperture_time_in_range = abs(aperture_time - expected_aperture_time) <= max(1e-09 * max(abs(aperture_time), abs(expected_aperture_time)), 0.0)  # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
        assert aperture_time_in_range is True

    @pytest.mark.channels('0')
    def test_fetch_multiple(self, session):
        session.source_mode = nidcpower.SourceMode.SINGLE_POINT
        session.configure_aperture_time(0, nidcpower.ApertureTimeUnits.SECONDS)
        session.voltage_level = 1
        count = 10
        session.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE
        with session.initiate():
            measurements = session.fetch_multiple(count)
            assert len(measurements) == count
            assert isinstance(measurements[1].voltage, float)
            assert isinstance(measurements[1].current, float)
            assert measurements[1].in_compliance in [True, False]
            assert measurements[1].voltage == 1.0
            assert measurements[1].current == 0.00001

    def test_measure_multiple(self, session):
        with session.initiate():
            # session is open to all 12 channels on the device
            measurements = session.measure_multiple()
            assert len(measurements) == 12
            assert measurements[1].in_compliance is None
            assert measurements[1].voltage == 0.0
            assert measurements[1].current == 0.00001
            # now a subset of the channels
            measurements = session.channels[range(4)].measure_multiple()
            assert len(measurements) == 4
            assert measurements[1].in_compliance is None
            assert measurements[1].voltage == 0.0
            assert measurements[1].current == 0.00001

    @pytest.mark.parametrize(
        'resource_name,channels,independent_channels,measurement_channels,expected_measured_channel',
        [
            ('Dev1', '1', False, None, '1'),
            ('Dev1', '2', False, '', '2'),
            ('Dev1', '3', False, ' ', '3'),
            ('Dev1', '4', False, '4', '4'),
            (' Dev1 ', ' 5 ', False, ' 5 ', '5'),
            ('Dev1', '1', True, None, 'Dev1/1'),
            ('Dev1', '2', True, '', 'Dev1/2'),
            ('Dev1', '3', True, ' ', 'Dev1/3'),
            ('Dev1', '4', True, '4', 'Dev1/4'),
            ('Dev1', 'Dev1/5', True, 'Dev1/5', 'Dev1/5'),
            ('Dev1/6', '', True, None, 'Dev1/6'),
            ('Dev1/7', ' ', True, ' ', 'Dev1/7'),
            ('  DEV1 / 8  ', ' ', True, ' dev1  /  8 ', 'DEV1/8')
        ]
    )
    def test_fetch_multiple_channels(
        self,
        session_creation_kwargs,
        resource_name,
        channels,
        independent_channels,
        measurement_channels,
        expected_measured_channel
    ):
        options = {'Simulate': True, 'DriverSetup': {'Model': '4162', 'BoardType': 'PXIe'}}
        with nidcpower.Session(
            resource_name,
            channels,
            options=options,
            independent_channels=independent_channels,
            **session_creation_kwargs
        ) as session:
            session.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE
            count = 10
            with session.initiate():
                if measurement_channels is None:
                    measurements = session.fetch_multiple(count)
                else:
                    measurements = session.channels[measurement_channels].fetch_multiple(count)
                assert len(measurements) == count
                for measurement in measurements:
                    assert measurement.channel == expected_measured_channel

    @pytest.mark.parametrize(
        'resource_name,channels,independent_channels,measurement_channels,expected_measured_channels',
        [
            ('Dev1', None, False, None, [str(x) for x in range(12)]),
            ('Dev1', '', False, '', [str(x) for x in range(12)]),
            ('Dev1', ' ', False, ' ', [str(x) for x in range(12)]),
            ('Dev1', '0,2-3,6', False, '2-3,0', ['2', '3', '0']),
            (' DEV1 ', ' 0 , 2 - 3 , 6 ', False, ' 2 - 3 , 0', ['2', '3', '0']),
            ('Dev1', None, True, None, [f'Dev1/{x}' for x in range(12)]),
            ('Dev1', '', True, '', [f'Dev1/{x}' for x in range(12)]),
            ('Dev1', ' ', True, ' ', [f'Dev1/{x}' for x in range(12)]),
            ('Dev1', '0:2,Dev1/4', True, 'Dev1/1:2,0', ['Dev1/1', 'Dev1/2', 'Dev1/0']),
            ('Dev1', 'Dev1/0:2,Dev1/4', True, 'Dev1/1:2,Dev1/0', ['Dev1/1', 'Dev1/2', 'Dev1/0']),
            ('Dev1/1', '', True, None, ['Dev1/1']),
            ('Dev1/1:4', ' ', True, '2:3', ['Dev1/2', 'Dev1/3']),
            ('Dev1/0-1,Dev2/0:2', ' ', True, 'Dev2/0-1,Dev1/0', ['Dev2/0', 'Dev2/1', 'Dev1/0']),
            ('Dev1/1:4,Dev1/6', ' ', True, '6,2-3', ['Dev1/6', 'Dev1/2', 'Dev1/3']),
            (' dev1 / 0 - 1 , DEV2 / 0 : 2 ', ' ', True, ' Dev2 / 0 - 1 , DEV1 / 0 ', ['DEV2/0', 'DEV2/1', 'dev1/0']),
            ('DEV1  /1:4,dev1/  6', ' ', True, ' 6 , 2 - 3 ', ['DEV1/6', 'DEV1/2', 'DEV1/3'])
        ]
    )
    def test_measure_multiple_channels(
        self,
        session_creation_kwargs,
        resource_name,
        channels,
        independent_channels,
        measurement_channels,
        expected_measured_channels
    ):
        options = {'Simulate': True, 'DriverSetup': {'Model': '4162', 'BoardType': 'PXIe'}}
        with nidcpower.Session(
            resource_name,
            channels,
            options=options,
            independent_channels=independent_channels,
            **session_creation_kwargs
        ) as session:
            with session.initiate():
                if measurement_channels is None:
                    measurements = session.measure_multiple()
                else:
                    measurements = session.channels[measurement_channels].measure_multiple()
                assert [measurement.channel for measurement in measurements] == expected_measured_channels

    @pytest.mark.resource_name('Dev1,Dev2')
    def test_measure_multiple_channel_ordering(self, session):
        for instrument in (1, 2):
            for channel in range(12):
                session.channels[f"Dev{instrument}/{channel}"].voltage_level = instrument + channel * 0.01
        with session.initiate():
            measurements = session.channels["Dev2/3-5, Dev1/0, Dev2/7"].measure_multiple()
            expected_measured_voltages_and_channels = (
                (2.03, "Dev2/3"),
                (2.04, "Dev2/4"),
                (2.05, "Dev2/5"),
                (1.00, "Dev1/0"),
                (2.07, "Dev2/7")
            )
            assert len(measurements) == len(expected_measured_voltages_and_channels)
            for measurement, expected_measured_voltage_and_channel in zip(
                measurements,
                expected_measured_voltages_and_channels
            ):
                expected_measured_voltage, expected_channel = expected_measured_voltage_and_channel
                assert measurement.voltage == pytest.approx(expected_measured_voltage)
                assert measurement.channel == expected_channel

    @pytest.mark.independent_channels(False)
    def test_measure_multiple_channel_ordering_non_independent_channels(self, session):
        for channel in range(12):
            session.channels[f"{channel}"].voltage_level = channel * 0.01
        with session.initiate():
            measurements = session.channels["3-4, 0, 7, 1"].measure_multiple()
            expected_measured_voltages_and_channels = (
                (0.03, "3"),
                (0.04, "4"),
                (0.00, "0"),
                (0.07, "7"),
                (0.01, "1")
            )
            assert len(measurements) == len(expected_measured_voltages_and_channels)
            for measurement, expected_measured_voltage_and_channel in zip(
                measurements,
                expected_measured_voltages_and_channels
            ):
                expected_measured_voltage, expected_channel = expected_measured_voltage_and_channel
                assert measurement.voltage == pytest.approx(expected_measured_voltage)
                assert measurement.channel == expected_channel

    @pytest.mark.parametrize(
        'resource_name,measurement_channels',
        [
            ('Dev1/0:1,Dev2/2:3', 'Dev1/0,2'),
            ('Dev1/0:1,Dev2/0:1', '2,3'),
            ('Dev1/0, Dev1/1, Dev2/2', '0, Dev1/1')
        ]
    )
    def test_measure_multiple_error_invalid_channels(self, session_creation_kwargs, resource_name, measurement_channels):
        options = {'Simulate': True, 'DriverSetup': {'Model': '4162', 'BoardType': 'PXIe'}}
        with nidcpower.Session(
            resource_name,
            channels=' ',
            options=options,
            independent_channels=True,
            **session_creation_kwargs
        ) as session:
            with session.initiate():
                with pytest.raises(nidcpower.errors.DriverError) as e:
                    session.channels[measurement_channels].measure_multiple()
                assert e.value.code == -1074135008
                assert 'Unknown channel or repeated capability name.' in e.value.description

    @pytest.mark.channels('0')
    def test_query_max_current_limit(self, session):
        max_current_limit = session.query_max_current_limit(6)
        assert max_current_limit == pytest.approx(0.1, 1e-9)  # for a simulated 4162 max current limit should be 0.1 for 6V Voltage level

    @pytest.mark.channels('0')
    def test_query_max_voltage_level(self, session):
        max_voltage_level = session.query_max_voltage_level(0.03)
        assert max_voltage_level == pytest.approx(24, 1e-9)  # for a simulated 4162 max voltage level should be 24V for 30mA current limit

    @pytest.mark.channels('0')
    def test_query_min_current_limit(self, session):
        min_current_limit = session.query_min_current_limit(0.03)
        assert min_current_limit == pytest.approx(0.1e-6, 1e-9)  # for a simulated 4162 min_current_limit should be 0.1uA for 30mV voltage level

    @pytest.mark.channels('0')
    def test_set_sequence_with_source_delays(self, session):
        session.set_sequence([0.1, 0.2, 0.3], [0.001, 0.002, 0.003])

    @pytest.mark.channels('0')
    def test_set_sequence_with_too_many_source_delays(self, session):
        with pytest.raises(ValueError):
            session.set_sequence([0.1, 0.2, 0.3], [0.001, 0.002, 0.003, 0.004])

    @pytest.mark.channels('0')
    def test_set_sequence_with_too_few_source_delays(self, session):
        with pytest.raises(ValueError):
            session.set_sequence([0.1, 0.2, 0.3, 0.4], [0.001, 0.002])

    @pytest.mark.channels('0')
    def test_wait_for_event_default_timeout(self, session):
        with session.initiate():
            session.wait_for_event(nidcpower.Event.SOURCE_COMPLETE)

    @pytest.mark.channels('0')
    def test_wait_for_event_with_timeout(self, session):
        with session.initiate():
            session.wait_for_event(nidcpower.Event.SOURCE_COMPLETE, hightime.timedelta(seconds=0.5))

    @pytest.mark.channels('0')
    def test_commit(self, session):
        non_default_current_limit = 0.00021
        session.current_limit = non_default_current_limit
        session.commit()

    @pytest.mark.channels('0')
    def test_import_export_buffer(self, session):
        test_value_1 = 1
        test_value_2 = 2
        session.voltage_level = test_value_1
        assert session.voltage_level == test_value_1
        buffer = session.export_attribute_configuration_buffer()
        session.voltage_level = test_value_2
        assert session.voltage_level == test_value_2
        session.import_attribute_configuration_buffer(buffer)
        assert session.voltage_level == test_value_1

    @pytest.mark.channels('0')
    def test_import_export_file(self, session):
        test_value_1 = 1
        test_value_2 = 2
        temp_file = tempfile.NamedTemporaryFile(suffix='.txt', delete=False)
        # NamedTemporaryFile() returns the file already opened, so we need to close it before we can use it
        temp_file.close()
        path = temp_file.name
        session.voltage_level = test_value_1
        assert session.voltage_level == test_value_1
        session.export_attribute_configuration_file(path)
        session.voltage_level = test_value_2
        assert session.voltage_level == test_value_2
        session.import_attribute_configuration_file(path)
        assert session.voltage_level == test_value_1
        os.remove(path)

    @pytest.mark.channels('0')
    def test_create_and_delete_advanced_sequence(self, session):
        properties_used = ['output_function', 'voltage_level']
        sequence_name = 'my_sequence'
        session.source_mode = nidcpower.SourceMode.SEQUENCE
        session.create_advanced_sequence(sequence_name=sequence_name, property_names=properties_used, set_as_active_sequence=True)
        session.create_advanced_sequence_step(set_as_active_step=True)
        assert session.active_advanced_sequence == sequence_name
        session.output_function = nidcpower.OutputFunction.DC_VOLTAGE
        session.voltage_level = 1
        session.delete_advanced_sequence(sequence_name=sequence_name)
        with pytest.raises(nidcpower.errors.DriverError):
            session.active_advanced_sequence = sequence_name

    @pytest.mark.channels('0')
    def test_create_advanced_sequence_commit_step(self, session):
        properties_used = ['output_function', 'voltage_level']
        sequence_name = 'my_sequence'
        session.source_mode = nidcpower.SourceMode.SEQUENCE
        session.create_advanced_sequence(sequence_name=sequence_name, property_names=properties_used, set_as_active_sequence=True)
        with pytest.raises(nidcpower.Error) as e:
            session.create_advanced_sequence_commit_step(set_as_active_step=True)
        assert e.value.code == -1074118619
        # Error Description: This device does not support the requested operation. Refer to the device
        # documentation to determine which operations it supports.

    @pytest.mark.channels('0')
    def test_create_and_delete_advanced_sequence_bad_name(self, session):
        properties_used = ['output_function_bad', 'voltage_level']
        sequence_name = 'my_sequence'
        session.source_mode = nidcpower.SourceMode.SEQUENCE
        with pytest.raises(KeyError):
            session.create_advanced_sequence(sequence_name=sequence_name, property_names=properties_used, set_as_active_sequence=True)

    @pytest.mark.channels('0')
    def test_create_and_delete_advanced_sequence_bad_type(self, session):
        properties_used = ['unlock', 'voltage_level']
        sequence_name = 'my_sequence'
        session.source_mode = nidcpower.SourceMode.SEQUENCE
        with pytest.raises(TypeError):
            session.create_advanced_sequence(sequence_name=sequence_name, property_names=properties_used, set_as_active_sequence=True)

    @pytest.mark.legacy_session_only
    def test_send_software_edge_trigger_error(self, session):
        with pytest.raises(nidcpower.Error) as e:
            session.send_software_edge_trigger(nidcpower.SendSoftwareEdgeTriggerType.START)
        assert e.value.code == -1074118587
        # Error Description: The requested function is not available when multiple channels are present in the same session.

    def test_get_ext_cal_last_date_and_time(self, session):
        last_cal = session.get_ext_cal_last_date_and_time()
        assert last_cal.year == 1940
        assert last_cal.month == 3
        assert last_cal.day == 1
        assert last_cal.hour == 0
        assert last_cal.minute == 0

    def test_get_ext_cal_last_temp(self, session):
        temperature = session.get_ext_cal_last_temp()
        assert temperature == 25.0

    def test_get_ext_cal_recommended_interval(self, session):
        interval = session.get_ext_cal_recommended_interval()
        assert interval.days == 365

    def test_set_get_vi_int_64_attribute(self, session):
        session.channels['0'].active_advanced_sequence_step = 1
        read_advanced_sequence_step = session.channels['0'].active_advanced_sequence_step
        assert read_advanced_sequence_step == 1

    @pytest.mark.parametrize(
        'channels,expected_channel_count',
        [
            ([0, 1], 2),
            (range(2), 2),
            ('0,1', 2),
            (None, 12)
        ]
    )
    def test_channels_argument_format(self, session_creation_kwargs, channels, expected_channel_count):
        with nidcpower.Session('4162', channels, False, 'Simulate=1, DriverSetup=Model:4162; BoardType:PXIe', **session_creation_kwargs) as simulated_session:
            assert simulated_session.channel_count == expected_channel_count

    def test_default_channels_argument(self, session_creation_kwargs):
        with nidcpower.Session(resource_name='4162', reset=False, options='Simulate=1, DriverSetup=Model:4162; BoardType:PXIe', **session_creation_kwargs) as simulated_session:
            assert simulated_session.channel_count == 12

    @pytest.mark.parametrize(
        'resource_name,channels,independent_channels',
        [
            ('Dev1', None, False),
            ('Dev1', '', False),
            ('Dev1', '0', False),
            ('Dev1', '0', True)
        ]
    )
    def test_init_issues_deprecation_warnings(self, session_creation_kwargs, resource_name, channels, independent_channels):
        """Tests for deprecation warnings for legacy initialization options.

        A deprecation warning should occur any time independent_channels is False or a channels
        argument is supplied.
        """
        options = {'Simulate': True, 'DriverSetup': {'Model': '4162', 'BoardType': 'PXIe'}}
        with pytest.deprecated_call() as dc:
            with nidcpower.Session(resource_name, channels, options=options, independent_channels=independent_channels, **session_creation_kwargs):
                pass
        assert len(dc.list) == 1  # assert only 1 deprecation warning was thrown
        message = dc.list[0].message.args[0]  # grabs the deprecation warning message
        if not independent_channels:
            assert message.find('Initializing session without independent channels enabled.') != -1
        if channels and independent_channels:
            assert message.find('Attempting to initialize an independent channels session with a channels argument.') != -1

    @pytest.mark.parametrize(
        'resource_name,channels',
        [
            ('Dev1', None),
            ('Dev1', ''),
            ('Dev1', '0'),
            ('Dev1', '0,1'),
            (['Dev1'], [0, 1]),
            (('Dev1',), (0, 1)),
            ('Dev1', range(2))
        ]
    )
    def test_init_backwards_compatibility_with_initialize_with_channels(self, session_creation_kwargs, resource_name, channels):
        """Tests that legacy sessions open without exception for valid arguments."""
        options = {'Simulate': True, 'DriverSetup': {'Model': '4162', 'BoardType': 'PXIe'}}
        with nidcpower.Session(resource_name, channels, options=options, independent_channels=False, **session_creation_kwargs):
            pass

    @pytest.mark.parametrize(
        'resource_name,channels',
        [
            ('Dev1', None),
            ('Dev1', ''),
            ('Dev1', '0'),  # backwards compatibility check
            ('Dev1', '0,1'),  # backwards compatibility check
            ('Dev1/0', None),
            ('Dev1/0', ''),
            ('Dev1/0,Dev1/1', None),
            ('Dev1/0,Dev2/1', None),
            ('Dev1/0,Dev2/1', ''),
            (['Dev1/0', 'Dev1/1'], ''),  # construct with list
            (('Dev1/0', 'Dev1/1'), ''),  # construct with tuple
            ('Dev1/0-3', None),
            ('Dev1/0:3', None)
        ]
    )
    def test_init_with_independent_channels(self, session_creation_kwargs, resource_name, channels):
        """Tests that independent channels sessions open without exception for valid arguments."""
        options = {'Simulate': True, 'DriverSetup': {'Model': '4162', 'BoardType': 'PXIe'}}
        with nidcpower.Session(resource_name, channels, options=options, independent_channels=True, **session_creation_kwargs):
            pass

    def test_init_raises_value_error_for_multi_instrument_resource_name_and_channels_argument(self, session_creation_kwargs):
        """Combining channels with multiple instruments is invalid.

        Tests that a value error is thrown when a multi-instrument resource name is provided with
        a channels argument. How to combine the two arguments is undefined.
        """
        options = {'Simulate': True, 'DriverSetup': {'Model': '4162', 'BoardType': 'PXIe'}}
        with pytest.raises(ValueError):
            with nidcpower.Session("Dev1,Dev2", "0", options=options, independent_channels=True, **session_creation_kwargs):
                pass

    @pytest.mark.parametrize(
        'resource_name,channels',
        [
            ('Dev1/0', '0'),  # combines to 'Dev1/0/0'
            ('Dev1/0', '0,1'),  # combines to 'Dev1/0/0,1'
            ('Dev1/0', '0:3'),  # combines to 'Dev1/0/0:3'
            ('Dev1/0', '0-3'),  # combines to 'Dev1/0/0-3'
            ('Dev1/0', range(4))  # combines to 'Dev1/0/0-3'
        ]
    )
    def test_init_raises_driver_errors_for_invalid_arguments(self, session_creation_kwargs, resource_name, channels):
        """Tests for driver errors that should occur for invalid initialization arguments."""
        options = {'Simulate': True, 'DriverSetup': {'Model': '4162', 'BoardType': 'PXIe'}}
        with pytest.raises(nidcpower.errors.DriverError) as e:
            with nidcpower.Session(resource_name, channels, options=options, **session_creation_kwargs):
                pass
        assert e.value.code == -1074097793
        # Error Description: The specified device cannot be found.

    @pytest.mark.parametrize(
        'resource_name,channels',
        [
            ('Dev1/0', None),
            ('Dev1/0', 'Dev1/0'),
            ('Dev1/0,Dev2/0', 'Dev1/0'),
            ('Dev1,Dev2', '')
        ]
    )
    def test_init_raises_driver_errors_for_invalid_arguments_legacy_session(self, session_creation_kwargs, resource_name, channels):
        """Tests invalid initializer arguments for legacy initialize with channels sessions.

        Multi-instrument resource names are valid for simulated initialize with channels sessions. So,
        we attempt to initialize a true session and assert an unsupported device exception is raised.
        """

        with pytest.raises(nidcpower.errors.DriverError) as e:
            with nidcpower.Session(resource_name, channels, independent_channels=False, **session_creation_kwargs):
                pass
        assert e.value.code == -1074118656
        # Error Description: Device was not recognized. The device is not supported with this driver or version.

    @pytest.mark.include_legacy_session
    def test_repeated_capabilities_on_method_when_all_channels_are_specified(self, session):
        """Sessions should not error when specifying all channels by number."""
        assert session.channels['0'].output_enabled is True
        session.channels['0'].output_enabled = False
        session.channels['0-11'].reset()
        assert session.channels['0'].output_enabled is True

    @pytest.mark.legacy_session_only
    def test_error_channel_name_not_allowed_in_legacy_session(self, session):
        with pytest.raises(nidcpower.Error) as e:
            session.channels['0'].reset()
        assert e.value.code == -1074118494
        # Error Description: The channel name string must represent all channels in the session because
        # the session was not initialized with independent channels. To specify a subset of channels
        # for this function, first initialize the session with independent channels.

    @pytest.mark.legacy_session_only
    def test_error_channel_name_not_allowed(self, session):
        with pytest.raises(nidcpower.Error) as e:
            session.channels['0'].instrument_model
        assert e.value.code == -1074134971
        # Error Description: The channel or repeated capability name is not allowed.

    @pytest.mark.resource_name('Dev1,Dev2')
    @pytest.mark.parametrize(
        'channels',
        [
            'Dev1/0-11,Dev2/0-11',
            'Dev1/2:5,Dev2/4:7',
            'Dev1/10,Dev2/11',
            'Dev1/3,Dev2/0:11'
        ]
    )
    def test_repeated_capabilities_with_initiate_multi_instrument_session(self, session, channels):
        session.channels[channels].initiate()

    @pytest.mark.resource_name('Dev1')
    @pytest.mark.parametrize('channels', ['Dev1/0', 'Dev1/9-11', '', '0', '4:6', '2-10', '0-11'])
    def test_repeated_capabilities_with_initiate_single_instrument_session(self, session, channels):
        session.channels[channels].initiate()

    @pytest.mark.legacy_session_only
    @pytest.mark.parametrize('channels', ['', '0-11'])
    def test_repeated_capabilities_with_initiate_legacy_session(self, session, channels):
        """Initiate should work on legacy sessions when all channels are specified."""
        session.channels[channels].initiate()

    @pytest.mark.resource_name('Dev1/0-3,Dev2/0,Dev3/0:3')
    @pytest.mark.parametrize('indices', ('0:8', range(9)))
    def test_repeated_capabilities_with_initiate_and_get_channel_names(self, session, indices):
        session.channels[session.get_channel_names(indices)].initiate()

    @pytest.mark.resource_name('Dev1/0')
    @pytest.mark.parametrize('channels', ('1', '0-1', 1))
    def test_invalid_channels_repeated_capabilities(self, session, channels):
        with pytest.raises(nidcpower.Error) as e:
            session.channels[channels].output_function = nidcpower.OutputFunction.DC_VOLTAGE
        assert e.value.code == -1074135008
        # Error Description: Unknown channel or repeated capability name.

    @pytest.mark.resource_name('Dev1,Dev2,Dev3')
    @pytest.mark.parametrize(
        'device_name',
        [
            'Dev1',
            'Dev2',
            'Dev3',
            'Dev1,Dev2',
            'Dev1,Dev2,Dev3',
            ''
        ]
    )
    def test_instruments_repeated_capability(self, session, device_name):
        assert session.instruments[device_name].instrument_model == 'NI PXIe-4162'

    @pytest.mark.resource_name('Dev1/0:3, Dev2/0:3')
    @pytest.mark.parametrize(
        'channels',
        [
            'Dev1/0',
            'Dev1/0-3',
            'Dev2/0',
            'Dev2/0:3',
            'Dev1/0,Dev2/0',
            'Dev1/0:1,Dev2/2-3',
            'Dev1/3,Dev2/0-3'
        ]
    )
    def test_create_and_delete_advanced_sequence_repeated_capabilities(self, session, channels):
        channels_session = session.channels[channels]
        properties_used = ['output_function', 'voltage_level']
        sequence_name = 'my_sequence'
        channels_session.source_mode = nidcpower.SourceMode.SEQUENCE
        channels_session.create_advanced_sequence(sequence_name=sequence_name, property_names=properties_used, set_as_active_sequence=True)
        channels_session.create_advanced_sequence_step(set_as_active_step=True)
        assert channels_session.active_advanced_sequence == sequence_name
        channels_session.output_function = nidcpower.OutputFunction.DC_VOLTAGE
        channels_session.voltage_level = 1
        channels_session.delete_advanced_sequence(sequence_name=sequence_name)
        with pytest.raises(nidcpower.errors.DriverError):
            channels_session.active_advanced_sequence = sequence_name

    @pytest.mark.resource_name('Dev1/0, Dev2/0')
    @pytest.mark.parametrize('channels', ('Dev1/0', 'Dev2/0', 'Dev1/0,Dev2/0'))
    def test_create_advanced_sequence_commit_step_repeated_capabilities(self, session, channels):
        channels_session = session.channels[channels]
        properties_used = ['output_function', 'voltage_level']
        sequence_name = 'my_sequence'
        channels_session.source_mode = nidcpower.SourceMode.SEQUENCE
        channels_session.create_advanced_sequence(sequence_name=sequence_name, property_names=properties_used, set_as_active_sequence=True)
        with pytest.raises(nidcpower.Error) as e:
            channels_session.create_advanced_sequence_commit_step(set_as_active_step=True)
        assert e.value.code == -1074118619
        # Error Description: This device does not support the requested operation. Refer to the device
        # documentation to determine which operations it supports.

    @pytest.mark.resource_name('Dev1/0:3, Dev2/0:3')
    @pytest.mark.parametrize('method', ['abort', 'commit', 'reset'])
    @pytest.mark.parametrize(
        'channels',
        [
            'Dev1/0',
            'Dev1/0-3',
            'Dev2/0',
            'Dev2/0:3',
            'Dev1/0,Dev2/0',
            'Dev1/0:1,Dev2/2-3',
            'Dev1/3,Dev2/0-3'
        ]
    )
    def test_repeated_capabilities_parameterless_methods(self, session, channels, method):
        """Double parametrize markers of this method results in nested parameterization of the test."""
        getattr(session.channels[channels], method)()  # get method by name then invoke it

    @pytest.mark.resource_name('Dev1/0:3, Dev2/0:3')
    @pytest.mark.parametrize(
        'channels',
        [
            'Dev1/0',
            'Dev1/0-3',
            'Dev2/0',
            'Dev2/0:3',
            'Dev1/0,Dev2/0',
            'Dev1/0:1,Dev2/2-3',
            'Dev1/3,Dev2/0-3'
        ]
    )
    def test_send_software_edge_trigger_repeated_capabilities(self, session, channels):
        channels_session = session.channels[channels]
        channels_session.initiate()
        channels_session.send_software_edge_trigger(nidcpower.SendSoftwareEdgeTriggerType.START)

    @pytest.mark.resource_name('Dev1/0:3, Dev2/0:3')
    @pytest.mark.parametrize(
        'channels',
        [
            'Dev1/0',
            'Dev1/0-3',
            'Dev2/0',
            'Dev2/0:3',
            'Dev1/0,Dev2/0',
            'Dev1/0:1,Dev2/2-3',
            'Dev1/3,Dev2/0-3'
        ]
    )
    def test_wait_for_event_repeated_capabilities(self, session, channels):
        channels_session = session.channels[channels]
        with channels_session.initiate():
            channels_session.wait_for_event(nidcpower.Event.SOURCE_COMPLETE)

    @pytest.mark.resource_name("4190/0")
    @pytest.mark.options("Simulate=1, DriverSetup=Model:4190; BoardType:PXIe")
    def test_fetch_multiple_lcr(self, session):
        session.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE
        session.instrument_mode = nidcpower.InstrumentMode.LCR
        session.lcr_stimulus_function = nidcpower.LCRStimulusFunction.VOLTAGE
        session.lcr_voltage_amplitude = 0.7
        session.lcr_frequency = 10_000.0
        session.lcr_dc_bias_source = nidcpower.LCRDCBiasSource.VOLTAGE
        session.lcr_dc_bias_voltage_level = 1.0
        count = 3
        with session.initiate():
            measurements = session.fetch_multiple_lcr(count)
            assert len(measurements) == count
            for measurement in measurements:
                assert measurement.vdc == pytest.approx(session.lcr_dc_bias_voltage_level, 1e-9)
                assert measurement.stimulus_frequency == pytest.approx(session.lcr_frequency, 1e-9)
                assert measurement.ac_voltage.real == pytest.approx(session.lcr_voltage_amplitude, 1e-9)
                assert measurement.ac_voltage.imag == pytest.approx(0.0, 1e-9)
                assert measurement.measurement_mode == nidcpower.InstrumentMode.LCR
                assert not measurement.dc_in_compliance
                assert not measurement.ac_in_compliance
                assert not measurement.unbalanced

    @pytest.mark.resource_name("4190/0")
    @pytest.mark.options("Simulate=1, DriverSetup=Model:4190; BoardType:PXIe")
    def test_measure_multiple_lcr(self, session):
        session.instrument_mode = nidcpower.InstrumentMode.LCR
        session.lcr_stimulus_function = nidcpower.LCRStimulusFunction.CURRENT
        session.lcr_current_amplitude = 700.0e-6
        session.lcr_frequency = 10_000.0
        session.lcr_dc_bias_source = nidcpower.LCRDCBiasSource.CURRENT
        session.lcr_dc_bias_current_level = 1.0e-6
        with session.initiate():
            measurements = session.measure_multiple_lcr()
            assert measurements[0].idc == pytest.approx(session.lcr_dc_bias_current_level, 1e-9)
            assert measurements[0].stimulus_frequency == pytest.approx(session.lcr_frequency, 1e-9)
            assert measurements[0].ac_current.real == pytest.approx(session.lcr_current_amplitude, 1e-9)
            assert measurements[0].ac_current.imag == pytest.approx(0.0, 1e-9)
            assert measurements[0].measurement_mode == nidcpower.InstrumentMode.LCR
            assert not measurements[0].dc_in_compliance
            assert not measurements[0].ac_in_compliance
            assert not measurements[0].unbalanced

    @pytest.mark.parametrize(
        'resource_name,channels,independent_channels,measurement_channels,expected_measured_channel',
        [
            ('Dev1', None, False, None, '0'),
            ('Dev1', '', False, '', '0'),
            ('Dev1', ' ', False, ' ', '0'),
            (' Dev1 ', ' 0 ', False, ' 0 ', '0'),
            ('Dev1', None, True, None, 'Dev1/0'),
            ('Dev1', '', True, '', 'Dev1/0'),
            ('Dev1', ' ', True, ' ', 'Dev1/0'),
            ('Dev1', '0', True, '0', 'Dev1/0'),
            ('Dev1', 'Dev1/0', True, 'Dev1/0', 'Dev1/0'),
            ('Dev1/0', '', True, None, 'Dev1/0'),
            ('Dev1/0', ' ', True, ' ', 'Dev1/0'),
            ('  DEV1 / 0  ', ' ', True, ' dev1  /  0 ', 'DEV1/0'),
        ]
    )
    def test_fetch_multiple_lcr_channels(
        self,
        session_creation_kwargs,
        resource_name,
        channels,
        independent_channels,
        measurement_channels,
        expected_measured_channel
    ):
        options = {'Simulate': True, 'DriverSetup': {'Model': '4190', 'BoardType': 'PXIe'}}
        with nidcpower.Session(
            resource_name,
            channels,
            options=options,
            independent_channels=independent_channels,
            **session_creation_kwargs
        ) as session:
            session.instrument_mode = nidcpower.InstrumentMode.LCR
            session.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE
            count = 10
            with session.initiate():
                if measurement_channels is None:
                    lcr_measurements = session.fetch_multiple_lcr(count)
                else:
                    lcr_measurements = session.channels[measurement_channels].fetch_multiple_lcr(count)
                assert len(lcr_measurements) == count
                for lcr_measurement_object in lcr_measurements:
                    assert lcr_measurement_object.channel == expected_measured_channel

    @pytest.mark.parametrize(
        'resource_name,channels,independent_channels,measurement_channels,expected_measured_channels',
        [
            ('Dev1', None, False, None, ['0']),
            ('Dev1', '', False, '', ['0']),
            ('Dev1', ' ', False, ' ', ['0']),
            (' DEV1 ', ' 0 ', False, ' 0 ', ['0']),
            ('Dev1', None, True, None, ['Dev1/0']),
            ('Dev1', '', True, '', ['Dev1/0']),
            ('Dev1', ' ', True, ' ', ['Dev1/0']),
            ('Dev1', '0', True, 'Dev1/0', ['Dev1/0']),
            ('Dev1', 'Dev1/0', True, '0', ['Dev1/0']),
            ('Dev1/0', '', True, None, ['Dev1/0']),
            ('Dev1/0', ' ', True, ' ', ['Dev1/0']),
            ('Dev1,Dev2', ' ', True, 'Dev2/0,Dev1/0', ['Dev2/0', 'Dev1/0']),
            (' DEV1 / 0 , dev2 / 0 ', ' ', True, 'dev1  /0,DEV2/  0', ['DEV1/0', 'dev2/0']),
        ]
    )
    def test_measure_multiple_lcr_channels(
        self,
        session_creation_kwargs,
        resource_name,
        channels,
        independent_channels,
        measurement_channels,
        expected_measured_channels
    ):
        options = {'Simulate': True, 'DriverSetup': {'Model': '4190', 'BoardType': 'PXIe'}}
        with nidcpower.Session(
            resource_name,
            channels,
            options=options,
            independent_channels=independent_channels,
            **session_creation_kwargs
        ) as session:
            session.instrument_mode = nidcpower.InstrumentMode.LCR
            with session.initiate():
                if measurement_channels is None:
                    lcr_measurements = session.measure_multiple_lcr()
                else:
                    lcr_measurements = session.channels[measurement_channels].measure_multiple_lcr()
                assert [
                    lcr_measurement_object.channel for lcr_measurement_object in lcr_measurements
                ] == expected_measured_channels

    @pytest.mark.resource_name("4190/0")
    @pytest.mark.options("Simulate=1, DriverSetup=Model:4190; BoardType:PXIe")
    @pytest.mark.parametrize("additional_frequencies", [None, [], [9_000.0, 12_345.0, 12_346.0]])
    def test_perform_lcr_open_compensation(self, session, additional_frequencies):
        if additional_frequencies is None:
            nidcpower.Session.perform_lcr_open_compensation(session)
        else:
            nidcpower.Session.perform_lcr_open_compensation(session, additional_frequencies)

    @pytest.mark.resource_name("4190/0")
    @pytest.mark.options("Simulate=1, DriverSetup=Model:4190; BoardType:PXIe")
    @pytest.mark.parametrize("additional_frequencies", [None, [], [9_000.0, 12_345.0, 12_346.0]])
    def test_perform_lcr_short_compensation(self, session, additional_frequencies):
        if additional_frequencies is None:
            nidcpower.Session.perform_lcr_short_compensation(session)
        else:
            nidcpower.Session.perform_lcr_short_compensation(session, additional_frequencies)

    @pytest.mark.resource_name("4190/0")
    @pytest.mark.options("Simulate=1, DriverSetup=Model:4190; BoardType:PXIe")
    def test_perform_lcr_load_compensation(self, session):
        session.perform_lcr_load_compensation(
            [
                nidcpower.LCRLoadCompensationSpot(
                    frequency=100_000.0,
                    reference_value_type=nidcpower.LCRReferenceValueType.IMPEDANCE,
                    reference_value=complex(100.0, 1000.0)
                ),
                nidcpower.LCRLoadCompensationSpot(
                    frequency=200_000.0,
                    reference_value_type=nidcpower.LCRReferenceValueType.IDEAL_CAPACITANCE,
                    reference_value=300.0e-9
                ),
                nidcpower.LCRLoadCompensationSpot(
                    frequency=300_000.0,
                    reference_value_type=nidcpower.LCRReferenceValueType.IDEAL_INDUCTANCE,
                    reference_value=400.0e-6
                ),
                nidcpower.LCRLoadCompensationSpot(
                    frequency=400_000.0,
                    reference_value_type=nidcpower.LCRReferenceValueType.IDEAL_RESISTANCE,
                    reference_value=200.0
                )
            ]
        )

    @pytest.mark.resource_name("4190/0")
    @pytest.mark.options("Simulate=1, DriverSetup=Model:4190; BoardType:PXIe")
    @pytest.mark.parametrize(
        "compensation_function",
        [
            nidcpower.Session.perform_lcr_open_custom_cable_compensation,
            nidcpower.Session.perform_lcr_short_custom_cable_compensation,
        ],
    )
    def test_perform_lcr_open_short_custom_cable_compensation(self, session, compensation_function):
        compensation_function(session)

    @pytest.mark.resource_name("4190/0")
    @pytest.mark.options("Simulate=1, DriverSetup=Model:4190; BoardType:PXIe")
    def test_lcr_custom_cable_compensation_data(self, session):
        compensation_data = session.get_lcr_custom_cable_compensation_data()
        session.configure_lcr_custom_cable_compensation(compensation_data)

        session.configure_lcr_custom_cable_compensation(list(compensation_data))

        session.configure_lcr_custom_cable_compensation(bytes(compensation_data))

        with tempfile.NamedTemporaryFile(suffix='.bin', delete=False) as temp_file:
            temp_file.write(compensation_data)
        with open(temp_file.name, 'rb') as reopened_temp_file:
            compensation_data_bytes_from_file = reopened_temp_file.read()
        session.configure_lcr_custom_cable_compensation(compensation_data_bytes_from_file)

    @pytest.mark.resource_name("4190/0")
    @pytest.mark.options("Simulate=1, DriverSetup=Model:4190; BoardType:PXIe")
    @pytest.mark.parametrize(
        "compensation_type",
        [
            nidcpower.LCRCompensationType.OPEN_CUSTOM_CABLE,
            nidcpower.LCRCompensationType.SHORT_CUSTOM_CABLE,
            nidcpower.LCRCompensationType.OPEN,
            nidcpower.LCRCompensationType.SHORT,
            nidcpower.LCRCompensationType.LOAD,
        ],
    )
    def test_get_lcr_compensation_last_date_and_time(self, session, compensation_type):
        last_compensation_datetime = session.get_lcr_compensation_last_date_and_time(compensation_type)
        assert last_compensation_datetime.year == 1940
        assert last_compensation_datetime.month == 3
        assert last_compensation_datetime.day == 1
        assert last_compensation_datetime.hour == 0
        assert last_compensation_datetime.minute == 0

    # Multi-Threading tests
    def test_multi_threading_lock_unlock(self, session):
        system_test_utilities.impl_test_multi_threading_lock_unlock(session)

    def test_multi_threading_ivi_synchronized_wrapper_releases_lock(self, session):
        system_test_utilities.impl_test_multi_threading_ivi_synchronized_wrapper_releases_lock(
            session.abort)


class TestLibrary(SystemTests):
    @pytest.fixture(scope='class')
    def session_creation_kwargs(self):
        return {}

    @pytest.mark.resource_name("4190/0")
    @pytest.mark.options("Simulate=1, DriverSetup=Model:4190; BoardType:PXIe")
    def test_lcr_compensation_data(self, session):
        compensation_data = session.get_lcr_compensation_data()
        session.configure_lcr_compensation(compensation_data)

        session.configure_lcr_compensation(compensation_data.decode())

        session.configure_lcr_compensation(list(compensation_data))

        session.configure_lcr_compensation(bytes(compensation_data))

        with tempfile.NamedTemporaryFile(suffix='.bin', delete=False) as temp_file:
            temp_file.write(compensation_data)
        with open(temp_file.name, 'rb') as reopened_temp_file:
            compensation_data_bytes_from_file = reopened_temp_file.read()
        session.configure_lcr_compensation(compensation_data_bytes_from_file)


class TestGrpc(SystemTests):
    @pytest.fixture(scope='class')
    def grpc_channel(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        config_file_path = os.path.join(current_directory, 'grpc_server_config.json')
        with system_test_utilities.GrpcServerProcess(config_file_path) as proc:
            channel = grpc.insecure_channel(f"localhost:{proc.server_port}")
            yield channel

    @pytest.fixture(scope='class')
    def session_creation_kwargs(self, grpc_channel):
        grpc_options = nidcpower.GrpcSessionOptions(grpc_channel, "")
        return {'grpc_options': grpc_options}

    def test_get_lcr_compensation_data(self, session):
        with pytest.raises(NotImplementedError) as exc_info:
            session.get_lcr_compensation_data()
        assert exc_info.value.args[0] == 'get_lcr_compensation_data is not supported over gRPC'
        assert str(exc_info.value) == 'get_lcr_compensation_data is not supported over gRPC'

    def test_configure_lcr_compensation(self, session):
        with pytest.raises(NotImplementedError) as exc_info:
            session.configure_lcr_compensation([])
        assert exc_info.value.args[0] == 'configure_lcr_compensation is not supported over gRPC'
        assert str(exc_info.value) == 'configure_lcr_compensation is not supported over gRPC'
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidcpower/templates/session.py/fancy_advanced_sequence.py.mako sha256=d59b95b6588fba4d9daabf791e890c4bc832b788dbd70f1cab6370dd0bbc0584 bytes=1498 -->
## FILE: src/nidcpower/templates/session.py/fancy_advanced_sequence.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nidcpower/templates/session.py/fancy_advanced_sequence.py.mako`
- sha256: `d59b95b6588fba4d9daabf791e890c4bc832b788dbd70f1cab6370dd0bbc0584`
- bytes: 1498

````mako
<%page args="f, config, method_template"/>\
<%
    '''Implements Fancy Advanced Sequence'''
    import build.helper as helper

    suffix = method_template['method_python_name_suffix']

    # precalculate some lists
    attrs = helper.filter_codegen_attributes(config['attributes'])
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        # The way the NI-DCPower C API is designed, we need to know all the attribute ID's upfront in order to call
        # `niDCPower_CreateAdvancedSequence`. In order to find the attribute ID of each property, we look at the
        # member Attribute objects of Session. We use a set since we don't have to worry about is it already there.
        attribute_ids_used = set()
        for prop in property_names:
            if prop not in Session.__base__.__dict__:
                raise KeyError('{} is not an property on the nidcpower.Session'.format(prop))
            if not isinstance(Session.__base__.__dict__[prop], _attributes.Attribute):
                raise TypeError('{} is not a valid property: {}'.format(prop, type(Session.__base__.__dict__[prop])))
            attribute_ids_used.add(Session.__base__.__dict__[prop]._attribute_id)

        self._create_advanced_sequence_with_channels(sequence_name, list(attribute_ids_used), set_as_active_sequence)
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidcpower/templates/session.py/fancy_fetch_measure.py.mako sha256=8bc7822d89a34dc1f4ef3a5da69ce79e375fd73a432befd5edc6a880f1dedd05 bytes=2607 -->
## FILE: src/nidcpower/templates/session.py/fancy_fetch_measure.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nidcpower/templates/session.py/fancy_fetch_measure.py.mako`
- sha256: `8bc7822d89a34dc1f4ef3a5da69ce79e375fd73a432befd5edc6a880f1dedd05`
- bytes: 2607

````mako
<%page args="f, config, method_template"/>\
<%
    '''Forwards to _fetch_multiple() with a nicer interface'''
    import build.helper as helper

    suffix = method_template['method_python_name_suffix']

    # We explicitly only support fetch_multiple and measure_multiple
    if f['python_name'] == 'fetch_multiple':
        param_list = 'timeout, count'
        in_compliances_return = ', in_compliances'
        in_compliance_unpack = ', in_compliance'
        in_compliance_value = 'in_compliance'
        channel_names_zipped = ''
        channel_name_unpack = ''
        channel_name_value = 'channel_names[0]'
    elif f['python_name'] == 'measure_multiple':
        param_list = ''
        in_compliances_return = ''
        in_compliance_unpack = ''
        in_compliance_value = 'None'
        channel_names_zipped = ', channel_names'
        channel_name_unpack = ', channel_name'
        channel_name_value = 'channel_name'
    else:
        raise ValueError('Only fetch_multiple and measure_multiple are supported. Got {}'.format(f['python_name']))
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        import collections
        Measurement = collections.namedtuple('Measurement', ['voltage', 'current', 'in_compliance', 'channel'])

        voltage_measurements, current_measurements${in_compliances_return} = self._${f['python_name']}(${param_list})

        channel_names = _converters.expand_channel_string(
            self._repeated_capability,
            self._all_channels_in_session
        )
%if f['python_name'] == 'fetch_multiple':
        assert len(channel_names) == 1, "fetch_multiple only supports one channel at a time"
%elif f['python_name'] == 'measure_multiple':
        assert (
            len(channel_names) == len(voltage_measurements) and len(channel_names) == len(current_measurements)
        ), "measure_multiple should return as many voltage and current measurements as the number of channels specified through the channel string"
%endif
        return [
            Measurement(
                voltage=voltage,
                current=current,
                in_compliance=${in_compliance_value},
                channel=${channel_name_value}
            ) for voltage, current${in_compliance_unpack}${channel_name_unpack} in zip(
                voltage_measurements, current_measurements${in_compliances_return}${channel_names_zipped}
            )
        ]
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidcpower/templates/session.py/fancy_fetch_measure_lcr.py.mako sha256=9160da0f5573995043054d1813d659b8e3d5f260f85a1d3363c06b4371e3cb4a bytes=2019 -->
## FILE: src/nidcpower/templates/session.py/fancy_fetch_measure_lcr.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nidcpower/templates/session.py/fancy_fetch_measure_lcr.py.mako`
- sha256: `9160da0f5573995043054d1813d659b8e3d5f260f85a1d3363c06b4371e3cb4a`
- bytes: 2019

````mako
<%page args="f, config, method_template"/>\
<%
    '''Forwards to _fetch_multiple_lcr() and _measure_multiple_lcr(), then populate the `channel`
    field of the returned LCRMeasurement objects.
    '''
    import build.helper as helper

    suffix = method_template['method_python_name_suffix']

    # We explicitly only support fetch_multiple_lcr and measure_multiple_lcr
    if f['python_name'] == 'fetch_multiple_lcr':
        param_list = 'count, timeout'
        channel_names_zipped = ''
        channel_name_unpack = ''
        channel_name_value = 'channel_names[0]'
    elif f['python_name'] == 'measure_multiple_lcr':
        param_list = ''
        channel_names_zipped = ', channel_names'
        channel_name_unpack = ' channel_name'
        channel_name_value = 'channel_name'
    else:
        raise ValueError(
            f"Only fetch_multiple_lcr and measure_multiple_lcr are supported. Got {f['python_name']}"
        )
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        lcr_measurements = self._${f['python_name']}(${param_list})

        channel_names = _converters.expand_channel_string(
            self._repeated_capability,
            self._all_channels_in_session
        )
%if f['python_name'] == 'fetch_multiple_lcr':
        assert len(channel_names) == 1, "fetch_multiple_lcr only supports one channel at a time"
%elif f['python_name'] == 'measure_multiple_lcr':
        assert len(channel_names) == len(lcr_measurements), (
            "measure_multiple_lcr should return as many LCR measurements as the number of channels specified through the channel string"
        )
%endif
        for lcr_measurement_object,${channel_name_unpack} in zip(lcr_measurements${channel_names_zipped}):
            lcr_measurement_object.channel = ${channel_name_value}
        return lcr_measurements
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidcpower/templates/session.py/fancy_initialize.py.mako sha256=b13ea42385db9e75996412aceb073c7d2044e9e071725792db965294383ea084 bytes=2289 -->
## FILE: src/nidcpower/templates/session.py/fancy_initialize.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nidcpower/templates/session.py/fancy_initialize.py.mako`
- sha256: `b13ea42385db9e75996412aceb073c7d2044e9e071725792db965294383ea084`
- bytes: 2289

````mako
<%page args="f, config, method_template"/>\
<%
    '''Dispatches to the proper initialize method based on input parameters.'''
    import build.helper as helper

    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        if independent_channels:
            resource_string = resource_name  # store potential modifications to resource_name in a separate variable

            if channels:
                # if we have a channels arg, we need to try and combine it with the resource name
                # before calling into initialize with independent channels
                channel_list = (resource_name + "/" + channel for channel in channels.split(","))
                resource_string = ",".join(channel_list)

                import warnings
                warnings.warn(
                    "Attempting to initialize an independent channels session with a channels argument. The resource "
                    "name '" + resource_name + "' will be combined with the channels '" + channels + "' to form the "
                    "fully-qualified channel list '" + resource_string + "'. To avoid this warning, use a "
                    "fully-qualified channel list as the resource name instead of providing a channels argument.",
                    DeprecationWarning
                )

                if "," in resource_name:
                    raise ValueError(
                        "Channels cannot be combined with multiple instruments in the resource name '" + resource_name + "'. "
                        "Specify a list of fully-qualified channels as the resource name instead of supplying a "
                        "channels argument."
                    )

            return self._initialize_with_independent_channels(resource_string, reset, option_string)

        else:
            import warnings
            warnings.warn("Initializing session without independent channels enabled.", DeprecationWarning)

            return self._initialize_with_channels(resource_name, channels, reset, option_string)
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidcpower/unit_tests/test_nidcpower.py sha256=32baf6ad91b702f6b890098126c8c10796886a78be8180a5a2815317e9311dda bytes=13216 -->
## FILE: src/nidcpower/unit_tests/test_nidcpower.py

- repository: `ni/nimi-python`
- source_path: `src/nidcpower/unit_tests/test_nidcpower.py`
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

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/custom_types/history_ram_cycle_information.py sha256=03ca3bbe111135f4dda85bd70e50dae85821a13699a7998e72bc67f4724f61f2 bytes=2800 -->
## FILE: src/nidigital/custom_types/history_ram_cycle_information.py

- repository: `ni/nimi-python`
- source_path: `src/nidigital/custom_types/history_ram_cycle_information.py`
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

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/examples/burst_with_start_trigger/burst_with_start_trigger.digiproj sha256=724b25f235104f9785bc9f0f2f34fd37291da31f4521065c485acacef4ec71f1 bytes=3412 -->
## FILE: src/nidigital/examples/burst_with_start_trigger/burst_with_start_trigger.digiproj

- repository: `ni/nimi-python`
- source_path: `src/nidigital/examples/burst_with_start_trigger/burst_with_start_trigger.digiproj`
- sha256: `724b25f235104f9785bc9f0f2f34fd37291da31f4521065c485acacef4ec71f1`
- bytes: 3412

````text
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="31A6CD0BA6EF37ABFC895A8EB773D750" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="5.3.1.49912" FeatureSetName="Digital Pattern Editor" Name="http://www.ni.com/PatternBasedDigital" OldestCompatibleVersion="4.5.0.0" Version="4.6.0.49152" />
		<ParsableNamespace AssemblyFileVersion="5.3.1.49912" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="5.2.0.49153" Version="5.2.0.49153" />
		<ApplicationVersionInfo Build="5.3.1.49912" Name="Digital Pattern Editor" Version="19.0.0" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<ProjectSettings Id="1" ModelDefinitionType="ProjectSettings" Name="ZProjectSettings" />
		<EmbeddedDefinitionReference Id="2" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="3" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<FileReference Id="14" ModelDefinitionType="DigitalPatternEditor.PatternDefinition" Name="Pattern\.digipat" StoragePath="Pattern.digipat" />
			<FileReference Id="15" ModelDefinitionType="PinLevelsDefinition" Name="PinLevels\.digilevels" StoragePath="PinLevels.digilevels" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="17" ModelDefinitionType="SpecificationsDefinition" Name="Specifications\.specs" StoragePath="Specifications.specs" />
			<FileReference Id="18" ModelDefinitionType="PinMap" Name="PinMap\.pinmap" StoragePath="PinMap.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="19" ModelDefinitionType="TimingDefinition" Name="Timing\.digitiming" StoragePath="Timing.digitiming" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<EmbeddedDefinitionReference Id="20" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}CaptureResultsDefinition" Name="CaptureResults">
				<CaptureResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="22" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}BurstResultsDefinition" Name="BurstResults">
				<BurstResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="24" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}SystemInfoDefinition" Name="SystemInfo">
				<SystemInfoDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="25" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}DigitalScopeDefinition" Name="DigitalScope">
				<DigitalScopeDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
		</NameScopingEnvoy>
		<EmbeddedDefinitionReference Id="7" ModelDefinitionType="DigitalPatternEditor.ProjectPropertiesDefinition" Name="ProjectProperties">
			<ProjectPropertiesDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
		</EmbeddedDefinitionReference>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/examples/burst_with_start_trigger/nidigital_burst_with_start_trigger.py sha256=9ff318b5853307438a830c38c1e5e44831babb5e93d93d5584c02728dc27fd6a bytes=4126 -->
## FILE: src/nidigital/examples/burst_with_start_trigger/nidigital_burst_with_start_trigger.py

- repository: `ni/nimi-python`
- source_path: `src/nidigital/examples/burst_with_start_trigger/nidigital_burst_with_start_trigger.py`
- sha256: `9ff318b5853307438a830c38c1e5e44831babb5e93d93d5584c02728dc27fd6a`
- bytes: 4126

````python
#!/usr/bin/python

import argparse
import nidigital
import os
import sys


def example(resource_name, options, trigger_source=None, trigger_edge=None):

    with nidigital.Session(resource_name=resource_name, options=options) as session:

        dir = os.path.join(os.path.dirname(__file__))

        # Load the pin map (.pinmap) created using the Digital Pattern Editor
        pin_map_filename = os.path.join(dir, 'PinMap.pinmap')
        session.load_pin_map(pin_map_filename)

        # Load the specifications (.specs), levels (.digilevels), and timing (.digitiming) sheets created using the Digital Pattern Editor
        spec_filename = os.path.join(dir, 'Specifications.specs')
        levels_filename = os.path.join(dir, 'PinLevels.digilevels')
        timing_filename = os.path.join(dir, 'Timing.digitiming')
        session.load_specifications_levels_and_timing(spec_filename, levels_filename, timing_filename)

        # Apply the settings from the levels and timing sheets we just loaded to the session
        session.apply_levels_and_timing(levels_filename, timing_filename)

        # Loading the pattern file (.digipat) created using the Digital Pattern Editor
        pattern_filename = os.path.join(dir, 'Pattern.digipat')
        session.load_pattern(pattern_filename)

        if trigger_source is None:
            print('Start bursting pattern')
        else:
            # Specify a source and edge for the external start trigger
            session.start_trigger_type = nidigital.TriggerType.DIGITAL_EDGE
            session.digital_edge_start_trigger_source = trigger_source
            session.digital_edge_start_trigger_edge = nidigital.DigitalEdge.RISING if trigger_edge == 'Rising' else nidigital.DigitalEdge.FALLING
            print('Wait for start trigger and then start bursting pattern')

        # If start trigger is configured, waiting for the trigger to start bursting and then blocks until the pattern is done bursting
        # Else just start bursting and block until the pattern is done bursting
        session.burst_pattern(start_label='new_pattern')

        # Disconnect all channels using programmable onboard switching
        session.selected_function = nidigital.SelectedFunction.DISCONNECT
    print('Done bursting pattern')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Demonstrates how to create and configure a session that bursts a pattern on the digital pattern instrument using a start trigger', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2,PXI1Slot3', help='Resource name of a NI digital pattern instrument. Ensure the resource name matches the instrument name in the pinmap file.')
    parser.add_argument('-s', '--simulate', default='True', choices=['True', 'False'], help='Whether to run on simulated hardware or real hardware')
    subparser = parser.add_subparsers(dest='command', help='Sub-command help')
    start_trigger = subparser.add_parser('start-trigger', help='Configure start trigger')
    start_trigger.add_argument('-ts', '--trigger-source', default='/PXI1Slot2/PXI_Trig0', help='Source terminal for the start trigger')
    start_trigger.add_argument('-te', '--trigger-edge', default='Rising', choices=['Rising', 'Falling'], help='Trigger on rising edge or falling edge of start trigger')
    args = parser.parse_args(argsv)

    example(args.resource_name,
            'Simulate=1, DriverSetup=Model:6571' if args.simulate == 'True' else '',
            args.trigger_source if args.command == 'start-trigger' else None,
            args.trigger_edge if args.command == 'start-trigger' else None)


def main():
    _main(sys.argv[1:])


def test_main():
    _main([])
    _main(['start-trigger'])


def test_example():
    resource_name = 'PXI1Slot2,PXI1Slot3'
    options = {'simulate': True, 'driver_setup': {'Model': '6571'}, }
    example(resource_name, options)

    trigger_source = '/PXI1Slot2/PXI_Trig0'
    trigger_edge = 'Rising'
    example(resource_name, options, trigger_source, trigger_edge)


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/examples/burst_with_start_trigger/PinLevels.digilevels sha256=2748b207cbe7a8100f12e37d142219367486c7b1f8fc379f0471639ae96c4a4d bytes=579 -->
## FILE: src/nidigital/examples/burst_with_start_trigger/PinLevels.digilevels

- repository: `ni/nimi-python`
- source_path: `src/nidigital/examples/burst_with_start_trigger/PinLevels.digilevels`
- sha256: `2748b207cbe7a8100f12e37d142219367486c7b1f8fc379f0471639ae96c4a4d`
- bytes: 579

````text
<?xml version="1.0" encoding="utf-8"?>
<PinLevelsFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/PinLevels">
  <PinLevelsSheet>
    <DigitalPinLevelSets>
      <DigitalPinLevelSet pin="PinGroup1">
        <Vil>0</Vil>
        <Vih>3.3</Vih>
        <Vol>0.8</Vol>
        <Voh>2</Voh>
        <Vterm>0</Vterm>
        <TerminationMode>HighZ</TerminationMode>
      </DigitalPinLevelSet>
    </DigitalPinLevelSets>
  </PinLevelsSheet>
</PinLevelsFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/examples/burst_with_start_trigger/PinMap.pinmap sha256=2540d59e92fe6244268ddbdffe7646bafec6eb4e2f0b7ab5ded1891ce02a3245 bytes=2439 -->
## FILE: src/nidigital/examples/burst_with_start_trigger/PinMap.pinmap

- repository: `ni/nimi-python`
- source_path: `src/nidigital/examples/burst_with_start_trigger/PinMap.pinmap`
- sha256: `2540d59e92fe6244268ddbdffe7646bafec6eb4e2f0b7ab5ded1891ce02a3245`
- bytes: 2439

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.5">
	<Instruments>
		<NIDigitalPatternInstrument name="PXI1Slot2" numberOfChannels="32" group="Digital"/>
		<NIDigitalPatternInstrument name="PXI1Slot3" numberOfChannels="32" group="Digital" />
	</Instruments>
	<Pins>
		<DUTPin name="DUTPin1" />
		<DUTPin name="DUTPin2" />
		<DUTPin name="DUTPin3" />
		<DUTPin name="DUTPin4" />
		<DUTPin name="DUTPin5" />
		<DUTPin name="DUTPin6" />
		<DUTPin name="DUTPin7" />
		<DUTPin name="DUTPin8" />
	</Pins>
	<PinGroups>
		<PinGroup name="PinGroup1">
			<PinReference pin="DUTPin1" />
			<PinReference pin="DUTPin2" />
			<PinReference pin="DUTPin3" />
			<PinReference pin="DUTPin4" />
			<PinReference pin="DUTPin5" />
			<PinReference pin="DUTPin6" />
			<PinReference pin="DUTPin7" />
			<PinReference pin="DUTPin8" />
		</PinGroup>
	</PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="DUTPin1" siteNumber="0" instrument="PXI1Slot2" channel="0" />
		<Connection pin="DUTPin1" siteNumber="1" instrument="PXI1Slot3" channel="0" />
		<Connection pin="DUTPin2" siteNumber="0" instrument="PXI1Slot2" channel="1" />
		<Connection pin="DUTPin2" siteNumber="1" instrument="PXI1Slot3" channel="1" />
		<Connection pin="DUTPin3" siteNumber="0" instrument="PXI1Slot2" channel="2" />
		<Connection pin="DUTPin3" siteNumber="1" instrument="PXI1Slot3" channel="2" />
		<Connection pin="DUTPin4" siteNumber="0" instrument="PXI1Slot2" channel="3" />
		<Connection pin="DUTPin4" siteNumber="1" instrument="PXI1Slot3" channel="3" />
		<Connection pin="DUTPin5" siteNumber="0" instrument="PXI1Slot2" channel="4" />
		<Connection pin="DUTPin5" siteNumber="1" instrument="PXI1Slot3" channel="4" />
		<Connection pin="DUTPin6" siteNumber="0" instrument="PXI1Slot2" channel="5" />
		<Connection pin="DUTPin6" siteNumber="1" instrument="PXI1Slot3" channel="5" />
		<Connection pin="DUTPin7" siteNumber="0" instrument="PXI1Slot2" channel="6" />
		<Connection pin="DUTPin7" siteNumber="1" instrument="PXI1Slot3" channel="6" />
		<Connection pin="DUTPin8" siteNumber="0" instrument="PXI1Slot2" channel="7" />
		<Connection pin="DUTPin8" siteNumber="1" instrument="PXI1Slot3" channel="7" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/examples/burst_with_start_trigger/Specifications.specs sha256=82fcd2afa60bd93a85a9e0d1c43a4b074a33d9be0c8ab8c482e71eebb290a80a bytes=377 -->
## FILE: src/nidigital/examples/burst_with_start_trigger/Specifications.specs

- repository: `ni/nimi-python`
- source_path: `src/nidigital/examples/burst_with_start_trigger/Specifications.specs`
- sha256: `82fcd2afa60bd93a85a9e0d1c43a4b074a33d9be0c8ab8c482e71eebb290a80a`
- bytes: 377

````text
<?xml version="1.0" encoding="utf-8"?>
<Specifications xmlns:f="http://www.ni.com/schemas/Semiconductor/Formula.xsd" schemaVersion="1.0" xmlns="http://www.ni.com/schemas/Semiconductor/Specifications.xsd">
  <Section name="timing">
    <f:Formula symbol="period">
      <f:Definition>1 µs</f:Definition>
    </f:Formula>
  </Section>
  <Description />
</Specifications>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/examples/burst_with_start_trigger/Timing.digitiming sha256=11f50499d9e80ba116299c58bdb5fe599cd3f92e74b9575ef7a7e93c7155eeb1 bytes=827 -->
## FILE: src/nidigital/examples/burst_with_start_trigger/Timing.digitiming

- repository: `ni/nimi-python`
- source_path: `src/nidigital/examples/burst_with_start_trigger/Timing.digitiming`
- sha256: `11f50499d9e80ba116299c58bdb5fe599cd3f92e74b9575ef7a7e93c7155eeb1`
- bytes: 827

````text
<?xml version="1.0" encoding="utf-8"?>
<TimingFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/Timing">
  <TimingSheet>
    <TimeSets>
      <TimeSet name="tset0">
        <Period>timing.period</Period>
        <PinEdges>
          <PinEdge pin="PinGroup1">
            <DriveNonReturn>
              <On>0 µs</On>
              <Data>timing.period / 2</Data>
              <Off>timing.period</Off>
            </DriveNonReturn>
            <CompareStrobe>
              <Strobe>(3 * timing.period) / 4</Strobe>
            </CompareStrobe>
            <DataSource>Pattern</DataSource>
          </PinEdge>
        </PinEdges>
      </TimeSet>
    </TimeSets>
  </TimingSheet>
</TimingFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/examples/configure_time_set_and_voltage_levels/configure_time_set_and_voltage_levels.digiproj sha256=8f7fb3b1219e3a4171c3aef0754573743ceb03940c199e5de77246099ba33566 bytes=2619 -->
## FILE: src/nidigital/examples/configure_time_set_and_voltage_levels/configure_time_set_and_voltage_levels.digiproj

- repository: `ni/nimi-python`
- source_path: `src/nidigital/examples/configure_time_set_and_voltage_levels/configure_time_set_and_voltage_levels.digiproj`
- sha256: `8f7fb3b1219e3a4171c3aef0754573743ceb03940c199e5de77246099ba33566`
- bytes: 2619

````text
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="93A640AB629B66E20E11447A06D18A4D" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="5.3.2.50247" FeatureSetName="Digital Pattern Editor" Name="http://www.ni.com/PatternBasedDigital" OldestCompatibleVersion="4.5.0.0" Version="5.3.1.49152" />
		<ParsableNamespace AssemblyFileVersion="5.3.2.50247" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="5.2.0.49153" Version="5.2.0.49153" />
		<ApplicationVersionInfo Build="5.3.2.50247" Name="Digital Pattern Editor" Version="20.6.0" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<ProjectSettings Id="1" ModelDefinitionType="ProjectSettings" Name="ZProjectSettings" />
		<EmbeddedDefinitionReference Id="2" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="3" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<FileReference Id="14" ModelDefinitionType="DigitalPatternEditor.PatternDefinition" Name="Pattern\.digipat" StoragePath="Pattern.digipat" />
			<FileReference Id="15" ModelDefinitionType="PinMap" Name="PinMap\.pinmap" StoragePath="PinMap.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<EmbeddedDefinitionReference Id="18" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}CaptureResultsDefinition" Name="CaptureResults">
				<CaptureResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="20" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}BurstResultsDefinition" Name="BurstResults">
				<BurstResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="23" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}DigitalScopeDefinition" Name="DigitalScope">
				<DigitalScopeDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
		</NameScopingEnvoy>
		<EmbeddedDefinitionReference Id="7" ModelDefinitionType="DigitalPatternEditor.ProjectPropertiesDefinition" Name="ProjectProperties">
			<ProjectPropertiesDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
		</EmbeddedDefinitionReference>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/examples/configure_time_set_and_voltage_levels/nidigital_configure_time_set_and_voltage_levels.py sha256=e2838d45dc9515ea31da6129a13967e6143ef1932af9be594717b06f86dfa08d bytes=8657 -->
## FILE: src/nidigital/examples/configure_time_set_and_voltage_levels/nidigital_configure_time_set_and_voltage_levels.py

- repository: `ni/nimi-python`
- source_path: `src/nidigital/examples/configure_time_set_and_voltage_levels/nidigital_configure_time_set_and_voltage_levels.py`
- sha256: `e2838d45dc9515ea31da6129a13967e6143ef1932af9be594717b06f86dfa08d`
- bytes: 8657

````python
#!/usr/bin/python

import argparse
import nidigital
import os
import sys


class VoltageLevelsAndTerminationConfig():
    def __init__(self, vil, vih, vol, voh, vterm, termination_mode, iol, ioh, vcom):
        self.vil = vil
        self.vih = vih
        self.vol = vol
        self.voh = voh
        self.vterm = vterm
        self.termination_mode = termination_mode
        self.iol = iol
        self.ioh = ioh
        self.vcom = vcom


class TimeSetConfig():
    def __init__(self, time_set_name, period, drive_format, drive_on, drive_data, drive_return, drive_off, strobe_edge):
        self.time_set_name = time_set_name
        self.period = period
        self.drive_format = drive_format
        self.drive_on = drive_on
        self.drive_data = drive_data
        self.drive_return = drive_return
        self.drive_off = drive_off
        self.strobe_edge = strobe_edge


def convert_drive_format(drive_format):
    converter = {'NR': nidigital.DriveFormat.NR,
                 'RL': nidigital.DriveFormat.RL,
                 'RH': nidigital.DriveFormat.RH,
                 'SBC': nidigital.DriveFormat.SBC}
    return converter.get(drive_format, None)


def example(resource_name,
            options,
            channels,
            voltage_config,
            time_set_config):

    with nidigital.Session(resource_name=resource_name, options=options) as session:

        dir = os.path.dirname(__file__)

        # Load pin map (.pinmap) created using Digital Pattern Editor
        pin_map_filename = os.path.join(dir, 'PinMap.pinmap')
        session.load_pin_map(pin_map_filename)

        # Configure voltage levels and terminal voltage through driver API
        session.channels[channels].configure_voltage_levels(voltage_config.vil, voltage_config.vih, voltage_config.vol, voltage_config.voh, voltage_config.vterm)
        if voltage_config.termination_mode == 'High_Z':
            session.channels[channels].termination_mode = nidigital.TerminationMode.HIGH_Z
        elif voltage_config.termination_mode == 'Active_Load':
            session.channels[channels].termination_mode = nidigital.TerminationMode.ACTIVE_LOAD
            session.channels[channels].configure_active_load_levels(voltage_config.iol, voltage_config.ioh, voltage_config.vcom)
        else:
            session.channels[channels].termination_mode = nidigital.TerminationMode.VTERM

        # Configure time set through driver API
        session.create_time_set(time_set_config.time_set_name)  # Must match time set name in pattern file
        session.configure_time_set_period(time_set_config.time_set_name, time_set_config.period)
        session.channels[channels].configure_time_set_drive_edges(time_set_config.time_set_name, convert_drive_format(time_set_config.drive_format),
                                                                  time_set_config.drive_on, time_set_config.drive_data,
                                                                  time_set_config.drive_return, time_set_config.drive_off)
        session.channels[channels].configure_time_set_compare_edges_strobe(time_set_config.time_set_name, time_set_config.strobe_edge)

        # Load the pattern file (.digipat) created using Digital Pattern Editor
        pattern_filename = os.path.join(dir, 'Pattern.digipat')
        session.load_pattern(pattern_filename)

        # Burst pattern, blocks until the pattern is done bursting
        session.burst_pattern(start_label='new_pattern')
        print('Start bursting pattern')

        # Disconnect all channels using programmable onboard switching
        session.selected_function = nidigital.SelectedFunction.DISCONNECT
    print('Done bursting pattern')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Demonstrates how to create an instrument session, configure time set and voltage levels, and burst a pattern on the digital pattern instrument.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2,PXI1Slot3', help='Resource name of a NI digital pattern instrument, ensure the resource name matches the instrument name in the pinmap file.')
    parser.add_argument('-s', '--simulate', default='True', choices=['True', 'False'], help='Whether to run on simulated hardware or on real hardware')
    parser.add_argument('-c', '--channels', default='PinGroup1', help='Channel(s)/Pin(s) to configure')

    # Parameters to configure voltage
    parser.add_argument('--vil', default=0, type=float, help='The voltage that the instrument will apply to the input of the DUT when the pin driver drives a logic low (0)')
    parser.add_argument('--vih', default=3.3, type=float, help='The voltage that the instrument will apply to the input of the DUT when the test instrument drives a logic high (1)')
    parser.add_argument('--vol', default=1.6, type=float, help='The output voltage below which the comparator on the pin driver interprets a logic low (L)')
    parser.add_argument('--voh', default=1.7, type=float, help='The output voltage above which the comparator on the pin driver interprets a logic high (H)')
    parser.add_argument('--vterm', default=2, type=float, help='The termination voltage the instrument applies during non-drive cycles when the termination mode is set to Vterm')
    parser.add_argument('-term-mode', '--termination-mode', default='High_Z', choices=['High_Z', 'Active_Load', 'Three_Level_Drive'])
    parser.add_argument('--iol', default=0.002, type=float, help='The maximum current that the DUT sinks while outputting a voltage below VCOM')
    parser.add_argument('--ioh', default=-0.002, type=float, help='The maximum current that the DUT sources while outputting a voltage above VCOM')
    parser.add_argument('--vcom', default=0.0, type=float, help='The commutating voltage level at which the active load circuit switches between sourcing current and sinking current')

    # Parameters to configure timeset
    parser.add_argument('--period', default=0.00000002, type=float, help='Period in second')
    parser.add_argument('-format', '--drive-format', default='NR', choices=['NR', 'RL', 'RH', 'SBC'], help='Non-return | Return to low | Return to high | Surround by complement')
    parser.add_argument('--drive-on', default=0, type=float, help='The delay in seconds from the beginning of the vector period for turning on the pin driver')
    parser.add_argument('--drive-data', default=0, type=float, help='The delay in seconds from the beginning of the vector period until the pattern data is driven to the pattern value')
    parser.add_argument('--drive-return', default=0.000000015, type=float, help='The delay in seconds from the beginning of the vector period until the pin changes from the pattern data to the return value, as specified in the format.')
    parser.add_argument('--drive-off', default=0.00000002, type=float, help='The delay in seconds from the beginning of the vector period to turn off the pin driver when the next vector period uses a non-drive symbol (L, H, X, V, M, E).')
    parser.add_argument('--strobe-edge', default=0.00000001, type=float, help='The time in second when the comparison happens within a vector period')

    args = parser.parse_args(argsv)
    voltage_config = VoltageLevelsAndTerminationConfig(args.vil, args.vih, args.vol, args.voh, args.vterm, args.termination_mode, args.iol, args.ioh, args.vcom)
    time_set_config = TimeSetConfig("tset0", args.period, args.drive_format, args.drive_on, args.drive_data, args.drive_return, args.drive_off, args.strobe_edge)
    example(args.resource_name,
            'Simulate=1, DriverSetup=Model:6571' if args.simulate == 'True' else '',
            args.channels,
            voltage_config,
            time_set_config)


def main():
    _main(sys.argv[1:])


def test_main():
    _main([])


def test_example():
    resource_name = 'PXI1Slot2,PXI1Slot3'
    options = {'simulate': True, 'driver_setup': {'Model': '6571'}, }
    channels = 'PinGroup1'
    voltage_config = VoltageLevelsAndTerminationConfig(vil=0, vih=3.3, vol=1.6, voh=1.7, vterm=2,
                                                       termination_mode='Active_Load', iol=0.002, ioh=-0.002, vcom=0)
    time_set_config = TimeSetConfig(time_set_name="tset0",
                                    period=0.00000002,
                                    drive_format='NR',
                                    drive_on=0, drive_data=0, drive_return=0.000000015, drive_off=0.00000002, strobe_edge=0.00000001)
    example(resource_name, options, channels, voltage_config, time_set_config)


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/examples/configure_time_set_and_voltage_levels/PinMap.pinmap sha256=e70a33458c25fe4b51334e31029487000f04a8b0c606b2f69fa31a631169f7d8 bytes=2440 -->
## FILE: src/nidigital/examples/configure_time_set_and_voltage_levels/PinMap.pinmap

- repository: `ni/nimi-python`
- source_path: `src/nidigital/examples/configure_time_set_and_voltage_levels/PinMap.pinmap`
- sha256: `e70a33458c25fe4b51334e31029487000f04a8b0c606b2f69fa31a631169f7d8`
- bytes: 2440

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.5">
	<Instruments>
		<NIDigitalPatternInstrument name="PXI1Slot2" numberOfChannels="32" group="Digital" />
		<NIDigitalPatternInstrument name="PXI1Slot3" numberOfChannels="32" group="Digital" />
	</Instruments>
	<Pins>
		<DUTPin name="DUTPin1" />
		<DUTPin name="DUTPin2" />
		<DUTPin name="DUTPin3" />
		<DUTPin name="DUTPin4" />
		<DUTPin name="DUTPin5" />
		<DUTPin name="DUTPin6" />
		<DUTPin name="DUTPin7" />
		<DUTPin name="DUTPin8" />
	</Pins>
	<PinGroups>
		<PinGroup name="PinGroup1">
			<PinReference pin="DUTPin1" />
			<PinReference pin="DUTPin2" />
			<PinReference pin="DUTPin3" />
			<PinReference pin="DUTPin4" />
			<PinReference pin="DUTPin5" />
			<PinReference pin="DUTPin6" />
			<PinReference pin="DUTPin7" />
			<PinReference pin="DUTPin8" />
		</PinGroup>
	</PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="DUTPin1" siteNumber="0" instrument="PXI1Slot2" channel="0" />
		<Connection pin="DUTPin1" siteNumber="1" instrument="PXI1Slot3" channel="0" />
		<Connection pin="DUTPin2" siteNumber="0" instrument="PXI1Slot2" channel="1" />
		<Connection pin="DUTPin2" siteNumber="1" instrument="PXI1Slot3" channel="1" />
		<Connection pin="DUTPin3" siteNumber="0" instrument="PXI1Slot2" channel="2" />
		<Connection pin="DUTPin3" siteNumber="1" instrument="PXI1Slot3" channel="2" />
		<Connection pin="DUTPin4" siteNumber="0" instrument="PXI1Slot2" channel="3" />
		<Connection pin="DUTPin4" siteNumber="1" instrument="PXI1Slot3" channel="3" />
		<Connection pin="DUTPin5" siteNumber="0" instrument="PXI1Slot2" channel="4" />
		<Connection pin="DUTPin5" siteNumber="1" instrument="PXI1Slot3" channel="4" />
		<Connection pin="DUTPin6" siteNumber="0" instrument="PXI1Slot2" channel="5" />
		<Connection pin="DUTPin6" siteNumber="1" instrument="PXI1Slot3" channel="5" />
		<Connection pin="DUTPin7" siteNumber="0" instrument="PXI1Slot2" channel="6" />
		<Connection pin="DUTPin7" siteNumber="1" instrument="PXI1Slot3" channel="6" />
		<Connection pin="DUTPin8" siteNumber="0" instrument="PXI1Slot2" channel="7" />
		<Connection pin="DUTPin8" siteNumber="1" instrument="PXI1Slot3" channel="7" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/examples/ppmu_source_and_measure/nidigital_ppmu_source_and_measure.py sha256=2c51a7598b2c1ebabcea0a3fb89ef2a37a5d746d4d1abf8d27793e245ef6a1c9 bytes=8471 -->
## FILE: src/nidigital/examples/ppmu_source_and_measure/nidigital_ppmu_source_and_measure.py

- repository: `ni/nimi-python`
- source_path: `src/nidigital/examples/ppmu_source_and_measure/nidigital_ppmu_source_and_measure.py`
- sha256: `2c51a7598b2c1ebabcea0a3fb89ef2a37a5d746d4d1abf8d27793e245ef6a1c9`
- bytes: 8471

````python
#!/usr/bin/python

import argparse
import nidigital
import os
import pytest
import sys
import time


def example(resource_name, options, channels, measure, aperture_time,
            source=None, settling_time=None, current_level_range=None, current_level=None,
            voltage_limit_high=None, voltage_limit_low=None, current_limit_range=None, voltage_level=None):

    with nidigital.Session(resource_name=resource_name, options=options) as session:

        dir = os.path.join(os.path.dirname(__file__))

        # Load pin map (.pinmap) created using Digital Pattern Editor
        pin_map_filename = os.path.join(dir, 'PinMap.pinmap')
        session.load_pin_map(pin_map_filename)

        # Configure the PPMU measurement aperture time
        session.channels[channels].ppmu_aperture_time = aperture_time
        session.channels[channels].ppmu_aperture_time_units = nidigital.PPMUApertureTimeUnits.SECONDS

        # Configure and source
        if source == 'source-current':
            session.channels[channels].ppmu_output_function = nidigital.PPMUOutputFunction.CURRENT

            session.channels[channels].ppmu_current_level_range = current_level_range
            session.channels[channels].ppmu_current_level = current_level
            session.channels[channels].ppmu_voltage_limit_high = voltage_limit_high
            session.channels[channels].ppmu_voltage_limit_low = voltage_limit_low

            session.channels[channels].ppmu_source()

            # Settling time between sourcing and measuring
            time.sleep(settling_time)

        elif source == 'source-voltage':
            session.channels[channels].ppmu_output_function = nidigital.PPMUOutputFunction.VOLTAGE

            session.channels[channels].ppmu_current_limit_range = current_limit_range
            session.channels[channels].ppmu_voltage_level = voltage_level

            session.channels[channels].ppmu_source()

            # Settling time between sourcing and measuring
            time.sleep(settling_time)

        pin_info = session.channels[channels].get_pin_results_pin_information()

        # Measure
        if measure == 'current':
            current_measurements = session.channels[channels].ppmu_measure(nidigital.PPMUMeasurementType.CURRENT)

            print('{:<6} {:<20} {:<10}'.format('Site', 'Pin Name', 'Current'))

            for pin, current in zip(pin_info, current_measurements):
                print(f'{pin.site_number:<6d} {pin.pin_name:<20} {current:<10f}')
        else:
            voltage_measurements = session.channels[channels].ppmu_measure(nidigital.PPMUMeasurementType.VOLTAGE)

            print('{:<6} {:<20} {:<10}'.format('Site', 'Pin Name', 'Voltage'))

            for pin, voltage in zip(pin_info, voltage_measurements):
                print(f'{pin.site_number:<6d} {pin.pin_name:<20} {voltage:<10f}')

        # Disconnect all channels using programmable onboard switching
        session.channels[channels].selected_function = nidigital.SelectedFunction.DISCONNECT


def _main(argsv):
    parser = argparse.ArgumentParser(description='Demonstrates how to source/measure voltage/current using the PPMU on selected channels/pins of the digital pattern instrument',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2,PXI1Slot3', help='Resource name of a NI digital pattern instrument, ensure the resource name matches the instrument name in the pinmap file.')
    parser.add_argument('-s', '--simulate', default='True', choices=['True', 'False'], help='Whether to run on simulated hardware or on real hardware')
    parser.add_argument('-c', '--channels', default='DUTPin1, SystemPin1', help='Channel(s)/Pin(s) to use')
    parser.add_argument('-m', '--measure', default='voltage', choices=['voltage', 'current'], help='Measure voltage or measure current')
    parser.add_argument('-at', '--aperture-time', default=0.000004, type=float, help='Aperture time in seconds')
    subparser = parser.add_subparsers(dest='source', help='Sub-command help, by default it measures voltage and does not source')

    source_current = subparser.add_parser('source-current', help='Source current')
    source_current.add_argument('-clr', '--current-level-range', default=0.000002, type=float, help='Current level range in amps')
    source_current.add_argument('-cl', '--current-level', default=0.000002, type=float, help='Current level in amps')
    source_current.add_argument('-vlh', '--voltage-limit-high', default=3.3, type=float, help='Voltage limit high in volts')
    source_current.add_argument('-vll', '--voltage-limit-low', default=0, type=float, help='Voltage limit low in volts')
    source_current.add_argument('-st', '--settling-time', default=0.01, type=float, help='Settling time in seconds')

    source_voltage = subparser.add_parser('source-voltage', help='Source voltage')
    source_voltage.add_argument('-clr', '--current-limit-range', default=0.000002, type=float, help='Current limit range in amps')
    source_voltage.add_argument('-vl', '--voltage-level', default=3.3, type=float, help='Voltage level in volts')
    source_voltage.add_argument('-st', '--settling-time', default=0.01, type=float, help='Settling time in seconds')

    args = parser.parse_args(argsv)

    if args.source == 'source-current':
        example(
            args.resource_name,
            'Simulate=1, DriverSetup=Model:6571' if args.simulate == 'True' else '',
            args.channels,
            args.measure,
            args.aperture_time,
            args.source,
            args.settling_time,
            args.current_level_range,
            args.current_level,
            args.voltage_limit_high,
            args.voltage_limit_low)
    elif args.source == 'source-voltage':
        example(
            args.resource_name,
            'Simulate=1, DriverSetup=Model:6571' if args.simulate == 'True' else '',
            args.channels,
            args.measure,
            args.aperture_time,
            args.source,
            args.settling_time,
            current_limit_range=args.current_limit_range,
            voltage_level=args.voltage_level)
    else:
        if args.measure == 'current':
            raise ValueError('Cannot measure current on a channel that is not sourcing voltage or current')
        example(
            args.resource_name,
            'Simulate=1, DriverSetup=Model:6571' if args.simulate == 'True' else '',
            args.channels,
            args.measure,
            args.aperture_time)


def main():
    _main(sys.argv[1:])


def test_main():
    _main([])
    _main(['-m', 'voltage'])
    with pytest.raises(Exception):
        _main(['-m', 'current'])
    _main(['-m', 'voltage', 'source-current'])
    _main(['-m', 'current', 'source-current'])
    _main(['-m', 'voltage', 'source-voltage'])
    _main(['-m', 'current', 'source-voltage'])


def test_example():
    resource_name = 'PXI1Slot2,PXI1Slot3'
    options = {'simulate': True, 'driver_setup': {'Model': '6571'}, }
    channels = 'DUTPin1, SystemPin1'
    aperture_time = 0.000004

    example(resource_name, options, channels, 'voltage',
            aperture_time)
    with pytest.raises(Exception):
        example(resource_name, options, channels, 'current',
                aperture_time)

    settling_time = 0.01
    current_level_range = 0.000002
    current_level = 0.000002
    voltage_limit_high = 3.3
    voltage_limit_low = 0
    example(resource_name, options, channels, 'voltage',
            aperture_time, 'source-current', settling_time,
            current_level_range, current_level,
            voltage_limit_high, voltage_limit_low)
    example(resource_name, options, channels, 'current',
            aperture_time, 'source-current', settling_time,
            current_level_range, current_level,
            voltage_limit_high, voltage_limit_low)

    current_limit_range = 0.000002
    voltage_level = 3.3
    example(resource_name, options, channels, 'voltage',
            aperture_time, 'source-voltage', settling_time,
            current_limit_range=current_limit_range,
            voltage_level=voltage_level)
    example(resource_name, options, channels, 'current',
            aperture_time, 'source-voltage', settling_time,
            current_limit_range=current_limit_range,
            voltage_level=voltage_level)


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/examples/ppmu_source_and_measure/PinMap.pinmap sha256=1c924cddb5c38e38814bbb9fdc9b4a62ced96fee30597951a7c0450785e4a99b bytes=2551 -->
## FILE: src/nidigital/examples/ppmu_source_and_measure/PinMap.pinmap

- repository: `ni/nimi-python`
- source_path: `src/nidigital/examples/ppmu_source_and_measure/PinMap.pinmap`
- sha256: `1c924cddb5c38e38814bbb9fdc9b4a62ced96fee30597951a7c0450785e4a99b`
- bytes: 2551

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.5">
	<Instruments>
		<NIDigitalPatternInstrument name="PXI1Slot2" numberOfChannels="32" group="Digital" />
		<NIDigitalPatternInstrument name="PXI1Slot3" numberOfChannels="32" group="Digital" />
	</Instruments>
	<Pins>
		<DUTPin name="DUTPin1" />
		<DUTPin name="DUTPin2" />
		<DUTPin name="DUTPin3" />
		<DUTPin name="DUTPin4" />
		<DUTPin name="DUTPin5" />
		<DUTPin name="DUTPin6" />
		<DUTPin name="DUTPin7" />
		<DUTPin name="DUTPin8" />
		<SystemPin name="SystemPin1" />
	</Pins>
	<PinGroups>
		<PinGroup name="PinGroup1">
			<PinReference pin="DUTPin1" />
			<PinReference pin="DUTPin2" />
			<PinReference pin="DUTPin3" />
			<PinReference pin="DUTPin4" />
			<PinReference pin="DUTPin5" />
			<PinReference pin="DUTPin6" />
			<PinReference pin="DUTPin7" />
			<PinReference pin="DUTPin8" />
		</PinGroup>
	</PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="DUTPin1" siteNumber="0" instrument="PXI1Slot2" channel="0" />
		<Connection pin="DUTPin1" siteNumber="1" instrument="PXI1Slot3" channel="0" />
		<Connection pin="DUTPin2" siteNumber="0" instrument="PXI1Slot2" channel="1" />
		<Connection pin="DUTPin2" siteNumber="1" instrument="PXI1Slot3" channel="1" />
		<Connection pin="DUTPin3" siteNumber="0" instrument="PXI1Slot2" channel="2" />
		<Connection pin="DUTPin3" siteNumber="1" instrument="PXI1Slot3" channel="2" />
		<Connection pin="DUTPin4" siteNumber="0" instrument="PXI1Slot2" channel="3" />
		<Connection pin="DUTPin4" siteNumber="1" instrument="PXI1Slot3" channel="3" />
		<Connection pin="DUTPin5" siteNumber="0" instrument="PXI1Slot2" channel="4" />
		<Connection pin="DUTPin5" siteNumber="1" instrument="PXI1Slot3" channel="4" />
		<Connection pin="DUTPin6" siteNumber="0" instrument="PXI1Slot2" channel="5" />
		<Connection pin="DUTPin6" siteNumber="1" instrument="PXI1Slot3" channel="5" />
		<Connection pin="DUTPin7" siteNumber="0" instrument="PXI1Slot2" channel="6" />
		<Connection pin="DUTPin7" siteNumber="1" instrument="PXI1Slot3" channel="6" />
		<Connection pin="DUTPin8" siteNumber="0" instrument="PXI1Slot2" channel="7" />
		<Connection pin="DUTPin8" siteNumber="1" instrument="PXI1Slot3" channel="7" />
		<SystemConnection pin="SystemPin1" instrument="PXI1Slot2" channel="8" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/examples/ppmu_source_and_measure/ppmu_source_and_measure.digiproj sha256=70d97ebf7d293f7455a3723beb6137520625b4838cf9cc2e4c52214c43b91d67 bytes=2727 -->
## FILE: src/nidigital/examples/ppmu_source_and_measure/ppmu_source_and_measure.digiproj

- repository: `ni/nimi-python`
- source_path: `src/nidigital/examples/ppmu_source_and_measure/ppmu_source_and_measure.digiproj`
- sha256: `70d97ebf7d293f7455a3723beb6137520625b4838cf9cc2e4c52214c43b91d67`
- bytes: 2727

````text
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="FA43F2F930A03FFF190ABD78331B60FC" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="5.3.1.50584" FeatureSetName="Digital Pattern Editor" Name="http://www.ni.com/PatternBasedDigital" OldestCompatibleVersion="4.5.0.0" Version="4.6.0.49152" />
		<ParsableNamespace AssemblyFileVersion="5.3.1.50584" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="5.2.0.49153" Version="5.2.0.49153" />
		<ApplicationVersionInfo Build="5.3.1.50584" Name="Digital Pattern Editor" Version="19.0.0" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<ProjectSettings Id="1" ModelDefinitionType="ProjectSettings" Name="ZProjectSettings" />
		<EmbeddedDefinitionReference Id="2" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="3" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<FileReference Id="14" ModelDefinitionType="PinMap" Name="PinMap\.pinmap" StoragePath="PinMap.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<EmbeddedDefinitionReference Id="15" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}CaptureResultsDefinition" Name="CaptureResults">
				<CaptureResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="17" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}BurstResultsDefinition" Name="BurstResults">
				<BurstResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="19" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}SystemInfoDefinition" Name="SystemInfo">
				<SystemInfoDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="20" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}DigitalScopeDefinition" Name="DigitalScope">
				<DigitalScopeDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
		</NameScopingEnvoy>
		<EmbeddedDefinitionReference Id="7" ModelDefinitionType="DigitalPatternEditor.ProjectPropertiesDefinition" Name="ProjectProperties">
			<ProjectPropertiesDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
		</EmbeddedDefinitionReference>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/LATEST_RELEASE sha256=dd1b44562fc7c779fd9bef2e55d2e7b58783c4ca61885f5b549cd89de7e9a3fd bytes=7 -->
## FILE: src/nidigital/LATEST_RELEASE

- repository: `ni/nimi-python`
- source_path: `src/nidigital/LATEST_RELEASE`
- sha256: `dd1b44562fc7c779fd9bef2e55d2e7b58783c4ca61885f5b549cd89de7e9a3fd`
- bytes: 7

````text
1.4.9
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/metadata/__init__.py sha256=4b7b39cf71ea45690188c6523109d0f0f8d8fcd1aa92823d69a7a1554cb97ddc bytes=513 -->
## FILE: src/nidigital/metadata/__init__.py

- repository: `ni/nimi-python`
- source_path: `src/nidigital/metadata/__init__.py`
- sha256: `4b7b39cf71ea45690188c6523109d0f0f8d8fcd1aa92823d69a7a1554cb97ddc`
- bytes: 513

````python
from metadata.config import config
from metadata.functions import functions
from metadata.attributes import attributes
from metadata.enums import enums
import metadata.functions_addon
import metadata.attributes_addon
import metadata.enums_addon
import metadata.config_addon

import build.helper as helper
import sys

# Update generated functions data with hand maintained data
config['modules'] = sys.modules
helper.add_all_metadata(functions, attributes, enums, config)

__version__ = config['module_version']
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/metadata/attributes.py sha256=d9ad33537777672394a66a95989b575234d4e89cff7fc084b76d46e57f4a2cc0 bytes=56362 -->
## FILE: src/nidigital/metadata/attributes.py

- repository: `ni/nimi-python`
- source_path: `src/nidigital/metadata/attributes.py`
- sha256: `d9ad33537777672394a66a95989b575234d4e89cff7fc084b76d46e57f4a2cc0`
- bytes: 56362

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-Digital Pattern Driver API metadata version 24.3.0f175
attributes = {
    1050002: {
        'access': 'read-write',
        'documentation': {
            'description': 'Checks the range and validates parameter and attribute values you pass to NI-Digital Pattern Driver functions. Ranges are always checked, regardless of the attribute setting.\n'
        },
        'name': 'RANGE_CHECK',
        'type': 'ViBoolean'
    },
    1050003: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies whether the NI-Digital Pattern Driver queries the digital pattern instrument status after each operation. The instrument status is always queried, regardless of the attribute setting.\n'
        },
        'name': 'QUERY_INSTRUMENT_STATUS',
        'type': 'ViBoolean'
    },
    1050004: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies whether to cache the value of attributes. When caching is enabled, the instrument driver keeps track of the current instrument settings and avoids sending redundant commands to the instrument. This significantly increases execution speed. Caching is always enabled in the driver, regardless of the value of this attribute.'
        },
        'name': 'CACHE',
        'type': 'ViBoolean'
    },
    1050005: {
        'access': 'read-write',
        'documentation': {
            'description': 'Simulates I/O operations. After you open a session, you cannot change the simulation state. Use the niDigital_InitWithOptions function to enable simulation.\n'
        },
        'name': 'SIMULATE',
        'type': 'ViBoolean'
    },
    1050006: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies whether the IVI engine keeps a list of the value coercions it makes for integer and real type attributes. Enabling record value coercions is not supported.\n'
        },
        'name': 'RECORD_COERCIONS',
        'type': 'ViBoolean'
    },
    1050007: {
        'access': 'read only',
        'documentation': {
            'description': 'This attribute returns initial values for NI-Digital Pattern Driver attributes as a string.\n'
        },
        'name': 'DRIVER_SETUP',
        'type': 'ViString'
    },
    1050021: {
        'access': 'read-write',
        'documentation': {
            'description': 'This attribute is not supported.\n'
        },
        'name': 'INTERCHANGE_CHECK',
        'type': 'ViBoolean'
    },
    1050203: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns the number of channels that the specific digital pattern instrument driver supports.\n'
        },
        'name': 'CHANNEL_COUNT',
        'type': 'ViInt32'
    },
    1050302: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns a string that contains the prefix for the NI-Digital Pattern driver.\n'
        },
        'name': 'SPECIFIC_DRIVER_PREFIX',
        'type': 'ViString'
    },
    1050304: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns a string that contains the resource descriptor that the NI-Digital Pattern Driver uses to identify the digital pattern instrument.\n'
        },
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'type': 'ViString'
    },
    1050305: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns a string containing the logical name that you specified when opening the current IVI session. This attribute is not supported.\n'
        },
        'name': 'LOGICAL_NAME',
        'type': 'ViString'
    },
    1050327: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns a comma delimited string that contains the supported digital pattern instrument models for the specific driver.\n'
        },
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'type': 'ViString'
    },
    1050401: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns a string that contains a comma-separated list of class-extension groups that the driver implements.\n'
        },
        'name': 'GROUP_CAPABILITIES',
        'type': 'ViString'
    },
    1050510: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns a string that contains the firmware revision information for the digital pattern instrument.\n'
        },
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'supported_rep_caps': [
            'instruments'
        ],
        'type': 'ViString'
    },
    1050511: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns a string ("National Instruments") that contains the name of the manufacturer of the digital pattern instrument.\n'
        },
        'name': 'INSTRUMENT_MANUFACTURER',
        'type': 'ViString'
    },
    1050512: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns a string that contains the model number or name of the digital pattern instrument.\n'
        },
        'name': 'INSTRUMENT_MODEL',
        'type': 'ViString'
    },
    1050513: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns a string ("National Instruments") that contains the name of the vendor that supplies the NI-Digital Pattern Driver.\n'
        },
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'type': 'ViString'
    },
    1050514: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns a string that contains a brief description of the NI-Digital Pattern driver.\n'
        },
        'name': 'SPECIFIC_DRIVER_DESCRIPTION',
        'type': 'ViString'
    },
    1050515: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns the major version number of the class specification with which NI-Digital is compliant. This attribute is not supported.\n'
        },
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION',
        'type': 'ViInt32'
    },
    1050516: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns the minor version number of the class specification with which NI-Digital is compliant. This attribute is not supported.\n'
        },
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION',
        'type': 'ViInt32'
    },
    1050551: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns a string that contains additional version information about the NI-Digital Pattern Driver. For example, the driver can return Driver: NI-Digital 16.0 as the value of this attribute.\n'
        },
        'name': 'SPECIFIC_DRIVER_REVISION',
        'type': 'ViString'
    },
    1150001: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns the serial number of the device.\n'
        },
        'name': 'SERIAL_NUMBER',
        'supported_rep_caps': [
            'instruments'
        ],
        'type': 'ViString'
    },
    1150004: {
        'access': 'read-write',
        'documentation': {
            'caution': 'In the Disconnect state, some I/O protection and sensing circuitry remains exposed. Do not subject the instrument to voltage beyond its operating range.\n',
            'description': 'Specifies whether digital pattern instrument channels are controlled by the pattern sequencer or PPMU, disconnected, or off.\n',
            'note': 'You can make PPMU voltage measurements using the niDigital_PPMU_Measure function from within any NIDIGITAL_ATTR_SELECTED_FUNCTION.\n',
            'table_body': [
                [
                    'NIDIGITAL_VAL_DIGITAL',
                    'The pin is connected to the driver, comparator, and active load functions. The PPMU is not sourcing, but can make voltage measurements. The state of the digital pin driver when you change the NIDIGITAL_ATTR_SELECTED_FUNCTION to Digital is determined by the most recent call to the niDigital_WriteStatic function or the last vector of the most recently executed pattern burst, whichever happened last. Use the niDigital_WriteStatic function to control the state of the digital pin driver through software. Use the niDigital_FancyBurstPattern function to control the state of the digital pin driver through a pattern. Set the **selectDigitalFunction** parameter of the niDigital_FancyBurstPattern function to VI_TRUE to automatically switch the NIDIGITAL_ATTR_SELECTED_FUNCTION of the pins in the pattern burst to NIDIGITAL_VAL_DIGITAL.'
                ],
                [
                    'NIDIGITAL_VAL_PPMU',
                    'The pin is connected to the PPMU. The driver, comparator, and active load are off while this function is selected. Call the niDigital_PPMU_Source function to source a voltage or current. The niDigital_PPMU_Source function automatically switches the NIDIGITAL_ATTR_SELECTED_FUNCTION to the PPMU state and starts sourcing from the PPMU. Changing the NIDIGITAL_ATTR_SELECTED_FUNCTION to NIDIGITAL_VAL_DISCONNECT, NIDIGITAL_VAL_OFF, or NIDIGITAL_VAL_DIGITAL causes the PPMU to stop sourcing. If you set the NIDIGITAL_ATTR_SELECTED_FUNCTION attribute to PPMU, the PPMU is initially not sourcing.'
                ],
                [
                    'NIDIGITAL_VAL_OFF',
                    'The pin is electrically connected, and the PPMU and digital pin driver are off while this function is selected.'
                ],
                [
                    'NIDIGITAL_VAL_DISCONNECT',
                    'The pin is electrically disconnected from instrument functions. Selecting this function causes the PPMU to stop sourcing prior to disconnecting the pin.'
                ]
            ],
            'table_header': [
                'Defined Values:'
            ]
        },
        'enum': 'SelectedFunction',
        'name': 'SELECTED_FUNCTION',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViInt32'
    },
    1150006: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the behavior of the pin during non-drive cycles.\n',
            'table_body': [
                [
                    'NIDIGITAL_VAL_ACTIVE_LOAD',
                    'Specifies that, for non-drive pin states (L, H, X, V, M, E), the active load is connected and the instrument sources or sinks a defined amount of current to load the DUT. The amount of current sourced by the instrument and therefore sunk by the DUT is specified by IOL. The amount of current sunk by the instrument and therefore sourced by the DUT is specified by IOH. The voltage at which the instrument changes between sourcing and sinking is specified by VCOM.'
                ],
                [
                    'NIDIGITAL_VAL_VTERM',
                    'Specifies that, for non-drive pin states (L, H, X, V, M, E), the pin driver terminates the pin to the configured VTERM voltage through a 50 Ω impedance. VTERM is adjustable to allow for the pin to terminate at a set level. This is useful for instruments that might operate incorrectly if an instrument pin is unterminated and is allowed to float to any voltage level within the instrument voltage range. To address this issue, enable VTERM by configuring the VTERM pin level to the desired voltage and selecting the VTERM termination mode. Setting VTERM to 0 V and selecting the VTERM termination mode has the effect of connecting a 50 Ω termination to ground, which provides an effective 50 Ω impedance for the pin. This can be useful for improving signal integrity of certain DUTs by reducing reflections while the DUT drives the pin.'
                ],
                [
                    'NIDIGITAL_VAL_HIGH_Z',
                    'Specifies that, for non-drive pin states (L, H, X, V, M, E), the pin driver is put in a high-impedance state and the active load is disabled.'
                ]
            ],
            'table_header': [
                'Defined Values:'
            ]
        },
        'enum': 'TerminationMode',
        'name': 'TERMINATION_MODE',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViInt32'
    },
    1150007: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the voltage that the digital pattern instrument will apply to the input of the DUT when the test instrument drives a logic low (0).\n'
        },
        'name': 'VIL',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150008: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the voltage that the digital pattern instrument will apply to the input of the DUT when the test instrument drives a logic high (1).\n'
        },
        'name': 'VIH',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150009: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the output voltage from the DUT below which the comparator on the digital pattern test instrument interprets a logic low (L).\n'
        },
        'name': 'VOL',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150010: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the output voltage from the DUT above which the comparator on the digital pattern test instrument interprets a logic high (H).\n'
        },
        'name': 'VOH',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150011: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the termination voltage the digital pattern instrument applies during non-drive cycles when the termination mode is set to V :sub:`term`. The instrument applies the termination voltage through a 50 Ω parallel termination resistance.\n'
        },
        'name': 'VTERM',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150012: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the current that the DUT sinks from the active load while outputting a voltage below VCOM.\n'
        },
        'name': 'ACTIVE_LOAD_IOL',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150013: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the current that the DUT sources to the active load while outputting a voltage above VCOM.\n'
        },
        'name': 'ACTIVE_LOAD_IOH',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150014: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the voltage level at which the active load circuit switches between sourcing current and sinking current.\n'
        },
        'name': 'ACTIVE_LOAD_VCOM',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150015: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies whether the PPMU forces voltage or current to the DUT.\n',
            'table_body': [
                [
                    'NIDIGITAL_VAL_DC_VOLTAGE',
                    'Specifies the output function to DC Voltage.'
                ],
                [
                    'NIDIGITAL_VAL_DC_CURRENT',
                    'Specifies the output function to DC Current.'
                ]
            ],
            'table_header': [
                'Defined Values:'
            ]
        },
        'enum': 'PPMUOutputFunction',
        'name': 'PPMU_OUTPUT_FUNCTION',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViInt32'
    },
    1150016: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the voltage level, in volts, that the PPMU forces to the DUT. This attribute is applicable only when you set the NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION attribute to DC Voltage.\n'
        },
        'name': 'PPMU_VOLTAGE_LEVEL',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150017: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the valid range, in amps, to which the current limit can be set while the PPMU forces voltage to the DUT. This attribute is applicable only when you set the NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION attribute to DC Voltage.\n'
        },
        'name': 'PPMU_CURRENT_LIMIT_RANGE',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150019: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the current level, in amps, that the PPMU forces to the DUT. This attribute is applicable only when you set the NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION attribute to DC Current. Specify valid values for the current level using the niDigital_PPMU_ConfigureCurrentLevelRange function.\n'
        },
        'name': 'PPMU_CURRENT_LEVEL',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150020: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the range of valid values for the current level, in amps, that the PPMU forces to the DUT. This attribute is applicable only when you set the NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION attribute to DC Current.\n'
        },
        'name': 'PPMU_CURRENT_LEVEL_RANGE',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150021: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the minimum voltage limit, or low clamp voltage (V :sub:`CL` ), in volts, at the pin when the PPMU forces current to the DUT. This attribute is applicable only when you set the NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION attribute to DC Current.\n'
        },
        'name': 'PPMU_VOLTAGE_LIMIT_LOW',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150022: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the maximum voltage limit, or high clamp voltage (V :sub:`CH` ), in volts, at the pin when the PPMU forces current to the DUT. This attribute is applicable only when you set the NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION attribute to DC Current.\n'
        },
        'name': 'PPMU_VOLTAGE_LIMIT_HIGH',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150023: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the pattern name or exported pattern label from which to start bursting the pattern.\n'
        },
        'name': 'START_LABEL',
        'type': 'ViString'
    },
    1150029: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the Start trigger type. The digital pattern instrument waits for this trigger after you call the niDigital_init function or the niDigital_FancyBurstPattern function, and does not burst a pattern until this trigger is received.\n',
            'table_body': [
                [
                    'NIDIGITAL_VAL_NONE',
                    'Disables the Start trigger. Pattern bursting starts immediately after you call the niDigital_init function or the niDigital_FancyBurstPattern function.'
                ],
                [
                    'NIDIGITAL_VAL_DIGITAL_EDGE',
                    'Pattern bursting does not start until the digital pattern instrument detects a digital edge.'
                ],
                [
                    'NIDIGITAL_VAL_SOFTWARE',
                    'Pattern bursting does not start until the digital pattern instrument receives a software Start trigger. Create a software Start trigger by calling the niDigital_SendSoftwareEdgeTrigger function and selecting start trigger in the **trigger** parameter.Related information: SendSoftwareEdgeTrigger function.'
                ]
            ],
            'table_header': [
                'Defined Values:'
            ]
        },
        'enum': 'TriggerType',
        'name': 'START_TRIGGER_TYPE',
        'type': 'ViInt32'
    },
    1150030: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the source terminal for the Start trigger. This property is used when the NIDIGITAL_ATTR_START_TRIGGER_TYPE attribute is set to Digital Edge. You can specify source terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The source terminal can also be a terminal from another device, in which case the NI-Digital Pattern Driver automatically finds a route (if one is available) from that terminal to the input terminal (going through a physical PXI backplane trigger line). For example, you can set the source terminal on Dev1 to be /Dev2/StartTrigger.\n',
            'table_body': [
                [
                    'PXI_Trig0',
                    'PXI trigger line 0'
                ],
                [
                    'PXI_Trig1',
                    'PXI trigger line 1'
                ],
                [
                    'PXI_Trig2',
                    'PXI trigger line 2'
                ],
                [
                    'PXI_Trig3',
                    'PXI trigger line 3'
                ],
                [
                    'PXI_Trig4',
                    'PXI trigger line 4'
                ],
                [
                    'PXI_Trig5',
                    'PXI trigger line 5'
                ],
                [
                    'PXI_Trig6',
                    'PXI trigger line 6'
                ],
                [
                    'PXI_Trig7',
                    'PXI trigger line 7'
                ]
            ],
            'table_header': [
                'Defined Values:'
            ]
        },
        'name': 'DIGITAL_EDGE_START_TRIGGER_SOURCE',
        'type': 'ViString'
    },
    1150031: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the active edge for the Start trigger. This property is used when the NIDIGITAL_ATTR_START_TRIGGER_TYPE attribute is set to Digital Edge.\n',
            'table_body': [
                [
                    'NIDIGITAL_VAL_RISING_EDGE',
                    'Asserts the trigger when the signal transitions from low level to high level.'
                ],
                [
                    'NIDIGITAL_VAL_FALLING_EDGE',
                    'Asserts the trigger when the signal transitions from high level to low level.'
                ]
            ],
            'table_header': [
                'Defined Values:'
            ]
        },
        'enum': 'DigitalEdge',
        'name': 'DIGITAL_EDGE_START_TRIGGER_EDGE',
        'type': 'ViInt32'
    },
    1150032: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the destination terminal for exporting the Start trigger. Terminals can be specified in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.\n',
            'table_body': [
                [
                    'Do not export signal',
                    'The signal is not exported.'
                ],
                [
                    'PXI_Trig0',
                    'PXI trigger line 0'
                ],
                [
                    'PXI_Trig1',
                    'PXI trigger line 1'
                ],
                [
                    'PXI_Trig2',
                    'PXI trigger line 2'
                ],
                [
                    'PXI_Trig3',
                    'PXI trigger line 3'
                ],
                [
                    'PXI_Trig4',
                    'PXI trigger line 4'
                ],
                [
                    'PXI_Trig5',
                    'PXI trigger line 5'
                ],
                [
                    'PXI_Trig6',
                    'PXI trigger line 6'
                ],
                [
                    'PXI_Trig7',
                    'PXI trigger line 7'
                ]
            ],
            'table_header': [
                'Defined Values:'
            ]
        },
        'name': 'EXPORTED_START_TRIGGER_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150033: {
        'access': 'read-write',
        'documentation': {
            'description': 'Disables the conditional jump trigger or configures it for either hardware triggering or software triggering.  The default value is NIDIGITAL_VAL_NONE.\n',
            'table_body': [
                [
                    'NIDIGITAL_VAL_NONE',
                    'Disables the conditional jump trigger.'
                ],
                [
                    'NIDIGITAL_VAL_DIGITAL_EDGE',
                    'Configures the conditional jump trigger for hardware triggering.'
                ],
                [
                    'NIDIGITAL_VAL_SOFTWARE',
                    'Configures the conditional jump trigger for software triggering.'
                ]
            ],
            'table_header': [
                'Valid Values:'
            ]
        },
        'enum': 'TriggerType',
        'name': 'CONDITIONAL_JUMP_TRIGGER_TYPE',
        'supported_rep_caps': [
            'conditional_jump_triggers'
        ],
        'type': 'ViInt32'
    },
    1150034: {
        'access': 'read-write',
        'documentation': {
            'description': 'Configures the digital trigger source terminal for a conditional jump trigger instance. The PXIe-6570/6571 supports triggering through the PXI trigger bus. You can specify source terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The source terminal can also be a terminal from another device, in which case the NI-Digital Pattern Driver automatically finds a route (if one is available) from that terminal to the input terminal (going through a physical PXI backplane trigger line). For example, you can set the source terminal on Dev1 to be /Dev2/ConditionalJumpTrigger0. The default value is VI_NULL.\n',
            'table_body': [
                [
                    'String identifier to any valid terminal name'
                ]
            ],
            'table_header': [
                'Valid Values:'
            ]
        },
        'name': 'DIGITAL_EDGE_CONDITIONAL_JUMP_TRIGGER_SOURCE',
        'supported_rep_caps': [
            'conditional_jump_triggers'
        ],
        'type': 'ViString'
    },
    1150035: {
        'access': 'read-write',
        'documentation': {
            'description': 'Configures the active edge of the incoming trigger signal for the conditional jump trigger instance. The default value is NIDIGITAL_VAL_RISING_EDGE.\n',
            'table_body': [
                [
                    'NIDIGITAL_VAL_RISING_EDGE',
                    'Specifies the signal transition from low level to high level.'
                ],
                [
                    'NIDIGITAL_VAL_FALLING_EDGE',
                    'Specifies the signal transition from high level to low level.'
                ]
            ],
            'table_header': [
                'Valid Values:'
            ]
        },
        'enum': 'DigitalEdge',
        'name': 'DIGITAL_EDGE_CONDITIONAL_JUMP_TRIGGER_EDGE',
        'supported_rep_caps': [
            'conditional_jump_triggers'
        ],
        'type': 'ViInt32'
    },
    1150036: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the terminal to output the exported signal of the specified instance of the conditional jump trigger. The default value is VI_NULL.\n',
            'table_body': [
                [
                    'VI_NULL ("")',
                    'Returns an empty string'
                ],
                [
                    'PXI_Trig0',
                    'PXI trigger line 0'
                ],
                [
                    'PXI_Trig1',
                    'PXI trigger line 1'
                ],
                [
                    'PXI_Trig2',
                    'PXI trigger line 2'
                ],
                [
                    'PXI_Trig3',
                    'PXI trigger line 3'
                ],
                [
                    'PXI_Trig4',
                    'PXI trigger line 4'
                ],
                [
                    'PXI_Trig5',
                    'PXI trigger line 5'
                ],
                [
                    'PXI_Trig6',
                    'PXI trigger line 6'
                ],
                [
                    'PXI_Trig7',
                    'PXI trigger line 7'
                ]
            ],
            'table_header': [
                'Valid Values:'
            ]
        },
        'name': 'EXPORTED_CONDITIONAL_JUMP_TRIGGER_OUTPUT_TERMINAL',
        'supported_rep_caps': [
            'conditional_jump_triggers'
        ],
        'type': 'ViString'
    },
    1150037: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the measurement aperture time for the PPMU. The NIDIGITAL_ATTR_PPMU_APERTURE_TIME_UNITS attribute sets the units of the PPMU aperture time.\n'
        },
        'name': 'PPMU_APERTURE_TIME',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150038: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the units of the measurement aperture time for the PPMU.\n',
            'table_body': [
                [
                    'NIDIGITAL_VAL_SECONDS',
                    'Specifies the aperture time in seconds.'
                ]
            ],
            'table_header': [
                'Defined Values:'
            ]
        },
        'enum': 'PPMUApertureTimeUnits',
        'name': 'PPMU_APERTURE_TIME_UNITS',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViInt32'
    },
    1150039: {
        'access': 'read only',
        'documentation': {
            'description': 'Specifies the terminal name for the output trigger signal of the Start trigger. You can use this terminal name as an input signal source for another trigger.\n'
        },
        'name': 'START_TRIGGER_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150040: {
        'access': 'read only',
        'documentation': {
            'description': 'Specifies the terminal name from which the exported conditional jump trigger signal may be routed to other instruments through the PXI trigger bus. You can use this signal to trigger other instruments when the conditional jump trigger instance asserts on the digital pattern instrument.\n'
        },
        'name': 'CONDITIONAL_JUMP_TRIGGER_TERMINAL_NAME',
        'supported_rep_caps': [
            'conditional_jump_triggers'
        ],
        'type': 'ViString'
    },
    1150041: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the destination terminal for exporting the Pattern Opcode Event. Terminals can be specified in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.\n',
            'table_body': [
                [
                    'PXI_Trig0',
                    'PXI trigger line 0'
                ],
                [
                    'PXI_Trig1',
                    'PXI trigger line 1'
                ],
                [
                    'PXI_Trig2',
                    'PXI trigger line 2'
                ],
                [
                    'PXI_Trig3',
                    'PXI trigger line 3'
                ],
                [
                    'PXI_Trig4',
                    'PXI trigger line 4'
                ],
                [
                    'PXI_Trig5',
                    'PXI trigger line 5'
                ],
                [
                    'PXI_Trig6',
                    'PXI trigger line 6'
                ],
                [
                    'PXI_Trig7',
                    'PXI trigger line 7'
                ]
            ],
            'table_header': [
                'Defined Values:'
            ]
        },
        'name': 'EXPORTED_PATTERN_OPCODE_EVENT_OUTPUT_TERMINAL',
        'supported_rep_caps': [
            'pattern_opcode_events'
        ],
        'type': 'ViString'
    },
    1150042: {
        'access': 'read only',
        'documentation': {
            'description': 'Specifies the terminal name for the output trigger signal of the specified instance of a Pattern Opcode Event. You can use this terminal name as an input signal source for another trigger.\n'
        },
        'name': 'PATTERN_OPCODE_EVENT_TERMINAL_NAME',
        'supported_rep_caps': [
            'pattern_opcode_events'
        ],
        'type': 'ViString'
    },
    1150043: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the type of trigger condition on which History RAM starts acquiring pattern information.\n',
            'table_body': [
                [
                    'NIDIGITAL_VAL_FIRST_FAILURE',
                    'Starts acquiring pattern information in History RAM on the first failed cycle in a pattern burst.'
                ],
                [
                    'NIDIGITAL_VAL_CYCLE_NUMBER',
                    'Starts acquiring pattern information in History RAM starting from a specified cycle number.'
                ],
                [
                    'NIDIGITAL_VAL_PATTERN_LABEL',
                    'Starts acquiring pattern information in History RAM starting from a specified pattern label, augmented by vector and cycle offsets.'
                ]
            ],
            'table_header': [
                'Defined Values:'
            ]
        },
        'enum': 'HistoryRAMTriggerType',
        'name': 'HISTORY_RAM_TRIGGER_TYPE',
        'type': 'ViInt32'
    },
    1150044: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the cycle number on which History RAM starts acquiring pattern information when configured for a cycle number trigger.\n'
        },
        'name': 'CYCLE_NUMBER_HISTORY_RAM_TRIGGER_CYCLE_NUMBER',
        'type': 'ViInt64'
    },
    1150045: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the number of cycles that follow the specified pattern label and vector offset, after which History RAM will start acquiring pattern information when configured for a pattern label trigger.\n'
        },
        'name': 'PATTERN_LABEL_HISTORY_RAM_TRIGGER_CYCLE_OFFSET',
        'type': 'ViInt64'
    },
    1150046: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the pattern label, augmented by the vector and cycle offset, to determine the point where History RAM will start acquiring pattern information when configured for a pattern label trigger.\n'
        },
        'name': 'PATTERN_LABEL_HISTORY_RAM_TRIGGER_LABEL',
        'type': 'ViString'
    },
    1150047: {
        'access': 'read-write',
        'documentation': {
            'description': 'Configures which cycles History RAM acquires after the trigger conditions are met. If you configure History RAM to only acquire failed cycles, you must set the pretrigger samples for History RAM to 0.\n',
            'table_body': [
                [
                    'NIDIGITAL_VAL_FAILED_CYCLES',
                    'Only acquires cycles that fail a compare after the triggering conditions are met.'
                ],
                [
                    'NIDIGITAL_VAL_ALL_CYCLES',
                    'Acquires all cycles after the triggering conditions are met.'
                ]
            ],
            'table_header': [
                'Defined Values:'
            ]
        },
        'enum': 'HistoryRAMCyclesToAcquire',
        'name': 'HISTORY_RAM_CYCLES_TO_ACQUIRE',
        'type': 'ViInt32'
    },
    1150048: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the number of samples to acquire before the trigger conditions are met. If you configure History RAM to only acquire failed cycles, you must set the pretrigger samples for History RAM to 0.\n'
        },
        'name': 'HISTORY_RAM_PRETRIGGER_SAMPLES',
        'type': 'ViInt32'
    },
    1150051: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': 'Specifies the TDR Offset.\n'
        },
        'name': 'TDR_OFFSET',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150052: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the number of vectors that follow the specified pattern label, after which History RAM will start acquiring pattern information when configured for a pattern label trigger.\n'
        },
        'name': 'PATTERN_LABEL_HISTORY_RAM_TRIGGER_VECTOR_OFFSET',
        'type': 'ViInt64'
    },
    1150054: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the current limit, in amps, that the output cannot exceed while the PPMU forces voltage to the DUT. This attribute is applicable only when you set the NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION attribute to DC Voltage. The PXIe-6570/6571 does not support the NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT attribute and only allows configuration of the NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT_RANGE attribute.\n'
        },
        'name': 'PPMU_CURRENT_LIMIT',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150055: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns whether the device supports configuration of a current limit when you set the NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION attribute to DC Voltage.\n'
        },
        'name': 'PPMU_CURRENT_LIMIT_SUPPORTED',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViBoolean'
    },
    1150059: {
        'access': 'read only',
        'documentation': {
            'description': 'Specifies the terminal name for the output trigger signal of the Sequencer Flags trigger. You can use this terminal name as an input signal source for another trigger.\n'
        },
        'name': 'SEQUENCER_FLAG_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150060: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies whether the pattern comparisons are masked or not. When set to VI_TRUE for a specified pin, failures on that pin will be masked.\n'
        },
        'name': 'MASK_COMPARE',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViBoolean'
    },
    1150062: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies whether keep_alive opcodes should behave like halt opcodes.\n'
        },
        'name': 'HALT_ON_KEEP_ALIVE_OPCODE',
        'type': 'ViBoolean'
    },
    1150063: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns VI_TRUE if the digital pattern instrument is driving the keep alive pattern.\n'
        },
        'name': 'IS_KEEP_ALIVE_ACTIVE',
        'type': 'ViBoolean'
    },
    1150064: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies how the output should behave when the current limit is reached.\n',
            'table_body': [
                [
                    'NIDIGITAL_VAL_CURRENT_REGULATE',
                    'Controls output current so that it does not exceed the current limit. Power continues to generate even if the current limit is reached.'
                ]
            ],
            'table_header': [
                'Defined Values:'
            ]
        },
        'enum': 'PPMUCurrentLimitBehavior',
        'name': 'PPMU_CURRENT_LIMIT_BEHAVIOR',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViInt32'
    },
    1150069: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': 'Specifies the measurement time for the frequency counter.\n'
        },
        'name': 'FREQUENCY_COUNTER_MEASUREMENT_TIME',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64',
        'type_in_documentation': 'float in seconds or datetime.timedelta'
    },
    1150071: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies whether the NIDIGITAL_ATTR_TIMING_ABSOLUTE_DELAY attribute should be applied to adjust the digital pattern instrument timing reference relative to other instruments in the system. Do not use this feature with digital pattern instruments in a Semiconductor Test System (STS). Timing absolute delay conflicts with the adjustment performed during STS timing calibration. When set to VI_TRUE, the digital pattern instrument automatically adjusts the timing absolute delay to correct the instrument timing reference relative to other instruments in the system for better timing alignment among synchronized instruments.\n'
        },
        'name': 'TIMING_ABSOLUTE_DELAY_ENABLED',
        'type': 'ViBoolean'
    },
    1150072: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': 'Specifies a timing delay, measured in seconds, and applies the delay to the digital pattern instrument in addition to TDR and calibration adjustments. If the NIDIGITAL_ATTR_TIMING_ABSOLUTE_DELAY_ENABLED attribute is set to VI_TRUE, this value is the intermodule skew measured by NI-TClk. You can modify this value to override the timing delay and align the I/O timing of this instrument with another instrument that shares the same reference clock. If the NIDIGITAL_ATTR_TIMING_ABSOLUTE_DELAY_ENABLED attribute is VI_FALSE, this attribute will return 0.0. Changing the NIDIGITAL_ATTR_TIMING_ABSOLUTE_DELAY_ENABLED attribute from VI_FALSE to VI_TRUE will set the NIDIGITAL_ATTR_TIMING_ABSOLUTE_DELAY value back to your previously set value.\n'
        },
        'name': 'TIMING_ABSOLUTE_DELAY',
        'supported_rep_caps': [
            'instruments'
        ],
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150073: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the frequency for the clock generator.\n'
        },
        'name': 'CLOCK_GENERATOR_FREQUENCY',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViReal64'
    },
    1150074: {
        'access': 'read only',
        'documentation': {
            'description': 'Indicates whether the clock generator is running.\n'
        },
        'name': 'CLOCK_GENERATOR_IS_RUNNING',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViBoolean'
    },
    1150076: {
        'access': 'read-write',
        'documentation': {
            'description': 'Enables the instrument to operate in additional voltage ranges where instrument specifications may differ from standard ranges. When set to VI_TRUE, this attribute enables extended voltage range operation. Review specification deviations for application suitability before using this attribute. NI recommends setting this attribute to VI_FALSE when not using the extended voltage range to avoid unintentional use of this range. The extended voltage range is supported only for PPMU, with the output function set to DC Voltage. A voltage glitch may occur when you change the PPMU output voltage from a standard range to the extended voltage range, or vice-versa, while the PPMU is sourcing. NI recommends temporarily changing the NIDIGITAL_ATTR_SELECTED_FUNCTION attribute to Off before sourcing a voltage level that requires a range change.\n'
        },
        'name': 'PPMU_ALLOW_EXTENDED_VOLTAGE_RANGE',
        'supported_rep_caps': [
            'channels',
            'pins'
        ],
        'type': 'ViBoolean'
    },
    1150077: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the maximum number of History RAM samples to acquire per site. If the property is set to -1, it will acquire until the History RAM buffer is full.\n'
        },
        'grpc_enum': 'HistoryRAMMaxSamplesToAcquirePerSite',
        'name': 'HISTORY_RAM_MAX_SAMPLES_TO_ACQUIRE_PER_SITE',
        'type': 'ViInt32'
    },
    1150078: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies whether the instrument acquires a finite number of History Ram samples or acquires continuously. The maximum number of samples that will be acquired when this property is set to VI_TRUE is determined by the instrument History RAM depth specification and the History RAM Max Samples to Acquire Per Site property. The default value is VI_TRUE.\n',
            'table_body': [
                [
                    'VI_TRUE',
                    'Specifies that History RAM results will not stream into the host buffer until a History RAM fetch API is called.'
                ],
                [
                    'VI_FALSE',
                    'Specifies that History RAM results will automatically start streaming into a host buffer after a pattern is burst and the History RAM has triggered.'
                ]
            ],
            'table_header': [
                'Valid Values:'
            ]
        },
        'name': 'HISTORY_RAM_NUMBER_OF_SAMPLES_IS_FINITE',
        'type': 'ViBoolean'
    },
    1150079: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the size, in samples, of the host memory buffer. The default value is 32000.\n',
            'table_body': [
                [
                    '0-INT64_MAX'
                ]
            ],
            'table_header': [
                'Valid Values:'
            ]
        },
        'name': 'HISTORY_RAM_BUFFER_SIZE_PER_SITE',
        'type': 'ViInt64'
    },
    1150081: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies whether TDR Channels are connected to an open circuit or a short to ground.\n'
        },
        'enum': 'TDREndpointTermination',
        'name': 'TDR_ENDPOINT_TERMINATION',
        'type': 'ViInt32'
    },
    1150084: {
        'access': 'read-write',
        'documentation': {
            'description': 'Determines how the frequency counters of the digital pattern instrument make measurements.\n',
            'table_body': [
                [
                    'NIDIGITAL_VAL_BANKED',
                    'Each discrete frequency counter is mapped to specific channels and makes frequency measurements from only those channels. Use banked mode when you need access to the full measure frequency range of the instrument. **Note:** If you request frequency measurements from multiple channels within the same bank, the measurements are made in series for the channels in that bank.'
                ],
                [
                    'NIDIGITAL_VAL_PARALLEL',
                    'All discrete frequency counters make frequency measurements from all channels in parallel with one another. Use parallel mode to increase the speed of frequency measurements if you do not need access to the full measure frequency range of the instrument; in parallel mode, you can also add NIDIGITAL_ATTR_FREQUENCY_COUNTER_HYSTERESIS_ENABLED to reduce measurement noise.'
                ]
            ],
            'table_header': [
                'Valid Values:'
            ]
        },
        'enum': 'FrequencyMeasurementMode',
        'name': 'FREQUENCY_COUNTER_MEASUREMENT_MODE',
        'type': 'ViInt32'
    },
    1150085: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies whether hysteresis is enabled for the frequency counters of the digital pattern instrument.\n'
        },
        'name': 'FREQUENCY_COUNTER_HYSTERESIS_ENABLED',
        'type': 'ViBoolean'
    },
    1150086: {
        'access': 'read-write',
        'documentation': {
            'description': 'Disables the rio trigger or configures it for hardware triggering.  The default value is NIDIGITAL_VAL_NONE.\n',
            'table_body': [
                [
                    'NIDIGITAL_VAL_NONE',
                    'Disables the conditional jump trigger.'
                ],
                [
                    'NIDIGITAL_VAL_DIGITAL_EDGE',
                    'Configures the conditional jump trigger for hardware triggering.'
                ]
            ],
            'table_header': [
                'Valid Values:'
            ]
        },
        'enum': 'TriggerType',
        'name': 'RIO_TRIGGER_TYPE',
        'supported_rep_caps': [
            'rio_triggers'
        ],
        'type': 'ViInt32'
    },
    1150087: {
        'access': 'read-write',
        'documentation': {
            'description': 'Configures the digital trigger source terminal for a RIO trigger instance. The PXIe-6570/6571 supports triggering through the PXI trigger bus. You can specify source terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The source terminal can also be a terminal from another device, in which case the NI-Digital Pattern Driver automatically finds a route (if one is available) from that terminal to the input terminal (going through a physical PXI backplane trigger line). For example, you can set the source terminal on Dev1 to be /Dev2/RIOTrigger0. The default value is VI_NULL.\n',
            'table_body': [
                [
                    'String identifier to any valid terminal name'
                ]
            ],
            'table_header': [
                'Valid Values:'
            ]
        },
        'name': 'DIGITAL_EDGE_RIO_TRIGGER_SOURCE',
        'supported_rep_caps': [
            'rio_triggers'
        ],
        'type': 'ViString'
    },
    1150088: {
        'access': 'read-write',
        'documentation': {
            'description': 'Configures the active edge of the incoming trigger signal for the RIO trigger instance. The default value is NIDIGITAL_VAL_RISING_EDGE.\n',
            'table_body': [
                [
                    'NIDIGITAL_VAL_RISING_EDGE',
                    'Specifies the signal transition from low level to high level.'
                ],
                [
                    'NIDIGITAL_VAL_FALLING_EDGE',
                    'Specifies the signal transition from high level to low level.'
                ]
            ],
            'table_header': [
                'Valid Values:'
            ]
        },
        'enum': 'DigitalEdge',
        'name': 'DIGITAL_EDGE_RIO_TRIGGER_EDGE',
        'supported_rep_caps': [
            'rio_triggers'
        ],
        'type': 'ViInt32'
    },
    1150089: {
        'access': 'read only',
        'documentation': {
            'description': 'Specifies the terminal name from which the exported RIO trigger signal may be routed to other instruments through the PXI trigger bus. You can use this signal to trigger other instruments when the RIO trigger instance asserts on the digital pattern instrument.\n'
        },
        'name': 'RIO_TRIGGER_TERMINAL_NAME',
        'supported_rep_caps': [
            'rio_triggers'
        ],
        'type': 'ViString'
    },
    1150090: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the destination terminal for exporting the RIO Event. Terminals can be specified in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.\n',
            'table_body': [
                [
                    'PXI_Trig0',
                    'PXI trigger line 0'
                ],
                [
                    'PXI_Trig1',
                    'PXI trigger line 1'
                ],
                [
                    'PXI_Trig2',
                    'PXI trigger line 2'
                ],
                [
                    'PXI_Trig3',
                    'PXI trigger line 3'
                ],
                [
                    'PXI_Trig4',
                    'PXI trigger line 4'
                ],
                [
                    'PXI_Trig5',
                    'PXI trigger line 5'
                ],
                [
                    'PXI_Trig6',
                    'PXI trigger line 6'
                ],
                [
                    'PXI_Trig7',
                    'PXI trigger line 7'
                ]
            ],
            'table_header': [
                'Defined Values:'
            ]
        },
        'name': 'EXPORTED_RIO_EVENT_OUTPUT_TERMINAL',
        'supported_rep_caps': [
            'rio_events'
        ],
        'type': 'ViString'
    },
    1150091: {
        'access': 'read only',
        'documentation': {
            'description': 'Specifies the terminal name for the output signal of the specified instance of a RIO Event. You can use this terminal name as an input signal source for another trigger.\n'
        },
        'name': 'RIO_EVENT_TERMINAL_NAME',
        'supported_rep_caps': [
            'rio_events'
        ],
        'type': 'ViString'
    }
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/metadata/attributes_addon.py sha256=17a2127d02579d026109ae3070d68b679f75dfef78e81e17ee575a6a80fec153 bytes=201 -->
## FILE: src/nidigital/metadata/attributes_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nidigital/metadata/attributes_addon.py`
- sha256: `17a2127d02579d026109ae3070d68b679f75dfef78e81e17ee575a6a80fec153`
- bytes: 201

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/metadata/config.py sha256=938ccb4fa1feedec896a51dde152d45d7df59e65f44ae59a8f2a5802c3357b0e bytes=2109 -->
## FILE: src/nidigital/metadata/config.py

- repository: `ni/nimi-python`
- source_path: `src/nidigital/metadata/config.py`
- sha256: `938ccb4fa1feedec896a51dde152d45d7df59e65f44ae59a8f2a5802c3357b0e`
- bytes: 2109

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-Digital Pattern Driver API metadata version 24.3.0f175
config = {
    'api_version': '24.3.0f175',
    'c_function_prefix': 'niDigital_',
    'close_function': 'close',
    'context_manager_name': {
        'abort_function': 'Abort',
        'initiate_function': 'Initiate',
        'task': 'burst'
    },
    'custom_types': [
    ],
    'driver_name': 'NI-Digital Pattern Driver',
    'enum_whitelist_suffix': [
    ],
    'extra_errors_used': [
        'InvalidRepeatedCapabilityError',
        'SelfTestError'
    ],
    'grpc_service_class_prefix': 'NiDigital',
    'init_function': 'InitWithOptions',
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
    'module_name': 'nidigital',
    'proto_name': 'nidigitalpattern',
    'repeated_capabilities': [
        {
            'prefix': '',
            'python_name': 'channels'
        },
        {
            'prefix': '',
            'python_name': 'pins'
        },
        {
            'prefix': '',
            'python_name': 'instruments'
        },
        {
            'prefix': 'patternOpcodeEvent',
            'python_name': 'pattern_opcode_events'
        },
        {
            'prefix': 'conditionalJumpTrigger',
            'python_name': 'conditional_jump_triggers'
        },
        {
            'prefix': 'site',
            'python_name': 'sites'
        },
        {
            'prefix': 'RIOEvent',
            'python_name': 'rio_events'
        },
        {
            'prefix': 'RIOTrigger',
            'python_name': 'rio_triggers'
        }
    ],
    'session_class_description': 'An NI-Digital Pattern Driver session',
    'session_handle_parameter_name': 'vi',
    'uses_nitclk': True
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/metadata/config_addon.py sha256=dbb48ce37f86b47dbe649459416abd1dc304c94836b21645458303d1b6584f14 bytes=453 -->
## FILE: src/nidigital/metadata/config_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nidigital/metadata/config_addon.py`
- sha256: `dbb48ce37f86b47dbe649459416abd1dc304c94836b21645458303d1b6584f14`
- bytes: 453

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.4.10.dev0',
    'latest_runtime_version_tested_against': '2025 Q4',
    'initial_release_year': '2019',
    'custom_types': [
        {
            'ctypes_type': '',
            'file_name': 'history_ram_cycle_information',
            'python_name': 'HistoryRAMCycleInformation'
        }
    ],
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/metadata/enums.py sha256=602aaa303693a703532cece17dfbf6cf0a39a158ae3a7c9d25d3a6b325b92fff bytes=26916 -->
## FILE: src/nidigital/metadata/enums.py

- repository: `ni/nimi-python`
- source_path: `src/nidigital/metadata/enums.py`
- sha256: `602aaa303693a703532cece17dfbf6cf0a39a158ae3a7c9d25d3a6b325b92fff`
- bytes: 26916

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-Digital Pattern Driver API metadata version 24.3.0f175
enums = {
    'BitOrder': {
        'values': [
            {
                'documentation': {
                    'description': 'The most significant bit is first. The first bit is in the 2^n place, where n is the number of bits.'
                },
                'name': 'NIDIGITAL_VAL_MSB_FIRST',
                'value': 2500
            },
            {
                'documentation': {
                    'description': 'The least significant bit is first. The first bit is in the 2^0 place.'
                },
                'name': 'NIDIGITAL_VAL_LSB_FIRST',
                'value': 2501
            }
        ]
    },
    'ConditionalJumpTriggerId': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER0',
                'python_name': 'CONDITIONAL_JUMP_TRIGGER0',
                'value': 'conditionalJumpTrigger0'
            },
            {
                'name': 'NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER1',
                'python_name': 'CONDITIONAL_JUMP_TRIGGER1',
                'value': 'conditionalJumpTrigger1'
            },
            {
                'name': 'NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER2',
                'python_name': 'CONDITIONAL_JUMP_TRIGGER2',
                'value': 'conditionalJumpTrigger2'
            },
            {
                'name': 'NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER3',
                'python_name': 'CONDITIONAL_JUMP_TRIGGER3',
                'value': 'conditionalJumpTrigger3'
            }
        ]
    },
    'DigitalEdge': {
        'values': [
            {
                'documentation': {
                    'description': 'Asserts the trigger when the signal transitions from low level to high level.'
                },
                'name': 'NIDIGITAL_VAL_RISING_EDGE',
                'value': 1800
            },
            {
                'documentation': {
                    'description': 'Asserts the trigger when the signal transitions from high level to low level.'
                },
                'name': 'NIDIGITAL_VAL_FALLING_EDGE',
                'value': 1801
            }
        ]
    },
    'DriveFormat': {
        'values': [
            {
                'documentation': {
                    'description': 'Drive format remains at logic level after each bit.'
                },
                'name': 'NIDIGITAL_VAL_NR',
                'value': 1500
            },
            {
                'documentation': {
                    'description': 'Drive format returns to a logic level low after each bit.'
                },
                'name': 'NIDIGITAL_VAL_RL',
                'value': 1501
            },
            {
                'documentation': {
                    'description': 'Drive format returns to a logic level high after each bit.'
                },
                'name': 'NIDIGITAL_VAL_RH',
                'value': 1502
            },
            {
                'documentation': {
                    'description': 'Drive format returns to the complement logic level of the bit after each bit.'
                },
                'name': 'NIDIGITAL_VAL_SBC',
                'value': 1503
            }
        ]
    },
    'ExportSignal': {
        'values': [
            {
                'documentation': {
                    'description': 'Overrides the start trigger.'
                },
                'name': 'NIDIGITAL_VAL_START_TRIGGER',
                'value': 2000
            },
            {
                'documentation': {
                    'description': 'Specifies to route a conditional jump trigger.'
                },
                'name': 'NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER',
                'value': 2001
            },
            {
                'documentation': {
                    'description': 'Specifies to route a pattern opcode event signal.'
                },
                'name': 'NIDIGITAL_VAL_PATTERN_OPCODE_EVENT',
                'value': 2002
            },
            {
                'name': 'NIDIGITAL_VAL_REF_CLOCK',
                'value': 2003
            },
            {
                'documentation': {
                    'description': 'Specifies to route a RIO event signal.'
                },
                'name': 'NIDIGITAL_VAL_RIO_EVENT',
                'value': 2004
            }
        ]
    },
    'FrequencyMeasurementMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Frequency measurements are made serially for groups of channels associated with a single frequency counter for each group.\n\nMaximum frequency measured: 200 MHz.'
                },
                'name': 'NIDIGITAL_VAL_BANKED',
                'value': 3700
            },
            {
                'documentation': {
                    'description': 'Frequency measurements are made by multiple frequency counters in parallel.\n\nMaximum frequency measured: 100 MHz.'
                },
                'name': 'NIDIGITAL_VAL_PARALLEL',
                'value': 3701
            }
        ]
    },
    'HistoryRAMCyclesToAcquire': {
        'values': [
            {
                'documentation': {
                    'description': 'Acquires failed cycles.'
                },
                'name': 'NIDIGITAL_VAL_FAILED_CYCLES',
                'value': 2303
            },
            {
                'documentation': {
                    'description': 'Acquires all cycles.'
                },
                'name': 'NIDIGITAL_VAL_ALL_CYCLES',
                'value': 2304
            }
        ]
    },
    'HistoryRAMMaxSamplesToAcquirePerSite': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_ACQUIRE_ALL_SAMPLES',
                'value': -1
            }
        ]
    },
    'HistoryRAMTriggerType': {
        'values': [
            {
                'documentation': {
                    'description': 'First Failure History RAM trigger'
                },
                'name': 'NIDIGITAL_VAL_FIRST_FAILURE',
                'value': 2200
            },
            {
                'documentation': {
                    'description': 'Cycle Number History RAM trigger.'
                },
                'name': 'NIDIGITAL_VAL_CYCLE_NUMBER',
                'value': 2201
            },
            {
                'documentation': {
                    'description': 'Pattern Label History RAM trigger'
                },
                'name': 'NIDIGITAL_VAL_PATTERN_LABEL',
                'value': 2202
            }
        ]
    },
    'PPMUApertureTimeUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Unit in seconds.'
                },
                'name': 'NIDIGITAL_VAL_SECONDS',
                'value': 2100
            }
        ]
    },
    'PPMUCurrentLimitBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'Controls output current so that it does not exceed the current limit. Power continues to generate even if the current limit is reached.'
                },
                'name': 'NIDIGITAL_VAL_CURRENT_REGULATE',
                'value': 3100
            }
        ]
    },
    'PPMUMeasurementType': {
        'values': [
            {
                'documentation': {
                    'description': 'The PPMU measures current.'
                },
                'name': 'NIDIGITAL_VAL_MEASURE_CURRENT',
                'value': 2400
            },
            {
                'documentation': {
                    'description': 'The PPMU measures voltage.'
                },
                'name': 'NIDIGITAL_VAL_MEASURE_VOLTAGE',
                'value': 2401
            }
        ]
    },
    'PPMUOutputFunction': {
        'values': [
            {
                'documentation': {
                    'description': 'The PPMU forces voltage to the DUT.'
                },
                'name': 'NIDIGITAL_VAL_DC_VOLTAGE',
                'value': 1300
            },
            {
                'documentation': {
                    'description': 'The PPMU forces current to the DUT.'
                },
                'name': 'NIDIGITAL_VAL_DC_CURRENT',
                'value': 1301
            }
        ]
    },
    'PatternOpcodeEvent': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_PATTERN_OPCODE_EVENT0',
                'value': 'patternOpcodeEvent0'
            },
            {
                'name': 'NIDIGITAL_VAL_PATTERN_OPCODE_EVENT1',
                'value': 'patternOpcodeEvent1'
            },
            {
                'name': 'NIDIGITAL_VAL_PATTERN_OPCODE_EVENT2',
                'value': 'patternOpcodeEvent2'
            },
            {
                'name': 'NIDIGITAL_VAL_PATTERN_OPCODE_EVENT3',
                'value': 'patternOpcodeEvent3'
            }
        ]
    },
    'PinState': {
        'values': [
            {
                'documentation': {
                    'description': 'A digital state of 0.'
                },
                'name': 'NIDIGITAL_VAL_0',
                'pretty_name': '0',
                'python_name': 'ZERO',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'A digital state of 1.'
                },
                'name': 'NIDIGITAL_VAL_1',
                'pretty_name': '1',
                'python_name': 'ONE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'A digital state of L (low).'
                },
                'name': 'NIDIGITAL_VAL_L',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'A digital state of H (high).'
                },
                'name': 'NIDIGITAL_VAL_H',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'A digital state of X (non-drive state).'
                },
                'name': 'NIDIGITAL_VAL_X',
                'value': 5
            },
            {
                'documentation': {
                    'description': 'A digital state of M (midband).'
                },
                'name': 'NIDIGITAL_VAL_M',
                'value': 6
            },
            {
                'documentation': {
                    'description': 'A digital state of V (compare high or low, not midband; store results from capture functionality if configured).'
                },
                'name': 'NIDIGITAL_VAL_V',
                'value': 7
            },
            {
                'documentation': {
                    'description': 'A digital state of D (drive data from source functionality if configured).'
                },
                'name': 'NIDIGITAL_VAL_D',
                'value': 8
            },
            {
                'documentation': {
                    'description': 'A digital state of E (compare data from source functionality if configured).'
                },
                'name': 'NIDIGITAL_VAL_E',
                'value': 9
            },
            {
                'documentation': {
                    'description': 'Not a pin state is used for non-existent DUT cycles.'
                },
                'name': 'NIDIGITAL_VAL_NOT_A_PIN_STATE',
                'pretty_name': 'Not a Pin State',
                'value': 254
            },
            {
                'documentation': {
                    'description': 'Pin state could not be acquired because none of the pins mapped to the instrument in a multi-instrument session had any failures.'
                },
                'name': 'NIDIGITAL_VAL_PIN_STATE_NOT_ACQUIRED',
                'pretty_name': 'Pin State Not Acquired',
                'value': 255
            }
        ]
    },
    'RIOEvent': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_RIO_EVENT0',
                'value': 'RIOEvent0'
            },
            {
                'name': 'NIDIGITAL_VAL_RIO_EVENT1',
                'value': 'RIOEvent1'
            },
            {
                'name': 'NIDIGITAL_VAL_RIO_EVENT2',
                'value': 'RIOEvent2'
            },
            {
                'name': 'NIDIGITAL_VAL_RIO_EVENT3',
                'value': 'RIOEvent3'
            },
            {
                'name': 'NIDIGITAL_VAL_RIO_EVENT4',
                'value': 'RIOEvent4'
            },
            {
                'name': 'NIDIGITAL_VAL_RIO_EVENT5',
                'value': 'RIOEvent5'
            },
            {
                'name': 'NIDIGITAL_VAL_RIO_EVENT6',
                'value': 'RIOEvent6'
            },
            {
                'name': 'NIDIGITAL_VAL_RIO_EVENT7',
                'value': 'RIOEvent7'
            }
        ]
    },
    'RIOTriggerId': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_RIO_TRIGGER0',
                'python_name': 'RIO_TRIGGER0',
                'value': 'RIOTrigger0'
            },
            {
                'name': 'NIDIGITAL_VAL_RIO_TRIGGER1',
                'python_name': 'RIO_TRIGGER1',
                'value': 'RIOTrigger1'
            },
            {
                'name': 'NIDIGITAL_VAL_RIO_TRIGGER2',
                'python_name': 'RIO_TRIGGER2',
                'value': 'RIOTrigger2'
            },
            {
                'name': 'NIDIGITAL_VAL_RIO_TRIGGER3',
                'python_name': 'RIO_TRIGGER3',
                'value': 'RIOTrigger3'
            },
            {
                'name': 'NIDIGITAL_VAL_RIO_TRIGGER4',
                'python_name': 'RIO_TRIGGER4',
                'value': 'RIOTrigger4'
            },
            {
                'name': 'NIDIGITAL_VAL_RIO_TRIGGER5',
                'python_name': 'RIO_TRIGGER5',
                'value': 'RIOTrigger5'
            },
            {
                'name': 'NIDIGITAL_VAL_RIO_TRIGGER6',
                'python_name': 'RIO_TRIGGER6',
                'value': 'RIOTrigger6'
            },
            {
                'name': 'NIDIGITAL_VAL_RIO_TRIGGER7',
                'python_name': 'RIO_TRIGGER7',
                'value': 'RIOTrigger7'
            }
        ]
    },
    'SelectedFunction': {
        'values': [
            {
                'documentation': {
                    'description': 'The pattern sequencer controls the specified pin(s). If a pattern is currently bursting, the pin immediately switches to bursting the pattern. This option disconnects the PPMU.'
                },
                'name': 'NIDIGITAL_VAL_DIGITAL',
                'value': 1100
            },
            {
                'documentation': {
                    'description': 'The PPMU controls the specified pin(s) and connects the PPMU. The pin driver is in a non-drive state, and the active load is disabled. The PPMU does not start sourcing or measuring until Source or Measure(PpmuMeasurementType) is called.'
                },
                'name': 'NIDIGITAL_VAL_PPMU',
                'value': 1101
            },
            {
                'documentation': {
                    'description': 'Puts the digital driver in a non-drive state, disables the active load, disconnects the PPMU, and closes the I/O switch connecting the instrument channel.'
                },
                'name': 'NIDIGITAL_VAL_OFF',
                'value': 1102
            },
            {
                'documentation': {
                    'description': 'The I/O switch connecting the instrument channel is open to the I/O connector. If the PPMU is sourcing, it is stopped prior to opening the I/O switch.'
                },
                'name': 'NIDIGITAL_VAL_DISCONNECT',
                'value': 1103
            },
            {
                'documentation': {
                    'description': 'Yields control of the specified pin(s) to LabVIEW FPGA.'
                },
                'name': 'NIDIGITAL_VAL_RIO',
                'value': 1104
            }
        ]
    },
    'SequencerFlag': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_FLAG0',
                'value': 'seqflag0'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_FLAG1',
                'value': 'seqflag1'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_FLAG2',
                'value': 'seqflag2'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_FLAG3',
                'value': 'seqflag3'
            }
        ]
    },
    'SequencerRegister': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER0',
                'value': 'reg0'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER1',
                'value': 'reg1'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER2',
                'value': 'reg2'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER3',
                'value': 'reg3'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER4',
                'value': 'reg4'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER5',
                'value': 'reg5'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER6',
                'value': 'reg6'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER7',
                'value': 'reg7'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER8',
                'value': 'reg8'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER9',
                'value': 'reg9'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER10',
                'value': 'reg10'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER11',
                'value': 'reg11'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER12',
                'value': 'reg12'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER13',
                'value': 'reg13'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER14',
                'value': 'reg14'
            },
            {
                'name': 'NIDIGITAL_VAL_SEQUENCER_REGISTER15',
                'value': 'reg15'
            }
        ]
    },
    'SiteResultType': {
        'values': [
            {
                'documentation': {
                    'description': 'Pass/fail site result.'
                },
                'name': 'NIDIGITAL_VAL_PASS_FAIL',
                'value': 3300
            },
            {
                'documentation': {
                    'description': 'Capture waveform site result.'
                },
                'name': 'NIDIGITAL_VAL_CAPTURE_WAVEFORM',
                'value': 3301
            }
        ]
    },
    'SoftwareTrigger': {
        'values': [
            {
                'documentation': {
                    'description': 'Overrides the start trigger.'
                },
                'name': 'NIDIGITAL_VAL_START_TRIGGER',
                'value': 2000
            },
            {
                'documentation': {
                    'description': 'Specifies to route a conditional jump trigger.'
                },
                'name': 'NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER',
                'value': 2001
            }
        ]
    },
    'SourceDataMapping': {
        'values': [
            {
                'documentation': {
                    'description': 'Broadcasts the waveform you specify to all sites.'
                },
                'name': 'NIDIGITAL_VAL_BROADCAST',
                'value': 2600
            },
            {
                'documentation': {
                    'description': 'Sources unique waveform data to each site.'
                },
                'name': 'NIDIGITAL_VAL_SITE_UNIQUE',
                'value': 2601
            }
        ]
    },
    'TDREndpointTermination': {
        'values': [
            {
                'documentation': {
                    'description': 'TDR channels are connected to an open circuit.'
                },
                'name': 'NIDIGITAL_VAL_TDR_TO_OPEN',
                'value': 3600
            },
            {
                'documentation': {
                    'description': 'TDR channels are connected to a short to ground.'
                },
                'name': 'NIDIGITAL_VAL_TDR_TO_SHORT_TO_GROUND',
                'value': 3601
            }
        ]
    },
    'TerminationMode': {
        'values': [
            {
                'documentation': {
                    'description': 'The active load provides a constant current to a commutating voltage (Vcom).'
                },
                'name': 'NIDIGITAL_VAL_ACTIVE_LOAD',
                'value': 1200
            },
            {
                'documentation': {
                    'description': 'The pin driver drives Vterm.'
                },
                'name': 'NIDIGITAL_VAL_VTERM',
                'value': 1201
            },
            {
                'documentation': {
                    'description': 'The pin driver is in a non-drive state (in a high-impedance state) and the active load is disabled.'
                },
                'name': 'NIDIGITAL_VAL_HIGH_Z',
                'value': 1202
            }
        ]
    },
    'TimeSetEdgeType': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies the drive on edge of the time set.'
                },
                'name': 'NIDIGITAL_VAL_DRIVE_ON',
                'value': 2800
            },
            {
                'documentation': {
                    'description': 'Specifies the drive data edge of the time set.'
                },
                'name': 'NIDIGITAL_VAL_DRIVE_DATA',
                'value': 2801
            },
            {
                'documentation': {
                    'description': 'Specifies the drive return edge of the time set.'
                },
                'name': 'NIDIGITAL_VAL_DRIVE_RETURN',
                'value': 2802
            },
            {
                'documentation': {
                    'description': 'Specifies the drive off edge of the time set.'
                },
                'name': 'NIDIGITAL_VAL_DRIVE_OFF',
                'value': 2803
            },
            {
                'documentation': {
                    'description': 'Specifies the compare strobe of the time set.'
                },
                'name': 'NIDIGITAL_VAL_COMPARE_STROBE',
                'value': 2804
            },
            {
                'documentation': {
                    'description': 'Specifies the drive data 2 edge of the time set.'
                },
                'name': 'NIDIGITAL_VAL_DRIVE_DATA2',
                'value': 2805
            },
            {
                'documentation': {
                    'description': 'Specifies the drive return 2 edge of the time set.'
                },
                'name': 'NIDIGITAL_VAL_DRIVE_RETURN2',
                'value': 2806
            },
            {
                'documentation': {
                    'description': 'Specifies the compare strobe 2 of the time set.'
                },
                'name': 'NIDIGITAL_VAL_COMPARE_STROBE2',
                'value': 2807
            }
        ]
    },
    'TriggerTerminal': {
        'values': [
            {
                'name': 'NIDIGITAL_VAL_DO_NOT_EXPORT_STR',
                'value': ''
            },
            {
                'name': 'NIDIGITAL_VAL_PXI_TRIG0_STR',
                'value': 'PXI_Trig0'
            },
            {
                'name': 'NIDIGITAL_VAL_PXI_TRIG1_STR',
                'value': 'PXI_Trig1'
            },
            {
                'name': 'NIDIGITAL_VAL_PXI_TRIG2_STR',
                'value': 'PXI_Trig2'
            },
            {
                'name': 'NIDIGITAL_VAL_PXI_TRIG3_STR',
                'value': 'PXI_Trig3'
            },
            {
                'name': 'NIDIGITAL_VAL_PXI_TRIG4_STR',
                'value': 'PXI_Trig4'
            },
            {
                'name': 'NIDIGITAL_VAL_PXI_TRIG5_STR',
                'value': 'PXI_Trig5'
            },
            {
                'name': 'NIDIGITAL_VAL_PXI_TRIG6_STR',
                'value': 'PXI_Trig6'
            },
            {
                'name': 'NIDIGITAL_VAL_PXI_TRIG7_STR',
                'value': 'PXI_Trig7'
            }
        ]
    },
    'TriggerType': {
        'values': [
            {
                'documentation': {
                    'description': 'Disables the start trigger.'
                },
                'name': 'NIDIGITAL_VAL_NONE',
                'value': 1700
            },
            {
                'documentation': {
                    'description': 'Digital edge trigger.'
                },
                'name': 'NIDIGITAL_VAL_DIGITAL_EDGE',
                'value': 1701
            },
            {
                'documentation': {
                    'description': 'Software start trigger.'
                },
                'name': 'NIDIGITAL_VAL_SOFTWARE',
                'value': 1702
            }
        ]
    },
    'WriteStaticPinState': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies to drive low.'
                },
                'name': 'NIDIGITAL_VAL_0',
                'pretty_name': '0',
                'python_name': 'ZERO',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Specifies to drive high.'
                },
                'name': 'NIDIGITAL_VAL_1',
                'pretty_name': '1',
                'python_name': 'ONE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Specifies to not drive.'
                },
                'name': 'NIDIGITAL_VAL_X',
                'value': 5
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/metadata/enums_addon.py sha256=42efadd789827562c3fe0b9491864a7b05be03bcdeeda01001c5b25a6b544650 bytes=185 -->
## FILE: src/nidigital/metadata/enums_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nidigital/metadata/enums_addon.py`
- sha256: `42efadd789827562c3fe0b9491864a7b05be03bcdeeda01001c5b25a6b544650`
- bytes: 185

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/metadata/functions.py sha256=9dc7fa4195dc24600938734b6bc9cda00581d183785cfdad300851f6404c2e85 bytes=212916 -->
## FILE: src/nidigital/metadata/functions.py

- repository: `ni/nimi-python`
- source_path: `src/nidigital/metadata/functions.py`
- sha256: `9dc7fa4195dc24600938734b6bc9cda00581d183785cfdad300851f6404c2e85`
- bytes: 212916

`````python
# -*- coding: utf-8 -*-
# This file is generated from NI-Digital Pattern Driver API metadata version 24.3.0f175
functions = {
    'Abort': {
        'documentation': {
            'description': 'Stops bursting the pattern.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'AbortKeepAlive': {
        'documentation': {
            'description': 'Stops the keep alive pattern if it is currently running. If a pattern burst is in progress, the function aborts the pattern burst. If you start a new pattern burst while a keep alive pattern is running, the keep alive pattern runs to the last keep alive vector, and the new pattern burst starts on the next cycle.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ApplyLevelsAndTiming': {
        'documentation': {
            'description': 'Applies digital levels and timing values defined in previously loaded levels and timing sheets. When applying a levels sheet, only the levels specified in the sheet are affected. Any levels not specified in the sheet remain unchanged. When applying a timing sheet, all existing time sets are deleted before the new time sets are loaded.\n'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Comma-delimited list of strings in the form of ``siteN`` , where ``N`` is the site number. If you enter an empty string, this function applies the levels and initial states to all sites.\n'
                },
                'is_repeated_capability': True,
                'name': 'siteList',
                'repeated_capability_type': 'sites',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Name of the levels sheet to apply. Use the name of the sheet or pass the absolute file path you use in the niDigital_FancyLoadSpecificationsLevelsAndTiming function. The name of the levels sheet is the file name without the directory and file extension.\n'
                },
                'name': 'levelsSheet',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Name of the timing sheet to apply. Use the name of the sheet or pass the absolute file path that you use in the niDigital_FancyLoadSpecificationsLevelsAndTiming function. The name of the timing sheet is the file name without the directory and file extension.\n'
                },
                'name': 'timingSheet',
                'type': 'ViConstString'
            },
            {
                'default_value': 'None',
                'direction': 'in',
                'documentation': {
                    'description': 'Comma-delimited list of pins, pin groups, or channels to initialize to a high state.\n'
                },
                'name': 'initialStateHighPins',
                'python_api_converter_name': 'convert_repeated_capabilities_without_prefix',
                'type': 'ViConstString',
                'type_in_documentation': 'basic sequence types or str'
            },
            {
                'default_value': 'None',
                'direction': 'in',
                'documentation': {
                    'description': 'Comma-delimited list of pins, pin groups, or channels to initialize to a low state.\n'
                },
                'name': 'initialStateLowPins',
                'python_api_converter_name': 'convert_repeated_capabilities_without_prefix',
                'type': 'ViConstString',
                'type_in_documentation': 'basic sequence types or str'
            },
            {
                'default_value': 'None',
                'direction': 'in',
                'documentation': {
                    'description': 'Comma-delimited list of pins, pin groups, or channels to initialize to a non-drive state (X)\n'
                },
                'name': 'initialStateTristatePins',
                'python_api_converter_name': 'convert_repeated_capabilities_without_prefix',
                'type': 'ViConstString',
                'type_in_documentation': 'basic sequence types or str'
            }
        ],
        'repeated_capability_type': 'sites',
        'returns': 'ViStatus'
    },
    'ApplyTDROffsets': {
        'documentation': {
            'description': 'Applies the correction for propagation delay offsets to a digital pattern instrument. Use this function to apply TDR offsets that are stored from a past measurement or are measured by means other than the niDigital_TDR function. Also use this function to apply correction for offsets if the **applyOffsets** input of the niDigital_TDR function was set to False at the time of measurement.\n'
        },
        'grpc_name': 'ApplyTDROffsets',
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of offsets.\n'
                },
                'name': 'numOffsets',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'TDR offsets to apply, in seconds. Specify an offset for each pin or channel in the repeated capabilities. If the repeated capabilities contain pin names, you must specify offsets for each site in the channel map per pin.\n'
                },
                'name': 'offsets',
                'python_api_converter_name': 'convert_timedeltas_to_seconds_real64',
                'size': {
                    'mechanism': 'len',
                    'value': 'numOffsets'
                },
                'type': 'ViReal64[]',
                'type_in_documentation': 'basic sequence of hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'BurstPattern': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Uses the **startLabel** you specify to burst the pattern on the sites you specify and provides the option to wait for the burst to complete. Digital pins retain their state at the end of a pattern burst until the first vector of a subsequent pattern burst, a call to niDigital_WriteStatic, or a call to niDigital_ApplyLevelsAndTiming.\n'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The sites on which to burst the pattern as a comma-delimited list of strings in the form site\\ ``N``, where ``N`` is the site number. If you specify an empty string, the pattern is burst on all sites.\n'
                },
                'is_repeated_capability': True,
                'name': 'siteList',
                'repeated_capability_type': 'sites',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pattern name or exported pattern label from which to start bursting the pattern.\n'
                },
                'name': 'startLabel',
                'type': 'ViConstString'
            },
            {
                'default_value': True,
                'direction': 'in',
                'documentation': {
                    'description': 'A Boolean that specifies whether to select the digital function for the pins in the pattern prior to bursting.\n'
                },
                'name': 'selectDigitalFunction',
                'type': 'ViBoolean'
            },
            {
                'default_value': True,
                'direction': 'in',
                'documentation': {
                    'description': 'A Boolean that indicates whether to wait until the bursting is complete.\n'
                },
                'name': 'waitUntilDone',
                'type': 'ViBoolean'
            },
            {
                'default_value': 'hightime.timedelta(seconds=10.0)',
                'direction': 'in',
                'documentation': {
                    'description': 'Maximum time (in seconds) allowed for this function to complete. If this function does not complete within this time interval, this function returns an error.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'repeated_capability_type': 'sites',
        'returns': 'ViStatus'
    },
    'ClockGenerator_Abort': {
        'documentation': {
            'description': 'Stops clock generation on the specified channel(s) or pin(s) and pin group(s).\n'
        },
        'grpc_name': 'ClockGeneratorAbort',
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelList',
                'type': 'ViConstString'
            }
        ],
        'python_name': 'clock_generator_abort',
        'returns': 'ViStatus'
    },
    'ClockGenerator_GenerateClock': {
        'documentation': {
            'description': 'Configures clock generator frequency and initiates clock generation on the specified channel(s) or pin(s) and pin group(s).\n'
        },
        'grpc_name': 'ClockGeneratorGenerateClock',
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The frequency of the clock generation, in Hz.\n'
                },
                'name': 'frequency',
                'type': 'ViReal64'
            },
            {
                'default_value': True,
                'direction': 'in',
                'documentation': {
                    'description': 'A Boolean that specifies whether to select the digital function for the pins specified prior to starting clock generation.\n'
                },
                'name': 'selectDigitalFunction',
                'type': 'ViBoolean'
            }
        ],
        'python_name': 'clock_generator_generate_clock',
        'returns': 'ViStatus'
    },
    'Commit': {
        'documentation': {
            'description': 'Applies all previously configured pin levels, termination modes, clocks, triggers, and pattern timing to a digital pattern instrument. If you do not call the niDigital_Commit function, then the initiate function or the niDigital_FancyBurstPattern function will implicitly call this function for you. Calling this function moves the session from the Uncommitted state to the Committed state.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureActiveLoadLevels': {
        'documentation': {
            'description': 'Configures I\\ :sub:`OL`, I\\ :sub:`OH`, and V\\ :sub:`COM` levels for the active load on the pins you specify. The DUT sources or sinks current based on the level values. To enable active load, set the termination mode to NIDIGITAL_VAL_ACTIVE_LOAD. To disable active load, set the termination mode of the instrument to NIDIGITAL_VAL_HIGH_Z or NIDIGITAL_VAL_VTERM.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Maximum current that the DUT sinks while outputting a voltage below V\\ :sub:`COM`.\n'
                },
                'name': 'iol',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Maximum current that the DUT sources while outputting a voltage above V\\ :sub:`COM`.\n'
                },
                'name': 'ioh',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Commutating voltage level at which the active load circuit switches between sourcing current and sinking current.\n'
                },
                'name': 'vcom',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePatternBurstSites': {
        'documentation': {
            'description': 'Configures which sites burst the pattern on the next call to the initiate function. The pattern burst sites can also be modified through the repeated capabilities for the niDigital_FancyBurstPattern function. If a site has been disabled through the niDigital_DisableSites function, the site does not burst a pattern even if included in the pattern burst sites.\n'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'A comma-delimited list of strings in the form of site\\ ``N``, where ``N`` is the site number. If you specify an empty string, the function returns pass or fail results for all sites. If the string is empty, all sites are configured for pattern bursting.\n'
                },
                'is_repeated_capability': True,
                'name': 'siteList',
                'repeated_capability_type': 'sites',
                'type': 'ViConstString'
            }
        ],
        'repeated_capability_type': 'sites',
        'returns': 'ViStatus'
    },
    'ConfigureTimeSetCompareEdgesStrobe': {
        'documentation': {
            'description': 'Configures the strobe edge time for the specified pins. Use this function to modify time set values after applying a timing sheet with the niDigital_ApplyLevelsAndTiming function, or to create time sets programmatically without the use of timing sheets. This function does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital_ApplyLevelsAndTiming; it only affects the values of the current timing context.\n'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of pin and pin group names for which to configure the time set edges.\n'
                },
                'is_repeated_capability': True,
                'name': 'pinList',
                'repeated_capability_type': 'pins',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified time set name.\n'
                },
                'grpc_name': 'time_set_name',
                'name': 'timeSet',
                'python_name': 'time_set_name',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Time when the comparison happens within a vector period.\n'
                },
                'name': 'strobeEdge',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'repeated_capability_type': 'pins',
        'returns': 'ViStatus'
    },
    'ConfigureTimeSetCompareEdgesStrobe2x': {
        'documentation': {
            'description': 'Configures the compare strobes for the specified pins in the time set, including the 2x strobe. Use this function to modify time set values after applying a timing sheet with the niDigital_ApplyLevelsAndTiming function, or to create time sets programmatically without the use of timing sheets. This function does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital_ApplyLevelsAndTiming; it only affects the values of the current timing context.\n'
        },
        'grpc_name': 'ConfigureTimeSetCompareEdgesStrobe2x',
        'has_repeated_capability': True,
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of pin and pin group names for which to configure the time set edges.\n'
                },
                'is_repeated_capability': True,
                'name': 'pinList',
                'repeated_capability_type': 'pins',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified time set name.\n'
                },
                'grpc_name': 'time_set_name',
                'name': 'timeSet',
                'python_name': 'time_set_name',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Time when the comparison happens within a vector period.\n'
                },
                'name': 'strobeEdge',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Time when the comparison happens for the second DUT cycle within a vector period.\n'
                },
                'name': 'strobe2Edge',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'repeated_capability_type': 'pins',
        'returns': 'ViStatus'
    },
    'ConfigureTimeSetDriveEdges': {
        'documentation': {
            'description': 'Configures the drive format and drive edge placement for the specified pins. Use this function to modify time set values after applying a timing sheet with the niDigital_ApplyLevelsAndTiming function, or to create time sets programmatically without the use of timing sheets. This function does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital_ApplyLevelsAndTiming; it only affects the values of the current timing context.\n'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of pin and pin group names for which to configure the time set edges.\n'
                },
                'is_repeated_capability': True,
                'name': 'pinList',
                'repeated_capability_type': 'pins',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified time set name.\n'
                },
                'grpc_name': 'time_set_name',
                'name': 'timeSet',
                'python_name': 'time_set_name',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Drive format of the time set.\n\n-   NIDIGITAL_VAL_NR: Non-return.\n-   NIDIGITAL_VAL_RL: Return to low.\n-   NIDIGITAL_VAL_RH: Return to high.\n-   NIDIGITAL_VAL_SBC: Surround by complement.\n'
                },
                'enum': 'DriveFormat',
                'name': 'format',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Delay, in seconds, from the beginning of the vector period for turning on the pin driver.This option applies only when the prior vector left the pin in a non-drive pin state (L, H, X, V, M, E). For the SBC format, this option specifies the delay from the beginning of the vector period at which the complement of the pattern value is driven.\n'
                },
                'name': 'driveOnEdge',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Delay, in seconds, from the beginning of the vector period until the pattern data is driven to the pattern value.The ending state from the previous vector persists until this point.\n'
                },
                'name': 'driveDataEdge',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Delay, in seconds, from the beginning of the vector period until the pin changes from the pattern data to the return value, as specified in the format.\n'
                },
                'name': 'driveReturnEdge',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Delay, in seconds, from the beginning of the vector period to turn off the pin driver when the next vector period uses a non-drive symbol (L, H, X, V, M, E).\n'
                },
                'name': 'driveOffEdge',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'repeated_capability_type': 'pins',
        'returns': 'ViStatus'
    },
    'ConfigureTimeSetDriveEdges2x': {
        'documentation': {
            'description': 'Configures the drive edges of the pins in the time set, including 2x edges. Use this function to modify time set values after applying a timing sheet with the niDigital_ApplyLevelsAndTiming function, or to create time sets programmatically without the use of timing sheets. This function does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital_ApplyLevelsAndTiming; it only affects the values of the current timing context.\n'
        },
        'grpc_name': 'ConfigureTimeSetDriveEdges2x',
        'has_repeated_capability': True,
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of pin and pin group names for which to configure the time set edges.\n'
                },
                'is_repeated_capability': True,
                'name': 'pinList',
                'repeated_capability_type': 'pins',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified time set name.\n'
                },
                'grpc_name': 'time_set_name',
                'name': 'timeSet',
                'python_name': 'time_set_name',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Drive format of the time set.\n\n-   NIDIGITAL_VAL_NR: Non-return.\n-   NIDIGITAL_VAL_RL: Return to low.\n-   NIDIGITAL_VAL_RH: Return to high.\n-   NIDIGITAL_VAL_SBC: Surround by complement.\n'
                },
                'enum': 'DriveFormat',
                'name': 'format',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Delay, in seconds, from the beginning of the vector period for turning on the pin driver.This option applies only when the prior vector left the pin in a non-drive pin state (L, H, X, V, M, E). For the SBC format, this option specifies the delay from the beginning of the vector period at which the complement of the pattern value is driven.\n'
                },
                'name': 'driveOnEdge',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Delay, in seconds, from the beginning of the vector period until the pattern data is driven to the pattern value.The ending state from the previous vector persists until this point.\n'
                },
                'name': 'driveDataEdge',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Delay, in seconds, from the beginning of the vector period until the pin changes from the pattern data to the return value, as specified in the format.\n'
                },
                'name': 'driveReturnEdge',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Delay, in seconds, from the beginning of the vector period to turn off the pin driver when the next vector period uses a non-drive symbol (L, H, X, V, M, E).\n'
                },
                'name': 'driveOffEdge',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Delay, in seconds, from the beginning of the vector period until the pattern data in the second DUT cycle is driven to the pattern value.\n'
                },
                'name': 'driveData2Edge',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Delay, in seconds, from the beginning of the vector period until the pin changes from the pattern data in the second DUT cycle to the return value, as specified in the format.\n'
                },
                'name': 'driveReturn2Edge',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'repeated_capability_type': 'pins',
        'returns': 'ViStatus'
    },
    'ConfigureTimeSetDriveFormat': {
        'documentation': {
            'description': 'Configures the drive format for the pins specified in the **pinList**. Use this function to modify time set values after applying a timing sheet with the niDigital_ApplyLevelsAndTiming function, or to create time sets programmatically without the use of timing sheets. This function does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital_ApplyLevelsAndTiming; it only affects the values of the current timing context.\n'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of pin and pin group names for which to configure the time set edges.\n'
                },
                'is_repeated_capability': True,
                'name': 'pinList',
                'repeated_capability_type': 'pins',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified time set name.\n'
                },
                'grpc_name': 'time_set_name',
                'name': 'timeSet',
                'python_name': 'time_set_name',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Drive format of the time set.\n\n-   NIDIGITAL_VAL_NR: Non-return.\n-   NIDIGITAL_VAL_RL: Return to low.\n-   NIDIGITAL_VAL_RH: Return to high.\n-   NIDIGITAL_VAL_SBC: Surround by complement.\n'
                },
                'enum': 'DriveFormat',
                'name': 'driveFormat',
                'type': 'ViInt32'
            }
        ],
        'repeated_capability_type': 'pins',
        'returns': 'ViStatus'
    },
    'ConfigureTimeSetEdge': {
        'documentation': {
            'description': 'Configures the edge placement for the pins specified in the pin list. Use this function to modify time set values after applying a timing sheet with the niDigital_ApplyLevelsAndTiming function, or to create time sets programmatically without the use of timing sheets. This function does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital_ApplyLevelsAndTiming; it only affects the values of the current timing context.\n'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified digital pattern instrument handle\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of pin and pin group names for which to configure the time set edges.\n'
                },
                'is_repeated_capability': True,
                'name': 'pinList',
                'repeated_capability_type': 'pins',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified time set name.\n'
                },
                'grpc_name': 'time_set_name',
                'name': 'timeSet',
                'python_name': 'time_set_name',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Name of the edge.\n\n-   NIDIGITAL_VAL_DRIVE_ON\n-   NIDIGITAL_VAL_DRIVE_DATA\n-   NIDIGITAL_VAL_DRIVE_RETURN\n-   NIDIGITAL_VAL_DRIVE_OFF\n-   NIDIGITAL_VAL_COMPARE_STROBE\n-   NIDIGITAL_VAL_DRIVE_DATA2\n-   NIDIGITAL_VAL_DRIVE_RETURN2\n-   NIDIGITAL_VAL_COMPARE_STROBE2\n'
                },
                'enum': 'TimeSetEdgeType',
                'name': 'edge',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The time from the beginning of the vector period in which to place the edge.\n'
                },
                'name': 'time',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'repeated_capability_type': 'pins',
        'returns': 'ViStatus'
    },
    'ConfigureTimeSetEdgeMultiplier': {
        'documentation': {
            'description': 'Configures the edge multiplier of the pins in the time set. Use this function to modify time set values after applying a timing sheet with the niDigital_ApplyLevelsAndTiming function, or to create time sets programmatically without the use of timing sheets. This function does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital_ApplyLevelsAndTiming; it only affects the values of the current timing context.\n'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified digital pattern instrument handle\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of pin and pin group names for which to configure the time set edges.\n'
                },
                'is_repeated_capability': True,
                'name': 'pinList',
                'repeated_capability_type': 'pins',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified time set name.\n'
                },
                'grpc_name': 'time_set_name',
                'name': 'timeSet',
                'python_name': 'time_set_name',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified edge multiplier for the pins in the pin list.\n'
                },
                'name': 'edgeMultiplier',
                'type': 'ViInt32'
            }
        ],
        'repeated_capability_type': 'pins',
        'returns': 'ViStatus'
    },
    'ConfigureTimeSetPeriod': {
        'documentation': {
            'description': 'Configures the period of a time set. Use this function to modify time set values after applying a timing sheet with the niDigital_ApplyLevelsAndTiming function, or to create time sets programmatically without the use of timing sheets. This function does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital_ApplyLevelsAndTiming; it only affects the values of the current timing context.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified time set name.\n'
                },
                'grpc_name': 'time_set_name',
                'name': 'timeSet',
                'python_name': 'time_set_name',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Period for this time set, in seconds.\n'
                },
                'name': 'period',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureVoltageLevels': {
        'documentation': {
            'description': 'Configures voltage levels for the pins you specify.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Voltage that the instrument will apply to the input of the DUT when the pin driver drives a logic low (0).\n'
                },
                'name': 'vil',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Voltage that the instrument will apply to the input of the DUT when the test instrument drives a logic high (1).\n'
                },
                'name': 'vih',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Output voltage below which the comparator on the pin driver interprets a logic low (L).\n'
                },
                'name': 'vol',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Output voltage above which the comparator on the pin driver interprets a logic high (H).\n'
                },
                'name': 'voh',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Termination voltage the instrument applies during non-drive cycles when the termination mode is set to V\\ :sub:`term`. The instrument applies the termination voltage through a 50 ohm parallel termination resistance.\n'
                },
                'name': 'vterm',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateCaptureWaveformFromFileDigicapture': {
        'documentation': {
            'description': 'Creates a capture waveform with the configuration information from a Digicapture file generated by the Digital Pattern Editor.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Waveform name you want to use. You must specify waveform_name if the file contains multiple waveforms. Use the waveform_name with the capture_start opcode in your pattern.\n'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Absolute file path to the capture waveform file (.digicapture) you want to load.\n'
                },
                'name': 'waveformFilePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateCaptureWaveformParallel': {
        'documentation': {
            'description': 'Sets the capture waveform settings for parallel acquisition. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.\n'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of capture pins from the waveform. The **pinList** must match the capture pins in the pattern that references the waveform. The pin order in the **pinList** determines the bit positions of the data captured by the niDigital_FetchCaptureWaveform function.\n'
                },
                'is_repeated_capability': True,
                'name': 'pinList',
                'repeated_capability_type': 'pins',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Waveform name you want to use. Use the waveform_name with the capture_start opcode in your pattern.\n'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            }
        ],
        'repeated_capability_type': 'pins',
        'returns': 'ViStatus'
    },
    'CreateCaptureWaveformSerial': {
        'documentation': {
            'description': 'Sets the capture waveform settings for serial acquisition. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.\n'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of capture pins from the waveform. The **pinList** must match the capture pins in the pattern that references the waveform. The pin order in the **pinList** determines the bit positions of the data captured by the niDigital_FetchCaptureWaveform function.\n'
                },
                'is_repeated_capability': True,
                'name': 'pinList',
                'repeated_capability_type': 'pins',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Waveform name you want to use. Use the waveform_name with the capture_start opcode in your pattern.\n'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Width in bits of each serial sample. Valid values are between 1 and 32.\n'
                },
                'name': 'sampleWidth',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Order in which to shift the bits.\n\n-   NIDIGITAL_VAL_MSB_FIRST: Specifies the bit order by most significant bit first.\n-   NIDIGITAL_VAL_LSB_FIRST: Specifies the bit order by least significant bit first.\n'
                },
                'enum': 'BitOrder',
                'name': 'bitOrder',
                'type': 'ViInt32'
            }
        ],
        'repeated_capability_type': 'pins',
        'returns': 'ViStatus'
    },
    'CreateSourceWaveformFromFileTDMS': {
        'documentation': {
            'description': 'Creates a source waveform with configuration information from a TDMS file generated by the Digital Pattern Editor. It also optionally writes waveform data from the file.\n'
        },
        'grpc_name': 'CreateSourceWaveformFromFileTDMS',
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The waveform name you want to use from the file. You must specify waveform_name if the file contains multiple waveforms. Use the waveform_name with the source_start opcode in your pattern.\n'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Absolute file path to the load source waveform file (.tdms).\n'
                },
                'name': 'waveformFilePath',
                'type': 'ViConstString'
            },
            {
                'default_value': True,
                'direction': 'in',
                'documentation': {
                    'description': 'A Boolean that writes waveform data to source memory if True and the waveform data is in the file.\n'
                },
                'name': 'writeWaveformData',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateSourceWaveformParallel': {
        'documentation': {
            'description': 'Sets the source waveform settings required for parallel sourcing. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.\n'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Source pins for the waveform. The **pinList** must match the source pins in the pattern that references the waveform. The pin order in the **pinList** determines the bit positions of the data written by the niDigital_WriteSourceWaveform function.\n'
                },
                'is_repeated_capability': True,
                'name': 'pinList',
                'repeated_capability_type': 'pins',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.\n'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Parameter that specifies how to map data on multiple sites.\n\n-   NIDIGITAL_VAL_BROADCAST: Broadcasts the waveform you specify to all sites.\n-   NIDIGITAL_VAL_SITE_UNIQUE: Sources unique waveform data to each site.\n'
                },
                'enum': 'SourceDataMapping',
                'name': 'dataMapping',
                'type': 'ViInt32'
            }
        ],
        'repeated_capability_type': 'pins',
        'returns': 'ViStatus'
    },
    'CreateSourceWaveformSerial': {
        'documentation': {
            'description': 'Sets the source waveform settings required for serial sourcing. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.\n'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Source pins for the waveform. The **pinList** must match the source pins in the pattern that references the waveform. The pin order in the **pinList** determines the bit positions of the data written by the niDigital_WriteSourceWaveform function.\n'
                },
                'is_repeated_capability': True,
                'name': 'pinList',
                'repeated_capability_type': 'pins',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.\n'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Parameter that specifies how to map data on multiple sites.\n\n-   NIDIGITAL_VAL_BROADCAST: Broadcasts the waveform you specify to all sites.\n-   NIDIGITAL_VAL_SITE_UNIQUE: Sources unique waveform data to each site.\n'
                },
                'enum': 'SourceDataMapping',
                'name': 'dataMapping',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Width in bits of each serial sample. Valid values are between 1 and 32.\n'
                },
                'name': 'sampleWidth',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Order in which to shift the bits.\n\n-   NIDIGITAL_VAL_MSB_FIRST: Specifies the bit order by most significant bit first.\n-   NIDIGITAL_VAL_LSB_FIRST: Specifies the bit order by least significant bit first.\n'
                },
                'enum': 'BitOrder',
                'name': 'bitOrder',
                'type': 'ViInt32'
            }
        ],
        'repeated_capability_type': 'pins',
        'returns': 'ViStatus'
    },
    'CreateTimeSet': {
        'documentation': {
            'description': 'Creates a time set with the name that you specify. Use this function when you want to create time sets programmatically rather than with a timing sheet.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified name of the new time set.\n'
                },
                'name': 'name',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DeleteAllTimeSets': {
        'documentation': {
            'description': 'Deletes all time sets from instrument memory.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableSites': {
        'documentation': {
            'description': 'Disables specified sites. Disabled sites are not included in pattern bursts initiated by the initiate function or the niDigital_FancyBurstPattern function, even if the site is specified in the list of pattern burst sites in niDigital_ConfigurePatternBurstSites function or in the repeated capabilities for the niDigital_FancyBurstPattern function. Additionally, if you specify a list of pin or pin group names in repeated capabilities in any NI-Digital function, digital pattern instrument channels mapped to disabled sites are not affected by the function. The functions that return per-pin data, such as the niDigital_PPMU_Measure function, do not return data for channels mapped to disabled sites. The digital pattern instrument channels mapped to the sites specified are left in their current state. NI TestStand Semiconductor Module requires all sites to always be enabled, and manages the set of active sites without disabling the sites in the digital instrument session. Do not use this function with the Semiconductor Module.\n'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Comma-delimited list of strings in the form of site\\ ``N``, where ``N`` is the site number. If you enter an empty string, the function disables all sites.\n'
                },
                'is_repeated_capability': True,
                'name': 'siteList',
                'repeated_capability_type': 'sites',
                'type': 'ViConstString'
            }
        ],
        'repeated_capability_type': 'sites',
        'returns': 'ViStatus'
    },
    'EnableSites': {
        'documentation': {
            'description': 'Enables the sites you specify. All sites are enabled by default.\n'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Comma-delimited list of strings in the form of site\\ ``N``, where ``N`` is the site number. If you enter an empty string, the function enables all sites.\n'
                },
                'is_repeated_capability': True,
                'name': 'siteList',
                'repeated_capability_type': 'sites',
                'type': 'ViConstString'
            }
        ],
        'repeated_capability_type': 'sites',
        'returns': 'ViStatus'
    },
    'FancySelfTest': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Returns self test results from a digital pattern instrument. This test requires several minutes to execute.\n\nRaises `SelfTestError` on self test failure. Attributes on exception object:\n\n- code - failure code from driver\n- message - status message from driver\n',
            'table_body': [
                [
                    '0',
                    'Self test passed.'
                ],
                [
                    '1',
                    'Self test failed.'
                ]
            ],
            'table_header': [
                'Self-Test Code',
                'Description'
            ]
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_self_test'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': 'self_test',
        'returns': 'ViStatus'
    },
    'FetchCaptureWaveformU32': {
        'codegen_method': 'library-only',
        'documentation': {
            'description': 'Fetches a defined number of samples for a specific list of sites. This function only returns data from sites that are enabled when fetch is called.\n'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Site numbers listed as a comma-delimited list of strings of form site\\ ``N``, where ``N`` is the site number. If you enter an empty string, the function fetches data from all sites.\n'
                },
                'is_repeated_capability': True,
                'name': 'siteList',
                'repeated_capability_type': 'sites',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Waveform name you create with the create capture waveform function. Use the waveform_nam parameter with capture_start opcode in your pattern.\n'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of samples to fetch.\n'
                },
                'name': 'samplesToRead',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Maximum time (in seconds) allowed for this function to complete. If this function does not complete within this time interval, this function returns an error.\n'
                },
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements in the ViUInt32 array you specify for data. To determine the size of the buffer to allocate for the data array, pass a value of 0 to the **dataBufferSize** parameter and a value of VI_NULL to the **data** parameter. In this case, the value returned by the **actualNumWaveforms** and **actualSamplesPerWaveform** parameters determine the size of the array necessary to hold the data. The data buffer size should be the number of samples per waveform multiplied by the number of waveforms.\n'
                },
                'name': 'dataBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'An array of digital states read from the sites in the repeated capabilities. Each row in the array corresponds to a site in the list. If a site is disabled, not enabled for burst, or the current instrument does not include any capture pins, the function does not return data for that site. Data for each site in the repeated capabilities are returned sequentially (non-interleaved). If you are using a list of pin names to read data from multiple instruments, use the niDigital_SortSiteResultsViUInt32Waveform function to order and combine the data to match the repeated capabilities. You can also use the niDigital_GetSiteResultsSiteNumbers function to obtain a list of returned sites.\n'
                },
                'name': 'data',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dataBufferSize',
                    'value_twist': 'actualNumWaveforms'
                },
                'type': 'ViUInt32[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Number of waveforms written to the data array.\n'
                },
                'name': 'actualNumWaveforms',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Number of samples per waveform written to the data array.\n'
                },
                'name': 'actualSamplesPerWaveform',
                'type': 'ViInt32'
            }
        ],
        'repeated_capability_type': 'sites',
        'returns': 'ViStatus'
    },
    'FetchHistoryRAMCycleInformation': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Gets the per-cycle pattern information acquired for the specified cycle.\n'
        },
        'grpc_name': 'FetchHistoryRAMCycleInformation',
        'has_repeated_capability': True,
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Site specified as a string in the form of ``siteN``, where ``N`` is the site number. The function returns an error if more than one site is specified.\n'
                },
                'is_repeated_capability': True,
                'name': 'site',
                'repeated_capability_type': 'sites',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The index of the History RAM sample to fetch. Each History RAM sample contains information about a single cycle in the pattern burst.\n'
                },
                'name': 'sampleIndex',
                'type': 'ViInt64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned index of the pattern for the acquired cycle. Use niDigital_GetPatternName to get the name of the pattern from its index.\n'
                },
                'name': 'patternIndex',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned time set for the acquired cycle. Use niDigital_GetTimeSetName to get the name of the time set from its index.\n'
                },
                'name': 'timeSetIndex',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned vector number within the pattern for the acquired cycle. Vector numbers start at 0 from the beginning of the pattern.\n'
                },
                'name': 'vectorNumber',
                'type': 'ViInt64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the cycle number acquired by this History RAM sample. Cycle numbers start at 0 from the beginning of the pattern burst.\n'
                },
                'name': 'cycleNumber',
                'type': 'ViInt64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned number of DUT cycles contained in the cycle acquired by this History RAM sample. This is only needed if the pattern uses the edge multiplier feature.\n'
                },
                'name': 'numDutCycles',
                'type': 'ViInt32'
            }
        ],
        'repeated_capability_type': 'sites',
        'returns': 'ViStatus'
    },
    'FetchHistoryRAMCyclePinData': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Gets the per-pin pattern data acquired for the specified cycle.\n'
        },
        'grpc_name': 'FetchHistoryRAMCyclePinData',
        'has_repeated_capability': True,
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Site specified as a string in the form of ``siteN``, where ``N`` is the site number. The function returns an error if more than one site is specified.\n'
                },
                'is_repeated_capability': True,
                'name': 'site',
                'repeated_capability_type': 'sites',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified pins for which to retrieve History RAM data. If empty, the pin list from the pattern containing the start label is used. Call niDigital_GetPatternPinList or niDigital_GetPatternPinIndexeswith the start label to retrieve the pins associated with the pattern burst.\n'
                },
                'name': 'pinList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The index of the History RAM sample to fetch. Each History RAM sample contains information about a single cycle in the pattern burst.\n'
                },
                'name': 'sampleIndex',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified index of the DUT cycle. If the pattern does not use the edge multiplier feature, pass 0 for this parameter. For History RAM samples that contain multiple DUT cycles, indicated by the **numDutCycles** value returned by niDigital_FetchHistoryRAMCycleInformation, call this function multiple times to retrieve pin states for each DUT cycle. The DUT cycle index should start at 0.\n'
                },
                'name': 'dutCycleIndex',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified number of elements in the **expectedPinStates**, **actualPinStates**, and **perPinPassFail** arrays. All three array parameters must be of the same size if they are not set to VI_NULL.\n\nTo determine the size of the buffer to allocate for the arrays, pass a value of 0 to the **pinDataBufferSize** parameter and a value of VI_NULL to the array parameters. In this case, the value returned by the **actualNumPinData** parameter is the size of the arrays necessary to hold the data.\n'
                },
                'name': 'pinDataBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned pin state as expected by the loaded pattern in the order specified in **pinList**. Pins without defined edges in the specified DUT cycle will return NIDIGITAL_VAL_NOT_A_PIN_STATE\n'
                },
                'enum': 'PinState',
                'name': 'expectedPinStates',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'pinDataBufferSize',
                    'value_twist': 'actualNumPinData'
                },
                'type': 'ViUInt8[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned pin state acquired by History RAM in the order specified in **pinList**. Pins without defined edges in the specified DUT cycle will return NIDIGITAL_VAL_NOT_A_PIN_STATE\n'
                },
                'enum': 'PinState',
                'name': 'actualPinStates',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'pinDataBufferSize',
                    'value_twist': 'actualNumPinData'
                },
                'type': 'ViUInt8[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned pass fail information for pins in the order specified in **pinList**. Pins without defined edges in the specified DUT cycle will return pass (VI_TRUE).\n'
                },
                'name': 'perPinPassFail',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'pinDataBufferSize',
                    'value_twist': 'actualNumPinData'
                },
                'type': 'ViBoolean[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Number of values written to the array parameters.\n'
                },
                'name': 'actualNumPinData',
                'type': 'ViInt32'
            }
        ],
        'repeated_capability_type': 'sites',
        'returns': 'ViStatus'
    },
    'FetchHistoryRAMScanCycleNumber': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Fetches the History RAM Scan Cycle Number for the sample index. If the sample is not from a scan vector, the scan cycle number will be returned as -1.\n'
        },
        'grpc_name': 'FetchHistoryRAMScanCycleNumber',
        'has_repeated_capability': True,
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Site specified as a string in the form of ``siteN``, where ``N`` is the site number. The function returns an error if more than one site is specified.\n'
                },
                'is_repeated_capability': True,
                'name': 'site',
                'repeated_capability_type': 'sites',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The index of the History RAM sample to fetch. Each History RAM sample contains information about a single cycle in the pattern burst.\n'
                },
                'name': 'sampleIndex',
                'type': 'ViInt64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the scan cycle number acquired by this History RAM sample. Scan cycle numbers start at 0 from the first cycle of the scan vector. Scan cycle numbers are -1 for cycles that do not have a scan opcode.\n'
                },
                'name': 'scanCycleNumber',
                'type': 'ViInt64'
            }
        ],
        'repeated_capability_type': 'sites',
        'returns': 'ViStatus'
    },
    'FrequencyCounter_MeasureFrequency': {
        'documentation': {
            'description': 'Measures the frequency on the specified channel(s) over the specified measurement time. All channels in the repeated capabilities should have the same measurement time.\n'
        },
        'grpc_name': 'FrequencyCounterMeasureFrequency',
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified number of elements in the ViReal64 array you specify for the frequency counter measurements.\n'
                },
                'name': 'frequenciesBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned frequency counter measurement, in Hz.This function returns -1 if the measurement is invalid for the channel.\n'
                },
                'name': 'frequencies',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'frequenciesBufferSize',
                    'value_twist': 'actualNumFrequencies'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned number of frequency counter measurements written to the measurements array.\n'
                },
                'name': 'actualNumFrequencies',
                'type': 'ViInt32'
            }
        ],
        'python_name': 'frequency_counter_measure_frequency',
        'returns': 'ViStatus'
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Queries the value of a ViBoolean attribute. Use this function to get the values of digital pattern instrument-specific attributes and inherent IVI attributes.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.\n'
                },
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned current value of the attribute; pass the address of a ViBoolean variable.\n'
                },
                'name': 'value',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt32': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Queries the value of a ViInt32 attribute. Use this function to get the values of digital pattern instrument-specific attributes and inherent IVI attributes.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.\n'
                },
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned current value of the attribute; pass the address of a ViInt32 variable.\n'
                },
                'name': 'value',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt64': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Queries the value of a ViInt64 attribute. Use this function to get the values of digital pattern instrument-specific attributes and inherent IVI attributes.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.\n'
                },
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned current value of the attribute; pass the address of a ViInt64 variable.\n'
                },
                'name': 'value',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'This function queries the value of a ViReal64 attribute. Use this function to get the values of digital pattern instrument-specific attributes and inherent IVI attributes.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.\n'
                },
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned current value of the attribute; pass the address of a ViReal64 variable.\n'
                },
                'name': 'value',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Queries the value of a ViString attribute. Use this function to get the values of digital pattern instrument-specific attributes and inherent IVI attributes. You must provide a ViChar array to serve as a buffer for the value. You pass the number of bytes in the buffer as the **bufferSize**. If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **bufferSize**, the function copies (bufferSize - 1) bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the **bufferSize** you must pass to get the entire value. For example, if the value is "123456" and the **bufferSize** is 4, the function places "123" into the buffer and returns 7. If you want to call this function just to get the required buffer size, you can pass 0 for the **bufferSize** and VI_NULL for the value.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.\n'
                },
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements in the ViChar array you specify for value.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The buffer in which the function returns the current value of the attribute; the buffer must be of type ViChar and have at least as many bytes as indicated in the **bufferSize**.\n'
                },
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
    'GetChannelNameFromString': {
        'documentation': {
            'description': 'Returns a list of channel names for given channel indices.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Index list for the channels in the session. Valid values are from zero to the total number of channels in the session minus one. The index string can be one of the following formats:\n\n-   A comma-separated list—for example, "0,2,3,1"\n-   A range using a hyphen—for example, "0-3"\n-   A range using a colon—for example, "0:3 "\n\nYou can combine comma-separated lists and ranges that use a hyphen or colon. Both out-of-order and repeated indices are supported ("2,3,0", "1,2,2,3"). White space characters, including spaces, tabs, feeds, and carriage returns, are allowed between characters. Ranges can be incrementing or decrementing.\n'
                },
                'grpc_name': 'indices',
                'name': 'index',
                'python_api_converter_name': 'convert_repeated_capabilities_without_prefix',
                'python_name': 'indices',
                'type': 'ViConstString',
                'type_in_documentation': 'basic sequence types, str, or int'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements in the ViChar array you specify for name.\n'
                },
                'name': 'nameBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The channel name(s) at the specified indices.\n'
                },
                'grpc_name': 'names',
                'name': 'name',
                'python_api_converter_name': 'convert_comma_separated_string_to_list',
                'python_name': 'names',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'nameBufferSize'
                },
                'type': 'ViChar[]',
                'type_in_documentation': 'list of str'
            }
        ],
        'python_name': 'get_channel_names',
        'render_in_session_base': True,
        'returns': 'ViStatus'
    },
    'GetError': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the error information associated with the digital pattern instrument handle. This function retrieves and then clears the error information for the session. If **vi** is VI_NULL, this function retrieves and then clears the error information for the current thread. You must provide a ViChar array to serve as a buffer for the value. You pass the number of bytes in the buffer as the buffer size. If the current value of the error description, including the terminating NULL byte, is larger than the size you indicate in the buffer size, the function copies (buffer size -1) bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. If you want to call this function just to get the required buffer size, you can pass 0 for the buffer size and VI_NULL for **errorDescription**.\n'
        },
        'included_in_proto': True,
        'is_error_handling': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'none'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned error code for the session or execution thread.\n'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements in the ViChar array you specify for **errorDescription**.\n'
                },
                'name': 'errorDescriptionBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned error description for the IVI session or execution thread.\nIf there is no description, the function returns an empty string. The buffer must contain at least as many elements as the value you specify with the buffer size parameter.\nIf you pass 0 for **errorDescriptionBufferSize**, you can pass VI_NULL for this parameter.\n'
                },
                'name': 'errorDescription',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'errorDescriptionBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'GetFailCount': {
        'documentation': {
            'description': 'Returns the comparison fail count for pins in the repeated capabilities.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements in the ViInt64 array you specify for **failureCount**. To determine the size of the buffer to allocate for the **failureCount** array, pass a value of 0 to the **bufferSize** parameter and a value of VI_NULL to the **failureCount** parameter. In this case, the value returned by the **actualNumRead** parameter is the size of the array necessary to hold the failure counts.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Number of failures in an array. If a site is disabled or not enabled for burst, the function does not return data for that site. You can also use the niDigital_FancyGetPinResultsPinInformation function to obtain a sorted list of returned sites and channels.\n'
                },
                'name': 'failureCount',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualNumRead'
                },
                'type': 'ViInt64[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Number of failure count values written to the **failureCount** array.\n'
                },
                'name': 'actualNumRead',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetHistoryRAMSampleCount': {
        'documentation': {
            'description': 'Returns the number of samples History RAM acquired on the last pattern burst.\n',
            'note': '\nBefore bursting a pattern, you must configure the History RAM trigger and specify which cycles to acquire.\n\nNIDIGITAL_ATTR_HISTORY_RAM_TRIGGER_TYPE should be used to specify the trigger condition on which History RAM\nstarts acquiring pattern information.\n\nIf History RAM trigger is configured as NIDIGITAL_VAL_CYCLE_NUMBER,\nNIDIGITAL_ATTR_CYCLE_NUMBER_HISTORY_RAM_TRIGGER_CYCLE_NUMBER should be used to specify the cycle number on which\nHistory RAM starts acquiring pattern information.\n\nIf History RAM trigger is configured as NIDIGITAL_VAL_PATTERN_LABEL,\nNIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_LABEL should be used to specify the pattern label from which to\nstart acquiring pattern information.\nNIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_VECTOR_OFFSET should be used to specify the number of vectors\nfollowing the specified pattern label from which to start acquiring pattern information.\nNIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_CYCLE_OFFSET should be used to specify the number of cycles\nfollowing the specified pattern label and vector offset from which to start acquiring pattern information.\n\nFor all History RAM trigger conditions, NIDIGITAL_ATTR_HISTORY_RAM_PRETRIGGER_SAMPLES should be used to specify\nthe number of samples to acquire before the trigger conditions are met. If you configure History RAM to only\nacquire failed cycles, you must set NIDIGITAL_ATTR_HISTORY_RAM_PRETRIGGER_SAMPLES to 0.\n\nNIDIGITAL_ATTR_HISTORY_RAM_CYCLES_TO_ACQUIRE should be used to specify which cycles History RAM acquires after\nthe trigger conditions are met.\n'
        },
        'grpc_name': 'GetHistoryRAMSampleCount',
        'has_repeated_capability': True,
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Site specified as a string in the form of ``siteN``, where ``N`` is the site number. The function returns an error if more than one site is specified.\n'
                },
                'is_repeated_capability': True,
                'name': 'site',
                'repeated_capability_type': 'sites',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned number of samples that History RAM acquired.\n'
                },
                'name': 'sampleCount',
                'type': 'ViInt64'
            }
        ],
        'repeated_capability_type': 'sites',
        'returns': 'ViStatus'
    },
    'GetPatternName': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'TBD'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'patternIndex',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'nameBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'name',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'nameBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'render_in_session_base': True,
        'returns': 'ViStatus'
    },
    'GetPatternPinList': {
        'documentation': {
            'description': 'Returns the pattern pin list.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pattern name or exported pattern label from which to get the pin names that the pattern references.\n'
                },
                'name': 'startLabel',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements in the ViChar array you specify for **pinList**.\n'
                },
                'name': 'pinListBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'List of pins referenced by the pattern with the **startLabel**.\n'
                },
                'name': 'pinList',
                'python_api_converter_name': 'convert_comma_separated_string_to_list',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'pinListBufferSize'
                },
                'type': 'ViChar[]',
                'type_in_documentation': 'list of str'
            }
        ],
        'python_name': 'get_pattern_pin_names',
        'returns': 'ViStatus'
    },
    'GetPinName': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the name of the pin at the index you specify. You must provide a ViChar array to serve as a buffer for the value. You pass the number of bytes in the buffer as the **nameBufferSize**. If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the buffer size, the function copies (buffer size - 1) bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. If you want to call this function just to get the required buffer size, you can pass 0 for **nameBufferSize** and VI_NULL for the name.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Index of pin to query. Pin indexes begin at 0.\n'
                },
                'name': 'pinIndex',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements in the ViChar array you specify for name.\n'
                },
                'name': 'nameBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the pin name at the specified **pinIndex**.\n'
                },
                'name': 'name',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'nameBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'render_in_session_base': True,
        'returns': 'ViStatus'
    },
    'GetPinResultsPinInformation': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the pin names, site numbers, and channel names that correspond to per-pin data read from the digital pattern instrument. The function returns pin information in the same order as values read using the niDigital_ReadStatic function, niDigital_PPMU_Measure function, and niDigital_GetFailCount function. Use this function to match values the previously listed functions return with pins, sites, and instrument channels.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements in the arrays you specify for **pinIndexes**, **siteNumbers**, and **channelIndexes**, if they are not NULL. To determine the size of the buffer to allocate for the arrays, pass a value of 0 to the **bufferSize** parameter and a value of VI_NULL to the array parameters. In this case, the value returned by the **actualNumValues** parameter is the size of the arrays necessary to hold the output values.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned index of the pins corresponding to data read from the digital pattern instrument using the specified repeated capabilities. If you do not want to use this parameter, pass VI_NULL.\nCall niDigital_GetPinName to get the name of the pin associated with an index.\n'
                },
                'name': 'pinIndexes',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualNumValues'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned site numbers that correspond to data read from the digital pattern instrument using the specified repeated capabilities. If you do not want to use this parameter, pass VI_NULL.\n'
                },
                'name': 'siteNumbers',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualNumValues'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned index of channels corresponding to data read from the digital pattern instrument using the specified repeated capabilities. If you do not want to use this parameter, pass VI_NULL.\nCall niDigital_GetChannelName to get the name of the channel associated with an index. Channel indexes are one-based.\n'
                },
                'name': 'channelIndexes',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualNumValues'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The number of values written to the output arrays. This function always writes the same number of values to all output arrays, if they are not set to VI_NULL.\n'
                },
                'name': 'actualNumValues',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSitePassFail': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the pass or fail results for each site.\n'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'A comma-delimited list of strings in the form of site\\ ``N``, where ``N`` is the site number. If you specify an empty string, the function returns pass or fail results for all sites.\n'
                },
                'is_repeated_capability': True,
                'name': 'siteList',
                'repeated_capability_type': 'sites',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements in the ViBoolean array you specify for **passFail**. To determine the size of the buffer to allocate for the **passFail** array, pass a value of 0 to the **passFailBufferSize** parameter and a value of VI_NULL to the **passFail** parameter. In this case, the value returned by the **actualNumSites** parameter is the size of the array necessary to hold the pass/fail values.\n'
                },
                'name': 'passFailBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned array of pass (VI_TRUE) and fail results for the sites you specify in the repeated capabilities. If sites span multiple digital pattern instruments, you must use an AND operator for the partial results for those sites returned by each instrument. If a site is disabled or not enabled for burst, the function does not return data for that site. Use the niDigital_SortSiteResultsViBoolean function to order and combine the data to match the repeated capabilities. You can also use the niDigital_GetSiteResultsSiteNumbers function to determine the order of the sites returned from this function call so that you can match the pass array with site numbers.\n'
                },
                'name': 'passFail',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'passFailBufferSize',
                    'value_twist': 'actualNumSites'
                },
                'type': 'ViBoolean[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Number of values written to the **passFailBufferSize** and **passFail** arrays.\n'
                },
                'name': 'actualNumSites',
                'type': 'ViInt32'
            }
        ],
        'repeated_capability_type': 'sites',
        'returns': 'ViStatus'
    },
    'GetSiteResultsSiteNumbers': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the site numbers that correspond to per-site data read from the digital pattern instrument. The function returns site numbers in the same order as values read using the niDigital_GetSitePassFail and niDigital_FetchCaptureWaveformU32 functions. Use this function to match values the previously listed functions return with site numbers.\n'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Site numbers listed as a comma-delimited list of strings of form site\\ ``N``, where ``N`` is the site number.\n'
                },
                'is_repeated_capability': True,
                'name': 'siteList',
                'repeated_capability_type': 'sites',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The type of data specified in the results array.\n\n-   NIDIGITAL_VAL_PASS_FAIL: Get site numbers for pass/fail data.\n-   NIDIGITAL_VAL_CAPTURE_WAVEFORM: Get site numbers for capture waveforms.\n'
                },
                'enum': 'SiteResultType',
                'name': 'siteResultType',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements in the ViInt32 array you specify for **siteNumbers**. To determine the size of the buffer to allocate for the **siteNumbers** array, pass a value of 0 to the **siteNumbersBufferSize** parameter and a value of VI_NULL to the **siteNumbers** parameter. In this case, the value returned by the **actualNumSiteNumbers** parameter is the size of the array necessary to hold the site numbers.\n'
                },
                'name': 'siteNumbersBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned array of site numbers that correspond to the values specified by **siteResultType**.\n'
                },
                'name': 'siteNumbers',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'siteNumbersBufferSize',
                    'value_twist': 'actualNumSiteNumbers'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Number of sites written in the **siteNumbers** array.\n'
                },
                'name': 'actualNumSiteNumbers',
                'type': 'ViInt32'
            }
        ],
        'repeated_capability_type': 'sites',
        'returns': 'ViStatus'
    },
    'GetTimeSetDriveFormat': {
        'documentation': {
            'description': 'Returns the drive format of a pin in the specified time set.\n'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified digital pattern instrument handle\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Name of the specified pin.\n'
                },
                'is_repeated_capability': True,
                'name': 'pin',
                'repeated_capability_type': 'pins',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified time set name.\n'
                },
                'grpc_name': 'time_set_name',
                'name': 'timeSet',
                'python_name': 'time_set_name',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returned drive format of the time set for the specified pin.\n'
                },
                'enum': 'DriveFormat',
                'name': 'format',
                'type': 'ViInt32'
            }
        ],
        'repeated_capability_type': 'pins',
        'returns': 'ViStatus'
    },
    'GetTimeSetEdge': {
        'documentation': {
            'description': 'Returns the edge time of a pin in the specified time set.\n'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified digital pattern instrument handle\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Name of the specified pin.\n'
                },
                'is_repeated_capability': True,
                'name': 'pin',
                'repeated_capability_type': 'pins',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified time set name.\n'
                },
                'grpc_name': 'time_set_name',
                'name': 'timeSet',
                'python_name': 'time_set_name',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Name of the edge.\n\n-   NIDIGITAL_VAL_DRIVE_ON\n-   NIDIGITAL_VAL_DRIVE_DATA\n-   NIDIGITAL_VAL_DRIVE_RETURN\n-   NIDIGITAL_VAL_DRIVE_OFF\n-   NIDIGITAL_VAL_COMPARE_STROBE\n-   NIDIGITAL_VAL_DRIVE_DATA2\n-   NIDIGITAL_VAL_DRIVE_RETURN2\n-   NIDIGITAL_VAL_COMPARE_STROBE2\n'
                },
                'enum': 'TimeSetEdgeType',
                'name': 'edge',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Time from the beginning of the vector period in which to place the edge.\n'
                },
                'name': 'time',
                'python_api_converter_name': 'convert_seconds_real64_to_timedelta',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta'
            }
        ],
        'repeated_capability_type': 'pins',
        'returns': 'ViStatus'
    },
    'GetTimeSetEdgeMultiplier': {
        'documentation': {
            'description': 'Returns the edge multiplier of the specified time set.\n'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Name of the specified pin.\n'
                },
                'is_repeated_capability': True,
                'name': 'pin',
                'repeated_capability_type': 'pins',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified time set name.\n'
                },
                'grpc_name': 'time_set_name',
                'name': 'timeSet',
                'python_name': 'time_set_name',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returned edge multiplier of the time set for the specified pin.\n'
                },
                'name': 'edgeMultiplier',
                'type': 'ViInt32'
            }
        ],
        'repeated_capability_type': 'pins',
        'returns': 'ViStatus'
    },
    'GetTimeSetName': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'TBD'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'timeSetIndex',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'nameBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'name',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'nameBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'render_in_session_base': True,
        'returns': 'ViStatus'
    },
    'GetTimeSetPeriod': {
        'documentation': {
            'description': 'Returns the period of the specified time set.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified digital pattern instrument handle\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified time set name.\n'
                },
                'grpc_name': 'time_set_name',
                'name': 'timeSet',
                'python_name': 'time_set_name',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returned period, in seconds, that the edge is configured to.\n'
                },
                'name': 'period',
                'python_api_converter_name': 'convert_seconds_real64_to_timedelta',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitWithOptions': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Creates and returns a new session to the specified digital pattern instrument to use in all subsequent function calls. To place the instrument in a known startup state when creating a new session, set the reset parameter to VI_TRUE, which is equivalent to calling the niDigital_reset function immediately after initializing the session.\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': '__init__',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'initialization_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified resource name shown in Measurement & Automation Explorer (MAX) for a digital pattern instrument, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. **resourceName** can also be a logical IVI name. This parameter accepts a comma-delimited list of strings in the form PXI1Slot2,PXI1Slot3, where ``PXI1Slot2`` is one instrument resource name and ``PXI1Slot3`` is another. When including more than one digital pattern instrument in the comma-delimited list of strings, list the instruments in the same order they appear in the pin map.\n\n+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+\n| |Note| | Note\xa0\xa0 You only can specify multiple instruments of the same model. For example, you can list two PXIe-6570s but not a PXIe-6570 and PXIe-6571. The instruments must be in the same chassis. |\n+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+\n\n.. |Note| image:: note.gif\n',
                    'note': '\n'
                },
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': 'A Boolean that verifies that the digital pattern instrument you initialize is supported by NI-Digital. NI-Digital automatically performs this query, so setting this parameter is not necessary.\n'
                },
                'name': 'idQuery',
                'type': 'ViBoolean',
                'use_in_python_api': False
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': 'A Boolean that specifies whether to reset a digital pattern instrument to a known state when the session is initialized. Setting the **resetDevice** value to VI_TRUE is equivalent to calling the niDigital_reset function immediately after initializing the session.\n'
                },
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'default_value': '""',
                'direction': 'in',
                'documentation': {
                    'description': 'The initial values of certain properties for the NI-Digital Pattern Driver session. The string can be empty. You can use the DriverSetup flag to simulate a digital pattern instrument. When simulating a digital pattern instrument, you must specify the model you want to simulate. For example, Simulate = 1, DriverSetup = Model:6570.\n'
                },
                'name': 'optionString',
                'python_api_converter_name': 'convert_init_with_options_dictionary',
                'type': 'ViConstString',
                'type_in_documentation': 'dict'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned instrument session.\n'
                },
                'grpc_name': 'vi',
                'name': 'newVi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'Initiate': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Starts bursting the pattern configured by NIDIGITAL_ATTR_START_LABEL, causing the NI-Digital session to be committed. To stop the pattern burst, call niDigital_Abort. If keep alive pattern is bursting when niDigital_Abort is called or upon exiting the context manager, keep alive pattern will not be stopped. To stop the keep alive pattern, call niDigital_AbortKeepAlive.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'IsDone': {
        'documentation': {
            'description': 'Checks the hardware to determine if the pattern burst has completed or if any errors have occurred.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'A Boolean that indicates whether the pattern burst completed.\n'
                },
                'name': 'done',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'IsSiteEnabled': {
        'documentation': {
            'description': 'Checks if a specified site is enabled.\n',
            'note': 'The function returns an error if more than one site is specified.\n'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Site specified as a string in the form of ``siteN``, where ``N`` is the site number. The function returns an error if more than one site is specified.\n'
                },
                'is_repeated_capability': True,
                'name': 'site',
                'repeated_capability_type': 'sites',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Boolean value that returns whether the site is enabled or disabled.\n'
                },
                'name': 'enable',
                'type': 'ViBoolean'
            }
        ],
        'repeated_capability_type': 'sites',
        'returns': 'ViStatus'
    },
    'LoadLevels': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Loads a levels sheet from a specified file.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Absolute file path to the specified levels sheet file.\n'
                },
                'grpc_name': 'file_path',
                'name': 'levelsFilePath',
                'python_name': 'file_path',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'LoadPattern': {
        'documentation': {
            'description': 'Loads the specified pattern file.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Absolute file path of the binary .digipat pattern file to load. Specify the pattern to burst using NIDIGITAL_ATTR_START_LABEL or the start_label parameter of the niDigital_FancyBurstPattern function.\n'
                },
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'LoadPinMap': {
        'documentation': {
            'description': 'Loads a pin map file. You can load only a single pin and channel map file during an NI-Digital Pattern Driver session. To switch pin maps, create a new session or call the niDigital_reset function.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Absolute file path to a pin map file created with the Digital Pattern Editor or the NI TestStand Semiconductor Module.\n'
                },
                'grpc_name': 'file_path',
                'name': 'pinMapFilePath',
                'python_name': 'file_path',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'LoadSpecifications': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Loads a specifications sheet from a specified file.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Absolute file path to a specifications file.\n'
                },
                'grpc_name': 'file_path',
                'name': 'specificationsFilePath',
                'python_name': 'file_path',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'LoadTiming': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Loads a timing sheet from a specified file.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Absolute file path to the specified timing sheet file.\n'
                },
                'grpc_name': 'file_path',
                'name': 'timingFilePath',
                'python_name': 'file_path',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'LockSession': {
        'documentation': {
            'description': 'Obtains the multithreaded lock on the instrument session. Before doing so, the function waits until all other execution threads have released the lock on the instrument session. Other threads might have obtained the lock on this session in the following ways: niDigital_LockSession After the call to niDigital_LockSession returns successfully, no other threads can access the instrument session until you call niDigital_UnlockSession. Use niDigital_LockSession and niDigital_UnlockSession around a sequence of calls to instrument driver functions if you require exclusive access through the end of the sequence. You can safely make nested calls to niDigital_LockSession within the same thread. To completely unlock the session, you must balance each call to niDigital_LockSession with a call to niDigital_UnlockSession. If, however, you use the **callerHasLock** parameter in all calls to niDigital_LockSession and niDigital_UnlockSession within a function, the IVI Library locks the session only once within the function, regardless of the number of calls you make to niDigital_LockSession. This functionality allows you to call niDigital_UnlockSession just once at the end of the function.\n'
        },
        'included_in_proto': False,
        'method_templates': [
            {
                'documentation_filename': 'lock',
                'library_interpreter_filename': 'lock',
                'method_python_name_suffix': '',
                'session_filename': 'lock'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'This parameter serves as a convenience. If you do not want to use this parameter, pass VI_NULL. You can use this parameter in complex functions to track lock status and the need to unlock the session. Pass the address of a local ViBoolean variable in the declaration of the local variable and initialize it to VI_FALSE. Also, pass the address of the same local variable to any other calls you make to niDigital_LockSession or niDigital_UnlockSession in the same function.\n'
                },
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'python_name': 'lock',
        'render_in_session_base': True,
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'PPMU_Measure': {
        'documentation': {
            'description': 'Instructs the PPMU to measure voltage or current. This function can be called to take a voltage measurement even if the pin function is not set to PPMU.\n'
        },
        'grpc_name': 'PPMUMeasure',
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Parameter that specifies whether the PPMU measures voltage or current from the DUT.\n\n-   NIDIGITAL_VAL_MEASURE_CURRENT: The PPMU measures current from the DUT.\n-   NIDIGITAL_VAL_MEASURE_VOLTAGE: The PPMU measures voltage from the DUT.\n'
                },
                'enum': 'PPMUMeasurementType',
                'name': 'measurementType',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements in the ViReal64 array you specify for measurements. To determine the size of the buffer to allocate for the measurements array, pass a value of 0 to the **bufferSize** parameter and a value of VI_NULL to the **measurements** parameter. In this case, the value returned by the **actualNumRead** parameter is the size of the array necessary to hold the measurements.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned array of measurements in the order you specify in the repeated capabilities. If a site is disabled, the function does not return data for that site. You can also use the niDigital_FancyGetPinResultsPinInformation function to obtain a sorted list of returned sites and channels.\n'
                },
                'name': 'measurements',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualNumRead'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Number of measurements written to the measurements array.\n'
                },
                'name': 'actualNumRead',
                'type': 'ViInt32'
            }
        ],
        'python_name': 'ppmu_measure',
        'returns': 'ViStatus'
    },
    'PPMU_Source': {
        'documentation': {
            'description': 'Starts sourcing voltage or current from the PPMU. This function automatically selects the PPMU function. Changes to PPMU source settings do not take effect until you call this function. If you modify source settings after you call this function, you must call this function again for changes in the configuration to take effect.\n'
        },
        'grpc_name': 'PPMUSource',
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelList',
                'type': 'ViConstString'
            }
        ],
        'python_name': 'ppmu_source',
        'returns': 'ViStatus'
    },
    'ReadSequencerFlag': {
        'documentation': {
            'description': 'Reads the state of a pattern sequencer flag. Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime test program.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The pattern sequencer flag you want to read.\n\n-   NIDIGITAL_VAL_SEQUENCER_FLAG0 ("seqflag0"): Reads pattern sequencer flag 0.\n-   NIDIGITAL_VAL_SEQUENCER_FLAG1 ("seqflag1"): Reads pattern sequencer flag 1.\n-   NIDIGITAL_VAL_SEQUENCER_FLAG2 ("seqflag2"): Reads pattern sequencer flag 2.\n-   NIDIGITAL_VAL_SEQUENCER_FLAG3 ("seqflag3"): Reads pattern sequencer flag 3.\n'
                },
                'enum': 'SequencerFlag',
                'grpc_enum': None,
                'name': 'flag',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'A Boolean that indicates the state of the pattern sequencer flag you specify.\n'
                },
                'name': 'value',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadSequencerRegister': {
        'documentation': {
            'description': 'Reads the value of a pattern sequencer register. Use pattern sequencer registers to pass numeric values between the pattern sequencer and a runtime test program. For example, you can use this function to read a register modified by the write_reg opcode during a pattern burst.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The sequencer register to read from.\n\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER0 ("reg0"): Reads sequencer register 0.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER1 ("reg1"): Reads sequencer register 1.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER2 ("reg2"): Reads sequencer register 2.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER3 ("reg3"): Reads sequencer register 3.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER4 ("reg4"): Reads sequencer register 4.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER5 ("reg5"): Reads sequencer register 5.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER6 ("reg6"): Reads sequencer register 6.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER7 ("reg7"): Reads sequencer register 7.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER8 ("reg8"): Reads sequencer register 8.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER9 ("reg9"): Reads sequencer register 9.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER10 ("reg10"): Reads sequencer register 10.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER11 ("reg11"): Reads sequencer register 11.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER12 ("reg12"): Reads sequencer register 12.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER13 ("reg13"): Reads sequencer register 13.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER14 ("reg14"): Reads sequencer register 14.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER15 ("reg15"): Reads sequencer register 15.\n'
                },
                'enum': 'SequencerRegister',
                'grpc_enum': None,
                'name': 'reg',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Value read from the sequencer register.\n'
                },
                'name': 'value',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadStatic': {
        'documentation': {
            'description': 'Reads the current state of comparators for pins you specify in the repeated capabilities. If there are uncommitted changes to levels or the termination mode, this function commits the changes to the pins.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements in the ViUInt8 array you specify for data. To determine the size of the buffer to allocate for the data array, pass a value of 0 to the **bufferSize** parameter and a value of VI_NULL to the **data** parameter. In this case, the value returned by the **actualNumRead** parameter is the size of the array necessary to hold the data.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned array of pin states read from the channels in the repeated capabilities. Data is returned in the order you specify in the repeated capabilities. If a site is disabled, the function does not return data for that site. You can also use the niDigital_FancyGetPinResultsPinInformation function to obtain a sorted list of returned sites and channels.\n\n-   NIDIGITAL_VAL_L: The comparators read a logic low pin state.\n-   NIDIGITAL_VAL_H: The comparators read a logic high pin state.\n-   NIDIGITAL_VAL_M: The comparators read a midband pin state.\n-   NIDIGITAL_VAL_V: The comparators read a value that is above VOH and below VOL, which can occur when you set VOL higher than VOH.\n'
                },
                'enum': 'PinState',
                'name': 'data',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualNumRead'
                },
                'type': 'ViUInt8[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The number of values written to the data array.\n'
                },
                'name': 'actualNumRead',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetDevice': {
        'documentation': {
            'description': 'Returns a digital pattern instrument to a known state. This function performs the following actions:\n\n- Aborts pattern execution.\n- Clears pin maps, time sets, source and capture waveforms, and patterns.\n- Resets all properties to default values, including the NIDIGITAL_ATTR_SELECTED_FUNCTION property that is set to NIDIGITAL_VAL_DISCONNECT, causing the I/O switches to open.\n- Stops export of all external signals and events.\n- Clears over-temperature and over-power conditions.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SelfCalibrate': {
        'documentation': {
            'description': 'Performs self-calibration on a digital pattern instrument.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SendSoftwareEdgeTrigger': {
        'documentation': {
            'description': 'Forces a particular edge-based trigger to occur regardless of how the specified trigger is configured. You can use this function as a software override.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Trigger specifies the trigger you want to override.',
                    'table_body': [
                        [
                            'NIDIGITAL_VAL_START_TRIGGER',
                            'Overrides the Start trigger. You must specify an empty string in the trigger_identifier parameter.'
                        ],
                        [
                            'NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER',
                            'Specifies to route a conditional jump trigger. You must specify a conditional jump trigger in the trigger_identifier parameter.'
                        ]
                    ],
                    'table_header': [
                        'Defined Values'
                    ]
                },
                'enum': 'SoftwareTrigger',
                'name': 'trigger',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Trigger Identifier specifies the instance of the trigger you want to override.\nIf trigger is specified as NIDIGITAL_VAL_START_TRIGGER, this parameter must be an empty string. If trigger is\nspecified as NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER, allowed values are conditionalJumpTrigger0,\nconditionalJumpTrigger1, conditionalJumpTrigger2, and conditionalJumpTrigger3.\n'
                },
                'name': 'triggerIdentifier',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Sets the value of a ViBoolean attribute. Use this function to set the values of digital pattern instrument-specific attributes and inherent IVI attributes.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.\n'
                },
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The value to which you want to set the attribute; some of the values might not be valid depending on the current settings of the instrument session.\n'
                },
                'name': 'value',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt32': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Sets the value of a ViInt32 attribute. Use this function to set the values of digital pattern instrument-specific attributes and inherent IVI attributes.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.\n'
                },
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The value to which you want to set the attribute; some of the values might not be valid depending on the current settings of the instrument session.\n'
                },
                'grpc_enum': 'NiDigitalInt32AttributeValues',
                'name': 'value',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt64': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Sets the value of a ViInt64 attribute. Use this function to set the values of digital pattern instrument-specific attributes and inherent IVI attributes.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.\n'
                },
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The value to which you want to set the attribute; some of the values might not be valid depending on the current settings of the instrument session.\n'
                },
                'grpc_name': 'value_raw',
                'name': 'value',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Sets the value of a ViIntReal64 attribute. Use this function to set the values of digital pattern instrument-specific attributes and inherent IVI attributes.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.\n'
                },
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The value to which you want to set the attribute; some of the values might not be valid depending on the current settings of the instrument session.\n'
                },
                'grpc_name': 'value_raw',
                'name': 'value',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Sets the value of a ViString attribute. Use this function to set the values of digital pattern instrument-specific attributes and inherent IVI attributes.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.\n'
                },
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The value to which you want to set the attribute; some of the values might not be valid depending on the current settings of the instrument session.\n'
                },
                'grpc_name': 'value_raw',
                'name': 'value',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetRuntimeEnvironment': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'TBD'
        },
        'included_in_proto': False,
        'method_templates': [
            {
                'documentation_filename': 'none',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'none'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'environment',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'environmentVersion',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'reserved1',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'reserved2',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'TDR': {
        'documentation': {
            'description': 'Measures propagation delays through cables, connectors, and load boards using Time-Domain Reflectometry (TDR). Ensure that the channels and pins you select are connected to an open circuit.\n'
        },
        'grpc_name': 'TDR',
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'default_value': True,
                'direction': 'in',
                'documentation': {
                    'description': 'A Boolean that specifies whether to apply the measured TDR offsets. If you need to adjust the measured offsets prior to applying, set this input to VI_FALSE, and call the niDigital_ApplyTDROffsets function to specify the adjusted TDR offsets values.\n'
                },
                'name': 'applyOffsets',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements in the ViReal64 array you specify for offsets. To determine the size of the buffer to allocate for the offsets array, pass a value of 0 to the **offsetsBufferSize** parameter and a value of VI_NULL to the **offsets** parameter. In this case, the value returned by the **actualNumOffsets** parameter is the size of the array necessary to hold the TDR offsets.\n'
                },
                'name': 'offsetsBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Measured TDR offsets specified in seconds.\n'
                },
                'name': 'offsets',
                'python_api_converter_name': 'convert_seconds_real64_to_timedeltas',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'offsetsBufferSize',
                    'value_twist': 'actualNumOffsets'
                },
                'type': 'ViReal64[]',
                'type_in_documentation': 'list of hightime.timedelta'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Number of offsets written to the offsets array.\n'
                },
                'name': 'actualNumOffsets',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'UnloadAllPatterns': {
        'documentation': {
            'description': 'Unloads all patterns, source waveforms, and capture waveforms from a digital pattern instrument.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': 'A Boolean that specifies whether to keep or unload the keep alive pattern.\n'
                },
                'name': 'unloadKeepAlivePattern',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'UnloadSpecifications': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Unloads the given specifications sheet present in the previously loaded specifications file that you select. You must call the niDigital_LoadSpecifications function to reload the file with updated specifications values. You must then call the niDigital_ApplyLevelsAndTiming function in order to apply the levels and timing values that reference the updated specifications values.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Absolute file path to a loaded specifications file.\n'
                },
                'grpc_name': 'file_path',
                'name': 'specificationsFilePath',
                'python_name': 'file_path',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'UnlockSession': {
        'documentation': {
            'description': 'Releases a lock that you acquired on an instrument session using the niDigital_LockSession function.\n'
        },
        'included_in_proto': False,
        'method_templates': [
            {
                'documentation_filename': 'unlock',
                'library_interpreter_filename': 'unlock',
                'method_python_name_suffix': '',
                'session_filename': 'unlock'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'This parameter serves as a convenience. If you do not want to use this parameter, pass VI_NULL. You can use this parameter in complex functions to track lock status and the need to unlock the session. Pass the address of a local ViBoolean variable in the declaration of the local variable and initialize it to VI_FALSE. Also, pass the address of the same local variable to any other calls you make to niDigital_LockSession or niDigital_UnlockSession in the same function.\n'
                },
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'python_name': 'unlock',
        'render_in_session_base': True,
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'WaitUntilDone': {
        'documentation': {
            'description': 'Waits until the pattern burst has completed or the timeout has expired.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'hightime.timedelta(seconds=10.0)',
                'direction': 'in',
                'documentation': {
                    'description': 'Maximum time (in seconds) allowed for this function to complete. If this function does not complete within this time interval, this function returns an error.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteSequencerFlag': {
        'documentation': {
            'description': 'Writes the state of a pattern sequencer flag. Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime test program.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The pattern sequencer flag to write.\n\n-   NIDIGITAL_VAL_SEQUENCER_FLAG0 ("seqflag0"): Writes pattern sequencer flag 0.\n-   NIDIGITAL_VAL_SEQUENCER_FLAG1 ("seqflag1"): Writes pattern sequencer flag 1.\n-   NIDIGITAL_VAL_SEQUENCER_FLAG2 ("seqflag2"): Writes pattern sequencer flag 2.\n-   NIDIGITAL_VAL_SEQUENCER_FLAG3 ("seqflag3"): Writes pattern sequencer flag 3.\n'
                },
                'enum': 'SequencerFlag',
                'grpc_enum': None,
                'name': 'flag',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'A Boolean that assigns a state to the pattern sequencer flag you specify.\n'
                },
                'name': 'value',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteSequencerRegister': {
        'documentation': {
            'description': 'Writes a value to a pattern sequencer register. Use pattern sequencer registers to pass numeric values between the pattern sequencer and a runtime test program.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The sequencer register you want to write to.\n\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER0 ("reg0"): Writes sequencer register 0.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER1 ("reg1"): Writes sequencer register 1.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER2 ("reg2"): Writes sequencer register 2.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER3 ("reg3"): Writes sequencer register 3.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER4 ("reg4"): Writes sequencer register 4.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER5 ("reg5"): Writes sequencer register 5.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER6 ("reg6"): Writes sequencer register 6.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER7 ("reg7"): Writes sequencer register 7.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER8 ("reg8"): Writes sequencer register 8.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER9 ("reg9"): Writes sequencer register 9.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER10 ("reg10"): Writes sequencer register 10.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER11 ("reg11"): Writes sequencer register 11.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER12 ("reg12"): Writes sequencer register 12.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER13 ("reg13"): Writes sequencer register 13.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER14 ("reg14"): Writes sequencer register 14.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER15 ("reg15"): Writes sequencer register 15.\n'
                },
                'enum': 'SequencerRegister',
                'grpc_enum': None,
                'name': 'reg',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The value you want to write to the register.\n'
                },
                'name': 'value',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteSourceWaveformBroadcastU32': {
        'documentation': {
            'description': 'Writes the same waveform data to all sites. Use this write function if you set the data_mapping parameter of the create source waveform function to NIDIGITAL_VAL_BROADCAST.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.\n'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Size of the data array.\n'
                },
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '1D array of samples to use as source data to apply to all sites.\n'
                },
                'name': 'waveformData',
                'size': {
                    'mechanism': 'len',
                    'value': 'waveformSize'
                },
                'type': 'ViUInt32[]'
            }
        ],
        'python_name': 'write_source_waveform_broadcast',
        'returns': 'ViStatus'
    },
    'WriteSourceWaveformDataFromFileTDMS': {
        'documentation': {
            'description': 'Writes a source waveform based on the waveform data and configuration information the file contains.\n'
        },
        'grpc_name': 'WriteSourceWaveformDataFromFileTDMS',
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.\n'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Absolute file path to the load source waveform file (.tdms).\n'
                },
                'name': 'waveformFilePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteSourceWaveformSiteUniqueU32': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Writes one waveform per site. Use this write function if you set the parameter of the create source waveform function to Site Unique.\n'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Site numbers listed as a comma-delimited list of strings of form site\\ ``N``, where ``N`` is the site number.\n'
                },
                'is_repeated_capability': True,
                'name': 'siteList',
                'repeated_capability_type': 'sites',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.\n'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of waveforms.\n'
                },
                'name': 'numWaveforms',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of samples per waveform.\n'
                },
                'name': 'samplesPerWaveform',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'An array of samples to use as source data. Data for each site must be appended sequentially in the array (non-interleaved).\n'
                },
                'name': 'waveformData',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'ViUInt32[]',
                'use_array': True
            }
        ],
        'repeated_capability_type': 'sites',
        'returns': 'ViStatus'
    },
    'WriteStatic': {
        'documentation': {
            'description': 'Writes a static state to the specified pins. The selected pins remain in the specified state until the next pattern burst or call to this function. If there are uncommitted changes to levels or the termination mode, this function commits the changes to the pins. This function does not change the selected pin function. If you write a static state to a pin that does not have the Digital function selected, the new static state is stored by the instrument, and affects the state of the pin the next time you change the selected function to Digital.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Parameter that specifies one of the following digital states to assign to the pin.\n\n-   NIDIGITAL_VAL_0: Specifies to drive low.\n-   NIDIGITAL_VAL_1: Specifies to drive high.\n-   NIDIGITAL_VAL_X: Specifies to not drive.\n'
                },
                'enum': 'WriteStaticPinState',
                'name': 'state',
                'type': 'ViUInt8'
            }
        ],
        'returns': 'ViStatus'
    },
    'close': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Closes the specified instrument session to a digital pattern instrument, aborts pattern execution, and unloads pattern memory. The channels on a digital pattern instrument remain in their current state.\n'
        },
        'grpc_name': 'Close',
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': '_close',
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'error_message': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Takes the error code returned by the digital pattern instrument driver functions, interprets it, and returns it as a user readable string.\n'
        },
        'grpc_name': 'ErrorMessage',
        'included_in_proto': True,
        'is_error_handling': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns. You may also specify VI_NULL as the instrument session to retrieve the error message even when the niDigital_init function or the niDigital_InitWithOptions function fails.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified error code.\n'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The error information formatted as a string. The array must contain at least 256 characters.\n'
                },
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'reset': {
        'documentation': {
            'description': 'Returns a digital pattern instrument to a known state. This function performs the following actions:\n\n- Aborts pattern execution.\n- Clears pin maps, time sets, source and capture waveforms, and patterns.\n- Resets all properties to default values, including the NIDIGITAL_ATTR_SELECTED_FUNCTION property that is set to NIDIGITAL_VAL_DISCONNECT, causing the I/O switches to open.\n- Stops exporting all external signals and events.\n'
        },
        'grpc_name': 'Reset',
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'self_test': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns self test results from a digital pattern instrument. This test requires several minutes to execute.\n'
        },
        'grpc_name': 'SelfTest',
        'included_in_proto': True,
        'method_name_for_documentation': 'self_test',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'A parameter that indicates if the self test passed (0) or failed (!=0).\n'
                },
                'name': 'testResult',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned self test status message. The array must contain at least 256 characters.\n'
                },
                'name': 'testMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 2048
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    }
}
`````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/metadata/functions_addon.py sha256=d346a487824f812d4807baa51c9ce324334e9c401ca1037e027fa48961d9d6db bytes=26695 -->
## FILE: src/nidigital/metadata/functions_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nidigital/metadata/functions_addon.py`
- sha256: `d346a487824f812d4807baa51c9ce324334e9c401ca1037e027fa48961d9d6db`
- bytes: 26695

````python
# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
}

functions_additional_burst_pattern = {
    'FancyBurstPattern': {
        'python_name': 'burst_pattern',
        'codegen_method': 'python-only',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
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
                'library_interpreter_filename': 'none',
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
                'library_interpreter_filename': 'none',
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
                'library_interpreter_filename': 'none',
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
                'library_interpreter_filename': 'fancy_fetch_capture_waveform',
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
                'library_interpreter_filename': 'none',
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
                'library_interpreter_filename': 'none',
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
                'library_interpreter_filename': 'none',
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

functions_additional_enable_match_fail_combination = {
    'EnableMatchFailCombination': {
        'codegen_method': 'yes',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'enable_match_fail_combination',
                'method_python_name_suffix': '',
                'session_filename': 'none',
            }
        ],
        'documentation': {
            'description': 'Configures digital pattern instruments and the PXIe-6674T timing and synchronization instrument to combine pattern comparison results and control subsequent pattern execution across digital pattern instruments based on those results. You must initialize the PXIe-6674T using NI-Sync and use the niTClk Synchronize function to synchronize instruments before calling the niDigital_EnableMatchFailCombination function.\n'
        },
        'included_in_proto': False,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of sessions.\n'
                },
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified array of sessions synchronized using NI-TClk.\n'
                },
                'name': 'sessions',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified NI-Sync session.\n'
                },
                'name': 'syncSession',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'FancyEnableMatchFailCombination': {
        'python_name': 'enable_match_fail_combination',
        'codegen_method': 'python-only',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_enable_match_fail_combination',
            }
        ],
        'documentation': {
            'description': 'Configures digital pattern instruments and the PXIe-6674T timing and synchronization instrument to combine pattern comparison results and control subsequent pattern execution across digital pattern instruments based on those results. You must initialize the PXIe-6674T using NI-Sync and call this method from a multi-instrument session.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified NI-Sync session.\n'
                },
                'name': 'syncSession',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/metadata/nidigitalpattern.proto sha256=de25c25a4cf80415b4349f29651bc1f18417039b177f8dd641de5ce216de3a35 bytes=54672 -->
## FILE: src/nidigital/metadata/nidigitalpattern.proto

- repository: `ni/nimi-python`
- source_path: `src/nidigital/metadata/nidigitalpattern.proto`
- sha256: `de25c25a4cf80415b4349f29651bc1f18417039b177f8dd641de5ce216de3a35`
- bytes: 54672

````protobuf

//---------------------------------------------------------------------
// This file is generated from NI-Digital Pattern Driver API metadata version 24.3.0f175
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
  rpc Init(InitRequest) returns (InitResponse);
  rpc InitWithOptions(InitWithOptionsRequest) returns (InitWithOptionsResponse);
  rpc Close(CloseRequest) returns (CloseResponse);
  rpc Reset(ResetRequest) returns (ResetResponse);
  rpc ResetDevice(ResetDeviceRequest) returns (ResetDeviceResponse);
  rpc SelfTest(SelfTestRequest) returns (SelfTestResponse);
  rpc GetError(GetErrorRequest) returns (GetErrorResponse);
  rpc ClearError(ClearErrorRequest) returns (ClearErrorResponse);
  rpc ErrorMessage(ErrorMessageRequest) returns (ErrorMessageResponse);
  rpc SelfCalibrate(SelfCalibrateRequest) returns (SelfCalibrateResponse);
  rpc GetAttributeViInt32(GetAttributeViInt32Request) returns (GetAttributeViInt32Response);
  rpc GetAttributeViInt64(GetAttributeViInt64Request) returns (GetAttributeViInt64Response);
  rpc GetAttributeViReal64(GetAttributeViReal64Request) returns (GetAttributeViReal64Response);
  rpc GetAttributeViString(GetAttributeViStringRequest) returns (GetAttributeViStringResponse);
  rpc GetAttributeViSession(GetAttributeViSessionRequest) returns (GetAttributeViSessionResponse);
  rpc GetAttributeViBoolean(GetAttributeViBooleanRequest) returns (GetAttributeViBooleanResponse);
  rpc SetAttributeViInt32(SetAttributeViInt32Request) returns (SetAttributeViInt32Response);
  rpc SetAttributeViInt64(SetAttributeViInt64Request) returns (SetAttributeViInt64Response);
  rpc SetAttributeViReal64(SetAttributeViReal64Request) returns (SetAttributeViReal64Response);
  rpc SetAttributeViString(SetAttributeViStringRequest) returns (SetAttributeViStringResponse);
  rpc SetAttributeViSession(SetAttributeViSessionRequest) returns (SetAttributeViSessionResponse);
  rpc SetAttributeViBoolean(SetAttributeViBooleanRequest) returns (SetAttributeViBooleanResponse);
  rpc ResetAttribute(ResetAttributeRequest) returns (ResetAttributeResponse);
  rpc LoadPinMap(LoadPinMapRequest) returns (LoadPinMapResponse);
  rpc EnableSites(EnableSitesRequest) returns (EnableSitesResponse);
  rpc DisableSites(DisableSitesRequest) returns (DisableSitesResponse);
  rpc IsSiteEnabled(IsSiteEnabledRequest) returns (IsSiteEnabledResponse);
  rpc CreatePinMap(CreatePinMapRequest) returns (CreatePinMapResponse);
  rpc CreatePinGroup(CreatePinGroupRequest) returns (CreatePinGroupResponse);
  rpc CreateChannelMap(CreateChannelMapRequest) returns (CreateChannelMapResponse);
  rpc MapPinToChannel(MapPinToChannelRequest) returns (MapPinToChannelResponse);
  rpc EndChannelMap(EndChannelMapRequest) returns (EndChannelMapResponse);
  rpc GetPinName(GetPinNameRequest) returns (GetPinNameResponse);
  rpc GetChannelName(GetChannelNameRequest) returns (GetChannelNameResponse);
  rpc SelectFunction(SelectFunctionRequest) returns (SelectFunctionResponse);
  rpc ReadStatic(ReadStaticRequest) returns (ReadStaticResponse);
  rpc WriteStatic(WriteStaticRequest) returns (WriteStaticResponse);
  rpc ClockGeneratorGenerateClock(ClockGeneratorGenerateClockRequest) returns (ClockGeneratorGenerateClockResponse);
  rpc ClockGeneratorInitiate(ClockGeneratorInitiateRequest) returns (ClockGeneratorInitiateResponse);
  rpc ClockGeneratorAbort(ClockGeneratorAbortRequest) returns (ClockGeneratorAbortResponse);
  rpc LoadSpecifications(LoadSpecificationsRequest) returns (LoadSpecificationsResponse);
  rpc UnloadSpecifications(UnloadSpecificationsRequest) returns (UnloadSpecificationsResponse);
  rpc LoadLevels(LoadLevelsRequest) returns (LoadLevelsResponse);
  rpc LoadTiming(LoadTimingRequest) returns (LoadTimingResponse);
  rpc ApplyLevelsAndTiming(ApplyLevelsAndTimingRequest) returns (ApplyLevelsAndTimingResponse);
  rpc ConfigureVoltageLevels(ConfigureVoltageLevelsRequest) returns (ConfigureVoltageLevelsResponse);
  rpc ConfigureActiveLoadLevels(ConfigureActiveLoadLevelsRequest) returns (ConfigureActiveLoadLevelsResponse);
  rpc ConfigureTerminationMode(ConfigureTerminationModeRequest) returns (ConfigureTerminationModeResponse);
  rpc CreateTimeSet(CreateTimeSetRequest) returns (CreateTimeSetResponse);
  rpc ConfigureTimeSetPeriod(ConfigureTimeSetPeriodRequest) returns (ConfigureTimeSetPeriodResponse);
  rpc ConfigureTimeSetDriveEdges(ConfigureTimeSetDriveEdgesRequest) returns (ConfigureTimeSetDriveEdgesResponse);
  rpc ConfigureTimeSetCompareEdgesStrobe(ConfigureTimeSetCompareEdgesStrobeRequest) returns (ConfigureTimeSetCompareEdgesStrobeResponse);
  rpc ConfigureTimeSetDriveFormat(ConfigureTimeSetDriveFormatRequest) returns (ConfigureTimeSetDriveFormatResponse);
  rpc DeleteAllTimeSets(DeleteAllTimeSetsRequest) returns (DeleteAllTimeSetsResponse);
  rpc ConfigureTimeSetEdgeMultiplier(ConfigureTimeSetEdgeMultiplierRequest) returns (ConfigureTimeSetEdgeMultiplierResponse);
  rpc ConfigureTimeSetDriveEdges2x(ConfigureTimeSetDriveEdges2xRequest) returns (ConfigureTimeSetDriveEdges2xResponse);
  rpc ConfigureTimeSetCompareEdgesStrobe2x(ConfigureTimeSetCompareEdgesStrobe2xRequest) returns (ConfigureTimeSetCompareEdgesStrobe2xResponse);
  rpc ConfigureTimeSetEdge(ConfigureTimeSetEdgeRequest) returns (ConfigureTimeSetEdgeResponse);
  rpc GetTimeSetPeriod(GetTimeSetPeriodRequest) returns (GetTimeSetPeriodResponse);
  rpc GetTimeSetEdge(GetTimeSetEdgeRequest) returns (GetTimeSetEdgeResponse);
  rpc GetTimeSetEdgeMultiplier(GetTimeSetEdgeMultiplierRequest) returns (GetTimeSetEdgeMultiplierResponse);
  rpc GetTimeSetDriveFormat(GetTimeSetDriveFormatRequest) returns (GetTimeSetDriveFormatResponse);
  rpc GetTimeSetName(GetTimeSetNameRequest) returns (GetTimeSetNameResponse);
  rpc TDR(TDRRequest) returns (TDRResponse);
  rpc ApplyTDROffsets(ApplyTDROffsetsRequest) returns (ApplyTDROffsetsResponse);
  rpc PPMUConfigureOutputFunction(PPMUConfigureOutputFunctionRequest) returns (PPMUConfigureOutputFunctionResponse);
  rpc PPMUConfigureApertureTime(PPMUConfigureApertureTimeRequest) returns (PPMUConfigureApertureTimeResponse);
  rpc PPMUConfigureVoltageLevel(PPMUConfigureVoltageLevelRequest) returns (PPMUConfigureVoltageLevelResponse);
  rpc PPMUConfigureCurrentLimit(PPMUConfigureCurrentLimitRequest) returns (PPMUConfigureCurrentLimitResponse);
  rpc PPMUConfigureCurrentLimitRange(PPMUConfigureCurrentLimitRangeRequest) returns (PPMUConfigureCurrentLimitRangeResponse);
  rpc PPMUConfigureCurrentLevel(PPMUConfigureCurrentLevelRequest) returns (PPMUConfigureCurrentLevelResponse);
  rpc PPMUConfigureCurrentLevelRange(PPMUConfigureCurrentLevelRangeRequest) returns (PPMUConfigureCurrentLevelRangeResponse);
  rpc PPMUConfigureVoltageLimits(PPMUConfigureVoltageLimitsRequest) returns (PPMUConfigureVoltageLimitsResponse);
  rpc PPMUSource(PPMUSourceRequest) returns (PPMUSourceResponse);
  rpc PPMUMeasure(PPMUMeasureRequest) returns (PPMUMeasureResponse);
  rpc LoadPattern(LoadPatternRequest) returns (LoadPatternResponse);
  rpc UnloadAllPatterns(UnloadAllPatternsRequest) returns (UnloadAllPatternsResponse);
  rpc ConfigureStartLabel(ConfigureStartLabelRequest) returns (ConfigureStartLabelResponse);
  rpc ConfigurePatternBurstSites(ConfigurePatternBurstSitesRequest) returns (ConfigurePatternBurstSitesResponse);
  rpc GetPatternPinIndexes(GetPatternPinIndexesRequest) returns (GetPatternPinIndexesResponse);
  rpc GetPatternPinList(GetPatternPinListRequest) returns (GetPatternPinListResponse);
  rpc GetPatternName(GetPatternNameRequest) returns (GetPatternNameResponse);
  rpc BurstPattern(BurstPatternRequest) returns (BurstPatternResponse);
  rpc BurstPatternSynchronized(BurstPatternSynchronizedRequest) returns (BurstPatternSynchronizedResponse);
  rpc Commit(CommitRequest) returns (CommitResponse);
  rpc Initiate(InitiateRequest) returns (InitiateResponse);
  rpc IsDone(IsDoneRequest) returns (IsDoneResponse);
  rpc WaitUntilDone(WaitUntilDoneRequest) returns (WaitUntilDoneResponse);
  rpc Abort(AbortRequest) returns (AbortResponse);
  rpc AbortKeepAlive(AbortKeepAliveRequest) returns (AbortKeepAliveResponse);
  rpc ConfigurePatternLabelHistoryRAMTrigger(ConfigurePatternLabelHistoryRAMTriggerRequest) returns (ConfigurePatternLabelHistoryRAMTriggerResponse);
  rpc ConfigureCycleNumberHistoryRAMTrigger(ConfigureCycleNumberHistoryRAMTriggerRequest) returns (ConfigureCycleNumberHistoryRAMTriggerResponse);
  rpc ConfigureFirstFailureHistoryRAMTrigger(ConfigureFirstFailureHistoryRAMTriggerRequest) returns (ConfigureFirstFailureHistoryRAMTriggerResponse);
  rpc ConfigureHistoryRAMCyclesToAcquire(ConfigureHistoryRAMCyclesToAcquireRequest) returns (ConfigureHistoryRAMCyclesToAcquireResponse);
  rpc GetHistoryRAMSampleCount(GetHistoryRAMSampleCountRequest) returns (GetHistoryRAMSampleCountResponse);
  rpc FetchHistoryRAMCycleInformation(FetchHistoryRAMCycleInformationRequest) returns (FetchHistoryRAMCycleInformationResponse);
  rpc FetchHistoryRAMCyclePinData(FetchHistoryRAMCyclePinDataRequest) returns (FetchHistoryRAMCyclePinDataResponse);
  rpc FetchHistoryRAMScanCycleNumber(FetchHistoryRAMScanCycleNumberRequest) returns (FetchHistoryRAMScanCycleNumberResponse);
  rpc CreateSourceWaveformParallel(CreateSourceWaveformParallelRequest) returns (CreateSourceWaveformParallelResponse);
  rpc CreateSourceWaveformSerial(CreateSourceWaveformSerialRequest) returns (CreateSourceWaveformSerialResponse);
  rpc CreateSourceWaveformFromFileTDMS(CreateSourceWaveformFromFileTDMSRequest) returns (CreateSourceWaveformFromFileTDMSResponse);
  rpc WriteSourceWaveformBroadcastU32(WriteSourceWaveformBroadcastU32Request) returns (WriteSourceWaveformBroadcastU32Response);
  rpc WriteSourceWaveformSiteUniqueU32(WriteSourceWaveformSiteUniqueU32Request) returns (WriteSourceWaveformSiteUniqueU32Response);
  rpc WriteSourceWaveformDataFromFileTDMS(WriteSourceWaveformDataFromFileTDMSRequest) returns (WriteSourceWaveformDataFromFileTDMSResponse);
  rpc CreateCaptureWaveformParallel(CreateCaptureWaveformParallelRequest) returns (CreateCaptureWaveformParallelResponse);
  rpc CreateCaptureWaveformSerial(CreateCaptureWaveformSerialRequest) returns (CreateCaptureWaveformSerialResponse);
  rpc CreateCaptureWaveformFromFileDigicapture(CreateCaptureWaveformFromFileDigicaptureRequest) returns (CreateCaptureWaveformFromFileDigicaptureResponse);
  rpc FetchCaptureWaveformU32(FetchCaptureWaveformU32Request) returns (FetchCaptureWaveformU32Response);
  rpc ExportSignal(ExportSignalRequest) returns (ExportSignalResponse);
  rpc ConfigureDigitalEdgeStartTrigger(ConfigureDigitalEdgeStartTriggerRequest) returns (ConfigureDigitalEdgeStartTriggerResponse);
  rpc ConfigureSoftwareEdgeStartTrigger(ConfigureSoftwareEdgeStartTriggerRequest) returns (ConfigureSoftwareEdgeStartTriggerResponse);
  rpc DisableStartTrigger(DisableStartTriggerRequest) returns (DisableStartTriggerResponse);
  rpc ConfigureDigitalEdgeConditionalJumpTrigger(ConfigureDigitalEdgeConditionalJumpTriggerRequest) returns (ConfigureDigitalEdgeConditionalJumpTriggerResponse);
  rpc ConfigureSoftwareEdgeConditionalJumpTrigger(ConfigureSoftwareEdgeConditionalJumpTriggerRequest) returns (ConfigureSoftwareEdgeConditionalJumpTriggerResponse);
  rpc DisableConditionalJumpTrigger(DisableConditionalJumpTriggerRequest) returns (DisableConditionalJumpTriggerResponse);
  rpc SendSoftwareEdgeTrigger(SendSoftwareEdgeTriggerRequest) returns (SendSoftwareEdgeTriggerResponse);
  rpc WriteSequencerFlag(WriteSequencerFlagRequest) returns (WriteSequencerFlagResponse);
  rpc WriteSequencerFlagSynchronized(WriteSequencerFlagSynchronizedRequest) returns (WriteSequencerFlagSynchronizedResponse);
  rpc ReadSequencerFlag(ReadSequencerFlagRequest) returns (ReadSequencerFlagResponse);
  rpc WriteSequencerRegister(WriteSequencerRegisterRequest) returns (WriteSequencerRegisterResponse);
  rpc ReadSequencerRegister(ReadSequencerRegisterRequest) returns (ReadSequencerRegisterResponse);
  rpc EnableMatchFailCombination(EnableMatchFailCombinationRequest) returns (EnableMatchFailCombinationResponse);
  rpc GetSitePassFail(GetSitePassFailRequest) returns (GetSitePassFailResponse);
  rpc GetFailCount(GetFailCountRequest) returns (GetFailCountResponse);
  rpc GetPinResultsPinInformation(GetPinResultsPinInformationRequest) returns (GetPinResultsPinInformationResponse);
  rpc GetSiteResultsSiteNumbers(GetSiteResultsSiteNumbersRequest) returns (GetSiteResultsSiteNumbersResponse);
  rpc FrequencyCounterConfigureMeasurementTime(FrequencyCounterConfigureMeasurementTimeRequest) returns (FrequencyCounterConfigureMeasurementTimeResponse);
  rpc FrequencyCounterConfigureMeasurementMode(FrequencyCounterConfigureMeasurementModeRequest) returns (FrequencyCounterConfigureMeasurementModeResponse);
  rpc FrequencyCounterMeasureFrequency(FrequencyCounterMeasureFrequencyRequest) returns (FrequencyCounterMeasureFrequencyResponse);
  rpc GetChannelNameFromString(GetChannelNameFromStringRequest) returns (GetChannelNameFromStringResponse);
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
  NIDIGITAL_ATTRIBUTE_SPECIFIC_DRIVER_VENDOR = 1050513;
  NIDIGITAL_ATTRIBUTE_SPECIFIC_DRIVER_DESCRIPTION = 1050514;
  NIDIGITAL_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION = 1050515;
  NIDIGITAL_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION = 1050516;
  NIDIGITAL_ATTRIBUTE_SPECIFIC_DRIVER_REVISION = 1050551;
  NIDIGITAL_ATTRIBUTE_INSTRUMENT_MODEL = 1050512;
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
  NIDIGITAL_ATTRIBUTE_START_TRIGGER_TERMINAL_NAME = 1150039;
  NIDIGITAL_ATTRIBUTE_PPMU_APERTURE_TIME = 1150037;
  NIDIGITAL_ATTRIBUTE_PPMU_APERTURE_TIME_UNITS = 1150038;
  NIDIGITAL_ATTRIBUTE_EXPORTED_PATTERN_OPCODE_EVENT_OUTPUT_TERMINAL = 1150041;
  NIDIGITAL_ATTRIBUTE_PATTERN_OPCODE_EVENT_TERMINAL_NAME = 1150042;
  NIDIGITAL_ATTRIBUTE_HISTORY_RAM_TRIGGER_TYPE = 1150043;
  NIDIGITAL_ATTRIBUTE_CYCLE_NUMBER_HISTORY_RAM_TRIGGER_CYCLE_NUMBER = 1150044;
  NIDIGITAL_ATTRIBUTE_PATTERN_LABEL_HISTORY_RAM_TRIGGER_CYCLE_OFFSET = 1150045;
  NIDIGITAL_ATTRIBUTE_PATTERN_LABEL_HISTORY_RAM_TRIGGER_LABEL = 1150046;
  NIDIGITAL_ATTRIBUTE_HISTORY_RAM_CYCLES_TO_ACQUIRE = 1150047;
  NIDIGITAL_ATTRIBUTE_HISTORY_RAM_PRETRIGGER_SAMPLES = 1150048;
  NIDIGITAL_ATTRIBUTE_TDR_ENDPOINT_TERMINATION = 1150081;
  NIDIGITAL_ATTRIBUTE_RIO_TRIGGER_TYPE = 1150086;
  NIDIGITAL_ATTRIBUTE_DIGITAL_EDGE_RIO_TRIGGER_SOURCE = 1150087;
  NIDIGITAL_ATTRIBUTE_DIGITAL_EDGE_RIO_TRIGGER_EDGE = 1150088;
  NIDIGITAL_ATTRIBUTE_RIO_TRIGGER_TERMINAL_NAME = 1150089;
  NIDIGITAL_ATTRIBUTE_EXPORTED_RIO_EVENT_OUTPUT_TERMINAL = 1150090;
  NIDIGITAL_ATTRIBUTE_RIO_EVENT_TERMINAL_NAME = 1150091;
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
  NIDIGITAL_ATTRIBUTE_FREQUENCY_COUNTER_MEASUREMENT_MODE = 1150084;
  NIDIGITAL_ATTRIBUTE_FREQUENCY_COUNTER_HYSTERESIS_ENABLED = 1150085;
  NIDIGITAL_ATTRIBUTE_TIMING_ABSOLUTE_DELAY_ENABLED = 1150071;
  NIDIGITAL_ATTRIBUTE_TIMING_ABSOLUTE_DELAY = 1150072;
  NIDIGITAL_ATTRIBUTE_CLOCK_GENERATOR_FREQUENCY = 1150073;
  NIDIGITAL_ATTRIBUTE_CLOCK_GENERATOR_IS_RUNNING = 1150074;
  NIDIGITAL_ATTRIBUTE_PPMU_ALLOW_EXTENDED_VOLTAGE_RANGE = 1150076;
  NIDIGITAL_ATTRIBUTE_HISTORY_RAM_MAX_SAMPLES_TO_ACQUIRE_PER_SITE = 1150077;
  NIDIGITAL_ATTRIBUTE_HISTORY_RAM_NUMBER_OF_SAMPLES_IS_FINITE = 1150078;
  NIDIGITAL_ATTRIBUTE_HISTORY_RAM_BUFFER_SIZE_PER_SITE = 1150079;
  NIDIGITAL_ATTRIBUTE_CONDITIONAL_JUMP_TRIGGER_TYPE = 1150033;
  NIDIGITAL_ATTRIBUTE_DIGITAL_EDGE_CONDITIONAL_JUMP_TRIGGER_SOURCE = 1150034;
  NIDIGITAL_ATTRIBUTE_DIGITAL_EDGE_CONDITIONAL_JUMP_TRIGGER_EDGE = 1150035;
  NIDIGITAL_ATTRIBUTE_EXPORTED_CONDITIONAL_JUMP_TRIGGER_OUTPUT_TERMINAL = 1150036;
  NIDIGITAL_ATTRIBUTE_CONDITIONAL_JUMP_TRIGGER_TERMINAL_NAME = 1150040;
}

enum PpmuApertureTimeUnits {
  PPMU_APERTURE_TIME_UNITS_UNSPECIFIED = 0;
  PPMU_APERTURE_TIME_UNITS_NIDIGITAL_VAL_SECONDS = 2100;
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

enum DriveFormat {
  DRIVE_FORMAT_UNSPECIFIED = 0;
  DRIVE_FORMAT_NIDIGITAL_VAL_NR = 1500;
  DRIVE_FORMAT_NIDIGITAL_VAL_RL = 1501;
  DRIVE_FORMAT_NIDIGITAL_VAL_RH = 1502;
  DRIVE_FORMAT_NIDIGITAL_VAL_SBC = 1503;
}

enum HistoryRamCyclesToAcquire {
  HISTORY_RAM_CYCLES_TO_ACQUIRE_UNSPECIFIED = 0;
  HISTORY_RAM_CYCLES_TO_ACQUIRE_NIDIGITAL_VAL_FAILED_CYCLES = 2303;
  HISTORY_RAM_CYCLES_TO_ACQUIRE_NIDIGITAL_VAL_ALL_CYCLES = 2304;
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

enum ExportSignal {
  EXPORT_SIGNAL_UNSPECIFIED = 0;
  EXPORT_SIGNAL_NIDIGITAL_VAL_START_TRIGGER = 2000;
  EXPORT_SIGNAL_NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER = 2001;
  EXPORT_SIGNAL_NIDIGITAL_VAL_PATTERN_OPCODE_EVENT = 2002;
  EXPORT_SIGNAL_NIDIGITAL_VAL_REF_CLOCK = 2003;
  EXPORT_SIGNAL_NIDIGITAL_VAL_RIO_EVENT = 2004;
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

enum FrequencyMeasurementMode {
  FREQUENCY_MEASUREMENT_MODE_UNSPECIFIED = 0;
  FREQUENCY_MEASUREMENT_MODE_NIDIGITAL_VAL_BANKED = 3700;
  FREQUENCY_MEASUREMENT_MODE_NIDIGITAL_VAL_PARALLEL = 3701;
}

enum WriteStaticPinState {
  WRITE_STATIC_PIN_STATE_NIDIGITAL_VAL_0 = 0;
  WRITE_STATIC_PIN_STATE_NIDIGITAL_VAL_1 = 1;
  WRITE_STATIC_PIN_STATE_NIDIGITAL_VAL_X = 5;
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

message CloseRequest {
  nidevice_grpc.Session vi = 1;
}

message CloseResponse {
  int32 status = 1;
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

message SelfTestRequest {
  nidevice_grpc.Session vi = 1;
}

message SelfTestResponse {
  int32 status = 1;
  sint32 test_result = 2;
  string test_message = 3;
}

message GetErrorRequest {
  nidevice_grpc.Session vi = 1;
}

message GetErrorResponse {
  int32 status = 1;
  sint32 error_code = 2;
  string error_description = 3;
}

message ClearErrorRequest {
  nidevice_grpc.Session vi = 1;
}

message ClearErrorResponse {
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

message SelfCalibrateRequest {
  nidevice_grpc.Session vi = 1;
}

message SelfCalibrateResponse {
  int32 status = 1;
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

message GetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDigitalAttribute attribute = 3;
}

message GetAttributeViStringResponse {
  int32 status = 1;
  string value = 2;
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

message GetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDigitalAttribute attribute = 3;
}

message GetAttributeViBooleanResponse {
  int32 status = 1;
  bool value = 2;
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

message SetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDigitalAttribute attribute = 3;
  string value_raw = 4;
}

message SetAttributeViStringResponse {
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

message SetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiDigitalAttribute attribute = 3;
  bool value = 4;
}

message SetAttributeViBooleanResponse {
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

message LoadPinMapRequest {
  nidevice_grpc.Session vi = 1;
  string file_path = 2;
}

message LoadPinMapResponse {
  int32 status = 1;
}

message EnableSitesRequest {
  nidevice_grpc.Session vi = 1;
  string site_list = 2;
}

message EnableSitesResponse {
  int32 status = 1;
}

message DisableSitesRequest {
  nidevice_grpc.Session vi = 1;
  string site_list = 2;
}

message DisableSitesResponse {
  int32 status = 1;
}

message IsSiteEnabledRequest {
  nidevice_grpc.Session vi = 1;
  string site = 2;
}

message IsSiteEnabledResponse {
  int32 status = 1;
  bool enable = 2;
}

message CreatePinMapRequest {
  nidevice_grpc.Session vi = 1;
  string dut_pin_list = 2;
  string system_pin_list = 3;
}

message CreatePinMapResponse {
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

message CreateChannelMapRequest {
  nidevice_grpc.Session vi = 1;
  sint32 num_sites = 2;
}

message CreateChannelMapResponse {
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

message EndChannelMapRequest {
  nidevice_grpc.Session vi = 1;
}

message EndChannelMapResponse {
  int32 status = 1;
}

message GetPinNameRequest {
  nidevice_grpc.Session vi = 1;
  sint32 pin_index = 2;
}

message GetPinNameResponse {
  int32 status = 1;
  string name = 2;
}

message GetChannelNameRequest {
  nidevice_grpc.Session vi = 1;
  sint32 index = 2;
}

message GetChannelNameResponse {
  int32 status = 1;
  string name = 2;
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

message ClockGeneratorAbortRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
}

message ClockGeneratorAbortResponse {
  int32 status = 1;
}

message LoadSpecificationsRequest {
  nidevice_grpc.Session vi = 1;
  string file_path = 2;
}

message LoadSpecificationsResponse {
  int32 status = 1;
}

message UnloadSpecificationsRequest {
  nidevice_grpc.Session vi = 1;
  string file_path = 2;
}

message UnloadSpecificationsResponse {
  int32 status = 1;
}

message LoadLevelsRequest {
  nidevice_grpc.Session vi = 1;
  string file_path = 2;
}

message LoadLevelsResponse {
  int32 status = 1;
}

message LoadTimingRequest {
  nidevice_grpc.Session vi = 1;
  string file_path = 2;
}

message LoadTimingResponse {
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

message CreateTimeSetRequest {
  nidevice_grpc.Session vi = 1;
  string name = 2;
}

message CreateTimeSetResponse {
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

message ConfigureTimeSetCompareEdgesStrobeRequest {
  nidevice_grpc.Session vi = 1;
  string pin_list = 2;
  string time_set_name = 3;
  double strobe_edge = 4;
}

message ConfigureTimeSetCompareEdgesStrobeResponse {
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

message DeleteAllTimeSetsRequest {
  nidevice_grpc.Session vi = 1;
}

message DeleteAllTimeSetsResponse {
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

message GetTimeSetPeriodRequest {
  nidevice_grpc.Session vi = 1;
  string time_set_name = 2;
}

message GetTimeSetPeriodResponse {
  int32 status = 1;
  double period = 2;
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

message GetTimeSetNameRequest {
  nidevice_grpc.Session vi = 1;
  sint32 time_set_index = 2;
}

message GetTimeSetNameResponse {
  int32 status = 1;
  string name = 2;
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

message ApplyTDROffsetsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  repeated double offsets = 3;
}

message ApplyTDROffsetsResponse {
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

message PPMUConfigureVoltageLevelRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double voltage_level = 3;
}

message PPMUConfigureVoltageLevelResponse {
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

message PPMUConfigureVoltageLimitsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double lower_voltage_limit = 3;
  double upper_voltage_limit = 4;
}

message PPMUConfigureVoltageLimitsResponse {
  int32 status = 1;
}

message PPMUSourceRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
}

message PPMUSourceResponse {
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

message LoadPatternRequest {
  nidevice_grpc.Session vi = 1;
  string file_path = 2;
}

message LoadPatternResponse {
  int32 status = 1;
}

message UnloadAllPatternsRequest {
  nidevice_grpc.Session vi = 1;
  bool unload_keep_alive_pattern = 2;
}

message UnloadAllPatternsResponse {
  int32 status = 1;
}

message ConfigureStartLabelRequest {
  nidevice_grpc.Session vi = 1;
  string label = 2;
}

message ConfigureStartLabelResponse {
  int32 status = 1;
}

message ConfigurePatternBurstSitesRequest {
  nidevice_grpc.Session vi = 1;
  string site_list = 2;
}

message ConfigurePatternBurstSitesResponse {
  int32 status = 1;
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

message GetPatternNameRequest {
  nidevice_grpc.Session vi = 1;
  sint32 pattern_index = 2;
}

message GetPatternNameResponse {
  int32 status = 1;
  string name = 2;
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

message CommitRequest {
  nidevice_grpc.Session vi = 1;
}

message CommitResponse {
  int32 status = 1;
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

message WaitUntilDoneRequest {
  nidevice_grpc.Session vi = 1;
  double timeout = 2;
}

message WaitUntilDoneResponse {
  int32 status = 1;
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

message ConfigureCycleNumberHistoryRAMTriggerRequest {
  nidevice_grpc.Session vi = 1;
  int64 cycle_number = 2;
  sint32 pretrigger_samples = 3;
}

message ConfigureCycleNumberHistoryRAMTriggerResponse {
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

message GetHistoryRAMSampleCountRequest {
  nidevice_grpc.Session vi = 1;
  string site = 2;
}

message GetHistoryRAMSampleCountResponse {
  int32 status = 1;
  int64 sample_count = 2;
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

message CreateSourceWaveformFromFileTDMSRequest {
  nidevice_grpc.Session vi = 1;
  string waveform_name = 2;
  string waveform_file_path = 3;
  bool write_waveform_data = 4;
}

message CreateSourceWaveformFromFileTDMSResponse {
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

message WriteSourceWaveformDataFromFileTDMSRequest {
  nidevice_grpc.Session vi = 1;
  string waveform_name = 2;
  string waveform_file_path = 3;
}

message WriteSourceWaveformDataFromFileTDMSResponse {
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

message CreateCaptureWaveformFromFileDigicaptureRequest {
  nidevice_grpc.Session vi = 1;
  string waveform_name = 2;
  string waveform_file_path = 3;
}

message CreateCaptureWaveformFromFileDigicaptureResponse {
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

message ConfigureSoftwareEdgeStartTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message ConfigureSoftwareEdgeStartTriggerResponse {
  int32 status = 1;
}

message DisableStartTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message DisableStartTriggerResponse {
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

message ConfigureSoftwareEdgeConditionalJumpTriggerRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_identifier = 2;
}

message ConfigureSoftwareEdgeConditionalJumpTriggerResponse {
  int32 status = 1;
}

message DisableConditionalJumpTriggerRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_identifier = 2;
}

message DisableConditionalJumpTriggerResponse {
  int32 status = 1;
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

message ReadSequencerFlagRequest {
  nidevice_grpc.Session vi = 1;
  string flag = 2;
}

message ReadSequencerFlagResponse {
  int32 status = 1;
  bool value = 2;
}

message WriteSequencerRegisterRequest {
  nidevice_grpc.Session vi = 1;
  string reg = 2;
  sint32 value = 3;
}

message WriteSequencerRegisterResponse {
  int32 status = 1;
}

message ReadSequencerRegisterRequest {
  nidevice_grpc.Session vi = 1;
  string reg = 2;
}

message ReadSequencerRegisterResponse {
  int32 status = 1;
  sint32 value = 2;
}

message EnableMatchFailCombinationRequest {
  uint32 session_count = 1;
  repeated nidevice_grpc.Session sessions = 2;
  nidevice_grpc.Session sync_session = 3;
}

message EnableMatchFailCombinationResponse {
  int32 status = 1;
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

message GetFailCountRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
}

message GetFailCountResponse {
  int32 status = 1;
  repeated int64 failure_count = 2;
  sint32 actual_num_read = 3;
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

message FrequencyCounterConfigureMeasurementTimeRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double measurement_time = 3;
}

message FrequencyCounterConfigureMeasurementTimeResponse {
  int32 status = 1;
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

message FrequencyCounterMeasureFrequencyRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
}

message FrequencyCounterMeasureFrequencyResponse {
  int32 status = 1;
  repeated double frequencies = 2;
  sint32 actual_num_frequencies = 3;
}

message GetChannelNameFromStringRequest {
  nidevice_grpc.Session vi = 1;
  string indices = 2;
}

message GetChannelNameFromStringResponse {
  int32 status = 1;
  string names = 2;
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/nidigital.mak sha256=b2b6146eaa79a21abd0726e49ea8105c1ffb9e3405b86f8be4b0b0232ca4a773 bytes=468 -->
## FILE: src/nidigital/nidigital.mak

- repository: `ni/nimi-python`
- source_path: `src/nidigital/nidigital.mak`
- sha256: `b2b6146eaa79a21abd0726e49ea8105c1ffb9e3405b86f8be4b0b0232ca4a773`
- bytes: 468

````makefile
PROTO_FILE = $(METADATA_DIR)/nidigitalpattern.proto

include $(BUILD_HELPER_DIR)/defines.mak

MODULE_FILES_TO_GENERATE := $(DEFAULT_PY_FILES_TO_GENERATE)

MODULE_FILES_TO_COPY := $(DEFAULT_PY_FILES_TO_COPY)

RST_FILES_TO_GENERATE := $(DEFAULT_RST_FILES_TO_GENERATE)

SPHINX_CONF_PY := $(DEFAULT_SPHINX_CONF_PY)
READTHEDOCS_CONFIG := $(DEFAULT_READTHEDOCS_CONFIG)

CUSTOM_TYPES_TO_COPY += \
    history_ram_cycle_information.py \

include $(BUILD_HELPER_DIR)/rules.mak
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/grpc_server_config.json sha256=a3bcfb47f8a8d2ab88966bf165a5f028bb3bfae73e5d24bd90edcdb3ac43fa9e bytes=156 -->
## FILE: src/nidigital/system_tests/grpc_server_config.json

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/grpc_server_config.json`
- sha256: `a3bcfb47f8a8d2ab88966bf165a5f028bb3bfae73e5d24bd90edcdb3ac43fa9e`
- bytes: 156

````json
{
    "address": "[::1]",
    "port": 31761,
    "security" : {
       "server_cert": "",
       "server_key": "",
       "root_cert": ""
    }
 }
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/multiple_patterns/pin_levels.digilevels sha256=8476ee4cebdd5267c105961ec5a26674daa4df8ef6f3e96b9421957bbf1f5638 bytes=555 -->
## FILE: src/nidigital/system_tests/test_files/multiple_patterns/pin_levels.digilevels

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/multiple_patterns/pin_levels.digilevels`
- sha256: `8476ee4cebdd5267c105961ec5a26674daa4df8ef6f3e96b9421957bbf1f5638`
- bytes: 555

````text
<?xml version="1.0" encoding="utf-8"?>
<PinLevelsFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/PinLevels">
  <PinLevelsSheet>
    <DigitalPinLevelSets>
      <DigitalPinLevelSet pin="AllPins">
        <Vil>1 V</Vil>
        <Vih>5 V</Vih>
        <Vol>2 V</Vol>
        <Voh>4 V</Voh>
        <TerminationMode>HighZ</TerminationMode>
      </DigitalPinLevelSet>
    </DigitalPinLevelSets>
  </PinLevelsSheet>
</PinLevelsFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/multiple_patterns/pin_map.pinmap sha256=6d1fb7cf77a8a6f626f2c4c72af1f58b1eb5639d2088764aff54967b2589231d bytes=3971 -->
## FILE: src/nidigital/system_tests/test_files/multiple_patterns/pin_map.pinmap

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/multiple_patterns/pin_map.pinmap`
- sha256: `6d1fb7cf77a8a6f626f2c4c72af1f58b1eb5639d2088764aff54967b2589231d`
- bytes: 3971

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.5">
	<Instruments>
		<NIDigitalPatternInstrument name="PXI1Slot2" numberOfChannels="32" group="Digital" />
		<NIDigitalPatternInstrument name="PXI1Slot5" numberOfChannels="32" group="Digital" />
	</Instruments>
	<Pins>
		<DUTPin name="LO0" />
		<DUTPin name="LO1" />
		<DUTPin name="LO2" />
		<DUTPin name="LO3" />
		<DUTPin name="HI0" />
		<DUTPin name="HI1" />
		<DUTPin name="HI2" />
		<DUTPin name="HI3" />
	</Pins>
	<PinGroups>
		<PinGroup name="AllPins">
			<PinReference pin="LO0" />
			<PinReference pin="LO1" />
			<PinReference pin="LO2" />
			<PinReference pin="LO3" />
			<PinReference pin="HI0" />
			<PinReference pin="HI1" />
			<PinReference pin="HI2" />
			<PinReference pin="HI3" />
		</PinGroup>
		<PinGroup name="LowPins">
			<PinReference pin="LO0" />
			<PinReference pin="LO1" />
			<PinReference pin="LO2" />
			<PinReference pin="LO3" />
		</PinGroup>
		<PinGroup name="HighPins">
			<PinReference pin="HI0" />
			<PinReference pin="HI1" />
			<PinReference pin="HI2" />
			<PinReference pin="HI3" />
		</PinGroup>
	</PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
		<Site siteNumber="2" />
		<Site siteNumber="3" />
	</Sites>
	<Connections>
		<Connection pin="HI0" siteNumber="0" instrument="PXI1Slot2" channel="0" />
		<Connection pin="HI0" siteNumber="1" instrument="PXI1Slot2" channel="1" />
		<Connection pin="HI0" siteNumber="2" instrument="PXI1Slot2" channel="2" />
		<Connection pin="HI0" siteNumber="3" instrument="PXI1Slot2" channel="3" />
		<Connection pin="HI1" siteNumber="0" instrument="PXI1Slot2" channel="4" />
		<Connection pin="HI1" siteNumber="1" instrument="PXI1Slot2" channel="5" />
		<Connection pin="HI1" siteNumber="2" instrument="PXI1Slot2" channel="6" />
		<Connection pin="HI1" siteNumber="3" instrument="PXI1Slot2" channel="7" />
		<Connection pin="HI2" siteNumber="0" instrument="PXI1Slot2" channel="8" />
		<Connection pin="HI2" siteNumber="1" instrument="PXI1Slot2" channel="9" />
		<Connection pin="HI2" siteNumber="2" instrument="PXI1Slot2" channel="10" />
		<Connection pin="HI2" siteNumber="3" instrument="PXI1Slot2" channel="11" />
		<Connection pin="HI3" siteNumber="0" instrument="PXI1Slot2" channel="12" />
		<Connection pin="HI3" siteNumber="1" instrument="PXI1Slot2" channel="13" />
		<Connection pin="HI3" siteNumber="3" instrument="PXI1Slot2" channel="15" />
		<Connection pin="HI3" siteNumber="2" instrument="PXI1Slot2" channel="14" />
		<Connection pin="LO0" siteNumber="0" instrument="PXI1Slot5" channel="16" />
		<Connection pin="LO0" siteNumber="1" instrument="PXI1Slot5" channel="17" />
		<Connection pin="LO0" siteNumber="2" instrument="PXI1Slot5" channel="18" />
		<Connection pin="LO0" siteNumber="3" instrument="PXI1Slot5" channel="19" />
		<Connection pin="LO1" siteNumber="0" instrument="PXI1Slot5" channel="20" />
		<Connection pin="LO1" siteNumber="1" instrument="PXI1Slot5" channel="21" />
		<Connection pin="LO1" siteNumber="2" instrument="PXI1Slot5" channel="22" />
		<Connection pin="LO1" siteNumber="3" instrument="PXI1Slot5" channel="23" />
		<Connection pin="LO2" siteNumber="0" instrument="PXI1Slot5" channel="24" />
		<Connection pin="LO2" siteNumber="1" instrument="PXI1Slot5" channel="25" />
		<Connection pin="LO2" siteNumber="2" instrument="PXI1Slot5" channel="26" />
		<Connection pin="LO2" siteNumber="3" instrument="PXI1Slot5" channel="27" />
		<Connection pin="LO3" siteNumber="0" instrument="PXI1Slot5" channel="28" />
		<Connection pin="LO3" siteNumber="1" instrument="PXI1Slot5" channel="29" />
		<Connection pin="LO3" siteNumber="2" instrument="PXI1Slot5" channel="30" />
		<Connection pin="LO3" siteNumber="3" instrument="PXI1Slot5" channel="31" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/multiple_patterns/specifications.specs sha256=0977c459ca4ca8266670d25873e498fd847d0fe9ab4b1d01ca3ef26d5ec6575d bytes=354 -->
## FILE: src/nidigital/system_tests/test_files/multiple_patterns/specifications.specs

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/multiple_patterns/specifications.specs`
- sha256: `0977c459ca4ca8266670d25873e498fd847d0fe9ab4b1d01ca3ef26d5ec6575d`
- bytes: 354

````text
<?xml version="1.0" encoding="utf-8"?>
<Specifications xmlns:f="http://www.ni.com/schemas/Semiconductor/Formula.xsd" schemaVersion="1.0" xmlns="http://www.ni.com/schemas/Semiconductor/Specifications.xsd">
  <Section name="AC">
    <f:Formula symbol="Period">
      <f:Definition>10 µ</f:Definition>
    </f:Formula>
  </Section>
</Specifications>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/multiple_patterns/test.digiproj sha256=5c66fdb7a53335109cca8be332e28da2d2dc484e853f6542b03f68c617f3aa47 bytes=3568 -->
## FILE: src/nidigital/system_tests/test_files/multiple_patterns/test.digiproj

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/multiple_patterns/test.digiproj`
- sha256: `5c66fdb7a53335109cca8be332e28da2d2dc484e853f6542b03f68c617f3aa47`
- bytes: 3568

````text
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="8B6DA5F67609C4E6786E0723E5D3D84A" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="5.3.1.52024" FeatureSetName="Digital Pattern Editor" Name="http://www.ni.com/PatternBasedDigital" OldestCompatibleVersion="4.5.0.0" Version="4.6.0.49152" />
		<ParsableNamespace AssemblyFileVersion="5.3.1.52024" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="5.2.0.49153" Version="5.2.0.49153" />
		<ApplicationVersionInfo Build="5.3.1.52024" Name="Digital Pattern Editor" Version="19.0.0" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<ProjectSettings Id="1" ModelDefinitionType="ProjectSettings" Name="ZProjectSettings" />
		<EmbeddedDefinitionReference Id="2" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="3" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<EmbeddedDefinitionReference Id="8" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}CaptureResultsDefinition" Name="CaptureResults">
				<CaptureResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="10" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}BurstResultsDefinition" Name="BurstResults">
				<BurstResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="12" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}SystemInfoDefinition" Name="SystemInfo">
				<SystemInfoDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="13" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}DigitalScopeDefinition" Name="DigitalScope">
				<DigitalScopeDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<FileReference Id="16" ModelDefinitionType="PinMap" Name="pin_map\.pinmap" StoragePath="pin_map.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="17" ModelDefinitionType="SpecificationsDefinition" Name="specifications\.specs" StoragePath="specifications.specs" />
			<FileReference Id="18" ModelDefinitionType="PinLevelsDefinition" Name="pin_levels\.digilevels" StoragePath="pin_levels.digilevels" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="19" ModelDefinitionType="TimingDefinition" Name="timing\.digitiming" StoragePath="timing.digitiming" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="20" ModelDefinitionType="DigitalPatternEditor.PatternDefinition" Name="pattern_a\.digipat" StoragePath="pattern_a.digipat" />
			<FileReference Id="23" ModelDefinitionType="DigitalPatternEditor.PatternDefinition" Name="pattern_b\.digipat" StoragePath="pattern_b.digipat" />
		</NameScopingEnvoy>
		<EmbeddedDefinitionReference Id="7" ModelDefinitionType="DigitalPatternEditor.ProjectPropertiesDefinition" Name="ProjectProperties">
			<ProjectPropertiesDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
		</EmbeddedDefinitionReference>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/multiple_patterns/timing.digitiming sha256=92d67c7e5b650a22e7e11508373f89994c08faed279ce44b344a2d7b1af25ae2 bytes=862 -->
## FILE: src/nidigital/system_tests/test_files/multiple_patterns/timing.digitiming

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/multiple_patterns/timing.digitiming`
- sha256: `92d67c7e5b650a22e7e11508373f89994c08faed279ce44b344a2d7b1af25ae2`
- bytes: 862

````text
<?xml version="1.0" encoding="utf-8"?>
<TimingFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/Timing">
  <TimingSheet>
    <TimeSets>
      <TimeSet name="t0">
        <Period>AC.Period</Period>
        <PinEdges>
          <PinEdge pin="AllPins">
            <ReturnToLow>
              <On>AC.Period * 0.1</On>
              <Data>AC.Period * 0.2</Data>
              <Return>AC.Period * 0.8</Return>
              <Off>AC.Period * 0.9</Off>
            </ReturnToLow>
            <CompareStrobe>
              <Strobe>AC.Period * 0.5</Strobe>
            </CompareStrobe>
            <DataSource>Pattern</DataSource>
          </PinEdge>
        </PinEdges>
      </TimeSet>
    </TimeSets>
  </TimingSheet>
</TimingFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/pin_map.pinmap sha256=4833390f1a2d0c2996859ea82c39b8e27019358d4aeeb99a182ff2427e690fc6 bytes=1443 -->
## FILE: src/nidigital/system_tests/test_files/pin_map.pinmap

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/pin_map.pinmap`
- sha256: `4833390f1a2d0c2996859ea82c39b8e27019358d4aeeb99a182ff2427e690fc6`
- bytes: 1443

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.5">
	<Instruments>
		<NIDigitalPatternInstrument name="PXI1Slot2" numberOfChannels="32" group="Digital" />
		<NIDigitalPatternInstrument name="PXI1Slot5" numberOfChannels="32" group="Digital" />
	</Instruments>
	<Pins>
		<DUTPin name="PinA" />
		<DUTPin name="PinB" />
		<DUTPin name="PinC" />
		<SystemPin name="SysPin" />
	</Pins>
	<PinGroups>
		<PinGroup name="DutPins">
			<PinReference pin="PinA" />
			<PinReference pin="PinB" />
			<PinReference pin="PinC" />
		</PinGroup>
		<PinGroup name="SysPins">
			<PinReference pin="SysPin" />
		</PinGroup>
	</PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="PinA" siteNumber="0" instrument="PXI1Slot2" channel="0" />
		<Connection pin="PinA" siteNumber="1" instrument="PXI1Slot5" channel="0" />
		<Connection pin="PinB" siteNumber="0" instrument="PXI1Slot2" channel="1" />
		<Connection pin="PinB" siteNumber="1" instrument="PXI1Slot5" channel="1" />
		<Connection pin="PinC" siteNumber="0" instrument="PXI1Slot2" channel="2" />
		<Connection pin="PinC" siteNumber="1" instrument="PXI1Slot5" channel="2" />
		<SystemConnection pin="SysPin" instrument="PXI1Slot2" channel="3" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/simple_pattern/pin_levels.digilevels sha256=8476ee4cebdd5267c105961ec5a26674daa4df8ef6f3e96b9421957bbf1f5638 bytes=555 -->
## FILE: src/nidigital/system_tests/test_files/simple_pattern/pin_levels.digilevels

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/simple_pattern/pin_levels.digilevels`
- sha256: `8476ee4cebdd5267c105961ec5a26674daa4df8ef6f3e96b9421957bbf1f5638`
- bytes: 555

````text
<?xml version="1.0" encoding="utf-8"?>
<PinLevelsFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/PinLevels">
  <PinLevelsSheet>
    <DigitalPinLevelSets>
      <DigitalPinLevelSet pin="AllPins">
        <Vil>1 V</Vil>
        <Vih>5 V</Vih>
        <Vol>2 V</Vol>
        <Voh>4 V</Voh>
        <TerminationMode>HighZ</TerminationMode>
      </DigitalPinLevelSet>
    </DigitalPinLevelSets>
  </PinLevelsSheet>
</PinLevelsFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/simple_pattern/pin_map.pinmap sha256=6d1fb7cf77a8a6f626f2c4c72af1f58b1eb5639d2088764aff54967b2589231d bytes=3971 -->
## FILE: src/nidigital/system_tests/test_files/simple_pattern/pin_map.pinmap

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/simple_pattern/pin_map.pinmap`
- sha256: `6d1fb7cf77a8a6f626f2c4c72af1f58b1eb5639d2088764aff54967b2589231d`
- bytes: 3971

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.5">
	<Instruments>
		<NIDigitalPatternInstrument name="PXI1Slot2" numberOfChannels="32" group="Digital" />
		<NIDigitalPatternInstrument name="PXI1Slot5" numberOfChannels="32" group="Digital" />
	</Instruments>
	<Pins>
		<DUTPin name="LO0" />
		<DUTPin name="LO1" />
		<DUTPin name="LO2" />
		<DUTPin name="LO3" />
		<DUTPin name="HI0" />
		<DUTPin name="HI1" />
		<DUTPin name="HI2" />
		<DUTPin name="HI3" />
	</Pins>
	<PinGroups>
		<PinGroup name="AllPins">
			<PinReference pin="LO0" />
			<PinReference pin="LO1" />
			<PinReference pin="LO2" />
			<PinReference pin="LO3" />
			<PinReference pin="HI0" />
			<PinReference pin="HI1" />
			<PinReference pin="HI2" />
			<PinReference pin="HI3" />
		</PinGroup>
		<PinGroup name="LowPins">
			<PinReference pin="LO0" />
			<PinReference pin="LO1" />
			<PinReference pin="LO2" />
			<PinReference pin="LO3" />
		</PinGroup>
		<PinGroup name="HighPins">
			<PinReference pin="HI0" />
			<PinReference pin="HI1" />
			<PinReference pin="HI2" />
			<PinReference pin="HI3" />
		</PinGroup>
	</PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
		<Site siteNumber="2" />
		<Site siteNumber="3" />
	</Sites>
	<Connections>
		<Connection pin="HI0" siteNumber="0" instrument="PXI1Slot2" channel="0" />
		<Connection pin="HI0" siteNumber="1" instrument="PXI1Slot2" channel="1" />
		<Connection pin="HI0" siteNumber="2" instrument="PXI1Slot2" channel="2" />
		<Connection pin="HI0" siteNumber="3" instrument="PXI1Slot2" channel="3" />
		<Connection pin="HI1" siteNumber="0" instrument="PXI1Slot2" channel="4" />
		<Connection pin="HI1" siteNumber="1" instrument="PXI1Slot2" channel="5" />
		<Connection pin="HI1" siteNumber="2" instrument="PXI1Slot2" channel="6" />
		<Connection pin="HI1" siteNumber="3" instrument="PXI1Slot2" channel="7" />
		<Connection pin="HI2" siteNumber="0" instrument="PXI1Slot2" channel="8" />
		<Connection pin="HI2" siteNumber="1" instrument="PXI1Slot2" channel="9" />
		<Connection pin="HI2" siteNumber="2" instrument="PXI1Slot2" channel="10" />
		<Connection pin="HI2" siteNumber="3" instrument="PXI1Slot2" channel="11" />
		<Connection pin="HI3" siteNumber="0" instrument="PXI1Slot2" channel="12" />
		<Connection pin="HI3" siteNumber="1" instrument="PXI1Slot2" channel="13" />
		<Connection pin="HI3" siteNumber="3" instrument="PXI1Slot2" channel="15" />
		<Connection pin="HI3" siteNumber="2" instrument="PXI1Slot2" channel="14" />
		<Connection pin="LO0" siteNumber="0" instrument="PXI1Slot5" channel="16" />
		<Connection pin="LO0" siteNumber="1" instrument="PXI1Slot5" channel="17" />
		<Connection pin="LO0" siteNumber="2" instrument="PXI1Slot5" channel="18" />
		<Connection pin="LO0" siteNumber="3" instrument="PXI1Slot5" channel="19" />
		<Connection pin="LO1" siteNumber="0" instrument="PXI1Slot5" channel="20" />
		<Connection pin="LO1" siteNumber="1" instrument="PXI1Slot5" channel="21" />
		<Connection pin="LO1" siteNumber="2" instrument="PXI1Slot5" channel="22" />
		<Connection pin="LO1" siteNumber="3" instrument="PXI1Slot5" channel="23" />
		<Connection pin="LO2" siteNumber="0" instrument="PXI1Slot5" channel="24" />
		<Connection pin="LO2" siteNumber="1" instrument="PXI1Slot5" channel="25" />
		<Connection pin="LO2" siteNumber="2" instrument="PXI1Slot5" channel="26" />
		<Connection pin="LO2" siteNumber="3" instrument="PXI1Slot5" channel="27" />
		<Connection pin="LO3" siteNumber="0" instrument="PXI1Slot5" channel="28" />
		<Connection pin="LO3" siteNumber="1" instrument="PXI1Slot5" channel="29" />
		<Connection pin="LO3" siteNumber="2" instrument="PXI1Slot5" channel="30" />
		<Connection pin="LO3" siteNumber="3" instrument="PXI1Slot5" channel="31" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/simple_pattern/specifications.specs sha256=0977c459ca4ca8266670d25873e498fd847d0fe9ab4b1d01ca3ef26d5ec6575d bytes=354 -->
## FILE: src/nidigital/system_tests/test_files/simple_pattern/specifications.specs

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/simple_pattern/specifications.specs`
- sha256: `0977c459ca4ca8266670d25873e498fd847d0fe9ab4b1d01ca3ef26d5ec6575d`
- bytes: 354

````text
<?xml version="1.0" encoding="utf-8"?>
<Specifications xmlns:f="http://www.ni.com/schemas/Semiconductor/Formula.xsd" schemaVersion="1.0" xmlns="http://www.ni.com/schemas/Semiconductor/Specifications.xsd">
  <Section name="AC">
    <f:Formula symbol="Period">
      <f:Definition>10 µ</f:Definition>
    </f:Formula>
  </Section>
</Specifications>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/simple_pattern/test.digiproj sha256=6439d0d60790b7879db624d6fa058f5702105a35ef4811ffce34447f2866fce8 bytes=3415 -->
## FILE: src/nidigital/system_tests/test_files/simple_pattern/test.digiproj

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/simple_pattern/test.digiproj`
- sha256: `6439d0d60790b7879db624d6fa058f5702105a35ef4811ffce34447f2866fce8`
- bytes: 3415

````text
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="E3A8965ACB2DA3FB3488B870364FC0F5" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="5.3.1.52024" FeatureSetName="Digital Pattern Editor" Name="http://www.ni.com/PatternBasedDigital" OldestCompatibleVersion="4.5.0.0" Version="4.6.0.49152" />
		<ParsableNamespace AssemblyFileVersion="5.3.1.52024" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="5.2.0.49153" Version="5.2.0.49153" />
		<ApplicationVersionInfo Build="5.3.1.52024" Name="Digital Pattern Editor" Version="19.0.0" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<ProjectSettings Id="1" ModelDefinitionType="ProjectSettings" Name="ZProjectSettings" />
		<EmbeddedDefinitionReference Id="2" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="3" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<EmbeddedDefinitionReference Id="8" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}CaptureResultsDefinition" Name="CaptureResults">
				<CaptureResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="10" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}BurstResultsDefinition" Name="BurstResults">
				<BurstResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="12" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}SystemInfoDefinition" Name="SystemInfo">
				<SystemInfoDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="13" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}DigitalScopeDefinition" Name="DigitalScope">
				<DigitalScopeDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<FileReference Id="16" ModelDefinitionType="PinMap" Name="pin_map\.pinmap" StoragePath="pin_map.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="17" ModelDefinitionType="SpecificationsDefinition" Name="specifications\.specs" StoragePath="specifications.specs" />
			<FileReference Id="18" ModelDefinitionType="PinLevelsDefinition" Name="pin_levels\.digilevels" StoragePath="pin_levels.digilevels" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="19" ModelDefinitionType="TimingDefinition" Name="timing\.digitiming" StoragePath="timing.digitiming" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="20" ModelDefinitionType="DigitalPatternEditor.PatternDefinition" Name="pattern\.digipat" StoragePath="pattern.digipat" />
		</NameScopingEnvoy>
		<EmbeddedDefinitionReference Id="7" ModelDefinitionType="DigitalPatternEditor.ProjectPropertiesDefinition" Name="ProjectProperties">
			<ProjectPropertiesDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
		</EmbeddedDefinitionReference>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/simple_pattern/timing.digitiming sha256=92d67c7e5b650a22e7e11508373f89994c08faed279ce44b344a2d7b1af25ae2 bytes=862 -->
## FILE: src/nidigital/system_tests/test_files/simple_pattern/timing.digitiming

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/simple_pattern/timing.digitiming`
- sha256: `92d67c7e5b650a22e7e11508373f89994c08faed279ce44b344a2d7b1af25ae2`
- bytes: 862

````text
<?xml version="1.0" encoding="utf-8"?>
<TimingFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/Timing">
  <TimingSheet>
    <TimeSets>
      <TimeSet name="t0">
        <Period>AC.Period</Period>
        <PinEdges>
          <PinEdge pin="AllPins">
            <ReturnToLow>
              <On>AC.Period * 0.1</On>
              <Data>AC.Period * 0.2</Data>
              <Return>AC.Period * 0.8</Return>
              <Off>AC.Period * 0.9</Off>
            </ReturnToLow>
            <CompareStrobe>
              <Strobe>AC.Period * 0.5</Strobe>
            </CompareStrobe>
            <DataSource>Pattern</DataSource>
          </PinEdge>
        </PinEdges>
      </TimeSet>
    </TimeSets>
  </TimingSheet>
</TimingFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/specifications_levels_and_timing_multiple/levels1.digilevels sha256=27891cae48c9cedfd3199edcf7613dc03769ebdf68c80e6aed84623d7f5f4e24 bytes=632 -->
## FILE: src/nidigital/system_tests/test_files/specifications_levels_and_timing_multiple/levels1.digilevels

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/specifications_levels_and_timing_multiple/levels1.digilevels`
- sha256: `27891cae48c9cedfd3199edcf7613dc03769ebdf68c80e6aed84623d7f5f4e24`
- bytes: 632

````text
<?xml version="1.0" encoding="utf-8"?>
<PinLevelsFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/PinLevels">
  <PinLevelsSheet>
    <DigitalPinLevelSets>
      <DigitalPinLevelSet pin="AllPins">
        <Vil>1 V</Vil>
        <Vih>3 V + DC.VCC + DC.Offset</Vih>
        <Vol>2 V</Vol>
        <Voh>4 V</Voh>
        <TerminationMode>HighZ</TerminationMode>
        <Comment>Depends on both specs files</Comment>
      </DigitalPinLevelSet>
    </DigitalPinLevelSets>
  </PinLevelsSheet>
</PinLevelsFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/specifications_levels_and_timing_multiple/levels2.digilevels sha256=8c1bee69b5352f4dff9f2ffdd2df55565e540a8703fb5f0879b216288b60388a bytes=632 -->
## FILE: src/nidigital/system_tests/test_files/specifications_levels_and_timing_multiple/levels2.digilevels

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/specifications_levels_and_timing_multiple/levels2.digilevels`
- sha256: `8c1bee69b5352f4dff9f2ffdd2df55565e540a8703fb5f0879b216288b60388a`
- bytes: 632

````text
<?xml version="1.0" encoding="utf-8"?>
<PinLevelsFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/PinLevels">
  <PinLevelsSheet>
    <DigitalPinLevelSets>
      <DigitalPinLevelSet pin="AllPins">
        <Vil>1 V</Vil>
        <Vih>2 V + DC.VCC + DC.Offset</Vih>
        <Vol>2 V</Vol>
        <Voh>4 V</Voh>
        <TerminationMode>HighZ</TerminationMode>
        <Comment>Depends on both specs files</Comment>
      </DigitalPinLevelSet>
    </DigitalPinLevelSets>
  </PinLevelsSheet>
</PinLevelsFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/specifications_levels_and_timing_multiple/pin_map.pinmap sha256=6d1fb7cf77a8a6f626f2c4c72af1f58b1eb5639d2088764aff54967b2589231d bytes=3971 -->
## FILE: src/nidigital/system_tests/test_files/specifications_levels_and_timing_multiple/pin_map.pinmap

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/specifications_levels_and_timing_multiple/pin_map.pinmap`
- sha256: `6d1fb7cf77a8a6f626f2c4c72af1f58b1eb5639d2088764aff54967b2589231d`
- bytes: 3971

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.5">
	<Instruments>
		<NIDigitalPatternInstrument name="PXI1Slot2" numberOfChannels="32" group="Digital" />
		<NIDigitalPatternInstrument name="PXI1Slot5" numberOfChannels="32" group="Digital" />
	</Instruments>
	<Pins>
		<DUTPin name="LO0" />
		<DUTPin name="LO1" />
		<DUTPin name="LO2" />
		<DUTPin name="LO3" />
		<DUTPin name="HI0" />
		<DUTPin name="HI1" />
		<DUTPin name="HI2" />
		<DUTPin name="HI3" />
	</Pins>
	<PinGroups>
		<PinGroup name="AllPins">
			<PinReference pin="LO0" />
			<PinReference pin="LO1" />
			<PinReference pin="LO2" />
			<PinReference pin="LO3" />
			<PinReference pin="HI0" />
			<PinReference pin="HI1" />
			<PinReference pin="HI2" />
			<PinReference pin="HI3" />
		</PinGroup>
		<PinGroup name="LowPins">
			<PinReference pin="LO0" />
			<PinReference pin="LO1" />
			<PinReference pin="LO2" />
			<PinReference pin="LO3" />
		</PinGroup>
		<PinGroup name="HighPins">
			<PinReference pin="HI0" />
			<PinReference pin="HI1" />
			<PinReference pin="HI2" />
			<PinReference pin="HI3" />
		</PinGroup>
	</PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
		<Site siteNumber="2" />
		<Site siteNumber="3" />
	</Sites>
	<Connections>
		<Connection pin="HI0" siteNumber="0" instrument="PXI1Slot2" channel="0" />
		<Connection pin="HI0" siteNumber="1" instrument="PXI1Slot2" channel="1" />
		<Connection pin="HI0" siteNumber="2" instrument="PXI1Slot2" channel="2" />
		<Connection pin="HI0" siteNumber="3" instrument="PXI1Slot2" channel="3" />
		<Connection pin="HI1" siteNumber="0" instrument="PXI1Slot2" channel="4" />
		<Connection pin="HI1" siteNumber="1" instrument="PXI1Slot2" channel="5" />
		<Connection pin="HI1" siteNumber="2" instrument="PXI1Slot2" channel="6" />
		<Connection pin="HI1" siteNumber="3" instrument="PXI1Slot2" channel="7" />
		<Connection pin="HI2" siteNumber="0" instrument="PXI1Slot2" channel="8" />
		<Connection pin="HI2" siteNumber="1" instrument="PXI1Slot2" channel="9" />
		<Connection pin="HI2" siteNumber="2" instrument="PXI1Slot2" channel="10" />
		<Connection pin="HI2" siteNumber="3" instrument="PXI1Slot2" channel="11" />
		<Connection pin="HI3" siteNumber="0" instrument="PXI1Slot2" channel="12" />
		<Connection pin="HI3" siteNumber="1" instrument="PXI1Slot2" channel="13" />
		<Connection pin="HI3" siteNumber="3" instrument="PXI1Slot2" channel="15" />
		<Connection pin="HI3" siteNumber="2" instrument="PXI1Slot2" channel="14" />
		<Connection pin="LO0" siteNumber="0" instrument="PXI1Slot5" channel="16" />
		<Connection pin="LO0" siteNumber="1" instrument="PXI1Slot5" channel="17" />
		<Connection pin="LO0" siteNumber="2" instrument="PXI1Slot5" channel="18" />
		<Connection pin="LO0" siteNumber="3" instrument="PXI1Slot5" channel="19" />
		<Connection pin="LO1" siteNumber="0" instrument="PXI1Slot5" channel="20" />
		<Connection pin="LO1" siteNumber="1" instrument="PXI1Slot5" channel="21" />
		<Connection pin="LO1" siteNumber="2" instrument="PXI1Slot5" channel="22" />
		<Connection pin="LO1" siteNumber="3" instrument="PXI1Slot5" channel="23" />
		<Connection pin="LO2" siteNumber="0" instrument="PXI1Slot5" channel="24" />
		<Connection pin="LO2" siteNumber="1" instrument="PXI1Slot5" channel="25" />
		<Connection pin="LO2" siteNumber="2" instrument="PXI1Slot5" channel="26" />
		<Connection pin="LO2" siteNumber="3" instrument="PXI1Slot5" channel="27" />
		<Connection pin="LO3" siteNumber="0" instrument="PXI1Slot5" channel="28" />
		<Connection pin="LO3" siteNumber="1" instrument="PXI1Slot5" channel="29" />
		<Connection pin="LO3" siteNumber="2" instrument="PXI1Slot5" channel="30" />
		<Connection pin="LO3" siteNumber="3" instrument="PXI1Slot5" channel="31" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/specifications_levels_and_timing_multiple/specs1.specs sha256=38eb53ddc5cde54749fb10750b1c2293bc9b03039187b47021d73e4e48c40201 bytes=479 -->
## FILE: src/nidigital/system_tests/test_files/specifications_levels_and_timing_multiple/specs1.specs

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/specifications_levels_and_timing_multiple/specs1.specs`
- sha256: `38eb53ddc5cde54749fb10750b1c2293bc9b03039187b47021d73e4e48c40201`
- bytes: 479

````text
<?xml version="1.0" encoding="utf-8"?>
<Specifications xmlns:f="http://www.ni.com/schemas/Semiconductor/Formula.xsd" schemaVersion="1.0" xmlns="http://www.ni.com/schemas/Semiconductor/Specifications.xsd">
  <Section name="AC">
    <f:Formula symbol="Period">
      <f:Definition>10 µ</f:Definition>
    </f:Formula>
  </Section>
  <Section name="DC">
    <f:Formula symbol="VCC">
      <f:Definition>2 V</f:Definition>
    </f:Formula>
  </Section>
</Specifications>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/specifications_levels_and_timing_multiple/specs2.specs sha256=eacfa5788bec3bbbb44e9f8cc0bc56051ac303610ca8ed1e1ae41ecb671f089e bytes=550 -->
## FILE: src/nidigital/system_tests/test_files/specifications_levels_and_timing_multiple/specs2.specs

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/specifications_levels_and_timing_multiple/specs2.specs`
- sha256: `eacfa5788bec3bbbb44e9f8cc0bc56051ac303610ca8ed1e1ae41ecb671f089e`
- bytes: 550

````text
<?xml version="1.0" encoding="utf-8"?>
<Specifications xmlns:f="http://www.ni.com/schemas/Semiconductor/Formula.xsd" schemaVersion="1.0" xmlns="http://www.ni.com/schemas/Semiconductor/Specifications.xsd">
  <Section name="AC">
    <f:Formula symbol="Frequency">
      <f:Definition>1 / AC.Period</f:Definition>
      <f:Comment>Depends on specs1.specs</f:Comment>
    </f:Formula>
  </Section>
  <Section name="DC">
    <f:Formula symbol="Offset">
      <f:Definition>100 mV</f:Definition>
    </f:Formula>
  </Section>
</Specifications>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/specifications_levels_and_timing_multiple/test.digiproj sha256=363b7f1a765711011b5f84242a0ed171a95fdbc1258e7608542fd1eace5f8bbb bytes=3636 -->
## FILE: src/nidigital/system_tests/test_files/specifications_levels_and_timing_multiple/test.digiproj

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/specifications_levels_and_timing_multiple/test.digiproj`
- sha256: `363b7f1a765711011b5f84242a0ed171a95fdbc1258e7608542fd1eace5f8bbb`
- bytes: 3636

````text
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="4EB353DE0E5729B338D9BA13B1063297" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="5.3.1.52024" FeatureSetName="Digital Pattern Editor" Name="http://www.ni.com/PatternBasedDigital" OldestCompatibleVersion="4.5.0.0" Version="4.6.0.49152" />
		<ParsableNamespace AssemblyFileVersion="5.3.1.52024" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="5.2.0.49153" Version="5.2.0.49153" />
		<ApplicationVersionInfo Build="5.3.1.52024" Name="Digital Pattern Editor" Version="19.0.0" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<ProjectSettings Id="1" ModelDefinitionType="ProjectSettings" Name="ZProjectSettings" />
		<EmbeddedDefinitionReference Id="2" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="3" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<EmbeddedDefinitionReference Id="8" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}CaptureResultsDefinition" Name="CaptureResults">
				<CaptureResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="10" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}BurstResultsDefinition" Name="BurstResults">
				<BurstResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="12" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}SystemInfoDefinition" Name="SystemInfo">
				<SystemInfoDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="13" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}DigitalScopeDefinition" Name="DigitalScope">
				<DigitalScopeDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<FileReference Id="16" ModelDefinitionType="PinMap" Name="pin_map\.pinmap" StoragePath="pin_map.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="17" ModelDefinitionType="SpecificationsDefinition" Name="specs1\.specs" StoragePath="specs1.specs" />
			<FileReference Id="18" ModelDefinitionType="PinLevelsDefinition" Name="levels1\.digilevels" StoragePath="levels1.digilevels" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="19" ModelDefinitionType="TimingDefinition" Name="timing1\.digitiming" StoragePath="timing1.digitiming" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="23" ModelDefinitionType="SpecificationsDefinition" Name="specs2\.specs" StoragePath="specs2.specs" />
			<FileReference Id="24" ModelDefinitionType="PinLevelsDefinition" Name="levels2\.digilevels" StoragePath="levels2.digilevels" />
			<FileReference Id="25" ModelDefinitionType="TimingDefinition" Name="timing2\.digitiming" StoragePath="timing2.digitiming" />
		</NameScopingEnvoy>
		<EmbeddedDefinitionReference Id="7" ModelDefinitionType="DigitalPatternEditor.ProjectPropertiesDefinition" Name="ProjectProperties">
			<ProjectPropertiesDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
		</EmbeddedDefinitionReference>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/specifications_levels_and_timing_multiple/timing1.digitiming sha256=a52ec9ba50997cd14e7df7733f7b62935799e74dd3f64dbdae11db3438918a89 bytes=949 -->
## FILE: src/nidigital/system_tests/test_files/specifications_levels_and_timing_multiple/timing1.digitiming

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/specifications_levels_and_timing_multiple/timing1.digitiming`
- sha256: `a52ec9ba50997cd14e7df7733f7b62935799e74dd3f64dbdae11db3438918a89`
- bytes: 949

````text
<?xml version="1.0" encoding="utf-8"?>
<TimingFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/Timing">
  <TimingSheet>
    <TimeSets>
      <TimeSet name="t0">
        <Period>AC.Period + (1 / AC.Frequency) * 0.1</Period>
        <PinEdges>
          <PinEdge pin="AllPins">
            <ReturnToLow>
              <On>AC.Period * 0.1</On>
              <Data>AC.Period * 0.2</Data>
              <Return>AC.Period * 0.8</Return>
              <Off>AC.Period * 0.9</Off>
            </ReturnToLow>
            <CompareStrobe>
              <Strobe>AC.Period * 0.5</Strobe>
            </CompareStrobe>
            <DataSource>Pattern</DataSource>
            <Comment>Depends on both specs files</Comment>
          </PinEdge>
        </PinEdges>
      </TimeSet>
    </TimeSets>
  </TimingSheet>
</TimingFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/specifications_levels_and_timing_multiple/timing2.digitiming sha256=8aa81b52a808036bb838bf227cb3a35b9b1e02ea61dc53070296dca892c15b95 bytes=949 -->
## FILE: src/nidigital/system_tests/test_files/specifications_levels_and_timing_multiple/timing2.digitiming

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/specifications_levels_and_timing_multiple/timing2.digitiming`
- sha256: `8aa81b52a808036bb838bf227cb3a35b9b1e02ea61dc53070296dca892c15b95`
- bytes: 949

````text
<?xml version="1.0" encoding="utf-8"?>
<TimingFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/Timing">
  <TimingSheet>
    <TimeSets>
      <TimeSet name="t0">
        <Period>AC.Period + (1 / AC.Frequency) * 0.2</Period>
        <PinEdges>
          <PinEdge pin="AllPins">
            <ReturnToLow>
              <On>AC.Period * 0.1</On>
              <Data>AC.Period * 0.2</Data>
              <Return>AC.Period * 0.8</Return>
              <Off>AC.Period * 0.9</Off>
            </ReturnToLow>
            <CompareStrobe>
              <Strobe>AC.Period * 0.5</Strobe>
            </CompareStrobe>
            <DataSource>Pattern</DataSource>
            <Comment>Depends on both specs files</Comment>
          </PinEdge>
        </PinEdges>
      </TimeSet>
    </TimeSets>
  </TimingSheet>
</TimingFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/specifications_levels_and_timing_single/levels.digilevels sha256=2763c4175d788b8f73aeffb64dcf1eb2c8bd25e79cbe771a6860d1b0fe041573 bytes=620 -->
## FILE: src/nidigital/system_tests/test_files/specifications_levels_and_timing_single/levels.digilevels

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/specifications_levels_and_timing_single/levels.digilevels`
- sha256: `2763c4175d788b8f73aeffb64dcf1eb2c8bd25e79cbe771a6860d1b0fe041573`
- bytes: 620

````text
<?xml version="1.0" encoding="utf-8"?>
<PinLevelsFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/PinLevels">
  <PinLevelsSheet>
    <DigitalPinLevelSets>
      <DigitalPinLevelSet pin="AllPins">
        <Vil>1 V</Vil>
        <Vih>3 V + DC.VCC</Vih>
        <Vol>2 V</Vol>
        <Voh>4 V</Voh>
        <TerminationMode>HighZ</TerminationMode>
        <Comment>Depends on both specs files</Comment>
      </DigitalPinLevelSet>
    </DigitalPinLevelSets>
  </PinLevelsSheet>
</PinLevelsFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/specifications_levels_and_timing_single/pin_map.pinmap sha256=6d1fb7cf77a8a6f626f2c4c72af1f58b1eb5639d2088764aff54967b2589231d bytes=3971 -->
## FILE: src/nidigital/system_tests/test_files/specifications_levels_and_timing_single/pin_map.pinmap

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/specifications_levels_and_timing_single/pin_map.pinmap`
- sha256: `6d1fb7cf77a8a6f626f2c4c72af1f58b1eb5639d2088764aff54967b2589231d`
- bytes: 3971

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.5">
	<Instruments>
		<NIDigitalPatternInstrument name="PXI1Slot2" numberOfChannels="32" group="Digital" />
		<NIDigitalPatternInstrument name="PXI1Slot5" numberOfChannels="32" group="Digital" />
	</Instruments>
	<Pins>
		<DUTPin name="LO0" />
		<DUTPin name="LO1" />
		<DUTPin name="LO2" />
		<DUTPin name="LO3" />
		<DUTPin name="HI0" />
		<DUTPin name="HI1" />
		<DUTPin name="HI2" />
		<DUTPin name="HI3" />
	</Pins>
	<PinGroups>
		<PinGroup name="AllPins">
			<PinReference pin="LO0" />
			<PinReference pin="LO1" />
			<PinReference pin="LO2" />
			<PinReference pin="LO3" />
			<PinReference pin="HI0" />
			<PinReference pin="HI1" />
			<PinReference pin="HI2" />
			<PinReference pin="HI3" />
		</PinGroup>
		<PinGroup name="LowPins">
			<PinReference pin="LO0" />
			<PinReference pin="LO1" />
			<PinReference pin="LO2" />
			<PinReference pin="LO3" />
		</PinGroup>
		<PinGroup name="HighPins">
			<PinReference pin="HI0" />
			<PinReference pin="HI1" />
			<PinReference pin="HI2" />
			<PinReference pin="HI3" />
		</PinGroup>
	</PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
		<Site siteNumber="2" />
		<Site siteNumber="3" />
	</Sites>
	<Connections>
		<Connection pin="HI0" siteNumber="0" instrument="PXI1Slot2" channel="0" />
		<Connection pin="HI0" siteNumber="1" instrument="PXI1Slot2" channel="1" />
		<Connection pin="HI0" siteNumber="2" instrument="PXI1Slot2" channel="2" />
		<Connection pin="HI0" siteNumber="3" instrument="PXI1Slot2" channel="3" />
		<Connection pin="HI1" siteNumber="0" instrument="PXI1Slot2" channel="4" />
		<Connection pin="HI1" siteNumber="1" instrument="PXI1Slot2" channel="5" />
		<Connection pin="HI1" siteNumber="2" instrument="PXI1Slot2" channel="6" />
		<Connection pin="HI1" siteNumber="3" instrument="PXI1Slot2" channel="7" />
		<Connection pin="HI2" siteNumber="0" instrument="PXI1Slot2" channel="8" />
		<Connection pin="HI2" siteNumber="1" instrument="PXI1Slot2" channel="9" />
		<Connection pin="HI2" siteNumber="2" instrument="PXI1Slot2" channel="10" />
		<Connection pin="HI2" siteNumber="3" instrument="PXI1Slot2" channel="11" />
		<Connection pin="HI3" siteNumber="0" instrument="PXI1Slot2" channel="12" />
		<Connection pin="HI3" siteNumber="1" instrument="PXI1Slot2" channel="13" />
		<Connection pin="HI3" siteNumber="3" instrument="PXI1Slot2" channel="15" />
		<Connection pin="HI3" siteNumber="2" instrument="PXI1Slot2" channel="14" />
		<Connection pin="LO0" siteNumber="0" instrument="PXI1Slot5" channel="16" />
		<Connection pin="LO0" siteNumber="1" instrument="PXI1Slot5" channel="17" />
		<Connection pin="LO0" siteNumber="2" instrument="PXI1Slot5" channel="18" />
		<Connection pin="LO0" siteNumber="3" instrument="PXI1Slot5" channel="19" />
		<Connection pin="LO1" siteNumber="0" instrument="PXI1Slot5" channel="20" />
		<Connection pin="LO1" siteNumber="1" instrument="PXI1Slot5" channel="21" />
		<Connection pin="LO1" siteNumber="2" instrument="PXI1Slot5" channel="22" />
		<Connection pin="LO1" siteNumber="3" instrument="PXI1Slot5" channel="23" />
		<Connection pin="LO2" siteNumber="0" instrument="PXI1Slot5" channel="24" />
		<Connection pin="LO2" siteNumber="1" instrument="PXI1Slot5" channel="25" />
		<Connection pin="LO2" siteNumber="2" instrument="PXI1Slot5" channel="26" />
		<Connection pin="LO2" siteNumber="3" instrument="PXI1Slot5" channel="27" />
		<Connection pin="LO3" siteNumber="0" instrument="PXI1Slot5" channel="28" />
		<Connection pin="LO3" siteNumber="1" instrument="PXI1Slot5" channel="29" />
		<Connection pin="LO3" siteNumber="2" instrument="PXI1Slot5" channel="30" />
		<Connection pin="LO3" siteNumber="3" instrument="PXI1Slot5" channel="31" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/specifications_levels_and_timing_single/specs.specs sha256=38eb53ddc5cde54749fb10750b1c2293bc9b03039187b47021d73e4e48c40201 bytes=479 -->
## FILE: src/nidigital/system_tests/test_files/specifications_levels_and_timing_single/specs.specs

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/specifications_levels_and_timing_single/specs.specs`
- sha256: `38eb53ddc5cde54749fb10750b1c2293bc9b03039187b47021d73e4e48c40201`
- bytes: 479

````text
<?xml version="1.0" encoding="utf-8"?>
<Specifications xmlns:f="http://www.ni.com/schemas/Semiconductor/Formula.xsd" schemaVersion="1.0" xmlns="http://www.ni.com/schemas/Semiconductor/Specifications.xsd">
  <Section name="AC">
    <f:Formula symbol="Period">
      <f:Definition>10 µ</f:Definition>
    </f:Formula>
  </Section>
  <Section name="DC">
    <f:Formula symbol="VCC">
      <f:Definition>2 V</f:Definition>
    </f:Formula>
  </Section>
</Specifications>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/specifications_levels_and_timing_single/test.digiproj sha256=74925b7625b0a70f8892f16800dc788b92daab7602abad6b40a6238f1a911b9d bytes=3244 -->
## FILE: src/nidigital/system_tests/test_files/specifications_levels_and_timing_single/test.digiproj

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/specifications_levels_and_timing_single/test.digiproj`
- sha256: `74925b7625b0a70f8892f16800dc788b92daab7602abad6b40a6238f1a911b9d`
- bytes: 3244

````text
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="041CFD3898DCA61BFAE728BF3559B76A" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="5.3.1.52024" FeatureSetName="Digital Pattern Editor" Name="http://www.ni.com/PatternBasedDigital" OldestCompatibleVersion="4.5.0.0" Version="4.6.0.49152" />
		<ParsableNamespace AssemblyFileVersion="5.3.1.52024" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="5.2.0.49153" Version="5.2.0.49153" />
		<ApplicationVersionInfo Build="5.3.1.52024" Name="Digital Pattern Editor" Version="19.0.0" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<ProjectSettings Id="1" ModelDefinitionType="ProjectSettings" Name="ZProjectSettings" />
		<EmbeddedDefinitionReference Id="2" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="3" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<EmbeddedDefinitionReference Id="8" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}CaptureResultsDefinition" Name="CaptureResults">
				<CaptureResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="10" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}BurstResultsDefinition" Name="BurstResults">
				<BurstResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="12" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}SystemInfoDefinition" Name="SystemInfo">
				<SystemInfoDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="13" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}DigitalScopeDefinition" Name="DigitalScope">
				<DigitalScopeDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<FileReference Id="16" ModelDefinitionType="PinMap" Name="pin_map\.pinmap" StoragePath="pin_map.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="17" ModelDefinitionType="SpecificationsDefinition" Name="specs\.specs" StoragePath="specs.specs" />
			<FileReference Id="18" ModelDefinitionType="PinLevelsDefinition" Name="levels\.digilevels" StoragePath="levels.digilevels" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="19" ModelDefinitionType="TimingDefinition" Name="timing\.digitiming" StoragePath="timing.digitiming" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
		</NameScopingEnvoy>
		<EmbeddedDefinitionReference Id="7" ModelDefinitionType="DigitalPatternEditor.ProjectPropertiesDefinition" Name="ProjectProperties">
			<ProjectPropertiesDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
		</EmbeddedDefinitionReference>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nidigital/system_tests/test_files/specifications_levels_and_timing_single/timing.digitiming sha256=92cac071a9e478b29e66f70bdde1424f9fe9ba1863a5557da1a98d6135e11d44 bytes=922 -->
## FILE: src/nidigital/system_tests/test_files/specifications_levels_and_timing_single/timing.digitiming

- repository: `ni/nimi-python`
- source_path: `src/nidigital/system_tests/test_files/specifications_levels_and_timing_single/timing.digitiming`
- sha256: `92cac071a9e478b29e66f70bdde1424f9fe9ba1863a5557da1a98d6135e11d44`
- bytes: 922

````text
<?xml version="1.0" encoding="utf-8"?>
<TimingFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/Timing">
  <TimingSheet>
    <TimeSets>
      <TimeSet name="t0">
        <Period>AC.Period</Period>
        <PinEdges>
          <PinEdge pin="AllPins">
            <ReturnToLow>
              <On>AC.Period * 0.1</On>
              <Data>AC.Period * 0.2</Data>
              <Return>AC.Period * 0.8</Return>
              <Off>AC.Period * 0.9</Off>
            </ReturnToLow>
            <CompareStrobe>
              <Strobe>AC.Period * 0.5</Strobe>
            </CompareStrobe>
            <DataSource>Pattern</DataSource>
            <Comment>Depends on both specs files</Comment>
          </PinEdge>
        </PinEdges>
      </TimeSet>
    </TimeSets>
  </TimingSheet>
</TimingFile>
````
