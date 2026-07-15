# NI OSS SOURCE SNAPSHOT: nimi-python

<!--NI_OSS_SNAPSHOT repo=ni/nimi-python commit=6511f8025f072f7f7021953888b916bbdc31aa2a -->

<!--NI_OSS_SOURCE repo=nimi-python path=src/nirfsg/metadata/functions.py sha256=a099fd956bbfc9e128b736c67d47d283a68bb71cedef1aa9413314439e270ea2 bytes=263904 -->
## FILE: src/nirfsg/metadata/functions.py

- repository: `ni/nimi-python`
- source_path: `src/nirfsg/metadata/functions.py`
- sha256: `a099fd956bbfc9e128b736c67d47d283a68bb71cedef1aa9413314439e270ea2`
- bytes: 263904

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-RFSG API metadata version 26.3.0d9999
functions = {
    'Abort': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nStops signal generation.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`NI-RFSG Programming State Model <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5670_programming_state_model.html>`_'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'AllocateArbWaveform': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nAllocates onboard memory space for the arbitrary waveform.\n\nUse this function to specify the total size of a waveform before writing the data. Use this function only if you are calling the nirfsg_WriteArbWaveform function multiple times to write a large waveform in smaller blocks.\n\nThe NI-RFSG device must be in the Configuration state before you call this function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Streaming Waveform Data <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming_waveform_data.html>`_'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name used to identify the waveform. This string is case-insensitive and alphanumeric, and it does not use reserved words.'
                },
                'name': 'waveformName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples to reserve in the onboard memory for the specified waveform. Each I/Q pair is considered one sample.'
                },
                'name': 'sizeInSamples',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ChangeExternalCalibrationPassword': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nChanges the external calibration password of the device.\n\n**Supported Devices:** PXIe-5611, PXIe-5653/5654, PXIe-5673/5673E, PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the old (current) external calibration password. This password is case sensitive.'
                },
                'name': 'oldPassword',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the new (desired) external calibration password.'
                },
                'name': 'newPassword',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckGenerationStatus': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nChecks the status of the generation.\n\nCall this function to check for any errors that might occur during the signal generation or to check whether the device has finished generating.\n\n**Supported Devices** : PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns information about the completion of signal generation.\n\n**Defined Values** :',
                    'table_body': [
                        [
                            'VI_TRUE',
                            'Signal generation is complete.'
                        ],
                        [
                            'VI_FALSE',
                            'Signal generation is occurring.'
                        ]
                    ],
                    'table_header': [
                        'Value',
                        'Description'
                    ]
                },
                'name': 'isDone',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckIfScriptExists': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReturns whether the script that you specify as NIRFSG_ATTR_SCRIPT_NAME exists.\n\n**Supported Devices** : PXIe-5673/5673E. PXIe-5830/5831/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the script. This string is case-insensitive.'
                },
                'name': 'scriptName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns VI_TRUE if the script exists.\n\n**Defined Values** :',
                    'table_body': [
                        [
                            'VI_TRUE',
                            'The script exists.'
                        ],
                        [
                            'VI_FALSE',
                            'The script does not exist.'
                        ]
                    ],
                    'table_header': [
                        'Value',
                        'Description'
                    ]
                },
                'name': 'scriptExists',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckIfWaveformExists': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReturns whether the waveform that you specify as NIRFSG_ATTR_WAVEFORM_NAME exists.\n\n**Supported Devices** : PXIe-5673/5673E, PXIe-5830/5831/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name used to store the waveform. This string is case-insensitive.'
                },
                'name': 'waveformName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns VI_TRUE if the waveform exists.\n\n**Defined Values** :',
                    'table_body': [
                        [
                            'VI_TRUE',
                            'The waveform exists.'
                        ],
                        [
                            'VI_FALSE',
                            'The waveform does not exist.'
                        ]
                    ],
                    'table_header': [
                        'Value',
                        'Description'
                    ]
                },
                'name': 'waveformExists',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearAllArbWaveforms': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nDeletes all currently defined waveforms and scripts.\n\nThe NI-RFSG device must be in the Configuration state before you call this function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearArbWaveform': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nDeletes a specified waveform from the pool of currently defined waveforms.\n\nThe NI-RFSG device must be in the Configuration state before you call this function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Name of the stored waveform to delete.'
                },
                'grpc_name': 'name',
                'name': 'name',
                'python_name': 'waveform_name',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearSelfCalibrateRange': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nClears the data obtained from the nirfsg_SelfCalibrateRange function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'Commit': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nPrograms the device with the correct settings.\n\nCalling this function moves the NI-RFSG device from the Configuration state to the Committed state. After this function executes, a change to any attribute reverts the NI-RFSG device to the Configuration state.\n\n**Supported devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`NI-RFSG Programming State Model <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5670_programming_state_model.html>`_'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDeembeddingTableInterpolationLinear': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSelects the linear interpolation method.\n\nIf the carrier frequency does not match a row in the de-embedding table, NI-RFSG performs a linear interpolation based on the entries in the de-embedding table to determine the parameters to use for de-embedding.\n\n**Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).'
                },
                'name': 'port',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the table.'
                },
                'name': 'tableName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the format of parameters to interpolate. **Defined Values** :',
                    'table_body': [
                        [
                            'NIRFSG_VAL_LINEAR_INTERPOLATION_FORMAT_REAL_AND_IMAGINARY',
                            '26000 (0x6590)',
                            'Results in a linear interpolation of the real portion of the complex number and a separate linear interpolation of the complex portion.'
                        ],
                        [
                            'NIRFSG_VAL_LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_AND_PHASE',
                            '26001 (0x6591)',
                            'Results in a linear interpolation of the magnitude and a separate linear interpolation of the phase.'
                        ],
                        [
                            'NIRFSG_VAL_LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_DB_AND_PHASE',
                            '26002 (0x6592)',
                            'Results in a linear interpolation of the magnitude, in decibels, and a separate linear interpolation of the phase.'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Value',
                        'Description'
                    ]
                },
                'enum': 'Format',
                'name': 'format',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDeembeddingTableInterpolationNearest': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSelects the nearest interpolation method.\n\nNI-RFSG uses the parameters of the table nearest to the carrier frequency for de-embedding.\n\n**Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).'
                },
                'name': 'port',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the table.'
                },
                'name': 'tableName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDeembeddingTableInterpolationSpline': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSelects the spline interpolation method.\n\nIf the carrier frequency does not match a row in the de-embedding table, NI-RFSG performs a spline interpolation based on the entries in the de-embedding table to determine the parameters to use for de-embedding.\n\n**Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).'
                },
                'name': 'port',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the table.'
                },
                'name': 'tableName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeScriptTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the specified Script Trigger for digital edge triggering.\n\nThe NI-RFSG device must be in the Configuration state before calling this function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_\n\n`Digital Edge Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_edge.html>`_'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the Script Trigger to configure.'
                },
                'grpc_enum': 'DigitalEdgeScriptTriggerIdentifier',
                'is_repeated_capability': True,
                'name': 'triggerId',
                'repeated_capability_type': 'script_triggers',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the source terminal for the digital edge Script Trigger. NI-RFSG sets the NIRFSG_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE attribute to this value.'
                },
                'grpc_enum': 'TriggerSource',
                'name': 'source',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the active edge for the digital edge Script Trigger. NI-RFSG sets the NIRFSG_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE attribute to this value.'
                },
                'enum': 'ScriptTriggerDigitalEdgeEdge',
                'grpc_enum': 'DigitalEdgeEdge',
                'name': 'edge',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'repeated_capability_type': 'script_triggers',
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeStartTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the Start Trigger for digital edge triggering.\n\nThe NI-RFSG device must be in the Configuration state before calling this function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_\n\n`Digital Edge Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_edge.html>`_',
            'note': 'For the PXIe-5654/5654 with PXIe-5696, the Start Trigger is valid only with a timer-based list when RF list mode is enabled.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the source terminal for the digital edge trigger. NI-RFSG sets the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE attribute to this value.'
                },
                'grpc_enum': 'TriggerSource',
                'name': 'source',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the active edge for the Start Trigger. NI-RFSG sets the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE attribute to this value.'
                },
                'enum': 'StartTriggerDigitalEdgeEdge',
                'grpc_enum': 'DigitalEdgeEdge',
                'name': 'edge',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalLevelScriptTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures a specified Script Trigger for digital level triggering.\n\nThe NI-RFSG device must be in the Configuration state before calling this function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_\n\n`Digital Level Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_level.html>`_'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the Script Trigger to configure.'
                },
                'grpc_enum': 'DigitalEdgeScriptTriggerIdentifier',
                'is_repeated_capability': True,
                'name': 'triggerId',
                'repeated_capability_type': 'script_triggers',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the trigger source terminal for the digital level Script Trigger. NI-RFSG sets the NIRFSG_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE attribute to this value.'
                },
                'name': 'source',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the active level for the digital level Script Trigger. NI-RFSG sets the NIRFSG_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL attribute to this value.'
                },
                'name': 'level',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'repeated_capability_type': 'script_triggers',
        'returns': 'ViStatus'
    },
    'ConfigureRF': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the frequency and power level of the RF output signal.\n\nThe PXI-5670/5671, PXIe-5672, and PXIe-5860 device must be in the Configuration state before calling this function. The PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXIe-5673/5673E, and PXIe-5830/5831/5832/5840/5841/5842 device can be in the Configuration or Generation state when you call this function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the frequency of the generated RF signal, in hertz. For arbitrary waveform generation, this parameter specifies the center frequency of the signal.\n\n**Units** : hertz (Hz)'
                },
                'name': 'frequency',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies either the average power level or peak power level of the generated RF signal, depending on the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute.\n\n**Units** : dBm'
                },
                'name': 'powerLevel',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureRefClock': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the NI-RFSG device Reference Clock.\n\nThe Reference Clock ensures that the NI-RFSG devices are operating from a common timebase. The NI-RFSG device must be in the Configuration state before calling this function.\n\n**Supported Devices** : PXI-5610, PXIe-5644/5645/5646, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`PXIe-5672 Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_\n\n`PXIe-5673 Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/10mhzreference_phase1.html>`_\n\n`PXIe-5673E Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/10mhzreference.html>`_\n\n`PXIe-5830 Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_\n\n`PXIe-5831 Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the source of Reference Clock signal.',
                    'table_body': [
                        [
                            '"OnboardClock"',
                            ' Uses the onboard Reference Clock as the clock source. **PXIe-5830/5831/5832** :For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. **PXIe-5831 with PXIe-5653** :Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. **PXIe-5832 with PXIe-5653** :Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. **PXIe-5841 with PXIe-5655** :Lock to the PXIe-5655 onboard clock. Connect the REF OUT connector on the PXIe-5655 to the PXIe-5841 REF IN connector. **PXIe-5842** :Lock to the PXIe-5655 onboard clock. Cables between modules are required as shown in the Getting Started Guide for the instrument.'
                        ],
                        [
                            '"RefIn"',
                            'Uses the clock signal present at the front panel REF IN connector as the clock source. **PXIe-5830/5831/5832** :For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. For the PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For the PXIe-5831, lock the external signal to the PXIe-3622 REF IN connector. For the PXIe-5832, lock the external signal to the PXIe-3623 REF IN connector. **PXIe-5831 with PXIe-5653** :Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. **PXIe-5832 with PXIe-5653** :Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector.  **PXIe-5841 with PXIe-5655** :Lock to the signal at the REF IN connector on the associated PXIe-5655. Connect the PXIe-5655 REF OUT connector to the PXIe-5841 REF IN connector. **PXIe-5842** :Lock to the signal at the REF IN connector on the associated PXIe-5655. Cables between modules are required as shown in the Getting Started Guide for the instrument.'
                        ],
                        [
                            '"PXI_CLK"',
                            'Uses the PXI_CLK signal, which is present on the PXI backplane, as the clock source.'
                        ],
                        [
                            '"ClkIn"',
                            'Uses the clock signal present at the front panel CLK IN connector as the clock source. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5841 with PXIe-5655/5842.'
                        ],
                        [
                            '"RefIn2"',
                            '\\-'
                        ],
                        [
                            '"PXI_ClkMaster"',
                            'This value is valid on only the PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653. **PXIe-5831 with PXIe-5653** :NI-RFSG configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3622 to use PXI_Clk as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. **PXIe-5832 with PXIe-5653** :NI-RFSG configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3623 to use PXI_Clk as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector.'
                        ]
                    ],
                    'table_header': [
                        'Possible Values',
                        'Description'
                    ]
                },
                'name': 'refClockSource',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the Reference Clock rate, in hertz (Hz), of the signal present at the REF IN or CLK IN connector. The default value is NIRFSG_VAL_AUTO, which allows NI-RFSG to use the default Reference Clock rate for the device or automatically detect the Reference Clock rate, if supported. This parameter is only valid when the NIRFSG_ATTR_REF_CLOCK_SOURCE parameter is set to ClkIn, RefIn or RefIn2. Refer to the NIRFSG_ATTR_REF_CLOCK_RATE attribute for possible values.'
                },
                'name': 'refClockRate',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareScriptTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the Script Trigger for software triggering.\n\nRefer to the nirfsg_SendSoftwareEdgeTrigger function for more information about using the software Script Trigger. The NI-RFSG device must be in the Configuration state before calling this function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_\n\n`Trigger Types <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_types.html>`_'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the Script Trigger to configure.'
                },
                'grpc_enum': 'DigitalEdgeScriptTriggerIdentifier',
                'is_repeated_capability': True,
                'name': 'triggerId',
                'repeated_capability_type': 'script_triggers',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'repeated_capability_type': 'script_triggers',
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareStartTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the Start Trigger for software triggering.\n\nRefer to the nirfsg_SendSoftwareEdgeTrigger function for more information about using a software trigger. The NI-RFSG device must be in the Configuration state before calling this function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_\n\n`Trigger Types <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_types.html>`_'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateDeembeddingSparameterTableArray': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nCreates an s-parameter de-embedding table for the port from the input data.\n\nIf you only create one table for a port, NI-RFSG automatically selects that table to de-embed the measurement.\n\n**Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`De-embedding Overview <https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html>`_'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'numpy_write_method',
                'method_python_name_suffix': '',
                'session_filename': 'numpy_write_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).'
                },
                'name': 'port',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced.'
                },
                'name': 'tableName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the frequencies for the NIRFSG_ATTR_SPARAMETER_TABLE rows. Frequencies must be unique and in ascending order.'
                },
                'name': 'frequencies',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'frequenciesSize'
                },
                'type': 'ViReal64[]',
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the frequency array.'
                },
                'name': 'frequenciesSize',
                'type': 'ViInt32',
                'use_array': False
            },
            {
                'array_dimensions': 3,
                'complex_array_representation': 'complex_number_array',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the S-parameters for each frequency. S-parameters for each frequency are placed in the array in the following order: s11, s12, s21, s22.'
                },
                'name': 'sparameterTable',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'sparameterTableSize'
                },
                'type': 'NIComplexNumber[]',
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the S-parameter table array.'
                },
                'name': 'sparameterTableSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': False
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of DUT ports.'
                },
                'name': 'numberOfPorts',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': False
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the orientation of the input data relative to the port on the DUT port.\n\n**Defined Values** :',
                    'table_body': [
                        [
                            'NIRFSG_VAL_PORT1_TOWARDS_DUT',
                            '24000 (0x5dc0)',
                            'Port 1 of the S2P is oriented towards the DUT port.'
                        ],
                        [
                            'NIRFSG_VAL_PORT2_TOWARDS_DUT',
                            '24001 (0x5dc1)',
                            'Port 2 of the S2P is oriented towards the DUT port.'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Value',
                        'Description'
                    ]
                },
                'enum': 'SparameterOrientation',
                'name': 'sparameterOrientation',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateDeembeddingSparameterTableS2PFile': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nCreates an S-parameter de-embedding table for the port based on the specified S2P file.\n\nIf you only create one table for a port, NI-RFSG automatically selects that table to de-embed the measurement.\n\n**Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`De-embedding Overview <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/de_embedding_overview.html>`_\n\n`S-parameters <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/s_parameters.html>`_'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842 is empty string.'
                },
                'name': 'port',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced.'
                },
                'name': 'tableName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the path to the S2P file that contains de-embedding information for the specified port.'
                },
                'name': 's2pFilePath',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': ' Specifies the orientation of the data in the S2P file relative to the port on the DUT port. **Defined Values** :',
                    'table_body': [
                        [
                            'NIRFSG_VAL_PORT1_TOWARDS_DUT',
                            '24000 (0x5dc0)',
                            'Port 1 of the S2P is oriented towards the DUT port.'
                        ],
                        [
                            'NIRFSG_VAL_PORT2_TOWARDS_DUT',
                            '24001 (0x5dc1)',
                            'Port 2 of the S2P is oriented towards the DUT port.'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Value',
                        'Description'
                    ]
                },
                'enum': 'SparameterOrientation',
                'name': 'sparameterOrientation',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'DeleteAllDeembeddingTables': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nDeletes all configured de-embedding tables for the session.\n\n**Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'DeleteDeembeddingTable': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nDeletes the selected de-embedding table for a given port.\n\n**Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).'
                },
                'name': 'port',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the table.'
                },
                'name': 'tableName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'DeleteScript': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nDeletes a specified script from the pool of currently defined scripts. The NI-RFSG device must be in the Configuration state before you call this function.\n\n**Supported Devices** :PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the script to delete. This string is case-insensitive.'
                },
                'name': 'scriptName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableScriptTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the device not to wait for the specified Script Trigger.\n\nCall this function only if you previously configured a Script Trigger and now want it disabled. The NI-RFSG device must be in the Configuration state before you call this function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the Script trigger to configure.'
                },
                'grpc_enum': 'DigitalEdgeScriptTriggerIdentifier',
                'is_repeated_capability': True,
                'name': 'triggerId',
                'repeated_capability_type': 'script_triggers',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'repeated_capability_type': 'script_triggers',
        'returns': 'ViStatus'
    },
    'DisableStartTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the device not to wait for a Start Trigger.\n\nThis function is necessary only if you previously configured a Start Trigger and now want it disabled. The NI-RFSG device must be in the Configuration state before calling this function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ErrorMessage': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConverts an error code returned by an NI-RFSG function into a user-readable string.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'is_error_handling': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ViSession handle that you obtain from nirfsg_Init or nirfsg_InitWithOptions. The handle identifies a particular instrument session.\n\nYou can pass VI_NULL for this parameter. Passing VI_NULL is useful when nirfsg_Init or nirfsg_InitWithOptions fails.\n\n**Default Value** : VI_NULL'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the status parameter that is returned from any NI-RFSG function.\n\n**Default Value** : 0 (VI_SUCCESS)'
                },
                'name': 'errorCode',
                'type': 'ViStatus',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the user-readable message string that corresponds to the status code you specify.'
                },
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'FancyCreateDeembeddingSparameterTableArray': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nCreates an s-parameter de-embedding table for the port from the input data.\n\nIf you only create one table for a port, NI-RFSG automatically selects that table to de-embed the measurement.\n\n**Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`De-embedding Overview<https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html>`_'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'create_deembedding_sparameter_table_array',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'create_deembedding_sparameter_table_array'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).'
                },
                'name': 'port',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced.'
                },
                'name': 'tableName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the frequencies for the NIRFSG_ATTR_SPARAMETER_TABLE rows. Frequencies must be unique and in ascending order.'
                },
                'name': 'frequencies',
                'numpy': True,
                'type': 'ViReal64[]',
                'type_in_documentation': 'numpy.array(dtype=numpy.float64)',
                'use_in_python_api': True
            },
            {
                'array_dimensions': 3,
                'complex_array_representation': 'complex_number_array',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the S-parameters for each frequency. S-parameters for each frequency are placed in the array in the following order: s11, s12, s21, s22.'
                },
                'name': 'sparameterTable',
                'numpy': True,
                'type': 'NIComplexNumber[]',
                'type_in_documentation': 'numpy.array(dtype=numpy.complex128)',
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the orientation of the input data relative to the port on the DUT port.\n\n**Defined Values** :',
                    'table_body': [
                        [
                            'NIRFSG_VAL_PORT1_TOWARDS_DUT',
                            '24000 (0x5dc0)',
                            'Port 1 of the S2P is oriented towards the DUT port.'
                        ],
                        [
                            'NIRFSG_VAL_PORT2_TOWARDS_DUT',
                            '24001 (0x5dc1)',
                            'Port 2 of the S2P is oriented towards the DUT port.'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Value',
                        'Description'
                    ]
                },
                'enum': 'SparameterOrientation',
                'grpc_enum': None,
                'name': 'sparameterOrientation',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'python_name': 'create_deembedding_sparameter_table_array',
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'FancyGetDeembeddingSparameters': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nReturns the S-parameters used for de-embedding a measurement on the selected port.\n\nThis includes interpolation of the parameters based on the configured carrier frequency. This function returns an empty array if no de-embedding is done.\n\nIf you want to call this function just to get the required buffer size, you can pass 0 for **S-parameter Size** and VI_NULL for the **S-parameters** buffer.\n\n**Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860',
            'note': 'The port orientation for the returned S-parameters is normalized to NIRFSG_VAL_PORT1_TOWARDS_DUT.'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'get_deembedding_sparameters',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'array_dimensions': 2,
                'complex_array_representation': 'complex_number_array',
                'direction': 'out',
                'documentation': {
                    'description': 'Returns an array of S-parameters. The S-parameters are returned in the following order: s11, s12, s21, s22.'
                },
                'name': 'sparameters',
                'numpy': True,
                'type': 'NIComplexNumber[]',
                'type_in_documentation': 'numpy.array(dtype=numpy.complex128)',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'python_name': 'get_deembedding_sparameters',
        'returns': None,
        'use_session_lock': False
    },
    'GetAllNamedWaveformNames': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReturn names of the waveforms present in the memory.\n\n**Supported Devices** :PXIe-5830/5831/5840/5841/5842E'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns a list of string having waveform names.'
                },
                'name': 'waveformNames',
                'python_api_converter_name': 'convert_comma_separated_string_to_list',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualBufferSize'
                },
                'type': 'ViChar[]',
                'type_in_documentation': 'list of str',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the number of bytes in the ViChar buffer you specify for the NIRFSG_ATTR_WAVEFORM_NAMES parameter.\n\nIf you pass 0, you can pass VI_NULL for the NIRFSG_ATTR_WAVEFORM_NAMES parameter.'
                },
                'name': 'bufferSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Fetch the number of bytes needed to pass in the NIRFSG_ATTR_BUFFER_SIZE parameter.\n\nIt can be fetch by passing VI_NULL in the NIRFSG_ATTR_WAVEFORM_NAMES parameter.'
                },
                'name': 'actualBufferSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAllScriptNames': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReturn names of the scripts present in the memory.\n\n**Supported Devices** :PXIe-5830/5831/5840/5841/5842E'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns a list of string having script names.'
                },
                'name': 'scriptNames',
                'python_api_converter_name': 'convert_comma_separated_string_to_list',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualBufferSize'
                },
                'type': 'ViChar[]',
                'type_in_documentation': 'list of str',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the number of bytes in the ViChar buffer you specify for the **waveformNames** parameter.\n\nIf you pass 0, you can pass VI_NULL for the **waveformNames** parameter.'
                },
                'name': 'bufferSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Fetch the number of bytes needed to pass in the NIRFSG_ATTR_BUFFER_SIZE parameter.\n\nIt can be fetch by passing VI_NULL in the NIRFSG_ATTR_SCRIPT_NAMES parameter.'
                },
                'name': 'actualBufferSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViBoolean attribute.\n\nUse this low-level function to get the values of inherent IVI attributes, class-defined attributes, and instrument-specific attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:\n\n- State caching is disabled for the entire session or for the particular attribute.\n- State caching is enabled, and the currently cached value is invalid.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'grpc_name': 'attribute_id',
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the current value of the attribute. Pass the address of a ViBoolean variable.'
                },
                'name': 'value',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt32': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViInt32 attribute.\n\nUse this low-level function to get the values of inherent IVI attributes, class-defined attributes, and instrument-specific attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:\n\n- State caching is disabled for the entire session or for the particular attribute.\n- State caching is enabled, and the currently cached value is invalid.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'grpc_name': 'attribute_id',
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the current value of the attribute. Pass the address of a ViInt32 variable.'
                },
                'name': 'value',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViInt64 attribute.\n\nYou can use this low-level function to get the values of inherent IVI attributes, class-defined attributes, and instrument-specific attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:\n\n- State caching is disabled for the entire session or for the particular attribute.\n- State caching is enabled, and the currently cached value is invalid.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'grpc_name': 'attribute_id',
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the current value of the attribute. Pass the address of a ViInt64 variable.'
                },
                'name': 'value',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViReal64 attribute.\n\nUse this low-level function to get the values of inherent IVI attributes, class-defined attributes, and instrument-specific attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:\n\n- State caching is disabled for the entire session or for the particular attribute.\n- State caching is enabled, and the currently cached value is invalid.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'grpc_name': 'attribute_id',
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the current value of the attribute. Pass the address of a ViReal64 variable.'
                },
                'name': 'value',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViSession': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViSession attribute.\n\nUse this low-level function to get the values of inherent IVI attributes, class-defined attributes, and instrument-specific attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:\n\n- State caching is disabled for the entire session or for the particular attribute.\n- State caching is enabled, and the currently cached value is invalid.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'grpc_name': 'attribute_id',
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the current value of the attribute. Pass the address of a ViSession variable.'
                },
                'name': 'value',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViString attribute.\n\nUse this low-level function to get the values of inherent IVI attributes, class-defined attributes, and instrument-specific attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:\n\n- State caching is disabled for the entire session or for the particular attribute.\n- State caching is enabled, and the currently cached value is invalid.\n\nYou must provide a ViString (ViChar array) to serve as a buffer for the value. Pass the number of bytes in the buffer as the Buffer Size parameter. If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the buffer size parameter, the function copies buffer size-1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.\n\nTo call this function to get only the required buffer size, pass 0 for the buffer size and VI_NULL for the attribute value buffer.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'grpc_name': 'attribute_id',
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the number of bytes in the ViChar buffer you specify for the **waveformNames** parameter.\n\nIf you pass 0, you can pass VI_NULL for the **waveformNames** parameter.'
                },
                'name': 'bufSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The buffer in which the function returns the current value of the attribute. The buffer must be of type ViChar and have at least as many bytes as indicated in the **bufferSize** parameter.\n\nIf you specify 0 for the **bufferSize** parameter, you can pass VI_NULL for this parameter.'
                },
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufSize'
                },
                'type': 'ViChar[]',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'GetDeembeddingSparameters': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns the S-parameters used for de-embedding a measurement on the selected port.\n\nThis includes interpolation of the parameters based on the configured carrier frequency. This function returns an empty array if no de-embedding is done.\n\nIf you want to call this function just to get the required buffer size, you can pass 0 for **S-parameter Size** and VI_NULL for the **S-parameters** buffer.\n\n**Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860',
            'note': 'The port orientation for the returned S-parameters is normalized to NIRFSG_VAL_PORT1_TOWARDS_DUT.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'get_deembedding_sparameter',
                'method_python_name_suffix': '',
                'session_filename': 'none'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'array_dimensions': 2,
                'complex_array_representation': 'complex_number_array',
                'direction': 'out',
                'documentation': {
                    'description': 'Returns an array of S-parameters. The S-parameters are returned in the following order: s11, s12, s21, s22.'
                },
                'name': 'sparameters',
                'numpy': True,
                'type': 'NIComplexNumber[]',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the array that is returned by the NIRFSG_ATTR_SPARAMETERS output.'
                },
                'name': 'sparametersArraySize',
                'type': 'ViInt32',
                'use_array': False
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the number of S-parameters.'
                },
                'name': 'numberOfSparameters',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the number of S-parameter ports. The **sparameter** array is always *n* x *n*, where span *n* is the number of ports.'
                },
                'name': 'numberOfPorts',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'GetDeembeddingTableNumberOfPorts': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns the number of S-parameter ports.'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the number of S-parameter ports. The **sparameter** array is always *n* x *n*, where span *n* is the number of ports.'
                },
                'name': 'numberOfPorts',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetError': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nRetrieves and then clears the IVI error information for the session or the current execution thread.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5840/5841/5842/5860',
            'note': 'If the **bufferSize** parameter is 0, this function does not clear the error information. By passing 0 to the **bufferSize** parameter, you can determine the buffer size required to obtain the entire NIRFSG_ATTR_ERROR_DESCRIPTION string. You can then call this function again with a sufficiently large buffer. If you specify a valid IVI session for the NIRFSG_ATTR_VI parameter, this function retrieves and clears the error information for the session. If you pass VI_NULL for the NIRFSG_ATTR_VI parameter, this function retrieves and clears the error information for the current execution thread. If the NIRFSG_ATTR_VI parameter is an invalid session, this function does nothing and returns an error. Normally, the error information describes the first error that occurred since the user last called this function or the niRFSG_ClearError function.'
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the error code for the session or execution thread. If you pass 0 for the **BufferSize** parameter, you can pass VI_NULL for this parameter.'
                },
                'name': 'errorCode',
                'type': 'ViStatus',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'default_value': '256',
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the number of bytes in the ViChar array you specify for the **description** parameter.\n\nIf the NIRFSG_ATTR_ERROR_DESCRIPTION, including the terminating NULL byte, contains more bytes than you indicate in this parameter, the function copies **bufferSize** - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. Forexample, if the value is 123456 and the buffer size is 4, the function places 123 into the buffer and returns 7. If you pass 0, you can pass VI_NULL for the **description** parameter.\n\n**Default Value** : None'
                },
                'name': 'errorDescriptionBufferSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the NIRFSG_ATTR_ERROR_DESCRIPTION for the IVI session or execution thread.\n\nIf there is no description, the function returns an empty string. The buffer must contain at least as many elements as the value you specify with the **bufferSize** parameter. If the NIRFSG_ATTR_ERROR_DESCRIPTION, including the terminating NULL byte, contains more bytes than you indicate with the **bufferSize** parameter, the function copies **bufferSize** - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is 123456 and the buffer size is 4, the function places 123 into the buffer and returns 7. If you pass 0, you can pass VI_NULL for this parameter.'
                },
                'name': 'errorDescription',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'errorDescriptionBufferSize'
                },
                'type': 'ViChar[]',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'GetExternalCalibrationLastDateAndTime': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns the date and time of the last successful external calibration.\n\nThe time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30PM, this function returns\n\n14 for the hours parameter and\n\n30 for the minutes parameter.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'get_ext_cal_last_date_and_time',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the year of the last successful calibration.'
                },
                'name': 'year',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the month of the last successful calibration.'
                },
                'name': 'month',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the day of the last successful calibration.'
                },
                'name': 'day',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the hour of the last successful calibration.'
                },
                'name': 'hour',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the minute of the last successful calibration.'
                },
                'name': 'minute',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the second of the last successful calibration.'
                },
                'name': 'second',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'GetLastExtCalLastDateAndTime': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nReturns the date and time of the last successful external calibration.\n\nThe time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30PM, this function returns\n\n14 for the hours parameter and\n\n30 for the minutes parameter.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
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
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'lastCalDatetime',
                'type': 'hightime.datetime'
            }
        ],
        'python_name': 'get_ext_cal_last_date_and_time',
        'real_datetime_call': 'GetExternalCalibrationLastDateAndTime',
        'returns': 'ViStatus'
    },
    'GetLastSelfCalLastDateAndTime': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nReturns the date and time of the last successful self-calibration.\n\nThe time returned is 24-hour local time. For example, if the device was calibrated at 2:30PM, this function returns\n\n14 for the hours parameter and\n\n30 for the minutes parameter.\n\n**Supported Devices** : PXI-5610, PXIe-5644/5645/5646, PXIe-5653, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
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
                'default_value': 'Module.PRIMARY_MODULE',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies from which stand-alone module to retrieve the last successful self-calibration date and time.'
                },
                'enum': 'Module',
                'grpc_enum': None,
                'name': 'module',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'lastCalDatetime',
                'type': 'hightime.datetime'
            }
        ],
        'python_name': 'get_self_cal_last_date_and_time',
        'real_datetime_call': 'GetSelfCalibrationDateAndTime',
        'returns': 'ViStatus'
    },
    'GetMaxSettablePower': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReturns the maximum settable output power level for the current configuration.\n\n**Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns maximum settable power level in dBm.'
                },
                'name': 'value',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'GetScript': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReturns the content of specified script.\n\n**Supported Devices** :PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the script. This string is case-insensitive.'
                },
                'name': 'scriptName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the script.'
                },
                'name': 'script',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualBufferSize'
                },
                'type': 'ViChar[]',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the number of bytes in the ViChar buffer you specify for the **waveformNames** parameter.\n\nIf you pass 0, you can pass VI_NULL for the **waveformNames** parameter.'
                },
                'name': 'bufferSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Fetch the number of bytes needed to pass in the NIRFSG_ATTR_BUFFER_SIZE parameter.\n\nIt can be fetch by passing VI_NULL in the NIRFSG_ATTR_SCRIPT_NAMES parameter.'
                },
                'name': 'actualBufferSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSelfCalibrationDateAndTime': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns the date and time of the last successful self-calibration.\n\nThe time returned is 24-hour local time. For example, if the device was calibrated at 2:30PM, this function returns\n\n14 for the hours parameter and\n\n30 for the minutes parameter.\n\n**Supported Devices** : PXI-5610, PXIe-5644/5645/5646, PXIe-5653, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'get_self_calibration_date_and_time',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies from which stand-alone module to retrieve the last successful self-calibration date and time.'
                },
                'enum': 'Module',
                'grpc_enum': None,
                'name': 'module',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the year of the last successful calibration.'
                },
                'name': 'year',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the month of the last successful calibration.'
                },
                'name': 'month',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the day of the last successful calibration.'
                },
                'name': 'day',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the hour of the last successful calibration.'
                },
                'name': 'hour',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the minute of the last successful calibration.'
                },
                'name': 'minute',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the second of the last successful calibration.'
                },
                'name': 'second',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSelfCalibrationTemperature': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReturns the temperature, in degrees Celsius, of the device at the last successful self-calibration.\n\n**Supported Devices** : PXI-5610, PXIe-5653, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831 (IF only)/5832 (IF only)/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'default_value': 'Module.PRIMARY_MODULE',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies from which stand-alone module to retrieve the last successful self-calibration temperature. \n                    **Default Value** : NIRFSG_VAL_PRIMARY_MODULE\n                    **Defined Values** :\n                    ',
                    'table_body': [
                        [
                            'NIRFSG_VAL_PRIMARY_MODULE',
                            '13000 (0x32c8)',
                            'The stand-alone device or the main module in a multi-module device.'
                        ],
                        [
                            'NIRFSG_VAL_AWG',
                            '13001 (0x32c9)',
                            'The AWG associated with the primary module.'
                        ],
                        [
                            'NIRFSG_VAL_LO',
                            '13002 (0x32ca)',
                            'The LO associated with the primary module.'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Value',
                        'Description'
                    ]
                },
                'enum': 'Module',
                'name': 'module',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the temperature, in degrees Celsius, of the device at the last successful self-calibration.'
                },
                'name': 'temperature',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'GetTerminalName': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReturns the fully-qualified name of the specified signal.\n\nThe fully-qualified name is helpful to automatically route signals in a multisegment chassis.\n\n**Supported Devices** : PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_\n\n`Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_\n\n`Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the signal to query. **Defined Values** :\n                    ',
                    'table_body': [
                        [
                            'NIRFSG_VAL_START_TRIGGER',
                            '0 (0x0)',
                            'Exports a Start Trigger.'
                        ],
                        [
                            'NIRFSG_VAL_SCRIPT_TRIGGER',
                            '1 (0x1)',
                            'Exports a Script Trigger.'
                        ],
                        [
                            'NIRFSG_VAL_MARKER_EVENT',
                            '2 (0x2)',
                            'Exports a Marker Event.'
                        ],
                        [
                            'NIRFSG_VAL_REF_CLOCK',
                            '3 (0x3)',
                            'Exports the Reference Clock.'
                        ],
                        [
                            'NIRFSG_VAL_STARTED_EVENT',
                            '4 (0x4)',
                            'Exports a Started Event.'
                        ],
                        [
                            'NIRFSG_VAL_DONE_EVENT',
                            '5 (0x5)',
                            'Exports a Done Event.'
                        ],
                        [
                            'NIRFSG_VAL_CONFIGURATION_LIST_STEP_TRIGGER',
                            '6 (0x6)',
                            'Exports a Configuration List Step Trigger.'
                        ],
                        [
                            'NIRFSG_VAL_CONFIGURATION_SETTLED_EVENT',
                            '7 (0x7)',
                            'Exports a Configuration Settled Event.'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Value',
                        'Description'
                    ]
                },
                'enum': 'Signal',
                'name': 'signal',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies which instance of the selected signal to query. This parameter is necessary when you set the NIRFSG_ATTR_SIGNAL parameter to NIRFSG_VAL_SCRIPT_TRIGGER or NIRFSG_VAL_MARKER_EVENT  . Otherwise, set the NIRFSG_ATTR_SIGNAL_IDENTIFIER parameter to "" (empty string). **Possible Values** :\n                    ',
                    'table_body': [
                        [
                            '"marker0"',
                            'Specifies Marker 0.'
                        ],
                        [
                            '"marker1"',
                            'Specifies Marker 1.'
                        ],
                        [
                            '"marker2"',
                            'Specifies Marker 2.'
                        ],
                        [
                            '"marker3"',
                            'Specifies Marker 3.'
                        ],
                        [
                            '"scriptTrigger0"',
                            'Specifies Script Trigger 0.'
                        ],
                        [
                            '"scriptTrigger1"',
                            'Specifies Script Trigger 1.'
                        ],
                        [
                            '"scriptTrigger2"',
                            'Specifies Script Trigger 2.'
                        ],
                        [
                            '"scriptTrigger3"',
                            'Specifies Script Trigger 3.'
                        ]
                    ],
                    'table_header': [
                        'Possible Value',
                        'Description'
                    ]
                },
                'grpc_enum': 'SignalIdentifier',
                'name': 'signalIdentifier',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the number of bytes in the ViChar buffer you specify for the **NIRFSG_ATTR_TERMINAL_NAME** parameter.\n\nIf you pass 0, you can pass VI_NULL for the **NIRFSG_ATTR_TERMINAL_NAME** parameter.'
                },
                'name': 'bufferSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the string to use as the source for other devices.'
                },
                'name': 'terminalName',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'GetWaveformBurstStartLocations': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReturns the burst start locations of the waveform stored in the NI-RFSG session.\n\n**Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name. Example: "waveform::waveform0/marker0"'
                },
                'is_repeated_capability': True,
                'name': 'channelName',
                'repeated_capability_type': 'waveforms',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the burst start locations array.'
                },
                'name': 'numberOfLocations',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the burst start locations stored in the NI-RFSG session for the waveform that you specified in the NIRFSG_ATTR_CHANNEL_NAME parameter. This value is expressed in samples.'
                },
                'name': 'locations',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'numberOfLocations',
                    'value_twist': 'requiredSize'
                },
                'type': 'ViReal64[]',
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the required size for the output array if you pass NULL to NIRFSG_ATTR_LOCATIONS parameter.'
                },
                'name': 'requiredSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'repeated_capability_type': 'waveforms',
        'returns': 'ViStatus'
    },
    'GetWaveformBurstStopLocations': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReturns the burst stop locations of the waveform stored in the NI-RFSG session.\n\n**Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name. Example: "waveform::waveform0/marker0"'
                },
                'is_repeated_capability': True,
                'name': 'channelName',
                'repeated_capability_type': 'waveforms',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the burst start locations array.'
                },
                'name': 'numberOfLocations',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the burst start locations stored in the NI-RFSG session for the waveform that you specified in the NIRFSG_ATTR_CHANNEL_NAME parameter. This value is expressed in samples.'
                },
                'name': 'locations',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'numberOfLocations',
                    'value_twist': 'requiredSize'
                },
                'type': 'ViReal64[]',
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the required size for the output array if you pass NULL to NIRFSG_ATTR_LOCATIONS parameter.'
                },
                'name': 'requiredSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'repeated_capability_type': 'waveforms',
        'returns': 'ViStatus'
    },
    'GetWaveformMarkerEventLocations': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReturns the marker locations associated with the waveform and the marker stored in the NI-RFSG session.\n\n**Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
                },
                'is_repeated_capability': True,
                'name': 'channelName',
                'repeated_capability_type': 'markers',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the locations array.'
                },
                'name': 'numberOfLocations',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the marker locations stored in the NI-RFSG database for the channel you specified in the NIRFSG_ATTR_CHANNEL_NAME parameter. This value is expressed in samples.'
                },
                'name': 'locations',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'numberOfLocations',
                    'value_twist': 'requiredSize'
                },
                'type': 'ViReal64[]',
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the required size for the output array if you pass NULL to **Locations** parameter.'
                },
                'name': 'requiredSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'repeated_capability_type': 'markers',
        'returns': 'ViStatus'
    },
    'InitWithOptions': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nOpens a session to the device you specify as the NIRFSG_ATTR_RESOURCE_NAME and returns a ViSession handle that you use to identify the NI-RFSG device in all subsequent NI-RFSG function calls.\n\nThis function also configures the device through the NIRFSG_ATTR_OPTION_STRING input.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Simulating an NI RF Signal Generator <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/simulate.html>`_',
            'note': 'For multichannel devices such as the PXIe-5860, the resource name must include the channel number to use. The channel number is specified by appending /*ChannelNumber* to the device name, where *ChannelNumber* is the channel number (0, 1, etc.). For example, if the device name is PXI1Slot2 and you want to use channel 0, use the resource name PXI1Slot2/0.'
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
                    'description': 'Specifies the resource name of the device to initialize.\n\nFor NI-DAQmx devices, the syntax is the device name specified in MAX. Typical default names for NI-DAQmx devices in MAX are Dev2 or PXISlot2. You can rename an NI-DAQmx device in MAX.\n\nYou can also specify the name of an IVI logical name configured with the IVI Configuration utility. Refer to the *IVI* topic of the *Measurement & Automation Explorer Help* for more information.',
                    'note': 'NI-RFSG device names are not case-sensitive. However, all IVI names, such as logical names, are case-sensitive. If you use an IVI logical name, make sure the name is identical to the name shown in the IVI Configuration Utility.'
                },
                'name': 'resourceName',
                'type': 'ViRsrc',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies whether you want NI-RFSG to perform an ID query.\n\n**Defined Values** :',
                    'table_body': [
                        [
                            'VI_TRUE (1)',
                            'Perform ID query.'
                        ],
                        [
                            'VI_FALSE (0)',
                            'Do not perform ID query.'
                        ]
                    ],
                    'table_header': [
                        'Value',
                        'Description'
                    ]
                },
                'name': 'idQuery',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies whether you want to reset the NI-RFSG device during the initialization procedure.\n\n**Defined Values** :',
                    'table_body': [
                        [
                            'VI_TRUE (1)',
                            'Reset device.'
                        ],
                        [
                            'VI_FALSE (0)',
                            'Do not reset device.'
                        ]
                    ],
                    'table_header': [
                        'Value',
                        'Description'
                    ]
                },
                'name': 'resetDevice',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'default_value': '""',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the initial value of certain attributes for the session. The following table lists the attributes and the name you pass in this parameter to identify the attribute.\n\nThe format of this string consists of the following relations:\n"AttributeName=Value"\n\nwhere\n*AttributeName* is the name of the attribute and *Value* is the value to which the attribute is set. To set multiple attributes, separate their assignments with a comma, as shown in the following option string:\n\n"RangeCheck=1,QueryInstrStatus=0,Cache=1,DriverSetup=AWG:pxi1slot4"\n\nThe `DriverSetup string <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/driver_setup_string.html>`_ is required in order to simulate a specific device.'
                },
                'name': 'optionString',
                'python_api_converter_name': 'convert_init_with_options_dictionary',
                'type': 'ViConstString',
                'type_in_documentation': 'dict'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns a ViSession handle that you use to identify the NI-RFSG device in all subsequent NI-RFSG function calls.'
                },
                'grpc_name': 'vi',
                'name': 'newVi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'Initiate': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nInitiates signal generation, causing the NI-RFSG device to leave the Configuration state and enter the Generation state.\n\nIf the settings have not been committed to the device before you call this function, they are committed by this function. The operation returns when the RF output signal settles. To return to the Configuration state, call the nirfsg_Abort function.\n\n**Supported Devices** : PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'LoadConfigurationsFromFile': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nLoads the configurations from the specified file to the NI-RFSG driver session.\n\nThe VI does an implicit reset before loading the configurations from the file.\n\n**Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the absolute path of the file from which the NI-RFSG loads the configurations.'
                },
                'name': 'filePath',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'LockSession': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nObtains a multithread lock on the instrument session.\n\nBefore doing so, this function waits until all other execution threads have released their locks on the instrument session.\n\nOther threads might have obtained a lock on this session in the following ways:\n\n- Your application already called the nirfsg_LockSession function.\n- A call to NI-RFSG locked the session.\n\nAfter the call to this function returns successfully, no other threads can access the instrument session until you call the nirfsg_UnlockSession function. Use the nirfsg_LockSession function and the nirfsg_UnlockSession function around a sequence of calls to NI-RFSG functions if you require that the NI-RFSG device retain its settings through the end of the sequence.\n\nYou can safely make nested calls to the nirfsg_LockSession function within the same thread. To completely unlock the session, balance each call to the nirfsg_LockSession function with a call to the nirfsg_UnlockSession function. If, however, you use the NIRFSG_ATTR_CALLER_HAS_LOCK parameter in all calls to the nirfsg_LockSession function and the nirfsg_UnlockSession function within a function, the IVI Library locks the session only once within the function regardless of the number of calls you make to the nirfsg_LockSession function. Locking the session only once allows you to call nirfsg_UnlockSession just once at the end of the function.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5840/5841/5842/5860'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Keeps track of whether you obtain a lock and therefore need to unlock the session. Pass the address of a local ViBoolean variable. In the declaration of the local variable, initialize it to VI_FALSE. Pass the address of the same local variable to any other calls you make to the nirfsg_LockSession function or the nirfsg_UnlockSession function in the same function.\n\nThis parameter serves as a convenience. If you do not want to use this parameter, pass VI_NULL.\n\nThe parameter is an input/output parameter. The nirfsg_LockSession function and the nirfsg_UnlockSession each inspect the current value and take the following actions:\n\n- If the value is VI_TRUE, the nirfsg_LockSession function does not lock the session again. If the value is VI_FALSE, the nirfsg_LockSession function obtains the lock and sets the value of the parameter to VI_TRUE.\n- If the value is VI_FALSE, the nirfsg_UnlockSession function does not attempt to unlock the session. If the value is VI_TRUE, the nirfsg_UnlockSession function releases the lock and sets the value of the parameter to VI_FALSE.\n\nThus, you can call the nirfsg_UnlockSession function at the end of your function without worrying about whether you have the lock.\n\nExample:\n\nViStatus TestFunc (ViSession vi, ViInt32 flags)\n{\nViStatus error = VI_SUCCESS;\nViBoolean haveLock = VI_FALSE;\n\nif (flags & BIT_1)\n{\nviCheckErr( nirfsg_LockSession(vi, &haveLock));\nviCheckErr( TakeAction1(vi));\nif (flags & BIT_2)\n{\nviCheckErr( nirfsg_UnlockSession(vi, &haveLock));\nviCheckErr( TakeAction2(vi));\nviCheckErr( nirfsg_LockSession(vi, &haveLock));\n}\nif (flags & BIT_3)\nviCheckErr( TakeAction3(vi));\n}\n\nError:\n\nAt this point, you cannot really be sure that you have the lock.\nFortunately, the haveLock variable takes care of that for you.\n\nnirfsg_UnlockSession(vi, &haveLock);\nreturn error;\n}'
                },
                'name': 'callerHasLock',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'python_name': 'lock',
        'render_in_session_base': True,
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'PerformPowerSearch': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nPerforms a power search if the NIRFSG_ATTR_ALC_CONTROL attribute is disabled.\n\nCalling this function disables modulation for a short time while the device levels the output signal.\n\n**Supported Devices** : PXIe-5654 with PXIe-5696\n\n**Related Topics**\n\n`Power Search <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_power_search.html>`_',
            'note': 'Power search temporarily enables the ALC, so ensure the appropriate included cable is connected between the PXIe-5654 ALCIN connector and the PXIe-5696 ALCOUT connector to successfully perform a power search.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'PerformThermalCorrection': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nCorrects for any signal drift due to environmental temperature variation when generating the same signal for extended periods of time without a parameter change.\n\nUnder normal circumstances of short-term signal generation, NI-RFSG performs thermal correction automatically by ensuring stable power levels, and you do not need to call this function.\n\nUse this function when generating the same signal for an extended period of time in a temperature-fluctuating environment. The NI-RFSG device must be in the Generation state before calling this function.\n\n**Supported Devices** : PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Thermal Management <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/thermal_management.html>`_\n\n`Impairment Calibration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/vector_calibration.html>`_'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'QueryArbWaveformCapabilities': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nQueries and returns the waveform capabilities of the NI-RFSG device.\n\nThese capabilities are related to the current device configuration. The NI-RFSG device must be in the Configuration or the Generation state before calling this function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the value of the NIRFSG_ATTR_ARB_MAX_NUMBER_WAVEFORMS attribute. This value is the maximum number of waveforms you can write.'
                },
                'name': 'maxNumberWaveforms',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the value of the NIRFSG_ATTR_ARB_WAVEFORM_QUANTUM attribute. If the waveform quantum is *q*, then the size of the waveform that you write should be a multiple of *q*. The units are expressed in samples.'
                },
                'name': 'waveformQuantum',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the value of the NIRFSG_ATTR_ARB_WAVEFORM_SIZE_MIN attribute. The number of samples of the waveform that you write must be greater than or equal to this value.'
                },
                'name': 'minWaveformSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the value of the NIRFSG_ATTR_ARB_WAVEFORM_SIZE_MAX attribute. The number of samples of the waveform that you write must be less than or equal to this value.'
                },
                'name': 'maxWaveformSize',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadAndDownloadWaveformFromFileTDMS': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReads the waveforms from a TDMS file and downloads one waveform into each of the NI RF vector signal generators.\n\nThis function reads the following information from the TDMS file and writes it into the NI-RFSG session:\n\n- Sample Rate\n- PAPR\n- Runtime Scaling\n- RF Blanking Marker Locations\n- RF Blanking Enabled\n- Burst Start Locations\n- Burst Stop Locations\n- RF Blanking Marker Source\n- Signal Bandwidth\n- Waveform Size\n\nIf RF blanking marker locations are present in the file but burst locations are not present, burst locations are calculated from RF blanking marker locations and stored in the NI-RFSG session.\n\n**Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name used to store the waveform. This string is case-insensitive.\n\nExample:\n\n"waveform::waveform0"'
                },
                'name': 'waveformName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the absolute path to the TDMS file from which the NI-RFSG reads the waveforms.'
                },
                'name': 'filePath',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the index of the waveform to be read from the TDMS file.'
                },
                'name': 'waveformIndex',
                'type': 'ViUInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetDevice': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nPerforms a hard reset on the device which consists of the following actions:\n\n- Signal generation is stopped.\n- All routes are released.\n- External bidirectional terminals are tristated.\n- FPGAs are reset.\n- Hardware is configured to its default state.\n- All session attributes are reset to their default states.\n\nDuring a device reset, routes of signals between this and other devices are released, regardless of which device created the route.\n\n- PXI-5610, PXI-5670/5671, PXIe-5672-- After calling this function, the device requires 25 seconds before returning to full functionality. NI-RFSG enforces this condition by adding a wait, if needed, the next time you try to access the device.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E\n\n**Related Topics**\n\n`Thermal Shutdown <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/thermal_shutdown_monitoring_5650_5651_5652.html>`_',
            'note': 'You must call the nirfsg_ResetDevice function if the NI-RFSG device has shut down because of a high-temperature condition.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetWithDefaults': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nPerforms a software reset of the device, returning it to the default state and applying any initial default settings from the IVI Configuration Store.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696,PXI-5670/5671, PXIe-5672/5673/5673E'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetWithOptions': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nResets all properties to default values and specifies steps to omit during the reset process, such as signal routes.\n\nBy default, this function exhibits the same behavior as nirfsg_Reset. You can specify steps to omit using the steps to omit parameter. For example, if you specify NIRFSG_VAL_RESET_WITH_OPTIONS_ROUTES for the NIRFSG_ATTR_STEPS_TO_OMIT parameter, this function does not release signal routes during the reset process.\n\nWhen routes of signals between two devices are released, they are released regardless of which device created the route.\n\nTo avoid resetting routes on PXIe-5820/5830/5831/5832/5840/5841/5842/5860 that are in use by NI-RFSA sessions, NI recommends using this function instead of nirfsg_Reset, with NIRFSG_ATTR_STEPS_TO_OMIT set to NIRFSG_VAL_RESET_WITH_OPTIONS_ROUTES.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_\n\n`Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies a list of steps to skip during the reset process. The default value is NIRFSG_VAL_RESET_WITH_OPTIONS_NONE, which specifies that no step is omitted during reset. **Defined Values** :',
                    'note': 'NIRFSG_VAL_RESET_WITH_OPTIONS_ROUTES is not supported in external calibration or alignment sessions.\nYou can combine multiple enums.ResetWithOptionsStepsToOmit flags using the bitwise OR (|) operator.',
                    'table_body': [
                        [
                            'NIRFSG_VAL_RESET_WITH_OPTIONS_NONE',
                            '0 (0x0)',
                            'No step is omitted during reset.'
                        ],
                        [
                            'NIRFSG_VAL_RESET_WITH_OPTIONS_WAVEFORMS',
                            '1 (0x1)',
                            'Omits clearing waveforms.'
                        ],
                        [
                            'NIRFSG_VAL_RESET_WITH_OPTIONS_SCRIPTS',
                            '2 (0x2)',
                            'Omits clearing scripts.'
                        ],
                        [
                            'NIRFSG_VAL_RESET_WITH_OPTIONS_ROUTES',
                            '4 (0x4)',
                            'Omits the routing reset step. Routing is preserved after a reset. However, routing related properties are reset to default, and routing is released if the default properties are committed after a reset.'
                        ],
                        [
                            'NIRFSG_VAL_RESET_WITH_OPTIONS_DEEMBEDDING_TABLES',
                            '8 (0x8)',
                            'Omits deleting de-embedding tables. This step is valid only for the PXIe-5830/5831/5832/5840.'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Value',
                        'Description'
                    ]
                },
                'enum': 'ResetWithOptionsStepsToOmit',
                'name': 'stepsToOmit',
                'type': 'ViUInt64',
                'type_in_documentation': 'Bitwise combination of enums.ResetWithOptionsStepsToOmit flags',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'SaveConfigurationsToFile': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSaves the configurations of the session to the specified file.\n\n**Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the channel.'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the absolute path of the file to which the NI-RFSG saves the configurations.'
                },
                'name': 'filePath',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'SelectArbWaveform': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSpecifies the waveform that is generated upon a call to the nirfsg_Initiate function when the generation_mode property is set to NIRFSG_VAL_ARB_WAVEFORM.\n\nYou must specify a waveform using the NIRFSG_ATTR_NAME parameter if you have written multiple waveforms. The NI-RFSG device must be in the Configuration state before you call this function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Assigning Properties or Attributes to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the stored waveform to generate. This is a case-insensitive alphanumeric string that does not use reserved words. NI-RFSG sets the NIRFSG_ATTR_ARB_SELECTED_WAVEFORM attribute to this value.'
                },
                'grpc_name': 'name',
                'name': 'name',
                'python_name': 'waveform_name',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'SelfCal': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nPerforms an internal self-calibration on the device and associated modules that support self-calibration.\n\nIf the calibration is successful, new calibration data and constants are stored in the onboard nonvolatile memory of the module.\n\nThe PXIe-5841 maintains separate self-calibration data for both the PXIe-5841 standalone and when associated with the PXIe-5655. Use this function once for each intended configuration.\n\n**Supported Devices** : PXI-5610, PXIe-5653, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
            'note': 'If there is an existing NI-RFSA session open for the same PXIe-5820/5830/5831/5832/5840/5841/5842/5860 while this function runs, it may remain open but cannot be used for operations that access the hardware, for example niRFSA_Commit or niRFSA_Initiate. For the existing open session to use the new self-calibration data, the session will need to be closed and reopened.\n\n**PXIe-5860**\n\nWhile this VI is running on one channel, if there are any existing NI-RFSG or NI-RFSA sessions open on the other channel, they may remain open but cannot be used for operations that access the hardware, for example niRFSG Commit or niRFSG Initiate or niRFSA Commit or niRFSA Initiate. For the existing open session to use the new self-calibration data, the session will need to be closed and reopened.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'SelfCalibrateRange': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSelf-calibrates all configurations within the specified frequency and peak power level limits.\n\nSelf-calibration range data is valid until you restart the system or call the nirfsg_ClearSelfCalibrateRange function.\n\nNI recommends that no external signals are present on the RF In or IQ In ports during the calibration.\n\nFor best results, NI recommends that you perform self-calibration without omitting any steps. However, if certain aspects of performance are less important for your application, you can omit certain steps for faster calibration.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842',
            'note': '- This function does not update self-calibration date and temperature.\n\n - If there is an existing NI-RFSA session open for the same PXIe-5644/5645/5646, it may remain open but cannot be used while this function runs.\n\n - If there is an existing NI-RFSA session open for the same PXIe-5820/5830/5831/5832/5840/5841/5842 while this function runs, it may remain open but cannot be used for operations that access the hardware, for example niRFSA_Commit or niRFSA_Initiate.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies which calibration steps to skip during the self-calibration process. The default value is an empty array, which indicates that no calibration steps are omitted.\n\n**Default Value** : NIRFSG_VAL_SELF_CAL_OMIT_NONE\n\n**Defined Values:**',
                    'note': 'You can combine multiple enums.SelfCalibrateRangeStepsToOmit flags using the bitwise OR (|) operator.',
                    'table_body': [
                        [
                            'NIRFSG_VAL_SELF_CAL_OMIT_NONE',
                            '0 (0x0)',
                            'No calibration steps are omitted.'
                        ],
                        [
                            'NIRFSG_VAL_SELF_CAL_LO_SELF_CAL',
                            '1 (0x1)',
                            'Omits the LO Self Cal step. If you omit this step, the power level of the LO is not adjusted.'
                        ],
                        [
                            'NIRFSG_VAL_SELF_CAL_POWER_LEVEL_ACCURACY',
                            '2 (0x2)',
                            'Omits the Power Level Accuracy step. If you omit this step, the power level accuracy of the device is not adjusted.'
                        ],
                        [
                            'NIRFSG_VAL_SELF_CAL_RESIDUAL_LO_POWER',
                            '4 (0x4)',
                            'Omits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted.'
                        ],
                        [
                            'NIRFSG_VAL_SELF_CAL_IMAGE_SUPPRESSION',
                            '8 (0x8)',
                            'Omits the Image Suppression step. If you omit this step, the Residual Sideband Image performance is not adjusted.'
                        ],
                        [
                            'NIRFSG_VAL_SELF_CAL_SYNTHESIZER_ALIGNMENT',
                            '16 (0x10)',
                            'Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Value',
                        'Description'
                    ]
                },
                'enum': 'SelfCalibrateRangeStepsToOmit',
                'name': 'stepsToOmit',
                'type': 'ViInt64',
                'type_in_documentation': 'Bitwise combination of enums.SelfCalibrateRangeStepsToOmit flags',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the minimum frequency to calibrate.'
                },
                'name': 'minFrequency',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the maximum frequency to calibrate.'
                },
                'name': 'maxFrequency',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the minimum power level to calibrate.'
                },
                'name': 'minPowerLevel',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the maximum power level to calibrate.'
                },
                'name': 'maxPowerLevel',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'SendSoftwareEdgeTrigger': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nForces a trigger to occur.\n\nThe specified trigger generates regardless of whether the trigger has been configured as a software trigger.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the trigger to send.\n\n**Default Value:** NIRFSG_VAL_START_TRIGGER\n\n**Defined Values:**',
                    'table_body': [
                        [
                            'NIRFSG_VAL_START_TRIGGER',
                            '0 (0x0)',
                            'Specifies the Start Trigger.'
                        ],
                        [
                            'NIRFSG_VAL_SCRIPT_TRIGGER',
                            '1 (0x1)',
                            'Specifies the Script Trigger.'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Value',
                        'Description'
                    ]
                },
                'enum': 'SoftwareTriggerType',
                'name': 'trigger',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the Script Trigger to configure. This parameter is valid only when you set the NIRFSG_ATTR_TRIGGER parameter to NIRFSG_VAL_START_TRIGGER. Otherwise, set the NIRFSG_ATTR_TRIGGER_IDENTIFIER parameter to "" (empty string).\n\n**Default Value:** "" (empty string)\n\n**Possible Values:**',
                    'table_body': [
                        [
                            'scriptTrigger0',
                            'Specifies Script Trigger 0.'
                        ],
                        [
                            'scriptTrigger1',
                            'Specifies Script Trigger 1.'
                        ],
                        [
                            'scriptTrigger2',
                            'Specifies Script Trigger 2.'
                        ],
                        [
                            'scriptTrigger3',
                            'Specifies Script Trigger 3.'
                        ],
                        [
                            '',
                            'None (no signal to export)'
                        ]
                    ],
                    'table_header': [
                        'Possible Value',
                        'Description'
                    ]
                },
                'enum': 'TriggerIdentifier',
                'name': 'triggerIdentifier',
                'grpc_enum': 'SignalIdentifier',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'render_in_session_base': True,
        'returns': 'ViStatus'
    },
    'SetArbWaveformNextWritePosition': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the start position to use for writing a waveform before calling the nirfsg_WriteArbWaveform function.\n\nThis function allows you to write to arbitrary locations within the waveform. These settings apply only to the next write to the waveform specified by the **name** input of the nirfsg_AllocateArbWaveform function or the nirfsg_WriteArbWaveform function. Subsequent writes to that waveform begin where the last write ended, unless this function is called again.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
            'note': 'If you use this function to write the waveform that is currently generating, an undefined output may result.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the waveform. This string is case-insensitive and alphanumeric, and it cannot use `reserved words <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_instructions.html>`_.'
                },
                'name': 'waveformName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the reference position in the waveform. The position and NIRFSG_ATTR_OFFSET together determine where to start loading data into the waveform.\n\n**Defined Values:**',
                    'table_body': [
                        [
                            'NIRFSG_VAL_START_OF_WAVEFORM',
                            '8000 (0x1f40)',
                            'The reference position is relative to the start of the waveform.'
                        ],
                        [
                            'NIRFSG_VAL_CURRENT_POSITION',
                            '8001 (0x1f41)',
                            'The reference position is relative to the current position.'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Value',
                        'Description'
                    ]
                },
                'enum': 'RelativeTo',
                'name': 'relativeTo',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the offset from the **relative to** parameter at which to start loading the data into the waveform.'
                },
                'name': 'offset',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of a ViBoolean attribute.\n\nUse this low-level function to set the values of inherent IVI attributes, class-defined attributes, and instrument-specific attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:\n\n- State caching is disabled for the entire session or for the particular attribute.\n- State caching is enabled, and the currently cached value is invalid or is different than the value you specify.\n\nNI-RFSG contains high-level functions that set most of the instrument attributes. Use the high-level driver functions as much as possible, as they handle order dependencies and multithread locking. The high-level functions also perform status checking only after setting all of the attributes. In contrast, when you set multiple attributes using the SetAttribute functions, the functions check the instrument status after each call.\n\nAlso, when state caching is enabled, the high-level functions that configure multiple attributes perform instrument I/O only for the attributes whose value you change. Thus, you can safely call the high-level functions without the penalty of redundant instrument I/O.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'grpc_name': 'attribute_id',
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value to which you want to set the attribute.',
                    'note': 'Some values may not be valid. The allowed values depend on the current settings of the instrument session.'
                },
                'name': 'value',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt32': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of a ViInt32 attribute.\n\nUse this low-level function to set the values of inherent IVI attributes, class-defined attributes, and instrument-specific attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:\n\n- State caching is disabled for the entire session or for the particular attribute.\n- State caching is enabled, and the currently cached value is invalid or is different than the value you specify.\n\nNI-RFSG contains high-level functions that set most of the instrument attributes. Use the high-level driver functions as much as possible, as they handle order dependencies and multithread locking. The high-level functions also perform status checking only after setting all of the attributes. In contrast, when you set multiple attributes using the SetAttribute functions, the functions check the instrument status after each call.\n\nAlso, when state caching is enabled, the high-level functions that configure multiple attributes perform instrument I/O only for the attributes whose value you change. Thus, you can safely call the high-level functions without the penalty of redundant instrument I/O.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'grpc_name': 'attribute_id',
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the value to which you want to set the attribute.',
                    'note': 'Some values may not be valid. The allowed values depend on the current settings of the instrument session.'
                },
                'grpc_enum': 'NiRFSGInt32AttributeValues',
                'name': 'value',
                'type': 'ViInt32',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of a ViInt64 attribute.\n\nUse this low-level function to set the values of inherent IVI attributes, class-defined attributes, and instrument-specific attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:\n\n- State caching is disabled for the entire session or for the particular attribute.\n- State caching is enabled, and the currently cached value is invalid or is different than the value you specify.\n\nNI-RFSG contains high-level functions that set most of the instrument attributes. Use the high-level driver functions as much as possible, as they handle order dependencies and multithread locking. The high-level functions also perform status checking only after setting all of the attributes. In contrast, when you set multiple attributes using the SetAttribute functions, the functions check the instrument status after each call.\n\nAlso, when state caching is enabled, the high-level functions that configure multiple attributes perform instrument I/O only for the attributes whose value you change. Thus, you can safely call the high-level functions without the penalty of redundant instrument I/O.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'grpc_name': 'attribute_id',
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value to which you want to set the attribute.\n\n<blockquote>\nSome values may not be valid. The allowed values depend on the current settings of the instrument session.\n</blockquote>'
                },
                'grpc_enum': 'NiRFSGInt64AttributeValues',
                'name': 'value',
                'type': 'ViInt64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of a ViReal64 attribute.\n\nUse this low-level function to set the values of inherent IVI attributes, class-defined attributes, and instrument-specific attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:\n\n- State caching is disabled for the entire session or for the particular attribute.\n- State caching is enabled, and the currently cached value is invalid or is different than the value you specify.\n\nNI-RFSG contains high-level functions that set most of the instrument attributes. Use the high-level driver functions as much as possible, as they handle order dependencies and multithread locking. The high-level functions also perform status checking only after setting all of the attributes. In contrast, when you set multiple attributes using the SetAttribute functions, the functions check the instrument status after each call.\n\nAlso, when state caching is enabled, the high-level functions that configure multiple attributes perform instrument I/O only for the attributes whose value you change. Thus, you can safely call the high-level functions without the penalty of redundant instrument I/O.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'grpc_name': 'attribute_id',
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value to which you want to set the attribute.',
                    'note': 'Some values may not be valid. The allowed values depend on the current settings of the instrument session.'
                },
                'grpc_enum': 'NiRFSGReal64AttributeValues',
                'name': 'value',
                'type': 'ViReal64',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViSession': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of a ViSession attribute.\n\nUse this low-level function to set the values of inherent IVI attributes, class-defined attributes, and instrument-specific attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:\n\n- State caching is disabled for the entire session or for the particular attribute.\n- State caching is enabled, and the currently cached value is invalid or is different than the value you specify.\n\nNI-RFSG contains high-level functions that set most of the instrument attributes. Use the high-level driver functions as much as possible, as they handle order dependencies and multithread locking. The high-level functions also perform status checking only after setting all of the attributes. In contrast, when you set multiple attributes using the SetAttribute functions, the functions check the instrument status after each call.\n\nAlso, when state caching is enabled, the high-level functions that configure multiple attributes perform instrument I/O only for the attributes whose value you change. Thus, you can safely call the high-level functions without the penalty of redundant instrument I/O.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'grpc_name': 'attribute_id',
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value to which you want to set the attribute.',
                    'note': 'Some values may not be valid. The allowed values depend on the current settings of the instrument session.'
                },
                'name': 'value',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of a ViString attribute.\n\nUse this low-level function to set the values of inherent IVI attributes, class-defined attributes, and instrument-specific attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:\n\n- State caching is disabled for the entire session or for the particular attribute.\n- State caching is enabled, and the currently cached value is invalid or is different than the value you specify.\n\nNI-RFSG contains high-level functions that set most of the instrument attributes. Use the high-level driver functions as much as possible, as they handle order dependencies and multithread locking. The high-level functions also perform status checking only after setting all of the attributes. In contrast, when you set multiple attributes using the SetAttribute functions, the functions check the instrument status after each call.\n\nAlso, when state caching is enabled, the high-level functions that configure multiple attributes perform instrument I/O only for the attributes whose value you change. Thus, you can safely call the high-level functions without the penalty of redundant instrument I/O.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
                },
                'name': 'channelName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'grpc_name': 'attribute_id',
                'name': 'attribute',
                'type': 'ViAttr',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value to which you want to set the attribute.',
                    'note': 'Some values may not be valid. The allowed values depend on the current settings of the instrument session.'
                },
                'grpc_mapped_enum': 'NiRFSGStringAttributeValuesMapped',
                'name': 'value',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'SetWaveformBurstStartLocations': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the start location of the burst in samples where the burst refers to the active portion of a waveform.\n\n**Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name. Example: "waveform::waveform0/marker0"'
                },
                'is_repeated_capability': True,
                'name': 'channelName',
                'repeated_capability_type': 'waveforms',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the burst start locations array.'
                },
                'name': 'numberOfLocations',
                'type': 'ViInt32',
                'use_array': False
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Returns the burst start locations stored in the NI-RFSG session for the waveform that you specified in the NIRFSG_ATTR_CHANNEL_NAME parameter. This value is expressed in samples.'
                },
                'name': 'locations',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfLocations'
                },
                'type': 'ViReal64[]',
                'use_in_python_api': True
            }
        ],
        'repeated_capability_type': 'waveforms',
        'returns': 'ViStatus'
    },
    'SetWaveformBurstStopLocations': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the stop location of the burst in samples where the burst refers to the active portion of a waveform.\n\n**Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
                },
                'is_repeated_capability': True,
                'name': 'channelName',
                'repeated_capability_type': 'waveforms',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the burst stop locations array.'
                },
                'name': 'numberOfLocations',
                'type': 'ViInt32',
                'use_array': False
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the burst stop locations, in samples, to store in the NI-RFSG session.'
                },
                'name': 'locations',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfLocations'
                },
                'type': 'ViReal64[]',
                'use_in_python_api': True
            }
        ],
        'repeated_capability_type': 'waveforms',
        'returns': 'ViStatus'
    },
    'SetWaveformMarkerEventLocations': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the marker locations associated with waveform and marker in the NI-RFSG session.\n\n**Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842'
        },
        'has_repeated_capability': True,
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the waveform name and the marker name.\n\nExample:\n\n"waveform::waveform0/marker0"'
                },
                'is_repeated_capability': True,
                'name': 'channelName',
                'repeated_capability_type': 'markers',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the locations array.'
                },
                'name': 'numberOfLocations',
                'type': 'ViInt32',
                'use_array': False
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the marker location, in samples, to store in the NI-RFSG database.'
                },
                'name': 'locations',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfLocations'
                },
                'type': 'ViReal64[]',
                'use_in_python_api': True
            }
        ],
        'repeated_capability_type': 'markers',
        'returns': 'ViStatus'
    },
    'UnlockSession': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReleases a lock obtained on an NI-RFSG device session by calling the nirfsg_LockSession function.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5840/5841/5842/5860'
        },
        'included_in_proto': True,
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Keeps track of whether you obtain a lock and therefore need to unlock the session. Pass the address of a local ViBoolean variable. In the declaration of the local variable, initialize it to VI_FALSE. Pass the address of the same local variable to any other calls you make to the nirfsg_LockSession function or the nirfsg_UnlockSession function in the same function.\n\nThis parameter serves as a convenience. If you do not want to use this parameter, pass VI_NULL.\n\nThe parameter is an input/output parameter. The nirfsg_LockSession function and the nirfsg_UnlockSession each inspect the current value and take the following actions:\n\n- If the value is VI_TRUE, the nirfsg_LockSession function does not lock the session again. If the value is VI_FALSE, the nirfsg_LockSession function obtains the lock and sets the value of the parameter to VI_TRUE.\n- If the value is VI_FALSE, the nirfsg_UnlockSession function does not attempt to unlock the session. If the value is VI_TRUE, the nirfsg_UnlockSession function releases the lock and sets the value of the parameter to VI_FALSE.\n\nThus, you can call the nirfsg_UnlockSession function at the end of your function without worrying about whether you have the lock.\n\nExample:\n\nViStatus TestFunc (ViSession vi, ViInt32 flags)\n{\nViStatus error = VI_SUCCESS;\nViBoolean haveLock = VI_FALSE;\n\nif (flags & BIT_1)\n{\nviCheckErr( nirfsg_LockSession(vi, &haveLock));\nviCheckErr( TakeAction1(vi));\nif (flags & BIT_2)\n{\nviCheckErr( nirfsg_UnlockSession(vi, &haveLock));\nviCheckErr( TakeAction2(vi));\nviCheckErr( nirfsg_LockSession(vi, &haveLock));\n}\nif (flags & BIT_3)\nviCheckErr( TakeAction3(vi));\n}\n\nError:\n\nAt this point, you cannot really be sure that you have the lock.\nFortunately, the haveLock variable takes care of that for you.\n\nnirfsg_UnlockSession(vi, &haveLock);\nreturn error;\n}'
                },
                'name': 'callerHasLock',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'python_name': 'unlock',
        'render_in_session_base': True,
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'WaitUntilSettled': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nWaits until the RF output signal has settled. This function is useful for devices that support changes while in the Generation state.\n\nCall this function after making a dynamic change to wait for the output signal to settle.\n\nYou can also call this function after calling the nirfsg_Commit function to wait for changes to settle. The nirfsg_WaitUntilSettled function is not required after calling the nirfsg_Initiate function because the nirfsg_Initiate automatically waits for the output to settle.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'default_value': 'hightime.timedelta(seconds=10.0)',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the maximum time the function waits for the output to settle. If the maximum time is exceeded, this function returns an error. The units are expressed in milliseconds.\n\n**Default Value** : 10000'
                },
                'name': 'maxTimeMilliseconds',
                'python_api_converter_name': 'convert_timedelta_to_milliseconds_int32',
                'type': 'ViInt32',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or int in milliseconds',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteArbWaveformComplexF32': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nWrites an arbitrary waveform to the NI-RFSG device starting at the position of the last data written in onboard memory.\n\nThis function accepts the complex baseband data in the form of complex singles. If the waveform to write is already allocated using the nirfsg_AllocateArbWaveform function, the more_data_pending parameter is ignored. The PXI-5670/5671 must be in the Configuration state before you call this function. When streaming is enabled, you can call this function when the PXIe-5672/5673/5673E or PXIe-5820/5830/5831/5832/5840/5841/5842/5860 is in the Generation state.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Streaming <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/streaming.html>`_\n\n`Assigning Properties or Attributes to a Waveform <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/assigning-properties-or-attributes-to-a-wavef.html>`_',
            'note': 'On the PXIe-5644/5645/5646, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860, the more_data_pending parameter is always ignored. To write data in blocks on these devices, you must allocate the waveform before writing it.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_name_for_documentation': 'write_arb_waveform',
        'method_templates': [
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'numpy_write_method',
                'method_python_name_suffix': '',
                'session_filename': 'numpy_write_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name used to identify the waveform. This string is case-insensitive and alphanumeric, and it does not use reserved words.'
                },
                'name': 'waveformName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples in both of the data arrays.'
                },
                'name': 'numberOfSamples',
                'type': 'ViInt32',
                'use_array': False
            },
            {
                'complex_array_representation': 'complex_number_array',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the array of data to load into the waveform. The array must have at least as many elements as the value in the **size_in_samples** parameter in the nirfsg_AllocateArbWaveform function.'
                },
                'grpc_name': 'wfm_data',
                'name': 'waveformDataArray',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfSamples'
                },
                'type': 'NIComplexNumberF32[]',
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies whether or not the data block contains the end of the waveform. Set this parameter to VI_TRUE to allow data to be appended later to the waveform. Splitting the waveform into multiple data blocks can reduce the memory requirements of the write operation. Append data to a previously written waveform by using the same waveform in the NIRFSG_ATTR_WAVEFORM_NAME parameter. Set more_data_pending to VI_FALSE to indicate that this data block contains the end of the waveform. If the waveform is already allocated, this parameter is ignored.'
                },
                'name': 'moreDataPending',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteArbWaveformComplexF64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nWrites an arbitrary waveform to the NI-RFSG device starting at the position of the last data written in onboard memory.\n\nThis function accepts the complex baseband data in the form of complex doubles. If the waveform to write is already allocated using the nirfsg_AllocateArbWaveform, the more_data_pending parameter is ignored. The PXI-5670/5671 must be in the Configuration state before you call this function. When streaming is enabled, you can call this function when the PXIe-5672/5673/5673E or PXIe-5820/5830/5831/5832/5840/5841/5842 is in the Generation state.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n**Related Topics**\n\n`Streaming <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/streaming.html>`_\n\n`Assigning Properties or Attributes to a Waveform <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/assigning-properties-or-attributes-to-a-wavef.html>`_',
            'note': 'On the PXIe-5644/5645/5646, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842, the more_data_pending parameter is always ignored. To write data in blocks on these devices, you must allocate the waveform before writing it.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_name_for_documentation': 'write_arb_waveform',
        'method_templates': [
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'numpy_write_method',
                'method_python_name_suffix': '',
                'session_filename': 'numpy_write_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name used to identify the waveform. This string is case-insensitive and alphanumeric, and it does not use reserved words.'
                },
                'name': 'waveformName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples in the data array.'
                },
                'name': 'numberOfSamples',
                'type': 'ViInt32',
                'use_array': False
            },
            {
                'complex_array_representation': 'complex_number_array',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the array of data to load into the waveform. The array must have at least as many elements as the value in the **size_in_samples** parameter in the nirfsg_AllocateArbWaveform function.'
                },
                'grpc_name': 'wfm_data',
                'name': 'waveformDataArray',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfSamples'
                },
                'type': 'NIComplexNumber[]',
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies whether or not the data block contains the end of the waveform. Set this parameter to VI_TRUE to allow data to be appended later to the waveform. Splitting the waveform into multiple data blocks can reduce the memory requirements of the write operation. Append data to a previously written waveform by using the same waveform in the **name** parameter. Set more_data_pending to VI_FALSE to indicate that this data block contains the end of the waveform. If the waveform is already allocated, this parameter is ignored.'
                },
                'name': 'moreDataPending',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteArbWaveformComplexI16': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nWrites an arbitrary waveform to the NI-RFSG device starting at the position of the last data written in onboard memory.\n\nThis function accepts the interleaved I/Q data of a complex baseband signal. The PXI-5670/5671 must be in the Configuration state before you call this function. When streaming is enabled, this function can be called when the PXIe-5672/5673/5673E or PXIe-5820/5830/5831/5832/5840/5841/5842/5860 is in the Generation state.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Streaming <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/streaming.html>`_\n\n`Assigning Properties or Attributes to a Waveform <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/assigning-properties-or-attributes-to-a-wavef.html>`_',
            'note': 'This function only supports NIRFSG_VAL_PEAK_POWER mode as specified in the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute. If you download a waveform when using this function, you cannot set the NIRFSG_ATTR_POWER_LEVEL_TYPE to NIRFSG_VAL_AVERAGE_POWER without causing error in the output.'
        },
        'included_in_proto': True,
        'is_error_handling': False,
        'method_name_for_documentation': 'write_arb_waveform',
        'method_templates': [
            {
                'documentation_filename': 'numpy_method',
                'library_interpreter_filename': 'numpy_write_method',
                'method_python_name_suffix': '',
                'session_filename': 'numpy_write_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name used to identify the waveform. This string is case-insensitive and alphanumeric, and it does not use reserved words.'
                },
                'name': 'waveformName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples in the data array.'
                },
                'name': 'numberOfSamples',
                'type': 'ViInt32',
                'use_array': False
            },
            {
                'complex_array_representation': 'interleaved_real_number_array',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the array of data to load into the waveform. The array must have at least as many elements as the value in the **size_in_samples** parameter in the nirfsg_AllocateArbWaveform function.'
                },
                'grpc_name': 'wfm_data',
                'name': 'waveformDataArray',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfSamples'
                },
                'type': 'NIComplexI16[]',
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteArbWaveformDispatcher': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nWrites an arbitrary waveform to the NI-RFSG device starting at the position of the last data written in onboard memory.\n\nThis function accepts the complex baseband data in the form of numpy array of numpy.complex64 or numpy.complex128 or interleaved numpy array of numpy.int16. If the waveform to write is already allocated using the nirfsg_AllocateArbWaveform, the more_data_pending parameter is ignored. The PXI-5670/5671 must be in the Configuration state before you call this function. When streaming is enabled, you can call this function when the PXIe-5672/5673/5673E or PXIe-5820/5830/5831/5832/5840/5841/5842/5860 is in the Generation state.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Streaming <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/streaming.html>`_\n\n`Assigning Properties or Attributes to a Waveform <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/assigning-properties-or-attributes-to-a-wavef.html>`_',
            'note': 'On the PXIe-5644/5645/5646, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860, the more_data_pending parameter is always ignored. To write data in blocks on these devices, you must allocate the waveform before writing it.\nIf you are writing interleaved numpy array of numpy.int16, then this function only supports NIRFSG_VAL_PEAK_POWER mode as specified in the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute. If you download a waveform as interleaved numpy array of numpy.int16 when using this function, you cannot set the NIRFSG_ATTR_POWER_LEVEL_TYPE to NIRFSG_VAL_AVERAGE_POWER without causing error in the output.'
        },
        'included_in_proto': False,
        'is_error_handling': False,
        'method_name_for_documentation': 'write_arb_waveform',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'write_arb_waveform'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name used to identify the waveform. This string is case-insensitive and alphanumeric, and it does not use reserved words.'
                },
                'name': 'waveformName',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'complex_array_representation': 'complex_number_array',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the array of data to load into the waveform. The array must have at least as many elements as the value in the **size_in_samples** parameter in the nirfsg_AllocateArbWaveform function.'
                },
                'name': 'waveformDataArray',
                'numpy': True,
                'type': 'NIComplexNumber[]',
                'type_in_documentation': 'numpy array of numpy.complex64, numpy array of numpy.complex128 or interleaved complex data in the form of numpy array of numpy.int16',
                'use_in_python_api': True
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies whether or not the data block contains the end of the waveform. Set this parameter to VI_TRUE to allow data to be appended later to the waveform. Splitting the waveform into multiple data blocks can reduce the memory requirements of the write operation. Append data to a previously written waveform by using the same waveform in the **name** parameter. Set more_data_pending to VI_FALSE to indicate that this data block contains the end of the waveform. If the waveform is already allocated, this parameter is ignored.'
                },
                'name': 'moreDataPending',
                'type': 'ViBoolean',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'python_name': 'write_arb_waveform',
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'WriteScript': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nWrites a script to the device to control waveform generation in Script mode.\n\nFirst, configure your device for Script mode by setting the generation_mode property. The NI-RFSG device must be in the Configuration state before calling the nirfsg_WriteScript function.\n\n**Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Scripting Instructions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_instructions.html>`_--Refer to this topic for more information about VST restrictions on scripts.\n\n`Common Scripting Use Cases <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_use_cases.html>`_',
            'note': 'If you are using an RF vector signal transceiver (VST) device, some script instructions may not be supported.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies a string containing a syntactically correct script. NI-RFSG supports multiple scripts that are selected with the NIRFSG_ATTR_SELECTED_SCRIPT attribute. Refer to `Scripting Instructions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_instructions.html>`_ for more information about using scripts.'
                },
                'name': 'script',
                'type': 'ViConstString',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'close': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nAborts any signal generation in progress and destroys the instrument driver session.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_\n\n`NI-RFSG Programming State Model <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5670_programming_state_model.html>`_'
        },
        'grpc_name': 'Close',
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'python_name': '_close',
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'fancy_self_test': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nPerforms a self-test on the NI-RFSG device and returns the test results.\n\nThis function performs a simple series of tests to ensure that the NI-RFSG device is powered up and responding.\n\nThis function does not affect external I/O connections or connections between devices. Complete functional testing and calibration are not performed by this function. The NI-RFSG device must be in the Configuration state before you call this function.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Device Warm-Up <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/warmup.html>`_',
            'table_body': [
                [
                    '0',
                    'Passed self-test'
                ],
                [
                    '1',
                    'Self-test failed'
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
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': 'self_test',
        'returns': 'ViStatus'
    },
    'reset': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nResets all attributes to their default values and moves the NI-RFSG device to the Configuration state.\n\nThis function aborts the generation, deletes all de-embedding tables, clears all routes, and resets session attributes to their initial values. During a reset, routes of signals between this and other devices are released, regardless of which device created the route.\n\nGenerally, calling this function instead of the nirfsg_ResetDevice function is acceptable. The nirfsg_Reset function executes faster than the nirfsg_ResetDevice function.\n\nTo avoid resetting routes on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860 that are in use by NI-RFSA sessions, NI recommends using the nirfsg_ResetWithOptions function, with **stepsToOmit** set to NIRFSG_VAL_RESET_WITH_OPTIONS_ROUTES .\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
            'note': 'This function resets all configured routes for the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860 in NI-RFSA and NI-RFSG.'
        },
        'grpc_name': 'Reset',
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession',
                'use_array': False,
                'use_in_python_api': True
            }
        ],
        'returns': 'ViStatus'
    },
    'self_test': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nPerforms a self-test on the NI-RFSG device and returns the test results.\n\nThis function performs a simple series of tests to ensure that the NI-RFSG device is powered up and responding.\n\nThis function does not affect external I/O connections or connections between devices. Complete functional testing and calibration are not performed by this function. The NI-RFSG device must be in the Configuration state before you call this function.\n\n**Supported Devices** : PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Device Warm-Up <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/warmup.html>`_'
        },
        'grpc_name': 'SelfTest',
        'included_in_proto': True,
        'method_name_for_documentation': 'self_test',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. The ViSession handle is obtained from the nirfsg_Init function or the nirfsg_InitWithOptions function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'This parameter contains the value returned from the NI-RFSG device self test.',
                    'table_body': [
                        [
                            '0',
                            'Self test passed'
                        ],
                        [
                            '1',
                            'Self test failed'
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
                    'description': 'Returns the self-test response string from the NI-RFSG device. For an explanation of the string contents, refer to the **status** parameter of this function.\n\nYou must pass a ViChar array with at least 256 bytes.'
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

<!--NI_OSS_SOURCE repo=nimi-python path=src/nirfsg/metadata/functions_addon.py sha256=f9b535c8d10404d8faf24ce86229f202442b6f7a37382315272c89709484ec8d bytes=342 -->
## FILE: src/nirfsg/metadata/functions_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nirfsg/metadata/functions_addon.py`
- sha256: `f9b535c8d10404d8faf24ce86229f202442b6f7a37382315272c89709484ec8d`
- bytes: 342

````python
# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {}
functions_additional_fetch_array_measurement = {
}

functions_additional_fetch_array_measurement_stats = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nirfsg/metadata/nirfsg.proto sha256=2377c8ceff39282f9a0bb06eca59d20017defd207c191b0139787732c7eb30f9 bytes=72188 -->
## FILE: src/nirfsg/metadata/nirfsg.proto

- repository: `ni/nimi-python`
- source_path: `src/nirfsg/metadata/nirfsg.proto`
- sha256: `2377c8ceff39282f9a0bb06eca59d20017defd207c191b0139787732c7eb30f9`
- bytes: 72188

````protobuf

//---------------------------------------------------------------------
// This file is generated from NI-RFSG API metadata version 25.5.0
//---------------------------------------------------------------------
// Proto file for the NI-RFSG Metadata
//---------------------------------------------------------------------
syntax = "proto3";

option java_multiple_files = true;
option java_package = "com.ni.grpc.nirfsg";
option java_outer_classname = "NiRFSG";
option csharp_namespace = "NationalInstruments.Grpc.NiRFSG";

package nirfsg_grpc;

import "nidevice.proto";
import "session.proto";

service NiRFSG {
  rpc Abort(AbortRequest) returns (AbortResponse);
  rpc AllocateArbWaveform(AllocateArbWaveformRequest) returns (AllocateArbWaveformResponse);
  rpc CheckAttributeViBoolean(CheckAttributeViBooleanRequest) returns (CheckAttributeViBooleanResponse);
  rpc CheckAttributeViInt32(CheckAttributeViInt32Request) returns (CheckAttributeViInt32Response);
  rpc CheckAttributeViInt64(CheckAttributeViInt64Request) returns (CheckAttributeViInt64Response);
  rpc CheckAttributeViReal64(CheckAttributeViReal64Request) returns (CheckAttributeViReal64Response);
  rpc CheckAttributeViSession(CheckAttributeViSessionRequest) returns (CheckAttributeViSessionResponse);
  rpc CheckAttributeViString(CheckAttributeViStringRequest) returns (CheckAttributeViStringResponse);
  rpc CheckGenerationStatus(CheckGenerationStatusRequest) returns (CheckGenerationStatusResponse);
  rpc CheckIfConfigurationListExists(CheckIfConfigurationListExistsRequest) returns (CheckIfConfigurationListExistsResponse);
  rpc CheckIfScriptExists(CheckIfScriptExistsRequest) returns (CheckIfScriptExistsResponse);
  rpc CheckIfWaveformExists(CheckIfWaveformExistsRequest) returns (CheckIfWaveformExistsResponse);
  rpc ClearAllArbWaveforms(ClearAllArbWaveformsRequest) returns (ClearAllArbWaveformsResponse);
  rpc ClearArbWaveform(ClearArbWaveformRequest) returns (ClearArbWaveformResponse);
  rpc ClearError(ClearErrorRequest) returns (ClearErrorResponse);
  rpc ClearSelfCalibrateRange(ClearSelfCalibrateRangeRequest) returns (ClearSelfCalibrateRangeResponse);
  rpc Close(CloseRequest) returns (CloseResponse);
  rpc Commit(CommitRequest) returns (CommitResponse);
  rpc ConfigureDeembeddingTableInterpolationLinear(ConfigureDeembeddingTableInterpolationLinearRequest) returns (ConfigureDeembeddingTableInterpolationLinearResponse);
  rpc ConfigureDeembeddingTableInterpolationNearest(ConfigureDeembeddingTableInterpolationNearestRequest) returns (ConfigureDeembeddingTableInterpolationNearestResponse);
  rpc ConfigureDeembeddingTableInterpolationSpline(ConfigureDeembeddingTableInterpolationSplineRequest) returns (ConfigureDeembeddingTableInterpolationSplineResponse);
  rpc ConfigureDigitalEdgeConfigurationListStepTrigger(ConfigureDigitalEdgeConfigurationListStepTriggerRequest) returns (ConfigureDigitalEdgeConfigurationListStepTriggerResponse);
  rpc ConfigureDigitalEdgeScriptTrigger(ConfigureDigitalEdgeScriptTriggerRequest) returns (ConfigureDigitalEdgeScriptTriggerResponse);
  rpc ConfigureDigitalEdgeStartTrigger(ConfigureDigitalEdgeStartTriggerRequest) returns (ConfigureDigitalEdgeStartTriggerResponse);
  rpc ConfigureDigitalLevelScriptTrigger(ConfigureDigitalLevelScriptTriggerRequest) returns (ConfigureDigitalLevelScriptTriggerResponse);
  rpc ConfigureDigitalModulationUserDefinedWaveform(ConfigureDigitalModulationUserDefinedWaveformRequest) returns (ConfigureDigitalModulationUserDefinedWaveformResponse);
  rpc ConfigureGenerationMode(ConfigureGenerationModeRequest) returns (ConfigureGenerationModeResponse);
  rpc ConfigureOutputEnabled(ConfigureOutputEnabledRequest) returns (ConfigureOutputEnabledResponse);
  rpc ConfigureP2PEndpointFullnessStartTrigger(ConfigureP2PEndpointFullnessStartTriggerRequest) returns (ConfigureP2PEndpointFullnessStartTriggerResponse);
  rpc ConfigurePXIChassisClk10(ConfigurePXIChassisClk10Request) returns (ConfigurePXIChassisClk10Response);
  rpc ConfigurePowerLevelType(ConfigurePowerLevelTypeRequest) returns (ConfigurePowerLevelTypeResponse);
  rpc ConfigureRF(ConfigureRFRequest) returns (ConfigureRFResponse);
  rpc ConfigureRefClock(ConfigureRefClockRequest) returns (ConfigureRefClockResponse);
  rpc ConfigureSignalBandwidth(ConfigureSignalBandwidthRequest) returns (ConfigureSignalBandwidthResponse);
  rpc ConfigureSoftwareScriptTrigger(ConfigureSoftwareScriptTriggerRequest) returns (ConfigureSoftwareScriptTriggerResponse);
  rpc ConfigureSoftwareStartTrigger(ConfigureSoftwareStartTriggerRequest) returns (ConfigureSoftwareStartTriggerResponse);
  rpc ConfigureUpconverterPLLSettlingTime(ConfigureUpconverterPLLSettlingTimeRequest) returns (ConfigureUpconverterPLLSettlingTimeResponse);
  rpc CreateConfigurationList(CreateConfigurationListRequest) returns (CreateConfigurationListResponse);
  rpc CreateConfigurationListStep(CreateConfigurationListStepRequest) returns (CreateConfigurationListStepResponse);
  rpc CreateDeembeddingSparameterTableArray(CreateDeembeddingSparameterTableArrayRequest) returns (CreateDeembeddingSparameterTableArrayResponse);
  rpc CreateDeembeddingSparameterTableS2PFile(CreateDeembeddingSparameterTableS2PFileRequest) returns (CreateDeembeddingSparameterTableS2PFileResponse);
  rpc DeleteAllDeembeddingTables(DeleteAllDeembeddingTablesRequest) returns (DeleteAllDeembeddingTablesResponse);
  rpc DeleteConfigurationList(DeleteConfigurationListRequest) returns (DeleteConfigurationListResponse);
  rpc DeleteDeembeddingTable(DeleteDeembeddingTableRequest) returns (DeleteDeembeddingTableResponse);
  rpc DeleteScript(DeleteScriptRequest) returns (DeleteScriptResponse);
  rpc Disable(DisableRequest) returns (DisableResponse);
  rpc DisableAllModulation(DisableAllModulationRequest) returns (DisableAllModulationResponse);
  rpc DisableConfigurationListStepTrigger(DisableConfigurationListStepTriggerRequest) returns (DisableConfigurationListStepTriggerResponse);
  rpc DisableScriptTrigger(DisableScriptTriggerRequest) returns (DisableScriptTriggerResponse);
  rpc DisableStartTrigger(DisableStartTriggerRequest) returns (DisableStartTriggerResponse);
  rpc ErrorMessage(ErrorMessageRequest) returns (ErrorMessageResponse);
  rpc ErrorQuery(ErrorQueryRequest) returns (ErrorQueryResponse);
  rpc ExportSignal(ExportSignalRequest) returns (ExportSignalResponse);
  rpc GetAllNamedWaveformNames(GetAllNamedWaveformNamesRequest) returns (GetAllNamedWaveformNamesResponse);
  rpc GetAllScriptNames(GetAllScriptNamesRequest) returns (GetAllScriptNamesResponse);
  rpc GetScript(GetScriptRequest) returns (GetScriptResponse);
  rpc GetAttributeViBoolean(GetAttributeViBooleanRequest) returns (GetAttributeViBooleanResponse);
  rpc GetAttributeViInt32(GetAttributeViInt32Request) returns (GetAttributeViInt32Response);
  rpc GetAttributeViInt64(GetAttributeViInt64Request) returns (GetAttributeViInt64Response);
  rpc GetAttributeViReal64(GetAttributeViReal64Request) returns (GetAttributeViReal64Response);
  rpc GetAttributeViSession(GetAttributeViSessionRequest) returns (GetAttributeViSessionResponse);
  rpc GetAttributeViString(GetAttributeViStringRequest) returns (GetAttributeViStringResponse);
  rpc GetChannelName(GetChannelNameRequest) returns (GetChannelNameResponse);
  rpc GetDeembeddingSparameters(GetDeembeddingSparametersRequest) returns (GetDeembeddingSparametersResponse);
  rpc GetError(GetErrorRequest) returns (GetErrorResponse);
  rpc GetExternalCalibrationLastDateAndTime(GetExternalCalibrationLastDateAndTimeRequest) returns (GetExternalCalibrationLastDateAndTimeResponse);
  rpc GetMaxSettablePower(GetMaxSettablePowerRequest) returns (GetMaxSettablePowerResponse);
  rpc GetSelfCalibrationDateAndTime(GetSelfCalibrationDateAndTimeRequest) returns (GetSelfCalibrationDateAndTimeResponse);
  rpc GetSelfCalibrationTemperature(GetSelfCalibrationTemperatureRequest) returns (GetSelfCalibrationTemperatureResponse);
  rpc GetTerminalName(GetTerminalNameRequest) returns (GetTerminalNameResponse);
  rpc GetUserData(GetUserDataRequest) returns (GetUserDataResponse);
  rpc GetWaveformBurstStartLocations(GetWaveformBurstStartLocationsRequest) returns (GetWaveformBurstStartLocationsResponse);
  rpc GetWaveformBurstStopLocations(GetWaveformBurstStopLocationsRequest) returns (GetWaveformBurstStopLocationsResponse);
  rpc GetWaveformMarkerEventLocations(GetWaveformMarkerEventLocationsRequest) returns (GetWaveformMarkerEventLocationsResponse);
  rpc Init(InitRequest) returns (InitResponse);
  rpc InitWithOptions(InitWithOptionsRequest) returns (InitWithOptionsResponse);
  rpc Initiate(InitiateRequest) returns (InitiateResponse);
  rpc InvalidateAllAttributes(InvalidateAllAttributesRequest) returns (InvalidateAllAttributesResponse);
  rpc LoadConfigurationsFromFile(LoadConfigurationsFromFileRequest) returns (LoadConfigurationsFromFileResponse);
  rpc PerformPowerSearch(PerformPowerSearchRequest) returns (PerformPowerSearchResponse);
  rpc PerformThermalCorrection(PerformThermalCorrectionRequest) returns (PerformThermalCorrectionResponse);
  rpc QueryArbWaveformCapabilities(QueryArbWaveformCapabilitiesRequest) returns (QueryArbWaveformCapabilitiesResponse);
  rpc ReadAndDownloadWaveformFromFileTDMS(ReadAndDownloadWaveformFromFileTDMSRequest) returns (ReadAndDownloadWaveformFromFileTDMSResponse);
  rpc Reset(ResetRequest) returns (ResetResponse);
  rpc ResetAttribute(ResetAttributeRequest) returns (ResetAttributeResponse);
  rpc ResetDevice(ResetDeviceRequest) returns (ResetDeviceResponse);
  rpc ResetWithDefaults(ResetWithDefaultsRequest) returns (ResetWithDefaultsResponse);
  rpc ResetWithOptions(ResetWithOptionsRequest) returns (ResetWithOptionsResponse);
  rpc RevisionQuery(RevisionQueryRequest) returns (RevisionQueryResponse);
  rpc SaveConfigurationsToFile(SaveConfigurationsToFileRequest) returns (SaveConfigurationsToFileResponse);
  rpc SelectArbWaveform(SelectArbWaveformRequest) returns (SelectArbWaveformResponse);
  rpc SelfCal(SelfCalRequest) returns (SelfCalResponse);
  rpc SelfCalibrateRange(SelfCalibrateRangeRequest) returns (SelfCalibrateRangeResponse);
  rpc SelfTest(SelfTestRequest) returns (SelfTestResponse);
  rpc SendSoftwareEdgeTrigger(SendSoftwareEdgeTriggerRequest) returns (SendSoftwareEdgeTriggerResponse);
  rpc SetArbWaveformNextWritePosition(SetArbWaveformNextWritePositionRequest) returns (SetArbWaveformNextWritePositionResponse);
  rpc SetAttributeViBoolean(SetAttributeViBooleanRequest) returns (SetAttributeViBooleanResponse);
  rpc SetAttributeViInt32(SetAttributeViInt32Request) returns (SetAttributeViInt32Response);
  rpc SetAttributeViInt64(SetAttributeViInt64Request) returns (SetAttributeViInt64Response);
  rpc SetAttributeViReal64(SetAttributeViReal64Request) returns (SetAttributeViReal64Response);
  rpc SetAttributeViSession(SetAttributeViSessionRequest) returns (SetAttributeViSessionResponse);
  rpc SetAttributeViString(SetAttributeViStringRequest) returns (SetAttributeViStringResponse);
  rpc SetUserData(SetUserDataRequest) returns (SetUserDataResponse);
  rpc SetWaveformBurstStartLocations(SetWaveformBurstStartLocationsRequest) returns (SetWaveformBurstStartLocationsResponse);
  rpc SetWaveformBurstStopLocations(SetWaveformBurstStopLocationsRequest) returns (SetWaveformBurstStopLocationsResponse);
  rpc SetWaveformMarkerEventLocations(SetWaveformMarkerEventLocationsRequest) returns (SetWaveformMarkerEventLocationsResponse);
  rpc WaitUntilSettled(WaitUntilSettledRequest) returns (WaitUntilSettledResponse);
  rpc WriteArbWaveform(WriteArbWaveformRequest) returns (WriteArbWaveformResponse);
  rpc WriteArbWaveformComplexF32(WriteArbWaveformComplexF32Request) returns (WriteArbWaveformComplexF32Response);
  rpc WriteArbWaveformComplexF64(WriteArbWaveformComplexF64Request) returns (WriteArbWaveformComplexF64Response);
  rpc WriteArbWaveformComplexI16(WriteArbWaveformComplexI16Request) returns (WriteArbWaveformComplexI16Response);
  rpc WriteArbWaveformF32(WriteArbWaveformF32Request) returns (WriteArbWaveformF32Response);
  rpc WriteScript(WriteScriptRequest) returns (WriteScriptResponse);
}

enum NiRFSGAttribute {
  NIRFSG_ATTRIBUTE_UNSPECIFIED = 0;
  NIRFSG_ATTRIBUTE_RANGE_CHECK = 1050002;
  NIRFSG_ATTRIBUTE_QUERY_INSTRUMENT_STATUS = 1050003;
  NIRFSG_ATTRIBUTE_CACHE = 1050004;
  NIRFSG_ATTRIBUTE_SIMULATE = 1050005;
  NIRFSG_ATTRIBUTE_RECORD_COERCIONS = 1050006;
  NIRFSG_ATTRIBUTE_DRIVER_SETUP = 1050007;
  NIRFSG_ATTRIBUTE_INTERCHANGE_CHECK = 1050021;
  NIRFSG_ATTRIBUTE_SPY = 1050022;
  NIRFSG_ATTRIBUTE_USE_SPECIFIC_SIMULATION = 1050023;
  NIRFSG_ATTRIBUTE_CHANNEL_COUNT = 1050203;
  NIRFSG_ATTRIBUTE_SPECIFIC_DRIVER_PREFIX = 1050302;
  NIRFSG_ATTRIBUTE_IO_RESOURCE_DESCRIPTOR = 1050304;
  NIRFSG_ATTRIBUTE_LOGICAL_NAME = 1050305;
  NIRFSG_ATTRIBUTE_SUPPORTED_INSTRUMENT_MODELS = 1050327;
  NIRFSG_ATTRIBUTE_GROUP_CAPABILITIES = 1050401;
  NIRFSG_ATTRIBUTE_FUNCTION_CAPABILITIES = 1050402;
  NIRFSG_ATTRIBUTE_INSTRUMENT_FIRMWARE_REVISION = 1050510;
  NIRFSG_ATTRIBUTE_INSTRUMENT_MANUFACTURER = 1050511;
  NIRFSG_ATTRIBUTE_INSTRUMENT_MODEL = 1050512;
  NIRFSG_ATTRIBUTE_SPECIFIC_DRIVER_VENDOR = 1050513;
  NIRFSG_ATTRIBUTE_SPECIFIC_DRIVER_DESCRIPTION = 1050514;
  NIRFSG_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION = 1050515;
  NIRFSG_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION = 1050516;
  NIRFSG_ATTRIBUTE_SPECIFIC_DRIVER_REVISION = 1050551;
  NIRFSG_ATTRIBUTE_REF_CLOCK_SOURCE = 1150001;
  NIRFSG_ATTRIBUTE_DIGITAL_EDGE_START_TRIGGER_SOURCE = 1150002;
  NIRFSG_ATTRIBUTE_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL = 1150003;
  NIRFSG_ATTRIBUTE_PXI_CHASSIS_CLK10_SOURCE = 1150004;
  NIRFSG_ATTRIBUTE_PHASE_CONTINUITY_ENABLED = 1150005;
  NIRFSG_ATTRIBUTE_FREQUENCY_TOLERANCE = 1150006;
  NIRFSG_ATTRIBUTE_SIGNAL_BANDWIDTH = 1150007;
  NIRFSG_ATTRIBUTE_AUTOMATIC_THERMAL_CORRECTION = 1150008;
  NIRFSG_ATTRIBUTE_ATTENUATOR_HOLD_ENABLED = 1150009;
  NIRFSG_ATTRIBUTE_ATTENUATOR_HOLD_MAX_POWER = 1150010;
  NIRFSG_ATTRIBUTE_PEAK_ENVELOPE_POWER = 1150011;
  NIRFSG_ATTRIBUTE_DIGITAL_EQUALIZATION_ENABLED = 1150012;
  NIRFSG_ATTRIBUTE_LO_OUT_ENABLED = 1150013;
  NIRFSG_ATTRIBUTE_ALLOW_OUT_OF_SPECIFICATION_USER_SETTINGS = 1150014;
  NIRFSG_ATTRIBUTE_ARB_CARRIER_FREQUENCY = 1150015;
  NIRFSG_ATTRIBUTE_ARB_POWER = 1150016;
  NIRFSG_ATTRIBUTE_DEVICE_TEMPERATURE = 1150017;
  NIRFSG_ATTRIBUTE_GENERATION_MODE = 1150018;
  NIRFSG_ATTRIBUTE_SCRIPT_TRIGGER_TYPE = 1150019;
  NIRFSG_ATTRIBUTE_DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE = 1150020;
  NIRFSG_ATTRIBUTE_DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE = 1150021;
  NIRFSG_ATTRIBUTE_EXPORTED_SCRIPT_TRIGGER_OUTPUT_TERMINAL = 1150022;
  NIRFSG_ATTRIBUTE_SELECTED_SCRIPT = 1150023;
  NIRFSG_ATTRIBUTE_PHASE_OFFSET = 1150024;
  NIRFSG_ATTRIBUTE_ARB_PRE_FILTER_GAIN = 1150025;
  NIRFSG_ATTRIBUTE_SERIAL_NUMBER = 1150026;
  NIRFSG_ATTRIBUTE_LOOP_BANDWIDTH = 1150027;
  NIRFSG_ATTRIBUTE_ARB_ONBOARD_SAMPLE_CLOCK_MODE = 1150029;
  NIRFSG_ATTRIBUTE_ARB_SAMPLE_CLOCK_SOURCE = 1150030;
  NIRFSG_ATTRIBUTE_ARB_SAMPLE_CLOCK_RATE = 1150031;
  NIRFSG_ATTRIBUTE_ANALOG_MODULATION_TYPE = 1150032;
  NIRFSG_ATTRIBUTE_ANALOG_MODULATION_WAVEFORM_TYPE = 1150033;
  NIRFSG_ATTRIBUTE_ANALOG_MODULATION_WAVEFORM_FREQUENCY = 1150034;
  NIRFSG_ATTRIBUTE_ANALOG_MODULATION_FM_DEVIATION = 1150035;
  NIRFSG_ATTRIBUTE_DIGITAL_MODULATION_TYPE = 1150036;
  NIRFSG_ATTRIBUTE_DIGITAL_MODULATION_SYMBOL_RATE = 1150037;
  NIRFSG_ATTRIBUTE_DIGITAL_MODULATION_WAVEFORM_TYPE = 1150038;
  NIRFSG_ATTRIBUTE_DIGITAL_MODULATION_PRBS_ORDER = 1150039;
  NIRFSG_ATTRIBUTE_DIGITAL_MODULATION_PRBS_SEED = 1150040;
  NIRFSG_ATTRIBUTE_DIGITAL_MODULATION_FSK_DEVIATION = 1150041;
  NIRFSG_ATTRIBUTE_DIRECT_DOWNLOAD = 1150042;
  NIRFSG_ATTRIBUTE_POWER_LEVEL_TYPE = 1150043;
  NIRFSG_ATTRIBUTE_DIGITAL_PATTERN = 1150044;
  NIRFSG_ATTRIBUTE_STREAMING_ENABLED = 1150045;
  NIRFSG_ATTRIBUTE_STREAMING_WAVEFORM_NAME = 1150046;
  NIRFSG_ATTRIBUTE_STREAMING_SPACE_AVAILABLE_IN_WAVEFORM = 1150047;
  NIRFSG_ATTRIBUTE_DATA_TRANSFER_BLOCK_SIZE = 1150048;
  NIRFSG_ATTRIBUTE_ARB_WAVEFORM_SOFTWARE_SCALING_FACTOR = 1150052;
  NIRFSG_ATTRIBUTE_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL = 1150053;
  NIRFSG_ATTRIBUTE_DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE = 1150054;
  NIRFSG_ATTRIBUTE_DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL = 1150055;
  NIRFSG_ATTRIBUTE_ARB_FILTER_TYPE = 1150056;
  NIRFSG_ATTRIBUTE_ARB_FILTER_ROOT_RAISED_COSINE_ALPHA = 1150057;
  NIRFSG_ATTRIBUTE_UPCONVERTER_CENTER_FREQUENCY_INCREMENT = 1150058;
  NIRFSG_ATTRIBUTE_UPCONVERTER_CENTER_FREQUENCY_INCREMENT_ANCHOR = 1150059;
  NIRFSG_ATTRIBUTE_ARB_FILTER_RAISED_COSINE_ALPHA = 1150060;
  NIRFSG_ATTRIBUTE_MEMORY_SIZE = 1150061;
  NIRFSG_ATTRIBUTE_ANALOG_MODULATION_PM_DEVIATION = 1150062;
  NIRFSG_ATTRIBUTE_EXPORTED_DONE_EVENT_OUTPUT_TERMINAL = 1150063;
  NIRFSG_ATTRIBUTE_EXPORTED_MARKER_EVENT_OUTPUT_TERMINAL = 1150064;
  NIRFSG_ATTRIBUTE_EXPORTED_STARTED_EVENT_OUTPUT_TERMINAL = 1150065;
  NIRFSG_ATTRIBUTE_LO_OUT_POWER = 1150066;
  NIRFSG_ATTRIBUTE_LO_IN_POWER = 1150067;
  NIRFSG_ATTRIBUTE_ARB_TEMPERATURE = 1150068;
  NIRFSG_ATTRIBUTE_IQ_IMPAIRMENT_ENABLED = 1150069;
  NIRFSG_ATTRIBUTE_IQ_I_OFFSET = 1150070;
  NIRFSG_ATTRIBUTE_IQ_Q_OFFSET = 1150071;
  NIRFSG_ATTRIBUTE_IQ_GAIN_IMBALANCE = 1150072;
  NIRFSG_ATTRIBUTE_IQ_SKEW = 1150073;
  NIRFSG_ATTRIBUTE_LO_TEMPERATURE = 1150075;
  NIRFSG_ATTRIBUTE_EXTERNAL_CALIBRATION_RECOMMENDED_INTERVAL = 1150076;
  NIRFSG_ATTRIBUTE_EXTERNAL_CALIBRATION_TEMPERATURE = 1150077;
  NIRFSG_ATTRIBUTE_EXTERNAL_CALIBRATION_USER_DEFINED_INFO = 1150078;
  NIRFSG_ATTRIBUTE_EXTERNAL_CALIBRATION_USER_DEFINED_INFO_MAX_SIZE = 1150079;
  NIRFSG_ATTRIBUTE_IQ_OFFSET_UNITS = 1150081;
  NIRFSG_ATTRIBUTE_FREQUENCY_SETTLING_UNITS = 1150082;
  NIRFSG_ATTRIBUTE_FREQUENCY_SETTLING = 1150083;
  NIRFSG_ATTRIBUTE_MODULE_REVISION = 1150084;
  NIRFSG_ATTRIBUTE_EXTERNAL_GAIN = 1150085;
  NIRFSG_ATTRIBUTE_DATA_TRANSFER_MAXIMUM_BANDWIDTH = 1150086;
  NIRFSG_ATTRIBUTE_DATA_TRANSFER_PREFERRED_PACKET_SIZE = 1150087;
  NIRFSG_ATTRIBUTE_DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READS = 1150088;
  NIRFSG_ATTRIBUTE_ARB_OSCILLATOR_PHASE_DAC_VALUE = 1150089;
  NIRFSG_ATTRIBUTE_ACTIVE_CONFIGURATION_LIST = 1150096;
  NIRFSG_ATTRIBUTE_ACTIVE_CONFIGURATION_LIST_STEP = 1150097;
  NIRFSG_ATTRIBUTE_CONFIGURATION_LIST_STEP_TRIGGER_TYPE = 1150098;
  NIRFSG_ATTRIBUTE_DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE = 1150099;
  NIRFSG_ATTRIBUTE_TIMER_EVENT_INTERVAL = 1150100;
  NIRFSG_ATTRIBUTE_CONFIGURATION_LIST_REPEAT = 1150102;
  NIRFSG_ATTRIBUTE_DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_EDGE = 1150103;
  NIRFSG_ATTRIBUTE_CORRECTION_TEMPERATURE = 1150104;
  NIRFSG_ATTRIBUTE_EXPORTED_CONFIGURATION_LIST_STEP_TRIGGER_OUTPUT_TERMINAL = 1150105;
  NIRFSG_ATTRIBUTE_STARTED_EVENT_TERMINAL_NAME = 1150112;
  NIRFSG_ATTRIBUTE_DONE_EVENT_TERMINAL_NAME = 1150113;
  NIRFSG_ATTRIBUTE_START_TRIGGER_TERMINAL_NAME = 1150114;
  NIRFSG_ATTRIBUTE_MARKER_EVENT_TERMINAL_NAME = 1150115;
  NIRFSG_ATTRIBUTE_SCRIPT_TRIGGER_TERMINAL_NAME = 1150116;
  NIRFSG_ATTRIBUTE_CONFIGURATION_LIST_STEP_TRIGGER_TERMINAL_NAME = 1150117;
  NIRFSG_ATTRIBUTE_YIG_MAIN_COIL_DRIVE = 1150118;
  NIRFSG_ATTRIBUTE_CONFIGURATION_LIST_STEP_IN_PROGRESS = 1150122;
  NIRFSG_ATTRIBUTE_P2P_ENABLED = 1150123;
  NIRFSG_ATTRIBUTE_P2P_ENDPOINT_SIZE = 1150124;
  NIRFSG_ATTRIBUTE_P2P_SPACE_AVAILABLE_IN_ENDPOINT = 1150125;
  NIRFSG_ATTRIBUTE_P2P_MOST_SPACE_AVAILABLE_IN_ENDPOINT = 1150126;
  NIRFSG_ATTRIBUTE_P2P_ENDPOINT_COUNT = 1150127;
  NIRFSG_ATTRIBUTE_P2P_ENDPOINT_FULLNESS_START_TRIGGER_LEVEL = 1150128;
  NIRFSG_ATTRIBUTE_EXPORTED_CONFIGURATION_SETTLED_EVENT_OUTPUT_TERMINAL = 1150129;
  NIRFSG_ATTRIBUTE_PEAK_POWER_ADJUSTMENT = 1150132;
  NIRFSG_ATTRIBUTE_REF_PLL_BANDWIDTH = 1150133;
  NIRFSG_ATTRIBUTE_P2P_DATA_TRANSFER_PERMISSION_INTERVAL = 1150134;
  NIRFSG_ATTRIBUTE_P2P_DATA_TRANSFER_PERMISSION_INITIAL_CREDITS = 1150135;
  NIRFSG_ATTRIBUTE_SELF_CALIBRATION_TEMPERATURE = 1150136;
  NIRFSG_ATTRIBUTE_AMPLITUDE_SETTLING = 1150137;
  NIRFSG_ATTRIBUTE_STREAMING_WRITE_TIMEOUT = 1150140;
  NIRFSG_ATTRIBUTE_PEAK_POWER_ADJUSTMENT_INHERITANCE = 1150141;
  NIRFSG_ATTRIBUTE_SYNC_SCRIPT_TRIGGER_MASTER = 1150142;
  NIRFSG_ATTRIBUTE_SYNC_SCRIPT_TRIGGER_DIST_LINE = 1150143;
  NIRFSG_ATTRIBUTE_OUTPUT_PORT = 1150144;
  NIRFSG_ATTRIBUTE_IQ_OUT_PORT_CARRIER_FREQUENCY = 1150145;
  NIRFSG_ATTRIBUTE_IQ_OUT_PORT_TERMINAL_CONFIGURATION = 1150146;
  NIRFSG_ATTRIBUTE_IQ_OUT_PORT_LEVEL = 1150147;
  NIRFSG_ATTRIBUTE_IQ_OUT_PORT_COMMON_MODE_OFFSET = 1150148;
  NIRFSG_ATTRIBUTE_IQ_OUT_PORT_OFFSET = 1150149;
  NIRFSG_ATTRIBUTE_LO_SOURCE = 1150150;
  NIRFSG_ATTRIBUTE_LO_FREQUENCY_STEP_SIZE = 1150151;
  NIRFSG_ATTRIBUTE_LO_PLL_FRACTIONAL_MODE_ENABLED = 1150152;
  NIRFSG_ATTRIBUTE_INTERPOLATION_DELAY = 1150153;
  NIRFSG_ATTRIBUTE_EVENTS_DELAY = 1150154;
  NIRFSG_ATTRIBUTE_SYNC_START_TRIGGER_MASTER = 1150155;
  NIRFSG_ATTRIBUTE_SYNC_START_TRIGGER_DIST_LINE = 1150156;
  NIRFSG_ATTRIBUTE_ARB_WAVEFORM_REPEAT_COUNT_IS_FINITE = 1150157;
  NIRFSG_ATTRIBUTE_ARB_WAVEFORM_REPEAT_COUNT = 1150158;
  NIRFSG_ATTRIBUTE_UPCONVERTER_FREQUENCY_OFFSET = 1150160;
  NIRFSG_ATTRIBUTE_IQ_OUT_PORT_TEMPERATURE = 1150161;
  NIRFSG_ATTRIBUTE_RF_BLANKING_SOURCE = 1150162;
  NIRFSG_ATTRIBUTE_IQ_OUT_PORT_LOAD_IMPEDANCE = 1150163;
  NIRFSG_ATTRIBUTE_ANALOG_MODULATION_FM_NARROWBAND_INTEGRATOR = 1150165;
  NIRFSG_ATTRIBUTE_ANALOG_MODULATION_FM_SENSITIVITY = 1150166;
  NIRFSG_ATTRIBUTE_ANALOG_MODULATION_AM_SENSITIVITY = 1150167;
  NIRFSG_ATTRIBUTE_ANALOG_MODULATION_PM_SENSITIVITY = 1150168;
  NIRFSG_ATTRIBUTE_ATTENUATOR_SETTING = 1150173;
  NIRFSG_ATTRIBUTE_CONFIGURATION_LIST_IS_DONE = 1150175;
  NIRFSG_ATTRIBUTE_SYNC_SAMPLE_CLOCK_MASTER = 1150180;
  NIRFSG_ATTRIBUTE_SYNC_SAMPLE_CLOCK_DIST_LINE = 1150181;
  NIRFSG_ATTRIBUTE_AE_TEMPERATURE = 1150182;
  NIRFSG_ATTRIBUTE_AMP_PATH = 1150185;
  NIRFSG_ATTRIBUTE_FPGA_BITFILE_PATH = 1150186;
  NIRFSG_ATTRIBUTE_FAST_TUNING_OPTION = 1150188;
  NIRFSG_ATTRIBUTE_PULSE_MODULATION_MODE = 1150190;
  NIRFSG_ATTRIBUTE_ANALOG_MODULATION_FM_BAND = 1150191;
  NIRFSG_ATTRIBUTE_ANALOG_MODULATION_PM_MODE = 1150192;
  NIRFSG_ATTRIBUTE_CONFIGURATION_SETTLED_EVENT_TERMINAL_NAME = 1150194;
  NIRFSG_ATTRIBUTE_ALC_CONTROL = 1150195;
  NIRFSG_ATTRIBUTE_AUTO_POWER_SEARCH = 1150196;
  NIRFSG_ATTRIBUTE_LO_FREQUENCY = 1150199;
  NIRFSG_ATTRIBUTE_ARB_DIGITAL_GAIN = 1150204;
  NIRFSG_ATTRIBUTE_MARKER_EVENT_OUTPUT_BEHAVIOR = 1150206;
  NIRFSG_ATTRIBUTE_MARKER_EVENT_PULSE_WIDTH = 1150207;
  NIRFSG_ATTRIBUTE_MARKER_EVENT_PULSE_WIDTH_UNITS = 1150208;
  NIRFSG_ATTRIBUTE_MARKER_EVENT_TOGGLE_INITIAL_STATE = 1150209;
  NIRFSG_ATTRIBUTE_MODULE_POWER_CONSUMPTION = 1150210;
  NIRFSG_ATTRIBUTE_FPGA_TEMPERATURE = 1150211;
  NIRFSG_ATTRIBUTE_TEMPERATURE_READ_INTERVAL = 1150212;
  NIRFSG_ATTRIBUTE_P2P_IS_FINITE_GENERATION = 1150217;
  NIRFSG_ATTRIBUTE_P2P_NUMBER_OF_SAMPLES_TO_GENERATE = 1150218;
  NIRFSG_ATTRIBUTE_P2P_GENERATION_FIFO_SAMPLE_QUANTUM = 1150219;
  NIRFSG_ATTRIBUTE_RELATIVE_DELAY = 1150220;
  NIRFSG_ATTRIBUTE_ABSOLUTE_DELAY = 1150225;
  NIRFSG_ATTRIBUTE_DEVICE_INSTANTANEOUS_BANDWIDTH = 1150226;
  NIRFSG_ATTRIBUTE_OVERFLOW_ERROR_REPORTING = 1150228;
  NIRFSG_ATTRIBUTE_HOST_DMA_BUFFER_SIZE = 1150239;
  NIRFSG_ATTRIBUTE_SELECTED_PORTS = 1150241;
  NIRFSG_ATTRIBUTE_LO_OUT_EXPORT_CONFIGURE_FROM_RFSA = 1150242;
  NIRFSG_ATTRIBUTE_RF_IN_LO_EXPORT_ENABLED = 1150243;
  NIRFSG_ATTRIBUTE_THERMAL_CORRECTION_TEMPERATURE_RESOLUTION = 1150244;
  NIRFSG_ATTRIBUTE_UPCONVERTER_FREQUENCY_OFFSET_MODE = 1150248;
  NIRFSG_ATTRIBUTE_AVAILABLE_PORTS = 1150249;
  NIRFSG_ATTRIBUTE_FPGA_TARGET_NAME = 1150251;
  NIRFSG_ATTRIBUTE_DEEMBEDDING_TYPE = 1150252;
  NIRFSG_ATTRIBUTE_DEEMBEDDING_SELECTED_TABLE = 1150253;
  NIRFSG_ATTRIBUTE_LO_VCO_FREQUENCY_STEP_SIZE = 1150257;
  NIRFSG_ATTRIBUTE_THERMAL_CORRECTION_HEADROOM_RANGE = 1150258;
  NIRFSG_ATTRIBUTE_WAVEFORM_IQ_RATE = 1150263;
  NIRFSG_ATTRIBUTE_WAVEFORM_SIGNAL_BANDWIDTH = 1150264;
  NIRFSG_ATTRIBUTE_WAVEFORM_RUNTIME_SCALING = 1150265;
  NIRFSG_ATTRIBUTE_WAVEFORM_PAPR = 1150266;
  NIRFSG_ATTRIBUTE_FIXED_GROUP_DELAY_ACROSS_PORTS = 1150271;
  NIRFSG_ATTRIBUTE_WAVEFORM_FILEPATH = 1150272;
  NIRFSG_ATTRIBUTE_WRITE_WAVEFORM_BURST_DETECTION = 1150273;
  NIRFSG_ATTRIBUTE_WRITE_WAVEFORM_BURST_DETECTION_MODE = 1150274;
  NIRFSG_ATTRIBUTE_WRITE_WAVEFORM_BURST_DETECTION_MINIMUM_QUIET_TIME = 1150275;
  NIRFSG_ATTRIBUTE_WRITE_WAVEFORM_BURST_DETECTION_POWER_THRESHOLD = 1150276;
  NIRFSG_ATTRIBUTE_WRITE_WAVEFORM_BURST_DETECTION_MINIMUM_BURST_TIME = 1150277;
  NIRFSG_ATTRIBUTE_WAVEFORM_RF_BLANKING = 1150278;
  NIRFSG_ATTRIBUTE_DEEMBEDDING_COMPENSATION_GAIN = 1150289;
  NIRFSG_ATTRIBUTE_LOAD_CONFIGURATIONS_FROM_FILE_LOAD_OPTIONS = 1150290;
  NIRFSG_ATTRIBUTE_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS = 1150291;
  NIRFSG_ATTRIBUTE_EXPORTED_REF_CLOCK_RATE = 1150292;
  NIRFSG_ATTRIBUTE_WRITE_WAVEFORM_NORMALIZATION = 1150293;
  NIRFSG_ATTRIBUTE_WAVEFORM_WAVEFORM_SIZE = 1150297;
  NIRFSG_ATTRIBUTE_PULSE_MODULATION_ACTIVE_LEVEL = 1150307;
  NIRFSG_ATTRIBUTE_PULSE_MODULATION_SOURCE = 1150308;
  NIRFSG_ATTRIBUTE_EXPORTED_PULSE_MODULATION_EVENT_OUTPUT_TERMINAL = 1150309;
  NIRFSG_ATTRIBUTE_EXPORTED_PULSE_MODULATION_EVENT_ACTIVE_LEVEL = 1150310;
  NIRFSG_ATTRIBUTE_SELECTED_PATH = 1150311;
  NIRFSG_ATTRIBUTE_AVAILABLE_PATHS = 1150312;
  NIRFSG_ATTRIBUTE_COMPENSATE_FOR_FILTER_GROUP_DELAY = 1152832;
  NIRFSG_ATTRIBUTE_UPCONVERTER_GAIN = 1154097;
  NIRFSG_ATTRIBUTE_UPCONVERTER_CENTER_FREQUENCY = 1154098;
  NIRFSG_ATTRIBUTE_FREQUENCY = 1250001;
  NIRFSG_ATTRIBUTE_POWER_LEVEL = 1250002;
  NIRFSG_ATTRIBUTE_OUTPUT_ENABLED = 1250004;
  NIRFSG_ATTRIBUTE_PULSE_MODULATION_ENABLED = 1250051;
  NIRFSG_ATTRIBUTE_REF_CLOCK_RATE = 1250322;
  NIRFSG_ATTRIBUTE_IQ_ENABLED = 1250401;
  NIRFSG_ATTRIBUTE_IQ_NOMINAL_VOLTAGE = 1250402;
  NIRFSG_ATTRIBUTE_IQ_SWAP_ENABLED = 1250404;
  NIRFSG_ATTRIBUTE_ARB_SELECTED_WAVEFORM = 1250451;
  NIRFSG_ATTRIBUTE_IQ_RATE = 1250452;
  NIRFSG_ATTRIBUTE_ARB_FILTER_FREQUENCY = 1250453;
  NIRFSG_ATTRIBUTE_ARB_MAX_NUMBER_WAVEFORMS = 1250454;
  NIRFSG_ATTRIBUTE_ARB_WAVEFORM_QUANTUM = 1250455;
  NIRFSG_ATTRIBUTE_ARB_WAVEFORM_SIZE_MIN = 1250456;
  NIRFSG_ATTRIBUTE_ARB_WAVEFORM_SIZE_MAX = 1250457;
  NIRFSG_ATTRIBUTE_START_TRIGGER_TYPE = 1250458;
  NIRFSG_ATTRIBUTE_DIGITAL_EDGE_START_TRIGGER_EDGE = 1250459;
}

enum DigitalEdgeConfigurationListStepTriggerSource {
  DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_UNSPECIFIED = 0;
  DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PFI0 = 1;
  DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PFI1 = 2;
  DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PFI2 = 3;
  DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PFI3 = 4;
  DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PXI_TRIG0 = 5;
  DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PXI_TRIG1 = 6;
  DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PXI_TRIG2 = 7;
  DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PXI_TRIG3 = 8;
  DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PXI_TRIG4 = 9;
  DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PXI_TRIG5 = 10;
  DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PXI_TRIG6 = 11;
  DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PXI_TRIG7 = 12;
  DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PXI_STAR = 13;
  DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_MARKER0_EVENT = 14;
  DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_MARKER1_EVENT = 15;
  DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_MARKER2_EVENT = 16;
  DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_MARKER3_EVENT = 17;
  DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_TIMER_EVENT = 18;
  DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_TRIG_IN = 19;
}

enum DigitalEdgeEdge {
  DIGITAL_EDGE_EDGE_RISING_EDGE = 0;
  DIGITAL_EDGE_EDGE_FALLING_EDGE = 1;
}

enum DigitalEdgeScriptTriggerIdentifier {
  DIGITAL_EDGE_SCRIPT_TRIGGER_IDENTIFIER_UNSPECIFIED = 0;
  DIGITAL_EDGE_SCRIPT_TRIGGER_IDENTIFIER_SCRIPT_TRIGGER0 = 1;
  DIGITAL_EDGE_SCRIPT_TRIGGER_IDENTIFIER_SCRIPT_TRIGGER1 = 2;
  DIGITAL_EDGE_SCRIPT_TRIGGER_IDENTIFIER_SCRIPT_TRIGGER2 = 3;
  DIGITAL_EDGE_SCRIPT_TRIGGER_IDENTIFIER_SCRIPT_TRIGGER3 = 4;
}

enum DigitalLevelActiveLevel {
  DIGITAL_LEVEL_ACTIVE_LEVEL_UNSPECIFIED = 0;
  DIGITAL_LEVEL_ACTIVE_LEVEL_ACTIVE_HIGH = 9000;
  DIGITAL_LEVEL_ACTIVE_LEVEL_ACTIVE_LOW = 9001;
}

enum GenerationMode {
  GENERATION_MODE_UNSPECIFIED = 0;
  GENERATION_MODE_CW = 1000;
  GENERATION_MODE_ARB_WAVEFORM = 1001;
  GENERATION_MODE_SCRIPT = 1002;
}

enum LinearInterpolationFormat {
  LINEAR_INTERPOLATION_FORMAT_UNSPECIFIED = 0;
  LINEAR_INTERPOLATION_FORMAT_REAL_AND_IMAGINARY = 26000;
  LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_AND_PHASE = 26001;
  LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_DB_AND_PHASE = 26002;
}

enum Module {
  MODULE_UNSPECIFIED = 0;
  MODULE_PRIMARY_MODULE = 13000;
  MODULE_AWG = 13001;
  MODULE_LO = 13002;
}

enum OutputSignal {
  OUTPUT_SIGNAL_UNSPECIFIED = 0;
  OUTPUT_SIGNAL_DO_NOT_EXPORT = 1;
  OUTPUT_SIGNAL_PFI0 = 2;
  OUTPUT_SIGNAL_PFI1 = 3;
  OUTPUT_SIGNAL_PFI4 = 4;
  OUTPUT_SIGNAL_PFI5 = 5;
  OUTPUT_SIGNAL_PXI_STAR = 6;
  OUTPUT_SIGNAL_PXI_TRIG0 = 7;
  OUTPUT_SIGNAL_PXI_TRIG1 = 8;
  OUTPUT_SIGNAL_PXI_TRIG2 = 9;
  OUTPUT_SIGNAL_PXI_TRIG3 = 10;
  OUTPUT_SIGNAL_PXI_TRIG4 = 11;
  OUTPUT_SIGNAL_PXI_TRIG5 = 12;
  OUTPUT_SIGNAL_PXI_TRIG6 = 13;
  OUTPUT_SIGNAL_REF_OUT2 = 14;
  OUTPUT_SIGNAL_REF_OUT = 15;
  OUTPUT_SIGNAL_TRIG_OUT = 16;
}

enum PXIChassisClk10 {
  PXI_CHASSIS_CLK10_UNSPECIFIED = 0;
  PXI_CHASSIS_CLK10_NONE = 1;
  PXI_CHASSIS_CLK10_ONBOARD_CLOCK = 2;
  PXI_CHASSIS_CLK10_REF_IN = 3;
}

enum PowerLevelType {
  POWER_LEVEL_TYPE_UNSPECIFIED = 0;
  POWER_LEVEL_TYPE_AVERAGE_POWER = 7000;
  POWER_LEVEL_TYPE_PEAK_POWER = 7001;
}

enum RefClockSource {
  REF_CLOCK_SOURCE_UNSPECIFIED = 0;
  REF_CLOCK_SOURCE_ONBOARD_CLOCK = 1;
  REF_CLOCK_SOURCE_REF_IN = 2;
  REF_CLOCK_SOURCE_PXI_CLK = 3;
  REF_CLOCK_SOURCE_CLK_IN = 4;
  REF_CLOCK_SOURCE_REF_IN_2 = 5;
  REF_CLOCK_SOURCE_PXI_CLK_MASTER = 6;
}

enum RelativeTo {
  RELATIVE_TO_UNSPECIFIED = 0;
  RELATIVE_TO_START_OF_WAVEFORM = 8000;
  RELATIVE_TO_CURRENT_POSITION = 8001;
}

enum ResetWithOptionsStepsToOmit {
  RESET_WITH_OPTIONS_STEPS_TO_OMIT_NONE = 0;
  RESET_WITH_OPTIONS_STEPS_TO_OMIT_WAVEFORMS = 1;
  RESET_WITH_OPTIONS_STEPS_TO_OMIT_SCRIPTS = 2;
  RESET_WITH_OPTIONS_STEPS_TO_OMIT_ROUTES = 4;
  RESET_WITH_OPTIONS_STEPS_TO_OMIT_DEEMBEDDING_TABLES = 8;
}

enum RoutedSignal {
  ROUTED_SIGNAL_START_TRIGGER = 0;
  ROUTED_SIGNAL_CONFIGURATION_LIST_STEP_TRIGGER = 6;
  ROUTED_SIGNAL_CONFIGURATION_SETTLED_EVENT = 7;
  ROUTED_SIGNAL_DONE_EVENT = 5;
  ROUTED_SIGNAL_MARKER_EVENT = 2;
  ROUTED_SIGNAL_REF_CLOCK = 3;
  ROUTED_SIGNAL_SCRIPT_TRIGGER = 1;
  ROUTED_SIGNAL_STARTED_EVENT = 4;
}

enum SParameterOrientation {
  S_PARAMETER_ORIENTATION_UNSPECIFIED = 0;
  S_PARAMETER_ORIENTATION_PORT1_TOWARDS_DUT = 24000;
  S_PARAMETER_ORIENTATION_PORT2_TOWARDS_DUT = 24001;
}

enum SelfCalibrateRangeStepsToOmit {
  SELF_CALIBRATE_RANGE_STEPS_TO_OMIT_OMIT_NONE = 0;
  SELF_CALIBRATE_RANGE_STEPS_TO_OMIT_LO_SELF_CAL = 1;
  SELF_CALIBRATE_RANGE_STEPS_TO_OMIT_POWER_LEVEL_ACCURACY = 2;
  SELF_CALIBRATE_RANGE_STEPS_TO_OMIT_RESIDUAL_LO_POWER = 4;
  SELF_CALIBRATE_RANGE_STEPS_TO_OMIT_IMAGE_SUPPRESSION = 8;
  SELF_CALIBRATE_RANGE_STEPS_TO_OMIT_SYNTHESIZER_ALIGNMENT = 16;
}

enum SignalIdentifier {
  SIGNAL_IDENTIFIER_UNSPECIFIED = 0;
  SIGNAL_IDENTIFIER_NONE = 1;
  SIGNAL_IDENTIFIER_SCRIPT_TRIGGER0 = 2;
  SIGNAL_IDENTIFIER_SCRIPT_TRIGGER1 = 3;
  SIGNAL_IDENTIFIER_SCRIPT_TRIGGER2 = 4;
  SIGNAL_IDENTIFIER_SCRIPT_TRIGGER3 = 5;
  SIGNAL_IDENTIFIER_MARKER0 = 6;
  SIGNAL_IDENTIFIER_MARKER1 = 7;
  SIGNAL_IDENTIFIER_MARKER2 = 8;
  SIGNAL_IDENTIFIER_MARKER3 = 9;
}

enum TriggerSource {
  TRIGGER_SOURCE_UNSPECIFIED = 0;
  TRIGGER_SOURCE_PFI0 = 1;
  TRIGGER_SOURCE_PFI1 = 2;
  TRIGGER_SOURCE_PFI2 = 3;
  TRIGGER_SOURCE_PFI3 = 4;
  TRIGGER_SOURCE_PXI_TRIG0 = 5;
  TRIGGER_SOURCE_PXI_TRIG1 = 6;
  TRIGGER_SOURCE_PXI_TRIG2 = 7;
  TRIGGER_SOURCE_PXI_TRIG3 = 8;
  TRIGGER_SOURCE_PXI_TRIG4 = 9;
  TRIGGER_SOURCE_PXI_TRIG5 = 10;
  TRIGGER_SOURCE_PXI_TRIG6 = 11;
  TRIGGER_SOURCE_PXI_TRIG7 = 12;
  TRIGGER_SOURCE_PXI_STAR = 13;
  TRIGGER_SOURCE_PXIE_DSTARB = 14;
  TRIGGER_SOURCE_SYNC_START_TRIGGER = 15;
  TRIGGER_SOURCE_SYNC_SCRIPT_TRIGGER = 16;
  TRIGGER_SOURCE_TRIG_IN = 17;
  TRIGGER_SOURCE_PULSE_IN = 18;
  TRIGGER_SOURCE_DIO0 = 19;
  TRIGGER_SOURCE_DIO1 = 20;
  TRIGGER_SOURCE_DIO2 = 21;
  TRIGGER_SOURCE_DIO3 = 22;
  TRIGGER_SOURCE_DIO4 = 23;
  TRIGGER_SOURCE_DIO5 = 24;
  TRIGGER_SOURCE_DIO6 = 25;
  TRIGGER_SOURCE_DIO7 = 26;
}

enum NiRFSGInt32AttributeValues {
  option allow_alias = true;
  NIRFSG_INT32_UNSPECIFIED = 0;
  NIRFSG_INT32_AMP_PATH_HIGH_POWER = 16000;
  NIRFSG_INT32_AMP_PATH_LOW_HARMONIC = 16001;
  NIRFSG_INT32_ANALOG_MODULATION_FM_BAND_NARROWBAND = 17000;
  NIRFSG_INT32_ANALOG_MODULATION_FM_BAND_WIDEBAND = 17001;
  NIRFSG_INT32_ANALOG_MODULATION_FM_NARROWBAND_INTEGRATOR_100_HZ_TO_1_KHZ = 18000;
  NIRFSG_INT32_ANALOG_MODULATION_FM_NARROWBAND_INTEGRATOR_1_KHZ_TO_10_KHZ = 18001;
  NIRFSG_INT32_ANALOG_MODULATION_FM_NARROWBAND_INTEGRATOR_10_KHZ_TO_100_KHZ = 18002;
  NIRFSG_INT32_ANALOG_MODULATION_PM_MODE_HIGH_DEVIATION = 19000;
  NIRFSG_INT32_ANALOG_MODULATION_PM_MODE_LOW_PHASE_NOISE = 19001;
  NIRFSG_INT32_ANALOG_MODULATION_TYPE_NONE = 0;
  NIRFSG_INT32_ANALOG_MODULATION_TYPE_FM = 2000;
  NIRFSG_INT32_ANALOG_MODULATION_TYPE_PM = 2001;
  NIRFSG_INT32_ANALOG_MODULATION_TYPE_AM = 2002;
  NIRFSG_INT32_ANALOG_MODULATION_WAVEFORM_TYPE_SINE = 3000;
  NIRFSG_INT32_ANALOG_MODULATION_WAVEFORM_TYPE_SQUARE = 3001;
  NIRFSG_INT32_ANALOG_MODULATION_WAVEFORM_TYPE_TRIANGLE = 3002;
  NIRFSG_INT32_ARB_FILTER_TYPE_NONE = 10000;
  NIRFSG_INT32_ARB_FILTER_TYPE_ROOT_RAISED_COSINE = 10001;
  NIRFSG_INT32_ARB_FILTER_TYPE_RAISED_COSINE = 10002;
  NIRFSG_INT32_ARB_ONBOARD_SAMPLE_CLOCK_MODE_HIGH_RESOLUTION = 6000;
  NIRFSG_INT32_ARB_ONBOARD_SAMPLE_CLOCK_MODE_DIVIDE_DOWN = 6001;
  NIRFSG_INT32_CONFIG_LIST_TRIGGER_DIG_EDGE_EDGE_RISING_EDGE = 0;
  NIRFSG_INT32_CONFIGURATION_LIST_REPEAT_CONFIGURATION_LIST_REPEAT_CONTINUOUS = 0;
  NIRFSG_INT32_CONFIGURATION_LIST_REPEAT_CONFIGURATION_LIST_REPEAT_SINGLE = 1;
  NIRFSG_INT32_DEEMBEDDING_TYPE_NONE = 25000;
  NIRFSG_INT32_DEEMBEDDING_TYPE_SCALAR = 25001;
  NIRFSG_INT32_DEEMBEDDING_TYPE_VECTOR = 25002;
  NIRFSG_INT32_DIGITAL_EDGE_EDGE_RISING_EDGE = 0;
  NIRFSG_INT32_DIGITAL_EDGE_EDGE_FALLING_EDGE = 1;
  NIRFSG_INT32_DIGITAL_LEVEL_ACTIVE_LEVEL_ACTIVE_HIGH = 9000;
  NIRFSG_INT32_DIGITAL_LEVEL_ACTIVE_LEVEL_ACTIVE_LOW = 9001;
  NIRFSG_INT32_DIGITAL_MODULATION_TYPE_NONE = 0;
  NIRFSG_INT32_DIGITAL_MODULATION_TYPE_FSK = 4000;
  NIRFSG_INT32_DIGITAL_MODULATION_TYPE_OOK = 4001;
  NIRFSG_INT32_DIGITAL_MODULATION_TYPE_PSK = 4002;
  NIRFSG_INT32_DIGITAL_MODULATION_WAVEFORM_TYPE_PRBS = 5000;
  NIRFSG_INT32_DIGITAL_MODULATION_WAVEFORM_TYPE_USER_DEFINED = 5001;
  NIRFSG_INT32_ENABLE_VALUES_DISABLE = 0;
  NIRFSG_INT32_ENABLE_VALUES_ENABLE = 1;
  NIRFSG_INT32_FREQUENCY_SETTLING_UNITS_TIME_AFTER_LOCK = 12000;
  NIRFSG_INT32_FREQUENCY_SETTLING_UNITS_TIME_AFTER_IO = 12001;
  NIRFSG_INT32_FREQUENCY_SETTLING_UNITS_PPM = 12002;
  NIRFSG_INT32_GENERATION_MODE_CW = 1000;
  NIRFSG_INT32_GENERATION_MODE_ARB_WAVEFORM = 1001;
  NIRFSG_INT32_GENERATION_MODE_SCRIPT = 1002;
  NIRFSG_INT32_IQ_OFFSET_UNITS_PERCENT = 11000;
  NIRFSG_INT32_IQ_OFFSET_UNITS_VOLTS = 11001;
  NIRFSG_INT32_IQ_OUT_PORT_TERM_CONFIG_DIFFERENTIAL = 15000;
  NIRFSG_INT32_IQ_OUT_PORT_TERM_CONFIG_SINGLE_ENDED = 15001;
  NIRFSG_INT32_LIST_STEP_TRIGGER_TYPE_NONE = 0;
  NIRFSG_INT32_LIST_STEP_TRIGGER_TYPE_DIGITAL_EDGE = 1;
  NIRFSG_INT32_LOAD_OPTIONS_SKIP_NONE = 0;
  NIRFSG_INT32_LOAD_OPTIONS_SKIP_WAVEFORMS = 1;
  NIRFSG_INT32_LOOP_BANDWIDTH_NARROW = 0;
  NIRFSG_INT32_LOOP_BANDWIDTH_MEDIUM = 1;
  NIRFSG_INT32_LOOP_BANDWIDTH_WIDE = 2;
  NIRFSG_INT32_MARKER_EVENT_OUTPUT_BEHAVIOR_PULSE = 23000;
  NIRFSG_INT32_MARKER_EVENT_OUTPUT_BEHAVIOR_TOGGLE = 23001;
  NIRFSG_INT32_MARKER_EVENT_PULSE_WIDTH_UNITS_SECONDS = 22000;
  NIRFSG_INT32_MARKER_EVENT_PULSE_WIDTH_UNITS_SAMPLE_CLOCK_PERIODS = 22001;
  NIRFSG_INT32_MARKER_EVENT_TOGGLE_INITIAL_STATE_DIGITAL_LOW = 21000;
  NIRFSG_INT32_MARKER_EVENT_TOGGLE_INITIAL_STATE_DIGITAL_HIGH = 21001;
  NIRFSG_INT32_OUTPUT_PORT_RF_OUT = 14000;
  NIRFSG_INT32_OUTPUT_PORT_IQ_OUT = 14001;
  NIRFSG_INT32_OUTPUT_PORT_CAL_OUT = 14002;
  NIRFSG_INT32_OUTPUT_PORT_I_ONLY = 14003;
  NIRFSG_INT32_OVERFLOW_ERROR_REPORTING_WARNING = 1301;
  NIRFSG_INT32_OVERFLOW_ERROR_REPORTING_DISABLED = 1302;
  NIRFSG_INT32_PPA_SCRIPT_INHERITANCE_EXACT_MATCH = 0;
  NIRFSG_INT32_PPA_SCRIPT_INHERITANCE_MINIMUM = 1;
  NIRFSG_INT32_PPA_SCRIPT_INHERITANCE_MAXIMUM = 2;
  NIRFSG_INT32_PHASE_CONTINUITY_DISABLE = 0;
  NIRFSG_INT32_PHASE_CONTINUITY_AUTO = -1;
  NIRFSG_INT32_PHASE_CONTINUITY_ENABLE = 1;
  NIRFSG_INT32_POWER_LEVEL_TYPE_AVERAGE_POWER = 7000;
  NIRFSG_INT32_POWER_LEVEL_TYPE_PEAK_POWER = 7001;
  NIRFSG_INT32_PULSE_MODULATION_MODE_OPTIMAL_MATCH = 20000;
  NIRFSG_INT32_PULSE_MODULATION_MODE_HIGH_ISOLATION = 20001;
  NIRFSG_INT32_RESET_OPTIONS_SKIP_NONE = 0;
  NIRFSG_INT32_RESET_OPTIONS_SKIP_WAVEFORMS = 1;
  NIRFSG_INT32_RESET_OPTIONS_SKIP_SCRIPTS = 2;
  NIRFSG_INT32_RESET_OPTIONS_SKIP_DEEMBEDING_TABLES = 8;
  NIRFSG_INT32_RF_IN_LO_EXPORT_ENABLED_DISABLE = 0;
  NIRFSG_INT32_RF_IN_LO_EXPORT_ENABLED_UNSPECIFIED = -2;
  NIRFSG_INT32_RF_IN_LO_EXPORT_ENABLED_ENABLE = 1;
  NIRFSG_INT32_SCRIPT_TRIGGER_TYPE_NONE = 0;
  NIRFSG_INT32_SCRIPT_TRIGGER_TYPE_DIGITAL_EDGE = 1;
  NIRFSG_INT32_SCRIPT_TRIGGER_TYPE_DIGITAL_LEVEL = 8000;
  NIRFSG_INT32_SCRIPT_TRIGGER_TYPE_SOFTWARE = 2;
  NIRFSG_INT32_START_TRIGGER_TYPE_NONE = 0;
  NIRFSG_INT32_START_TRIGGER_TYPE_DIGITAL_EDGE = 1;
  NIRFSG_INT32_START_TRIGGER_TYPE_SOFTWARE = 2;
  NIRFSG_INT32_START_TRIGGER_TYPE_P2_P_ENDPOINT_FULLNESS = 3;
  NIRFSG_INT32_UPCONVERTER_FREQUENCY_OFFSET_MODE_AUTO = -1;
  NIRFSG_INT32_UPCONVERTER_FREQUENCY_OFFSET_MODE_ENABLE = 1;
  NIRFSG_INT32_UPCONVERTER_FREQUENCY_OFFSET_MODE_USER_DEFINED = 5001;
  NIRFSG_INT32_WRITE_WAVEFORM_BURST_DETECTION_MODE_MANUAL = 0;
  NIRFSG_INT32_WRITE_WAVEFORM_BURST_DETECTION_MODE_AUTO = -1;
  NIRFSG_INT32_YIG_MAIN_COIL_SLOW = 0;
  NIRFSG_INT32_YIG_MAIN_COIL_FAST = 1;
}

enum NiRFSGReal64AttributeValues {
  NIRFSG_REAL64_UNSPECIFIED = 0;
  NIRFSG_REAL64_REF_CLOCK_RATE_10_MHZ = 10000000;
  NIRFSG_REAL64_REF_CLOCK_RATE_AUTO = -1;
}

enum NiRFSGStringAttributeValuesMapped {
  NIRFSG_STRING_MAPPED_UNSPECIFIED = 0;
  NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_DO_NOT_EXPORT = 1;
  NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PFI0 = 2;
  NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PFI1 = 3;
  NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PFI4 = 4;
  NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PFI5 = 5;
  NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PXI_TRIG0 = 6;
  NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PXI_TRIG1 = 7;
  NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PXI_TRIG2 = 8;
  NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PXI_TRIG3 = 9;
  NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PXI_TRIG4 = 10;
  NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PXI_TRIG5 = 11;
  NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PXI_TRIG6 = 12;
  NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PXIE_DSTARC = 13;
  NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_TRIG_OUT = 14;
  NIRFSG_STRING_ARB_SAMPLE_CLOCK_SOURCE_ONBOARD_CLOCK = 15;
  NIRFSG_STRING_ARB_SAMPLE_CLOCK_SOURCE_CLK_IN = 16;
  NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_DO_NOT_EXPORT = 17;
  NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PFI0 = 18;
  NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PFI1 = 19;
  NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PXI_TRIG0 = 20;
  NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PXI_TRIG1 = 21;
  NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PXI_TRIG2 = 22;
  NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PXI_TRIG3 = 23;
  NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PXI_TRIG4 = 24;
  NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PXI_TRIG5 = 25;
  NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PXI_TRIG6 = 26;
  NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PXIE_DSTARC = 27;
  NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_TRIG_OUT = 28;
  NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PFI0 = 29;
  NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PFI1 = 30;
  NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PXI_TRIG0 = 31;
  NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PXI_TRIG1 = 32;
  NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PXI_TRIG2 = 33;
  NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PXI_TRIG3 = 34;
  NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PXI_TRIG4 = 35;
  NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PXI_TRIG5 = 36;
  NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PXI_TRIG6 = 37;
  NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PXI_TRIG7 = 38;
  NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PXIE_DSTARB = 39;
  NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_MARKER0_EVENT = 40;
  NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_MARKER1_EVENT = 41;
  NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_MARKER2_EVENT = 42;
  NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_MARKER3_EVENT = 43;
  NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_TIMER_EVENT = 44;
  NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_TRIG_IN = 45;
  NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_DO_NOT_EXPORT = 46;
  NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_PXI_TRIG0 = 47;
  NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_PXI_TRIG1 = 48;
  NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_PXI_TRIG2 = 49;
  NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_PXI_TRIG3 = 50;
  NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_PXI_TRIG4 = 51;
  NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_PXI_TRIG5 = 52;
  NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_PXI_TRIG6 = 53;
  NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_PXIE_DSTARC = 54;
  NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_TRIG_OUT = 55;
  NIRFSG_STRING_LO_SOURCE_ONBOARD = 56;
  NIRFSG_STRING_LO_SOURCE_LO_IN = 57;
  NIRFSG_STRING_LO_SOURCE_SECONDARY = 58;
  NIRFSG_STRING_LO_SOURCE_SG_SA_SHARED = 59;
  NIRFSG_STRING_LO_SOURCE_AUTOMATIC_SG_SA_SHARED = 60;
  NIRFSG_STRING_PXI_CHASSIS_CLK10_NONE = 61;
  NIRFSG_STRING_PXI_CHASSIS_CLK10_ONBOARD_CLOCK = 62;
  NIRFSG_STRING_PXI_CHASSIS_CLK10_REF_IN = 63;
  NIRFSG_STRING_REF_CLOCK_OUTPUT_TERM_DO_NOT_EXPORT = 64;
  NIRFSG_STRING_REF_CLOCK_OUTPUT_TERM_REF_OUT = 65;
  NIRFSG_STRING_REF_CLOCK_OUTPUT_TERM_REF_OUT2 = 66;
  NIRFSG_STRING_REF_CLOCK_OUTPUT_TERM_CLK_OUT = 67;
  NIRFSG_STRING_REF_CLOCK_SOURCE_ONBOARD_CLOCK = 68;
  NIRFSG_STRING_REF_CLOCK_SOURCE_REF_IN = 69;
  NIRFSG_STRING_REF_CLOCK_SOURCE_PXI_CLK = 70;
  NIRFSG_STRING_REF_CLOCK_SOURCE_CLK_IN = 71;
  NIRFSG_STRING_REF_CLOCK_SOURCE_REF_IN_2 = 72;
  NIRFSG_STRING_REF_CLOCK_SOURCE_PXI_CLK_MASTER = 73;
  NIRFSG_STRING_TRIGGER_SOURCE_PFI0 = 74;
  NIRFSG_STRING_TRIGGER_SOURCE_PFI1 = 75;
  NIRFSG_STRING_TRIGGER_SOURCE_PFI2 = 76;
  NIRFSG_STRING_TRIGGER_SOURCE_PFI3 = 77;
  NIRFSG_STRING_TRIGGER_SOURCE_PXI_TRIG0 = 78;
  NIRFSG_STRING_TRIGGER_SOURCE_PXI_TRIG1 = 79;
  NIRFSG_STRING_TRIGGER_SOURCE_PXI_TRIG2 = 80;
  NIRFSG_STRING_TRIGGER_SOURCE_PXI_TRIG3 = 81;
  NIRFSG_STRING_TRIGGER_SOURCE_PXI_TRIG4 = 82;
  NIRFSG_STRING_TRIGGER_SOURCE_PXI_TRIG5 = 83;
  NIRFSG_STRING_TRIGGER_SOURCE_PXI_TRIG6 = 84;
  NIRFSG_STRING_TRIGGER_SOURCE_PXI_TRIG7 = 85;
  NIRFSG_STRING_TRIGGER_SOURCE_PXI_STAR = 86;
  NIRFSG_STRING_TRIGGER_SOURCE_PXIE_DSTARB = 87;
  NIRFSG_STRING_TRIGGER_SOURCE_SYNC_START_TRIGGER = 88;
  NIRFSG_STRING_TRIGGER_SOURCE_SYNC_SCRIPT_TRIGGER = 89;
  NIRFSG_STRING_TRIGGER_SOURCE_TRIG_IN = 90;
  NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_DIO0 = 91;
  NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_DIO1 = 92;
  NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_DIO2 = 93;
  NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_DIO3 = 94;
  NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_DIO4 = 95;
  NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_DIO5 = 96;
  NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_DIO6 = 97;
  NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_DIO7 = 98;
  NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_DIO0 = 99;
  NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_DIO1 = 100;
  NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_DIO2 = 101;
  NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_DIO3 = 102;
  NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_DIO4 = 103;
  NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_DIO5 = 104;
  NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_DIO6 = 105;
  NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_DIO7 = 106;
  NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_DIO0 = 107;
  NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_DIO1 = 108;
  NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_DIO2 = 109;
  NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_DIO3 = 110;
  NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_DIO4 = 111;
  NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_DIO5 = 112;
  NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_DIO6 = 113;
  NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_DIO7 = 114;
  NIRFSG_STRING_TRIGGER_SOURCE_PULSE_IN = 115;
  NIRFSG_STRING_TRIGGER_SOURCE_DIO0 = 116;
  NIRFSG_STRING_TRIGGER_SOURCE_DIO1 = 117;
  NIRFSG_STRING_TRIGGER_SOURCE_DIO2 = 118;
  NIRFSG_STRING_TRIGGER_SOURCE_DIO3 = 119;
  NIRFSG_STRING_TRIGGER_SOURCE_DIO4 = 120;
  NIRFSG_STRING_TRIGGER_SOURCE_DIO5 = 121;
  NIRFSG_STRING_TRIGGER_SOURCE_DIO6 = 122;
  NIRFSG_STRING_TRIGGER_SOURCE_DIO7 = 123;
}

message AbortRequest {
  nidevice_grpc.Session vi = 1;
}

message AbortResponse {
  int32 status = 1;
}

message AllocateArbWaveformRequest {
  nidevice_grpc.Session vi = 1;
  string waveform_name = 2;
  sint32 size_in_samples = 3;
}

message AllocateArbWaveformResponse {
  int32 status = 1;
}

message CheckAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiRFSGAttribute attribute_id = 3;
  bool value = 4;
}

message CheckAttributeViBooleanResponse {
  int32 status = 1;
}

message CheckAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiRFSGAttribute attribute_id = 3;
  oneof value_enum {
    NiRFSGInt32AttributeValues value = 4;
    sint32 value_raw = 5;
  }
}

message CheckAttributeViInt32Response {
  int32 status = 1;
}

message CheckAttributeViInt64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiRFSGAttribute attribute_id = 3;
  int64 value_raw = 4;
}

message CheckAttributeViInt64Response {
  int32 status = 1;
}

message CheckAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiRFSGAttribute attribute_id = 3;
  oneof value_enum {
    NiRFSGReal64AttributeValues value = 4;
    double value_raw = 5;
  }
}

message CheckAttributeViReal64Response {
  int32 status = 1;
}

message CheckAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiRFSGAttribute attribute_id = 3;
  nidevice_grpc.Session value = 4;
}

message CheckAttributeViSessionResponse {
  int32 status = 1;
}

message CheckAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiRFSGAttribute attribute_id = 3;
  oneof value_enum {
    NiRFSGStringAttributeValuesMapped value_mapped = 4;
    string value_raw = 5;
  }
}

message CheckAttributeViStringResponse {
  int32 status = 1;
}

message CheckGenerationStatusRequest {
  nidevice_grpc.Session vi = 1;
}

message CheckGenerationStatusResponse {
  int32 status = 1;
  bool is_done = 2;
}

message CheckIfConfigurationListExistsRequest {
  nidevice_grpc.Session vi = 1;
  string list_name = 2;
}

message CheckIfConfigurationListExistsResponse {
  int32 status = 1;
  bool list_exists = 2;
}

message CheckIfScriptExistsRequest {
  nidevice_grpc.Session vi = 1;
  string script_name = 2;
}

message CheckIfScriptExistsResponse {
  int32 status = 1;
  bool script_exists = 2;
}

message CheckIfWaveformExistsRequest {
  nidevice_grpc.Session vi = 1;
  string waveform_name = 2;
}

message CheckIfWaveformExistsResponse {
  int32 status = 1;
  bool waveform_exists = 2;
}

message ClearAllArbWaveformsRequest {
  nidevice_grpc.Session vi = 1;
}

message ClearAllArbWaveformsResponse {
  int32 status = 1;
}

message ClearArbWaveformRequest {
  nidevice_grpc.Session vi = 1;
  string name = 2;
}

message ClearArbWaveformResponse {
  int32 status = 1;
}

message ClearErrorRequest {
  nidevice_grpc.Session vi = 1;
}

message ClearErrorResponse {
  int32 status = 1;
}

message ClearSelfCalibrateRangeRequest {
  nidevice_grpc.Session vi = 1;
}

message ClearSelfCalibrateRangeResponse {
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

message ConfigureDeembeddingTableInterpolationLinearRequest {
  nidevice_grpc.Session vi = 1;
  string port = 2;
  string table_name = 3;
  oneof format_enum {
    LinearInterpolationFormat format = 4;
    sint32 format_raw = 5;
  }
}

message ConfigureDeembeddingTableInterpolationLinearResponse {
  int32 status = 1;
}

message ConfigureDeembeddingTableInterpolationNearestRequest {
  nidevice_grpc.Session vi = 1;
  string port = 2;
  string table_name = 3;
}

message ConfigureDeembeddingTableInterpolationNearestResponse {
  int32 status = 1;
}

message ConfigureDeembeddingTableInterpolationSplineRequest {
  nidevice_grpc.Session vi = 1;
  string port = 2;
  string table_name = 3;
}

message ConfigureDeembeddingTableInterpolationSplineResponse {
  int32 status = 1;
}

message ConfigureDigitalEdgeConfigurationListStepTriggerRequest {
  nidevice_grpc.Session vi = 1;
  oneof source_enum {
    DigitalEdgeConfigurationListStepTriggerSource source_mapped = 2;
    string source_raw = 3;
  }
  oneof edge_enum {
    DigitalEdgeEdge edge = 4;
    sint32 edge_raw = 5;
  }
}

message ConfigureDigitalEdgeConfigurationListStepTriggerResponse {
  int32 status = 1;
}

message ConfigureDigitalEdgeScriptTriggerRequest {
  nidevice_grpc.Session vi = 1;
  oneof trigger_id_enum {
    DigitalEdgeScriptTriggerIdentifier trigger_id_mapped = 2;
    string trigger_id_raw = 3;
  }
  oneof source_enum {
    TriggerSource source_mapped = 4;
    string source_raw = 5;
  }
  oneof edge_enum {
    DigitalEdgeEdge edge = 6;
    sint32 edge_raw = 7;
  }
}

message ConfigureDigitalEdgeScriptTriggerResponse {
  int32 status = 1;
}

message ConfigureDigitalEdgeStartTriggerRequest {
  nidevice_grpc.Session vi = 1;
  oneof source_enum {
    TriggerSource source_mapped = 2;
    string source_raw = 3;
  }
  oneof edge_enum {
    DigitalEdgeEdge edge = 4;
    sint32 edge_raw = 5;
  }
}

message ConfigureDigitalEdgeStartTriggerResponse {
  int32 status = 1;
}

message ConfigureDigitalLevelScriptTriggerRequest {
  nidevice_grpc.Session vi = 1;
  oneof trigger_id_enum {
    DigitalEdgeScriptTriggerIdentifier trigger_id_mapped = 2;
    string trigger_id_raw = 3;
  }
  oneof source_enum {
    TriggerSource source_mapped = 4;
    string source_raw = 5;
  }
  oneof level_enum {
    DigitalLevelActiveLevel level = 6;
    sint32 level_raw = 7;
  }
}

message ConfigureDigitalLevelScriptTriggerResponse {
  int32 status = 1;
}

message ConfigureDigitalModulationUserDefinedWaveformRequest {
  nidevice_grpc.Session vi = 1;
  bytes user_defined_waveform = 2;
}

message ConfigureDigitalModulationUserDefinedWaveformResponse {
  int32 status = 1;
}

message ConfigureGenerationModeRequest {
  nidevice_grpc.Session vi = 1;
  oneof generation_mode_enum {
    GenerationMode generation_mode = 2;
    sint32 generation_mode_raw = 3;
  }
}

message ConfigureGenerationModeResponse {
  int32 status = 1;
}

message ConfigureOutputEnabledRequest {
  nidevice_grpc.Session vi = 1;
  bool output_enabled = 2;
}

message ConfigureOutputEnabledResponse {
  int32 status = 1;
}

message ConfigureP2PEndpointFullnessStartTriggerRequest {
  nidevice_grpc.Session vi = 1;
  int64 p2p_endpoint_fullness_level = 2;
}

message ConfigureP2PEndpointFullnessStartTriggerResponse {
  int32 status = 1;
}

message ConfigurePXIChassisClk10Request {
  nidevice_grpc.Session vi = 1;
  oneof pxi_clk10_source_enum {
    PXIChassisClk10 pxi_clk10_source_mapped = 2;
    string pxi_clk10_source_raw = 3;
  }
}

message ConfigurePXIChassisClk10Response {
  int32 status = 1;
}

message ConfigurePowerLevelTypeRequest {
  nidevice_grpc.Session vi = 1;
  oneof power_level_type_enum {
    PowerLevelType power_level_type = 2;
    sint32 power_level_type_raw = 3;
  }
}

message ConfigurePowerLevelTypeResponse {
  int32 status = 1;
}

message ConfigureRFRequest {
  nidevice_grpc.Session vi = 1;
  double frequency = 2;
  double power_level = 3;
}

message ConfigureRFResponse {
  int32 status = 1;
}

message ConfigureRefClockRequest {
  nidevice_grpc.Session vi = 1;
  oneof ref_clock_source_enum {
    RefClockSource ref_clock_source_mapped = 2;
    string ref_clock_source_raw = 3;
  }
  double ref_clock_rate = 4;
}

message ConfigureRefClockResponse {
  int32 status = 1;
}

message ConfigureSignalBandwidthRequest {
  nidevice_grpc.Session vi = 1;
  double signal_bandwidth = 2;
}

message ConfigureSignalBandwidthResponse {
  int32 status = 1;
}

message ConfigureSoftwareScriptTriggerRequest {
  nidevice_grpc.Session vi = 1;
  oneof trigger_id_enum {
    DigitalEdgeScriptTriggerIdentifier trigger_id_mapped = 2;
    string trigger_id_raw = 3;
  }
}

message ConfigureSoftwareScriptTriggerResponse {
  int32 status = 1;
}

message ConfigureSoftwareStartTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message ConfigureSoftwareStartTriggerResponse {
  int32 status = 1;
}

message ConfigureUpconverterPLLSettlingTimeRequest {
  nidevice_grpc.Session vi = 1;
  double pll_settling_time = 2;
  bool ensure_pll_locked = 3;
}

message ConfigureUpconverterPLLSettlingTimeResponse {
  int32 status = 1;
}

message CreateConfigurationListRequest {
  nidevice_grpc.Session vi = 1;
  string list_name = 2;
  repeated NiRFSGAttribute configuration_list_attributes = 3;
  bool set_as_active_list = 4;
}

message CreateConfigurationListResponse {
  int32 status = 1;
}

message CreateConfigurationListStepRequest {
  nidevice_grpc.Session vi = 1;
  bool set_as_active_step = 2;
}

message CreateConfigurationListStepResponse {
  int32 status = 1;
}

message CreateDeembeddingSparameterTableArrayRequest {
  nidevice_grpc.Session vi = 1;
  string port = 2;
  string table_name = 3;
  repeated double frequencies = 4;
  repeated nidevice_grpc.NIComplexNumber sparameter_table = 5;
  sint32 number_of_ports = 6;
  oneof sparameter_orientation_enum {
    SParameterOrientation sparameter_orientation = 7;
    sint32 sparameter_orientation_raw = 8;
  }
}

message CreateDeembeddingSparameterTableArrayResponse {
  int32 status = 1;
}

message CreateDeembeddingSparameterTableS2PFileRequest {
  nidevice_grpc.Session vi = 1;
  string port = 2;
  string table_name = 3;
  string s2p_file_path = 4;
  oneof sparameter_orientation_enum {
    SParameterOrientation sparameter_orientation = 5;
    sint32 sparameter_orientation_raw = 6;
  }
}

message CreateDeembeddingSparameterTableS2PFileResponse {
  int32 status = 1;
}

message DeleteAllDeembeddingTablesRequest {
  nidevice_grpc.Session vi = 1;
}

message DeleteAllDeembeddingTablesResponse {
  int32 status = 1;
}

message DeleteConfigurationListRequest {
  nidevice_grpc.Session vi = 1;
  string list_name = 2;
}

message DeleteConfigurationListResponse {
  int32 status = 1;
}

message DeleteDeembeddingTableRequest {
  nidevice_grpc.Session vi = 1;
  string port = 2;
  string table_name = 3;
}

message DeleteDeembeddingTableResponse {
  int32 status = 1;
}

message DeleteScriptRequest {
  nidevice_grpc.Session vi = 1;
  string script_name = 2;
}

message DeleteScriptResponse {
  int32 status = 1;
}

message DisableRequest {
  nidevice_grpc.Session vi = 1;
}

message DisableResponse {
  int32 status = 1;
}

message DisableAllModulationRequest {
  nidevice_grpc.Session vi = 1;
}

message DisableAllModulationResponse {
  int32 status = 1;
}

message DisableConfigurationListStepTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message DisableConfigurationListStepTriggerResponse {
  int32 status = 1;
}

message DisableScriptTriggerRequest {
  nidevice_grpc.Session vi = 1;
  oneof trigger_id_enum {
    DigitalEdgeScriptTriggerIdentifier trigger_id_mapped = 2;
    string trigger_id_raw = 3;
  }
}

message DisableScriptTriggerResponse {
  int32 status = 1;
}

message DisableStartTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message DisableStartTriggerResponse {
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

message ExportSignalRequest {
  nidevice_grpc.Session vi = 1;
  oneof signal_enum {
    RoutedSignal signal = 2;
    sint32 signal_raw = 3;
  }
  oneof signal_identifier_enum {
    SignalIdentifier signal_identifier_mapped = 4;
    string signal_identifier_raw = 5;
  }
  oneof output_terminal_enum {
    OutputSignal output_terminal_mapped = 6;
    string output_terminal_raw = 7;
  }
}

message ExportSignalResponse {
  int32 status = 1;
}

message GetAllNamedWaveformNamesRequest {
  nidevice_grpc.Session vi = 1;
}

message GetAllNamedWaveformNamesResponse {
  int32 status = 1;
  string waveform_names = 2;
  sint32 actual_buffer_size = 3;
}

message GetAllScriptNamesRequest {
  nidevice_grpc.Session vi = 1;
}

message GetAllScriptNamesResponse {
  int32 status = 1;
  string script_names = 2;
  sint32 actual_buffer_size = 3;
}

message GetScriptRequest {
  nidevice_grpc.Session vi = 1;
  string script_name = 2;
}

message GetScriptResponse {
  int32 status = 1;
  string script = 2;
  sint32 actual_buffer_size = 3;
}

message GetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiRFSGAttribute attribute_id = 3;
}

message GetAttributeViBooleanResponse {
  int32 status = 1;
  bool value = 2;
}

message GetAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiRFSGAttribute attribute_id = 3;
}

message GetAttributeViInt32Response {
  int32 status = 1;
  sint32 value = 2;
}

message GetAttributeViInt64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiRFSGAttribute attribute_id = 3;
}

message GetAttributeViInt64Response {
  int32 status = 1;
  int64 value = 2;
}

message GetAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiRFSGAttribute attribute_id = 3;
}

message GetAttributeViReal64Response {
  int32 status = 1;
  double value = 2;
}

message GetAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiRFSGAttribute attribute_id = 3;
}

message GetAttributeViSessionResponse {
  int32 status = 1;
  nidevice_grpc.Session value = 2;
}

message GetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiRFSGAttribute attribute_id = 3;
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

message GetDeembeddingSparametersRequest {
  nidevice_grpc.Session vi = 1;
}

message GetDeembeddingSparametersResponse {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexNumber sparameters = 2;
  sint32 number_of_sparameters = 3;
  sint32 number_of_ports = 4;
}

message GetErrorRequest {
  nidevice_grpc.Session vi = 1;
}

message GetErrorResponse {
  int32 status = 1;
  sint32 error_code = 2;
  string error_description = 3;
}

message GetExternalCalibrationLastDateAndTimeRequest {
  nidevice_grpc.Session vi = 1;
}

message GetExternalCalibrationLastDateAndTimeResponse {
  int32 status = 1;
  sint32 year = 2;
  sint32 month = 3;
  sint32 day = 4;
  sint32 hour = 5;
  sint32 minute = 6;
  sint32 second = 7;
}

message GetMaxSettablePowerRequest {
  nidevice_grpc.Session vi = 1;
}

message GetMaxSettablePowerResponse {
  int32 status = 1;
  double value = 2;
}

message GetSelfCalibrationDateAndTimeRequest {
  nidevice_grpc.Session vi = 1;
  oneof module_enum {
    Module module = 2;
    sint32 module_raw = 3;
  }
}

message GetSelfCalibrationDateAndTimeResponse {
  int32 status = 1;
  sint32 year = 2;
  sint32 month = 3;
  sint32 day = 4;
  sint32 hour = 5;
  sint32 minute = 6;
  sint32 second = 7;
}

message GetSelfCalibrationTemperatureRequest {
  nidevice_grpc.Session vi = 1;
  oneof module_enum {
    Module module = 2;
    sint32 module_raw = 3;
  }
}

message GetSelfCalibrationTemperatureResponse {
  int32 status = 1;
  double temperature = 2;
}

message GetTerminalNameRequest {
  nidevice_grpc.Session vi = 1;
  oneof signal_enum {
    RoutedSignal signal = 2;
    sint32 signal_raw = 3;
  }
  oneof signal_identifier_enum {
    SignalIdentifier signal_identifier_mapped = 4;
    string signal_identifier_raw = 5;
  }
}

message GetTerminalNameResponse {
  int32 status = 1;
  string terminal_name = 2;
}

message GetUserDataRequest {
  nidevice_grpc.Session vi = 1;
  string identifier = 2;
}

message GetUserDataResponse {
  int32 status = 1;
  bytes data = 2;
  sint32 actual_data_size = 3;
}

message GetWaveformBurstStartLocationsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message GetWaveformBurstStartLocationsResponse {
  int32 status = 1;
  repeated double locations = 2;
  sint32 required_size = 3;
}

message GetWaveformBurstStopLocationsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message GetWaveformBurstStopLocationsResponse {
  int32 status = 1;
  repeated double locations = 2;
  sint32 required_size = 3;
}

message GetWaveformMarkerEventLocationsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message GetWaveformMarkerEventLocationsResponse {
  int32 status = 1;
  repeated double locations = 2;
  sint32 required_size = 3;
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
  nidevice_grpc.Session new_vi = 2;
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

message LoadConfigurationsFromFileRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string file_path = 3;
}

message LoadConfigurationsFromFileResponse {
  int32 status = 1;
}

message PerformPowerSearchRequest {
  nidevice_grpc.Session vi = 1;
}

message PerformPowerSearchResponse {
  int32 status = 1;
}

message PerformThermalCorrectionRequest {
  nidevice_grpc.Session vi = 1;
}

message PerformThermalCorrectionResponse {
  int32 status = 1;
}

message QueryArbWaveformCapabilitiesRequest {
  nidevice_grpc.Session vi = 1;
}

message QueryArbWaveformCapabilitiesResponse {
  int32 status = 1;
  sint32 max_number_waveforms = 2;
  sint32 waveform_quantum = 3;
  sint32 min_waveform_size = 4;
  sint32 max_waveform_size = 5;
}

message ReadAndDownloadWaveformFromFileTDMSRequest {
  nidevice_grpc.Session vi = 1;
  string waveform_name = 2;
  string file_path = 3;
  uint32 waveform_index = 4;
}

message ReadAndDownloadWaveformFromFileTDMSResponse {
  int32 status = 1;
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
  NiRFSGAttribute attribute_id = 3;
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

message ResetWithDefaultsRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetWithDefaultsResponse {
  int32 status = 1;
}

message ResetWithOptionsRequest {
  nidevice_grpc.Session vi = 1;
  oneof steps_to_omit_enum {
    ResetWithOptionsStepsToOmit steps_to_omit = 2;
    uint64 steps_to_omit_raw = 3;
  }
}

message ResetWithOptionsResponse {
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

message SaveConfigurationsToFileRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string file_path = 3;
}

message SaveConfigurationsToFileResponse {
  int32 status = 1;
}

message SelectArbWaveformRequest {
  nidevice_grpc.Session vi = 1;
  string name = 2;
}

message SelectArbWaveformResponse {
  int32 status = 1;
}

message SelfCalRequest {
  nidevice_grpc.Session vi = 1;
}

message SelfCalResponse {
  int32 status = 1;
}

message SelfCalibrateRangeRequest {
  nidevice_grpc.Session vi = 1;
  oneof steps_to_omit_enum {
    SelfCalibrateRangeStepsToOmit steps_to_omit = 2;
    int64 steps_to_omit_raw = 3;
  }
  double min_frequency = 4;
  double max_frequency = 5;
  double min_power_level = 6;
  double max_power_level = 7;
}

message SelfCalibrateRangeResponse {
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

message SendSoftwareEdgeTriggerRequest {
  nidevice_grpc.Session vi = 1;
  oneof trigger_enum {
    RoutedSignal trigger = 2;
    sint32 trigger_raw = 3;
  }
  oneof trigger_identifier_enum {
    SignalIdentifier trigger_identifier_mapped = 4;
    string trigger_identifier_raw = 5;
  }
}

message SendSoftwareEdgeTriggerResponse {
  int32 status = 1;
}

message SetArbWaveformNextWritePositionRequest {
  nidevice_grpc.Session vi = 1;
  string waveform_name = 2;
  oneof relative_to_enum {
    RelativeTo relative_to = 3;
    sint32 relative_to_raw = 4;
  }
  sint32 offset = 5;
}

message SetArbWaveformNextWritePositionResponse {
  int32 status = 1;
}

message SetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiRFSGAttribute attribute_id = 3;
  bool value = 4;
}

message SetAttributeViBooleanResponse {
  int32 status = 1;
}

message SetAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiRFSGAttribute attribute_id = 3;
  oneof value_enum {
    NiRFSGInt32AttributeValues value = 4;
    sint32 value_raw = 5;
  }
}

message SetAttributeViInt32Response {
  int32 status = 1;
}

message SetAttributeViInt64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiRFSGAttribute attribute_id = 3;
  int64 value_raw = 4;
}

message SetAttributeViInt64Response {
  int32 status = 1;
}

message SetAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiRFSGAttribute attribute_id = 3;
  oneof value_enum {
    NiRFSGReal64AttributeValues value = 4;
    double value_raw = 5;
  }
}

message SetAttributeViReal64Response {
  int32 status = 1;
}

message SetAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiRFSGAttribute attribute_id = 3;
  nidevice_grpc.Session value = 4;
}

message SetAttributeViSessionResponse {
  int32 status = 1;
}

message SetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiRFSGAttribute attribute_id = 3;
  oneof value_enum {
    NiRFSGStringAttributeValuesMapped value_mapped = 4;
    string value_raw = 5;
  }
}

message SetAttributeViStringResponse {
  int32 status = 1;
}

message SetUserDataRequest {
  nidevice_grpc.Session vi = 1;
  string identifier = 2;
  bytes data = 3;
}

message SetUserDataResponse {
  int32 status = 1;
}

message SetWaveformBurstStartLocationsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  repeated double locations = 3;
}

message SetWaveformBurstStartLocationsResponse {
  int32 status = 1;
}

message SetWaveformBurstStopLocationsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  repeated double locations = 3;
}

message SetWaveformBurstStopLocationsResponse {
  int32 status = 1;
}

message SetWaveformMarkerEventLocationsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  repeated double locations = 3;
}

message SetWaveformMarkerEventLocationsResponse {
  int32 status = 1;
}

message WaitUntilSettledRequest {
  nidevice_grpc.Session vi = 1;
  sint32 max_time_milliseconds = 2;
}

message WaitUntilSettledResponse {
  int32 status = 1;
}

message WriteArbWaveformRequest {
  nidevice_grpc.Session vi = 1;
  string waveform_name = 2;
  repeated double i_data = 3;
  repeated double q_data = 4;
  bool more_data_pending = 5;
}

message WriteArbWaveformResponse {
  int32 status = 1;
}

message WriteArbWaveformComplexF32Request {
  nidevice_grpc.Session vi = 1;
  string waveform_name = 2;
  repeated nidevice_grpc.NIComplexNumberF32 wfm_data = 3;
  bool more_data_pending = 4;
}

message WriteArbWaveformComplexF32Response {
  int32 status = 1;
}

message WriteArbWaveformComplexF64Request {
  nidevice_grpc.Session vi = 1;
  string waveform_name = 2;
  repeated nidevice_grpc.NIComplexNumber wfm_data = 3;
  bool more_data_pending = 4;
}

message WriteArbWaveformComplexF64Response {
  int32 status = 1;
}

message WriteArbWaveformComplexI16Request {
  nidevice_grpc.Session vi = 1;
  string waveform_name = 2;
  repeated nidevice_grpc.NIComplexI16 wfm_data = 3;
}

message WriteArbWaveformComplexI16Response {
  int32 status = 1;
}

message WriteArbWaveformF32Request {
  nidevice_grpc.Session vi = 1;
  string waveform_name = 2;
  repeated float i_data = 3;
  repeated float q_data = 4;
  bool more_data_pending = 5;
}

message WriteArbWaveformF32Response {
  int32 status = 1;
}

message WriteScriptRequest {
  nidevice_grpc.Session vi = 1;
  string script = 2;
}

message WriteScriptResponse {
  int32 status = 1;
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nirfsg/nirfsg.mak sha256=dc04419d34183ed523d3c2e591ca0e96987ce3fbd9d353cfeaf97b8df20208b2 bytes=368 -->
## FILE: src/nirfsg/nirfsg.mak

- repository: `ni/nimi-python`
- source_path: `src/nirfsg/nirfsg.mak`
- sha256: `dc04419d34183ed523d3c2e591ca0e96987ce3fbd9d353cfeaf97b8df20208b2`
- bytes: 368

````makefile


include $(BUILD_HELPER_DIR)/defines.mak

MODULE_FILES_TO_GENERATE := $(DEFAULT_PY_FILES_TO_GENERATE) _complextype.py

MODULE_FILES_TO_COPY := $(DEFAULT_PY_FILES_TO_COPY)

RST_FILES_TO_GENERATE := $(DEFAULT_RST_FILES_TO_GENERATE)

SPHINX_CONF_PY := $(DEFAULT_SPHINX_CONF_PY)
READTHEDOCS_CONFIG := $(DEFAULT_READTHEDOCS_CONFIG)

include $(BUILD_HELPER_DIR)/rules.mak
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nirfsg/system_tests/grpc_server_config.json sha256=eee1e42d6f7aa2578848988eb1097f8370506d8ddda321a4de10b282b5530512 bytes=154 -->
## FILE: src/nirfsg/system_tests/grpc_server_config.json

- repository: `ni/nimi-python`
- source_path: `src/nirfsg/system_tests/grpc_server_config.json`
- sha256: `eee1e42d6f7aa2578848988eb1097f8370506d8ddda321a4de10b282b5530512`
- bytes: 154

````json
{
    "address": "[::1]",
    "port": 31766,
    "security" : {
       "server_cert": "",
       "server_key": "",
       "root_cert": ""
    }
 }
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nirfsg/system_tests/samples2pfile.s2p sha256=cd3e855a3390c4935fe3c86c20202aa89e5bf495bc63dc611402b9a7147cd686 bytes=335 -->
## FILE: src/nirfsg/system_tests/samples2pfile.s2p

- repository: `ni/nimi-python`
- source_path: `src/nirfsg/system_tests/samples2pfile.s2p`
- sha256: `cd3e855a3390c4935fe3c86c20202aa89e5bf495bc63dc611402b9a7147cd686`
- bytes: 335

````text
! 2-port S-parameter file, four frequency points
# GHz S RI R 50.0
!freq RS11  IS11  RS21  AS21  MS12  AS12  MS22  AS22
0.500 1.0   0.0   1.0   0.0   1.0   0.0   1.0   0.0
1.000 2.0   0.0   2.0   0.0   2.0   0.0   2.0   0.0
2.000 3.0   0.0   3.0   0.0   3.0   0.0   3.0   0.0
6.000 4.0   0.0   4.0   0.0   4.0   0.0   4.0   0.0
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nirfsg/system_tests/test_system_nirfsg.py sha256=9ca0dcf1bdfb0b6718181171679a8a6a4775c33dc059adc5a7cd9af0185d5c30 bytes=38104 -->
## FILE: src/nirfsg/system_tests/test_system_nirfsg.py

- repository: `ni/nimi-python`
- source_path: `src/nirfsg/system_tests/test_system_nirfsg.py`
- sha256: `9ca0dcf1bdfb0b6718181171679a8a6a4775c33dc059adc5a7cd9af0185d5c30`
- bytes: 38104

````python
import array
import grpc
import hightime
import nirfsg
import numpy as np
import os
import pathlib
import pytest
import sys
import time


sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent / 'shared'))
import system_test_utilities  # noqa: E402

# Set up global information we need
test_files_base_dir = os.path.join(os.path.dirname(__file__))
use_simulated_session = True
real_hw_resource_name = '5841'


def get_test_file_path(file_name):
    return os.path.join(test_files_base_dir, file_name)


sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent / 'generated/nirfsg'))


class SystemTests:
    @pytest.fixture(scope='function')
    def rfsg_device_session(self, session_creation_kwargs):
        if use_simulated_session:
            with nirfsg.Session("5841sim", options="Simulate=1, DriverSetup=Model:5841", **session_creation_kwargs) as sim_5841_session:
                yield sim_5841_session
        else:
            with nirfsg.Session(real_hw_resource_name, **session_creation_kwargs) as real_rfsg_device_session:
                yield real_rfsg_device_session

    @pytest.fixture(scope='function')
    def simulated_5831_device_session(self, session_creation_kwargs):
        with nirfsg.Session("5831sim", options="Simulate=1, DriverSetup=Model:5831", **session_creation_kwargs) as sim_5831_session:
            yield sim_5831_session

# Attribute set and get related tests
    def test_get_float_attribute(self, rfsg_device_session):
        value = rfsg_device_session.power_level
        assert isinstance(value, float)

    def test_set_float_attribute(self, rfsg_device_session):
        rfsg_device_session.power_level = -3.0
        assert rfsg_device_session.power_level == -3.0

    def test_get_string_attribute(self, rfsg_device_session):
        model = rfsg_device_session.instrument_model
        assert model == "NI PXIe-5841"

    def test_get_list_of_strings_attribute(self, rfsg_device_session):
        models = rfsg_device_session.supported_instrument_models
        assert isinstance(models, list) and all(isinstance(model, str) for model in models)
        assert "NI PXIe-5841" in models

    def test_set_string_attribute(self, rfsg_device_session):
        rfsg_device_session.selected_script = "myScript"
        assert rfsg_device_session.selected_script == "myScript"

    def test_get_timedelta_attribute(self, rfsg_device_session):
        value = rfsg_device_session.external_calibration_recommended_interval
        assert isinstance(value, hightime.timedelta)

    def test_get_int32_attribute(self, rfsg_device_session):
        value = rfsg_device_session.arb_waveform_quantum
        assert isinstance(value, int)

    def test_set_int32_enum_attribute(self, rfsg_device_session):
        rfsg_device_session.frequency_settling_units = nirfsg.FrequencySettlingUnits.TIME_AFTER_LOCK
        assert rfsg_device_session.frequency_settling_units == nirfsg.FrequencySettlingUnits.TIME_AFTER_LOCK

    def test_set_invalid_attribute_raises(self, rfsg_device_session):
        with pytest.raises(AttributeError):
            rfsg_device_session.non_existent_attribute = 123

# Multi-threading related tests
    def test_multi_threading_lock_unlock(self, rfsg_device_session):
        system_test_utilities.impl_test_multi_threading_lock_unlock(rfsg_device_session)

    def test_multi_threading_ivi_synchronized_wrapper_releases_lock(self, rfsg_device_session):
        system_test_utilities.impl_test_multi_threading_ivi_synchronized_wrapper_releases_lock(rfsg_device_session.abort)

# Error handling related tests
    def test_error_message(self, session_creation_kwargs):
        try:
            with nirfsg.Session(resource_name="invalid_model", id_query=False, reset_device=False, options="Simulate=1, DriverSetup=Model:invalid_model", **session_creation_kwargs):
                assert False
        except nirfsg.Error as e:
            assert e.code == -1074135025
            assert "Invalid model in DriverSetup string" in e.description

    def test_get_error(self, rfsg_device_session):
        try:
            rfsg_device_session.instrument_model = ''
            assert False
        except nirfsg.Error as e:
            assert e.code == -1074135027
            assert "Attribute is read-only" in e.description

# Utility method tests
    def test_reset(self, rfsg_device_session):
        default_power_level = rfsg_device_session.power_level
        rfsg_device_session.power_level = default_power_level + 1.0
        assert rfsg_device_session.power_level == default_power_level + 1.0
        rfsg_device_session.reset()
        assert rfsg_device_session.power_level == default_power_level

    def test_reset_with_options(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        waveform_data = np.full(1000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform', waveform_data, False)
        default_power_level = rfsg_device_session.power_level
        rfsg_device_session.power_level = default_power_level + 1.0
        assert rfsg_device_session.power_level == default_power_level + 1.0
        steps_to_omit_without_waveforms = nirfsg.ResetWithOptionsStepsToOmit.ROUTES
        steps_to_omit_with_waveforms = nirfsg.ResetWithOptionsStepsToOmit.WAVEFORMS | nirfsg.ResetWithOptionsStepsToOmit.ROUTES
        rfsg_device_session.reset_with_options(steps_to_omit_with_waveforms)
        assert rfsg_device_session.power_level == default_power_level
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform')
        assert waveform_exists is True
        rfsg_device_session.reset_with_options(steps_to_omit_without_waveforms)
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform')
        assert waveform_exists is False

    def test_self_test(self, rfsg_device_session):
        # We should not get an assert if self_test passes
        rfsg_device_session.self_test()

    @pytest.mark.skipif(use_simulated_session is False, reason="Takes long time in real device")
    def test_self_cal(self, rfsg_device_session):
        rfsg_device_session.self_cal()

    @pytest.mark.skipif(use_simulated_session is False, reason="Takes long time in real device")
    def test_self_cal_range(self, rfsg_device_session):
        steps_to_omit = nirfsg.SelfCalibrateRangeStepsToOmit.LO_SELF_CAL | nirfsg.SelfCalibrateRangeStepsToOmit.IMAGE_SUPPRESSION
        rfsg_device_session.self_calibrate_range(steps_to_omit, 1e9, 2e9, -20, 0)

    def test_clear_self_calibrate_range(self, rfsg_device_session):
        rfsg_device_session.clear_self_calibrate_range()

    @pytest.mark.skipif(use_simulated_session is True, reason="Bad date returned by driver for simulated device")
    def test_get_ext_cal_last_date_and_time(self, rfsg_device_session):
        dt = rfsg_device_session.get_ext_cal_last_date_and_time()
        assert isinstance(dt, hightime.datetime)

    @pytest.mark.skipif(use_simulated_session is True, reason="Bad date returned by driver for simulated device")
    def test_get_self_cal_last_date_and_time(self, rfsg_device_session):
        dt = rfsg_device_session.get_self_cal_last_date_and_time(nirfsg.Module.PRIMARY_MODULE)
        assert isinstance(dt, hightime.datetime)

    def test_get_terminal_name(self, rfsg_device_session):
        terminal_name = rfsg_device_session.get_terminal_name(nirfsg.Signal.MARKER_EVENT, 'marker3')
        assert '/ao/0/Marker3Event' in terminal_name

    def test_query_arb_waveform_capabilities(self, rfsg_device_session):
        max_number_waveforms, waveform_quantum, min_waveform_size, max_waveform_size = rfsg_device_session.query_arb_waveform_capabilities()
        assert max_number_waveforms == 67108864
        assert waveform_quantum == 1
        assert min_waveform_size == 8
        assert max_waveform_size == 536870912

# Repeated capability tests
    def test_markers_rep_cap(self, rfsg_device_session):
        marker = rfsg_device_session.markers[0]
        requested_terminal_name = '/Dev0/PXI_Trig0'
        marker.exported_marker_event_output_terminal = requested_terminal_name
        assert marker.exported_marker_event_output_terminal == requested_terminal_name

    def test_script_triggers_rep_cap(self, rfsg_device_session):
        trigger = rfsg_device_session.script_triggers[0]
        requested_terminal_name = '/Dev0/PXI_Trig0'
        trigger.exported_script_trigger_output_terminal = requested_terminal_name
        assert trigger.exported_script_trigger_output_terminal == requested_terminal_name

    def test_waveforms_rep_cap(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        waveform_data = np.full(1000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform', waveform_data, False)
        requested_waveform_iq_rate = 1e6
        rfsg_device_session.waveforms['mywaveform'].waveform_iq_rate = requested_waveform_iq_rate
        assert rfsg_device_session.waveforms['mywaveform'].waveform_iq_rate == requested_waveform_iq_rate

    def test_ports_rep_cap(self, simulated_5831_device_session):
        requested_deembedding_type = nirfsg.DeembeddingType.SCALAR
        simulated_5831_device_session.ports['if1'].deembedding_type = requested_deembedding_type
        assert simulated_5831_device_session.ports['if1'].deembedding_type == requested_deembedding_type

    def test_los_rep_cap(self, simulated_5831_device_session):
        requested_lo_source = nirfsg.LoSource.SG_SA_SHARED
        simulated_5831_device_session.los[2].lo_source = requested_lo_source
        assert simulated_5831_device_session.los[2].lo_source == requested_lo_source

# Configuration methods related tests
    def test_configure_rf(self, rfsg_device_session):
        rfsg_device_session.configure_rf(2e9, -5.0)
        assert rfsg_device_session.power_level == -5.0
        assert rfsg_device_session.frequency == 2e9

    def test_write_arb_waveform_numpy_complex128(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        waveform_data = np.full(1000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform1', waveform_data, False)
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform1')
        assert waveform_exists is True
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform2')
        assert waveform_exists is False

    def test_write_arb_waveform_numpy_complex64(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        waveform_data = np.full(1600, 1 + 0j, dtype=np.complex64)
        rfsg_device_session.write_arb_waveform('mywaveform2', waveform_data, False)
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform2')
        assert waveform_exists is True
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform3')
        assert waveform_exists is False

    def test_write_arb_waveform_numpy_interleaved_int16(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        rfsg_device_session.power_level_type = nirfsg.PowerLevelType.PEAK  # Needed for writing unscaled int16 data
        waveform_data = np.array([1, 0] * 3000, dtype=np.int16)
        rfsg_device_session.write_arb_waveform('mywaveform3', waveform_data, False)
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform3')
        assert waveform_exists is True
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform1')
        assert waveform_exists is False

    def test_write_arb_waveform_with_wrong_datatype(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        waveform_data_wrong_numpy_type = np.array([1, 0] * 3000, dtype=np.int32)
        waveform_data_non_numpy_type = array.array('h', [1, 0] * 3000)
        try:
            rfsg_device_session.write_arb_waveform('mywaveform3', waveform_data_wrong_numpy_type, False)
            assert False
        except TypeError:
            pass
        try:
            rfsg_device_session.write_arb_waveform('mywaveform1', waveform_data_non_numpy_type, False)
            assert False
        except TypeError:
            pass

    def test_clear_arb_waveform(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        waveform_data = np.full(1000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform1', waveform_data, False)
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform1')
        assert waveform_exists is True
        rfsg_device_session.clear_arb_waveform('mywaveform1')
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform1')
        assert waveform_exists is False

    def test_clear_all_arb_waveforms(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        waveform_data = np.full(1000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform1', waveform_data, False)
        rfsg_device_session.write_arb_waveform('mywaveform2', waveform_data, False)
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform1')
        assert waveform_exists is True
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform2')
        assert waveform_exists is True
        rfsg_device_session.clear_all_arb_waveforms()
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform1')
        assert waveform_exists is False
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform2')
        assert waveform_exists is False

    def test_allocate_arb_waveform(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        rfsg_device_session.power_level_type = nirfsg.PowerLevelType.PEAK  # To be able to call write multiple times on same waveform
        waveform_data = np.full(1000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.allocate_arb_waveform('foo', len(waveform_data) * 2)
        rfsg_device_session.write_arb_waveform('foo', waveform_data, True)
        rfsg_device_session.write_arb_waveform('foo', waveform_data, False)

    def test_set_arb_waveform_next_write_position(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        rfsg_device_session.power_level_type = nirfsg.PowerLevelType.PEAK  # To be able to call write multiple times on same waveform
        waveform_data = np.full(1000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform1', waveform_data, True)
        rfsg_device_session.set_arb_waveform_next_write_position('mywaveform1', nirfsg.RelativeTo.START_OF_WAVEFORM, 500)
        waveform_data_new_second_half = np.full(500, 0 + 1j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform1', waveform_data_new_second_half, False)

    def test_set_get_burst_start_stop_locations(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        waveform_data = np.full(1000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform1', waveform_data, False)
        startlocations = [1, 100, 200]
        stoplocations = [50, 175, 750]
        rfsg_device_session.waveforms['mywaveform1'].set_waveform_burst_start_locations(startlocations)
        rfsg_device_session.waveforms['mywaveform1'].set_waveform_burst_stop_locations(stoplocations)
        startlocations_out = rfsg_device_session.waveforms['mywaveform1'].get_waveform_burst_start_locations()
        stoplocations_out = rfsg_device_session.waveforms['mywaveform1'].get_waveform_burst_stop_locations()
        assert startlocations_out == startlocations
        assert stoplocations_out == stoplocations

    def test_set_get_marker_event_locations(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        waveform_data = np.full(1000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform1', waveform_data, False)
        markerlocations = [1, 100, 200]
        rfsg_device_session.waveforms['mywaveform1'].markers[0].set_waveform_marker_event_locations(markerlocations)
        markerlocations_out = rfsg_device_session.waveforms['mywaveform1'].markers[0].get_waveform_marker_event_locations()
        assert markerlocations_out == markerlocations

    def test_write_script(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.SCRIPT
        waveform_data = np.full(1000, 0.707 + 0.707j, dtype=np.complex64)
        rfsg_device_session.write_arb_waveform('mywaveform1', waveform_data, False)
        script = '''script myScript1
        repeat forever
        generate mywaveform1
        end repeat
        end script'''
        rfsg_device_session.write_script(script)

    @pytest.mark.skipif(use_simulated_session is True, reason="Scripts not compiled on simulated device")
    def test_check_if_script_exists(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.SCRIPT
        waveform_data = np.full(1000, 0.707 + 0.707j, dtype=np.complex64)
        rfsg_device_session.write_arb_waveform('mywaveform1', waveform_data, False)
        script = '''script myScript1
        repeat forever
        generate mywaveform1
        end repeat
        end script'''
        rfsg_device_session.write_script(script)
        script_exists = rfsg_device_session.check_if_script_exists('myScript1')
        assert script_exists is True
        script_exists = rfsg_device_session.check_if_script_exists('myScript2')
        assert script_exists is False

    @pytest.mark.skipif(use_simulated_session is True, reason="Scripts not compiled on simulated device")
    def test_write_script_with_bad_script(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.SCRIPT
        script = '''script myScript1
        repeat forever
        generate mywaveform1
        end repeat
        end script'''
        try:
            rfsg_device_session.write_script(script)
            assert False
        except nirfsg.Error as e:
            assert e.code == -1074101603
            assert "A waveform matching the provided name does not exist in memory" in e.description

    @pytest.mark.skipif(use_simulated_session is True, reason="Scripts not compiled on simulated device")
    def test_get_script(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.SCRIPT
        waveform_data = np.full(1000, 0.707 + 0.707j, dtype=np.complex64)
        rfsg_device_session.write_arb_waveform('mywaveform1', waveform_data, False)
        script_content = '''script myScript1
        repeat forever
        generate mywaveform1
        end repeat
        end script'''
        rfsg_device_session.write_script(script_content)
        retrieved_script = rfsg_device_session.get_script('myScript1')
        assert retrieved_script == script_content

    @pytest.mark.skipif(use_simulated_session is True, reason="Scripts not compiled on simulated device")
    def test_delete_script(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.SCRIPT
        waveform_data = np.full(1000, 0.707 + 0.707j, dtype=np.complex64)
        rfsg_device_session.write_arb_waveform('mywaveform1', waveform_data, False)
        script = '''script myScript1
        repeat forever
        generate mywaveform1
        end repeat
        end script'''
        rfsg_device_session.write_script(script)
        script_exists = rfsg_device_session.check_if_script_exists('myScript1')
        assert script_exists is True
        rfsg_device_session.delete_script('myScript1')
        script_exists = rfsg_device_session.check_if_script_exists('myScript1')
        assert script_exists is False

    def test_configure_software_trigger(self, rfsg_device_session):
        rfsg_device_session.configure_software_start_trigger()
        assert rfsg_device_session.start_trigger_type == nirfsg.StartTriggerType.SOFTWARE
        rfsg_device_session.script_triggers[0].configure_software_script_trigger()
        assert rfsg_device_session.script_triggers[0].script_trigger_type == nirfsg.ScriptTriggerType.SOFTWARE

    def test_configure_digital_edge_trigger(self, rfsg_device_session):
        rfsg_device_session.configure_digital_edge_start_trigger('PXI_Trig1', nirfsg.StartTriggerDigitalEdgeEdge.RISING)
        rfsg_device_session.script_triggers[1].configure_digital_edge_script_trigger('PXI_Trig2', nirfsg.ScriptTriggerDigitalEdgeEdge.FALLING)
        assert rfsg_device_session.start_trigger_type == nirfsg.StartTriggerType.DIGITAL_EDGE
        assert rfsg_device_session.digital_edge_start_trigger_source == 'PXI_Trig1'
        assert rfsg_device_session.digital_edge_start_trigger_edge == nirfsg.StartTriggerDigitalEdgeEdge.RISING
        assert rfsg_device_session.script_triggers[1].script_trigger_type == nirfsg.ScriptTriggerType.DIGITAL_EDGE
        assert rfsg_device_session.script_triggers[1].digital_edge_script_trigger_source == 'PXI_Trig2'
        assert rfsg_device_session.script_triggers[1].digital_edge_script_trigger_edge == nirfsg.ScriptTriggerDigitalEdgeEdge.FALLING

    def test_disable_trigger(self, rfsg_device_session):
        rfsg_device_session.configure_software_start_trigger()
        assert rfsg_device_session.start_trigger_type == nirfsg.StartTriggerType.SOFTWARE
        rfsg_device_session.disable_start_trigger()
        assert rfsg_device_session.start_trigger_type == nirfsg.StartTriggerType.NONE
        rfsg_device_session.script_triggers[3].configure_software_script_trigger()
        assert rfsg_device_session.script_triggers[3].script_trigger_type == nirfsg.ScriptTriggerType.SOFTWARE
        rfsg_device_session.script_triggers[3].disable_script_trigger()
        assert rfsg_device_session.script_triggers[3].script_trigger_type == nirfsg.ScriptTriggerType.NONE

    @pytest.mark.skipif(use_simulated_session is True, reason="RoCo is not invoked for simulated device")
    def test_export_started_event_with_invalid_terminal(self, rfsg_device_session):
        try:
            rfsg_device_session.exported_started_event_output_terminal = 'InvalidTerminal'
            rfsg_device_session.commit()
            assert False
        except nirfsg.Error as e:
            assert e.code == -1074107490
            assert 'Destination terminal to be routed could not be found on the device' in e.description

    def test_save_load_configuration(self, rfsg_device_session):
        rfsg_device_session.configure_rf(2e9, -5.0)
        rfsg_device_session.iq_rate = 1e6
        rfsg_device_session.save_configurations_to_file(get_test_file_path('tempConfiguration.json'))
        assert os.path.exists(get_test_file_path('tempConfiguration.json'))
        rfsg_device_session.configure_rf(3e9, -15.0)
        rfsg_device_session.iq_rate = 2e6
        assert rfsg_device_session.frequency == 3e9
        assert rfsg_device_session.power_level == -15.0
        assert rfsg_device_session.iq_rate == 2e6
        rfsg_device_session.load_configurations_from_file(get_test_file_path('tempConfiguration.json'))
        assert rfsg_device_session.frequency == 2e9
        assert rfsg_device_session.power_level == -5.0
        assert rfsg_device_session.iq_rate == 1e6
        os.remove(get_test_file_path('tempConfiguration.json'))

# Basic tests for generation
    @pytest.mark.skipif(use_simulated_session is False, reason="Test executed with status check in real hw")
    def test_cw_generation(self, rfsg_device_session):
        rfsg_device_session.configure_rf(2e9, -5.0)
        with rfsg_device_session.initiate():
            rfsg_device_session.check_generation_status()

    @pytest.mark.skipif(use_simulated_session is True, reason="is_done is always True on simulated device")
    def test_cw_generation_with_status(self, rfsg_device_session):
        rfsg_device_session.configure_rf(2e9, -5.0)
        with rfsg_device_session.initiate():
            is_done = rfsg_device_session.check_generation_status()
            assert is_done is False  # is_done will never be True in CW mode

    def test_abort(self, rfsg_device_session):
        rfsg_device_session.configure_rf(2e9, -5.0)
        rfsg_device_session.initiate()
        rfsg_device_session.check_generation_status()
        rfsg_device_session.abort()

    @pytest.mark.skipif(use_simulated_session is True, reason="is_done is always True on simulated device")
    def test_abort_with_status(self, rfsg_device_session):
        rfsg_device_session.configure_rf(2e9, -5.0)
        with rfsg_device_session.initiate():
            is_done = rfsg_device_session.check_generation_status()
            assert is_done is False  # is_done will never be True in CW mode
        is_done = rfsg_device_session.check_generation_status()
        assert is_done is True  # is_done should now be True after aborting

    @pytest.mark.skipif(use_simulated_session is False, reason="Test executed with status check in real hw")
    def test_multiple_arb_waveform_generation(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        waveform_data1 = np.full(1000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform1', waveform_data1, False)
        waveform_data2 = np.full(8000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform2', waveform_data2, False)
        rfsg_device_session.arb_selected_waveform = 'mywaveform1'
        with rfsg_device_session.initiate():
            rfsg_device_session.check_generation_status()
        rfsg_device_session.arb_selected_waveform = 'mywaveform2'
        with rfsg_device_session.initiate():
            rfsg_device_session.check_generation_status()

    @pytest.mark.skipif(use_simulated_session is True, reason="is_done is always True on simulated device")
    def test_multiple_arb_waveform_generation_with_status(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        waveform_data1 = np.full(1000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform1', waveform_data1, False)
        waveform_data2 = np.full(8000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform2', waveform_data2, False)
        rfsg_device_session.arb_selected_waveform = 'mywaveform1'
        with rfsg_device_session.initiate():
            is_done = rfsg_device_session.check_generation_status()
            assert is_done is False  # is_done will never be True since we have not authored waveform_repeat_count
        rfsg_device_session.arb_selected_waveform = 'mywaveform2'
        with rfsg_device_session.initiate():
            is_done = rfsg_device_session.check_generation_status()
            assert is_done is False  # is_done will never be True since we have not authored waveform_repeat_count

    @pytest.mark.skipif(use_simulated_session is False, reason="Test executed with status check in real hw")
    def test_multiple_script_generation(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.SCRIPT
        waveform_data = np.full(2000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform', waveform_data, False)
        script0 = '''script myScript0
        repeat 1
        generate mywaveform
        end repeat
        end script'''
        script1 = '''script myScript1
        repeat forever
        generate mywaveform
        end repeat
        end script'''
        rfsg_device_session.write_script(script0)
        rfsg_device_session.write_script(script1)
        rfsg_device_session.selected_script = 'myScript0'
        with rfsg_device_session.initiate():
            rfsg_device_session.check_generation_status()
        rfsg_device_session.selected_script = 'myScript1'
        with rfsg_device_session.initiate():
            rfsg_device_session.check_generation_status()

    @pytest.mark.skipif(use_simulated_session is True, reason="is_done is always True on simulated device")
    def test_multiple_script_generation_with_status(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.SCRIPT
        waveform_data = np.full(2000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform', waveform_data, False)
        script0 = '''script myScript0
        repeat 1
        generate mywaveform
        end repeat
        end script'''
        script1 = '''script myScript1
        repeat forever
        generate mywaveform
        end repeat
        end script'''
        rfsg_device_session.write_script(script0)
        rfsg_device_session.write_script(script1)
        rfsg_device_session.selected_script = 'myScript0'
        with rfsg_device_session.initiate():
            time.sleep(2)
            is_done = rfsg_device_session.check_generation_status()
            assert is_done is True  # is_done will be True since we are repeating only once
        rfsg_device_session.selected_script = 'myScript1'
        with rfsg_device_session.initiate():
            is_done = rfsg_device_session.check_generation_status()
            assert is_done is False  # is_done will never be True since we are repeating forever

    def test_send_software_edge_trigger(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.SCRIPT
        waveform_data = np.full(2000, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('mywaveform', waveform_data, False)
        script0 = '''script myScript0
        wait until scriptTrigger0
        generate mywaveform
        end script'''
        rfsg_device_session.write_script(script0)
        rfsg_device_session.configure_software_start_trigger()
        rfsg_device_session.script_triggers[0].configure_software_script_trigger()
        with rfsg_device_session.initiate():
            rfsg_device_session.send_software_edge_trigger(nirfsg.SoftwareTriggerType.START, nirfsg.TriggerIdentifier.NONE)
            rfsg_device_session.send_software_edge_trigger(nirfsg.SoftwareTriggerType.SCRIPT, nirfsg.TriggerIdentifier.SCRIPT_TRIGGER0)

    @pytest.mark.skipif(sys.platform == "linux", reason="Function not supported on Linux OS")
    def test_create_deembedding_sparameter_table_s2p_file(self, rfsg_device_session):
        rfsg_device_session.create_deembedding_sparameter_table_s2p_file('', 'myTable1', get_test_file_path('samples2pfile.s2p'), nirfsg.SparameterOrientation.PORT2_TOWARDS_DUT)
        rfsg_device_session.create_deembedding_sparameter_table_s2p_file('', 'myTable2', get_test_file_path('samples2pfile.s2p'), nirfsg.SparameterOrientation.PORT1_TOWARDS_DUT)
        rfsg_device_session.configure_deembedding_table_interpolation_linear('', 'myTable1', nirfsg.Format.MAGNITUDE_AND_PHASE)
        rfsg_device_session.ports[''].deembedding_selected_table = 'myTable1'
        with rfsg_device_session.initiate():
            rfsg_device_session.check_generation_status()
        rfsg_device_session.delete_deembedding_table('', 'myTable1')
        rfsg_device_session.ports[''].deembedding_selected_table = 'myTable2'
        with rfsg_device_session.initiate():
            rfsg_device_session.check_generation_status()
        rfsg_device_session.delete_all_deembedding_tables()
        try:
            rfsg_device_session.commit()
            assert False
        except nirfsg.Error as e:
            assert e.code == -1074097772
            assert 'The specified de-embedding table cannot be found' in e.description
        rfsg_device_session.ports[''].deembedding_selected_table = ''
        with rfsg_device_session.initiate():
            rfsg_device_session.check_generation_status()

    def test_set_get_deembedding_sparameters(self, rfsg_device_session):
        frequencies = np.array([1e9, 2e9, 3e9], dtype=np.float64)
        sparameter_tables = np.array([[[1 + 1j, 2 + 2j], [3 + 3j, 4 + 4j]], [[5 + 5j, 6 + 6j], [7 + 7j, 8 + 8j]], [[9 + 9j, 10 + 10j], [11 + 11j, 12 + 12j]]], dtype=np.complex128)
        expected_sparameter_table = np.array([[5 + 5j, 6 + 6j], [7 + 7j, 8 + 8j]], dtype=np.complex128)
        rfsg_device_session.create_deembedding_sparameter_table_array('', 'myTable1', frequencies, sparameter_tables, nirfsg.SparameterOrientation.PORT2_TOWARDS_DUT)
        rfsg_device_session.frequency = 2e9
        returned_sparameter_table = rfsg_device_session.get_deembedding_sparameters()
        assert returned_sparameter_table.all() == expected_sparameter_table.all()

    def test_create_deembedding_sparameter_table_array_error_cases(self, rfsg_device_session):
        frequencies = np.array([1e9, 2e9, 3e9], dtype=np.float64)
        wrong_number_of_tables = np.full((2, 2, 2), 2.0 + 0.0j, dtype=np.complex128)
        wrong_table_size = np.full((3, 2, 3), 2.0 + 0.0j, dtype=np.complex128)
        wrong_array_dimensions = np.full((3, 2), 2.0 + 0.0j, dtype=np.complex128)
        try:
            rfsg_device_session.create_deembedding_sparameter_table_array('', 'myTable1', frequencies, wrong_number_of_tables, nirfsg.SparameterOrientation.PORT2_TOWARDS_DUT)
            assert False
        except ValueError as e:
            assert str(e) == 'Frequencies count does not match the sparameter table count. Frequencies count is 3 and sparameter table count is 2.'
        try:
            rfsg_device_session.create_deembedding_sparameter_table_array('', 'myTable1', frequencies, wrong_table_size, nirfsg.SparameterOrientation.PORT2_TOWARDS_DUT)
            assert False
        except ValueError as e:
            assert str(e) == 'Row and column count of sparameter table should be equal. Table row count is 2 and column count is 3.'
        try:
            rfsg_device_session.create_deembedding_sparameter_table_array('', 'myTable1', frequencies, wrong_array_dimensions, nirfsg.SparameterOrientation.PORT2_TOWARDS_DUT)
            assert False
        except ValueError as e:
            assert str(e) == 'Unsupported array dimension. Is 2, expected 3'

    def test_read_and_download_waveform_from_file_tdms(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        rfsg_device_session.read_and_download_waveform_from_file_tdms('mywaveform', get_test_file_path('ValidWaveformTDMSFile.tdms'), 0)
        waveform_exists = rfsg_device_session.check_if_waveform_exists('mywaveform')
        assert waveform_exists is True

    def test_wait_until_settled(self, rfsg_device_session):
        rfsg_device_session.configure_rf(2e9, -5.0)
        with rfsg_device_session.initiate():
            rfsg_device_session.wait_until_settled()

    @pytest.mark.skipif(use_simulated_session is True, reason="Scripts not compiled on simulated device")
    def test_get_all_script_names(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.SCRIPT
        waveform_data = np.full(1000, 0.707 + 0.707j, dtype=np.complex64)
        rfsg_device_session.write_arb_waveform('mywaveform', waveform_data, False)
        script1 = '''script myScript1
        repeat forever
        generate mywaveform
        end repeat
        end script'''
        script2 = '''script myScript2
        repeat forever
        generate mywaveform
        end repeat
        end script'''
        rfsg_device_session.write_script(script1)
        rfsg_device_session.write_script(script2)
        script_names = rfsg_device_session.get_all_script_names()
        assert 'myScript1' in script_names
        assert 'myScript2' in script_names


class TestLibrary(SystemTests):
    @pytest.fixture(scope='class')
    def session_creation_kwargs(self):
        return {}

    # grpc-device had a bug in get_all_named_waveform_names
    # (https://github.com/ni/grpc-device/pull/1243), which is now merged.
    # This test is temporarily kept in TestLibrary until the pipeline uses a
    # grpc-device version that includes this fix
    def test_get_all_named_waveform_names(self, rfsg_device_session):
        rfsg_device_session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        waveform_data1 = np.full(1000, 1 + 0j, dtype=np.complex128)
        waveform_data2 = np.full(800, 1 + 0j, dtype=np.complex128)
        rfsg_device_session.write_arb_waveform('waveform1', waveform_data1, False)
        rfsg_device_session.write_arb_waveform('waveform2', waveform_data2, False)
        names = rfsg_device_session.get_all_named_waveform_names()
        assert 'waveform1' in names
        assert 'waveform2' in names


@pytest.mark.skipif(sys.maxsize < 2**32, reason="gRPC tests not supported on 32-bit Python")
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
        grpc_options = nirfsg.GrpcSessionOptions(grpc_channel, "")
        return {'grpc_options': grpc_options}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nirfsg/templates/_grpc_stub_interpreter.py/get_deembedding_sparameter.py.mako sha256=5462992546bb85e0e228755a04dc4727d09feea28c81f9bcd40f8ed24ab417fa bytes=691 -->
## FILE: src/nirfsg/templates/_grpc_stub_interpreter.py/get_deembedding_sparameter.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nirfsg/templates/_grpc_stub_interpreter.py/get_deembedding_sparameter.py.mako`
- sha256: `5462992546bb85e0e228755a04dc4727d09feea28c81f9bcd40f8ed24ab417fa`
- bytes: 691

````mako
<%page args="f, config, method_template"/>\
<%
    '''Retrieves S-parameters from the gRPC call response and converts them to a reshaped numpy array.'''
    import build.helper as helper
%>\

    def ${f['interpreter_name']}(self):
        import numpy as np
        response = self._invoke(
            self._client.GetDeembeddingSparameters,
            grpc_types.GetDeembeddingSparametersRequest(vi=self._vi),
        )
        number_of_ports = response.number_of_ports
        sparameters = np.array([c.real + 1j * c.imaginary for c in response.sparameters], dtype=np.complex128)
        sparameters = sparameters.reshape((number_of_ports, number_of_ports))
        return sparameters
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nirfsg/templates/_library_interpreter.py/get_deembedding_sparameter.py.mako sha256=b930f3738e5706392e47781e65190ba1ef8dd60080ff673bc292a62ed2b673bb bytes=1490 -->
## FILE: src/nirfsg/templates/_library_interpreter.py/get_deembedding_sparameter.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nirfsg/templates/_library_interpreter.py/get_deembedding_sparameter.py.mako`
- sha256: `b930f3738e5706392e47781e65190ba1ef8dd60080ff673bc292a62ed2b673bb`
- bytes: 1490

````mako
<%page args="f, config, method_template"/>\
<%
    '''Gets S-parameters from the driver. Queries the number of ports, retrieves the S-parameter data into a pre-allocated buffer, and reshapes it.'''
    import build.helper as helper
%>\

    def ${f['interpreter_name']}(self):
        import numpy as np
        number_of_ports = self.get_deembedding_table_number_of_ports()
        sparameters_array_size = number_of_ports ** 2
        sparameters = np.full((number_of_ports, number_of_ports), 0 + 0j, dtype=np.complex128)
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        sparameters_ctype = _get_ctypes_pointer_for_buffer(value=sparameters, library_type=_complextype.NIComplexNumber)  # case B510
        sparameters_array_size_ctype = _visatype.ViInt32(sparameters_array_size)  # case S150
        number_of_sparameters_ctype = _visatype.ViInt32()  # case S220
        number_of_ports_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSG_GetDeembeddingSparameters(vi_ctype, sparameters_ctype, sparameters_array_size_ctype, None if number_of_sparameters_ctype is None else (ctypes.pointer(number_of_sparameters_ctype)), None if number_of_ports_ctype is None else (ctypes.pointer(number_of_ports_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        sparameters = sparameters.reshape((int(number_of_ports_ctype.value), int(number_of_ports_ctype.value)))
        return sparameters
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nirfsg/templates/session.py/create_deembedding_sparameter_table_array.py.mako sha256=13c60ef3ef0f02c0c660843b16eb73a0c051f8f2cc9698504d16da2774ec5bf1 bytes=1800 -->
## FILE: src/nirfsg/templates/session.py/create_deembedding_sparameter_table_array.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nirfsg/templates/session.py/create_deembedding_sparameter_table_array.py.mako`
- sha256: `13c60ef3ef0f02c0c660843b16eb73a0c051f8f2cc9698504d16da2774ec5bf1`
- bytes: 1800

````mako
<%page args="f, config, method_template"/>\
<%
    '''Ensures that incoming array has appropriate dimension sizes and calculates the number of ports and sparameter table size parameters based on array dimensions before calling into "create_deembedding_sparameter_table_array" method.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
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
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nirfsg/templates/session.py/write_arb_waveform.py.mako sha256=c6190880c9c5792741d765dd6c0cfb0d5f3cb30ac37e290fba681fcfc2a39910 bytes=1366 -->
## FILE: src/nirfsg/templates/session.py/write_arb_waveform.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nirfsg/templates/session.py/write_arb_waveform.py.mako`
- sha256: `c6190880c9c5792741d765dd6c0cfb0d5f3cb30ac37e290fba681fcfc2a39910`
- bytes: 1366

````mako
<%page args="f, config, method_template"/>\
<%
    '''Dispatches to the appropriate "write arb waveform" method based on the waveform type.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
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
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/custom_types/measurement_stats.py sha256=666cc48ad3ee3e5c4dc00b84f0100981f0d5ba0a52d1a9ad7cd2100567a22a6d bytes=1690 -->
## FILE: src/niscope/custom_types/measurement_stats.py

- repository: `ni/nimi-python`
- source_path: `src/niscope/custom_types/measurement_stats.py`
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

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/custom_types/waveform_info.py sha256=77e275741d5b86defd3ee729318ac3718f938c14873879b4b43f4636949c94ee bytes=6375 -->
## FILE: src/niscope/custom_types/waveform_info.py

- repository: `ni/nimi-python`
- source_path: `src/niscope/custom_types/waveform_info.py`
- sha256: `77e275741d5b86defd3ee729318ac3718f938c14873879b4b43f4636949c94ee`
- bytes: 6375

````python
import ctypes

import niscope._visatype


# This class is an internal implementation detail
# ctypes definition
# Name must match exactly what the name of the structure type is named in the C API.
class struct_niScope_wfmInfo(ctypes.Structure):  # noqa N801
    _pack_ = 8
    _fields_ = [
        ('absolute_initial_x', niscope._visatype.ViReal64),
        ('relative_initial_x', niscope._visatype.ViReal64),
        ('x_increment', niscope._visatype.ViReal64),
        ('actual_samples', niscope._visatype.ViInt32),
        ('offset', niscope._visatype.ViReal64),
        ('gain', niscope._visatype.ViReal64),
        ('reserved1', niscope._visatype.ViReal64),
        ('reserved2', niscope._visatype.ViReal64),
    ]

    def __init__(self, data=None, absolute_initial_x=0.0, relative_initial_x=0.0,
                 x_increment=0.0, actual_samples=0, offset=0.0, gain=0.0,
                 reserved1=0.0, reserved2=0.0):
        super(ctypes.Structure, self).__init__()
        if data is not None:
            self.absolute_initial_x = data.absolute_initial_x
            self.relative_initial_x = data.relative_initial_x
            self.x_increment = data.x_increment
            self.actual_samples = data.actual_samples
            self.offset = data.offset
            self.gain = data.gain
            self.reserved1 = data.reserved1
            self.reserved2 = data.reserved2
        else:
            self.absolute_initial_x = absolute_initial_x
            self.relative_initial_x = relative_initial_x
            self.x_increment = x_increment
            self.actual_samples = actual_samples
            self.offset = offset
            self.gain = gain
            self.reserved1 = reserved1
            self.reserved2 = reserved2


class WaveformInfo:
    def __init__(self, data=None, absolute_initial_x=0.0, relative_initial_x=0.0,
                 x_increment=0.0, offset=0.0, gain=0.0,
                 reserved1=0.0, reserved2=0.0):
        if data is not None:
            self.absolute_initial_x = data.absolute_initial_x
            self.relative_initial_x = data.relative_initial_x
            self.x_increment = data.x_increment
            self.offset = data.offset
            self.gain = data.gain
            self.reserved1 = data.reserved1
            self.reserved2 = data.reserved2
            self._actual_samples = data.actual_samples
        else:
            self.absolute_initial_x = absolute_initial_x
            self.relative_initial_x = relative_initial_x
            self.x_increment = x_increment
            self.offset = offset
            self.gain = gain
            self.reserved1 = reserved1
            self.reserved2 = reserved2
            # _actual_samples is only used to calculate the end of the waveform we extract from the
            # entire 1D array of samples. It is only filled in when calling into the niscope driver.
            self._actual_samples = None

        # Additional fields filled in during fetch or fetch_into
        self.channel = None
        self.record = None
        self.samples = None

    def __repr__(self):
        parameter_list = [
            f'absolute_initial_x={self.absolute_initial_x}',
            f'relative_initial_x={self.relative_initial_x}',
            f'x_increment={self.x_increment}',
            f'offset={self.offset}',
            f'gain={self.gain}'
        ]

        return '{}({})'.format(self.__class__.__name__, ', '.join(parameter_list))

    def __str__(self):
        # different format lines
        row_format_g = '{:<20}: {:,.6g}\n'
        row_format_d = '{:<20}: {:,}\n'
        row_format_s = '{:<20}: {:}\n'

        string_representation = ''
        if self.channel is not None:  # We explicitly look for not None to differentiate from empty string
            string_representation += row_format_s.format('Channel', self.channel)
        if self.record is not None:  # We explicitly look for not None to differentiate from 0
            string_representation += row_format_d.format('Record', self.record)

        string_representation += row_format_g.format('Absolute X0', self.absolute_initial_x)
        string_representation += row_format_g.format('Relative X0', self.relative_initial_x)
        string_representation += row_format_g.format('dt', self.x_increment)
        string_representation += row_format_g.format('Offset', self.offset)
        string_representation += row_format_g.format('Gain', self.gain)
        if self.samples is not None:  # We explicitly look for not None to differentiate from empty array
            string_representation += row_format_g.format('Waveform Length', len(self.samples))

        # Put possible private variable last
        if self._actual_samples is not None:  # We explicitly look for not None to differentiate from 0
            string_representation += row_format_d.format('_actual samples', self._actual_samples)

        return string_representation


def _populate_samples_info(waveform_infos, sample_data, num_samples_per_waveform):
    '''Chunk up flat array of sample_data and copy each chunk into individual WaveformInfo instance

    Args:
        waveform_infos (Iterable of WaveformInfo): WaveformInfo class instances

        sample_data (Iterable of float): Waveform sample data

        num_samples_per_waveform (int): Number of samples belonging to each waveform
    '''
    for i in range(len(waveform_infos)):
        start = i * num_samples_per_waveform
        end = start + waveform_infos[i]._actual_samples
        # We use the actual number of samples returned from the device to determine the end of the waveform.
        # We then remove it from waveform_info since the length of the waveform will tell us that information.
        waveform_infos[i]._actual_samples = None
        waveform_infos[i].samples = sample_data[start:end]


def _populate_channel_and_record_info(waveform_infos, channels, records):
    '''Populate the channel and record attributes of WaveformInfo instances

    Args:
        waveform_infos (Iterable of WaveformInfo): WaveformInfo class instances

        channels (Iterable of str): Channel names

        records (Iterable of int): Record numbers
    '''
    i = 0
    for record in records:
        for channel in channels:
            waveform_infos[i].channel = channel
            waveform_infos[i].record = record
            i += 1
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/examples/niscope_fetch.py sha256=d4eda26530a25debac27d4af3b72ab6fdffc757ed3bc2ee991e5f94d72232879 bytes=1906 -->
## FILE: src/niscope/examples/niscope_fetch.py

- repository: `ni/nimi-python`
- source_path: `src/niscope/examples/niscope_fetch.py`
- sha256: `d4eda26530a25debac27d4af3b72ab6fdffc757ed3bc2ee991e5f94d72232879`
- bytes: 1906

````python
#!/usr/bin/python

import argparse
import niscope
import pprint
import sys

pp = pprint.PrettyPrinter(indent=4, width=80)


def example(resource_name, channels, options, length, voltage):
    with niscope.Session(resource_name=resource_name, options=options) as session:
        session.configure_vertical(range=voltage, coupling=niscope.VerticalCoupling.AC)
        session.configure_horizontal_timing(min_sample_rate=50000000, min_num_pts=length, ref_position=50.0, num_records=1, enforce_realtime=True)
        with session.initiate():
            waveforms = session.channels[channels].fetch(num_samples=length)
        for i in range(len(waveforms)):
            print(f'Waveform {i} information:')
            print(str(waveforms[i]) + '\n\n')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Acquires one record from the given channels.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of an NI digitizer.')
    parser.add_argument('-c', '--channels', default='0', help='Channel(s) to use')
    parser.add_argument('-l', '--length', default=1000, type=int, help='Measure record length')
    parser.add_argument('-v', '--voltage', default=1.0, type=float, help='Voltage range (V)')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.channels, args.option_string, args.length, args.voltage)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5164', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', '0', options, 1000, 1.0)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/examples/niscope_fetch_forever.py sha256=558fa4bac6c1acee9ef0442bd17a35257cd6969c61f0d147c630abe6b1ddba72 bytes=3552 -->
## FILE: src/niscope/examples/niscope_fetch_forever.py

- repository: `ni/nimi-python`
- source_path: `src/niscope/examples/niscope_fetch_forever.py`
- sha256: `558fa4bac6c1acee9ef0442bd17a35257cd6969c61f0d147c630abe6b1ddba72`
- bytes: 3552

````python
#!/usr/bin/python

import argparse
import hightime
import niscope
import numpy as np
import pprint
import sys


pp = pprint.PrettyPrinter(indent=4, width=80)


# We use fetch_into which allows us to allocate a single buffer per channel and "fetch into" it a section at a time without having to
# reconstruct the waveform once we are done
def example(resource_name, options, total_acquisition_time_in_seconds, voltage, sample_rate_in_hz, samples_per_fetch):
    total_samples = int(total_acquisition_time_in_seconds * sample_rate_in_hz)
    # 1. Opening session
    with niscope.Session(resource_name=resource_name, options=options) as session:
        # We will acquire on all channels of the device
        channel_list = [c for c in range(session.channel_count)]  # Need an actual list and not a range

        # 2. Creating numpy arrays
        waveforms = [np.ndarray(total_samples, dtype=np.float64) for c in channel_list]

        # 3. Configuring
        session.configure_horizontal_timing(min_sample_rate=sample_rate_in_hz, min_num_pts=1, ref_position=0.0, num_records=1, enforce_realtime=True)
        session.channels[channel_list].configure_vertical(voltage, coupling=niscope.VerticalCoupling.DC, enabled=True)
        # Configure software trigger, but never send the trigger.
        # This starts an infinite acquisition, until you call session.abort() or session.close()
        session.configure_trigger_software()
        current_pos = 0
        # 4. initiating
        with session.initiate():
            while current_pos < total_samples:
                # We fetch each channel at a time so we don't have to de-interleave afterwards
                # We do not keep the wfm_info returned from fetch_into
                for channel, waveform in zip(channel_list, waveforms):
                    # 5. fetching - we return the slice of the waveform array that we want to "fetch into"
                    session.channels[channel].fetch_into(waveform[current_pos:current_pos + samples_per_fetch], relative_to=niscope.FetchRelativeTo.READ_POINTER,
                                                         offset=0, record_number=0, num_records=1, timeout=hightime.timedelta(seconds=5.0))
                current_pos += samples_per_fetch


def _main(argsv):
    parser = argparse.ArgumentParser(description='Fetch more samples than will fit in memory.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of an NI digitizer.')
    parser.add_argument('-t', '--time', default=10, type=int, help='Time to sample (s)')
    parser.add_argument('-v', '--voltage', default=1.0, type=float, help='Voltage range (V)')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    parser.add_argument('-r', '--sample-rate', default=1000.0, type=float, help='Sample Rate (Hz)')
    parser.add_argument('-s', '--samples-per-fetch', default=100, type=int, help='Samples per fetch')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.time, args.voltage, args.sample_rate, args.samples_per_fetch)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5164', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', options, 10, 1.0, 1000.0, 100)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/examples/niscope_fetch_into.py sha256=1ab090f2398174d632afdd4350f0a0fac2e1267ee7a4767083d22775f4d86dff bytes=2794 -->
## FILE: src/niscope/examples/niscope_fetch_into.py

- repository: `ni/nimi-python`
- source_path: `src/niscope/examples/niscope_fetch_into.py`
- sha256: `1ab090f2398174d632afdd4350f0a0fac2e1267ee7a4767083d22775f4d86dff`
- bytes: 2794

````python
#!/usr/bin/python

import argparse
import niscope
import numpy
import pprint
import sys

pp = pprint.PrettyPrinter(indent=4, width=80)


def example(resource_name, channels, options, length, voltage):
    # fetch_into() allows you to preallocate and reuse the destination of the fetched waveforms, which can result in better performance at the expense of the usability of fetch().
    channels = [ch.strip() for ch in channels.split(",")]
    num_channels = len(channels)
    num_records = 5
    total_num_wfms = num_channels * num_records
    # preallocate a single array for all samples in all waveforms
    # Supported array types are: numpy.float64, numpy.int8, numpy.int16, numpy.int32
    # int8, int16, int32 are for fetching unscaled data, which is the fastest way to fetch.
    # Gain and Offset are stored in the returned WaveformInfo objects and can be applied to the data by the user later.
    wfm = numpy.ndarray(length * total_num_wfms, dtype=numpy.float64)
    with niscope.Session(resource_name=resource_name, options=options) as session:
        session.configure_vertical(range=voltage, coupling=niscope.VerticalCoupling.AC)
        session.configure_horizontal_timing(min_sample_rate=50000000, min_num_pts=length, ref_position=50.0, num_records=num_records, enforce_realtime=True)
        with session.initiate():
            waveforms = session.channels[channels].fetch_into(waveform=wfm, num_records=num_records)
        for i in range(len(waveforms)):
            print(f'Waveform {i} information:')
            print(f'{waveforms[i]}\n\n')
            print(f'Samples: {waveforms[i].samples.tolist()}')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Fetches data directly into a preallocated numpy array.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of an NI digitizer.')
    parser.add_argument('-c', '--channels', default='0', help='Channel(s) to use')
    parser.add_argument('-l', '--length', default=100, type=int, help='Measure record length')
    parser.add_argument('-v', '--voltage', default=1.0, type=float, help='Voltage range (V)')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.channels, args.option_string, args.length, args.voltage)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5164', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', '0, 1', options, 100, 1.0)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/examples/niscope_read.py sha256=a1cc3be8a713e0345af9bbc5f161f8c5b1f491f62ab797e7556d7f7ebbc891c9 bytes=1868 -->
## FILE: src/niscope/examples/niscope_read.py

- repository: `ni/nimi-python`
- source_path: `src/niscope/examples/niscope_read.py`
- sha256: `a1cc3be8a713e0345af9bbc5f161f8c5b1f491f62ab797e7556d7f7ebbc891c9`
- bytes: 1868

````python
#!/usr/bin/python

import argparse
import niscope
import pprint
import sys

pp = pprint.PrettyPrinter(indent=4, width=80)


def example(resource_name, channels, options, length, voltage):
    with niscope.Session(resource_name=resource_name, options=options) as session:
        session.configure_vertical(range=voltage, coupling=niscope.VerticalCoupling.AC)
        session.configure_horizontal_timing(min_sample_rate=50000000, min_num_pts=length, ref_position=50.0, num_records=1, enforce_realtime=True)
        waveforms = session.channels[channels].read(num_samples=length)
        for i in range(len(waveforms)):
            print(f'Waveform {i} information:')
            print(str(waveforms[i]) + '\n\n')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Acquires one record from the given channels.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of an NI digitizer.')
    parser.add_argument('-c', '--channels', default='0', help='Channel(s) to use')
    parser.add_argument('-l', '--length', default=1000, type=int, help='Measure record length')
    parser.add_argument('-v', '--voltage', default=1.0, type=float, help='Voltage range (V)')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.channels, args.option_string, args.length, args.voltage)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5164', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', '0', options, 1000, 1.0)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/LATEST_RELEASE sha256=dd1b44562fc7c779fd9bef2e55d2e7b58783c4ca61885f5b549cd89de7e9a3fd bytes=7 -->
## FILE: src/niscope/LATEST_RELEASE

- repository: `ni/nimi-python`
- source_path: `src/niscope/LATEST_RELEASE`
- sha256: `dd1b44562fc7c779fd9bef2e55d2e7b58783c4ca61885f5b549cd89de7e9a3fd`
- bytes: 7

````text
1.4.9
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/metadata/__init__.py sha256=872d8093d28c53d452cef0cda3cb5cf21438e93c89ba24650a431194d1f57f45 bytes=1166 -->
## FILE: src/niscope/metadata/__init__.py

- repository: `ni/nimi-python`
- source_path: `src/niscope/metadata/__init__.py`
- sha256: `872d8093d28c53d452cef0cda3cb5cf21438e93c89ba24650a431194d1f57f45`
- bytes: 1166

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

if 'note' not in config['functions']['_init_function']['parameters'][3]:
    config['functions']['_init_function']['parameters'][3]['note'] = []
if not isinstance(config['functions']['_init_function']['parameters'][3]['note'], list):
    config['functions']['_init_function']['parameters'][3]['note'] = [config['functions']['_init_function']['parameters'][3]['note']]

config['functions']['_init_function']['parameters'][3]['note'].append(
'''
You can also use the option string to attach an accessory such as the NI 5900 to your digitizer session to allow the seamless use of the accessory: 

Options: { 'driver_setup': { 'Accessory': 'Dev1' } }
''')

__version__ = config['module_version']
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/metadata/attributes.py sha256=4993f766a8952674142676ad0c377fc271fbfd4c5a111e32ce19a22fb156b1c6 bytes=87441 -->
## FILE: src/niscope/metadata/attributes.py

- repository: `ni/nimi-python`
- source_path: `src/niscope/metadata/attributes.py`
- sha256: `4993f766a8952674142676ad0c377fc271fbfd4c5a111e32ce19a22fb156b1c6`
- bytes: 87441

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-SCOPE API metadata version 25.0.0f151
attributes = {
    1050005: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether or not to simulate instrument driver I/O operations.  If simulation is enabled, instrument driver functions perform range checking and call Ivi_GetAttribute and Ivi_SetAttribute functions, but they do not perform instrument I/O.  For output parameters that represent instrument data, the instrument driver functions return calculated values.\nThe default value is VI_FALSE.  Use the niScope_InitWithOptions function to override this value.\n'
        },
        'lv_property': 'Inherent IVI Attributes:User Options:Simulate',
        'name': 'SIMULATE',
        'type': 'ViBoolean'
    },
    1050203: {
        'access': 'read only',
        'documentation': {
            'description': '\nIndicates the number of channels that the specific instrument driver supports.\nFor channel-based properties, the IVI engine maintains a separate cache value for each channel.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Capabilities:Channel Count',
        'name': 'CHANNEL_COUNT',
        'type': 'ViInt32'
    },
    1050304: {
        'access': 'read only',
        'documentation': {
            'description': '\nIndicates the resource descriptor the driver uses to identify the physical device.  If you initialize the driver with a logical name, this attribute contains the resource descriptor that corresponds to the entry in the IVI Configuration utility.\nIf you initialize the instrument driver with the resource descriptor, this attribute contains that value.You can pass a logical name to niScope_Init or niScope_InitWithOptions. The IVI Configuration utility must contain an entry for the logical name. The logical name entry refers to a virtual instrument section in the IVI Configuration file. The virtual instrument section specifies a physical device and initial user options.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:Resource Descriptor',
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'type': 'ViString'
    },
    1050305: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string containing the logical name you specified when opening the current IVI session.  You can pass a logical name to niScope_Init or niScope_InitWithOptions. The IVI Configuration utility must contain an entry for the logical name. The logical name entry refers to a virtual instrument section in the IVI Configuration file. The virtual instrument section specifies a physical device and initial user options.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:Logical Name',
        'name': 'LOGICAL_NAME',
        'type': 'ViString'
    },
    1050327: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string that contains a comma-separated list of the instrument model numbers supported by this driver.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models',
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'type': 'ViString'
    },
    1050510: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string that contains the firmware revision information for the instrument you are currently using.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Firmware Revision',
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'supported_rep_caps': [
            'instruments'
        ],
        'type': 'ViString'
    },
    1050511: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string that contains the name of the instrument manufacturer.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Manufacturer',
        'name': 'INSTRUMENT_MANUFACTURER',
        'type': 'ViString'
    },
    1050512: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string that contains the model number of the current instrument.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Model',
        'name': 'INSTRUMENT_MODEL',
        'type': 'ViString'
    },
    1050513: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string that contains the name of the vendor that supplies this driver.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Driver Vendor',
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'type': 'ViString'
    },
    1050514: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string that contains a brief description of the specific driver\n'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Description',
        'name': 'SPECIFIC_DRIVER_DESCRIPTION',
        'type': 'ViString'
    },
    1050551: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string that contains additional version information about this instrument driver.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Revision',
        'name': 'SPECIFIC_DRIVER_REVISION',
        'type': 'ViString'
    },
    1150001: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the number of records to acquire. Can be used for multi-record acquisition and single-record acquisitions. Setting this to 1 indicates a single-record acquisition.\n'
        },
        'lv_property': 'Horizontal:Number of Records',
        'name': 'HORZ_NUM_RECORDS',
        'type': 'ViInt32'
    },
    1150002: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the input source for the PLL reference clock (the 1 MHz to 20 MHz clock on the NI 5122, the 10 MHz clock for the NI 5112/5620/5621/5911) to which the digitizer will be phase-locked; for the NI 5102, this is the source of the board clock.\n'
        },
        'lv_property': 'Clocking:Reference (Input) Clock Source',
        'name': 'INPUT_CLOCK_SOURCE',
        'type': 'ViString'
    },
    1150003: {
        'access': 'read-write',
        'documentation': {
            'description': "\nSpecifies the output source for the 10 MHz clock to which another digitizer's sample clock can be phased-locked.\n"
        },
        'lv_property': 'Clocking:Output Clock Source',
        'name': 'OUTPUT_CLOCK_SOURCE',
        'type': 'ViString'
    },
    1150004: {
        'access': 'read-write',
        'documentation': {
            'description': '\nIndicates whether the digitizer enforces real-time measurements or allows equivalent-time measurements.\n'
        },
        'lv_property': 'Horizontal:Enforce Realtime',
        'name': 'HORZ_ENFORCE_REALTIME',
        'type': 'ViBoolean'
    },
    1150005: {
        'access': 'read-write',
        'documentation': {
            'description': '\nIndicates the bit width of the binary data in the acquired waveform.  Useful for determining which Binary Fetch function to use. Compare to NISCOPE_ATTR_RESOLUTION.\nTo configure the device to store samples with a lower resolution that the native, set this attribute to the desired binary width.\nThis can be useful for streaming at faster speeds at the cost of resolution. The least significant bits will be lost with this configuration.\nValid Values: 8, 16, 32\n'
        },
        'lv_property': 'Acquisition:Binary Sample Width',
        'name': 'BINARY_SAMPLE_WIDTH',
        'type': 'ViInt32'
    },
    1150006: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the size of the hysteresis window on either side of the trigger level.  The digitizer triggers when the trigger signal passes through the threshold you specify with the Trigger Level parameter, has the slope you specify with the Trigger Slope parameter,  and passes through the hysteresis window that you specify with this parameter.'
        },
        'lv_property': 'Triggering:Trigger Hysteresis',
        'name': 'TRIGGER_HYSTERESIS',
        'type': 'ViReal64'
    },
    1150008: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether you want the device to be a master or a slave. The master typically originates the trigger signal and clock sync pulse. For a standalone device, set this attribute to VI_FALSE.\n'
        },
        'lv_property': 'Synchronization:Master Enable',
        'name': 'MASTER_ENABLE',
        'type': 'ViBoolean'
    },
    1150009: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecify the sampling rate for the acquisition in Samples per second.\nValid Values:\nThe combination of sampling rate and min record length must allow the digitizer to sample at a valid sampling rate for the acquisition type specified in niScope_ConfigureAcquisition and not require more memory than the onboard memory module allows.\n'
        },
        'lv_property': 'Horizontal:Min Sample Rate',
        'name': 'MIN_SAMPLE_RATE',
        'type': 'ViReal64'
    },
    1150012: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether you want a trigger to occur when the signal enters or leaves the window specified by NISCOPE_ATTR_TRIGGER_WINDOW_LOW_LEVEL, or NISCOPE_ATTR_TRIGGER_WINDOW_HIGH_LEVEL.\n'
        },
        'enum': 'TriggerWindowMode',
        'lv_property': 'Triggering:Trigger Window:Window Mode',
        'name': 'TRIGGER_WINDOW_MODE',
        'type': 'ViInt32'
    },
    1150013: {
        'access': 'read-write',
        'documentation': {
            'description': '\nPass the lower voltage threshold you want the digitizer to use for window triggering.\nThe digitizer triggers when the trigger signal enters or leaves the window you specify with NISCOPE_ATTR_TRIGGER_WINDOW_LOW_LEVEL and NISCOPE_ATTR_TRIGGER_WINDOW_HIGH_LEVEL.\nUnits: Volts\nValid Values:\nThe values of the Vertical Range and Vertical Offset parameters in niScope_ConfigureVertical determine the valid range for the Low Window Level on the channel you use as the Trigger Source parameter in niScope_ConfigureTriggerSource.  The value you pass for this parameter must meet the following conditions.\nLow Trigger Level <= Vertical Range/2 + Vertical Offset\nLow Trigger Level >= (-Vertical Range/2) + Vertical Offset\nLow Trigger Level < High Trigger Level\n'
        },
        'lv_property': 'Triggering:Trigger Window:Low Level',
        'name': 'TRIGGER_WINDOW_LOW_LEVEL',
        'type': 'ViReal64'
    },
    1150014: {
        'access': 'read-write',
        'documentation': {
            'description': '\nPass the upper voltage threshold you want the digitizer to use for window triggering.\nThe digitizer triggers when the trigger signal enters or leaves the window you specify with NISCOPE_ATTR_TRIGGER_WINDOW_LOW_LEVEL and NISCOPE_ATTR_TRIGGER_WINDOW_HIGH_LEVEL\nValid Values:\nThe values of the Vertical Range and Vertical Offset parameters in niScope_ConfigureVertical determine the valid range for the High Window Level on the channel you use as the Trigger Source parameter in niScope_ConfigureTriggerSource.  The value you pass for this parameter must meet the following conditions.\nHigh Trigger Level <= Vertical Range/2 + Vertical Offset\nHigh Trigger Level >= (-Vertical Range/2) + Vertical Offset\nHigh Trigger Level > Low Trigger Level\n'
        },
        'lv_property': 'Triggering:Trigger Window:High Level',
        'name': 'TRIGGER_WINDOW_HIGH_LEVEL',
        'type': 'ViReal64'
    },
    1150016: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSpecifies the units of the reference levels.\nNISCOPE_VAL_MEAS_VOLTAGE--Specifies that the reference levels are given in units of volts\nNISCOPE_VAL_MEAS_PERCENTAGE--Percentage units, where the measurements voltage low and voltage high represent 0% and 100%, respectively.\nDefault: NISCOPE_VAL_MEAS_PERCENTAGE\n'
        },
        'enum': 'RefLevelUnits',
        'lv_property': 'Waveform Measurement:Reference Levels:Units',
        'name': 'MEAS_REF_LEVEL_UNITS',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150018: {
        'access': 'read-write',
        'attribute_class': 'AttributeViStringRepeatedCapability',
        'codegen_method': 'public',
        'documentation': {
            'description': "\nSpecifies the second channel for two-channel measurements, such as NISCOPE_VAL_ADD_CHANNELS. If processing steps are registered with this channel, the processing is done before the waveform is used in a two-channel measurement.\nDefault: '0'\n"
        },
        'lv_property': 'Waveform Measurement:Other Channel',
        'name': 'MEAS_OTHER_CHANNEL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViString',
        'type_in_documentation': 'str or int'
    },
    1150019: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\nDigital hysteresis that is used in several of the scalar waveform measurements. This attribute specifies the percentage of the full-scale vertical range for the hysteresis window size.\nDefault: 2%\n'
        },
        'lv_property': 'Waveform Measurement:Hysteresis Percent',
        'name': 'MEAS_HYSTERESIS_PERCENT',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150020: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSpecifies the size (that is, the number of bins) in the last acquisition histogram. This histogram is used to determine several scalar measurements, most importantly voltage low and voltage high.\nDefault: 256\n'
        },
        'lv_property': 'Waveform Measurement:Last Acq. Histogram Size',
        'name': 'MEAS_LAST_ACQ_HISTOGRAM_SIZE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150021: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\nDetermines the multiple acquisition voltage histogram size. The size is set the first time a voltage histogram measurement is called after clearing the measurement history with the function niScope_ClearWaveformMeasurementStats.\nDefault: 256\n'
        },
        'lv_property': 'Waveform Measurement:Voltage Histogram:Size',
        'name': 'MEAS_VOLTAGE_HISTOGRAM_SIZE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150022: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSpecifies the lowest voltage value included in the multiple-acquisition voltage histogram. The units are always volts.\nDefault: -10.0 V\n'
        },
        'lv_property': 'Waveform Measurement:Voltage Histogram:Low Volts',
        'name': 'MEAS_VOLTAGE_HISTOGRAM_LOW_VOLTS',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150023: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSpecifies the highest voltage value included in the multiple acquisition voltage histogram. The units are always volts.\nDefault: 10.0 V\n'
        },
        'lv_property': 'Waveform Measurement:Voltage Histogram:High Volts',
        'name': 'MEAS_VOLTAGE_HISTOGRAM_HIGH_VOLTS',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150024: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\nDetermines the multiple acquisition voltage histogram size. The size is set during the first call to a time histogram measurement after clearing the measurement history with niScope_ClearWaveformMeasurementStats.\nDefault: 256\n'
        },
        'lv_property': 'Waveform Measurement:Time Histogram:Size',
        'name': 'MEAS_TIME_HISTOGRAM_SIZE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150025: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSpecifies the lowest voltage value included in the multiple acquisition time histogram. The units are always volts.\nDefault: -10.0 V\n'
        },
        'lv_property': 'Waveform Measurement:Time Histogram:Low Volts',
        'name': 'MEAS_TIME_HISTOGRAM_LOW_VOLTS',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150026: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSpecifies the highest voltage value included in the multiple-acquisition time histogram. The units are always volts.\nDefault: 10.0 V\n'
        },
        'lv_property': 'Waveform Measurement:Time Histogram:High Volts',
        'name': 'MEAS_TIME_HISTOGRAM_HIGH_VOLTS',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150027: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSpecifies the lowest time value included in the multiple-acquisition time histogram. The units are always seconds.\nDefault: -5.0e-4 seconds\n'
        },
        'lv_property': 'Waveform Measurement:Time Histogram:Low Time',
        'name': 'MEAS_TIME_HISTOGRAM_LOW_TIME',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150028: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSpecifies the highest time value included in the multiple acquisition time histogram. The units are always seconds.\nDefault: 5.0e-4 seconds\n'
        },
        'lv_property': 'Waveform Measurement:Time Histogram:High Time',
        'name': 'MEAS_TIME_HISTOGRAM_HIGH_TIME',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150029: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSpecifies the polynomial order used for the polynomial interpolation measurement. For example, an order of 1 is linear interpolation whereas an order of 2 specifies parabolic interpolation. Any positive integer is valid.\nDefault: 1\n'
        },
        'lv_property': 'Waveform Measurement:Interpolation:Polynomial Interpolation Order',
        'name': 'MEAS_POLYNOMIAL_INTERPOLATION_ORDER',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150030: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\nThe new number of points for polynomial interpolation is the sampling factor times the input number of points. For example, if you acquire 1,000 points with the digitizer and set this attribute to 2.5, calling niScope_FetchWaveformMeasurementArray with the NISCOPE_VAL_POLYNOMIAL_INTERPOLATION measurement resamples the waveform to 2,500 points.\nDefault: 2.0\n'
        },
        'lv_property': 'Waveform Measurement:Interpolation:Sampling Factor',
        'name': 'MEAS_INTERPOLATION_SAMPLING_FACTOR',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150031: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSpecifies the cutoff frequency in hertz for filters of type lowpass and highpass. The cutoff frequency definition varies depending on the filter.\nDefault: 1.0e6 Hz\n'
        },
        'lv_property': 'Waveform Measurement:Filter:Cutoff Frequency',
        'name': 'MEAS_FILTER_CUTOFF_FREQ',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150032: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\nThe center frequency in hertz for filters of type bandpass and bandstop. The width of the filter is specified by NISCOPE_ATTR_MEAS_FILTER_WIDTH, where the cutoff frequencies are the center ± width.\nDefault: 1.0e6 Hz\n'
        },
        'lv_property': 'Waveform Measurement:Filter:Center Frequency',
        'name': 'MEAS_FILTER_CENTER_FREQ',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150033: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSpecifies the amount of ripple in the passband in units of decibels (positive values). Used only for Chebyshev filters. The more ripple allowed gives a sharper cutoff for a given filter order.\nDefault: 0.1 dB\n'
        },
        'lv_property': 'Waveform Measurement:Filter:Ripple',
        'name': 'MEAS_FILTER_RIPPLE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150034: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\nThe percentage (0 - 100%) of the IIR filtered waveform to eliminate from the beginning of the waveform. This allows eliminating the transient portion of the waveform that is undefined due to the assumptions necessary at the boundary condition.\nDefault: 20.0%\n'
        },
        'lv_property': 'Waveform Measurement:Filter:Percent Waveform Transient',
        'name': 'MEAS_FILTER_TRANSIENT_WAVEFORM_PERCENT',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150035: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSpecifies the type of filter, for both IIR and FIR filters. The allowed values are the following:\n·  NISCOPE_VAL_MEAS_LOWPASS\n·  NISCOPE_VAL_MEAS_HIGHPASS\n·  NISCOPE_VAL_MEAS_BANDPASS\n·  NISCOPE_VAL_MEAS_BANDSTOP\nDefault: NISCOPE_VAL_MEAS_LOWPASS\n'
        },
        'enum': 'FilterType',
        'lv_property': 'Waveform Measurement:Filter:Type',
        'name': 'MEAS_FILTER_TYPE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150036: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSpecifies the order of an IIR filter. All positive integers are valid.\nDefault: 2\n'
        },
        'lv_property': 'Waveform Measurement:Filter:IIR Order',
        'name': 'MEAS_FILTER_ORDER',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150037: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\nDefines the number of taps (coefficients) for an FIR filter.\nDefault: 25\n'
        },
        'lv_property': 'Waveform Measurement:Filter:FIR Taps',
        'name': 'MEAS_FILTER_TAPS',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150038: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\nStores the low reference level used in many scalar measurements. Different channels may have different reference levels. Do not use the IVI-defined, nonchannel-based attributes such as NISCOPE_ATTR_MEAS_LOW_REF if you use this attribute to set various channels to different values.\nDefault: 10%\n'
        },
        'lv_property': 'Waveform Measurement:Reference Levels:Channel Based Low Ref Level',
        'name': 'MEAS_CHAN_LOW_REF_LEVEL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150039: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\nStores the mid reference level used in many scalar measurements. Different channels may have different reference levels. Do not use the IVI-defined, nonchannel-based attributes such as NISCOPE_ATTR_MEAS_MID_REF if you use this attribute to set various channels to different values.\nDefault: 50%\n'
        },
        'lv_property': 'Waveform Measurement:Reference Levels:Channel Based Mid Ref Level',
        'name': 'MEAS_CHAN_MID_REF_LEVEL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150040: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\nStores the high reference level used in many scalar measurements. Different channels may have different reference levels. Do not use the IVI-defined, nonchannel-based attributes such as NISCOPE_ATTR_MEAS_HIGH_REF if you use this attribute to set various channels to different values.\nDefault: 90%\n'
        },
        'lv_property': 'Waveform Measurement:Reference Levels:Channel Based High Ref Level',
        'name': 'MEAS_CHAN_HIGH_REF_LEVEL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150041: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSpecifies the width of bandpass and bandstop type filters in hertz. The cutoff frequencies occur at NISCOPE_ATTR_MEAS_FILTER_CENTER_FREQ ± one-half width.\nDefault: 1.0e3 Hz\n'
        },
        'lv_property': 'Waveform Measurement:Filter:Width',
        'name': 'MEAS_FILTER_WIDTH',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150042: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSpecifies the FIR window type. The possible choices are:\nNISCOPE_VAL_NONE\nNISCOPE_VAL_HANNING_WINDOW\nNISCOPE_VAL_HAMMING_WINDOW\nNISCOPE_VAL_TRIANGLE_WINDOW\nNISCOPE_VAL_FLAT_TOP_WINDOW\nNISCOPE_VAL_BLACKMAN_WINDOW\nThe symmetric windows are applied to the FIR filter coefficients to limit passband ripple in FIR filters.\nDefault: NISCOPE_VAL_NONE\n'
        },
        'enum': 'FIRFilterWindow',
        'lv_property': 'Waveform Measurement:Filter:FIR Window',
        'name': 'MEAS_FIR_FILTER_WINDOW',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150043: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\nEvery element of an array is multiplied by this scalar value during the Array Gain measurement.  Refer to NISCOPE_VAL_ARRAY_GAIN for more information.\nDefault: 1.0\n'
        },
        'lv_property': 'Waveform Measurement:Array Gain',
        'name': 'MEAS_ARRAY_GAIN',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150044: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\nEvery element of an array is added to this scalar value during the Array Offset measurement. Refer to NISCOPE_VAL_ARRAY_OFFSET for more information.\nDefault: 0.0\n'
        },
        'lv_property': 'Waveform Measurement:Array Offset',
        'name': 'MEAS_ARRAY_OFFSET',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150045: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSpecifies the method used to map percentage reference units to voltages for the reference. Possible values are:\nNISCOPE_VAL_MEAS_LOW_HIGH\nNISCOPE_VAL_MEAS_MIN_MAX\nNISCOPE_VAL_MEAS_BASE_TOP\nDefault: NISCOPE_VAL_MEAS_BASE_TOP\n'
        },
        'enum': 'PercentageMethod',
        'lv_property': 'Waveform Measurement:Reference Levels:Percentage Units Method',
        'name': 'MEAS_PERCENTAGE_METHOD',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150053: {
        'access': 'read-write',
        'documentation': {
            'description': "\nSpecifies the source the digitizer monitors for a start (acquisition arm) trigger.  When the start trigger is received, the digitizer begins acquiring pretrigger samples.\nValid Values:\nNISCOPE_VAL_IMMEDIATE     ('VAL_IMMEDIATE')    - Triggers immediately\nNISCOPE_VAL_RTSI_0        ('VAL_RTSI_0')       - RTSI 0\nNISCOPE_VAL_RTSI_1        ('VAL_RTSI_1')       - RTSI 1\nNISCOPE_VAL_RTSI_2        ('VAL_RTSI_2')       - RTSI 2\nNISCOPE_VAL_RTSI_3        ('VAL_RTSI_3')       - RTSI 3\nNISCOPE_VAL_RTSI_4        ('VAL_RTSI_4')       - RTSI 4\nNISCOPE_VAL_RTSI_5        ('VAL_RTSI_5')       - RTSI 5\nNISCOPE_VAL_RTSI_6        ('VAL_RTSI_6')       - RTSI 6\nNISCOPE_VAL_PFI_0         ('VAL_PFI_0')        - PFI 0\nNISCOPE_VAL_PFI_1         ('VAL_PFI_1')        - PFI 1\nNISCOPE_VAL_PFI_2         ('VAL_PFI_2')        - PFI 2\nNISCOPE_VAL_PXI_STAR      ('VAL_PXI_STAR')     - PXI Star Trigger\n"
        },
        'lv_property': 'Synchronization:Start Trigger (Acq. Arm):Source',
        'name': 'ACQ_ARM_SOURCE',
        'type': 'ViString'
    },
    1150065: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the record arm source.\n'
        },
        'lv_property': 'Synchronization:Record Arm Source',
        'name': 'RECORD_ARM_SOURCE',
        'type': 'ViString'
    },
    1150066: {
        'access': 'read only',
        'name': 'IS_PROBE_COMP_ON',
        'supported_rep_caps': [
            'instruments'
        ],
        'type': 'ViBoolean'
    },
    1150067: {
        'access': 'read-write',
        'name': 'USE_SPEC_INITIAL_X',
        'type': 'ViBoolean'
    },
    1150068: {
        'access': 'read-write',
        'documentation': {
            'description': '\nIndicates whether more records can be configured with niScope_ConfigureHorizontalTiming than fit in the onboard memory. If this attribute is set to VI_TRUE, it is necessary to fetch records while the acquisition is in progress.  Eventually, some of the records will be overwritten.  An error is returned from the fetch function if you attempt to fetch a record that has been overwritten.\n'
        },
        'lv_property': 'Horizontal:Enable Records > Memory',
        'name': 'ALLOW_MORE_RECORDS_THAN_MEMORY',
        'type': 'ViBoolean'
    },
    1150069: {
        'access': 'read only',
        'documentation': {
            'description': '\nReturns the total combined amount of onboard memory for all channels in bytes.\n'
        },
        'lv_property': 'Horizontal:Memory Size',
        'name': 'ONBOARD_MEMORY_SIZE',
        'supported_rep_caps': [
            'instruments'
        ],
        'type': 'ViInt32'
    },
    1150070: {
        'access': 'read-write',
        'documentation': {
            'description': '\nThe number of averages for each bin in an RIS acquisition.  The number of averages times the oversampling factor is the minimum number of real-time acquisitions necessary to reconstruct the RIS waveform.  Averaging is useful in RIS because the trigger times are not evenly spaced, so adjacent points in the reconstructed waveform not be accurately spaced.  By averaging, the errors in both time and voltage are smoothed.\n'
        },
        'lv_property': 'Horizontal:RIS Num Avg',
        'name': 'RIS_NUM_AVERAGES',
        'type': 'ViInt32'
    },
    1150071: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the algorithm for random-interleaved sampling, which is used if the sample rate exceeds the value of NISCOPE_ATTR_MAX_REAL_TIME_SAMPLING_RATE.\n'
        },
        'enum': 'RISMethod',
        'lv_property': 'Horizontal:RIS Method',
        'name': 'RIS_METHOD',
        'type': 'ViInt32'
    },
    1150073: {
        'access': 'read only',
        'documentation': {
            'description': '\nReturns the maximum real time sample rate in Hz.\n'
        },
        'lv_property': 'Horizontal:Maximum Real Time Sample Rate',
        'name': 'MAX_REAL_TIME_SAMPLING_RATE',
        'type': 'ViReal64'
    },
    1150074: {
        'access': 'read only',
        'documentation': {
            'description': '\nReturns the maximum sample rate in RIS mode in Hz.\n'
        },
        'lv_property': 'Horizontal:Maximum RIS Rate',
        'name': 'MAX_RIS_RATE',
        'type': 'ViReal64'
    },
    1150075: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the input impedance for the external analog trigger channel in Ohms.\nValid Values:\n50      - 50 ohms\n1000000 - 1 mega ohm\n'
        },
        'lv_property': 'Triggering:Trigger Impedance',
        'name': 'TRIGGER_IMPEDANCE',
        'type': 'ViReal64'
    },
    1150077: {
        'access': 'read-write',
        'codegen_method': 'private',
        'documentation': {
            'description': '\nPosition to start fetching within one record.\nDefault Value: NISCOPE_VAL_PRETRIGGER\n'
        },
        'enum': 'FetchRelativeTo',
        'lv_property': 'Fetch:Fetch Relative To',
        'name': 'FETCH_RELATIVE_TO',
        'type': 'ViInt32'
    },
    1150078: {
        'access': 'read-write',
        'codegen_method': 'private',
        'documentation': {
            'description': '\nOffset in samples to start fetching data within each record. The offset is applied relative to NISCOPE_ATTR_FETCH_RELATIVE_TO.The offset can be positive or negative.\nDefault Value: 0\n'
        },
        'lv_property': 'Fetch:Fetch Offset',
        'name': 'FETCH_OFFSET',
        'type': 'ViInt32'
    },
    1150079: {
        'access': 'read-write',
        'codegen_method': 'private',
        'documentation': {
            'description': '\nZero-based index of the first record to fetch.  Use NISCOPE_FETCH_NUM_RECORDS to set the number of records to fetch.\nDefault Value: 0.\n'
        },
        'lv_property': 'Fetch:Fetch Record Number',
        'name': 'FETCH_RECORD_NUMBER',
        'type': 'ViInt32'
    },
    1150080: {
        'access': 'read-write',
        'codegen_method': 'private',
        'documentation': {
            'description': '\nNumber of records to fetch. Use -1 to fetch all configured records.\nDefault Value: -1\n'
        },
        'lv_property': 'Fetch:Fetch Number of Records',
        'name': 'FETCH_NUM_RECORDS',
        'type': 'ViInt32'
    },
    1150081: {
        'access': 'read-write',
        'codegen_method': 'private',
        'documentation': {
            'description': '\nNumber of samples to fetch when performing a measurement. Use -1 to fetch the actual record length.\nDefault Value: -1\n'
        },
        'lv_property': 'Fetch:Fetch Meas Num Samples',
        'name': 'FETCH_MEAS_NUM_SAMPLES',
        'type': 'ViInt32'
    },
    1150082: {
        'access': 'read only',
        'documentation': {
            'description': '\nActual number of samples acquired in the record specified by NISCOPE_ATTR_FETCH_RECORD_NUMBER from the NISCOPE_ATTR_FETCH_RELATIVE_TO and NISCOPE_ATTR_FETCH_OFFSET attributes.\n'
        },
        'lv_property': 'Fetch:Points Done',
        'name': 'POINTS_DONE',
        'type': 'ViReal64'
    },
    1150083: {
        'access': 'read only',
        'documentation': {
            'description': '\nSpecifies the number of records that have been completely acquired.\n'
        },
        'lv_property': 'Fetch:Records Done',
        'name': 'RECORDS_DONE',
        'type': 'ViInt32'
    },
    1150084: {
        'access': 'read only',
        'documentation': {
            'description': '\nReturns the number of samples (NISCOPE_ATTR_POINTS_DONE) that have been acquired but not fetched for the record specified by NISCOPE_ATTR_FETCH_RECORD_NUMBER.\n'
        },
        'lv_property': 'Fetch:Fetch Backlog',
        'name': 'BACKLOG',
        'type': 'ViReal64'
    },
    1150086: {
        'access': 'read only',
        'documentation': {
            'description': '\nReturns the temperature of the device in degrees Celsius from the onboard sensor.\n'
        },
        'lv_property': 'Device:Temperature',
        'name': 'DEVICE_TEMPERATURE',
        'supported_rep_caps': [
            'instruments'
        ],
        'type': 'ViReal64'
    },
    1150087: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the source of the sample clock timebase, which is the timebase used to control waveform sampling.  The actual sample rate may be the timebase itself or a divided version of the timebase, depending on the NISCOPE_ATTR_MIN_SAMPLE_RATE (for internal sources) or the NISCOPE_ATTR_SAMP_CLK_TIMEBASE_DIV (for external sources).\n'
        },
        'lv_property': 'Clocking:Sample Clock Timebase Source',
        'name': 'SAMP_CLK_TIMEBASE_SRC',
        'type': 'ViString'
    },
    1150088: {
        'access': 'read-write',
        'documentation': {
            'description': '\nIf NISCOPE_ATTR_SAMP_CLK_TIMEBASE_SRC is an external source, specifies the frequency in hertz of the external clock used as the timebase source.\n'
        },
        'lv_property': 'Clocking:Sample Clock Timebase Rate',
        'name': 'SAMP_CLK_TIMEBASE_RATE',
        'type': 'ViReal64'
    },
    1150089: {
        'access': 'read-write',
        'documentation': {
            'description': '\nIf NISCOPE_ATTR_SAMP_CLK_TIMEBASE_SRC is an external source, specifies the ratio between the sample clock timebase rate and the actual sample rate, which can be slower.\n'
        },
        'lv_property': 'Clocking:Sample Clock Timebase Divisor',
        'name': 'SAMP_CLK_TIMEBASE_DIV',
        'type': 'ViInt32'
    },
    1150090: {
        'access': 'read-write',
        'documentation': {
            'description': '\nIf NISCOPE_ATTR_INPUT_CLOCK_SOURCE is an external source, this attribute specifies the frequency of the input,  or reference clock, to which the internal sample clock timebase is synchronized. The frequency is in hertz.\n'
        },
        'lv_property': 'Clocking:Reference Clock Rate',
        'name': 'REF_CLK_RATE',
        'type': 'ViReal64'
    },
    1150093: {
        'access': 'read-write',
        'documentation': {
            'description': "\nRestores the video-triggered data retrieved by the digitizer to the video signal's zero reference point.\nValid Values:\nVI_TRUE - Enable DC restore\nVI_FALSE - Disable DC restore\n"
        },
        'lv_property': 'Triggering:Trigger Video:Enable DC Restore',
        'name': 'ENABLE_DC_RESTORE',
        'type': 'ViBoolean'
    },
    1150094: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the source the digitizer monitors for an advance trigger.  When the advance trigger is received, the digitizer begins acquiring pretrigger samples.\n'
        },
        'lv_property': 'Synchronization:Advance Trigger:Source',
        'name': 'ADV_TRIG_SRC',
        'type': 'ViString'
    },
    1150095: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the source the digitizer monitors for an arm reference trigger.  When the arm reference trigger is received, the digitizer begins looking for a reference (stop) trigger from the user-configured trigger source.\n'
        },
        'lv_property': 'Synchronization:Arm Reference Trigger:Source',
        'name': 'ARM_REF_TRIG_SRC',
        'type': 'ViString'
    },
    1150096: {
        'access': 'read-write',
        'documentation': {
            'description': '\nThis attribute controls whether the TDC is used to compute an accurate trigger.\n'
        },
        'lv_property': 'Horizontal:Advanced:Enable TDC',
        'name': 'REF_TRIG_TDC_ENABLE',
        'type': 'ViBoolean'
    },
    1150097: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the destination to export the Start trigger.  When the start trigger is received, the digitizer begins acquiring samples.\nConsult your device documentation for a specific list of valid destinations.\n'
        },
        'lv_property': 'Synchronization:Start Trigger (Acq. Arm):Output Terminal',
        'name': 'EXPORTED_START_TRIGGER_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150098: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the destination export for the reference (stop) trigger.\nConsult your device documentation for a specific list of valid destinations.\n'
        },
        'lv_property': 'Triggering:Trigger Output Terminal',
        'name': 'EXPORTED_REF_TRIGGER_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150099: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the destination for the End of Record Event.    When this event is asserted, the digitizer has completed sampling for the current record.\nConsult your device documentation for a specific list of valid destinations.\n'
        },
        'lv_property': 'Synchronization:End of Record:Output Terminal',
        'name': 'END_OF_RECORD_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150100: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the poll interval in milliseconds to use during RIS acquisitions to check whether the acquisition is complete.\n'
        },
        'lv_property': '',
        'name': 'POLL_INTERVAL',
        'type': 'ViInt32'
    },
    1150101: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the destination for the End of Acquisition Event.    When this event is asserted, the digitizer has completed sampling for all records.\nConsult your device documentation for a specific list of valid destinations.\n'
        },
        'lv_property': 'Synchronization:End of Acquisition:Output Terminal',
        'name': 'END_OF_ACQUISITION_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150102: {
        'access': 'read only',
        'documentation': {
            'description': '\nIndicates the bit width of valid data (as opposed to padding bits) in the acquired waveform. Compare to NISCOPE_ATTR_BINARY_SAMPLE_WIDTH.\n'
        },
        'lv_property': 'Acquisition:Resolution',
        'name': 'RESOLUTION',
        'type': 'ViInt32'
    },
    1150103: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': '\nPass the length of time you want the digitizer to wait after it starts acquiring data until the digitizer enables the trigger system to detect a reference (stop) trigger.\nUnits: Seconds\nValid Values: 0.0 - 171.8\n'
        },
        'lv_property': 'Triggering:Start To Ref Trigger Holdoff',
        'name': 'START_TO_REF_TRIGGER_HOLDOFF',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150104: {
        'access': 'read only',
        'documentation': {
            'description': '\nReturns the serial number of the device.\n'
        },
        'lv_property': 'Device:Serial Number',
        'name': 'SERIAL_NUMBER',
        'supported_rep_caps': [
            'instruments'
        ],
        'type': 'ViString'
    },
    1150106: {
        'access': 'read-write',
        'documentation': {
            'description': '\nIndicates whether the digitizer should use RIS sample rates when searching for a frequency in autosetup.\nValid Values:\nVI_TRUE  (1) - Use RIS sample rates in autosetup\nVI_FALSE (0) - Do not use RIS sample rates in autosetup\n'
        },
        'lv_property': 'Acquisition:Advanced:Enable RIS in Auto Setup',
        'name': 'RIS_IN_AUTO_SETUP_ENABLE',
        'type': 'ViBoolean'
    },
    1150107: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the terminal configuration for the channel.\n'
        },
        'enum': 'TerminalConfiguration',
        'lv_property': 'Vertical:Channel Terminal Configuration',
        'name': 'CHANNEL_TERMINAL_CONFIGURATION',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150109: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the destination to export the advance trigger.  When the advance trigger is received, the digitizer begins acquiring samples for the Nth record.\nConsult your device documentation for a specific list of valid destinations.\n'
        },
        'lv_property': 'Synchronization:Advance Trigger:Output Terminal',
        'name': 'EXPORTED_ADVANCE_TRIGGER_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150110: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the destination for the Ready for Start Event.  When this event is asserted, the digitizer is ready to receive a start trigger.\nConsult your device documentation for a specific list of valid destinations.\n'
        },
        'lv_property': 'Synchronization:Ready for Start:Output Terminal',
        'name': 'READY_FOR_START_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150111: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the destination for the Ready for Reference Event.  When this event is asserted, the digitizer is ready to receive a reference trigger.\nConsult your device documentation for a specific list of valid destinations.\n'
        },
        'lv_property': 'Synchronization:Ready for Reference:Output Terminal',
        'name': 'READY_FOR_REF_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150112: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the destination for the Ready for Advance Event.    When this event is asserted, the digitizer is ready to receive an advance trigger.\nConsult your device documentation for a specific list of valid destinations.\n'
        },
        'lv_property': 'Synchronization:Ready for Advance:Output Terminal',
        'name': 'READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150128: {
        'access': 'read-write',
        'documentation': {
            'description': "\nSpecifies whether the digitizer acquires the waveform using multiple ADCs for the channel enabling a higher maximum real-time sampling rate.\nValid Values:\nVI_TRUE  (1) - Use multiple interleaved ADCs on this channel\nVI_FALSE (0) - Use only this channel's ADC to acquire data for this channel\n"
        },
        'lv_property': 'Horizontal:Enable Time Interleaved Sampling',
        'name': 'ENABLE_TIME_INTERLEAVED_SAMPLING',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViBoolean'
    },
    1150132: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether runt triggers are time qualified, and if so, how the oscilloscope triggers in relation to the duration range bounded by the NISCOPE_ATTR_RUNT_TIME_LOW_LIMIT and NISCOPE_ATTR_RUNT_TIME_HIGH_LIMIT attributes.\n'
        },
        'enum': 'RuntTimeCondition',
        'name': 'RUNT_TIME_CONDITION',
        'type': 'ViInt32'
    },
    1150133: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies, in seconds, the low runt threshold time.\n\nThis attribute sets the lower bound on the duration of runt pulses that may trigger the oscilloscope. The NISCOPE_ATTR_RUNT_TIME_CONDITION attribute determines how the oscilloscope triggers in relation to the runt time limits.\n'
        },
        'name': 'RUNT_TIME_LOW_LIMIT',
        'type': 'ViReal64'
    },
    1150134: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies, in seconds, the high runt threshold time.\n\nThis attribute sets the upper bound on the duration of runt pulses that may trigger the oscilloscope. The NISCOPE_ATTR_RUNT_TIME_CONDITION attribute determines how the oscilloscope triggers in relation to the runt time limits.\n'
        },
        'name': 'RUNT_TIME_HIGH_LIMIT',
        'type': 'ViReal64'
    },
    1150137: {
        'access': 'read-write',
        'documentation': {
            'description': '\nReturns the voltage of the CableSense signal that is written to the EEPROM of the oscilloscope during factory calibration.\n',
            'table_body': [
                [
                    '**Supported Devices**'
                ],
                [
                    'PXIe-5110'
                ],
                [
                    'PXIe-5111'
                ],
                [
                    'PXIe-5113'
                ],
                [
                    'PXIe-5160'
                ],
                [
                    'PXIe-5162'
                ]
            ]
        },
        'name': 'CABLE_SENSE_VOLTAGE',
        'type': 'ViReal64'
    },
    1150138: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether and how the oscilloscope is configured to generate a CableSense signal on the specified channels when the niScope_CableSenseSignalStart function is called.\n\nDevice-Specific Behavior:\n    PXIe-5160/5162\n        - The value of this attribute must be identical across all channels whose input impedance is set to 50 ohms.\n        - If this attribute is set to a value other than NISCOPE_VAL_CABLE_SENSE_MODE_DISABLED for any channel(s), the input impedance of all channels for which this attribute is set to NISCOPE_VAL_CABLE_SENSE_MODE_DISABLED must be set to 1 M Ohm.',
            'note': 'the input impedance of the channel(s) to convey the CableSense signal must be set to 50 ohms.',
            'table_body': [
                [
                    '**Supported Devices**'
                ],
                [
                    'PXIe-5110'
                ],
                [
                    'PXIe-5111'
                ],
                [
                    'PXIe-5113'
                ],
                [
                    'PXIe-5160'
                ],
                [
                    'PXIe-5162'
                ]
            ]
        },
        'enum': 'CableSenseMode',
        'name': 'CABLE_SENSE_MODE',
        'type': 'ViReal64'
    },
    1150139: {
        'access': 'read-write',
        'documentation': {
            'description': '\nTBD\n'
        },
        'name': 'CABLE_SENSE_SIGNAL_ENABLE',
        'type': 'ViBoolean'
    },
    1150140: {
        'access': 'read only',
        'documentation': {
            'description': '\nReturns a comma-separated list of the channels enabled for the session in ascending order.\n\nIf no channels are enabled, this attribute returns an empty string, "".\nIf all channels are enabled, this attribute enumerates all of the channels.\n\nBecause this attribute returns channels in ascending order, but the order in which you specify channels for the input is important, the value of this attribute may not necessarily reflect the order in which NI-SCOPE performs certain actions.\n\nRefer to Channel String Syntax in the NI High-Speed Digitizers Help for more information on the effects of channel order in NI-SCOPE.\n'
        },
        'name': 'ENABLED_CHANNELS',
        'type': 'ViString'
    },
    1150141: {
        'access': 'read only',
        'documentation': {
            'description': '\nReturns the fully qualified name for the End of Acquisition Event terminal.    You can use this terminal as the source for a trigger.\n'
        },
        'lv_property': 'Synchronization:End of Acquisition:Terminal Name',
        'name': 'END_OF_ACQUISITION_EVENT_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150142: {
        'access': 'read only',
        'documentation': {
            'description': '\nReturns the fully qualified name for the End of Record Event terminal.    You can use this terminal as the source for a trigger.\n'
        },
        'lv_property': 'Synchronization:End of Record:Terminal Name',
        'name': 'END_OF_RECORD_EVENT_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150143: {
        'access': 'read only',
        'documentation': {
            'description': '\nReturns the fully qualified name for the Advance Trigger terminal.  You can use this terminal as the source for another trigger.\n'
        },
        'lv_property': 'Synchronization:Advance Trigger:Terminal Name',
        'name': 'ADVANCE_TRIGGER_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150144: {
        'access': 'read only',
        'documentation': {
            'description': '\nReturns the fully qualified name for the Reference Trigger terminal.  You can use this terminal as the source for another trigger.\n'
        },
        'lv_property': 'Triggering:Terminal Name',
        'name': 'REF_TRIGGER_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150145: {
        'access': 'read only',
        'documentation': {
            'description': '\nReturns the fully qualified name for the Start Trigger terminal.  You can use this terminal as the source for another trigger.\n'
        },
        'lv_property': 'Synchronization:Start Trigger (Acq. Arm):Terminal Name',
        'name': 'START_TRIGGER_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150146: {
        'access': 'read only',
        'documentation': {
            'description': '\nReturns the fully qualified name for the Ready for Advance Event terminal.    You can use this terminal as the source for a trigger.\n'
        },
        'lv_property': 'Synchronization:Ready for Advance:Terminal Name',
        'name': 'READY_FOR_ADVANCE_EVENT_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150147: {
        'access': 'read only',
        'documentation': {
            'description': '\nReturns the fully qualified name for the Ready for Reference Event terminal.    You can use this terminal as the source for a trigger.\n'
        },
        'lv_property': 'Synchronization:Ready for Reference:Terminal Name',
        'name': 'READY_FOR_REF_EVENT_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150148: {
        'access': 'read only',
        'documentation': {
            'description': '\nReturns the fully qualified name for the Ready for Start Event terminal.    You can use this terminal as the source for a trigger.\n'
        },
        'lv_property': 'Synchronization:Ready for Start:Terminal Name',
        'name': 'READY_FOR_START_EVENT_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150271: {
        'access': 'read-write',
        'documentation': {
            'description': '\nThe NI 5922 flexible-resolution digitizer uses an onboard FIR lowpass antialias filter.\nUse this attribute to select from several types of filters to achieve desired filtering characteristics.\n'
        },
        'enum': 'FlexFIRAntialiasFilterType',
        'lv_property': 'Vertical:Advanced:Flex FIR Antialias Filter Type',
        'name': 'FLEX_FIR_ANTIALIAS_FILTER_TYPE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150278: {
        'access': 'read only',
        'documentation': {
            'description': '\nSpecifies if the last acquisition was auto triggered.  You can use the Auto Triggered attribute to find out if the last acquisition was triggered.\n'
        },
        'lv_property': 'Triggering:Auto Triggered',
        'name': 'TRIGGER_AUTO_TRIGGERED',
        'type': 'ViBoolean'
    },
    1150279: {
        'access': 'read only',
        'documentation': {
            'description': '\nReturns the calibration gain for the current device configuration.\n\n**Related topics:**\n`NI 5122/5124/5142 Calibration <digitizers.chm::/5122_Calibration.html>`__\n',
            'note': '\nThis property is supported only by the NI PXI-5900 differential amplifier.\n'
        },
        'name': 'SIGNAL_COND_GAIN',
        'python_name': 'accessory_gain',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150280: {
        'access': 'read only',
        'documentation': {
            'description': '\nReturns the calibration offset for the current device configuration.\n\n**Related topics:**\n`NI 5122/5124/5142 Calibration <digitizers.chm::/5122_Calibration.html>`__\n',
            'note': '\nThis property is supported only by the NI PXI-5900 differential amplifier.\n'
        },
        'name': 'SIGNAL_COND_OFFSET',
        'python_name': 'accessory_offset',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150312: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns the number of coefficients that the FIR filter can accept.  This filter is designed to compensate the input signal for artifacts introduced to the signal outside of the digitizer.  However, since this is a generic FIR filter any coefficients are valid.  Coefficients should be between +1 and -1 in value.'
        },
        'lv_property': 'Onboard Signal Processing:Equalization:Equalization Num Coefficients',
        'name': 'EQUALIZATION_NUM_COEFFICIENTS',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150313: {
        'access': 'read-write',
        'documentation': {
            'description': 'Enables the onboard signal processing FIR block. This block is connected directly to the input signal.  This filter is designed to compensate the input signal for artifacts introduced to the signal outside of the digitizer. However, since this is a generic FIR filter any coefficients are valid.  Coefficients should be between +1 and -1 in value.'
        },
        'lv_property': 'Onboard Signal Processing:Equalization:Equalization Filter Enabled',
        'name': 'EQUALIZATION_FILTER_ENABLED',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViBoolean'
    },
    1150314: {
        'access': 'read-write',
        'documentation': {
            'description': '\nIndicates which analog compare circuitry to use on the device.\n'
        },
        'enum': 'RefTriggerDetectorLocation',
        'lv_property': 'Triggering:Onboard Signal Processing:Ref Trigger Detection Location',
        'name': 'REF_TRIGGER_DETECTOR_LOCATION',
        'type': 'ViInt32'
    },
    1150315: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': '\nThe amount of time the trigger circuit must not detect a signal above the trigger level before the trigger is armed.  This attribute is useful for triggering at the beginning and not in the middle of signal bursts.\n'
        },
        'lv_property': 'Triggering:Onboard Signal Processing:Ref Trigger Min Quiet Time',
        'name': 'REF_TRIGGER_MINIMUM_QUIET_TIME',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150316: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the maximum number of samples to transfer at one time from the device to host memory. Increasing this number should result in better fetching performance because the driver does not need to restart the transfers as often. However, increasing this number may also increase the amount of page-locked memory required from the system.\n'
        },
        'lv_property': 'Fetch:Data Transfer Block Size',
        'name': 'DATA_TRANSFER_BLOCK_SIZE',
        'type': 'ViInt32'
    },
    1150318: {
        'access': 'read-write',
        'documentation': {
            'description': '\nEnables the bandpass filter on the specificed channel.  The default value is FALSE.\n'
        },
        'lv_property': 'Vertical:Advanced:Bandpass Filter Enabled',
        'name': 'BANDPASS_FILTER_ENABLED',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViBoolean'
    },
    1150321: {
        'access': 'read-write',
        'documentation': {
            'description': '\nThis property specifies the maximum bandwidth that the device is allowed to consume.\n'
        },
        'lv_property': 'Fetch:Advanced:Maximum Bandwidth',
        'name': 'DATA_TRANSFER_MAXIMUM_BANDWIDTH',
        'type': 'ViReal64'
    },
    1150322: {
        'access': 'read-write',
        'documentation': {
            'description': '\nThis property specifies the size of (read request|memory write) data payload. Due to alignment of the data buffers, the hardware may not always generate a packet of this size.\n'
        },
        'lv_property': 'Fetch:Advanced:Preferred Packet Size',
        'name': 'DATA_TRANSFER_PREFERRED_PACKET_SIZE',
        'type': 'ViInt32'
    },
    1150366: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': '\nEnd of Record to Advance Trigger Holdoff is the length of time (in\nseconds) that a device waits between the completion of one record and\nthe acquisition of pre-trigger samples for the next record. During this\ntime, the acquisition engine state delays the transition to the Wait for\nAdvance Trigger state, and will not store samples in onboard memory,\naccept an Advance Trigger, or trigger on the input signal..\n**Supported Devices**: NI 5185/5186\n'
        },
        'lv_property': 'Triggering:End of Record to Advance Trigger Holdoff',
        'name': 'END_OF_RECORD_TO_ADVANCE_TRIGGER_HOLDOFF',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150367: {
        'access': 'read-write',
        'documentation': {
            'description': '\nIf NISCOPE_ATTR_SAMP_CLK_TIMEBASE_SRC is an external source, this property specifies the ratio between the NISCOPE_ATTR_SAMP_CLK_TIMEBASE_RATE and the actual sample rate, which can be higher. This property can be used in conjunction with NISCOPE_ATTR_SAMP_CLK_TIMEBASE_DIV.\nSome devices use multiple ADCs to sample the same channel at an effective sample rate that is greater than the specified clock rate. When providing an external sample clock use this property to indicate when you want a higher sample rate. Valid values for this property vary by device and current configuration.\n\n**Related topics:**\n`Sample Clock <digitizers.chm::/Sample_Clock.html>`__\n'
        },
        'name': 'SAMP_CLK_TIMEBASE_MULT',
        'python_name': 'sample_clock_timebase_multiplier',
        'type': 'ViInt32'
    },
    1150374: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': '\nGets or sets the absolute time offset of the sample clock relative to\nthe reference clock in terms of seconds.\n',
            'note': '\nConfigures the sample clock relationship with respect to the reference\nclock. This parameter is factored into NI-TClk adjustments and is\ntypically used to improve the repeatability of NI-TClk Synchronization.\nWhen this parameter is read, the currently programmed value is returned.\nThe range of the absolute sample clock offset is [-.5 sample clock\nperiods, .5 sample clock periods]. The default absolute sample clock\noffset is 0s.\n'
        },
        'lv_property': 'Clocking:Advanced:Absolute Sample Clock Offset',
        'name': 'ABSOLUTE_SAMPLE_CLOCK_OFFSET',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150375: {
        'access': 'read only',
        'documentation': {
            'description': 'Gets the absolute file path to the bitfile loaded on the FPGA.',
            'note': 'Gets the absolute file path to the bitfile loaded on the FPGA.'
        },
        'lv_property': 'Device:FPGA Bitfile Path',
        'name': 'FPGA_BITFILE_PATH',
        'type': 'ViString'
    },
    1150376: {
        'access': 'read-write',
        'documentation': {
            'description': '\nEnables the interleaving offset correction on the specified channel. The\ndefault value is TRUE.\n**Related topics:**\n`Timed Interleaved\nSampling <digitizers.chm::/TimeInterleavedSampling.html>`__\n',
            'note': 'If disabled, warranted specifications are not guaranteed.'
        },
        'lv_property': 'Vertical:Advanced:Interleaving Offset Correction Enabled',
        'name': 'INTERLEAVING_OFFSET_CORRECTION_ENABLED',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViBoolean'
    },
    1150377: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the frequency for the highpass filter in Hz. The device uses\none of the valid values listed below. If an invalid value is specified,\nno coercion occurs. The default value is 0.\n**(PXIe-5164) Valid Values:**\n0 90 450\n**Related topics:**\n`Digital Filtering <digitizers.chm::/Digital_Filtering_Overview.html>`__\n'
        },
        'lv_property': 'Vertical:Advanced:High Pass Filter Frequency',
        'name': 'HIGH_PASS_FILTER_FREQUENCY',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1151303: {
        'access': 'read only',
        'documentation': {
            'description': '\nIf TRUE, the PLL has remained locked to the external reference clock since it was last checked. If FALSE,  the PLL has become unlocked from the external reference clock since it was last checked.\n'
        },
        'lv_property': 'Clocking:PLL Lock Status',
        'name': 'PLL_LOCK_STATUS',
        'supported_rep_caps': [
            'instruments'
        ],
        'type': 'ViBoolean'
    },
    1250001: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the absolute value of the input range for a channel in volts.  For example, to acquire a sine wave that spans between -5 and +5 V, set this attribute to 10.0 V.\nRefer to the NI High-Speed Digitizers Help for a list of supported vertical ranges for each device.  If the specified range is not supported by a device, the value is coerced up to the next valid range.\n'
        },
        'lv_property': 'Vertical:Vertical Range',
        'name': 'VERTICAL_RANGE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250002: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the location of the center of the range. The value is with respect to ground and is in volts.  For example, to acquire a sine wave that spans between 0.0 and 10.0 V, set this attribute to 5.0 V.\n',
            'note': 'This attribute is not supported by all digitizers.Refer to the NI High-Speed Digitizers Help for a list of vertical offsets supported for each device.'
        },
        'lv_property': 'Vertical:Vertical Offset',
        'name': 'VERTICAL_OFFSET',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250003: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies how the digitizer couples the input signal for the channel.  When input coupling changes, the input stage takes a finite amount of time to settle.\n'
        },
        'enum': 'VerticalCoupling',
        'lv_property': 'Vertical:Vertical Coupling',
        'name': 'VERTICAL_COUPLING',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1250004: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the probe attenuation for the input channel. For example, for a 10:1 probe,  set this attribute to 10.0.\nValid Values:\nAny positive real number. Typical values are 1, 10, and 100.\n'
        },
        'lv_property': 'Vertical:Probe Attenuation',
        'name': 'PROBE_ATTENUATION',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250005: {
        'access': 'read-write',
        'documentation': {
            'description': "\nSpecifies whether the digitizer acquires a waveform for the channel.\nValid Values:\nVI_TRUE  (1) - Acquire data on this channel\nVI_FALSE (0) - Don't acquire data on this channel\n"
        },
        'lv_property': 'Vertical:Channel Enabled',
        'name': 'CHANNEL_ENABLED',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViBoolean'
    },
    1250006: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the bandwidth of the channel. Express this value as the frequency at which the input circuitry attenuates the input signal by 3 dB. The units are hertz.\nDefined Values:\nNISCOPE_VAL_BANDWIDTH_FULL (-1.0)\nNISCOPE_VAL_BANDWIDTH_DEVICE_DEFAULT (0.0)\nNISCOPE_VAL_20MHZ_BANDWIDTH (20000000.0)\nNISCOPE_VAL_100MHZ_BANDWIDTH (100000000.0)\nNISCOPE_VAL_20MHZ_MAX_INPUT_FREQUENCY (20000000.0)\nNISCOPE_VAL_100MHZ_MAX_INPUT_FREQUENCY (100000000.0)\n'
        },
        'lv_property': 'Vertical:Maximum Input Frequency',
        'name': 'MAX_INPUT_FREQUENCY',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250007: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': '\nSpecifies the length of time that corresponds to the record length.\nUnits: Seconds\n'
        },
        'lv_property': 'Horizontal:Advanced:Time Per Record',
        'name': 'HORZ_TIME_PER_RECORD',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1250008: {
        'access': 'read only',
        'documentation': {
            'description': '\nReturns the actual number of points the digitizer acquires for each channel.  The value is equal to or greater than the minimum number of points you specify with NISCOPE_ATTR_HORZ_MIN_NUM_PTS.\nAllocate a ViReal64 array of this size or greater to pass as the WaveformArray parameter of the Read and Fetch functions. This attribute is only valid after a call to the one of the Configure Horizontal functions.\n'
        },
        'lv_property': 'Horizontal:Actual Record Length',
        'name': 'HORZ_RECORD_LENGTH',
        'type': 'ViInt32'
    },
    1250009: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the minimum number of points you require in the waveform record for each channel.  NI-SCOPE uses the value you specify to configure the record length that the digitizer uses for waveform acquisition. NISCOPE_ATTR_HORZ_RECORD_LENGTH returns the actual record length.\nValid Values: 1 - available onboard memory\n'
        },
        'lv_property': 'Horizontal:Min Number of Points',
        'name': 'HORZ_MIN_NUM_PTS',
        'type': 'ViInt32'
    },
    1250010: {
        'access': 'read only',
        'documentation': {
            'description': '\nReturns the effective sample rate using the current configuration. The units are samples per second.  This attribute is only valid after a call to the one of the Configure Horizontal functions.\nUnits: Hertz (Samples / Second)\n'
        },
        'lv_property': 'Horizontal:Actual Sample Rate',
        'name': 'HORZ_SAMPLE_RATE',
        'type': 'ViReal64'
    },
    1250011: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the position of the Reference Event in the waveform record.  When the digitizer detects a trigger, it waits the length of time the NISCOPE_ATTR_TRIGGER_DELAY_TIME attribute specifies. The event that occurs when the delay time elapses is the Reference Event. The Reference Event is relative to the start of the record and is a percentage of the record length. For example, the value 50.0 corresponds to the center of the waveform record and 0.0 corresponds to the first element in the waveform record.\nValid Values: 0.0 - 100.0\n'
        },
        'lv_property': 'Horizontal:Reference Position',
        'name': 'HORZ_RECORD_REF_POSITION',
        'type': 'ViReal64'
    },
    1250012: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the type of trigger to use.\n'
        },
        'enum': 'TriggerType',
        'lv_property': 'Triggering:Trigger Type',
        'name': 'TRIGGER_TYPE',
        'type': 'ViInt32'
    },
    1250013: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the source the digitizer monitors for the trigger event.\n'
        },
        'lv_property': 'Triggering:Trigger Source',
        'name': 'TRIGGER_SOURCE',
        'type': 'ViString'
    },
    1250014: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies how the digitizer couples the trigger source. This attribute affects instrument operation only when NISCOPE_ATTR_TRIGGER_TYPE is set to NISCOPE_VAL_EDGE_TRIGGER, NISCOPE_VAL_HYSTERESIS_TRIGGER, or NISCOPE_VAL_WINDOW_TRIGGER.\n'
        },
        'enum': 'TriggerCoupling',
        'lv_property': 'Triggering:Trigger Coupling',
        'name': 'TRIGGER_COUPLING',
        'type': 'ViInt32'
    },
    1250015: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': '\nSpecifies the trigger delay time in seconds. The trigger delay time is the length of time the digitizer waits after it receives the trigger. The event that occurs when the trigger delay elapses is the Reference Event.\nValid Values: 0.0 - 171.8\n'
        },
        'lv_property': 'Triggering:Trigger Delay',
        'name': 'TRIGGER_DELAY_TIME',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1250016: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': '\nSpecifies the length of time (in seconds) the digitizer waits after detecting a trigger before enabling the trigger subsystem to detect another trigger. This attribute affects instrument operation only when the digitizer requires multiple acquisitions to build a complete waveform. The digitizer requires multiple waveform acquisitions when it uses equivalent-time sampling or when the digitizer is configured for a multi-record acquisition through a call to niScope_ConfigureHorizontalTiming.\nValid Values: 0.0 - 171.8\n'
        },
        'lv_property': 'Triggering:Trigger Holdoff',
        'name': 'TRIGGER_HOLDOFF',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1250017: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the voltage threshold for the trigger subsystem. The units are volts.  This attribute affects instrument behavior only when the NISCOPE_ATTR_TRIGGER_TYPE is set to NISCOPE_VAL_EDGE_TRIGGER, NISCOPE_VAL_HYSTERESIS_TRIGGER, or NISCOPE_VAL_WINDOW_TRIGGER.\nValid Values:\nThe values of the range and offset parameters in niScope_ConfigureVertical determine the valid range for the trigger level on the channel you use as the Trigger Source. The value you pass for this parameter must meet the following conditions:\n'
        },
        'lv_property': 'Triggering:Trigger Level',
        'name': 'TRIGGER_LEVEL',
        'type': 'ViReal64'
    },
    1250018: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies if a rising or a falling edge triggers the digitizer.  This attribute affects instrument operation only when NISCOPE_ATTR_TRIGGER_TYPE is set to NISCOPE_VAL_EDGE_TRIGGER, NISCOPE_VAL_HYSTERESIS_TRIGGER, or NISCOPE_VAL_WINDOW_TRIGGER.\n'
        },
        'enum': 'TriggerSlope',
        'lv_property': 'Triggering:Trigger Slope',
        'name': 'TRIGGER_SLOPE',
        'type': 'ViInt32'
    },
    1250101: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies how the digitizer acquires data and fills the waveform record.\n'
        },
        'enum': 'AcquisitionType',
        'lv_property': 'Acquisition:Acquisition Type',
        'name': 'ACQUISITION_TYPE',
        'type': 'ViInt32'
    },
    1250102: {
        'access': 'read-write',
        'documentation': {
            'description': '\nConfigures the device to automatically complete an acquisition if a trigger has not been received.\nValid Values:\nNone (1)         - Normal triggering\nAuto Trigger (2) - Auto trigger acquisition if no trigger arrives\n'
        },
        'enum': 'TriggerModifier',
        'lv_property': 'Triggering:Trigger Modifier',
        'name': 'TRIGGER_MODIFIER',
        'type': 'ViInt32'
    },
    1250103: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the input impedance for the channel in Ohms.\n'
        },
        'lv_property': 'Vertical:Input Impedance',
        'name': 'INPUT_IMPEDANCE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250106: {
        'access': 'read only',
        'documentation': {
            'description': '\nIndicates the sample mode the digitizer is currently using.\n'
        },
        'lv_property': 'Acquisition:Sample Mode',
        'name': 'SAMPLE_MODE',
        'type': 'ViInt32'
    },
    1250109: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': '\nSpecifies the length of time from the trigger event to the first point in the waveform record in seconds.  If the value is positive, the first point in the waveform record occurs after the trigger event (same as specifying NISCOPE_ATTR_TRIGGER_DELAY_TIME).  If the value is negative, the first point in the waveform record occurs before the trigger event (same as specifying NISCOPE_ATTR_HORZ_RECORD_REF_POSITION).\n'
        },
        'lv_property': 'Horizontal:Advanced:Acquisition Start Time',
        'name': 'ACQUISITION_START_TIME',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1250201: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the type of video signal, such as NTSC, PAL, or SECAM.\n'
        },
        'enum': 'VideoSignalFormat',
        'lv_property': 'Triggering:Trigger Video:Signal Format',
        'name': 'TV_TRIGGER_SIGNAL_FORMAT',
        'type': 'ViInt32'
    },
    1250204: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether the video signal sync is positive or negative.\n'
        },
        'enum': 'VideoPolarity',
        'lv_property': 'Triggering:Trigger Video:Polarity',
        'name': 'TV_TRIGGER_POLARITY',
        'type': 'ViInt32'
    },
    1250205: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the condition in the video signal that causes the digitizer to trigger.\n'
        },
        'enum': 'VideoTriggerEvent',
        'lv_property': 'Triggering:Trigger Video:Event',
        'name': 'TV_TRIGGER_EVENT',
        'type': 'ViInt32'
    },
    1250206: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the line on which to trigger, if NISCOPE_ATTR_TV_TRIGGER_EVENT is set to line number. The valid ranges of the attribute depend on the signal format selected.  M-NTSC has a valid range of 1 to 525.  B/G-PAL, SECAM, 576i, and 576p have a valid range of 1 to 625. 720p has a valid range of 1 to 750. 1080i and 1080p have a valid range of 1125.\n'
        },
        'lv_property': 'Triggering:Trigger Video:Line Number',
        'name': 'TV_TRIGGER_LINE_NUMBER',
        'type': 'ViInt32'
    },
    1250301: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the higher of two thresholds, in volts, that bound the vertical range to examine for runt pulses.\n\nThe runt threshold that causes the oscilloscope to trigger depends on the runt polarity you select. Refer to the NISCOPE_ATTR_RUNT_POLARITY attribute for more information.\n'
        },
        'name': 'RUNT_HIGH_THRESHOLD',
        'type': 'ViReal64'
    },
    1250302: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the lower of two thresholds, in volts, that bound the vertical range to examine for runt pulses.\n\nThe runt threshold that causes the oscilloscope to trigger depends on the runt polarity you select. Refer to the NISCOPE_ATTR_RUNT_POLARITY attribute for more information.\n'
        },
        'name': 'RUNT_LOW_THRESHOLD',
        'type': 'ViReal64'
    },
    1250303: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the polarity of pulses that trigger the oscilloscope for runt triggering.\n\nWhen set to NISCOPE_VAL_RUNT_POSITIVE, the oscilloscope triggers when the following conditions are met:\n    * The leading edge of a pulse crosses the NISCOPE_ATTR_RUNT_LOW_THRESHOLD in a positive direction;\n    * The trailing edge of the pulse crosses the NISCOPE_ATTR_RUNT_LOW_THRESHOLD in a negative direction; and\n    * No portion of the pulse crosses the NISCOPE_ATTR_RUNT_HIGH_THRESHOLD.\n\nWhen set to NISCOPE_VAL_RUNT_NEGATIVE, the oscilloscope triggers when the following conditions are met:\n    * The leading edge of a pulse crosses the NISCOPE_ATTR_RUNT_HIGH_THRESHOLD in a negative direction;\n    * The trailing edge of the pulse crosses the NISCOPE_ATTR_RUNT_HIGH_THRESHOLD in a positive direction; and\n    * No portion of the pulse crosses the NISCOPE_ATTR_RUNT_LOW_THRESHOLD.\n\nWhen set to NISCOPE_VAL_RUNT_EITHER, the oscilloscope triggers in either case.'
        },
        'enum': 'RuntPolarity',
        'name': 'RUNT_POLARITY',
        'type': 'ViInt32'
    },
    1250401: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the glitch duration, in seconds.\n\nThe oscilloscope triggers when it detects of pulse of duration either less than or greater than this value depending on the value of the NISCOPE_ATTR_GLITCH_CONDITION attribute.'
        },
        'name': 'GLITCH_WIDTH',
        'type': 'ViReal64'
    },
    1250402: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the polarity of pulses that trigger the oscilloscope for glitch triggering.'
        },
        'enum': 'GlitchPolarity',
        'name': 'GLITCH_POLARITY',
        'type': 'ViInt32'
    },
    1250403: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies whether the oscilloscope triggers on pulses of duration less than or greater than the value specified by the NISCOPE_ATTR_GLITCH_WIDTH attribute.'
        },
        'enum': 'GlitchCondition',
        'name': 'GLITCH_CONDITION',
        'type': 'ViInt32'
    },
    1250501: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the low width threshold, in seconds.\n\nThis attribute sets the lower bound on the duration range that triggers the oscilloscope. The NISCOPE_ATTR_WIDTH_CONDITION attribute determines how the oscilloscope triggers in relation to the width thresholds.\n'
        },
        'name': 'WIDTH_LOW_THRESHOLD',
        'type': 'ViReal64'
    },
    1250502: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the high width threshold, in seconds.\n\nThis attributes sets the upper bound on the duration range that triggers the oscilloscope. The NISCOPE_ATTR_WIDTH_CONDITION attribute determines how the oscilloscope triggers in relation to the width thresholds.\n'
        },
        'name': 'WIDTH_HIGH_THRESHOLD',
        'type': 'ViReal64'
    },
    1250503: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the polarity of pulses that trigger the oscilloscope for width triggering.\n'
        },
        'enum': 'WidthPolarity',
        'name': 'WIDTH_POLARITY',
        'type': 'ViInt32'
    },
    1250504: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether the oscilloscope triggers on pulses within or outside the duration range bounded by the NISCOPE_ATTR_WIDTH_LOW_THRESHOLD and NISCOPE_ATTR_WIDTH_HIGH_THRESHOLD attributes.\n'
        },
        'enum': 'WidthCondition',
        'name': 'WIDTH_CONDITION',
        'type': 'ViInt32'
    },
    1250607: {
        'access': 'read-write',
        'codegen_method': 'public',
        'name': 'MEAS_HIGH_REF',
        'type': 'ViReal64'
    },
    1250608: {
        'access': 'read-write',
        'codegen_method': 'public',
        'name': 'MEAS_LOW_REF',
        'type': 'ViReal64'
    },
    1250609: {
        'access': 'read-write',
        'codegen_method': 'public',
        'name': 'MEAS_MID_REF',
        'type': 'ViReal64'
    }
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/metadata/attributes_addon.py sha256=17a2127d02579d026109ae3070d68b679f75dfef78e81e17ee575a6a80fec153 bytes=201 -->
## FILE: src/niscope/metadata/attributes_addon.py

- repository: `ni/nimi-python`
- source_path: `src/niscope/metadata/attributes_addon.py`
- sha256: `17a2127d02579d026109ae3070d68b679f75dfef78e81e17ee575a6a80fec153`
- bytes: 201

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/metadata/config.py sha256=7c479e1c1b75e10d18ab0fd9e1b898f33838170b486de8394315614153faed98 bytes=1604 -->
## FILE: src/niscope/metadata/config.py

- repository: `ni/nimi-python`
- source_path: `src/niscope/metadata/config.py`
- sha256: `7c479e1c1b75e10d18ab0fd9e1b898f33838170b486de8394315614153faed98`
- bytes: 1604

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-SCOPE API metadata version 25.0.0f151
config = {
    'api_version': '25.0.0f151',
    'c_function_prefix': 'niScope_',
    'close_function': 'close',
    'context_manager_name': {
        'abort_function': 'Abort',
        'initiate_function': 'InitiateAcquisition',
        'task': 'acquisition'
    },
    'custom_types': [
        {
            'ctypes_type': 'struct_niScope_wfmInfo',
            'file_name': 'waveform_info',
            'grpc_name': 'WaveformInfo',
            'python_name': 'WaveformInfo'
        }
    ],
    'driver_name': 'NI-SCOPE',
    'extra_errors_used': [
        'InvalidRepeatedCapabilityError',
        'SelfTestError'
    ],
    'grpc_service_class_prefix': 'NiScope',
    'init_function': 'InitWithOptions',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'niscope',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niScope_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niScope_64.dll',
                'type': 'cdll'
            }
        }
    },
    'module_name': 'niscope',
    'repeated_capabilities': [
        {
            'prefix': '',
            'python_name': 'channels'
        },
        {
            'prefix': '',
            'python_name': 'instruments'
        }
    ],
    'session_class_description': 'An NI-SCOPE session to an NI digitizer.',
    'session_handle_parameter_name': 'vi',
    'uses_nitclk': True
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/metadata/config_addon.py sha256=d4a420ab3044d356d18ec6cac4a89b366bca2177cbc0e6a5cb2de2401a14cb81 bytes=729 -->
## FILE: src/niscope/metadata/config_addon.py

- repository: `ni/nimi-python`
- source_path: `src/niscope/metadata/config_addon.py`
- sha256: `d4a420ab3044d356d18ec6cac4a89b366bca2177cbc0e6a5cb2de2401a14cb81`
- bytes: 729

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.4.10.dev0',
    'latest_runtime_version_tested_against': '2025 Q4',
    'initial_release_year': '2017',
    'custom_types': [
        # Redundant, since waveform_info is also in the base config.py file. See issue 1495 (https://github.com/ni/nimi-python/issues/1495) 
        {
            'ctypes_type': 'struct_niScope_wfmInfo',
            'file_name': 'waveform_info',
            'python_name': 'WaveformInfo'
        },
        {
            'ctypes_type': '',
            'file_name': 'measurement_stats',
            'python_name': 'MeasurementStats'
        }
    ]
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/metadata/enums.py sha256=b870fcd857227a23758729e020d59cf9690b5a4bb70b1bf70c4feffed129f2df bytes=94419 -->
## FILE: src/niscope/metadata/enums.py

- repository: `ni/nimi-python`
- source_path: `src/niscope/metadata/enums.py`
- sha256: `b870fcd857227a23758729e020d59cf9690b5a4bb70b1bf70c4feffed129f2df`
- bytes: 94419

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-SCOPE API metadata version 25.0.0f151
enums = {
    '5900AccessoryInAScopeSessionValues': {
        'values': [
            {
                'name': 'NISCOPE_VAL_ACCESSORY_DRIVER_SETUP_OPTION',
                'value': 'Accessory'
            },
            {
                'name': 'NISCOPE_VAL_ACCESSORY_DRIVER_SETUP_ACCMODEL',
                'value': 'AccModel'
            },
            {
                'name': 'NISCOPE_VAL_ACCESSORY_DRIVER_SETUP_ACCBUS',
                'value': 'AccBoardType'
            },
            {
                'name': 'NISCOPE_VAL_ACCESSORY_DRIVER_SETUP_DEFAULT_MODEL',
                'value': '5900'
            },
            {
                'name': 'NISCOPE_VAL_ACCESSORY_DRIVER_SETUP_DEFAULT_BUS',
                'value': 'PXI'
            },
            {
                'name': 'NISCOPE_VAL_ACCESSORY_DIGITIZER_IMPEDANCE',
                'value': 1000000.0
            },
            {
                'name': 'NISCOPE_VAL_ACCESSORY_5900_SCALE_FACTOR',
                'value': 4.0
            }
        ]
    },
    'AccessoryTypes': {
        'values': [
            {
                'name': 'NISCOPE_VAL_ACCESSORY_TYPE_NONE',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_ACCESSORY_TYPE_5900',
                'value': 1
            }
        ]
    },
    'AcquisitionStatus': {
        'values': [
            {
                'name': 'NISCOPE_VAL_ACQ_COMPLETE',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_ACQ_IN_PROGRESS',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_ACQ_STATUS_UNKNOWN',
                'value': -1
            }
        ]
    },
    'AcquisitionType': {
        'values': [
            {
                'documentation': {
                    'description': 'Sets the digitizer to normal resolution mode. The digitizer can use real-time sampling or equivalent-time sampling.'
                },
                'name': 'NISCOPE_VAL_NORMAL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Sets the digitizer to flexible resolution mode if supported.  The digitizer uses different hardware configurations to change the resolution depending on the sampling rate used.'
                },
                'name': 'NISCOPE_VAL_FLEXRES',
                'value': 1001
            },
            {
                'documentation': {
                    'description': 'Sets the digitizer to DDC mode on the NI 5620/5621.'
                },
                'name': 'NISCOPE_VAL_DDC',
                'value': 1002
            }
        ]
    },
    'AddressType': {
        'values': [
            {
                'documentation': {
                    'description': 'Physical address.'
                },
                'name': 'NISCOPE_VAL_ADDR_PHYSICAL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Virtual address.'
                },
                'name': 'NISCOPE_VAL_ADDR_VIRTUAL',
                'value': 1
            }
        ]
    },
    'AgcAverageControl': {
        'values': [
            {
                'documentation': {
                    'description': 'Mean average.'
                },
                'name': 'NISCOPE_VAL_MEAN',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Median average.'
                },
                'name': 'NISCOPE_VAL_MEDIAN',
                'value': 1
            }
        ]
    },
    'AoutParallelOutputSource': {
        'values': [
            {
                'documentation': {
                    'description': '\nSpecifies I data as the source for the AOUT parallel output from the\nDDC.\n'
                },
                'name': 'NISCOPE_VAL_I_DATA',
                'value': 0
            },
            {
                'documentation': {
                    'description': '\nSpecifies magnitude data as the source for the AOUT parallel output from\nthe DDC.\n'
                },
                'name': 'NISCOPE_VAL_MAGNITUDE_DATA',
                'value': 1
            },
            {
                'documentation': {
                    'description': '\nSpecifies frequency data as the source for the AOUT parallel output from\nthe DDC.\n'
                },
                'name': 'NISCOPE_VAL_FREQUENCY_DATA',
                'value': 2
            }
        ]
    },
    'ArrayMeasurement': {
        'values': [
            {
                'documentation': {
                    'description': 'None'
                },
                'name': 'NISCOPE_VAL_NO_MEASUREMENT',
                'value': 4000
            },
            {
                'documentation': {
                    'description': 'Last Acquisition Histogram '
                },
                'name': 'NISCOPE_VAL_LAST_ACQ_HISTOGRAM',
                'value': 4001
            },
            {
                'documentation': {
                    'description': 'FFT Phase Spectrum'
                },
                'name': 'NISCOPE_VAL_FFT_PHASE_SPECTRUM',
                'value': 4002
            },
            {
                'documentation': {
                    'description': 'FFT Amp. Spectrum (Volts RMS)'
                },
                'name': 'NISCOPE_VAL_FFT_AMP_SPECTRUM_VOLTS_RMS',
                'value': 4003
            },
            {
                'documentation': {
                    'description': 'Multi Acquisition Voltage Histogram'
                },
                'name': 'NISCOPE_VAL_MULTI_ACQ_VOLTAGE_HISTOGRAM',
                'value': 4004
            },
            {
                'documentation': {
                    'description': 'Multi Acquisition Time Histogram'
                },
                'name': 'NISCOPE_VAL_MULTI_ACQ_TIME_HISTOGRAM',
                'value': 4005
            },
            {
                'documentation': {
                    'description': 'Array Integral'
                },
                'name': 'NISCOPE_VAL_ARRAY_INTEGRAL',
                'value': 4006
            },
            {
                'documentation': {
                    'description': 'Derivative'
                },
                'name': 'NISCOPE_VAL_DERIVATIVE',
                'value': 4007
            },
            {
                'documentation': {
                    'description': 'Inverse'
                },
                'name': 'NISCOPE_VAL_INVERSE',
                'value': 4008
            },
            {
                'documentation': {
                    'description': 'Hanning Window'
                },
                'name': 'NISCOPE_VAL_HANNING_WINDOW',
                'value': 4009
            },
            {
                'documentation': {
                    'description': 'Flat Top Window'
                },
                'name': 'NISCOPE_VAL_FLAT_TOP_WINDOW',
                'value': 4010
            },
            {
                'documentation': {
                    'description': 'Polynomial Interpolation'
                },
                'name': 'NISCOPE_VAL_POLYNOMIAL_INTERPOLATION',
                'value': 4011
            },
            {
                'documentation': {
                    'description': 'Multiply Channels'
                },
                'name': 'NISCOPE_VAL_MULTIPLY_CHANNELS',
                'value': 4012
            },
            {
                'documentation': {
                    'description': 'Add Channels'
                },
                'name': 'NISCOPE_VAL_ADD_CHANNELS',
                'value': 4013
            },
            {
                'documentation': {
                    'description': 'Subtract Channels'
                },
                'name': 'NISCOPE_VAL_SUBTRACT_CHANNELS',
                'value': 4014
            },
            {
                'documentation': {
                    'description': 'Divide Channels'
                },
                'name': 'NISCOPE_VAL_DIVIDE_CHANNELS',
                'value': 4015
            },
            {
                'documentation': {
                    'description': 'Multi Acquisition Average'
                },
                'name': 'NISCOPE_VAL_MULTI_ACQ_AVERAGE',
                'value': 4016
            },
            {
                'documentation': {
                    'description': 'Butterworth IIR Filter'
                },
                'name': 'NISCOPE_VAL_BUTTERWORTH_FILTER',
                'value': 4017
            },
            {
                'documentation': {
                    'description': 'Chebyshev IIR Filter'
                },
                'name': 'NISCOPE_VAL_CHEBYSHEV_FILTER',
                'value': 4018
            },
            {
                'documentation': {
                    'description': 'FFT Amp. Spectrum (dB)'
                },
                'name': 'NISCOPE_VAL_FFT_AMP_SPECTRUM_DB',
                'value': 4019
            },
            {
                'documentation': {
                    'description': 'Hamming Window'
                },
                'name': 'NISCOPE_VAL_HAMMING_WINDOW',
                'value': 4020
            },
            {
                'documentation': {
                    'description': 'FIR Windowed Filter'
                },
                'name': 'NISCOPE_VAL_WINDOWED_FIR_FILTER',
                'value': 4021
            },
            {
                'documentation': {
                    'description': 'Bessel IIR Filter'
                },
                'name': 'NISCOPE_VAL_BESSEL_FILTER',
                'value': 4022
            },
            {
                'documentation': {
                    'description': 'Triangle Window'
                },
                'name': 'NISCOPE_VAL_TRIANGLE_WINDOW',
                'value': 4023
            },
            {
                'documentation': {
                    'description': 'Blackman Window'
                },
                'name': 'NISCOPE_VAL_BLACKMAN_WINDOW',
                'value': 4024
            },
            {
                'documentation': {
                    'description': 'Array Offset'
                },
                'name': 'NISCOPE_VAL_ARRAY_OFFSET',
                'value': 4025
            },
            {
                'documentation': {
                    'description': 'Array Gain'
                },
                'name': 'NISCOPE_VAL_ARRAY_GAIN',
                'value': 4026
            }
        ]
    },
    'AttributeRetrievalModes': {
        'values': [
            {
                'name': 'NISCOPE_VAL_ATTRIBUTE_RETRIEVAL_MODE_COERCED',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_ATTRIBUTE_RETRIEVAL_MODE_DESIRED',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_ATTRIBUTE_RETRIEVAL_MODE_DEFAULT',
                'value': 2
            }
        ]
    },
    'BoutParallelOutputSource': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies magnitude data as the source.'
                },
                'name': 'NISCOPE_VAL_MAGNITUDE_DATA',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Specifies Q data as the source.'
                },
                'name': 'NISCOPE_VAL_Q_DATA',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Specifies phase data as the source.'
                },
                'name': 'NISCOPE_VAL_PHASE_DATA',
                'value': 4
            }
        ]
    },
    'CableSenseMode': {
        'values': [
            {
                'documentation': {
                    'description': 'The oscilloscope is not configured to emit a CableSense signal.'
                },
                'name': 'NISCOPE_VAL_CABLE_SENSE_MODE_DISABLED',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The oscilloscope is configured to emit a single CableSense pulse.'
                },
                'name': 'NISCOPE_VAL_CABLE_SENSE_MODE_ON_DEMAND',
                'value': 1
            }
        ]
    },
    'CalEndActions': {
        'values': [
            {
                'name': 'NISCOPE_VAL_CAL_ACTION_STORE',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_CAL_ACTION_ABORT',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_CAL_ACTION_RESET',
                'value': 101
            }
        ]
    },
    'CalibrationAccessorySources': {
        'values': [
            {
                'name': 'NISCOPE_VAL_CAL_SOURCE_GROUND',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_CAL_SOURCE_POSITIVEFS',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_CAL_SOURCE_NEGATIVEFS',
                'value': 2
            }
        ]
    },
    'CalibrationOptions': {
        'values': [
            {
                'name': 'NISCOPE_VAL_CALIBRATE_LINEARITY',
                'value': 102
            }
        ]
    },
    'CalibrationTypes': {
        'values': [
            {
                'name': 'NISCOPE_VAL_CAL_SELF',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_CAL_EXTERNAL',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_CAL_MANUFACTURE',
                'value': 2
            }
        ]
    },
    'ClearableMeasurement': {
        'values': [
            {
                'name': 'NISCOPE_VAL_ALL_MEASUREMENTS',
                'value': 10000
            },
            {
                'name': 'NISCOPE_VAL_MULTI_ACQ_VOLTAGE_HISTOGRAM',
                'value': 4004
            },
            {
                'name': 'NISCOPE_VAL_MULTI_ACQ_TIME_HISTOGRAM',
                'value': 4005
            },
            {
                'name': 'NISCOPE_VAL_MULTI_ACQ_AVERAGE',
                'value': 4016
            },
            {
                'name': 'NISCOPE_VAL_FREQUENCY',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_AVERAGE_FREQUENCY',
                'value': 1016
            },
            {
                'name': 'NISCOPE_VAL_FFT_FREQUENCY',
                'value': 1008
            },
            {
                'name': 'NISCOPE_VAL_PERIOD',
                'value': 3
            },
            {
                'name': 'NISCOPE_VAL_AVERAGE_PERIOD',
                'value': 1015
            },
            {
                'name': 'NISCOPE_VAL_RISE_TIME',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_FALL_TIME',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_RISE_SLEW_RATE',
                'value': 1010
            },
            {
                'name': 'NISCOPE_VAL_FALL_SLEW_RATE',
                'value': 1011
            },
            {
                'name': 'NISCOPE_VAL_OVERSHOOT',
                'value': 18
            },
            {
                'name': 'NISCOPE_VAL_PRESHOOT',
                'value': 19
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_RMS',
                'value': 4
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_CYCLE_RMS',
                'value': 16
            },
            {
                'name': 'NISCOPE_VAL_AC_ESTIMATE',
                'value': 1012
            },
            {
                'name': 'NISCOPE_VAL_FFT_AMPLITUDE',
                'value': 1009
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_AVERAGE',
                'value': 10
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_CYCLE_AVERAGE',
                'value': 17
            },
            {
                'name': 'NISCOPE_VAL_DC_ESTIMATE',
                'value': 1013
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_MAX',
                'value': 6
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_MIN',
                'value': 7
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_PEAK_TO_PEAK',
                'value': 5
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HIGH',
                'value': 8
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_LOW',
                'value': 9
            },
            {
                'name': 'NISCOPE_VAL_AMPLITUDE',
                'value': 15
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_TOP',
                'value': 1007
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_BASE',
                'value': 1006
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_BASE_TO_TOP',
                'value': 1017
            },
            {
                'name': 'NISCOPE_VAL_WIDTH_NEG',
                'value': 11
            },
            {
                'name': 'NISCOPE_VAL_WIDTH_POS',
                'value': 12
            },
            {
                'name': 'NISCOPE_VAL_DUTY_CYCLE_NEG',
                'value': 13
            },
            {
                'name': 'NISCOPE_VAL_DUTY_CYCLE_POS',
                'value': 14
            },
            {
                'name': 'NISCOPE_VAL_INTEGRAL',
                'value': 1005
            },
            {
                'name': 'NISCOPE_VAL_AREA',
                'value': 1003
            },
            {
                'name': 'NISCOPE_VAL_CYCLE_AREA',
                'value': 1004
            },
            {
                'name': 'NISCOPE_VAL_TIME_DELAY',
                'value': 1014
            },
            {
                'name': 'NISCOPE_VAL_PHASE_DELAY',
                'value': 1018
            },
            {
                'name': 'NISCOPE_VAL_LOW_REF_VOLTS',
                'value': 1000
            },
            {
                'name': 'NISCOPE_VAL_MID_REF_VOLTS',
                'value': 1001
            },
            {
                'name': 'NISCOPE_VAL_HIGH_REF_VOLTS',
                'value': 1002
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN',
                'value': 2000
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_STDEV',
                'value': 2001
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEDIAN',
                'value': 2003
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MODE',
                'value': 2010
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MAX',
                'value': 2005
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MIN',
                'value': 2006
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_PEAK_TO_PEAK',
                'value': 2002
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_STDEV',
                'value': 2007
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_2_STDEV',
                'value': 2008
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_3_STDEV',
                'value': 2009
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_HITS',
                'value': 2004
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_NEW_HITS',
                'value': 2011
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MEAN',
                'value': 3000
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_STDEV',
                'value': 3001
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MEDIAN',
                'value': 3003
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MODE',
                'value': 3010
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MAX',
                'value': 3005
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MIN',
                'value': 3006
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_PEAK_TO_PEAK',
                'value': 3002
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_STDEV',
                'value': 3007
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_2_STDEV',
                'value': 3008
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_3_STDEV',
                'value': 3009
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_HITS',
                'value': 3004
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_NEW_HITS',
                'value': 3011
            }
        ]
    },
    'ClockingTerminalValues': {
        'values': [
            {
                'name': 'NISCOPE_VAL_NO_SOURCE',
                'value': 'VAL_NO_SOURCE'
            },
            {
                'name': 'NISCOPE_VAL_RTSI_CLOCK',
                'value': 'VAL_RTSI_CLOCK'
            },
            {
                'name': 'NISCOPE_VAL_EXTERNAL',
                'value': 'VAL_EXTERNAL'
            },
            {
                'name': 'NISCOPE_VAL_PFI_0',
                'value': 'VAL_PFI_0'
            },
            {
                'name': 'NISCOPE_VAL_PFI_1',
                'value': 'VAL_PFI_1'
            },
            {
                'name': 'NISCOPE_VAL_PFI_2',
                'value': 'VAL_PFI_2'
            },
            {
                'name': 'NISCOPE_VAL_CLK_IN',
                'value': 'VAL_CLK_IN'
            },
            {
                'name': 'NISCOPE_VAL_CLK_OUT',
                'value': 'VAL_CLK_OUT'
            },
            {
                'name': 'NISCOPE_VAL_INTERNAL10MHZ_OSC',
                'value': 'VAL_INTERNAL10MHZ_OSC'
            },
            {
                'name': 'NISCOPE_VAL_PXI_CLK',
                'value': 'VAL_PXI_CLK'
            },
            {
                'name': 'NISCOPE_VAL_PXI_CLK10',
                'value': 'VAL_PXI_CLK10'
            },
            {
                'name': 'NISCOPE_VAL_PXI_CLK100',
                'value': 'VAL_PXI_CLK100'
            },
            {
                'name': 'NISCOPE_VAL_PXIE_DSTAR_A',
                'value': 'VAL_PXIE_DSTAR_A'
            },
            {
                'name': 'NISCOPE_VAL_AUX_0_CLK_IN',
                'value': 'VAL_AUX_0_CLK_IN'
            },
            {
                'name': 'NISCOPE_VAL_AUX_0_CLK_OUT',
                'value': 'VAL_AUX_0_CLK_OUT'
            },
            {
                'name': 'NISCOPE_VAL_ONBOARD_CONFIGURABLE_RATE_CLK',
                'value': 'VAL_ONBOARD_CONFIGURABLE_RATE_CLK'
            }
        ]
    },
    'CoefficientType': {
        'values': [
            {
                'name': 'NISCOPE_VAL_PFIR_COEFFICIENTS',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_DISCRIMINATOR_FIR_COEFFICIENTS',
                'value': 1
            }
        ]
    },
    'ConfigurationListStepTriggerSources': {
        'values': [
            {
                'name': 'NISCOPE_VAL_END_OF_RECORD_EVENT_STR',
                'value': 'VAL_END_OF_RECORD_EVENT'
            },
            {
                'name': 'NISCOPE_VAL_TIMER_EVENT_STR',
                'value': 'VAL_TIMER_EVENT'
            },
            {
                'name': 'NISCOPE_VAL_START_TRIGGER_STR',
                'value': 'VAL_START_TRIGGER'
            }
        ]
    },
    'ControlBandwidthLimitBandpassFilters': {
        'values': [
            {
                'name': 'NISCOPE_VAL_BANDWIDTH_LIMIT_DEFAULT',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_BANDWIDTH_LIMIT_25MHZ',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_BANDWIDTH_LIMIT_50MHZ',
                'value': 2
            }
        ]
    },
    'CoordinateConverterInput': {
        'values': [
            {
                'documentation': {
                    'description': '\nSelects the HB filter as the source for the input to the coordinate\nconverter.\n'
                },
                'name': 'NISCOPE_VAL_RESAMPLER_HB',
                'value': 0
            },
            {
                'documentation': {
                    'description': '\nSelects the programmable FIR filter as the source for the input to the\ncoordinate converter.\n'
                },
                'name': 'NISCOPE_VAL_PROGRAMMABLE_FIR',
                'value': 1
            }
        ]
    },
    'DDCMuxModes': {
        'values': [
            {
                'name': 'NISCOPE_VAL_MUX_ADC',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_MUX_DDC',
                'value': 1
            }
        ]
    },
    'DataJustificationMode': {
        'values': [
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISCOPE_VAL_LEFT',
                'value': 1
            },
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISCOPE_VAL_RIGHT',
                'value': 2
            }
        ]
    },
    'DataProcessingMode': {
        'values': [
            {
                'documentation': {
                    'description': 'The waveform data points are real numbers (I data).'
                },
                'name': 'NISCOPE_VAL_REAL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The waveform data points are complex numbers (IQ data).'
                },
                'name': 'NISCOPE_VAL_COMPLEX',
                'value': 1
            }
        ]
    },
    'DeviceStatuses': {
        'values': [
            {
                'name': 'NISCOPE_VAL_DEVICE_STATE_UNKNOWN',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_DEVICE_INITIALIZING',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_DEVICE_READY',
                'value': 16
            },
            {
                'name': 'NISCOPE_VAL_DEVICE_RESERVED',
                'value': 256
            }
        ]
    },
    'DiscriminatorFIRInputSource': {
        'values': [
            {
                'documentation': {
                    'description': 'Sets the discriminator FIR input source to phase.'
                },
                'name': 'NISCOPE_VAL_PHASE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Sets the discriminator FIR input source to magnitude.'
                },
                'name': 'NISCOPE_VAL_MAGNITUDE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Sets the discriminator FIR input source to resampler.'
                },
                'name': 'NISCOPE_VAL_RESAMPLER',
                'value': 2
            }
        ]
    },
    'DiscriminatorFIRSymmetry': {
        'values': [
            {
                'documentation': {
                    'description': 'Sets the discriminator FIR symmetry to symmetric.'
                },
                'name': 'NISCOPE_VAL_SYMMETRIC',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Sets the discriminator FIR symmetry to asymmetric.'
                },
                'name': 'NISCOPE_VAL_ASYMMETRIC',
                'value': 1
            }
        ]
    },
    'DiscriminatorFIRSymmetryType': {
        'values': [
            {
                'documentation': {
                    'description': 'Sets the discriminator FIR symmetry type to even.'
                },
                'name': 'NISCOPE_VAL_EVEN',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Sets the discriminator FIR symmetry type to odd.'
                },
                'name': 'NISCOPE_VAL_ODD',
                'value': 1
            }
        ]
    },
    'ExportableSignals': {
        'values': [
            {
                'name': 'NISCOPE_VAL_REF_TRIGGER',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_START_TRIGGER',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_END_OF_ACQUISITION_EVENT',
                'value': 3
            },
            {
                'name': 'NISCOPE_VAL_END_OF_RECORD_EVENT',
                'value': 4
            },
            {
                'name': 'NISCOPE_VAL_ADVANCE_TRIGGER',
                'value': 5
            },
            {
                'name': 'NISCOPE_VAL_READY_FOR_ADVANCE_EVENT',
                'value': 6
            },
            {
                'name': 'NISCOPE_VAL_READY_FOR_START_EVENT',
                'value': 7
            },
            {
                'name': 'NISCOPE_VAL_READY_FOR_REF_EVENT',
                'value': 10
            },
            {
                'name': 'NISCOPE_VAL_5V_OUT',
                'python_name': 'FIVE_V_OUT',
                'value': 13
            },
            {
                'name': 'NISCOPE_VAL_REF_CLOCK',
                'value': 100
            },
            {
                'name': 'NISCOPE_VAL_SAMPLE_CLOCK',
                'value': 101
            }
        ]
    },
    'FIRFilterWindow': {
        'values': [
            {
                'documentation': {
                    'description': 'No window.'
                },
                'name': 'NISCOPE_VAL_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Specifies a Hanning window.'
                },
                'name': 'NISCOPE_VAL_HANNING',
                'value': 409
            },
            {
                'documentation': {
                    'description': 'Specifies a Flat Top window.'
                },
                'name': 'NISCOPE_VAL_FLAT_TOP',
                'value': 410
            },
            {
                'documentation': {
                    'description': 'Specifies a Hamming window.'
                },
                'name': 'NISCOPE_VAL_HAMMING',
                'value': 420
            },
            {
                'documentation': {
                    'description': 'Specifies a Triangle window.'
                },
                'name': 'NISCOPE_VAL_TRIANGLE',
                'value': 423
            },
            {
                'documentation': {
                    'description': 'Specifies a Blackman window.'
                },
                'name': 'NISCOPE_VAL_BLACKMAN',
                'value': 424
            }
        ]
    },
    'FetchRecordModes': {
        'values': [
            {
                'name': 'NISCOPE_VAL_RELATIVE_TO_RECORD_NUMBER',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_RELATIVE_TO_NEXT_RECORD',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_RELATIVE_TO_LAST_FETCHED',
                'value': 2
            }
        ]
    },
    'FetchRelativeTo': {
        'values': [
            {
                'documentation': {
                    'description': 'The read pointer is set to zero when a new acquisition is initiated. After every fetch the read pointer is incremeted to be the sample after the last sample retrieved.  Therefore, you can repeatedly fetch relative to the read pointer for a continuous acquisition program.'
                },
                'name': 'NISCOPE_VAL_READ_POINTER',
                'value': 388
            },
            {
                'documentation': {
                    'description': 'Fetches relative to the first pretrigger point requested with niScope_ConfigureHorizontalTiming.'
                },
                'name': 'NISCOPE_VAL_PRETRIGGER',
                'value': 477
            },
            {
                'documentation': {
                    'description': 'Fetch data at the last sample acquired.'
                },
                'name': 'NISCOPE_VAL_NOW',
                'value': 481
            },
            {
                'documentation': {
                    'description': 'Fetch data starting at the first point sampled by the digitizer.'
                },
                'name': 'NISCOPE_VAL_START',
                'value': 482
            },
            {
                'documentation': {
                    'description': 'Fetch at the first posttrigger sample.'
                },
                'name': 'NISCOPE_VAL_TRIGGER',
                'value': 483
            }
        ]
    },
    'FetchWaitModes': {
        'values': [
            {
                'name': 'NISCOPE_VAL_WAIT_DEFAULT',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_WAIT_POLL',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_WAIT_SLEEP',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_WAIT_YIELD',
                'value': 3
            },
            {
                'name': 'NISCOPE_VAL_WAIT_INTERRUPT',
                'value': 4
            }
        ]
    },
    'FilterType': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies lowpass as the filter type.'
                },
                'name': 'NISCOPE_VAL_LOWPASS',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Specifies highpass as the filter type.'
                },
                'name': 'NISCOPE_VAL_HIGHPASS',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Specifies bandpass as the filter type.'
                },
                'name': 'NISCOPE_VAL_BANDPASS',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Specifies bandstop as the filter type.'
                },
                'name': 'NISCOPE_VAL_BANDSTOP',
                'value': 3
            }
        ]
    },
    'FlexFIRAntialiasFilterType': {
        'values': [
            {
                'documentation': {
                    'description': 'This filter is optimized for alias protection and frequency-domain flatness'
                },
                'name': 'NISCOPE_VAL_48_TAP_STANDARD',
                'python_name': 'FOURTYEIGHT_TAP_STANDARD',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'This filter is optimized for the lowest possible bandwidth for a 48 tap filter and maximizes the SNR'
                },
                'name': 'NISCOPE_VAL_48_TAP_HANNING',
                'python_name': 'FOURTYEIGHT_TAP_HANNING',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'This filter is optimized for the lowest possible bandwidth for a 16 tap filter and maximizes the SNR'
                },
                'name': 'NISCOPE_VAL_16_TAP_HANNING',
                'python_name': 'SIXTEEN_TAP_HANNING',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'This filter is optimized for the lowest possible bandwidth for a 8 tap filter and maximizes the SNR'
                },
                'name': 'NISCOPE_VAL_8_TAP_HANNING',
                'python_name': 'EIGHT_TAP_HANNING',
                'value': 3
            }
        ]
    },
    'GlitchCondition': {
        'values': [
            {
                'documentation': {
                    'description': 'Trigger on pulses with a duration greater than the specified glitch width.'
                },
                'name': 'NISCOPE_VAL_GLITCH_GREATER_THAN',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Trigger on pulses with a duration shorter than the specified glitch width.'
                },
                'name': 'NISCOPE_VAL_GLITCH_LESS_THAN',
                'value': 1
            }
        ]
    },
    'GlitchPolarity': {
        'values': [
            {
                'documentation': {
                    'description': 'Trigger on pulses of positive polarity relative to the trigger threshold.'
                },
                'name': 'NISCOPE_VAL_GLITCH_POSITIVE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Trigger on pulses of negative polarity relative to the trigger threshold.'
                },
                'name': 'NISCOPE_VAL_GLITCH_NEGATIVE',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Trigger on pulses of either positive or negative polarity.'
                },
                'name': 'NISCOPE_VAL_GLITCH_EITHER',
                'value': 3
            }
        ]
    },
    'HorzConfigModes': {
        'values': [
            {
                'name': 'NISCOPE_VAL_AMBIGUOUS_USE_CASE',
                'value': -1
            },
            {
                'name': 'NISCOPE_VAL_USE_IVI_SAMPLE_RATE',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_USE_DAQMX_SAMPLE_RATE',
                'value': 1
            }
        ]
    },
    'InputImpedance': {
        'values': [
            {
                'name': 'NISCOPE_VAL_50_OHMS',
                'value': 50.0
            },
            {
                'name': 'NISCOPE_VAL_75_OHMS',
                'value': 75.0
            },
            {
                'name': 'NISCOPE_VAL_1_MEG_OHM',
                'value': 1000000.0
            }
        ]
    },
    'InternalExportSignalValues': {
        'values': [
            {
                'name': 'NISCOPE_VAL_READY_FOR_START_OR_ADVANCE_EVENT',
                'value': 8
            },
            {
                'name': 'NISCOPE_VAL_READY_FOR_REF_ARM_EVENT',
                'value': 9
            },
            {
                'name': 'NISCOPE_VAL_ASYNC_REF_EVENT',
                'value': 11
            },
            {
                'name': 'NISCOPE_VAL_STARTED_EVENT',
                'value': 12
            },
            {
                'name': 'NISCOPE_VAL_TIMER_EVENT',
                'value': 15
            }
        ]
    },
    'InternalExternalCalibrationRoutingTerminal': {
        'values': [
            {
                'name': 'NISCOPE_VAL_INTERNAL_TIMEBASE',
                'value': 'VAL_INTERNAL_TIMEBASE'
            }
        ]
    },
    'Interpolation': {
        'values': [
            {
                'name': 'NISCOPE_VAL_NO_INTERPOLATION',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_SINE_X',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_LINEAR',
                'value': 3
            }
        ]
    },
    'LinearizationCalMethods': {
        'values': [
            {
                'name': 'NISCOPE_VAL_LINEARIZATION_CAL_METHOD_SOFTWARE',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_LINEARIZATION_CAL_METHOD_FIRMWARE',
                'value': 2
            }
        ]
    },
    'LvfpgaCoercionValues': {
        'values': [
            {
                'name': 'NISCOPE_VAL_NO_SIZE_COERCION',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_PROPORTIONAL_SIZE_COERCION',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_FIXED_SIZE_COERCION',
                'value': 2
            }
        ]
    },
    'MaxInputFrequency': {
        'values': [
            {
                'name': 'NISCOPE_VAL_BANDWIDTH_FULL',
                'value': -1.0
            },
            {
                'name': 'NISCOPE_VAL_BANDWIDTH_DEVICE_DEFAULT',
                'value': 0.0
            },
            {
                'name': 'NISCOPE_VAL_20MHZ_BANDWIDTH',
                'value': 20000000.0
            },
            {
                'name': 'NISCOPE_VAL_100MHZ_BANDWIDTH',
                'value': 100000000.0
            },
            {
                'name': 'NISCOPE_VAL_20MHZ_MAX_INPUT_FREQUENCY',
                'value': 20000000.0
            },
            {
                'name': 'NISCOPE_VAL_100MHZ_MAX_INPUT_FREQUENCY',
                'value': 100000000.0
            }
        ]
    },
    'MaxTime': {
        'values': [
            {
                'name': 'NISCOPE_VAL_MAX_TIME_INFINITE',
                'value': 4294967295
            },
            {
                'name': 'NISCOPE_VAL_MAX_TIME_IMMEDIATE',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_MAX_TIME_NONE',
                'value': 0
            }
        ]
    },
    'MeasFilterType': {
        'values': [
            {
                'name': 'NISCOPE_VAL_MEAS_LOWPASS',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_MEAS_HIGHPASS',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_MEAS_BANDPASS',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_MEAS_BANDSTOP',
                'value': 3
            }
        ]
    },
    'MeasPercentageMethod': {
        'values': [
            {
                'name': 'NISCOPE_VAL_MEAS_LOW_HIGH',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_MEAS_MIN_MAX',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_MEAS_BASE_TOP',
                'value': 2
            }
        ]
    },
    'MeasRefLevelUnits': {
        'values': [
            {
                'name': 'NISCOPE_VAL_MEAS_VOLTAGE',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_MEAS_PERCENTAGE',
                'value': 1
            }
        ]
    },
    'MruSignalNames': {
        'values': [
            {
                'name': 'NISCOPE_VAL_START_TRIG_SIGNAL_STR',
                'value': 'StartTrigger'
            },
            {
                'name': 'NISCOPE_VAL_REF_TRIG_SIGNAL_STR',
                'value': 'ReferenceTrigger'
            },
            {
                'name': 'NISCOPE_VAL_ADV_TRIG_SIGNAL_STR',
                'value': 'RecordAdvanceTrigger'
            },
            {
                'name': 'NISCOPE_VAL_RDY_FOR_START_EVENT_SIGNAL_STR',
                'value': 'ReadyForStartEvent'
            },
            {
                'name': 'NISCOPE_VAL_RDY_FOR_REF_EVENT_SIGNAL_STR',
                'value': 'ReadyForReferenceEvent'
            },
            {
                'name': 'NISCOPE_VAL_RDY_FOR_ADV_EVENT_SIGNAL_STR',
                'value': 'ReadyForAdvanceEvent'
            },
            {
                'name': 'NISCOPE_VAL_END_OF_RECORD_EVENT_SIGNAL_STR',
                'value': 'EndOfRecordEvent'
            },
            {
                'name': 'NISCOPE_VAL_DONE_EVENT_SIGNAL_STR',
                'value': 'DoneEvent'
            }
        ]
    },
    'NotificationType': {
        'values': [
            {
                'documentation': {
                    'description': 'Never send notification.'
                },
                'name': 'NISCOPE_VAL_NOTIFY_NEVER',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Notify when digitizer acquisition is done.'
                },
                'name': 'NISCOPE_VAL_NOTIFY_DONE',
                'value': 1
            }
        ]
    },
    'Option': {
        'values': [
            {
                'documentation': {
                    'description': 'Self Calibrating all Channels'
                },
                'name': 'NISCOPE_VAL_SELF_CALIBRATE_ALL_CHANNELS',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Restore External Calibration.'
                },
                'name': 'NISCOPE_VAL_RESTORE_EXTERNAL_CALIBRATION',
                'value': 1
            }
        ]
    },
    'OptionsForErrorHandling': {
        'values': [
            {
                'name': 'NISCOPE_VAL_CAL_ABORT_ON_ERR',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_CAL_ABORT_ON_MAJOR_ERR',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_CAL_SKIP_BAD_SECTIONS',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_CAL_RESET_BAD_SECTIONS',
                'value': 3
            }
        ]
    },
    'OverflowErrorReporting': {
        'values': [
            {
                'documentation': {
                    'description': '\nExecution stops and NI-SCOPE returns an error when an overflow has\noccurred in the OSP block.\n'
                },
                'name': 'NISCOPE_VAL_ERROR_REPORTING_ERROR',
                'value': 0
            },
            {
                'documentation': {
                    'description': '\nExecution continues and NI-SCOPE returns a warning when an overflow has\noccurred in the OSP block.\n'
                },
                'name': 'NISCOPE_VAL_ERROR_REPORTING_WARNING',
                'value': 1
            },
            {
                'documentation': {
                    'description': '\nNI-SCOPE does not return an error when an overflow has occurred in the\nOSP block.\n'
                },
                'name': 'NISCOPE_VAL_ERROR_REPORTING_DISABLED',
                'value': 2
            }
        ]
    },
    'P2PStreamRelativeTo': {
        'values': [
            {
                'name': 'NISCOPE_VAL_STREAM_RELATIVE_TO_START_TRIGGER',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_STREAM_RELATIVE_TO_REFERENCE_TRIGGER',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_STREAM_RELATIVE_TO_SYNC_TRIGGER',
                'value': 2
            }
        ]
    },
    'PercentageMethod': {
        'values': [
            {
                'documentation': {
                    'description': '\nSpecifies that the reference level percentages should be computed using\nthe low/high method,\n'
                },
                'name': 'NISCOPE_VAL_LOWHIGH',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Reference level percentages are computed using the min/max method.'
                },
                'name': 'NISCOPE_VAL_MINMAX',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Reference level percentages are computed using the base/top method.'
                },
                'name': 'NISCOPE_VAL_BASETOP',
                'value': 2
            }
        ]
    },
    'PllCommitActions': {
        'values': [
            {
                'name': 'NISCOPE_VAL_PLL_COMMIT_ACTION_NORMAL',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_PLL_COMMIT_ACTION_SKIP_NEW_TASK_LOCK',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_PLL_COMMIT_ACTION_FORCE_LOCK',
                'value': 2
            }
        ]
    },
    'Privileges': {
        'values': [
            {
                'name': 'NISCOPE_VAL_MONITOR',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_REVOKABLE_CONTROL',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_NON_REVOKABLE_CONTROL',
                'value': 3
            }
        ]
    },
    'ProgFIRFilterRealComplex': {
        'values': [
            {
                'documentation': {
                    'description': 'Sets a dual real filter.'
                },
                'name': 'NISCOPE_VAL_REAL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Sets a complex filter.'
                },
                'name': 'NISCOPE_VAL_COMPLEX',
                'value': 1
            }
        ]
    },
    'ProgFIRFilterSymmetry': {
        'values': [
            {
                'documentation': {
                    'description': 'Sets a symmetric filter.'
                },
                'name': 'NISCOPE_VAL_SYMMETRIC',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Sets an asymmetric filter.'
                },
                'name': 'NISCOPE_VAL_ASYMMETRIC',
                'value': 1
            }
        ]
    },
    'ProgFIRFilterSymmetryType': {
        'values': [
            {
                'documentation': {
                    'description': 'Sets the discriminator FIR symmetry type to even.'
                },
                'name': 'NISCOPE_VAL_EVEN',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Sets the discriminator FIR symmetry type to odd.'
                },
                'name': 'NISCOPE_VAL_ODD',
                'value': 1
            }
        ]
    },
    'QInputToCoordConverter': {
        'values': [
            {
                'documentation': {
                    'description': 'Enables the Q input to coordinate converter.'
                },
                'name': 'NISCOPE_VAL_I_AND_Q',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Zeroes out the Q input the to coordinate converter.'
                },
                'name': 'NISCOPE_VAL_Q_ZEROED',
                'value': 1
            }
        ]
    },
    'RISMethod': {
        'values': [
            {
                'documentation': {
                    'description': 'Acquires exactly the specified number of records for each bin in the RIS acquisition.  An error is returned from the fetch function if the RIS acquisition does not successfully acquire the specified number of waveforms within the timeout period.  You may call the fetch function again to allow more time for the acquisition to finish.'
                },
                'name': 'NISCOPE_VAL_RIS_EXACT_NUM_AVERAGES',
                'value': 1
            },
            {
                'documentation': {
                    'description': '\nEach RIS sample is the average of a least a minimum number of randomly\ndistributed points.\n'
                },
                'name': 'NISCOPE_VAL_RIS_MIN_NUM_AVERAGES',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Returns the RIS waveform after the specified timeout even if it is incomplete.  If no waveforms have been acquired in certain bins, these bins will have a NaN (when fetching scaled data) or a zero (when fetching binary data). A warning (positive error code) is returned from the fetch function if the RIS acquisition did not finish.  The acquisition aborts when data is returned.'
                },
                'name': 'NISCOPE_VAL_RIS_INCOMPLETE',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Limits the waveforms in the various bins to be within 200 ps of the center of the bin.'
                },
                'name': 'NISCOPE_VAL_RIS_LIMITED_BIN_WIDTH',
                'value': 5
            }
        ]
    },
    'RecordCountModes': {
        'values': [
            {
                'name': 'NISCOPE_VAL_FINITE_RECORDS',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_CONTINUOUS_RECORDS',
                'value': 1
            }
        ]
    },
    'RefLevelUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies that the reference levels are given in units of volts.'
                },
                'name': 'NISCOPE_VAL_VOLTS',
                'value': 0
            },
            {
                'documentation': {
                    'description': '\n(Default) Specifies that the reference levels are given in percentage\nunits.\n'
                },
                'name': 'NISCOPE_VAL_PERCENTAGE',
                'value': 1
            }
        ]
    },
    'RefTriggerDetectorLocation': {
        'values': [
            {
                'documentation': {
                    'description': 'use the hardware analog circuitry to implement the reference trigger.  This option will trigger before any onboard signal processing.'
                },
                'name': 'NISCOPE_VAL_ANALOG_DETECTION_CIRCUIT',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'use the onboard signal processing logic to implement the reference trigger.  This option will trigger based on the onboard signal processed data.'
                },
                'name': 'NISCOPE_VAL_DDC_OUTPUT',
                'value': 1
            }
        ]
    },
    'ReferenceParameterForRoutingAndStoringAndFetchingIntRef': {
        'values': [
            {
                'name': 'NISCOPE_VAL_CAL_10V_CH0',
                'value': 0
            }
        ]
    },
    'ResamplerFilterMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Resampler enabled.'
                },
                'name': 'NISCOPE_VAL_RESAMPLER_ENABLED',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'HB 1 enabled.'
                },
                'name': 'NISCOPE_VAL_HB_1_ENABLED',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Resampler and HB 1.'
                },
                'name': 'NISCOPE_VAL_RESAMPLER_AND_HB_1',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Both HB Filters.'
                },
                'name': 'NISCOPE_VAL_BOTH_HB_FILTERS',
                'value': 6
            },
            {
                'documentation': {
                    'description': 'Resampler and Both HB Filters.'
                },
                'name': 'NISCOPE_VAL_RESAMPLER_AND_BOTH_HB_FILTERS',
                'value': 7
            }
        ]
    },
    'RouteInternalReferenceOptions': {
        'values': [
            {
                'name': 'NISCOPE_VAL_CAL_UNROUTE_SIGNAL',
                'value': '(ViUInt32)0xfffffff'
            },
            {
                'name': 'NISCOPE_VAL_CAL_POSITIVE',
                'value': '(ViUInt32)0xffff'
            },
            {
                'name': 'NISCOPE_VAL_CAL_NEGATIVE',
                'value': 0
            }
        ]
    },
    'RuntPolarity': {
        'values': [
            {
                'documentation': {
                    'description': 'Trigger on pulses of positive polarity relative to NISCOPE_ATTR_RUNT_LOW_THRESHOLD that do not cross NISCOPE_ATTR_RUNT_HIGH_THRESHOLD.'
                },
                'name': 'NISCOPE_VAL_RUNT_POSITIVE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Trigger on pulses of negative polarity relative to NISCOPE_ATTR_RUNT_HIGH_THRESHOLD that do not cross NISCOPE_ATTR_RUNT_LOW_THRESHOLD.'
                },
                'name': 'NISCOPE_VAL_RUNT_NEGATIVE',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Trigger on pulses of either positive or negative polarity.'
                },
                'name': 'NISCOPE_VAL_RUNT_EITHER',
                'value': 3
            }
        ]
    },
    'RuntTimeCondition': {
        'values': [
            {
                'documentation': {
                    'description': '\nTime qualification is disabled. Trigger on runt pulses based solely on the voltage level of the pulses.\n'
                },
                'name': 'NISCOPE_VAL_RUNT_TIME_CONDITION_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': '\nTrigger on pulses that, in addition to meeting runt voltage criteria, have a duration within the range bounded by NISCOPE_ATTR_RUNT_TIME_LOW_LIMIT and NISCOPE_ATTR_RUNT_TIME_HIGH_LIMIT.\n'
                },
                'name': 'NISCOPE_VAL_RUNT_TIME_CONDITION_WITHIN',
                'value': 1
            },
            {
                'documentation': {
                    'description': '\nTrigger on pulses that, in addition to meeting runt voltage criteria, have a duration not within the range bounded by NISCOPE_ATTR_RUNT_TIME_LOW_LIMIT and NISCOPE_ATTR_RUNT_TIME_HIGH_LIMIT.\n'
                },
                'name': 'NISCOPE_VAL_RUNT_TIME_CONDITION_OUTSIDE',
                'value': 2
            }
        ]
    },
    'SampClkTimepaceSrc': {
        'values': [
            {
                'name': 'NISCOPE_VAL_CLK_IN',
                'value': 'VAL_CLK_IN'
            },
            {
                'name': 'NISCOPE_VAL_NO_SOURCE',
                'value': 'VAL_NO_SOURCE'
            },
            {
                'name': 'NISCOPE_VAL_PXI_STAR',
                'value': 'VAL_PXI_STAR'
            },
            {
                'name': 'NISCOPE_VAL_PXIE_DSTAR_A',
                'value': 'VAL_PXIE_DSTAR_A'
            },
            {
                'name': 'NISCOPE_VAL_AUX_0_CLK_IN',
                'value': 'VAL_AUX_0_CLK_IN'
            },
            {
                'name': 'NISCOPE_VAL_ONBOARD_CONFIGURABLE_RATE_CLK',
                'value': 'VAL_ONBOARD_CONFIGURABLE_RATE_CLK'
            }
        ]
    },
    'SampleCountModes': {
        'values': [
            {
                'name': 'NISCOPE_VAL_FINITE_SAMPLES',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_CONTINUOUS_SAMPLES',
                'value': 1
            }
        ]
    },
    'SampleMode': {
        'values': [
            {
                'name': 'NISCOPE_VAL_REAL_TIME',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_EQUIVALENT_TIME',
                'value': 1
            }
        ]
    },
    'ScalarMeasurement': {
        'values': [
            {
                'documentation': {
                    'description': 'None'
                },
                'name': 'NISCOPE_VAL_NO_MEASUREMENT',
                'value': 4000
            },
            {
                'name': 'NISCOPE_VAL_RISE_TIME',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_FALL_TIME',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_FREQUENCY',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_PERIOD',
                'value': 3
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_RMS',
                'value': 4
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_PEAK_TO_PEAK',
                'value': 5
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_MAX',
                'value': 6
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_MIN',
                'value': 7
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HIGH',
                'value': 8
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_LOW',
                'value': 9
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_AVERAGE',
                'value': 10
            },
            {
                'name': 'NISCOPE_VAL_WIDTH_NEG',
                'value': 11
            },
            {
                'name': 'NISCOPE_VAL_WIDTH_POS',
                'value': 12
            },
            {
                'name': 'NISCOPE_VAL_DUTY_CYCLE_NEG',
                'value': 13
            },
            {
                'name': 'NISCOPE_VAL_DUTY_CYCLE_POS',
                'value': 14
            },
            {
                'name': 'NISCOPE_VAL_AMPLITUDE',
                'value': 15
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_CYCLE_RMS',
                'value': 16
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_CYCLE_AVERAGE',
                'value': 17
            },
            {
                'name': 'NISCOPE_VAL_OVERSHOOT',
                'value': 18
            },
            {
                'name': 'NISCOPE_VAL_PRESHOOT',
                'value': 19
            },
            {
                'name': 'NISCOPE_VAL_LOW_REF_VOLTS',
                'value': 1000
            },
            {
                'name': 'NISCOPE_VAL_MID_REF_VOLTS',
                'value': 1001
            },
            {
                'name': 'NISCOPE_VAL_HIGH_REF_VOLTS',
                'value': 1002
            },
            {
                'name': 'NISCOPE_VAL_AREA',
                'value': 1003
            },
            {
                'name': 'NISCOPE_VAL_CYCLE_AREA',
                'value': 1004
            },
            {
                'name': 'NISCOPE_VAL_INTEGRAL',
                'value': 1005
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_BASE',
                'value': 1006
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_TOP',
                'value': 1007
            },
            {
                'name': 'NISCOPE_VAL_FFT_FREQUENCY',
                'value': 1008
            },
            {
                'name': 'NISCOPE_VAL_FFT_AMPLITUDE',
                'value': 1009
            },
            {
                'name': 'NISCOPE_VAL_RISE_SLEW_RATE',
                'value': 1010
            },
            {
                'name': 'NISCOPE_VAL_FALL_SLEW_RATE',
                'value': 1011
            },
            {
                'name': 'NISCOPE_VAL_AC_ESTIMATE',
                'value': 1012
            },
            {
                'name': 'NISCOPE_VAL_DC_ESTIMATE',
                'value': 1013
            },
            {
                'name': 'NISCOPE_VAL_TIME_DELAY',
                'value': 1014
            },
            {
                'name': 'NISCOPE_VAL_AVERAGE_PERIOD',
                'value': 1015
            },
            {
                'name': 'NISCOPE_VAL_AVERAGE_FREQUENCY',
                'value': 1016
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_BASE_TO_TOP',
                'value': 1017
            },
            {
                'name': 'NISCOPE_VAL_PHASE_DELAY',
                'value': 1018
            }
        ]
    },
    'SessionState': {
        'values': [
            {
                'name': 'NISCOPE_VAL_IDLE',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_VERIFIED',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_COMMITTED',
                'value': 4
            },
            {
                'name': 'NISCOPE_VAL_RUNNING',
                'value': 8
            }
        ]
    },
    'StreamingPositionType': {
        'values': [
            {
                'documentation': {
                    'description': 'Data is streamed from the start trigger.'
                },
                'name': 'NISCOPE_VAL_START_TRIGGER',
                'value': 2
            },
            {
                'documentation': {
                    'description': '\nData is streamed relative to the reference trigger and reference\nposition.\n'
                },
                'name': 'NISCOPE_VAL_REFERENCE_TRIGGER',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Data is streamed relative to the sync trigger and reference position.'
                },
                'name': 'NISCOPE_VAL_SYNC_TRIGGER',
                'value': 2
            }
        ]
    },
    'SyncoutClkSelect': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies CLKIN as the source for Syncout CLK.'
                },
                'name': 'NISCOPE_VAL_CLKIN',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Specifies PROCCLK as the source for Syncout CLK.'
                },
                'name': 'NISCOPE_VAL_PROCCLK',
                'value': 1
            }
        ]
    },
    'TVTriggerSignalFormat': {
        'values': [
            {
                'name': 'NISCOPE_VAL_NTSC',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_PAL',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_SECAM',
                'value': 3
            },
            {
                'name': 'NISCOPE_VAL_M_PAL',
                'value': 1001
            },
            {
                'name': 'NISCOPE_VAL_480I_59_94_FIELDS_PER_SECOND',
                'value': 1010
            },
            {
                'name': 'NISCOPE_VAL_480I_60_FIELDS_PER_SECOND',
                'value': 1011
            },
            {
                'name': 'NISCOPE_VAL_480P_59_94_FRAMES_PER_SECOND',
                'value': 1015
            },
            {
                'name': 'NISCOPE_VAL_480P_60_FRAMES_PER_SECOND',
                'value': 1016
            },
            {
                'name': 'NISCOPE_VAL_576I_50_FIELDS_PER_SECOND',
                'value': 1020
            },
            {
                'name': 'NISCOPE_VAL_576P_50_FRAMES_PER_SECOND',
                'value': 1025
            },
            {
                'name': 'NISCOPE_VAL_720P_50_FRAMES_PER_SECOND',
                'value': 1031
            },
            {
                'name': 'NISCOPE_VAL_720P_59_94_FRAMES_PER_SECOND',
                'value': 1032
            },
            {
                'name': 'NISCOPE_VAL_720P_60_FRAMES_PER_SECOND',
                'value': 1033
            },
            {
                'name': 'NISCOPE_VAL_1080I_50_FIELDS_PER_SECOND',
                'value': 1040
            },
            {
                'name': 'NISCOPE_VAL_1080I_59_94_FIELDS_PER_SECOND',
                'value': 1041
            },
            {
                'name': 'NISCOPE_VAL_1080I_60_FIELDS_PER_SECOND',
                'value': 1042
            },
            {
                'name': 'NISCOPE_VAL_1080P_24_FRAMES_PER_SECOND',
                'value': 1045
            }
        ]
    },
    'TerminalConfiguration': {
        'values': [
            {
                'documentation': {
                    'description': 'Channel is single ended'
                },
                'name': 'NISCOPE_VAL_SINGLE_ENDED',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Channel is unbalanced differential'
                },
                'name': 'NISCOPE_VAL_UNBALANCED_DIFFERENTIAL',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Channel is differential'
                },
                'name': 'NISCOPE_VAL_DIFFERENTIAL',
                'value': 2
            }
        ]
    },
    'TimeHistogram': {
        'values': [
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MEAN',
                'value': 3000
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_STDEV',
                'value': 3001
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_PEAK_TO_PEAK',
                'value': 3002
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MEDIAN',
                'value': 3003
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_HITS',
                'value': 3004
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MAX',
                'value': 3005
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MIN',
                'value': 3006
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_STDEV',
                'value': 3007
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_2_STDEV',
                'value': 3008
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_3_STDEV',
                'value': 3009
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MODE',
                'value': 3010
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_NEW_HITS',
                'value': 3011
            }
        ]
    },
    'TimingNcoFreqOffsetBits': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies 8 offset bits in the timing NCO.'
                },
                'name': 'NISCOPE_VAL__8_BITS',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Specifies 16 offset bits in the timing NCO.'
                },
                'name': 'NISCOPE_VAL__16_BITS',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Specifies 24 offset bits in the timing NCO.'
                },
                'name': 'NISCOPE_VAL__24_BITS',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Specifies 32 offset bits in the timing NCO.'
                },
                'name': 'NISCOPE_VAL__32_BITS',
                'value': 3
            }
        ]
    },
    'TriggerCoupling': {
        'values': [
            {
                'documentation': {
                    'description': 'AC coupling'
                },
                'name': 'NISCOPE_VAL_AC',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'DC coupling'
                },
                'name': 'NISCOPE_VAL_DC',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Highpass filter coupling'
                },
                'name': 'NISCOPE_VAL_HF_REJECT',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Lowpass filter coupling'
                },
                'name': 'NISCOPE_VAL_LF_REJECT',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Highpass and lowpass filter coupling'
                },
                'name': 'NISCOPE_VAL_AC_PLUS_HF_REJECT',
                'value': 1001
            }
        ]
    },
    'TriggerModifier': {
        'values': [
            {
                'documentation': {
                    'description': 'Normal triggering.'
                },
                'name': 'NISCOPE_VAL_NO_TRIGGER_MOD',
                'value': 1
            },
            {
                'documentation': {
                    'description': '\nSoftware will trigger an acquisition automatically if no trigger arrives\nafter a certain amount of time.\n'
                },
                'name': 'NISCOPE_VAL_AUTO',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_AUTO_LEVEL',
                'value': 3
            }
        ]
    },
    'TriggerSlope': {
        'values': [
            {
                'documentation': {
                    'description': 'Falling edge'
                },
                'name': 'NISCOPE_VAL_NEGATIVE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Rising edge'
                },
                'name': 'NISCOPE_VAL_POSITIVE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Either edge'
                },
                'name': 'NISCOPE_VAL_SLOPE_EITHER',
                'value': 3
            }
        ]
    },
    'TriggerSource': {
        'values': [
            {
                'name': 'NISCOPE_VAL_IMMEDIATE',
                'value': 'VAL_IMMEDIATE'
            },
            {
                'name': 'NISCOPE_VAL_EXTERNAL',
                'value': 'VAL_EXTERNAL'
            },
            {
                'name': 'NISCOPE_VAL_SW_TRIG_FUNC',
                'value': 'VAL_SW_TRIG_FUNC'
            },
            {
                'name': 'NISCOPE_VAL_TTL0',
                'value': 'VAL_TTL0'
            },
            {
                'name': 'NISCOPE_VAL_TTL1',
                'value': 'VAL_TTL1'
            },
            {
                'name': 'NISCOPE_VAL_TTL2',
                'value': 'VAL_TTL2'
            },
            {
                'name': 'NISCOPE_VAL_TTL3',
                'value': 'VAL_TTL3'
            },
            {
                'name': 'NISCOPE_VAL_TTL4',
                'value': 'VAL_TTL4'
            },
            {
                'name': 'NISCOPE_VAL_TTL5',
                'value': 'VAL_TTL5'
            },
            {
                'name': 'NISCOPE_VAL_TTL6',
                'value': 'VAL_TTL6'
            },
            {
                'name': 'NISCOPE_VAL_TTL7',
                'value': 'VAL_TTL7'
            },
            {
                'name': 'NISCOPE_VAL_ECL0',
                'value': 'VAL_ECL0'
            },
            {
                'name': 'NISCOPE_VAL_ECL1',
                'value': 'VAL_ECL1'
            },
            {
                'name': 'NISCOPE_VAL_PXI_STAR',
                'value': 'VAL_PXI_STAR'
            },
            {
                'name': 'NISCOPE_VAL_RTSI_0',
                'value': 'VAL_RTSI_0'
            },
            {
                'name': 'NISCOPE_VAL_RTSI_1',
                'value': 'VAL_RTSI_1'
            },
            {
                'name': 'NISCOPE_VAL_RTSI_2',
                'value': 'VAL_RTSI_2'
            },
            {
                'name': 'NISCOPE_VAL_RTSI_3',
                'value': 'VAL_RTSI_3'
            },
            {
                'name': 'NISCOPE_VAL_RTSI_4',
                'value': 'VAL_RTSI_4'
            },
            {
                'name': 'NISCOPE_VAL_RTSI_5',
                'value': 'VAL_RTSI_5'
            },
            {
                'name': 'NISCOPE_VAL_RTSI_6',
                'value': 'VAL_RTSI_6'
            },
            {
                'name': 'NISCOPE_VAL_RTSI_7',
                'value': 'VAL_RTSI_7'
            },
            {
                'name': 'NISCOPE_VAL_PFI_0',
                'value': 'VAL_PFI_0'
            },
            {
                'name': 'NISCOPE_VAL_PFI_1',
                'value': 'VAL_PFI_1'
            },
            {
                'name': 'NISCOPE_VAL_PFI_2',
                'value': 'VAL_PFI_2'
            },
            {
                'name': 'NISCOPE_VAL_PFI_3',
                'value': 'VAL_PFI_3'
            },
            {
                'name': 'NISCOPE_VAL_PFI_4',
                'value': 'VAL_PFI_4'
            },
            {
                'name': 'NISCOPE_VAL_PFI_5',
                'value': 'VAL_PFI_5'
            },
            {
                'name': 'NISCOPE_VAL_PFI_6',
                'value': 'VAL_PFI_6'
            },
            {
                'name': 'NISCOPE_VAL_PFI_7',
                'value': 'VAL_PFI_7'
            },
            {
                'name': 'NISCOPE_VAL_AUX_0_PFI_0',
                'value': 'VAL_AUX_0_PFI_0'
            },
            {
                'name': 'NISCOPE_VAL_AUX_0_PFI_1',
                'value': 'VAL_AUX_0_PFI_1'
            },
            {
                'name': 'NISCOPE_VAL_AUX_0_PFI_3',
                'value': 'VAL_AUX_0_PFI_3'
            },
            {
                'name': 'NISCOPE_VAL_AUX_0_PFI_4',
                'value': 'VAL_AUX_0_PFI_4'
            },
            {
                'name': 'NISCOPE_VAL_AUX_0_PFI_5',
                'value': 'VAL_AUX_0_PFI_5'
            },
            {
                'name': 'NISCOPE_VAL_AUX_0_PFI_6',
                'value': 'VAL_AUX_0_PFI_6'
            },
            {
                'name': 'NISCOPE_VAL_AUX_0_PFI_7',
                'value': 'VAL_AUX_0_PFI_7'
            },
            {
                'name': 'NISCOPE_VAL_AUX_0_PFI_2',
                'value': 'VAL_AUX_0_PFI_2'
            }
        ]
    },
    'TriggerType': {
        'values': [
            {
                'documentation': {
                    'description': 'Configures the digitizer for edge triggering.  An edge trigger occurs when the trigger signal crosses the trigger level specified with the set trigger slope.  You configure the trigger level and slope with niScope_ConfigureTriggerEdge.'
                },
                'name': 'NISCOPE_VAL_EDGE_TRIGGER',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Configures the digitizer for hysteresis triggering.  A hysteresis trigger occurs when the trigger signal crosses the trigger level with the specified slope and passes through the hysteresis window you specify. You configure the trigger level, slope, and hysteresis with niScope_ConfigureTriggerHysteresis.'
                },
                'name': 'NISCOPE_VAL_HYSTERESIS_TRIGGER',
                'value': 1001
            },
            {
                'documentation': {
                    'description': 'Configures the digitizer for digital triggering. A digital trigger occurs when the trigger signal has the specified slope. You configure the trigger slope with niScope_ConfigureTriggerDigital.'
                },
                'name': 'NISCOPE_VAL_DIGITAL_TRIGGER',
                'value': 1002
            },
            {
                'documentation': {
                    'description': 'Configures the digitizer for window triggering.  A window trigger occurs when the trigger signal enters or leaves the window defined by the values you specify with the Low Window Level, High Window Level, and Window Mode Parameters.  You configure the low window level high window level, and window mode with niScope_ConfigureTriggerWindow.'
                },
                'name': 'NISCOPE_VAL_WINDOW_TRIGGER',
                'value': 1003
            },
            {
                'documentation': {
                    'description': 'Configures the digitizer for software triggering.  A software trigger occurs when niScope_SendSoftwareTrigger is called.'
                },
                'name': 'NISCOPE_VAL_SOFTWARE_TRIGGER',
                'value': 1004
            },
            {
                'documentation': {
                    'description': 'Configures the digitizer for video/TV triggering.   You configure the video trigger parameters like signal Format, Line to trigger off of, Polarity, and Enable DC Restore with niScope_ConfigureTriggerVideo.'
                },
                'name': 'NISCOPE_VAL_TV_TRIGGER',
                'value': 5
            },
            {
                'name': 'NISCOPE_VAL_GLITCH_TRIGGER',
                'value': 4
            },
            {
                'name': 'NISCOPE_VAL_WIDTH_TRIGGER',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_RUNT_TRIGGER',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Configures the digitizer for immediate triggering.   An immediate trigger occurs as soon as the pretrigger samples are acquired.'
                },
                'name': 'NISCOPE_VAL_IMMEDIATE_TRIGGER',
                'value': 6
            }
        ]
    },
    'TriggerWindowMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Trigger upon entering the window'
                },
                'name': 'NISCOPE_VAL_ENTERING_WINDOW',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Trigger upon leaving the window'
                },
                'name': 'NISCOPE_VAL_LEAVING_WINDOW',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_ENTERING_OR_LEAVING_WINDOW',
                'value': 2
            }
        ]
    },
    'VerticalCoupling': {
        'values': [
            {
                'documentation': {
                    'description': 'AC coupling'
                },
                'name': 'NISCOPE_VAL_AC',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'DC coupling'
                },
                'name': 'NISCOPE_VAL_DC',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'GND coupling'
                },
                'name': 'NISCOPE_VAL_GND',
                'value': 2
            }
        ]
    },
    'VideoFormats': {
        'values': [
            {
                'name': 'NISCOPE_VAL_CUSTOM_FORMAT',
                'value': 400
            }
        ]
    },
    'VideoPolarity': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies that the video signal has positive polarity.'
                },
                'name': 'NISCOPE_VAL_TV_POSITIVE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Specifies that the video signal has negative polarity.'
                },
                'name': 'NISCOPE_VAL_TV_NEGATIVE',
                'value': 2
            }
        ]
    },
    'VideoSignalFormat': {
        'values': [
            {
                'documentation': {
                    'description': 'NTSC signal format supports line numbers from 1 to 525'
                },
                'name': 'NISCOPE_VAL_NTSC',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'PAL signal format supports line numbers from 1 to 625'
                },
                'name': 'NISCOPE_VAL_PAL',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'SECAM signal format supports line numbers from 1 to 625'
                },
                'name': 'NISCOPE_VAL_SECAM',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'M-PAL signal format supports line numbers from 1 to 525'
                },
                'name': 'NISCOPE_VAL_M_PAL',
                'value': 1001
            },
            {
                'documentation': {
                    'description': '480 lines, interlaced, 59.94 fields per second'
                },
                'name': 'NISCOPE_VAL_VIDEO_480I_59_94_FIELDS_PER_SECOND',
                'value': 1010
            },
            {
                'documentation': {
                    'description': '480 lines, interlaced, 60 fields per second'
                },
                'name': 'NISCOPE_VAL_VIDEO_480I_60_FIELDS_PER_SECOND',
                'value': 1011
            },
            {
                'documentation': {
                    'description': '480 lines, progressive, 59.94 frames per second'
                },
                'name': 'NISCOPE_VAL_VIDEO_480P_59_94_FRAMES_PER_SECOND',
                'value': 1015
            },
            {
                'documentation': {
                    'description': '480 lines, progressive,60 frames per second'
                },
                'name': 'NISCOPE_VAL_VIDEO_480P_60_FRAMES_PER_SECOND',
                'value': 1016
            },
            {
                'documentation': {
                    'description': '576 lines, interlaced, 50 fields per second'
                },
                'name': 'NISCOPE_VAL_VIDEO_576I_50_FIELDS_PER_SECOND',
                'value': 1020
            },
            {
                'documentation': {
                    'description': '576 lines, progressive, 50 frames per second'
                },
                'name': 'NISCOPE_VAL_VIDEO_576P_50_FRAMES_PER_SECOND',
                'value': 1025
            },
            {
                'documentation': {
                    'description': '720 lines, progressive, 50 frames per second'
                },
                'name': 'NISCOPE_VAL_VIDEO_720P_50_FRAMES_PER_SECOND',
                'value': 1031
            },
            {
                'documentation': {
                    'description': '720 lines, progressive, 59.94 frames per second'
                },
                'name': 'NISCOPE_VAL_VIDEO_720P_59_94_FRAMES_PER_SECOND',
                'value': 1032
            },
            {
                'documentation': {
                    'description': '720 lines, progressive, 60 frames per second'
                },
                'name': 'NISCOPE_VAL_VIDEO_720P_60_FRAMES_PER_SECOND',
                'value': 1033
            },
            {
                'documentation': {
                    'description': '1,080 lines, interlaced, 50 fields per second'
                },
                'name': 'NISCOPE_VAL_VIDEO_1080I_50_FIELDS_PER_SECOND',
                'value': 1040
            },
            {
                'documentation': {
                    'description': '1,080 lines, interlaced, 59.94 fields per second'
                },
                'name': 'NISCOPE_VAL_VIDEO_1080I_59_94_FIELDS_PER_SECOND',
                'value': 1041
            },
            {
                'documentation': {
                    'description': '1,080 lines, interlaced, 60 fields per second'
                },
                'name': 'NISCOPE_VAL_VIDEO_1080I_60_FIELDS_PER_SECOND',
                'value': 1042
            },
            {
                'documentation': {
                    'description': '1,080 lines, progressive, 24 frames per second'
                },
                'name': 'NISCOPE_VAL_VIDEO_1080P_24_FRAMES_PER_SECOND',
                'value': 1045
            }
        ]
    },
    'VideoTriggerEvent': {
        'values': [
            {
                'documentation': {
                    'description': 'Trigger on field 1 of the signal'
                },
                'name': 'NISCOPE_VAL_TV_EVENT_FIELD1',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Trigger on field 2 of the signal'
                },
                'name': 'NISCOPE_VAL_TV_EVENT_FIELD2',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Trigger on the first field acquired'
                },
                'name': 'NISCOPE_VAL_TV_EVENT_ANY_FIELD',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Trigger on the first line acquired'
                },
                'name': 'NISCOPE_VAL_TV_EVENT_ANY_LINE',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Trigger on a specific line of a video signal.  Valid values vary depending on the signal format configured.'
                },
                'name': 'NISCOPE_VAL_TV_EVENT_LINE_NUMBER',
                'value': 5
            }
        ]
    },
    'VoltageHistogram': {
        'values': [
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN',
                'value': 2000
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_STDEV',
                'value': 2001
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_PEAK_TO_PEAK',
                'value': 2002
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEDIAN',
                'value': 2003
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_HITS',
                'value': 2004
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MAX',
                'value': 2005
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MIN',
                'value': 2006
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_STDEV',
                'value': 2007
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_2_STDEV',
                'value': 2008
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_3_STDEV',
                'value': 2009
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MODE',
                'value': 2010
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_NEW_HITS',
                'value': 2011
            }
        ]
    },
    'WhichTrigger': {
        'values': [
            {
                'name': 'NISCOPE_VAL_SOFTWARE_TRIGGER_START',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_SOFTWARE_TRIGGER_ARM_REFERENCE',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_SOFTWARE_TRIGGER_REFERENCE',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_SOFTWARE_TRIGGER_ADVANCE',
                'value': 3
            }
        ]
    },
    'WidthCondition': {
        'values': [
            {
                'documentation': {
                    'description': 'Trigger on pulses with a duration within the range bounded by NISCOPE_ATTR_WIDTH_LOW_THRESHOLD and NISCOPE_ATTR_WIDTH_HIGH_THRESHOLD.'
                },
                'name': 'NISCOPE_VAL_WIDTH_WITHIN',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Trigger on pulses with a duration not within the range bounded by NISCOPE_ATTR_WIDTH_LOW_THRESHOLD and NISCOPE_ATTR_WIDTH_HIGH_THRESHOLD.'
                },
                'name': 'NISCOPE_VAL_WIDTH_OUTSIDE',
                'value': 2
            }
        ]
    },
    'WidthPolarity': {
        'values': [
            {
                'documentation': {
                    'description': 'Trigger on pulses of positive polarity relative to the trigger threshold.'
                },
                'name': 'NISCOPE_VAL_WIDTH_POSITIVE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Trigger on pulses of negative polarity relative to the trigger threshold.'
                },
                'name': 'NISCOPE_VAL_WIDTH_NEGATIVE',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Trigger on pulses of either positive or negative polarity.'
                },
                'name': 'NISCOPE_VAL_WIDTH_EITHER',
                'value': 3
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/metadata/enums_addon.py sha256=6679b48316d199674e91c7dc700f9768376a2671afeea80f4c06ac360cd41596 bytes=186 -->
## FILE: src/niscope/metadata/enums_addon.py

- repository: `ni/nimi-python`
- source_path: `src/niscope/metadata/enums_addon.py`
- sha256: `6679b48316d199674e91c7dc700f9768376a2671afeea80f4c06ac360cd41596`
- bytes: 186

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/metadata/functions.py sha256=d14b0676762c2c277f5f36025a4518db306d3e3d08194f39ab5e1e0635111aad bytes=191589 -->
## FILE: src/niscope/metadata/functions.py

- repository: `ni/nimi-python`
- source_path: `src/niscope/metadata/functions.py`
- sha256: `d14b0676762c2c277f5f36025a4518db306d3e3d08194f39ab5e1e0635111aad`
- bytes: 191589

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-SCOPE API metadata version 25.0.0f151
functions = {
    'Abort': {
        'documentation': {
            'description': '\nAborts an acquisition and returns the digitizer to the Idle state. Call\nthis function if the digitizer times out waiting for a trigger.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'AcquisitionStatus': {
        'documentation': {
            'description': '\nReturns status information about the acquisition to the **status**\noutput parameter.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns whether the acquisition is complete, in progress, or unknown.\n\n**Defined Values**\n\nNISCOPE_VAL_ACQ_COMPLETE\n\nNISCOPE_VAL_ACQ_IN_PROGRESS\n\nNISCOPE_VAL_ACQ_STATUS_UNKNOWN\n'
                },
                'enum': 'AcquisitionStatus',
                'name': 'acquisitionStatus',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ActualMeasWfmSize': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the total available size of an array measurement acquisition.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe `array\nmeasurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__\nto perform.\n'
                },
                'enum': 'ArrayMeasurement',
                'name': 'arrayMeasFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the size (in number of samples) of the resulting analysis\nwaveform.\n'
                },
                'name': 'measWaveformSize',
                'type': 'ViInt32'
            }
        ],
        'render_in_session_base': True,
        'returns': 'ViStatus'
    },
    'ActualNumWfms': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nHelps you to declare appropriately sized waveforms. NI-SCOPE handles the\nchannel list parsing for you.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the number of records times the number of channels; if you are\noperating in DDC mode (NI 5620/5621 only), this value is multiplied by\ntwo.\n'
                },
                'name': 'numWfms',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'AddWaveformProcessing': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nAdds one measurement to the list of processing steps that are completed\nbefore the measurement. The processing is added on a per channel basis,\nand the processing measurements are completed in the same order they are\nregistered. All measurement library parameters—the attributes starting\nwith "meas_"—are cached at the time of registering the\nprocessing, and this set of parameters is used during the processing\nstep. The processing measurements are streamed, so the result of the\nfirst processing step is used as the input for the next step. The\nprocessing is done before any other measurements.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe `array\nmeasurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__\nto add.\n'
                },
                'enum': 'ArrayMeasurement',
                'name': 'measFunction',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'AutoSetup': {
        'documentation': {
            'description': '\nAutomatically configures the instrument. When you call this function,\nthe digitizer senses the input signal and automatically configures many\nof the instrument settings. If a signal is detected on a channel, the\ndriver chooses the smallest available vertical range that is larger than\nthe signal range. For example, if the signal is a 1.2 V\\ :sub:`pk-pk`\nsine wave, and the device supports 1 V and 2 V vertical ranges, the\ndriver will choose the 2 V vertical range for that channel.\n\nIf no signal is found on any analog input channel, a warning is\nreturned, and all channels are enabled. A channel is considered to have\na signal present if the signal is at least 10% of the smallest vertical\nrange available for that channel.\n\nThe following settings are changed:\n',
            'table_body': [
                [
                    '**General**'
                ],
                [
                    'Acquisition mode',
                    'Normal'
                ],
                [
                    'Reference clock',
                    'Internal'
                ],
                [
                    '**Vertical**'
                ],
                [
                    'Vertical coupling',
                    'AC (DC for NI 5621)'
                ],
                [
                    'Vertical bandwidth',
                    'Full'
                ],
                [
                    'Vertical range',
                    'Changed by auto setup'
                ],
                [
                    'Vertical offset',
                    '0 V'
                ],
                [
                    'Probe attenuation',
                    'Unchanged by auto setup'
                ],
                [
                    'Input impedance',
                    'Unchanged by auto setup'
                ],
                [
                    '**Horizontal**'
                ],
                [
                    'Sample rate',
                    'Changed by auto setup'
                ],
                [
                    'Min record length',
                    'Changed by auto setup'
                ],
                [
                    'Enforce realtime',
                    'True'
                ],
                [
                    'Number of Records',
                    'Changed to 1'
                ],
                [
                    '**Triggering**'
                ],
                [
                    'Trigger type',
                    'Edge if signal present, otherwise immediate'
                ],
                [
                    'Trigger channel',
                    'Lowest numbered channel with a signal present'
                ],
                [
                    'Trigger slope',
                    'Positive'
                ],
                [
                    'Trigger coupling',
                    'DC'
                ],
                [
                    'Reference position',
                    '50%'
                ],
                [
                    'Trigger level',
                    '50% of signal on trigger channel'
                ],
                [
                    'Trigger delay',
                    '0'
                ],
                [
                    'Trigger holdoff',
                    '0'
                ],
                [
                    'Trigger output',
                    'None'
                ]
            ]
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalFetchDate': {
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
                'enum': 'CalibrationTypes',
                'name': 'whichOne',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'day',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalFetchTemperature': {
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
                'grpc_enum': 'CalibrationTypes',
                'name': 'whichOne',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalSelfCalibrate': {
        'documentation': {
            'description': '\nSelf-calibrates most NI digitizers, including all SMC-based devices and\nmost Traditional NI-DAQ (Legacy) devices. To verify that your digitizer\nsupports self-calibration, refer to `Features Supported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__.\n\nFor SMC-based digitizers, if the self-calibration is performed\nsuccessfully in a regular session, the calibration constants are\nimmediately stored in the self-calibration area of the EEPROM. If the\nself-calibration is performed in an external calibration session, the\ncalibration constants take effect immediately for the duration of the\nsession. However, they are not stored in the EEPROM until\nniScope_CalEnd is called with **action** set to\nNISCOPE_VAL_ACTION_STORE and no errors occur.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'default_value': 'Option.SELF_CALIBRATE_ALL_CHANNELS',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe calibration option. Use VI_NULL for a normal self-calibration\noperation or NISCOPE_VAL_CAL_RESTORE_EXTERNAL_CALIBRATION to\nrestore the previous calibration.\n'
                },
                'enum': 'Option',
                'name': 'option',
                'type': 'ViInt32'
            }
        ],
        'python_name': 'self_cal',
        'returns': 'ViStatus'
    },
    'ClearWaveformMeasurementStats': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nClears the waveform stats on the channel and measurement you specify. If\nyou want to clear all of the measurements, use\nNISCOPE_VAL_ALL_MEASUREMENTS in the **clearableMeasurementFunction**\nparameter.\n\nEvery time a measurement is called, the statistics information is\nupdated, including the min, max, mean, standard deviation, and number of\nupdates. This information is fetched with\nniScope_FetchMeasurementStats. The multi-acquisition array measurements\nare also cleared with this function.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'default_value': 'ClearableMeasurement.ALL_MEASUREMENTS',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe `scalar\nmeasurement <REPLACE_DRIVER_SPECIFIC_URL_2(scalar_measurements_refs)>`__\nor `array\nmeasurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__\nto clear the stats for.\n'
                },
                'enum': 'ClearableMeasurement',
                'name': 'clearableMeasurementFunction',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearWaveformProcessing': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nClears the list of processing steps assigned to the given channel. The\nprocessing is added using the niScope_AddWaveformProcessing function,\nwhere the processing steps are completed in the same order in which they\nare registered. The processing measurements are streamed, so the result\nof the first processing step is used as the input for the next step. The\nprocessing is also done before any other measurements.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'Commit': {
        'documentation': {
            'description': '\nCommits to hardware all the parameter settings associated with the task.\nUse this function if you want a parameter change to be immediately\nreflected in the hardware. This function is not supported for\nTraditional NI-DAQ (Legacy) devices.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureChanCharacteristics': {
        'documentation': {
            'description': '\nConfigures the attributes that control the electrical characteristics of\nthe channel—the input impedance and the bandwidth.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe input impedance for the channel; NI-SCOPE sets\nNISCOPE_ATTR_INPUT_IMPEDANCE to this value.\n'
                },
                'name': 'inputImpedance',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe bandwidth for the channel; NI-SCOPE sets\nNISCOPE_ATTR_MAX_INPUT_FREQUENCY to this value. Pass 0 for this\nvalue to use the hardware default bandwidth. Pass –1 for this value to\nachieve full bandwidth.\n'
                },
                'name': 'maxInputFrequency',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureEqualizationFilterCoefficients': {
        'documentation': {
            'description': '\nConfigures the custom coefficients for the equalization FIR filter on\nthe device. This filter is designed to compensate the input signal for\nartifacts introduced to the signal outside of the digitizer. Because\nthis filter is a generic FIR filter, any coefficients are valid.\nCoefficient values should be between +1 and –1.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of coefficients being passed in the **coefficients** array.'
                },
                'name': 'numberOfCoefficients',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe custom coefficients for the equalization FIR filter on the device.\nThese coefficients should be between +1 and –1. You can obtain the\nnumber of coefficients from the\n`NISCOPE_ATTR_EQUALIZATION_NUM_COEFFICIENTS <cviNISCOPE_ATTR_EQUALIZATION_NUM_COEFFICIENTS.html>`__\nattribute. The\n`NISCOPE_ATTR_EQUALIZATION_FILTER_ENABLED <cviNISCOPE_ATTR_EQUALIZATION_FILTER_ENABLED.html>`__\nattribute must be set to TRUE to enable the filter.\n'
                },
                'name': 'coefficients',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfCoefficients'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureHorizontalTiming': {
        'documentation': {
            'description': '\nConfigures the common properties of the horizontal subsystem for a\nmultirecord acquisition in terms of minimum sample rate.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe sampling rate for the acquisition. Refer to\nNISCOPE_ATTR_MIN_SAMPLE_RATE for more information.\n'
                },
                'name': 'minSampleRate',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe minimum number of points you need in the record for each channel;\ncall niScope_ActualRecordLength to obtain the actual record length\nused.\n\nValid Values: Greater than 1; limited by available memory\n'
                },
                'name': 'minNumPts',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe position of the Reference Event in the waveform record specified as\na percentage.\n'
                },
                'name': 'refPosition',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of records to acquire'
                },
                'name': 'numRecords',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIndicates whether the digitizer enforces real-time measurements or\nallows equivalent-time (RIS) measurements; not all digitizers support\nRIS—refer to `Features Supported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for\nmore information.\n\nDefault value: VI_TRUE\n\n**Defined Values**\n\nVI_TRUE—Allow real-time acquisitions only\n\nVI_FALSE—Allow real-time and equivalent-time acquisitions\n'
                },
                'name': 'enforceRealtime',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureRefLevels': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThis function is included for compliance with the IviScope Class\nSpecification.\n\nConfigures the reference levels for all channels of the digitizer. The\nlevels may be set on a per channel basis by setting\nNISCOPE_ATTR_MEAS_CHAN_HIGH_REF_LEVEL,\nNISCOPE_ATTR_MEAS_CHAN_LOW_REF_LEVEL, and\nNISCOPE_ATTR_MEAS_CHAN_MID_REF_LEVEL\n\nThis function configures the reference levels for waveform measurements.\nCall this function before calling niScope_FetchMeasurement to take a\nrise time, fall time, width negative, width positive, duty cycle\nnegative, or duty cycle positive measurement.\n'
        },
        'included_in_proto': False,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 10.0,
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the low reference you want the digitizer to use for waveform\nmeasurements.\n\nUnits: Either a percentage or voltage based on\nNISCOPE_ATTR_MEAS_REF_LEVEL_UNITS. A percentage is calculated with\nthe voltage low and voltage high measurements representing 0% and 100%,\nrespectively.\n\nDefault Value: 10.0\n'
                },
                'name': 'low',
                'type': 'ViReal64'
            },
            {
                'default_value': 50.0,
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the mid reference you want the digitizer to use for waveform\nmeasurements.\n\nUnits: Either a percentage or voltage based on\nNISCOPE_ATTR_MEAS_REF_LEVEL_UNITS. A percentage is calculated with\nthe voltage low and voltage high measurements representing 0% and 100%,\nrespectively.\n\nDefault Value: 50.0\n'
                },
                'name': 'mid',
                'type': 'ViReal64'
            },
            {
                'default_value': 90.0,
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the high reference you want the digitizer to use for waveform\nmeasurements.\n\nUnits: Either a percentage or voltage based on\nNISCOPE_ATTR_MEAS_REF_LEVEL_UNITS. A percentage is calculated with\nthe voltage low and voltage high measurements representing 0% and 100%,\nrespectively.\n\nDefault Value: 90.0\n'
                },
                'name': 'high',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerDigital': {
        'documentation': {
            'description': '\nConfigures the common properties of a digital trigger.\n\nWhen you initiate an acquisition, the digitizer waits for the start\ntrigger, which is configured through the NISCOPE_ATTR_ACQ_ARM_SOURCE\n(Start Trigger Source) attribute. The default is immediate. Upon\nreceiving the start trigger the digitizer begins sampling pretrigger\npoints. After the digitizer finishes sampling pretrigger points, the\ndigitizer waits for a reference (stop) trigger that you specify with a\nfunction such as this one. Upon receiving the reference trigger the\ndigitizer finishes the acquisition after completing posttrigger\nsampling. With each Configure Trigger function, you specify\nconfiguration parameters such as the trigger source and the amount of\ntrigger delay.\n',
            'note': '\nFor multirecord acquisitions, all records after the first record are\nstarted by using the Advance Trigger Source. The default is immediate.\n\nYou can adjust the amount of pre-trigger and post-trigger samples using\nthe reference position parameter on the\nniScope_ConfigureHorizontalTiming function. The default is half of the\nrecord length.\n\nSome features are not supported by all digitizers. Refer to `Features\nSupported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for\nmore information.\n\nDigital triggering is not supported in RIS mode.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the trigger source. Refer to NISCOPE_ATTR_TRIGGER_SOURCE\nfor defined values.\n'
                },
                'name': 'triggerSource',
                'type': 'ViConstString'
            },
            {
                'default_value': 'TriggerSlope.POSITIVE',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether you want a rising edge or a falling edge to trigger\nthe digitizer. Refer to NISCOPE_ATTR_TRIGGER_SLOPE for more\ninformation.\n'
                },
                'enum': 'TriggerSlope',
                'name': 'slope',
                'type': 'ViInt32'
            },
            {
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe length of time the digitizer waits after detecting a trigger before\nenabling NI-SCOPE to detect another trigger. Refer to\nNISCOPE_ATTR_TRIGGER_HOLDOFF for more information.\n'
                },
                'name': 'holdoff',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nHow long the digitizer waits after receiving the trigger to start\nacquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more\ninformation.\n'
                },
                'name': 'delay',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerEdge': {
        'documentation': {
            'description': '\nConfigures common properties for analog edge triggering.\n\nWhen you initiate an acquisition, the digitizer waits for the start\ntrigger, which is configured through the NISCOPE_ATTR_ACQ_ARM_SOURCE\n(Start Trigger Source) attribute. The default is immediate. Upon\nreceiving the start trigger the digitizer begins sampling pretrigger\npoints. After the digitizer finishes sampling pretrigger points, the\ndigitizer waits for a reference (stop) trigger that you specify with a\nfunction such as this one. Upon receiving the reference trigger the\ndigitizer finishes the acquisition after completing posttrigger\nsampling. With each Configure Trigger function, you specify\nconfiguration parameters such as the trigger source and the amount of\ntrigger delay.\n',
            'note': '\nSome features are not supported by all digitizers. Refer to `Features\nSupported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for\nmore information.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the trigger source. Refer to NISCOPE_ATTR_TRIGGER_SOURCE\nfor defined values.\n'
                },
                'name': 'triggerSource',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe voltage threshold for the trigger. Refer to\nNISCOPE_ATTR_TRIGGER_LEVEL for more information.\n'
                },
                'name': 'level',
                'type': 'ViReal64'
            },
            {
                'default_value': 'TriggerSlope.POSITIVE',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether you want a rising edge or a falling edge to trigger\nthe digitizer. Refer to NISCOPE_ATTR_TRIGGER_SLOPE for more\ninformation.\n'
                },
                'enum': 'TriggerSlope',
                'name': 'slope',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nApplies coupling and filtering options to the trigger signal. Refer to\nNISCOPE_ATTR_TRIGGER_COUPLING for more information.\n'
                },
                'enum': 'TriggerCoupling',
                'name': 'triggerCoupling',
                'type': 'ViInt32'
            },
            {
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe length of time the digitizer waits after detecting a trigger before\nenabling NI-SCOPE to detect another trigger. Refer to\nNISCOPE_ATTR_TRIGGER_HOLDOFF for more information.\n'
                },
                'name': 'holdoff',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nHow long the digitizer waits after receiving the trigger to start\nacquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more\ninformation.\n'
                },
                'name': 'delay',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerHysteresis': {
        'documentation': {
            'description': '\nConfigures common properties for analog hysteresis triggering. This kind\nof trigger specifies an additional value, specified in the\n**hysteresis** parameter, that a signal must pass through before a\ntrigger can occur. This additional value acts as a kind of buffer zone\nthat keeps noise from triggering an acquisition.\n\nWhen you initiate an acquisition, the digitizer waits for the start\ntrigger, which is configured through the\nNISCOPE_ATTR_ACQ_ARM_SOURCE. The default is immediate. Upon\nreceiving the start trigger the digitizer begins sampling pretrigger\npoints. After the digitizer finishes sampling pretrigger points, the\ndigitizer waits for a reference (stop) trigger that you specify with a\nfunction such as this one. Upon receiving the reference trigger the\ndigitizer finishes the acquisition after completing posttrigger\nsampling. With each Configure Trigger function, you specify\nconfiguration parameters such as the trigger source and the amount of\ntrigger delay.\n',
            'note': '\nSome features are not supported by all digitizers. Refer to `Features\nSupported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for\nmore information.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the trigger source. Refer to NISCOPE_ATTR_TRIGGER_SOURCE\nfor defined values.\n'
                },
                'name': 'triggerSource',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe voltage threshold for the trigger. Refer to\nNISCOPE_ATTR_TRIGGER_LEVEL for more information.\n'
                },
                'name': 'level',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe size of the hysteresis window on either side of the **level** in\nvolts; the digitizer triggers when the trigger signal passes through the\nhysteresis value you specify with this parameter, has the slope you\nspecify with **slope**, and passes through the **level**. Refer to\nNISCOPE_ATTR_TRIGGER_HYSTERESIS for defined values.\n'
                },
                'name': 'hysteresis',
                'type': 'ViReal64'
            },
            {
                'default_value': 'TriggerSlope.POSITIVE',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether you want a rising edge or a falling edge to trigger\nthe digitizer. Refer to NISCOPE_ATTR_TRIGGER_SLOPE for more\ninformation.\n'
                },
                'enum': 'TriggerSlope',
                'name': 'slope',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nApplies coupling and filtering options to the trigger signal. Refer to\nNISCOPE_ATTR_TRIGGER_COUPLING for more information.\n'
                },
                'enum': 'TriggerCoupling',
                'name': 'triggerCoupling',
                'type': 'ViInt32'
            },
            {
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe length of time the digitizer waits after detecting a trigger before\nenabling NI-SCOPE to detect another trigger. Refer to\nNISCOPE_ATTR_TRIGGER_HOLDOFF for more information.\n'
                },
                'name': 'holdoff',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nHow long the digitizer waits after receiving the trigger to start\nacquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more\ninformation.\n'
                },
                'name': 'delay',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerImmediate': {
        'documentation': {
            'description': '\nConfigures common properties for immediate triggering. Immediate\ntriggering means the digitizer triggers itself.\n\nWhen you initiate an acquisition, the digitizer waits for a trigger. You\nspecify the type of trigger that the digitizer waits for with a\nConfigure Trigger function, such as niScope_ConfigureTriggerImmediate.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerSoftware': {
        'documentation': {
            'description': '\nConfigures common properties for software triggering.\n\nWhen you initiate an acquisition, the digitizer waits for the start\ntrigger, which is configured through the NISCOPE_ATTR_ACQ_ARM_SOURCE\n(Start Trigger Source) attribute. The default is immediate. Upon\nreceiving the start trigger the digitizer begins sampling pretrigger\npoints. After the digitizer finishes sampling pretrigger points, the\ndigitizer waits for a reference (stop) trigger that you specify with a\nfunction such as this one. Upon receiving the reference trigger the\ndigitizer finishes the acquisition after completing posttrigger\nsampling. With each Configure Trigger function, you specify\nconfiguration parameters such as the trigger source and the amount of\ntrigger delay.\n\nTo trigger the acquisition, use niScope_SendSoftwareTriggerEdge.\n',
            'note': '\nSome features are not supported by all digitizers. Refer to `Features\nSupported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for\nmore information.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe length of time the digitizer waits after detecting a trigger before\nenabling NI-SCOPE to detect another trigger. Refer to\nNISCOPE_ATTR_TRIGGER_HOLDOFF for more information.\n'
                },
                'name': 'holdoff',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nHow long the digitizer waits after receiving the trigger to start\nacquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more\ninformation.\n'
                },
                'name': 'delay',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerVideo': {
        'documentation': {
            'description': '\nConfigures the common properties for video triggering, including the\nsignal format, TV event, line number, polarity, and enable DC restore. A\nvideo trigger occurs when the digitizer finds a valid video signal sync.\n\nWhen you initiate an acquisition, the digitizer waits for the start\ntrigger, which is configured through the NISCOPE_ATTR_ACQ_ARM_SOURCE\n(Start Trigger Source) attribute. The default is immediate. Upon\nreceiving the start trigger the digitizer begins sampling pretrigger\npoints. After the digitizer finishes sampling pretrigger points, the\ndigitizer waits for a reference (stop) trigger that you specify with a\nfunction such as this one. Upon receiving the reference trigger the\ndigitizer finishes the acquisition after completing posttrigger\nsampling. With each Configure Trigger function, you specify\nconfiguration parameters such as the trigger source and the amount of\ntrigger delay.\n',
            'note': '\nSome features are not supported by all digitizers. Refer to `Features\nSupported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for\nmore information.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the trigger source. Refer to NISCOPE_ATTR_TRIGGER_SOURCE\nfor defined values.\n'
                },
                'name': 'triggerSource',
                'type': 'ViConstString'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': '\nOffsets each video line so the clamping level (the portion of the video\nline between the end of the color burst and the beginning of the active\nimage) is moved to zero volt. Refer to\nNISCOPE_ATTR_ENABLE_DC_RESTORE for defined values.\n'
                },
                'name': 'enableDcRestore',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the type of video signal sync the digitizer should look for.\nRefer to NISCOPE_ATTR_TV_TRIGGER_SIGNAL_FORMAT for more\ninformation.\n'
                },
                'enum': 'VideoSignalFormat',
                'name': 'signalFormat',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the TV event you want to trigger on. You can trigger on a\nspecific or on the next coming line or field of the signal.\n'
                },
                'enum': 'VideoTriggerEvent',
                'name': 'event',
                'type': 'ViInt32'
            },
            {
                'default_value': 1,
                'direction': 'in',
                'documentation': {
                    'description': '\nSelects the line number to trigger on. The line number range covers an\nentire frame and is referenced as shown on `Vertical Blanking and\nSynchronization\nSignal <REPLACE_DRIVER_SPECIFIC_URL_1(gray_scale_image)>`__. Refer to\nNISCOPE_ATTR_TV_TRIGGER_LINE_NUMBER for more information.\n\nDefault value: 1\n'
                },
                'name': 'lineNumber',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the polarity of the video signal sync.'
                },
                'enum': 'VideoPolarity',
                'name': 'polarity',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nApplies coupling and filtering options to the trigger signal. Refer to\nNISCOPE_ATTR_TRIGGER_COUPLING for more information.\n'
                },
                'enum': 'TriggerCoupling',
                'name': 'triggerCoupling',
                'type': 'ViInt32'
            },
            {
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe length of time the digitizer waits after detecting a trigger before\nenabling NI-SCOPE to detect another trigger. Refer to\nNISCOPE_ATTR_TRIGGER_HOLDOFF for more information.\n'
                },
                'name': 'holdoff',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nHow long the digitizer waits after receiving the trigger to start\nacquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more\ninformation.\n'
                },
                'name': 'delay',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerWindow': {
        'documentation': {
            'description': '\nConfigures common properties for analog window triggering. A window\ntrigger occurs when a signal enters or leaves a window you specify with\nthe **high level** or **low level** parameters.\n\nWhen you initiate an acquisition, the digitizer waits for the start\ntrigger, which is configured through the NISCOPE_ATTR_ACQ_ARM_SOURCE\n(Start Trigger Source) attribute. The default is immediate. Upon\nreceiving the start trigger the digitizer begins sampling pretrigger\npoints. After the digitizer finishes sampling pretrigger points, the\ndigitizer waits for a reference (stop) trigger that you specify with a\nfunction such as this one. Upon receiving the reference trigger the\ndigitizer finishes the acquisition after completing posttrigger\nsampling. With each Configure Trigger function, you specify\nconfiguration parameters such as the trigger source and the amount of\ntrigger delay.\n\nTo trigger the acquisition, use niScope_SendSoftwareTriggerEdge.\n',
            'note': 'Some features are not supported by all digitizers.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the trigger source. Refer to NISCOPE_ATTR_TRIGGER_SOURCE\nfor defined values.\n'
                },
                'name': 'triggerSource',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPasses the voltage threshold you want the digitizer to use for low\ntriggering.\n'
                },
                'name': 'lowLevel',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPasses the voltage threshold you want the digitizer to use for high\ntriggering.\n'
                },
                'name': 'highLevel',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether you want the trigger to occur when the signal enters\nor leaves a window.\n'
                },
                'enum': 'TriggerWindowMode',
                'name': 'windowMode',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nApplies coupling and filtering options to the trigger signal. Refer to\nNISCOPE_ATTR_TRIGGER_COUPLING for more information.\n'
                },
                'enum': 'TriggerCoupling',
                'name': 'triggerCoupling',
                'type': 'ViInt32'
            },
            {
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe length of time the digitizer waits after detecting a trigger before\nenabling NI-SCOPE to detect another trigger. Refer to\nNISCOPE_ATTR_TRIGGER_HOLDOFF for more information.\n'
                },
                'name': 'holdoff',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nHow long the digitizer waits after receiving the trigger to start\nacquiring data. Refer to NISCOPE_ATTR_TRIGGER_DELAY_TIME for more\ninformation.\n'
                },
                'name': 'delay',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureVertical': {
        'documentation': {
            'description': '\nConfigures the most commonly configured attributes of the digitizer\nvertical subsystem, such as the range, offset, coupling, probe\nattenuation, and the channel.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the vertical range Refer to NISCOPE_ATTR_VERTICAL_RANGE for\nmore information.\n'
                },
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'default_value': 0.0,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the vertical offset. Refer to NISCOPE_ATTR_VERTICAL_OFFSET\nfor more information.\n'
                },
                'name': 'offset',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies how to couple the input signal. Refer to\nNISCOPE_ATTR_VERTICAL_COUPLING for more information.\n'
                },
                'enum': 'VerticalCoupling',
                'name': 'coupling',
                'type': 'ViInt32'
            },
            {
                'default_value': 1.0,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the probe attenuation. Refer to\nNISCOPE_ATTR_PROBE_ATTENUATION for valid values.\n'
                },
                'name': 'probeAttenuation',
                'type': 'ViReal64'
            },
            {
                'default_value': True,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether the channel is enabled for acquisition. Refer to\nNISCOPE_ATTR_CHANNEL_ENABLED for more information.\n'
                },
                'name': 'enabled',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'Disable': {
        'documentation': {
            'description': '\nAborts any current operation, opens data channel relays, and releases\nRTSI and PFI lines.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributeConfigurationBuffer': {
        'documentation': {
            'description': '\nExports the attribute configuration of the session to a configuration\nbuffer.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers, channel counts, and onboard memory\nsizes.\n\nThis function verifies that the attributes you have configured for the\nsession are valid. If the configuration is invalid, NI‑SCOPE returns an\nerror.\n\n**Related Topics:**\n\n`Attributes and Attribute\nFunctions <REPLACE_DRIVER_SPECIFIC_URL_1(attributes_and_attribute_functions)>`__\n\n`Setting Attributes Before Reading\nAttributes <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the size, in bytes, of the byte array to export. If you enter\n0, this function returns the needed size.\n'
                },
                'name': 'sizeInBytes',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nSpecifies the byte array buffer to be populated with the exported\nattribute configuration.\n'
                },
                'name': 'configuration',
                'python_api_converter_name': 'convert_to_bytes',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'sizeInBytes'
                },
                'type': 'ViInt8[]',
                'type_in_documentation': 'bytes',
                'use_array': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributeConfigurationFile': {
        'documentation': {
            'description': '\nExports the attribute configuration of the session to the specified\nfile.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers, channel counts, and onboard memory\nsizes.\n\nThis function verifies that the attributes you have configured for the\nsession are valid. If the configuration is invalid, NI‑SCOPE returns an\nerror.\n\n**Related Topics:**\n\n`Attributes and Attribute\nFunctions <REPLACE_DRIVER_SPECIFIC_URL_1(attributes_and_attribute_functions)>`__\n\n`Setting Attributes Before Reading\nAttributes <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the absolute path to the file to contain the exported\nattribute configuration. If you specify an empty or relative path, this\nfunction returns an error.\n**Default file extension:** .niscopeconfig\n'
                },
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'FancyFetch': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nReturns the waveform from a previously initiated acquisition that the\ndigitizer acquires for the specified channel. This function returns\nscaled voltage waveforms.\n\nThis function may return multiple waveforms depending on the number of\nchannels, the acquisition type, and the number of records you specify.',
            'note': 'Some functionality, such as time stamping, is not supported in all digitizers.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_fetch'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The instrument handle you obtain from niScope_init that identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The channel(s) to fetch from.'
                },
                'name': 'channelList',
                'type': 'ViString'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': 'The maximum number of samples to fetch for each waveform. If the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. If it fails to complete within the timeout period, the function raises.'
                },
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'default_value': 'FetchRelativeTo.PRETRIGGER',
                'direction': 'in',
                'documentation': {
                    'description': 'Position to start fetching within one record.'
                },
                'enum': 'FetchRelativeTo',
                'grpc_enum': None,
                'name': 'relativeTo',
                'type': 'ViInt32'
            },
            {
                'default_value': 0,
                'direction': 'in',
                'documentation': {
                    'description': 'Offset in samples to start fetching data within each record. The offset can be positive or negative.'
                },
                'name': 'offset',
                'type': 'ViInt32'
            },
            {
                'default_value': 0,
                'direction': 'in',
                'documentation': {
                    'description': 'Zero-based index of the first record to fetch.'
                },
                'name': 'recordNumber',
                'type': 'ViInt32'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': 'Number of records to fetch. Use -1 to fetch all configured records.'
                },
                'name': 'numRecords',
                'type': 'ViInt32'
            },
            {
                'default_value': 'hightime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': 'The time to wait for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 seconds for this parameter implies infinite timeout.'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'python_type': 'hightime.timedelta, datetime.timedelta, or float',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a list of class instances with the following timing and scaling information about each waveform:\n\n-  **relative_initial_x** (float) the time (in seconds) from the trigger to the first sample in the fetched waveform\n-  **absolute_initial_x** (float) timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.\n-  **x_increment** (float) the time between points in the acquired waveform in seconds\n-  **channel** (str) channel name this waveform was acquired from\n-  **record** (int) record number of this waveform\n-  **gain** (float) the gain factor of the given channel; useful for scaling binary data with the following formula:\n\n    .. math::\n\n        voltage = binary data * gain factor + offset\n\n-  **offset** (float) the offset factor of the given channel; useful for scaling binary data with the following formula:\n\n    .. math::\n\n        voltage = binary data * gain factor + offset\n\n- **samples** (array of float) floating point array of samples. Length will be of the actual samples acquired\n'
                },
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'python-code',
                    'value': '(num_samples * self.actual_num_wfms(channel_list))'
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'python_name': 'fetch',
        'returns': 'ViStatus'
    },
    'FancyGetEqualizationFilterCoefficients': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Retrieves the custom coefficients for the equalization FIR filter on the device. This filter is designed to compensate the input signal for artifacts introduced to the signal outside of the digitizer. Because this filter is a generic FIR filter, any coefficients are valid. Coefficient values should be between +1 and –1.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'get_equalization_filter_coefficients'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The instrument handle you obtain from niScope_init that identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The channel to configure.'
                },
                'name': 'channel',
                'type': 'ViString'
            }
        ],
        'python_name': 'get_equalization_filter_coefficients',
        'returns': 'ViStatus'
    },
    'FancyGetExtCalLastDateAndTime': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Returns the date and time of the last external calibration performed.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_get_cal_last_date'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niScope_init.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **date** of the last calibration. A hightime.datetime object is returned, but only contains resolution to the day.'
                },
                'name': 'lastCalDatetime',
                'python_type': 'hightime.timedelta, datetime.timedelta, or float',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'python_name': 'get_ext_cal_last_date_and_time',
        'returns': 'ViStatus'
    },
    'FancyGetExtCalLastTemp': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Returns the onboard temperature, in degrees Celsius, of an oscilloscope at the time of the last successful external calibration.\nThe temperature returned by this node is an onboard temperature read from a sensor on the surface of the oscilloscope. This temperature should not be confused with the environmental temperature of the oscilloscope surroundings. During operation, the onboard temperature is normally higher than the environmental temperature.\nTemperature-sensitive parameters are calibrated during self-calibration. Therefore, the self-calibration temperature is usually more important to read than the external calibration temperature.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_get_cal_last_temp'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niScope_init.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **temperature** in degrees Celsius during the last calibration.'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'python_name': 'get_ext_cal_last_temp',
        'returns': 'ViStatus'
    },
    'FancyGetSelfCalLastDateAndTime': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Returns the date and time of the last self calibration performed.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_get_cal_last_date'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niScope_init.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **date** of the last calibration. A hightime.datetime object is returned, but only contains resolution to the day.'
                },
                'name': 'lastCalDatetime',
                'python_type': 'hightime.timedelta, datetime.timedelta, or float',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'python_name': 'get_self_cal_last_date_and_time',
        'returns': 'ViStatus'
    },
    'FancyGetSelfCalLastTemp': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Returns the onboard temperature, in degrees Celsius, of an oscilloscope at the time of the last successful self calibration.\nThe temperature returned by this node is an onboard temperature read from a sensor on the surface of the oscilloscope. This temperature should not be confused with the environmental temperature of the oscilloscope surroundings. During operation, the onboard temperature is normally higher than the environmental temperature.\nTemperature-sensitive parameters are calibrated during self-calibration. Therefore, the self-calibration temperature is usually more important to read than the external calibration temperature.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_get_cal_last_temp'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niScope_init.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **temperature** in degrees Celsius during the last calibration.'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'python_name': 'get_self_cal_last_temp',
        'returns': 'ViStatus'
    },
    'FancyRead': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nInitiates an acquisition, waits for it to complete, and retrieves the\ndata. The process is similar to calling niScope_InitiateAcquisition,\nniScope_AcquisitionStatus, and niScope_Fetch. The only difference is\nthat with niScope_Read, you enable all channels specified with\n**channelList** before the acquisition; in the other method, you enable\nthe channels with niScope_ConfigureVertical.\n\nThis function may return multiple waveforms depending on the number of\nchannels, the acquisition type, and the number of records you specify.',
            'note': 'Some functionality, such as time stamping, is not supported in all digitizers.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_fetch'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The instrument handle you obtain from niScope_init that identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The channel(s) to read from.'
                },
                'name': 'channelList',
                'type': 'ViString'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': 'The maximum number of samples to fetch for each waveform. If the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. If it fails to complete within the timeout period, the function raises.'
                },
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'default_value': 'FetchRelativeTo.PRETRIGGER',
                'direction': 'in',
                'documentation': {
                    'description': 'Position to start fetching within one record.'
                },
                'enum': 'FetchRelativeTo',
                'grpc_enum': None,
                'name': 'relativeTo',
                'type': 'ViInt32'
            },
            {
                'default_value': 0,
                'direction': 'in',
                'documentation': {
                    'description': 'Offset in samples to start fetching data within each record. The offset can be positive or negative.'
                },
                'name': 'offset',
                'type': 'ViInt32'
            },
            {
                'default_value': 0,
                'direction': 'in',
                'documentation': {
                    'description': 'Zero-based index of the first record to fetch.'
                },
                'name': 'recordNumber',
                'type': 'ViInt32'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': 'Number of records to fetch. Use -1 to fetch all configured records.'
                },
                'name': 'numRecords',
                'type': 'ViInt32'
            },
            {
                'default_value': 'hightime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': 'The time to wait for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 seconds for this parameter implies infinite timeout.'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'python_type': 'hightime.timedelta, datetime.timedelta, or float',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a list of class instances with the following timing and scaling information about each waveform:\n\n-  **relative_initial_x** (float) the time (in seconds) from the trigger to the first sample in the fetched waveform\n-  **absolute_initial_x** (float) timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.\n-  **x_increment** (float) the time between points in the acquired waveform in seconds\n-  **channel** (str) channel name this waveform was acquired from\n-  **record** (int) record number of this waveform\n-  **gain** (float) the gain factor of the given channel; useful for scaling binary data with the following formula:\n\n    .. math::\n\n        voltage = binary data * gain factor + offset\n\n-  **offset** (float) the offset factor of the given channel; useful for scaling binary data with the following formula:\n\n    .. math::\n\n        voltage = binary data * gain factor + offset\n\n- **samples** (array of float) floating point array of samples. Length will be of the actual samples acquired\n'
                },
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'python-code',
                    'value': '(num_samples * self.actual_num_wfms(channel_list))'
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'python_name': 'read',
        'returns': 'ViStatus'
    },
    'Fetch': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns the waveform from a previously initiated acquisition that the\ndigitizer acquires for the specified channel. This function returns\nscaled voltage waveforms.\n\nThis function may return multiple waveforms depending on the number of\nchannels, the acquisition type, and the number of records you specify.\n',
            'note': '\nYou can use niScope_Read instead of this function. niScope_Read\nstarts an acquisition on all enabled channels, waits for the acquisition\nto complete, and returns the waveform for the specified channel.\n\nSome functionality, such as time stamping, is not supported in all\ndigitizers. Refer to `Features Supported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for\nmore information.\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'fetch',
        'method_templates': [
            {
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            },
            {
                'library_interpreter_filename': 'numpy_read_method',
                'method_python_name_suffix': '_into_numpy',
                'session_filename': 'numpy_read_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'default_value': 'hightime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe maximum number of samples to fetch for each waveform. If the\nacquisition finishes with fewer points than requested, some devices\nreturn partial data if the acquisition finished, was aborted, or a\ntimeout of 0 was used. If it fails to complete within the timeout\nperiod, the function returns an error.\n'
                },
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array whose length is the **numSamples** times number of\nwaveforms. Call niScope_ActualNumwfms to determine the number of\nwaveforms.\n\nNI-SCOPE returns this data sequentially, so all record 0 waveforms are\nfirst. For example, with a channel list of 0,1, you would have the\nfollowing index values:\n\nindex 0 = record 0, channel 0\n\nindex *x* = record 0, channel 1\n\nindex 2\\ *x* = record 1, channel 0\n\nindex 3\\ *x* = record 1, channel 1\n\nWhere *x* = the record length\n'
                },
                'name': 'waveform',
                'numpy': True,
                'size': {
                    'mechanism': 'python-code',
                    'value': '(num_samples * self.actual_num_wfms(channel_list))'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a list of class instances with the following timing and scaling\ninformation about each waveform:\n\n-  **relativeInitialX**—the time (in seconds) from the trigger to the\n   first sample in the fetched waveform\n-  **absoluteInitialX**—timestamp (in seconds) of the first fetched\n   sample. This timestamp is comparable between records and\n   acquisitions; devices that do not support this parameter use 0 for\n   this output.\n-  **xIncrement**—the time between points in the acquired waveform in\n   seconds\n-  **actualSamples**—the actual number of samples fetched and placed in\n   the waveform array\n-  **gain**—the gain factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\n-  **offset**—the offset factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\nCall niScope_ActualNumWfms to determine the size of this array.\n'
                },
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self.actual_num_wfms(channel_list)'
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchArrayMeasurement': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nObtains a waveform from the digitizer and returns the specified\nmeasurement array. This function may return multiple waveforms depending\non the number of channels, the acquisition type, and the number of\nrecords you specify.\n',
            'note': '\nSome functionality, such as time stamping, is not supported in all\ndigitizers. Refer to `Features Supported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for\nmore information.\n'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'default_value': 'hightime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe `array\nmeasurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__\nto perform.\n'
                },
                'enum': 'ArrayMeasurement',
                'name': 'arrayMeasFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe maximum number of samples returned in the measurement waveform array\nfor each waveform measurement. Default Value: None (returns all available samples).\n',
                    'note': '\nUse the attribute NISCOPE_ATTR_FETCH_MEAS_NUM_SAMPLES to set the\nnumber of samples to fetch when performing a measurement. For more\ninformation about when to use this attribute, refer to the `NI\nKnowledgeBase <javascript:WWW(WWW_KB_MEAS)>`__.\n'
                },
                'grpc_name': 'meas_wfm_size',
                'name': 'measWfmSize',
                'python_name': 'measurement_waveform_size',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array whose length is the number of waveforms times\n**measurementWaveformSize**; call niScope_ActualNumWfms to determine the number of\nwaveforms; call niScope_ActualMeasWfmSize to determine the size of each\nwaveform.\n\nNI-SCOPE returns this data sequentially, so all record 0 waveforms are\nfirst. For example, with channel list of 0, 1, you would have the\nfollowing index values:\n\nindex 0 = record 0, channel 0\n\nindex *x* = record 0, channel 1\n\nindex 2\\ *x* = record 1, channel 0\n\nindex 3\\ *x* = record 1, channel 1\n\nWhere *x* = the record length\n'
                },
                'name': 'measWfm',
                'size': {
                    'mechanism': 'python-code',
                    'value': '(measurement_waveform_size * self.actual_num_wfms(channel_list))'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a list of class instances with the following timing and scaling\ninformation about each waveform:\n\n-  **relativeInitialX**—the time (in seconds) from the trigger to the\n   first sample in the fetched waveform\n-  **absoluteInitialX**—timestamp (in seconds) of the first fetched\n   sample. This timestamp is comparable between records and\n   acquisitions; devices that do not support this parameter use 0 for\n   this output.\n-  **xIncrement**—the time between points in the acquired waveform in\n   seconds\n-  **actualSamples**—the actual number of samples fetched and placed in\n   the waveform array\n-  **gain**—the gain factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\n-  **offset**—the offset factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\nCall niScope_ActualNumWfms to determine the size of this array.\n'
                },
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self.actual_num_wfms(channel_list)'
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchBinary16': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nRetrieves data from a previously initiated acquisition and returns\nbinary 16-bit waveforms. This function may return multiple waveforms\ndepending on the number of channels, the acquisition type, and the\nnumber of records you specify.\n\nRefer to `Using Fetch\nFunctions <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for\nmore information on using this function.\n',
            'note': '\nSome functionality, such as time stamping, is not supported in all\ndigitizers. Refer to `Features Supported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for\nmore information.\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'fetch_into',
        'method_templates': [
            {
                'library_interpreter_filename': 'numpy_read_method',
                'method_python_name_suffix': '_into_numpy',
                'session_filename': 'numpy_read_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'default_value': 'hightime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe maximum number of samples to fetch for each waveform. If the\nacquisition finishes with fewer points than requested, some devices\nreturn partial data if the acquisition finished, was aborted, or a\ntimeout of 0 was used. If it fails to complete within the timeout\nperiod, the function returns an error.\n'
                },
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array whose length is the **numSamples** times number of\nwaveforms. Call niScope_ActualNumwfms to determine the number of\nwaveforms.\n\nNI-SCOPE returns this data sequentially, so all record 0 waveforms are\nfirst. For example, with a channel list of 0,1, you would have the\nfollowing index values:\n\nindex 0 = record 0, channel 0\n\nindex *x* = record 0, channel 1\n\nindex 2\\ *x* = record 1, channel 0\n\nindex 3\\ *x* = record 1, channel 1\n\nWhere *x* = the record length\n'
                },
                'name': 'waveform',
                'numpy': True,
                'size': {
                    'mechanism': 'python-code',
                    'value': '(num_samples * self.actual_num_wfms(channel_list))'
                },
                'type': 'ViInt16[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a list of class instances with the following timing and scaling\ninformation about each waveform:\n\n-  **relativeInitialX**—the time (in seconds) from the trigger to the\n   first sample in the fetched waveform\n-  **absoluteInitialX**—timestamp (in seconds) of the first fetched\n   sample. This timestamp is comparable between records and\n   acquisitions; devices that do not support this parameter use 0 for\n   this output.\n-  **xIncrement**—the time between points in the acquired waveform in\n   seconds\n-  **actualSamples**—the actual number of samples fetched and placed in\n   the waveform array\n-  **gain**—the gain factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\n-  **offset**—the offset factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\nCall niScope_ActualNumWfms to determine the size of this array.\n'
                },
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self.actual_num_wfms(channel_list)'
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchBinary32': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nRetrieves data from a previously initiated acquisition and returns\nbinary 32-bit waveforms. This function may return multiple waveforms\ndepending on the number of channels, the acquisition type, and the\nnumber of records you specify.\n\nRefer to `Using Fetch\nFunctions <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for\nmore information on using this function.\n',
            'note': '\nSome functionality, such as time stamping, is not supported in all\ndigitizers. Refer to `Features Supported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for\nmore information.\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'fetch_into',
        'method_templates': [
            {
                'library_interpreter_filename': 'numpy_read_method',
                'method_python_name_suffix': '_into_numpy',
                'session_filename': 'numpy_read_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'default_value': 'hightime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe maximum number of samples to fetch for each waveform. If the\nacquisition finishes with fewer points than requested, some devices\nreturn partial data if the acquisition finished, was aborted, or a\ntimeout of 0 was used. If it fails to complete within the timeout\nperiod, the function returns an error.\n'
                },
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array whose length is the **numSamples** times number of\nwaveforms. Call niScope_ActualNumwfms to determine the number of\nwaveforms.\n\nNI-SCOPE returns this data sequentially, so all record 0 waveforms are\nfirst. For example, with a channel list of 0,1, you would have the\nfollowing index values:\n\nindex 0 = record 0, channel 0\n\nindex *x* = record 0, channel 1\n\nindex 2\\ *x* = record 1, channel 0\n\nindex 3\\ *x* = record 1, channel 1\n\nWhere *x* = the record length\n'
                },
                'name': 'waveform',
                'numpy': True,
                'size': {
                    'mechanism': 'python-code',
                    'value': '(num_samples * self.actual_num_wfms(channel_list))'
                },
                'type': 'ViInt32[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a list of class instances with the following timing and scaling\ninformation about each waveform:\n\n-  **relativeInitialX**—the time (in seconds) from the trigger to the\n   first sample in the fetched waveform\n-  **absoluteInitialX**—timestamp (in seconds) of the first fetched\n   sample. This timestamp is comparable between records and\n   acquisitions; devices that do not support this parameter use 0 for\n   this output.\n-  **xIncrement**—the time between points in the acquired waveform in\n   seconds\n-  **actualSamples**—the actual number of samples fetched and placed in\n   the waveform array\n-  **gain**—the gain factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\n-  **offset**—the offset factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\nCall niScope_ActualNumWfms to determine the size of this array.\n'
                },
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self.actual_num_wfms(channel_list)'
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchBinary8': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nRetrieves data from a previously initiated acquisition and returns\nbinary 8-bit waveforms. This function may return multiple waveforms\ndepending on the number of channels, the acquisition type, and the\nnumber of records you specify.\n\nRefer to `Using Fetch\nFunctions <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for\nmore information on using this function.\n',
            'note': '\nSome functionality, such as time stamping, is not supported in all\ndigitizers. Refer to `Features Supported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for\nmore information.\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'fetch_into',
        'method_templates': [
            {
                'library_interpreter_filename': 'numpy_read_method',
                'method_python_name_suffix': '_into_numpy',
                'session_filename': 'numpy_read_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'default_value': 'hightime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe maximum number of samples to fetch for each waveform. If the\nacquisition finishes with fewer points than requested, some devices\nreturn partial data if the acquisition finished, was aborted, or a\ntimeout of 0 was used. If it fails to complete within the timeout\nperiod, the function returns an error.\n'
                },
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array whose length is the **numSamples** times number of\nwaveforms. Call niScope_ActualNumwfms to determine the number of\nwaveforms.\n\nNI-SCOPE returns this data sequentially, so all record 0 waveforms are\nfirst. For example, with a channel list of 0,1, you would have the\nfollowing index values:\n\nindex 0 = record 0, channel 0\n\nindex *x* = record 0, channel 1\n\nindex 2\\ *x* = record 1, channel 0\n\nindex 3\\ *x* = record 1, channel 1\n\nWhere *x* = the record length\n'
                },
                'name': 'waveform',
                'numpy': True,
                'size': {
                    'mechanism': 'python-code',
                    'value': '(num_samples * self.actual_num_wfms(channel_list))'
                },
                'type': 'ViInt8[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a list of class instances with the following timing and scaling\ninformation about each waveform:\n\n-  **relativeInitialX**—the time (in seconds) from the trigger to the\n   first sample in the fetched waveform\n-  **absoluteInitialX**—timestamp (in seconds) of the first fetched\n   sample. This timestamp is comparable between records and\n   acquisitions; devices that do not support this parameter use 0 for\n   this output.\n-  **xIncrement**—the time between points in the acquired waveform in\n   seconds\n-  **actualSamples**—the actual number of samples fetched and placed in\n   the waveform array\n-  **gain**—the gain factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\n-  **offset**—the offset factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\nCall niScope_ActualNumWfms to determine the size of this array.\n'
                },
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self.actual_num_wfms(channel_list)'
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchDispatcher': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nReturns the waveform from a previously initiated acquisition that the\ndigitizer acquires for the specified channel. This function returns\nscaled voltage waveforms.\n\nThis function may return multiple waveforms depending on the number of\nchannels, the acquisition type, and the number of records you specify.',
            'note': 'Some functionality, such as time stamping, is not supported in all digitizers.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '_into',
                'session_filename': 'fetch_waveform'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The instrument handle you obtain from niScope_init that identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The channel(s) to fetch from.'
                },
                'name': 'channelList',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nnumpy array of the appropriate type and size that should be acquired as a 1D array. Size should be **num_samples** times number of waveforms. Call niScope_ActualNumWfms to determine the number of waveforms.\n\nTypes supported are\n\n- `numpy.float64`\n- `numpy.int8`\n- `numpy.in16`\n- `numpy.int32`\n\nExample:\n\n.. code-block:: python\n\n    waveform = numpy.ndarray(num_samples * session.actual_num_wfms(), dtype=numpy.float64)\n    wfm_info = session['0,1'].fetch_into(waveform, timeout=5.0)"
                },
                'name': 'waveform',
                'numpy': True,
                'type': 'ViReal64',
                'use_array': True
            },
            {
                'default_value': 'FetchRelativeTo.PRETRIGGER',
                'direction': 'in',
                'documentation': {
                    'description': 'Position to start fetching within one record.'
                },
                'enum': 'FetchRelativeTo',
                'grpc_enum': None,
                'name': 'relativeTo',
                'type': 'ViInt32'
            },
            {
                'default_value': 0,
                'direction': 'in',
                'documentation': {
                    'description': 'Offset in samples to start fetching data within each record.The offset can be positive or negative.'
                },
                'name': 'offset',
                'type': 'ViInt32'
            },
            {
                'default_value': 0,
                'direction': 'in',
                'documentation': {
                    'description': 'Zero-based index of the first record to fetch.'
                },
                'name': 'recordNumber',
                'type': 'ViInt32'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': 'Number of records to fetch. Use -1 to fetch all configured records.'
                },
                'name': 'numRecords',
                'type': 'ViInt32'
            },
            {
                'default_value': 'hightime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': 'The time to wait in seconds for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout.'
                },
                'name': 'timeout',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a list of class instances with the following timing and scaling information about each waveform:\n\n-  **relative_initial_x** (float) the time (in seconds) from the trigger to the first sample in the fetched waveform\n-  **absolute_initial_x** (float) timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.\n-  **x_increment** (float) the time between points in the acquired waveform in seconds\n-  **channel** (str) channel name this waveform was acquired from\n-  **record** (int) record number of this waveform\n-  **gain** (float) the gain factor of the given channel; useful for scaling binary data with the following formula:\n\n    .. math::\n\n        voltage = binary data * gain factor + offset\n\n-  **offset** (float) the offset factor of the given channel; useful for scaling binary data with the following formula:\n\n    .. math::\n\n        voltage = binary data * gain factor + offset\n\n- **samples** (array of float) floating point array of samples. Length will be of the actual samples acquired\n'
                },
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self.actual_num_wfms(channel_list)'
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'python_name': 'fetch',
        'returns': 'ViStatus'
    },
    'FetchMeasurementStats': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nObtains a waveform measurement and returns the measurement value. This\nfunction may return multiple statistical results depending on the number\nof channels, the acquisition type, and the number of records you\nspecify.\n\nYou specify a particular measurement type, such as rise time, frequency,\nor voltage peak-to-peak. The waveform on which the digitizer calculates\nthe waveform measurement is from an acquisition that you previously\ninitiated. The statistics for the specified measurement function are\nreturned, where the statistics are updated once every acquisition when\nthe specified measurement is fetched by any of the Fetch Measurement\nfunctions. If a Fetch Measurement function has not been called, this\nfunction fetches the data on which to perform the measurement. The\nstatistics are cleared by calling\nniScope_ClearWaveformMeasurementStats. Refer to `Using Fetch\nFunctions <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for\nmore information on incorporating fetch functions in your application.\n\nMany of the measurements use the low, mid, and high reference levels.\nYou configure the low, mid, and high references with\nNISCOPE_ATTR_MEAS_CHAN_LOW_REF_LEVEL,\nNISCOPE_ATTR_MEAS_CHAN_MID_REF_LEVEL, and\nNISCOPE_ATTR_MEAS_CHAN_HIGH_REF_LEVEL to set each channel\ndifferently.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'default_value': 'hightime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe `scalar\nmeasurement <REPLACE_DRIVER_SPECIFIC_URL_2(scalar_measurements_refs)>`__\nto be performed on each fetched waveform.\n'
                },
                'enum': 'ScalarMeasurement',
                'name': 'scalarMeasFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the resulting measurement'
                },
                'name': 'result',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self.actual_num_wfms(channel_list)'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the mean scalar value, which is obtained by averaging each\nniScope_FetchMeasurementStats call.\n'
                },
                'name': 'mean',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self.actual_num_wfms(channel_list)'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the standard deviation of the most recent **numInStats**\nmeasurements.\n'
                },
                'name': 'stdev',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self.actual_num_wfms(channel_list)'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the smallest scalar value acquired (the minimum of the\n**numInStats** measurements).\n'
                },
                'name': 'min',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self.actual_num_wfms(channel_list)'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the largest scalar value acquired (the maximum of the\n**numInStats** measurements).\n'
                },
                'name': 'max',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self.actual_num_wfms(channel_list)'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the number of times niScope_FetchMeasurementStats has been\ncalled.\n'
                },
                'name': 'numInStats',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self.actual_num_wfms(channel_list)'
                },
                'type': 'ViInt32[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViBoolean attribute. You can use this function to\nget the values of instrument-specific attributes and inherent IVI\nattributes. If the attribute represents an instrument state, this\nfunction performs instrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute; pass the address of a\nViBoolean variable.\n'
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
            'description': '\nQueries the value of a ViInt32 attribute. You can use this function to\nget the values of instrument-specific attributes and inherent IVI\nattributes. If the attribute represents an instrument state, this\nfunction performs instrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the current value of the attribute.'
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
            'description': '\nQueries the value of a ViInt64 attribute. You can use this function to\nget the values of instrument-specific attributes and inherent IVI\nattributes. If the attribute represents an instrument state, this\nfunction performs instrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the current value of the attribute.'
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
            'description': '\nQueries the value of a ViReal64 attribute. You can use this function to\nget the values of instrument-specific attributes and inherent IVI\nattributes. If the attribute represents an instrument state, this\nfunction performs instrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute; pass the address of a\nViReal64 variable.\n'
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
            'description': '\nQueries the value of a ViString attribute. You can use this function to\nget the values of instrument-specific attributes and inherent IVI\nattributes. If the attribute represents an instrument state, this\nfunction performs instrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid.\n\nYou must provide a ViChar array to serve as a buffer for the value. You\npass the number of bytes in the buffer as the **bufSize**. If the\ncurrent value of the attribute, including the terminating NUL byte, is\nlarger than the size you indicate in the **bufSize**, the function\ncopies (**bufSize** – 1) bytes into the buffer, places an ASCII NUL byte\nat the end of the buffer, and returns the **bufSize** you must pass to\nget the entire value. For example, if the value is 123456 and the\n**bufSize** is 4, the function places 123 into the buffer and returns 7.\nIf you want to call this function just to get the required buffer size,\nyou can pass 0 for the **bufSize** and VI_NULL for the **value**.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of bytes in the ViChar array you specify for **value**.'
                },
                'name': 'bufSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe buffer in which the function returns the current value of the\nattribute; the buffer must be of type ViChar and have at least as many\nbytes as indicated in the **bufSize**.\n'
                },
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufSize'
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
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
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
                    'description': 'The number of elements in the ViChar array you specify for name.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The channel name(s) at the specified indices.\n'
                },
                'grpc_name': 'name',
                'name': 'name',
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
        'python_name': 'get_channel_names',
        'returns': 'ViStatus'
    },
    'GetEqualizationFilterCoefficients': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nRetrieves the custom coefficients for the equalization FIR filter on the\ndevice. This filter is designed to compensate the input signal for\nartifacts introduced to the signal outside of the digitizer. Because\nthis filter is a generic FIR filter, any coefficients are valid.\nCoefficient values should be between +1 and –1.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channel',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of coefficients being passed in the **coefficients** array.'
                },
                'name': 'numberOfCoefficients',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe custom coefficients for the equalization FIR filter on the device.\nThese coefficients should be between +1 and –1. You can obtain the\nnumber of coefficients from the\n`NISCOPE_ATTR_EQUALIZATION_NUM_COEFFICIENTS <cviNISCOPE_ATTR_EQUALIZATION_NUM_COEFFICIENTS.html>`__\nattribute.\n'
                },
                'name': 'coefficients',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfCoefficients'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetError': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReads an error code and message from the error queue. NI\ndigitizers do not contain an error queue. Errors are\nreported as they occur. Therefore, this function does not detect errors.\n',
            'note': '\nThis function is included for compliance with the IviScope Class\nSpecification.\n'
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
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nPasses the number of bytes in the ViChar array you specify for the\nDescription parameter.\n\nIf the error description, including the terminating NULL byte, contains\nmore bytes than you indicate in this parameter, the function copies\n**bufferSize** – 1 bytes into the buffer, places an ASCII NULL byte at\nthe end of the buffer, and returns the buffer size you must pass to get\nthe entire value. For example, if the value is "123456" and the Buffer\nSize is 4, the function places "123" into the buffer and returns 7.\n\nIf you pass a negative number, the function copies the value to the\nbuffer regardless of the number of bytes in the value.\n\nIf you pass 0, you can pass VI_NULL for the **description** parameter.\n'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the Error Code that is returned from any of the instrument driver\nfunctions.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the error description for the IVI session or execution thread.\n\nIf there is no description, the function returns an empty string. The\nbuffer must contain at least as many elements as the value you specify\nwith the Buffer Size parameter.\n\nIf you pass 0 for the **bufferSize**, you can pass VI_NULL for this\nparameter.\n'
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
    'ImportAttributeConfigurationBuffer': {
        'documentation': {
            'description': '\nImports an attribute configuration to the session from the specified\nconfiguration buffer.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers, channel counts, and onboard memory\nsizes.\n\n**Related Topics:**\n\n`Attributes and Attribute\nFunctions <REPLACE_DRIVER_SPECIFIC_URL_1(attributes_and_attribute_functions)>`__\n\n`Setting Attributes Before Reading\nAttributes <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__\n',
            'note': '\nYou cannot call this function while the session is in a running state,\nsuch as while acquiring a signal.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the size, in bytes, of the byte array to import. If you enter\n0, this function returns the needed size.\n'
                },
                'name': 'sizeInBytes',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the byte array buffer that contains the attribute\nconfiguration to import.\n'
                },
                'name': 'configuration',
                'python_api_converter_name': 'convert_to_bytes',
                'size': {
                    'mechanism': 'len',
                    'value': 'sizeInBytes'
                },
                'type': 'ViInt8[]',
                'type_in_documentation': 'bytes'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributeConfigurationFile': {
        'documentation': {
            'description': '\nImports an attribute configuration to the session from the specified\nfile.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers, channel counts, and onboard memory\nsizes.\n\n**Related Topics:**\n\n`Attributes and Attribute\nFunctions <REPLACE_DRIVER_SPECIFIC_URL_1(attributes_and_attribute_functions)>`__\n\n`Setting Attributes Before Reading\nAttributes <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__\n',
            'note': '\nYou cannot call this function while the session is in a running state,\nsuch as while acquiring a signal.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the absolute path to the file containing the attribute\nconfiguration to import. If you specify an empty or relative path, this\nfunction returns an error.\n**Default File Extension:** .niscopeconfig\n'
                },
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitWithOptions': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nPerforms the following initialization actions:\n\n-  Creates a new IVI instrument driver and optionally sets the initial\n   state of the following session properties: Range Check, Cache,\n   Simulate, Record Value Coercions\n-  Opens a session to the specified device using the interface and\n   address you specify for the **resourceName**\n-  Resets the digitizer to a known state if **resetDevice** is set to\n   VI_TRUE\n-  Queries the instrument ID and verifies that it is valid for this\n   instrument driver if the **IDQuery** is set to VI_TRUE\n-  Returns an instrument handle that you use to identify the instrument\n   in all subsequent instrument driver function calls\n'
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
                    'caution': '\nTraditional NI-DAQ and NI-DAQmx device names are not case-sensitive.\nHowever, all IVI names, such as logical names, are case-sensitive. If\nyou use logical names, driver session names, or virtual names in your\nprogram, you must make sure that the name you use matches the name in\nthe IVI Configuration Store file exactly, without any variations in the\ncase of the characters.\n',
                    'description': '\n| Specifies the resource name of the device to initialize\n\nFor Traditional NI-DAQ devices, the syntax is DAQ::\\ *n*, where *n* is\nthe device number assigned by MAX, as shown in Example 1.\n\nFor NI-DAQmx devices, the syntax is just the device name specified in\nMAX, as shown in Example 2. Typical default names for NI-DAQmx devices\nin MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by\nright-clicking on the name in MAX and entering a new name.\n\nAn alternate syntax for NI-DAQmx devices consists of DAQ::NI-DAQmx\ndevice name, as shown in Example 3. This naming convention allows for\nthe use of an NI-DAQmx device in an application that was originally\ndesigned for a Traditional NI-DAQ device. For example, if the\napplication expects DAQ::1, you can rename the NI-DAQmx device to 1 in\nMAX and pass in DAQ::1 for the resource name, as shown in Example 4.\n\nIf you use the DAQ::\\ *n* syntax and an NI-DAQmx device name already\nexists with that same name, the NI-DAQmx device is matched first.\n\nYou can also pass in the name of an IVI logical name or an IVI virtual\nname configured with the IVI Configuration utility, as shown in Example\n5. A logical name identifies a particular virtual instrument. A virtual\nname identifies a specific device and specifies the initial settings for\nthe session.\n',
                    'table_body': [
                        [
                            '1',
                            'Traditional NI-DAQ device',
                            'DAQ::1 (1 = device number)'
                        ],
                        [
                            '2',
                            'NI-DAQmx device',
                            'myDAQmxDevice (myDAQmxDevice = device name)'
                        ],
                        [
                            '3',
                            'NI-DAQmx device',
                            'DAQ::myDAQmxDevice (myDAQmxDevice = device name)'
                        ],
                        [
                            '4',
                            'NI-DAQmx device',
                            'DAQ::2 (2 = device name)'
                        ],
                        [
                            '5',
                            'IVI logical name or IVI virtual name',
                            'myLogicalName (myLogicalName = name)'
                        ]
                    ],
                    'table_header': [
                        'Example',
                        'Device Type',
                        'Syntax'
                    ]
                },
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecify whether to perform an ID query.\n\nWhen you set this parameter to VI_TRUE, NI-SCOPE verifies that the\ndevice you initialize is a type that it supports.\n\nWhen you set this parameter to VI_FALSE, the function initializes the\ndevice without performing an ID query.\n\n**Defined Values**\n\n| VI_TRUE—Perform ID query\n| VI_FALSE—Skip ID query\n\n**Default Value**: VI_TRUE\n'
                },
                'name': 'idQuery',
                'type': 'ViBoolean'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecify whether to reset the device during the initialization process.\n\nDefault Value: VI_TRUE\n\n**Defined Values**\n\nVI_TRUE (1)—Reset device\n\nVI_FALSE (0)—Do not reset device\n',
                    'note': '\nFor the NI 5112, repeatedly resetting the device may cause excessive\nwear on the electromechanical relays. Refer to `NI 5112\nElectromechanical Relays <REPLACE_DRIVER_SPECIFIC_URL_1(5112_relays)>`__\nfor recommended programming practices.\n'
                },
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'default_value': '""',
                'direction': 'in',
                'documentation': {
                    'description': '\n| Specifies initialization commands. The following table lists the\n  attributes and the name you use in the **optionString** to identify\n  the attribute.\n\nDefault Values: "Simulate=0,RangeCheck=1,QueryInstrStatus=1,Cache=1"\n\nYou can use the option string to simulate a device. The DriverSetup flag\nspecifies the model that is to be simulated and the type of the model.\nOne example to simulate an NI PXI-5102 would be as follows:\n\nOption String: Simulate = 1, DriverSetup = Model:5102; BoardType:PXI\n\nRefer to the example niScope EX Simulated Acquisition for more\ninformation on simulation.\n\nYou can also use the option string to attach an accessory such as the\nNI 5900 to your digitizer session to allow the seamless use of the\naccessory:\n\nOption String: DriverSetup = Accessory:Dev1\n\nRefer to the example niScope EX External Amplifier for more information.\n',
                    'table_body': [
                    ]
                },
                'name': 'optionString',
                'python_api_converter_name': 'convert_init_with_options_dictionary',
                'type': 'ViConstString',
                'type_in_documentation': 'dict'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a session handle that you can use to identify the device in all\nsubsequent NI-SCOPE function calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'InitiateAcquisition': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nInitiates a waveform acquisition.\n\nAfter calling this function, the digitizer leaves the Idle state and\nwaits for a trigger. The digitizer acquires a waveform for each channel\nyou enable with niScope_ConfigureVertical.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'LockSession': {
        'documentation': {
            'description': '\nObtains a multithread lock on the instrument session. Before doing so,\nit waits until all other execution threads have released their locks on\nthe instrument session. Other threads might have obtained a lock on this\nsession in the following ways:\n\n-  Your application called niScope_LockSession\n-  A call to the instrument driver locked the session\n-  A call to the IVI engine locked the session\n\nAfter your call to niScope_LockSession returns successfully, no other\nthreads can access the instrument session until you call\nniScope_UnlockSession. Use niScope_LockSession and\nniScope_UnlockSession around a sequence of calls to instrument driver\nfunctions if you require that the instrument retain its settings through\nthe end of the sequence.\n\nYou can safely make nested calls to niScope_LockSession within the same\nthread. To completely unlock the session, you must balance each call to\nniScope_LockSession with a call to niScope_UnlockSession. If, however,\nyou use the **callerHasLock** in all calls to niScope_LockSession and\nniScope_UnlockSession within a function, the IVI Library locks the\nsession only once within the function regardless of the number of calls\nyou make to niScope_LockSession. This allows you to call\nniScope_UnlockSession just once at the end of the function.\n'
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
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter serves as a convenience. If you do not want to use this\nparameter, pass VI_NULL.\n\nUse this parameter in complex functions to keep track of whether you\nhave obtained a lock and therefore need to unlock the session. Pass the\naddress of a local ViBoolean variable. In the declaration of the local\nvariable, initialize it to VI_FALSE. Pass the address of the same local\nvariable to any other calls you make to niScope_LockSession or\nniScope_UnlockSession in the same function.\n'
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
    'ProbeCompensationSignalStart': {
        'documentation': {
            'description': 'Starts the 1 kHz square wave output on PFI 1 for probe compensation.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ProbeCompensationSignalStop': {
        'documentation': {
            'description': 'Stops the 1 kHz square wave output on PFI 1 for probe compensation.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'Read': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nInitiates an acquisition, waits for it to complete, and retrieves the\ndata. The process is similar to calling niScope_InitiateAcquisition,\nniScope_AcquisitionStatus, and niScope_Fetch. The only difference is\nthat with niScope_Read, you enable all channels specified with\n**channelList** before the acquisition; in the other method, you enable\nthe channels with niScope_ConfigureVertical.\n\nThis function may return multiple waveforms depending on the number of\nchannels, the acquisition type, and the number of records you specify.\n',
            'note': '\nSome functionality is not supported in all digitizers. Refer to\n`Features Supported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for\nmore information.\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'read',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'default_value': 'hightime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe maximum number of samples to fetch for each waveform. If the\nacquisition finishes with fewer points than requested, some devices\nreturn partial data if the acquisition finished, was aborted, or a\ntimeout of 0 was used. If it fails to complete within the timeout\nperiod, the function returns an error.\n'
                },
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array whose length is the **numSamples** times number of\nwaveforms. Call niScope_ActualNumwfms to determine the number of\nwaveforms.\n\nNI-SCOPE returns this data sequentially, so all record 0 waveforms are\nfirst. For example, with a channel list of 0,1, you would have the\nfollowing index values:\n\nindex 0 = record 0, channel 0\n\nindex *x* = record 0, channel 1\n\nindex 2\\ *x* = record 1, channel 0\n\nindex 3\\ *x* = record 1, channel 1\n\nWhere *x* = the record length\n'
                },
                'name': 'waveform',
                'size': {
                    'mechanism': 'python-code',
                    'value': '(num_samples * self.actual_num_wfms(channel_list))'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a list of class instances with the following timing and scaling\ninformation about each waveform:\n\n-  **relativeInitialX**—the time (in seconds) from the trigger to the\n   first sample in the fetched waveform\n-  **absoluteInitialX**—timestamp (in seconds) of the first fetched\n   sample. This timestamp is comparable between records and\n   acquisitions; devices that do not support this parameter use 0 for\n   this output.\n-  **xIncrement**—the time between points in the acquired waveform in\n   seconds\n-  **actualSamples**—the actual number of samples fetched and placed in\n   the waveform array\n-  **gain**—the gain factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\n-  **offset**—the offset factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\nCall niScope_ActualNumWfms to determine the size of this array.\n'
                },
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self.actual_num_wfms(channel_list)'
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetDevice': {
        'documentation': {
            'description': '\nPerforms a hard reset of the device. Acquisition stops, all routes are\nreleased, RTSI and PFI lines are tristated, hardware is configured to\nits default state, and all session attributes are reset to their default\nstate.\n\n-  `Thermal Shutdown <digitizers.chm::/Thermal_Shutdown.html>`__\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetWithDefaults': {
        'documentation': {
            'description': '\nPerforms a software reset of the device, returning it to the default\nstate and applying any initial default settings from the IVI\nConfiguration Store.\n'
        },
        'included_in_proto': False,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SendSoftwareTriggerEdge': {
        'documentation': {
            'description': '\nSends the selected trigger to the digitizer. Call this function if you\ncalled niScope_ConfigureTriggerSoftware when you want the Reference\ntrigger to occur. You can also call this function to override a misused\nedge, digital, or hysteresis trigger. If you have configured\nNISCOPE_ATTR_ACQ_ARM_SOURCE, NISCOPE_ATTR_ARM_REF_TRIG_SRC, or\nNISCOPE_ATTR_ADV_TRIG_SRC, call this function when you want to send\nthe corresponding trigger to the digitizer.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the type of trigger to send to the digitizer.\n\n**Defined Values**\n\n| NISCOPE_VAL_SOFTWARE_TRIGGER_START (0L)\n|  NISCOPE_VAL_SOFTWARE_TRIGGER_ARM_REFERENCE (1L)\n| NISCOPE_VAL_SOFTWARE_TRIGGER_REFERENCE (2L)\n| NISCOPE_VAL_SOFTWARE_TRIGGER_ADVANCE (3L)\n'
                },
                'enum': 'WhichTrigger',
                'name': 'whichTrigger',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of a ViBoolean attribute. This is a low-level function\nthat you can use to set the values of instrument-specific attributes and\ninherent IVI attributes. If the attribute represents an instrument\nstate, this function performs instrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid or\n   is different than the value you specify.\n',
            'note': '\nNI-SCOPE contains high-level functions that set most of the instrument\nattributes. Use the high-level driver functions as much as possible\nbecause they handle order dependencies and multithread locking for you.\nIn addition, the high-level functions perform status checking only after\nsetting all of the attributes. In contrast, when you set multiple\nattributes using the SetAttribute functions, the functions check the\ninstrument status after each call. Also, when state caching is enabled,\nthe high-level functions that configure multiple attributes perform\ninstrument I/O only for the attributes whose value you change. Thus, you\ncan safely call the high-level functions without the penalty of\nredundant instrument I/O.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe value that you want to set the attribute to. Some values might not\nbe valid depending on the current settings of the instrument session.\n'
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
            'description': '\nSets the value of a ViInt32 attribute. This is a low-level function that\nyou can use to set the values of instrument-specific attributes and\ninherent IVI attributes. If the attribute represents an instrument\nstate, this function performs instrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid or\n   is different than the value you specify.\n',
            'note': '\nNI-SCOPE contains high-level functions that set most of the instrument\nattributes. Use the high-level functions as much as possible because\nthey handle order dependencies and multithread locking for you. In\naddition, high-level functions perform status checking only after\nsetting all of the attributes. In contrast, when you set multiple\nattributes using the Set Attribute functions, the functions check the\ninstrument status after each call. Also, when state caching is enabled,\nthe high-level functions that configure multiple attributes perform\ninstrument I/O only for the attributes whose value you change. Thus, you\ncan safely call the high-level functions without the penalty of\nredundant instrument I/O.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe value that you want to set the attribute. Some values might not be\nvalid depending on the current settings of the instrument session.\n'
                },
                'grpc_enum': 'NiScopeInt32AttributeValues',
                'name': 'value',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of a ViInt64 attribute. This is a low-level function that\nyou can use to set the values of instrument-specific attributes and\ninherent IVI attributes. If the attribute represents an instrument\nstate, this function performs instrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid or\n   is different than the value you specify.\n',
            'note': '\nNI-SCOPE contains high-level functions that set most of the instrument\nattributes. Use the high-level functions as much as possible because\nthey handle order dependencies and multithread locking for you. In\naddition, high-level functions perform status checking only after\nsetting all of the attributes. In contrast, when you set multiple\nattributes using the Set Attribute functions, the functions check the\ninstrument status after each call. Also, when state caching is enabled,\nthe high-level functions that configure multiple attributes perform\ninstrument I/O only for the attributes whose value you change. Thus, you\ncan safely call the high-level functions without the penalty of\nredundant instrument I/O.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe value that you want to set the attribute. Some values might not be\nvalid depending on the current settings of the instrument session.\n'
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
            'description': '\nSets the value of a ViReal64 attribute. This is a low-level function\nthat you can use to set the values of instrument-specific attributes and\ninherent IVI attributes. If the attribute represents an instrument\nstate, this function performs instrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid or\n   is different than the value you specify.\n',
            'note': '\nNI-SCOPE contains high-level functions that set most of the instrument\nattributes. Use the high-level driver functions as much as possible\nbecause they handle order dependencies and multithread locking for you.\nIn addition, the high-level functions perform status checking only after\nsetting all of the attributes. In contrast, when you set multiple\nattributes using the Set Attribute functions, the functions check the\ninstrument status after each call. Also, when state caching is enabled,\nthe high-level functions that configure multiple attributes perform\ninstrument I/O only for the attributes whose value you change. Thus, you\ncan safely call the high-level functions without the penalty of\nredundant instrument I/O.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe value that you want to set the attribute to. Some values might not\nbe valid depending on the current settings of the instrument session.\n'
                },
                'grpc_enum': 'NiScopeReal64AttributeValues',
                'name': 'value',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of a ViString attribute.\n\nThis is a low-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes. If the\nattribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid or\n   is different than the value you specify.\n',
            'note': '\nNI-SCOPE contains high-level functions that set most of the instrument\nattributes. Use the high-level driver functions as much as possible\nbecause they handle order dependencies and multithread locking for you.\nIn addition, the high-level functions perform status checking only after\nsetting all of the attributes. In contrast, when you set multiple\nattributes using the SetAttribute functions, the functions check the\ninstrument status after each call. Also, when state caching is enabled,\nthe high-level functions that configure multiple attributes perform\ninstrument I/O only for the attributes whose value you change. Thus, you\ncan safely call the high-level functions without the penalty of\nredundant instrument I/O.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe value that you want to set the attribute to. Some values might not\nbe valid depending on the current settings of the instrument session.\n'
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
    'UnlockSession': {
        'documentation': {
            'description': '\nReleases a lock that you acquired on an instrument session using\nniScope_LockSession.\n'
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
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter serves as a convenience; if you do not want to use this\nparameter, pass VI_NULL.\n\nUse this parameter in complex functions to keep track of whether you\nhave obtained a lock and therefore need to unlock the session; pass the\naddress of a local ViBoolean variable; in the declaration of the local\nvariable, initialize it to VI_FALSE; pass the address of the same local\nvariable to any other calls you make to niScope_LockSession or\nniScope_UnlockSession in the same function.\n'
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
    'close': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nWhen you are finished using an instrument driver session, you must call\nthis function to perform the following actions:\n\n-  Closes the instrument I/O session.\n-  Destroys the IVI session and all of its attributes.\n-  Deallocates any memory resources used by the IVI session.\n'
        },
        'grpc_name': 'Close',
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
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
            'description': 'Takes the **Error_Code** returned by the instrument driver functions, interprets it, and returns it as a user-readable string.',
            'note': '\nWhen using grpc-device, this method will call GetErrorMessage server-side while providing the same interface.\n'
        },
        'grpc_name': 'GetErrorMessage',
        'included_in_proto': True,
        'is_error_handling': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niScope_init or niScope_InitWithOptions. The default is None.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The **error_code** returned from the instrument. The default is 0, indicating VI_SUCCESS.'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The error information formatted into a string.'
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
            'description': '\nRuns the instrument self-test routine and returns the test result(s). Refer to the\ndevice-specific help topics for an explanation of the message contents.\n\nRaises `SelfTestError` on self test failure. Attributes on exception object:\n\n- code - failure code from driver\n- message - status message from driver\n',
            'table_body': [
                [
                    '0',
                    'Passed self-test'
                ],
                [
                    '1',
                    'Self-test failed'
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
                    'description': 'The instrument handle you obtain from niScope_init that identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': 'self_test',
        'returns': 'ViStatus'
    },
    'reset': {
        'documentation': {
            'description': "\nStops the acquisition, releases routes, and all session attributes are\nreset to their `default\nstates <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cviattribute_defaults)>`__.\n"
        },
        'grpc_name': 'Reset',
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
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
            'description': 'Runs the instrument self-test routine and returns the test result(s).'
        },
        'grpc_name': 'SelfTest',
        'included_in_proto': True,
        'method_name_for_documentation': 'self_test',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis control contains the value returned from the instrument self-test.\n\n**Self-Test Code Description**\n\n0—Self-test passed\n\n1—Self-test failed\n'
                },
                'name': 'selfTestResult',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the self-test response string from the instrument. Refer to the\ndevice-specific help topics for an explanation of the string contents;\nyou must pass a ViChar array at least IVI_MAX_MESSAGE_BUF_SIZE bytes\nin length.\n'
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

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/metadata/functions_addon.py sha256=49d9dd6a418b5b48cee4b81f13e844498033e2e01526f72f58684727b53ae0c2 bytes=12340 -->
## FILE: src/niscope/metadata/functions_addon.py

- repository: `ni/nimi-python`
- source_path: `src/niscope/metadata/functions_addon.py`
- sha256: `49d9dd6a418b5b48cee4b81f13e844498033e2e01526f72f58684727b53ae0c2`
- bytes: 12340

````python
# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {}
functions_additional_fetch_array_measurement = {
    'FancyFetchArrayMeasurement': {
        'codegen_method': 'python-only',
        'python_name': 'fetch_array_measurement',
        'documentation': {
            'description': '\nObtains a waveform from the digitizer and returns the specified\nmeasurement array. This function may return multiple waveforms depending\non the number of channels, the acquisition type, and the number of\nrecords you specify.\n',
            'note': '\nSome functionality, such as time stamping, is not supported in all\ndigitizers.\n'
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_fetch_array_measurement'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe array measurement to perform.\n'
                },
                'enum': 'ArrayMeasurement',
                'name': 'arrayMeasFunction',
                'type': 'ViInt32'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': '\nThe maximum number of samples returned in the measurement waveform array\nfor each waveform measurement. Default Value: None (returns all available samples).\n',
                },
                'name': 'measWfmSize',
                'type': 'ViInt32'
            },
            {
                'default_value': 'FetchRelativeTo.PRETRIGGER',
                'direction': 'in',
                'documentation': {
                    'description': 'Position to start fetching within one record.'
                },
                'enum': 'FetchRelativeTo',
                'name': 'relativeTo',
                'type': 'ViInt32'
            },
            {
                'default_value': 0,
                'direction': 'in',
                'documentation': {
                    'description': 'Offset in samples to start fetching data within each record. The offset can be positive or negative.'
                },
                'name': 'offset',
                'type': 'ViInt32'
            },
            {
                'default_value': 0,
                'direction': 'in',
                'documentation': {
                    'description': 'Zero-based index of the first record to fetch.'
                },
                'name': 'recordNumber',
                'type': 'ViInt32'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': 'Number of records to fetch. Use `None` to fetch all configured records.'
                },
                'name': 'numRecords',
                'type': 'ViInt32'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': 'Number of samples to fetch when performing a measurement. Use `None` to fetch the actual record length.'
                },
                'name': 'measNumSamples',
                'type': 'ViInt32'
            },
            {
                'default_value': 'hightime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a list of class instances with the following timing and scaling\ninformation about each waveform:\n\n-  **relativeInitialX**—the time (in seconds) from the trigger to the\n   first sample in the fetched waveform\n-  **absoluteInitialX**—timestamp (in seconds) of the first fetched\n   sample. This timestamp is comparable between records and\n   acquisitions; devices that do not support this parameter use 0 for\n   this output.\n-  **xIncrement**—the time between points in the acquired waveform in\n   seconds\n-  **channel**-channel name this waveform was acquired from\n-  **record**-record number of this waveform\n-  **gain**—the gain factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\n-  **offset**—the offset factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\n-  **samples**-floating point array of samples. Length will be of actual samples acquired.\n'
                },
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'python-code',
                    'value': None
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'returns': 'ViStatus'
    }
}

functions_additional_fetch_array_measurement_stats = {
    'FancyFetchMeasurementStats': {
        'codegen_method': 'python-only',
        'python_name': 'fetch_measurement_stats',
        'documentation': {
            'description': '\nObtains a waveform measurement and returns the measurement value. This\nfunction may return multiple statistical results depending on the number\nof channels, the acquisition type, and the number of records you\nspecify.\n\nYou specify a particular measurement type, such as rise time, frequency,\nor voltage peak-to-peak. The waveform on which the digitizer calculates\nthe waveform measurement is from an acquisition that you previously\ninitiated. The statistics for the specified measurement function are\nreturned, where the statistics are updated once every acquisition when\nthe specified measurement is fetched by any of the Fetch Measurement\nfunctions. If a Fetch Measurement function has not been called, this\nfunction fetches the data on which to perform the measurement. The\nstatistics are cleared by calling\nniScope_ClearWaveformMeasurementStats.\n\nMany of the measurements use the low, mid, and high reference levels.\nYou configure the low, mid, and high references with\nNISCOPE_ATTR_MEAS_CHAN_LOW_REF_LEVEL,\nNISCOPE_ATTR_MEAS_CHAN_MID_REF_LEVEL, and\nNISCOPE_ATTR_MEAS_CHAN_HIGH_REF_LEVEL to set each channel\ndifferently.\n'
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_fetch_measurement_stats'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe scalar measurement to be performed on each fetched waveform.\n'
                },
                'enum': 'ScalarMeasurement',
                'name': 'scalarMeasFunction',
                'type': 'ViInt32'
            },
            {
                'default_value': 'FetchRelativeTo.PRETRIGGER',
                'direction': 'in',
                'documentation': {
                    'description': 'Position to start fetching within one record.'
                },
                'enum': 'FetchRelativeTo',
                'name': 'relativeTo',
                'type': 'ViInt32'
            },
            {
                'default_value': 0,
                'direction': 'in',
                'documentation': {
                    'description': 'Offset in samples to start fetching data within each record. The offset can be positive or negative.'
                },
                'name': 'offset',
                'type': 'ViInt32'
            },
            {
                'default_value': 0,
                'direction': 'in',
                'documentation': {
                    'description': 'Zero-based index of the first record to fetch.'
                },
                'name': 'recordNumber',
                'type': 'ViInt32'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': 'Number of records to fetch. Use `None` to fetch all configured records.'
                },
                'name': 'numRecords',
                'type': 'ViInt32'
            },
            {
                'default_value': 'hightime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns a list of class instances with the following measurement statistics\nabout the specified measurement:\n\n-	**result** (float): the resulting measurement\n-	**mean** (float): the mean scalar value, which is obtained by\naveraging each fetch_measurement_stats call\n-	**stdev** (float): the standard deviations of the most recent\n**numInStats** measurements\n-	**min_val** (float): the smallest scalar value acquired (the minimum\nof the **numInStats** measurements)\n-	**max_val** (float): the largest scalar value acquired (the maximum\nof the **numInStats** measurements)\n-	**num_in_stats** (int): the number of times fetch_measurement_stats has been called\n-	**channel** (str): channel name this result was acquired from\n-	**record** (int): record number of this result'
                },
                'name': 'measurement_stats',
                'size': {
                    'mechanism': 'python-code',
                    'value': None
                },
                'type': 'MeasurementStats[]'
            }
        ],
        'returns': 'ViStatus'
    }
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/metadata/niscope.proto sha256=27e3ff3b9d54f38ee33d379864e5a0f94917850535bc0ed5d3e941d4888bf647 bytes=70217 -->
## FILE: src/niscope/metadata/niscope.proto

- repository: `ni/nimi-python`
- source_path: `src/niscope/metadata/niscope.proto`
- sha256: `27e3ff3b9d54f38ee33d379864e5a0f94917850535bc0ed5d3e941d4888bf647`
- bytes: 70217

````protobuf

//---------------------------------------------------------------------
// This file is generated from NI-SCOPE API metadata version 25.0.0f151
//---------------------------------------------------------------------
// Proto file for the NI-SCOPE Metadata
//---------------------------------------------------------------------
syntax = "proto3";

option java_multiple_files = true;
option java_package = "com.ni.grpc.scope";
option java_outer_classname = "NiScope";
option csharp_namespace = "NationalInstruments.Grpc.Scope";

package niscope_grpc;

import "nidevice.proto";
import "session.proto";

service NiScope {
  rpc Init(InitRequest) returns (InitResponse);
  rpc InitWithOptions(InitWithOptionsRequest) returns (InitWithOptionsResponse);
  rpc Close(CloseRequest) returns (CloseResponse);
  rpc AutoSetup(AutoSetupRequest) returns (AutoSetupResponse);
  rpc ConfigureVertical(ConfigureVerticalRequest) returns (ConfigureVerticalResponse);
  rpc ConfigureChanCharacteristics(ConfigureChanCharacteristicsRequest) returns (ConfigureChanCharacteristicsResponse);
  rpc ConfigureHorizontalTiming(ConfigureHorizontalTimingRequest) returns (ConfigureHorizontalTimingResponse);
  rpc ConfigureClock(ConfigureClockRequest) returns (ConfigureClockResponse);
  rpc ExportSignal(ExportSignalRequest) returns (ExportSignalResponse);
  rpc AdjustSampleClockRelativeDelay(AdjustSampleClockRelativeDelayRequest) returns (AdjustSampleClockRelativeDelayResponse);
  rpc ConfigureTriggerEdge(ConfigureTriggerEdgeRequest) returns (ConfigureTriggerEdgeResponse);
  rpc ConfigureTriggerGlitch(ConfigureTriggerGlitchRequest) returns (ConfigureTriggerGlitchResponse);
  rpc ConfigureTriggerHysteresis(ConfigureTriggerHysteresisRequest) returns (ConfigureTriggerHysteresisResponse);
  rpc ConfigureTriggerWindow(ConfigureTriggerWindowRequest) returns (ConfigureTriggerWindowResponse);
  rpc ConfigureTriggerSoftware(ConfigureTriggerSoftwareRequest) returns (ConfigureTriggerSoftwareResponse);
  rpc SendSoftwareTriggerEdge(SendSoftwareTriggerEdgeRequest) returns (SendSoftwareTriggerEdgeResponse);
  rpc ConfigureTriggerImmediate(ConfigureTriggerImmediateRequest) returns (ConfigureTriggerImmediateResponse);
  rpc ConfigureTriggerRunt(ConfigureTriggerRuntRequest) returns (ConfigureTriggerRuntResponse);
  rpc ConfigureTriggerDigital(ConfigureTriggerDigitalRequest) returns (ConfigureTriggerDigitalResponse);
  rpc ConfigureTriggerVideo(ConfigureTriggerVideoRequest) returns (ConfigureTriggerVideoResponse);
  rpc ConfigureTriggerWidth(ConfigureTriggerWidthRequest) returns (ConfigureTriggerWidthResponse);
  rpc ConfigureEqualizationFilterCoefficients(ConfigureEqualizationFilterCoefficientsRequest) returns (ConfigureEqualizationFilterCoefficientsResponse);
  rpc GetEqualizationFilterCoefficients(GetEqualizationFilterCoefficientsRequest) returns (GetEqualizationFilterCoefficientsResponse);
  rpc GetFrequencyResponse(GetFrequencyResponseRequest) returns (GetFrequencyResponseResponse);
  rpc ConfigureAcquisition(ConfigureAcquisitionRequest) returns (ConfigureAcquisitionResponse);
  rpc InitiateAcquisition(InitiateAcquisitionRequest) returns (InitiateAcquisitionResponse);
  rpc Abort(AbortRequest) returns (AbortResponse);
  rpc Commit(CommitRequest) returns (CommitResponse);
  rpc Read(ReadRequest) returns (ReadResponse);
  rpc Fetch(FetchRequest) returns (FetchResponse);
  rpc FetchBinary8(FetchBinary8Request) returns (FetchBinary8Response);
  rpc FetchBinary16(FetchBinary16Request) returns (FetchBinary16Response);
  rpc FetchBinary32(FetchBinary32Request) returns (FetchBinary32Response);
  rpc FetchComplex(FetchComplexRequest) returns (FetchComplexResponse);
  rpc FetchComplexBinary16(FetchComplexBinary16Request) returns (FetchComplexBinary16Response);
  rpc AcquisitionStatus(AcquisitionStatusRequest) returns (AcquisitionStatusResponse);
  rpc ActualNumWfms(ActualNumWfmsRequest) returns (ActualNumWfmsResponse);
  rpc ActualMeasWfmSize(ActualMeasWfmSizeRequest) returns (ActualMeasWfmSizeResponse);
  rpc ActualRecordLength(ActualRecordLengthRequest) returns (ActualRecordLengthResponse);
  rpc SampleRate(SampleRateRequest) returns (SampleRateResponse);
  rpc SampleMode(SampleModeRequest) returns (SampleModeResponse);
  rpc AddWaveformProcessing(AddWaveformProcessingRequest) returns (AddWaveformProcessingResponse);
  rpc ClearWaveformProcessing(ClearWaveformProcessingRequest) returns (ClearWaveformProcessingResponse);
  rpc ClearWaveformMeasurementStats(ClearWaveformMeasurementStatsRequest) returns (ClearWaveformMeasurementStatsResponse);
  rpc ReadMeasurement(ReadMeasurementRequest) returns (ReadMeasurementResponse);
  rpc FetchMeasurement(FetchMeasurementRequest) returns (FetchMeasurementResponse);
  rpc FetchMeasurementStats(FetchMeasurementStatsRequest) returns (FetchMeasurementStatsResponse);
  rpc FetchArrayMeasurement(FetchArrayMeasurementRequest) returns (FetchArrayMeasurementResponse);
  rpc Reset(ResetRequest) returns (ResetResponse);
  rpc SelfTest(SelfTestRequest) returns (SelfTestResponse);
  rpc Disable(DisableRequest) returns (DisableResponse);
  rpc ResetDevice(ResetDeviceRequest) returns (ResetDeviceResponse);
  rpc CalSelfCalibrate(CalSelfCalibrateRequest) returns (CalSelfCalibrateResponse);
  rpc RevisionQuery(RevisionQueryRequest) returns (RevisionQueryResponse);
  rpc ProbeCompensationSignalStart(ProbeCompensationSignalStartRequest) returns (ProbeCompensationSignalStartResponse);
  rpc ProbeCompensationSignalStop(ProbeCompensationSignalStopRequest) returns (ProbeCompensationSignalStopResponse);
  rpc CableSenseSignalStart(CableSenseSignalStartRequest) returns (CableSenseSignalStartResponse);
  rpc CableSenseSignalStop(CableSenseSignalStopRequest) returns (CableSenseSignalStopResponse);
  rpc GetChannelName(GetChannelNameRequest) returns (GetChannelNameResponse);
  rpc GetChannelNameFromString(GetChannelNameFromStringRequest) returns (GetChannelNameFromStringResponse);
  rpc ErrorHandler(ErrorHandlerRequest) returns (ErrorHandlerResponse);
  rpc GetError(GetErrorRequest) returns (GetErrorResponse);
  rpc GetErrorMessage(GetErrorMessageRequest) returns (GetErrorMessageResponse);
  rpc GetAttributeViInt32(GetAttributeViInt32Request) returns (GetAttributeViInt32Response);
  rpc SetAttributeViInt32(SetAttributeViInt32Request) returns (SetAttributeViInt32Response);
  rpc CheckAttributeViInt32(CheckAttributeViInt32Request) returns (CheckAttributeViInt32Response);
  rpc GetAttributeViInt64(GetAttributeViInt64Request) returns (GetAttributeViInt64Response);
  rpc SetAttributeViInt64(SetAttributeViInt64Request) returns (SetAttributeViInt64Response);
  rpc CheckAttributeViInt64(CheckAttributeViInt64Request) returns (CheckAttributeViInt64Response);
  rpc GetAttributeViReal64(GetAttributeViReal64Request) returns (GetAttributeViReal64Response);
  rpc SetAttributeViReal64(SetAttributeViReal64Request) returns (SetAttributeViReal64Response);
  rpc CheckAttributeViReal64(CheckAttributeViReal64Request) returns (CheckAttributeViReal64Response);
  rpc GetAttributeViString(GetAttributeViStringRequest) returns (GetAttributeViStringResponse);
  rpc SetAttributeViString(SetAttributeViStringRequest) returns (SetAttributeViStringResponse);
  rpc CheckAttributeViString(CheckAttributeViStringRequest) returns (CheckAttributeViStringResponse);
  rpc GetAttributeViSession(GetAttributeViSessionRequest) returns (GetAttributeViSessionResponse);
  rpc SetAttributeViSession(SetAttributeViSessionRequest) returns (SetAttributeViSessionResponse);
  rpc CheckAttributeViSession(CheckAttributeViSessionRequest) returns (CheckAttributeViSessionResponse);
  rpc GetAttributeViBoolean(GetAttributeViBooleanRequest) returns (GetAttributeViBooleanResponse);
  rpc SetAttributeViBoolean(SetAttributeViBooleanRequest) returns (SetAttributeViBooleanResponse);
  rpc CheckAttributeViBoolean(CheckAttributeViBooleanRequest) returns (CheckAttributeViBooleanResponse);
  rpc ImportAttributeConfigurationBuffer(ImportAttributeConfigurationBufferRequest) returns (ImportAttributeConfigurationBufferResponse);
  rpc ExportAttributeConfigurationBuffer(ExportAttributeConfigurationBufferRequest) returns (ExportAttributeConfigurationBufferResponse);
  rpc ImportAttributeConfigurationFile(ImportAttributeConfigurationFileRequest) returns (ImportAttributeConfigurationFileResponse);
  rpc ExportAttributeConfigurationFile(ExportAttributeConfigurationFileRequest) returns (ExportAttributeConfigurationFileResponse);
  rpc GetScalingCoefficients(GetScalingCoefficientsRequest) returns (GetScalingCoefficientsResponse);
  rpc GetNormalizationCoefficients(GetNormalizationCoefficientsRequest) returns (GetNormalizationCoefficientsResponse);
  rpc GetStreamEndpointHandle(GetStreamEndpointHandleRequest) returns (GetStreamEndpointHandleResponse);
  rpc CalFetchDate(CalFetchDateRequest) returns (CalFetchDateResponse);
  rpc CalFetchTemperature(CalFetchTemperatureRequest) returns (CalFetchTemperatureResponse);
}

enum NiScopeAttribute {
  NISCOPE_ATTRIBUTE_UNSPECIFIED = 0;
  NISCOPE_ATTRIBUTE_MEAS_HIGH_REF = 1250607;
  NISCOPE_ATTRIBUTE_MEAS_LOW_REF = 1250608;
  NISCOPE_ATTRIBUTE_CACHE = 1050004;
  NISCOPE_ATTRIBUTE_MEAS_MID_REF = 1250609;
  NISCOPE_ATTRIBUTE_RANGE_CHECK = 1050002;
  NISCOPE_ATTRIBUTE_QUERY_INSTRUMENT_STATUS = 1050003;
  NISCOPE_ATTRIBUTE_RECORD_COERCIONS = 1050006;
  NISCOPE_ATTRIBUTE_SIMULATE = 1050005;
  NISCOPE_ATTRIBUTE_INTERCHANGE_CHECK = 1050021;
  NISCOPE_ATTRIBUTE_CHANNEL_COUNT = 1050203;
  NISCOPE_ATTRIBUTE_SUPPORTED_INSTRUMENT_MODELS = 1050327;
  NISCOPE_ATTRIBUTE_GROUP_CAPABILITIES = 1050401;
  NISCOPE_ATTRIBUTE_SPECIFIC_DRIVER_DESCRIPTION = 1050514;
  NISCOPE_ATTRIBUTE_SPECIFIC_DRIVER_PREFIX = 1050302;
  NISCOPE_ATTRIBUTE_SPECIFIC_DRIVER_VENDOR = 1050513;
  NISCOPE_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION = 1050515;
  NISCOPE_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION = 1050516;
  NISCOPE_ATTRIBUTE_SPECIFIC_DRIVER_REVISION = 1050551;
  NISCOPE_ATTRIBUTE_INSTRUMENT_MANUFACTURER = 1050511;
  NISCOPE_ATTRIBUTE_INSTRUMENT_MODEL = 1050512;
  NISCOPE_ATTRIBUTE_INSTRUMENT_FIRMWARE_REVISION = 1050510;
  NISCOPE_ATTRIBUTE_IO_RESOURCE_DESCRIPTOR = 1050304;
  NISCOPE_ATTRIBUTE_LOGICAL_NAME = 1050305;
  NISCOPE_ATTRIBUTE_DRIVER_SETUP = 1050007;
  NISCOPE_ATTRIBUTE_ACQUISITION_TYPE = 1250101;
  NISCOPE_ATTRIBUTE_SAMPLE_MODE = 1250106;
  NISCOPE_ATTRIBUTE_CHANNEL_ENABLED = 1250005;
  NISCOPE_ATTRIBUTE_PROBE_ATTENUATION = 1250004;
  NISCOPE_ATTRIBUTE_VERTICAL_RANGE = 1250001;
  NISCOPE_ATTRIBUTE_VERTICAL_OFFSET = 1250002;
  NISCOPE_ATTRIBUTE_WIDTH_CONDITION = 1250504;
  NISCOPE_ATTRIBUTE_WIDTH_LOW_THRESHOLD = 1250501;
  NISCOPE_ATTRIBUTE_WIDTH_HIGH_THRESHOLD = 1250502;
  NISCOPE_ATTRIBUTE_WIDTH_POLARITY = 1250503;
  NISCOPE_ATTRIBUTE_VERTICAL_COUPLING = 1250003;
  NISCOPE_ATTRIBUTE_MAX_INPUT_FREQUENCY = 1250006;
  NISCOPE_ATTRIBUTE_INPUT_IMPEDANCE = 1250103;
  NISCOPE_ATTRIBUTE_HORZ_TIME_PER_RECORD = 1250007;
  NISCOPE_ATTRIBUTE_ACQUISITION_START_TIME = 1250109;
  NISCOPE_ATTRIBUTE_HORZ_MIN_NUM_PTS = 1250009;
  NISCOPE_ATTRIBUTE_HORZ_RECORD_LENGTH = 1250008;
  NISCOPE_ATTRIBUTE_HORZ_RECORD_REF_POSITION = 1250011;
  NISCOPE_ATTRIBUTE_HORZ_SAMPLE_RATE = 1250010;
  NISCOPE_ATTRIBUTE_TRIGGER_TYPE = 1250012;
  NISCOPE_ATTRIBUTE_TRIGGER_SOURCE = 1250013;
  NISCOPE_ATTRIBUTE_TRIGGER_LEVEL = 1250017;
  NISCOPE_ATTRIBUTE_TRIGGER_DELAY_TIME = 1250015;
  NISCOPE_ATTRIBUTE_TRIGGER_HOLDOFF = 1250016;
  NISCOPE_ATTRIBUTE_TRIGGER_COUPLING = 1250014;
  NISCOPE_ATTRIBUTE_TRIGGER_SLOPE = 1250018;
  NISCOPE_ATTRIBUTE_TV_TRIGGER_EVENT = 1250205;
  NISCOPE_ATTRIBUTE_TV_TRIGGER_LINE_NUMBER = 1250206;
  NISCOPE_ATTRIBUTE_TV_TRIGGER_SIGNAL_FORMAT = 1250201;
  NISCOPE_ATTRIBUTE_TV_TRIGGER_POLARITY = 1250204;
  NISCOPE_ATTRIBUTE_HORZ_NUM_RECORDS = 1150001;
  NISCOPE_ATTRIBUTE_INPUT_CLOCK_SOURCE = 1150002;
  NISCOPE_ATTRIBUTE_OUTPUT_CLOCK_SOURCE = 1150003;
  NISCOPE_ATTRIBUTE_HORZ_ENFORCE_REALTIME = 1150004;
  NISCOPE_ATTRIBUTE_BINARY_SAMPLE_WIDTH = 1150005;
  NISCOPE_ATTRIBUTE_CABLE_SENSE_VOLTAGE = 1150137;
  NISCOPE_ATTRIBUTE_CABLE_SENSE_MODE = 1150138;
  NISCOPE_ATTRIBUTE_CABLE_SENSE_SIGNAL_ENABLE = 1150139;
  NISCOPE_ATTRIBUTE_TRIGGER_HYSTERESIS = 1150006;
  NISCOPE_ATTRIBUTE_CLOCK_SYNC_PULSE_SOURCE = 1150007;
  NISCOPE_ATTRIBUTE_MASTER_ENABLE = 1150008;
  NISCOPE_ATTRIBUTE_MIN_SAMPLE_RATE = 1150009;
  NISCOPE_ATTRIBUTE_TRIGGER_WINDOW_MODE = 1150012;
  NISCOPE_ATTRIBUTE_TRIGGER_WINDOW_LOW_LEVEL = 1150013;
  NISCOPE_ATTRIBUTE_TRIGGER_WINDOW_HIGH_LEVEL = 1150014;
  NISCOPE_ATTRIBUTE_MEAS_REF_LEVEL_UNITS = 1150016;
  NISCOPE_ATTRIBUTE_MEAS_OTHER_CHANNEL = 1150018;
  NISCOPE_ATTRIBUTE_MEAS_HYSTERESIS_PERCENT = 1150019;
  NISCOPE_ATTRIBUTE_MEAS_LAST_ACQ_HISTOGRAM_SIZE = 1150020;
  NISCOPE_ATTRIBUTE_MEAS_VOLTAGE_HISTOGRAM_SIZE = 1150021;
  NISCOPE_ATTRIBUTE_MEAS_VOLTAGE_HISTOGRAM_LOW_VOLTS = 1150022;
  NISCOPE_ATTRIBUTE_MEAS_VOLTAGE_HISTOGRAM_HIGH_VOLTS = 1150023;
  NISCOPE_ATTRIBUTE_MEAS_TIME_HISTOGRAM_SIZE = 1150024;
  NISCOPE_ATTRIBUTE_MEAS_TIME_HISTOGRAM_LOW_VOLTS = 1150025;
  NISCOPE_ATTRIBUTE_MEAS_TIME_HISTOGRAM_HIGH_VOLTS = 1150026;
  NISCOPE_ATTRIBUTE_MEAS_TIME_HISTOGRAM_LOW_TIME = 1150027;
  NISCOPE_ATTRIBUTE_MEAS_TIME_HISTOGRAM_HIGH_TIME = 1150028;
  NISCOPE_ATTRIBUTE_MEAS_POLYNOMIAL_INTERPOLATION_ORDER = 1150029;
  NISCOPE_ATTRIBUTE_MEAS_INTERPOLATION_SAMPLING_FACTOR = 1150030;
  NISCOPE_ATTRIBUTE_MEAS_FILTER_CUTOFF_FREQ = 1150031;
  NISCOPE_ATTRIBUTE_MEAS_FILTER_CENTER_FREQ = 1150032;
  NISCOPE_ATTRIBUTE_MEAS_FILTER_RIPPLE = 1150033;
  NISCOPE_ATTRIBUTE_MEAS_FILTER_TRANSIENT_WAVEFORM_PERCENT = 1150034;
  NISCOPE_ATTRIBUTE_MEAS_FILTER_TYPE = 1150035;
  NISCOPE_ATTRIBUTE_MEAS_FILTER_ORDER = 1150036;
  NISCOPE_ATTRIBUTE_MEAS_FILTER_TAPS = 1150037;
  NISCOPE_ATTRIBUTE_MEAS_CHAN_LOW_REF_LEVEL = 1150038;
  NISCOPE_ATTRIBUTE_MEAS_CHAN_MID_REF_LEVEL = 1150039;
  NISCOPE_ATTRIBUTE_MEAS_CHAN_HIGH_REF_LEVEL = 1150040;
  NISCOPE_ATTRIBUTE_MEAS_FILTER_WIDTH = 1150041;
  NISCOPE_ATTRIBUTE_MEAS_FIR_FILTER_WINDOW = 1150042;
  NISCOPE_ATTRIBUTE_MEAS_ARRAY_GAIN = 1150043;
  NISCOPE_ATTRIBUTE_MEAS_ARRAY_OFFSET = 1150044;
  NISCOPE_ATTRIBUTE_MEAS_PERCENTAGE_METHOD = 1150045;
  NISCOPE_ATTRIBUTE_ACQ_ARM_SOURCE = 1150053;
  NISCOPE_ATTRIBUTE_IS_PROBE_COMP_ON = 1150066;
  NISCOPE_ATTRIBUTE_USE_SPEC_INITIAL_X = 1150067;
  NISCOPE_ATTRIBUTE_ALLOW_MORE_RECORDS_THAN_MEMORY = 1150068;
  NISCOPE_ATTRIBUTE_ONBOARD_MEMORY_SIZE = 1150069;
  NISCOPE_ATTRIBUTE_RIS_NUM_AVERAGES = 1150070;
  NISCOPE_ATTRIBUTE_RUNT_TIME_CONDITION = 1150132;
  NISCOPE_ATTRIBUTE_RUNT_TIME_LOW_LIMIT = 1150133;
  NISCOPE_ATTRIBUTE_RUNT_TIME_HIGH_LIMIT = 1150134;
  NISCOPE_ATTRIBUTE_RUNT_POLARITY = 1250303;
  NISCOPE_ATTRIBUTE_RUNT_LOW_THRESHOLD = 1250302;
  NISCOPE_ATTRIBUTE_RUNT_HIGH_THRESHOLD = 1250301;
  NISCOPE_ATTRIBUTE_RIS_METHOD = 1150071;
  NISCOPE_ATTRIBUTE_FETCH_INTERLEAVED_DATA = 1150072;
  NISCOPE_ATTRIBUTE_MAX_REAL_TIME_SAMPLING_RATE = 1150073;
  NISCOPE_ATTRIBUTE_MAX_RIS_RATE = 1150074;
  NISCOPE_ATTRIBUTE_TRIGGER_IMPEDANCE = 1150075;
  NISCOPE_ATTRIBUTE_DEVICE_NUMBER = 1150076;
  NISCOPE_ATTRIBUTE_FETCH_RELATIVE_TO = 1150077;
  NISCOPE_ATTRIBUTE_FETCH_OFFSET = 1150078;
  NISCOPE_ATTRIBUTE_FETCH_RECORD_NUMBER = 1150079;
  NISCOPE_ATTRIBUTE_FETCH_NUM_RECORDS = 1150080;
  NISCOPE_ATTRIBUTE_FETCH_MEAS_NUM_SAMPLES = 1150081;
  NISCOPE_ATTRIBUTE_POINTS_DONE = 1150082;
  NISCOPE_ATTRIBUTE_RECORDS_DONE = 1150083;
  NISCOPE_ATTRIBUTE_BACKLOG = 1150084;
  NISCOPE_ATTRIBUTE_POLL_INTERVAL = 1150100;
  NISCOPE_ATTRIBUTE_PLL_LOCK_STATUS = 1151303;
  NISCOPE_ATTRIBUTE_DEVICE_TEMPERATURE = 1150086;
  NISCOPE_ATTRIBUTE_SAMP_CLK_TIMEBASE_SRC = 1150087;
  NISCOPE_ATTRIBUTE_SAMP_CLK_TIMEBASE_RATE = 1150088;
  NISCOPE_ATTRIBUTE_SAMP_CLK_TIMEBASE_DIV = 1150089;
  NISCOPE_ATTRIBUTE_REF_CLK_RATE = 1150090;
  NISCOPE_ATTRIBUTE_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL = 1150091;
  NISCOPE_ATTRIBUTE_ENABLE_DC_RESTORE = 1150093;
  NISCOPE_ATTRIBUTE_ADV_TRIG_SRC = 1150094;
  NISCOPE_ATTRIBUTE_ARM_REF_TRIG_SRC = 1150095;
  NISCOPE_ATTRIBUTE_REF_TRIG_TDC_ENABLE = 1150096;
  NISCOPE_ATTRIBUTE_RESOLUTION = 1150102;
  NISCOPE_ATTRIBUTE_START_TO_REF_TRIGGER_HOLDOFF = 1150103;
  NISCOPE_ATTRIBUTE_SERIAL_NUMBER = 1150104;
  NISCOPE_ATTRIBUTE_OSCILLATOR_PHASE_DAC_VALUE = 1150105;
  NISCOPE_ATTRIBUTE_RIS_IN_AUTO_SETUP_ENABLE = 1150106;
  NISCOPE_ATTRIBUTE_CHANNEL_TERMINAL_CONFIGURATION = 1150107;
  NISCOPE_ATTRIBUTE_EXPORTED_ADVANCE_TRIGGER_OUTPUT_TERMINAL = 1150109;
  NISCOPE_ATTRIBUTE_READY_FOR_START_EVENT_OUTPUT_TERMINAL = 1150110;
  NISCOPE_ATTRIBUTE_READY_FOR_REF_EVENT_OUTPUT_TERMINAL = 1150111;
  NISCOPE_ATTRIBUTE_READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL = 1150112;
  NISCOPE_ATTRIBUTE_FLEX_FIR_ANTIALIAS_FILTER_TYPE = 1150271;
  NISCOPE_ATTRIBUTE_DDC_ENABLED = 1150300;
  NISCOPE_ATTRIBUTE_DDC_FREQUENCY_TRANSLATION_ENABLED = 1150302;
  NISCOPE_ATTRIBUTE_DDC_CENTER_FREQUENCY = 1150303;
  NISCOPE_ATTRIBUTE_DDC_DATA_PROCESSING_MODE = 1150304;
  NISCOPE_ATTRIBUTE_DDC_FREQUENCY_TRANSLATION_PHASE_I = 1150305;
  NISCOPE_ATTRIBUTE_DDC_FREQUENCY_TRANSLATION_PHASE_Q = 1150306;
  NISCOPE_ATTRIBUTE_DIGITAL_GAIN = 1150307;
  NISCOPE_ATTRIBUTE_DIGITAL_OFFSET = 1150308;
  NISCOPE_ATTRIBUTE_OVERFLOW_ERROR_REPORTING = 1150309;
  NISCOPE_ATTRIBUTE_DDC_Q_SOURCE = 1150310;
  NISCOPE_ATTRIBUTE_FETCH_INTERLEAVED_IQ_DATA = 1150311;
  NISCOPE_ATTRIBUTE_EQUALIZATION_NUM_COEFFICIENTS = 1150312;
  NISCOPE_ATTRIBUTE_EQUALIZATION_FILTER_ENABLED = 1150313;
  NISCOPE_ATTRIBUTE_REF_TRIGGER_DETECTOR_LOCATION = 1150314;
  NISCOPE_ATTRIBUTE_REF_TRIGGER_MINIMUM_QUIET_TIME = 1150315;
  NISCOPE_ATTRIBUTE_ENABLE_TIME_INTERLEAVED_SAMPLING = 1150128;
  NISCOPE_ATTRIBUTE_ENABLED_CHANNELS = 1150140;
  NISCOPE_ATTRIBUTE_DATA_TRANSFER_BLOCK_SIZE = 1150316;
  NISCOPE_ATTRIBUTE_TRIGGER_MODIFIER = 1250102;
  NISCOPE_ATTRIBUTE_TRIGGER_AUTO_TRIGGERED = 1150278;
  NISCOPE_ATTRIBUTE_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL = 1150097;
  NISCOPE_ATTRIBUTE_EXPORTED_REF_TRIGGER_OUTPUT_TERMINAL = 1150098;
  NISCOPE_ATTRIBUTE_END_OF_RECORD_EVENT_OUTPUT_TERMINAL = 1150099;
  NISCOPE_ATTRIBUTE_END_OF_ACQUISITION_EVENT_OUTPUT_TERMINAL = 1150101;
  NISCOPE_ATTRIBUTE_5V_OUT_OUTPUT_TERMINAL = 1150129;
  NISCOPE_ATTRIBUTE_BANDPASS_FILTER_ENABLED = 1150318;
  NISCOPE_ATTRIBUTE_DITHER_ENABLED = 1150319;
  NISCOPE_ATTRIBUTE_FRACTIONAL_RESAMPLE_ENABLED = 1150320;
  NISCOPE_ATTRIBUTE_GLITCH_CONDITION = 1250403;
  NISCOPE_ATTRIBUTE_GLITCH_WIDTH = 1250401;
  NISCOPE_ATTRIBUTE_GLITCH_POLARITY = 1250402;
  NISCOPE_ATTRIBUTE_DATA_TRANSFER_MAXIMUM_BANDWIDTH = 1150321;
  NISCOPE_ATTRIBUTE_DATA_TRANSFER_PREFERRED_PACKET_SIZE = 1150322;
  NISCOPE_ATTRIBUTE_SIGNAL_COND_GAIN = 1150279;
  NISCOPE_ATTRIBUTE_SIGNAL_COND_OFFSET = 1150280;
  NISCOPE_ATTRIBUTE_P2P_ENABLED = 1150338;
  NISCOPE_ATTRIBUTE_P2P_CHANNELS_TO_STREAM = 1150339;
  NISCOPE_ATTRIBUTE_P2P_ENDPOINT_SIZE = 1150342;
  NISCOPE_ATTRIBUTE_P2P_SAMPLES_AVAIL_IN_ENDPOINT = 1150328;
  NISCOPE_ATTRIBUTE_P2P_MOST_SAMPLES_AVAIL_IN_ENDPOINT = 1150341;
  NISCOPE_ATTRIBUTE_P2P_SAMPLES_TRANSFERRED = 1150340;
  NISCOPE_ATTRIBUTE_P2P_ENDPOINT_OVERFLOW = 1150344;
  NISCOPE_ATTRIBUTE_P2P_FIFO_ENDPOINT_COUNT = 1150345;
  NISCOPE_ATTRIBUTE_P2P_ONBOARD_MEMORY_ENABLED = 1150354;
  NISCOPE_ATTRIBUTE_P2P_MANUAL_CONFIGURATION_ENABLED = 1150343;
  NISCOPE_ATTRIBUTE_P2P_DATA_TRANS_PERMISSION_ADDR = 1150329;
  NISCOPE_ATTRIBUTE_P2P_DATA_TRANS_PERMISSION_ADDR_TYPE = 1150330;
  NISCOPE_ATTRIBUTE_P2P_DESTINATION_WINDOW_ADDR = 1150331;
  NISCOPE_ATTRIBUTE_P2P_DESTINATION_WINDOW_ADDR_TYPE = 1150332;
  NISCOPE_ATTRIBUTE_P2P_DESTINATION_WINDOW_SIZE = 1150333;
  NISCOPE_ATTRIBUTE_P2P_NOTIFY_PUSH_MESSAGE_ON = 1150334;
  NISCOPE_ATTRIBUTE_P2P_NOTIFY_MESSAGE_PUSH_ADDR = 1150335;
  NISCOPE_ATTRIBUTE_P2P_NOTIFY_MESSAGE_PUSH_ADDR_TYPE = 1150336;
  NISCOPE_ATTRIBUTE_P2P_NOTIFY_MESSAGE_PUSH_VALUE = 1150337;
  NISCOPE_ATTRIBUTE_SAMP_CLK_TIMEBASE_MULT = 1150367;
  NISCOPE_ATTRIBUTE_P2P_STREAM_RELATIVE_TO = 1150373;
  NISCOPE_ATTRIBUTE_P2P_SAMPLES_TRANSFERRED_PER_RECORD = 1150380;
  NISCOPE_ATTRIBUTE_END_OF_RECORD_TO_ADVANCE_TRIGGER_HOLDOFF = 1150366;
  NISCOPE_ATTRIBUTE_ABSOLUTE_SAMPLE_CLOCK_OFFSET = 1150374;
  NISCOPE_ATTRIBUTE_FPGA_BITFILE_PATH = 1150375;
  NISCOPE_ATTRIBUTE_INTERLEAVING_OFFSET_CORRECTION_ENABLED = 1150376;
  NISCOPE_ATTRIBUTE_HIGH_PASS_FILTER_FREQUENCY = 1150377;
  NISCOPE_ATTRIBUTE_END_OF_ACQUISITION_EVENT_TERMINAL_NAME = 1150141;
  NISCOPE_ATTRIBUTE_END_OF_RECORD_EVENT_TERMINAL_NAME = 1150142;
  NISCOPE_ATTRIBUTE_ADVANCE_TRIGGER_TERMINAL_NAME = 1150143;
  NISCOPE_ATTRIBUTE_REF_TRIGGER_TERMINAL_NAME = 1150144;
  NISCOPE_ATTRIBUTE_START_TRIGGER_TERMINAL_NAME = 1150145;
  NISCOPE_ATTRIBUTE_READY_FOR_ADVANCE_EVENT_TERMINAL_NAME = 1150146;
  NISCOPE_ATTRIBUTE_READY_FOR_REF_EVENT_TERMINAL_NAME = 1150147;
  NISCOPE_ATTRIBUTE_READY_FOR_START_EVENT_TERMINAL_NAME = 1150148;
}

enum WhichTrigger {
  WHICH_TRIGGER_NISCOPE_VAL_SOFTWARE_TRIGGER_START = 0;
  WHICH_TRIGGER_NISCOPE_VAL_SOFTWARE_TRIGGER_ARM_REFERENCE = 1;
  WHICH_TRIGGER_NISCOPE_VAL_SOFTWARE_TRIGGER_REFERENCE = 2;
  WHICH_TRIGGER_NISCOPE_VAL_SOFTWARE_TRIGGER_ADVANCE = 3;
}

enum VerticalCoupling {
  VERTICAL_COUPLING_NISCOPE_VAL_AC = 0;
  VERTICAL_COUPLING_NISCOPE_VAL_DC = 1;
  VERTICAL_COUPLING_NISCOPE_VAL_GND = 2;
}

enum TriggerCoupling {
  TRIGGER_COUPLING_NISCOPE_VAL_AC = 0;
  TRIGGER_COUPLING_NISCOPE_VAL_DC = 1;
  TRIGGER_COUPLING_NISCOPE_VAL_HF_REJECT = 3;
  TRIGGER_COUPLING_NISCOPE_VAL_LF_REJECT = 4;
  TRIGGER_COUPLING_NISCOPE_VAL_AC_PLUS_HF_REJECT = 1001;
}

enum TriggerSlope {
  TRIGGER_SLOPE_NISCOPE_VAL_NEGATIVE = 0;
  TRIGGER_SLOPE_NISCOPE_VAL_POSITIVE = 1;
  TRIGGER_SLOPE_NISCOPE_VAL_SLOPE_EITHER = 3;
}

enum VideoPolarity {
  VIDEO_POLARITY_UNSPECIFIED = 0;
  VIDEO_POLARITY_NISCOPE_VAL_TV_POSITIVE = 1;
  VIDEO_POLARITY_NISCOPE_VAL_TV_NEGATIVE = 2;
}

enum VideoTriggerEvent {
  VIDEO_TRIGGER_EVENT_UNSPECIFIED = 0;
  VIDEO_TRIGGER_EVENT_NISCOPE_VAL_TV_EVENT_FIELD1 = 1;
  VIDEO_TRIGGER_EVENT_NISCOPE_VAL_TV_EVENT_FIELD2 = 2;
  VIDEO_TRIGGER_EVENT_NISCOPE_VAL_TV_EVENT_ANY_FIELD = 3;
  VIDEO_TRIGGER_EVENT_NISCOPE_VAL_TV_EVENT_ANY_LINE = 4;
  VIDEO_TRIGGER_EVENT_NISCOPE_VAL_TV_EVENT_LINE_NUMBER = 5;
}

enum GlitchCondition {
  GLITCH_CONDITION_UNSPECIFIED = 0;
  GLITCH_CONDITION_NISCOPE_VAL_GLITCH_GREATER_THAN = 2;
  GLITCH_CONDITION_NISCOPE_VAL_GLITCH_LESS_THAN = 1;
}

enum GlitchPolarity {
  GLITCH_POLARITY_UNSPECIFIED = 0;
  GLITCH_POLARITY_NISCOPE_VAL_GLITCH_POSITIVE = 1;
  GLITCH_POLARITY_NISCOPE_VAL_GLITCH_NEGATIVE = 2;
  GLITCH_POLARITY_NISCOPE_VAL_GLITCH_EITHER = 3;
}

enum WidthCondition {
  WIDTH_CONDITION_UNSPECIFIED = 0;
  WIDTH_CONDITION_NISCOPE_VAL_WIDTH_WITHIN = 1;
  WIDTH_CONDITION_NISCOPE_VAL_WIDTH_OUTSIDE = 2;
}

enum WidthPolarity {
  WIDTH_POLARITY_UNSPECIFIED = 0;
  WIDTH_POLARITY_NISCOPE_VAL_WIDTH_POSITIVE = 1;
  WIDTH_POLARITY_NISCOPE_VAL_WIDTH_NEGATIVE = 2;
  WIDTH_POLARITY_NISCOPE_VAL_WIDTH_EITHER = 3;
}

enum RuntPolarity {
  RUNT_POLARITY_UNSPECIFIED = 0;
  RUNT_POLARITY_NISCOPE_VAL_RUNT_POSITIVE = 1;
  RUNT_POLARITY_NISCOPE_VAL_RUNT_NEGATIVE = 2;
  RUNT_POLARITY_NISCOPE_VAL_RUNT_EITHER = 3;
}

enum ClockingTerminalValues {
  CLOCKING_TERMINAL_VALUES_UNSPECIFIED = 0;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_NO_SOURCE = 1;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_RTSI_CLOCK = 2;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_EXTERNAL = 3;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_PFI_0 = 4;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_PFI_1 = 5;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_PFI_2 = 6;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_CLK_IN = 7;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_CLK_OUT = 8;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_INTERNAL10MHZ_OSC = 9;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_PXI_CLK = 10;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_PXI_CLK10 = 11;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_PXI_CLK100 = 12;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_PXIE_DSTAR_A = 13;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_AUX_0_CLK_IN = 14;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_AUX_0_CLK_OUT = 15;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_ONBOARD_CONFIGURABLE_RATE_CLK = 16;
}

enum ExportableSignals {
  EXPORTABLE_SIGNALS_UNSPECIFIED = 0;
  EXPORTABLE_SIGNALS_NISCOPE_VAL_REF_TRIGGER = 1;
  EXPORTABLE_SIGNALS_NISCOPE_VAL_START_TRIGGER = 2;
  EXPORTABLE_SIGNALS_NISCOPE_VAL_END_OF_ACQUISITION_EVENT = 3;
  EXPORTABLE_SIGNALS_NISCOPE_VAL_END_OF_RECORD_EVENT = 4;
  EXPORTABLE_SIGNALS_NISCOPE_VAL_ADVANCE_TRIGGER = 5;
  EXPORTABLE_SIGNALS_NISCOPE_VAL_READY_FOR_ADVANCE_EVENT = 6;
  EXPORTABLE_SIGNALS_NISCOPE_VAL_READY_FOR_START_EVENT = 7;
  EXPORTABLE_SIGNALS_NISCOPE_VAL_READY_FOR_REF_EVENT = 10;
  EXPORTABLE_SIGNALS_NISCOPE_VAL_5V_OUT = 13;
  EXPORTABLE_SIGNALS_NISCOPE_VAL_REF_CLOCK = 100;
  EXPORTABLE_SIGNALS_NISCOPE_VAL_SAMPLE_CLOCK = 101;
}

enum TriggerWindowMode {
  TRIGGER_WINDOW_MODE_NISCOPE_VAL_ENTERING_WINDOW = 0;
  TRIGGER_WINDOW_MODE_NISCOPE_VAL_LEAVING_WINDOW = 1;
  TRIGGER_WINDOW_MODE_NISCOPE_VAL_ENTERING_OR_LEAVING_WINDOW = 2;
}

enum AcquisitionStatus {
  ACQUISITION_STATUS_NISCOPE_VAL_ACQ_IN_PROGRESS = 0;
  ACQUISITION_STATUS_NISCOPE_VAL_ACQ_COMPLETE = 1;
  ACQUISITION_STATUS_NISCOPE_VAL_ACQ_STATUS_UNKNOWN = -1;
}

enum ScalarMeasurement {
  SCALAR_MEASUREMENT_NISCOPE_VAL_RISE_TIME = 0;
  SCALAR_MEASUREMENT_NISCOPE_VAL_NO_MEASUREMENT = 4000;
  SCALAR_MEASUREMENT_NISCOPE_VAL_FALL_TIME = 1;
  SCALAR_MEASUREMENT_NISCOPE_VAL_FREQUENCY = 2;
  SCALAR_MEASUREMENT_NISCOPE_VAL_PERIOD = 3;
  SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_RMS = 4;
  SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_PEAK_TO_PEAK = 5;
  SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_MAX = 6;
  SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_MIN = 7;
  SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HIGH = 8;
  SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_LOW = 9;
  SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_AVERAGE = 10;
  SCALAR_MEASUREMENT_NISCOPE_VAL_WIDTH_NEG = 11;
  SCALAR_MEASUREMENT_NISCOPE_VAL_WIDTH_POS = 12;
  SCALAR_MEASUREMENT_NISCOPE_VAL_DUTY_CYCLE_NEG = 13;
  SCALAR_MEASUREMENT_NISCOPE_VAL_DUTY_CYCLE_POS = 14;
  SCALAR_MEASUREMENT_NISCOPE_VAL_AMPLITUDE = 15;
  SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_CYCLE_RMS = 16;
  SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_CYCLE_AVERAGE = 17;
  SCALAR_MEASUREMENT_NISCOPE_VAL_OVERSHOOT = 18;
  SCALAR_MEASUREMENT_NISCOPE_VAL_PRESHOOT = 19;
  SCALAR_MEASUREMENT_NISCOPE_VAL_LOW_REF_VOLTS = 1000;
  SCALAR_MEASUREMENT_NISCOPE_VAL_MID_REF_VOLTS = 1001;
  SCALAR_MEASUREMENT_NISCOPE_VAL_HIGH_REF_VOLTS = 1002;
  SCALAR_MEASUREMENT_NISCOPE_VAL_AREA = 1003;
  SCALAR_MEASUREMENT_NISCOPE_VAL_CYCLE_AREA = 1004;
  SCALAR_MEASUREMENT_NISCOPE_VAL_INTEGRAL = 1005;
  SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_BASE = 1006;
  SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_TOP = 1007;
  SCALAR_MEASUREMENT_NISCOPE_VAL_FFT_FREQUENCY = 1008;
  SCALAR_MEASUREMENT_NISCOPE_VAL_FFT_AMPLITUDE = 1009;
  SCALAR_MEASUREMENT_NISCOPE_VAL_RISE_SLEW_RATE = 1010;
  SCALAR_MEASUREMENT_NISCOPE_VAL_FALL_SLEW_RATE = 1011;
  SCALAR_MEASUREMENT_NISCOPE_VAL_AC_ESTIMATE = 1012;
  SCALAR_MEASUREMENT_NISCOPE_VAL_DC_ESTIMATE = 1013;
  SCALAR_MEASUREMENT_NISCOPE_VAL_TIME_DELAY = 1014;
  SCALAR_MEASUREMENT_NISCOPE_VAL_AVERAGE_PERIOD = 1015;
  SCALAR_MEASUREMENT_NISCOPE_VAL_AVERAGE_FREQUENCY = 1016;
  SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_BASE_TO_TOP = 1017;
  SCALAR_MEASUREMENT_NISCOPE_VAL_PHASE_DELAY = 1018;
}

enum ArrayMeasurement {
  ARRAY_MEASUREMENT_UNSPECIFIED = 0;
  ARRAY_MEASUREMENT_NISCOPE_VAL_NO_MEASUREMENT = 4000;
  ARRAY_MEASUREMENT_NISCOPE_VAL_LAST_ACQ_HISTOGRAM = 4001;
  ARRAY_MEASUREMENT_NISCOPE_VAL_FFT_PHASE_SPECTRUM = 4002;
  ARRAY_MEASUREMENT_NISCOPE_VAL_FFT_AMP_SPECTRUM_VOLTS_RMS = 4003;
  ARRAY_MEASUREMENT_NISCOPE_VAL_MULTI_ACQ_VOLTAGE_HISTOGRAM = 4004;
  ARRAY_MEASUREMENT_NISCOPE_VAL_MULTI_ACQ_TIME_HISTOGRAM = 4005;
  ARRAY_MEASUREMENT_NISCOPE_VAL_ARRAY_INTEGRAL = 4006;
  ARRAY_MEASUREMENT_NISCOPE_VAL_DERIVATIVE = 4007;
  ARRAY_MEASUREMENT_NISCOPE_VAL_INVERSE = 4008;
  ARRAY_MEASUREMENT_NISCOPE_VAL_HANNING_WINDOW = 4009;
  ARRAY_MEASUREMENT_NISCOPE_VAL_FLAT_TOP_WINDOW = 4010;
  ARRAY_MEASUREMENT_NISCOPE_VAL_POLYNOMIAL_INTERPOLATION = 4011;
  ARRAY_MEASUREMENT_NISCOPE_VAL_MULTIPLY_CHANNELS = 4012;
  ARRAY_MEASUREMENT_NISCOPE_VAL_ADD_CHANNELS = 4013;
  ARRAY_MEASUREMENT_NISCOPE_VAL_SUBTRACT_CHANNELS = 4014;
  ARRAY_MEASUREMENT_NISCOPE_VAL_DIVIDE_CHANNELS = 4015;
  ARRAY_MEASUREMENT_NISCOPE_VAL_MULTI_ACQ_AVERAGE = 4016;
  ARRAY_MEASUREMENT_NISCOPE_VAL_BUTTERWORTH_FILTER = 4017;
  ARRAY_MEASUREMENT_NISCOPE_VAL_CHEBYSHEV_FILTER = 4018;
  ARRAY_MEASUREMENT_NISCOPE_VAL_FFT_AMP_SPECTRUM_DB = 4019;
  ARRAY_MEASUREMENT_NISCOPE_VAL_HAMMING_WINDOW = 4020;
  ARRAY_MEASUREMENT_NISCOPE_VAL_WINDOWED_FIR_FILTER = 4021;
  ARRAY_MEASUREMENT_NISCOPE_VAL_BESSEL_FILTER = 4022;
  ARRAY_MEASUREMENT_NISCOPE_VAL_TRIANGLE_WINDOW = 4023;
  ARRAY_MEASUREMENT_NISCOPE_VAL_BLACKMAN_WINDOW = 4024;
  ARRAY_MEASUREMENT_NISCOPE_VAL_ARRAY_OFFSET = 4025;
  ARRAY_MEASUREMENT_NISCOPE_VAL_ARRAY_GAIN = 4026;
}

enum CalibrationTypes {
  CALIBRATION_TYPES_NISCOPE_VAL_CAL_EXTERNAL = 0;
  CALIBRATION_TYPES_NISCOPE_VAL_CAL_SELF = 1;
  CALIBRATION_TYPES_NISCOPE_VAL_CAL_MANUFACTURE = 2;
}

enum ClearableMeasurement {
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_RISE_TIME = 0;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_ALL_MEASUREMENTS = 10000;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_MULTI_ACQ_VOLTAGE_HISTOGRAM = 4004;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_MULTI_ACQ_TIME_HISTOGRAM = 4005;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_MULTI_ACQ_AVERAGE = 4016;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_FREQUENCY = 2;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_AVERAGE_FREQUENCY = 1016;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_FFT_FREQUENCY = 1008;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_PERIOD = 3;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_AVERAGE_PERIOD = 1015;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_FALL_TIME = 1;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_RISE_SLEW_RATE = 1010;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_FALL_SLEW_RATE = 1011;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_OVERSHOOT = 18;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_PRESHOOT = 19;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_RMS = 4;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_CYCLE_RMS = 16;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_AC_ESTIMATE = 1012;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_FFT_AMPLITUDE = 1009;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_AVERAGE = 10;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_CYCLE_AVERAGE = 17;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_DC_ESTIMATE = 1013;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_MAX = 6;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_MIN = 7;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_PEAK_TO_PEAK = 5;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HIGH = 8;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_LOW = 9;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_AMPLITUDE = 15;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_TOP = 1007;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_BASE = 1006;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_BASE_TO_TOP = 1017;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_WIDTH_NEG = 11;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_WIDTH_POS = 12;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_DUTY_CYCLE_NEG = 13;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_DUTY_CYCLE_POS = 14;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_INTEGRAL = 1005;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_AREA = 1003;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_CYCLE_AREA = 1004;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_DELAY = 1014;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_PHASE_DELAY = 1018;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_LOW_REF_VOLTS = 1000;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_MID_REF_VOLTS = 1001;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_HIGH_REF_VOLTS = 1002;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN = 2000;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_STDEV = 2001;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEDIAN = 2003;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_MODE = 2010;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_MAX = 2005;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_MIN = 2006;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_PEAK_TO_PEAK = 2002;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_STDEV = 2007;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_2_STDEV = 2008;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_3_STDEV = 2009;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_HITS = 2004;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_NEW_HITS = 2011;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_MEAN = 3000;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_STDEV = 3001;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_MEDIAN = 3003;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_MODE = 3010;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_MAX = 3005;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_MIN = 3006;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_PEAK_TO_PEAK = 3002;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_STDEV = 3007;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_2_STDEV = 3008;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_3_STDEV = 3009;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_HITS = 3004;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_NEW_HITS = 3011;
}

enum Option {
  OPTION_NISCOPE_VAL_SELF_CALIBRATE_ALL_CHANNELS = 0;
  OPTION_NISCOPE_VAL_RESTORE_EXTERNAL_CALIBRATION = 1;
}

enum VideoSignalFormat {
  VIDEO_SIGNAL_FORMAT_UNSPECIFIED = 0;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_NTSC = 1;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_PAL = 2;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_SECAM = 3;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_M_PAL = 1001;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_480I_59_94_FIELDS_PER_SECOND = 1010;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_480I_60_FIELDS_PER_SECOND = 1011;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_480P_59_94_FRAMES_PER_SECOND = 1015;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_480P_60_FRAMES_PER_SECOND = 1016;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_576I_50_FIELDS_PER_SECOND = 1020;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_576P_50_FRAMES_PER_SECOND = 1025;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_720P_50_FRAMES_PER_SECOND = 1031;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_720P_59_94_FRAMES_PER_SECOND = 1032;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_720P_60_FRAMES_PER_SECOND = 1033;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_1080I_50_FIELDS_PER_SECOND = 1040;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_1080I_59_94_FIELDS_PER_SECOND = 1041;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_1080I_60_FIELDS_PER_SECOND = 1042;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_1080P_24_FRAMES_PER_SECOND = 1045;
}

enum NiScopeInt32AttributeValues {
  option allow_alias = true;
  NISCOPE_INT32_UNSPECIFIED = 0;
  NISCOPE_INT32_ACQUISITION_TYPE_VAL_NORMAL = 0;
  NISCOPE_INT32_ACQUISITION_TYPE_VAL_FLEXRES = 1001;
  NISCOPE_INT32_ACQUISITION_TYPE_VAL_DDC = 1002;
  NISCOPE_INT32_ADDRESS_TYPE_VAL_ADDR_PHYSICAL = 0;
  NISCOPE_INT32_ADDRESS_TYPE_VAL_ADDR_VIRTUAL = 1;
  NISCOPE_INT32_DATA_PROCESSING_MODE_VAL_REAL = 0;
  NISCOPE_INT32_DATA_PROCESSING_MODE_VAL_COMPLEX = 1;
  NISCOPE_INT32_FIR_FILTER_WINDOW_VAL_NONE = 0;
  NISCOPE_INT32_FIR_FILTER_WINDOW_VAL_HANNING = 409;
  NISCOPE_INT32_FIR_FILTER_WINDOW_VAL_FLAT_TOP = 410;
  NISCOPE_INT32_FIR_FILTER_WINDOW_VAL_HAMMING = 420;
  NISCOPE_INT32_FIR_FILTER_WINDOW_VAL_TRIANGLE = 423;
  NISCOPE_INT32_FIR_FILTER_WINDOW_VAL_BLACKMAN = 424;
  NISCOPE_INT32_FETCH_RELATIVE_TO_VAL_READ_POINTER = 388;
  NISCOPE_INT32_FETCH_RELATIVE_TO_VAL_PRETRIGGER = 477;
  NISCOPE_INT32_FETCH_RELATIVE_TO_VAL_NOW = 481;
  NISCOPE_INT32_FETCH_RELATIVE_TO_VAL_START = 482;
  NISCOPE_INT32_FETCH_RELATIVE_TO_VAL_TRIGGER = 483;
  NISCOPE_INT32_FLEX_FIR_ANTIALIAS_FILTER_TYPE_VAL_48_TAP_STANDARD = 0;
  NISCOPE_INT32_FLEX_FIR_ANTIALIAS_FILTER_TYPE_VAL_48_TAP_HANNING = 1;
  NISCOPE_INT32_FLEX_FIR_ANTIALIAS_FILTER_TYPE_VAL_16_TAP_HANNING = 2;
  NISCOPE_INT32_FLEX_FIR_ANTIALIAS_FILTER_TYPE_VAL_8_TAP_HANNING = 3;
  NISCOPE_INT32_GLITCH_CONDITION_VAL_GLITCH_GREATER_THAN = 2;
  NISCOPE_INT32_GLITCH_CONDITION_VAL_GLITCH_LESS_THAN = 1;
  NISCOPE_INT32_GLITCH_POLARITY_VAL_GLITCH_POSITIVE = 1;
  NISCOPE_INT32_GLITCH_POLARITY_VAL_GLITCH_NEGATIVE = 2;
  NISCOPE_INT32_GLITCH_POLARITY_VAL_GLITCH_EITHER = 3;
  NISCOPE_INT32_MEAS_FILTER_TYPE_VAL_MEAS_LOWPASS = 0;
  NISCOPE_INT32_MEAS_FILTER_TYPE_VAL_MEAS_HIGHPASS = 1;
  NISCOPE_INT32_MEAS_FILTER_TYPE_VAL_MEAS_BANDPASS = 2;
  NISCOPE_INT32_MEAS_FILTER_TYPE_VAL_MEAS_BANDSTOP = 3;
  NISCOPE_INT32_MEAS_PERCENTAGE_METHOD_VAL_MEAS_LOW_HIGH = 0;
  NISCOPE_INT32_MEAS_PERCENTAGE_METHOD_VAL_MEAS_MIN_MAX = 1;
  NISCOPE_INT32_MEAS_PERCENTAGE_METHOD_VAL_MEAS_BASE_TOP = 2;
  NISCOPE_INT32_MEAS_REF_LEVEL_UNITS_VAL_MEAS_VOLTAGE = 0;
  NISCOPE_INT32_MEAS_REF_LEVEL_UNITS_VAL_MEAS_PERCENTAGE = 1;
  NISCOPE_INT32_NOTIFICATION_TYPE_VAL_NOTIFY_NEVER = 0;
  NISCOPE_INT32_NOTIFICATION_TYPE_VAL_NOTIFY_DONE = 1;
  NISCOPE_INT32_OVERFLOW_ERROR_REPORTING_VAL_ERROR_REPORTING_ERROR = 0;
  NISCOPE_INT32_OVERFLOW_ERROR_REPORTING_VAL_ERROR_REPORTING_WARNING = 1;
  NISCOPE_INT32_OVERFLOW_ERROR_REPORTING_VAL_ERROR_REPORTING_DISABLED = 2;
  NISCOPE_INT32_P2_P_STREAM_RELATIVE_TO_VAL_STREAM_RELATIVE_TO_START_TRIGGER = 0;
  NISCOPE_INT32_P2_P_STREAM_RELATIVE_TO_VAL_STREAM_RELATIVE_TO_REFERENCE_TRIGGER = 1;
  NISCOPE_INT32_P2_P_STREAM_RELATIVE_TO_VAL_STREAM_RELATIVE_TO_SYNC_TRIGGER = 2;
  NISCOPE_INT32_RIS_METHOD_VAL_RIS_EXACT_NUM_AVERAGES = 1;
  NISCOPE_INT32_RIS_METHOD_VAL_RIS_MIN_NUM_AVERAGES = 2;
  NISCOPE_INT32_RIS_METHOD_VAL_RIS_INCOMPLETE = 3;
  NISCOPE_INT32_RIS_METHOD_VAL_RIS_LIMITED_BIN_WIDTH = 5;
  NISCOPE_INT32_REF_TRIGGER_DETECTOR_LOCATION_VAL_ANALOG_DETECTION_CIRCUIT = 0;
  NISCOPE_INT32_REF_TRIGGER_DETECTOR_LOCATION_VAL_DDC_OUTPUT = 1;
  NISCOPE_INT32_RUNT_POLARITY_VAL_RUNT_POSITIVE = 1;
  NISCOPE_INT32_RUNT_POLARITY_VAL_RUNT_NEGATIVE = 2;
  NISCOPE_INT32_RUNT_POLARITY_VAL_RUNT_EITHER = 3;
  NISCOPE_INT32_RUNT_TIME_CONDITION_VAL_RUNT_TIME_CONDITION_NONE = 0;
  NISCOPE_INT32_RUNT_TIME_CONDITION_VAL_RUNT_TIME_CONDITION_WITHIN = 1;
  NISCOPE_INT32_RUNT_TIME_CONDITION_VAL_RUNT_TIME_CONDITION_OUTSIDE = 2;
  NISCOPE_INT32_SAMPLE_MODE_VAL_REAL_TIME = 0;
  NISCOPE_INT32_SAMPLE_MODE_VAL_EQUIVALENT_TIME = 1;
  NISCOPE_INT32_TERMINAL_CONFIGURATION_VAL_SINGLE_ENDED = 0;
  NISCOPE_INT32_TERMINAL_CONFIGURATION_VAL_UNBALANCED_DIFFERENTIAL = 1;
  NISCOPE_INT32_TERMINAL_CONFIGURATION_VAL_DIFFERENTIAL = 2;
  NISCOPE_INT32_TRIGGER_COUPLING_VAL_AC = 0;
  NISCOPE_INT32_TRIGGER_COUPLING_VAL_DC = 1;
  NISCOPE_INT32_TRIGGER_COUPLING_VAL_HF_REJECT = 3;
  NISCOPE_INT32_TRIGGER_COUPLING_VAL_LF_REJECT = 4;
  NISCOPE_INT32_TRIGGER_COUPLING_VAL_AC_PLUS_HF_REJECT = 1001;
  NISCOPE_INT32_TRIGGER_MODIFIER_VAL_NO_TRIGGER_MOD = 1;
  NISCOPE_INT32_TRIGGER_MODIFIER_VAL_AUTO = 2;
  NISCOPE_INT32_TRIGGER_MODIFIER_VAL_AUTO_LEVEL = 3;
  NISCOPE_INT32_TRIGGER_SLOPE_VAL_NEGATIVE = 0;
  NISCOPE_INT32_TRIGGER_SLOPE_VAL_POSITIVE = 1;
  NISCOPE_INT32_TRIGGER_SLOPE_VAL_SLOPE_EITHER = 3;
  NISCOPE_INT32_TRIGGER_TYPE_VAL_EDGE_TRIGGER = 1;
  NISCOPE_INT32_TRIGGER_TYPE_VAL_HYSTERESIS_TRIGGER = 1001;
  NISCOPE_INT32_TRIGGER_TYPE_VAL_DIGITAL_TRIGGER = 1002;
  NISCOPE_INT32_TRIGGER_TYPE_VAL_WINDOW_TRIGGER = 1003;
  NISCOPE_INT32_TRIGGER_TYPE_VAL_SOFTWARE_TRIGGER = 1004;
  NISCOPE_INT32_TRIGGER_TYPE_VAL_TV_TRIGGER = 5;
  NISCOPE_INT32_TRIGGER_TYPE_VAL_GLITCH_TRIGGER = 4;
  NISCOPE_INT32_TRIGGER_TYPE_VAL_WIDTH_TRIGGER = 2;
  NISCOPE_INT32_TRIGGER_TYPE_VAL_RUNT_TRIGGER = 3;
  NISCOPE_INT32_TRIGGER_TYPE_VAL_IMMEDIATE_TRIGGER = 6;
  NISCOPE_INT32_TRIGGER_WINDOW_MODE_VAL_ENTERING_WINDOW = 0;
  NISCOPE_INT32_TRIGGER_WINDOW_MODE_VAL_LEAVING_WINDOW = 1;
  NISCOPE_INT32_TRIGGER_WINDOW_MODE_VAL_ENTERING_OR_LEAVING_WINDOW = 2;
  NISCOPE_INT32_VERTICAL_COUPLING_VAL_AC = 0;
  NISCOPE_INT32_VERTICAL_COUPLING_VAL_DC = 1;
  NISCOPE_INT32_VERTICAL_COUPLING_VAL_GND = 2;
  NISCOPE_INT32_VIDEO_POLARITY_VAL_TV_POSITIVE = 1;
  NISCOPE_INT32_VIDEO_POLARITY_VAL_TV_NEGATIVE = 2;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_NTSC = 1;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_PAL = 2;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_SECAM = 3;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_M_PAL = 1001;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_480I_59_94_FIELDS_PER_SECOND = 1010;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_480I_60_FIELDS_PER_SECOND = 1011;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_480P_59_94_FRAMES_PER_SECOND = 1015;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_480P_60_FRAMES_PER_SECOND = 1016;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_576I_50_FIELDS_PER_SECOND = 1020;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_576P_50_FRAMES_PER_SECOND = 1025;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_720P_50_FRAMES_PER_SECOND = 1031;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_720P_59_94_FRAMES_PER_SECOND = 1032;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_720P_60_FRAMES_PER_SECOND = 1033;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_1080I_50_FIELDS_PER_SECOND = 1040;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_1080I_59_94_FIELDS_PER_SECOND = 1041;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_1080I_60_FIELDS_PER_SECOND = 1042;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_1080P_24_FRAMES_PER_SECOND = 1045;
  NISCOPE_INT32_VIDEO_TRIGGER_EVENT_VAL_TV_EVENT_FIELD1 = 1;
  NISCOPE_INT32_VIDEO_TRIGGER_EVENT_VAL_TV_EVENT_FIELD2 = 2;
  NISCOPE_INT32_VIDEO_TRIGGER_EVENT_VAL_TV_EVENT_ANY_FIELD = 3;
  NISCOPE_INT32_VIDEO_TRIGGER_EVENT_VAL_TV_EVENT_ANY_LINE = 4;
  NISCOPE_INT32_VIDEO_TRIGGER_EVENT_VAL_TV_EVENT_LINE_NUMBER = 5;
  NISCOPE_INT32_WIDTH_CONDITION_VAL_WIDTH_WITHIN = 1;
  NISCOPE_INT32_WIDTH_CONDITION_VAL_WIDTH_OUTSIDE = 2;
  NISCOPE_INT32_WIDTH_POLARITY_VAL_WIDTH_POSITIVE = 1;
  NISCOPE_INT32_WIDTH_POLARITY_VAL_WIDTH_NEGATIVE = 2;
  NISCOPE_INT32_WIDTH_POLARITY_VAL_WIDTH_EITHER = 3;
}

enum NiScopeReal64AttributeValues {
  option allow_alias = true;
  NISCOPE_REAL64_UNSPECIFIED = 0;
  NISCOPE_REAL64_CABLE_SENSE_MODE_VAL_CABLE_SENSE_MODE_DISABLED = 0;
  NISCOPE_REAL64_CABLE_SENSE_MODE_VAL_CABLE_SENSE_MODE_ON_DEMAND = 1;
}

enum NiScopeReal64AttributeValuesMapped {
  NISCOPE_REAL64_MAPPED_UNSPECIFIED = 0;
  NISCOPE_REAL64_INPUT_IMPEDANCE_VAL_50_OHMS = 1;
  NISCOPE_REAL64_INPUT_IMPEDANCE_VAL_75_OHMS = 2;
  NISCOPE_REAL64_INPUT_IMPEDANCE_VAL_1_MEG_OHM = 3;
  NISCOPE_REAL64_MAX_INPUT_FREQUENCY_VAL_BANDWIDTH_DEVICE_DEFAULT = 4;
  NISCOPE_REAL64_MAX_INPUT_FREQUENCY_VAL_BANDWIDTH_FULL = 5;
  NISCOPE_REAL64_MAX_INPUT_FREQUENCY_VAL_20MHZ_BANDWIDTH = 6;
  NISCOPE_REAL64_MAX_INPUT_FREQUENCY_VAL_100MHZ_BANDWIDTH = 7;
  NISCOPE_REAL64_MAX_INPUT_FREQUENCY_VAL_20MHZ_MAX_INPUT_FREQUENCY = 8;
  NISCOPE_REAL64_MAX_INPUT_FREQUENCY_VAL_100MHZ_MAX_INPUT_FREQUENCY = 9;
}

enum NiScopeStringAttributeValuesMapped {
  NISCOPE_STRING_MAPPED_UNSPECIFIED = 0;
  NISCOPE_STRING_SAMP_CLK_TIMEPACE_SRC_VAL_CLK_IN = 1;
  NISCOPE_STRING_SAMP_CLK_TIMEPACE_SRC_VAL_NO_SOURCE = 2;
  NISCOPE_STRING_SAMP_CLK_TIMEPACE_SRC_VAL_PXI_STAR = 3;
  NISCOPE_STRING_SAMP_CLK_TIMEPACE_SRC_VAL_PXIE_DSTAR_A = 4;
  NISCOPE_STRING_SAMP_CLK_TIMEPACE_SRC_VAL_AUX_0_CLK_IN = 5;
  NISCOPE_STRING_SAMP_CLK_TIMEPACE_SRC_VAL_ONBOARD_CONFIGURABLE_RATE_CLK = 6;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_IMMEDIATE = 7;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_EXTERNAL = 8;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_SW_TRIG_FUNC = 9;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_TTL0 = 10;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_TTL1 = 11;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_TTL2 = 12;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_TTL3 = 13;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_TTL4 = 14;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_TTL5 = 15;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_TTL6 = 16;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_TTL7 = 17;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_ECL0 = 18;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_ECL1 = 19;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_PXI_STAR = 20;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_RTSI_0 = 21;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_RTSI_1 = 22;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_RTSI_2 = 23;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_RTSI_3 = 24;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_RTSI_4 = 25;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_RTSI_5 = 26;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_RTSI_6 = 27;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_RTSI_7 = 28;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_PFI_0 = 29;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_PFI_1 = 30;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_PFI_2 = 31;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_PFI_3 = 32;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_PFI_4 = 33;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_PFI_5 = 34;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_PFI_6 = 35;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_PFI_7 = 36;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_AUX_0_PFI_0 = 37;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_AUX_0_PFI_1 = 38;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_AUX_0_PFI_3 = 39;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_AUX_0_PFI_4 = 40;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_AUX_0_PFI_5 = 41;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_AUX_0_PFI_6 = 42;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_AUX_0_PFI_7 = 43;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_AUX_0_PFI_2 = 44;
}

message WaveformInfo {
  double absolute_initial_x = 1;
  double relative_initial_x = 2;
  double x_increment = 3;
  sint32 actual_samples = 4;
  double offset = 5;
  double gain = 6;
  double reserved1 = 7;
  double reserved2 = 8;
}

message CoefficientInfo {
  double offset = 1;
  double gain = 2;
  double reserved1 = 3;
  double reserved2 = 4;
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

message AutoSetupRequest {
  nidevice_grpc.Session vi = 1;
}

message AutoSetupResponse {
  int32 status = 1;
}

message ConfigureVerticalRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double range = 3;
  double offset = 4;
  oneof coupling_enum {
    VerticalCoupling coupling = 5;
    sint32 coupling_raw = 6;
  }
  double probe_attenuation = 7;
  bool enabled = 8;
}

message ConfigureVerticalResponse {
  int32 status = 1;
}

message ConfigureChanCharacteristicsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double input_impedance = 3;
  double max_input_frequency = 4;
}

message ConfigureChanCharacteristicsResponse {
  int32 status = 1;
}

message ConfigureHorizontalTimingRequest {
  nidevice_grpc.Session vi = 1;
  double min_sample_rate = 2;
  sint32 min_num_pts = 3;
  double ref_position = 4;
  sint32 num_records = 5;
  bool enforce_realtime = 6;
}

message ConfigureHorizontalTimingResponse {
  int32 status = 1;
}

message ConfigureClockRequest {
  nidevice_grpc.Session vi = 1;
  oneof input_clock_source_enum {
    string input_clock_source_raw = 2;
    ClockingTerminalValues input_clock_source_mapped = 6;
  }
  oneof output_clock_source_enum {
    string output_clock_source_raw = 3;
    ClockingTerminalValues output_clock_source_mapped = 7;
  }
  oneof clock_sync_pulse_source_enum {
    string clock_sync_pulse_source_raw = 4;
    ClockingTerminalValues clock_sync_pulse_source_mapped = 8;
  }
  bool master_enabled = 5;
}

message ConfigureClockResponse {
  int32 status = 1;
}

message ExportSignalRequest {
  nidevice_grpc.Session vi = 1;
  oneof signal_enum {
    ExportableSignals signal = 2;
    sint32 signal_raw = 3;
  }
  string signal_identifier = 4;
  oneof output_terminal_enum {
    ClockingTerminalValues output_terminal_mapped = 5;
    string output_terminal_raw = 6;
  }
}

message ExportSignalResponse {
  int32 status = 1;
}

message AdjustSampleClockRelativeDelayRequest {
  nidevice_grpc.Session vi = 1;
  double delay = 2;
}

message AdjustSampleClockRelativeDelayResponse {
  int32 status = 1;
}

message ConfigureTriggerEdgeRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_source = 2;
  double level = 3;
  oneof slope_enum {
    TriggerSlope slope = 4;
    sint32 slope_raw = 5;
  }
  oneof trigger_coupling_enum {
    TriggerCoupling trigger_coupling = 6;
    sint32 trigger_coupling_raw = 7;
  }
  double holdoff = 8;
  double delay = 9;
}

message ConfigureTriggerEdgeResponse {
  int32 status = 1;
}

message ConfigureTriggerGlitchRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_source = 2;
  double level = 3;
  double width = 4;
  oneof polarity_enum {
    GlitchPolarity polarity = 5;
    sint32 polarity_raw = 6;
  }
  oneof glitch_condition_enum {
    GlitchCondition glitch_condition = 7;
    sint32 glitch_condition_raw = 8;
  }
  oneof trigger_coupling_enum {
    TriggerCoupling trigger_coupling = 9;
    sint32 trigger_coupling_raw = 10;
  }
  double holdoff = 11;
  double delay = 12;
}

message ConfigureTriggerGlitchResponse {
  int32 status = 1;
}

message ConfigureTriggerHysteresisRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_source = 2;
  double level = 3;
  double hysteresis = 4;
  oneof slope_enum {
    TriggerSlope slope = 5;
    sint32 slope_raw = 6;
  }
  oneof trigger_coupling_enum {
    TriggerCoupling trigger_coupling = 7;
    sint32 trigger_coupling_raw = 8;
  }
  double holdoff = 9;
  double delay = 10;
}

message ConfigureTriggerHysteresisResponse {
  int32 status = 1;
}

message ConfigureTriggerWindowRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_source = 2;
  double low_level = 3;
  double high_level = 4;
  oneof window_mode_enum {
    TriggerWindowMode window_mode = 5;
    sint32 window_mode_raw = 6;
  }
  oneof trigger_coupling_enum {
    TriggerCoupling trigger_coupling = 7;
    sint32 trigger_coupling_raw = 8;
  }
  double holdoff = 9;
  double delay = 10;
}

message ConfigureTriggerWindowResponse {
  int32 status = 1;
}

message ConfigureTriggerSoftwareRequest {
  nidevice_grpc.Session vi = 1;
  double holdoff = 2;
  double delay = 3;
}

message ConfigureTriggerSoftwareResponse {
  int32 status = 1;
}

message SendSoftwareTriggerEdgeRequest {
  nidevice_grpc.Session vi = 1;
  oneof which_trigger_enum {
    WhichTrigger which_trigger = 2;
    sint32 which_trigger_raw = 3;
  }
}

message SendSoftwareTriggerEdgeResponse {
  int32 status = 1;
}

message ConfigureTriggerImmediateRequest {
  nidevice_grpc.Session vi = 1;
}

message ConfigureTriggerImmediateResponse {
  int32 status = 1;
}

message ConfigureTriggerRuntRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_source = 2;
  double low_threshold = 3;
  double high_threshold = 4;
  oneof polarity_enum {
    RuntPolarity polarity = 5;
    sint32 polarity_raw = 6;
  }
  oneof trigger_coupling_enum {
    TriggerCoupling trigger_coupling = 7;
    sint32 trigger_coupling_raw = 8;
  }
  double holdoff = 9;
  double delay = 10;
}

message ConfigureTriggerRuntResponse {
  int32 status = 1;
}

message ConfigureTriggerDigitalRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_source = 2;
  oneof slope_enum {
    TriggerSlope slope = 3;
    sint32 slope_raw = 4;
  }
  double holdoff = 5;
  double delay = 6;
}

message ConfigureTriggerDigitalResponse {
  int32 status = 1;
}

message ConfigureTriggerVideoRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_source = 2;
  bool enable_dc_restore = 3;
  oneof signal_format_enum {
    VideoSignalFormat signal_format = 4;
    sint32 signal_format_raw = 5;
  }
  oneof event_enum {
    VideoTriggerEvent event = 6;
    sint32 event_raw = 7;
  }
  sint32 line_number = 8;
  oneof polarity_enum {
    VideoPolarity polarity = 9;
    sint32 polarity_raw = 10;
  }
  oneof trigger_coupling_enum {
    TriggerCoupling trigger_coupling = 11;
    sint32 trigger_coupling_raw = 12;
  }
  double holdoff = 13;
  double delay = 14;
}

message ConfigureTriggerVideoResponse {
  int32 status = 1;
}

message ConfigureTriggerWidthRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_source = 2;
  double level = 3;
  double low_threshold = 4;
  double high_threshold = 5;
  oneof polarity_enum {
    WidthPolarity polarity = 6;
    sint32 polarity_raw = 7;
  }
  oneof condition_enum {
    WidthCondition condition = 8;
    sint32 condition_raw = 9;
  }
  oneof trigger_coupling_enum {
    TriggerCoupling trigger_coupling = 10;
    sint32 trigger_coupling_raw = 11;
  }
  double holdoff = 12;
  double delay = 13;
}

message ConfigureTriggerWidthResponse {
  int32 status = 1;
}

message ConfigureEqualizationFilterCoefficientsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  repeated double coefficients = 3;
}

message ConfigureEqualizationFilterCoefficientsResponse {
  int32 status = 1;
}

message GetEqualizationFilterCoefficientsRequest {
  nidevice_grpc.Session vi = 1;
  string channel = 2;
  sint32 number_of_coefficients = 3;
}

message GetEqualizationFilterCoefficientsResponse {
  int32 status = 1;
  repeated double coefficients = 2;
}

message GetFrequencyResponseRequest {
  nidevice_grpc.Session vi = 1;
  string channel = 2;
  sint32 buffer_size = 3;
}

message GetFrequencyResponseResponse {
  int32 status = 1;
  repeated double frequencies = 2;
  repeated double amplitudes = 3;
  repeated double phases = 4;
  sint32 number_of_frequencies = 5;
}

message ConfigureAcquisitionRequest {
  nidevice_grpc.Session vi = 1;
  sint32 acquisition_type = 2;
}

message ConfigureAcquisitionResponse {
  int32 status = 1;
}

message InitiateAcquisitionRequest {
  nidevice_grpc.Session vi = 1;
}

message InitiateAcquisitionResponse {
  int32 status = 1;
}

message AbortRequest {
  nidevice_grpc.Session vi = 1;
}

message AbortResponse {
  int32 status = 1;
}

message CommitRequest {
  nidevice_grpc.Session vi = 1;
}

message CommitResponse {
  int32 status = 1;
}

message ReadRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double timeout = 3;
  sint32 num_samples = 4;
}

message ReadResponse {
  int32 status = 1;
  repeated double waveform = 2;
  repeated WaveformInfo wfm_info = 3;
}

message FetchRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double timeout = 3;
  sint32 num_samples = 4;
}

message FetchResponse {
  int32 status = 1;
  repeated double waveform = 2;
  repeated WaveformInfo wfm_info = 3;
}

message FetchBinary8Request {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double timeout = 3;
  sint32 num_samples = 4;
}

message FetchBinary8Response {
  int32 status = 1;
  bytes waveform = 2;
  repeated WaveformInfo wfm_info = 3;
}

message FetchBinary16Request {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double timeout = 3;
  sint32 num_samples = 4;
}

message FetchBinary16Response {
  int32 status = 1;
  repeated sint32 waveform = 2;
  repeated WaveformInfo wfm_info = 3;
}

message FetchBinary32Request {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double timeout = 3;
  sint32 num_samples = 4;
}

message FetchBinary32Response {
  int32 status = 1;
  repeated sint32 waveform = 2;
  repeated WaveformInfo wfm_info = 3;
}

message FetchComplexRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double timeout = 3;
  sint32 num_samples = 4;
}

message FetchComplexResponse {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexNumber wfm = 2;
  repeated WaveformInfo wfm_info = 3;
}

message FetchComplexBinary16Request {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double timeout = 3;
  sint32 num_samples = 4;
}

message FetchComplexBinary16Response {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexI16 wfm = 2;
  repeated WaveformInfo wfm_info = 3;
}

message AcquisitionStatusRequest {
  nidevice_grpc.Session vi = 1;
}

message AcquisitionStatusResponse {
  int32 status = 1;
  AcquisitionStatus acquisition_status = 2;
  sint32 acquisition_status_raw = 3;
}

message ActualNumWfmsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
}

message ActualNumWfmsResponse {
  int32 status = 1;
  sint32 num_wfms = 2;
}

message ActualMeasWfmSizeRequest {
  nidevice_grpc.Session vi = 1;
  oneof array_meas_function_enum {
    ArrayMeasurement array_meas_function = 2;
    sint32 array_meas_function_raw = 3;
  }
}

message ActualMeasWfmSizeResponse {
  int32 status = 1;
  sint32 meas_waveform_size = 2;
}

message ActualRecordLengthRequest {
  nidevice_grpc.Session vi = 1;
}

message ActualRecordLengthResponse {
  int32 status = 1;
  sint32 record_length = 2;
}

message SampleRateRequest {
  nidevice_grpc.Session vi = 1;
}

message SampleRateResponse {
  int32 status = 1;
  double sample_rate = 2;
}

message SampleModeRequest {
  nidevice_grpc.Session vi = 1;
}

message SampleModeResponse {
  int32 status = 1;
  sint32 sample_mode = 2;
}

message AddWaveformProcessingRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  oneof meas_function_enum {
    ArrayMeasurement meas_function = 3;
    sint32 meas_function_raw = 4;
  }
}

message AddWaveformProcessingResponse {
  int32 status = 1;
}

message ClearWaveformProcessingRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
}

message ClearWaveformProcessingResponse {
  int32 status = 1;
}

message ClearWaveformMeasurementStatsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  oneof clearable_measurement_function_enum {
    ClearableMeasurement clearable_measurement_function = 3;
    sint32 clearable_measurement_function_raw = 4;
  }
}

message ClearWaveformMeasurementStatsResponse {
  int32 status = 1;
}

message ReadMeasurementRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double timeout = 3;
  oneof scalar_meas_function_enum {
    ScalarMeasurement scalar_meas_function = 4;
    sint32 scalar_meas_function_raw = 5;
  }
}

message ReadMeasurementResponse {
  int32 status = 1;
  repeated double result = 2;
}

message FetchMeasurementRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double timeout = 3;
  oneof scalar_meas_function_enum {
    ScalarMeasurement scalar_meas_function = 4;
    sint32 scalar_meas_function_raw = 5;
  }
}

message FetchMeasurementResponse {
  int32 status = 1;
  repeated double result = 2;
}

message FetchMeasurementStatsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double timeout = 3;
  oneof scalar_meas_function_enum {
    ScalarMeasurement scalar_meas_function = 4;
    sint32 scalar_meas_function_raw = 5;
  }
}

message FetchMeasurementStatsResponse {
  int32 status = 1;
  repeated double result = 2;
  repeated double mean = 3;
  repeated double stdev = 4;
  repeated double min = 5;
  repeated double max = 6;
  repeated sint32 num_in_stats = 7;
}

message FetchArrayMeasurementRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double timeout = 3;
  oneof array_meas_function_enum {
    ArrayMeasurement array_meas_function = 4;
    sint32 array_meas_function_raw = 5;
  }
  optional sint32 meas_wfm_size = 6;
}

message FetchArrayMeasurementResponse {
  int32 status = 1;
  repeated double meas_wfm = 2;
  repeated WaveformInfo wfm_info = 3;
}

message ResetRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetResponse {
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

message DisableRequest {
  nidevice_grpc.Session vi = 1;
}

message DisableResponse {
  int32 status = 1;
}

message ResetDeviceRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetDeviceResponse {
  int32 status = 1;
}

message CalSelfCalibrateRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  oneof option_enum {
    Option option = 3;
    sint32 option_raw = 4;
  }
}

message CalSelfCalibrateResponse {
  int32 status = 1;
}

message RevisionQueryRequest {
  nidevice_grpc.Session vi = 1;
}

message RevisionQueryResponse {
  int32 status = 1;
  string driver_revision = 2;
  string firmware_revision = 3;
}

message ProbeCompensationSignalStartRequest {
  nidevice_grpc.Session vi = 1;
}

message ProbeCompensationSignalStartResponse {
  int32 status = 1;
}

message ProbeCompensationSignalStopRequest {
  nidevice_grpc.Session vi = 1;
}

message ProbeCompensationSignalStopResponse {
  int32 status = 1;
}

message CableSenseSignalStartRequest {
  nidevice_grpc.Session vi = 1;
}

message CableSenseSignalStartResponse {
  int32 status = 1;
}

message CableSenseSignalStopRequest {
  nidevice_grpc.Session vi = 1;
}

message CableSenseSignalStopResponse {
  int32 status = 1;
}

message GetChannelNameRequest {
  nidevice_grpc.Session vi = 1;
  sint32 index = 2;
}

message GetChannelNameResponse {
  int32 status = 1;
  string channel_string = 2;
}

message GetChannelNameFromStringRequest {
  nidevice_grpc.Session vi = 1;
  string index = 2;
}

message GetChannelNameFromStringResponse {
  int32 status = 1;
  string name = 2;
}

message ErrorHandlerRequest {
  nidevice_grpc.Session vi = 1;
  sint32 error_code = 2;
  string error_source = 3;
}

message ErrorHandlerResponse {
  int32 status = 1;
  string error_description = 2;
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

message GetAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
}

message GetAttributeViInt32Response {
  int32 status = 1;
  sint32 value = 2;
}

message SetAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
  oneof value_enum {
    sint32 value_raw = 4;
    NiScopeInt32AttributeValues value = 5;
  }
}

message SetAttributeViInt32Response {
  int32 status = 1;
}

message CheckAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
  oneof value_enum {
    sint32 value_raw = 4;
    NiScopeInt32AttributeValues value = 5;
  }
}

message CheckAttributeViInt32Response {
  int32 status = 1;
}

message GetAttributeViInt64Request {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
}

message GetAttributeViInt64Response {
  int32 status = 1;
  int64 value = 2;
}

message SetAttributeViInt64Request {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
  int64 value_raw = 4;
}

message SetAttributeViInt64Response {
  int32 status = 1;
}

message CheckAttributeViInt64Request {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
  int64 value_raw = 4;
}

message CheckAttributeViInt64Response {
  int32 status = 1;
}

message GetAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
}

message GetAttributeViReal64Response {
  int32 status = 1;
  double value = 2;
}

message SetAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
  oneof value_enum {
    double value_raw = 4;
    NiScopeReal64AttributeValues value = 5;
    NiScopeReal64AttributeValuesMapped value_mapped = 6;
  }
}

message SetAttributeViReal64Response {
  int32 status = 1;
}

message CheckAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
  oneof value_enum {
    double value_raw = 4;
    NiScopeReal64AttributeValues value = 5;
    NiScopeReal64AttributeValuesMapped value_mapped = 6;
  }
}

message CheckAttributeViReal64Response {
  int32 status = 1;
}

message GetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
}

message GetAttributeViStringResponse {
  int32 status = 1;
  string value = 2;
}

message SetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
  oneof value_enum {
    NiScopeStringAttributeValuesMapped value_mapped = 4;
    string value_raw = 5;
  }
}

message SetAttributeViStringResponse {
  int32 status = 1;
}

message CheckAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
  oneof value_enum {
    NiScopeStringAttributeValuesMapped value_mapped = 4;
    string value_raw = 5;
  }
}

message CheckAttributeViStringResponse {
  int32 status = 1;
}

message GetAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
}

message GetAttributeViSessionResponse {
  int32 status = 1;
  nidevice_grpc.Session value = 2;
}

message SetAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
  nidevice_grpc.Session value = 4;
}

message SetAttributeViSessionResponse {
  int32 status = 1;
}

message CheckAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
  nidevice_grpc.Session value = 4;
}

message CheckAttributeViSessionResponse {
  int32 status = 1;
}

message GetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
}

message GetAttributeViBooleanResponse {
  int32 status = 1;
  bool value = 2;
}

message SetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
  bool value = 4;
}

message SetAttributeViBooleanResponse {
  int32 status = 1;
}

message CheckAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
  bool value = 4;
}

message CheckAttributeViBooleanResponse {
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

message GetScalingCoefficientsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
}

message GetScalingCoefficientsResponse {
  int32 status = 1;
  repeated CoefficientInfo coefficient_info = 2;
  sint32 number_of_coefficient_sets = 3;
}

message GetNormalizationCoefficientsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
}

message GetNormalizationCoefficientsResponse {
  int32 status = 1;
  repeated CoefficientInfo coefficient_info = 2;
  sint32 number_of_coefficient_sets = 3;
}

message GetStreamEndpointHandleRequest {
  nidevice_grpc.Session vi = 1;
  string stream_name = 2;
}

message GetStreamEndpointHandleResponse {
  int32 status = 1;
  uint32 writer_handle = 2;
}

message CalFetchDateRequest {
  nidevice_grpc.Session vi = 1;
  oneof which_one_enum {
    CalibrationTypes which_one = 2;
    sint32 which_one_raw = 3;
  }
}

message CalFetchDateResponse {
  int32 status = 1;
  sint32 year = 2;
  sint32 month = 3;
  sint32 day = 4;
}

message CalFetchTemperatureRequest {
  nidevice_grpc.Session vi = 1;
  oneof which_one_enum {
    CalibrationTypes which_one = 2;
    sint32 which_one_raw = 3;
  }
}

message CalFetchTemperatureResponse {
  int32 status = 1;
  double temperature = 2;
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/niscope.mak sha256=6bc8b2600c7df911813b1fdc1030a44e877e532dd3288e968f50663f72a871db bytes=429 -->
## FILE: src/niscope/niscope.mak

- repository: `ni/nimi-python`
- source_path: `src/niscope/niscope.mak`
- sha256: `6bc8b2600c7df911813b1fdc1030a44e877e532dd3288e968f50663f72a871db`
- bytes: 429

````makefile


include $(BUILD_HELPER_DIR)/defines.mak

MODULE_FILES_TO_GENERATE := $(DEFAULT_PY_FILES_TO_GENERATE)

MODULE_FILES_TO_COPY := $(DEFAULT_PY_FILES_TO_COPY)

RST_FILES_TO_GENERATE := $(DEFAULT_RST_FILES_TO_GENERATE)

SPHINX_CONF_PY := $(DEFAULT_SPHINX_CONF_PY)
READTHEDOCS_CONFIG := $(DEFAULT_READTHEDOCS_CONFIG)

CUSTOM_TYPES_TO_COPY += \
    waveform_info.py \
    measurement_stats.py \

include $(BUILD_HELPER_DIR)/rules.mak
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/system_tests/grpc_server_config.json sha256=4cd9aaace0e188d725e02f4f09ea2046d066246d5036c3ada3415b8aa3c5f59e bytes=156 -->
## FILE: src/niscope/system_tests/grpc_server_config.json

- repository: `ni/nimi-python`
- source_path: `src/niscope/system_tests/grpc_server_config.json`
- sha256: `4cd9aaace0e188d725e02f4f09ea2046d066246d5036c3ada3415b8aa3c5f59e`
- bytes: 156

````json
{
    "address": "[::1]",
    "port": 31764,
    "security" : {
       "server_cert": "",
       "server_key": "",
       "root_cert": ""
    }
 }
````
