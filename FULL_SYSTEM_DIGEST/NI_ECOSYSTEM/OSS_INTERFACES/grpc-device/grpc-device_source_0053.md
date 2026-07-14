# NI OSS SOURCE SNAPSHOT: grpc-device

<!--NI_OSS_SNAPSHOT repo=ni/grpc-device commit=13c1d30177e5da4b0c444b2ceab74506ca3847fb -->

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nixnet/enums.py sha256=da6a01c594570919cc6f417c761f100eeac60f25667ee5b0efb8e68f29ba3d69 bytes=103603 -->
## FILE: source/codegen/metadata/nixnet/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nixnet/enums.py`
- sha256: `da6a01c594570919cc6f417c761f100eeac60f25667ee5b0efb8e68f29ba3d69`
- bytes: 103603

````python
enums = {
    'BlinkMode': {
        'values': [
            {
                'name': 'DISABLE',
                'value': 0
            },
            {
                'name': 'ENABLE',
                'value': 1
            }
        ]
    },
    'CanCommState': {
        'force-include': True,
        'values': [
            {
                'name': 'ERROR_ACTIVE',
                'value': 0
            },
            {
                'name': 'ERROR_PASSIVE',
                'value': 1
            },
            {
                'name': 'BUS_OFF',
                'value': 2
            },
            {
                'name': 'INIT',
                'value': 3
            }
        ]
    },
    'CanLastErr': {
        'force-include': True,
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'STUFF',
                'value': 1
            },
            {
                'name': 'FORM',
                'value': 2
            },
            {
                'name': 'ACK',
                'value': 3
            },
            {
                'name': 'BIT_1',
                'value': 4
            },
            {
                'name': 'BIT_0',
                'value': 5
            },
            {
                'name': 'CRC',
                'value': 6
            }
        ]
    },
    'CopyMode': {
        'values': [
            {
                'name': 'DB_MERGE_COPY_USE_SOURCE',
                'value': 0
            },
            {
                'name': 'DB_MERGE_COPY_USE_TARGET',
                'value': 1
            },
            {
                'name': 'DB_MERGE_MERGE_USE_SOURCE',
                'value': 2
            },
            {
                'name': 'DB_MERGE_MERGE_USE_TARGET',
                'value': 3
            }
        ]
    },
    'CreateSessionMode': {
        'values': [
            {
                'name': 'SIGNAL_IN_SINGLE_POINT',
                'value': 0
            },
            {
                'name': 'SIGNAL_IN_WAVEFORM',
                'value': 1
            },
            {
                'name': 'SIGNAL_IN_XY',
                'value': 2
            },
            {
                'name': 'SIGNAL_OUT_SINGLE_POINT',
                'value': 3
            },
            {
                'name': 'SIGNAL_OUT_WAVEFORM',
                'value': 4
            },
            {
                'name': 'SIGNAL_OUT_XY',
                'value': 5
            },
            {
                'name': 'FRAME_IN_STREAM',
                'value': 6
            },
            {
                'name': 'FRAME_IN_QUEUED',
                'value': 7
            },
            {
                'name': 'FRAME_IN_SINGLE_POINT',
                'value': 8
            },
            {
                'name': 'FRAME_OUT_STREAM',
                'value': 9
            },
            {
                'name': 'FRAME_OUT_QUEUED',
                'value': 10
            },
            {
                'name': 'FRAME_OUT_SINGLE_POINT',
                'value': 11
            },
            {
                'name': 'SIGNAL_CONVERSION_SINGLE_POINT',
                'value': 12
            }
        ]
    },
    'DBProperty': {
        'generate-mapping-type': True,
        'values': [
            {
                'name': 'DATABASE_CLST_REFS',
                'type': 'db_ref_array',
                'value': 100663298
            },
            {
                'name': 'DATABASE_NAME',
                'type': 'string',
                'value': 50331649
            },
            {
                'name': 'DATABASE_SHOW_INVALID_FROM_OPEN',
                'type': 'boolean',
                'value': 33554435
            },
            {
                'name': 'CLST_BAUD_RATE_64',
                'type': 'u64',
                'value': 151060481
            },
            {
                'name': 'CLST_APPLICATION_PROTOCOL',
                'type': 'u32',
                'value': 65651
            },
            {
                'name': 'CLST_BAUD_RATE',
                'type': 'u32',
                'value': 65537
            },
            {
                'name': 'CLST_CAN_FD_BAUD_RATE_64',
                'type': 'u64',
                'value': 151060497
            },
            {
                'name': 'CLST_CAN_FD_BAUD_RATE',
                'type': 'u32',
                'value': 65553
            },
            {
                'name': 'CLST_CAN_FD_ISO_MODE',
                'type': 'u32',
                'value': 65652
            },
            {
                'name': 'CLST_CAN_IO_MODE',
                'type': 'u32',
                'value': 65552
            },
            {
                'name': 'CLST_COMMENT',
                'type': 'string',
                'value': 50397192
            },
            {
                'name': 'CLST_CONFIG_STATUS',
                'type': 'u32',
                'value': 65545
            },
            {
                'name': 'CLST_DATABASE_REF',
                'type': 'db_ref',
                'value': 83951618
            },
            {
                'name': 'CLST_ECU_REFS',
                'type': 'db_ref_array',
                'value': 100728835
            },
            {
                'name': 'CLST_FLEX_RAY_ACT_PT_OFF',
                'type': 'u32',
                'value': 65568
            },
            {
                'name': 'CLST_FLEX_RAY_ALW_PASS_ACT',
                'type': 'u32',
                'value': 65650
            },
            {
                'name': 'CLST_FLEX_RAY_CAS_RX_L_MAX',
                'type': 'u32',
                'value': 65569
            },
            {
                'name': 'CLST_FLEX_RAY_CHANNELS',
                'type': 'u32',
                'value': 65570
            },
            {
                'name': 'CLST_FLEX_RAY_CLST_DRIFT_DMP',
                'type': 'u32',
                'value': 65571
            },
            {
                'name': 'CLST_FLEX_RAY_COLD_ST_ATS',
                'type': 'u32',
                'value': 65572
            },
            {
                'name': 'CLST_FLEX_RAY_CYCLE',
                'type': 'u32',
                'value': 65573
            },
            {
                'name': 'CLST_FLEX_RAY_DYN_SEG_START',
                'type': 'u32',
                'value': 65574
            },
            {
                'name': 'CLST_FLEX_RAY_DYN_SLOT_IDL_PH',
                'type': 'u32',
                'value': 65575
            },
            {
                'name': 'CLST_FLEX_RAY_LATEST_GUAR_DYN',
                'type': 'u32',
                'value': 65579
            },
            {
                'name': 'CLST_FLEX_RAY_LATEST_USABLE_DYN',
                'type': 'u32',
                'value': 65578
            },
            {
                'name': 'CLST_FLEX_RAY_LIS_NOISE',
                'type': 'u32',
                'value': 65576
            },
            {
                'name': 'CLST_FLEX_RAY_MACRO_PER_CYCLE',
                'type': 'u32',
                'value': 65577
            },
            {
                'name': 'CLST_FLEX_RAY_MACROTICK',
                'type': 'f64',
                'value': 16842800
            },
            {
                'name': 'CLST_FLEX_RAY_MAX_WO_CLK_COR_FAT',
                'type': 'u32',
                'value': 65585
            },
            {
                'name': 'CLST_FLEX_RAY_MAX_WO_CLK_COR_PAS',
                'type': 'u32',
                'value': 65586
            },
            {
                'name': 'CLST_FLEX_RAY_MINISLOT',
                'type': 'u32',
                'value': 65588
            },
            {
                'name': 'CLST_FLEX_RAY_MINISLOT_ACT_PT',
                'type': 'u32',
                'value': 65587
            },
            {
                'name': 'CLST_FLEX_RAY_NIT',
                'type': 'u32',
                'value': 65590
            },
            {
                'name': 'CLST_FLEX_RAY_NIT_START',
                'type': 'u32',
                'value': 65591
            },
            {
                'name': 'CLST_FLEX_RAY_NM_VEC_LEN',
                'type': 'u32',
                'value': 65589
            },
            {
                'name': 'CLST_FLEX_RAY_NUM_MINISLT',
                'type': 'u32',
                'value': 65592
            },
            {
                'name': 'CLST_FLEX_RAY_NUM_STAT_SLT',
                'type': 'u32',
                'value': 65593
            },
            {
                'name': 'CLST_FLEX_RAY_OFF_COR_ST',
                'type': 'u32',
                'value': 65600
            },
            {
                'name': 'CLST_FLEX_RAY_PAYLD_LEN_DYN_MAX',
                'type': 'u32',
                'value': 65601
            },
            {
                'name': 'CLST_FLEX_RAY_PAYLD_LEN_MAX',
                'type': 'u32',
                'value': 65602
            },
            {
                'name': 'CLST_FLEX_RAY_PAYLD_LEN_ST',
                'type': 'u32',
                'value': 65603
            },
            {
                'name': 'CLST_FLEX_RAY_STAT_SLOT',
                'type': 'u32',
                'value': 65605
            },
            {
                'name': 'CLST_FLEX_RAY_SYM_WIN',
                'type': 'u32',
                'value': 65606
            },
            {
                'name': 'CLST_FLEX_RAY_SYM_WIN_START',
                'type': 'u32',
                'value': 65607
            },
            {
                'name': 'CLST_FLEX_RAY_SYNC_NODE_MAX',
                'type': 'u32',
                'value': 65608
            },
            {
                'name': 'CLST_FLEX_RAY_TSS_TX',
                'type': 'u32',
                'value': 65609
            },
            {
                'name': 'CLST_FLEX_RAY_USE_WAKEUP',
                'type': 'boolean',
                'value': 33620053
            },
            {
                'name': 'CLST_FLEX_RAY_WAKE_SYM_RX_IDL',
                'type': 'u32',
                'value': 65616
            },
            {
                'name': 'CLST_FLEX_RAY_WAKE_SYM_RX_LOW',
                'type': 'u32',
                'value': 65617
            },
            {
                'name': 'CLST_FLEX_RAY_WAKE_SYM_RX_WIN',
                'type': 'u32',
                'value': 65618
            },
            {
                'name': 'CLST_FLEX_RAY_WAKE_SYM_TX_IDL',
                'type': 'u32',
                'value': 65619
            },
            {
                'name': 'CLST_FLEX_RAY_WAKE_SYM_TX_LOW',
                'type': 'u32',
                'value': 65620
            },
            {
                'name': 'CLST_FRM_REFS',
                'type': 'db_ref_array',
                'value': 100728836
            },
            {
                'name': 'CLST_LIN_SCHEDULES',
                'type': 'db_ref_array',
                'value': 100728944
            },
            {
                'name': 'CLST_LIN_TICK',
                'type': 'f64',
                'value': 16842865
            },
            {
                'name': 'CLST_NAME',
                'type': 'string',
                'value': 50397189
            },
            {
                'name': 'CLST_PDU_REFS',
                'type': 'db_ref_array',
                'value': 100728840
            },
            {
                'name': 'CLST_PD_US_REQD',
                'type': 'boolean',
                'value': 33619978
            },
            {
                'name': 'CLST_PROTOCOL',
                'type': 'u32',
                'value': 65542
            },
            {
                'name': 'CLST_SIG_REFS',
                'type': 'db_ref_array',
                'value': 100728839
            },
            {
                'name': 'FRM_APPLICATION_PROTOCOL',
                'type': 'u32',
                'value': 131172
            },
            {
                'name': 'FRM_CAN_EXT_ID',
                'type': 'boolean',
                'value': 33685520
            },
            {
                'name': 'FRM_CAN_IO_MODE',
                'type': 'u32',
                'value': 131174
            },
            {
                'name': 'FRM_CAN_TIMING_TYPE',
                'type': 'u32',
                'value': 131089
            },
            {
                'name': 'FRM_CAN_TX_TIME',
                'type': 'f64',
                'value': 16908306
            },
            {
                'name': 'FRM_CLUSTER_REF',
                'type': 'db_ref',
                'value': 84017153
            },
            {
                'name': 'FRM_COMMENT',
                'type': 'string',
                'value': 50462722
            },
            {
                'name': 'FRM_CONFIG_STATUS',
                'type': 'u32',
                'value': 131081
            },
            {
                'name': 'FRM_DEFAULT_PAYLOAD',
                'type': 'u8_array',
                'value': 167903237
            },
            {
                'name': 'FRM_FLEX_RAY_BASE_CYCLE',
                'type': 'u32',
                'value': 131104
            },
            {
                'name': 'FRM_FLEX_RAY_CH_ASSIGN',
                'type': 'u32',
                'value': 131105
            },
            {
                'name': 'FRM_FLEX_RAY_CYCLE_REP',
                'type': 'u32',
                'value': 131106
            },
            {
                'name': 'FRM_FLEX_RAY_IN_CYC_REP_CH_ASSIGNS',
                'type': 'u32_array',
                'value': 134348850
            },
            {
                'name': 'FRM_FLEX_RAY_IN_CYC_REP_ENABLED',
                'type': 'boolean',
                'value': 33685552
            },
            {
                'name': 'FRM_FLEX_RAY_IN_CYC_REP_IDS',
                'type': 'u32_array',
                'value': 134348849
            },
            {
                'name': 'FRM_FLEX_RAY_PREAMBLE',
                'type': 'boolean',
                'value': 33685539
            },
            {
                'name': 'FRM_FLEX_RAY_STARTUP',
                'type': 'boolean',
                'value': 33685540
            },
            {
                'name': 'FRM_FLEX_RAY_SYNC',
                'type': 'boolean',
                'value': 33685541
            },
            {
                'name': 'FRM_FLEX_RAY_TIMING_TYPE',
                'type': 'u32',
                'value': 131110
            },
            {
                'name': 'FRM_ID',
                'type': 'u32',
                'value': 131075
            },
            {
                'name': 'FRM_LIN_CHECKSUM',
                'type': 'u32',
                'value': 131152
            },
            {
                'name': 'FRM_MUX_DATA_MUX_SIG_REF',
                'type': 'db_ref',
                'value': 84017217
            },
            {
                'name': 'FRM_MUX_IS_MUXED',
                'type': 'boolean',
                'value': 33685568
            },
            {
                'name': 'FRM_MUX_STATIC_SIG_REFS',
                'type': 'db_ref_array',
                'value': 100794434
            },
            {
                'name': 'FRM_MUX_SUBFRAME_REFS',
                'type': 'db_ref_array',
                'value': 100794435
            },
            {
                'name': 'FRM_NAME',
                'type': 'string',
                'value': 50462724
            },
            {
                'name': 'FRM_PDU_START_BITS',
                'type': 'u32_array',
                'value': 134348897
            },
            {
                'name': 'FRM_PDU_UPDATE_BITS',
                'type': 'u32_array',
                'value': 134348899
            },
            {
                'name': 'FRM_PDU_REFS',
                'type': 'db_ref_array',
                'value': 100794464
            },
            {
                'name': 'FRM_PAYLOAD_LEN',
                'type': 'u32',
                'value': 131079
            },
            {
                'name': 'FRM_SIG_REFS',
                'type': 'db_ref_array',
                'value': 100794376
            },
            {
                'name': 'FRM_VARIABLE_PAYLOAD',
                'type': 'boolean',
                'value': 33685605
            },
            {
                'name': 'SIG_BYTE_ORDR',
                'type': 'u32',
                'value': 196609
            },
            {
                'name': 'SIG_COMMENT',
                'type': 'string',
                'value': 50528258
            },
            {
                'name': 'SIG_CONFIG_STATUS',
                'type': 'u32',
                'value': 196617
            },
            {
                'name': 'SIG_DATA_TYPE',
                'type': 'u32',
                'value': 196611
            },
            {
                'name': 'SIG_DEFAULT',
                'type': 'f64',
                'value': 16973828
            },
            {
                'name': 'SIG_FRAME_REF',
                'type': 'db_ref',
                'value': 84082693
            },
            {
                'name': 'SIG_MAX',
                'type': 'f64',
                'value': 16973830
            },
            {
                'name': 'SIG_MIN',
                'type': 'f64',
                'value': 16973831
            },
            {
                'name': 'SIG_MUX_IS_DATA_MUX',
                'type': 'boolean',
                'value': 33751088
            },
            {
                'name': 'SIG_MUX_IS_DYNAMIC',
                'type': 'boolean',
                'value': 33751089
            },
            {
                'name': 'SIG_MUX_VALUE',
                'type': 'u32',
                'value': 196658
            },
            {
                'name': 'SIG_MUX_SUBFRM_REF',
                'type': 'db_ref',
                'value': 84082739
            },
            {
                'name': 'SIG_NAME',
                'type': 'string',
                'value': 50528264
            },
            {
                'name': 'SIG_NAME_UNIQUE_TO_CLUSTER',
                'type': 'string',
                'value': 50528272
            },
            {
                'name': 'SIG_NUM_BITS',
                'type': 'u32',
                'value': 196626
            },
            {
                'name': 'SIG_PDU_REF',
                'type': 'db_ref',
                'value': 84082705
            },
            {
                'name': 'SIG_SCALE_FAC',
                'type': 'f64',
                'value': 16973843
            },
            {
                'name': 'SIG_SCALE_OFF',
                'type': 'f64',
                'value': 16973844
            },
            {
                'name': 'SIG_START_BIT',
                'type': 'u32',
                'value': 196629
            },
            {
                'name': 'SIG_UNIT',
                'type': 'string',
                'value': 50528278
            },
            {
                'name': 'SUBFRM_CONFIG_STATUS',
                'type': 'u32',
                'value': 262153
            },
            {
                'name': 'SUBFRM_DYN_SIG_REFS',
                'type': 'db_ref_array',
                'value': 100925441
            },
            {
                'name': 'SUBFRM_FRM_REF',
                'type': 'db_ref',
                'value': 84148226
            },
            {
                'name': 'SUBFRM_MUX_VALUE',
                'type': 'u32',
                'value': 262147
            },
            {
                'name': 'SUBFRM_NAME',
                'type': 'string',
                'value': 50593796
            },
            {
                'name': 'SUBFRM_NAME_UNIQUE_TO_CLUSTER',
                'type': 'string',
                'value': 50593799
            },
            {
                'name': 'SUBFRM_PDU_REF',
                'type': 'db_ref',
                'value': 84148229
            },
            {
                'name': 'ECU_CLST_REF',
                'type': 'db_ref',
                'value': 84213761
            },
            {
                'name': 'ECU_COMMENT',
                'type': 'string',
                'value': 50659333
            },
            {
                'name': 'ECU_CONFIG_STATUS',
                'type': 'u32',
                'value': 327689
            },
            {
                'name': 'ECU_FLEX_RAY_IS_COLDSTART',
                'type': 'boolean',
                'value': 33882128
            },
            {
                'name': 'ECU_FLEX_RAY_CONNECTED_CHS',
                'type': 'u32',
                'value': 327700
            },
            {
                'name': 'ECU_FLEX_RAY_STARTUP_FRAME_REF',
                'type': 'db_ref',
                'value': 84213777
            },
            {
                'name': 'ECU_FLEX_RAY_WAKEUP_CHS',
                'type': 'u32',
                'value': 327699
            },
            {
                'name': 'ECU_FLEX_RAY_WAKEUP_PTRN',
                'type': 'u32',
                'value': 327698
            },
            {
                'name': 'ECU_RX_FRM_REFS',
                'type': 'db_ref_array',
                'value': 100990979
            },
            {
                'name': 'ECU_TX_FRM_REFS',
                'type': 'db_ref_array',
                'value': 100990980
            },
            {
                'name': 'ECU_LIN_CONFIG_NAD',
                'type': 'u32',
                'value': 327715
            },
            {
                'name': 'ECU_LIN_FUNCTION_ID',
                'type': 'u32',
                'value': 327717
            },
            {
                'name': 'ECU_LIN_INITIAL_NAD',
                'type': 'u32',
                'value': 327714
            },
            {
                'name': 'ECU_LIN_MASTER',
                'type': 'boolean',
                'value': 33882144
            },
            {
                'name': 'ECU_LINP2MIN',
                'type': 'f64',
                'value': 17104934
            },
            {
                'name': 'ECU_LIN_PROTOCOL_VER',
                'type': 'u32',
                'value': 327713
            },
            {
                'name': 'ECU_LINS_TMIN',
                'type': 'f64',
                'value': 17104935
            },
            {
                'name': 'ECU_LIN_SUPPLIER_ID',
                'type': 'u32',
                'value': 327716
            },
            {
                'name': 'ECU_NAME',
                'type': 'string',
                'value': 50659330
            },
            {
                'name': 'ECU_J1939_NODE_NAME',
                'type': 'u64',
                'value': 151322665
            },
            {
                'name': 'ECU_J1939_PREFERRED_ADDRESS',
                'type': 'u32',
                'value': 327720
            },
            {
                'name': 'LIN_SCHED_CLST_REF',
                'type': 'db_ref',
                'value': 84279301
            },
            {
                'name': 'LIN_SCHED_COMMENT',
                'type': 'string',
                'value': 50724870
            },
            {
                'name': 'LIN_SCHED_CONFIG_STATUS',
                'type': 'u32',
                'value': 393223
            },
            {
                'name': 'LIN_SCHED_ENTRIES',
                'type': 'db_ref_array',
                'value': 101056513
            },
            {
                'name': 'LIN_SCHED_NAME',
                'type': 'string',
                'value': 50724866
            },
            {
                'name': 'LIN_SCHED_PRIORITY',
                'type': 'u32',
                'value': 393219
            },
            {
                'name': 'LIN_SCHED_RUN_MODE',
                'type': 'u32',
                'value': 393220
            },
            {
                'name': 'LIN_SCHED_ENTRY_COLLISION_RES_SCHED',
                'type': 'db_ref',
                'value': 84344833
            },
            {
                'name': 'LIN_SCHED_ENTRY_DELAY',
                'type': 'f64',
                'value': 17235970
            },
            {
                'name': 'LIN_SCHED_ENTRY_EVENT_ID',
                'type': 'u32',
                'value': 458755
            },
            {
                'name': 'LIN_SCHED_ENTRY_FRAMES',
                'type': 'db_ref_array',
                'value': 101122052
            },
            {
                'name': 'LIN_SCHED_ENTRY_NAME',
                'type': 'string',
                'value': 50790406
            },
            {
                'name': 'LIN_SCHED_ENTRY_NAME_UNIQUE_TO_CLUSTER',
                'type': 'string',
                'value': 50790408
            },
            {
                'name': 'LIN_SCHED_ENTRY_NC_FF_DATA_BYTES',
                'type': 'u8_array',
                'value': 168230921
            },
            {
                'name': 'LIN_SCHED_ENTRY_SCHED',
                'type': 'db_ref',
                'value': 84344839
            },
            {
                'name': 'LIN_SCHED_ENTRY_TYPE',
                'type': 'u32',
                'value': 458757
            },
            {
                'name': 'PDU_CLUSTER_REF',
                'type': 'db_ref',
                'value': 84410372
            },
            {
                'name': 'PDU_COMMENT',
                'type': 'string',
                'value': 50855938
            },
            {
                'name': 'PDU_CONFIG_STATUS',
                'type': 'u32',
                'value': 524295
            },
            {
                'name': 'PDU_DEFAULT_PAYLOAD',
                'type': 'u8_array',
                'value': 168296453
            },
            {
                'name': 'PDU_FRM_REFS',
                'type': 'db_ref_array',
                'value': 101187590
            },
            {
                'name': 'PDU_MUX_DATA_MUX_SIG_REF',
                'type': 'db_ref',
                'value': 84410377
            },
            {
                'name': 'PDU_MUX_IS_MUXED',
                'type': 'boolean',
                'value': 34078728
            },
            {
                'name': 'PDU_MUX_STATIC_SIG_REFS',
                'type': 'db_ref_array',
                'value': 101187594
            },
            {
                'name': 'PDU_MUX_SUBFRAME_REFS',
                'type': 'db_ref_array',
                'value': 101187595
            },
            {
                'name': 'PDU_NAME',
                'type': 'string',
                'value': 50855937
            },
            {
                'name': 'PDU_PAYLOAD_LEN',
                'type': 'u32',
                'value': 524291
            },
            {
                'name': 'PDU_SIG_REFS',
                'type': 'db_ref_array',
                'value': 101187589
            }
        ]
    },
    'DBPropertyValue': {
        'generate-mappings': True,
        'values': [
            {
                'name': 'CAN_IO_MODE_CAN',
                'value': 0
            },
            {
                'name': 'CAN_IO_MODE_CAN_FD',
                'value': 1
            },
            {
                'name': 'CAN_IO_MODE_CAN_FD_BRS',
                'value': 2
            },
            {
                'name': 'PROTOCOL_UNKNOWN',
                'value': 4294967294
            },
            {
                'name': 'PROTOCOL_CAN',
                'value': 0
            },
            {
                'name': 'PROTOCOL_FLEX_RAY',
                'value': 1
            },
            {
                'name': 'PROTOCOL_LIN',
                'value': 2
            },
            {
                'name': 'PROTOCOL_ETHERNET',
                'value': 3
            },
            {
                'name': 'APP_PROTOCOL_NONE',
                'value': 0
            },
            {
                'name': 'APP_PROTOCOL_J1939',
                'value': 1
            },
            {
                'name': 'FRM_FLEX_RAY_CH_ASSIGN_A',
                'value': 1
            },
            {
                'name': 'FRM_FLEX_RAY_CH_ASSIGN_B',
                'value': 2
            },
            {
                'name': 'FRM_FLEX_RAY_CH_ASSIGN_A_AND_B',
                'value': 3
            },
            {
                'name': 'FRM_FLEX_RAY_CH_ASSIGN_NONE',
                'value': 4
            },
            {
                'name': 'CLST_FLEX_RAY_SAMP_CLK_PER_P0125US',
                'value': 0
            },
            {
                'name': 'CLST_FLEX_RAY_SAMP_CLK_PER_P025US',
                'value': 1
            },
            {
                'name': 'CLST_FLEX_RAY_SAMP_CLK_PER_P05US',
                'value': 2
            },
            {
                'name': 'SIG_BYTE_ORDR_LITTLE_ENDIAN',
                'value': 0
            },
            {
                'name': 'SIG_BYTE_ORDR_BIG_ENDIAN',
                'value': 1
            },
            {
                'name': 'SIG_DATA_TYPE_SIGNED',
                'value': 0
            },
            {
                'name': 'SIG_DATA_TYPE_UNSIGNED',
                'value': 1
            },
            {
                'name': 'SIG_DATA_TYPE_IEEE_FLOAT',
                'value': 2
            },
            {
                'name': 'SIG_DATA_TYPE_BYTE_ARRAY',
                'value': 3
            },
            {
                'name': 'LIN_PROTOCOL_VER_1_2',
                'value': 2
            },
            {
                'name': 'LIN_PROTOCOL_VER_1_3',
                'value': 3
            },
            {
                'name': 'LIN_PROTOCOL_VER_2_0',
                'value': 4
            },
            {
                'name': 'LIN_PROTOCOL_VER_2_1',
                'value': 5
            },
            {
                'name': 'LIN_PROTOCOL_VER_2_2',
                'value': 6
            },
            {
                'name': 'LIN_SCHED_RUN_MODE_CONTINUOUS',
                'value': 0
            },
            {
                'name': 'LIN_SCHED_RUN_MODE_ONCE',
                'value': 1
            },
            {
                'name': 'LIN_SCHED_RUN_MODE_NULL',
                'value': 2
            },
            {
                'name': 'LIN_SCHED_ENTRY_TYPE_UNCONDITIONAL',
                'value': 0
            },
            {
                'name': 'LIN_SCHED_ENTRY_TYPE_SPORADIC',
                'value': 1
            },
            {
                'name': 'LIN_SCHED_ENTRY_TYPE_EVENT_TRIGGERED',
                'value': 2
            },
            {
                'name': 'LIN_SCHED_ENTRY_TYPE_NODE_CONFIG_SERVICE',
                'value': 3
            }
        ]
    },
    'EnetFlags': {
        'generate-mappings': True,
        'force-include': True,
        'values': [
            {
                'name': 'TRANSMIT',
                'value': 2147483648
            },
            {
                'name': 'RECEIVE',
                'value': 1073741824
            },
            {
                'name': 'NETWORK_SYNCED',
                'value': 8388608
            },
            {
                'name': 'ERROR',
                'value': 65536
            }
        ]
    },
    'EnetFrameType': {
        'force-include': True,
        'values': [
            {
                'name': 'DATA',
                'value': 0
            },
            {
                'name': 'DELAY',
                'value': 225
            },
            {
                'name': 'FUTURE_TIME_WAIT',
                'value': 226
            }
        ]
    },
    'FlexRayPocState': {
        'force-include': True,
        'values': [
            {
                'name': 'DEFAULT_CONFIG',
                'value': 0
            },
            {
                'name': 'READY',
                'value': 1
            },
            {
                'name': 'NORMAL_ACTIVE',
                'value': 2
            },
            {
                'name': 'NORMAL_PASSIVE',
                'value': 3
            },
            {
                'name': 'HALT',
                'value': 4
            },
            {
                'name': 'MONITOR',
                'value': 5
            },
            {
                'name': 'CONFIG',
                'value': 15
            }
        ]
    },
    'FlexRaySymbol': {
        'force-include': True,
        'values': [
            {
                'name': 'MTS',
                'value': 0
            },
            {
                'name': 'WAKEUP',
                'value': 1
            }
        ]
    },
    'FrameFlags': {
        'force-include': True,
        'values': [
            {
                'name': 'FLEX_RAY_STARTUP',
                'value': 1
            },
            {
                'name': 'FLEX_RAY_SYNC',
                'value': 2
            },
            {
                'name': 'FLEX_RAY_PREAMBLE',
                'value': 4
            },
            {
                'name': 'FLEX_RAY_CH_A',
                'value': 16
            },
            {
                'name': 'FLEX_RAY_CH_B',
                'value': 32
            },
            {
                'name': 'LIN_EVENT_SLOT',
                'value': 1
            },
            {
                'name': 'TRANSMIT_ECHO',
                'value': 128
            }
        ]
    },
    'FrameType': {
        'force-include': True,
        'values': [
            {
                'name': 'CAN_DATA',
                'value': 0
            },
            {
                'name': 'CAN_REMOTE',
                'value': 1
            },
            {
                'name': 'CAN_BUS_ERROR',
                'value': 2
            },
            {
                'name': 'CAN20_DATA',
                'value': 8
            },
            {
                'name': 'CANFD_DATA',
                'value': 16
            },
            {
                'name': 'CANFDBRS_DATA',
                'value': 24
            },
            {
                'name': 'FLEX_RAY_DATA',
                'value': 32
            },
            {
                'name': 'FLEX_RAY_NULL',
                'value': 33
            },
            {
                'name': 'FLEX_RAY_SYMBOL',
                'value': 34
            },
            {
                'name': 'LIN_DATA',
                'value': 64
            },
            {
                'name': 'LIN_BUS_ERROR',
                'value': 65
            },
            {
                'name': 'LIN_NO_RESPONSE',
                'value': 66
            },
            {
                'name': 'J1939_DATA',
                'value': 192
            },
            {
                'name': 'SPECIAL_DELAY',
                'value': 224
            },
            {
                'name': 'SPECIAL_LOG_TRIGGER',
                'value': 225
            },
            {
                'name': 'SPECIAL_START_TRIGGER',
                'value': 226
            }
        ]
    },
    'GetDBCAttributeMode': {
        'values': [
            {
                'name': 'ATTRIBUTE',
                'value': 0
            },
            {
                'name': 'ENUMERATION_LIST',
                'value': 1
            },
            {
                'name': 'ATTRIBUTE_LIST',
                'value': 2
            },
            {
                'name': 'VALUE_TABLE_LIST',
                'value': 3
            }
        ]
    },
    'LinCommState': {
        'force-include': True,
        'values': [
            {
                'name': 'IDLE',
                'value': 0
            },
            {
                'name': 'ACTIVE',
                'value': 1
            },
            {
                'name': 'INACTIVE',
                'value': 2
            }
        ]
    },
    'LinDiagnosticSchedule': {
        'force-include': True,
        'values': [
            {
                'name': 'NULL',
                'value': 0
            },
            {
                'name': 'MASTER_REQ',
                'value': 1
            },
            {
                'name': 'SLAVE_RESP',
                'value': 2
            }
        ]
    },
    'LinLastErrCode': {
        'force-include': True,
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'UNKNOWN_ID',
                'value': 1
            },
            {
                'name': 'FORM',
                'value': 2
            },
            {
                'name': 'FRAMING',
                'value': 3
            },
            {
                'name': 'READBACK',
                'value': 4
            },
            {
                'name': 'TIMEOUT',
                'value': 5
            },
            {
                'name': 'CRC',
                'value': 6
            }
        ]
    },
    'Property': {
        'generate-mapping-type': True,
        'values': [
            {
                'name': 'SESSION_APPLICATION_PROTOCOL',
                'type': 'u32',
                'value': 1048721
            },
            {
                'name': 'SESSION_AUTO_START',
                'type': 'boolean',
                'value': 34603009
            },
            {
                'name': 'SESSION_CLUSTER_NAME',
                'type': 'string',
                'value': 51380234
            },
            {
                'name': 'SESSION_DATABASE_NAME',
                'type': 'string',
                'value': 51380226
            },
            {
                'name': 'SESSION_ENET_FRAME_FILTER',
                'type': 'string',
                'value': 51380468
            },
            {
                'name': 'SESSION_ENET_LOG_ERROR',
                'type': 'boolean',
                'value': 34603197
            },
            {
                'name': 'SESSION_ENET_LOG_FILE',
                'type': 'string',
                'value': 51380410
            },
            {
                'name': 'SESSION_ENET_LOG_MODE',
                'type': 'u32',
                'value': 1048761
            },
            {
                'name': 'SESSION_ENET_LOG_ENABLE_MULTIPLE_FILES',
                'type': 'boolean',
                'value': 34603257
            },
            {
                'name': 'SESSION_ENET_LOG_FILE_SIZE_THRESHOLD',
                'type': 'u64',
                'value': 152043770
            },
            {
                'name': 'SESSION_ENET_LOG_OPERATION',
                'type': 'u32',
                'value': 1048763
            },
            {
                'name': 'SESSION_ENET_NUM_FRAMES_RECEIVED',
                'type': 'u64',
                'value': 152043759
            },
            {
                'name': 'SESSION_ENET_SOURCE_MAC_ADDRESS_AUTO',
                'type': 'boolean',
                'value': 34603177
            },
            {
                'name': 'SESSION_INTF_BAUD_RATE_64',
                'type': 'u64',
                'value': 152043542
            },
            {
                'name': 'SESSION_INTF_ADJUST_LOCAL_TIME',
                'type': 'u64',
                'value': 152043691
            },
            {
                'name': 'SESSION_INTF_BAUD_RATE',
                'type': 'u32',
                'value': 1048598
            },
            {
                'name': 'SESSION_INTF_BUS_ERR_TO_IN_STRM',
                'type': 'boolean',
                'value': 34603029
            },
            {
                'name': 'SESSION_INTF_CAN_FD_BAUD_RATE_64',
                'type': 'u64',
                'value': 152043559
            },
            {
                'name': 'SESSION_INTF_CAN_DISABLE_PROT_EXCEPTION_HANDLING',
                'type': 'boolean',
                'value': 34603172
            },
            {
                'name': 'SESSION_INTF_CAN_EDGE_FILTER',
                'type': 'boolean',
                'value': 34603170
            },
            {
                'name': 'SESSION_INTF_CAN_EXT_TCVR_CONFIG',
                'type': 'u32',
                'value': 1048611
            },
            {
                'name': 'SESSION_INTF_CAN_FD_BAUD_RATE',
                'type': 'u32',
                'value': 1048615
            },
            {
                'name': 'SESSION_INTF_CAN_FD_ISO_MODE',
                'type': 'u32',
                'value': 1048638
            },
            {
                'name': 'SESSION_INTF_CAN_IO_MODE',
                'type': 'u32',
                'value': 1048614
            },
            {
                'name': 'SESSION_INTF_CAN_LSTN_ONLY',
                'type': 'boolean',
                'value': 34603042
            },
            {
                'name': 'SESSION_INTF_CAN_PEND_TX_ORDER',
                'type': 'u32',
                'value': 1048608
            },
            {
                'name': 'SESSION_INTF_CAN_SING_SHOT',
                'type': 'boolean',
                'value': 34603044
            },
            {
                'name': 'SESSION_INTF_CAN_TERM',
                'type': 'u32',
                'value': 1048613
            },
            {
                'name': 'SESSION_INTF_CAN_TCVR_STATE',
                'type': 'u32',
                'value': 1048616
            },
            {
                'name': 'SESSION_INTF_CAN_TCVR_TYPE',
                'type': 'u32',
                'value': 1048617
            },
            {
                'name': 'SESSION_INTF_CAN_TX_IO_MODE',
                'type': 'u32',
                'value': 1048633
            },
            {
                'name': 'SESSION_INTF_CAN_TRANSMIT_PAUSE',
                'type': 'boolean',
                'value': 34603171
            },
            {
                'name': 'SESSION_INTF_ECHO_TX',
                'type': 'boolean',
                'value': 34603024
            },
            {
                'name': 'SESSION_INTF_ENET_EPT_RECEIVE_FILTER',
                'type': 'nxEptRxFilter_Element_t_array',
                'value': 202375356
            },
            {
                'name': 'SESSION_INTF_ENET_EPT_TRANSMIT_BANDWIDTH',
                'type': 'u64',
                'value': 152043711
            },
            {
                'name': 'SESSION_INTF_ENET_IPV4_ADDRESS',
                'type': 'string',
                'value': 51380459
            },
            {
                'name': 'SESSION_INTF_ENET_JUMBO_FRAMES',
                'type': 'u32',
                'value': 1048819
            },
            {
                'name': 'SESSION_INTF_ENET_LINK_SPEED',
                'type': 'u32',
                'value': 1048818
            },
            {
                'name': 'SESSION_INTF_ENET_LINK_SPEED_CONFIGURED',
                'type': 'u32',
                'value': 1048817
            },
            {
                'name': 'SESSION_INTF_ENET_MAC_ADDRESS',
                'type': 'string',
                'value': 51380392
            },
            {
                'name': 'SESSION_INTF_ENET_OS_NETWORK_ADAPTER_DESCRIPTION',
                'type': 'string',
                'value': 51380461
            },
            {
                'name': 'SESSION_INTF_ENET_OS_NETWORK_ADAPTER_NAME',
                'type': 'string',
                'value': 51380460
            },
            {
                'name': 'SESSION_INTF_ENET_OPERATIONAL_STATUS',
                'type': 'u32',
                'value': 1048746
            },
            {
                'name': 'SESSION_INTF_ENET_OUT_STRM_TIMESCALE',
                'type': 'u32',
                'value': 1048823
            },
            {
                'name': 'SESSION_INTF_ENET_PHY_POWER_MODE',
                'type': 'u32',
                'value': 1048825
            },
            {
                'name': 'SESSION_INTF_ENET_PHY_STATE',
                'type': 'u32',
                'value': 1048743
            },
            {
                'name': 'SESSION_INTF_ENET_PORT_MODE',
                'type': 'u32',
                'value': 1048742
            },
            {
                'name': 'SESSION_INTF_ENET_SIGNAL_QUALITY',
                'type': 'i32',
                'value': 235929846
            },
            {
                'name': 'SESSION_INTF_ENET_SLEEP_CAPABILITY',
                'type': 'u32',
                'value': 1048824
            },
            {
                'name': 'SESSION_INTF_ENET_STATS_COUNTER_NAMES',
                'type': 'string',
                'value': 68157612
            },
            {
                'name': 'SESSION_INTF_ENET_STATS_COUNTER_VALUES',
                'type': 'string',
                'value': 68157613
            },
            {
                'name': 'SESSION_INTF_ENET_STATS_RX_BAD_FRAMES',
                'type': 'u64',
                'value': 152043702
            },
            {
                'name': 'SESSION_INTF_ENET_STATS_RX_BYTES',
                'type': 'u64',
                'value': 152043694
            },
            {
                'name': 'SESSION_INTF_ENET_STATS_RX_GOOD_FRAMES',
                'type': 'u64',
                'value': 152043695
            },
            {
                'name': 'SESSION_INTF_ENET_STATS_TX_BYTES',
                'type': 'u64',
                'value': 152043703
            },
            {
                'name': 'SESSION_INTF_ENET_STATS_TX_GOOD_FRAMES',
                'type': 'u64',
                'value': 152043704
            },
            {
                'name': 'SESSION_INTF_ENET_STATS_PHY_COUNTER_NAMES',
                'type': 'string',
                'value': 68157693
            },
            {
                'name': 'SESSION_INTF_ENET_STATS_PHY_COUNTER_VALUES',
                'type': 'string',
                'value': 68157694
            },
            {
                'name': 'SESSION_INTF_ENET_STATS_PHY_LOW_POWER_SLEEP',
                'type': 'u64',
                'value': 152043777
            },
            {
                'name': 'SESSION_INTF_ENET_STATS_PHY_SLEEP_FAILURE',
                'type': 'u64',
                'value': 152043779
            },
            {
                'name': 'SESSION_INTF_ENET_STATS_PHY_WAKEUP_FAILURE',
                'type': 'u64',
                'value': 152043778
            },
            {
                'name': 'SESSION_INTF_ENET_STATS_PHY_WAKEUP_PULSE',
                'type': 'u64',
                'value': 152043775
            },
            {
                'name': 'SESSION_INTF_ENET_STATS_PHY_WAKEUP_REQUEST',
                'type': 'u64',
                'value': 152043776
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_ADJUST_NETWORK_TIME',
                'type': 'u64',
                'value': 152043729
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_BMCA_ENABLED',
                'type': 'boolean',
                'value': 34603202
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_CLK_ACCURACY',
                'type': 'u32',
                'value': 1048774
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_CLK_CLASS',
                'type': 'u32',
                'value': 1048773
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_CLK_ID',
                'type': 'string',
                'value': 51380420
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_CLK_OFFSET_VAR',
                'type': 'u32',
                'value': 1048775
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_GM_CLK_ACCURACY',
                'type': 'u32',
                'value': 1048781
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_GM_CLK_CLASS',
                'type': 'u32',
                'value': 1048780
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_GM_CLK_ID',
                'type': 'string',
                'value': 51380427
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_GM_CLK_OFFSET_VAR',
                'type': 'u32',
                'value': 1048782
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_GM_PRIORITY_1',
                'type': 'u32',
                'value': 1048783
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_GM_PRIORITY_2',
                'type': 'u32',
                'value': 1048784
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_OFFSET_FROM_MASTER',
                'type': 'u64',
                'value': 152043715
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PORT_AS_CAPABLE',
                'type': 'boolean',
                'value': 34603233
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PORT_ANNOUNCE_RECEIPT_TIMEOUT',
                'type': 'u32',
                'value': 1048800
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PORT_ANNOUNCE_TRANSMIT_ENABLED',
                'type': 'boolean',
                'value': 34603231
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PORT_LOG_ANNOUNCE_INTERVAL',
                'type': 'u32',
                'value': 1048798
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PORT_LOG_ANNOUNCE_INTERVAL_CONFIGURED',
                'type': 'u32',
                'value': 1048797
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PORT_LOG_PDELAY_INTERVAL',
                'type': 'u32',
                'value': 1048793
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PORT_LOG_PDELAY_INTERVAL_CONFIGURED',
                'type': 'u32',
                'value': 1048792
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PORT_LOG_SYNC_INTERVAL',
                'type': 'u32',
                'value': 1048795
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PORT_LOG_SYNC_INTERVAL_CONFIGURED',
                'type': 'u32',
                'value': 1048794
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PORT_PDELAY_ENABLED',
                'type': 'boolean',
                'value': 34603223
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PORT_STATE',
                'type': 'u32',
                'value': 1048787
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PORT_STATE_CONFIGURED',
                'type': 'u32',
                'value': 1048786
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PORT_PROP_DELAY',
                'type': 'f64',
                'value': 17826004
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PORT_PROP_DELAY_CONFIGURED',
                'type': 'f64',
                'value': 17826005
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PORT_PROP_DELAY_THRESHOLD',
                'type': 'f64',
                'value': 17826006
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PORT_STATS_COUNTER_NAMES',
                'type': 'string',
                'value': 68157667
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PORT_STATS_COUNTER_VALUES',
                'type': 'string',
                'value': 68157668
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PORT_STATS_RX_ANNOUNCE',
                'type': 'u64',
                'value': 152043750
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PORT_STATS_RX_PDELAY_REQUEST',
                'type': 'u64',
                'value': 152043751
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PORT_STATS_RX_SYNC',
                'type': 'u64',
                'value': 152043749
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PORT_STATS_TX_ANNOUNCE',
                'type': 'u64',
                'value': 152043753
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PORT_STATS_TX_PDELAY_REQUEST',
                'type': 'u64',
                'value': 152043754
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PORT_STATS_TX_SYNC',
                'type': 'u64',
                'value': 152043752
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PORT_SYNC_RECEIPT_TIMEOUT',
                'type': 'u32',
                'value': 1048796
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PORT_SYNC_STATUS',
                'type': 'u32',
                'value': 1048816
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PORT_SYNCED',
                'type': 'boolean',
                'value': 34603234
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PRIORITY_1',
                'type': 'u32',
                'value': 1048776
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PRIORITY_2',
                'type': 'u32',
                'value': 1048777
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PROTOCOL',
                'type': 'u32',
                'value': 1048768
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_PROTOCOL_ENABLED',
                'type': 'boolean',
                'value': 34603201
            },
            {
                'name': 'SESSION_INTF_ENET_TIME_STEPS_TO_GM',
                'type': 'u32',
                'value': 1048778
            },
            {
                'name': 'SESSION_INTF_ENET_TRIGGER_PPS_SYNCED',
                'type': 'boolean',
                'value': 34603268
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_ACC_START_RNG',
                'type': 'u32',
                'value': 1048624
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_ALW_HLT_CLK',
                'type': 'boolean',
                'value': 34603057
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_ALW_PASS_ACT',
                'type': 'u32',
                'value': 1048626
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_AUTO_ASLP_WHN_STP',
                'type': 'boolean',
                'value': 34603066
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_CLST_DRIFT_DMP',
                'type': 'u32',
                'value': 1048627
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_COLDSTART',
                'type': 'boolean',
                'value': 34603060
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_CONNECTED_CHS',
                'type': 'u32',
                'value': 1048636
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_DEC_CORR',
                'type': 'u32',
                'value': 1048629
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_DELAY_COMP_A',
                'type': 'u32',
                'value': 1048630
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_DELAY_COMP_B',
                'type': 'u32',
                'value': 1048631
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_KEY_SLOT_ID',
                'type': 'u32',
                'value': 1048632
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_LATEST_TX',
                'type': 'u32',
                'value': 1048641
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_LIST_TIMO',
                'type': 'u32',
                'value': 1048642
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_MAC_INIT_OFF_A',
                'type': 'u32',
                'value': 1048643
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_MAC_INIT_OFF_B',
                'type': 'u32',
                'value': 1048644
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_MAX_DRIFT',
                'type': 'u32',
                'value': 1048647
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_MIC_INIT_OFF_A',
                'type': 'u32',
                'value': 1048645
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_MIC_INIT_OFF_B',
                'type': 'u32',
                'value': 1048646
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_MICROTICK',
                'type': 'u32',
                'value': 1048648
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_NULL_TO_IN_STRM',
                'type': 'boolean',
                'value': 34603081
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_OFF_CORR',
                'type': 'u32',
                'value': 1048664
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_OFF_CORR_OUT',
                'type': 'u32',
                'value': 1048656
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_RATE_CORR',
                'type': 'u32',
                'value': 1048665
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_RATE_CORR_OUT',
                'type': 'u32',
                'value': 1048658
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_SAMP_PER_MICRO',
                'type': 'u32',
                'value': 1048659
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_SING_SLOT_EN',
                'type': 'boolean',
                'value': 34603092
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_SLEEP',
                'type': 'u32',
                'value': 1048635
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_STATISTICS_EN',
                'type': 'boolean',
                'value': 34603098
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_SYM_TO_IN_STRM',
                'type': 'boolean',
                'value': 34603069
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_SYNC_STATUS',
                'type': 'u32',
                'value': 1048671
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_SYNC_CH_A_EVEN',
                'type': 'u32_array',
                'value': 135266395
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_SYNC_CH_A_ODD',
                'type': 'u32_array',
                'value': 135266396
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_SYNC_CH_B_EVEN',
                'type': 'u32_array',
                'value': 135266397
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_SYNC_CH_B_ODD',
                'type': 'u32_array',
                'value': 135266398
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_TERM',
                'type': 'u32',
                'value': 1048663
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_WAKEUP_CH',
                'type': 'u32',
                'value': 1048661
            },
            {
                'name': 'SESSION_INTF_FLEX_RAY_WAKEUP_PTRN',
                'type': 'u32',
                'value': 1048662
            },
            {
                'name': 'SESSION_INTF_NAME',
                'type': 'string',
                'value': 51380243
            },
            {
                'name': 'SESSION_INTF_LIN_BREAK_DELIMITER_LENGTH',
                'type': 'u32',
                'value': 1048821
            },
            {
                'name': 'SESSION_INTF_LIN_BREAK_LENGTH',
                'type': 'u32',
                'value': 1048688
            },
            {
                'name': 'SESSION_INTF_LIN_CHECKSUM_TO_IN_STRM',
                'type': 'boolean',
                'value': 34603137
            },
            {
                'name': 'SESSION_INTF_LIN_DIAG_P2_MIN',
                'type': 'f64',
                'value': 17825911
            },
            {
                'name': 'SESSION_INTF_LIN_DIAG_ST_MIN',
                'type': 'f64',
                'value': 17825910
            },
            {
                'name': 'SESSION_INTF_LIN_MASTER',
                'type': 'boolean',
                'value': 34603122
            },
            {
                'name': 'SESSION_INTF_LIN_NO_RESPONSE_TO_IN_STRM',
                'type': 'boolean',
                'value': 34603136
            },
            {
                'name': 'SESSION_INTF_LINO_STR_SLV_RSP_LST_BY_NAD',
                'type': 'u32_array',
                'value': 135266425
            },
            {
                'name': 'SESSION_INTF_LIN_SCHED_NAMES',
                'type': 'string',
                'value': 68157557
            },
            {
                'name': 'SESSION_INTF_LIN_SLEEP',
                'type': 'u32',
                'value': 1048691
            },
            {
                'name': 'SESSION_INTF_LIN_ALW_START_WO_BUS_PWR',
                'type': 'boolean',
                'value': 34603128
            },
            {
                'name': 'SESSION_INTF_LIN_TERM',
                'type': 'u32',
                'value': 1048692
            },
            {
                'name': 'SESSION_INTF_OUT_STRM_LIST',
                'type': 'db_ref_array',
                'value': 101711889
            },
            {
                'name': 'SESSION_INTF_OUT_STRM_LIST_BY_ID',
                'type': 'u32_array',
                'value': 135266337
            },
            {
                'name': 'SESSION_INTF_OUT_STRM_TIMNG',
                'type': 'u32',
                'value': 1048594
            },
            {
                'name': 'SESSION_INTF_SRC_TERM_START_TRIGGER',
                'type': 'string',
                'value': 51380368
            },
            {
                'name': 'SESSION_INTF_START_TRIG_TO_IN_STRM',
                'type': 'boolean',
                'value': 34603028
            },
            {
                'name': 'SESSION_LIST',
                'type': 'string',
                'value': 68157443
            },
            {
                'name': 'SESSION_MODE',
                'type': 'u32',
                'value': 1048580
            },
            {
                'name': 'SESSION_NUM_IN_LIST',
                'type': 'u32',
                'value': 1048581
            },
            {
                'name': 'SESSION_NUM_FRAMES',
                'type': 'u32',
                'value': 1048589
            },
            {
                'name': 'SESSION_NUM_PEND',
                'type': 'u32',
                'value': 1048582
            },
            {
                'name': 'SESSION_NUM_UNUSED',
                'type': 'u32',
                'value': 1048587
            },
            {
                'name': 'SESSION_PAYLD_LEN_MAX',
                'type': 'u32',
                'value': 1048585
            },
            {
                'name': 'SESSION_PROTOCOL',
                'type': 'u32',
                'value': 1048584
            },
            {
                'name': 'SESSION_QUEUE_SIZE',
                'type': 'u32',
                'value': 1048588
            },
            {
                'name': 'SESSION_RESAMP_RATE',
                'type': 'f64',
                'value': 17825799
            },
            {
                'name': 'SESSION_J1939_ECU',
                'type': 'db_ref',
                'value': 84934803
            },
            {
                'name': 'SESSION_J1939_ECU_BUSY',
                'type': 'boolean',
                'value': 34603169
            },
            {
                'name': 'SESSION_J1939_FILL_BYTE',
                'type': 'u32',
                'value': 1048735
            },
            {
                'name': 'SESSION_J1939_INCLUDE_DEST_ADDR_IN_PGN',
                'type': 'boolean',
                'value': 34603173
            },
            {
                'name': 'SESSION_J1939_MAX_REPEAT_CTS',
                'type': 'u32',
                'value': 1048734
            },
            {
                'name': 'SESSION_J1939_ADDRESS',
                'type': 'u32',
                'value': 1048722
            },
            {
                'name': 'SESSION_J1939_NAME',
                'type': 'u64',
                'value': 152043668
            },
            {
                'name': 'SESSION_J1939_NUM_PACKETS_RECV',
                'type': 'u32',
                'value': 1048732
            },
            {
                'name': 'SESSION_J1939_NUM_PACKETS_RESP',
                'type': 'u32',
                'value': 1048733
            },
            {
                'name': 'SESSION_J1939_HOLD_TIME_TH',
                'type': 'f64',
                'value': 17825947
            },
            {
                'name': 'SESSION_J1939_RESPONSE_TIME_TR_GD',
                'type': 'f64',
                'value': 17825946
            },
            {
                'name': 'SESSION_J1939_RESPONSE_TIME_TR_SD',
                'type': 'f64',
                'value': 17825945
            },
            {
                'name': 'SESSION_J1939_TIMEOUT_T1',
                'type': 'f64',
                'value': 17825941
            },
            {
                'name': 'SESSION_J1939_TIMEOUT_T2',
                'type': 'f64',
                'value': 17825942
            },
            {
                'name': 'SESSION_J1939_TIMEOUT_T3',
                'type': 'f64',
                'value': 17825943
            },
            {
                'name': 'SESSION_J1939_TIMEOUT_T4',
                'type': 'f64',
                'value': 17825944
            },
            {
                'name': 'SESSION_J1939_WRITE_QUEUE_SIZE',
                'type': 'u32',
                'value': 1048736
            },
            {
                'name': 'SYS_CDAQ_PKT_TIME',
                'type': 'f64',
                'value': 17891340
            },
            {
                'name': 'SYS_DEV_REFS',
                'type': 'dev_ref_array',
                'value': 101777410
            },
            {
                'name': 'SYS_INTF_REFS',
                'type': 'intf_ref_array',
                'value': 101777411
            },
            {
                'name': 'SYS_INTF_REFS_ALL',
                'type': 'intf_ref_array',
                'value': 101777421
            },
            {
                'name': 'SYS_INTF_REFS_CAN',
                'type': 'intf_ref_array',
                'value': 101777412
            },
            {
                'name': 'SYS_INTF_REFS_ETHERNET',
                'type': 'intf_ref_array',
                'value': 101777409
            },
            {
                'name': 'SYS_INTF_REFS_FLEX_RAY',
                'type': 'intf_ref_array',
                'value': 101777413
            },
            {
                'name': 'SYS_INTF_REFS_LIN',
                'type': 'intf_ref_array',
                'value': 101777415
            },
            {
                'name': 'SYS_VER_BUILD',
                'type': 'u32',
                'value': 1114118
            },
            {
                'name': 'SYS_VER_MAJOR',
                'type': 'u32',
                'value': 1114120
            },
            {
                'name': 'SYS_VER_MINOR',
                'type': 'u32',
                'value': 1114121
            },
            {
                'name': 'SYS_VER_PHASE',
                'type': 'u32',
                'value': 1114122
            },
            {
                'name': 'SYS_VER_UPDATE',
                'type': 'u32',
                'value': 1114123
            },
            {
                'name': 'DEV_FORM_FAC',
                'type': 'u32',
                'value': 1179649
            },
            {
                'name': 'DEV_INTF_REFS',
                'type': 'intf_ref_array',
                'value': 101842946
            },
            {
                'name': 'DEV_INTF_REFS_ALL',
                'type': 'intf_ref_array',
                'value': 101842952
            },
            {
                'name': 'DEV_NUM_PORTS',
                'type': 'u32',
                'value': 1179652
            },
            {
                'name': 'DEV_NUM_PORTS_ALL',
                'type': 'u32',
                'value': 1179655
            },
            {
                'name': 'DEV_NAME',
                'type': 'string',
                'value': 51511299
            },
            {
                'name': 'DEV_PRODUCT_NUM',
                'type': 'u32',
                'value': 1179656
            },
            {
                'name': 'DEV_SER_NUM',
                'type': 'u32',
                'value': 1179653
            },
            {
                'name': 'DEV_SLOT_NUM',
                'type': 'u32',
                'value': 1179654
            },
            {
                'name': 'INTF_CAN_TERM_CAP',
                'type': 'u32',
                'value': 1245192
            },
            {
                'name': 'INTF_CAN_TCVR_CAP',
                'type': 'u32',
                'value': 1245191
            },
            {
                'name': 'INTF_DEV_REF',
                'type': 'dev_ref',
                'value': 85131265
            },
            {
                'name': 'INTF_DONGLE_COMPATIBLE_FIRMWARE_VERSION',
                'type': 'u32',
                'value': 1245199
            },
            {
                'name': 'INTF_DONGLE_COMPATIBLE_REVISION',
                'type': 'u32',
                'value': 1245198
            },
            {
                'name': 'INTF_DONGLE_FIRMWARE_VERSION',
                'type': 'u32',
                'value': 1245197
            },
            {
                'name': 'INTF_DONGLE_ID',
                'type': 'u32',
                'value': 1245194
            },
            {
                'name': 'INTF_DONGLE_REVISION',
                'type': 'u32',
                'value': 1245196
            },
            {
                'name': 'INTF_DONGLE_STATE',
                'type': 'u32',
                'value': 1245193
            },
            {
                'name': 'INTF_NAME',
                'type': 'string',
                'value': 51576834
            },
            {
                'name': 'INTF_NUM',
                'type': 'u32',
                'value': 1245187
            },
            {
                'name': 'INTF_PORT_NUM',
                'type': 'u32',
                'value': 1245188
            },
            {
                'name': 'INTF_PROTOCOL',
                'type': 'u32',
                'value': 1245189
            }
        ]
    },
    'PropertyValue': {
        'generate-mappings': True,
        'values': [
            {
                'name': 'CAN_FD_MODE_ISO',
                'value': 0
            },
            {
                'name': 'CAN_FD_MODE_NON_ISO',
                'value': 1
            },
            {
                'name': 'CAN_FD_MODE_ISO_LEGACY',
                'value': 2
            },
            {
                'name': 'CAN_IO_MODE_CAN',
                'value': 0
            },
            {
                'name': 'CAN_IO_MODE_CAN_FD',
                'value': 1
            },
            {
                'name': 'CAN_IO_MODE_CAN_FD_BRS',
                'value': 2
            },
            {
                'name': 'EPT_RX_FILTER_USE_FLAGS_VID',
                'value': 1
            },
            {
                'name': 'EPT_RX_FILTER_USE_FLAGS_PRIORITY',
                'value': 2
            },
            {
                'name': 'EPT_RX_FILTER_USE_FLAGS_DESTINATION_MAC',
                'value': 4
            },
            {
                'name': 'PHASE_DEVELOPMENT',
                'value': 0
            },
            {
                'name': 'PHASE_ALPHA',
                'value': 1
            },
            {
                'name': 'PHASE_BETA',
                'value': 2
            },
            {
                'name': 'PHASE_RELEASE',
                'value': 3
            },
            {
                'name': 'DEV_FORM_PXI',
                'value': 0
            },
            {
                'name': 'DEV_FORM_PCI',
                'value': 1
            },
            {
                'name': 'DEV_FORM_C_SERIES',
                'value': 2
            },
            {
                'name': 'DEV_FORM_PXIE',
                'value': 3
            },
            {
                'name': 'DEV_FORM_USB',
                'value': 4
            },
            {
                'name': 'DEV_FORM_PCIE',
                'value': 5
            },
            {
                'name': 'CAN_TERM_CAP_NO',
                'value': 0
            },
            {
                'name': 'CAN_TERM_CAP_YES',
                'value': 1
            },
            {
                'name': 'CAN_TCVR_CAP_HS',
                'value': 0
            },
            {
                'name': 'CAN_TCVR_CAP_LS',
                'value': 1
            },
            {
                'name': 'CAN_TCVR_CAP_XS',
                'value': 3
            },
            {
                'name': 'CAN_TCVR_CAP_XS_HS_LS',
                'value': 4
            },
            {
                'name': 'CAN_TCVR_CAP_UNKNOWN',
                'value': 4294967295
            },
            {
                'name': 'PROTOCOL_UNKNOWN',
                'value': 4294967294
            },
            {
                'name': 'PROTOCOL_CAN',
                'value': 0
            },
            {
                'name': 'PROTOCOL_FLEX_RAY',
                'value': 1
            },
            {
                'name': 'PROTOCOL_LIN',
                'value': 2
            },
            {
                'name': 'PROTOCOL_ETHERNET',
                'value': 3
            },
            {
                'name': 'APP_PROTOCOL_NONE',
                'value': 0
            },
            {
                'name': 'APP_PROTOCOL_J1939',
                'value': 1
            },
            {
                'name': 'DONGLE_STATE_NO_DONGLE_NO_EXT_POWER',
                'value': 1
            },
            {
                'name': 'DONGLE_STATE_NO_DONGLE_EXT_POWER',
                'value': 2
            },
            {
                'name': 'DONGLE_STATE_DONGLE_NO_EXT_POWER',
                'value': 3
            },
            {
                'name': 'DONGLE_STATE_READY',
                'value': 4
            },
            {
                'name': 'DONGLE_STATE_BUSY',
                'value': 5
            },
            {
                'name': 'DONGLE_STATE_COMM_ERROR',
                'value': 13
            },
            {
                'name': 'DONGLE_STATE_OVER_CURRENT',
                'value': 14
            },
            {
                'name': 'DONGLE_ID_LS_CAN',
                'value': 1
            },
            {
                'name': 'DONGLE_ID_HS_CAN',
                'value': 2
            },
            {
                'name': 'DONGLE_ID_SW_CAN',
                'value': 3
            },
            {
                'name': 'DONGLE_ID_XS_CAN',
                'value': 4
            },
            {
                'name': 'DONGLE_ID_LIN',
                'value': 6
            },
            {
                'name': 'DONGLE_ID_DONGLE_LESS',
                'value': 13
            },
            {
                'name': 'DONGLE_ID_UNKNOWN',
                'value': 14
            },
            {
                'name': 'CAN_TERM_OFF',
                'value': 0
            },
            {
                'name': 'CAN_TERM_ON',
                'value': 1
            },
            {
                'name': 'CAN_TCVR_STATE_NORMAL',
                'value': 0
            },
            {
                'name': 'CAN_TCVR_STATE_SLEEP',
                'value': 1
            },
            {
                'name': 'CAN_TCVR_STATE_SW_WAKEUP',
                'value': 2
            },
            {
                'name': 'CAN_TCVR_STATE_SW_HIGH_SPEED',
                'value': 3
            },
            {
                'name': 'CAN_TCVR_TYPE_HS',
                'value': 0
            },
            {
                'name': 'CAN_TCVR_TYPE_LS',
                'value': 1
            },
            {
                'name': 'CAN_TCVR_TYPE_SW',
                'value': 2
            },
            {
                'name': 'CAN_TCVR_TYPE_EXT',
                'value': 3
            },
            {
                'name': 'CAN_TCVR_TYPE_DISC',
                'value': 4
            },
            {
                'name': 'FLEX_RAY_SAMP_PER_MICRO_1',
                'value': 0
            },
            {
                'name': 'FLEX_RAY_SAMP_PER_MICRO_2',
                'value': 1
            },
            {
                'name': 'FLEX_RAY_SAMP_PER_MICRO_4',
                'value': 2
            },
            {
                'name': 'FLEX_RAY_TERM_OFF',
                'value': 0
            },
            {
                'name': 'FLEX_RAY_TERM_ON',
                'value': 1
            },
            {
                'name': 'LIN_SLEEP_REMOTE_SLEEP',
                'value': 0
            },
            {
                'name': 'LIN_SLEEP_REMOTE_WAKE',
                'value': 1
            },
            {
                'name': 'LIN_SLEEP_LOCAL_SLEEP',
                'value': 2
            },
            {
                'name': 'LIN_SLEEP_LOCAL_WAKE',
                'value': 3
            },
            {
                'name': 'LIN_TERM_OFF',
                'value': 0
            },
            {
                'name': 'LIN_TERM_ON',
                'value': 1
            },
            {
                'name': 'OUT_STRM_TIMNG_IMMEDIATE',
                'value': 0
            },
            {
                'name': 'OUT_STRM_TIMNG_REPLAY_EXCLUSIVE',
                'value': 1
            },
            {
                'name': 'OUT_STRM_TIMNG_REPLAY_INCLUSIVE',
                'value': 2
            },
            {
                'name': 'CAN_PEND_TX_ORDER_AS_SUBMITTED',
                'value': 0
            },
            {
                'name': 'CAN_PEND_TX_ORDER_BY_IDENTIFIER',
                'value': 1
            },
            {
                'name': 'FLEX_RAY_SLEEP_LOCAL_SLEEP',
                'value': 0
            },
            {
                'name': 'FLEX_RAY_SLEEP_LOCAL_WAKE',
                'value': 1
            },
            {
                'name': 'FLEX_RAY_SLEEP_REMOTE_WAKE',
                'value': 2
            },
            {
                'name': 'CAN_EXT_TCVR_CONFIG_NORMAL_SUPPORTED',
                'value': 4
            },
            {
                'name': 'CAN_EXT_TCVR_CONFIG_SLEEP_SUPPORTED',
                'value': 32
            },
            {
                'name': 'CAN_EXT_TCVR_CONFIG_SW_WAKEUP_SUPPORTED',
                'value': 256
            },
            {
                'name': 'CAN_EXT_TCVR_CONFIG_SW_HIGH_SPEED_SUPPORTED',
                'value': 2048
            },
            {
                'name': 'CAN_EXT_TCVR_CONFIG_POWER_ON_SUPPORTED',
                'value': 16384
            },
            {
                'name': 'CAN_EXT_TCVR_CONFIG_NORMAL_OUTPUT_0_SET',
                'value': 1
            },
            {
                'name': 'CAN_EXT_TCVR_CONFIG_SLEEP_OUTPUT_0_SET',
                'value': 8
            },
            {
                'name': 'CAN_EXT_TCVR_CONFIG_SW_WAKEUP_OUTPUT_0_SET',
                'value': 64
            },
            {
                'name': 'CAN_EXT_TCVR_CONFIG_SW_HIGH_SPEED_OUTPUT_0_SET',
                'value': 512
            },
            {
                'name': 'CAN_EXT_TCVR_CONFIG_POWER_ON_OUTPUT_0_SET',
                'value': 4096
            },
            {
                'name': 'CAN_EXT_TCVR_CONFIG_NORMAL_OUTPUT_1_SET',
                'value': 2
            },
            {
                'name': 'CAN_EXT_TCVR_CONFIG_SLEEP_OUTPUT_1_SET',
                'value': 16
            },
            {
                'name': 'CAN_EXT_TCVR_CONFIG_SW_WAKEUP_OUTPUT_1_SET',
                'value': 128
            },
            {
                'name': 'CAN_EXT_TCVR_CONFIG_SW_HIGH_SPEED_OUTPUT_1_SET',
                'value': 1024
            },
            {
                'name': 'CAN_EXT_TCVR_CONFIG_POWER_ON_OUTPUT_1_SET',
                'value': 8192
            },
            {
                'name': 'CAN_EXT_TCVR_CONFIG_N_ERR_CONNECTED',
                'value': 2147483648
            },
            {
                'name': 'ENET_PORT_MODE_DIRECT',
                'value': 0
            },
            {
                'name': 'ENET_PORT_MODE_TAP',
                'value': 1
            },
            {
                'name': 'ENET_PHY_STATE_SLAVE',
                'value': 0
            },
            {
                'name': 'ENET_PHY_STATE_MASTER',
                'value': 1
            },
            {
                'name': 'ENET_PHY_STATE_AUTO',
                'value': 2
            },
            {
                'name': 'ENET_LINK_SPEED_LINK_DOWN',
                'value': 0
            },
            {
                'name': 'ENET_LINK_SPEED_100_MBPS',
                'value': 1
            },
            {
                'name': 'ENET_LINK_SPEED_1000_MBPS',
                'value': 2
            },
            {
                'name': 'ENET_JUMBO_FRAMES_DISABLED',
                'value': 0
            },
            {
                'name': 'ENET_JUMBO_FRAMES_9018_BYTES',
                'value': 1
            },
            {
                'name': 'ENET_OPERATIONAL_STATUS_DOWN',
                'value': 0
            },
            {
                'name': 'ENET_OPERATIONAL_STATUS_UP',
                'value': 1
            },
            {
                'name': 'ENET_LOG_MODE_OFF',
                'value': 0
            },
            {
                'name': 'ENET_LOG_MODE_LOG',
                'value': 1
            },
            {
                'name': 'ENET_LOG_OPERATION_CREATE_OR_REPLACE',
                'value': 0
            },
            {
                'name': 'ENET_LOG_OPERATION_CREATE',
                'value': 1
            },
            {
                'name': 'ENET_TIME_PROTOCOL_IEEE_8021AS',
                'value': 0
            },
            {
                'name': 'ENET_TIME_CLK_ACCURACY_WITHIN_25NSEC',
                'value': 32
            },
            {
                'name': 'ENET_TIME_CLK_ACCURACY_WITHIN_100NSEC',
                'value': 33
            },
            {
                'name': 'ENET_TIME_CLK_ACCURACY_WITHIN_250NSEC',
                'value': 34
            },
            {
                'name': 'ENET_TIME_CLK_ACCURACY_WITHIN_1USEC',
                'value': 35
            },
            {
                'name': 'ENET_TIME_CLK_ACCURACY_WITHIN_2500NSEC',
                'value': 36
            },
            {
                'name': 'ENET_TIME_CLK_ACCURACY_WITHIN_10USEC',
                'value': 37
            },
            {
                'name': 'ENET_TIME_CLK_ACCURACY_WITHIN_25USEC',
                'value': 38
            },
            {
                'name': 'ENET_TIME_CLK_ACCURACY_WITHIN_100USEC',
                'value': 39
            },
            {
                'name': 'ENET_TIME_CLK_ACCURACY_WITHIN_250USEC',
                'value': 40
            },
            {
                'name': 'ENET_TIME_CLK_ACCURACY_WITHIN_1MSEC',
                'value': 41
            },
            {
                'name': 'ENET_TIME_CLK_ACCURACY_WITHIN_2500USEC',
                'value': 42
            },
            {
                'name': 'ENET_TIME_CLK_ACCURACY_WITHIN_10MSEC',
                'value': 43
            },
            {
                'name': 'ENET_TIME_CLK_ACCURACY_WITHIN_25MSEC',
                'value': 44
            },
            {
                'name': 'ENET_TIME_CLK_ACCURACY_WITHIN_100MSEC',
                'value': 45
            },
            {
                'name': 'ENET_TIME_CLK_ACCURACY_WITHIN_250MSEC',
                'value': 46
            },
            {
                'name': 'ENET_TIME_CLK_ACCURACY_WITHIN_1SEC',
                'value': 47
            },
            {
                'name': 'ENET_TIME_CLK_ACCURACY_WITHIN_10SEC',
                'value': 48
            },
            {
                'name': 'ENET_TIME_CLK_ACCURACY_GREATHER_THAN_10SEC',
                'value': 49
            },
            {
                'name': 'ENET_TIME_CLK_ACCURACY_UNKNOWN',
                'value': 254
            },
            {
                'name': 'ENET_TIME_PORT_SYNC_STATUS_SYNCED',
                'value': 0
            },
            {
                'name': 'ENET_TIME_PORT_SYNC_STATUS_ENET_LINK_DOWN',
                'value': 1
            },
            {
                'name': 'ENET_TIME_PORT_SYNC_STATUS_PROTOCOL_DISABLED',
                'value': 2
            },
            {
                'name': 'ENET_TIME_PORT_SYNC_STATUS_MEASURING_PROP_DELAY',
                'value': 3
            },
            {
                'name': 'ENET_TIME_PORT_SYNC_STATUS_MASTER_PENDING_ANNOUNCE',
                'value': 4
            },
            {
                'name': 'ENET_TIME_PORT_SYNC_STATUS_WAITING_FOR_MASTER',
                'value': 5
            },
            {
                'name': 'ENET_TIME_PORT_SYNC_STATUS_SYNCING_TO_MASTER',
                'value': 6
            },
            {
                'name': 'ENET_TIME_PORT_SYNC_STATUS_PEER_NOT_PROTO_CAPABLE',
                'value': 7
            },
            {
                'name': 'ENET_TIME_PORT_SYNC_STATUS_PROP_DELAY_EXCEEDS_TRESHOLD',
                'value': 8
            },
            {
                'name': 'ENET_TIME_PORT_SYNC_STATUS_SYNC_RECEIPT_TIMEOUT',
                'value': 9
            },
            {
                'name': 'ENET_TIME_PORT_SYNC_STATUS_FREQUENCY_OUT_OF_RANGE',
                'value': 10
            },
            {
                'name': 'ENET_TIME_PORT_SYNC_STATUS_SYNC_INTERVAL_OUT_OF_RANGE',
                'value': 11
            },
            {
                'name': 'ENET_TIME_PORT_SYNC_STATUS_MULTIPLE_MASTERS_DETECTED',
                'value': 12
            },
            {
                'name': 'ENET_TIME_PORT_STATE_DISABLED',
                'value': 3
            },
            {
                'name': 'ENET_TIME_PORT_STATE_MASTER',
                'value': 6
            },
            {
                'name': 'ENET_TIME_PORT_STATE_PASSIVE',
                'value': 7
            },
            {
                'name': 'ENET_TIME_PORT_STATE_SLAVE',
                'value': 9
            },
            {
                'name': 'ENET_TIME_P_DELAY_REQ_INTERVAL_125MS',
                'value': -3
            },
            {
                'name': 'ENET_TIME_P_DELAY_REQ_INTERVAL_250MS',
                'value': -2
            },
            {
                'name': 'ENET_TIME_P_DELAY_REQ_INTERVAL_500MS',
                'value': -1
            },
            {
                'name': 'ENET_TIME_P_DELAY_REQ_INTERVAL_1S',
                'value': 0
            },
            {
                'name': 'ENET_TIME_P_DELAY_REQ_INTERVAL_2S',
                'value': 1
            },
            {
                'name': 'ENET_TIME_SYNC_INTERVAL_125MS',
                'value': -3
            },
            {
                'name': 'ENET_TIME_SYNC_INTERVAL_250MS',
                'value': -2
            },
            {
                'name': 'ENET_TIME_SYNC_INTERVAL_500MS',
                'value': -1
            },
            {
                'name': 'ENET_TIME_SYNC_INTERVAL_1S',
                'value': 0
            },
            {
                'name': 'ENET_TIME_SYNC_INTERVAL_2S',
                'value': 1
            },
            {
                'name': 'ENET_TIME_ANNOUNCE_INTERVAL_125MS',
                'value': -3
            },
            {
                'name': 'ENET_TIME_ANNOUNCE_INTERVAL_250MS',
                'value': -2
            },
            {
                'name': 'ENET_TIME_ANNOUNCE_INTERVAL_500MS',
                'value': -1
            },
            {
                'name': 'ENET_TIME_ANNOUNCE_INTERVAL_1S',
                'value': 0
            },
            {
                'name': 'ENET_TIME_ANNOUNCE_INTERVAL_2S',
                'value': 1
            },
            {
                'name': 'ENET_SLEEP_CAPABILITY_DISABLED_OR_NOT_AVAILABLE',
                'value': 0
            },
            {
                'name': 'ENET_SLEEP_CAPABILITY_ENABLED',
                'value': 1
            },
            {
                'name': 'ENET_PHY_POWER_MODE_NORMAL',
                'value': 0
            },
            {
                'name': 'ENET_PHY_POWER_MODE_SLEEP',
                'value': 1
            }
        ]
    },
    'ReadState': {
        'values': [
            {
                'name': 'TIME_CURRENT',
                'value': 118685697
            },
            {
                'name': 'TIME_COMMUNICATING',
                'value': 118685698
            },
            {
                'name': 'TIME_START',
                'value': 118685699
            },
            {
                'name': 'SESSION_INFO',
                'value': 1245188
            },
            {
                'name': 'TIME_CURRENT_2',
                'value': 202571781
            },
            {
                'name': 'TIME_COMMUNICATING_2',
                'value': 202571782
            },
            {
                'name': 'TIME_START_2',
                'value': 202571783
            },
            {
                'name': 'CAN_COMM',
                'value': 1245200
            },
            {
                'name': 'FLEX_RAY_COMM',
                'value': 1245216
            },
            {
                'name': 'FLEX_RAY_STATS',
                'value': 135462945
            },
            {
                'name': 'LIN_COMM',
                'value': 1245232
            },
            {
                'name': 'J1939_COMM',
                'value': 1245248
            }
        ]
    },
    'SessionInfoState': {
        'force-include': True,
        'values': [
            {
                'name': 'STOPPED',
                'value': 0
            },
            {
                'name': 'STARTED',
                'value': 1
            },
            {
                'name': 'MIX',
                'value': 2
            }
        ]
    },
    'StartStopScope': {
        'values': [
            {
                'name': 'NORMAL',
                'value': 0
            },
            {
                'name': 'SESSION_ONLY',
                'value': 1
            },
            {
                'name': 'INTERFACE_ONLY',
                'value': 2
            },
            {
                'name': 'SESSION_ONLY_BLOCKING',
                'value': 3
            }
        ]
    },
    'SubProperty': {
        'generate-mapping-type': True,
        'values': [
            {
                'name': 'SESSION_SUB_CAN_START_TIME_OFF',
                'type': 'f64',
                'value': 17825921
            },
            {
                'name': 'SESSION_SUB_CAN_TX_TIME',
                'type': 'f64',
                'value': 17825922
            },
            {
                'name': 'SESSION_SUB_LIN_TX_N_CORRUPTED_CHKSUMS',
                'type': 'u32',
                'value': 1048709
            },
            {
                'name': 'SESSION_SUB_OUTPUT_QUEUE_UPDATE_FREQ',
                'type': 'u32',
                'value': 1048708
            },
            {
                'name': 'SESSION_SUB_J1939_ADDR_FILTER',
                'type': 'string',
                'value': 51380358
            },
            {
                'name': 'SESSION_SUB_SKIP_N_CYCLIC_FRAMES',
                'type': 'u32',
                'value': 1048707
            }
        ]
    },
    'SubPropertyValue': {
        'values': [
            {
                'name': 'FRM_FLEX_RAY_CH_ASSIGN_A',
                'value': 1
            },
            {
                'name': 'FRM_FLEX_RAY_CH_ASSIGN_B',
                'value': 2
            },
            {
                'name': 'FRM_FLEX_RAY_CH_ASSIGN_A_AND_B',
                'value': 3
            },
            {
                'name': 'FRM_FLEX_RAY_CH_ASSIGN_NONE',
                'value': 4
            },
            {
                'name': 'FRM_FLEX_RAY_TIMING_CYCLIC',
                'value': 0
            },
            {
                'name': 'FRM_FLEX_RAY_TIMING_EVENT',
                'value': 1
            },
            {
                'name': 'FRM_CAN_TIMING_CYCLIC_DATA',
                'value': 0
            },
            {
                'name': 'FRM_CAN_TIMING_EVENT_DATA',
                'value': 1
            },
            {
                'name': 'FRM_CAN_TIMING_CYCLIC_REMOTE',
                'value': 2
            },
            {
                'name': 'FRM_CAN_TIMING_EVENT_REMOTE',
                'value': 3
            },
            {
                'name': 'FRM_CAN_TIMING_CYCLIC_EVENT',
                'value': 4
            },
            {
                'name': 'FRM_LIN_CHECKSUM_CLASSIC',
                'value': 0
            },
            {
                'name': 'FRM_LIN_CHECKSUM_ENHANCED',
                'value': 1
            }
        ]
    },
    'TerminalName': {
        'generate-mappings': True,
        'values': [
            {
                'name': 'PXI_TRIG_0',
                'value': 'PXI_Trig0'
            },
            {
                'name': 'PXI_TRIG_1',
                'value': 'PXI_Trig1'
            },
            {
                'name': 'PXI_TRIG_2',
                'value': 'PXI_Trig2'
            },
            {
                'name': 'PXI_TRIG_3',
                'value': 'PXI_Trig3'
            },
            {
                'name': 'PXI_TRIG_4',
                'value': 'PXI_Trig4'
            },
            {
                'name': 'PXI_TRIG_5',
                'value': 'PXI_Trig5'
            },
            {
                'name': 'PXI_TRIG_6',
                'value': 'PXI_Trig6'
            },
            {
                'name': 'PXI_TRIG_7',
                'value': 'PXI_Trig7'
            },
            {
                'name': 'FRONT_PANEL_0',
                'value': 'FrontPanel0'
            },
            {
                'name': 'FRONT_PANEL_1',
                'value': 'FrontPanel1'
            },
            {
                'name': 'PXI_STAR',
                'value': 'PXI_Star'
            },
            {
                'name': 'PXI_CLK_10',
                'value': 'PXI_Clk10'
            },
            {
                'name': '10_MHZ_TIMEBASE',
                'value': '10MHzTimebase'
            },
            {
                'name': '1_MHZ_TIMEBASE',
                'value': '1MHzTimebase'
            },
            {
                'name': 'MASTER_TIMEBASE',
                'value': 'MasterTimebase'
            },
            {
                'name': 'COMM_TRIGGER',
                'value': 'CommTrigger'
            },
            {
                'name': 'START_TRIGGER',
                'value': 'StartTrigger'
            },
            {
                'name': 'FLEX_RAY_START_CYCLE',
                'value': 'FlexRayStartCycle'
            },
            {
                'name': 'FLEX_RAY_MACROTICK',
                'value': 'FlexRayMacrotick'
            },
            {
                'name': 'LOG_TRIGGER',
                'value': 'LogTrigger'
            },
            {
                'name': 'TIME_TRIGGER',
                'value': 'TimeTrigger'
            },
            {
                'name': 'NETWORK_TIME_PPS',
                'value': 'NetworkTimePPS'
            },
            {
                'name': 'NETWORK_TIME_1_MHZ',
                'value': 'NetworkTime1MHz'
            }
        ]
    },
    'TimeOut': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'INFINITE',
                'value': -1
            }
        ]
    },
    'TimeScale': {
        'values': [
            {
                'name': 'LOCAL_TIME',
                'value': 0
            },
            {
                'name': 'NETWORK_TIME',
                'value': 1
            }
        ]
    },
    'WaitCondition': {
        'values': [
            {
                'name': 'TRANSMIT_COMPLETE',
                'value': 32769
            },
            {
                'name': 'INTF_COMMUNICATING',
                'value': 32770
            },
            {
                'name': 'INTF_REMOTE_WAKEUP',
                'value': 32771
            },
            {
                'name': 'ETHERNET_SYNCED',
                'value': 32772
            }
        ]
    },
    'WriteState': {
        'values': [
            {
                'name': 'LIN_SCHEDULE_CHANGE',
                'value': 1245313
            },
            {
                'name': 'LIN_DIAGNOSTIC_SCHEDULE_CHANGE',
                'value': 1245315
            },
            {
                'name': 'FLEX_RAY_SYMBOL',
                'value': 1245314
            },
            {
                'name': 'ETHERNET_SLEEP',
                'value': 1245316
            },
            {
                'name': 'ETHERNET_WAKE',
                'value': 1245317
            }
        ]
    },
    'Protocol': {
        'force-include': True,
        'values': [
            {
                'name': 'CAN',
                'value': 1
            },
            {
                'name': 'LIN',
                'value': 2
            },
            {
                'name': 'FLEX_RAY',
                'value': 3
            },
            {
                'name': 'J1939',
                'value': 4
            },
            {
                'name': 'ENET',
                'value': 5
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nixnet/enums_addon.py sha256=3f7624b42cd1fdd7313b8af4877786ee007f2cacad4ae9936fc6cc665b2dfb87 bytes=556 -->
## FILE: source/codegen/metadata/nixnet/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nixnet/enums_addon.py`
- sha256: `3f7624b42cd1fdd7313b8af4877786ee007f2cacad4ae9936fc6cc665b2dfb87`
- bytes: 556

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}

enums_validation_suppressions = {
    "PropertyValue": ["ENUMS_SHOULD_NOT_HAVE_DUPLICATE_VALUES"],
    "DBPropertyValue": ["ENUMS_SHOULD_NOT_HAVE_DUPLICATE_VALUES"],
    "StateValue": ["ENUMS_SHOULD_NOT_HAVE_DUPLICATE_VALUES"],
    "SubPropertyValue": ["ENUMS_SHOULD_NOT_HAVE_DUPLICATE_VALUES"],
    "FrameFlags": ["ENUMS_SHOULD_NOT_HAVE_DUPLICATE_VALUES"]
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nixnet/functions.py sha256=8631a6740c2b82abd4d93523228f56fcdf4277e571d10f4af4430eae030bf3f6 bytes=54199 -->
## FILE: source/codegen/metadata/nixnet/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nixnet/functions.py`
- sha256: `8631a6740c2b82abd4d93523228f56fcdf4277e571d10f4af4430eae030bf3f6`
- bytes: 54199

````python
functions = {
    'Blink': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'interfaceRef',
                'type': 'nxSessionRef_t'
            },
            {
                'direction': 'in',
                'enum': 'BlinkMode',
                'name': 'modifier',
                'type': 'u32'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'Clear': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'ConnectTerminals': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'direction': 'in',
                'enum': 'TerminalName',
                'name': 'source',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'enum': 'TerminalName',
                'name': 'destination',
                'type': 'const char[]'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'ConvertByteArrayToFramesSinglePoint': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'direction': 'in',
                'name': 'valueBuffer',
                'size': {
                    'mechanism': 'len-in-bytes',
                    'value': 'sizeOfValueBuffer'
                },
                'type': 'u8[]'
            },
            {
                'direction': 'in',
                'name': 'sizeOfValueBuffer',
                'type': 'u32'
            },
            {
                'direction': 'in',
                'name': 'number_of_frames',
                'proto_only': True,
                'type': 'u32'
            },
            {
                'direction': 'in',
                'name': 'max_payload_per_frame',
                'proto_only': True,
                'type': 'u32',
            },
            {
                'direction': 'in',
                'name': 'protocol',
                'proto_only': True,
                'enum': 'Protocol',
                'type': 'u32'
            },
            {
                'direction': 'out',
                'name': 'buffer',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'sizeOfBuffer'
                },
                'type': 'u8[]',
                'grpc_type': 'repeated FrameBufferResponse',
                'supports_standard_copy_convert': True,
                'additional_arguments_to_copy_convert': ['number_of_bytes_returned', 'protocol', 'enetflags_output_map_']
            },
            {
                'direction': 'in',
                'name': 'sizeOfBuffer',
                'hardcoded_value': 'get_frame_buffer_size(number_of_frames, max_payload_per_frame, protocol)',
                'type': 'u32',
                'include_in_proto': False
            },
            {
                'direction': 'out',
                'name': 'numberOfBytesReturned',
                'type': 'u32',
                'include_in_proto': False
            }
        ],
        'returns': 'nxStatus_t'
    },
    'ConvertFramesToByteArraySinglePoint': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'direction': 'in',
                'name': 'frameBuffer',
                'type': 'u8',
                'pointer': True,
                'grpc_type': 'repeated FrameBufferRequest',
                'supports_standard_copy_convert': True,
                'additional_arguments_to_copy_convert': ['enetflags_input_map_']
            },
            {
                'direction': 'in',
                'name': 'numberOfBytesForFrames',
                'hardcoded_value': 'frame_buffer.size()',
                'type': 'u32',
                'include_in_proto': False
            },
            {
                'direction': 'out',
                'name': 'valueBuffer',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'sizeOfValueBuffer'
                },
                'type': 'u8[]'
            },
            {
                'direction': 'in',
                'name': 'sizeOfValueBuffer',
                'type': 'u32'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'ConvertFramesToSignalsSinglePoint': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'name': 'numberOfSignals',
                'direction': 'in',
                'type': 'u32',
                'proto_only': True
            },
            {
                'direction': 'in',
                'name': 'frameBuffer',
                'type': 'u8',
                'pointer': True,
                'grpc_type': 'repeated FrameBufferRequest',
                'supports_standard_copy_convert': True,
                'additional_arguments_to_copy_convert': ['enetflags_input_map_']
            },
            {
                'direction': 'in',
                'name': 'numberOfBytesForFrames',
                'hardcoded_value': 'frame_buffer.size()',
                'type': 'u32',
                'include_in_proto': False
            },
            {
                'direction': 'out',
                'name': 'valueBuffer',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfSignals'
                },
                'type': 'f64[]'
            },
            {
                'direction': 'in',
                'name': 'sizeOfValueBuffer',
                'include_in_proto': False,
                'hardcoded_value': 'number_of_signals * sizeof(f64)',
                'type': 'u32'
            },
            {
                'direction': 'out',
                'name': 'timestampBuffer',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfSignals'
                },
                'type': 'nxTimestamp100ns_t[]'
            },
            {
                'direction': 'in',
                'name': 'sizeOfTimestampBuffer',
                'include_in_proto': False,
                'hardcoded_value': 'number_of_signals * sizeof(f64)',
                'type': 'u32'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'ConvertSignalsToFramesSinglePoint': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'direction': 'in',
                'name': 'valueBuffer',
                'size': {
                    'mechanism': 'len-in-bytes',
                    'value': 'sizeOfValueBuffer'
                },
                'type': 'f64[]'
            },
            {
                'direction': 'in',
                'name': 'sizeOfValueBuffer',
                'type': 'u32'
            },
            {
                'direction': 'in',
                'name': 'number_of_frames',
                'proto_only': True,
                'type': 'u32'
            },
            {
                'direction': 'in',
                'name': 'max_payload_per_frame',
                'proto_only': True,
                'type': 'u32',
            },
            {
                'direction': 'in',
                'name': 'protocol',
                'proto_only': True,
                'enum': 'Protocol',
                'type': 'u32'
            },
            {
                'direction': 'out',
                'name': 'buffer',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'sizeOfBuffer'
                },
                'type': 'u8[]',
                'grpc_type': 'repeated FrameBufferResponse',
                'supports_standard_copy_convert': True,
                'additional_arguments_to_copy_convert': ['number_of_bytes_returned', 'protocol', 'enetflags_output_map_']
            },
            {
                'direction': 'in',
                'name': 'sizeOfBuffer',
                'hardcoded_value': 'get_frame_buffer_size(number_of_frames, max_payload_per_frame, protocol)',
                'type': 'u32',
                'include_in_proto': False
            },
            {
                'direction': 'out',
                'name': 'numberOfBytesReturned',
                'type': 'u32',
                'include_in_proto': False
            }
        ],
        'returns': 'nxStatus_t'
    },
    'ConvertTimestamp100nsTo1ns': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'from_timestamp_100ns',
                'type': 'nxTimestamp100ns_t'
            },
            {
                'direction': 'out',
                'name': 'to_timestamp_1ns',
                'type': 'nxTimestamp1ns_t'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'ConvertTimestamp1nsTo100ns': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'from_timestamp_1ns',
                'type': 'nxTimestamp1ns_t'
            },
            {
                'direction': 'out',
                'name': 'to_timestamp_100ns',
                'type': 'nxTimestamp100ns_t'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'CreateSession': {
        'init_method': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'databaseName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'clusterName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'list',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'grpc_name': 'interface_name',
                'name': 'interface',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'enum': 'CreateSessionMode',
                'name': 'mode',
                'type': 'u32'
            },
            {
                'direction': 'out',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'int32'
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
        'returns': 'nxStatus_t'
    },
    'CreateSessionByRef': {
        'init_method': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'numberOfDatabaseRef',
                'type': 'u32'
            },
            {
                'direction': 'in',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfDatabaseRef'
                },
                'name': 'arrayOfDatabaseRef',
                'type': 'nxDatabaseRef_t[]'
            },
            {
                'direction': 'in',
                'grpc_name': 'interface_name',
                'name': 'interface',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'enum': 'CreateSessionMode',
                'name': 'mode',
                'type': 'u32'
            },
            {
                'direction': 'out',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'int32'
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
        'returns': 'nxStatus_t'
    },
    'DbAddAlias': {
        'cname': 'nxdbAddAlias',
        'parameters': [
            {
                'direction': 'in',
                'name': 'databaseAlias',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'databaseFilepath',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'defaultBaudRate',
                'type': 'u32'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'DbAddAlias64': {
        'cname': 'nxdbAddAlias64',
        'parameters': [
            {
                'direction': 'in',
                'name': 'databaseAlias',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'databaseFilepath',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'defaultBaudRate',
                'type': 'u64'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'DbCloseDatabase': {
        'cname': 'nxdbCloseDatabase',
        'custom_close_method': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'database',
                'type': 'nxDatabaseRef_t'
            },
            {
                'direction': 'in',
                'name': 'closeAllRefs',
                'type': 'u32'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'DbCreateObject': {
        'cname': 'nxdbCreateObject',
        'init_method': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'parentObject',
                'type': 'nxDatabaseRef_t'
            },
            {
                'direction': 'in',
                'name': 'objectClass',
                'type': 'u32'
            },
            {
                'direction': 'in',
                'name': 'objectName',
                'type': 'const char[]'
            },
            {
                'cross_driver_session': 'nxDatabaseRef_t',
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'dbObject',
                'type': 'nxDatabaseRef_t'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'DbDeleteObject': {
        'cname': 'nxdbDeleteObject',
        'custom_close_method': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'dbObject',
                'type': 'nxDatabaseRef_t'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'DbDeploy': {
        'cname': 'nxdbDeploy',
        'parameters': [
            {
                'direction': 'in',
                'name': 'ipAddress',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'databaseAlias',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'waitForComplete',
                'type': 'u32'
            },
            {
                'direction': 'out',
                'name': 'percentComplete',
                'type': 'u32'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'DbFindObject': {
        'cname': 'nxdbFindObject',
        'init_method': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'parentObject',
                'type': 'nxDatabaseRef_t'
            },
            {
                'direction': 'in',
                'name': 'objectClass',
                'type': 'u32'
            },
            {
                'direction': 'in',
                'name': 'objectName',
                'type': 'const char[]'
            },
            {
                'cross_driver_session': 'nxDatabaseRef_t',
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'dbObject',
                'type': 'nxDatabaseRef_t'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'DbGetDBCAttribute': {
        'cname': 'nxdbGetDBCAttribute',
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'direction': 'in',
                'name': 'dbObject',
                'type': 'nxDatabaseRef_t'
            },
            {
                'direction': 'in',
                'enum': 'GetDBCAttributeMode',
                'name': 'mode',
                'type': 'u32'
            },
            {
                'direction': 'in',
                'name': 'attributeName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'include_in_proto': False,
                'name': 'attributeTextSize',
                'type': 'u32'
            },
            {
                'direction': 'out',
                'name': 'attributeText',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'attributeTextSize'
                },
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'isDefault',
                'type': 'u32'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'DbGetDBCAttributeSize': {
        'cname': 'nxdbGetDBCAttributeSize',
        'parameters': [
            {
                'direction': 'in',
                'name': 'dbObject',
                'type': 'nxDatabaseRef_t'
            },
            {
                'direction': 'in',
                'enum': 'GetDBCAttributeMode',
                'name': 'mode',
                'type': 'u32'
            },
            {
                'direction': 'in',
                'name': 'attributeName',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'attributeTextSize',
                'type': 'u32'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'DbGetDatabaseList': {
        'cname': 'nxdbGetDatabaseList',
        'codegen_method': 'CustomCode',
        'include_in_client': False,
        'parameters': [
            {
                'direction': 'in',
                'name': 'ipAddress',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'sizeofAliasBuffer',
                'type': 'u32',
                'include_in_proto': False
            },
            {
                'direction': 'out',
                'name': 'aliasBuffer',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'sizeofAliasBuffer'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'sizeofFilepathBuffer',
                'type': 'u32',
                'include_in_proto': False
            },
            {
                'direction': 'out',
                'name': 'filepathBuffer',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'sizeofFilepathBuffer'
                },
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'numberOfDatabases',
                'type': 'u32'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'DbGetDatabaseListSizes': {
        'cname': 'nxdbGetDatabaseListSizes',
        'parameters': [
            {
                'direction': 'in',
                'name': 'ipAddress',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'sizeofAliasBuffer',
                'type': 'u32'
            },
            {
                'direction': 'out',
                'name': 'sizeofFilepathBuffer',
                'type': 'u32'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'DbGetProperty': {
        'cname': 'nxdbGetProperty',
        'codegen_method': 'CustomCodeCustomProtoMessage',
        'include_in_client': False,
        'parameters': [
            {
                'direction': 'in',
                'name': 'dbObject',
                'type': 'nxDatabaseRef_t'
            },
            {
                'direction': 'in',
                'enum': 'DBProperty',
                'name': 'propertyID',
                'type': 'u32'
            },
            {
                'direction': 'in',
                'include_in_proto': False,
                'name': 'propertySize',
                'type': 'u32'
            },
            {
                'direction': 'out',
                'enum': 'DBPropertyValue',
                'size': {
                    'mechanism': 'custom-code',
                    'value': ''
                },
                'name': 'propertyValue',
                'type': 'void *'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'DbGetPropertySize': {
        'cname': 'nxdbGetPropertySize',
        'parameters': [
            {
                'direction': 'in',
                'name': 'dbObject',
                'type': 'nxDatabaseRef_t'
            },
            {
                'direction': 'in',
                'enum': 'DBProperty',
                'name': 'propertyID',
                'type': 'u32'
            },
            {
                'direction': 'out',
                'name': 'propertySize',
                'type': 'u32'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'DbMerge': {
        'cname': 'nxdbMerge',
        'parameters': [
            {
                'direction': 'in',
                'name': 'targetCluster',
                'type': 'nxDatabaseRef_t'
            },
            {
                'direction': 'in',
                'name': 'sourceObj',
                'type': 'nxDatabaseRef_t'
            },
            {
                'direction': 'in',
                'enum': 'CopyMode',
                'name': 'copyMode',
                'type': 'u32'
            },
            {
                'direction': 'in',
                'name': 'prefix',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'waitForComplete',
                'type': 'u32'
            },
            {
                'direction': 'out',
                'name': 'percentComplete',
                'type': 'u32'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'DbOpenDatabase': {
        'cname': 'nxdbOpenDatabase',
        'custom_close': 'DbCloseDatabase(id, false)',
        'init_method': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'databaseName',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'database',
                'type': 'nxDatabaseRef_t'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'int32'
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
        'returns': 'nxStatus_t'
    },
    'DbRemoveAlias': {
        'cname': 'nxdbRemoveAlias',
        'parameters': [
            {
                'direction': 'in',
                'name': 'databaseAlias',
                'type': 'const char[]'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'DbSaveDatabase': {
        'cname': 'nxdbSaveDatabase',
        'parameters': [
            {
                'direction': 'in',
                'name': 'database',
                'type': 'nxDatabaseRef_t'
            },
            {
                'direction': 'in',
                'name': 'dbFilepath',
                'type': 'const char[]'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'DbSetProperty': {
        'cname': 'nxdbSetProperty',
        'codegen_method': 'CustomCodeCustomProtoMessage',
        'include_in_client': False,
        'parameters': [
            {
                'direction': 'in',
                'name': 'dbObject',
                'type': 'nxDatabaseRef_t'
            },
            {
                'direction': 'in',
                'enum': 'DBProperty',
                'name': 'propertyID',
                'type': 'u32'
            },
            {
                'direction': 'in',
                'include_in_proto': False,
                'name': 'propertySize',
                'type': 'u32'
            },
            {
                'direction': 'in',
                'name': 'propertyValue',
                'size': {
                    'mechanism': 'len-in-bytes',
                    'value': 'propertySize'
                },
                'type': 'void *'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'DbUndeploy': {
        'cname': 'nxdbUndeploy',
        'parameters': [
            {
                'direction': 'in',
                'name': 'ipAddress',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'databaseAlias',
                'type': 'const char[]'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'DisconnectTerminals': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'direction': 'in',
                'enum': 'TerminalName',
                'name': 'source',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'enum': 'TerminalName',
                'name': 'destination',
                'type': 'const char[]'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'Flush': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'FutureTimeTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'direction': 'in',
                'name': 'when',
                'type': 'nxTimestamp1ns_t'
            },
            {
                'direction': 'in',
                'enum': 'TimeScale',
                'name': 'timescale',
                'type': 'u32'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'GetProperty': {
        'codegen_method': 'CustomCodeCustomProtoMessage',
        'include_in_client': False,
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'direction': 'in',
                'enum': 'Property',
                'name': 'propertyID',
                'type': 'u32'
            },
            {
                'include_in_proto': False,
                'direction': 'in',
                'name': 'propertySize',
                'type': 'u32'
            },
            {
                'direction': 'out',
                'enum': 'PropertyValue',
                'name': 'propertyValue',
                'size': {
                    'mechanism': 'custom-code',
                    'value': ''
                },
                'type': 'void *'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'GetPropertySize': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'direction': 'in',
                'enum': 'Property',
                'name': 'propertyID',
                'type': 'u32'
            },
            {
                'direction': 'out',
                'name': 'propertySize',
                'type': 'u32'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'GetSubProperty': {
        'codegen_method': 'CustomCodeCustomProtoMessage',
        'include_in_client': False,
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'direction': 'in',
                'name': 'activeIndex',
                'type': 'u32'
            },
            {
                'direction': 'in',
                'enum': 'SubProperty',
                'name': 'propertyID',
                'type': 'u32'
            },
            {
                'direction': 'in',
                'include_in_proto': False,
                'name': 'propertySize',
                'type': 'u32'
            },
            {
                'direction': 'out',
                'enum': 'SubPropertyValue',
                'size': {
                    'mechanism': 'custom-code',
                    'value': ''
                },
                'name': 'propertyValue',
                'type': 'void *'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'GetSubPropertySize': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'direction': 'in',
                'name': 'activeIndex',
                'type': 'u32'
            },
            {
                'direction': 'in',
                'enum': 'SubProperty',
                'name': 'propertyID',
                'type': 'u32'
            },
            {
                'direction': 'out',
                'name': 'propertySize',
                'type': 'u32'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'ReadFrame': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'direction': 'in',
                'name': 'number_of_frames',
                'proto_only': True,
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'max_payload_per_frame',
                'proto_only': True,
                'type': 'u32',
            },
            {
                'direction': 'in',
                'name': 'protocol',
                'proto_only': True,
                'enum': 'Protocol',
                'type': 'u32'
            },
            {
                'direction': 'out',
                'name': 'buffer',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'sizeOfBuffer'
                },
                'type': 'u8[]',
                'grpc_type': 'repeated FrameBufferResponse',
                'supports_standard_copy_convert': True,
                'additional_arguments_to_copy_convert': ['number_of_bytes_returned', 'protocol', 'enetflags_output_map_']
            },
            {
                'direction': 'in',
                'name': 'sizeOfBuffer',
                'hardcoded_value': 'get_frame_buffer_size(number_of_frames, max_payload_per_frame, protocol)',
                'type': 'u32',
                'include_in_proto': False
            },
            {
                'direction': 'in',
                'enum': 'TimeOut',
                'name': 'timeout',
                'type': 'f64'
            },
            {
                'direction': 'out',
                'name': 'numberOfBytesReturned',
                'type': 'u32',
                'include_in_proto': False
            }
        ],
        'returns': 'nxStatus_t'
    },
    'ReadSignalSinglePoint': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'direction': 'in',
                'name': 'numberOfSignals',
                'type': 'u32',
                'proto_only': True
            },
            {
                'direction': 'out',
                'name': 'valueBuffer',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfSignals'
                },
                'type': 'f64[]'
            },
            {
                'direction': 'in',
                'include_in_proto': False,
                'name': 'sizeOfValueBuffer',
                'hardcoded_value': 'number_of_signals * sizeof(f64)',
                'type': 'u32'
            },
            {
                'direction': 'out',
                'name': 'timestampBuffer',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfSignals'
                },
                'type': 'nxTimestamp100ns_t[]'
            },
            {
                'direction': 'in',
                'name': 'sizeOfTimestampBuffer',
                'include_in_proto': False,
                'hardcoded_value': 'number_of_signals * sizeof(f64)',
                'type': 'u32'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'ReadSignalWaveform': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'direction': 'in',
                'enum': 'TimeOut',
                'name': 'timeout',
                'type': 'f64'
            },
            {
                'direction': 'in',
                'name': 'samplesPerSignal',
                'type': 'u32',
                'proto_only': True
            },
            {
                'direction': 'in',
                'name': 'numberOfSignals',
                'type': 'u32',
                'proto_only': True
            },
            {
                'direction': 'out',
                'name': 'startTime',
                'type': 'nxTimestamp100ns_t'
            },
            {
                'direction': 'out',
                'name': 'deltaTime',
                'type': 'f64'
            },
            {
                'direction': 'out',
                'name': 'valueBuffer',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'samples_per_signal * number_of_signals'
                },
                'type': 'f64[]',
                'supports_standard_copy_convert': True,
                'additional_arguments_to_copy_convert': ['number_of_values_returned', 'number_of_signals']
            },
            {
                'direction': 'in',
                'include_in_proto': False,
                'hardcoded_value': 'samples_per_signal * number_of_signals * sizeof(f64)',
                'name': 'sizeOfValueBuffer',
                'type': 'u32'
            },
            {
                'direction': 'out',
                'name': 'numberOfValuesReturned',
                'include_in_proto': False,
                'type': 'u32'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'ReadSignalXY': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'direction': 'in',
                'name': 'timeLimit',
                'pointer': True,
                'input_passed_by_ptr': True,
                'type': 'nxTimestamp100ns_t'
            },
            {
                'direction': 'in',
                'name': 'samplesPerSignal',
                'type': 'u32',
                'proto_only': True
            },
            {
                'direction': 'in',
                'name': 'numberOfSignals',
                'type': 'u32',
                'proto_only': True
            },
            {
                'direction': 'out',
                'name': 'valueBuffer',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'samples_per_signal * number_of_signals'
                },
                'type': 'f64[]'
            },
            {
                'direction': 'in',
                'include_in_proto': False,
                'hardcoded_value': 'samples_per_signal * number_of_signals * sizeof(f64)',
                'name': 'sizeOfValueBuffer',
                'type': 'u32'
            },
            {
                'direction': 'out',
                'name': 'timestampBuffer',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'samples_per_signal * number_of_signals'
                },
                'type': 'nxTimestamp100ns_t[]'
            },
            {
                'direction': 'in',
                'include_in_proto': False,
                'name': 'sizeOfTimestampBuffer',
                'hardcoded_value': 'samples_per_signal * number_of_signals * sizeof(f64)',
                'type': 'u32'
            },
            {
                'direction': 'out',
                'name': 'numPairsBuffer',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfSignals'
                },
                'type': 'u32[]'
            },
            {
                'direction': 'in',
                'name': 'sizeOfNumPairsBuffer',
                'include_in_proto': False,
                'hardcoded_value': 'number_of_signals * sizeof(u32)',
                'type': 'u32'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'ReadState': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'direction': 'in',
                'enum': 'ReadState',
                'name': 'stateID',
                'type': 'u32'
            },
            {
                'direction': 'in',
                'name': 'stateSize',
                'type': 'u32',
                'include_in_proto': False
            },
            {
                'direction': 'out',
                'name': 'stateValue',
                'type': 'void *',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'stateSize'
                },
                'grpc_type' : 'ReadStateValue'
            },
            {
                'direction': 'out',
                'name': 'fault',
                'type': 'nxStatus_t'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'ReadStateTimeTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'direction': 'in',
                'enum': 'TimeOut',
                'name': 'timeout',
                'type': 'f64'
            },
            {
                'direction': 'in',
                'name': 'stateSize',
                'type': 'u32',
                'hardcoded_value': 'sizeof(nxTimeLocalNetwork_t)',
                'include_in_proto': False
            },
            {
                'direction': 'out',
                'name': 'stateValue',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'stateSize'
                },
                'type': 'struct _nxTimeLocalNetwork_t',
                'grpc_type' : 'TimeLocalNetwork'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'SetProperty': {
        'codegen_method': 'CustomCodeCustomProtoMessage',
        'include_in_client': False,
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'direction': 'in',
                'enum': 'Property',
                'name': 'propertyID',
                'type': 'u32'
            },
            {
                'direction': 'in',
                'include_in_proto': False,
                'name': 'propertySize',
                'type': 'u32'
            },
            {
                'direction': 'in',
                'enum': 'PropertyValue',
                'size': {
                    'mechanism': 'len',
                    'value': 'propertySize'
                },
                'name': 'propertyValue',
                'type': 'void *'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'SetSubProperty': {
        'codegen_method': 'CustomCodeCustomProtoMessage',
        'include_in_client': False,
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'direction': 'in',
                'name': 'activeIndex',
                'type': 'u32'
            },
            {
                'direction': 'in',
                'enum': 'SubProperty',
                'name': 'propertyID',
                'type': 'u32'
            },
            {
                'direction': 'in',
                'include_in_proto': False,
                'name': 'propertySize',
                'type': 'u32'
            },
            {
                'direction': 'in',
                'name': 'propertyValue',
                'enum': 'SubPropertyValue',
                'size': {
                    'mechanism': 'len',
                    'value': 'propertySize'
                },
                'type': 'void *'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'Start': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'direction': 'in',
                'enum': 'StartStopScope',
                'name': 'scope',
                'type': 'u32'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'StatusToString': {
        'status_expression' : '0',
        'parameters': [
            {
                'direction': 'in',
                'name': 'statusID',
                'type': 'nxStatus_t'
            },
            {
                'direction': 'in',
                'include_in_proto': False,
                'hardcoded_value': '2048U',
                'name': 'sizeofString',
                'type': 'u32'
            },
            {
                'direction': 'out',
                'name': 'statusDescription',
                'size': {
                    'mechanism': 'fixed',
                    'value': 2048
                },
                'type': 'char[]'
            }
        ],
        'returns': 'void'
    },
    'Stop': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'direction': 'in',
                'enum': 'StartStopScope',
                'name': 'scope',
                'type': 'u32'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'SystemClose': {
        'custom_close_method': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'system',
                'type': 'nxSessionRef_t'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'SystemOpen': {
        'custom_close': 'SystemClose(id)',
        'init_method': True,
        'parameters': [
            {
                'direction': 'out',
                'name': 'system',
                'type': 'nxSessionRef_t'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'int32'
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
        'returns': 'nxStatus_t'
    },
    'Wait': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'direction': 'in',
                'enum': 'WaitCondition',
                'name': 'condition',
                'type': 'u32'
            },
            {
                'direction': 'in',
                'name': 'paramIn',
                'type': 'u32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'f64'
            },
            {
                'direction': 'out',
                'name': 'paramOut',
                'type': 'u32'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'WriteFrame': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'direction': 'in',
                'name': 'buffer',
                'type': 'u8',
                'pointer': True,
                'grpc_type': 'repeated FrameBufferRequest',
                'supports_standard_copy_convert': True,
                'additional_arguments_to_copy_convert': ['enetflags_input_map_']
            },
            {
                'direction': 'in',
                'name': 'numberOfBytesForFrames',
                'hardcoded_value': 'buffer.size()',
                'type': 'u32',
                'include_in_proto': False
            },
            {
                'direction': 'in',
                'enum': 'TimeOut',
                'name': 'timeout',
                'type': 'f64'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'WriteSignalSinglePoint': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'direction': 'in',
                'name': 'valueBuffer',
                'size': {
                    'mechanism': 'len-in-bytes',
                    'value': 'sizeOfValueBuffer'
                },
                'type': 'f64[]'
            },
            {
                'direction': 'in',
                'name': 'sizeOfValueBuffer',
                'type': 'u32'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'WriteSignalWaveform': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'direction': 'in',
                'enum': 'TimeOut',
                'name': 'timeout',
                'type': 'f64'
            },
            {
                'direction': 'in',
                'name': 'valueBuffer',
                'size': {
                    'mechanism': 'len-in-bytes',
                    'value': 'sizeOfValueBuffer'
                },
                'type': 'f64[]'
            },
            {
                'direction': 'in',
                'name': 'sizeOfValueBuffer',
                'type': 'u32'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'WriteSignalXY': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'direction': 'in',
                'enum': 'TimeOut',
                'name': 'timeout',
                'type': 'f64'
            },
            {
                'direction': 'in',
                'name': 'valueBuffer',
                'size': {
                    'mechanism': 'len-in-bytes',
                    'value': 'sizeOfValueBuffer'
                },
                'type': 'f64[]'
            },
            {
                'direction': 'in',
                'name': 'sizeOfValueBuffer',
                'type': 'u32'
            },
            {
                'direction': 'in',
                'name': 'timestampBuffer',
                'size': {
                    'mechanism': 'len-in-bytes',
                    'value': 'sizeOfTimestampBuffer'
                },
                'type': 'nxTimestamp100ns_t[]'
            },
            {
                'direction': 'in',
                'name': 'sizeOfTimestampBuffer',
                'type': 'u32'
            },
            {
                'direction': 'in',
                'name': 'numPairsBuffer',
                'size': {
                    'mechanism': 'len-in-bytes',
                    'value': 'sizeOfNumPairsBuffer'
                },
                'type': 'u32[]'
            },
            {
                'direction': 'in',
                'name': 'sizeOfNumPairsBuffer',
                'type': 'u32'
            }
        ],
        'returns': 'nxStatus_t'
    },
    'WriteState': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nxSessionRef_t'
            },
            {
                'direction': 'in',
                'enum': 'WriteState',
                'name': 'stateID',
                'type': 'u32'
            },
            {
                'direction': 'in',
                'name': 'stateSize',
                'type': 'u32'
            },
            {
                'direction': 'in',
                'name': 'stateValue',
                'size': {
                    'mechanism': 'len-in-bytes',
                    'value': 'stateSize'
                },
                'type': 'void *',
                'grpc_type' : 'WriteStateValue'
            }
        ],
        'returns': 'nxStatus_t'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nixnet/functions_addon.py sha256=ceef314306e111183d1709307b9c107416f8968ce2cddcb9a8f63ad136887314 bytes=239 -->
## FILE: source/codegen/metadata/nixnet/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nixnet/functions_addon.py`
- sha256: `ceef314306e111183d1709307b9c107416f8968ce2cddcb9a8f63ad136887314`
- bytes: 239

````python
# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nixnetsocket/__init__.py sha256=952a0d82b5c67b27eeaf8e0816eabd4873f9b98fd229321d326c96b674efc2ba bytes=513 -->
## FILE: source/codegen/metadata/nixnetsocket/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nixnetsocket/__init__.py`
- sha256: `952a0d82b5c67b27eeaf8e0816eabd4873f9b98fd229321d326c96b674efc2ba`
- bytes: 513

````python
from .functions import functions
from .functions_addon import functions_validation_suppressions
from .attributes import attributes
from .enums_addon import enums_validation_suppressions
from .enums import enums
from .config import config

metadata = {
    "functions": functions,
    "functions_validation_suppressions": functions_validation_suppressions,
    "attributes": attributes,
    "enums": enums,
    "enums_validation_suppressions": enums_validation_suppressions,
    "config": config,
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nixnetsocket/attributes.py sha256=e9075ea450a8e6e7fe87996b579a158386973d65dbf4b8df93a880099d15b50a bytes=17 -->
## FILE: source/codegen/metadata/nixnetsocket/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nixnetsocket/attributes.py`
- sha256: `e9075ea450a8e6e7fe87996b579a158386973d65dbf4b8df93a880099d15b50a`
- bytes: 17

````python
attributes = {}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nixnetsocket/attributes_addon.py sha256=cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f bytes=207 -->
## FILE: source/codegen/metadata/nixnetsocket/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nixnetsocket/attributes_addon.py`
- sha256: `cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f`
- bytes: 207

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nixnetsocket/config.py sha256=44b4d4dc1ab23db060f7416c316a95b4fb1cc1b31c9107973b754025609ad3ae bytes=2479 -->
## FILE: source/codegen/metadata/nixnetsocket/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nixnetsocket/config.py`
- sha256: `44b4d4dc1ab23db060f7416c316a95b4fb1cc1b31c9107973b754025609ad3ae`
- bytes: 2479

````python
# -*- coding: utf-8 -*-
config = {
    'api_version': '21.8.0',
    'c_header': 'nxsocket.h',
    'c_function_prefix': 'nx',
    'service_class_prefix': 'NiXnetSocket',
    'java_package': 'com.ni.grpc.xnetsocket',
    'csharp_namespace': 'NationalInstruments.Grpc.NiXnetSocket',
    'namespace_component': 'nixnetsocket',
    'close_function': 'Close',
    'custom_types': [],
    'additional_headers': { 
        "custom/xnetsocket_converters.h": ["service.cpp"],
        "custom/xnetsocket_errors.h": ["service.cpp"],
        "custom/xnetsocket_aliases.h": ["library_interface.h"] 
    },
    'get_last_error': [
        {
            'name': 'error_message',
            'type': 'char[]'
        }, 
        {
            'name': 'error_num', 
            'type': 'int32_t'
        }
    ],
    'type_to_grpc_type': {
        'nxSOCKET': 'nidevice_grpc.Session',
        'nxfd_set': 'repeated nidevice_grpc.Session',
        'nxIpStackRef_t': 'nidevice_grpc.Session',
        'char[]': 'string',
        'int32_t': 'int32',
        'void*': 'bytes',
        'int': 'int32',
        'nxsocklen_t': 'int32',
        'size_t': 'uint64',
        'uint32_t': 'uint32',
        'uint16_t': 'uint16',
        'int64_t': 'int64',
        'nxaddrinfo': 'repeated AddrInfo',
        'nxlinger': 'Linger',
        'nxsockaddr': 'SockAddr',
        'nxtimeval': 'google.protobuf.Duration',
        'nxVirtualInterface_t': 'repeated VirtualInterface',
        'nixnetsocket_grpc::IpStackInfoString': 'string'
    },
    'code_readiness': 'Release',
    'driver_name': 'NI-XNETSOCKET',
    'extra_errors_used': [
    ],
    'init_function': 'Socket',
    'resource_handle_type': ['nxSOCKET', 'nxIpStackRef_t'],
    'status_ok': 'status >= 0',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nixntipstack',
                'type': 'cdll',
                'abi_version': '1'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'nixntipstack.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'nixntipstack.dll',
                'type': 'cdll'
            }
        }
    },
    'linux_rt_support': True,
    'metadata_version': '0.1',
    'module_name': 'nixnetsocket',
    'session_class_description': 'An NI-XNET ethernet socket',
    'session_handle_parameter_name': 'socket'
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nixnetsocket/config_addon.py sha256=b7926e5e93e1fe91f1c439d0bd8730cb336d31f8601a1da7a7a0f79ba29dc4b6 bytes=133 -->
## FILE: source/codegen/metadata/nixnetsocket/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nixnetsocket/config_addon.py`
- sha256: `b7926e5e93e1fe91f1c439d0bd8730cb336d31f8601a1da7a7a0f79ba29dc4b6`
- bytes: 133

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nixnetsocket/custom_proto.mako sha256=79849fd53b8dc5a06d30ea175c156422a231bf1b5045c31826931acd92d6794c bytes=1846 -->
## FILE: source/codegen/metadata/nixnetsocket/custom_proto.mako

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nixnetsocket/custom_proto.mako`
- sha256: `79849fd53b8dc5a06d30ea175c156422a231bf1b5045c31826931acd92d6794c`
- bytes: 1846

````mako
message IPAddress {
  AddressFamily family = 1;
  string address = 2;
  string net_mask = 3;
  uint32 prefix_length = 4;
}

message GatewayAddress {
  AddressFamily family = 1;
  string address = 2;
}

message VirtualInterface {
  string xnet_interface_name = 1;
  string vlan_name = 2;
  string mac_address = 3;
  uint32 mac_mtu = 4;
  OperationalStatus operational_status = 5;
  uint32 if_index = 6;
  repeated IPAddress ip_addresses = 7;
  repeated GatewayAddress gateway_addresses = 8;
}

message InAddr {
  uint32 addr = 1;
}

message In6Addr {
  bytes addr = 1;
}

message Addr {
  oneof addr {
    InAddr ipv4 = 1;
    In6Addr ipv6 = 2;
  }
}

message SockAddrIn {
  uint32 port = 1;
  InAddr addr = 2;
}

message SockAddrIn6 {
  uint32 port = 1;
  uint32 flowinfo = 2;
  In6Addr addr = 3;
  uint32 scope_id = 4;
}

message SockAddr {
  oneof addr {
    SockAddrIn ipv4 = 1;
    SockAddrIn6 ipv6 = 2;
  }
}

message AddrInfo {
  repeated GetAddrInfoFlags flags_array = 1;
  int32 flags_raw = 2;
  AddressFamily family = 3;
  SocketProtocolType sock_type = 4;
  IPProtocol protocol = 5;
  SockAddr addr = 6;
  string canon_name = 7;
}

message AddrInfoHint {
  repeated GetAddrInfoFlags flags_array = 1;
  int32 flags_raw = 2;
  AddressFamily family = 3;
  SocketProtocolType sock_type = 4;
  IPProtocol protocol = 5;
}

message Linger {
  int32 onoff = 1;
  int32 linger = 2;
}

message IPMReq {
  InAddr multiaddr = 1;
  InAddr imr_interface = 2;
}

message IPv6MReq {
  In6Addr multiaddr = 1;
  int32 ipv6mr_interface = 2;
}

message SockOptData {
  oneof data {
    int32 data_int32 = 1;
    bool data_bool = 2;
    string data_string = 3;
    Linger data_linger = 4;
    IPMReq data_ip_mreq = 5;
    IPv6MReq data_ipv6_mreq = 6;
  }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nixnetsocket/enums.py sha256=a1659735e7129a5fc59ce787bf7a6ea13bf5d1d99fa9cddab35d74cd21c9818a bytes=6574 -->
## FILE: source/codegen/metadata/nixnetsocket/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nixnetsocket/enums.py`
- sha256: `a1659735e7129a5fc59ce787bf7a6ea13bf5d1d99fa9cddab35d74cd21c9818a`
- bytes: 6574

````python
enums = {
    'AddressFamily': {
        'values': [
            {
                'name': 'INET',
                'value': 2
            },
            {
                'name': 'INET6',
                'value': 10
            }
        ]
    },
    'GetAddrInfoFlags': {
        'force-include': True,
        'values': [
            {
                'name': 'PASSIVE',
                'value': 1
            },
            {
                'name': 'CANONNAME',
                'value': 2
            },
            {
                'name': 'NUMERICHOST',
                'value': 4
            },
            {
                'name': 'NUMERICSERV',
                'value': 8
            },
            {
                'name': 'V4MAPPED',
                'value': 16
            },
            {
                'name': 'ALL',
                'value': 32
            },
            {
                'name': 'ADDRCONFIG',
                'value': 64
            },
            {
                'name': 'LOCALQUERY',
                'value': 128
            },
            {
                'name': 'PREFER_V4',
                'value': 256
            },
            {
                'name': 'UNICAST_REPLY',
                'value': 512
            },
            {
                'name': 'SHARED_RRSET',
                'value': 1024
            },
            {
                'name': 'BYPASS_CACHE',
                'value': 2048
            }
        ]
    },
    'GetNameInfoFlags': {
        'values': [
            {
                'name': 'NOFQDN',
                'value': 1
            },
            {
                'name': 'NUMERICHOST',
                'value': 2
            },
            {
                'name': 'NAMEREQD',
                'value': 4
            },
            {
                'name': 'NUMERICSERV',
                'value': 8
            },
            {
                'name': 'DGRAM',
                'value': 16
            }
        ]
    },
    'IPProtocol': {
        'values': [
            {
                'name': 'IP',
                'value': 0
            },
            {
                'name': 'TCP',
                'value': 6
            },
            {
                'name': 'UDP',
                'value': 8
            },
            {
                'name': 'IPV6',
                'value': 12
            }
        ]
    },
    'IPStackInfoStringFormat': {
        'enum-value-prefix': 'IPSTACK_INFO_STR_FORMAT',
        'values': [
            {
                'name': 'JSON',
                'value': 0
            },
            {
                'name': 'TEXT',
                'value': 1
            }
        ]
    },
   'OperationalStatus': {
        'enum-value-prefix': 'OPERATIONAL_STATUS',
        'force-include': True,
        'values': [
            {
                'name': 'DOWN',
                'value': 0
            },
            {
                'name': 'UP',
                'value': 1
            }
        ]
    },
    'OptName': {
        'values': [
            {
                'name': 'TCP_NODELAY',
                'value': 1
            },
            {
                'name': 'IP_ADD_MEMBERSHIP',
                'value': 3
            },
            {
                'name': 'IP_DROP_MEMBERSHIP',
                'value': 4
            },
            {
                'name': 'IP_MULTICAST_IF',
                'value': 5
            },
            {
                'name': 'IP_MULTICAST_TTL',
                'value': 6
            },
            {
                'name': 'IPV6_JOIN_GROUP',
                'value': 12
            },
            {
                'name': 'IPV6_LEAVE_GROUP',
                'value': 13
            },
            {
                'name': 'IPV6_ADD_MEMBERSHIP',
                'value': 12
            },
            {
                'name': 'IPV6_DROP_MEMBERSHIP',
                'value': 13
            },
            {
                'name': 'IPV6_MULTICAST_IF',
                'value': 14
            },
            {
                'name': 'IPV6_MULTICAST_HOPS',
                'value': 15
            },
            {
                'name': 'IPV6_V6ONLY',
                'value': 16
            },
            {
                'name': 'SO_RXDATA',
                'value': 257
            },
            {
                'name': 'SO_RCVBUF',
                'value': 258
            },
            {
                'name': 'SO_SNDBUF',
                'value': 259
            },
            {
                'name': 'SO_NONBLOCK',
                'value': 260
            },
            {
                'name': 'SO_BINDTODEVICE',
                'value': 261
            },
            {
                'name': 'SO_ERROR',
                'value': 262
            },
            {
                'name': 'SO_LINGER',
                'value': 263
            },
            {
                'name': 'SO_REUSEADDR',
                'value': 264
            },
        ]
    },
    'RecvFlags': {
        'values': [
            {
                'name': 'MSG_PEEK',
                'value': 1
            }
        ]
    },
    'Shutdown': {
        'values': [
            {
                'name': 'RD',
                'value': 0
            },
            {
                'name': 'WR',
                'value': 1
            },
            {
                'name': 'RDWR',
                'value': 2
            }
        ]
    },
    'SocketOptionLevel': {
        'values': [
            {
                'name': 'PROTO_IP',
                'value': 0
            },
            {
                'name': 'PROTO_TCP',
                'value': 6
            },
            {
                'name': 'PROTO_UDP',
                'value': 8
            },
            {
                'name': 'PROTO_IPV6',
                'value': 12
            },
            {
                'name': 'SOCKET',
                'value': 13
            }
        ]
    },
    'SocketProtocolType': {
        'values': [
            {
                'name': 'STREAM',
                'value': 1
            },
            {
                'name': 'DGRAM',
                'value': 2
            }
        ]
    },
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nixnetsocket/enums_addon.py sha256=a5862640c4541b2aa0d943deaafb68bf7e07b2257715d6d1a0ba67180be8adc0 bytes=291 -->
## FILE: source/codegen/metadata/nixnetsocket/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nixnetsocket/enums_addon.py`
- sha256: `a5862640c4541b2aa0d943deaafb68bf7e07b2257715d6d1a0ba67180be8adc0`
- bytes: 291

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}

enums_validation_suppressions = {
    "OptName": ["ENUMS_SHOULD_NOT_HAVE_DUPLICATE_VALUES"]
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nixnetsocket/functions.py sha256=0ffdb00f314084164a5b5f05e7610b3e9df3c396364c4fa9122ac655bbe5fcc6 bytes=33719 -->
## FILE: source/codegen/metadata/nixnetsocket/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nixnetsocket/functions.py`
- sha256: `0ffdb00f314084164a5b5f05e7610b3e9df3c396364c4fa9122ac655bbe5fcc6`
- bytes: 33719

````python
functions = {
    'Accept': {
        'cname': 'nxaccept',
        'init_method': True,
        'status_expression': 'socket_out == -1 ? -1 : 0',
        'parameters': [
            {
                'direction': 'in',
                'name': 'socket',
                'type': 'nxSOCKET'
            },
            {
                'direction': 'out',
                'grpc_type': 'SockAddr',
                'name': 'addr',
                'supports_standard_output_allocation': True,
                'supports_standard_copy_convert': True,
                'type': 'nxsockaddr'
            },
            {
                'direction': 'out',
                'name': 'addrlen',
                'include_in_proto': False,
                'type': 'nxsocklen_t',
                'hardcoded_value': 'static_cast<nxsocklen_t>(sizeof(addr.storage))'
            },
            {
                'direction': 'out',
                'cpp_local_name': 'socket_out',
                'name': 'socket',
                'return_value': True,
                'type': 'nxSOCKET'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'int32'
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
        'returns': 'nxSOCKET'
    },
    'Bind': {
        'cname': 'nxbind',
        'parameters': [
            {
                'direction': 'in',
                'name': 'socket',
                'type': 'nxSOCKET'
            },
            {
                'direction': 'in',
                'grpc_type': 'SockAddr',
                'name': 'name',
                'pointer': True,
                'supports_standard_copy_convert': True,
                'type': 'nxsockaddr'
            },
            {
                'direction': 'in',
                'name': 'namelen',
                'hardcoded_value': 'name.size()',
                'include_in_proto': False,
                'type': 'nxsocklen_t'
            },
        ],
        'returns': 'int32_t'
    },
    'Close': {
        'cname': 'nxclose',
        'parameters': [
            {
                'direction': 'in',
                'name': 'socket',
                'type': 'nxSOCKET'
            }
        ],
        'returns': 'int32_t'
    },
    'Connect': {
        'cname': 'nxconnect',
        'parameters': [
            {
                'direction': 'in',
                'name': 'socket',
                'type': 'nxSOCKET'
            },
            {
                'direction': 'in',
                'grpc_type': 'SockAddr',
                'name': 'name',
                'pointer': True,
                'supports_standard_copy_convert': True,
                'type': 'nxsockaddr'
            },
            {
                'direction': 'in',
                'name': 'namelen',
                'hardcoded_value': 'name.size()',
                'include_in_proto': False,
                'type': 'nxsocklen_t'
            },
        ],
        'returns': 'int32_t'
    },
    'FdIsSet': {
        'cname': 'nxfd_isset',
        'status_expression': '0',
        'parameters': [
            {
                'direction': 'in',
                'name': 'fd',
                'type': 'nxSOCKET'
            },
            {
                'direction': 'in',
                'name': 'set',
                'pointer': True,
                'supports_standard_copy_convert': True,
                'additional_arguments_to_copy_convert': ['session_repository_'],
                'type': 'nxfd_set'
            },
            {
                'direction': 'out',
                'name': 'is_set',
                'return_value': True,
                'type': 'int32_t'
            }
        ],
        'returns': 'int32_t'
    },
    'FreeAddrInfo': {
        'codegen_method': 'private',
        'cname': 'nxfreeaddrinfo',
        'parameters': [
            {
                'direction': 'in',
                'name': 'res',
                'type': 'nxaddrinfo',
                'pointer': True
            }
        ],
        'returns': 'int32_t'
    },
    'GetAddrInfo': {
        'cname': 'nxgetaddrinfo',
        'parameters': [
            {
                'direction': 'in', 
                'name': 'stack_ref', 
                'type': 'nxIpStackRef_t'
            },
            {
                'direction': 'in',
                'name': 'node',
                'type': 'const char[]',
                'proto_only': True
            },
            {
                'direction': 'in',
                'name': 'node_api',
                'type': 'const char[]',
                'hardcoded_value': 'request->node() == "" ? nullptr : node',
                'include_in_proto': False
            },
            {
                'direction': 'in',
                'name': 'service',
                'type': 'const char[]',
                'proto_only': True
            },
            {
                'direction': 'in',
                'name': 'service_api',
                'type': 'const char[]',
                'hardcoded_value': 'request->service() == "" ? nullptr : service',
                'include_in_proto': False
            },
            {
                'direction': 'in',
                'name': 'hints',
                'supports_standard_copy_convert': True,
                'grpc_type': 'AddrInfoHint',
                'pointer': True,
                'type': 'nxaddrinfo'
            },
            {
                'direction': 'out',
                'name': 'res',
                'supports_standard_copy_convert': True,
                'supports_standard_output_allocation': True,
                'additional_arguments_to_output_allocation': ['library_'],
                'pointer': True,
                'type': 'nxaddrinfo'
            }
        ],
        'returns': 'int32_t'
    },
    'GetLastErrorNum': {
        'codegen_method': 'private',
        'cname': 'nxgetlasterrornum',
        'parameters': [],
        'returns': 'int32_t'
    },
    'GetLastErrorStr': {
        'codegen_method': 'private',
        'cname': 'nxgetlasterrorstr',
        'status_expression': 'error ? 0 : -1',
        'parameters': [
            {
                'direction': 'out',
                'include_in_proto': False,
                'name': 'buf',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'bufLen'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'bufLen',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'error',
                'return_value': True,
                'type': 'char[]'
            },
        ],
        'returns': 'char*'
    },
    'GetNameInfo': {
        'cname': 'nxgetnameinfo',
        'parameters': [
            {
                'direction': 'in', 
                'name': 'stack_ref', 
                'type': 'nxIpStackRef_t'
            },
            {
                'direction': 'in',
                'grpc_type': 'SockAddr',
                'name': 'addr',
                'pointer': True,
                'supports_standard_copy_convert': True,
                'type': 'nxsockaddr'
            },
            {
                'direction': 'in',
                'name': 'addrlen',
                'hardcoded_value': 'addr.size()',
                'include_in_proto': False,
                'type': 'nxsocklen_t'
            },
            {
                'direction': 'out',
                'name': 'host',
                'type': 'char[]',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'hostlen'
                }
            },
            {
                'direction': 'in',
                'name': 'hostlen',
                'type': 'nxsocklen_t'
            },
            {
                'direction': 'out',
                'name': 'serv',
                'type': 'char[]',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'servlen'
                }
            },
            {
                'direction': 'in',
                'name': 'servlen',
                'type': 'nxsocklen_t'
            },
            {
                'bitfield_as_enum_array': 'GetNameInfoFlags',
                'direction': 'in',
                'name': 'flags',
                'type': 'int32_t',
            },
        ],
        'returns': 'int32_t'
    },
    'GetPeerName': {
        'cname': 'nxgetpeername',
        'parameters': [
            {
                'direction': 'in',
                'name': 'socket',
                'type': 'nxSOCKET'
            },
            {
                'direction': 'out',
                'grpc_type': 'SockAddr',
                'name': 'addr',
                'supports_standard_output_allocation': True,
                'supports_standard_copy_convert': True,
                'type': 'nxsockaddr'
            },
            {
                'direction': 'out',
                'name': 'addrlen',
                'hardcoded_value': 'static_cast<nxsocklen_t>(sizeof(addr.storage))',
                'include_in_proto': False,
                'type': 'nxsocklen_t'
            },
        ],
        'returns': 'int32_t'
    },
    'GetSockName': {
        'cname': 'nxgetsockname',
        'parameters': [
            {
                'direction': 'in',
                'name': 'socket',
                'type': 'nxSOCKET'
            },
            {
                'direction': 'out',
                'grpc_type': 'SockAddr',
                'name': 'addr',
                'supports_standard_output_allocation': True,
                'supports_standard_copy_convert': True,
                'type': 'nxsockaddr'
            },
            {
                'direction': 'out',
                'name': 'addrlen',
                'hardcoded_value': 'static_cast<nxsocklen_t>(sizeof(addr.storage))',
                'include_in_proto': False,
                'type': 'nxsocklen_t'
            },
        ],
        'returns': 'int32_t'
    },
    'GetSockOpt': {
        'cname': 'nxgetsockopt',
        'parameters': [
            {
                'direction': 'in',
                'name': 'socket',
                'type': 'nxSOCKET'
            },
            {
                'direction': 'in',
                'name': 'level',
                'type': 'int32_t',
                'enum': 'SocketOptionLevel'
            },
            {
                'direction': 'in',
                'name': 'optname',
                'type': 'int32_t',
                'enum': 'OptName'
            },
            {
                'direction': 'out',
                'name': 'optval',
                'grpc_type': 'SockOptData',
                'supports_standard_output_allocation': True,
                "additional_arguments_to_output_allocation": ['library_','optname'],
                'supports_standard_copy_convert': True,
                'pointer': True,
                'type': 'void *'
            },
            {
                'direction': 'out',
                'name': 'optlen',
                'hardcoded_value': 'optval.size(socket, level)',
                'include_in_proto': False,
                'type': 'nxsocklen_t'
            }
        ],
        'returns': 'int32_t'
    },
    'InetAddr': {
        'cname': 'nxinet_addr',
        'status_expression': 'addr == -1 ? -1 : 0',
        'parameters': [
            {
                'direction': 'in',
                'name': 'stack_ref',
                'type': 'nxIpStackRef_t'
            },
            {
                'direction': 'in',
                'name': 'cp',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'name': 'addr',
                'return_value': True,
                'type': 'uint32_t'
            },
        ],
        'returns': 'uint32_t'
    },
    'InetAToN': {
        'cname': 'nxinet_aton',
        'parameters': [
            {
                'direction': 'in',
                'name': 'stack_ref',
                'type': 'nxIpStackRef_t'
            },
            {
                'direction': 'in',
                'name': 'cp',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'grpc_type': 'InAddr',
                'name': 'name',
                'supports_standard_copy_convert': True,
                'supports_standard_output_allocation': True,
                'type': 'nxin_addr'
            },
        ],
        'returns': 'int32_t'
    },
    'InetNToA': {
        'cname': 'nxinet_ntoa',
        'status_expression': 'address ? 0 : -1',
        'parameters': [
            {
                'direction': 'in',
                'name': 'stack_ref',
                'type': 'nxIpStackRef_t'
            },
            {
                'direction': 'in',
                'grpc_name': 'in_addr',
                'grpc_type': 'InAddr',
                'name': 'in',
                'supports_standard_copy_convert': True,
                'type': 'nxin_addr'
            },
            {
                'direction': 'out',
                'name': 'address',
                'return_value': True,
                'type': 'char[]'
            },
        ],
        'returns': 'char*'
    },
    'InetNToP': {
        'cname': 'nxinet_ntop',
        'status_expression': 'address ? 0 : -1',
        'parameters': [
            {
                'direction': 'in',
                'name': 'stack_ref',
                'type': 'nxIpStackRef_t'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'get_address_family(request->addr().addr_case())',
                'include_in_proto': False,
                'name': 'af',
                'type': 'int32_t'
            },
            {
                'direction': 'in',
                'grpc_name': 'addr',
                'name': 'src',
                'grpc_type': 'Addr',
                'pointer': True,
                'supports_standard_copy_convert': True,
                'type': 'void'
            },
            {
                'direction': 'out',
                'name': 'dst',
                'include_in_proto': False,
                'size': {
                    'mechanism': 'fixed',
                    'value': 'nxINET6_ADDRSTRLEN'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'hardcoded_value': 'nxINET6_ADDRSTRLEN',
                'include_in_proto': False,
                'type': 'nxsocklen_t'
            },
            {
                'direction': 'out',
                'name': 'address',
                'return_value': True,
                'type': 'char[]'
            },
        ],
        'returns': 'const char*'
    },
    'InetPToN': {
        'cname': 'nxinet_pton',
        'parameters': [
            {
                'direction': 'in',
                'name': 'stack_ref',
                'type': 'nxIpStackRef_t'
            },
            {
                'direction': 'in',
                'enum': 'AddressFamily',
                'name': 'af',
                'type': 'int32_t'
            },
            {
                'direction': 'in',
                'grpc_name': 'address',
                'name': 'src',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'grpc_name': 'addr',
                'grpc_type': 'Addr',
                'name': 'dst',
                'supports_standard_output_allocation': True,
                "additional_arguments_to_output_allocation": ["af"],
                'supports_standard_copy_convert': True,
                'type': 'void'
            },
        ],
        'returns': 'int32_t'
    },
    'IpStackClear': {
        'custom_close_method': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'stack_ref',
                'type': 'nxIpStackRef_t'
            },
        ],
        'returns': 'int32_t'
    },
    'IpStackCreate': {
        'custom_close': 'IpStackClear(id)',
        'init_method': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'stack_name',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'config',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'stack_ref',
                'type': 'nxIpStackRef_t'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'int32'
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
        'returns': 'int32_t'
    },
    'IpStackFreeAllStacksInfoStr': {
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'in',
                'name': 'info',
                'type': 'nixnetsocket_grpc::IpStackInfoString',
            },
        ],
        'returns': 'void',
    },
    'IpStackFreeInfo': {
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'in',
                'name': 'firstVirtualInterface',
                'pointer': True,
                'type': 'nxVirtualInterface_t',
            },
        ],
        'returns': 'int32_t'
    },
    'IpStackGetAllStacksInfoStr': {
        'parameters': [
            {
                'direction': 'in', 
                'enum': 'IPStackInfoStringFormat',
                'name': 'format', 
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'info',
                'supports_standard_output_allocation': True,
                'additional_arguments_to_output_allocation': ['library_'],
                'supports_standard_copy_convert': True,
                'type': 'nixnetsocket_grpc::IpStackInfoString',
            },
        ],
        'returns': 'int32_t',
    },
    'IpStackGetInfo': {
        'parameters': [
            {
                'direction': 'in', 
                'name': 'stack_ref', 
                'type': 'nxIpStackRef_t'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nxIPSTACK_INFO_ID',
                'include_in_proto': False,
                'name': 'info_id',
                'type': 'uint32_t',
            },
            {
                'direction': 'out',
                'name': 'virtual_interfaces',
                'pointer': True,
                'supports_standard_output_allocation': True,
                'additional_arguments_to_output_allocation': ['library_'],
                'supports_standard_copy_convert': True,
                'type': 'nxVirtualInterface_t',
            },
        ],
        'returns': 'int32_t',
    },
    'IpStackOpen': {
        'custom_close': 'IpStackClear(id)',
        'init_method': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'stack_name',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'stack_ref',
                'type': 'nxIpStackRef_t'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'int32'
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
        'returns': 'int32_t'
    },
    'IpStackWaitForInterface': {
        'parameters': [
            {
                'direction': 'in', 
                'name': 'stack_ref',
                'type': 'nxIpStackRef_t'
            },
            {
                'direction': 'in', 
                'name': 'localInterface', 
                'type': 'const char[]'
            },
            {
                'direction': 'in', 
                'name': 'timeoutMs', 
                'type': 'int32_t'
            },
        ],
        'returns': 'int32_t',
    },
    'Listen': {
        'cname': 'nxlisten',
        'parameters': [
            {
                'direction': 'in',
                'name': 'socket',
                'type': 'nxSOCKET'
            },
            {
                'direction': 'in',
                'name': 'backlog',
                'type': 'int32_t'
            },
        ],
        'returns': 'int32_t'
    },
     'Recv': {
        'cname': 'nxrecv',
        'parameters': [
            {
                'direction': 'in',
                'name': 'socket',
                'type': 'nxSOCKET'
            },
            {
                'direction': 'out',
                'grpc_name': 'data',
                'name': 'mem',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'size'
                },
                'grpc_type': 'bytes',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'int32_t'
            },
            {
                'bitfield_as_enum_array': 'RecvFlags',
                'direction': 'in',
                'name': 'flags',
                'type': 'int32_t'
            },
        ],
        'returns': 'int32_t'
    },
    'RecvFrom': {
        'cname': 'nxrecvfrom',
        'parameters': [
            {
                'direction': 'in',
                'name': 'socket',
                'type': 'nxSOCKET'
            },
            {
                'direction': 'out',
                'grpc_name': 'data',
                'name': 'mem',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'size'
                },
                'grpc_type': 'bytes',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'int32_t'
            },
            {
                'bitfield_as_enum_array': 'RecvFlags',
                'direction': 'in',
                'name': 'flags',
                'type': 'int32_t'
            },
            {
                'direction': 'out',
                'grpc_name': 'from_addr',
                'grpc_type': 'SockAddr',
                'name': 'from',
                'supports_standard_output_allocation': True,
                'supports_standard_copy_convert': True,
                'type': 'nxsockaddr'
            },
            {
                'direction': 'out',
                'name': 'fromlen',
                'include_in_proto': False,
                'type': 'nxsocklen_t',
                'hardcoded_value': 'static_cast<nxsocklen_t>(sizeof(from_addr.storage))'
            },
        ],
        'returns': 'int32_t'
    },
    'Select': {
        'cname': 'nxselect',
        'parameters': [
            {
                'direction': 'in',
                'hardcoded_value': '0',
                'include_in_proto': False,
                'name': 'nfds',
                'type': 'int32_t'
            },
            {
                'direction': 'in',
                'name': 'readfds',
                'pointer': True,
                'supports_standard_copy_convert': True,
                'additional_arguments_to_copy_convert': ['session_repository_'],
                'type': 'nxfd_set'
            },
            {
                'direction': 'in',
                'name': 'writefds',
                'pointer': True,
                'supports_standard_copy_convert': True,
                'additional_arguments_to_copy_convert': ['session_repository_'],
                'type': 'nxfd_set'
            },
            {
                'direction': 'in',
                'name': 'exceptfds',
                'pointer': True,
                'supports_standard_copy_convert': True,
                'additional_arguments_to_copy_convert': ['session_repository_'],
                'type': 'nxfd_set'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'pointer': True,
                'supports_standard_copy_convert': True,
                'type': 'nxtimeval'
            },
        ],
        'returns': 'int32_t'
    },
    'Send': {
        'cname': 'nxsend',
        'parameters': [
            {
                'direction': 'in',
                'name': 'socket',
                'type': 'nxSOCKET'
            },
            {
                'direction': 'in',
                'grpc_name': 'data',
                'name': 'dataptr',
                'pointer': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'pointer': True,
                'grpc_type': 'bytes',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'int32_t'
            },
            {
                'direction': 'in',
                'grpc_name': 'flags_raw',
                'name': 'flags',
                'type': 'int32_t'
            },
        ],
        'returns': 'int32_t'
    },
    'SendTo': {
        'cname': 'nxsendto',
        'parameters': [
            {
                'direction': 'in',
                'name': 'socket',
                'type': 'nxSOCKET'
            },
            {
                'direction': 'in',
                'grpc_name': 'data',
                'name': 'dataptr',
                'pointer': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'pointer': True,
                'grpc_type': 'bytes',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'int32_t'
            },
            {
                'direction': 'in',
                'grpc_name': 'flags_raw',
                'name': 'flags',
                'type': 'int32_t'
            },
            {
                'direction': 'in',
                'grpc_type': 'SockAddr',
                'name': 'to',
                'pointer': True,
                'supports_standard_copy_convert': True,
                'type': 'nxsockaddr'
            },
            {
                'direction': 'in',
                'name': 'tolen',
                'hardcoded_value': 'to.size()',
                'include_in_proto': False,
                'type': 'nxsocklen_t'
            },
        ],
        'returns': 'int32_t'
    },
    'SetSockOpt': {
        'cname': 'nxsetsockopt',
        'parameters': [
            {
                'direction': 'in',
                'name': 'socket',
                'type': 'nxSOCKET'
            },
            {
                'direction': 'in',
                'name': 'level',
                'type': 'int32_t',
                'enum': 'SocketOptionLevel'
            },
            {
                'direction': 'in',
                'name': 'optname',
                'type': 'int32_t',
                'enum': 'OptName'
            },
            {
                'direction': 'in',
                'name': 'opt_data',
                'grpc_type': 'SockOptData',
                'supports_standard_copy_convert': True,
                'proto_only': True,
                'type': 'SockOptDataInputConverter'
            },
            {
                'direction': 'in',
                'name': 'optval',
                'hardcoded_value': 'opt_data.data()',
                'include_in_proto': False,
                'pointer': True,
                'type': 'void'
            },
            {
                'direction': 'in',
                'name': 'optlen',
                'hardcoded_value': 'opt_data.size()',
                'include_in_proto': False,
                'type': 'nxsocklen_t'
            }
        ],
        'returns': 'int32_t'
    },
    'Shutdown': {
        'cname': 'nxshutdown',
        'parameters': [
            {
                'direction': 'in',
                'name': 'socket',
                'type': 'nxSOCKET'
            },
             {
                'direction': 'in',
                'name': 'how',
                'type': 'int32_t',
                'enum': 'Shutdown'
            },
        ],
        'returns': 'int32_t'
    },
    'Socket': {
        'cname': 'nxsocket',
        'init_method': True,
        'status_expression': 'socket == -1 ? -1 : 0',
        'parameters': [
            {
                'direction': 'in',
                'name': 'stack_ref',
                'type': 'nxIpStackRef_t'
            },
            {
                'direction': 'in',
                'name': 'domain',
                'type': 'int32_t',
                'enum': 'AddressFamily'
            },
            {
                'direction': 'in',
                'name': 'type',
                'type': 'int32_t',
                'enum': 'SocketProtocolType'
            },
            {
                'direction': 'in',
                'name': 'protocol',
                'type': 'int32_t',
                'enum': 'IPProtocol'
            },
            {
                'direction': 'out',
                'name': 'socket',
                'return_value': True,
                'type': 'nxSOCKET'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'int32'
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
        'returns': 'nxSOCKET'
    },
    'StrErrR': {
        'cname': 'nxstrerr_r',
        'exclude_from_get_last_error': True,
        'status_expression': 'error ? 0 : -1',
        'parameters': [
            {
                'direction': 'in',
                'name': 'errnum',
                'type': 'int'
            },
            {
                'direction': 'out',
                'include_in_proto': False,
                'name': 'buf',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'bufLen'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'bufLen',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'error',
                'return_value': True,
                'type': 'char[]'
            },
        ],
        'returns': 'char*'
    },
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nixnetsocket/functions_addon.py sha256=e85743f1e3f7db4a9900caf8a01ab4889bc72bd3b0c07b67f55c181a3f7e9bf0 bytes=400 -->
## FILE: source/codegen/metadata/nixnetsocket/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nixnetsocket/functions_addon.py`
- sha256: `e85743f1e3f7db4a9900caf8a01ab4889bc72bd3b0c07b67f55c181a3f7e9bf0`
- bytes: 400

````python
functions_override_metadata = {}

# Client requests the amount of data to read.
functions_validation_suppressions = {
    name: {"parameters": {"mem": ["ARRAY_PARAMETER_NEEDS_SIZE"]}} for name in ["Recv", "RecvFrom"]
}

# Allocated with supports_standard_output_allocation.
functions_validation_suppressions["GetSockOpt"] = {
    "parameters": {"optval": ["ARRAY_PARAMETER_NEEDS_SIZE"]}
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/visa/__init__.py sha256=80aa5e93c151b9a34e9755e0c4a699cb31ceb6c43e74436ffb5e5770ebb452ad bytes=250 -->
## FILE: source/codegen/metadata/visa/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/visa/__init__.py`
- sha256: `80aa5e93c151b9a34e9755e0c4a699cb31ceb6c43e74436ffb5e5770ebb452ad`
- bytes: 250

````python
from .functions import functions
from .attributes import attributes
from .enums import enums
from .config import config

metadata = {
    "functions" : functions,
    "attributes" : attributes,
    "enums" : enums,
    "config" : config
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/visa/attributes.py sha256=0bfff50d9c18d322ea41731094d71ae9d32d28e695bc23b65d5a9dd6b1283320 bytes=73607 -->
## FILE: source/codegen/metadata/visa/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/visa/attributes.py`
- sha256: `0bfff50d9c18d322ea41731094d71ae9d32d28e695bc23b65d5a9dd6b1283320`
- bytes: 73607

````python
attributes = {
    -1073807359: {
        'access': 'read only',
        'documentation': {
            'description': " This attribute specifies the resource class (for example, 'INSTR') as defined by the canonical resource name. "
        },
        'name': 'RSRC_CLASS',
        'type': 'ViString'
    },
    -1073807358: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the unique identifier for a resource compliant with the address structure shown in the following table.  Optional string segments are shown in square brackets. Interface            Syntax GPIB INSTR           GPIB[board]::primary address[::secondary address][::INSTR] GPIB INTFC           GPIB[board]::INTFC GPIB SERVANT         GPIB[board]::SERVANT GPIB-VXI INSTR       GPIB-VXI[board]::VXI logical address[::INSTR] GPIB-VXI BACKPLANE   GPIB-VXI[board][::mainframe logical address]::BACKPLANE GPIB-VXI MEMACC      GPIB-VXI[board]::MEMACC PXI INSTR            PXI[bus]::device[::function][::INSTR] PXI INSTR            PXI[interface]::[bus-]device[.function][::INSTR] PXI BACKPLANE        PXI[interface]::chassis::BACKPLANE PXI MEMACC           PXI[interface]::MEMACC Serial INSTR         ASRL[board][::INSTR] TCPIP INSTR          TCPIP[board]::host address[::LAN device name][::INSTR] TCPIP SOCKET         TCPIP[board]::host address::port::SOCKET VXI INSTR            VXI[board]::VXI logical address[::INSTR] VXI BACKPLANE        VXI[board][::mainframe logical address]::BACKPLANE VXI MEMACC           VXI[board]::MEMACC VXI SERVANT          VXI[board]::SERVANT USB INSTR            USB[board]::vendor id::product id::serial number[::interface number][::INSTR] USB RAW              USB[board]::vendor id::product id::serial number[::interface number]::RAW FIREWIRE INSTR       FIREWIRE[board]::vendor id::chip id::INSTR Remote Access        visa://hostname[:port]/resource '
        },
        'name': 'RSRC_NAME',
        'type': 'ViString'
    },
    -1073807246: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute is a human-readable string representation of the local controller associated with this session. '
        },
        'name': 'MANF_NAME',
        'type': 'ViString'
    },
    -1073807241: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute is a human-readable string representation of the device model. '
        },
        'name': 'MODEL_NAME',
        'type': 'ViString'
    },
    -1073807127: {
        'access': 'read only',
        'documentation': {
            'description': ' Human-readable text describing the given interface. '
        },
        'name': 'INTF_INST_NAME',
        'type': 'ViString'
    },
    -1073806988: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute value is the name of the manufacturer that created the VISA implementation. '
        },
        'name': 'RSRC_MANF_NAME',
        'type': 'ViString'
    },
    -1073806955: {
        'access': 'read only',
        'documentation': {
            'description': ' This is the TCPIP address of the device to which the session is connected. This string is formatted in dot notation. '
        },
        'name': 'TCPIP_ADDR',
        'type': 'ViString'
    },
    -1073806954: {
        'access': 'read only',
        'documentation': {
            'description': ' This specifies the host name of the device. If no host name is available, this attribute returns an empty string. '
        },
        'name': 'TCPIP_HOSTNAME',
        'type': 'ViString'
    },
    -1073806951: {
        'access': 'read only',
        'documentation': {
            'description': ' This specifies the LAN device name used by the VXI-11 protocol during connection. This attribute is valid only on TCPIP INSTR sessions. '
        },
        'name': 'TCPIP_DEVICE_NAME',
        'type': 'ViString'
    },
    -1073806944: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the USB serial number of this device. '
        },
        'name': 'USB_SERIAL_NUM',
        'type': 'ViString'
    },
    -1073806841: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the slot path of this device. '
        },
        'name': 'PXI_SLOTPATH',
        'type': 'ViString'
    },
    -1073806736: {
        'access': 'read only',
        'documentation': {
            'description': ' The name of the CA that signed the certificate . For an LDevId this will indicate the name of the PKI CA. '
        },
        'name': 'TCPIP_SERVER_CERT_ISSUER_NAME',
        'type': 'ViString'
    },
    -1073806735: {
        'access': 'read only',
        'documentation': {
            'description': ' The subject field from the certificate. That is, the entity associated with the public key in the certificate. '
        },
        'name': 'TCPIP_SERVER_CERT_SUBJECT_NAME',
        'type': 'ViString'
    },
    -1073806734: {
        'access': 'read only',
        'documentation': {
            'description': " The expiration date of the server certificate. The form is UTC Time 'YYMMDDhhmm[ss]Z'. "
        },
        'name': 'TCPIP_SERVER_CERT_EXPIRATION_DATE',
        'type': 'ViString'
    },
    -1073806732: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns a string that indicates the SASL mechanism used to authenticate the client. The string is as defined by IANA in: https://www.iana.org/assignments/sasl-mechanisms. '
        },
        'name': 'TCPIP_SASL_MECHANISM',
        'type': 'ViString'
    },
    -1073806731: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns a string that indicates the cipher suite used by TLS, which tells the user something about the security of the connection. For details, refer to https://www.iana.org/assignments/tls-parameters. For example, look at TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384. '
        },
        'name': 'TCPIP_TLS_CIPHER_SUITE',
        'type': 'ViString'
    },
    -1073806730: {
        'access': 'read only',
        'documentation': {
            'description': ' The full text of the server certificate in RFC 5652 PEM format. The passed in data buffer must be of size at least equal to the Certificate Size attribute (VI_ATTR_TCPIP_SERVER_CERT_SIZE). '
        },
        'name': 'TCPIP_SERVER_CERT',
        'type': 'ViUInt8 []'
    },
    -1073790910: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute contains the name of the operation generating this event. This is valid for the VI_EVENT_IO_COMPLETION and VI_EVENT_EXCEPTION events. '
        },
        'name': 'OPER_NAME',
        'type': 'ViString'
    },
    -1073790568: {
        'access': 'read only',
        'documentation': {
            'description': ' This is the TCP/IP address of the device from which the session received a connection. '
        },
        'name': 'RECV_TCPIP_ADDR',
        'type': 'ViString'
    },
    -1073790543: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute contains the actual received data from the USB Interrupt. The passed in data buffer must be of size at least equal to the Usb Received Interrupt Size Attribute (VI_ATTR_USB_RECV_INTR_SIZE). This is valid for the VI_EVENT_USB_INTR event. '
        },
        'name': 'USB_RECV_INTR_DATA',
        'type': 'ViUInt8 []'
    },
    1073676291: {
        'access': 'read only',
        'documentation': {
            'description': ' This attributes returns the implementation version of the object. The version value has a hexadecimal format 0xXXXYYYZZ, where XXX is the major version, YYY is the minor version, and ZZ is the subminor version. The subminor version is usually 0 for releases. Other values are used to indicate a patch or beta version. '
        },
        'name': 'RSRC_IMPL_VERSION',
        'type': 'ViVersion'
    },
    1073676292: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute indicates the current locking state of the resource. The resource can be unlocked, locked with an exclusive lock, or locked with a shared lock. '
        },
        'enum': 'LockState',
        'name': 'RSRC_LOCK_STATE',
        'type': 'ViAccessMode'
    },
    1073676293: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the maximum number of events that can be queued at any time on the given session. Events that occur after the queue has become full will be discarded. This is a Read/Write attribute until the first time viEnableEvent() is called on a session. Thereafter, this attribute is Read Only. '
        },
        'name': 'MAX_QUEUE_LENGTH',
        'type': 'ViUInt32'
    },
    1073676295: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute value is the data used privately by the application for a particular session. This data is not used by VISA for any purposes. It is provided to the application for its own use. '
        },
        'name': 'USER_DATA',
        'type': 'ViAddr'
    },
    1073676301: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute determines which FDC channel will be used to transfer the buffer. '
        },
        'name': 'FDC_CHNL',
        'type': 'ViUInt16'
    },
    1073676303: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies which FDC mode to use (either normal or stream mode). '
        },
        'enum': 'FdcMode',
        'name': 'FDC_MODE',
        'type': 'ViUInt16'
    },
    1073676307: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies specifies whether to use a channel pair (VI_TRUE) or a single channel (VI_FLASE) for transferring data. '
        },
        'name': 'FDC_USE_PAIR',
        'type': 'ViBoolean'
    },
    1073676310: {
        'access': 'read-write',
        'documentation': {
            'description': " This attribute specifies whether to assert END during the transfer of the last byte of the buffer. This attribute is relevant only in viWrite and related operations. On Serial INSTR sessions, if this attribute is set to VI_FALSE, the write will transmit the exact contents of the user buffer, without modifying it and without appending anything to the data being written. If this attribute is set to VI_TRUE, VISA will perform the behavior described in VI_ATTR_ASRL_END_OUT. On GPIB, VXI, GPIB-VXI, TCP/IP INSTR, and USB INSTR sessions, if this attribute is set to VI_TRUE, VISA will include the 488.2 defined 'end of message' terminator. "
        },
        'name': 'SEND_END_EN',
        'type': 'ViBoolean'
    },
    1073676312: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute represents the termination character. When the termination character is read and VI_ATTR_TERMCHAR_EN is enabled during a read operation, the read operation terminates. '
        },
        'name': 'TERMCHAR',
        'type': 'ViUInt8'
    },
    1073676314: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the minimum timeout value to use (in milliseconds) when accessing the device associated with the given session. A timeout value of VI_TMO_IMMEDIATE means that operations should never wait for the device to respond. A timeout value of VI_TMO_INFINITE disables the timeout mechanism. ',
            'note': 'that the actual timeout used may be higher than the one requested.'
        },
        'enum': 'TmoValue',
        'name': 'TMO_VALUE',
        'type': 'ViUInt32'
    },
    1073676315: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies whether the device is to be readdressed before every transfer. '
        },
        'name': 'GPIB_READDR_EN',
        'type': 'ViBoolean'
    },
    1073676316: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies which protocol to use. In VXI systems, for example, you can choose between normal word serial or Fast Data Channel (FDC). In GPIB, you can choose between normal and high-speed (HS488) data transfers. In Serial, you can choose between normal and 488.2 modes.  The 488.2 mode adds the ability to use viAssertTrigger(), viReadSTB(), and viClear() by sending the corresponding 488.2-defined command strings. '
        },
        'enum': 'IoProt',
        'name': 'IO_PROT',
        'type': 'ViUInt16'
    },
    1073676318: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies whether I/O accesses should use DMA or PIO (Programmed I/O). '
        },
        'name': 'DMA_ALLOW_EN',
        'type': 'ViBoolean'
    },
    1073676321: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute is the baud rate of the interface. It is represented as an unsigned 32-bit integer so that any baud rate can be used, but it usually requires a commonly used rate such as 300, 1200, 2400, or 9600 baud. '
        },
        'name': 'ASRL_BAUD',
        'type': 'ViUInt32'
    },
    1073676322: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute is the number of data bits contained in each frame (from 5 to 8). The data bits for each frame are located in the low-order bits of every byte stored in memory. '
        },
        'name': 'ASRL_DATA_BITS',
        'type': 'ViUInt16'
    },
    1073676323: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute is the parity used with every frame transmitted and received. '
        },
        'enum': 'AsrlParity',
        'name': 'ASRL_PARITY',
        'type': 'ViUInt16'
    },
    1073676324: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute is the number of stop bits used to indicate the end of a frame. '
        },
        'enum': 'AsrlStop',
        'name': 'ASRL_STOP_BITS',
        'type': 'ViUInt16'
    },
    1073676325: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute indicates the type of flow control used by the transfer mechanism. '
        },
        'enum': 'AsrlFlow',
        'name': 'ASRL_FLOW_CNTRL',
        'type': 'ViUInt16'
    },
    1073676330: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the operational mode of the formatted I/O read buffer. When the operational mode is set to VI_FLUSH_DISABLE (default), the buffer is flushed only on explicit calls to viFlush(). If the operational mode is set to VI_FLUSH_ON_ACCESS, the buffer is flushed every time a viScanf() operation completes. '
        },
        'enum': 'RdOperMode',
        'name': 'RD_BUF_OPER_MODE',
        'type': 'ViUInt16'
    },
    1073676331: {
        'access': 'read only',
        'documentation': {
            'description': ' This is the current size of the formatted I/O input buffer for this session. '
        },
        'name': 'RD_BUF_SIZE',
        'type': 'ViUInt32'
    },
    1073676333: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the operational mode of the formatted I/O write buffer. When the operational mode is set to VI_FLUSH_WHEN_FULL (default), the buffer is flushed when an END indicator is written to the buffer, or when the buffer fills up. If the operational mode is set to VI_FLUSH_ON_ACCESS, the write buffer is flushed under the same conditions, and also every time a viPrintf() operation completes. '
        },
        'enum': 'WrOperMode',
        'name': 'WR_BUF_OPER_MODE',
        'type': 'ViUInt16'
    },
    1073676334: {
        'access': 'read only',
        'documentation': {
            'description': ' This is the current size of the formatted I/O output buffer for this session. '
        },
        'name': 'WR_BUF_SIZE',
        'type': 'ViUInt32'
    },
    1073676342: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute is relevant only in viRead and related operations. For all session types on which this attribute is supported, if this attribute is set to VI_TRUE, read will not terminate due to an END condition. However, a read may still terminate successfully if VI_ATTR_TERMCHAR_EN is set to VI_TRUE. Otherwise, read will not terminate until all of the requested data is received (or an error occurs). On Serial INSTR sessions, if this attribute is set to VI_FALSE, VISA will perform the behavior described in VI_ATTR_ASRL_END_IN. On USB RAW sessions, if this attribute is set to VI_FALSE, VISA will perform the behavior described in VI_ATTR_USB_END_IN. On TCP/IP SOCKET sessions, if this attribute is set to VI_FALSE, if NI-VISA reads some data and then detects a pause in the arrival of data packets, it will terminate the read operation. On TCP/IP SOCKET sessions, this attribute defaults to VI_TRUE in NI-VISA. On VXI INSTR sessions, if this attribute is set to VI_FALSE, the END bit terminates read operations. '
        },
        'name': 'SUPPRESS_END_EN',
        'type': 'ViBoolean'
    },
    1073676344: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute determines whether the read operation should terminate when a termination character is received. '
        },
        'name': 'TERMCHAR_EN',
        'type': 'ViBoolean'
    },
    1073676345: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the address modifier to be used in high-level access operations, such as viOutXX() and viMoveOutXX(), when writing to the destination. '
        },
        'enum': 'AccessPriv',
        'name': 'DEST_ACCESS_PRIV',
        'type': 'ViUInt16'
    },
    1073676346: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the byte order to be used in high-level access operations, such as viOutXX() and viMoveOutXX(), when writing to the destination. '
        },
        'enum': 'ByteOrder',
        'name': 'DEST_BYTE_ORDER',
        'type': 'ViUInt16'
    },
    1073676348: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the address modifier to be used in high-level access operations, such as viInXX() and viMoveInXX(), when reading from the source. '
        },
        'enum': 'AccessPriv',
        'name': 'SRC_ACCESS_PRIV',
        'type': 'ViUInt16'
    },
    1073676349: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the byte order to be used in high-level access operations, such as viInXX() and viMoveInXX(), when reading from the source. '
        },
        'enum': 'ByteOrder',
        'name': 'SRC_BYTE_ORDER',
        'type': 'ViUInt16'
    },
    1073676352: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute is used in the viMoveInXX() operations to specify by how many elements the source offset is to be incremented after every transfer. The default value of this attribute is 1 (that is, the source address will be incremented by the access width after each transfer), and the viMoveInXX() operations move from consecutive elements. If this attribute is set to 0, the viMoveInXX() operations will always read from the same element, essentially treating the source as a FIFO register. '
        },
        'name': 'SRC_INCREMENT',
        'type': 'ViInt32'
    },
    1073676353: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute is used in the viMoveOutXX() operations to specify by how many elements the destination offset is to be incremented after every transfer. The default value of this attribute is 1 (that is, the destination address will be incremented by the access width after each transfer), and the viMoveOutXX() operations move into consecutive elements. If this attribute is set to 0, the viMoveOutXX() operations will always write to the same element, essentially treating the destination as a FIFO register. '
        },
        'name': 'DEST_INCREMENT',
        'type': 'ViInt32'
    },
    1073676357: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the address modifier to be used in low-level access operations, such as viMapAddress(), viPeekXX() and viPokeXX(), when accessing the mapped window. '
        },
        'enum': 'AccessPriv',
        'name': 'WIN_ACCESS_PRIV',
        'type': 'ViUInt16'
    },
    1073676359: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the byte order to be used in low-level access operations, such as viMapAddress(), viPeekXX() and viPokeXX(), when accessing the mapped window. '
        },
        'enum': 'ByteOrder',
        'name': 'WIN_BYTE_ORDER',
        'type': 'ViUInt16'
    },
    1073676375: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute shows the current state of the GPIB ATN (ATentioN) interface line. '
        },
        'enum': 'LineState',
        'name': 'GPIB_ATN_STATE',
        'type': 'ViInt16'
    },
    1073676380: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute shows whether the specified GPIB interface is currently addressed to talk or listen, or is not addressed. '
        },
        'enum': 'GpibAddr',
        'name': 'GPIB_ADDR_STATE',
        'type': 'ViUInt16'
    },
    1073676382: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute shows whether the specified GPIB interface is currently CIC (Controller In Charge). '
        },
        'name': 'GPIB_CIC_STATE',
        'type': 'ViBoolean'
    },
    1073676386: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute shows the current state of the GPIB NDAC (Not Data ACcepted) interface line. '
        },
        'enum': 'LineState',
        'name': 'GPIB_NDAC_STATE',
        'type': 'ViInt16'
    },
    1073676391: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute shows the current state of the GPIB SRQ (Service ReQuest) interface line. '
        },
        'enum': 'LineState',
        'name': 'GPIB_SRQ_STATE',
        'type': 'ViInt16'
    },
    1073676392: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute shows whether the specified GPIB interface is currently the system controller. '
        },
        'name': 'GPIB_SYS_CNTRL_STATE',
        'type': 'ViBoolean'
    },
    1073676393: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the total number of meters of GPIB cable used in the specified GPIB interface. '
        },
        'enum': 'GpibHighSpeedCableLen',
        'name': 'GPIB_HS488_CBL_LEN',
        'type': 'ViInt16'
    },
    1073676395: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute is the unique logical address of the commander of the VXI device used by the given session. '
        },
        'name': 'CMDR_LA',
        'type': 'ViInt16'
    },
    1073676396: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute represents the VXI-defined device class to which the resource belongs. '
        },
        'enum': 'VxiDevClass',
        'name': 'VXI_DEV_CLASS',
        'type': 'ViUInt16'
    },
    1073676400: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the lowest logical address in the mainframe. If the logical address is not known, VI_UNKNOWN_LA is returned. '
        },
        'name': 'MAINFRAME_LA',
        'type': 'ViInt16'
    },
    1073676427: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute shows the current state of the VXI/VME interrupt lines. This is a bit vector with bits 0-6 corresponding to interrupt lines 1-7. '
        },
        'name': 'VXI_VME_INTR_STATUS',
        'type': 'ViUInt16'
    },
    1073676429: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute shows the current state of the VXI trigger lines. This is a bit vector with bits 0-9 corresponding to VI_TRIG_TTL0 through VI_TRIG_ECL1. '
        },
        'name': 'VXI_TRIG_STATUS',
        'type': 'ViUInt32'
    },
    1073676436: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute shows the current state of the VXI SYSFAIL (SYStem FAILure) backplane line. '
        },
        'enum': 'LineState',
        'name': 'VXI_VME_SYSFAIL_STATE',
        'type': 'ViInt16'
    },
    1073676440: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the base address of the interface bus to which this window is mapped. If the value of VI_ATTR_WIN_ACCESS is VI_NMAPPED, the value of this attribute is meaningless. '
        },
        'name': 'WIN_BASE_ADDR',
        'type': 'ViBusAddress'
    },
    1073676442: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the size of the region mapped to this window. If the value of VI_ATTR_WIN_ACCESS is VI_NMAPPED, the value of this attribute is meaningless. '
        },
        'name': 'WIN_SIZE',
        'type': 'ViBusSize'
    },
    1073676460: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute shows the number of bytes available in the global receive buffer. '
        },
        'name': 'ASRL_AVAIL_NUM',
        'type': 'ViUInt32'
    },
    1073676461: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the base address of the device in VXIbus memory address space. This base address is applicable to A24 or A32 address space. If the value of VI_ATTR_MEM_SPACE is VI_A16_SPACE, the value of this attribute is meaningless for VXI devices. '
        },
        'name': 'MEM_BASE',
        'type': 'ViBusAddress'
    },
    1073676462: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute shows the current state of the Clear To Send (CTS) input signal. '
        },
        'enum': 'LineState',
        'name': 'ASRL_CTS_STATE',
        'type': 'ViInt16'
    },
    1073676463: {
        'access': 'read-write',
        'documentation': {
            'description': " This attribute represents the current state of the Data Carrier Detect (DCD) input signal. The DCD signal is often used by modems to indicate the detection of a carrier (remote modem) on the telephone line. The DCD signal is also known as 'Receive Line Signal Detect (RLSD).' This attribute is Read Only except when the VI_ATTR_ASRL_WIRE_MODE attribute is set to VI_ASRL_WIRE_232_DCE, or VI_ASRL_WIRE_232_AUTO with the hardware currently in the DCE state. "
        },
        'enum': 'LineState',
        'name': 'ASRL_DCD_STATE',
        'type': 'ViInt16'
    },
    1073676464: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute indicates the method used to terminate write operations. '
        },
        'name': 'ASRL_DISCARD_NULL',
        'type': 'ViBoolean'
    },
    1073676465: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute shows the current state of the Data Set Ready (DSR) input signal. '
        },
        'enum': 'LineState',
        'name': 'ASRL_DSR_STATE',
        'type': 'ViInt16'
    },
    1073676466: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute is used to manually assert or unassert the Data Terminal Ready (DTR) output signal. '
        },
        'enum': 'LineState',
        'name': 'ASRL_DTR_STATE',
        'type': 'ViInt16'
    },
    1073676467: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute indicates the method used to terminate read operations. '
        },
        'enum': 'AsrlEndIn',
        'name': 'ASRL_END_IN',
        'type': 'ViUInt16'
    },
    1073676468: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute indicates the method used to terminate write operations. '
        },
        'enum': 'AsrlEndOut',
        'name': 'ASRL_END_OUT',
        'type': 'ViUInt16'
    },
    1073676478: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the character to be placed in the user buffer when an error is detected (such as parity error). '
        },
        'name': 'ASRL_REPLACE_CHAR',
        'type': 'ViUInt8'
    },
    1073676479: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute represents the current state of the Ring Indicator (RI) input signal. The RI signal is often used by modems to indicate that the telephone line is ringing. This attribute is Read Only except when the VI_ATTR_ASRL_WIRE_MODE attribute is set to VI_ASRL_WIRE_232_DCE, or VI_ASRL_WIRE_232_AUTO with the hardware currently in the DCE state. '
        },
        'enum': 'LineState',
        'name': 'ASRL_RI_STATE',
        'type': 'ViInt16'
    },
    1073676480: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute is used to manually assert or unassert the Request To Send (RTS) output signal. When the VI_ATTR_ASRL_FLOW_CNTRL attribute is set to VI_ASRL_FLOW_RTS_CTS, this attribute is ignored when changed, but can be read to determine whether the background flow control is asserting or unasserting the signal. '
        },
        'enum': 'LineState',
        'name': 'ASRL_RTS_STATE',
        'type': 'ViInt16'
    },
    1073676481: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the character used to restart data flow when the flow control is set to VI_ASRL_FLOW_XON_XOFF. '
        },
        'name': 'ASRL_XON_CHAR',
        'type': 'ViUInt8'
    },
    1073676482: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the character used to temporarily pause data flow when the flow control is set to VI_ASRL_FLOW_XON_XOFF. '
        },
        'name': 'ASRL_XOFF_CHAR',
        'type': 'ViUInt8'
    },
    1073676483: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the modes in which the current window may be accessed. If VI_NMAPPED, the window is not currently mapped. If VI_USE_OPERS, the window can be accessed through the viPeekXX() and viPokeXX() operations only. VI_DEREF_ADDR specifies that you can either use operations or directly dereference the mapped address as a pointer. VI_DEREF_ADDR_BYTE_SWAP specifies that you can either use operations or dereference the mapped address as a pointer. If the mapped address is dereferenced as a pointer, the host byte order does not match the device byte order, byte-swapping is required. '
        },
        'enum': 'WinAccess',
        'name': 'WIN_ACCESS',
        'type': 'ViUInt16'
    },
    1073676501: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the logical address of the VXI or VME device used by the given session. For a VME device, the logical address is actually a pseudo-address in the range 256 to 511. For MEMACC sessions, this is the logical address of the local controller. '
        },
        'name': 'VXI_LA',
        'type': 'ViInt16'
    },
    1073676505: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute is the manufacturer identification number of the device. '
        },
        'name': 'MANF_ID',
        'type': 'ViUInt16'
    },
    1073676509: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the size of memory requested by the device in VXIbus address space. If the value of VI_ATTR_MEM_SPACE is VI_A16_SPACE, the value of this attribute is meaningless for VXI devices. '
        },
        'name': 'MEM_SIZE',
        'type': 'ViBusSize'
    },
    1073676510: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the VXIbus address space used by the device. The three types are A16 only, A16/A24, or A16/A32 memory address space. '
        },
        'enum': 'MemSpace',
        'name': 'MEM_SPACE',
        'type': 'ViUInt16'
    },
    1073676511: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the model code for the device. '
        },
        'name': 'MODEL_CODE',
        'type': 'ViUInt16'
    },
    1073676520: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the physical slot location of the device. If the slot number is not known, VI_UNKNOWN_SLOT is returned. '
        },
        'name': 'SLOT',
        'type': 'ViInt16'
    },
    1073676544: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies whether the device associated with this session is an immediate servant of the controller running VISA. '
        },
        'name': 'IMMEDIATE_SERV',
        'type': 'ViBoolean'
    },
    1073676545: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the board number of the GPIB board to which the GPIB-VXI is attached. '
        },
        'name': 'INTF_PARENT_NUM',
        'type': 'ViUInt16'
    },
    1073676656: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute returns the VISA specification version to which the object complies. The version value has a hexadecimal format 0xXXXYYYZZ, where XXX is the major version, YYY is the minor version, and ZZ is the subminor version. The subminor version is usually 0 for the specification version. '
        },
        'name': 'RSRC_SPEC_VERSION',
        'type': 'ViVersion'
    },
    1073676657: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the interface type of the given session. '
        },
        'name': 'INTF_TYPE',
        'type': 'ViUInt16'
    },
    1073676658: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the primary address of the GPIB device used by the given session. '
        },
        'name': 'GPIB_PRIMARY_ADDR',
        'type': 'ViUInt16'
    },
    1073676659: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the secondary address of the GPIB device used by the given session. If the device does not have a secondary address, the value of this attribute will be VI_NO_SEC_ADDR. '
        },
        'name': 'GPIB_SECONDARY_ADDR',
        'type': 'ViUInt16'
    },
    1073676661: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute value corresponds to the VXI manufacturer ID of the manufacturer that created the VISA implementation. '
        },
        'name': 'RSRC_MANF_ID',
        'type': 'ViUInt16'
    },
    1073676662: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the board number for the given interface. '
        },
        'name': 'INTF_NUM',
        'type': 'ViUInt16'
    },
    1073676663: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute is the identifier for the current triggering mechanism. This is a Read/Write attribute when the corresponding session is not enabled to receive trigger events. When the session is enabled to receive trigger events, this attribute is Read Only. This attribute is not available for all interfaces (such as serial). '
        },
        'enum': 'TrigId',
        'name': 'TRIG_ID',
        'type': 'ViInt16'
    },
    1073676673: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute shows the current state of the REN (Remote ENable) line. '
        },
        'enum': 'LineState',
        'name': 'GPIB_REN_STATE',
        'type': 'ViInt16'
    },
    1073676676: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies whether to unaddress the device (UNT and UNL) after each read or write operation. '
        },
        'name': 'GPIB_UNADDR_EN',
        'type': 'ViBoolean'
    },
    1073676681: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the 488 status byte of the local controller associated with this session. '
        },
        'name': 'DEV_STATUS_BYTE',
        'type': 'ViUInt8'
    },
    1073676690: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies whether viReadToFile() will overwrite (truncate) or append when opening a file. '
        },
        'name': 'FILE_APPEND_EN',
        'type': 'ViBoolean'
    },
    1073676692: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute shows which VXI trigger lines this implementation supports. This is a bit vector with bits 0-9 corresponding to VI_TRIG_TTL0 through VI_TRIG_ECL1. '
        },
        'name': 'VXI_TRIG_SUPPORT',
        'type': 'ViUInt32'
    },
    1073676695: {
        'access': 'read only',
        'documentation': {
            'description': ' This specifies the port number for a given TCPIP address. For a TCPIP SOCKET Resource, this is a required part of the address string. This attribute is valid only on TCPIP SOCKET sessions. '
        },
        'name': 'TCPIP_PORT',
        'type': 'ViUInt16'
    },
    1073676698: {
        'access': 'read-write',
        'documentation': {
            'description': ' The Nagle algorithm is disabled when this attribute is enabled (and vice versa). The Nagle algorithm improves network performance by buffering send data until a full-size packet can be sent. This attribute is enabled by default in VISA to verify that synchronous writes get flushed immediately. This attribute is valid only on TCPIP SOCKET sessions. '
        },
        'name': 'TCPIP_NODELAY',
        'type': 'ViBoolean'
    },
    1073676699: {
        'access': 'read-write',
        'documentation': {
            'description': ' Setting this attribute to VI_TRUE requests that a TCP/IP provider enable the use of keep-alive packets on TCP connections. After the system detects that a connection was dropped, VISA will return a lost connection error code VI_ERROR_CONN_LOST on subsequent I/O calls on the session. The time required for the system to detect that the connection was dropped is dependent on the system and is not settable. '
        },
        'name': 'TCPIP_KEEPALIVE',
        'type': 'ViBoolean'
    },
    1073676703: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies whether the device is 488.2 compliant. This attribute is valid only on VXI INSTR, GPIB-VXI INSTR, and USB INSTR sessions. '
        },
        'name': '4882_COMPLIANT',
        'type': 'ViBoolean'
    },
    1073676705: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the USB interface number used by the given session. '
        },
        'name': 'USB_INTFC_NUM',
        'type': 'ViInt16'
    },
    1073676706: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the endpoint number of the USB bulk-out or interrupt-out pipe used by the given session. This endpoint is used in viWrite and related operations. This attribute is valid only on USB RAW sessions. '
        },
        'name': 'USB_BULK_OUT_PIPE',
        'type': 'ViInt16'
    },
    1073676707: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the endpoint number of the USB bulk-in pipe used by the given session. This endpoint is used in viRead and related operations. This attribute is valid only on USB RAW sessions. '
        },
        'name': 'USB_BULK_IN_PIPE',
        'type': 'ViInt16'
    },
    1073676708: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the endpoint number of the USB interrupt-in pipe used by the given session. This endpoint is used in viEnableEvent for VI_EVENT_USB_INTR. This attribute is valid only on USB RAW sessions. '
        },
        'name': 'USB_INTR_IN_PIPE',
        'type': 'ViInt16'
    },
    1073676709: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the USB class used by the given session. This attribute is valid only on USB RAW sessions. '
        },
        'name': 'USB_CLASS',
        'type': 'ViInt16'
    },
    1073676710: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the USB subclass used by the given session. This attribute is valid only on USB RAW sessions. '
        },
        'name': 'USB_SUBCLASS',
        'type': 'ViInt16'
    },
    1073676711: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the USB protocol used by the given session. '
        },
        'name': 'USB_PROTOCOL',
        'type': 'ViInt16'
    },
    1073676712: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the USB alternate setting used by the given session. This attribute is valid only on USB RAW sessions. '
        },
        'name': 'USB_ALT_SETTING',
        'type': 'ViInt16'
    },
    1073676713: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute indicates the method used to terminate read operations. '
        },
        'enum': 'UsbEndIn',
        'name': 'USB_END_IN',
        'type': 'ViUInt16'
    },
    1073676714: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the number of interfaces supported by this USB device. This attribute is valid only on USB RAW sessions. '
        },
        'name': 'USB_NUM_INTFCS',
        'type': 'ViInt16'
    },
    1073676715: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the number of pipes supported by this USB interface. This attribute is valid only on USB RAW sessions. '
        },
        'name': 'USB_NUM_PIPES',
        'type': 'ViInt16'
    },
    1073676716: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies whether the USB bulk-out or interrupt-out pipe used by the given session is stalled or ready. This attribute is valid only on USB RAW sessions. '
        },
        'enum': 'UsbPipeState',
        'name': 'USB_BULK_OUT_STATUS',
        'type': 'ViInt16'
    },
    1073676717: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies whether the USB bulk-in pipe used by the given session is stalled or ready. This attribute is valid only on USB RAW sessions. '
        },
        'enum': 'UsbPipeState',
        'name': 'USB_BULK_IN_STATUS',
        'type': 'ViInt16'
    },
    1073676718: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies whether the USB interrupt-in pipe used by the given session is stalled or ready. This attribute is valid only on USB RAW sessions. '
        },
        'enum': 'UsbPipeState',
        'name': 'USB_INTR_IN_STATUS',
        'type': 'ViInt16'
    },
    1073676719: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the maximum size of data that will be stored by any given USB interrupt. If a USB interrupt contains more data than this size, the data in excess of this size will be lost. '
        },
        'name': 'USB_MAX_INTR_SIZE',
        'type': 'ViUInt16'
    },
    1073676720: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the endpoint address of the USB control pipe used by the given session. A value of 0 signifies that the default control pipe will be used. This endpoint is used in viUsbControlIn and viUsbControlOut operations. This attribute is valid only on USB RAW sessions. '
        },
        'name': 'USB_CTRL_PIPE',
        'type': 'ViInt16'
    },
    1073676731: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute indicates whether the port is properly connected to another port or device. This attribute is valid only with serial drivers developed by National Instruments and documented to support this feature with the corresponding National Instruments hardware. '
        },
        'name': 'ASRL_CONNECTED',
        'type': 'ViBoolean'
    },
    1073676732: {
        'access': 'read-write',
        'documentation': {
            'description': " This attribute lets you manually control the serial port's break state.  If asserted, it suspends character transmission and places the transmission line in a break state until this attribute is unasserted. If you want VISA to send a break signal after each write operation automatically, use the Break Len and ASRL End Out properties instead. "
        },
        'enum': 'LineState',
        'name': 'ASRL_BREAK_STATE',
        'type': 'ViInt16'
    },
    1073676733: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute controls the duration (in milliseconds) of the break signal asserted when ASRL End Out is set to Break(3). Valid values are 1-500. '
        },
        'name': 'ASRL_BREAK_LEN',
        'type': 'ViInt16'
    },
    1073676734: {
        'access': 'read-write',
        'documentation': {
            'description': ' If disabled (VI_FALSE), the serial port suspends transmission as if an XOFF character has been received. If enabled (VI_TRUE), it resumes transmission as if an XON character has been received.  If XON/XOFF flow control (software handshaking) is not being used, it is invalid to disable this attribute. '
        },
        'name': 'ASRL_ALLOW_TRANSMIT',
        'type': 'ViBoolean'
    },
    1073676735: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute represents the current wire/transceiver mode. For RS-485 hardware, this attribute is valid only with the RS-485 serial driver developed by National Instruments. For RS-232 hardware, the values RS232/DCE and RS232/AUTO are valid only with RS-232 serial drivers developed by National Instruments and documented to support this feature with the corresponding National Instruments hardware. When this feature is not supported, RS232/DTE is the only valid value. '
        },
        'enum': 'AsrlWireMode',
        'name': 'ASRL_WIRE_MODE',
        'type': 'ViInt16'
    },
    1073676784: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the upper 16 bits of the 48-bit destination address for a Firewire device. '
        },
        'name': 'FIREWIRE_DEST_UPPER_OFFSET',
        'type': 'ViUInt16'
    },
    1073676785: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the upper 16 bits of the 48-bit source address for a Firewire device. '
        },
        'name': 'FIREWIRE_SRC_UPPER_OFFSET',
        'type': 'ViUInt16'
    },
    1073676786: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the upper 16 bits of the 48-bit address for a Firewire device when a window is mapped. '
        },
        'name': 'FIREWIRE_WIN_UPPER_OFFSET',
        'type': 'ViUInt16'
    },
    1073676787: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the vendor identification of a Firewire device. '
        },
        'name': 'FIREWIRE_VENDOR_ID',
        'type': 'ViUInt32'
    },
    1073676788: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the lower chip ID of a Firewire device. '
        },
        'name': 'FIREWIRE_LOWER_CHIP_ID',
        'type': 'ViUInt32'
    },
    1073676789: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the upper chip ID of a Firewire device. '
        },
        'name': 'FIREWIRE_UPPER_CHIP_ID',
        'type': 'ViUInt8'
    },
    1073676801: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the device number of the PCI device used by the given session. '
        },
        'name': 'PXI_DEV_NUM',
        'type': 'ViUInt16'
    },
    1073676802: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the function number of the PCI device used by the given session. For most devices this will be 0, but a multifunction device may have a function number up to 7. The meaning of a function number other than 0 is device-specific. '
        },
        'name': 'PXI_FUNC_NUM',
        'type': 'ViUInt16'
    },
    1073676805: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the PCI bus number of this device. '
        },
        'name': 'PXI_BUS_NUM',
        'type': 'ViUInt16'
    },
    1073676806: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the PXI chassis number of this device. '
        },
        'name': 'PXI_CHASSIS',
        'type': 'ViInt16'
    },
    1073676808: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the slot number or special feature connected to the local bus left lines of this device. '
        },
        'name': 'PXI_SLOT_LBUS_LEFT',
        'type': 'ViInt16'
    },
    1073676809: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the slot number or special feature connected to the local bus right lines of this device. '
        },
        'name': 'PXI_SLOT_LBUS_RIGHT',
        'type': 'ViInt16'
    },
    1073676810: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the trigger bus number of this device. '
        },
        'name': 'PXI_TRIG_BUS',
        'type': 'ViInt16'
    },
    1073676811: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the star trigger bus number of this device. '
        },
        'name': 'PXI_STAR_TRIG_BUS',
        'type': 'ViInt16'
    },
    1073676812: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the PXI_STAR line connected to this device. '
        },
        'name': 'PXI_STAR_TRIG_LINE',
        'type': 'ViInt16'
    },
    1073676813: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the segment to use to qualify trigSrc in viMapTrigger. '
        },
        'name': 'PXI_SRC_TRIG_BUS',
        'type': 'ViInt16'
    },
    1073676814: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the segment to use to qualify trigDest in viMapTrigger. '
        },
        'name': 'PXI_DEST_TRIG_BUS',
        'type': 'ViInt16'
    },
    1073676817: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies what type of address requirements (memory or I/O) the device has for this Base Address Register. If the device does not request addresses in this space, the value will be VI_PXI_ADDR_NONE. '
        },
        'enum': 'PxiMemType',
        'name': 'PXI_MEM_TYPE_BAR0',
        'type': 'ViUInt16'
    },
    1073676818: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies what type of address requirements (memory or I/O) the device has for this Base Address Register. If the device does not request addresses in this space, the value will be VI_PXI_ADDR_NONE. '
        },
        'enum': 'PxiMemType',
        'name': 'PXI_MEM_TYPE_BAR1',
        'type': 'ViUInt16'
    },
    1073676819: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies what type of address requirements (memory or I/O) the device has for this Base Address Register. If the device does not request addresses in this space, the value will be VI_PXI_ADDR_NONE. '
        },
        'enum': 'PxiMemType',
        'name': 'PXI_MEM_TYPE_BAR2',
        'type': 'ViUInt16'
    },
    1073676820: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies what type of address requirements (memory or I/O) the device has for this Base Address Register. If the device does not request addresses in this space, the value will be VI_PXI_ADDR_NONE. '
        },
        'enum': 'PxiMemType',
        'name': 'PXI_MEM_TYPE_BAR3',
        'type': 'ViUInt16'
    },
    1073676821: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies what type of address requirements (memory or I/O) the device has for this Base Address Register. If the device does not request addresses in this space, the value will be VI_PXI_ADDR_NONE. '
        },
        'enum': 'PxiMemType',
        'name': 'PXI_MEM_TYPE_BAR4',
        'type': 'ViUInt16'
    },
    1073676822: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies what type of address requirements (memory or I/O) the device has for this Base Address Register. If the device does not request addresses in this space, the value will be VI_PXI_ADDR_NONE. '
        },
        'enum': 'PxiMemType',
        'name': 'PXI_MEM_TYPE_BAR5',
        'type': 'ViUInt16'
    },
    1073676833: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the system-assigned base this device uses in the given space. If the device does not request addresses in this space, the value of this attribute is meaningless. '
        },
        'name': 'PXI_MEM_BASE_BAR0',
        'type': 'ViUInt32'
    },
    1073676834: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the system-assigned base this device uses in the given space. If the device does not request addresses in this space, the value of this attribute is meaningless. '
        },
        'name': 'PXI_MEM_BASE_BAR1',
        'type': 'ViUInt32'
    },
    1073676835: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the system-assigned base this device uses in the given space. If the device does not request addresses in this space, the value of this attribute is meaningless. '
        },
        'name': 'PXI_MEM_BASE_BAR2',
        'type': 'ViUInt32'
    },
    1073676836: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the system-assigned base this device uses in the given space. If the device does not request addresses in this space, the value of this attribute is meaningless. '
        },
        'name': 'PXI_MEM_BASE_BAR3',
        'type': 'ViUInt32'
    },
    1073676837: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the system-assigned base this device uses in the given space. If the device does not request addresses in this space, the value of this attribute is meaningless. '
        },
        'name': 'PXI_MEM_BASE_BAR4',
        'type': 'ViUInt32'
    },
    1073676838: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the system-assigned base this device uses in the given space. If the device does not request addresses in this space, the value of this attribute is meaningless. '
        },
        'name': 'PXI_MEM_BASE_BAR5',
        'type': 'ViUInt32'
    },
    1073676849: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the requested address size of this device in the given space. If the device does not request addresses in this space, the value of this attribute is meaningless. If this value cannot be safely determined, the value of this attribute will be 0xFFFFFFFF. '
        },
        'name': 'PXI_MEM_SIZE_BAR0',
        'type': 'ViUInt32'
    },
    1073676850: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the requested address size of this device in the given space. If the device does not request addresses in this space, the value of this attribute is meaningless. If this value cannot be safely determined, the value of this attribute will be 0xFFFFFFFF. '
        },
        'name': 'PXI_MEM_SIZE_BAR1',
        'type': 'ViUInt32'
    },
    1073676851: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the requested address size of this device in the given space. If the device does not request addresses in this space, the value of this attribute is meaningless. If this value cannot be safely determined, the value of this attribute will be 0xFFFFFFFF. '
        },
        'name': 'PXI_MEM_SIZE_BAR2',
        'type': 'ViUInt32'
    },
    1073676852: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the requested address size of this device in the given space. If the device does not request addresses in this space, the value of this attribute is meaningless. If this value cannot be safely determined, the value of this attribute will be 0xFFFFFFFF. '
        },
        'name': 'PXI_MEM_SIZE_BAR3',
        'type': 'ViUInt32'
    },
    1073676853: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the requested address size of this device in the given space. If the device does not request addresses in this space, the value of this attribute is meaningless. If this value cannot be safely determined, the value of this attribute will be 0xFFFFFFFF. '
        },
        'name': 'PXI_MEM_SIZE_BAR4',
        'type': 'ViUInt32'
    },
    1073676854: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the requested address size of this device in the given space. If the device does not request addresses in this space, the value of this attribute is meaningless. If this value cannot be safely determined, the value of this attribute will be 0xFFFFFFFF. '
        },
        'name': 'PXI_MEM_SIZE_BAR5',
        'type': 'ViUInt32'
    },
    1073676864: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies whether the device is PXI/PCI or PXI/PCI Express. '
        },
        'name': 'PXI_IS_EXPRESS',
        'type': 'ViBoolean'
    },
    1073676865: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the PCI Express link width of the PXI Express peripheral slot in which the device resides. '
        },
        'name': 'PXI_SLOT_LWIDTH',
        'type': 'ViInt16'
    },
    1073676866: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the maximum PCI Express link width of the device. '
        },
        'name': 'PXI_MAX_LWIDTH',
        'type': 'ViInt16'
    },
    1073676867: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the PCI Express link width negotiated between the PCI Express host controller and the device. '
        },
        'name': 'PXI_ACTUAL_LWIDTH',
        'type': 'ViInt16'
    },
    1073676868: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the differential star bus number of this device. A value of -1 means that the chassis is unidentified or does not have a timing slot. '
        },
        'name': 'PXI_DSTAR_BUS',
        'type': 'ViInt16'
    },
    1073676869: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies the set of differential star lines connected to this device. A value of -1 means that the chassis is unidentified or does not have a timing slot. '
        },
        'name': 'PXI_DSTAR_SET',
        'type': 'ViInt16'
    },
    1073676870: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether the implementation should attempt to combine bus write transfers into a larger transfer before bursting over the PCI bus. '
        },
        'name': 'PXI_ALLOW_WRITE_COMBINE',
        'type': 'ViBoolean'
    },
    1073676871: {
        'access': 'read only',
        'documentation': {
            'description': ' The number of slots occupied by this device. The value for non-PXI-Express devices is always 1. '
        },
        'name': 'PXI_SLOT_WIDTH',
        'type': 'ViUInt16'
    },
    1073676872: {
        'access': 'read only',
        'documentation': {
            'description': ' The number of slots occupied by the module to the left of the slot where this devfice connects to the PXI backplane. The value for non-PXI-Express devices is always 0. '
        },
        'name': 'PXI_SLOT_OFFSET',
        'type': 'ViUInt16'
    },
    1073676915: {
        'access': 'read only',
        'documentation': {
            'description': ' Indicates whether the certificate expires. Note that this may indicate that the certificate is from an IDevID. '
        },
        'name': 'TCPIP_SERVER_CERT_IS_PERPETUAL',
        'type': 'ViBoolean'
    },
    1073676919: {
        'access': 'read only',
        'documentation': {
            'description': ' The buffer size of the buffer required to hold the full text of the server certificate in RFC 5652 PEM format. '
        },
        'name': 'TCPIP_SERVER_CERT_SIZE',
        'type': 'ViUInt32'
    },
    1073677056: {
        'access': 'read-write',
        'documentation': {
            'description': " This enables HiSLIP 'Overlap' mode and its value defaults to the mode suggested by the instrument on HiSLIP connection. If disabled, the connection uses 'Synchronous' mode to detect and recover from interrupted errors. If enabled, the connection uses 'Overlapped' mode to allow overlapped responses. If changed, VISA will do a Device Clear operation to change the mode. "
        },
        'name': 'TCPIP_HISLIP_OVERLAP_EN',
        'type': 'ViBoolean'
    },
    1073677057: {
        'access': 'read only',
        'documentation': {
            'description': ' This is the HiSLIP protocol version used for a particular HiSLIP connetion. Currently, HiSLIP version 1.0 would return a ViVersion value of 0x00100000. '
        },
        'name': 'TCPIP_HISLIP_VERSION',
        'type': 'ViVersion'
    },
    1073677058: {
        'access': 'read-write',
        'documentation': {
            'description': ' This is the maximum HiSLIP message size VISA will accept from a HiSLIP system in units of kilobytes (1024 bytes). This defaults to 1024 (a 1 MB maximum message size). '
        },
        'name': 'TCPIP_HISLIP_MAX_MESSAGE_KB',
        'type': 'ViUInt32'
    },
    1073677059: {
        'access': 'read only',
        'documentation': {
            'description': ' Specifies whether this resource uses the HiSLIP protocol. '
        },
        'name': 'TCPIP_IS_HISLIP',
        'type': 'ViBoolean'
    },
    1073677060: {
        'access': 'read-write',
        'documentation': {
            'description': ' This is used to control and indicate if the communication is encrypted. '
        },
        'name': 'TCPIP_HISLIP_ENCRYPTION_EN',
        'type': 'ViBoolean'
    },
    1073692678: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute contains the job ID of the asynchronous operation that has completed. This is valid for the VI_EVENT_IO_COMPLETION only. '
        },
        'name': 'JOB_ID',
        'type': 'ViJobId'
    },
    1073692688: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute is the unique logical identifier for the event type of the specified event. '
        },
        'name': 'EVENT_TYPE',
        'type': 'ViEventType'
    },
    1073692689: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute is the 16-bit Status/ID value retrieved during the IACK cycle or from the Signal register. This is valid for the VI_EVENT_VXI_SIGP only. '
        },
        'name': 'SIGP_STATUS_ID',
        'type': 'ViUInt16'
    },
    1073692690: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute identifies the triggering mechanism on which the specified trigger event was received. This is valid for the VI_EVENT_TRIG only. '
        },
        'enum': 'TrigId',
        'name': 'RECV_TRIG_ID',
        'type': 'ViInt16'
    },
    1073692707: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute value is the 32-bit status/ID retrieved during the IACK cycle. This is valid for the VI_EVENT_VXI_VME_INTR only. '
        },
        'name': 'INTR_STATUS_ID',
        'type': 'ViUInt32'
    },
    1073692709: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute contains the return code of the operation generating this event. This is valid for the VI_EVENT_IO_COMPLETION, VI_EVENT_EXCEPTION, and VI_EVENT_USB_INTR events. '
        },
        'name': 'STATUS',
        'type': 'ViStatus'
    },
    1073692710: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute contains the actual number of elements that were asynchronously transferred. This is valid for the VI_EVENT_IO_COMPLETION only. '
        },
        'name': 'RET_COUNT',
        'type': 'ViUInt32'
    },
    1073692711: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute contains the address of a buffer that was used in an asynchronous operation. This is valid for the VI_EVENT_IO_COMPLETION only. '
        },
        'name': 'BUFFER',
        'type': 'ViUInt8 []'
    },
    1073692737: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute value is the VXI interrupt level on which the interrupt was received. This is valid for the VI_EVENT_VXI_VME_INTR only. '
        },
        'name': 'RECV_INTR_LEVEL',
        'type': 'ViInt16'
    },
    1073692739: {
        'access': 'read-write',
        'documentation': {
            'description': " This attribute specifies which VXI TLL triggers have mappings. This is a bit vector where bits 0-7 represent TTL triggers 0-7 respectively. A bit value of 0 means the corresponding trigger line is unmapped, and 1 means a mapping exists. Use VI_ATTR_VXI_TRIG_DIR to set an enabled line's direction. Bits 8 and 9 are reserved for future use. This attribute only applies to VXI INSTR Resources. "
        },
        'name': 'VXI_TRIG_LINES_EN',
        'type': 'ViUInt16'
    },
    1073692740: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the directions of the mapped TTL triggers lines. This is a bit vector where bits 0-7 represent TTL triggers 0-7 respectively. A bit value of 0 means the corresponding line is routed out of the frame, and a value of 1 means the line is routed into the frame. Lines must be enabled using VI_ATTR_VXI_TRIG_LINES_EN. Bits 8 and 9 are reserved for future use. This attribute only applies to VXI INSTR Resources. '
        },
        'name': 'VXI_TRIG_DIR',
        'type': 'ViUInt16'
    },
    1073693075: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute specifies whether the local controller has gained or lost CIC status. This is valid for the VI_EVENT_GPIB_CIC event. '
        },
        'name': 'GPIB_RECV_CIC_STATE',
        'type': 'ViBoolean'
    },
    1073693104: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute value is the number of bytes of USB interrupt data that is stored. This is valid for the VI_EVENT_USB_INTR event. '
        },
        'name': 'USB_RECV_INTR_SIZE',
        'type': 'ViUInt16'
    },
    1073693248: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute value is the index of the interrupt sequence that detected the interrupt condition. This is valid for the VI_EVENT_PXI_INTR event. '
        },
        'name': 'PXI_RECV_INTR_SEQ',
        'type': 'ViInt16'
    },
    1073693249: {
        'access': 'read only',
        'documentation': {
            'description': ' This attribute value is the first PXI/PCI register that was read in the successful interrupt detection sequence. This is valid for the VI_EVENT_PXI_INTR event. '
        },
        'name': 'PXI_RECV_INTR_DATA',
        'type': 'ViUInt32'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/visa/attributes_addon.py sha256=cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f bytes=207 -->
## FILE: source/codegen/metadata/visa/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/visa/attributes_addon.py`
- sha256: `cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f`
- bytes: 207

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/visa/config.py sha256=edd4de003ca483ce8c94ba7b8e4ebfea27294a810a6cff61cac85428af3e8dd2 bytes=1168 -->
## FILE: source/codegen/metadata/visa/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/visa/config.py`
- sha256: `edd4de003ca483ce8c94ba7b8e4ebfea27294a810a6cff61cac85428af3e8dd2`
- bytes: 1168

````python
# -*- coding: utf-8 -*-
config = {
    'additional_headers': {},
    'api_version': '23.0.0',
    'c_function_prefix': 'vi',
    'c_header': 'visa.h',
    'close_function': 'Close',
    'csharp_namespace': 'NationalInstruments.Grpc.Visa',
    'custom_header_suffix': '_attributes.h',
    'custom_types': [],
    'driver_name': 'VISA',
    'extra_errors_used': [],
    'init_function': 'Open',
    'java_package': 'com.ni.grpc.visa',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'visa',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'visa32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'visa64.dll',
                'type': 'cdll'
            }
        }
    },
    'linux_rt_support': True,
    'metadata_version': '0.1',
    'module_name': 'visa',
    'namespace_component': 'visa',
    'resource_handle_type': ['ViSession','ViObject'],
    'service_class_prefix': 'Visa',
    'session_handle_parameter_name': 'vi',
    'status_ok': 'status >= 0'
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/visa/config_addon.py sha256=d89084eb696ad3171488ab595af6d7415b8f7b9e66cd2472808ce19490a19b58 bytes=226 -->
## FILE: source/codegen/metadata/visa/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/visa/config_addon.py`
- sha256: `d89084eb696ad3171488ab595af6d7415b8f7b9e66cd2472808ce19490a19b58`
- bytes: 226

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.3.dev0',
    'latest_runtime_version_tested_against': '20.5.0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/visa/custom_header.mako sha256=8ab80b9270e30517023bccb956c4444e182d28ff363d9a9aa0f24223608b2697 bytes=3107 -->
## FILE: source/codegen/metadata/visa/custom_header.mako

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/visa/custom_header.mako`
- sha256: `8ab80b9270e30517023bccb956c4444e182d28ff363d9a9aa0f24223608b2697`
- bytes: 3107

````mako
<%
attributes = data['attributes']
config = data['config']
namespace_prefix = config["namespace_component"] + "_grpc"

u8_attrs = []
i16_attrs = []
u16_attrs = []
i32_attrs = []
u32_attrs = []
u64_attrs = []
bool_attrs = []
string_attrs = []
bytes_attrs = []

for key, attr in attributes.items():
    attr_type = attr["type"]
    attr_name = f"VI_ATTR_{attr['name']}"
    if ("_BASE" in attr['name']
      or "_COUNT" in attr['name']
      or "MEM_SIZE" in attr['name']
      or "WIN_SIZE" in attr['name']
    ):
        u32_attrs.append(f"{attr_name}_32")
        u64_attrs.append(f"{attr_name}_64")
    elif attr_type in ["ViUInt8"]:
        u8_attrs.append(attr_name)
    elif attr_type in ["ViInt16"]:
        i16_attrs.append(attr_name)
    elif attr_type in ["ViUInt16"]:
        u16_attrs.append(attr_name)
    elif attr_type in ["ViInt32", "ViStatus"]:
        i32_attrs.append(attr_name)
    elif attr_type in ["ViUInt32", "ViVersion", "ViAccessMode", "ViJobId", "ViEventType"]:
        u32_attrs.append(attr_name)
    elif attr_type in ["ViBusAddress", "ViBusSize", "ViAddr"]:
        u64_attrs.append(attr_name)
    elif attr_type in ["ViBoolean"]:
        bool_attrs.append(attr_name)
    elif attr_type in ["ViString"]:
        string_attrs.append(attr_name)
    elif attr_type in ["ViUInt8 []"]:
        bytes_attrs.append(attr_name)
    else:
        raise Exception(f"Unknown attribute type for {attr_name}")
%>
//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
#ifndef VISA_ATTRIBUTE_TYPES_H
#define VISA_ATTRIBUTE_TYPES_H

#define NIVISA_USB

#include <visa.h>
#include <visa/visa_service.h>

namespace ${namespace_prefix} {

  inline AttributeValueData::DataCase GetAttributeType(ViAttr attributeID)
  {
    switch (attributeID) {
% for attr in sorted(u8_attrs):
      case ${attr}:
% endfor
        return AttributeValueData::kValueU8;

% for attr in sorted(i16_attrs):
      case ${attr}:
% endfor
        return AttributeValueData::kValueI16;

% for attr in sorted(u16_attrs):
      case ${attr}:
% endfor
        return AttributeValueData::kValueU16;

% for attr in sorted(i32_attrs):
      case ${attr}:
% endfor
        return AttributeValueData::kValueI32;

% for attr in sorted(u32_attrs):
      case ${attr}:
% endfor
        return AttributeValueData::kValueU32;

% for attr in sorted(u64_attrs):
      case ${attr}:
% endfor
        return AttributeValueData::kValueU64;

% for attr in sorted(bool_attrs):
      case ${attr}:
% endfor
        return AttributeValueData::kValueBool;

% for attr in sorted(string_attrs):
      case ${attr}:
% endfor
        return AttributeValueData::kValueString;

% for attr in sorted(bytes_attrs):
      case ${attr}:
% endfor
        return AttributeValueData::kValueBytes;

      default:
        return AttributeValueData::DATA_NOT_SET;
      }
  }
}

#endif
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/visa/custom_proto.mako sha256=d7916791be5a488b77d80428a64eef462e31c5f081011227abd4073a9643fddd bytes=298 -->
## FILE: source/codegen/metadata/visa/custom_proto.mako

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/visa/custom_proto.mako`
- sha256: `d7916791be5a488b77d80428a64eef462e31c5f081011227abd4073a9643fddd`
- bytes: 298

````mako
message AttributeValueData {
  oneof data {
    uint32 value_u8 = 1;
    int32 value_i16 = 2;
    uint32 value_u16 = 3;
    int32 value_i32 = 4;
    uint32 value_u32 = 5;
    fixed64 value_u64 = 6;
    bool value_bool = 7;
    string value_string = 8;
    bytes value_bytes = 9;
  }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/visa/enums.py sha256=7cb3d0988c87e01899c6ebf909bc4c426962b9445010dfd6a7bb6871cb220094 bytes=37922 -->
## FILE: source/codegen/metadata/visa/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/visa/enums.py`
- sha256: `7cb3d0988c87e01899c6ebf909bc4c426962b9445010dfd6a7bb6871cb220094`
- bytes: 37922

````python
enums = {
    'AccessPriv': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies supervisory (privileged) data accesses'
                },
                'name': 'DATA_PRIV',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Specifies user (nonprivileged) data accesses'
                },
                'name': 'DATA_NPRIV',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Specifies supervisory (privileged) program accesses'
                },
                'name': 'PROG_PRIV',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Specifies user (nonprivileged) program accesses'
                },
                'name': 'PROG_NPRIV',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Specifies supervisory (privileged) block accesses'
                },
                'name': 'BLCK_PRIV',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Specifies user (nonprivileged) block accesses'
                },
                'name': 'BLCK_NPRIV',
                'value': 5
            },
            {
                'documentation': {
                    'description': 'Specifies supervisory (privileged) D64 accesses'
                },
                'name': 'D64_PRIV',
                'value': 6
            },
            {
                'documentation': {
                    'description': 'Specifies user (nonprivileged) D64 accesses'
                },
                'name': 'D64_NPRIV',
                'value': 7
            }
        ]
    },
    'AddressSpace': {
        'values': [
            {
                'name': 'LOCAL_SPACE',
                'value': 0
            },
            {
                'name': 'A16_SPACE',
                'value': 1
            },
            {
                'name': 'A24_SPACE',
                'value': 2
            },
            {
                'name': 'A32_SPACE',
                'value': 3
            },
            {
                'name': 'A64_SPACE',
                'value': 4
            },
            {
                'name': 'PXI_ALLOC_SPACE',
                'value': 9
            },
            {
                'name': 'PXI_CFG_SPACE',
                'value': 10
            },
            {
                'name': 'PXI_BAR0_SPACE',
                'value': 11
            },
            {
                'name': 'PXI_BAR1_SPACE',
                'value': 12
            },
            {
                'name': 'PXI_BAR2_SPACE',
                'value': 13
            },
            {
                'name': 'PXI_BAR3_SPACE',
                'value': 14
            },
            {
                'name': 'PXI_BAR4_SPACE',
                'value': 15
            },
            {
                'name': 'PXI_BAR5_SPACE',
                'value': 16
            },
            {
                'name': 'OPAQUE_SPACE',
                'value': 65535
            }
        ]
    },
    'AsrlEndIn': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies that there is no END indicator for read operations, so reads will not terminate until all of the requested data is received (or an error occurs)'
                },
                'name': 'NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Specifies that any byte with the highest bit set is to be treated as an END indicator'
                },
                'name': 'LAST_BIT',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Specifies that the termination character (specified by VI_ATTR_TERMCHAR) is to be treated as an END indicator (VI_ATTR_TERMCHAR_EN is ignored)'
                },
                'name': 'TERMCHAR',
                'value': 2
            }
        ]
    },
    'AsrlEndOut': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies that there is no END indicator for write operations, so writes will not append anything to the data being written'
                },
                'name': 'NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Specifies that the last byte (and only the last byte) be sent with the highest bit set'
                },
                'name': 'LAST_BIT',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Specifies that the termination character (specified by VI_ATTR_TERMCHAR) is to be appended to each buffer written when VI_SEND_END_EN is true'
                },
                'name': 'TERMCHAR',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Specifies that a BREAK be sent after the last byte of each write operation'
                },
                'name': 'BREAK',
                'value': 3
            }
        ]
    },
    'AsrlFlow': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies that no flow control is to be used, and buffers on both sides of the connection are assumed to be large enough to hold all data transferred'
                },
                'name': 'NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Specifies that software handshaking is to be used (XON and XOFF)'
                },
                'name': 'XON_XOFF',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Specifies that hardware handshaking is to be used (RTS output signal and CTS input signal)'
                },
                'name': 'RTS_CTS',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Specifies that hardware handshaking is to be used (DTR output signal and DSR input signal)'
                },
                'name': 'DTR_DSR',
                'value': 4
            }
        ]
    },
    'AsrlParity': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies that no parity bit exists'
                },
                'name': 'NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Specifies that odd parity should be used'
                },
                'name': 'ODD',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Specifies that even parity should be used'
                },
                'name': 'EVEN',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Specifies that the parity bit exists and is always 1'
                },
                'name': 'MARK',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Specifies that the parity bit exists and is always 0'
                },
                'name': 'SPACE',
                'value': 4
            }
        ]
    },
    'AsrlStop': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies that 1 stop bit is used per frame'
                },
                'name': 'ONE',
                'value': 10
            },
            {
                'documentation': {
                    'description': 'Specifies that 1.5 (one and one-half) stop bits are used per frame'
                },
                'name': 'ONE5',
                'value': 15
            },
            {
                'documentation': {
                    'description': 'Specifies that 2 stop bits are used per frame'
                },
                'name': 'TWO',
                'value': 20
            }
        ]
    },
    'AsrlWireMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies that the RS-485 wire mode is 4-wire mode'
                },
                'name': 'WIRE_485_4',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Specifies that the RS-485 wire mode is 2-wire DTR mode controlled with echo'
                },
                'name': 'WIRE_485_2_DTR_ECHO',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Specifies that the RS-485 wire mode is 2-wire DTR mode controlled without echo'
                },
                'name': 'WIRE_485_2_DTR_CTRL',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Specifies that the RS-485 wire mode is 2-wire auto mode controlled with TXRDY'
                },
                'name': 'WIRE_485_2_AUTO',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Specifies that the RS-232 wire mode is DTE mode'
                },
                'name': 'WIRE_232_DTE',
                'value': 128
            },
            {
                'documentation': {
                    'description': 'Specifies that the RS-232 wire mode is DCE mode'
                },
                'name': 'WIRE_232_DCE',
                'value': 129
            },
            {
                'documentation': {
                    'description': 'Specifies that the RS-232 wire mode is automatically detected by the hardware'
                },
                'name': 'WIRE_232_AUTO',
                'value': 130
            }
        ]
    },
    'AssertInterruptSignalMode': {
        'values': [
            {
                'name': 'ASSERT_IRQ1',
                'value': 1
            },
            {
                'name': 'ASSERT_IRQ2',
                'value': 2
            },
            {
                'name': 'ASSERT_IRQ3',
                'value': 3
            },
            {
                'name': 'ASSERT_IRQ4',
                'value': 4
            },
            {
                'name': 'ASSERT_IRQ5',
                'value': 5
            },
            {
                'name': 'ASSERT_IRQ6',
                'value': 6
            },
            {
                'name': 'ASSERT_IRQ7',
                'value': 7
            },
            {
                'name': 'ASSERT_SIGNAL',
                'value': -1
            },
            {
                'name': 'ASSERT_USE_ASSIGNED',
                'value': 0
            }
        ]
    },
    'AssertUtilSignalMode': {
        'values': [
            {
                'name': 'UTIL_ASSERT_SYSRESET',
                'value': 1
            },
            {
                'name': 'UTIL_ASSERT_SYSFAIL',
                'value': 2
            },
            {
                'name': 'UTIL_DEASSERT_SYSFAIL',
                'value': 3
            }
        ]
    },
    'BufferMask': {
        'values': [
            {
                'name': 'IO_IN_BUF',
                'value': 16
            },
            {
                'name': 'IO_OUT_BUF',
                'value': 32
            },
            {
                'name': 'IO_IN_BUF_DISCARD',
                'value': 64
            },
            {
                'name': 'IO_OUT_BUF_DISCARD',
                'value': 128
            }
        ]
    },
    'ByteOrder': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies Big Endian (Motorola) byte order accesses'
                },
                'name': 'BIG_ENDIAN',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Specifies Little Endian (Intel) byte order accesses'
                },
                'name': 'LITTLE_ENDIAN',
                'value': 1
            }
        ]
    },
    'EventMechanism': {
        'values': [
            {
                'name': 'QUEUE',
                'value': 1
            },
            {
                'name': 'HNDLR',
                'value': 2
            },
            {
                'name': 'SUSPEND_HNDLR',
                'value': 4
            },
            {
                'name': 'ALL_MECH',
                'value': 65535
            }
        ]
    },
    'EventType': {
        'values': [
            {
                'name': 'ALL_ENABLED_EVENTS',
                'value': 1073709055
            },
            {
                'name': 'EVENT_ASRL_BREAK',
                'value': 1073684515
            },
            {
                'name': 'EVENT_ASRL_CTS',
                'value': 1073684521
            },
            {
                'name': 'EVENT_ASRL_DSR',
                'value': 1073684522
            },
            {
                'name': 'EVENT_ASRL_DCD',
                'value': 1073684524
            },
            {
                'name': 'EVENT_ASRL_RI',
                'value': 1073684526
            },
            {
                'name': 'EVENT_ASRL_CHAR',
                'value': 1073684533
            },
            {
                'name': 'EVENT_ASRL_TERMCHAR',
                'value': 1073684516
            },
            {
                'name': 'EVENT_IO_COMPLETION',
                'value': 1073684489
            },
            {
                'name': 'EVENT_TRIG',
                'value': -1073799158
            },
            {
                'name': 'EVENT_SERVICE_REQ',
                'value': 1073684491
            },
            {
                'name': 'EVENT_CLEAR',
                'value': 1073684493
            },
            {
                'name': 'EVENT_EXCEPTION',
                'value': -1073799154
            },
            {
                'name': 'EVENT_GPIB_CIC',
                'value': 1073684498
            },
            {
                'name': 'EVENT_GPIB_TALK',
                'value': 1073684499
            },
            {
                'name': 'EVENT_GPIB_LISTEN',
                'value': 1073684500
            },
            {
                'name': 'EVENT_VXI_VME_SYSFAIL',
                'value': 1073684509
            },
            {
                'name': 'EVENT_VXI_VME_SYSRESET',
                'value': 1073684510
            },
            {
                'name': 'EVENT_VXI_SIGP',
                'value': 1073684512
            },
            {
                'name': 'EVENT_VXI_VME_INTR',
                'value': -1073799135
            },
            {
                'name': 'EVENT_PXI_INTR',
                'value': 1073684514
            },
            {
                'name': 'EVENT_TCPIP_CONNECT',
                'value': 1073684534
            },
            {
                'name': 'EVENT_USB_INTR',
                'value': 1073684535
            }
        ]
    },
    'FdcMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Uses normal FDC transfers'
                },
                'name': 'NORMAL',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Uses FDC stream transfers'
                },
                'name': 'STREAM',
                'value': 2
            }
        ]
    },
    'GpibAddr': {
        'values': [
            {
                'documentation': {
                    'description': 'The GPIB controller is not addressed'
                },
                'name': 'UNADDRESSED',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The GPIB controller is addressed to talk'
                },
                'name': 'TALKER',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'The GPIB controller is addressed to listen'
                },
                'name': 'LISTENER',
                'value': 2
            }
        ]
    },
    'GpibControlAtnMode': {
        'values': [
            {
                'name': 'ATN_DEASSERT',
                'value': 0
            },
            {
                'name': 'ATN_ASSERT',
                'value': 1
            },
            {
                'name': 'ATN_DEASSERT_HANDSHAKE',
                'value': 2
            },
            {
                'name': 'ATN_ASSERT_IMMEDIATE',
                'value': 3
            }
        ]
    },
    'GpibControlRenMode': {
        'values': [
            {
                'name': 'REN_DEASSERT',
                'value': 0
            },
            {
                'name': 'REN_ASSERT',
                'value': 1
            },
            {
                'name': 'REN_DEASSERT_GTL',
                'value': 2
            },
            {
                'name': 'REN_ASSERT_ADDRESS',
                'value': 3
            },
            {
                'name': 'REN_ASSERT_LLO',
                'value': 4
            },
            {
                'name': 'REN_ASSERT_ADDRESS_LLO',
                'value': 5
            },
            {
                'name': 'REN_ADDRESS_GTL',
                'value': 6
            }
        ]
    },
    'GpibHighSpeedCableLen': {
        'values': [
            {
                'documentation': {
                    'description': 'Not implemented'
                },
                'name': 'HS488_NIMPL',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'Disabled'
                },
                'name': 'HS488_DISABLED',
                'value': 0
            }
        ]
    },
    'IoProt': {
        'values': [
            {
                'documentation': {
                    'description': 'Normal protocol (meaning depends on interface type)'
                },
                'name': 'PROT_NORMAL',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Fast Data Channel (requires FDC-capable device)'
                },
                'name': 'PROT_FDC',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'High-Speed 488 transfers (valid for GPIB only)'
                },
                'name': 'PROT_HS488',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Use 488.2 commands for a Serial or Ethernet device (valid for ASRL, TCPIP, and USB only)'
                },
                'name': 'PROT_4882_STRS',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Vendor-specific transfers (valid for USB-TMC only)'
                },
                'name': 'PROT_USBTMC_VENDOR',
                'value': 5
            }
        ]
    },
    'LineState': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies that the line is currently asserted (for viGetAttribute) or should be asserted (for viSetAttribute)'
                },
                'name': 'ASSERTED',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Specifies that the line is currently unasserted (for viGetAttribute) or should be unasserted (for viSetAttribute)'
                },
                'name': 'UNASSERTED',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Specifies that the state of the line is currently unknown'
                },
                'name': 'UNKNOWN',
                'value': -1
            }
        ]
    },
    'LockState': {
        'values': [
            {
                'documentation': {
                    'description': 'The resource is not currently locked'
                },
                'name': 'NO_LOCK',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The resource has an exclusive lock (one session only)'
                },
                'name': 'EXCLUSIVE_LOCK',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'The resource has a lock that can be shared by multiple sessions'
                },
                'name': 'SHARED_LOCK',
                'value': 2
            }
        ]
    },
    'MemSpace': {
        'values': [
            {
                'documentation': {
                    'description': 'Device has memory in A16 space only'
                },
                'name': 'A16_SPACE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Device has memory in A24 space (for a VXI device, this is in addition to the A16 registers)'
                },
                'name': 'A24_SPACE',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Device has memory in A32 space (for a VXI device, this is in addition to the A16 registers)'
                },
                'name': 'A32_SPACE',
                'value': 3
            }
        ]
    },
    'PxiMemType': {
        'values': [
            {
                'documentation': {
                    'description': 'The device has no address requirements in this space'
                },
                'name': 'NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The device has memory address requirements in this space'
                },
                'name': 'MEM',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'The device has I/O address requirements in this space'
                },
                'name': 'IO',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'The device has configuration registers in this space'
                },
                'name': 'CFG',
                'value': 3
            }
        ]
    },
    'RdOperMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Flushes formatted input buffer after each read operation'
                },
                'name': 'ON_ACCESS',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Disables flushing of the formatted input buffer'
                },
                'name': 'DISABLE',
                'value': 3
            }
        ]
    },
    'TmoValue': {
        'generate-mappings': True,
        'values': [
            {
                'documentation': {
                    'description': 'Specifies never to wait for the device to respond'
                },
                'name': 'IMMEDIATE',
                'value': '0x0'
            },
            {
                'documentation': {
                    'description': 'Specifies never to timeout (disables the timeout mechanism)'
                },
                'name': 'INFINITE',
                'value': '0xFFFFFFFF'
            }
        ]
    },
    'TrigId': {
        'values': [
            {
                'documentation': {
                    'description': 'Selects software (Word Serial) triggering'
                },
                'name': 'SW',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'Selects hardware triggering on TTL line 0'
                },
                'name': 'TTL0',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Selects hardware triggering on TTL line 1'
                },
                'name': 'TTL1',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Selects hardware triggering on TTL line 2'
                },
                'name': 'TTL2',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Selects hardware triggering on TTL line 3'
                },
                'name': 'TTL3',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Selects hardware triggering on TTL line 4'
                },
                'name': 'TTL4',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Selects hardware triggering on TTL line 5'
                },
                'name': 'TTL5',
                'value': 5
            },
            {
                'documentation': {
                    'description': 'Selects hardware triggering on TTL line 6'
                },
                'name': 'TTL6',
                'value': 6
            },
            {
                'documentation': {
                    'description': 'Selects hardware triggering on TTL line 7'
                },
                'name': 'TTL7',
                'value': 7
            },
            {
                'documentation': {
                    'description': 'Selects hardware triggering on ECL line 0'
                },
                'name': 'ECL0',
                'value': 8
            },
            {
                'documentation': {
                    'description': 'Selects hardware triggering on ECL line 1'
                },
                'name': 'ECL1',
                'value': 9
            }
        ]
    },
    'TriggerLine': {
        'values': [
            {
                'name': 'ALL',
                'value': -2
            },
            {
                'name': 'SW',
                'value': -1
            },
            {
                'name': 'TTL0',
                'value': 0
            },
            {
                'name': 'TTL1',
                'value': 1
            },
            {
                'name': 'TTL2',
                'value': 2
            },
            {
                'name': 'TTL3',
                'value': 3
            },
            {
                'name': 'TTL4',
                'value': 4
            },
            {
                'name': 'TTL5',
                'value': 5
            },
            {
                'name': 'TTL6',
                'value': 6
            },
            {
                'name': 'TTL7',
                'value': 7
            },
            {
                'name': 'ECL0',
                'value': 8
            },
            {
                'name': 'ECL1',
                'value': 9
            },
            {
                'name': 'ECL2',
                'value': 10
            },
            {
                'name': 'ECL3',
                'value': 11
            },
            {
                'name': 'ECL4',
                'value': 12
            },
            {
                'name': 'ECL5',
                'value': 13
            },
            {
                'name': 'STAR_SLOT1',
                'value': 14
            },
            {
                'name': 'STAR_SLOT2',
                'value': 15
            },
            {
                'name': 'STAR_SLOT3',
                'value': 16
            },
            {
                'name': 'STAR_SLOT4',
                'value': 17
            },
            {
                'name': 'STAR_SLOT5',
                'value': 18
            },
            {
                'name': 'STAR_SLOT6',
                'value': 19
            },
            {
                'name': 'STAR_SLOT7',
                'value': 20
            },
            {
                'name': 'STAR_SLOT8',
                'value': 21
            },
            {
                'name': 'STAR_SLOT9',
                'value': 22
            },
            {
                'name': 'STAR_SLOT10',
                'value': 23
            },
            {
                'name': 'STAR_SLOT11',
                'value': 24
            },
            {
                'name': 'STAR_SLOT12',
                'value': 25
            },
            {
                'name': 'STAR_INSTR',
                'value': 26
            },
            {
                'name': 'PANEL_IN',
                'value': 27
            },
            {
                'name': 'PANEL_OUT',
                'value': 28
            },
            {
                'name': 'STAR_VXI0',
                'value': 29
            },
            {
                'name': 'STAR_VXI1',
                'value': 30
            },
            {
                'name': 'STAR_VXI2',
                'value': 31
            },
            {
                'name': 'TTL8',
                'value': 32
            },
            {
                'name': 'TTL9',
                'value': 33
            },
            {
                'name': 'TTL10',
                'value': 34
            },
            {
                'name': 'TTL11',
                'value': 35
            }
        ]
    },
    'TriggerProtocol': {
        'values': [
            {
                'name': 'PROT_DEFAULT',
                'value': 0
            },
            {
                'name': 'PROT_OFF',
                'value': 1
            },
            {
                'name': 'PROT_ON',
                'value': 2
            },
            {
                'name': 'PROT_SYNC',
                'value': 5
            },
            {
                'name': 'PROT_RESERVE',
                'value': 6
            },
            {
                'name': 'PROT_UNRESERVE',
                'value': 7
            }
        ]
    },
    'UsbEndIn': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies that short packets are ignored for read operations, so reads will not terminate until all of the requested data is received (or an error occurs)'
                },
                'name': 'NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Specifies that the read operation will terminate on a short packet; use this if the device will terminate all read transfers with a short packet, including sending a zero (short) packet when the last data packet is full'
                },
                'name': 'SHORT',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Specifies that the read operation will terminate on a short packet or when it receives the requested count of data bytes; use this if the device does not send zero packets'
                },
                'name': 'SHORT_OR_COUNT',
                'value': 5
            }
        ]
    },
    'UsbPipeState': {
        'values': [
            {
                'documentation': {
                    'description': 'Unknown pipe state'
                },
                'name': 'STATE_UNKNOWN',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'Pipe ready'
                },
                'name': 'READY',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Pipe stalled'
                },
                'name': 'STALLED',
                'value': 1
            }
        ]
    },
    'VxiCmdType': {
        'values': [
            {
                'name': 'VXI_RESP16',
                'value': 2
            },
            {
                'name': 'VXI_RESP32',
                'value': 4
            },
            {
                'name': 'VXI_CMD16',
                'value': 512
            },
            {
                'name': 'VXI_CMD16_RESP16',
                'value': 514
            },
            {
                'name': 'VXI_CMD32',
                'value': 1024
            },
            {
                'name': 'VXI_CMD32_RESP16',
                'value': 1026
            },
            {
                'name': 'VXI_CMD32_RESP32',
                'value': 1028
            }
        ]
    },
    'VxiDevClass': {
        'values': [
            {
                'documentation': {
                    'description': 'The VXI device is of type Memory class and supports register-based accesses'
                },
                'name': 'MEMORY',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The VXI device is of type Extended class and supports register-based accesses'
                },
                'name': 'EXTENDED',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'The VXI device is of type Message class and supports both register-based and message-based accesses'
                },
                'name': 'MESSAGE',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'The VXI device is of type Register class and supports register-based accesses'
                },
                'name': 'REGISTER',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'The type of the VXI or VME device is unknown, but it supports register-based accesses'
                },
                'name': 'OTHER',
                'value': 4
            }
        ]
    },
    'WinAccess': {
        'values': [
            {
                'documentation': {
                    'description': 'Window is not currently mapped'
                },
                'name': 'NMAPPED',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Low level accesses must use the viPeekXX/viPokeXX operations'
                },
                'name': 'USE_OPERS',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Low level accesses can dereference the address pointer directly'
                },
                'name': 'DEREF_ADDR',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Low level accesses can dereference the address pointer; byte-swapping is required'
                },
                'name': 'DEREF_ADDR_BYTE_SWAP',
                'value': 4
            }
        ]
    },
    'WrOperMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Flushes formatted output buffer after each write operation'
                },
                'name': 'ON_ACCESS',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Flushes formatted output buffer only when it becomes full'
                },
                'name': 'WHEN_FULL',
                'value': 2
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/visa/enums_addon.py sha256=9f25172e660fd7e043e0a5b4bbd8669084c5cf552aa295713232ee352147b900 bytes=192 -->
## FILE: source/codegen/metadata/visa/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/visa/enums_addon.py`
- sha256: `9f25172e660fd7e043e0a5b4bbd8669084c5cf552aa295713232ee352147b900`
- bytes: 192

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/visa/functions.py sha256=870fa9b353ebcfe13f826eb68fd448e37431a8715290307df7bc7d8f97f6a006 bytes=50665 -->
## FILE: source/codegen/metadata/visa/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/visa/functions.py`
- sha256: `870fa9b353ebcfe13f826eb68fd448e37431a8715290307df7bc7d8f97f6a006`
- bytes: 50665

````python
functions = {
    'AssertIntrSignal': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'AssertInterruptSignalMode',
                'name': 'mode',
                'type': 'ViInt16'
            },
            {
                'direction': 'in',
                'name': 'statusId',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'AssertTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'TriggerProtocol',
                'name': 'protocol',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'AssertUtilSignal': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'AssertUtilSignalMode',
                'name': 'mode',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'Clear': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'Close': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'CloseEvent': {
        'cname': 'viClose',
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'direction': 'in',
                'grpc_type': 'uint32',
                'name': 'eventHandle',
                'type': 'ViEvent'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableEvent': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'EventType',
                'grpc_type': 'uint32',
                'name': 'eventType',
                'type': 'ViEventType'
            },
            {
                'direction': 'in',
                'enum': 'EventMechanism',
                'name': 'eventMechanism',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'DiscardEvents': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'EventType',
                'grpc_type': 'uint32',
                'name': 'eventType',
                'type': 'ViEventType'
            },
            {
                'direction': 'in',
                'enum': 'EventMechanism',
                'name': 'eventMechanism',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'EnableEvent': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'EventType',
                'grpc_type': 'uint32',
                'name': 'eventType',
                'type': 'ViEventType'
            },
            {
                'direction': 'in',
                'enum': 'EventMechanism',
                'name': 'eventMechanism',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'grpc_type': 'uint32',
                'name': 'filterContext',
                'type': 'ViEventFilter'
            }
        ],
        'returns': 'ViStatus'
    },
    'FindNext': {
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'in',
                'name': 'findHandle',
                'type': 'ViFindList'
            },
            {
                'direction': 'out',
                'name': 'instrumentDescriptor',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FindRsrc': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'direction': 'in',
                'include_in_proto': False,
                'name': 'rsrcManagerHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'expression',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'include_in_proto': False,
                'name': 'findHandle',
                'type': 'ViFindList'
            },
            {
                'direction': 'out',
                'include_in_proto': False,
                'name': 'returnCount',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'grpc_type': 'repeated string',
                'name': 'instrumentDescriptor',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'Flush': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'BufferMask',
                'name': 'mask',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttribute': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'attributeName',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'grpc_type': 'AttributeValueData',
                'name': 'attributeValue',
                'type': 'void'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeEvent': {
        'cname': 'viGetAttribute',
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'direction': 'in',
                'grpc_type': 'uint32',
                'name': 'eventHandle',
                'type': 'ViEvent'
            },
            {
                'direction': 'in',
                'name': 'attributeName',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'grpc_type': 'AttributeValueData',
                'name': 'attributeValue',
                'type': 'void'
            }
        ],
        'returns': 'ViStatus'
    },
    'GpibCommand': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'grpc_type': 'bytes',
                'name': 'buffer',
                'size': {
                    'mechanism': 'len',
                    'value': 'count'
                },
                'type': 'ViByte[]'
            },
            {
                'direction': 'in',
                'name': 'count',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'name': 'returnCount',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GpibControlATN': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'GpibControlAtnMode',
                'name': 'mode',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'GpibControlREN': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'GpibControlRenMode',
                'name': 'mode',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'GpibPassControl': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'primaryAddress',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'name': 'secondaryAddress',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'GpibSendIFC': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'In16': {
        'cname': 'viIn16Ex',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'AddressSpace',
                'name': 'addressSpace',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'grpc_type': 'fixed64',
                'name': 'offset',
                'type': 'ViBusAddress64'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'In32': {
        'cname': 'viIn32Ex',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'AddressSpace',
                'name': 'addressSpace',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'grpc_type': 'fixed64',
                'name': 'offset',
                'type': 'ViBusAddress64'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'In64': {
        'cname': 'viIn64Ex',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'AddressSpace',
                'name': 'addressSpace',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'grpc_type': 'fixed64',
                'name': 'offset',
                'type': 'ViBusAddress64'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'ViUInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'In8': {
        'cname': 'viIn8Ex',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'AddressSpace',
                'name': 'addressSpace',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'grpc_type': 'fixed64',
                'name': 'offset',
                'type': 'ViBusAddress64'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'ViUInt8'
            }
        ],
        'returns': 'ViStatus'
    },
    'Lock': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'LockState',
                'grpc_type': 'uint32',
                'name': 'lockType',
                'type': 'ViAccessMode'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'requestedKey',
                'type': 'ViConstKeyId'
            },
            {
                'direction': 'out',
                'name': 'accessKey',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'MapAddress': {
        'cname': 'viMapAddressEx',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'AddressSpace',
                'name': 'addressSpace',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'grpc_type': 'fixed64',
                'name': 'offset',
                'type': 'ViBusAddress64'
            },
            {
                'direction': 'in',
                'grpc_type': 'uint64',
                'name': 'mapSize',
                'type': 'ViBusSize'
            },
            {
                'direction': 'in',
                'name': 'ownerAccess',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'name': 'suggestedAddress',
                'type': 'ViAddr'
            },
            {
                'direction': 'out',
                'name': 'address',
                'type': 'ViAddr'
            }
        ],
        'returns': 'ViStatus'
    },
    'MapTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'TriggerLine',
                'name': 'triggerSource',
                'type': 'ViInt16'
            },
            {
                'direction': 'in',
                'enum': 'TriggerLine',
                'name': 'triggerDestination',
                'type': 'ViInt16'
            },
            {
                'direction': 'in',
                'name': 'mode',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'MemAlloc': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'grpc_type': 'uint32',
                'name': 'size',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'grpc_type': 'uint32',
                'name': 'offset',
                'type': 'ViBusAddress'
            }
        ],
        'returns': 'ViStatus'
    },
    'MemAllocEx': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'grpc_type': 'uint64',
                'name': 'size',
                'type': 'ViBusSize'
            },
            {
                'direction': 'out',
                'grpc_type': 'fixed64',
                'name': 'offset',
                'type': 'ViBusAddress64'
            }
        ],
        'returns': 'ViStatus'
    },
    'MemFree': {
        'cname': 'viMemFreeEx',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'grpc_type': 'fixed64',
                'name': 'offset',
                'type': 'ViBusAddress64'
            }
        ],
        'returns': 'ViStatus'
    },
    'MoveIn16': {
        'cname': 'viMoveIn16Ex',
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'AddressSpace',
                'name': 'addressSpace',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'grpc_type': 'fixed64',
                'name': 'offset',
                'type': 'ViBusAddress64'
            },
            {
                'direction': 'in',
                'grpc_type': 'uint64',
                'name': 'count',
                'type': 'ViBusSize'
            },
            {
                'direction': 'out',
                'name': 'buffer',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'count'
                },
                'type': 'ViUInt16[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'MoveIn32': {
        'cname': 'viMoveIn32Ex',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'AddressSpace',
                'name': 'addressSpace',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'grpc_type': 'fixed64',
                'name': 'offset',
                'type': 'ViBusAddress64'
            },
            {
                'direction': 'in',
                'grpc_type': 'uint64',
                'name': 'count',
                'type': 'ViBusSize'
            },
            {
                'direction': 'out',
                'name': 'buffer',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'count'
                },
                'type': 'ViUInt32[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'MoveIn64': {
        'cname': 'viMoveIn64Ex',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'AddressSpace',
                'name': 'addressSpace',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'grpc_type': 'fixed64',
                'name': 'offset',
                'type': 'ViBusAddress64'
            },
            {
                'direction': 'in',
                'grpc_type': 'uint64',
                'name': 'count',
                'type': 'ViBusSize'
            },
            {
                'direction': 'out',
                'name': 'buffer',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'count'
                },
                'type': 'ViUInt64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'MoveIn8': {
        'cname': 'viMoveIn8Ex',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'AddressSpace',
                'name': 'addressSpace',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'grpc_type': 'fixed64',
                'name': 'offset',
                'type': 'ViBusAddress64'
            },
            {
                'direction': 'in',
                'grpc_type': 'uint64',
                'name': 'count',
                'type': 'ViBusSize'
            },
            {
                'direction': 'out',
                'name': 'buffer',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'count'
                },
                'type': 'ViUInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'MoveOut16': {
        'cname': 'viMoveOut16Ex',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'AddressSpace',
                'name': 'addressSpace',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'grpc_type': 'fixed64',
                'name': 'offset',
                'type': 'ViBusAddress64'
            },
            {
                'direction': 'in',
                'grpc_type': 'uint64',
                'name': 'count',
                'type': 'ViBusSize'
            },
            {
                'direction': 'in',
                'name': 'buffer',
                'size': {
                    'mechanism': 'len',
                    'value': 'count'
                },
                'type': 'ViUInt16[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'MoveOut32': {
        'cname': 'viMoveOut32Ex',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'AddressSpace',
                'name': 'addressSpace',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'grpc_type': 'fixed64',
                'name': 'offset',
                'type': 'ViBusAddress64'
            },
            {
                'direction': 'in',
                'grpc_type': 'uint64',
                'name': 'count',
                'type': 'ViBusSize'
            },
            {
                'direction': 'in',
                'name': 'buffer',
                'size': {
                    'mechanism': 'len',
                    'value': 'count'
                },
                'type': 'ViUInt32[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'MoveOut64': {
        'cname': 'viMoveOut64Ex',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'AddressSpace',
                'name': 'addressSpace',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'grpc_type': 'fixed64',
                'name': 'offset',
                'type': 'ViBusAddress64'
            },
            {
                'direction': 'in',
                'grpc_type': 'uint64',
                'name': 'count',
                'type': 'ViBusSize'
            },
            {
                'direction': 'in',
                'name': 'buffer',
                'size': {
                    'mechanism': 'len',
                    'value': 'count'
                },
                'type': 'ViUInt64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'MoveOut8': {
        'cname': 'viMoveOut8Ex',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'AddressSpace',
                'name': 'addressSpace',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'grpc_type': 'fixed64',
                'name': 'offset',
                'type': 'ViBusAddress64'
            },
            {
                'direction': 'in',
                'grpc_type': 'uint64',
                'name': 'count',
                'type': 'ViBusSize'
            },
            {
                'direction': 'in',
                'name': 'buffer',
                'size': {
                    'mechanism': 'len',
                    'value': 'count'
                },
                'type': 'ViUInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'Open': {
        'codegen_method': 'CustomCode',
        'init_method': True,
        'parameters': [
            {
                'direction': 'in',
                'include_in_proto': False,
                'name': 'rsrcManagerHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'instrumentDescriptor',
                'type': 'ViConstRsrc'
            },
            {
                'direction': 'in',
                'enum': 'LockState',
                'grpc_type': 'uint32',
                'name': 'accessMode',
                'type': 'ViAccessMode'
            },
            {
                'direction': 'in',
                'name': 'openTimeout',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'int32'
            },
            {
                'cppName': 'newSessionInitialized',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'newSessionInitialized',
                'proto_only': True,
                'type': 'bool'
            },
            {
                'direction': 'out',
                'grpc_type': 'repeated EventType',
                'name': 'supportedEvents',
                'proto_only': True,
                'type': 'ViEvent'
            }
        ],
        'returns': 'ViStatus'
    },
    'OpenDefaultRM': {
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'out',
                'include_in_proto': False,
                'name': 'rsrcManagerHandle',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'Out16': {
        'cname': 'viOut16Ex',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'AddressSpace',
                'name': 'addressSpace',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'grpc_type': 'fixed64',
                'name': 'offset',
                'type': 'ViBusAddress64'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'Out32': {
        'cname': 'viOut32Ex',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'AddressSpace',
                'name': 'addressSpace',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'grpc_type': 'fixed64',
                'name': 'offset',
                'type': 'ViBusAddress64'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'Out64': {
        'cname': 'viOut64Ex',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'AddressSpace',
                'name': 'addressSpace',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'grpc_type': 'fixed64',
                'name': 'offset',
                'type': 'ViBusAddress64'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'ViUInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'Out8': {
        'cname': 'viOut8Ex',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'AddressSpace',
                'name': 'addressSpace',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'grpc_type': 'fixed64',
                'name': 'offset',
                'type': 'ViBusAddress64'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'ViUInt8'
            }
        ],
        'returns': 'ViStatus'
    },
    'ParseRsrc': {
        'cname': 'viParseRsrcEx',
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'direction': 'in',
                'include_in_proto': False,
                'name': 'sessionHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'resourceName',
                'type': 'ViConstRsrc'
            },
            {
                'direction': 'out',
                'name': 'interfaceType',
                'type': 'ViUInt16'
            },
            {
                'direction': 'out',
                'name': 'interfaceNumber',
                'type': 'ViUInt16'
            },
            {
                'direction': 'out',
                'name': 'resourceClass',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            },
            {
                'direction': 'out',
                'name': 'expandedUnaliasedName',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            },
            {
                'direction': 'out',
                'name': 'aliasIfExists',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'Peek16': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'address',
                'type': 'ViAddr'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'void',
        'status_expression': '0'
    },
    'Peek32': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'address',
                'type': 'ViAddr'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'void',
        'status_expression': '0'
    },
    'Peek64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'address',
                'type': 'ViAddr'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'ViUInt64'
            }
        ],
        'returns': 'void',
        'status_expression': '0'
    },
    'Peek8': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'address',
                'type': 'ViAddr'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'ViUInt8'
            }
        ],
        'returns': 'void',
        'status_expression': '0'
    },
    'Poke16': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'address',
                'type': 'ViAddr'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'void',
        'status_expression': '0'
    },
    'Poke32': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'address',
                'type': 'ViAddr'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'void',
        'status_expression': '0'
    },
    'Poke64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'address',
                'type': 'ViAddr'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'ViUInt64'
            }
        ],
        'returns': 'void',
        'status_expression': '0'
    },
    'Poke8': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'address',
                'type': 'ViAddr'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'ViUInt8'
            }
        ],
        'returns': 'void',
        'status_expression': '0'
    },
    'PxiReserveTriggers': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'cnt',
                'type': 'ViInt16'
            },
            {
                'direction': 'in',
                'name': 'trigBuses',
                'size': {
                    'mechanism': 'len',
                    'value': 'cnt'
                },
                'type': 'ViInt16[]'
            },
            {
                'direction': 'in',
                'name': 'trigLines',
                'size': {
                    'mechanism': 'len',
                    'value': 'cnt'
                },
                'type': 'ViInt16[]'
            },
            {
                'direction': 'out',
                'include_in_proto': False,
                'name': 'failureIndex',
                'return_on_error_key': 'ni-failure-index',
                'type': 'ViInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'Read': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'grpc_type': 'bytes',
                'name': 'buffer',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'returnCount'
                },
                'type': 'ViByte[]'
            },
            {
                'direction': 'in',
                'name': 'count',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'name': 'returnCount',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadAsync': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'grpc_type': 'bytes',
                'include_in_proto': False,
                'name': 'readBuffer',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'count'
                },
                'type': 'ViByte[]'
            },
            {
                'direction': 'in',
                'name': 'count',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'grpc_type': 'uint32',
                'name': 'jobIdentifier',
                'type': 'ViJobId'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadSTB': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'statusByte',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttribute': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'attributeName',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'grpc_type': 'AttributeValueData',
                'name': 'attributeValue',
                'type': 'ViAttrState'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetBuf': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'BufferMask',
                'name': 'mask',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'StatusDesc': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'statusValue',
                'type': 'ViStatus'
            },
            {
                'direction': 'out',
                'name': 'statusDescription',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'Terminate': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'degree',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'grpc_type': 'uint32',
                'name': 'jobIdentifier',
                'type': 'ViJobId'
            }
        ],
        'returns': 'ViStatus'
    },
    'Unlock': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'UnmapAddress': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'UnmapTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'TriggerLine',
                'name': 'triggerSource',
                'type': 'ViInt16'
            },
            {
                'direction': 'in',
                'enum': 'TriggerLine',
                'name': 'triggerDestination',
                'type': 'ViInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'UsbControlIn': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'bmRequestType',
                'type': 'ViInt16'
            },
            {
                'direction': 'in',
                'name': 'bRequest',
                'type': 'ViInt16'
            },
            {
                'direction': 'in',
                'name': 'wValue',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'name': 'wIndex',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'name': 'wLength',
                'type': 'ViUInt16'
            },
            {
                'direction': 'out',
                'grpc_type': 'bytes',
                'name': 'buffer',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'returnCount'
                },
                'type': 'ViByte[]'
            },
            {
                'direction': 'out',
                'name': 'returnCount',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'UsbControlOut': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'bmRequestType',
                'type': 'ViInt16'
            },
            {
                'direction': 'in',
                'name': 'bRequest',
                'type': 'ViInt16'
            },
            {
                'direction': 'in',
                'name': 'wValue',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'name': 'wIndex',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'name': 'wLength',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'grpc_type': 'bytes',
                'name': 'buffer',
                'size': {
                    'mechanism': 'len',
                    'value': 'wLength'
                },
                'type': 'ViByte[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'VxiCommandQuery': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'VxiCmdType',
                'name': 'mode',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'name': 'command',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'name': 'commandResponse',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'WaitOnEvent': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'EventType',
                'grpc_type': 'uint32',
                'name': 'inEventType',
                'type': 'ViEventType'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'enum': 'EventType',
                'grpc_type': 'uint32',
                'name': 'outEventType',
                'type': 'ViEventType'
            },
            {
                'direction': 'out',
                'grpc_type': 'uint32',
                'name': 'eventHandle',
                'type': 'ViEvent'
            }
        ],
        'returns': 'ViStatus'
    },
    'Write': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'grpc_type': 'bytes',
                'name': 'buffer',
                'size': {
                    'mechanism': 'len',
                    'value': 'count'
                },
                'type': 'ViByte[]'
            },
            {
                'direction': 'in',
                'name': 'count',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'name': 'returnCount',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteAsync': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'grpc_type': 'bytes',
                'name': 'buffer',
                'size': {
                    'mechanism': 'len',
                    'value': 'count'
                },
                'type': 'ViByte[]'
            },
            {
                'direction': 'in',
                'name': 'count',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'grpc_type': 'uint32',
                'name': 'jobIdentifier',
                'type': 'ViJobId'
            }
        ],
        'returns': 'ViStatus'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/visa/functions_addon.py sha256=65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45 bytes=36 -->
## FILE: source/codegen/metadata/visa/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/visa/functions_addon.py`
- sha256: `65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45`
- bytes: 36

````python
functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata_mutation.py sha256=720f61d6bd8d8c34c27886ec38f21db7671abd5b5307d31e079b5a7fc054123a bytes=20326 -->
## FILE: source/codegen/metadata_mutation.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata_mutation.py`
- sha256: `720f61d6bd8d8c34c27886ec38f21db7671abd5b5307d31e079b5a7fc054123a`
- bytes: 20326

````python
"""Metadata mutation."""

import copy
from collections import namedtuple
from typing import Any, Dict, Optional

import common_helpers

RESERVED_WORDS = [
    "abstract",
    "as",
    "base",
    "bool",
    "break",
    "byte",
    "case",
    "catch",
    "char",
    "checked",
    "class",
    "const",
    "continue",
    "decimal",
    "default",
    "delegate",
    "do",
    "double",
    "else",
    "enum",
    "event",
    "explicit",
    "extern",
    "false",
    "finally",
    "fixed",
    "float",
    "for",
    "foreach",
    "goto",
    "if",
    "implicit",
    "in",
    "int",
    "interface",
    "internal",
    "is",
    "lock",
    "long",
    "namespace",
    "new",
    "null",
    "object",
    "operator",
    "out",
    "override",
    "params",
    "private",
    "protected",
    "public",
    "readonly",
    "ref",
    "return",
    "sbyte",
    "sealed",
    "short",
    "sizeof",
    "stackalloc",
    "static",
    "string",
    "struct",
    "switch",
    "this",
    "throw",
    "true",
    "try",
    "typeof",
    "uint",
    "ulong",
    "unchecked",
    "unsafe",
    "ushort",
    "using",
    "virtual",
    "void",
    "volatile",
    "while",
]

# These are all of the coerced narrow numerics used in RFmx and DAQmx.
# This will not account for other aliases of narrow numerics.
# Note that params can also be marked coerced instead of updating this list.
# uint8 is not included because it can be represented as a byte.
KNOWN_COERCED_NARROW_NUMERIC_TYPES = [
    "int8",
    "int8_t",
    "uint8_t",
    "int16",
    "int16_t",
    "uInt16",
    "uint16_t",
]

_ALREADY_MUTATED = (
    "NI-DCPower",
    "NI-Digital Pattern Driver",
    "NI-DMM",
    "NI-FAKE",
    "NI-FGEN",
    "NI-SCOPE",
    "NI-SWITCH",
    "NI-TClk",
)


def mutate(metadata: dict):
    """Mutate the given metadata."""
    config = metadata["config"]
    if config["driver_name"] in _ALREADY_MUTATED:
        return

    # Generate new streaming APIs for functions that support it.
    all_functions = {}

    for function_name, function in metadata["functions"].items():
        all_functions[function_name] = function

        if function.get("supports_streaming") is True:
            new_function_name = f"Begin{function_name}"
            all_functions[new_function_name] = generate_streaming_metadata(function)

    metadata["functions"] = all_functions

    move_zero_enums_to_front(metadata["enums"])

    for custom_type in config["custom_types"]:
        fields = custom_type["fields"]
        set_grpc_type_for_custom_type_fields(fields, config)

    attribute_expander = AttributeAccessorExpander(metadata)
    for function_name, function in metadata["functions"].items():
        parameters = function["parameters"]
        add_get_last_error_params_if_needed(function, config)
        sanitize_names(parameters)
        set_var_args_types(parameters, config)
        mark_size_params(parameters)
        mark_non_proto_params(parameters)
        mark_mapped_enum_params(parameters, metadata["enums"])
        populate_grpc_types(parameters, config)
        mark_coerced_narrow_numeric_parameters(parameters)
        attribute_expander.expand_attribute_value_params(function)
        attribute_expander.patch_attribute_enum_type(function_name, function)


def generate_streaming_metadata(function: dict) -> dict:
    """Generate the streaming API metadata for a given function."""
    streaming_parameters = []

    for param in function["parameters"]:
        new_param = copy.deepcopy(param)
        if new_param.get("is_streaming_type", False) is True:
            new_param["include_in_proto"] = False
        streaming_parameters.append(new_param)

    # Add the additional out parameter at the end
    streaming_parameters.append(
        {
            "direction": "out",
            "grpc_type": "ni.data_monikers.Moniker",
            "name": "moniker",
            "type": "ni::data_monikers::Moniker",
        }
    )

    # Construct the streaming API metadata
    streaming_metadata = {
        "is_streaming_api": True,
        "parameters": streaming_parameters,
        "returns": function["returns"],
    }

    return streaming_metadata


def sanitize_names(parameters):
    """Sanitize name fields on a list of parameter objects.

    Also, populate the cppname field with the sanitized value.
    """
    for parameter in parameters:
        if "callback_params" in parameter:
            sanitize_names(parameter["callback_params"])
        parameter["cppName"] = parameter["name"]
        if parameter["cppName"] in RESERVED_WORDS:
            parameter["cppName"] += "Parameter"


def set_var_args_types(parameters, config):
    """Set information about varargs parameters in the metadata."""
    for parameter in parameters:
        if common_helpers.is_repeated_varargs_parameter(parameter):
            parameter["type"] = "..."


def mark_size_params(parameters):
    """Mark the size parameters in the metadata."""
    for param in parameters:
        mechanism = common_helpers.get_size_mechanism(param)
        if mechanism in {
            "len",
            "ivi-dance",
            "passed-in",
            "passed-in-by-ptr",
            "ivi-dance-with-a-twist",
        }:
            size_param = _get_size_param(param, parameters)
            size_param["is_size_param"] = True
            if mechanism == "passed-in-by-ptr":
                size_param["pointer"] = True


def mark_coerced_narrow_numeric_parameters(parameters: dict) -> None:
    """Mark parameters with narrow numeric types as coerced."""
    for param in parameters:
        param_type = common_helpers.get_underlying_type(param)
        if param_type in KNOWN_COERCED_NARROW_NUMERIC_TYPES:
            param["coerced"] = True


def mark_non_proto_params(parameters):
    """Mark the parameters that shouldn't be included in the proto request message.

    Their values should be derived from other sources in the service handlers.
    """
    for param in parameters:
        mechanism = common_helpers.get_size_mechanism(param)
        if mechanism in {"len", "len-in-bytes", "ivi-dance", "ivi-dance-with-a-twist"}:
            size_param = _get_size_param(param, parameters)
            if size_param["direction"] == "in":
                # Output size_params can still be included in the proto
                # as information.
                size_param["include_in_proto"] = False
            if mechanism in ["len", "len-in-bytes"]:
                if "determine_size_from" not in size_param:
                    size_param["determine_size_from"] = []
                size_param["determine_size_from"].append(param["name"])
                is_optional = common_helpers.has_optional_size_tag(param)
                if is_optional != size_param.get("linked_params_are_optional", is_optional):
                    raise Exception(
                        "Code generator does not support linked params that are a mix of optional and required",
                        size_param,
                    )
                size_param["linked_params_are_optional"] = is_optional


def _get_size_param(param, parameters):
    named_params = {p["name"]: p for p in parameters}
    return named_params.get(param["size"]["value"], None)


def mark_mapped_enum_params(parameters, enums):
    """Mark enum paramaters as mapped-enum if the enum has mappings."""
    for param in (p for p in parameters if "enum" in p):
        enum_name = param["enum"]
        enum = enums[enum_name]
        if "generate-mappings" in enum:
            del param["enum"]
            param["mapped-enum"] = enum_name


def populate_grpc_types(parameters, config):
    """Set the grpc_type of each parameter that doesn't already have it set."""
    for parameter in parameters:
        if "callback_params" in parameter:
            populate_grpc_types(parameter["callback_params"], config)
        if "grpc_type" in parameter:
            continue
        parameter["grpc_type"] = common_helpers.get_grpc_type(parameter["type"], config)


def set_grpc_type_for_custom_type_fields(fields, config):
    """Set the grpc_type for each field of a custom type."""
    for field in fields:
        if "grpc_type" in field:
            continue
        elif "enum" in field:
            field["grpc_type"] = field["enum"]
        else:
            field["grpc_type"] = common_helpers.get_grpc_type(field["type"], config)


def _get_short_enum_type_name(typename: str) -> str:
    if typename in ["char[]", "const char[]", "char"]:
        return "String"
    stripped_name = common_helpers.strip_prefix(typename, "Vi")
    return common_helpers.ensure_pascal_case(stripped_name)


def _remove_leading_group_name(enum_value_name, group_name):
    return common_helpers.strip_prefix(enum_value_name, f"{group_name.upper()}_")


def _add_leading_enum_name(enum_value_name, enum_name, enum):
    enum_value_prefix = enum.get(
        "enum-value-prefix", common_helpers.pascal_to_snake(enum_name).upper()
    )
    return f"{enum_value_prefix}_{enum_value_name}"


def _add_attribute_values_enums(enums, attribute_enums_by_type, group_name):
    """Add new enums to enums metadata, for use as the value parameter of SetAttribute APIs."""
    for type_name in attribute_enums_by_type:
        unmapped_values = {}
        # For mapped enums, we want legacy (no 'order') entries first (in encounter order),
        # then append all ordered entries sorted by their 'order' field. We collect them
        # separately and merge after processing all contributing enums of this type.
        mapped_legacy_values = {}
        mapped_ordered_values = []  # list of tuples (order, value_name, value_value)

        for enum_name in sorted(attribute_enums_by_type[type_name]):
            enum = enums[enum_name]
            is_mapped_enum = enum.get("generate-mappings", False)
            for value in enum["values"]:
                # Remove the leading group name (if any) because it will be redundant in the
                # aggregate enum.
                value_name = _remove_leading_group_name(value["name"], group_name)
                # Add a leading enum to differentiate sub-enums within the aggregate values enum.
                value_name = _add_leading_enum_name(value_name, enum_name, enum)
                if is_mapped_enum:
                    if "order" in value:
                        mapped_ordered_values.append((value["order"], value_name, value["value"]))
                    else:
                        mapped_legacy_values[value_name] = value["value"]
                else:
                    unmapped_values[value_name] = value["value"]

        # Now append ordered mapped entries sorted by their 'order'.
        if mapped_ordered_values:
            # stable sort to maintain original order in case of same order fields
            mapped_ordered_values.sort(key=lambda t: t[0])
            for _, value_name, value_val in mapped_ordered_values:
                mapped_legacy_values[value_name] = value_val

        shortened_type_name = _get_short_enum_type_name(type_name)
        enum_value_prefix = (f"{group_name}_{shortened_type_name}").upper()
        unmapped_enum_name = _get_attribute_values_enum_name(group_name, type_name)
        mapped_enum_name = _get_attribute_values_enum_name(group_name, type_name, is_mapped=True)
        _add_enum(unmapped_enum_name, unmapped_values, enums, enum_value_prefix)
        _add_enum(mapped_enum_name, mapped_legacy_values, enums, enum_value_prefix, is_mapped=True)


AttributeReferencingParameter = namedtuple(
    "AttributeReferencingParameter", ["attribute_group", "parameter"]
)


class AttributeAccessorExpander:
    """Wraps an _attribute_type_map of: group -> type -> attributes.

    Also implements the metadata_mutations to _add_attribute_values_enums,
    _expand_attribute_function_value_param, and patch_attribute_enum_type.
    """

    def __init__(self, metadata):  # noqa: D107
        self._config = metadata["config"]
        self._enums = metadata["enums"]
        self._attribute_type_map = {}

        for group in common_helpers.get_attribute_groups(metadata):
            attribute_enums_by_type = common_helpers.get_attribute_enums_by_type(group.attributes)
            _add_attribute_values_enums(self._enums, attribute_enums_by_type, group.name)
            self._attribute_type_map[group.name] = attribute_enums_by_type

    def _get_attribute_reference_parameter(
        self, parameters
    ) -> Optional[AttributeReferencingParameter]:
        """Get the parameter that references an attribute, if there is one."""

        def try_resolve_attribute_reference(parameter) -> Optional[AttributeReferencingParameter]:
            param_type = parameter["grpc_type"]
            # All attribute parameters must have a grpc_type of {group_name}Attributes.
            # In MI, this is added during metadata mutation of ViAttr types.
            attr_suffix = common_helpers.get_attribute_enum_suffix(self._config)
            potential_attribute_name = common_helpers.strip_suffix(param_type, attr_suffix)
            if potential_attribute_name in self._attribute_type_map:
                return AttributeReferencingParameter(potential_attribute_name, parameter)
            return None

        # Assumption: there are 0 or 1 parameters that reference an attribute per function.
        attribute_resolve_results = (try_resolve_attribute_reference(p) for p in parameters)
        valid_references = (ref for ref in attribute_resolve_results if ref)
        return next(valid_references, None)

    def patch_attribute_enum_type(self, function_name, func):
        """Update the attribute parameter to point to the proper enum name.

        Only applies for drivers that splits attribute enums by type.

        For example, DAQmx has a Get/Set/ResetBufferAttributeUInt32 functions. The parameter that
        selects _which_ attribute needs to use the proper attribute enum. The input says that the
        grpc_type is BufferAttribute, but the generated code splits the enums by type, with a
        special group for Reset functions. So in this example, the Get and Set functions' attribute
        enum would be BufferUInt32Attribute, and the Reset function's attribute enum would be
        BufferResetAttribute.
        """
        if not common_helpers.get_split_attributes_by_type(self._config):
            return
        parameters = func["parameters"]
        attribute_reference = self._get_attribute_reference_parameter(parameters)
        if attribute_reference:
            group = attribute_reference.attribute_group
            attribute_param = attribute_reference.parameter
            if function_name.startswith("Reset"):
                sub_group = "Reset"
            else:
                value_param = _get_attribute_function_value_param(func)
                sub_group = common_helpers.get_grpc_type_name_for_identifier(
                    value_param["type"], self._config
                )
            if common_helpers.supports_raw_attributes(self._config):
                attribute_param["enum"] = common_helpers.get_attribute_enum_name(
                    group, sub_group, self._config
                )
                attribute_param["grpc_type"] = "int32"
                attribute_param["raw_attribute"] = True
            else:
                attribute_param["grpc_type"] = common_helpers.get_attribute_enum_name(
                    group, sub_group, self._config
                )

    def expand_attribute_value_params(self, func):
        """Update the attrVal parameter to use the proper enum, if available."""
        parameters = func["parameters"]
        attribute_reference = self._get_attribute_reference_parameter(parameters)
        if attribute_reference:
            _expand_attribute_function_value_param(
                func,
                self._enums,
                self._attribute_type_map[attribute_reference.attribute_group],
                attribute_reference.attribute_group,
            )


def _expand_attribute_function_value_param(
    function, enums, attribute_enums_by_type, service_class_prefix
):
    """For SetAttribute and CheckAttribute, update function metadata to mark value param as enum."""
    value_param = _get_attribute_function_value_param(function)
    if not value_param:
        return
    if value_param["direction"] == "out":
        if common_helpers.is_static_castable_enum_type(value_param):
            value_param["use_checked_enum_conversion"] = True
        else:
            return

    if value_param["type"] == "ViConstString":
        param_type = "ViString"
    else:
        param_type = common_helpers.get_underlying_type(value_param)
    if param_type in attribute_enums_by_type:
        enum_name = _get_attribute_values_enum_name(service_class_prefix, param_type)
        mapped_enum_name = _get_attribute_values_enum_name(
            service_class_prefix, param_type, is_mapped=True
        )
        enum_exists = enum_name in enums
        mapped_enum_exists = mapped_enum_name in enums
        if enum_exists:
            value_param["enum"] = enum_name
        if mapped_enum_exists:
            value_param["mapped-enum"] = mapped_enum_name
        if not enum_exists and not mapped_enum_exists:
            # Ideally there must be an enum associated with this parameter for SetAttribute* API.
            # Since the enum is empty, users will be passing in raw values. Make it clear via
            # naming.
            value_param["name"] += "_raw"


def _get_attribute_function_value_param(function):
    return next(
        (
            param
            for param in function["parameters"]
            if param["name"] in {"value", "attributeValue", "attrVal"}
        ),
        None,
    )


def _get_attribute_values_enum_name(group_name, type, is_mapped=False):
    enum_name_suffix = "Mapped" if is_mapped else ""
    shortened_type_name = _get_short_enum_type_name(type)
    return group_name + shortened_type_name + "AttributeValues" + enum_name_suffix


def _add_enum(enum_name, enum_values, enums, enum_value_prefix, is_mapped=False):
    if not enum_values:
        return
    values = [{"name": name, "value": enum_values[name]} for name in enum_values]
    new_enum = {
        "enum-value-prefix": enum_value_prefix,
        "generate-mappings": is_mapped,
        "values": values,
    }
    enums.update({enum_name: new_enum})


def move_zero_enums_to_front(enums: dict) -> None:
    """Put the enum value with value 0 _first_ if there is one, or else add UNSPECIFIED enum value.

    protobuf requires that the first enum value be zero. For enums missing a zero value,
    we will add an UNSPECIFIED enum value to the front (this is the best practice). But if
    there already is a zero enum, make sure that pre-existing zero value is at the front.
    """
    for enum in enums.values():
        values = enum["values"]
        try:
            i, _ = next((i, v) for i, v in enumerate(values) if v["value"] == 0)
            values.insert(0, values.pop(i))
        except StopIteration:
            pass


def add_get_last_error_params_if_needed(function_data: Dict[str, Any], config: dict) -> None:
    """Add get_last_error parameters to the list if any are specified in config."""
    if function_data.get("exclude_from_get_last_error"):
        return

    parameters = function_data["parameters"]
    for get_last_error_field in config.get("get_last_error", []):
        parameters.append(
            {
                "direction": "out",
                "get_last_error": "deprecated",
                "name": get_last_error_field["name"],
                "type": get_last_error_field["type"],
            }
        )
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata_validation.py sha256=085cf5be7743f6cf3457429dea657a2b9051b24ad3890aa2af80f9f671f21946 bytes=23295 -->
## FILE: source/codegen/metadata_validation.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata_validation.py`
- sha256: `085cf5be7743f6cf3457429dea657a2b9051b24ad3890aa2af80f9f671f21946`
- bytes: 23295

````python
"""Metadata validation."""

from typing import Any, Dict, List, Set

import common_helpers
import service_helpers
from schema import And, Optional, Or, Schema, Use  # type: ignore


# grpc device metadata mutations have been applied to MI drivers in
# source to minimize transformations that happen outside of hapigen
_ALREADY_MUTATED = (
    "NI-DCPower",
    "NI-Digital Pattern Driver",
    "NI-DMM",
    "NI-FAKE",
    "NI-FGEN",
    "NI-SCOPE",
    "NI-SWITCH",
    "NI-TClk",
)


class RULES:
    """Rules that can be suppressed."""

    # In general, arrays should have sizes passed in to the underlying C API.
    ARRAY_PARAMETER_NEEDS_SIZE = "ARRAY_PARAMETER_NEEDS_SIZE"
    # The gRPC layer can determine the size of input arrays, so we should not require callers to
    # pass in the size. We should not add any new suppressions of this type.
    INPUT_ARRAY_SHOULD_NOT_HAVE_PASSED_IN_SIZE = "INPUT_ARRAY_SHOULD_NOT_HAVE_PASSED_IN_SIZE"
    # In general, enums shouldn't have duplicate values. This is helpful for catching typos although
    # there are a few enums that have legitimate duplicates.
    ENUMS_SHOULD_NOT_HAVE_DUPLICATE_VALUES = "ENUMS_SHOULD_NOT_HAVE_DUPLICATE_VALUES"
    # The ENUMS_SHOULD_BE_USED validation rule is intended to catch enums that are not mapped
    # to functions or attributes because of incomplete or mishandled metadata. Note that any
    # unreferenced enums will not be included in the proto file. These enums should be reviewed
    # and if they are correctly included-but-not-referenced and are not required to be
    # in the proto file,the rule can be suppressed.
    ENUMS_SHOULD_BE_USED = "ENUMS_SHOULD_BE_USED"


DOCUMENTATION_SCHEMA = Schema(
    {
        "description": str,
        Optional("python_description"): str,
        Optional("note"): str,
        Optional("table_body"): list,
        Optional("caution"): str,
    }
)

SIZE_SCHEMA = Schema(
    {
        "mechanism": And(str, lambda s: not common_helpers.is_unsupported_size_mechanism_type(s)),
        "value": Or(str, int),
        Optional("value_twist"): str,
        Optional("tags"): [str],
        Optional("python_value"): str,
    },
)

PARAM_SCHEMA = Schema(
    {
        "direction": And(str, lambda s: s in ("in", "out")),
        "name": str,
        Optional("type"): str,
        Optional("grpc_type"): str,
        Optional("documentation"): DOCUMENTATION_SCHEMA,
        Optional("bitfield_as_enum_array"): str,
        Optional("enum"): str,
        Optional("size"): SIZE_SCHEMA,
        Optional("default_value"): Or(str, bool, int, float, None),
        Optional("is_repeated_capability"): bool,
        Optional("repeated_capability_type"): str,
        Optional("use_array"): bool,
        Optional("numpy"): bool,
        # integer in string form, make sure int(x) doesn't raise
        Optional("grpc_field_number"): And(str, Use(int)),
        # integer in string form, make sure int(x) doesn't raise
        Optional("grpc_raw_field_number"): And(str, Use(int)),
        # integer in string form, make sure int(x) doesn't raise
        Optional("grpc_mapped_field_number"): And(str, Use(int)),
        Optional("type_in_documentation"): str,
        Optional("include_in_proto"): bool,
        Optional("proto_only"): bool,
        Optional("is_session_handle"): bool,
        Optional("is_session_name"): bool,
        Optional("repeating_argument"): bool,
        Optional("python_api_converter_name"): str,
        Optional("attribute"): str,
        Optional("hardcoded_value"): str,
        Optional("is_compound_type"): bool,
        Optional("max_length"): int,
        Optional("repeated_var_args"): bool,
        Optional("pointer"): bool,
        Optional("coerced"): bool,
        Optional("callback_params"): [dict],
        Optional("callback_token"): bool,
        Optional("use_in_python_api"): bool,
        Optional("cross_driver_session"): str,
        Optional("cpp_local_name"): str,
        Optional("grpc_name"): str,
        Optional("return_value"): bool,
        Optional("supports_standard_copy_convert"): bool,
        Optional("supports_standard_output_allocation"): bool,
        Optional("get_last_error"): str,
        Optional("additional_arguments_to_copy_convert"): [str],
        Optional("additional_arguments_to_output_allocation"): [str],
        Optional("proto_only"): bool,
        Optional("input_passed_by_ptr"): bool,
        Optional("cppName"): str,
        Optional("determine_size_from"): [str],
        Optional("is_size_param"): bool,
        Optional("linked_params_are_optional"): bool,
        Optional("mapped-enum"): str,
        Optional("is_optional"): bool,
        Optional("is_optional_in_python"): bool,
        Optional("ctypes_data_type"): Or(str, None),
        Optional("has_explicit_buffer_size"): bool,
        Optional("is_list"): bool,
        Optional("python_data_type"): str,
        Optional("python_type_annotation"): str,
        Optional("python_description"): str,
        Optional("python_default_value"): Or(str, bool, int, float, None),
        Optional("is_grpc_enum"): bool,
        Optional("return_on_error_key"): str,
        Optional("is_streaming_type"): bool,
        Optional("value_converted_to_c_representation"): str,
    }
)

FUNCTION_SCHEMA = Schema(
    {
        "parameters": [PARAM_SCHEMA],
        "returns": str,
        Optional("cname"): str,
        Optional("codegen_method"): And(
            str,
            lambda s: s
            in (
                "public",
                "private",
                "CustomCode",
                "no",
                "python-only",
                "CustomCodeCustomProtoMessage",
                "CustomCodeNoLibrary",
            ),
        ),
        Optional("python_codegen_method"): And(
            str,
            lambda s: s
            in (
                "CustomCode",
                "no",
            ),
        ),
        Optional("init_method"): bool,
        Optional("stream_response"): bool,
        Optional("is_error_handling"): bool,
        Optional("render_in_session_base"): bool,
        Optional("method_name_for_documentation"): str,
        Optional("use_session_lock"): bool,
        Optional("documentation"): DOCUMENTATION_SCHEMA,
        Optional("method_templates"): list,
        Optional("custom_close"): str,
        Optional("custom_close_method"): bool,
        Optional("python_name"): str,
        Optional("status_expression"): str,
        Optional("include_in_client"): bool,
        Optional("exclude_from_get_last_error"): bool,
        Optional("calling_convention"): str,
        Optional("python_class_name"): str,
        Optional("handle_parameter"): dict,
        Optional("adaptor_parameter"): dict,
        Optional("is_python_factory"): bool,
        Optional("python_description"): str,
        Optional("timeout_error"): str,
        Optional("supports_streaming"): bool,
        Optional("moniker_streaming_type"): str,
    }
)

ATTRIBUTE_SCHEMA = Schema(
    {
        "name": str,
        Optional("access"): And(
            str, lambda s: s in ["read", "read only", "write", "write only", "read-write"]
        ),
        "type": str,
        Optional("resettable"): bool,
        Optional("enum"): str,
        Optional("python_enum"): str,
        Optional("channel_based"): bool,
        Optional("attribute_class"): str,
        Optional("type_in_documentation"): str,
        Optional("documentation"): DOCUMENTATION_SCHEMA,
        Optional("lv_property"): str,
        Optional("repeated_capability_type"): str,
        Optional("python_type"): str,
        Optional("python_name"): str,
        Optional("codegen_method"): str,
        Optional("grpc_type"): str,
        Optional("c_function_name"): str,
        Optional("calling_convention"): str,
        Optional("bitfield_enum"): str,
        Optional("ctypes_data_type"): str,
        Optional("handle_parameters"): dict,
        Optional("python_object_constructor_params"): dict,
        Optional("has_explicit_read_buffer_size"): bool,
        Optional("python_object_has_factory"): bool,
        Optional("python_object_module_location"): str,
        Optional("python_object_type"): str,
        Optional("has_explicit_write_buffer_size"): bool,
        Optional("is_list"): bool,
        Optional("is_python_object"): bool,
        Optional("lv_filter"): list,
        Optional("python_class_name"): str,
        Optional("python_data_type"): str,
        Optional("python_description"): str,
    }
)

SIMPLE_ATTRIBUTE_SCHEMA = Schema(
    {
        "name": str,
    },
)

ENUM_SCHEMA = Schema(
    {
        Optional("python_name"): str,
        "values": [
            {
                "name": str,
                "value": Or(str, int, float),
                Optional("order"): int,
                Optional("python_name"): str,
                Optional("documentation"): DOCUMENTATION_SCHEMA,
                Optional("type"): str,
            }
        ],
        Optional("generate-mappings"): bool,
        Optional("enum-value-prefix"): str,
        Optional("generate-mapping-type"): bool,
        Optional("force-include"): bool,
        Optional("codegen_method"): str,
    }
)


def validate_metadata(metadata: dict):
    """Validate the given metadata."""
    try:
        for function_name in metadata["functions"]:
            _validate_function(function_name, metadata)
        for attribute_group in common_helpers.get_attribute_groups(metadata):
            for attribute_id in attribute_group.attributes:
                _validate_attribute(attribute_group.attributes[attribute_id], metadata)
        function_enums = set(
            common_helpers.get_function_enums(metadata["functions"], metadata["enums"])
        )
        attribute_enums = _get_attribute_enums(metadata)
        used_enums = function_enums.union(attribute_enums)
        for enum_name in metadata["enums"]:
            if not _rule_is_suppressed(metadata, RULES.ENUMS_SHOULD_BE_USED, ["enums", enum_name]):
                _validate_enum(enum_name, used_enums, metadata)
    except Exception as e:
        raise Exception(f"Failed to validate {metadata['config']['namespace_component']}") from e


def _rule_is_suppressed(metadata: dict, rule: str, path: List[str]) -> bool:
    suppression_dict_name = path[0] + "_validation_suppressions"
    suppression_dict = metadata.get(suppression_dict_name, {})
    for entry in path[1:-1]:
        suppression_dict = suppression_dict.get(entry, {})
    last_entry = path[-1]
    if last_entry not in suppression_dict:
        return False
    return rule in suppression_dict[last_entry]


def _parameter_name_exists(function: dict, name: str) -> bool:
    return any([param for param in function["parameters"] if param["name"] == name])


def _validate_function(function_name: str, metadata: dict):
    try:
        function: Dict[str, Any] = metadata["functions"][function_name]
        ivi_dance_with_a_twist_params = []
        ivi_dance_with_a_twist_sizes = set()
        ivi_dance_with_a_twist_twists = set()
        if function.get("codegen_method", "public") != "no":
            FUNCTION_SCHEMA.validate(function)
            if "documentation" in function:
                DOCUMENTATION_SCHEMA.validate(function["documentation"])
            duplicate_resource_handles_allowed = metadata["config"].get(
                "duplicate_resource_handles_allowed", False
            )
            is_init_method = function.get("init_method", False)
            for parameter in function["parameters"]:
                _validate_parameter_size(parameter, function_name, metadata)
                if "type" not in parameter:
                    if "grpc_type" not in parameter:
                        raise Exception(f"parameter {parameter['name']} has no type or grpc_type!")
                    if not parameter.get("repeated_var_args", False) and not parameter.get(
                        "proto_only", False
                    ):
                        raise Exception(
                            f"parameter {parameter['name']} has no type and repeated_var_args or proto_only is not set!"
                        )
                if "enum" in parameter:
                    if parameter["enum"] not in metadata["enums"]:
                        raise Exception(
                            f"parameter {parameter['name']} has enum {parameter['enum']} that was not found!"
                        )
                if "max_length" in parameter:
                    if "repeated_var_args" not in parameter:
                        raise Exception(
                            f"parameter {parameter['name']} has max_length but no repeated_var_args!"
                        )
                if "callback_params" in parameter:
                    for callback_param in parameter["callback_params"]:
                        try:
                            PARAM_SCHEMA.validate(callback_param)
                        except Exception:
                            raise Exception(
                                f"Failed to validate callback_param with name {callback_param['name']}"
                            )
                if "hardcoded_value" in parameter:
                    if parameter.get("include_in_proto", True):
                        raise Exception(
                            f"parameter {parameter['name']} has hardcoded_value but is include_in_proto!"
                        )
                if "cross_driver_session" in parameter:
                    # Assumption: there's no code that automatically sets the grpc_type for
                    # cross_driver_sessions and nidevice_grpc.Session is the only type that works.
                    if parameter.get("grpc_type", None) not in [
                        "nidevice_grpc.Session",
                        "repeated nidevice_grpc.Session",
                    ]:
                        raise Exception(
                            f"parameter {parameter['name']} is a cross_driver_session but does not have a grpc_type of nidevice_grpc.Session!"
                        )
                    # Assumption: a method that creates a session (via accessing a cross-driver
                    # session) must be an init_method to ensure that the session is tracked in the
                    # session repository.
                    if parameter["direction"] == "out" and not function.get("init_method"):
                        raise Exception(
                            f"parameter {parameter['name']} is a cross_driver_session output but {function_name} is not an init_method!"
                        )
                if parameter.get("size", {}).get("mechanism", None) == "ivi-dance-with-a-twist":
                    size = parameter["size"]
                    ivi_dance_with_a_twist_params.append(parameter["name"])
                    ivi_dance_with_a_twist_sizes.add(size["value"])
                    ivi_dance_with_a_twist_twists.add(size["value_twist"])
                if duplicate_resource_handles_allowed:
                    if not is_init_method:
                        if parameter["direction"] == "out" and parameter[
                            "type"
                        ] in service_helpers.get_resource_handle_types(metadata["config"]):
                            raise Exception(
                                f"{metadata['config']['namespace_component']} allows duplicate resource handles in the session repository. Therefore, the handle we'd get for \"{parameter['name']}\" can't be mapped back to a Session to provide to the client!"
                            )
                if common_helpers.is_optional_param(parameter):
                    if common_helpers.is_enum(parameter):
                        raise Exception(
                            f"\"{parameter['name']}\" is marked optional and an enum which doesn't make sense!"
                        )
                    if function.get("codegen_method", "public") != "CustomCode":
                        raise Exception(
                            f"\"{parameter['name']}\" is marked optional but the function is not marked CustomCode!"
                        )
    except Exception as e:
        raise Exception(f"Failed to validate function {function_name}") from e


def _validate_attribute(attribute: dict, metadata: dict):
    try:
        if metadata["config"]["module_name"] == "nisync":
            # The attributes for nisync only have a name
            SIMPLE_ATTRIBUTE_SCHEMA.validate(attribute)
        else:
            ATTRIBUTE_SCHEMA.validate(attribute)
        if "enum" in attribute:
            if attribute["enum"] not in metadata["enums"]:
                raise Exception(
                    f"attribute {attribute['name']} has enum {attribute['enum']} that was not found!"
                )

    except Exception as e:
        raise Exception(
            f"Failed to validate attribute with name {attribute.get('name', '(none)')}"
        ) from e


def _validate_enum(enum_name: str, used_enums: Set[str], metadata: dict):
    try:
        enum: Dict[str, Any] = metadata["enums"][enum_name]
        ENUM_SCHEMA.validate(enum)
        if enum_name in used_enums:
            generate_mappings = enum.get("generate-mappings", False)
            value_types = set([type(value["value"]) for value in enum["values"]])
            if not generate_mappings:
                value_types.remove(type(1))
                if any(value_types):
                    raise Exception(
                        f"generate-mappings is False, but values have non-int types: {value_types}"
                    )
            # This is to avoid the duplicate enum value rule running on Attribute enums
            # that will be present in the pre-mutated drivers.
            if metadata["config"]["driver_name"] in _ALREADY_MUTATED:
                return
            values = [value["value"] for value in enum["values"]]
            values_set = set(values)
            if len(values) != len(values_set):
                if not _rule_is_suppressed(
                    metadata, RULES.ENUMS_SHOULD_NOT_HAVE_DUPLICATE_VALUES, ["enums", enum_name]
                ):
                    raise Exception(f"Duplicate values in enum!")
        else:
            raise Exception(
                f"Enum is in metadata but is not referenced by a function/attribute or force-included."
            )
    except Exception as e:
        raise Exception(f"Failed to validate enum with name {enum_name}") from e


def _validate_parameter_size(parameter: dict, function_name: str, metadata: dict):
    function: Dict[str, Any] = metadata["functions"][function_name]
    size = parameter.get("size", None)
    if size is None:
        if common_helpers.is_array(parameter.get("type", "")) and not _is_string_type(
            parameter, metadata
        ):
            if not _rule_is_suppressed(
                metadata,
                RULES.ARRAY_PARAMETER_NEEDS_SIZE,
                ["functions", function_name, "parameters", parameter["name"]],
            ):
                raise Exception(f"parameter {parameter['name']} is an array but has no size!")
    if size is not None:
        SIZE_SCHEMA.validate(size)
        mechanism = size["mechanism"]
        if mechanism in [
            "len",
            "len-in-bytes",
            "ivi-dance",
            "ivi-dance-with-a-twist",
            "passed-in",
            "passed-in-by-ptr",
            "two-dimension",
        ]:
            if not _parameter_name_exists(function, size["value"]):
                raise Exception(
                    f"parameter {parameter['name']} refers to nonexistant parameter {size['value']} in its size value!"
                )
        if mechanism == "two-dimension":
            size_param = common_helpers.get_param_with_name(function["parameters"], size["value"])
            if common_helpers.has_size_mechanism_tag(size_param, "optional"):
                # There may be a case where this is valid, but it's more likely as a mistake.
                raise Exception(
                    f"parameter {size_param['name']} is optional but used by {parameter['name']} as a two-dimension size param!"
                )

        if mechanism == "ivi-dance-with-a-twist":
            if "value_twist" not in size:
                raise Exception(
                    f"parameter {parameter['name']} doesn't have value_twist in its size parameter!"
                )
            if not _parameter_name_exists(function, size["value_twist"]):
                raise Exception(
                    f"parameter {parameter['name']} refers to nonexistant parameter {size['value_twist']} in its size value_twist!"
                )
        else:
            if "value_twist" in size:
                raise Exception(
                    f"parameter {parameter['name']} has value_twist in its size parameter but is not ivi-dance-with-a-twist!"
                )
        if parameter["direction"] == "in":
            if mechanism == "passed-in" or mechanism == "passed-in-by-ptr":
                if not _rule_is_suppressed(
                    metadata,
                    RULES.INPUT_ARRAY_SHOULD_NOT_HAVE_PASSED_IN_SIZE,
                    ["functions", function_name, "parameters", parameter["name"]],
                ):
                    raise Exception(
                        f"parameter {parameter['name']} is an input but has mechanism {mechanism}! Use mechanism len instead so the user doesn't have to explicitly pass in the size."
                    )
            if mechanism in ["ivi-dance", "ivi-dance-with-a-twist"]:
                raise Exception(
                    f"parameter {parameter['name']} is an input but has mechanism {mechanism}!"
                )
        else:
            if mechanism in ["len", "len-in-bytes"]:
                raise Exception(
                    f"parameter {parameter['name']} is an output but has mechanism {mechanism}!"
                )


def _get_attribute_enums(metadata: dict) -> Set[str]:
    attribute_enums = set()
    for attribute_group in common_helpers.get_attribute_groups(metadata):
        for attribute_id in attribute_group.attributes:
            attribute = attribute_group.attributes[attribute_id]
            if "enum" in attribute:
                attribute_enums.add(attribute["enum"])
    return attribute_enums


def _is_string_type(parameter: dict, metadata: dict) -> bool:
    if parameter.get("is_compound_type", False):
        return False
    grpc_type = parameter.get("grpc_type", None)
    if grpc_type is None:
        grpc_type = common_helpers.get_grpc_type(parameter["type"], metadata["config"])
    return grpc_type == "string"
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/proto_helpers.py sha256=18808821784ceb417227ed1e39cab797e6be9d838ac9912b0cd801a95079043b bytes=11262 -->
## FILE: source/codegen/proto_helpers.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/proto_helpers.py`
- sha256: `18808821784ceb417227ed1e39cab797e6be9d838ac9912b0cd801a95079043b`
- bytes: 11262

````python
"""Helpers for creating .proto files."""

from typing import List

import common_helpers


def _is_attribute_values(enum_name):
    return enum_name.endswith("AttributeValues")


def _should_add_unspecified_enum_value(enum_name, enum_values_metadata):
    """Return whether an UNSPECIFIED zero-value enum should be added to enum_values_metadata.

    UNSPECIFIED zero-values are a best practice in protobuf. BUT they're not helpful if there
    is some other zero-value. In that case they introduce an unnecessary alias and don't serve
    their purpose of ensuring a neutral default value.

    AttributeValues are aggregate enums that maybe have multiple zero value enums that may not
    be at the front of the list (also a requirement for protobuf). They always get an UNSPECIFIED
    value.
    """
    return _is_attribute_values(enum_name) or 0 not in (v["value"] for v in enum_values_metadata)


def _should_allow_alias(enum_values_metadata):
    # if enum.get("generate-mappings", False):
    #   return False
    enum_values = [e["value"] for e in enum_values_metadata]
    return len(enum_values) != len(set(enum_values))


def generate_parameter_field_number(parameter, used_indexes, field_name_suffix=""):
    """Get unique field number for field corresponding to this parameter in proto file.

    If field number is not stored in metadata of parameter, get the next unused integer value.
    """
    field_name_key = f"grpc{field_name_suffix}_field_number"
    if field_name_key in parameter:
        field_number = parameter[field_name_key]
    else:
        field_number = next(i for i in range(1, 100) if i not in used_indexes)
    used_indexes.append(int(field_number))
    return field_number


def get_enum_definitions(enums_to_define, enums):
    """Get a simplified definition for enums and the values in it.

    This is intended to be used for defining enums in the proto file.
    """
    enum_definitions = {}
    for enum_name in (e for e in enums if e in enums_to_define):
        enum = enums[enum_name]
        enum_value_prefix = common_helpers.get_enum_value_prefix(enum_name, enum)
        if enum.get("generate-mappings", False):
            values = [
                {"name": f"{enum_value_prefix}_{value['name']}", "value": index + 1}
                for index, value in enumerate(enum["values"])
            ]
        else:
            values = [
                {"name": f"{enum_value_prefix}_{value['name']}", "value": value["value"]}
                for value in enum["values"]
            ]

        if _should_add_unspecified_enum_value(enum_name, values):
            unspecified_value_name = (
                f"{enum_value_prefix}_MAPPED_UNSPECIFIED"
                if enum_name.endswith("AttributeValuesMapped")
                else f"{enum_value_prefix}_UNSPECIFIED"
            )
            values.insert(0, {"name": unspecified_value_name, "value": 0})

        allow_alias = _should_allow_alias(values)
        enum_definition = {"allow_alias": allow_alias, "values": values}

        enum_definitions.update({enum_name: enum_definition})

    return enum_definitions


def _is_array_input(parameter: dict):
    return common_helpers.is_array(parameter["type"]) and common_helpers.is_input_parameter(
        parameter
    )


def _is_decomposable_enum(parameter: dict):
    """Return whether the parameter is a decomposable enum.

    Enums are typically decomposed from a single param into an enum param and an _raw param.
    The exception is array_inputs which are left as single enum param.
    This is because protobuf does not support oneof on repeated types, so the standard input
    decomposition does not work for arrays.
    """
    return common_helpers.is_enum(parameter) and not (
        _is_array_input(parameter) and parameter["grpc_type"] != "string"
    )


def get_message_parameter_definitions(parameters):
    """Get a simplified list of all parameters.

    This is intended to be used for defining requests/response messages in proto file.
    """
    parameter_definitions = []
    used_indexes = []
    for parameter in parameters:
        is_array = (
            common_helpers.is_array(parameter["type"]) and not parameter["grpc_type"] == "string"
        )
        parameter_name = common_helpers.get_grpc_field_name(parameter)
        parameter_type = _get_parameter_type(parameter)
        if _is_decomposable_enum(parameter):
            is_request_message = common_helpers.is_input_parameter(parameter)
            enum_parameters = _get_enum_parameters(
                parameter, parameter_name, parameter_type, is_array, used_indexes
            )
            if is_request_message and not common_helpers.is_bitfield_as_enum_array(parameter):
                # use oneof for enums in request messages
                parameter_definitions.append(
                    {
                        "name": f"{parameter_name}_enum",
                        "use_oneof": True,
                        "parameters": enum_parameters,
                    }
                )
            else:
                # we define all enum fields in response messages
                parameter_definitions.extend(enum_parameters)
        else:
            if common_helpers.is_enum(parameter):
                # For input arrays of enums, don't generate a raw type, but do use the correct enum
                # type.
                parameter_type = f'repeated {parameter["enum"]}'
            grpc_field_number = generate_parameter_field_number(parameter, used_indexes)
            is_get_last_error_output = common_helpers.is_get_last_error_output_param(parameter)
            is_optional = common_helpers.is_optional_param(parameter)
            parameter_definitions.append(
                {
                    "name": parameter_name,
                    "type": parameter_type,
                    "grpc_field_number": grpc_field_number,
                    "is_get_last_error_output": is_get_last_error_output,
                    "is_optional": is_optional,
                }
            )
    return parameter_definitions


def _get_enum_parameters(parameter, parameter_name, parameter_type, is_array, used_indexes):
    """Get list of mapped/unmapped/raw parameters for enums as applicable."""
    enum_parameters = []
    if parameter.get("enum", None):
        enum_parameter_type = f"repeated {parameter['enum']}" if is_array else parameter["enum"]
        grpc_enum_field_number = generate_parameter_field_number(parameter, used_indexes)
        enum_parameters.append(
            {
                "name": parameter_name,
                "type": enum_parameter_type,
                "grpc_field_number": grpc_enum_field_number,
            }
        )
    if parameter.get("mapped-enum", None):
        mapped_type = (
            f"repeated {parameter['mapped-enum']}" if is_array else parameter["mapped-enum"]
        )
        grpc_mapped_field_number = generate_parameter_field_number(
            parameter, used_indexes, "_mapped"
        )
        enum_parameters.append(
            {
                "name": f"{parameter_name}_mapped",
                "type": mapped_type,
                "grpc_field_number": grpc_mapped_field_number,
            }
        )
    if "bitfield_as_enum_array" in parameter:
        enum_parameters.append(
            {
                "name": f"{parameter_name}_array",
                "type": f"repeated {parameter['bitfield_as_enum_array']}",
                "grpc_field_number": generate_parameter_field_number(
                    parameter, used_indexes, "_array"
                ),
            }
        )

    grpc_raw_field_number = generate_parameter_field_number(parameter, used_indexes, "_raw")
    enum_parameters.append(
        {
            "name": f"{parameter_name}_raw",
            "type": parameter_type,
            "grpc_field_number": grpc_raw_field_number,
        }
    )
    return sorted(enum_parameters, key=lambda x: x["grpc_field_number"])


def _get_parameter_type(parameter):
    if "grpc_type" not in parameter:
        raise KeyError(f"grpc_type not in {parameter['name']} with {parameter['type']}")
    return parameter["grpc_type"]


def is_session_name(parameter):
    """Whether the parameter is a session name parameter."""
    return parameter.get("is_session_name", False)


def _prepend_proto_only_session_name_parameter_if_necessary(
    func, input_parameters: List[dict]
) -> None:
    has_session_input = any(is_session_name(param) for param in input_parameters)
    # If the API defines a "session_name" param, we don't need to add another one.
    if not has_session_input:
        is_array_init = common_helpers.is_init_array_method(func)
        session_name_param = {
            "direction": "in",
            "name": "session_names" if is_array_init else "session_name",
            "type": "ViString",  # Not really used since this is proto/service-only
            "grpc_type": "repeated string" if is_array_init else "string",
        }
        input_parameters.insert(0, session_name_param)


def get_parameters(function):
    """Filter the parameters to ones we use in gRPC, and split into input/output parameters.

    Add a default "status" output parameter if there isn't one already.
    """
    parameter_array = common_helpers.filter_parameters_for_grpc_fields(function["parameters"])
    input_parameters = [p for p in parameter_array if common_helpers.is_input_parameter(p)]
    if common_helpers.is_init_method(function):
        _prepend_proto_only_session_name_parameter_if_necessary(function, input_parameters)

    default_status_param = {"name": "status", "type": "int32", "grpc_type": "int32"}
    output_parameters = [default_status_param]

    if common_helpers.has_async_streaming_response(function):
        callback_parameters = _get_callback_output_params(function)

        if any((p for p in callback_parameters if p["name"] == "status")):
            # if the callback provides a status, it can override default_status_param.
            output_parameters = callback_parameters
        else:
            output_parameters.extend(callback_parameters)
    else:
        output_parameters.extend(
            [p for p in parameter_array if common_helpers.is_output_parameter(p)]
        )

    return (input_parameters, output_parameters)


def _get_callback_output_params(function):
    """Look for a parameter that specifies callback_params and return those params.

    These will be used as the outputs of a streaming response.
    """
    params = [p for p in function["parameters"] if "callback_params" in p]
    if params:
        return common_helpers.filter_parameters_for_grpc_fields(params[0]["callback_params"])
    else:
        return []


def get_streaming_response_qualifier(function):
    """Get a qualifier to add to the function's returned response object if it uses streaming."""
    return "stream " if common_helpers.has_streaming_response(function) else ""
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/service_helpers.py sha256=a9cfb0642cb33d45b439a23cdbd238763d5a3200219c97110260d2782b7923e3 bytes=29288 -->
## FILE: source/codegen/service_helpers.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/service_helpers.py`
- sha256: `a9cfb0642cb33d45b439a23cdbd238763d5a3200219c97110260d2782b7923e3`
- bytes: 29288

````python
"""Helpers for creating service .h/.cpp files."""

from typing import Any, Dict, List, NamedTuple, Optional

import common_helpers


def get_include_guard_name(config, suffix):
    """Get an appropriate #include guard name."""
    include_guard_name = config["namespace_component"] + "_grpc" + suffix
    return include_guard_name.upper()


def get_c_element_type_for_array_that_needs_coercion(parameter):
    """Get the C element type for the given parameter, if it's an array that needs coercion."""
    if not parameter.get("coerced", False):
        return None
    if not common_helpers.is_array(parameter["type"]):
        return None
    return get_c_element_type(parameter)


def get_c_element_type(parameter):
    """Get the C element type for the given parameter."""
    stripped_type = parameter["type"]
    stripped_type = common_helpers.strip_prefix(stripped_type, "const ")
    stripped_type = common_helpers.strip_suffix(stripped_type, "*")
    stripped_type = common_helpers.strip_suffix(stripped_type, "[]")
    return stripped_type


def is_scalar_input_that_needs_coercion(parameter: dict) -> bool:
    """Whether the parameter is a scalar input that needs coercion."""
    return (
        common_helpers.is_input_parameter(parameter)
        and parameter.get("coerced", False)
        and not common_helpers.is_array(parameter["type"])
    )


def is_input_array_that_needs_coercion(parameter):
    """Whether the parameter is an input array that needs coercion."""
    return (
        common_helpers.is_input_parameter(parameter)
        and get_c_element_type_for_array_that_needs_coercion(parameter) is not None
    )


def _is_input_that_needs_coercion(parameter, custom_types: list):
    if not common_helpers.is_input_parameter(parameter):
        return False
    if parameter.get("coerced", False):
        return True
    if not common_helpers.is_struct(parameter):
        return False
    underlying_struct_name = common_helpers.get_underlying_type_name(parameter["type"])
    underlying_structs = [
        custom_type for custom_type in custom_types if custom_type["name"] == underlying_struct_name
    ]
    if not any([underlying_structs]):
        return False
    custom_type = underlying_structs[0]
    return any([field.get("coerced", False) for field in custom_type["fields"]])


def is_output_array_that_needs_coercion(parameter):
    """Whether the parameter is an output array that needs coercion."""
    return (
        common_helpers.is_output_parameter(parameter)
        and get_c_element_type_for_array_that_needs_coercion(parameter) is not None
    )


def create_args_for_callback(parameters):
    """Get the args needed for a CallbackRouter handler."""
    return ", ".join([f'{p["type"]} {common_helpers.get_grpc_field_name(p)}' for p in parameters])


def _is_array_that_requires_conversion(parameter):
    """Return whether the protobuf representation is not the same as the C API representation."""
    is_array = common_helpers.is_array(parameter["type"])

    if is_array:
        return (
            common_helpers.supports_standard_copy_conversion_routines(parameter)
            or get_c_element_type_for_array_that_needs_coercion(parameter) is not None
            # Sessions are "converted" by accessing the session repository.
            or parameter["grpc_type"] == "repeated nidevice_grpc.Session"
            # Vi*Int16s have a hardcoded copy convert routine that predates the coerced flag.
            or parameter["type"] == "ViInt16[]"
            or parameter["type"] == "ViUInt16[]"
        )

    return False


def _create_standard_arg(parameter):
    parameter_name = common_helpers.get_cpp_local_name(parameter)
    is_array = common_helpers.is_array(parameter["type"])
    is_output = common_helpers.is_output_parameter(parameter)
    is_hardcoded = "hardcoded_value" in parameter
    if is_output and common_helpers.is_string_arg(parameter):
        type_without_brackets = common_helpers.get_underlying_type_name(parameter["type"])
        return f"({type_without_brackets}*){parameter_name}.data(), "
    elif _is_array_that_requires_conversion(parameter):
        # Converted arrays are allocated into a std::vector. Access the C array via data().
        return f"{parameter_name}.data(), "
    elif "callback_params" in parameter and not is_hardcoded:
        return f"CallbackRouter::handle_callback, "
    elif "callback_token" in parameter and not is_hardcoded:
        return f"handler->token(), "
    elif is_size_param_passed_by_ptr(parameter):
        return f"&{parameter_name}_copy, "
    elif not is_array and is_output:
        return f"&{parameter_name}, "
    elif (
        not is_array
        and not is_output
        and "pointer" in parameter
        and "input_passed_by_ptr" in parameter
    ):
        return f"&{parameter_name}, "
    return f"{parameter_name}, "


def create_args(parameters):
    """Get the args needed to call the library function."""
    parameters = common_helpers.get_driver_api_params(parameters)
    result = ""
    have_expanded_varargs = False
    for parameter in parameters:
        if parameter.get("proto_only", False):
            continue
        if parameter.get("repeating_argument", False):
            continue
        parameter_name = common_helpers.get_cpp_local_name(parameter)
        if common_helpers.is_repeated_varargs_parameter(parameter):
            # Some methods have both input and output repeated varargs parameters,
            # so only expand them once.
            if have_expanded_varargs:
                continue
            have_expanded_varargs = True
            repeated_parameters = [
                p for p in parameters if common_helpers.is_repeating_parameter(p)
            ]
            # We need to pass one extra set of arguments because the last parameters have to be
            # nullptr's so the callee knows we're done passing arguments.
            max_length = parameter["max_length"] + 1
            for i in range(max_length):
                for parameter in repeated_parameters:
                    if common_helpers.is_input_parameter(parameter):
                        result += f'get_{parameter["name"]}_if({parameter_name}, {i}), '
                    else:
                        result += f'get_{parameter["name"]}_if({parameter["name"]}Vector, {i}), '
        else:
            result = f"{result}{_create_standard_arg(parameter)}"
    return result[:-2]


def create_args_for_ivi_dance(parameters):
    """Get the args needed to call the ivi-dance library function."""
    result = ""
    for parameter in parameters:
        if parameter.get("is_size_param", False):
            result = f"{result}0, "
        elif common_helpers.is_output_parameter(parameter):
            result = f"{result}nullptr, "
        else:
            result = result + _create_standard_arg(parameter)
    return result[:-2]


def create_args_for_ivi_dance_with_a_twist(parameters):
    """Get the args needed to call the ivi-dance-with-a-twist library function."""
    result = ""
    ivi_twist_array_params = [
        p for p in parameters if common_helpers.get_size_mechanism(p) == "ivi-dance-with-a-twist"
    ]
    arrays = {p["name"] for p in ivi_twist_array_params}
    twists = {p["size"]["value_twist"] for p in ivi_twist_array_params}
    sizes = {p["size"]["value"] for p in ivi_twist_array_params}

    for parameter in parameters:
        c_name = common_helpers.get_cpp_local_name(parameter)
        name = parameter["name"]
        if name in arrays:
            result = f"{result}nullptr, "
        elif name in twists:
            # Pass the twist output param by pointer.
            result = result + f"&{c_name}" + ", "
        elif name in sizes:
            result = f"{result}0, "
        else:
            result = result + _create_standard_arg(parameter)
    return result[:-2]


def create_params(parameters, expand_varargs=True):
    """Get the params needed for defining the library function."""
    parameters = common_helpers.get_driver_api_params(parameters)
    if not len(parameters):
        return ""
    repeated_parameters = [p for p in parameters if common_helpers.is_repeating_parameter(p)]
    # Some methods have both input and output repeated varargs parameters,
    # so only expand them once.
    if common_helpers.is_repeated_varargs_parameter(
        parameters[-1]
    ) and common_helpers.is_repeated_varargs_parameter(parameters[-2]):
        parameters = parameters[:-1]
    return ", ".join(
        _create_param(p, expand_varargs, repeated_parameters)
        for p in parameters
        if not p.get("proto_only", False)
    )


def _get_array_param_size(parameter) -> str:
    if "size" in parameter and parameter["size"]["mechanism"] == "fixed":
        return parameter["size"]["value"]

    return ""


def expand_varargs_parameters(parameters):
    """Get a modified list of parameters, with repeating_parameters repeated max_length times.

    The max_length value comes from the first repeated_var_args parameter. Each repeated parameter
    gets a number (starting at zero) appended to the parameter name.
    """
    parameters = common_helpers.get_driver_api_params(parameters)
    updated_parameters = [
        {**p, "cppName": p.get("value_converted_to_c_representation", p.get("cppName"))}
        for p in parameters
    ]
    if not common_helpers.has_repeated_varargs_parameter(updated_parameters):
        return updated_parameters
    # omit the varargs parameters that we're going to expand
    new_parameters = [p for p in parameters if not common_helpers.is_repeated_varargs_parameter(p)]
    varargs_parameters = [p for p in parameters if common_helpers.is_repeated_varargs_parameter(p)]
    max_length = varargs_parameters[0]["max_length"]
    repeated_parameters = [p for p in parameters if common_helpers.is_repeating_parameter(p)]
    for i in range(max_length):
        for p in repeated_parameters:
            new_parameters.append({"cppName": f'{p["name"]}{i}'})
    return new_parameters


def _create_param(parameter, expand_varargs=True, repeated_parameters=None):
    type = parameter["type"]
    name = parameter["cppName"]
    if common_helpers.is_struct(parameter):
        type = type.replace("struct ", "")
    if common_helpers.is_repeated_varargs_parameter(parameter):
        if expand_varargs:
            max_length = parameter["max_length"]
            s = ""
            for i in range(max_length):
                for parameter in repeated_parameters:
                    real_field_name = parameter["cppName"]
                    parameter["cppName"] = f"{real_field_name}{i}"
                    s += _create_param(parameter, expand_varargs=False) + ", "
                    parameter["cppName"] = real_field_name
            return s[:-2]
        else:
            return "..."
    elif common_helpers.is_array(type):
        if type == "void *":
            return f"void* {name}"
        array_size = _get_array_param_size(parameter)
        if type[:-2] == "void":  # Having void[] in C++ is not allowed, hence using it as void*
            return f"{type[:-2]}* {name}"
        else:
            return f"{type[:-2]} {name}[{array_size}]"
    else:
        pointer_qualifier = "*" * common_helpers.levels_of_pointer_indirection(parameter)
        return f"{type}{pointer_qualifier} {name}"


def _format_value(value):
    if isinstance(value, str):
        value = f'"{value}"'
    if isinstance(value, float):
        value = f"{value}f"
    return value


def get_input_lookup_values(enum_data):
    """Get an initializer list for a std::map that maps enum value index to enum value value."""
    out_value_format = ""
    is_int = isinstance(enum_data["values"][0]["value"], int)
    if is_int:
        out_value_format = "{0, 0},"
    for i, value in enumerate(enum_data["values"]):
        formated_value = str(_format_value(value["value"]))
        out_value_format += f"{{{i + 1}, {formated_value}}},"
    return out_value_format


def get_output_lookup_values(enum_data):
    """Get an initializer list for a std::map that maps enum value value to enum value index."""
    out_value_format = ""
    is_int = isinstance(enum_data["values"][0]["value"], int)
    if is_int:
        out_value_format = "{0, 0},"
    for i, value in enumerate(enum_data["values"]):
        formated_value = _format_value(value["value"])
        out_value_format += f"{{{formated_value}, {i + 1}}},"
    return out_value_format


def generate_enum_oneof_selector_map(enum_data):
    """ "Get an initializer list for a std::map that maps enum value value to enum value type."""
    id_type_content = ""
    for i, value in enumerate(enum_data["values"]):
        formated_value = _format_value(value["value"])
        type = value["type"]
        id_type_content += f"{{{formated_value}, {type}_}},"
    return id_type_content


def filter_api_functions(functions, only_mockable_functions=True):
    """Filter function metadata to only include those to be generated into the API library."""

    def filter_function(function):
        if function.get("codegen_method", "") in ["no", "CustomCodeNoLibrary"] or function.get(
            "is_streaming_api", False
        ):
            return False
        if only_mockable_functions and not common_helpers.can_mock_function(function["parameters"]):
            return False
        return True

    return [name for name, function in functions.items() if filter_function(function)]


def filter_proto_rpc_functions_to_generate(functions):
    """Return function metadata only for functions to include for generating proto rpc methods."""
    functions_for_code_gen = {"public"}
    return [
        name
        for name, function in functions.items()
        if function.get("codegen_method", "public") in functions_for_code_gen
    ]


def get_cname(functions, method_name, c_function_prefix):
    """Get the C name of the function."""
    if "cname" in functions[method_name]:
        return functions[method_name]["cname"]
    return c_function_prefix + method_name


def is_private_method(function_data):
    """Whether the function is private."""
    return function_data.get("codegen_method", "") == "private"


def is_custom_close_method(function_data):
    """Whether the function is a custom_close_method."""
    return function_data.get("custom_close_method", False)


def requires_checked_conversion(parameters, custom_types):
    """Whether any parameter needs coercion."""
    return any([_is_input_that_needs_coercion(p, custom_types) for p in parameters])


def get_request_param(method_name):
    """Get a parameter for taking in a Request object for the function with the given name."""
    return f"const {get_request_type(method_name)}* request"


def get_request_type(method_name):
    """Get the name of the Request class for the function with the given name."""
    return f"{method_name}Request"


def get_response_param(method_name):
    """Get a parameter for taking in a Response object for the function with the given name."""
    return f"{get_response_type(method_name)}* response"


def get_response_type(method_name):
    """Get the name of the Response class for the function with the given name."""
    return f"{method_name}Response"


def get_async_functions(functions):
    """Filter the functions to include only async functions (those with a streaming response)."""
    return {
        name: data
        for name, data in functions.items()
        if common_helpers.has_streaming_response(data)
    }


def get_functions_with_two_dimension_param(functions):
    """Filter the functions to include only those with a two-dimension array parameter."""
    return {
        name: data
        for name, data in functions.items()
        if common_helpers.has_two_dimension_array_param(data["parameters"])
    }


def get_callback_method_parameters(function_data):
    """Get the parameters of the given function's callback function parameter."""
    parameters = function_data["parameters"]
    callback_ptr_parameter = next((p for p in parameters if "callback_params" in p))
    output_parameters = callback_ptr_parameter["callback_params"]

    return output_parameters


def create_param_type_list(parameters):
    """Get a comma-separated list of parameter types."""
    return ", ".join([p["type"] for p in parameters])


def get_feature_toggles(config: dict) -> Dict[str, str]:
    """Get the feature_toggles config setting."""
    return config.get("feature_toggles", {})


def get_toggle_member_name(fully_qualified_toggle_name: str) -> str:
    """Get the member name to use for the given toggle, in the FeatureToggles class."""
    toggle_name = fully_qualified_toggle_name.split(".")[-1]
    return f"is_{toggle_name}_enabled"


def get_driver_service_readiness(config: dict) -> str:
    """Get the C++ constant representing the driver's code_readiness."""
    readiness = common_helpers.get_driver_readiness(config)
    return to_cpp_readiness(readiness)


def is_restricted_driver_service(config):
    """Whether the driver service is restricted."""
    return common_helpers.is_driver_restricted(config)


def to_cpp_readiness(user_readiness: str) -> str:
    """Get the C++ constant representing the given code_readiness."""
    return f"CodeReadiness::k{user_readiness}"


def get_enums_to_map(functions: dict, enums: dict) -> List[str]:
    """Get a list of the enums used by functions, for which mappings should be generated."""

    def get_enum_or_default(enum_name: str) -> dict:
        # Enums that are added during metadata mutation (like attributes)
        # may not be in the enum dictionary. Assume they don't generate-mappings.
        return enums.get(enum_name, {})

    def should_generate_mappings(enum_name: str) -> bool:
        enum = get_enum_or_default(enum_name)
        return enum.get("generate-mappings", False)

    function_enums = common_helpers.get_function_enums(functions, enums)
    return [e for e in function_enums if should_generate_mappings(e)]


def generate_mapping_enums_to_type(enums: dict) -> List[str]:
    """Get a list of the enums used by functions, for which mappings should be generated."""
    list_of_enums: List[str] = []
    for enum_name in enums.keys():
        if "generate-mapping-type" in enums[enum_name]:
            list_of_enums.append(enum_name)
    return list_of_enums


def get_distinct_types_from_enums(enums: dict) -> str:
    """Return a comma seperated string of different data types used in enums value type field."""
    distinct_type = set()
    for enum_name in enums.keys():
        if "generate-mapping-type" in enums[enum_name]:
            for i, value in enumerate(enums[enum_name]["values"]):
                type = value["type"]
                distinct_type.add(f"{type}_")
    return str.join(", ", sorted(distinct_type))


def get_bitfield_value_to_name_mapping(parameter: dict, enums: dict) -> Dict[int, str]:
    """Get a mapping from bitfield values to the corresponding C++ enum value constants."""
    enum_name = parameter["bitfield_as_enum_array"]
    enum = enums[enum_name]
    enum_value_prefix = common_helpers.get_enum_value_prefix(enum_name, enum)
    enum_qualified_name_prefix = f"{enum_name}::{enum_value_prefix}"

    return {
        v["value"]: f"{enum_qualified_name_prefix}_{v['name']}"
        for v in enum["values"]
        if v["value"] != 0  # zero values can't be flags!
    }


def get_resource_handle_types(config: dict) -> List[str]:
    """Get the resource_handle_type config setting."""
    resource_handle_type = config.get("resource_handle_type", ["ViSession"])
    if isinstance(resource_handle_type, str):
        return [resource_handle_type]
    else:
        return resource_handle_type


def _get_shared_resource_repository_ptr_type(resource_handle_type: str) -> str:
    resource_repository_type = f"nidevice_grpc::SessionResourceRepository<{resource_handle_type}>"
    return f"std::shared_ptr<{resource_repository_type}>"


class CrossDriverSessionDependency(NamedTuple):  # noqa: D101
    resource_handle_type: str
    resource_repository_alias: str
    resource_repository_type: str
    field_name: str
    local_name: str


SessionRepositoryHandleTypeDependencyMap = Dict[str, CrossDriverSessionDependency]


def get_driver_shared_resource_repository_ptr_deps(
    driver_config: dict, functions: dict
) -> SessionRepositoryHandleTypeDependencyMap:
    """Get handle-type to CrossDriverSessionDependency map used by this driver.

    Combine resource_handle_type and cross_driver_session types in single map since both
    of them together decide repositories required by driver. Combining into single map also
    helps remove duplicates.
    """
    resource_repository_deps = [
        _create_cross_driver_session_dependency(resource_handle_type)
        for resource_handle_type in get_resource_handle_types(driver_config)
    ]

    resource_repository_deps[0] = CrossDriverSessionDependency(
        resource_repository_deps[0].resource_handle_type,
        "ResourceRepositorySharedPtr",
        resource_repository_deps[0].resource_repository_type,
        "session_repository_",
        "resource_repository",
    )

    resource_repository_type_dependency_map = {
        d.resource_handle_type: d for d in resource_repository_deps
    }

    for d in get_cross_driver_session_dependencies(functions):
        resource_repository_type_dependency_map.update({d.resource_handle_type: d})

    return resource_repository_type_dependency_map


def _create_cross_driver_session_dependency(
    resource_handle_type: str,
) -> CrossDriverSessionDependency:
    return CrossDriverSessionDependency(
        resource_handle_type,
        f"{resource_handle_type}ResourceRepositorySharedPtr",
        _get_shared_resource_repository_ptr_type(resource_handle_type),
        f"{common_helpers.pascal_to_snake(resource_handle_type)}_resource_repository_",
        f"{common_helpers.pascal_to_snake(resource_handle_type)}_resource_repository",
    )


def _get_cross_driver_session_type(parameter: dict) -> Optional[str]:
    return parameter.get("cross_driver_session")


def get_cross_driver_session_dependencies(functions: dict) -> List[CrossDriverSessionDependency]:
    """Get a list of cross-driver session dependencies needed by any function parameter."""
    cross_driver_session_types = (
        _get_cross_driver_session_type(p) for f in functions.values() for p in f["parameters"]
    )
    return sorted(
        set(_create_cross_driver_session_dependency(t) for t in cross_driver_session_types if t)
    )


def get_cross_driver_session_dependency(parameter: dict) -> CrossDriverSessionDependency:
    """Get the cross-driver session dependency needed by the given parameter."""
    return _create_cross_driver_session_dependency(parameter["cross_driver_session"])


def session_repository_field_name(param: dict, config: dict) -> str:
    """Get the name of the session repository field used for the given parameter."""
    cross_driver_session_type = _get_cross_driver_session_type(param)

    if cross_driver_session_type:
        return get_cross_driver_session_dependency(param).field_name
    else:
        resource_handle_deps = get_driver_shared_resource_repository_ptr_deps(
            config,
            functions={},  # This is called for retrieving session repo field name for specific parameter, functions is not needed
        )
        resource_handle_dep = next(
            resource_handle_deps[resource_handle_type]
            for resource_handle_type in resource_handle_deps
            if resource_handle_type == common_helpers.get_underlying_type(param)
        )
        return resource_handle_dep.field_name


SessionRepositoryHandleTypeMap = Dict[str, Dict[str, Any]]


def list_session_repository_handle_types(
    driver_configs: List[dict],
) -> SessionRepositoryHandleTypeMap:
    """Get per-handle type config info, for the resource handle types used by the given configs.

    The included config info keys are: local_name and windows_only.
    """
    session_repository_handle_type_map = {}  # type: SessionRepositoryHandleTypeMap
    for config in driver_configs:
        handle_types = get_resource_handle_types(config)
        for handle_type in handle_types:
            if handle_type in session_repository_handle_type_map:
                old_windows_only = session_repository_handle_type_map[handle_type]["windows_only"]
                new_windows_only = config.get("windows_only", False) and old_windows_only
                session_repository_handle_type_map[handle_type]["windows_only"] = new_windows_only
            else:
                session_repository_handle_type_map[handle_type] = {
                    "local_name": f"{common_helpers.pascal_to_snake(handle_type)}_repository",
                    "windows_only": config.get("windows_only", False),
                }
    return session_repository_handle_type_map


def get_function_return_type(function_data: dict) -> str:
    """Get the return type for function_data."""
    return function_data["returns"]


def _get_return_value_parameter(parameters: List[dict]) -> Optional[dict]:
    return next((p for p in parameters if common_helpers.is_return_value(p)), None)


def get_return_value_name(function_data: dict) -> str:
    """Get the name of the return value for function_data. The default is "status"."""
    return_param = _get_return_value_parameter(function_data["parameters"])
    return common_helpers.get_cpp_local_name(return_param) if return_param else "status"


def has_status_expression(function_data: dict) -> bool:
    """Whether function_data has a custom status_expression."""
    return "status_expression" in function_data


def get_status_expression(function_data: dict) -> str:
    """Get the custom status_expression for function_data.

    The default is to use the value of status returned from the driver function.

    Raises if "status_expression" is not present.
    """
    return function_data["status_expression"]


def get_library_ptr_for_potentially_unmockable_function(config: dict, parameters: List[dict]):
    """Get the variable or expression for the library pointer.

    Returns library_ if parameters can be mocked and called through the shared interface,
    otherwise typecasts library to the concrete type.
    """
    return (
        "library_"
        if common_helpers.can_mock_function(parameters)
        else f"std::static_pointer_cast<{config['service_class_prefix']}Library>(library_)"
    )


def is_session_returned_from_function(parameters: List[dict]) -> bool:
    """Whether parameters includes a return_value parameter with grpc_type nidevice_grpc.Session."""
    return_param = _get_return_value_parameter(parameters)
    return return_param["grpc_type"] == "nidevice_grpc.Session" if return_param else False


def should_copy_to_response(parameter: dict) -> bool:
    """Whether the value of parameter should be copied to the Response message."""
    is_included_in_response_proto = parameter.get("include_in_proto", True)
    # Repeating parameters do a special mapping in the copy logic.
    # They should execute that map/copy logic even if include_in_proto is False.
    is_mapped_as_repeating_parameter = common_helpers.is_repeating_parameter(parameter)
    return is_included_in_response_proto or is_mapped_as_repeating_parameter


def is_size_param_passed_by_ptr(parameter: dict) -> bool:
    """Return whether parameters is a size param passed-by-pointer."""
    return parameter.get("is_size_param", False) and parameter.get("pointer", False)


def get_last_error_output_params(parameters: List[dict]) -> List[dict]:
    """Return list of get_last_error parameters."""
    get_last_error_outputs = [
        p for p in parameters if common_helpers.is_get_last_error_output_param(p)
    ]
    return get_last_error_outputs


def get_protobuf_cpplib_type(grpc_type: str) -> str:
    """Return the C++ type used grpc generated code for the given protobuf type.

    Note: this implementation is incomplete. It only handles the default case
    where the grpc_type name is the same as the cpplib typename and repeated
    message types. Add other mappings as needed.
    """
    stripped_repeated = common_helpers.strip_prefix(grpc_type, "repeated ")
    if stripped_repeated != grpc_type:
        return f"google::protobuf::RepeatedPtrField<{get_protobuf_cpplib_type(stripped_repeated)}>"

    if grpc_type == "string":
        return "std::string"

    return grpc_type
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/stage_client_files.py sha256=4c47fd655c48b0ac1faa077927f167684d42ab9284b324bfd405efded20a2b12 bytes=7342 -->
## FILE: source/codegen/stage_client_files.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/stage_client_files.py`
- sha256: `4c47fd655c48b0ac1faa077927f167684d42ab9284b324bfd405efded20a2b12`
- bytes: 7342

````python
"""Stage client files."""

from argparse import ArgumentParser
from pathlib import Path
from shutil import copy2, copytree
from tempfile import TemporaryDirectory
from typing import Dict, Iterable, List

from common_helpers import get_driver_readiness, is_driver_restricted
from template_helpers import load_metadata


class _ArtifactReadiness:
    """Class to determine whether a Path with a module-named artifact directory is release-ready."""

    _module_to_readiness = {}  # type: Dict[str, str]
    _module_to_restricted = {}  # type: Dict[str, bool]

    def __init__(self, metadata_dir: Path, ignore_release_readiness: bool):
        modules = [
            load_metadata(p) for p in metadata_dir.iterdir() if p.is_dir() and "fake" not in p.name
        ]

        self._module_to_readiness = {
            d["config"]["module_name"]: get_driver_readiness(d["config"]) for d in modules
        }

        self._module_to_restricted = {
            d["config"]["module_name"]: is_driver_restricted(d["config"]) for d in modules
        }

        self.ignore_release_readiness = ignore_release_readiness

    def is_release_ready(self, module_path: Path) -> bool:
        """Determine release-readiness.

        Do so by checking the name of the module_path directory against code_readiness for the
        module_name in config.py.
        """
        module_name = module_path.name
        if "fake" in module_name:
            return False

        # Special case for multidriver examples for RF located in this folder
        if module_name in ["session", "nirf"]:
            return True

        if module_name not in self._module_to_readiness:
            raise KeyError(f"No module config.py metadata for module_name: {module_path}")

        return (
            not self._module_to_restricted[module_name]
            and self._module_to_readiness[module_name] == "Release"
        )

    def get_release_ready_subdirs(self, directory: Path) -> Iterable[Path]:
        """Return all subdirectories of directory for which is_release_ready is True."""
        return (
            d
            for d in directory.iterdir()
            if d.is_dir() and (self.is_release_ready(d) or self.ignore_release_readiness)
        )


class _ArtifactLocations:
    repo_root: Path

    def __init__(self, repo_root: Path):
        self.repo_root = repo_root

    @property
    def examples(self) -> Path:
        return self.repo_root / "examples"

    @property
    def generated_files(self) -> Path:
        return self.repo_root / "generated"

    @property
    def shared_imported_protos(self) -> Path:
        return self.repo_root / "imports" / "protobuf"

    @property
    def shared_source_protos(self) -> Path:
        return self.repo_root / "source" / "protobuf"

    @property
    def restricted_protos(self) -> Path:
        return self.repo_root / "source" / "protobuf_restricted"

    @property
    def grpcdevice_protos(self) -> Path:
        return self.repo_root / "third_party" / "ni-apis" / "ni" / "grpcdevice" / "v1"

    @property
    def protobuftypes_protos(self) -> Path:
        return self.repo_root / "third_party" / "ni-apis" / "ni" / "protobuf" / "types"

    @property
    def metadata_dir(self) -> Path:
        return self.repo_root / "source" / "codegen" / "metadata"

    @property
    def config_dir(self) -> Path:
        return self.repo_root / "source" / "config"


def _get_release_proto_files(
    artifact_locations: _ArtifactLocations, readiness: _ArtifactReadiness
) -> List[Path]:
    release_driver_dirs = readiness.get_release_ready_subdirs(artifact_locations.generated_files)
    return [proto for d in release_driver_dirs for proto in d.glob("*.proto")]


def _get_release_example_directories(
    artifact_locations: _ArtifactLocations, readiness: _ArtifactReadiness
) -> Iterable[Path]:
    return readiness.get_release_ready_subdirs(artifact_locations.examples)


def stage_client_files(output_path: Path, ignore_release_readiness: bool):
    """Stage the client files into the given output path."""
    repo_root = Path(__file__).parent.parent.parent
    artifact_locations = _ArtifactLocations(repo_root)
    readiness = _ArtifactReadiness(artifact_locations.metadata_dir, ignore_release_readiness)

    proto_path = output_path / "proto"
    proto_path.mkdir(parents=True)

    for file in artifact_locations.shared_source_protos.glob("*.proto"):
        copy2(file, proto_path)

    for file in artifact_locations.shared_imported_protos.glob("*.proto"):
        copy2(file, proto_path)

    for file in artifact_locations.grpcdevice_protos.glob("*.proto"):
        copy2(file, proto_path)

    protobuf_types_path = proto_path / "ni" / "protobuf" / "types"
    protobuf_types_path.mkdir(parents=True, exist_ok=True)
    for file in artifact_locations.protobuftypes_protos.glob("*.proto"):
        copy2(file, protobuf_types_path)

    for file in _get_release_proto_files(artifact_locations, readiness):
        copy2(file, proto_path)

    if readiness.ignore_release_readiness:
        for file in artifact_locations.restricted_protos.iterdir():
            copy2(file, proto_path)

    examples_path = output_path / "examples"
    examples_path.mkdir(parents=True)

    for dir in _get_release_example_directories(artifact_locations, readiness):
        copytree(dir, examples_path / dir.name)

    config_path = output_path / "client.d"
    config_path.mkdir(parents=True)
    copy2(
        artifact_locations.config_dir / "ni-grpc-device.client.defaults.yml",
        config_path / "ni-grpc-device.defaults.yml",
    )
    copy2(
        artifact_locations.config_dir / "ni-grpc-device.client.caps.yml",
        config_path / "ni-grpc-device.caps.yml",
    )

    copy2(artifact_locations.repo_root / "LICENSE", output_path)
    copy2(artifact_locations.repo_root / "ThirdPartyNotices.txt", output_path)

    copy2(artifact_locations.repo_root / "examples" / "pyproject.toml", output_path)
    copy2(artifact_locations.repo_root / "examples" / "poetry.lock", output_path)

    copy2(artifact_locations.repo_root / "component.yml", output_path)


if __name__ == "__main__":
    parser = ArgumentParser(description="Stage client files for NI driver API gRPC services.")
    parser.add_argument(
        "--output",
        "-o",
        help="The path to the top-level directory to stage the client files. Must be empty or non-existent.",
    )

    parser.add_argument(
        "--ignore-release-readiness", action="store_true", help="Force-include all artifacts."
    )

    args = parser.parse_args()

    if args.output:
        stage_client_files(Path(args.output), args.ignore_release_readiness)
    else:
        print(
            """
***No --output directory specified.***
Performing Dry Run.
        """
        )
        with TemporaryDirectory() as tempdir:
            tempdirpath = Path(tempdir)
            stage_client_files(tempdirpath, args.ignore_release_readiness)
            created_files = (f for f in tempdirpath.glob("**/*") if not f.is_dir())
            for out_file in created_files:
                print(out_file.relative_to(tempdirpath))
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/template_helpers.py sha256=21d10dc43129ce5b13c390ae795a5c7a61ba591dc6970516319c2ecb569a79c5 bytes=1646 -->
## FILE: source/codegen/template_helpers.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/template_helpers.py`
- sha256: `21d10dc43129ce5b13c390ae795a5c7a61ba591dc6970516319c2ecb569a79c5`
- bytes: 1646

````python
"""Helpers for mako templates."""

from importlib import import_module
from pathlib import Path
from typing import Union

from mako.lookup import TemplateLookup  # type: ignore
from mako.template import Template  # type: ignore


def instantiate_mako_template(template_file_name: str) -> Template:
    """Instantiate the mako template in the given file."""
    current_dir = Path(__file__).parent
    template_directory = current_dir / "templates"
    template_file_path = template_directory / template_file_name
    template_lookup = TemplateLookup(directories=str(template_directory))
    return Template(filename=str(template_file_path), lookup=template_lookup)


def write_if_changed(output_file_path: Union[Path, str], new_contents: str) -> None:
    """Write new_contents to output_file_path if new_contents != the contents of output_file_path.

    This prevents downstream recompiles when codegen runs but does not change a given file.
    """
    old_contents = _read_file_contents(output_file_path)
    if old_contents != new_contents:
        with open(output_file_path, "w+", newline="") as f:
            f.write(new_contents)


def load_metadata(metadata_dir: Union[Path, str]) -> dict:
    """Load the metadata from the given directory."""
    metadata_path = Path(metadata_dir)
    module = import_module("metadata." + metadata_path.name)

    return module.metadata


def _read_file_contents(output_file_path: Union[Path, str]) -> str:
    try:
        with Path(output_file_path).open("r", newline="") as f:
            return f.read()
    except FileNotFoundError:
        return ""
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/templates/client.cpp.mako sha256=090152bafeba2b6c1a3a2fa60d2896de775143091d1beffd59cf14a4be183543 bytes=2555 -->
## FILE: source/codegen/templates/client.cpp.mako

- repository: `ni/grpc-device`
- source_path: `source/codegen/templates/client.cpp.mako`
- sha256: `090152bafeba2b6c1a3a2fa60d2896de775143091d1beffd59cf14a4be183543`
- bytes: 2555

````mako
<%
import common_helpers
import client_helpers
import service_helpers
from client_helpers import ParamMechanism

config = data['config']
functions = data['functions']
enums = data['enums']
functions = client_helpers.filter_functions_to_include_in_client(functions)

module_name = config["module_name"]
service_class_prefix = config["service_class_prefix"]
core_namespace = config["namespace_component"] + "_grpc"
namespace = f"{core_namespace}::experimental::client"

stub_ptr_alias = client_helpers.stub_ptr_alias()

%>\
<%namespace name="mako_helper" file="/client_helpers.mako"/>\

//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// EXPERIMENTAL Client convenience wrapper for ${config["driver_name"]}.
//---------------------------------------------------------------------
#include "${module_name}_client.h"

#include <grpcpp/grpcpp.h>

#include <${config["module_name"]}.grpc.pb.h>

#include <cstdint>
#include <memory>
#include <stdexcept>
#include <vector>

namespace ${namespace} {

% for function in common_helpers.filter_proto_rpc_functions(functions):
<%
  f = functions[function]
  stub_method_name = common_helpers.snake_to_pascal(function)
  client_method_name = common_helpers.pascal_to_snake(stub_method_name)
  request_type = service_helpers.get_request_type(stub_method_name)
  response_type = service_helpers.get_response_type(stub_method_name)
  stub_param = f"const {stub_ptr_alias}& stub"
  is_streaming = common_helpers.has_streaming_response(f)
  client_params = client_helpers.get_client_parameters(f, enums)
%>\
%   if is_streaming:
${client_helpers.streaming_response_type(response_type)}
${client_method_name}(${client_helpers.create_streaming_params(client_params, for_header = False)})
{
  auto request = ${request_type}{};
${mako_helper.build_request(client_params)}\

  return stub->${stub_method_name}(&context, request);
}
%   else:
${response_type}
${client_method_name}(${client_helpers.create_unary_params(client_params, for_header = False)})
{
  ::grpc::ClientContext context;

  auto request = ${request_type}{};
${mako_helper.build_request(client_params)}\

  auto response = ${response_type}{};

  raise_if_error(
      stub->${stub_method_name}(&context, request, &response),
      context);

  return response;
}
%   endif

% endfor

} // namespace ${namespace}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/templates/client.h.mako sha256=c8dbd2c9fe7ebb6479712d06d07210dbbf265b1bad649c4447bf53f9687b28d3 bytes=2387 -->
## FILE: source/codegen/templates/client.h.mako

- repository: `ni/grpc-device`
- source_path: `source/codegen/templates/client.h.mako`
- sha256: `c8dbd2c9fe7ebb6479712d06d07210dbbf265b1bad649c4447bf53f9687b28d3`
- bytes: 2387

````mako
<%
import common_helpers
import client_helpers
import service_helpers
from client_helpers import ParamMechanism

config = data['config']
functions = data['functions']
enums = data["enums"]
functions = client_helpers.filter_functions_to_include_in_client(functions)

service_class_prefix = config["service_class_prefix"]
include_guard_name = service_helpers.get_include_guard_name(config, "_CLIENT_H")
core_namespace = config["namespace_component"] + "_grpc"
namespace = f"{core_namespace}::experimental::client"

stub_ptr_alias = client_helpers.stub_ptr_alias()
pb_alias = client_helpers.protobuf_namespace_alias()
%>\
<%namespace name="mako_helper" file="/client_helpers.mako"/>\

//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// EXPERIMENTAL Client convenience wrapper for ${config["driver_name"]}.
//---------------------------------------------------------------------
#ifndef ${include_guard_name}
#define ${include_guard_name}

#include <grpcpp/grpcpp.h>

#include <${config["module_name"]}.grpc.pb.h>
#include <tests/utilities/client_helpers.h>

#include <memory>
#include <vector>

namespace ${namespace} {

namespace ${pb_alias} = ::google::protobuf;
using ${stub_ptr_alias} = std::unique_ptr<${service_class_prefix}::Stub>;
using namespace nidevice_grpc::experimental::client;


% for function in common_helpers.filter_proto_rpc_functions(functions):
<%
  f = functions[function]
  stub_method_name = common_helpers.snake_to_pascal(function)
  client_method_name = common_helpers.pascal_to_snake(stub_method_name)
  response_type = service_helpers.get_response_type(stub_method_name)
  stub_param = f"const {stub_ptr_alias}& stub"
  is_streaming = common_helpers.has_streaming_response(f)
  client_params = client_helpers.get_client_parameters(f, enums)
%>\
%   if is_streaming:
${client_helpers.streaming_response_type(response_type)} ${client_method_name}(${client_helpers.create_streaming_params(client_params, for_header = True)});
%   else:
${response_type} ${client_method_name}(${client_helpers.create_unary_params(client_params, for_header = True)});
%   endif
% endfor

} // namespace ${namespace}

#endif /* ${include_guard_name} */
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/templates/client_helpers.mako sha256=4978193b6ea72c5c847d87ff789e6bdb6e451955d7d15afd84a282ab5748a84b bytes=1590 -->
## FILE: source/codegen/templates/client_helpers.mako

- repository: `ni/grpc-device`
- source_path: `source/codegen/templates/client_helpers.mako`
- sha256: `4978193b6ea72c5c847d87ff789e6bdb6e451955d7d15afd84a282ab5748a84b`
- bytes: 1590

````mako
<%!
import common_helpers
import client_helpers
import service_helpers
from client_helpers import ParamMechanism
%>

## Copy data from the client method params to the request.
<%def name="build_request(client_params)">\
%   for param in client_params:
<%
  field_name = common_helpers.get_grpc_field_name_from_str(param.cppName)
  grpc_field_name = common_helpers.get_grpc_field_name_from_str(param.name)
%>\
%     if param.mechanism == ParamMechanism.ARRAY:
  copy_array(${field_name}, request.mutable_${field_name}());
%     elif param.mechanism in [ParamMechanism.ENUM, ParamMechanism.MAPPED_ENUM]:
<%
  enum_type = client_helpers.get_enum_value_type(param)
  raw_type = client_helpers.get_enum_raw_type(param)
  is_mapped = param.mechanism == ParamMechanism.MAPPED_ENUM
  maybe_mapped_suffix = "_mapped" if is_mapped else ""
%>\
  const auto ${field_name}_ptr = ${field_name}.get_if<${enum_type}>();
  const auto ${field_name}_raw_ptr = ${field_name}.get_if<${raw_type}>();
  if (${field_name}_ptr) {
    request.set_${grpc_field_name}${maybe_mapped_suffix}(*${field_name}_ptr);
  }
  else if (${field_name}_raw_ptr) {
    request.set_${grpc_field_name}_raw(*${field_name}_raw_ptr);
  }
%     elif param.mechanism == ParamMechanism.COPY:
  request.mutable_${grpc_field_name}()->CopyFrom(${field_name});
%     elif param.mechanism == ParamMechanism.BITFIELD_AS_ENUM_ARRAY:
  request.set_${grpc_field_name}_raw(copy_bitfield_as_enum_array(${field_name}));
%     else:
  request.set_${grpc_field_name}(${field_name});
%     endif
%   endfor
</%def>
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/templates/compilation_test.cpp.mako sha256=2f2cebde25097947158b0dda553f1d9aa6f34c660cc273463a7bb72e8ef73147 bytes=1413 -->
## FILE: source/codegen/templates/compilation_test.cpp.mako

- repository: `ni/grpc-device`
- source_path: `source/codegen/templates/compilation_test.cpp.mako`
- sha256: `2f2cebde25097947158b0dda553f1d9aa6f34c660cc273463a7bb72e8ef73147`
- bytes: 1413

````mako
<%
import service_helpers

config = data['config']
functions = data['functions']

module_name = config["module_name"]
c_function_prefix = config["c_function_prefix"]
%>\
//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Compilation test for the ${config["driver_name"]} Metadata
//---------------------------------------------------------------------
#include "${module_name}_library.h"

namespace ${config["namespace_component"]}_grpc {

% for method_name in service_helpers.filter_api_functions(functions, only_mockable_functions=False):
<%
  f = functions[method_name]
  parameters = f['parameters']
  return_type = f['returns']
  parameter_list = service_helpers.create_params(parameters, expand_varargs=True)
  argument_list = ', '.join(p['cppName'] for p in service_helpers.expand_varargs_parameters(parameters) if not p.get("proto_only", False))
  c_name = service_helpers.get_cname(functions, method_name, c_function_prefix)
%>\
% if not service_helpers.is_private_method(f) and not service_helpers.is_restricted_driver_service(config):
${return_type} ${method_name}(${parameter_list})
{
  return ${c_name}(${argument_list});
}

% endif
% endfor
}  // namespace ${config["namespace_component"]}_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/templates/library.cpp.mako sha256=7264cd67531b5c3f875961016285abbca164d5167597e2237428c394a90c78e8 bytes=4218 -->
## FILE: source/codegen/templates/library.cpp.mako

- repository: `ni/grpc-device`
- source_path: `source/codegen/templates/library.cpp.mako`
- sha256: `7264cd67531b5c3f875961016285abbca164d5167597e2237428c394a90c78e8`
- bytes: 4218

````mako
<%
import common_helpers
import service_helpers

config = data['config']
functions = data['functions']

service_class_prefix = config["service_class_prefix"]
module_name = config["module_name"]
c_function_prefix = config["c_function_prefix"]
c_dll_function_prefix = config.get("c_dll_function_prefix", c_function_prefix)
linux_library_info = config['library_info']['Linux']['64bit']
linux_library_name = linux_library_info['name']
linux_abi_version = linux_library_info.get('abi_version', None)
linux_so_version_suffix = f'.{linux_abi_version}' if linux_abi_version else ''
windows_library_info = config['library_info']['Windows']['64bit']
windows_library_name = windows_library_info['name']

class_name = f"{service_class_prefix}Library"

initialization_list = "shared_library_(shared_library)"
set_runtime_environment_supported = 'SetRuntimeEnvironment' in service_helpers.filter_api_functions(functions, only_mockable_functions=False)
if set_runtime_environment_supported:
  initialization_list += ", runtime_environment_set_(false)"
%>\
//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Service implementation for the ${config["driver_name"]} Metadata
//---------------------------------------------------------------------
#include "${module_name}_library.h"
#include <server/shared_library.h>
% if set_runtime_environment_supported:
#include "version.h"
% endif

#include <memory>

#if defined(_MSC_VER)
static const char* kLibraryName = "${windows_library_name}";
#else
static const char* kLibraryName = "lib${linux_library_name}.so${linux_so_version_suffix}";
#endif

namespace ${config["namespace_component"]}_grpc {

${class_name}::${class_name}() : ${class_name}(std::make_shared<nidevice_grpc::SharedLibrary>()) {}

${class_name}::${class_name}(std::shared_ptr<nidevice_grpc::SharedLibraryInterface> shared_library) : ${initialization_list}
{
  shared_library_->set_library_name(kLibraryName);
  shared_library_->load();
  bool loaded = shared_library_->is_loaded();
  memset(&function_pointers_, 0, sizeof(function_pointers_));
  if (!loaded) {
    return;
  }
% for method_name in service_helpers.filter_api_functions(functions, only_mockable_functions=False):
<%
  c_name = service_helpers.get_cname(functions, method_name, c_dll_function_prefix)
%>\
  function_pointers_.${method_name} = reinterpret_cast<${method_name}Ptr>(shared_library_->get_function_pointer("${c_name}"));
% endfor
% if set_runtime_environment_supported:

  if (function_pointers_.SetRuntimeEnvironment) {
    this->SetRuntimeEnvironment(nidevice_grpc::kNiDeviceGrpcOriginalFileName, nidevice_grpc::kNiDeviceGrpcFileVersion, "", "");
    this->runtime_environment_set_ = true;
  }
% endif
}

${class_name}::~${class_name}()
{
}

::grpc::Status ${class_name}::check_function_exists(std::string functionName)
{
  return shared_library_->function_exists(functionName.c_str())
    ? ::grpc::Status::OK
    : ::grpc::Status(::grpc::NOT_FOUND, "Could not find the function " + functionName);
}

% for method_name in service_helpers.filter_api_functions(functions, only_mockable_functions=False):
<%
  f = functions[method_name]
  parameters = f['parameters']
  return_type = f['returns']
  parameter_list = service_helpers.create_params(parameters, expand_varargs=True)
  argument_list = ', '.join(p['cppName'] for p in service_helpers.expand_varargs_parameters(parameters) if not p.get("proto_only", False))
  c_name = service_helpers.get_cname(functions, method_name, c_dll_function_prefix)
%>\
${return_type} ${class_name}::${method_name}(${parameter_list})
{
  if (!function_pointers_.${method_name}) {
    throw nidevice_grpc::LibraryLoadException("Could not find ${c_name}.");
  }
  return function_pointers_.${method_name}(${argument_list});
}

% endfor
% if set_runtime_environment_supported:
bool ${class_name}::is_runtime_environment_set() const { return this->runtime_environment_set_; }

% endif
}  // namespace ${config["namespace_component"]}_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/templates/library.h.mako sha256=6b137aaed6e38716990ca83edc2f968b21449ab93909468c49c30c384342e384 bytes=3351 -->
## FILE: source/codegen/templates/library.h.mako

- repository: `ni/grpc-device`
- source_path: `source/codegen/templates/library.h.mako`
- sha256: `6b137aaed6e38716990ca83edc2f968b21449ab93909468c49c30c384342e384`
- bytes: 3351

````mako
<%
import service_helpers

config = data['config']
functions = data['functions']

service_class_prefix = config["service_class_prefix"]
namespace_prefix = config["namespace_component"] + "_grpc"
include_guard_name = service_helpers.get_include_guard_name(config, "_LIBRARY_H")
c_function_prefix = config["c_function_prefix"]

class_name = f"{service_class_prefix}Library"
inherited_functions = service_helpers.filter_api_functions(functions)

set_runtime_environment_supported = 'SetRuntimeEnvironment' in service_helpers.filter_api_functions(functions, only_mockable_functions=False)
%>\
//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Real implementation of LibraryInterface for ${config["driver_name"]}
//---------------------------------------------------------------------
#ifndef ${include_guard_name}
#define ${include_guard_name}

#include "${config["module_name"]}_library_interface.h"

#include <server/shared_library_interface.h>

#include <memory>

namespace ${config["namespace_component"]}_grpc {

class ${class_name} : public ${namespace_prefix}::${class_name}Interface {
 public:
  ${class_name}();
  explicit ${class_name}(std::shared_ptr<nidevice_grpc::SharedLibraryInterface> shared_library);
  virtual ~${class_name}();

  ::grpc::Status check_function_exists(std::string functionName);
% for method_name in service_helpers.filter_api_functions(functions, only_mockable_functions=False):
<%
  f = functions[method_name]
  parameters = f['parameters']
  return_type = f['returns']
  override_specifier = " override" if method_name in inherited_functions else ""
%>\
  ${return_type} ${method_name}(${service_helpers.create_params(parameters, expand_varargs=True)})${override_specifier};
% endfor
% if set_runtime_environment_supported:
  bool is_runtime_environment_set() const; // needed to test that we properly call SetRuntimeEnvironment
% endif

 private:
% for method_name in service_helpers.filter_api_functions(functions, only_mockable_functions=False):
<%
  f = functions[method_name]
  parameters = f['parameters']
  return_type = f['returns']
  c_name = service_helpers.get_cname(functions, method_name, c_function_prefix)
%>\
## "Private" methods aren't in the public header, so generate the params from the metadata.
% if service_helpers.is_private_method(f) or service_helpers.is_restricted_driver_service(config):
  using ${method_name}Ptr = ${return_type} (*)(${service_helpers.create_params(parameters, expand_varargs=False)});
% else:
  using ${method_name}Ptr = decltype(&${c_name});
% endif
% endfor

  typedef struct FunctionPointers {
% for method_name in service_helpers.filter_api_functions(functions, only_mockable_functions=False):
    ${method_name}Ptr ${method_name};
% endfor
  } FunctionLoadStatus;

  std::shared_ptr<nidevice_grpc::SharedLibraryInterface> shared_library_;
  FunctionPointers function_pointers_;
% if set_runtime_environment_supported:
  bool runtime_environment_set_; // needed to test that we properly call SetRuntimeEnvironment
% endif
};

}  // namespace ${config["namespace_component"]}_grpc

#endif  // ${include_guard_name}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/templates/library_interface.h.mako sha256=cc48a332f5cba74e44bd4f9f71e5cfcfda71e56c0d5681579d5f7e0f88f8f6d2 bytes=1464 -->
## FILE: source/codegen/templates/library_interface.h.mako

- repository: `ni/grpc-device`
- source_path: `source/codegen/templates/library_interface.h.mako`
- sha256: `cc48a332f5cba74e44bd4f9f71e5cfcfda71e56c0d5681579d5f7e0f88f8f6d2`
- bytes: 1464

````mako
<%
import common_helpers
import service_helpers

config = data['config']
functions = data['functions']

service_class_prefix = config["service_class_prefix"]
include_guard_name = service_helpers.get_include_guard_name(config, "_LIBRARY_WRAPPER_H")
%>\
//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Library wrapper for implementing interactions with ${config["driver_name"]}
//---------------------------------------------------------------------
#ifndef ${include_guard_name}
#define ${include_guard_name}

#include <grpcpp/grpcpp.h>
#include <${config["c_header"]}>
% for additional_header in common_helpers.get_additional_headers(config, "library_interface.h"):
#include "${additional_header}"
% endfor

namespace ${config["namespace_component"]}_grpc {

class ${service_class_prefix}LibraryInterface {
 public:
  virtual ~${service_class_prefix}LibraryInterface() {}

% for method_name in service_helpers.filter_api_functions(functions):
<%
  f = functions[method_name]
  parameters = f['parameters']
  return_type = f['returns']
%>\
  virtual ${return_type} ${method_name}(${service_helpers.create_params(parameters, expand_varargs=True)}) = 0;
% endfor
};

}  // namespace ${config["namespace_component"]}_grpc
#endif  // ${include_guard_name}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/templates/mock_library.h.mako sha256=ed41bc5d6d26813a1fcf1c2cd3c7987a9c59379903e081744a6fd26b4448f3cc bytes=1717 -->
## FILE: source/codegen/templates/mock_library.h.mako

- repository: `ni/grpc-device`
- source_path: `source/codegen/templates/mock_library.h.mako`
- sha256: `ed41bc5d6d26813a1fcf1c2cd3c7987a9c59379903e081744a6fd26b4448f3cc`
- bytes: 1717

````mako
<%
import service_helpers

config = data['config']
functions = data['functions']

service_class_prefix = config["service_class_prefix"]
namespace_prefix = config["namespace_component"] + "_grpc"
include_guard_name = service_helpers.get_include_guard_name(config, "_MOCK_LIBRARY_H")
%>\
//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Mock of LibraryInterface for ${config["driver_name"]}
//---------------------------------------------------------------------
## Define section
#ifndef ${include_guard_name}
#define ${include_guard_name}

## Include section
#include <gmock/gmock.h>
#include <gtest/gtest.h>

#include "${config["module_name"]}_library_interface.h"

namespace ni {
namespace tests {
namespace unit {

class ${service_class_prefix}MockLibrary : public ${namespace_prefix}::${service_class_prefix}LibraryInterface {
 public:
% for method_name in service_helpers.filter_api_functions(functions):
<%
  f = functions[method_name]
  parameters = f['parameters']
  return_type = f['returns']
%>\
% if len(parameters) <= 15: # MOCK_METHOD shows compilation error (undefined GMOCK_PP_INTERNAL_FOR_EACH_IMPL_<type>) for params > 15
  MOCK_METHOD(${return_type}, ${method_name}, (${service_helpers.create_params(parameters)}), (override));
% else:
  ${return_type} ${method_name}(${service_helpers.create_params(parameters)}) { throw std::runtime_error("Not implemented."); }
% endif
% endfor
};

}  // namespace unit
}  // namespace tests
}  // namespace ni
#endif  // ${include_guard_name}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/templates/proto.mako sha256=eb060d574a2c4dd3831f248d5a2db4ca7fc5d2e833c3b7ee8de0f898c84c405e bytes=2855 -->
## FILE: source/codegen/templates/proto.mako

- repository: `ni/grpc-device`
- source_path: `source/codegen/templates/proto.mako`
- sha256: `eb060d574a2c4dd3831f248d5a2db4ca7fc5d2e833c3b7ee8de0f898c84c405e`
- bytes: 2855

````mako
<%
import common_helpers
import proto_helpers

config = data["config"]
enums = data["enums"]
functions = data["functions"]

service_class_prefix = config["service_class_prefix"]
function_enums = common_helpers.get_function_enums(functions, enums)
external_proto_deps = common_helpers.list_external_proto_dependencies(functions)
additional_protos = config.get("additional_protos", [])
additional_protos.extend(external_proto_deps)
%>\
<%namespace name="mako_helper" file="/proto_helpers.mako"/>\

//---------------------------------------------------------------------
// This file is generated from ${config["driver_name"]} API metadata version ${config["api_version"]}
//---------------------------------------------------------------------
// Proto file for the ${config["driver_name"]} Metadata
//---------------------------------------------------------------------
syntax = "proto3";

% if config.get("has_moniker_streaming_apis", False):
option cc_enable_arenas = true;
% endif
option java_multiple_files = true;
option java_package = "${config["java_package"]}";
option java_outer_classname = "${service_class_prefix}";
option csharp_namespace = "${config["csharp_namespace"]}";

package ${config["namespace_component"]}_grpc;

% if common_helpers.uses_nidevice_common_message_types(config, functions):
import "nidevice.proto";
% endif
import "session.proto";
% for proto in additional_protos:
import "${proto}";
% endfor

service ${service_class_prefix} {
% for function in common_helpers.filter_proto_rpc_functions(functions):
<%
  method_name = common_helpers.snake_to_pascal(function)
  streaming_qualifier = proto_helpers.get_streaming_response_qualifier(functions[function])
%>\
  rpc ${method_name}(${method_name}Request) returns (${streaming_qualifier}${method_name}Response);
% endfor
}

% for group in common_helpers.get_attribute_groups(data):
%   for define_attribute_enum, attributes in group.get_attributes_split_by_sub_group().items():
${mako_helper.define_attribute_enum(group.name, define_attribute_enum, attributes, config)}\
%   endfor
% endfor
${mako_helper.define_function_enums(function_enums)}\
${mako_helper.insert_custom_template_if_found()}\
% for custom_type in common_helpers.get_custom_types(config):
${mako_helper.define_custom_type(custom_type)}\

% endfor
% for function in common_helpers.filter_proto_rpc_functions_for_message(functions):
<%
  input_parameters, output_parameters = proto_helpers.get_parameters(functions[function])
%>\
${mako_helper.define_request_message(function, input_parameters)}\

${mako_helper.define_response_message(function, output_parameters)}\

% if common_helpers.is_moniker_streaming_function(functions[function]):
${mako_helper.define_moniker_request_response_messages(function, functions)}\

% endif
% endfor
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/templates/proto_helpers.mako sha256=1179511f2ddb06f79034f484d2da7d6d4e363eb8c8774a41bd5464fff5dbbc22 bytes=6027 -->
## FILE: source/codegen/templates/proto_helpers.mako

- repository: `ni/grpc-device`
- source_path: `source/codegen/templates/proto_helpers.mako`
- sha256: `1179511f2ddb06f79034f484d2da7d6d4e363eb8c8774a41bd5464fff5dbbc22`
- bytes: 6027

````mako
<%!
  from mako.exceptions import TopLevelLookupException

  import common_helpers
  import proto_helpers
%>

## Define a proto enum capturing attributes from the metadata.
<%def name="define_attribute_enum(group_name, sub_group, attributes, config)">\
<%
  attribute_value_prefix = group_name.upper() + "_ATTRIBUTE"

  # When attributes are split-by-datatype, the actual attributes don't need a type-name disambiguator because
  # the original unsplit list didn't have duplicates. 
  # But there are 2 cases that need to be disambiguated:
  # * Each attribute has an UNSPECIFIED placeholder.
  # * Reset attributes overlap the data-type-specific attributes.
  attribute_disambiguator = "_" + common_helpers.pascal_to_snake(sub_group).upper() if sub_group else ""
  disambiguated_attribute_value_prefix = group_name.upper() + attribute_disambiguator + "_ATTRIBUTE"
  unspecified_attribute_value_prefix = disambiguated_attribute_value_prefix
  attribute_value_prefix = disambiguated_attribute_value_prefix if sub_group == "Reset" else attribute_value_prefix
%>\
% if attributes:
<%
  # Check if any attribute has value 0
  has_zero_value = any(int(attr_id) == 0 for attr_id in attributes.keys())
%>\
enum ${common_helpers.get_attribute_enum_name(group_name, sub_group, config)} {
% if not has_zero_value:
  ${unspecified_attribute_value_prefix}_UNSPECIFIED = 0;
% endif
%   for attribute in attributes:
<%
   attribute_name = attributes[attribute]["name"]
%>\
  ${attribute_value_prefix}_${attribute_name} = ${attribute};
%   endfor
}

% endif
</%def>

## Define enums in the proto for each metadata enum referenced in a proto message.
<%def name="define_function_enums(function_enums)">\
<%
  enums = data["enums"]
  enum_definitions = proto_helpers.get_enum_definitions(function_enums, enums)
%>\
% for enum_name in enum_definitions:
enum ${enum_name} {
%   if enum_definitions[enum_name]["allow_alias"]:
  option allow_alias = true;
%   endif
%   for value in enum_definitions[enum_name]["values"]:
  ${value["name"]} = ${value["value"]};
%   endfor
}

% endfor
</%def>

## If there is a custom proto mako template in the metadata, insert it.
<%def name="insert_custom_template_if_found()">\
<%
  config = data["config"]
  lookup = data["lookup"]
  custom_template = None
  try:
    custom_template = lookup.get_template("custom_proto.mako").render()
  except TopLevelLookupException:
    pass # no template
%>\
% if custom_template:
${custom_template}
% endif
</%def>

## Define a proto request message for a given API function.
<%def name="define_request_message(function, input_parameters)">\
<%
  config = data["config"]
  service_class_prefix = config["service_class_prefix"]
  request_parameters = proto_helpers.get_message_parameter_definitions(input_parameters)
%>\
message ${common_helpers.snake_to_pascal(function)}Request {
% for parameter in request_parameters:
%   if parameter.get("use_oneof", False):
  oneof ${parameter["name"]} {
%     for oneof_parameter in parameter["parameters"]:
    ${oneof_parameter["type"]} ${oneof_parameter["name"]} = ${oneof_parameter["grpc_field_number"]};
%     endfor
  }
%   elif common_helpers.is_optional_param(parameter):
  optional ${parameter["type"]} ${parameter["name"]} = ${parameter["grpc_field_number"]};
%   else:
  ${parameter["type"]} ${parameter["name"]} = ${parameter["grpc_field_number"]};
%   endif
% endfor
}
</%def>

## Define a proto response message for a given API function.
<%def name="define_response_message(function, output_parameters)">\
<%
  config = data["config"]
  service_class_prefix = config["service_class_prefix"]
  response_parameters = proto_helpers.get_message_parameter_definitions(output_parameters)
%>\
message ${common_helpers.snake_to_pascal(function)}Response {
% for parameter in response_parameters:
% if parameter.get("is_get_last_error_output", False):
  ${parameter["type"]} ${parameter["name"]} = ${parameter["grpc_field_number"]} [deprecated = true];
% elif common_helpers.is_optional_param(parameter):
  optional ${parameter["type"]} ${parameter["name"]} = ${parameter["grpc_field_number"]};
% else:
  ${parameter["type"]} ${parameter["name"]} = ${parameter["grpc_field_number"]};
% endif
% endfor
}
</%def>

## Define a proto request and response messages for Moniker function.
<%def name="define_moniker_request_response_messages(begin_function_name, functions)">\
<%
  non_streaming_function_name = begin_function_name.replace("Begin", "")
  input_parameters, output_parameters = common_helpers.get_data_moniker_function_parameters(functions[non_streaming_function_name])
  request_parameters = proto_helpers.get_message_parameter_definitions(input_parameters)
  response_parameters = proto_helpers.get_message_parameter_definitions(output_parameters)
  request_message_type = common_helpers.get_data_moniker_request_message_type(begin_function_name)
  response_message_type = common_helpers.get_data_moniker_response_message_type(begin_function_name)
%>\
% if request_parameters:
message ${request_message_type} {
% for parameter in request_parameters:
  ${parameter["type"]} ${parameter["name"]} = ${parameter["grpc_field_number"]};
% endfor
}

% endif
message ${response_message_type} {
% for parameter in response_parameters:
  ${parameter["type"]} ${parameter["name"]} = ${parameter["grpc_field_number"]};
% endfor
}
</%def>

## Define a proto message for a given custom type.
<%def name="define_custom_type(custom_type)">\
<%
  config = data["config"]
  used_indexes = []
%>\
message ${custom_type["grpc_name"]} {
% for field in common_helpers.filter_parameters_for_grpc_fields(custom_type["fields"]):
<%
  field_type = field["grpc_type"]
  field_name = common_helpers.get_grpc_field_name(field)
  field_number = proto_helpers.generate_parameter_field_number(field, used_indexes)
%>\
  ${field_type} ${field_name} = ${field_number};
% endfor
}
</%def>
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/templates/register_all_services.cpp.mako sha256=c2882b3e9f6a6a4a6802d9ba6266dc86978e515855fd61414d57db4a81ffa452 bytes=2407 -->
## FILE: source/codegen/templates/register_all_services.cpp.mako

- repository: `ni/grpc-device`
- source_path: `source/codegen/templates/register_all_services.cpp.mako`
- sha256: `c2882b3e9f6a6a4a6802d9ba6266dc86978e515855fd61414d57db4a81ffa452`
- bytes: 2407

````mako
<%
import common_helpers
import service_helpers

driver_configs = [data["config"] for data in drivers]
repository_type_to_config = service_helpers.list_session_repository_handle_types(driver_configs)
%>\
//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Register all services implementation.
//---------------------------------------------------------------------
#include "register_all_services.h"

#include <string>
#include <vector>

#include <server/core_services_registrar.h>
#include <server/session_repository.h>

% for config in driver_configs:
<%
  module_name = config["module_name"]
%>\
<%block filter="common_helpers.os_conditional_compile_block(config)">\
#include "${module_name}/${module_name}_service_registrar.h"
</%block>\
% endfor

namespace nidevice_grpc {

std::shared_ptr<std::vector<std::shared_ptr<void>>> register_all_services(
  grpc::ServerBuilder& server_builder,
  const nidevice_grpc::FeatureToggles& feature_toggles)
{
  auto service_vector = std::make_shared<std::vector<std::shared_ptr<void>>>();

  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  service_vector->push_back(session_repository);
  nidevice_grpc::register_core_services(service_vector, server_builder, session_repository, feature_toggles);

% for type_name, config in repository_type_to_config.items():
<%block filter="common_helpers.os_conditional_compile_block(config)">\
  auto ${config["local_name"]} = std::make_shared<nidevice_grpc::SessionResourceRepository<${type_name}>>(session_repository);
</%block>\
% endfor

% for driver in drivers:
<%
  config = driver["config"]
  namespace = f"{config['namespace_component']}_grpc"
  resource_handle_deps = service_helpers.get_driver_shared_resource_repository_ptr_deps(config, driver["functions"])
%>\
<%block filter="common_helpers.os_conditional_compile_block(config)">\
  service_vector->push_back(
    ${namespace}::register_service(
      server_builder, 
% for resource_handle_type in resource_handle_deps:
      ${repository_type_to_config[resource_handle_type]["local_name"]},
% endfor
      feature_toggles));
</%block>\
% endfor

  return service_vector;
}

} // nidevice_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/templates/register_all_services.h.mako sha256=bba2c94763b59a9d9c1c8004c7dd6e80b4b1f212d04181473618c2d427726ad6 bytes=871 -->
## FILE: source/codegen/templates/register_all_services.h.mako

- repository: `ni/grpc-device`
- source_path: `source/codegen/templates/register_all_services.h.mako`
- sha256: `bba2c94763b59a9d9c1c8004c7dd6e80b4b1f212d04181473618c2d427726ad6`
- bytes: 871

````mako
<%
include_guard_name = "NIDEVICE_GRPC_REGISTER_ALL_SERVICES_H"
namespace = "nidevice_grpc"
%>\
//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Register all services header.
//---------------------------------------------------------------------
#ifndef ${include_guard_name}
#define ${include_guard_name}
#include <server/feature_toggles.h>

#include <memory>
#include <vector>

namespace grpc {
class ServerBuilder;
}

namespace ${namespace} {

std::shared_ptr<std::vector<std::shared_ptr<void>>> register_all_services(
  grpc::ServerBuilder& server_builder,
  const nidevice_grpc::FeatureToggles& feature_toggles);

} // ${namespace}

#endif  // ${include_guard_name}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/templates/service.cpp.mako sha256=7925b9750e6f402aac7ff7dd2a18e2feaf0fbfbc0f02e55ca94318bc6dcf608c bytes=11425 -->
## FILE: source/codegen/templates/service.cpp.mako

- repository: `ni/grpc-device`
- source_path: `source/codegen/templates/service.cpp.mako`
- sha256: `7925b9750e6f402aac7ff7dd2a18e2feaf0fbfbc0f02e55ca94318bc6dcf608c`
- bytes: 11425

````mako
<%
import common_helpers
import service_helpers

config = data['config']
functions = data['functions']

service_class_prefix = config["service_class_prefix"]
namespace_prefix = config["namespace_component"] + "_grpc::"
module_name = config["module_name"]
custom_types = common_helpers.get_custom_types(config)
(input_custom_types, output_custom_types) = common_helpers.get_input_and_output_custom_types(config, functions)
has_async_functions = any(service_helpers.get_async_functions(functions))
has_two_dimension_functions = any(service_helpers.get_functions_with_two_dimension_param(functions))
functions_to_generate = service_helpers.filter_proto_rpc_functions_to_generate(functions)
streaming_functions_to_generate = common_helpers.filter_moniker_streaming_functions(functions, functions_to_generate)
# If there are any non-mockable functions, we need to call the library directly, which
# means we need another include file
any_non_mockable_functions = any(not common_helpers.can_mock_function(functions[name]['parameters']) for name in functions_to_generate)
# Define the constant for buffer too small if we have any of these functions.
any_ivi_dance_functions = any(
  common_helpers.has_ivi_dance_with_a_twist_param(functions[name]['parameters']) or
  common_helpers.has_ivi_dance_param(functions[name]['parameters']) for name in functions_to_generate)

resource_repository_deps = service_helpers.get_driver_shared_resource_repository_ptr_deps(config, functions)
%>\
<%namespace name="mako_helper" file="/service_helpers.mako"/>\

//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Service implementation for the ${config["driver_name"]} Metadata
//---------------------------------------------------------------------
#include "${module_name}_service.h"

#include <sstream>
#include <fstream>
#include <iostream>
#include <atomic>
#include <vector>
% if has_two_dimension_functions:
#include <numeric>
% endif
% for additional_header in common_helpers.get_additional_headers(config, "service.cpp"):
#include "${additional_header}"
% endfor
#include <server/converters.h>
% if has_async_functions:
#include <server/callback_router.h>
#include <server/server_reactor.h>
% endif
% if any_non_mockable_functions:
#include "${module_name}_library.h"
% endif
% if streaming_functions_to_generate:
#include <server/data_moniker_service.h>
% endif

namespace ${config["namespace_component"]}_grpc {

  using nidevice_grpc::converters::allocate_output_storage;
  using nidevice_grpc::converters::calculate_linked_array_size;
  using nidevice_grpc::converters::convert_from_grpc;
  using nidevice_grpc::converters::convert_to_grpc;
  using nidevice_grpc::converters::MatchState;
% for function_name in streaming_functions_to_generate:
<%
function_data = functions[function_name]
parameters = function_data['parameters']
non_streaming_function_name = function_name.replace("Begin", "")
input_parameters, output_parameters = common_helpers.get_data_moniker_function_parameters(functions[non_streaming_function_name])
has_input_parameters = len(input_parameters) != 0
%>
${mako_helper.define_moniker_streaming_struct(begin_function_name=function_name, parameters=parameters, has_input_parameters=has_input_parameters)}\
% endfor

% if any_ivi_dance_functions:
  const auto kErrorReadBufferTooSmall = -200229;
  const auto kWarningCAPIStringTruncatedToFitBuffer = 200026;

% endif
  ${service_class_prefix}Service::${service_class_prefix}Service(
      LibrarySharedPtr library,
% for resource_handle_type in resource_repository_deps:
      ${resource_repository_deps[resource_handle_type].resource_repository_alias} ${resource_repository_deps[resource_handle_type].local_name},
% endfor
      const ${service_class_prefix}FeatureToggles& feature_toggles)
      : library_(library),
% for resource_handle_type in resource_repository_deps:
      ${resource_repository_deps[resource_handle_type].field_name}(${resource_repository_deps[resource_handle_type].local_name}),
% endfor
      feature_toggles_(feature_toggles)
  {
  }

  ${service_class_prefix}Service::~${service_class_prefix}Service()
  {
  }

  // Returns true if it's safe to use outputs of a method with the given status.
  inline bool status_ok(int32 status)
  {
    return ${config['status_ok']};
  }

% if common_helpers.has_enum_array_string_out_param(functions):
  template <typename TEnum>
  void ${service_class_prefix}Service::CopyBytesToEnums(const std::string& input, google::protobuf::RepeatedField<TEnum>* output)
  {
    for (auto item : input)
    {
      output->Add(item);
    }
  }

% endif
% if streaming_functions_to_generate:
  void RegisterMonikerEndpoints()
  {
% for function_name in streaming_functions_to_generate:
  ${mako_helper.register_moniker_functions(function_name)}\
% endfor
  }

% endif
% for function_name in streaming_functions_to_generate:
${mako_helper.define_moniker_function_body(function_name=function_name, functions=functions)}\

% endfor
% for function_name in service_helpers.filter_proto_rpc_functions_to_generate(functions):
<%
    function_data = functions[function_name]
    method_name = common_helpers.snake_to_pascal(function_name)
    parameters = function_data['parameters']
    request_param = service_helpers.get_request_param(method_name)
    response_param = service_helpers.get_response_param(method_name)
    response_type = service_helpers.get_response_type(method_name)
    is_async_streaming = common_helpers.has_async_streaming_response(function_data)
%>\
  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
% if is_async_streaming:
  ::grpc::ServerWriteReactor<${response_type}>*
  ${service_class_prefix}Service::${method_name}(::grpc::CallbackServerContext* context, ${request_param})
  {
${mako_helper.define_async_callback_method_body(function_name=function_name, function_data=function_data, parameters=parameters, config=config)}\
  }
% else:
  ::grpc::Status ${service_class_prefix}Service::${method_name}(::grpc::ServerContext* context, ${request_param}, ${response_param})
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
%   if common_helpers.has_unsupported_parameter(function_data):
      return ::grpc::Status(::grpc::UNIMPLEMENTED, "TODO: This server handler has not been implemented.");
%   elif common_helpers.is_cross_driver_init_method(function_data):
${mako_helper.define_cross_driver_init_method_body(function_name=function_name, function_data=function_data, parameters=parameters)}
%   elif common_helpers.is_init_method(function_data):
${mako_helper.define_init_method_body(function_name=function_name, function_data=function_data, parameters=parameters)}
%   elif common_helpers.has_ivi_dance_param(parameters):
${mako_helper.define_ivi_dance_method_body(function_name=function_name, function_data=function_data, parameters=parameters)}
%   elif common_helpers.has_ivi_dance_with_a_twist_param(parameters):
${mako_helper.define_ivi_dance_with_a_twist_method_body(function_name=function_name, function_data=function_data, parameters=parameters)}
%   elif common_helpers.has_repeated_varargs_parameter(parameters):
${mako_helper.define_repeated_varargs_method_body(function_name=function_name, function_data=function_data, parameters=parameters)}
%   elif common_helpers.is_function_in_streaming_functions(function_name, streaming_functions_to_generate):
${mako_helper.define_streaming_api_body(function_name=function_name, parameters=parameters)}
%   else:
${mako_helper.define_simple_method_body(function_name=function_name, function_data=function_data, parameters=parameters)}
%   endif
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }
% endif

% endfor

<%
  feature_toggles = service_helpers.get_feature_toggles(config)
%>\
  ${service_class_prefix}FeatureToggles::${service_class_prefix}FeatureToggles(
    const nidevice_grpc::FeatureToggles& feature_toggles)
<%block filter="common_helpers.trim_trailing_comma()">\
    : is_enabled(
        feature_toggles.is_feature_enabled("${config["module_name"]}", ${service_helpers.get_driver_service_readiness(config)})),
% for toggle, readiness in feature_toggles.items():
      ${service_helpers.get_toggle_member_name(toggle)}(
        feature_toggles.is_feature_enabled("${toggle}", ${service_helpers.to_cpp_readiness(readiness)})),
% endfor
</%block>\
  {
  }
} // namespace ${config["namespace_component"]}_grpc

% if any(input_custom_types) or any(output_custom_types):
namespace nidevice_grpc {
namespace converters {
%   for custom_type in custom_types:
%     if custom_type["name"] in output_custom_types:
template <>
void convert_to_grpc(const ${custom_type["name"]}& input, ${namespace_prefix}${custom_type["grpc_name"]}* output) 
{
%       for field in common_helpers.filter_parameters_for_grpc_fields(custom_type["fields"]):
%         if common_helpers.supports_standard_copy_conversion_routines(field):
  convert_to_grpc(${str.join(", ", [f'input.{field["name"]}', f'output->mutable_{common_helpers.get_grpc_field_name(field)}()'] + field.get("additional_arguments_to_copy_convert", []))});
%         else:
  output->set_${common_helpers.get_grpc_field_name(field)}(input.${field["name"]});
%         endif
%       endfor
}

%     endif
%     if custom_type["name"] in input_custom_types:
template <>
${custom_type["name"]} convert_from_grpc(const ${namespace_prefix}${custom_type["grpc_name"]}& input) 
{
  auto output = ${custom_type["name"]}();  
%       for field in common_helpers.filter_parameters_for_grpc_fields(custom_type["fields"]):
<%
            input_field_name = common_helpers.get_grpc_field_name(field)
            output_field_name = field["name"]
%>\
%             if field.get("coerced", False):
<%
               c_element_type = field["type"]
%>\
  if (input.${input_field_name}() < std::numeric_limits<${c_element_type}>::min() || input.${input_field_name}() > std::numeric_limits<${c_element_type}>::max()) {
      std::string message("value ");
      message.append(std::to_string(input.${input_field_name}()));
      message.append(" doesn't fit in datatype ");
      message.append("${c_element_type}");
      throw nidevice_grpc::ValueOutOfRangeException(message);
  }
  output.${output_field_name} = static_cast<${c_element_type}>(input.${input_field_name}());
%            elif common_helpers.supports_standard_copy_conversion_routines(field):
<%
  c_type = field['type']
  c_type_underlying_type = common_helpers.get_underlying_type_name(c_type)
  request_snippet = f'input.{input_field_name}()'
%>\
  output.${output_field_name} = convert_from_grpc<${c_type_underlying_type}>(${str.join(", ", [request_snippet] + field.get("additional_arguments_to_copy_convert", []))});
%            else:
  output.${output_field_name} = input.${input_field_name}();
%            endif
%       endfor
  return output;
}

%     endif
%   endfor
} // converters
} // nidevice_grpc

% endif
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/templates/service.h.mako sha256=017144d26f2165c65b45160a5f08d31fe5452d2d3dfed2ef39dc122ba27bccf9 bytes=7245 -->
## FILE: source/codegen/templates/service.h.mako

- repository: `ni/grpc-device`
- source_path: `source/codegen/templates/service.h.mako`
- sha256: `017144d26f2165c65b45160a5f08d31fe5452d2d3dfed2ef39dc122ba27bccf9`
- bytes: 7245

````mako
<%
import common_helpers
import service_helpers

enums = data['enums']
config = data['config']
functions = data['functions']

enums_to_map = service_helpers.get_enums_to_map(functions, enums)
enums_mapped_to_type = service_helpers.generate_mapping_enums_to_type(enums)
type_from_enum = service_helpers.get_distinct_types_from_enums(enums)
service_class_prefix = config["service_class_prefix"]
driver_library_interface = common_helpers.get_library_interface_type_name(config)
include_guard_name = service_helpers.get_include_guard_name(config, "_SERVICE_H")
namespace_prefix = config["namespace_component"] + "_grpc::"
custom_types = common_helpers.get_custom_types(config)
(input_custom_types, output_custom_types) = common_helpers.get_input_and_output_custom_types(config, functions)
resource_repository_deps = service_helpers.get_driver_shared_resource_repository_ptr_deps(config, functions)
resource_handle_types = service_helpers.get_resource_handle_types(config)
functions_to_generate = common_helpers.filter_proto_rpc_functions(functions)
data_moniker_functions = common_helpers.filter_moniker_streaming_functions(functions, functions_to_generate)

async_functions = service_helpers.get_async_functions(functions)
has_async_functions = any(async_functions)
base_class_name = f"{service_class_prefix}::Service"
for async_function in async_functions.keys():
  base_class_name = f"{service_class_prefix}::WithCallbackMethod_{async_function}<{base_class_name}>"
%>\

//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Service header for the ${config["driver_name"]} Metadata
//---------------------------------------------------------------------
#ifndef ${include_guard_name}
#define ${include_guard_name}

#include <${config["module_name"]}.grpc.pb.h>
#include <condition_variable>
#include <grpcpp/grpcpp.h>
#include <grpcpp/health_check_service_interface.h>
#include <grpcpp/ext/proto_server_reflection_plugin.h>
#include <map>
#include <server/converters.h>
#include <server/feature_toggles.h>
#include <server/session_resource_repository.h>
#include <server/shared_library.h>
#include <server/exceptions.h>

#include "${config["module_name"]}_library_interface.h"

namespace ${config["namespace_component"]}_grpc {

struct ${service_class_prefix}FeatureToggles
{
  using CodeReadiness = nidevice_grpc::FeatureToggles::CodeReadiness;
  ${service_class_prefix}FeatureToggles(const nidevice_grpc::FeatureToggles& feature_toggles = {});

  bool is_enabled;
% for toggle in service_helpers.get_feature_toggles(config):
  bool ${service_helpers.get_toggle_member_name(toggle)};
% endfor
};
% if data_moniker_functions:

void RegisterMonikerEndpoints();

% for function in data_moniker_functions:
<%
  method_name = common_helpers.get_data_moniker_function_name(function)
%>\
::grpc::Status ${method_name}(void* data, google::protobuf::Arena& arena, google::protobuf::Any& packedData);
% endfor
% endif

% if type_from_enum != "":
enum TypeIdentifier { ${type_from_enum} };

% endif
class ${service_class_prefix}Service final : public ${base_class_name} {
public:
  using LibrarySharedPtr = std::shared_ptr<${service_class_prefix}LibraryInterface>;
% for resource_handle_type in resource_repository_deps:
  using ${resource_repository_deps[resource_handle_type].resource_repository_alias} = ${resource_repository_deps[resource_handle_type].resource_repository_type};
% endfor

  ${service_class_prefix}Service(
    LibrarySharedPtr library,
% for resource_handle_type in resource_repository_deps:
    ${resource_repository_deps[resource_handle_type].resource_repository_alias} ${resource_repository_deps[resource_handle_type].local_name},
% endfor
    const ${service_class_prefix}FeatureToggles& feature_toggles = {});
  virtual ~${service_class_prefix}Service();

% for function in functions_to_generate:
<%
  f = functions[function]
  method_name = common_helpers.snake_to_pascal(function)
  request_type = service_helpers.get_request_type(method_name)
  response_type = service_helpers.get_response_type(method_name)
%>\
% if function in async_functions:
  ::grpc::ServerWriteReactor<${response_type}>* ${method_name}(::grpc::CallbackServerContext* context, const ${request_type}* request) override;
% else:
  ::grpc::Status ${method_name}(::grpc::ServerContext* context, const ${request_type}* request, ${response_type}* response) override;
% endif
% endfor
private:
  LibrarySharedPtr library_;
% for resource_handle_type in resource_repository_deps:
  ${resource_repository_deps[resource_handle_type].resource_repository_alias} ${resource_repository_deps[resource_handle_type].field_name};
% endfor
% for resource_handle_type in resource_handle_types:
<%
  cpp_handle_type = resource_handle_type[0].upper() + resource_handle_type[1:]
%>\
  ::grpc::Status ConvertApiErrorStatusFor${cpp_handle_type}(::grpc::ServerContextBase* context, int32_t status, ${resource_handle_type} ${config["session_handle_parameter_name"]});
% endfor
% if config["namespace_component"] == "nidaqmx":
  bool IsInternalAttribute(int32 attribute, const google::protobuf::EnumDescriptor* attribute_enum_descriptor);
% endif
% if common_helpers.has_viboolean_array_param(functions):
  void Copy(const std::vector<ViBoolean>& input, google::protobuf::RepeatedField<bool>* output);
% endif
% if common_helpers.has_enum_array_string_out_param(functions):
  template <typename TEnum>
  void CopyBytesToEnums(const std::string& input, google::protobuf::RepeatedField<TEnum>* output);
% endif
% for enum in enums_to_map:
<%
  enum_value = common_helpers.get_enum_value_cpp_type(enums[enum])
%>\
  std::map<std::int32_t, ${enum_value}> ${enum.lower()}_input_map_ { ${service_helpers.get_input_lookup_values(enums[enum])} };
  std::map<${enum_value}, std::int32_t> ${enum.lower()}_output_map_ { ${service_helpers.get_output_lookup_values(enums[enum])} };
% endfor
% for enum in enums_mapped_to_type:
  std::map<std::uint32_t, TypeIdentifier> ${enum.lower()}_type_map_ { ${service_helpers.generate_enum_oneof_selector_map(enums[enum])} };
% endfor

  ${service_class_prefix}FeatureToggles feature_toggles_;
};

} // namespace ${config["namespace_component"]}_grpc

<%
has_custom_types = False
for custom_type in custom_types:
  if custom_type["name"] in output_custom_types or custom_type["name"] in input_custom_types:
    has_custom_types = True
    break
%>\
% if has_custom_types:
namespace nidevice_grpc {
namespace converters {
%   for custom_type in custom_types:
	% if custom_type["name"] in output_custom_types:
template <>
void convert_to_grpc(const ${custom_type["name"]}& input, ${namespace_prefix}${custom_type["grpc_name"]}* output);
	% endif
	% if custom_type["name"] in input_custom_types:
template <>
${custom_type["name"]} convert_from_grpc(const ${namespace_prefix}${custom_type["grpc_name"]}& input);
	%endif
%   endfor
} // namespace converters
} // namespace nidevice_grpc

% endif
#endif  // ${include_guard_name}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/templates/service_helpers.mako sha256=91a320faf365c8d8197ba2e3906a3980282adc82ccc3b39b83a3369bb59e6cd0 bytes=57898 -->
## FILE: source/codegen/templates/service_helpers.mako

- repository: `ni/grpc-device`
- source_path: `source/codegen/templates/service_helpers.mako`
- sha256: `91a320faf365c8d8197ba2e3906a3980282adc82ccc3b39b83a3369bb59e6cd0`
- bytes: 57898

````mako
<%!
  import common_helpers
  import service_helpers
%>

## Generate the core method body for an Init method. This should be what gets included within the try block in the service method.
<%def name="define_init_method_body(function_name, function_data, parameters)">\
<%
  config = data['config']
  output_parameters = [p for p in parameters if common_helpers.is_output_parameter(p)]
  input_parameters = [p for p in parameters if common_helpers.is_input_parameter(p)]
  session_output_param = next((p for p in output_parameters if p['grpc_type'] == 'nidevice_grpc.Session'), None)
  session_behavior_param = next((p for p in input_parameters if p['grpc_type'] == 'nidevice_grpc.SessionInitializationBehavior'), None)
  session_initialized_param = next((p for p in output_parameters if common_helpers.is_proto_only_parameter(p) and p['type'] == 'bool'), None)
  output_parameters_to_initialize = [p for p in output_parameters if p['grpc_type'] != 'nidevice_grpc.Session']
  resource_handle_type = session_output_param['type']
  session_output_var_name = common_helpers.get_cpp_local_name(session_output_param)
  close_function_call = function_data['custom_close'] if 'custom_close' in function_data else f"{config['close_function']}(id)"

  explicit_session_params = (common_helpers.get_cpp_local_name(param) for param in parameters if param.get('is_session_name', False))
  session_field_name = next(explicit_session_params, 'session_name')
  add_session_snippet = 'add_session(grpc_device_session_name, init_lambda, cleanup_lambda)'
  if session_behavior_param and session_initialized_param:
      session_behavior_param_name = common_helpers.get_cpp_local_name(session_behavior_param)
      session_initialized_param_name = common_helpers.get_cpp_local_name(session_initialized_param)
      add_session_snippet = f'add_session(grpc_device_session_name, init_lambda, cleanup_lambda, {session_behavior_param_name}, &{session_initialized_param_name})'
%>\
${initialize_input_params(function_name, parameters, indent_level=1)}
${initialize_output_params(output_parameters_to_initialize, indent_level=1)}\
      auto init_lambda = [&] () {
## If the session is not returned, it's an output param and need to be declared before calling.
% if not service_helpers.is_session_returned_from_function(parameters):
        ${resource_handle_type} ${session_output_var_name};
% endif
${call_library_method(
  function_name=function_name,
  function_data=function_data,
  arg_string=service_helpers.create_args(parameters),
  indent_level=1,
  library_ptr=service_helpers.get_library_ptr_for_potentially_unmockable_function(config, parameters))
}\
        return std::make_tuple(status, ${session_output_var_name});
      };
      std::string grpc_device_session_name = request->${session_field_name}();
      // Capture the library shared_ptr by value. Do not capture `this` or any references.
      LibrarySharedPtr library = library_;
      auto cleanup_lambda = [library] (${resource_handle_type} id) { library->${close_function_call}; };
      int status = ${service_helpers.session_repository_field_name(session_output_param, config)}->${add_session_snippet};
${populate_response(function_data=function_data, parameters=parameters, init_method=True)}\
      return ::grpc::Status::OK;\
</%def>

<%def name="define_cross_driver_init_method_body(function_name, function_data, parameters)">\
<%
  config = data['config']
  initiating_driver_input_param = next(p for p in parameters if common_helpers.is_input_parameter(p) and p['grpc_type'] == 'nidevice_grpc.Session')
  output_parameters = [p for p in parameters if common_helpers.is_output_parameter(p)]
  session_output_param = next(p for p in output_parameters if p['grpc_type'] == 'nidevice_grpc.Session')
  output_parameters_to_initialize = [p for p in output_parameters if p['grpc_type'] != 'nidevice_grpc.Session']
  cross_driver_dep = service_helpers.get_cross_driver_session_dependency(session_output_param)
  session_output_var_name = common_helpers.get_cpp_local_name(session_output_param)
  session_output_field_name = common_helpers.get_grpc_field_name(session_output_param)
  initiating_driver_input_var_name = common_helpers.get_cpp_local_name(initiating_driver_input_param)
  initiating_driver_c_name = f'{initiating_driver_input_var_name}_grpc_session'
%>\
${initialize_input_params(function_name, parameters, indent_level=1)}
${initialize_output_params(output_parameters_to_initialize, indent_level=1)}\
      auto initiating_session_name = ${initiating_driver_c_name}.name();
      auto init_lambda = [&] () {
        ${cross_driver_dep.resource_handle_type} ${session_output_var_name};
        int status = library_->${function_name}(${service_helpers.create_args(parameters)});
        return std::make_tuple(status, ${session_output_var_name});
      };
      std::string session_name = request->session_name();
      int status = ${cross_driver_dep.field_name}->add_dependent_session(session_name, init_lambda, initiating_session_name);
      response->set_status(status);
      if (status == 0) {
        response->mutable_${session_output_field_name}()->set_name(session_name);
      }
      return ::grpc::Status::OK;\
</%def>

## Generate the core method body for an ivi-dance method. This should be what gets included within the try block in the service method.
<%def name="define_ivi_dance_method_body(function_name, function_data, parameters)">\
<%
  (size_param, array_param, non_ivi_params) = common_helpers.get_ivi_dance_params(parameters)
  output_parameters = [p for p in parameters if common_helpers.is_output_parameter(p)]
%>\
${initialize_input_params(function_name, non_ivi_params, indent_level=1)}\

      while (true) {
${call_library_method(
  function_name=function_name,
  function_data=function_data,
  arg_string=service_helpers.create_args_for_ivi_dance(parameters),
  indent_level=1)
}\
${populate_error_check(function_data, parameters, indent_level=1)}\
        ${size_param['type']} ${common_helpers.get_cpp_local_name(size_param)} = status;

${initialize_output_params(output_parameters, indent_level=2)}\
${call_library_method(
  function_name=function_name,
  function_data=function_data,
  arg_string=service_helpers.create_args(parameters),
  indent_level=1,
  declare_outputs=False)
}\
        ## We cast status into ${common_helpers.get_cpp_local_name(size_param)} above, so it's safe to cast
        ## back to status's type here. (we do this to avoid a compiler warning)
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer || status > static_cast<decltype(status)>(${common_helpers.get_cpp_local_name(size_param)})) {
          // buffer is now too small, try again
          continue;
        }
${populate_response(function_data=function_data, parameters=parameters, indent_level=1)}\
        return ::grpc::Status::OK;
      }\
</%def>

## Generate the core method body for an ivi-dance-with_a_twist method. This should be what gets included within the try block in the service method.
<%def name="define_ivi_dance_with_a_twist_method_body(function_name, function_data, parameters)">\
<%
  ivi_param_sets = common_helpers.get_ivi_dance_with_a_twist_params(parameters)
  non_ivi_params = common_helpers.get_params_not_in_ivi_twist(parameters, ivi_param_sets)
  output_parameters = [p for p in parameters if common_helpers.is_output_parameter(p)]
  array_output_parameters = [p for p in output_parameters if common_helpers.is_array(p['type'])]
  scalar_output_parameters = [p for p in output_parameters if p not in array_output_parameters]
%>\
${initialize_input_params(function_name, non_ivi_params, indent_level=1)}\
${initialize_output_params(scalar_output_parameters, indent_level=1)}\
      while (true) {
${call_library_method(
  function_name=function_name,
  function_data=function_data,
  arg_string=service_helpers.create_args_for_ivi_dance_with_a_twist(parameters),
  indent_level=1)
}\
${populate_error_check(function_data, parameters, indent_level=1)}\
${initialize_output_params(array_output_parameters, indent_level=2)}\
% for ivi_param_set in ivi_param_sets:
%   if not ivi_param_set.is_in_out_twist:
        auto ${ivi_param_set.size_param_name} = ${ivi_param_set.twist_param_name};
%   endif
% endfor
${call_library_method(
  function_name=function_name,
  function_data=function_data,
  arg_string=service_helpers.create_args(parameters),
  indent_level=1,
  declare_outputs=False)
}\
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
${populate_response(function_data=function_data, parameters=parameters, indent_level=1)}\
        return ::grpc::Status::OK;
      }\
</%def>


<%def name="define_async_callback_method_body(function_name, function_data, parameters, config)">\
<%
  callback_parameters = service_helpers.get_callback_method_parameters(function_data)
  response_parameters = common_helpers.filter_parameters_for_grpc_fields(callback_parameters)
  request_type = service_helpers.get_request_type(function_name)
  response_type = service_helpers.get_response_type(function_name)
  driver_library_interface = common_helpers.get_library_interface_type_name(config)
  service_class = config["service_class_prefix"] + "Service"
%>\
    using CallbackRouter = nidevice_grpc::CallbackRouter<int32, ${service_helpers.create_param_type_list(callback_parameters)}>;
    class ${function_name}Reactor : public nidevice_grpc::ServerWriterReactor<${response_type}, nidevice_grpc::CallbackRegistration> {
    public:
    ${function_name}Reactor(::grpc::CallbackServerContext* context, const ${request_type}* request, LibrarySharedPtr library, ${service_class}* service)
    {
      auto status = start(context, request, library, service);
      if (!status.ok()) {
        this->try_finish(std::move(status));
      }
    }

    ::grpc::Status start(::grpc::CallbackServerContext* context, const ${request_type}* request, LibrarySharedPtr library, ${service_class}* service)
    {
      try {
        auto handler = CallbackRouter::register_handler(
          [this](${service_helpers.create_args_for_callback(callback_parameters)}) {
            ${response_type} callback_response;
            auto response = &callback_response;
<%block filter="common_helpers.indent(2)">\
${set_response_values(output_parameters=response_parameters, init_method=False)}\
</%block>\
            queue_write(callback_response);
            return 0;
        });

        const auto& session_repository_ = service->session_repository_;
<%block filter="common_helpers.indent(1)">\
${initialize_input_params(function_name, parameters, indent_level=1)}\
</%block>\

${call_library_method(
  function_name=function_name,
  function_data=function_data,
  arg_string=service_helpers.create_args(parameters),
  library_ptr="library",
  indent_level=1)
}\
${populate_error_check(function_data, parameters, indent_level=1, service_deref="service->")}\

        // SendInitialMetadata after the driver call so that WaitForInitialMetadata can be used to ensure that calls are serialized.
        StartSendInitialMetadata();

        this->set_producer(std::move(handler));
      }
      catch (nidevice_grpc::NonDriverException& ex) {
         return ex.GetStatus();
      }

      return ::grpc::Status::OK;
    }
    };

    return new ${function_name}Reactor(context, request, library_, this);
</%def>

## Generate the core method body for a method with repeated varargs.
## This should be what gets included within the try block in the service method.
<%def name="define_repeated_varargs_method_body(function_name, function_data, parameters)">\
<%
  config = data['config']
  output_parameters = [p for p in parameters if common_helpers.is_output_parameter(p)]
%>\
${initialize_input_params(function_name, parameters, indent_level=1)}\
${initialize_output_params(output_parameters, indent_level=1)}\
${set_output_vararg_parameter_sizes(parameters)}\
${call_library_method(
  function_name=function_name,
  function_data=function_data,
  arg_string=service_helpers.create_args(parameters),
  library_ptr=service_helpers.get_library_ptr_for_potentially_unmockable_function(config, parameters))
}\
${populate_response(function_data=function_data, parameters=parameters)}\
      return ::grpc::Status::OK;\
</%def>

## Generate the core method body for an ivi-dance method. This should be what gets included within the try block in the service method.
<%def name="define_simple_method_body(function_name, function_data, parameters)">\
<%
  config = data['config']
  output_parameters = [p for p in parameters if common_helpers.is_output_parameter(p)]
%>\
${initialize_input_params(function_name, parameters, indent_level=1)}\
${initialize_output_params(output_parameters, indent_level=1)}\
% if function_name == config['close_function'] or service_helpers.is_custom_close_method(function_data):
<%
  session_param = common_helpers.get_first_session_param(parameters)
  session_param_name = f'{common_helpers.get_cpp_local_name(session_param)}_grpc_session'
%>\
      ${service_helpers.session_repository_field_name(session_param, config)}->remove_session(${session_param_name}.name());
% endif
${call_library_method(
  function_name=function_name,
  function_data=function_data,
  arg_string=service_helpers.create_args(parameters))
}\
${populate_response(function_data=function_data, parameters=parameters)}\
      return ::grpc::Status::OK;\
</%def>

<%def name="register_moniker_functions(function_name)">\
<%
  moniker_function_name = common_helpers.get_data_moniker_function_name(function_name)
%>\
    ni::data_monikers::DataMonikerService::RegisterMonikerEndpoint("${moniker_function_name}", ${moniker_function_name});
</%def>

<%def name="define_moniker_streaming_struct(begin_function_name, parameters, has_input_parameters)">\
<%
  config = data['config']
  service_class_prefix = config["service_class_prefix"]
  struct_name = common_helpers.get_data_moniker_struct_name(begin_function_name)
  moniker_input_parameters = common_helpers.get_non_streaming_input_parameters(parameters)
  request_message_type = common_helpers.get_data_moniker_request_message_type(begin_function_name)
  response_message_type = common_helpers.get_data_moniker_response_message_type(begin_function_name)
%>\
  struct ${struct_name}
  {
% for parameter in moniker_input_parameters:
<%
  parameter_name = common_helpers.get_cpp_local_name(parameter)
%>\
% if parameter.get('pointer', False):
     ${parameter['type']}* ${parameter_name};
% else:
     ${parameter['type']} ${parameter_name};
% endif
% endfor
% if has_input_parameters:
     ${service_class_prefix.lower()}_grpc::${request_message_type} request;
% endif
     ${service_class_prefix.lower()}_grpc::${response_message_type} response;
     std::shared_ptr<${service_class_prefix}LibraryInterface> library;
  };
</%def>

<%def name="define_moniker_function_body(function_name, functions)">\
<%
  function_data = functions[function_name]
  struct_name = common_helpers.get_data_moniker_struct_name(function_name)
  moniker_function_name = common_helpers.get_data_moniker_function_name(function_name)
  moniker_input_parameters = common_helpers.get_non_streaming_input_parameters(function_data['parameters'])
  streaming_param = common_helpers.get_first_streaming_parameter(function_data['parameters'])
  non_streaming_function_name = function_name.replace("Begin", "")
  non_streaming_function_parameters = functions[non_streaming_function_name]['parameters']
  arg_string = service_helpers.create_args(non_streaming_function_parameters)
  output_parameters = [p for p in non_streaming_function_parameters if common_helpers.is_output_parameter(p)]
%>\
  ::grpc::Status ${moniker_function_name}(void* data, google::protobuf::Arena& arena, google::protobuf::Any& packedData)
  {
    ${struct_name}* function_data = static_cast<${struct_name}*>(data);
    auto library = function_data->library;
    auto response = &function_data->response;
${initialize_moniker_input_parameters(moniker_input_parameters)}\
${initialize_moniker_request_for_in_functions(streaming_param, functions, function_name)}\
${initialize_output_params(output_parameters)}\

    auto status = library->${non_streaming_function_name}(${arg_string});

${populate_moniker_response_for_out_functions(output_parameters, streaming_param)}\
    return ::grpc::Status::OK;
  }
</%def>

<%def name="define_streaming_api_body(function_name, parameters)">\
<%
  struct_name = common_helpers.get_data_moniker_struct_name(function_name)
  moniker_function_name = common_helpers.get_data_moniker_function_name(function_name)
  moniker_input_parameters = common_helpers.get_non_streaming_input_parameters(parameters)
  output_parameters = [p for p in parameters if common_helpers.is_output_parameter(p)]
%>\
${initialize_input_params(function_name, moniker_input_parameters, indent_level=1)}
${initialize_moniker_struct(struct_name, moniker_input_parameters, output_parameters)}\
      auto moniker = std::make_unique<ni::data_monikers::Moniker>();
      ni::data_monikers::DataMonikerService::RegisterMonikerInstance("${moniker_function_name}", data.release(), *moniker);
      response->set_allocated_moniker(moniker.release());
      response->set_status(0);
      return ::grpc::Status::OK;\
</%def>

<%def name="initialize_moniker_request_for_in_functions(streaming_param, functions, begin_function_name)">\
% if streaming_param and streaming_param['direction'] == 'in':
  <%
    request_message_type = common_helpers.get_data_moniker_request_message_type(begin_function_name)
    non_streaming_function_name = begin_function_name.replace("Begin", "")
    input_parameters, output_parameters = common_helpers.get_data_moniker_function_parameters(functions[non_streaming_function_name])
    common_helpers.extend_input_params_with_size_params(input_parameters, functions[non_streaming_function_name])\
  %>\
  auto request = &function_data->request;

    packedData.UnpackTo(request);
${initialize_input_params(non_streaming_function_name, input_parameters)}\
% endif
</%def>

<%def name="populate_moniker_response_for_out_functions(output_parameters, streaming_param)">\
% if streaming_param['direction'] == 'out':
    if (status >= 0)
    {
      response->set_status(status);
${set_response_values(output_parameters=output_parameters, init_method=false)}\
      packedData.PackFrom(*response);
    }
    else
    {
      ## TODO this is not needed if we can make populate_response work which returns error through `AddTrailingMetadata`.
      ## But that needs `context` parameter which is not available in Moniker functions.
      return ::grpc::Status(grpc::StatusCode::UNKNOWN, "ni-error: " + status);
    }
% else:
    if (status < 0)
    {
      return ::grpc::Status(grpc::StatusCode::UNKNOWN, "ni-error: " + status);
    }
% endif
</%def>

<%def name="initialize_moniker_struct(struct_name, moniker_input_parameters, output_parameters)">\
<%
  config = data['config']
  service_class_prefix = config["service_class_prefix"]
  output_array_params = [p for p in output_parameters if common_helpers.is_array(p['type'])]
%>\
      auto data = std::make_unique<${struct_name}>();
% for parameter in moniker_input_parameters:
<%
  parameter_name = common_helpers.get_cpp_local_name(parameter)
%>\
      data->${parameter_name} = ${parameter_name};
% endfor
      data->library = std::shared_ptr<${service_class_prefix}LibraryInterface>(library_);

% for param in output_array_params:
<%
  grpc_field_name = common_helpers.get_grpc_field_name(param)
  size_param_name = common_helpers.camel_to_snake(common_helpers.get_size_param(param))
%>\
% if common_helpers.is_string_arg(param):
      data->response.mutable_${grpc_field_name}()->reserve(request->${size_param_name}());
      data->response.mutable_${grpc_field_name}()->resize(request->${size_param_name}(), 0);
% else:
      data->response.mutable_${grpc_field_name}()->Reserve(request->${size_param_name}());
      data->response.mutable_${grpc_field_name}()->Resize(request->${size_param_name}(), 0);
% endif
% endfor
</%def>

<%def name="initialize_moniker_input_parameters(moniker_input_parameters)">\
% for parameter in moniker_input_parameters:
<%
  parameter_name = common_helpers.get_cpp_local_name(parameter)
%>\
    auto ${parameter_name} = function_data->${parameter_name};
% endfor
</%def>

## Initialize the input parameters to the API call.
<%def name="initialize_input_params(function_name, parameters, indent_level=0)">\
<%
  input_parameters = [p for p in parameters if common_helpers.is_input_parameter(p)]
  input_vararg_parameters = [p for p in input_parameters if common_helpers.is_repeated_varargs_parameter(p)]
  input_vararg_parameter = input_vararg_parameters[0] if len(input_vararg_parameters) > 0 else None
%>\
<%block filter="common_helpers.indent(indent_level)">\
% for parameter in input_parameters:
${initialize_input_param(function_name, parameter, parameters, input_vararg_parameter)}\
% endfor
</%block>\
</%def>

## Initialize an input parameter for an API call.
<%def name="initialize_input_param(function_name, parameter, parameters, input_vararg_parameter=None)">\
% if common_helpers.is_repeating_parameter(parameter):
${initialize_repeating_param(parameter, input_vararg_parameter)}
% elif common_helpers.is_repeated_varargs_parameter(parameter):
${initialize_repeated_varargs_param(parameter)}
% elif common_helpers.is_bitfield_as_enum_array(parameter):
${initialize_bitfield_as_enum_array_param(function_name, parameter)}
% elif common_helpers.is_enum(parameter) and common_helpers.is_array(parameter['type']) and not common_helpers.is_string_arg(parameter):
${initialize_enum_array_input_param(function_name, parameter)}
% elif common_helpers.is_enum(parameter):
${initialize_enum_input_param(function_name, parameter)}
% elif 'hardcoded_value' in parameter:
${initialize_hardcoded_parameter(parameter)}
% elif 'callback_token' in parameter or 'callback_params' in parameter: ## pass
% elif "determine_size_from" in parameter:
${initialize_len_input_param(parameter, parameters)}
% elif common_helpers.is_two_dimension_array_param(parameter):
${initialize_two_dimension_input_param(parameter, parameters)}
% elif service_helpers.is_size_param_passed_by_ptr(parameter):
${initialize_pointer_input_parameter(parameter)}
% else:
${initialize_standard_input_param(parameter)}
% endif
</%def>

<%def name="initialize_repeating_param(parameter, input_vararg_parameter)">\
<%
  stripped_grpc_type = common_helpers.strip_repeated_from_grpc_type(input_vararg_parameter['grpc_type'])
  if stripped_grpc_type == 'string':
    stripped_grpc_type = 'std::string'
  parameter_c_type = parameter['type']
  parameter_c_type_pointer = parameter_c_type.replace('[]','*')
  parameter_name = common_helpers.get_grpc_field_name(parameter)
%>\
    auto get_${parameter['name']}_if = [](const google::protobuf::RepeatedPtrField<${stripped_grpc_type}>& vector, int n) -> ${parameter_c_type_pointer} {
          if (vector.size() > n) {
<%
    # Note that this code will not handle every datatype, but it works for all
    # the ones we currently use with repeated varargs.
    return_snippet = ''
    if input_vararg_parameter.get("is_compound_type", False):
      return_snippet += f'.{parameter_name}()'
    if common_helpers.is_string_arg(parameter):
      # Warning: We don't convert_from_grpc here (converting from utf-8) because we would need to
      # store the converted string in a buffer until the extracted c_str() is no longer needed. For
      # now this is fine, though, because the only driver that uses this is NI-DAQmx, for strings
      # that are ASCII-only. (For physical channels and lines.)
      return_snippet += f'.c_str()'
%>\
                return vector[n]${return_snippet};
          }
% if common_helpers.is_string_arg(parameter):
          return nullptr;
% else:
          return 0;
% endif
    };\
</%def>

<%def name="initialize_repeated_varargs_param(parameter)">\
<%
  config = data['config']
  parameter_name = common_helpers.get_cpp_local_name(parameter)
  field_name = common_helpers.get_grpc_field_name(parameter)
  stripped_grpc_type = common_helpers.strip_repeated_from_grpc_type(parameter['grpc_type'])
  request_snippet = f'request->{field_name}()'
  c_type = parameter['type']
  c_type_pointer = c_type.replace('[]','*')
  max_vector_size = parameter['max_length']
%>\
    auto ${parameter_name} = request->${field_name}();
    if (${parameter_name}.size() == 0) {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "No values for ${parameter["name"]} were specified");
    }
    if (${parameter_name}.size() > ${max_vector_size}) {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "More than ${max_vector_size} values for ${parameter["name"]} were specified");
    }
</%def>


## Initialize an enum array input parameter.
## This is a straight copy and does not support all of the features of enum parameters
## (i.e. mapped enums, _raw fields, etc.)
<%def name="initialize_enum_array_input_param(function_name, parameter)">\
<%
  parameter_name = common_helpers.get_cpp_local_name(parameter)
  field_name = common_helpers.get_grpc_field_name(parameter)
  element_type = service_helpers.get_c_element_type(parameter)
%>\
    auto ${parameter_name}_vector = std::vector<${element_type}>();
    ${parameter_name}_vector.reserve(request->${field_name}().size());
    std::transform(
      request->${field_name}().begin(),
      request->${field_name}().end(),
      std::back_inserter(${parameter_name}_vector),
      [](auto x) { return x; });
    auto ${parameter_name} = ${parameter_name}_vector.data();
</%def>

## Initialize a bitfield as enum array input parameter for an API call.
<%def name="initialize_bitfield_as_enum_array_param(function_name, parameter)">\
<%
  parameter_name = common_helpers.get_cpp_local_name(parameter)
  field_name = common_helpers.get_grpc_field_name(parameter)
  enum_type = common_helpers.get_bitfield_enum_type(parameter)
  bitfield_type = parameter["type"]
%>\
    const auto ${parameter_name} = nidevice_grpc::converters::convert_bitfield_as_enum_array_input(
      request->${field_name}_array(),
      request->${field_name}_raw());
</%def>

## Initialize an enum input parameter for an API call.
<%def name="initialize_enum_input_param(function_name, parameter)">\
<%
  config = data['config']
  enums = data['enums']
  namespace_prefix = config["namespace_component"] + "_grpc::"
  parameter_name = common_helpers.get_cpp_local_name(parameter)
  parameter_type_pointer = parameter['type'].replace('[]','*')
  field_name = common_helpers.get_grpc_field_name(parameter)
  pascal_field_name = common_helpers.snake_to_pascal(field_name)
  one_of_case_prefix = f'{namespace_prefix}{function_name}Request::{pascal_field_name}EnumCase'
  has_mapped_enum = 'mapped-enum' in parameter
  has_unmapped_enum = 'enum' in parameter
  if has_mapped_enum:
    map_name = parameter["mapped-enum"].lower() + "_input_map_"
    mapped_enum_iterator_name = field_name + "_imap_it"
    mapped_request_snippet = f'request->{field_name}_mapped()'
  if has_unmapped_enum:
    enum_request_snippet = f'request->{field_name}()'
    check_enum_is_valid = f"{namespace_prefix}{parameter['enum']}_IsValid({parameter_name})"
    check_enum_raw_is_valid = check_enum_is_valid
    if config["namespace_component"] == "nidaqmx":
          check_enum_raw_is_valid += f" || IsInternalAttribute({parameter_name}, {parameter['enum']}_descriptor())"

  raw_request_snippet = f'request->{field_name}_raw()'
  validate_attribute_enum = parameter.get("raw_attribute", False)
%>\
    ${parameter_type_pointer} ${parameter_name};
% if parameter['grpc_type'] == "string":
    std::string ${parameter_name}_buffer;
% endif
    switch (request->${field_name}_enum_case()) {
% if has_unmapped_enum:
      case ${one_of_case_prefix}::k${pascal_field_name}: {
%   if parameter['grpc_type'] == "string":
        ${parameter_name} = const_cast<${parameter['type']}>((${enum_request_snippet}).c_str());
%   else:
        ${parameter_name} = static_cast<${parameter['type']}>(${enum_request_snippet});
%   endif
%   if validate_attribute_enum:
## "raw" attributes always validate non-raw enum values before passing to driver
## this can be important if (a) the driver can't handle all validation scenarios
## and (b) the caller passes/casts an invalid enum value.
## Non-raw attributes allow the driver to handle validation.
        ${parameter_name} = ${check_enum_is_valid} ? ${parameter_name} : 0;
%   endif
        break;
      }
% endif
% if has_mapped_enum:
      case ${one_of_case_prefix}::k${pascal_field_name}Mapped: {
        auto ${mapped_enum_iterator_name} = ${map_name}.find(${mapped_request_snippet});
        if (${mapped_enum_iterator_name} == ${map_name}.end()) {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for ${parameter_name}_mapped was not specified or out of range.");
        }
%   if parameter['grpc_type'] == "string":
        ${parameter_name} = const_cast<${parameter_type_pointer}>((${f'{mapped_enum_iterator_name}->second'}).c_str());
%   else:
        ${parameter_name} = static_cast<${parameter['type']}>(${f'{mapped_enum_iterator_name}->second'});
%   endif
        break;
      }
% endif
      case ${one_of_case_prefix}::k${pascal_field_name}Raw: {
% if parameter['grpc_type'] == "string":
        ${parameter_name}_buffer = convert_from_grpc<std::string>(${raw_request_snippet});
        ${parameter_name} = const_cast<${parameter_type_pointer}>(${parameter_name}_buffer.c_str());
% else:
        ${parameter_name} = static_cast<${parameter['type']}>(${raw_request_snippet});
% endif
% if validate_attribute_enum: # raw validation can be overridden with a toggle.
        auto ${parameter_name}_is_valid = ${check_enum_raw_is_valid} || feature_toggles_.is_allow_undefined_attributes_enabled;
        ${parameter_name} = ${parameter_name}_is_valid ? ${parameter_name} : 0;
% endif
        break;
      }
      case ${one_of_case_prefix}::${field_name.upper()}_ENUM_NOT_SET: {
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for ${parameter_name} was not specified or out of range");
        break;
      }
    }
</%def>

## Initialize an input parameter that is determined by the 'len' size mechanism.
<%def name="initialize_len_input_param(parameter, parameters)">\
<%
  parameter_name = common_helpers.get_cpp_local_name(parameter)
  size_sources = common_helpers.get_grpc_field_names_for_param_names(
    parameters,
    parameter["determine_size_from"]
  )
  size_field_name = common_helpers.get_grpc_field_name_from_str(size_sources[-1])
  allow_optional = parameter["linked_params_are_optional"]
  allow_optional_as_cpp_constant = "true" if allow_optional else "false"
%>\
% if len(size_sources) > 1:
    auto ${parameter_name}_determine_from_sizes = std::array<int, ${len(size_sources)}>
    {
<%block filter="common_helpers.trim_trailing_comma()">\
% for size_source in size_sources:
      request->${size_source}_size(),
% endfor
</%block>\
    };
    const auto ${parameter_name}_size_calculation = calculate_linked_array_size(${parameter_name}_determine_from_sizes, ${allow_optional_as_cpp_constant});

    if (${parameter_name}_size_calculation.match_state == MatchState::MISMATCH) {
      return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The sizes of linked repeated fields [${str.join(', ', size_sources)}] do not match");
    }
% if allow_optional:
    // NULL out optional params with zero sizes.
    if (${parameter_name}_size_calculation.match_state == MatchState::MATCH_OR_ZERO) {
% for size_source in size_sources:
      ${size_source} = request->${size_source}_size() ? std::move(${size_source}) : nullptr;
% endfor
    }
% endif
    auto ${parameter_name} = ${parameter_name}_size_calculation.size;
% else:
<%
  size_field_name = size_sources[-1]
  linked_array_param_name = parameter["determine_size_from"]
  linked_array_param = common_helpers.get_param_with_name(parameters, linked_array_param_name[-1])
  calculate_len_in_bytes = common_helpers.get_size_mechanism(linked_array_param) == "len-in-bytes"
  linked_array_param_underlying_type = common_helpers.get_underlying_type(linked_array_param)
  if len(linked_array_param_name) > 1 and calculate_len_in_bytes:
    raise f"{parameter['name']} has 'len-in-bytes' set but has more than one 'determine-size-from' values!"
%>\
<%
  target_type = parameter['type']
  needs_range_check = target_type not in ['size_t']
%>\
%if not needs_range_check:
%if calculate_len_in_bytes:
    ${target_type} ${parameter_name} = static_cast<${target_type}>(request->${size_field_name}().size() * sizeof(${linked_array_param_underlying_type}));\
%elif linked_array_param['type'] in ['ViConstString', 'const char[]']:
    ${target_type} ${parameter_name} = static_cast<${target_type}>(convert_from_grpc<std::string>(request->${size_field_name}()).size());\
%else:
    ${target_type} ${parameter_name} = static_cast<${target_type}>(request->${size_field_name}().size());\
%endif
%else:
%if calculate_len_in_bytes:
    auto ${parameter_name}_raw = request->${size_field_name}().size() * sizeof(${linked_array_param_underlying_type});
%elif linked_array_param['type'] in ['ViConstString', 'const char[]']:
    auto ${parameter_name}_raw = convert_from_grpc<std::string>(request->${size_field_name}()).size();
%else:
    auto ${parameter_name}_raw = request->${size_field_name}().size();
%endif
    ${target_type} ${parameter_name} = nidevice_grpc::converters::convert_size<${target_type}>(${parameter_name}_raw, "${parameter_name}");\
%endif
% endif
</%def>

## Initialize an input parameter with the 'two-dimension' size mechanism.
<%def name="initialize_two_dimension_input_param(parameter, parameters)">\
<%
  parameter_name = common_helpers.get_cpp_local_name(parameter)
  size_param_name = common_helpers.get_size_param(parameter)
  size_param = common_helpers.get_param_with_name(parameters, size_param_name)
  size_field_name = common_helpers.get_grpc_field_name(size_param)
%>\
${initialize_standard_input_param(parameter)}
    auto total_length = std::accumulate(request->${size_field_name}().cbegin(), request->${size_field_name}().cend(), 0);

    if (total_length != request->${parameter_name}_size()) {
      return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The total size of the two-dimensional array ${parameter_name} does not match the expected size from the sum of ${size_field_name}");
    }
</%def>


## Initialize a 'hardcoded' param.
<%def name="initialize_hardcoded_parameter(parameter)">\
    auto ${common_helpers.get_cpp_local_name(parameter)} = ${parameter['hardcoded_value']};\
</%def>

## Initialize an input parameter that's passed by pointer.
<%def name="initialize_pointer_input_parameter(parameter)">\
    ${parameter['type']} ${common_helpers.get_cpp_local_name(parameter)}_copy = request->${common_helpers.get_cpp_local_name(parameter)}();\
</%def>


## Initialize an input parameter for an API call.
<%def name="initialize_standard_input_param(parameter)">\
<%
  config = data['config']
  parameter_name = common_helpers.get_cpp_local_name(parameter)
  field_name = common_helpers.get_grpc_field_name(parameter)
  request_snippet = f'request->{field_name}()'
  c_type = parameter['type']
  grpc_type = parameter.get('grpc_type', None)
  c_type_pointer = c_type.replace('[]','*')
  is_array = common_helpers.is_array(c_type)
  c_type_underlying_type = common_helpers.get_underlying_type_name(c_type)
  c_element_type_that_needs_coercion = service_helpers.get_c_element_type_for_array_that_needs_coercion(parameter)
%>\
% if c_type in ['ViConstString', 'const char[]']:
    auto ${parameter_name}_mbcs = convert_from_grpc<std::string>(${request_snippet});
    auto ${parameter_name} = ${parameter_name}_mbcs.c_str();\
% elif grpc_type == 'string':
    auto ${parameter_name}_mbcs = convert_from_grpc<std::string>(${request_snippet});
    ${c_type_pointer} ${parameter_name} = (${c_type_pointer})${parameter_name}_mbcs.c_str();\
% elif common_helpers.is_string_arg(parameter):
    ${c_type_pointer} ${parameter_name} = (${c_type_pointer})${request_snippet}.c_str();\
% elif common_helpers.supports_standard_copy_conversion_routines(parameter):
    auto ${parameter_name} = convert_from_grpc<${c_type_underlying_type}>(${str.join(", ", [request_snippet] + parameter.get("additional_arguments_to_copy_convert", []))});\
% elif grpc_type == 'repeated nidevice_grpc.Session':
    auto ${parameter_name}_request = ${request_snippet};
    std::vector<${c_type_underlying_type}> ${parameter_name};
    std::transform(
      ${parameter_name}_request.begin(),
      ${parameter_name}_request.end(),
      std::back_inserter(${parameter_name}),
      [&](auto session) { return ${service_helpers.session_repository_field_name(parameter, config)}->access_session(session.name()); }); \
% elif c_type == 'ViBoolean[]':
    auto ${parameter_name}_request = ${request_snippet};
    std::vector<${c_type_underlying_type}> ${parameter_name};
    std::transform(
      ${parameter_name}_request.begin(),
      ${parameter_name}_request.end(),
      std::back_inserter(${parameter_name}),
      [](auto x) { return x ? VI_TRUE : VI_FALSE; });
% elif c_type in ['ViInt16[]', 'ViUInt16[]']:
    auto ${parameter_name}_request = ${request_snippet};
    std::vector<${c_type_underlying_type}> ${parameter_name};
    std::transform(
      ${parameter_name}_request.begin(),
      ${parameter_name}_request.end(),
      std::back_inserter(${parameter_name}),
      [](auto x) { return (${c_type_underlying_type})x; }); \
% elif c_type == 'ViAddr':
    ${c_type} ${parameter_name} = reinterpret_cast<${c_type}>(${request_snippet});\
% elif c_type in ['ViChar', 'ViInt8', 'ViInt16']:
    ${c_type} ${parameter_name} = static_cast<${c_type}>(${request_snippet});\
% elif grpc_type == 'nidevice_grpc.Session':
    auto ${parameter_name}_grpc_session = ${request_snippet};
    ${c_type} ${parameter_name} = ${service_helpers.session_repository_field_name(parameter, config)}->access_session(${parameter_name}_grpc_session.name());\
% elif is_array and common_helpers.is_driver_typedef_with_same_size_but_different_qualifiers(c_type_underlying_type):
    auto ${parameter_name} = const_cast<${c_type_pointer}>(reinterpret_cast<const ${c_type_pointer}>(${request_snippet}.data()));\
% elif c_type in ['const int32[]', 'const uInt32[]']:
    auto ${parameter_name} = reinterpret_cast<${c_type_pointer}>(${request_snippet}.data());\
% elif grpc_type == 'bytes':
    auto ${parameter_name} = reinterpret_cast<const unsigned char*>(${request_snippet}.data());\
% elif service_helpers.is_scalar_input_that_needs_coercion(parameter):
    auto ${parameter_name}_raw = ${request_snippet};
    if (${parameter_name}_raw < std::numeric_limits<${c_type}>::min() || ${parameter_name}_raw > std::numeric_limits<${c_type}>::max()) {
        std::string message("value ");
        message.append(std::to_string(${parameter_name}_raw));
        message.append(" doesn't fit in datatype ");
        message.append("${c_type}");
        throw nidevice_grpc::ValueOutOfRangeException(message);
    }
    auto ${parameter_name} = static_cast<${c_type}>(${parameter_name}_raw);
% elif service_helpers.is_input_array_that_needs_coercion(parameter):
    auto ${parameter_name}_raw = ${request_snippet};
    auto ${parameter_name} = std::vector<${c_element_type_that_needs_coercion}>();
    ${parameter_name}.reserve(${parameter_name}_raw.size());
    std::transform(
      ${parameter_name}_raw.begin(),
      ${parameter_name}_raw.end(),
      std::back_inserter(${parameter_name}),
      [](auto x) {
            if (x < std::numeric_limits<${c_element_type_that_needs_coercion}>::min() || x > std::numeric_limits<${c_element_type_that_needs_coercion}>::max()) {
                std::string message("value ");
                message.append(std::to_string(x));
                message.append(" doesn't fit in datatype ");
                message.append("${c_element_type_that_needs_coercion}");
                throw nidevice_grpc::ValueOutOfRangeException(message);
            }
            return static_cast<${c_element_type_that_needs_coercion}>(x);
      });
% elif common_helpers.is_array(c_type):
    auto ${parameter_name} = const_cast<${c_type_pointer}>(${request_snippet}.data());\
% elif common_helpers.is_nidevice_enum_parameter(grpc_type):
    auto ${parameter_name} = ${request_snippet};\
% else:
    ${c_type} ${parameter_name} = ${request_snippet};\
% endif
</%def>

<%def name="set_output_vararg_parameter_sizes(parameters)">\
<%
  input_vararg_parameter = [p for p in parameters if common_helpers.is_repeated_varargs_parameter(p) and common_helpers.is_input_parameter(p)][0]
  input_parameter_name = common_helpers.get_cpp_local_name(input_vararg_parameter)
  output_vararg_parameters = [p for p in parameters if common_helpers.is_repeating_parameter(p) and not common_helpers.is_input_parameter(p)]
%>\
% for parameter in output_vararg_parameters:
<%
  parameter_name = common_helpers.get_cpp_local_name(parameter)
%>\
      ${parameter_name}Vector.resize(${input_parameter_name}.size());
% endfor
</%def>

## Initialize the output parameters for an API call.
<%def name="initialize_output_params(output_parameters, indent_level=0)">\
<%
  output_parameters = common_helpers.get_params_needing_initialization(output_parameters)
%>\
<%block filter="common_helpers.indent(indent_level)">\
% for parameter in output_parameters:
<%
  parameter_name = common_helpers.get_cpp_local_name(parameter)
  underlying_param_type = common_helpers.get_underlying_type_name(parameter["type"])
  grpc_type = parameter["grpc_type"]
  grpc_cpp_lib_type = service_helpers.get_protobuf_cpplib_type(grpc_type)
%>\
% if 'hardcoded_value' in parameter:
${initialize_hardcoded_parameter(parameter)}
% elif common_helpers.supports_standard_output_allocation_routines(parameter):
    auto ${parameter_name} = allocate_output_storage<${underlying_param_type}, ${grpc_cpp_lib_type}>(${str.join(", ", parameter.get("additional_arguments_to_output_allocation", []))});
% elif common_helpers.is_repeating_parameter(parameter):
    auto get_${parameter_name}_if = [](std::vector<${underlying_param_type}>& vector, int n) -> ${underlying_param_type}* {
          if (vector.size() > n) {
## Note that this code will not handle every datatype, but it works for all
## the ones we currently use with repeated varargs.
                return &(vector[n]);
          }
          return nullptr;
    };
    std::vector<${underlying_param_type}> ${parameter_name}Vector;
% elif common_helpers.is_repeated_varargs_parameter(parameter): # pass
% elif common_helpers.is_array(parameter['type']):
<%
  buffer_size = common_helpers.get_buffer_size_expression(parameter)
  size = common_helpers.get_size_expression(parameter)
%>\
%   if common_helpers.supports_standard_copy_conversion_routines(parameter):
    std::vector<${underlying_param_type}> ${parameter_name}(${size}, ${underlying_param_type}());
## Byte arrays are leveraging a string as a buffer, so we don't need to take special consideration of the null terminator.
%   elif grpc_type == 'bytes':
    std::string ${parameter_name}(${size}, '\0');
## Driver string APIs require room in the buffer for the null terminator. We need to account for that when sizing the string.
%   elif common_helpers.is_string_arg(parameter) and common_helpers.get_size_mechanism(parameter) == 'fixed':
    std::string ${parameter_name}(${size}, '\0');
%   elif common_helpers.is_string_arg(parameter):
    std::string ${parameter_name};
    if (${buffer_size} > 0) {
        ${parameter_name}.resize(${size});
    }
%   elif service_helpers.is_output_array_that_needs_coercion(parameter):
    std::vector<${underlying_param_type}> ${parameter_name}(${size});
%   elif common_helpers.is_enum(parameter):
    response->mutable_${parameter_name}_raw()->Resize(${size}, 0);
    ${underlying_param_type}* ${parameter_name} = reinterpret_cast<${underlying_param_type}*>(response->mutable_${parameter_name}_raw()->mutable_data());
%   elif common_helpers.is_driver_typedef_with_same_size_but_different_qualifiers(underlying_param_type):
    response->mutable_${parameter_name}()->Resize(${size}, 0);
    ${underlying_param_type}* ${parameter_name} = reinterpret_cast<${underlying_param_type}*>(response->mutable_${parameter_name}()->mutable_data());
%   else:
    response->mutable_${parameter_name}()->Resize(${size}, 0);
    ${underlying_param_type}* ${parameter_name} = response->mutable_${parameter_name}()->mutable_data();
%   endif
% else:
    ${underlying_param_type} ${parameter_name} {};
% endif
% endfor
</%block>\
</%def>


## Handles populating the response message after calling the driver API.
<%def name="populate_response(function_data, parameters, indent_level=0, init_method=False)">\
<%
  output_parameters = [p for p in parameters if common_helpers.is_output_parameter(p)]
  get_last_error_outputs = service_helpers.get_last_error_output_params(output_parameters)
  normal_outputs = [p for p in output_parameters if not p in get_last_error_outputs]
%>\
<%block filter="common_helpers.indent(indent_level)">\
${populate_error_check(function_data, parameters)}\
      response->set_status(status);
%if output_parameters:
${set_response_values(normal_outputs, init_method)}\
%endif
</%block>\
</%def>

## Handles populating the response message after calling the driver API.
<%def name="populate_error_check(function_data, parameters, indent_level=0, service_deref='')">\
<%
  config = data['config']
  input_parameters = [p for p in parameters if common_helpers.is_input_parameter(p)]
  resource_handle_types = service_helpers.get_resource_handle_types(config)
  error_parameters = [p for p in parameters if common_helpers.is_output_parameter(p) and "return_on_error_key" in p]
%>\
<%block filter="common_helpers.indent(indent_level)">\
<%
  session = 0
  handle_type = resource_handle_types[0]
  for parameter in input_parameters:
    if parameter['type'] in resource_handle_types:
      session = common_helpers.get_cpp_local_name(parameter)
      handle_type = parameter['type']
      break
  cpp_handle_type = handle_type[0].upper() + handle_type[1:]
  method_call = ""
  if function_data.get('exclude_from_get_last_error', False):
    method_call = f'return nidevice_grpc::ApiErrorToStatus(context, status);'
  else:
    method_call = f'return {service_deref}ConvertApiErrorStatusFor{cpp_handle_type}(context, status, {session});'
%>\
      %for error_parameter in error_parameters:
      context->AddTrailingMetadata("${error_parameter["return_on_error_key"]}", std::to_string(${common_helpers.pascal_to_snake(error_parameter["name"])}));
      %endfor
      %if "timeout_error" in function_data:
      if (!status_ok(status) && status != ${function_data["timeout_error"]}) {
      %else:
      if (!status_ok(status)) {
      %endif
        ${method_call}
      }
</%block>\
</%def>


## Set output parameters updated through API call on the gRPC response message.
<%def name="set_response_values(output_parameters, init_method)">\
<%
  output_parameters = [p for p in output_parameters if service_helpers.should_copy_to_response(p)]
  config = data['config']
  enums = data['enums']
  namespace_prefix = config["namespace_component"] + "_grpc::"
%>\
% for parameter in output_parameters:
<%
  parameter_name = common_helpers.get_cpp_local_name(parameter)
  field_name = common_helpers.get_grpc_field_name(parameter)
  if common_helpers.has_value_converted_to_c_representation(output_parameters, parameter):
    parameter_name = common_helpers.get_value_converted_to_c_representation(output_parameters, parameter)
%>\
%   if common_helpers.is_repeating_parameter(parameter):
<%
    varargs_parameter = [p for p in output_parameters if common_helpers.is_repeated_varargs_parameter(p)][0]
    varargs_parameter_name = common_helpers.get_cpp_local_name(varargs_parameter)
%>\
## Note that this currently only supports one repeated output parameter.
      for (int i = 0; i < ${parameter_name}Vector.size(); ++i) {
%     if 'enum' in parameter:
        response->add_${varargs_parameter_name}(static_cast<${parameter['enum']}>(${parameter_name}Vector[i]));
%     else:
        response->add_${varargs_parameter_name}(${parameter_name}Vector[i]);
%     endif
      }
%   elif common_helpers.is_repeated_varargs_parameter(parameter): #pass
%   elif common_helpers.is_enum(parameter) == True:
<%
  has_mapped_enum = 'mapped-enum' in parameter
  has_unmapped_enum = 'enum' in parameter
  is_bitfield_as_enum_array = 'bitfield_as_enum_array' in parameter
  if has_mapped_enum:
    mapped_enum_name = parameter["mapped-enum"]
    map_name = mapped_enum_name.lower() + "_output_map_"
    mapped_enum_iterator_name = parameter_name + "_omap_it"
  is_array = common_helpers.is_array(parameter["type"])
  is_string = common_helpers.is_string_arg(parameter)
  uses_raw_output_as_read_buffer = is_array and not is_string
  use_checked_enum_conversion = parameter.get("use_checked_enum_conversion", False)
%>\
%     if has_mapped_enum:
      auto ${mapped_enum_iterator_name} = ${map_name}.find(${parameter_name});
      if(${mapped_enum_iterator_name} != ${map_name}.end()) {
        response->set_${field_name}_mapped(static_cast<${namespace_prefix}${mapped_enum_name}>(${mapped_enum_iterator_name}->second));
      }
%     endif
%     if has_unmapped_enum:
%       if use_checked_enum_conversion:
      auto checked_convert_${parameter_name} = [](auto raw_value) {
        bool raw_value_is_valid = ${namespace_prefix}${parameter["enum"]}_IsValid(raw_value);
        auto valid_enum_value = raw_value_is_valid ? raw_value : 0;
        return static_cast<${namespace_prefix}${parameter["enum"]}>(valid_enum_value);
      };
%       endif
%       if is_string:
      CopyBytesToEnums(${parameter_name}, response->mutable_${field_name}());
%       elif uses_raw_output_as_read_buffer:
<%
      raw_response_field = f"response->{field_name}_raw()"
      cast_x_to_enum = f"static_cast<{namespace_prefix}{parameter['enum']}>(x)"
      checked_convert_x_to_enum = f"checked_convert_{parameter_name}(x)"
      convert_x_to_enum = checked_convert_x_to_enum if use_checked_enum_conversion else cast_x_to_enum
%>\
${initialize_response_buffer(parameter_name=parameter_name, parameter=parameter)}\
${copy_to_response_with_transform(source_buffer=raw_response_field, parameter_name=parameter_name, transform_x=convert_x_to_enum, size=common_helpers.get_size_expression(parameter))}\
%       elif parameter['type'] == 'ViReal64':
      if(${parameter_name} == (int)${parameter_name}) {
        response->set_${field_name}(static_cast<${namespace_prefix}${parameter["enum"]}>(static_cast<int>(${parameter_name})));
      }
%       elif parameter.get("use_checked_enum_conversion", False):
      response->set_${field_name}(checked_convert_${parameter_name}(${parameter_name}));
%       else:
      response->set_${field_name}(static_cast<${namespace_prefix}${parameter["enum"]}>(${parameter_name}));
%       endif
%     endif
%     if is_bitfield_as_enum_array:
%       for flag_value, flag_enum_name in service_helpers.get_bitfield_value_to_name_mapping(parameter, enums).items():
      if (${parameter_name} & ${hex(flag_value)})
        response->add_${field_name}_array(${flag_enum_name});
%       endfor
%     endif
%     if not uses_raw_output_as_read_buffer: # Set data to raw, unless we *got* the data from raw.
      response->set_${field_name}_raw(${parameter_name});
%     endif
%   elif service_helpers.is_output_array_that_needs_coercion(parameter):
${initialize_response_buffer(parameter_name=parameter_name, parameter=parameter)}\
${copy_to_response_with_transform(source_buffer=parameter_name, parameter_name=parameter_name, transform_x="x", size=common_helpers.get_size_expression(parameter))}\
%   elif common_helpers.supports_standard_copy_conversion_routines(parameter):
      convert_to_grpc(${str.join(", ", [f'{parameter_name}', f'response->mutable_{field_name}()'] + parameter.get("additional_arguments_to_copy_convert", []))});
%   elif parameter['grpc_type'] == 'string':
      std::string ${parameter_name}_utf8;
      convert_to_grpc(${parameter_name}, &${parameter_name}_utf8);
      response->set_${field_name}(${parameter_name}_utf8);
%   elif common_helpers.is_string_arg(parameter):
      response->set_${field_name}(${parameter_name});
%   elif parameter['grpc_type'] == 'nidevice_grpc.Session':
%      if not init_method: # Non-init methods need to resolve the session ID from the out param.
      auto grpc_device_session_name = ${service_helpers.session_repository_field_name(parameter, config)}->resolve_session_name(${parameter_name});
%      endif
      response->mutable_${field_name}()->set_name(grpc_device_session_name);
%   elif common_helpers.is_array(parameter['type']):
%     if common_helpers.get_size_mechanism(parameter) == 'passed-in-by-ptr':
### size may have changed
      response->mutable_${field_name}()->Resize(${common_helpers.get_size_expression(parameter)}, 0);
%     endif
### pass: other array types don't need to copy.
%   elif parameter['type'] == 'ViAddr':
      response->set_${field_name}(reinterpret_cast<uint64_t>(${parameter_name}));
%   else:
      response->set_${field_name}(${parameter_name});
%   endif
%   if common_helpers.is_regular_string_arg(parameter):
      nidevice_grpc::converters::trim_trailing_nulls(*(response->mutable_${field_name}()));
%   endif
### Handle ivi-dance-with-a-twist resizing.
%   if common_helpers.is_ivi_dance_array_with_a_twist_param(parameter):
<%
  size = common_helpers.get_size_expression(parameter)
%>\
%     if common_helpers.is_regular_byte_array_arg(parameter):
      response->mutable_${field_name}()->resize(${size});
%     elif common_helpers.is_regular_string_arg(parameter):
### pass: handled above with trim_trailing_nulls for all string outputs.
%     elif common_helpers.is_struct(parameter):
##        RepeatedPtrField doesn't support Resize(), so use DeleteSubrange()
##        to delete any extra elements.
      {
        auto shrunk_size = ${size};
        auto current_size = response->mutable_${field_name}()->size();
        if (shrunk_size != current_size) {
          response->mutable_${field_name}()->DeleteSubrange(shrunk_size, current_size - shrunk_size);
        }
      }
%     else:
## This code doesn't handle all parameter types (i.e., enums), see what initialize_output_params() does for that.
      response->mutable_${field_name}()->Resize(${size}, 0);
%     endif
%   endif
% endfor
</%def>

## Allocate the response buffer using get_size_expression.
<%def name="initialize_response_buffer(parameter_name, parameter)">\
      response->mutable_${parameter_name}()->Clear();
      response->mutable_${parameter_name}()->Reserve(${common_helpers.get_size_expression(parameter)});
</%def>

## Copy source_buffer to response->mutable_[parameter_name]() applying transform_x.
<%def name="copy_to_response_with_transform(source_buffer, parameter_name, transform_x, size)">\
      std::transform(
        ${source_buffer}.begin(),
        ${source_buffer}.begin() + ${size},
        google::protobuf::RepeatedFieldBackInserter(response->mutable_${parameter_name}()),
        [&](auto x) {
            return ${transform_x};
        });
</%def>

## Call the driver library method function_name.
## function_name: name of the function.
## function_data: function metadata.
## arg_string: comma separated argument list to pass to the function (see service_helpers.create_args),
## indent_level: (Optional) levels of additional indentation for the call snippet.
## library_ptr: (Optional) variable or expression for the library pointer (default: this->library_).
## declare_outputs: (Optional) If this is true, variables will be declared as "auto". If false, variables will just be assigned (default: False).
<%def name="call_library_method(
  function_name,
  function_data,
  arg_string,
  indent_level=0,
  library_ptr='library_',
  declare_outputs=True)">\
<%
  return_type = service_helpers.get_function_return_type(function_data)
  return_value_name = service_helpers.get_return_value_name(function_data)
  auto_decl = "auto " if declare_outputs else ""
%>\
<%block filter="common_helpers.indent(indent_level)">\
% if return_type != "void":
      ${auto_decl}${return_value_name} = ${library_ptr}->${function_name}(${arg_string});
% else:
      ${library_ptr}->${function_name}(${arg_string});
% endif
% if service_helpers.has_status_expression(function_data):
      ${auto_decl}status = ${service_helpers.get_status_expression(function_data)};
% endif
</%block>\
</%def>
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/templates/service_registrar.cpp.mako sha256=bc6aae2b020a85d108246949507d12a5546cb8aaf8d564e889f574f3781490a4 bytes=2245 -->
## FILE: source/codegen/templates/service_registrar.cpp.mako

- repository: `ni/grpc-device`
- source_path: `source/codegen/templates/service_registrar.cpp.mako`
- sha256: `bc6aae2b020a85d108246949507d12a5546cb8aaf8d564e889f574f3781490a4`
- bytes: 2245

````mako
<%
import common_helpers
import service_helpers

config = data["config"]

namespace = f"{config['namespace_component']}_grpc"
module_name = config["module_name"]
resource_repository_deps = service_helpers.get_driver_shared_resource_repository_ptr_deps(config, data["functions"])
service_class_prefix = config["service_class_prefix"]
%>\

//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Service registrar implementation for the ${config["driver_name"]} Metadata
//---------------------------------------------------------------------
#include "${module_name}_library.h"

#include <grpcpp/server_builder.h>

#include "${module_name}_service.h"
#include "${module_name}_service_registrar.h"
% if config.get("has_moniker_streaming_apis", False):
#include <server/data_moniker_service.h>
% endif

namespace ${namespace} {

std::shared_ptr<void> register_service(
  grpc::ServerBuilder& builder,
% for resource_handle_type in resource_repository_deps:
  const ${resource_repository_deps[resource_handle_type].resource_repository_type}& ${resource_repository_deps[resource_handle_type].local_name},
% endfor
  const nidevice_grpc::FeatureToggles& feature_toggles)
{
  auto toggles = ${service_class_prefix}FeatureToggles(feature_toggles);

  if (toggles.is_enabled)
  {
    auto library = std::make_shared<${service_class_prefix}Library>();
    auto service = std::make_shared<${service_class_prefix}Service>(
      library,
% for resource_handle_type in resource_repository_deps:
      ${resource_repository_deps[resource_handle_type].local_name},
% endfor
      toggles);
    builder.RegisterService(service.get());
% if config.get("has_moniker_streaming_apis", False):

    if (ni::data_monikers::is_moniker_streaming_enabled(feature_toggles)) {
<%
  namespace = f"{config['namespace_component']}_grpc"
%>\
<%block filter="common_helpers.os_conditional_compile_block(config)">\
      ${namespace}::RegisterMonikerEndpoints();
</%block>\
    }

% endif
    return service;
  }

  return {};
}

} // ${namespace}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/templates/service_registrar.h.mako sha256=543f54e266e43e643346441f52cd2cc832ac5d0db2ef3861c0f715c9c772ee84 bytes=1592 -->
## FILE: source/codegen/templates/service_registrar.h.mako

- repository: `ni/grpc-device`
- source_path: `source/codegen/templates/service_registrar.h.mako`
- sha256: `543f54e266e43e643346441f52cd2cc832ac5d0db2ef3861c0f715c9c772ee84`
- bytes: 1592

````mako
<%
import common_helpers
import service_helpers

config = data["config"]

include_guard_name = service_helpers.get_include_guard_name(config, "_SERVICE_REGISTRAR_H")
namespace = f"{config['namespace_component']}_grpc"
resource_handle_types = service_helpers.get_resource_handle_types(config)
resource_repository_deps = service_helpers.get_driver_shared_resource_repository_ptr_deps(config, data["functions"])
%>\

//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Service registrar header for the ${config["driver_name"]} Metadata
//---------------------------------------------------------------------
#ifndef ${include_guard_name}
#define ${include_guard_name}
#include <server/feature_toggles.h>
#include <server/session_resource_repository.h>

#include <memory>

#include <${config["c_header"]}> // for ${", ".join(resource_handle_types)}

namespace grpc {
class ServerBuilder;
}

namespace ${namespace} {
using CodeReadiness = nidevice_grpc::FeatureToggles::CodeReadiness;

std::shared_ptr<void> register_service(
  grpc::ServerBuilder& server_builder, 
% for resource_handle_type in resource_repository_deps:
  const ${resource_repository_deps[resource_handle_type].resource_repository_type}& ${resource_repository_deps[resource_handle_type].local_name},
% endfor
  const nidevice_grpc::FeatureToggles& feature_toggles);

} // ${namespace}

#endif  // ${include_guard_name}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/validate_examples.py sha256=16ddee31c30eb826927d4c91e416c68cb4c5da227bf1e996b4b0a0d9b14d161b bytes=5073 -->
## FILE: source/codegen/validate_examples.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/validate_examples.py`
- sha256: `16ddee31c30eb826927d4c91e416c68cb4c5da227bf1e996b4b0a0d9b14d161b`
- bytes: 5073

````python
"""Script for validating the examples."""

import re
from argparse import ArgumentParser
from contextlib import contextmanager
from os import chdir, getcwd, system as _system_core
from pathlib import Path
from shutil import copytree, rmtree
from sys import exit
from typing import List, NamedTuple, Optional

from stage_client_files import stage_client_files


class _CommandRecord(NamedTuple):
    exit_code: int
    command: str


_FAILED_COMMANDS: List[_CommandRecord] = []


def _system(command):
    """Capture the result of any failed system calls in _FAILED_COMMANDS."""
    exit_code = _system_core(command)
    if exit_code:
        _FAILED_COMMANDS.append(_CommandRecord(exit_code, command))


@contextmanager
def _create_stage_dir(staging_dir):
    initial_dir = getcwd()
    try:
        rmtree(staging_dir, ignore_errors=True)
        staging_dir.mkdir(parents=True)
        chdir(staging_dir)
        yield
    finally:
        chdir(initial_dir)


def _stage_client_files(artifact_location: Optional[str], staging_dir: Path) -> None:
    if artifact_location:
        copytree(artifact_location, staging_dir, dirs_exist_ok=True)
    else:
        stage_client_files(staging_dir, True)


def _validate_examples(
    driver_glob_expression: str,
    exclude: str,
    ip_address: str,
    device_name: str,
    artifact_location: Optional[str],
) -> None:
    ni_apis_root = Path(__file__).parent.parent.parent / "third_party" / "ni-apis"
    ni_apis_root = ni_apis_root.resolve()

    staging_dir = Path(__file__).parent.parent.parent / "build" / "validate_examples"
    staging_dir = staging_dir.resolve()

    print(f"Validating examples using staging_dir: {staging_dir}")

    with _create_stage_dir(staging_dir):
        _stage_client_files(artifact_location, staging_dir)
        examples_dir = staging_dir / "examples"
        proto_dir = staging_dir / "proto"

        proto_files_str = str.join(" ", [file.name for file in proto_dir.glob("*.proto")])

        _system("poetry lock")
        _system("poetry install")

        _system(
            rf"poetry run python -m grpc_tools.protoc -I{proto_dir} -I{ni_apis_root}/ni/grpcdevice/v1/ --python_out=. --grpc_python_out=. --mypy_out=. --mypy_grpc_out=. {proto_files_str}"
        )
        for dir in examples_dir.glob(driver_glob_expression):
            if exclude and re.search(exclude, dir.as_posix()):
                print(f"-- Skipping: {dir.name}")
                continue
            print()
            print(f"-- Validating: {dir.name}")

            # Use '=' to allow a leading dash, e.g. "-aio\.py$".
            extend_exclude_option = f' --extend-exclude="{exclude}"' if exclude else ""
            exclude_option = f' --exclude="{exclude}"' if exclude else ""

            print(f" -> Running black line-length 100")
            _system(f"poetry run black --check --line-length 100 {dir}{extend_exclude_option}")

            print(f" -> Running mypy")
            _system(
                f"poetry run mypy {dir} --check-untyped-defs --ignore-missing-imports{exclude_option}"
            )

            if ip_address:
                for file in dir.glob("*.py"):
                    if exclude and re.search(exclude, file.as_posix()):
                        print(f" -> Skipping example: {file.name}")
                        continue
                    print(f" -> Running example: {file.name}")
                    port = 31763
                    _system(rf"poetry run python {file} {ip_address} {port} {device_name}")


if __name__ == "__main__":
    parser = ArgumentParser(description="Validate grpc-device examples.")
    parser.add_argument(
        "-p",
        "--pattern",
        help='Glob expression for scrapigen driver names to validate (e.g., "*rfmx*").',
        default="*",
    )

    parser.add_argument(
        "-e",
        "--exclude",
        help="Regular expression matching files and directories to exclude from validation "
        '(e.g. --exclude="-aio\.py$"). Use forward slash as a directory separator.',
        default="",
    )
    parser.add_argument(
        "-s",
        "--server",
        help="grpc-device server IP address. If not specified, skip running examples.",
    )

    parser.add_argument(
        "-d",
        "--device",
        help="Device alias to run examples. Default: no device passed to example (uses session-level simulation).",
        default="",
    )

    parser.add_argument(
        "-a",
        "--artifacts",
        help="Pre-existing client artifact directory. If set, these files will be used. Otherwise, artifacts will be staged from source.",
        default=None,
    )

    args = parser.parse_args()

    _validate_examples(args.pattern, args.exclude, args.server, args.device, args.artifacts)

    if any(_FAILED_COMMANDS):
        for code, command in _FAILED_COMMANDS:
            print(f"FAILED STEP ({code}): [{command}]")

        exit(1)
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/validate_imported_protos.py sha256=e25ee0d50696503a3fa186babd8a2b2385d0c9aeb06369b0e82cec3b2b532613 bytes=2724 -->
## FILE: source/codegen/validate_imported_protos.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/validate_imported_protos.py`
- sha256: `e25ee0d50696503a3fa186babd8a2b2385d0c9aeb06369b0e82cec3b2b532613`
- bytes: 2724

````python
"""Script validating that any imported proto file matches its corresponding generated one.

Expects import path as source/codegen/metadata and generated folder path.

Background:
All MI driver metadata is being imported from hapigen. We're also creating .proto files
based on the metadata in that component. So when an MI driver is updated, the export will have
a metadata folder with [attributes.py, config.py, enums.py, functions.py, <driver-name>.proto].
Someone will import those five files to grpc-device's source/codegen/metadata folder.

Purpose:
Since, at the moment, we have both grpc-device and hapigen generating the driver .proto files
we want a way to validate that they're creating equivalent ones. This script will check imported
.proto files (copied out of hapigen-based driver exports) against their corresponding .proto file
that gets generated in grpc-device to make sure they match.

On Mismatch:
1. Make sure .proto from driver export is copied over to grpc-device
2. Make sure you built grpc-device locally to get any generated folder changes
   (specifically .proto files there)
3. The proto generators (mako and helper python files) likely changed between grpc-device and
   hapigen and need to be synced up.
"""

import filecmp
import glob
import os
import sys

import click


@click.command()
@click.option("--imported", "-i", help="Directory where imported .proto files reside")
@click.option("--generated", "-g", help="Directory where generated .proto files reside")
def _check_mismatched_protos(imported: str, generated: str):
    any_mismatches = False
    file_paths = glob.glob(f"{imported}/**/*.proto", recursive=True)
    for file_path in file_paths:
        driver_dir_name = os.path.split(os.path.split(file_path)[0])[1]
        file_name = os.path.basename(file_path)
        driver_and_file_path = f"{driver_dir_name}/{file_name}"
        generated_file_path = f"{generated}/{driver_and_file_path}"
        compare_result = filecmp.cmp(file_path, generated_file_path)
        if compare_result:
            print(
                f"[PASS] {f'{imported}/{driver_and_file_path}'} matched {f'{generated}/{driver_and_file_path}.'}"
            )
        else:
            any_mismatches = True
            print(
                f"[FAIL] {f'{imported}/{driver_and_file_path}'} did not match {f'{generated}/{driver_and_file_path}'}"
            )
    if any_mismatches:
        print("\nFail: Some imported proto files didn't match the generated ones.")
        sys.exit(1)
    else:
        print("\nSuccess: All the imported proto files matched the generated ones.")


if __name__ == "__main__":
    _check_mismatched_protos()
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/validate_linux_rt.py sha256=76355cef61fc887ddb79a82f32be15953acd92cf7aab3409ce5624d81aaf7165 bytes=4053 -->
## FILE: source/codegen/validate_linux_rt.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/validate_linux_rt.py`
- sha256: `76355cef61fc887ddb79a82f32be15953acd92cf7aab3409ce5624d81aaf7165`
- bytes: 4053

````python
"""Script for validating if a set of changed files warrants updating the Linux RT Feed.

Expects output of git diff --name-only <last-release-commit> <current-commit>
to be piped in so it can be read from sys.stdin
"""

import argparse
import fnmatch
import os
import sys
from pprint import pprint
from typing import Set

from template_helpers import load_metadata


def _get_codegen_changes(changed_files: Set[str]) -> Set[str]:
    return set(fnmatch.filter(changed_files, "source/codegen/*"))


def _get_test_changes(changed_files: Set[str]) -> Set[str]:
    return set(fnmatch.filter(changed_files, "source/tests/*"))


def _get_import_changes(changed_files: Set[str]) -> Set[str]:
    return set(fnmatch.filter(changed_files, "imports/*"))


def _get_markdown_changes(changed_files: Set[str]) -> Set[str]:
    return set(fnmatch.filter(changed_files, "*.md"))


def _get_non_rt_driver_changes(driver_name: str, changed_files: Set[str]) -> Set[str]:
    files_affecting_linux_rt = [
        f"generated/{driver_name}/*",
        f"examples/{driver_name}/*",
        f"source/custom/{driver_name}*",
    ]
    non_rt_driver_changes = set()

    for pattern in files_affecting_linux_rt:
        non_rt_driver_changes |= set(fnmatch.filter(changed_files, pattern))
    return non_rt_driver_changes


def _need_linux_rt_feed_update(metadata_dir: str, changed_files: Set[str]) -> bool:
    codegen_changes = _get_codegen_changes(changed_files)
    _print_changed_files("Codegen changes not affecting RT:", codegen_changes)
    remaining_changes = changed_files - codegen_changes
    test_changes = _get_test_changes(remaining_changes)
    _print_changed_files("Test related changes not affecting RT:", test_changes)
    remaining_changes -= test_changes
    import_changes = _get_import_changes(remaining_changes)
    _print_changed_files("Import related changes not affecting RT:", import_changes)
    remaining_changes -= import_changes
    markdown_changes = _get_markdown_changes(remaining_changes)
    _print_changed_files("Markdown changes not affecting RT:", markdown_changes)
    remaining_changes -= markdown_changes

    non_rt_drivers = [
        driver
        for driver in os.listdir(metadata_dir)
        if os.path.isdir(os.path.join(metadata_dir, driver))
        and not load_metadata(f"{metadata_dir}/{driver}/")["config"].get("linux_rt_support", False)
    ]
    non_rt_driver_changes = set()
    for non_rt_driver in non_rt_drivers:
        non_rt_driver_changes |= _get_non_rt_driver_changes(non_rt_driver, remaining_changes)
    _print_changed_files("Changes related to drivers not supported on RT:", non_rt_driver_changes)
    remaining_changes = remaining_changes - non_rt_driver_changes
    if non_rt_driver_changes and remaining_changes == {"source/CMakeLists.txt"}:
        return False
    if len(remaining_changes) > 0:
        _print_changed_files("Remaining changes likely affecting RT:", remaining_changes)
        return True
    return False


def _print_changed_files(title: str, changed_files: Set[str]):
    print(f"\n{title}\n")
    pprint(changed_files)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Check if any file has changed that affects the Linux RT Feed."
    )
    parser.add_argument(
        "metadata",
        help="The path to the directory containing all of the metadata.",
    )
    args = parser.parse_args()
    changed_files = set()
    for line in sys.stdin:
        changed_files.add(line.strip())
    env_file = os.getenv("GITHUB_ENV")
    update_linux_rt = False
    if _need_linux_rt_feed_update(args.metadata, changed_files):
        print("\nLinux RT's grpc-device dependency needs updating.")
        update_linux_rt = True
    else:
        print("\nLinux RT's grpc-device dependency doesn't need updating.")
    if env_file:
        with open(env_file, "a") as myfile:
            myfile.write(f"SHOULD_UPDATE_LINUX_RT={update_linux_rt}")
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/config/insecure_config.json sha256=a3eba6ee70821c78f1d05112d44fdb89a8c74cf76455c777f18b460d6ae970bc bytes=145 -->
## FILE: source/config/insecure_config.json

- repository: `ni/grpc-device`
- source_path: `source/config/insecure_config.json`
- sha256: `a3eba6ee70821c78f1d05112d44fdb89a8c74cf76455c777f18b460d6ae970bc`
- bytes: 145

````json
{
   "address": "[::]",
   "port": 31763,
   "security" : {
      "server_cert": "",
      "server_key": "",
      "root_cert": ""
   }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/config/localhost_config.json sha256=9a8f9fb98c948fa6c4f6ebaae6203f0dd71979b5ee2e40292077d226aa460a8f bytes=217 -->
## FILE: source/config/localhost_config.json

- repository: `ni/grpc-device`
- source_path: `source/config/localhost_config.json`
- sha256: `9a8f9fb98c948fa6c4f6ebaae6203f0dd71979b5ee2e40292077d226aa460a8f`
- bytes: 217

````json
{
    "address": "[::1]",
    "port": 31763,
    "sideband_address": "[::1]",
    "sideband_port": 50055,
    "security" : {
       "server_cert": "",
       "server_key": "",
       "root_cert": ""
    }
 }
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/config/mutual_tls.json sha256=a6d752c1151e2d89fec8a92509ca8beda92f4a12c782e5c20625b02c11c6ae66 bytes=219 -->
## FILE: source/config/mutual_tls.json

- repository: `ni/grpc-device`
- source_path: `source/config/mutual_tls.json`
- sha256: `a6d752c1151e2d89fec8a92509ca8beda92f4a12c782e5c20625b02c11c6ae66`
- bytes: 219

````json
{
   "address": "[::]" ,
   "port": 31763,
   "security" : {
      "server_cert": "server_self_signed_crt.pem",
      "server_key": "server_privatekey.pem",
      "root_cert": "client_self_signed_crt.pem"
   }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/config/ni-grpc-device.client.caps.yml sha256=184ded14e25253c9bcb72578443b7e3a98f679c6df92e2ba6225d2e6d5382981 bytes=1000 -->
## FILE: source/config/ni-grpc-device.client.caps.yml

- repository: `ni/grpc-device`
- source_path: `source/config/ni-grpc-device.client.caps.yml`
- sha256: `184ded14e25253c9bcb72578443b7e3a98f679c6df92e2ba6225d2e6d5382981`
- bytes: 1000

````yaml
# Capabilities declaration for ni-grpc-device client TLS support.
# This file informs ni-tls-config what TLS features the ni-grpc-device client supports.
#
# supports_server_mode_disabled: Whether client supports server_mode: Disabled
# supports_server_mode_trust_always: Whether client supports a trust-all mode
#
# supports_certificate_chain_file_scheme: Whether file:// URI scheme is supported for certs
# supports_certificate_key_file_scheme: Whether file:// URI scheme is supported for keys
# supports_trusted_certificates_file_scheme: Whether file:// URI scheme is supported for trusted certs
# supports_trusted_certificates_directory_scheme: Whether directory:// URI scheme is supported for trusted certs
#
supports_server_mode_disabled: true
supports_server_mode_trust_always: false

supports_certificate_chain_file_scheme: true
supports_certificate_key_file_scheme: true
supports_trusted_certificates_file_scheme: true
supports_trusted_certificates_directory_scheme: false
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/config/ni-grpc-device.client.defaults.yml sha256=5e7f905021e3fd01d7ea20ffdf391856ad08c12bde341336c4601b8d56eb4703 bytes=1456 -->
## FILE: source/config/ni-grpc-device.client.defaults.yml

- repository: `ni/grpc-device`
- source_path: `source/config/ni-grpc-device.client.defaults.yml`
- sha256: `5e7f905021e3fd01d7ea20ffdf391856ad08c12bde341336c4601b8d56eb4703`
- bytes: 1456

````yaml
file_version: 1
# Client-side TLS configuration defaults for ni-grpc-device.
#
# certificate_mode: Disabled (default) | Managed | Unmanaged
#   Disabled: Client does not use TLS certificates.
#   Managed: Client uses certificates managed by ni-tls-config.
#   Unmanaged: Client uses manually-provided certificate_chain and certificate_key paths.
#
# certificate_chain: Path to client certificate chain file (PEM format).
#   URI schemes supported: file://
#   Substitution variables: $(UserServicesDir), $(Service)
#
# certificate_key: Path to client private key file (PEM format).
#   URI schemes supported: file://
#   Substitution variables: $(UserServicesDir), $(Service)
#
# server_mode: Disabled (default) | TrustedCertificates | SkipHostnameValidation
#   Disabled: Client does not validate server certificates.
#   TrustedCertificates: Client validates server certificates against trusted_certificates.
#   SkipHostnameValidation: Client validates certificate but skips hostname verification.
#
# trusted_certificates: Default trust store for validating server certificates.
#   SystemDefault: Use system-default CA certificates.
#   To use specific certificates, override in known_servers.yml per-server.
#
certificate_mode: Disabled
certificate_chain: file://$(UserServicesDir)/$(Service)/cert.pem
certificate_key: file://$(UserServicesDir)/$(Service)/key.pem
server_mode: Disabled
trusted_certificates: SystemDefault
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/config/ni-grpc-device.server.caps.yml sha256=e7d9cd02557145b74fc5330181147cef3b8073988836ab2b084a0875e3473aaf bytes=1341 -->
## FILE: source/config/ni-grpc-device.server.caps.yml

- repository: `ni/grpc-device`
- source_path: `source/config/ni-grpc-device.server.caps.yml`
- sha256: `e7d9cd02557145b74fc5330181147cef3b8073988836ab2b084a0875e3473aaf`
- bytes: 1341

````yaml
# Capabilities declaration for ni-grpc-device server TLS support.
# This file informs ni-tls-config what TLS features the ni-grpc-device server supports.
# Read-only; do not edit manually.
#
# supports_certificate_mode_disabled: Whether server supports certificate_mode: Disabled
# supports_client_mode_disabled: Whether server supports client_mode: Disabled
# update_certificate_chain_without_restart: Whether cert changes apply without server restart
# update_trusted_certificates_without_restart: Whether trusted cert changes apply without restart
#
# supports_certificate_chain_file_scheme: Whether file:// URI scheme is supported for certs
# supports_certificate_key_file_scheme: Whether file:// URI scheme is supported for keys
# supports_trusted_certificates_file_scheme: Whether file:// URI scheme is supported for trusted certs
# supports_trusted_certificates_directory_scheme: Whether directory:// URI scheme is supported for trusted certs
#
supports_certificate_mode_disabled: true
supports_client_mode_disabled: true
update_certificate_chain_without_restart: false
update_trusted_certificates_without_restart: false

supports_certificate_chain_file_scheme: true
supports_certificate_key_file_scheme: true
supports_trusted_certificates_file_scheme: true
supports_trusted_certificates_directory_scheme: true
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/config/ni-grpc-device.server.conf.yml sha256=14284001f475f45ed8d64b52a2ccaedebf27a55fac2da539918ad45d10ade2f9 bytes=1621 -->
## FILE: source/config/ni-grpc-device.server.conf.yml

- repository: `ni/grpc-device`
- source_path: `source/config/ni-grpc-device.server.conf.yml`
- sha256: `14284001f475f45ed8d64b52a2ccaedebf27a55fac2da539918ad45d10ade2f9`
- bytes: 1621

````yaml
file_version: 1
# Server-side TLS configuration for ni-grpc-device.
#
# certificate_mode: Disabled (default) | ManagedSelfSigned | Unmanaged
#   Disabled: Server does not use TLS.
#   ManagedSelfSigned: Server uses self-signed certificates managed by ni-tls-config.
#   Unmanaged: Server uses manually-provided certificate_chain and certificate_key paths.
#
# certificate_chain: Path to server certificate chain file (PEM format).
#   URI schemes supported: file://, directory://
#   Substitution variables: $(SystemServicesDir), $(Service)
#
# certificate_key: Path to server private key file (PEM format).
#   URI schemes supported: file://
#   Substitution variables: $(SystemServicesDir), $(Service)
#
# client_mode: Disabled (default) | ManagedSelfSigned | Optional | Required
#   Disabled: Server does not request client certificates.
#   ManagedSelfSigned: Server requests and validates client certificates (self-signed).
#   Optional: Server requests but does not require valid client certificates.
#   Required: Server requires valid client certificates.
#
# trusted_certificates: Path to directory or file containing client certificates to trust.
#   URI schemes supported: file://, directory://
#   directory://: Server loads all .pem files in the directory.
#   Substitution variables: $(SystemServicesDir), $(Service)
#
certificate_mode: Disabled
certificate_chain: file://$(SystemServicesDir)/$(Service)/cert.pem
certificate_key: file://$(SystemServicesDir)/$(Service)/key.pem
client_mode: Disabled
trusted_certificates: directory://$(SystemServicesDir)/$(Service)/trusted.d
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/config/ni_tls_config.json sha256=b06b17572babf7aeb69f7ac93904a5c2b49fec60cc88896f95de5f522aebd4bf bytes=142 -->
## FILE: source/config/ni_tls_config.json

- repository: `ni/grpc-device`
- source_path: `source/config/ni_tls_config.json`
- sha256: `b06b17572babf7aeb69f7ac93904a5c2b49fec60cc88896f95de5f522aebd4bf`
- bytes: 142

````json
{
   "address": "[::]" ,
   "port": 31763,
   "security": "ni-tls-config",
   "feature_toggles": {
      "ni-tls-config": true
   }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/config/server_nitlsconfig.json sha256=fcddc87aef786b9a7ed93dbf415e2a2c02e821d5d33e6af94a4c5d5c4e575c56 bytes=123 -->
## FILE: source/config/server_nitlsconfig.json

- repository: `ni/grpc-device`
- source_path: `source/config/server_nitlsconfig.json`
- sha256: `fcddc87aef786b9a7ed93dbf415e2a2c02e821d5d33e6af94a4c5d5c4e575c56`
- bytes: 123

````json
{
    "port": 31763,
    "security" : "ni-tls-config",
    "feature_toggles": {
        "ni-tls-config": true
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/config/server_side_tls.json sha256=0587049a88066325378c4ae7016a0b569db5aee822c4c5527c5a556956c5074c bytes=193 -->
## FILE: source/config/server_side_tls.json

- repository: `ni/grpc-device`
- source_path: `source/config/server_side_tls.json`
- sha256: `0587049a88066325378c4ae7016a0b569db5aee822c4c5527c5a556956c5074c`
- bytes: 193

````json
{
   "address": "[::]" ,
   "port": 31763,
   "security" : {
      "server_cert": "server_self_signed_crt.pem",
      "server_key": "server_privatekey.pem",
      "root_cert": ""
   }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/ivi_errors.h sha256=9411d8c64a5405156b6617db99315221623e7b87cb36ca5eb10a30b5c1c53ab6 bytes=831 -->
## FILE: source/custom/ivi_errors.h

- repository: `ni/grpc-device`
- source_path: `source/custom/ivi_errors.h`
- sha256: `9411d8c64a5405156b6617db99315221623e7b87cb36ca5eb10a30b5c1c53ab6`
- bytes: 831

````c
#ifndef NIDEVICE_GRPC_DEVICE_IVI_ERRORS_H
#define NIDEVICE_GRPC_DEVICE_IVI_ERRORS_H
#include <vector>

#include "IviVisaType.h"

template <typename TLibraryPtr>
std::string get_last_error_message(TLibraryPtr& library)
{
  std::vector<char> error_message;
  ViStatus error_code;
  // Calling with no ViSession gives us thread-local errors instead of session
  // scoped errors. This method should only be used in cases where that is correct.
  constexpr auto INVALID_SESSION = static_cast<ViSession>(0UL);
  const auto buffer_size = library->GetError(INVALID_SESSION, &error_code, 0, nullptr);
  error_message.resize(buffer_size);
  library->GetError(INVALID_SESSION, &error_code, buffer_size, error_message.data());

  return std::string(error_message.data());
}

#endif  // NIDEVICE_GRPC_DEVICE_IVI_ERRORS_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nidaqmx_service.custom.cpp sha256=504d4f8d4d3f86ddfa87a3d0719423f7fa240ce37aae1a8a3288febdafb223d8 bytes=20324 -->
## FILE: source/custom/nidaqmx_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nidaqmx_service.custom.cpp`
- sha256: `504d4f8d4d3f86ddfa87a3d0719423f7fa240ce37aae1a8a3288febdafb223d8`
- bytes: 20324

````cpp
#include <nidaqmx/nidaqmx_service.h>
#include <vector>
#include <memory>
#include <cstdint>
#include <cstring>
#include <server/converters.h>
#include "NIDAQmxInternalWaveform.h"
#include <google/protobuf/descriptor.h>

namespace nidaqmx_grpc {

using nidevice_grpc::converters::convert_to_grpc;
using nidevice_grpc::converters::convert_dot_net_ticks_to_precision_timestamp;
using nidevice_grpc::converters::DotNetTicksPerSecond;
using google::protobuf::RepeatedPtrField;
using ::ni::protobuf::types::DoubleAnalogWaveform;
using ::ni::protobuf::types::DigitalWaveform;

namespace {

constexpr int32 READ_ALL_AVAILABLE = -1;

// Returns true if it's safe to use outputs of a method with the given status.
inline bool status_ok(int32 status)
{
  return status >= 0;
}

// Encapsulates timing arrays and pointers for waveform operations
struct TimingData {
  std::vector<int64> t0_array;
  std::vector<int64> dt_array;
  int64* t0_ptr = nullptr;
  int64* dt_ptr = nullptr;
  uInt32 timing_array_size = 0;

  TimingData(uInt32 num_channels) {
    if (num_channels == 0) {
      return;
    }
    t0_array.resize(num_channels, 0);
    dt_array.resize(num_channels, 0);
    t0_ptr = t0_array.data();
    dt_ptr = dt_array.data();
    timing_array_size = num_channels;
  }
};

// Universal callback function for setting waveform attributes (both analog and digital)
template<typename WaveformCollectionType>
int32 CVICALLBACK SetWfmAttrCallback(
    const uInt32 channel_index,
    const char attribute_name[],
    const int32 attribute_type,
    const void* value,
    const uInt32 value_size_in_bytes,
    void* callback_data)
{
  try {
    auto* waveforms = static_cast<WaveformCollectionType*>(callback_data);
    if (!waveforms || channel_index >= static_cast<uInt32>(waveforms->size())) {
      return -1;
    }

    auto* waveform = waveforms->Mutable(channel_index);
    if (!waveform) {
      return -1;
    }

    auto* attributes = waveform->mutable_attributes();
    ::ni::protobuf::types::WaveformAttributeValue attr_value;
    
    switch (attribute_type) {
      case DAQmx_Val_WfmAttrType_Bool32:
        if (value_size_in_bytes == sizeof(int32)) {
          const bool bool_val = (*static_cast<const int32*>(value)) != 0;
          attr_value.set_bool_value(bool_val);
        } else {
          return -1;
        }
        break;
        
      case DAQmx_Val_WfmAttrType_Float64:
        if (value_size_in_bytes == sizeof(double)) {
          const double double_val = *static_cast<const double*>(value);
          attr_value.set_double_value(double_val);
        } else {
          return -1;
        }
        break;
        
      case DAQmx_Val_WfmAttrType_Int32:
        if (value_size_in_bytes == sizeof(int32)) {
          const int32 int_val = *static_cast<const int32*>(value);
          attr_value.set_integer_value(int_val);
        } else {
          return -1;
        }
        break;
        
      case DAQmx_Val_WfmAttrType_String:
        if (value_size_in_bytes > 0) {
          const char* str_val = static_cast<const char*>(value);
          std::string string_val;
          convert_to_grpc(std::string(str_val), &string_val);
          attr_value.set_string_value(string_val);
        } else {
          return -1;
        }
        break;
        
      default:
        return -1;
    }
    
    (*attributes)[attribute_name] = attr_value;
    return 0;
  }
  catch (const std::exception&) {
    return -1;
  }
}

template<typename RequestType>
int32 GetWaveformAttributeMode(const RequestType* request)
{
  switch (request->waveform_attribute_mode_enum_case()) {
    case RequestType::WaveformAttributeModeEnumCase::kWaveformAttributeMode: {
      return static_cast<int32>(request->waveform_attribute_mode());
    }
    case RequestType::WaveformAttributeModeEnumCase::kWaveformAttributeModeRaw: {
      return static_cast<int32>(request->waveform_attribute_mode_raw());
    }
    case RequestType::WaveformAttributeModeEnumCase::WAVEFORM_ATTRIBUTE_MODE_ENUM_NOT_SET: {
      return 0;
    }
  }
  return 0;
}

template<typename WaveformType>
void SetWaveformTiming(
    uInt32 channel_index,
    const TimingData& timing_data,
    WaveformType* waveform)
{
  auto* waveform_t0 = waveform->mutable_t0();
  convert_dot_net_ticks_to_precision_timestamp(timing_data.t0_array[channel_index], waveform_t0);
  waveform->set_dt(static_cast<double>(timing_data.dt_array[channel_index]) / DotNetTicksPerSecond);
}

} // anonymous namespace

bool NiDAQmxService::IsInternalAttribute(int32 attribute, const google::protobuf::EnumDescriptor* attribute_enum_descriptor)
{
  return attribute == DAQmx_DefaultNumberOfSamplesToRead && 
         attribute_enum_descriptor == nidaqmx_grpc::ReadUInt32Attribute_descriptor();
}

::grpc::Status NiDAQmxService::ConvertApiErrorStatusForTaskHandle(::grpc::ServerContextBase* context, int32_t status, TaskHandle task)
{
  // This implementation assumes this method is always called on the same thread where the error occurred.
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  library_->GetExtendedErrorInfo(&description[0], nidevice_grpc::kMaxGrpcErrorDescriptionSize);
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

::grpc::Status NiDAQmxService::ReadAnalogWaveforms(::grpc::ServerContext* context, const ReadAnalogWaveformsRequest* request, ReadAnalogWaveformsResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto task_grpc_session = request->task();
    TaskHandle task = session_repository_->access_session(task_grpc_session.name());

    auto number_of_samples_per_channel = request->num_samps_per_chan();
    const auto timeout = request->timeout();
    
    uInt32 num_channels = 0;
    auto status = library_->GetReadAttributeUInt32(task, ReadUInt32Attribute::READ_ATTRIBUTE_NUM_CHANS, &num_channels);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForTaskHandle(context, status, task);
    }

    if (num_channels == 0) {
      return ::grpc::Status(::grpc::INVALID_ARGUMENT, "No channels to read");
    }

    if (number_of_samples_per_channel == READ_ALL_AVAILABLE) {
      uInt32 default_number = 0;
      status = library_->GetReadAttributeUInt32(task, DAQmx_DefaultNumberOfSamplesToRead, &default_number);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForTaskHandle(context, status, task);
      }
      number_of_samples_per_channel = static_cast<int32>(default_number);
    }

    std::vector<std::vector<float64>> read_arrays(num_channels);
    std::vector<float64*> read_array_ptrs(num_channels);
    
    const uInt32 size = (number_of_samples_per_channel > 0) ? number_of_samples_per_channel : 1;
    for (uInt32 i = 0; i < num_channels; ++i) {
      read_arrays[i].resize(size);
      read_array_ptrs[i] = read_arrays[i].data();
    }

    response->mutable_waveforms()->Reserve(num_channels);
    for (uInt32 i = 0; i < num_channels; ++i) {
      response->add_waveforms();
    }
    
    int32 waveform_attribute_mode = GetWaveformAttributeMode(request);
    const bool timing_enabled = (waveform_attribute_mode & WaveformAttributeMode::WAVEFORM_ATTRIBUTE_MODE_TIMING) != 0;
    const bool extended_properties_enabled = (waveform_attribute_mode & WaveformAttributeMode::WAVEFORM_ATTRIBUTE_MODE_EXTENDED_PROPERTIES) != 0;

    TimingData timing_data(timing_enabled ? num_channels : 0);

    DAQmxSetWfmAttrCallbackPtr callback_ptr = nullptr;
    if (extended_properties_enabled) {
      callback_ptr = &SetWfmAttrCallback<RepeatedPtrField<DoubleAnalogWaveform>>;
    }

    int32 samples_per_chan_read = 0;
    status = library_->InternalReadAnalogWaveformPerChan(
        task,
        number_of_samples_per_channel,
        timeout,
        timing_data.t0_array.data(),
        timing_data.dt_array.data(),
        timing_data.timing_array_size,
        callback_ptr,
        response->mutable_waveforms(),
        read_array_ptrs.data(),
        num_channels,
        number_of_samples_per_channel,
        &samples_per_chan_read,
        nullptr
    );

    context->AddTrailingMetadata("ni-samps-per-chan-read", std::to_string(samples_per_chan_read));
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForTaskHandle(context, status, task);
    }

    for (uInt32 channel = 0; channel < num_channels; ++channel) {
      auto* waveform = response->mutable_waveforms(channel);

      auto* y_data = waveform->mutable_y_data();
      y_data->Add(read_arrays[channel].data(), read_arrays[channel].data() + samples_per_chan_read);

      if (timing_enabled) {
        SetWaveformTiming(channel, timing_data, waveform);
      }
    }

    response->set_samps_per_chan_read(samples_per_chan_read);
    response->set_status(status);
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

::grpc::Status NiDAQmxService::ReadDigitalWaveforms(::grpc::ServerContext* context, const ReadDigitalWaveformsRequest* request, ReadDigitalWaveformsResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto task_grpc_session = request->task();
    TaskHandle task = session_repository_->access_session(task_grpc_session.name());

    auto number_of_samples_per_channel = request->num_samps_per_chan();
    const auto timeout = request->timeout();
    
    uInt32 num_channels = 0;
    auto status = library_->GetReadAttributeUInt32(task, ReadUInt32Attribute::READ_ATTRIBUTE_NUM_CHANS, &num_channels);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForTaskHandle(context, status, task);
    }

    if (num_channels == 0) {
      return ::grpc::Status(::grpc::INVALID_ARGUMENT, "No channels to read");
    }

    if (number_of_samples_per_channel == READ_ALL_AVAILABLE) {
      uInt32 default_number = 0;
      status = library_->GetReadAttributeUInt32(task, DAQmx_DefaultNumberOfSamplesToRead, &default_number);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForTaskHandle(context, status, task);
      }
      number_of_samples_per_channel = static_cast<int32>(default_number);
    }

    // Get the maximum number of lines per channel to calculate array size
    uInt32 max_bytes_per_chan = 0;
    status = library_->GetReadAttributeUInt32(task, ReadUInt32Attribute::READ_ATTRIBUTE_DIGITAL_LINES_BYTES_PER_CHAN, &max_bytes_per_chan);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForTaskHandle(context, status, task);
    }

    if (max_bytes_per_chan == 0) {
      return ::grpc::Status(::grpc::UNKNOWN, "Digital lines bytes per channel is 0");
    }

    // Calculate total array size needed (samples * channels * max_bytes_per_chan)
    const uInt32 num_samples = (number_of_samples_per_channel > 0) ? number_of_samples_per_channel : 1;
    const uInt32 array_size = num_samples * num_channels * max_bytes_per_chan;
    std::vector<uInt8> read_array(array_size);

    response->mutable_waveforms()->Reserve(num_channels);
    for (uInt32 i = 0; i < num_channels; ++i) {
      response->add_waveforms();
    }
    
    int32 waveform_attribute_mode = GetWaveformAttributeMode(request);
    const bool timing_enabled = (waveform_attribute_mode & WaveformAttributeMode::WAVEFORM_ATTRIBUTE_MODE_TIMING) != 0;
    const bool extended_properties_enabled = (waveform_attribute_mode & WaveformAttributeMode::WAVEFORM_ATTRIBUTE_MODE_EXTENDED_PROPERTIES) != 0;

    TimingData timing_data(timing_enabled ? num_channels : 0);

    DAQmxSetWfmAttrCallbackPtr callback_ptr = nullptr;
    if (extended_properties_enabled) {
      callback_ptr = &SetWfmAttrCallback<RepeatedPtrField<DigitalWaveform>>;
    }

    std::vector<uInt32> bytes_per_chan_array(num_channels);
    
    int32 samples_per_chan_read = 0;
    int32 num_bytes_per_samp = 0;
    status = library_->InternalReadDigitalWaveform(
        task,
        number_of_samples_per_channel,
        timeout,
        GROUP_BY_GROUP_BY_SCAN_NUMBER,
        timing_data.t0_array.data(),
        timing_data.dt_array.data(),
        timing_data.timing_array_size,
        callback_ptr,
        response->mutable_waveforms(),
        read_array.data(),
        array_size,
        &samples_per_chan_read,
        &num_bytes_per_samp,
        bytes_per_chan_array.data(),
        num_channels,
        nullptr
    );

    context->AddTrailingMetadata("ni-samps-per-chan-read", std::to_string(samples_per_chan_read));
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForTaskHandle(context, status, task);
    }

    for (uInt32 channel = 0; channel < num_channels; ++channel) {
      auto* waveform = response->mutable_waveforms(channel);

      const uInt32 bytes_per_chan = bytes_per_chan_array[channel];
      waveform->set_signal_count(static_cast<int32>(bytes_per_chan));

      auto* y_data = waveform->mutable_y_data();
      y_data->reserve(samples_per_chan_read * bytes_per_chan);
      
      // Data layout: grouped by scan number (interleaved)
      // Sample 0: Channel 0 signals, Channel 1 signals, Channel 2 signals, ...
      // Sample 1: Channel 0 signals, Channel 1 signals, Channel 2 signals, ...
      // Within each channel's data in a sample, signals are sequential: Signal0, Signal1, Signal2, ...
      for (int32 sample = 0; sample < samples_per_chan_read; ++sample) {
        const uInt32 sample_start = sample * num_channels * max_bytes_per_chan;
        const uInt32 channel_offset = sample_start + channel * max_bytes_per_chan;
        y_data->append(reinterpret_cast<const char*>(&read_array[channel_offset]), bytes_per_chan);
      }

      if (timing_enabled) {
        SetWaveformTiming(channel, timing_data, waveform);
      }
    }

    response->set_samps_per_chan_read(samples_per_chan_read);
    response->set_status(status);
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

::grpc::Status NiDAQmxService::WriteAnalogWaveforms(::grpc::ServerContext* context, const WriteAnalogWaveformsRequest* request, WriteAnalogWaveformsResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    const auto task_grpc_session = request->task();
    const TaskHandle task = session_repository_->access_session(task_grpc_session.name());

    const double timeout = request->timeout();
    const bool auto_start = request->auto_start();
    const auto& waveforms = request->waveforms();

    if (waveforms.empty()) {
      return ::grpc::Status(::grpc::INVALID_ARGUMENT, "No waveforms provided");
    }

    const uInt32 num_channels = static_cast<uInt32>(waveforms.size());
    const int32 number_of_samples_per_channel = static_cast<int32>(waveforms[0].y_data().size());
    
    for (uInt32 channel_index = 0; channel_index < num_channels; ++channel_index) {
      const auto& waveform = waveforms[channel_index];
      const auto& y_data = waveform.y_data();
      
      if (static_cast<int32>(y_data.size()) != number_of_samples_per_channel) {
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The waveforms must all have the same sample count.");
      }
    }

    std::vector<const float64*> write_array_ptrs(num_channels);
    
    for (uInt32 channel_index = 0; channel_index < num_channels; ++channel_index) {
      const auto& waveform = waveforms[channel_index];
      const auto& y_data = waveform.y_data();
      write_array_ptrs[channel_index] = y_data.data();
    }

    int32 samples_per_chan_written = 0;
    auto status = library_->InternalWriteAnalogWaveformPerChan(
        task,
        number_of_samples_per_channel,
        auto_start,
        timeout,
        write_array_ptrs.data(),
        num_channels,
        &samples_per_chan_written,
        nullptr
    );

    context->AddTrailingMetadata("ni-samps-per-chan-written", std::to_string(samples_per_chan_written));
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForTaskHandle(context, status, task);
    }

    response->set_samps_per_chan_written(samples_per_chan_written);
    response->set_status(status);
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

::grpc::Status NiDAQmxService::WriteDigitalWaveforms(::grpc::ServerContext* context, const WriteDigitalWaveformsRequest* request, WriteDigitalWaveformsResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto task_grpc_session = request->task();
    TaskHandle task = session_repository_->access_session(task_grpc_session.name());

    const auto auto_start = request->auto_start();
    const auto timeout = request->timeout();
    const auto& waveforms = request->waveforms();
    
    if (waveforms.empty()) {
      return ::grpc::Status(::grpc::INVALID_ARGUMENT, "No waveforms provided");
    }

    const uInt32 num_channels = static_cast<uInt32>(waveforms.size());
    const int32 number_of_samples_per_channel = static_cast<int32>(waveforms[0].y_data().size() / waveforms[0].signal_count());

    uInt32 max_bytes_per_chan = 0;
    for (const auto& waveform : waveforms) {
      const auto signal_count = waveform.signal_count();
      max_bytes_per_chan = std::max(max_bytes_per_chan, static_cast<uInt32>(signal_count));
    }

    std::vector<uInt32> bytes_per_chan_array(num_channels);
    for (uInt32 channel = 0; channel < num_channels; ++channel) {
      const auto& waveform = waveforms[channel];
      const auto signal_count = waveform.signal_count();
      const auto& y_data = waveform.y_data();
      
      if (y_data.size() != number_of_samples_per_channel * signal_count) {
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The waveforms must all have the same sample count.");
      }
      
      bytes_per_chan_array[channel] = static_cast<uInt32>(signal_count);
    }

    const uInt32 array_size = number_of_samples_per_channel * num_channels * max_bytes_per_chan;
    std::vector<uInt8> write_array(array_size, 0);

    for (uInt32 channel = 0; channel < num_channels; ++channel) {
      const auto& waveform = waveforms[channel];
      const auto signal_count = waveform.signal_count();
      const auto& y_data = waveform.y_data();

      // Data layout: grouped by scan number (interleaved)
      // Sample 0: Channel 0 signals, Channel 1 signals, Channel 2 signals, ...
      // Sample 1: Channel 0 signals, Channel 1 signals, Channel 2 signals, ...
      // Within each channel's data in a sample, signals are sequential: Signal0, Signal1, Signal2, ...
      for (int32 sample = 0; sample < number_of_samples_per_channel; ++sample) {
        const uInt32 dest_index = sample * num_channels * max_bytes_per_chan + channel * max_bytes_per_chan;
        const uInt32 src_index = sample * signal_count;
        std::memcpy(&write_array[dest_index], &y_data[src_index], signal_count);
      }
    }

    int32 samples_per_chan_written = 0;
    auto status = library_->InternalWriteDigitalWaveform(
        task,
        number_of_samples_per_channel,
        auto_start,
        timeout,
        GROUP_BY_GROUP_BY_SCAN_NUMBER,
        write_array.data(),
        bytes_per_chan_array.data(),
        num_channels,
        &samples_per_chan_written,
        nullptr
    );

    context->AddTrailingMetadata("ni-samps-per-chan-written", std::to_string(samples_per_chan_written));
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForTaskHandle(context, status, task);
    }

    response->set_samps_per_chan_written(samples_per_chan_written);
    response->set_status(status);
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

}  // namespace nidaqmx_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nidcpower_service.custom.cpp sha256=d5b5d3efa332537c6b0f6f865f06046979329b3f2f0eb2290c778576cdd02488 bytes=4908 -->
## FILE: source/custom/nidcpower_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nidcpower_service.custom.cpp`
- sha256: `d5b5d3efa332537c6b0f6f865f06046979329b3f2f0eb2290c778576cdd02488`
- bytes: 4908

````cpp
#include <nidcpower/nidcpower_service.h>

#include <stdexcept>

namespace nidcpower_grpc {
using nidevice_grpc::converters::convert_from_grpc;
using nidevice_grpc::converters::convert_to_grpc;

class DriverWarningOrErrorException : public std::runtime_error {
 private:
  int status_ = 0;

 public:
  DriverWarningOrErrorException(int status) : std::runtime_error(""), status_(status) {}
  int status() const
  {
    return status_;
  }
};

static void CheckStatus(int status)
{
  if (status != 0) {
    throw DriverWarningOrErrorException(status);
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status NiDCPowerService::MeasureMultiple(::grpc::ServerContext* context, const MeasureMultipleRequest* request, MeasureMultipleResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  ViSession vi = VI_NULL;
  try {
    auto vi_grpc_session = request->vi();
    vi = session_repository_->access_session(vi_grpc_session.name());
    auto channel_name_mbcs = convert_from_grpc<std::string>(request->channel_name());
    ViConstString channel_name = channel_name_mbcs.c_str();

    ViUInt32 number_of_channels;
    CheckStatus(library_->ParseChannelCount(vi, channel_name, &number_of_channels));
    response->mutable_voltage_measurements()->Resize(number_of_channels, 0.0);
    ViReal64* voltage_measurements = response->mutable_voltage_measurements()->mutable_data();
    response->mutable_current_measurements()->Resize(number_of_channels, 0.0);
    ViReal64* current_measurements = response->mutable_current_measurements()->mutable_data();

    auto status = library_->MeasureMultiple(vi, channel_name, voltage_measurements, current_measurements);
    if (status < VI_SUCCESS) {
      return ConvertApiErrorStatusForViSession(context, status, vi);
    }
    response->set_status(status);
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
  catch (const DriverWarningOrErrorException& ex) {
    if (ex.status() < VI_SUCCESS) {
      return ConvertApiErrorStatusForViSession(context, ex.status(), vi);
    }
    response->set_status(ex.status());
    return ::grpc::Status::OK;
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status NiDCPowerService::MeasureMultipleLCR(::grpc::ServerContext* context, const MeasureMultipleLCRRequest* request, MeasureMultipleLCRResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  ViSession vi = VI_NULL;
  try {
    auto vi_grpc_session = request->vi();
    vi = session_repository_->access_session(vi_grpc_session.name());
    auto channel_name_mbcs = convert_from_grpc<std::string>(request->channel_name());
    ViConstString channel_name = channel_name_mbcs.c_str();

    ViUInt32 number_of_channels;
    CheckStatus(library_->ParseChannelCount(vi, channel_name, &number_of_channels));
    std::vector<NILCRMeasurement_struct> measurements(number_of_channels, NILCRMeasurement_struct());

    auto status = library_->MeasureMultipleLCR(vi, channel_name, measurements.data());
    if (status < VI_SUCCESS) {
      return ConvertApiErrorStatusForViSession(context, status, vi);
    }
    response->set_status(status);
    convert_to_grpc(measurements, response->mutable_measurements());
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::LibraryLoadException& ex) {
    return ::grpc::Status(::grpc::NOT_FOUND, ex.what());
  }
  catch (const DriverWarningOrErrorException& ex) {
    if (ex.status() < VI_SUCCESS) {
      return ConvertApiErrorStatusForViSession(context, ex.status(), vi);
    }
    response->set_status(ex.status());
    return ::grpc::Status::OK;
  }
}

::grpc::Status NiDCPowerService::ConvertApiErrorStatusForViSession(::grpc::ServerContextBase* context, int32_t status, ViSession vi)
{
  static_assert(nidevice_grpc::kMaxGrpcErrorDescriptionSize >= 256, "ErrorMessage expects a minimum buffer size.");
  ViStatus error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  // Try first to get the most recent error with a dynamic message.
  library_->GetError(vi, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  if (error_code != status) {
    // Since another thread has changed the status, fall back to the static message lookup.
    description.assign(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
    library_->ErrorMessage(vi, status, &description[0]);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace nidcpower_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nidigitalpattern_service.custom.cpp sha256=69b2bb1bfed29d5473e2234c33f2697c864cfaeeb1caa02a6912a8df1c5e8551 bytes=3758 -->
## FILE: source/custom/nidigitalpattern_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nidigitalpattern_service.custom.cpp`
- sha256: `69b2bb1bfed29d5473e2234c33f2697c864cfaeeb1caa02a6912a8df1c5e8551`
- bytes: 3758

````cpp
#include <nidigitalpattern/nidigitalpattern_service.h>

namespace nidigitalpattern_grpc {
using nidevice_grpc::converters::convert_from_grpc;

const auto kErrorReadBufferTooSmall = -200229;
const auto kWarningCAPIStringTruncatedToFitBuffer = 200026;

// Returns true if it's safe to use outputs of a method with the given status.
inline bool status_ok(int32 status)
{
  return status >= 0;
}

::grpc::Status NiDigitalService::ConvertApiErrorStatusForViSession(::grpc::ServerContextBase* context, int32_t status, ViSession vi)
{
  static_assert(nidevice_grpc::kMaxGrpcErrorDescriptionSize >= 256, "ErrorMessage expects a minimum buffer size.");
  ViStatus error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  // Try first to get the most recent error with a dynamic message.
  library_->GetError(vi, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  if (error_code != status) {
    // Since another thread has changed the status, fall back to the static message lookup.
    description.assign(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
    library_->ErrorMessage(vi, status, &description[0]);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

::grpc::Status NiDigitalService::FetchCaptureWaveformU32(::grpc::ServerContext* context, const FetchCaptureWaveformU32Request* request, FetchCaptureWaveformU32Response* response)
{
  // This function is modified from the generated code to multiply the two 'ivi-dance' parameters
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto vi_grpc_session = request->vi();
    ViSession vi = session_repository_->access_session(vi_grpc_session.name());
    auto site_list_mbcs = convert_from_grpc<std::string>(request->site_list());
    auto site_list = site_list_mbcs.c_str();
    auto waveform_name_mbcs = convert_from_grpc<std::string>(request->waveform_name());
    auto waveform_name = waveform_name_mbcs.c_str();
    ViInt32 samples_to_read = request->samples_to_read();
    ViReal64 timeout = request->timeout();
    ViInt32 actual_num_waveforms{};
    ViInt32 actual_samples_per_waveform{};
    while (true) {
      auto status = library_->FetchCaptureWaveformU32(vi, site_list, waveform_name, samples_to_read, timeout, 0, nullptr, &actual_num_waveforms, &actual_samples_per_waveform);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      auto data_buffer_size = actual_num_waveforms * actual_samples_per_waveform;
      response->mutable_data()->Resize(data_buffer_size, 0);
      ViUInt32* data = reinterpret_cast<ViUInt32*>(response->mutable_data()->mutable_data());
      status = library_->FetchCaptureWaveformU32(vi, site_list, waveform_name, samples_to_read, timeout, data_buffer_size, data, &actual_num_waveforms, &actual_samples_per_waveform);
      if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
        // buffer is now too small, try again
        continue;
      }
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      data_buffer_size = actual_num_waveforms * actual_samples_per_waveform;
      response->set_status(status);
      response->mutable_data()->Resize(data_buffer_size, 0);
      response->set_actual_num_waveforms(actual_num_waveforms);
      response->set_actual_samples_per_waveform(actual_samples_per_waveform);
      return ::grpc::Status::OK;
    }
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

}  // namespace nidigitalpattern_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nidmm_restricted_service.custom.cpp sha256=a492e08e07f757c2af94541fe68e7dd26850f34ff3929f729cb2ec214d4439cd bytes=3837 -->
## FILE: source/custom/nidmm_restricted_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nidmm_restricted_service.custom.cpp`
- sha256: `a492e08e07f757c2af94541fe68e7dd26850f34ff3929f729cb2ec214d4439cd`
- bytes: 3837

````cpp
#include <nidmm_restricted/nidmm_restricted_service.h>
#include <server/converters.h>
#include "custom/ivi_errors.h"

#include <string>
#include <vector>

namespace nidmm_restricted_grpc {

using nidevice_grpc::converters::convert_from_grpc;
using nidevice_grpc::converters::convert_to_grpc;
using nidevice_grpc::converters::trim_trailing_nulls;

//---------------------------------------------------------------------
// ConvertApiErrorStatusForViSession
//---------------------------------------------------------------------
::grpc::Status NiDmmRestrictedService::ConvertApiErrorStatusForViSession(
    ::grpc::ServerContextBase* context,
    int32_t status,
    ViSession vi)
{
  ViStatus error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  // Try first to get the most recent error with a dynamic message.
  library_->GetError(vi, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  if (error_code != status) {
    // Since another thread has changed the status, fall back to the static message lookup.
    description.assign(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
    library_->GetErrorMessage(vi, status, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

//---------------------------------------------------------------------
// GetOpenSessionsInformation
//---------------------------------------------------------------------
::grpc::Status NiDmmRestrictedService::GetOpenSessionsInformation(
    ::grpc::ServerContext* context,
    const GetOpenSessionsInformationRequest* request,
    GetOpenSessionsInformationResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }

  try {
    // Convert resource name from gRPC string to native char pointer
    auto resource_name_mbcs = convert_from_grpc<std::string>(request->resource_name());
    ViRsrc resource_name = (ViRsrc)resource_name_mbcs.c_str();
    ViUInt64 buffer_size_needed_in_bytes{};

    // Local constants for NI error/warning codes
    const auto kErrorReadBufferTooSmall = -200229;
    const auto kWarningCAPIStringTruncatedToFitBuffer = 200026;

    while (true) {
      // First call to determine required buffer size with Empty string.
      // Avoid Null pointer since exception will be thrown for PAL devices.
      auto status = library_->GetOpenSessionsInformation(resource_name, (ViChar*)"", 0, &buffer_size_needed_in_bytes);
      if (status < 0) {
        return ConvertApiErrorStatusForViSession(context, status, 0);
      }

      std::string info_json;
      if (buffer_size_needed_in_bytes > 0) {
        info_json.resize(buffer_size_needed_in_bytes - 1);
      }

      auto buffer_size = buffer_size_needed_in_bytes;
      status = library_->GetOpenSessionsInformation(
          resource_name, (ViChar*)info_json.data(), buffer_size, &buffer_size_needed_in_bytes);

      if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
        // Buffer was too small, try again with new size
        continue;
      }

      if (status < 0) {
        return ConvertApiErrorStatusForViSession(context, status, 0);
      }

      response->set_status(status);
      std::string info_json_utf8;
      convert_to_grpc(info_json, &info_json_utf8);
      response->set_info_json(info_json_utf8);
      trim_trailing_nulls(*(response->mutable_info_json()));
      response->set_buffer_size_needed_in_bytes(buffer_size_needed_in_bytes);
      return ::grpc::Status::OK;
    }
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

}  // namespace nidmm_restricted_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nidmm_service.custom.cpp sha256=a5b826dcc83860c62b1097d89db0ba1d41b633e67260e404fa2145fac7254662 bytes=902 -->
## FILE: source/custom/nidmm_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nidmm_service.custom.cpp`
- sha256: `a5b826dcc83860c62b1097d89db0ba1d41b633e67260e404fa2145fac7254662`
- bytes: 902

````cpp
#include <nidmm/nidmm_service.h>

namespace nidmm_grpc {

::grpc::Status NiDmmService::ConvertApiErrorStatusForViSession(::grpc::ServerContextBase* context, int32_t status, ViSession vi)
{
  ViStatus error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  // Try first to get the most recent error with a dynamic message.
  library_->GetError(vi, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  if (error_code != status) {
    // Since another thread has changed the status, fall back to the static message lookup.
    description.assign(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
    library_->GetErrorMessage(vi, status, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace nidmm_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nifake_extension_service.custom.cpp sha256=a1e86985c05f6b0834ab3b8b6ba434bbc8e56f390ddfba10f25081076cd76cf7 bytes=458 -->
## FILE: source/custom/nifake_extension_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nifake_extension_service.custom.cpp`
- sha256: `a1e86985c05f6b0834ab3b8b6ba434bbc8e56f390ddfba10f25081076cd76cf7`
- bytes: 458

````cpp
#include <nifake_extension/nifake_extension_service.h>

namespace nifake_extension_grpc {

::grpc::Status NiFakeExtensionService::ConvertApiErrorStatusForViSession(::grpc::ServerContextBase* context, int32_t status, ViSession vi)
{
  std::string description = "In a real service, you'd look up the error message here.";
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace nifake_extension_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nifake_non_ivi_errors.h sha256=eb5fa5b5621edfa2f300d7df98b44bfc946877fc77c9eec33f36ab4b312b6f3e bytes=542 -->
## FILE: source/custom/nifake_non_ivi_errors.h

- repository: `ni/grpc-device`
- source_path: `source/custom/nifake_non_ivi_errors.h`
- sha256: `eb5fa5b5621edfa2f300d7df98b44bfc946877fc77c9eec33f36ab4b312b6f3e`
- bytes: 542

````c
#ifndef NIDEVICE_GRPC_DEVICE_NIFAKE_NON_IVI_ERRORS_H
#define NIDEVICE_GRPC_DEVICE_NIFAKE_NON_IVI_ERRORS_H

#include <vector>

template <typename TLibraryPtr>
std::string get_last_error(TLibraryPtr& library)
{
  std::vector<char> error_message;
  const auto buffer_size = library->GetLatestErrorMessage(nullptr, 0);
  error_message.resize(buffer_size);
  library->GetLatestErrorMessage(error_message.data(), buffer_size);

  return std::string(error_message.data());
}

#endif  // NIDEVICE_GRPC_DEVICE_NIFAKE_NON_IVI_ERRORS_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nifake_non_ivi_service.custom.cpp sha256=5835c74d0675b790a028d0b6c419c360fcc973cbba7470a7d4380465f018ae15 bytes=3413 -->
## FILE: source/custom/nifake_non_ivi_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nifake_non_ivi_service.custom.cpp`
- sha256: `5835c74d0675b790a028d0b6c419c360fcc973cbba7470a7d4380465f018ae15`
- bytes: 3413

````cpp
#include <nifake_non_ivi/nifake_non_ivi_service.h>
#include <server/callback_router.h>
#include <server/server_reactor.h>

#include <memory>
#include <thread>
namespace nifake_non_ivi_grpc {

::grpc::ServerWriteReactor<ReadStreamResponse>* NiFakeNonIviService::ReadStream(::grpc::CallbackServerContext* context, const ReadStreamRequest* request)
{
  // Wraps a thread to call join on destruct.
  struct AutoJoinThread {
    static std::unique_ptr<AutoJoinThread> make_auto_join(std::thread&& thread)
    {
      return std::make_unique<AutoJoinThread>(std::move(thread));
    }
    AutoJoinThread(std::thread&& thread) : thread_(std::move(thread))
    {
    }
    ~AutoJoinThread() { thread_.join(); }
    std::thread thread_;
  };

  class ReadStreamReactor : public nidevice_grpc::ServerWriterReactor<ReadStreamResponse, AutoJoinThread> {
   public:
    const int32_t MIN_VALUE = 0;
    const int32_t MAX_VALUE = 1000000;

    ReadStreamReactor(const ReadStreamRequest* request)
    {
      auto status = start(request);
      if (!status.ok()) {
        this->try_finish(std::move(status));
      }
    }

    ::grpc::Status start(const ReadStreamRequest* request) {
      if (request->start() < MIN_VALUE || request->start() > MAX_VALUE) {
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for start is out of range.");
      }
      if (request->stop() < MIN_VALUE || request->stop() > MAX_VALUE) {
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for stop is out of range.");
      }
      if (request->start() > request->stop()) {
        // This error has a different status code and an arbitrary delay for testing purposes.
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
        return ::grpc::Status(::grpc::UNKNOWN, "The values for start and stop are reversed.");
      }

      // Send initial metadata to indicate that the stream has started successfully.
      StartSendInitialMetadata();

      this->set_producer(start_thread(request->start(), request->stop()));
      return ::grpc::Status::OK;
    }

    std::unique_ptr<AutoJoinThread> start_thread(int32_t start, int32_t stop)
    {
      return AutoJoinThread::make_auto_join(std::thread([=]() {
        ReadStreamResponse response;
        for (auto i = start; i <= stop; ++i) {
          response.set_value(i);
          queue_write(response);
        }
      }));
    }
  };

  return new ReadStreamReactor(request);
}

::grpc::Status NiFakeNonIviService::ConvertApiErrorStatusForFakeHandle(::grpc::ServerContextBase* context, int32_t status, FakeHandle handle)
{
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  library_->GetLatestErrorMessage(&description[0], nidevice_grpc::kMaxGrpcErrorDescriptionSize);
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

::grpc::Status NiFakeNonIviService::ConvertApiErrorStatusForSecondarySessionHandle(::grpc::ServerContextBase* context, int32_t status, SecondarySessionHandle handle)
{
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  library_->GetLatestErrorMessage(&description[0], nidevice_grpc::kMaxGrpcErrorDescriptionSize);
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace nifake_non_ivi_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nifake_service.custom.cpp sha256=2537eb06f809d565cf695dd9fbbc62732adcb51d0da8234ac29eaad14eed0595 bytes=2766 -->
## FILE: source/custom/nifake_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nifake_service.custom.cpp`
- sha256: `2537eb06f809d565cf695dd9fbbc62732adcb51d0da8234ac29eaad14eed0595`
- bytes: 2766

````cpp

#pragma warning(push)
#pragma warning(disable : 4616)
#pragma warning(disable : 4146)
#pragma warning(disable : 4244)
#include <nifake/nifake_service.h>
#pragma warning(pop)

namespace nifake_grpc {

const auto kErrorReadBufferTooSmall = -200229;
const auto kWarningCAPIStringTruncatedToFitBuffer = 200026;

inline bool status_ok(int32_t status)
{
  return status >= 0;
}

::grpc::Status NiFakeService::ConvertApiErrorStatusForViSession(::grpc::ServerContextBase* context, int32_t status, ViSession vi)
{
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  library_->ErrorMessage(vi, status, &description[0]);
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status NiFakeService::IviDanceWithATwistCalculatedSizeOut(::grpc::ServerContext* context, const IviDanceWithATwistCalculatedSizeOutRequest* request, IviDanceWithATwistCalculatedSizeOutResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto vi_grpc_session = request->vi();
    ViSession vi = session_repository_->access_session(vi_grpc_session.name());
    ViInt32 actual_num_waveforms {};
    ViInt32 actual_samples_per_waveform {};
    while (true) {
      auto status = library_->IviDanceWithATwistCalculatedSizeOut(vi, 0, nullptr, &actual_num_waveforms, &actual_samples_per_waveform);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->mutable_data()->Resize(actual_num_waveforms, 0);
      ViUInt32* data = reinterpret_cast<ViUInt32*>(response->mutable_data()->mutable_data());
      auto data_buffer_size = actual_num_waveforms*actual_samples_per_waveform;
      status = library_->IviDanceWithATwistCalculatedSizeOut(vi, data_buffer_size, data, &actual_num_waveforms, &actual_samples_per_waveform);
      if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
        // buffer is now too small, try again
        continue;
      }
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForViSession(context, status, vi);
      }
      response->set_status(status);
      response->mutable_data()->Resize(actual_num_waveforms, 0);
      response->set_actual_num_waveforms(actual_num_waveforms);
      response->set_actual_samples_per_waveform(actual_samples_per_waveform);
      return ::grpc::Status::OK;
    }
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

}  // namespace nifake_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nifgen_service.custom.cpp sha256=37568b4af5135ddbb295627427271cb6b6347a28d5ad4495c1cfda5dbf513e86 bytes=2943 -->
## FILE: source/custom/nifgen_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nifgen_service.custom.cpp`
- sha256: `37568b4af5135ddbb295627427271cb6b6347a28d5ad4495c1cfda5dbf513e86`
- bytes: 2943

````cpp
#include <nifgen/nifgen_service.h>

#include <stdexcept>

namespace nifgen_grpc {

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status NiFgenService::CreateAdvancedArbSequence(::grpc::ServerContext* context, const CreateAdvancedArbSequenceRequest* request, CreateAdvancedArbSequenceResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto vi_grpc_session = request->vi();
    ViSession vi = session_repository_->access_session(vi_grpc_session.name());
    ViInt32 sequence_length = request->waveform_handles_array().size();
    auto waveform_handles_array = const_cast<ViInt32*>(reinterpret_cast<const ViInt32*>(request->waveform_handles_array().data()));
    auto loop_counts_array = const_cast<ViInt32*>(reinterpret_cast<const ViInt32*>(request->loop_counts_array().data()));
    auto sample_counts_array = const_cast<ViInt32*>(reinterpret_cast<const ViInt32*>(request->sample_counts_array().data()));
    auto marker_location_array = const_cast<ViInt32*>(reinterpret_cast<const ViInt32*>(request->marker_location_array().data()));

    if (marker_location_array != NULL) {
      response->mutable_coerced_markers_array()->Resize(sequence_length, 0);
    }
    ViInt32* coerced_markers_array = reinterpret_cast<ViInt32*>(response->mutable_coerced_markers_array()->mutable_data());
    ViInt32 sequence_handle{};
    auto status = library_->CreateAdvancedArbSequence(vi, sequence_length, waveform_handles_array, loop_counts_array, sample_counts_array, marker_location_array, coerced_markers_array, &sequence_handle);
    if (status < VI_SUCCESS) {
      return ConvertApiErrorStatusForViSession(context, status, vi);
    }
    response->set_status(status);
    response->set_sequence_handle(sequence_handle);
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

::grpc::Status NiFgenService::ConvertApiErrorStatusForViSession(::grpc::ServerContextBase* context, int32_t status, ViSession vi)
{
  static_assert(nidevice_grpc::kMaxGrpcErrorDescriptionSize >= 256, "ErrorMessage expects a minimum buffer size.");
  ViStatus error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  // Try first to get the most recent error with a dynamic message.
  library_->GetError(vi, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  if (error_code != status) {
    // Since another thread has changed the status, fall back to the static message lookup.
    description.assign(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
    library_->ErrorMessage(vi, status, &description[0]);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace nifgen_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nifpga_service.custom.cpp sha256=0244edefaae1172da8ae16a140c1e47696bedaf744eb75007401d1e936ebec59 bytes=458 -->
## FILE: source/custom/nifpga_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nifpga_service.custom.cpp`
- sha256: `0244edefaae1172da8ae16a140c1e47696bedaf744eb75007401d1e936ebec59`
- bytes: 458

````cpp
#include <nifpga.pb.h>
#include <nifpga/nifpga_service.h>

namespace nifpga_grpc {
::grpc::Status NiFpgaService::ConvertApiErrorStatusForNiFpga_Session(::grpc::ServerContextBase* context, int32_t status, NiFpga_Session session)
{
  // There is no function in FPGA C API to get error descriptions.
  std::string description("Error");
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}
}  // namespace nifpga_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nimxlcterminaladaptor_restricted_converters.h sha256=04b4a7e08cfea6ded12ada93eff7e5164b9f7d426a91a640606484fae85fc8e5 bytes=3482 -->
## FILE: source/custom/nimxlcterminaladaptor_restricted_converters.h

- repository: `ni/grpc-device`
- source_path: `source/custom/nimxlcterminaladaptor_restricted_converters.h`
- sha256: `04b4a7e08cfea6ded12ada93eff7e5164b9f7d426a91a640606484fae85fc8e5`
- bytes: 3482

````c
#ifndef NIDEVICE_GRPC_DEVICE_NIMXLCTERMINALADAPTOR_RESTRICTED_CONVERTERS_H
#define NIDEVICE_GRPC_DEVICE_NIMXLCTERMINALADAPTOR_RESTRICTED_CONVERTERS_H

#include "nimxlcterminaladaptor_restricted.pb.h"
#include "nimxlcterminaladaptor_restricted/nimxlcterminaladaptor_restricted_library_interface.h"
#include "server/converters.h"
#include "server/session_resource_repository.h"
#include <nierr_Status.h>

#include <algorithm>
#include <bitset>
#include <cstring>
#include <memory>

namespace nimxlcterminaladaptor_restricted_grpc {

// Add underscore to usings so they don't conflict with including files in the same namespace.
namespace pb_ = ::google::protobuf;

template <typename TServerContext>
struct NIErrStatusOutputConverter {
  NIErrStatusOutputConverter(TServerContext *serverContext)
  {
    context = serverContext;
    nierr_Status_initialize(&status);
    url_table_initialize();
  }

  ~NIErrStatusOutputConverter()
  {
    nierr_Status_jsonFree(&status);
  }

  nierr_Status* operator&()
  {
    return &status;
  }

  std::string url_encode(const char* input) const
  {
    std::string encoded(input);
    // Replace the following characters to their equivalent '%xx' hex code
    for (size_t position = 0; position < encoded.length(); ) {
      if (urlLookupTable.test(encoded[position])) {
        position++;
      }
      else {
        char character[4];
        snprintf(character, 4, "%%%2x", static_cast<int>(encoded[position]));
        encoded.replace(position, 1, character);
        position += 3;
      }
    }
    return encoded;
  }

  static const std::bitset<256> url_table_initialize()
  {
    std::bitset<256> table;
    for (int i = 'a'; i <= 'z'; i++) table.set(i);
    for (int i = 'A'; i <= 'Z'; i++) table.set(i);
    for (int i = '0'; i <= '9'; i++) table.set(i);
    table.set('-');
    table.set('_');
    table.set('.');
    table.set('~');

    return table;
  }

  void to_grpc(nimxlcterminaladaptor_restricted_grpc::NIErrStatus& output) const
  {
    output.set_code(status.code);
    if (nierr_Status_isFatal(&status))
    {
      context->AddTrailingMetadata("ni-error", std::to_string(status.code));

      if (status.json)
      {
        context->AddTrailingMetadata("ni-error-json", url_encode(status.json));
      }
    }
    else if (status.json)
    {
      output.set_json(url_encode(status.json));
    }
  }

  TServerContext *context;
  nierr_Status status{};
  static const std::bitset<256> urlLookupTable;
};

template <typename TServerContext> const std::bitset<256> NIErrStatusOutputConverter<TServerContext>::urlLookupTable = NIErrStatusOutputConverter<TServerContext>::url_table_initialize();

inline void convert_to_grpc(const NIErrStatusOutputConverter<grpc::ServerContext>& storage, nimxlcterminaladaptor_restricted_grpc::NIErrStatus* output)
{
  storage.to_grpc(*output);
}

}  // namespace nimxlcterminaladaptor_restricted_grpc

// Template specializations go in nidevice_grpc::converters.
namespace nidevice_grpc {
namespace converters {

template <>
struct TypeToStorageType<nierr_Status, nimxlcterminaladaptor_restricted_grpc::NIErrStatus> {
  using StorageType = nimxlcterminaladaptor_restricted_grpc::NIErrStatusOutputConverter<grpc::ServerContext>;
};

}  // namespace converters
}  // namespace nidevice_grpc

#endif /* NIDEVICE_GRPC_DEVICE_NIMXLCTERMINALADAPTOR_RESTRICTED_CONVERTERS_H */
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nimxlcterminaladaptor_restricted_service.custom.cpp sha256=0de62ab6803b3d25361a11d6c755bf51d3322ab6a5d6da36b0f02d27ea077124 bytes=4685 -->
## FILE: source/custom/nimxlcterminaladaptor_restricted_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nimxlcterminaladaptor_restricted_service.custom.cpp`
- sha256: `0de62ab6803b3d25361a11d6c755bf51d3322ab6a5d6da36b0f02d27ea077124`
- bytes: 4685

````cpp
#include <custom/nimxlcterminaladaptor_restricted_converters.h>
#include <nierr_Status.h>
#include <nimxlcterminaladaptor_restricted.pb.h>
#include <nimxlcterminaladaptor_restricted/nimxlcterminaladaptor_restricted_service.h>
#include <server/converters.h>

#include <iostream>
#include <map>

namespace nimxlcterminaladaptor_restricted_grpc {

using nidevice_grpc::converters::allocate_output_storage;
using nidevice_grpc::converters::convert_to_grpc;
using nimxlcterminaladaptor_restricted_grpc::NIErrStatus;

class DeviceContainerPtr {
 public:
  DeviceContainerPtr(NimxlcTerminalAdaptorRestrictedLibraryInterface* library, nimxlc_DeviceContainer container)
  {
    library_ = library;
    container_ = container;
  }

  ~DeviceContainerPtr()
  {
    library_->DeviceContainer_destroy(container_);
    container_ = nullptr;
    library_ = nullptr;
  }

  operator nimxlc_DeviceContainer*()
  {
    return &container_;
  }

 private:
  nimxlc_DeviceContainer container_;
  NimxlcTerminalAdaptorRestrictedLibraryInterface* library_;
};

class TerminalContainerPtr {
 public:
  TerminalContainerPtr(NimxlcTerminalAdaptorRestrictedLibraryInterface* library, nimxlc_TerminalContainer container)
  {
    library_ = library;
    container_ = container;
  }

  ~TerminalContainerPtr()
  {
    library_->TerminalContainer_destroy(container_);
    container_ = nullptr;
    library_ = nullptr;
  }

  operator nimxlc_TerminalContainer*()
  {
    return &container_;
  }

 private:
  nimxlc_TerminalContainer container_;
  NimxlcTerminalAdaptorRestrictedLibraryInterface* library_;
};

::grpc::Status NimxlcTerminalAdaptorRestrictedService::GetDeviceContainer(::grpc::ServerContext* context, const GetDeviceContainerRequest* request, GetDeviceContainerResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto grpc_session = request->session();
    nimxlc_Session session = session_repository_->access_session(grpc_session.name());

    auto status = allocate_output_storage<nierr_Status, NIErrStatus>(context);
    DeviceContainerPtr deviceContainerPtr(library_.get(), library_->getDeviceContainer(session, &status));
    if (nierr_Status_isNotFatal(&status)) {
      nimxlc_DeviceIterator deviceIterator = library_->DeviceContainer_begin(*deviceContainerPtr);
      while (!library_->DeviceIterator_isEnd(*deviceContainerPtr, deviceIterator) && nierr_Status_isNotFatal(&status)) {
        auto device = response->add_container_out();
        device->set_name(library_->DeviceIterator_getDeviceName(*deviceContainerPtr, deviceIterator, &status));
        device->set_supportsonboardclock(library_->DeviceIterator_supportsOnBoardClock(*deviceContainerPtr, deviceIterator, &status));

        TerminalContainerPtr terminalContainerPtr(library_.get(), library_->DeviceIterator_getTerminalContainer(*deviceContainerPtr, deviceIterator, &status));
        if (nierr_Status_isNotFatal(&status)) {
          nimxlc_TerminalIterator terminalIterator = library_->TerminalContainer_begin(*terminalContainerPtr);
          while (!library_->TerminalIterator_isEnd(*terminalContainerPtr, terminalIterator) && nierr_Status_isNotFatal(&status)) {
            auto terminal = device->add_terminals();
            terminal->set_name(library_->TerminalIterator_getTerminalName(*terminalContainerPtr, terminalIterator, &status));
            terminal->set_visibility(library_->TerminalIterator_getVisibility(*terminalContainerPtr, terminalIterator, &status));

            library_->TerminalIterator_next(&terminalIterator);
          }
        }

        library_->DeviceIterator_next(&deviceIterator);
      }
    }

    int32_t statusCode = (&status)->code;
    response->set_status(statusCode);
    convert_to_grpc(status, response->mutable_c_status());
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

::grpc::Status NimxlcTerminalAdaptorRestrictedService::ConvertApiErrorStatusForNimxlc_Session(::grpc::ServerContextBase* context, int32_t status, nimxlc_Session session)
{
  std::string description;
  auto metadata = context->client_metadata();
  auto iterator = metadata.find("ni-error");
  if (iterator != metadata.end()) {
    description = "Error " + std::string(iterator->second.data(), iterator->second.length()) + " has occurred in nimxlcTerminalAdaptor. Refer to the trailing metadata for details.";
  }

  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace nimxlcterminaladaptor_restricted_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nirfmx_errors.h sha256=872f0cd5c50a0e2115d565be265fa914f09d4126bbdaf9c977cd5a424c13f74e bytes=914 -->
## FILE: source/custom/nirfmx_errors.h

- repository: `ni/grpc-device`
- source_path: `source/custom/nirfmx_errors.h`
- sha256: `872f0cd5c50a0e2115d565be265fa914f09d4126bbdaf9c977cd5a424c13f74e`
- bytes: 914

````c
#ifndef NIDEVICE_GRPC_DEVICE_NIRFMX_ERRORS_H
#define NIDEVICE_GRPC_DEVICE_NIRFMX_ERRORS_H
#include <nirfmxinstr/nirfmxinstr_library_interface.h>  // For niRFmxInstrHandle, int32

#include <vector>

template <typename TLibraryPtr>
std::string get_last_error_message(TLibraryPtr& library)
{
  std::vector<char> error_message;
  int32 error_code;
  // Calling with no instr handle gives us thread-local errors instead of handle
  // scoped errors. This method should only be used in cases where that is correct.
  constexpr auto NO_INSTR_HANDLE = static_cast<niRFmxInstrHandle>(nullptr);
  const auto buffer_size = library->GetError(NO_INSTR_HANDLE, &error_code, 0, nullptr);
  error_message.resize(buffer_size);
  library->GetError(NO_INSTR_HANDLE, &error_code, buffer_size, error_message.data());

  return std::string(error_message.data());
}

#endif  // NIDEVICE_GRPC_DEVICE_NIRFMX_ERRORS_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nirfmxbluetooth_service.custom.cpp sha256=bf4277b49e81ee5ca96defae4b4396b50524f357e466157ce5fa4362dc7b0e66 bytes=1009 -->
## FILE: source/custom/nirfmxbluetooth_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nirfmxbluetooth_service.custom.cpp`
- sha256: `bf4277b49e81ee5ca96defae4b4396b50524f357e466157ce5fa4362dc7b0e66`
- bytes: 1009

````cpp
#include <nirfmxbluetooth/nirfmxbluetooth_service.h>

namespace nirfmxbluetooth_grpc {

::grpc::Status NiRFmxBluetoothService::ConvertApiErrorStatusForNiRFmxInstrHandle(::grpc::ServerContextBase* context, int32_t status, niRFmxInstrHandle instrumentHandle)
{
  ViStatus error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  // Try first to get the most recent error with a dynamic message.
  library_->GetError(instrumentHandle, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  if (error_code != status) {
    // Since another thread has changed the status, fall back to the static message lookup.
    description.assign(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
    library_->GetErrorString(instrumentHandle, status, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace nirfmxbluetooth_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nirfmxbluetoothgen_service.custom.cpp sha256=d1b5fba916c6c8b2e905fc5646611c443ad38ca5b52294e3a77c7c126f5e789d bytes=1421 -->
## FILE: source/custom/nirfmxbluetoothgen_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nirfmxbluetoothgen_service.custom.cpp`
- sha256: `d1b5fba916c6c8b2e905fc5646611c443ad38ca5b52294e3a77c7c126f5e789d`
- bytes: 1421

````cpp
#include <nirfmxbluetoothgen/nirfmxbluetoothgen_service.h>
#include <nirfsg/nirfsg_library.h>

namespace nirfmxbluetoothgen_grpc {

::grpc::Status NiRFmxBluetoothGenService::ConvertApiErrorStatusForNiBTSGSession(::grpc::ServerContextBase* context, int32_t status, niBTSGSession session)
{
  ViStatus error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  description.assign(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  library_->GetErrorString(session, status, &description[0], nidevice_grpc::kMaxGrpcErrorDescriptionSize);
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

::grpc::Status NiRFmxBluetoothGenService::ConvertApiErrorStatusForViSession(::grpc::ServerContextBase* context, int32_t status, ViSession RFSGHandle)
{
  auto library = std::make_shared<nirfsg_grpc::NiRFSGLibrary>();

  ViStatus error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  library->GetError(RFSGHandle, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  if (error_code != status) {
    description.assign(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
    library->ErrorMessage(RFSGHandle, status, &description[0]);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace nirfmxbluetoothgen_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nirfmxcdma2k_service.custom.cpp sha256=65d31eb98c40b72f071c5b8a59aba90e05475fe38aaa96407de2539c67768be5 bytes=994 -->
## FILE: source/custom/nirfmxcdma2k_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nirfmxcdma2k_service.custom.cpp`
- sha256: `65d31eb98c40b72f071c5b8a59aba90e05475fe38aaa96407de2539c67768be5`
- bytes: 994

````cpp
#include <nirfmxcdma2k/nirfmxcdma2k_service.h>

namespace nirfmxcdma2k_grpc {

::grpc::Status NiRFmxCDMA2kService::ConvertApiErrorStatusForNiRFmxInstrHandle(::grpc::ServerContextBase* context, int32_t status, niRFmxInstrHandle instrumentHandle)
{
  ViStatus error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  // Try first to get the most recent error with a dynamic message.
  library_->GetError(instrumentHandle, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  if (error_code != status) {
    // Since another thread has changed the status, fall back to the static message lookup.
    description.assign(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
    library_->GetErrorString(instrumentHandle, status, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace nirfmxcdma2k_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nirfmxdemod_service.custom.cpp sha256=3d0144857413204ac04e2e2f375809dc54ebd5c78d7a02d7024f923a9bc9b380 bytes=989 -->
## FILE: source/custom/nirfmxdemod_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nirfmxdemod_service.custom.cpp`
- sha256: `3d0144857413204ac04e2e2f375809dc54ebd5c78d7a02d7024f923a9bc9b380`
- bytes: 989

````cpp
#include <nirfmxdemod/nirfmxdemod_service.h>

namespace nirfmxdemod_grpc {

::grpc::Status NiRFmxDemodService::ConvertApiErrorStatusForNiRFmxInstrHandle(::grpc::ServerContextBase* context, int32_t status, niRFmxInstrHandle instrumentHandle)
{
  ViStatus error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  // Try first to get the most recent error with a dynamic message.
  library_->GetError(instrumentHandle, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  if (error_code != status) {
    // Since another thread has changed the status, fall back to the static message lookup.
    description.assign(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
    library_->GetErrorString(instrumentHandle, status, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace nirfmxdemod_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nirfmxgsm_service.custom.cpp sha256=f6e53f893c726e8bc93d6cdbca763f8ebb15735fede2efa9a2b324d88b71e165 bytes=979 -->
## FILE: source/custom/nirfmxgsm_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nirfmxgsm_service.custom.cpp`
- sha256: `f6e53f893c726e8bc93d6cdbca763f8ebb15735fede2efa9a2b324d88b71e165`
- bytes: 979

````cpp
#include <nirfmxgsm/nirfmxgsm_service.h>

namespace nirfmxgsm_grpc {

::grpc::Status NiRFmxGSMService::ConvertApiErrorStatusForNiRFmxInstrHandle(::grpc::ServerContextBase* context, int32_t status, niRFmxInstrHandle instrumentHandle)
{
  ViStatus error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  // Try first to get the most recent error with a dynamic message.
  library_->GetError(instrumentHandle, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  if (error_code != status) {
    // Since another thread has changed the status, fall back to the static message lookup.
    description.assign(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
    library_->GetErrorString(instrumentHandle, status, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace nirfmxgsm_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nirfmxinstr_restricted_service.custom.cpp sha256=535cf4b0194f7efa7108829fa1b9e55a5d0175c71e167b1503649683fd84e4df bytes=11108 -->
## FILE: source/custom/nirfmxinstr_restricted_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nirfmxinstr_restricted_service.custom.cpp`
- sha256: `535cf4b0194f7efa7108829fa1b9e55a5d0175c71e167b1503649683fd84e4df`
- bytes: 11108

````cpp
#include <nirfmxinstr_restricted/nirfmxinstr_restricted_service.h>

namespace nirfmxinstr_restricted_grpc {
using nidevice_grpc::converters::convert_to_grpc;

// Returns true if it's safe to use outputs of a method with the given status.
inline bool status_ok(int32 status)
{
  return status >= 0;
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status NiRFmxInstrRestrictedService::ConvertApiErrorStatusForNiRFmxInstrHandle(::grpc::ServerContextBase* context, int32_t status, niRFmxInstrHandle instrumentHandle)
{
  int32 error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  // Try first to get the most recent error with a dynamic message.
  library_->GetError(instrumentHandle, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  if (error_code != status) {
    // Since another thread has changed the status, fall back to the static message lookup.
    description.assign(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
    library_->GetErrorString(instrumentHandle, status, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status NiRFmxInstrRestrictedService::GetInitiaitedSnapshotStrings(
    ::grpc::ServerContext* context,
    const GetInitiaitedSnapshotStringsRequest* request,
    GetInitiaitedSnapshotStringsResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto instrument_grpc_session = request->instrument();
    niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
    uInt64 snapshot_info_cache_index{};
    int32 personality_id_array_actual_size{};
    int32 signal_names_actual_size{};
    int32 result_names_actual_size{};
    int32 snapshot_identifiers_actual_size{};
    int32 snapshot_timestamp_array_actual_size{};
    auto status = library_->GetInitiaitedSnapshotStrings(
        instrument,
        &snapshot_info_cache_index,
        nullptr,  // personalityIDArray
        0,        // personalityIDArraySize
        &personality_id_array_actual_size,
        nullptr,  // signalNames
        0,        // signalNamesSize
        &signal_names_actual_size,
        nullptr,  // resultNames
        0,        // resultNamesSize
        &result_names_actual_size,
        nullptr,  // snapshotIdentifiers
        0,        // snapshotIdentifiersSize
        &snapshot_identifiers_actual_size,
        nullptr,  // snapshotTimestampArray
        0,        // snapshotTimestampArraySize
        &snapshot_timestamp_array_actual_size);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
    }
    if (snapshot_info_cache_index != 0) {
      response->mutable_personality_id_array()->Resize(personality_id_array_actual_size, 0);
      int32* personality_id_array = reinterpret_cast<int32*>(response->mutable_personality_id_array()->mutable_data());
      std::string signal_names;
      if (signal_names_actual_size > 0) {
        signal_names.resize(signal_names_actual_size - 1);
      }
      std::string result_names;
      if (result_names_actual_size > 0) {
        result_names.resize(result_names_actual_size - 1);
      }
      std::string snapshot_identifiers;
      if (snapshot_identifiers_actual_size > 0) {
        snapshot_identifiers.resize(snapshot_identifiers_actual_size - 1);
      }
      response->mutable_snapshot_timestamp_array()->Resize(snapshot_timestamp_array_actual_size, 0);
      uInt64* snapshot_timestamp_array = reinterpret_cast<uInt64*>(response->mutable_snapshot_timestamp_array()->mutable_data());
      auto personality_id_array_size = personality_id_array_actual_size;
      auto result_names_size = result_names_actual_size;
      auto signal_names_size = signal_names_actual_size;
      auto snapshot_identifiers_size = snapshot_identifiers_actual_size;
      auto snapshot_timestamp_array_size = snapshot_timestamp_array_actual_size;
      status = library_->GetSnapshotInfoFromCache(
          instrument,
          snapshot_info_cache_index,
          personality_id_array,
          personality_id_array_size,
          &personality_id_array_actual_size,
          (char*)signal_names.data(),
          signal_names_size,
          &signal_names_actual_size,
          (char*)result_names.data(),
          result_names_size,
          &result_names_actual_size,
          (char*)snapshot_identifiers.data(),
          snapshot_identifiers_size,
          &snapshot_identifiers_actual_size,
          snapshot_timestamp_array,
          snapshot_timestamp_array_size,
          &snapshot_timestamp_array_actual_size);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->mutable_personality_id_array()->Resize(personality_id_array_actual_size, 0);
      std::string signal_names_utf8;
      convert_to_grpc(signal_names, &signal_names_utf8);
      response->set_signal_names(signal_names_utf8);
      nidevice_grpc::converters::trim_trailing_nulls(*(response->mutable_signal_names()));
      signal_names_actual_size = static_cast<int32>(signal_names_utf8.length() + 1);
      std::string result_names_utf8;
      convert_to_grpc(result_names, &result_names_utf8);
      response->set_result_names(result_names_utf8);
      nidevice_grpc::converters::trim_trailing_nulls(*(response->mutable_result_names()));
      result_names_actual_size = static_cast<int32>(result_names_utf8.length() + 1);
      std::string snapshot_identifiers_utf8;
      convert_to_grpc(snapshot_identifiers, &snapshot_identifiers_utf8);
      response->set_snapshot_identifiers(snapshot_identifiers_utf8);
      nidevice_grpc::converters::trim_trailing_nulls(*(response->mutable_snapshot_identifiers()));
      snapshot_identifiers_actual_size = static_cast<int32>(snapshot_identifiers_utf8.length() + 1);
      response->mutable_snapshot_timestamp_array()->Resize(snapshot_timestamp_array_actual_size, 0);
    }
    response->set_status(status);
    response->set_personality_id_array_actual_size(personality_id_array_actual_size);
    response->set_signal_names_actual_size(signal_names_actual_size);
    response->set_result_names_actual_size(result_names_actual_size);
    response->set_snapshot_identifiers_actual_size(snapshot_identifiers_actual_size);
    response->set_snapshot_timestamp_array_actual_size(snapshot_timestamp_array_actual_size);
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status NiRFmxInstrRestrictedService::GetLatestConfigurationSnapshot(
    ::grpc::ServerContext* context,
    const GetLatestConfigurationSnapshotRequest* request,
    GetLatestConfigurationSnapshotResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto instrument_grpc_session = request->instrument();
    niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
    uInt64 snapshot_info_cache_index{};
    int32 personality_id{};
    int32 signal_name_actual_size{};
    int32 snapshot_identifier_actual_size{};
    int32 signal_configuration_state{};
    uInt64 signal_timestamp{};
    auto status = library_->GetLatestConfigurationSnapshot(
        instrument,
        &snapshot_info_cache_index,
        &personality_id,
        nullptr,  // signalName
        0,        // signalNameSize
        &signal_name_actual_size,
        nullptr,  // snapshotIdentifier
        0,        // snapshotIdentifierSize
        &snapshot_identifier_actual_size,
        &signal_configuration_state,
        &signal_timestamp);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
    }
    if (snapshot_info_cache_index != 0) {
      std::string signal_name;
      if (signal_name_actual_size > 0) {
        signal_name.resize(signal_name_actual_size - 1);
      }
      std::string snapshot_identifier;
      if (snapshot_identifier_actual_size > 0) {
        snapshot_identifier.resize(snapshot_identifier_actual_size - 1);
      }
      auto signal_name_size = signal_name_actual_size;
      auto snapshot_identifier_size = snapshot_identifier_actual_size;
      status = library_->GetSnapshotInfoFromCache(
          instrument,
          snapshot_info_cache_index,
          nullptr,  // personalityIDArray
          0,        // personalityIDArraySize
          nullptr,  // personalityIDArrayActualSize
          (char*)signal_name.data(),
          signal_name_size,
          &signal_name_actual_size,
          nullptr,  // resultNames
          0,        // resultNamesSize
          nullptr,  // resultNamesActualSize
          (char*)snapshot_identifier.data(),
          snapshot_identifier_size,
          &snapshot_identifier_actual_size,
          nullptr,   // snapshotTimestampArray
          0,         // snapshotTimestampArraySize
          nullptr);  // snapshotTimestampArrayActualSize
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      std::string signal_name_utf8;
      convert_to_grpc(signal_name, &signal_name_utf8);
      response->set_signal_name(signal_name_utf8);
      nidevice_grpc::converters::trim_trailing_nulls(*(response->mutable_signal_name()));
      signal_name_actual_size = static_cast<int32>(signal_name_utf8.length() + 1);
      std::string snapshot_identifier_utf8;
      convert_to_grpc(snapshot_identifier, &snapshot_identifier_utf8);
      response->set_snapshot_identifier(snapshot_identifier_utf8);
      nidevice_grpc::converters::trim_trailing_nulls(*(response->mutable_snapshot_identifier()));
      snapshot_identifier_actual_size = static_cast<int32>(snapshot_identifier_utf8.length() + 1);
    }
    response->set_status(status);
    response->set_personality_id(personality_id);
    response->set_signal_name_actual_size(signal_name_actual_size);
    response->set_snapshot_identifier_actual_size(snapshot_identifier_actual_size);
    response->set_signal_configuration_state(signal_configuration_state);
    response->set_signal_timestamp(signal_timestamp);
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}
}  // namespace nirfmxinstr_restricted_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nirfmxinstr_service.custom.cpp sha256=91bc331930f94e7605e55013f85619e0c2e07651e73362c1a1cccbfa758a7888 bytes=6485 -->
## FILE: source/custom/nirfmxinstr_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nirfmxinstr_service.custom.cpp`
- sha256: `91bc331930f94e7605e55013f85619e0c2e07651e73362c1a1cccbfa758a7888`
- bytes: 6485

````cpp
#include <nirfmxinstr/nirfmxinstr_service.h>
#include <server/converters.h>

#include <sstream>

namespace nirfmxinstr_grpc {
using nidevice_grpc::converters::convert_from_grpc;
using nidevice_grpc::converters::convert_to_grpc;

const auto kErrorReadBufferTooSmall = -200229;
const auto kWarningCAPIStringTruncatedToFitBuffer = 200026;

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status NiRFmxInstrService::GetNIRFSASessionArray(::grpc::ServerContext* context, const GetNIRFSASessionArrayRequest* request, GetNIRFSASessionArrayResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto instrument_grpc_session = request->instrument();
    auto instrument = session_repository_->access_session(instrument_grpc_session.name());
    auto initiating_session_name = instrument_grpc_session.name();
    auto nirfsa_sessions = std::vector<ViSession>{};

    int32 array_size{};
    int32 actual_array_size{};

    while (true) {
      auto status = library_->GetNIRFSASessionArray(instrument, nullptr, 0, &actual_array_size);
      if (status < 0) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      array_size = actual_array_size;
      nirfsa_sessions.resize(array_size);
      status = library_->GetNIRFSASessionArray(instrument, nirfsa_sessions.data(), array_size, &actual_array_size);
      if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
        // buffer is now too small, try again
        continue;
      }

      if (request->session_names_size() != 0 && request->session_names_size() != array_size) {
        std::stringstream stream;
        stream << "Number of session_names must be zero or match actual array size (" << array_size << ").";
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, stream.str());
      }
      if (status < 0) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      for (auto i = 0; i < array_size; ++i) {
        auto init_lambda = [&]() {
          return std::make_tuple(0, nirfsa_sessions[i]);
        };
        auto session_name = request->session_names_size() ? request->session_names(i) : "";
        int status = vi_session_resource_repository_->add_dependent_session(session_name, init_lambda, initiating_session_name);
        auto session = response->add_nirfsa_sessions();
        session->set_name(session_name);
      }
      return ::grpc::Status::OK;
    }
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
// BuildPortString is custom implemented to account for a bug in the buffer size returned from the ivi-dance call to BuildPortString2.
// We adjust the resulting size from the ivi-dance call to account for the channel_number input.
// See AB#1835966 for details about the RFmx Instr Bug.
::grpc::Status NiRFmxInstrService::BuildPortString(::grpc::ServerContext* context, const BuildPortStringRequest* request, BuildPortStringResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
    char* selector_string = const_cast<char*>(selector_string_mbcs.c_str());
    auto port_name_mbcs = convert_from_grpc<std::string>(request->port_name());
    char* port_name = const_cast<char*>(port_name_mbcs.c_str());
    auto device_name_mbcs = convert_from_grpc<std::string>(request->device_name());
    char* device_name = const_cast<char*>(device_name_mbcs.c_str());
    int32 channel_number = request->channel_number();

    while (true) {
      auto status = library_->BuildPortString(selector_string, port_name, device_name, channel_number, 0, nullptr);
      if (status < 0) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, 0);
      }
      int32 selector_string_out_length = static_cast<int32>(status + std::to_string(channel_number).length());  // AB#1835966: RFmx Instr BuildPortString2 Bug.

      std::string selector_string_out;
      if (selector_string_out_length > 0) {
        selector_string_out.resize(selector_string_out_length - 1);
      }
      status = library_->BuildPortString(selector_string, port_name, device_name, channel_number, selector_string_out_length, (char*)selector_string_out.data());
      if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer || status > static_cast<decltype(status)>(selector_string_out_length)) {
        // buffer is now too small, try again
        continue;
      }
      if (status < 0) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, 0);
      }
      response->set_status(status);
      std::string selector_string_out_utf8;
      convert_to_grpc(selector_string_out, &selector_string_out_utf8);
      response->set_selector_string_out(selector_string_out_utf8);
      nidevice_grpc::converters::trim_trailing_nulls(*(response->mutable_selector_string_out()));
      return ::grpc::Status::OK;
    }
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

::grpc::Status NiRFmxInstrService::ConvertApiErrorStatusForNiRFmxInstrHandle(::grpc::ServerContextBase* context, int32_t status, niRFmxInstrHandle instrumentHandle)
{
  int32 error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  // Try first to get the most recent error with a dynamic message.
  library_->GetError(instrumentHandle, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  if (error_code != status) {
    // Since another thread has changed the status, fall back to the static message lookup.
    description.assign(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
    library_->GetErrorString(instrumentHandle, status, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace nirfmxinstr_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nirfmxlte_service.custom.cpp sha256=0f8979a671d3b267281c9a67435c520624a2bcc0a4a0a1d4d66c15d0b4f57023 bytes=979 -->
## FILE: source/custom/nirfmxlte_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nirfmxlte_service.custom.cpp`
- sha256: `0f8979a671d3b267281c9a67435c520624a2bcc0a4a0a1d4d66c15d0b4f57023`
- bytes: 979

````cpp
#include <nirfmxlte/nirfmxlte_service.h>

namespace nirfmxlte_grpc {

::grpc::Status NiRFmxLTEService::ConvertApiErrorStatusForNiRFmxInstrHandle(::grpc::ServerContextBase* context, int32_t status, niRFmxInstrHandle instrumentHandle)
{
  ViStatus error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  // Try first to get the most recent error with a dynamic message.
  library_->GetError(instrumentHandle, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  if (error_code != status) {
    // Since another thread has changed the status, fall back to the static message lookup.
    description.assign(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
    library_->GetErrorString(instrumentHandle, status, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace nirfmxlte_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nirfmxnr_service.custom.cpp sha256=0f9499d5f0d09c92d3fb1d71f3bd8b94de5aa9918be8e3214aa1cd49695488f6 bytes=971 -->
## FILE: source/custom/nirfmxnr_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nirfmxnr_service.custom.cpp`
- sha256: `0f9499d5f0d09c92d3fb1d71f3bd8b94de5aa9918be8e3214aa1cd49695488f6`
- bytes: 971

````cpp
#include <nirfmxnr/nirfmxnr_service.h>

namespace nirfmxnr_grpc {

::grpc::Status NiRFmxNRService::ConvertApiErrorStatusForNiRFmxInstrHandle(::grpc::ServerContextBase* context, int32_t status, niRFmxInstrHandle instrumentHandle)
{
  int32 error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  // Try first to get the most recent error with a dynamic message.
  library_->GetError(instrumentHandle, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  if (error_code != status) {
    // Since another thread has changed the status, fall back to the static message lookup.
    description.assign(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
    library_->GetErrorString(instrumentHandle, status, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace nirfmxnr_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nirfmxpulse_service.custom.cpp sha256=8c6589dbd1faca060e94d2fc2a4cac7022d87c05d843310619fd0e7fd6b6ef0d bytes=989 -->
## FILE: source/custom/nirfmxpulse_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nirfmxpulse_service.custom.cpp`
- sha256: `8c6589dbd1faca060e94d2fc2a4cac7022d87c05d843310619fd0e7fd6b6ef0d`
- bytes: 989

````cpp
#include <nirfmxpulse/nirfmxpulse_service.h>

namespace nirfmxpulse_grpc {

::grpc::Status NiRFmxPulseService::ConvertApiErrorStatusForNiRFmxInstrHandle(::grpc::ServerContextBase* context, int32_t status, niRFmxInstrHandle instrumentHandle)
{
  ViStatus error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  // Try first to get the most recent error with a dynamic message.
  library_->GetError(instrumentHandle, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  if (error_code != status) {
    // Since another thread has changed the status, fall back to the static message lookup.
    description.assign(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
    library_->GetErrorString(instrumentHandle, status, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace nirfmxpulse_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nirfmxspecan_restricted_service.custom.cpp sha256=20dc8b8cb57c10e209d94c60e938d62caad2c156f565e27d870529c6e63df405 bytes=972 -->
## FILE: source/custom/nirfmxspecan_restricted_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nirfmxspecan_restricted_service.custom.cpp`
- sha256: `20dc8b8cb57c10e209d94c60e938d62caad2c156f565e27d870529c6e63df405`
- bytes: 972

````cpp
#include <nirfmxspecan_restricted/nirfmxspecan_restricted_service.h>

namespace nirfmxspecan_restricted_grpc {

::grpc::Status NiRFmxSpecAnRestrictedService::ConvertApiErrorStatusForNiRFmxInstrHandle(::grpc::ServerContextBase* context, int32_t status, niRFmxInstrHandle instrumentHandle)
{
  ViStatus error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  // Try first to get the most recent error with a dynamic message.
  library_->GetError(instrumentHandle, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  if (error_code != status) {
    // Since another thread has changed the status, fall back to the static message lookup.
    library_->GetErrorString(instrumentHandle, status, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace nirfmxspecan_restricted_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nirfmxspecan_service.custom.cpp sha256=3facca044d69e15cdea7589793dda70a097edc9a072d9a1a0dcde55ad925c646 bytes=3311 -->
## FILE: source/custom/nirfmxspecan_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nirfmxspecan_service.custom.cpp`
- sha256: `3facca044d69e15cdea7589793dda70a097edc9a072d9a1a0dcde55ad925c646`
- bytes: 3311

````cpp
#include <nirfmxspecan/nirfmxspecan_service.h>
using nidevice_grpc::converters::convert_to_grpc;
using nidevice_grpc::converters::convert_from_grpc;
using nidevice_grpc::converters::calculate_linked_array_size;
using nidevice_grpc::converters::MatchState;

namespace nirfmxspecan_grpc {

  // Returns true if it's safe to use outputs of a method with the given status.
  inline bool status_ok(int32 status)
  {
    return status >= 0;
  }

  ::grpc::Status NiRFmxSpecAnService::ConvertApiErrorStatusForNiRFmxInstrHandle(::grpc::ServerContextBase* context, int32_t status, niRFmxInstrHandle instrumentHandle)
  {
    ViStatus error_code{};
    std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
    // Try first to get the most recent error with a dynamic message.
    library_->GetError(instrumentHandle, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
    if (error_code != status) {
      // Since another thread has changed the status, fall back to the static message lookup.
      library_->GetErrorString(instrumentHandle, status, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
    }
    return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxSpecAnService::DPDCfgApplyDPDUserLookupTableInterleavedIQ(::grpc::ServerContext*context,   const DPDCfgApplyDPDUserLookupTableInterleavedIQRequest* request,  DPDCfgApplyDPDUserLookupTableInterleavedIQResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      auto lut_input_powers = const_cast<float32*>(request->lut_input_powers().data());
      auto lut_complex_gains = const_cast<float32*>(request->lut_complex_gains().data());
      auto array_size = 0;
      if (request->lut_input_powers_size()) {
        array_size = request->lut_input_powers_size() * 2;
        if (request->lut_complex_gains_size()) {
          if (request->lut_complex_gains_size() != array_size) {
            return ::grpc::Status(::grpc::INVALID_ARGUMENT, "lut_complex_gains size must be twice the size of lut_input_powers.");
          }
        }
      }
      else if (request->lut_complex_gains_size()) {
        array_size = request->lut_complex_gains_size();
      }
      auto status = library_->DPDCfgApplyDPDUserLookupTableInterleavedIQ(instrument, selector_string,  lut_input_powers, lut_complex_gains, array_size);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

}  // namespace nirfmxspecan_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nirfmxtdscdma_service.custom.cpp sha256=c398f5cb0b24aeea2ddaeaee8a3f229ef7506d095c00379c10aee535cd9161c1 bytes=999 -->
## FILE: source/custom/nirfmxtdscdma_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nirfmxtdscdma_service.custom.cpp`
- sha256: `c398f5cb0b24aeea2ddaeaee8a3f229ef7506d095c00379c10aee535cd9161c1`
- bytes: 999

````cpp
#include <nirfmxtdscdma/nirfmxtdscdma_service.h>

namespace nirfmxtdscdma_grpc {

::grpc::Status NiRFmxTDSCDMAService::ConvertApiErrorStatusForNiRFmxInstrHandle(::grpc::ServerContextBase* context, int32_t status, niRFmxInstrHandle instrumentHandle)
{
  ViStatus error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  // Try first to get the most recent error with a dynamic message.
  library_->GetError(instrumentHandle, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  if (error_code != status) {
    // Since another thread has changed the status, fall back to the static message lookup.
    description.assign(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
    library_->GetErrorString(instrumentHandle, status, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace nirfmxtdscdma_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nirfmxvna_service.custom.cpp sha256=f1162c9f33940a3fea8f4c103d4abb99f1451bb1d39228a2fe6d56f6f26adc57 bytes=979 -->
## FILE: source/custom/nirfmxvna_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nirfmxvna_service.custom.cpp`
- sha256: `f1162c9f33940a3fea8f4c103d4abb99f1451bb1d39228a2fe6d56f6f26adc57`
- bytes: 979

````cpp
#include <nirfmxvna/nirfmxvna_service.h>

namespace nirfmxvna_grpc {

::grpc::Status NiRFmxVNAService::ConvertApiErrorStatusForNiRFmxInstrHandle(::grpc::ServerContextBase* context, int32_t status, niRFmxInstrHandle instrumentHandle)
{
  ViStatus error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  // Try first to get the most recent error with a dynamic message.
  library_->GetError(instrumentHandle, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  if (error_code != status) {
    // Since another thread has changed the status, fall back to the static message lookup.
    description.assign(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
    library_->GetErrorString(instrumentHandle, status, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace nirfmxvna_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nirfmxwcdma_service.custom.cpp sha256=2117d659773f13f2038a7c0e5ed8a9f11722ead79a6e3ba0456acf7cf1449cdd bytes=989 -->
## FILE: source/custom/nirfmxwcdma_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nirfmxwcdma_service.custom.cpp`
- sha256: `2117d659773f13f2038a7c0e5ed8a9f11722ead79a6e3ba0456acf7cf1449cdd`
- bytes: 989

````cpp
#include <nirfmxwcdma/nirfmxwcdma_service.h>

namespace nirfmxwcdma_grpc {

::grpc::Status NiRFmxWCDMAService::ConvertApiErrorStatusForNiRFmxInstrHandle(::grpc::ServerContextBase* context, int32_t status, niRFmxInstrHandle instrumentHandle)
{
  ViStatus error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  // Try first to get the most recent error with a dynamic message.
  library_->GetError(instrumentHandle, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  if (error_code != status) {
    // Since another thread has changed the status, fall back to the static message lookup.
    description.assign(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
    library_->GetErrorString(instrumentHandle, status, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace nirfmxwcdma_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nirfmxwlan_restricted_service.custom.cpp sha256=36a03fdef8fc873018ef92d4f4d1eca9cd48e4218f24bd58796074cc2fc928ab bytes=962 -->
## FILE: source/custom/nirfmxwlan_restricted_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nirfmxwlan_restricted_service.custom.cpp`
- sha256: `36a03fdef8fc873018ef92d4f4d1eca9cd48e4218f24bd58796074cc2fc928ab`
- bytes: 962

````cpp
#include <nirfmxwlan_restricted/nirfmxwlan_restricted_service.h>

namespace nirfmxwlan_restricted_grpc {

::grpc::Status NiRFmxWLANRestrictedService::ConvertApiErrorStatusForNiRFmxInstrHandle(::grpc::ServerContextBase* context, int32_t status, niRFmxInstrHandle instrumentHandle)
{
  ViStatus error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  // Try first to get the most recent error with a dynamic message.
  library_->GetError(instrumentHandle, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  if (error_code != status) {
    // Since another thread has changed the status, fall back to the static message lookup.
    library_->GetErrorString(instrumentHandle, status, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace nirfmxwlan_restricted_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nirfmxwlan_service.custom.cpp sha256=81a82b1795b3cf9c1bc62a2a10eb5ead99e1e469bfedf10e5349f00696888a4b bytes=981 -->
## FILE: source/custom/nirfmxwlan_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nirfmxwlan_service.custom.cpp`
- sha256: `81a82b1795b3cf9c1bc62a2a10eb5ead99e1e469bfedf10e5349f00696888a4b`
- bytes: 981

````cpp
#include <nirfmxwlan/nirfmxwlan_service.h>

namespace nirfmxwlan_grpc {

::grpc::Status NiRFmxWLANService::ConvertApiErrorStatusForNiRFmxInstrHandle(::grpc::ServerContextBase* context, int32_t status, niRFmxInstrHandle instrumentHandle)
{
  int32 error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  // Try first to get the most recent error with a dynamic message.
  library_->GetError(instrumentHandle, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  if (error_code != status) {
    // Since another thread has changed the status, fall back to the static message lookup.
    description.assign(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
    library_->GetErrorString(instrumentHandle, status, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace nirfmxwlan_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nirfmxwlangen_service.custom.cpp sha256=31c73e3b25308c14d169cb32444802b60477ab0197e0c3045bdd06fca2d2deb6 bytes=12777 -->
## FILE: source/custom/nirfmxwlangen_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nirfmxwlangen_service.custom.cpp`
- sha256: `31c73e3b25308c14d169cb32444802b60477ab0197e0c3045bdd06fca2d2deb6`
- bytes: 12777

````cpp
#include <nirfmxwlangen/nirfmxwlangen_service.h>
#include <nirfsg/nirfsg_library.h>

namespace nirfmxwlangen_grpc {
using nidevice_grpc::converters::convert_to_grpc;
using nidevice_grpc::converters::convert_from_grpc;
const auto kErrorReadBufferTooSmall = -200229;
const auto kWarningCAPIStringTruncatedToFitBuffer = 200026;

// Returns true if it's safe to use outputs of a method with the given status.
inline bool status_ok(int32 status)
{
  return status >= 0;
}

::grpc::Status NiRFmxWLANGenService::ConvertApiErrorStatusForNiWLANGenerationSession(::grpc::ServerContextBase* context, int32_t status, niWLANGenerationSession session)
{
  ViStatus error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  description.assign(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  library_->GetErrorString(session, status, &description[0], nidevice_grpc::kMaxGrpcErrorDescriptionSize);
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

::grpc::Status NiRFmxWLANGenService::ConvertApiErrorStatusForViSession(::grpc::ServerContextBase* context, int32_t status, ViSession RFSGHandle)
{
  auto library = std::make_shared<nirfsg_grpc::NiRFSGLibrary>();

  ViStatus error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  library->GetError(RFSGHandle, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  if (error_code != status) {
    description.assign(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
    library->ErrorMessage(RFSGHandle, status, &description[0]);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status NiRFmxWLANGenService::CreateMIMOWaveformsComplexF64(::grpc::ServerContext* context, const CreateMIMOWaveformsComplexF64Request* request, CreateMIMOWaveformsComplexF64Response* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto session_grpc_session = request->session();
    niWLANGenerationSession session = session_repository_->access_session(session_grpc_session.name());
    int32 reset = request->reset();

    int32 number_of_transmit_channels, iq_waveform_size, number_of_segments;

    auto status = library_->GetScalarAttributeI32(session, "", 47, &number_of_transmit_channels);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForNiWLANGenerationSession(context, status, session);
    }

    status = library_->GetScalarAttributeI32(session, "", 37, &iq_waveform_size);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForNiWLANGenerationSession(context, status, session);
    }

    status = library_->GetScalarAttributeI32(session, "", 75, &number_of_segments);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForNiWLANGenerationSession(context, status, session);
    }

    int32 number_of_tx_chains = number_of_transmit_channels * number_of_segments;

    response->mutable_t0()->Resize(number_of_tx_chains, 0);
    float64* t0 = response->mutable_t0()->mutable_data();
    response->mutable_dt()->Resize(number_of_tx_chains, 0);
    float64* dt = response->mutable_dt()->mutable_data();
    std::vector<NIComplexNumber_struct> waveforms(iq_waveform_size * number_of_tx_chains, NIComplexNumber_struct());

    int32 done{};
    status = library_->CreateMIMOWaveformsComplexF64(session, reset, t0, dt, waveforms.data(), number_of_tx_chains, iq_waveform_size, nullptr, &done);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForNiWLANGenerationSession(context, status, session);
    }
    response->set_status(status);
    convert_to_grpc(waveforms, response->mutable_waveforms());
    response->set_actual_num_samples_in_each_wfm(iq_waveform_size);
    response->set_done(done);
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status NiRFmxWLANGenService::CreateMIMOWaveformsComplexF64InterleavedIQ(::grpc::ServerContext* context, const CreateMIMOWaveformsComplexF64InterleavedIQRequest* request, CreateMIMOWaveformsComplexF64InterleavedIQResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto session_grpc_session = request->session();
    niWLANGenerationSession session = session_repository_->access_session(session_grpc_session.name());
    int32 reset = request->reset();

    int32 number_of_transmit_channels, iq_waveform_size, number_of_segments;

    auto status = library_->GetScalarAttributeI32(session, "", 47, &number_of_transmit_channels);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForNiWLANGenerationSession(context, status, session);
    }

    status = library_->GetScalarAttributeI32(session, "", 37, &iq_waveform_size);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForNiWLANGenerationSession(context, status, session);
    }

    status = library_->GetScalarAttributeI32(session, "", 75, &number_of_segments);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForNiWLANGenerationSession(context, status, session);
    }

    int32 number_of_tx_chains = number_of_transmit_channels * number_of_segments;

    response->mutable_waveforms()->Resize(number_of_tx_chains * iq_waveform_size * 2, 0);
    float64* waveforms = response->mutable_waveforms()->mutable_data();
    response->mutable_t0()->Resize(number_of_tx_chains, 0);
    float64* t0 = response->mutable_t0()->mutable_data();
    response->mutable_dt()->Resize(number_of_tx_chains, 0);
    float64* dt = response->mutable_dt()->mutable_data();
    int32 done{};
    status = library_->CreateMIMOWaveformsComplexF64InterleavedIQ(session, reset, t0, dt, waveforms, number_of_tx_chains, iq_waveform_size, nullptr, &done);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForNiWLANGenerationSession(context, status, session);
    }
    response->set_status(status);
    response->set_actual_num_samples_in_each_wfm(iq_waveform_size);
    response->set_done(done);
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status NiRFmxWLANGenService::GetMappingMatrix(::grpc::ServerContext* context, const GetMappingMatrixRequest* request, GetMappingMatrixResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto session_grpc_session = request->session();
    niWLANGenerationSession session = session_repository_->access_session(session_grpc_session.name());
    auto channel_string_mbcs = convert_from_grpc<std::string>(request->channel_string());
    char* channel_string = (char*)channel_string_mbcs.c_str();

    while (true) {

      std::vector<NIComplexNumber_struct> mapping_matrix(request->num_mapping_matrix_rows() * request->num_mapping_matrix_columns(), NIComplexNumber_struct());
      int32 status = library_->GetMappingMatrix(session, channel_string, mapping_matrix.data(), request->num_mapping_matrix_rows(), request->num_mapping_matrix_columns());
      if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
        // buffer is now too small, try again
        continue;
      }
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiWLANGenerationSession(context, status, session);
      }
      response->set_status(status);
      convert_to_grpc(mapping_matrix, response->mutable_mapping_matrix());
      return ::grpc::Status::OK;
    }
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status NiRFmxWLANGenService::SetMappingMatrix(::grpc::ServerContext* context, const SetMappingMatrixRequest* request, SetMappingMatrixResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto session_grpc_session = request->session();
    niWLANGenerationSession session = session_repository_->access_session(session_grpc_session.name());
    auto channel_string_mbcs = convert_from_grpc<std::string>(request->channel_string());
    char* channel_string = (char*)channel_string_mbcs.c_str();
    auto mapping_matrix = convert_from_grpc<NIComplexNumber_struct>(request->mapping_matrix());
    int32 num_mapping_matrix_rows = request->num_mapping_matrix_rows();
    int32 num_mapping_matrix_columns = request->num_mapping_matrix_columns();
    auto status = library_->SetMappingMatrix(session, channel_string, mapping_matrix.data(), num_mapping_matrix_rows, num_mapping_matrix_columns);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForNiWLANGenerationSession(context, status, session);
    }
    response->set_status(status);
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status NiRFmxWLANGenService::GetMappingMatrixInterleavedIQ(::grpc::ServerContext* context, const GetMappingMatrixInterleavedIQRequest* request, GetMappingMatrixInterleavedIQResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto session_grpc_session = request->session();
    niWLANGenerationSession session = session_repository_->access_session(session_grpc_session.name());
    auto channel_string_mbcs = convert_from_grpc<std::string>(request->channel_string());
    char* channel_string = (char*)channel_string_mbcs.c_str();

    while (true) {

      response->mutable_mapping_matrix()->Resize(request->num_mapping_matrix_rows() * request->num_mapping_matrix_columns() * 2, 0);
      float64* mapping_matrix = response->mutable_mapping_matrix()->mutable_data();
      int32 status = library_->GetMappingMatrixInterleavedIQ(session, channel_string, mapping_matrix, request->num_mapping_matrix_rows(), request->num_mapping_matrix_columns());
      if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
        // buffer is now too small, try again
        continue;
      }
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiWLANGenerationSession(context, status, session);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status NiRFmxWLANGenService::SetMappingMatrixInterleavedIQ(::grpc::ServerContext* context, const SetMappingMatrixInterleavedIQRequest* request, SetMappingMatrixInterleavedIQResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto session_grpc_session = request->session();
    niWLANGenerationSession session = session_repository_->access_session(session_grpc_session.name());
    auto channel_string_mbcs = convert_from_grpc<std::string>(request->channel_string());
    char* channel_string = (char*)channel_string_mbcs.c_str();

    auto mapping_matrix = const_cast<float64*>(request->mapping_matrix().data());
    int32 num_mapping_matrix_rows = request->num_mapping_matrix_rows();
    int32 num_mapping_matrix_columns = request->num_mapping_matrix_columns();
    
    auto status = library_->SetMappingMatrixInterleavedIQ(session, channel_string, mapping_matrix, num_mapping_matrix_rows, num_mapping_matrix_columns);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForNiWLANGenerationSession(context, status, session);
    }
    response->set_status(status);
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

}  // namespace nirfmxwlangen_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nirfsa_aliases.h sha256=93a9a88b5b411d7ae0737aeac376bf8db46f5ee996ad065d3cb83749d9f8aafd bytes=369 -->
## FILE: source/custom/nirfsa_aliases.h

- repository: `ni/grpc-device`
- source_path: `source/custom/nirfsa_aliases.h`
- sha256: `93a9a88b5b411d7ae0737aeac376bf8db46f5ee996ad065d3cb83749d9f8aafd`
- bytes: 369

````c
#ifndef NIDEVICE_GRPC_DEVICE_NIRFSA_ALIASES_H
#define NIDEVICE_GRPC_DEVICE_NIRFSA_ALIASES_H
#include <niRFSA.h>

// Alias SmtSpectrumInfo so that our standard disambiguating reference scheme works.
// Note that this matches how all other typedefs are defined.
using SmtSpectrumInfo_struct = SmtSpectrumInfo;

#endif /* NIDEVICE_GRPC_DEVICE_NIRFSA_ALIASES_H */
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nirfsa_service.custom.cpp sha256=a7b3ced2c8c685e17924522d2207378d4ec62e0bf301a6c36c2afb4c0c055130 bytes=977 -->
## FILE: source/custom/nirfsa_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nirfsa_service.custom.cpp`
- sha256: `a7b3ced2c8c685e17924522d2207378d4ec62e0bf301a6c36c2afb4c0c055130`
- bytes: 977

````cpp
#include <nirfsa/nirfsa_service.h>

namespace nirfsa_grpc {

::grpc::Status NiRFSAService::ConvertApiErrorStatusForViSession(::grpc::ServerContextBase* context, int32_t status, ViSession vi)
{
  static_assert(nidevice_grpc::kMaxGrpcErrorDescriptionSize >= 1024, "ErrorMessage expects a minimum buffer size.");
  ViStatus error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  // Try first to get the most recent error with a dynamic message.
  library_->GetError(vi, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  if (error_code != status) {
    // Since another thread has changed the status, fall back to the static message lookup.
    description.assign(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
    library_->ErrorMessage(vi, status, &description[0]);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace nirfsa_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nirfsg_restricted_service.custom.cpp sha256=2ac8644a294797f844218f3adb11e0624b40bd7bcc1e35ef2304546e8821b8d2 bytes=955 -->
## FILE: source/custom/nirfsg_restricted_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nirfsg_restricted_service.custom.cpp`
- sha256: `2ac8644a294797f844218f3adb11e0624b40bd7bcc1e35ef2304546e8821b8d2`
- bytes: 955

````cpp
#include <nirfsg_restricted/nirfsg_restricted_service.h>

namespace nirfsg_restricted_grpc {

::grpc::Status NiRFSGRestrictedService::ConvertApiErrorStatusForViSession(::grpc::ServerContextBase* context, int32_t status, ViSession vi)
{
  static_assert(nidevice_grpc::kMaxGrpcErrorDescriptionSize >= 1024, "ErrorMessage expects a minimum buffer size.");
  ViStatus error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  // Try first to get the most recent error with a dynamic message.
  library_->GetError(vi, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  if (error_code != status) {
    // Since another thread has changed the status, fall back to the static message lookup.
    library_->ErrorMessage(vi, status, &description[0]);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace nirfsg_restricted_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nirfsg_service.custom.cpp sha256=a67789114db9a7f2e1655ab68c18cb0df9963e38314617121e850787d1c3fe50 bytes=977 -->
## FILE: source/custom/nirfsg_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nirfsg_service.custom.cpp`
- sha256: `a67789114db9a7f2e1655ab68c18cb0df9963e38314617121e850787d1c3fe50`
- bytes: 977

````cpp
#include <nirfsg/nirfsg_service.h>

namespace nirfsg_grpc {

::grpc::Status NiRFSGService::ConvertApiErrorStatusForViSession(::grpc::ServerContextBase* context, int32_t status, ViSession vi)
{
  static_assert(nidevice_grpc::kMaxGrpcErrorDescriptionSize >= 1024, "ErrorMessage expects a minimum buffer size.");
  ViStatus error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  // Try first to get the most recent error with a dynamic message.
  library_->GetError(vi, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  if (error_code != status) {
    // Since another thread has changed the status, fall back to the static message lookup.
    description.assign(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
    library_->ErrorMessage(vi, status, &description[0]);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace nirfsg_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/niscope_restricted_service.custom.cpp sha256=a2ac8220ec834103021933717b956941b0eb8f17abe043ec83c35727aa4bcf26 bytes=966 -->
## FILE: source/custom/niscope_restricted_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/niscope_restricted_service.custom.cpp`
- sha256: `a2ac8220ec834103021933717b956941b0eb8f17abe043ec83c35727aa4bcf26`
- bytes: 966

````cpp
#include <niscope_restricted/niscope_restricted_service.h>

namespace niscope_restricted_grpc {

::grpc::Status NiScopeRestrictedService::ConvertApiErrorStatusForViSession(::grpc::ServerContextBase* context, int32_t status, ViSession vi)
{
  ViStatus error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  // Try first to get the most recent error with a dynamic message.
  library_->GetError(vi, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  if (error_code != status) {
    // Since another thread has changed the status, fall back to the static message lookup.
    description.assign(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
    library_->GetErrorMessage(vi, status, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace niscope_restricted_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/niscope_service.custom.cpp sha256=4a1c36ddc28df38ae9bf894761171175075805305489fd0568bab25c87d55d1f bytes=25403 -->
## FILE: source/custom/niscope_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/niscope_service.custom.cpp`
- sha256: `4a1c36ddc28df38ae9bf894761171175075805305489fd0568bab25c87d55d1f`
- bytes: 25403

````cpp
#include <niscope/niscope_service.h>
#include <server/converters.h>

#include <stdexcept>

namespace niscope_grpc {
using nidevice_grpc::converters::convert_from_grpc;
using nidevice_grpc::converters::convert_to_grpc;

const auto kErrorReadBufferTooSmall = -200229;

struct DriverWarningOrErrorException : std::runtime_error {
  DriverWarningOrErrorException(int status) : std::runtime_error("") { status_ = status; }
  int status_ = 0;
};

void CheckStatus(int status)
{
  if (status != 0) {
    throw DriverWarningOrErrorException(status);
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status NiScopeService::Fetch(::grpc::ServerContext* context, const FetchRequest* request, FetchResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  ViSession vi = VI_NULL;
  try {
    auto session = request->vi();
    vi = session_repository_->access_session(session.name());
    auto channel_list_mbcs = convert_from_grpc<std::string>(request->channel_list());
    ViConstString channel_list = channel_list_mbcs.c_str();
    ViReal64 timeout = request->timeout();
    ViInt32 num_samples = request->num_samples();
    if (num_samples < 0) {
      CheckStatus(library_->ActualRecordLength(vi, &num_samples));
    }

    ViInt32 num_waveforms;
    CheckStatus(library_->ActualNumWfms(vi, channel_list, &num_waveforms));

    response->mutable_waveform()->Resize(num_samples * num_waveforms, 0.0);
    ViReal64* waveform = response->mutable_waveform()->mutable_data();
    std::vector<niScope_wfmInfo> waveform_info(num_waveforms, niScope_wfmInfo());
    auto status = library_->Fetch(vi, channel_list, timeout, num_samples, waveform, waveform_info.data());
    if (status < VI_SUCCESS) {
      return ConvertApiErrorStatusForViSession(context, status, vi);
    }
    response->set_status(status);
    convert_to_grpc(waveform_info, response->mutable_wfm_info());
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
  catch (const DriverWarningOrErrorException& ex) {
    if (ex.status_ < VI_SUCCESS) {
      return ConvertApiErrorStatusForViSession(context, ex.status_, vi);
    }
    response->set_status(ex.status_);
    return ::grpc::Status::OK;
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status NiScopeService::FetchBinary8(::grpc::ServerContext* context, const FetchBinary8Request* request, FetchBinary8Response* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  ViSession vi = VI_NULL;
  try {
    auto session = request->vi();
    vi = session_repository_->access_session(session.name());
    auto channel_list_mbcs = convert_from_grpc<std::string>(request->channel_list());
    ViConstString channel_list = channel_list_mbcs.c_str();
    ViReal64 timeout = request->timeout();
    ViInt32 num_samples = request->num_samples();
    if (num_samples < 0) {
      CheckStatus(library_->ActualRecordLength(vi, &num_samples));
    }

    ViInt32 num_waveforms;
    CheckStatus(library_->ActualNumWfms(vi, channel_list, &num_waveforms));

    response->mutable_waveform()->insert(0, (size_t)(num_samples * num_waveforms), '\0');
    ViInt8* waveform = (ViInt8*)response->mutable_waveform()->data();
    std::vector<niScope_wfmInfo> waveform_info(num_waveforms, niScope_wfmInfo());
    auto status = library_->FetchBinary8(vi, channel_list, timeout, num_samples, waveform, waveform_info.data());
    if (status < VI_SUCCESS) {
      return ConvertApiErrorStatusForViSession(context, status, vi);
    }
    response->set_status(status);
    convert_to_grpc(waveform_info, response->mutable_wfm_info());
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
  catch (const DriverWarningOrErrorException& ex) {
    if (ex.status_ < VI_SUCCESS) {
      return ConvertApiErrorStatusForViSession(context, ex.status_, vi);
    }
    response->set_status(ex.status_);
    return ::grpc::Status::OK;
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status NiScopeService::FetchBinary16(::grpc::ServerContext* context, const FetchBinary16Request* request, FetchBinary16Response* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  ViSession vi = VI_NULL;
  try {
    auto session = request->vi();
    vi = session_repository_->access_session(session.name());
    auto channel_list_mbcs = convert_from_grpc<std::string>(request->channel_list());
    ViConstString channel_list = channel_list_mbcs.c_str();
    ViReal64 timeout = request->timeout();
    ViInt32 num_samples = request->num_samples();
    if (num_samples < 0) {
      CheckStatus(library_->ActualRecordLength(vi, &num_samples));
    }

    ViInt32 num_waveforms;
    CheckStatus(library_->ActualNumWfms(vi, channel_list, &num_waveforms));

    std::vector<ViInt16> waveform(num_samples * num_waveforms, 0);
    std::vector<niScope_wfmInfo> waveform_info(num_waveforms, niScope_wfmInfo());
    auto status = library_->FetchBinary16(vi, channel_list, timeout, num_samples, waveform.data(), waveform_info.data());
    if (status < VI_SUCCESS) {
      return ConvertApiErrorStatusForViSession(context, status, vi);
    }
    response->set_status(status);
    convert_to_grpc(waveform_info, response->mutable_wfm_info());
    response->mutable_waveform()->Add(waveform.begin(), waveform.end());
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
  catch (const DriverWarningOrErrorException& ex) {
    if (ex.status_ < VI_SUCCESS) {
      return ConvertApiErrorStatusForViSession(context, ex.status_, vi);
    }
    response->set_status(ex.status_);
    return ::grpc::Status::OK;
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status NiScopeService::FetchBinary32(::grpc::ServerContext* context, const FetchBinary32Request* request, FetchBinary32Response* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  ViSession vi = VI_NULL;
  try {
    auto session = request->vi();
    vi = session_repository_->access_session(session.name());
    auto channel_list_mbcs = convert_from_grpc<std::string>(request->channel_list());
    ViConstString channel_list = channel_list_mbcs.c_str();
    ViReal64 timeout = request->timeout();
    ViInt32 num_samples = request->num_samples();
    if (num_samples < 0) {
      CheckStatus(library_->ActualRecordLength(vi, &num_samples));
    }

    ViInt32 num_waveforms;
    CheckStatus(library_->ActualNumWfms(vi, channel_list, &num_waveforms));

    std::vector<ViInt32> waveform(num_samples * num_waveforms, 0);
    std::vector<niScope_wfmInfo> waveform_info(num_waveforms, niScope_wfmInfo());
    auto status = library_->FetchBinary32(vi, channel_list, timeout, num_samples, waveform.data(), waveform_info.data());
    if (status < VI_SUCCESS) {
      return ConvertApiErrorStatusForViSession(context, status, vi);
    }
    response->set_status(status);
    response->mutable_waveform()->Add(waveform.begin(), waveform.end());
    convert_to_grpc(waveform_info, response->mutable_wfm_info());
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
  catch (const DriverWarningOrErrorException& ex) {
    if (ex.status_ < VI_SUCCESS) {
      return ConvertApiErrorStatusForViSession(context, ex.status_, vi);
    }
    response->set_status(ex.status_);
    return ::grpc::Status::OK;
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status NiScopeService::FetchArrayMeasurement(::grpc::ServerContext* context, const FetchArrayMeasurementRequest* request, FetchArrayMeasurementResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  ViSession vi = VI_NULL;
  try {
    auto session = request->vi();
    vi = session_repository_->access_session(session.name());
    auto channel_list_mbcs = convert_from_grpc<std::string>(request->channel_list());
    ViConstString channel_list = channel_list_mbcs.c_str();
    ViReal64 timeout = request->timeout();
    ViInt32 array_meas_function;
    switch (request->array_meas_function_enum_case()) {
      case niscope_grpc::FetchArrayMeasurementRequest::ArrayMeasFunctionEnumCase::kArrayMeasFunction:
        array_meas_function = (ViInt32)request->array_meas_function();
        break;
      case niscope_grpc::FetchArrayMeasurementRequest::ArrayMeasFunctionEnumCase::kArrayMeasFunctionRaw:
        array_meas_function = (ViInt32)request->array_meas_function_raw();
        break;
      case niscope_grpc::FetchArrayMeasurementRequest::ArrayMeasFunctionEnumCase::ARRAY_MEAS_FUNCTION_ENUM_NOT_SET:
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for array_meas_function was not specified or out of range");
        break;
    }

    // meas_wfm_size is marked optional in the proto file.
    // If it was set to a non-negative value, use it.
    // If it wasn't set or if it was set to a negative number, use the ActualMeasWfmSize.
    ViInt32 measurement_waveform_size = -1;
    if (request->has_meas_wfm_size()) {
      measurement_waveform_size = request->meas_wfm_size();
    }
    if (measurement_waveform_size < 0) {
      CheckStatus(library_->ActualMeasWfmSize(vi, array_meas_function, &measurement_waveform_size));
    }

    ViInt32 num_waveforms;
    CheckStatus(library_->ActualNumWfms(vi, channel_list, &num_waveforms));

    response->mutable_meas_wfm()->Resize(num_waveforms * measurement_waveform_size, 0);
    ViReal64* meas_wfm = response->mutable_meas_wfm()->mutable_data();
    std::vector<niScope_wfmInfo> waveform_info(num_waveforms, niScope_wfmInfo());
    auto status = library_->FetchArrayMeasurement(vi, channel_list, timeout, array_meas_function, measurement_waveform_size, meas_wfm, waveform_info.data());
    if (status < VI_SUCCESS) {
      return ConvertApiErrorStatusForViSession(context, status, vi);
    }
    response->set_status(status);
    convert_to_grpc(waveform_info, response->mutable_wfm_info());
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
  catch (const DriverWarningOrErrorException& ex) {
    if (ex.status_ < VI_SUCCESS) {
      return ConvertApiErrorStatusForViSession(context, ex.status_, vi);
    }
    response->set_status(ex.status_);
    return ::grpc::Status::OK;
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status NiScopeService::FetchMeasurementStats(::grpc::ServerContext* context, const FetchMeasurementStatsRequest* request, FetchMeasurementStatsResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  ViSession vi = VI_NULL;
  try {
    auto session = request->vi();
    vi = session_repository_->access_session(session.name());
    auto channel_list_mbcs = convert_from_grpc<std::string>(request->channel_list());
    ViConstString channel_list = channel_list_mbcs.c_str();
    ViReal64 timeout = request->timeout();
    ViInt32 scalar_meas_function;
    switch (request->scalar_meas_function_enum_case()) {
      case niscope_grpc::FetchMeasurementStatsRequest::ScalarMeasFunctionEnumCase::kScalarMeasFunction:
        scalar_meas_function = (ViInt32)request->scalar_meas_function();
        break;
      case niscope_grpc::FetchMeasurementStatsRequest::ScalarMeasFunctionEnumCase::kScalarMeasFunctionRaw:
        scalar_meas_function = (ViInt32)request->scalar_meas_function_raw();
        break;
      case niscope_grpc::FetchMeasurementStatsRequest::ScalarMeasFunctionEnumCase::SCALAR_MEAS_FUNCTION_ENUM_NOT_SET:
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for scalar_meas_function was not specified or out of range");
        break;
    }

    ViInt32 num_waveforms;
    CheckStatus(library_->ActualNumWfms(vi, channel_list, &num_waveforms));

    response->mutable_result()->Resize(num_waveforms, 0.0);
    ViReal64* result = response->mutable_result()->mutable_data();
    response->mutable_mean()->Resize(num_waveforms, 0.0);
    ViReal64* mean = response->mutable_mean()->mutable_data();
    response->mutable_stdev()->Resize(num_waveforms, 0.0);
    ViReal64* stdev = response->mutable_stdev()->mutable_data();
    response->mutable_min()->Resize(num_waveforms, 0.0);
    ViReal64* min = response->mutable_min()->mutable_data();
    response->mutable_max()->Resize(num_waveforms, 0.0);
    ViReal64* max = response->mutable_max()->mutable_data();
    std::vector<ViInt32> num_in_stats(num_waveforms, 0);
    auto status = library_->FetchMeasurementStats(vi, channel_list, timeout, scalar_meas_function, result, mean, stdev, min, max, num_in_stats.data());
    if (status < VI_SUCCESS) {
      return ConvertApiErrorStatusForViSession(context, status, vi);
    }
    response->set_status(status);
    response->mutable_num_in_stats()->Add(num_in_stats.begin(), num_in_stats.end());
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
  catch (const DriverWarningOrErrorException& ex) {
    if (ex.status_ < VI_SUCCESS) {
      return ConvertApiErrorStatusForViSession(context, ex.status_, vi);
    }
    response->set_status(ex.status_);
    return ::grpc::Status::OK;
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status NiScopeService::Read(::grpc::ServerContext* context, const ReadRequest* request, ReadResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  ViSession vi = VI_NULL;
  try {
    auto session = request->vi();
    vi = session_repository_->access_session(session.name());
    auto channel_list_mbcs = convert_from_grpc<std::string>(request->channel_list());
    ViConstString channel_list = channel_list_mbcs.c_str();
    ViReal64 timeout = request->timeout();
    ViInt32 num_samples = request->num_samples();
    if (num_samples < 0) {
      CheckStatus(library_->ActualRecordLength(vi, &num_samples));
    }

    ViInt32 num_waveforms;
    CheckStatus(library_->ActualNumWfms(vi, channel_list, &num_waveforms));

    response->mutable_waveform()->Resize(num_samples * num_waveforms, 0.0);
    ViReal64* waveform = response->mutable_waveform()->mutable_data();
    std::vector<niScope_wfmInfo> waveform_info(num_waveforms, niScope_wfmInfo());
    auto status = library_->Read(vi, channel_list, timeout, num_samples, waveform, waveform_info.data());
    if (status < VI_SUCCESS) {
      return ConvertApiErrorStatusForViSession(context, status, vi);
    }
    response->set_status(status);
    convert_to_grpc(waveform_info, response->mutable_wfm_info());
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
  catch (const DriverWarningOrErrorException& ex) {
    if (ex.status_ < VI_SUCCESS) {
      return ConvertApiErrorStatusForViSession(context, ex.status_, vi);
    }
    response->set_status(ex.status_);
    return ::grpc::Status::OK;
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status NiScopeService::FetchComplex(::grpc::ServerContext* context, const FetchComplexRequest* request, FetchComplexResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  ViSession vi = VI_NULL;
  try {
    auto session = request->vi();
    vi = session_repository_->access_session(session.name());
    auto channel_list_mbcs = convert_from_grpc<std::string>(request->channel_list());
    ViConstString channel_list = channel_list_mbcs.c_str();
    ViReal64 timeout = request->timeout();
    ViInt32 num_samples = request->num_samples();
    if (num_samples < 0) {
      CheckStatus(library_->ActualRecordLength(vi, &num_samples));
    }

    ViInt32 num_waveforms;
    CheckStatus(library_->ActualNumWfms(vi, channel_list, &num_waveforms));

    std::vector<NIComplexNumber_struct> waveform(num_samples * num_waveforms, NIComplexNumber_struct());
    std::vector<niScope_wfmInfo> waveform_info(num_waveforms, niScope_wfmInfo());
    auto status = library_->FetchComplex(vi, channel_list, timeout, num_samples, waveform.data(), waveform_info.data());
    if (status < VI_SUCCESS) {
      return ConvertApiErrorStatusForViSession(context, status, vi);
    }
    response->set_status(status);
    convert_to_grpc(waveform, response->mutable_wfm());
    convert_to_grpc(waveform_info, response->mutable_wfm_info());
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
  catch (const DriverWarningOrErrorException& ex) {
    if (ex.status_ < VI_SUCCESS) {
      return ConvertApiErrorStatusForViSession(context, ex.status_, vi);
    }
    response->set_status(ex.status_);
    return ::grpc::Status::OK;
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status NiScopeService::FetchComplexBinary16(::grpc::ServerContext* context, const FetchComplexBinary16Request* request, FetchComplexBinary16Response* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  ViSession vi = VI_NULL;
  try {
    auto session = request->vi();
    vi = session_repository_->access_session(session.name());
    auto channel_list_mbcs = convert_from_grpc<std::string>(request->channel_list());
    ViConstString channel_list = channel_list_mbcs.c_str();
    ViReal64 timeout = request->timeout();
    ViInt32 num_samples = request->num_samples();
    if (num_samples < 0) {
      CheckStatus(library_->ActualRecordLength(vi, &num_samples));
    }

    ViInt32 num_waveforms;
    CheckStatus(library_->ActualNumWfms(vi, channel_list, &num_waveforms));

    std::vector<NIComplexI16_struct> waveform(num_samples * num_waveforms, NIComplexI16_struct());
    std::vector<niScope_wfmInfo> waveform_info(num_waveforms, niScope_wfmInfo());
    auto status = library_->FetchComplexBinary16(vi, channel_list, timeout, num_samples, waveform.data(), waveform_info.data());
    if (status < VI_SUCCESS) {
      return ConvertApiErrorStatusForViSession(context, status, vi);
    }
    response->set_status(status);
    convert_to_grpc(waveform, response->mutable_wfm());
    convert_to_grpc(waveform_info, response->mutable_wfm_info());
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
  catch (const DriverWarningOrErrorException& ex) {
    if (ex.status_ < VI_SUCCESS) {
      return ConvertApiErrorStatusForViSession(context, ex.status_, vi);
    }
    response->set_status(ex.status_);
    return ::grpc::Status::OK;
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status NiScopeService::FetchMeasurement(::grpc::ServerContext* context, const FetchMeasurementRequest* request, FetchMeasurementResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  ViSession vi = VI_NULL;
  try {
    auto session = request->vi();
    vi = session_repository_->access_session(session.name());
    auto channel_list_mbcs = convert_from_grpc<std::string>(request->channel_list());
    ViConstString channel_list = channel_list_mbcs.c_str();
    ViReal64 timeout = request->timeout();
    ViInt32 scalar_meas_function;
    switch (request->scalar_meas_function_enum_case()) {
      case niscope_grpc::FetchMeasurementRequest::ScalarMeasFunctionEnumCase::kScalarMeasFunction:
        scalar_meas_function = (ViInt32)request->scalar_meas_function();
        break;
      case niscope_grpc::FetchMeasurementRequest::ScalarMeasFunctionEnumCase::kScalarMeasFunctionRaw:
        scalar_meas_function = (ViInt32)request->scalar_meas_function_raw();
        break;
      case niscope_grpc::FetchMeasurementRequest::ScalarMeasFunctionEnumCase::SCALAR_MEAS_FUNCTION_ENUM_NOT_SET:
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for scalar_meas_function was not specified or out of range");
        break;
    }

    ViInt32 num_waveforms;
    CheckStatus(library_->ActualNumWfms(vi, channel_list, &num_waveforms));

    response->mutable_result()->Resize(num_waveforms, 0.0);
    ViReal64* result = response->mutable_result()->mutable_data();
    auto status = library_->FetchMeasurement(vi, channel_list, timeout, scalar_meas_function, result);
    if (status < VI_SUCCESS) {
      return ConvertApiErrorStatusForViSession(context, status, vi);
    }
    response->set_status(status);
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
  catch (const DriverWarningOrErrorException& ex) {
    if (ex.status_ < VI_SUCCESS) {
      return ConvertApiErrorStatusForViSession(context, ex.status_, vi);
    }
    response->set_status(ex.status_);
    return ::grpc::Status::OK;
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status NiScopeService::ReadMeasurement(::grpc::ServerContext* context, const ReadMeasurementRequest* request, ReadMeasurementResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  ViSession vi = VI_NULL;
  try {
    auto session = request->vi();
    vi = session_repository_->access_session(session.name());
    auto channel_list_mbcs = convert_from_grpc<std::string>(request->channel_list());
    ViConstString channel_list = channel_list_mbcs.c_str();
    ViReal64 timeout = request->timeout();
    ViInt32 scalar_meas_function;
    switch (request->scalar_meas_function_enum_case()) {
      case niscope_grpc::ReadMeasurementRequest::ScalarMeasFunctionEnumCase::kScalarMeasFunction:
        scalar_meas_function = (ViInt32)request->scalar_meas_function();
        break;
      case niscope_grpc::ReadMeasurementRequest::ScalarMeasFunctionEnumCase::kScalarMeasFunctionRaw:
        scalar_meas_function = (ViInt32)request->scalar_meas_function_raw();
        break;
      case niscope_grpc::ReadMeasurementRequest::ScalarMeasFunctionEnumCase::SCALAR_MEAS_FUNCTION_ENUM_NOT_SET:
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for scalar_meas_function was not specified or out of range");
        break;
    }

    ViInt32 num_waveforms;
    CheckStatus(library_->ActualNumWfms(vi, channel_list, &num_waveforms));

    response->mutable_result()->Resize(num_waveforms, 0.0);
    ViReal64* result = response->mutable_result()->mutable_data();
    auto status = library_->ReadMeasurement(vi, channel_list, timeout, scalar_meas_function, result);
    if (status < VI_SUCCESS) {
      return ConvertApiErrorStatusForViSession(context, status, vi);
    }
    response->set_status(status);
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
  catch (const DriverWarningOrErrorException& ex) {
    if (ex.status_ < VI_SUCCESS) {
      return ConvertApiErrorStatusForViSession(context, ex.status_, vi);
    }
    response->set_status(ex.status_);
    return ::grpc::Status::OK;
  }
}

::grpc::Status NiScopeService::ConvertApiErrorStatusForViSession(::grpc::ServerContextBase* context, int32_t status, ViSession vi)
{
  ViStatus error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  // Try first to get the most recent error with a dynamic message.
  library_->GetError(vi, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  if (error_code != status) {
    // Since another thread has changed the status, fall back to the static message lookup.
    description.assign(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
    library_->GetErrorMessage(vi, status, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace niscope_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/niswitch_service.custom.cpp sha256=ce9f3d29a468445efb332aacab0d38065791b67c643cb4a132350b1666171446 bytes=986 -->
## FILE: source/custom/niswitch_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/niswitch_service.custom.cpp`
- sha256: `ce9f3d29a468445efb332aacab0d38065791b67c643cb4a132350b1666171446`
- bytes: 986

````cpp
#include <niswitch/niswitch_service.h>

namespace niswitch_grpc {

::grpc::Status NiSwitchService::ConvertApiErrorStatusForViSession(::grpc::ServerContextBase* context, int32_t status, ViSession vi)
{
  static_assert(nidevice_grpc::kMaxGrpcErrorDescriptionSize >= 256, "ErrorMessage expects a minimum buffer size.");
  ViStatus error_code{};
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  // Try first to get the most recent error with a dynamic message.
  library_->GetError(vi, &error_code, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  if (error_code != status) {
    // Since another thread has changed the status, fall back to the static message lookup.
    description.assign(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
    library_->ErrorMessage(vi, status, &description[0]);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace niswitch_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nisync_service.custom.cpp sha256=35d0336152c0f7b6ddc10553774552826451a1c448a03be5c5a1a29108a3c9f7 bytes=2897 -->
## FILE: source/custom/nisync_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nisync_service.custom.cpp`
- sha256: `35d0336152c0f7b6ddc10553774552826451a1c448a03be5c5a1a29108a3c9f7`
- bytes: 2897

````cpp
#include <nisync/nisync_service.h>

namespace nisync_grpc {
using nidevice_grpc::converters::convert_from_grpc;

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status NiSyncService::ReadMultipleTriggerTimeStamp(::grpc::ServerContext* context, const ReadMultipleTriggerTimeStampRequest* request, ReadMultipleTriggerTimeStampResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto vi_grpc_session = request->vi();
    ViSession vi = session_repository_->access_session(vi_grpc_session.name());
    auto terminal_mbcs = convert_from_grpc<std::string>(request->terminal());
    ViConstString terminal = terminal_mbcs.c_str();
    ViUInt32 timestamps_to_read = request->timestamps_to_read();
    ViReal64 timeout = request->timeout();
    response->mutable_time_seconds_buffer()->Resize(timestamps_to_read, 0);
    ViUInt32* time_seconds_buffer = reinterpret_cast<ViUInt32*>(response->mutable_time_seconds_buffer()->mutable_data());
    response->mutable_time_nanoseconds_buffer()->Resize(timestamps_to_read, 0);
    ViUInt32* time_nanoseconds_buffer = reinterpret_cast<ViUInt32*>(response->mutable_time_nanoseconds_buffer()->mutable_data());
    response->mutable_time_fractional_nanoseconds_buffer()->Resize(timestamps_to_read, 0);
    ViUInt16* time_fractional_nanoseconds_buffer = reinterpret_cast<ViUInt16*>(response->mutable_time_fractional_nanoseconds_buffer()->mutable_data());
    response->mutable_detected_edge_buffer()->Resize(timestamps_to_read, 0);
    ViInt32* detected_edge_buffer = reinterpret_cast<ViInt32*>(response->mutable_detected_edge_buffer()->mutable_data());
    ViUInt32 timestamps_read{};
    auto status = library_->ReadMultipleTriggerTimeStamp(vi, terminal, timestamps_to_read, timeout, time_seconds_buffer, time_nanoseconds_buffer, time_fractional_nanoseconds_buffer, detected_edge_buffer, &timestamps_read);
    if (status < VI_SUCCESS && status != NISYNC_ERROR_DRIVER_TIMEOUT) {
      return ConvertApiErrorStatusForViSession(context, status, vi);
    }
    response->set_status(status);
    response->set_timestamps_read(timestamps_read);
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

::grpc::Status NiSyncService::ConvertApiErrorStatusForViSession(::grpc::ServerContextBase* context, int32_t status, ViSession vi)
{
  static_assert(nidevice_grpc::kMaxGrpcErrorDescriptionSize >= 256, "ErrorMessage expects a minimum buffer size.");
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  library_->ErrorMessage(vi, status, &description[0]);
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace nisync_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nitclk_service.custom.cpp sha256=dc0a3d9385b83ead6342b860cdaf5a8730f0415fbc0e500b3872a4b5e4829c82 bytes=641 -->
## FILE: source/custom/nitclk_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nitclk_service.custom.cpp`
- sha256: `dc0a3d9385b83ead6342b860cdaf5a8730f0415fbc0e500b3872a4b5e4829c82`
- bytes: 641

````cpp
#include <nitclk/nitclk_service.h>

#include <stdexcept>

namespace nitclk_grpc {
const auto kErrorReadBufferTooSmall = -200229;
const auto kWarningCAPIStringTruncatedToFitBuffer = 200026;

::grpc::Status NiTClkService::ConvertApiErrorStatusForViSession(::grpc::ServerContextBase* context, int32_t status, ViSession session_number)
{
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  library_->GetExtendedErrorInfo(&description[0], nidevice_grpc::kMaxGrpcErrorDescriptionSize);
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace nitclk_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nixnet_converters.h sha256=e59b8ab6fd849892690d404e24c5f00c2da35ba34f775e579d13e6f20cb26579 bytes=9771 -->
## FILE: source/custom/nixnet_converters.h

- repository: `ni/grpc-device`
- source_path: `source/custom/nixnet_converters.h`
- sha256: `e59b8ab6fd849892690d404e24c5f00c2da35ba34f775e579d13e6f20cb26579`
- bytes: 9771

````c
#ifndef NIDEVICE_GRPC_DEVICE_NIXNET_CONVERTERS_H
#define NIDEVICE_GRPC_DEVICE_NIXNET_CONVERTERS_H
#include <nixnet.h>
#include <nixnet.pb.h>

#include "server/converters.h"

namespace nixnet_grpc {
namespace converters {
void SetCanCommResponse(const u32 input, nixnet_grpc::CanCommResponse* output);
void SetFlexRayCommResponse(const u32 input, nixnet_grpc::FlexRayCommResponse* output);
void SetLinCommResponse(const u32* input, nixnet_grpc::LinCommResponse* output);
void SetSessionInfoResponse(const u32& input, nixnet_grpc::SessionInfoResponse* output);
}  // namespace converters

constexpr auto ENET_FRAME_HEADER_LENGTH = static_cast<u16>(sizeof(nxFrameEnet_t) - 1);  // last byte in nxFrameEnet_t is u8 FrameData[1]
constexpr auto ENET_FRAME_FCS_SIZE = 4;

u32 get_frame_buffer_size(int32 number_of_frames, u32 max_payload_size, u32 protocol);

struct FrameHolder {
  FrameHolder(const ::google::protobuf::RepeatedPtrField<FrameBufferRequest>& input, std::map<std::int32_t, std::int32_t> enetflags_input_map)
  {
    // all frames in repeated field must be of same type
    switch (input[0].frame_case()) {
      case FrameBufferRequest::kCan:
        InitializeCanFrames(input);
        break;
      case FrameBufferRequest::kLin:
        InitializeLinFrames(input);
        break;
      case FrameBufferRequest::kFlexRay:
        InitializeFlexRayFrames(input);
        break;
      case FrameBufferRequest::kJ1939:
        InitializeJ1939Frames(input);
        break;
      case FrameBufferRequest::kEnet:
        InitializeEnetFrames(input, enetflags_input_map);
        break;
      default:
        throw std::invalid_argument("The value for FrameBufferRequest not specified or not supported");
        break;
    }
  }

  void InitializeCanFrames(const ::google::protobuf::RepeatedPtrField<FrameBufferRequest>& input)
  {
    std::vector<uint8_t> frame_data;
    for (auto grpc_frame : input) {
      if (!grpc_frame.has_can()) {
        throw std::invalid_argument("All FrameBufferRequest instances in repeated field should have same oneof set for the frame");
      }
      ConvertFrame(grpc_frame.can(), frame_data);

      frame_buffer.insert(frame_buffer.end(), frame_data.begin(), frame_data.end());
    }
  }

  void InitializeLinFrames(const ::google::protobuf::RepeatedPtrField<FrameBufferRequest>& input)
  {
    std::vector<uint8_t> frame_data;
    for (auto grpc_frame : input) {
      if (!grpc_frame.has_lin()) {
        throw std::invalid_argument("All FrameBufferRequest instances in repeated field should have same oneof set for the frame");
      }
      ConvertFrame(grpc_frame.lin(), frame_data);

      frame_buffer.insert(frame_buffer.end(), frame_data.begin(), frame_data.end());
    }
  }

  void InitializeFlexRayFrames(const ::google::protobuf::RepeatedPtrField<FrameBufferRequest>& input)
  {
    std::vector<uint8_t> frame_data;
    for (auto grpc_frame : input) {
      if (!grpc_frame.has_flex_ray()) {
        throw std::invalid_argument("All FrameBufferRequest instances in repeated field should have same oneof set for the frame");
      }
      ConvertFrame(grpc_frame.flex_ray(), frame_data);

      frame_buffer.insert(frame_buffer.end(), frame_data.begin(), frame_data.end());
    }
  }

  void InitializeJ1939Frames(const ::google::protobuf::RepeatedPtrField<FrameBufferRequest>& input)
  {
    std::vector<uint8_t> frame_data;
    for (auto grpc_frame : input) {
      if (!grpc_frame.has_j1939()) {
        throw std::invalid_argument("All FrameBufferRequest instances in repeated field should have same oneof set for the frame");
      }
      ConvertFrame(grpc_frame.j1939(), frame_data);

      frame_buffer.insert(frame_buffer.end(), frame_data.begin(), frame_data.end());
    }
  }

  void InitializeEnetFrames(const ::google::protobuf::RepeatedPtrField<FrameBufferRequest>& input, std::map<std::int32_t, std::int32_t> enetflags_input_map)
  {
    std::vector<uint8_t> frame_data;
    for (auto grpc_frame : input) {
      if (!grpc_frame.has_enet()) {
        throw std::invalid_argument("All FrameBufferRequest instances in repeated field should have same oneof set for the frame");
      }

      u32 frame_size = get_frame_buffer_size(1, static_cast<u32>(grpc_frame.enet().frame_data().length()), Protocol::PROTOCOL_ENET);
      frame_data.resize(frame_size, 0);
      nxFrameEnet_t* current_frame = (nxFrameEnet_t*)frame_data.data();
      // The Length field in ENET write frame is big-endian. Typecast to u16 before doing the conversion
      // as lengh field is 16 bits and BigToHostOrder16 works only for 16 bits.
      current_frame->Length = BigToHostOrder16(frame_size);
      switch (grpc_frame.enet().type_enum_case()) {
        case nixnet_grpc::EnetFrameRequest::TypeEnumCase::kType: {
          current_frame->Type = static_cast<u8>(grpc_frame.enet().type());
          break;
        }
        case nixnet_grpc::EnetFrameRequest::TypeEnumCase::kTypeRaw: {
          current_frame->Type = static_cast<u8>(grpc_frame.enet().type_raw());
          break;
        }
        case nixnet_grpc::EnetFrameRequest::TypeEnumCase::TYPE_ENUM_NOT_SET: {
          throw std::invalid_argument("The value for type was not specified or out of range");
        }
      }
      current_frame->DeviceTimestamp = grpc_frame.enet().device_timestamp();
      current_frame->NetworkTimestamp = grpc_frame.enet().network_timestamp();
      current_frame->Flags = 0;
      for (int i = 0; i < grpc_frame.enet().flags_mapped_size(); i++) {
        auto enet_flags_enum_imap_it = enetflags_input_map.find(grpc_frame.enet().flags_mapped()[i]);
        if (enet_flags_enum_imap_it == enetflags_input_map.end()) {
          return throw std::invalid_argument("The value for enet flags was not specified or out of range.");
        }
        current_frame->Flags = current_frame->Flags | enet_flags_enum_imap_it->second;
      }
      std::memcpy(
          current_frame->FrameData,
          grpc_frame.enet().frame_data().data(),
          grpc_frame.enet().frame_data().length());

      frame_buffer.insert(frame_buffer.end(), frame_data.begin(), frame_data.end());
    }
  }

  void ConvertFrame(const FrameRequest& input, std::vector<uint8_t>& output)
  {
    auto payload_length = input.payload().length();
    auto frame_size = nxFrameSize(payload_length);

    // We need to clear the output buffer since it is being reused for multiple frames.
    // Not clearing it might result in stale data from the previous frame into this one.
    output.clear();
    output.resize(frame_size, 0);
    nxFrameVar_t* current_frame = (nxFrameVar_t*)output.data();
    current_frame->Timestamp = input.timestamp();
    current_frame->Identifier = input.identifier();
    switch (input.type_enum_case()) {
      case nixnet_grpc::FrameRequest::TypeEnumCase::kType: {
        current_frame->Type = static_cast<u8>(input.type());
        break;
      }
      case nixnet_grpc::FrameRequest::TypeEnumCase::kTypeRaw: {
        current_frame->Type = static_cast<u8>(input.type_raw());
        break;
      }
      case nixnet_grpc::FrameRequest::TypeEnumCase::TYPE_ENUM_NOT_SET: {
        throw std::invalid_argument("The value for type was not specified or out of range");
      }
    }
    current_frame->Flags = 0;
    for (int i = 0; i < input.flags_size(); i++) {
      current_frame->Flags = current_frame->Flags | input.flags()[i];
    }
    current_frame->Info = input.info();
    nxFrameSetPayloadLength(current_frame, payload_length);
    std::memcpy(
        current_frame->Payload,
        input.payload().data(),
        payload_length);
  }

  // Implicit conversion to u8* simplifies codegen because these are passed by pointer to
  // the driver.
  operator u8*()
  {
    return frame_buffer.data();
  }

  operator const u8*() const
  {
    return frame_buffer.data();
  }

  // size() method is used to simplify codegen calculating the size of the
  // selected frame buffer.
  uint32_t size() const
  {
    // size_of_buffer param for all frame APIs is uint32, we can't possibly exceed that.
    return (uint32_t)frame_buffer.size();
  }

  std::vector<uint8_t> frame_buffer;
};

void convert_to_grpc(std::vector<u8>& input, google::protobuf::RepeatedPtrField<nixnet_grpc::FrameBufferResponse>* output, u32 number_of_bytes, u32 protocol, std::map<std::int32_t, std::int32_t> enetflags_output_map);

void convert_to_grpc(const void* input, nixnet_grpc::FrameBufferResponse* output, u32 protocol, std::map<std::int32_t, std::int32_t> enetflags_output_map);

template <typename TFrame>
nixnet_grpc::FrameHolder convert_from_grpc(const ::google::protobuf::RepeatedPtrField<nixnet_grpc::FrameBufferRequest>& input, std::map<std::int32_t, std::int32_t> enetflags_input_map)
{
  return nixnet_grpc::FrameHolder(input, enetflags_input_map);
}

void convert_to_grpc(std::vector<f64>& input, google::protobuf::RepeatedField<double>* output, u32 number_of_values_returned, u32 number_of_signals);
}  // namespace nixnet_grpc

namespace nidevice_grpc {
namespace converters {
template <>
void convert_to_grpc(const _nxFlexRayStats_t& input, nixnet_grpc::FlexRayStats* output);
template <>
void convert_to_grpc(const _nxJ1939CommState_t& input, nixnet_grpc::J1939CommState* output);
template <>
void convert_to_grpc(const nxEptRxFilter_Element_t& input, nixnet_grpc::EptRxFilter* output);
template <>
nxEptRxFilter_Element_t convert_from_grpc(const nixnet_grpc::EptRxFilter& input);
}  // namespace converters
}  // namespace nidevice_grpc

#endif /* NIDEVICE_GRPC_DEVICE_NIXNET_CONVERTERS_H */
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nixnet_service.custom.cpp sha256=e20018ba547190d32bee356ddbd2bd38b7dc2fe1a1e8000ab4f2cb0b970bbfcd bytes=63780 -->
## FILE: source/custom/nixnet_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nixnet_service.custom.cpp`
- sha256: `e20018ba547190d32bee356ddbd2bd38b7dc2fe1a1e8000ab4f2cb0b970bbfcd`
- bytes: 63780

````cpp
#include <custom/nixnet_converters.h>
#include <nixnet.pb.h>
#include <nixnet/nixnet_service.h>
#include <server/converters.h>

#include <stdexcept>

using namespace nixnet_grpc::converters;

namespace nixnet_grpc {
using nidevice_grpc::converters::convert_from_grpc;
using nidevice_grpc::converters::convert_to_grpc;

namespace converters {
// Helper to read fields of u32 returned by nxReadState of nxState_CANComm and set them on gRPC message
void SetCanCommResponse(const u32 input, nixnet_grpc::CanCommResponse* output)
{
  u32 comm_state = nxCANComm_Get_CommState(input);
  u32 last_error = nxCANComm_Get_LastErr(input);

  output->set_comm_state(static_cast<nixnet_grpc::CanCommState>(comm_state));
  output->set_comm_state_raw(comm_state);
  output->set_transceiver_error(nxCANComm_Get_TcvrErr(input));
  output->set_sleep(nxCANComm_Get_Sleep(input));
  output->set_last_error(static_cast<nixnet_grpc::CanLastErr>(last_error));
  output->set_last_error_raw(last_error);
  output->set_transmit_error_counter(nxCANComm_Get_TxErrCount(input));
  output->set_receive_error_counter(nxCANComm_Get_RxErrCount(input));
}

// Helper to read fields of u32 returned by nxReadState of nxState_FlexRayComm and set them on gRPC message
void SetFlexRayCommResponse(const u32 input, nixnet_grpc::FlexRayCommResponse* output)
{
  u32 poc_state = nxFlexRayComm_Get_POCState(input);

  output->set_poc_state(static_cast<nixnet_grpc::FlexRayPocState>(poc_state));
  output->set_poc_state_raw(poc_state);
  output->set_clock_correction_failed(nxFlexRayComm_Get_ClockCorrFailed(input));
  output->set_passive_to_active_count(nxFlexRayComm_Get_PassiveToActiveCount(input));
  output->set_channel_a_sleep(nxFlexRayComm_Get_ChannelASleep(input));
  output->set_channel_b_sleep(nxFlexRayComm_Get_ChannelBSleep(input));
}

// Helper to read two fields of u32 returned by nxReadState of nxState_LINComm and set them on gRPC message
void SetLinCommResponse(const u32* input, nixnet_grpc::LinCommResponse* output)
{
  u32 comm_state = nxLINComm_Get_CommState(input[0]);
  output->set_sleep(nxLINComm_Get_Sleep(input[0]));
  output->set_comm_state(static_cast<nixnet_grpc::LinCommState>(comm_state));
  output->set_comm_state_raw(comm_state);
  output->set_last_error(nxLINComm_Get_LastErrCode(input[0]));
  output->set_last_error_received(nxLINComm_Get_LastErrReceived(input[0]));
  output->set_last_error_expected(nxLINComm_Get_LastErrExpected(input[0]));
  output->set_last_error_id(nxLINComm_Get_LastErrID(input[0]));
  output->set_transceiver_ready(nxLINComm_Get_TcvrRdy(input[0]));
  output->set_schedule_index(nxLINComm_Get2_ScheduleIndex(input[1]));
}

// Helper to read fields of u32 returned by nxReadState of nxState_SessionInfo and set them on gRPC message
void SetSessionInfoResponse(const u32& input, nixnet_grpc::SessionInfoResponse* output)
{
  output->set_info(static_cast<nixnet_grpc::SessionInfoState>(input));
  output->set_info_raw(input);
}
}  // namespace converters

// Returns true if it's safe to use outputs of a method with the given status.
inline bool status_ok(int32 status)
{
  return status >= 0;
}

// Helper to compute the StateSize based on the StateID
u32 GetStateSize(u32 state_id)
{
  u32 state_size;
  switch (state_id) {
    case nixnet_grpc::ReadState::READ_STATE_TIME_CURRENT:
    case nixnet_grpc::ReadState::READ_STATE_TIME_COMMUNICATING:
    case nixnet_grpc::ReadState::READ_STATE_TIME_START: {
      state_size = sizeof(nxTimestamp100ns_t);
      break;
    }
    case nixnet_grpc::ReadState::READ_STATE_CAN_COMM:
    case nixnet_grpc::ReadState::READ_STATE_FLEX_RAY_COMM:
    case nixnet_grpc::ReadState::READ_STATE_SESSION_INFO: {
      state_size = sizeof(u32);
      break;
    }
    case nixnet_grpc::ReadState::READ_STATE_FLEX_RAY_STATS: {
      state_size = sizeof(nxFlexRayStats_t);
      break;
    }
    case nixnet_grpc::ReadState::READ_STATE_LIN_COMM: {
      // The StateValue for nxState_LinComm should point to a u32 array with 2 elements.
      state_size = sizeof(u32) * 2;
      break;
    }
    case nixnet_grpc::ReadState::READ_STATE_J1939_COMM: {
      state_size = sizeof(nxJ1939CommState_t);
      break;
    }
    case nixnet_grpc::ReadState::READ_STATE_TIME_CURRENT_2:
    case nixnet_grpc::ReadState::READ_STATE_TIME_COMMUNICATING_2:
    case nixnet_grpc::ReadState::READ_STATE_TIME_START_2: {
      state_size = sizeof(nxTimeLocalNetwork_t);
      break;
    }
    default: {
      throw std::invalid_argument("The value for state_id was not specified or out of range");
    }
  }
  return state_size;
}

// Helper to get the LinDiagnosticScheduleChange value
u32 GetLinDiagnosticScheduleChangeValue(const WriteStateRequest* request)
{
  u32 state_value;
  switch (request->state_value().lin_diagnostic_schedule_change().schedule_enum_case()) {
    case nixnet_grpc::LinDiagnosticScheduleChangeRequest::ScheduleEnumCase::kSchedule: {
      state_value = static_cast<u32>(request->state_value().lin_diagnostic_schedule_change().schedule());
      break;
    }
    case nixnet_grpc::LinDiagnosticScheduleChangeRequest::ScheduleEnumCase::kScheduleRaw: {
      state_value = static_cast<u32>(request->state_value().lin_diagnostic_schedule_change().schedule_raw());
      break;
    }
    case nixnet_grpc::LinDiagnosticScheduleChangeRequest::ScheduleEnumCase::SCHEDULE_ENUM_NOT_SET: {
      throw std::invalid_argument("The value for Lin Diagnostic Schedule Change was not specified or out of range");
    }
  }
  return state_value;
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
// ReadState API has an output parameter of type void * called StateValue. Based on the value of StateID,
// StateValue can point to u32, nxTimestamp100ns_t, _nxFlexRayStats_t, etc. which are of different sizes.
// Based on the StateID, we are setting the size of StateValue and after calling the ReadState API, the
// response is set appropriately.
::grpc::Status NiXnetService::ReadState(::grpc::ServerContext* context, const ReadStateRequest* request, ReadStateResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto session_grpc_session = request->session();
    nxSessionRef_t session = session_repository_->access_session(session_grpc_session.name());
    u32 state_id;
    switch (request->state_id_enum_case()) {
      case nixnet_grpc::ReadStateRequest::StateIdEnumCase::kStateId: {
        state_id = static_cast<u32>(request->state_id());
        break;
      }
      case nixnet_grpc::ReadStateRequest::StateIdEnumCase::kStateIdRaw: {
        state_id = static_cast<u32>(request->state_id_raw());
        break;
      }
      case nixnet_grpc::ReadStateRequest::StateIdEnumCase::STATE_ID_ENUM_NOT_SET: {
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for state_id was not specified or out of range");
        break;
      }
    }

    u32 state_size = GetStateSize(state_id);
    response->mutable_state_value()->mutable_state_value_raw()->resize(state_size, 0);
    nxStatus_t fault{};

    auto status = library_->ReadState(session, state_id, state_size, const_cast<char*>(response->mutable_state_value()->mutable_state_value_raw()->data()), &fault);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForNxSessionRef_t(context, status, session);
    }
    response->set_status(status);
    void* state_value_raw = (void*)response->state_value().state_value_raw().data();
    switch (state_id) {
      case nixnet_grpc::ReadState::READ_STATE_TIME_CURRENT: {
        response->mutable_state_value()->set_time_current(*(nxTimestamp100ns_t*)state_value_raw);
        break;
      }
      case nixnet_grpc::ReadState::READ_STATE_TIME_COMMUNICATING: {
        response->mutable_state_value()->set_time_communicating(*(nxTimestamp100ns_t*)state_value_raw);
        break;
      }
      case nixnet_grpc::ReadState::READ_STATE_TIME_START: {
        response->mutable_state_value()->set_time_start(*(nxTimestamp100ns_t*)state_value_raw);
        break;
      }
      case nixnet_grpc::ReadState::READ_STATE_CAN_COMM: {
        SetCanCommResponse(*(u32*)state_value_raw, response->mutable_state_value()->mutable_can_comm());
        break;
      }
      case nixnet_grpc::ReadState::READ_STATE_FLEX_RAY_COMM: {
        SetFlexRayCommResponse(*(u32*)state_value_raw, response->mutable_state_value()->mutable_flex_ray_comm());
        break;
      }
      case nixnet_grpc::ReadState::READ_STATE_LIN_COMM: {
        SetLinCommResponse((u32*)state_value_raw, response->mutable_state_value()->mutable_lin_comm());
        break;
      }
      case nixnet_grpc::ReadState::READ_STATE_SESSION_INFO: {
        SetSessionInfoResponse(*(u32*)state_value_raw, response->mutable_state_value()->mutable_session_info());
        break;
      }
      case nixnet_grpc::ReadState::READ_STATE_FLEX_RAY_STATS: {
        convert_to_grpc(*(_nxFlexRayStats_t*)state_value_raw, response->mutable_state_value()->mutable_flex_ray_stats());
        break;
      }
      case nixnet_grpc::ReadState::READ_STATE_J1939_COMM: {
        convert_to_grpc(*(_nxJ1939CommState_t*)state_value_raw, response->mutable_state_value()->mutable_j1939_comm_state());
        break;
      }
      case nixnet_grpc::ReadState::READ_STATE_TIME_CURRENT_2: {
        convert_to_grpc(*(_nxTimeLocalNetwork_t*)state_value_raw, response->mutable_state_value()->mutable_time_current2());
        break;
      }
      case nixnet_grpc::ReadState::READ_STATE_TIME_COMMUNICATING_2: {
        convert_to_grpc(*(_nxTimeLocalNetwork_t*)state_value_raw, response->mutable_state_value()->mutable_time_communicating2());
        break;
      }
      case nixnet_grpc::ReadState::READ_STATE_TIME_START_2: {
        convert_to_grpc(*(_nxTimeLocalNetwork_t*)state_value_raw, response->mutable_state_value()->mutable_time_start2());
        break;
      }
      default: {
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for state_id was not specified or out of range");
      }
    }
    response->set_fault(fault);
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
// WriteState API has an input of type void * called StateValue. There are different possible values for
// StateValue based on the value of StateID passed in by user. We have defined complex message
// for StateValue with fields correponding to each of these StateIds in oneof. We have to assert that
// correct StateValue oneof is set by user based on StateId passed in. This requires custom implementation.
::grpc::Status NiXnetService::WriteState(::grpc::ServerContext* context, const WriteStateRequest* request, WriteStateResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto session_grpc_session = request->session();
    nxSessionRef_t session = session_repository_->access_session(session_grpc_session.name());
    u32 state_id;
    switch (request->state_id_enum_case()) {
      case nixnet_grpc::WriteStateRequest::StateIdEnumCase::kStateId: {
        state_id = static_cast<u32>(request->state_id());
        break;
      }
      case nixnet_grpc::WriteStateRequest::StateIdEnumCase::kStateIdRaw: {
        state_id = static_cast<u32>(request->state_id_raw());
        break;
      }
      case nixnet_grpc::WriteStateRequest::StateIdEnumCase::STATE_ID_ENUM_NOT_SET: {
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for state_id was not specified or out of range");
        break;
      }
    }

    u32 state_size = sizeof(u32);
    u32 state_value;
    switch (request->state_value().value_case()) {
      case nixnet_grpc::WriteStateValue::ValueCase::kLinScheduleChange: {
        if (state_id != nixnet_grpc::WriteState::WRITE_STATE_LIN_SCHEDULE_CHANGE) {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "StateValue for specified StateID is not set");
        }
        state_value = request->state_value().lin_schedule_change();
        break;
      }
      case nixnet_grpc::WriteStateValue::ValueCase::kFlexRaySymbol: {
        if (state_id != nixnet_grpc::WriteState::WRITE_STATE_FLEX_RAY_SYMBOL) {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "StateValue for specified StateID is not set");
        }
        state_value = request->state_value().flex_ray_symbol();
        break;
      }
      case nixnet_grpc::WriteStateValue::ValueCase::kLinDiagnosticScheduleChange: {
        if (state_id != nixnet_grpc::WriteState::WRITE_STATE_LIN_DIAGNOSTIC_SCHEDULE_CHANGE) {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "StateValue for specified StateID is not set");
        }
        state_value = GetLinDiagnosticScheduleChangeValue(request);
        break;
      }
      case nixnet_grpc::WriteStateValue::ValueCase::kEthernetSleep: {
        if (state_id != nixnet_grpc::WriteState::WRITE_STATE_ETHERNET_SLEEP) {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "StateValue for specified StateID is not set");
        }
        state_value = request->state_value().ethernet_sleep();
        break;
      }
      case nixnet_grpc::WriteStateValue::ValueCase::kEthernetWake: {
        if (state_id != nixnet_grpc::WriteState::WRITE_STATE_ETHERNET_WAKE) {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "StateValue for specified StateID is not set");
        }
        state_value = request->state_value().ethernet_wake();
        break;
      }
      default: {
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for state_id was not specified or out of range");
      }
    }
    auto status = library_->WriteState(session, state_id, state_size, &state_value);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForNxSessionRef_t(context, status, session);
    }
    response->set_status(status);
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
// GetProperty API has an output of type void * which has different possible values based on PropertyId
// passed in by user. We have defined complex message with oneof corresponding to each of these possible
// value types. Based on PropertyId passed in, we need to interpret data returned by library and populate
// corresponding fields in the response. This requires custom implementation.
::grpc::Status NiXnetService::GetProperty(::grpc::ServerContext* context, const GetPropertyRequest* request, GetPropertyResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  nidevice_grpc::Session session_grpc_session;
  try {
    switch (request->session_repository_case()) {
      case nixnet_grpc::GetPropertyRequest::SessionRepositoryCase::kDevice: {
        session_grpc_session = request->device();
        break;
      }
      case nixnet_grpc::GetPropertyRequest::SessionRepositoryCase::kInterfaceRef: {
        session_grpc_session = request->interface_ref();
        break;
      }
      case nixnet_grpc::GetPropertyRequest::SessionRepositoryCase::kSession: {
        session_grpc_session = request->session();
        break;
      }
      case nixnet_grpc::GetPropertyRequest::SessionRepositoryCase::SESSION_REPOSITORY_NOT_SET: {
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for session/interface/device was not specified or out of range");
        break;
      }
    }
    // We store device, interface and session references in session_repository_ itself, either as owned session or
    // as dependent session. So we should always do a lookup in session_repository_.
    nxSessionRef_t session = session_repository_->access_session(session_grpc_session.name());
    u32 property_id;
    switch (request->property_id_enum_case()) {
      case nixnet_grpc::GetPropertyRequest::PropertyIdEnumCase::kPropertyId: {
        property_id = static_cast<u32>(request->property_id());
        break;
      }
      case nixnet_grpc::GetPropertyRequest::PropertyIdEnumCase::kPropertyIdRaw: {
        property_id = static_cast<u32>(request->property_id_raw());
        break;
      }
      case nixnet_grpc::GetPropertyRequest::PropertyIdEnumCase::PROPERTY_ID_ENUM_NOT_SET: {
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for property_id was not specified or out of range");
        break;
      }
    }

    u32 property_size{};
    auto status = library_->GetPropertySize(session, property_id, &property_size);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForNxSessionRef_t(context, status, session);
    }

    switch (property_type_map_[property_id]) {
      case u32_: {
        u32 property_value{};
        status = library_->GetProperty(session, property_id, property_size, &property_value);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNxSessionRef_t(context, status, session);
        }
        response->set_u32_scalar(property_value);
        break;
      }
      case boolean_: {
        bool property_value{};
        status = library_->GetProperty(session, property_id, property_size, &property_value);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNxSessionRef_t(context, status, session);
        }
        response->set_bool_scalar(property_value);
        break;
      }
      case u64_: {
        u64 property_value{};
        status = library_->GetProperty(session, property_id, property_size, &property_value);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNxSessionRef_t(context, status, session);
        }
        response->set_u64_scalar(property_value);
        break;
      }
      case i32_: {
        i32 property_value{};
        status = library_->GetProperty(session, property_id, property_size, &property_value);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNxSessionRef_t(context, status, session);
        }
        response->set_i32_scalar(property_value);
        break;
      }
      case f64_: {
        f64 property_value{};
        status = library_->GetProperty(session, property_id, property_size, &property_value);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNxSessionRef_t(context, status, session);
        }
        response->set_f64_scalar(property_value);
        break;
      }
      case string_: {
        std::string property_value(property_size, '\0');
        status = library_->GetProperty(session, property_id, property_size, const_cast<char*>(property_value.c_str()));
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNxSessionRef_t(context, status, session);
        }
        std::string property_value_utf8;
        convert_to_grpc(property_value, &property_value_utf8);
        response->set_str(property_value_utf8);
        break;
      }
      case u32_array_: {
        int32_t number_of_elements = property_size / sizeof(u32);
        response->mutable_u32_array()->mutable_u32_array()->Clear();
        response->mutable_u32_array()->mutable_u32_array()->Resize(number_of_elements, 0);
        u32* property_value = reinterpret_cast<u32*>(response->mutable_u32_array()->mutable_u32_array()->mutable_data());
        status = library_->GetProperty(session, property_id, property_size, property_value);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNxSessionRef_t(context, status, session);
        }
        break;
      }
      case db_ref_: {
        auto initiating_session_name = session_grpc_session.name();
        auto init_lambda = [&]() {
          nxDatabaseRef_t property_value;
          status = library_->GetProperty(session, property_id, property_size, &property_value);
          return std::make_tuple(status, property_value);
        };
        std::string session_name;
        status = nx_database_ref_t_resource_repository_->add_dependent_session(session_name, init_lambda, initiating_session_name);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNxSessionRef_t(context, status, session);
        }
        response->mutable_db_ref()->set_name(session_name);
        break;
      }
      case db_ref_array_: {
        auto initiating_session_name = session_grpc_session.name();
        int32_t number_of_elements = property_size / sizeof(nxDatabaseRef_t);
        std::vector<nxDatabaseRef_t> property_value_vector(number_of_elements, 0U);
        nxDatabaseRef_t* property_value = static_cast<nxDatabaseRef_t*>(property_value_vector.data());
        status = library_->GetProperty(session, property_id, property_size, property_value);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNxSessionRef_t(context, status, session);
        }
        response->mutable_db_ref_array()->mutable_db_ref()->Clear();
        response->mutable_db_ref_array()->mutable_db_ref()->Reserve(number_of_elements);
        std::transform(
            property_value_vector.begin(),
            property_value_vector.end(),
            google::protobuf::RepeatedFieldBackInserter(response->mutable_db_ref_array()->mutable_db_ref()),
            [&](auto x) {
              auto init_lambda = [&]() {
                return std::make_tuple(status, x);
              };
              std::string session_name;
              status = nx_database_ref_t_resource_repository_->add_dependent_session(session_name, init_lambda, initiating_session_name);
              nidevice_grpc::Session dependent_session{};
              dependent_session.set_name(session_name);
              return dependent_session;
            });
        break;
      }
      case dev_ref_: {
        auto initiating_session_name = session_grpc_session.name();
        auto init_lambda = [&]() {
          nxSessionRef_t property_value;
          status = library_->GetProperty(session, property_id, property_size, &property_value);
          return std::make_tuple(status, property_value);
        };
        std::string session_name;
        // We are adding it to session_repository_ and not to "device repository", because devices don't have a close API,
        // so it makes sense to tie their lifetime with session's lifetime.
        status = session_repository_->add_dependent_session(session_name, init_lambda, initiating_session_name);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNxSessionRef_t(context, status, session);
        }
        response->mutable_dev_ref()->set_name(session_name);
        break;
      }
      case dev_ref_array_: {
        auto initiating_session_name = session_grpc_session.name();
        int32_t number_of_elements = property_size / sizeof(nxSessionRef_t);
        std::vector<nxSessionRef_t> property_value_vector(number_of_elements, 0U);
        nxSessionRef_t* property_value = property_value_vector.data();
        status = library_->GetProperty(session, property_id, property_size, property_value);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNxSessionRef_t(context, status, session);
        }
        response->mutable_dev_ref_array()->mutable_dev_ref()->Clear();
        response->mutable_dev_ref_array()->mutable_dev_ref()->Reserve(number_of_elements);
        std::transform(
            property_value_vector.begin(),
            property_value_vector.end(),
            google::protobuf::RepeatedFieldBackInserter(response->mutable_dev_ref_array()->mutable_dev_ref()),
            [&](auto x) {
              auto init_lambda = [&]() {
                return std::make_tuple(status, x);
              };
              std::string session_name;
              // We are adding it to session_repository_ and not to "device repository", because devices don't have a close API,
              // so it makes sense to tie their lifetime with session's lifetime.
              status = session_repository_->add_dependent_session(session_name, init_lambda, initiating_session_name);
              nidevice_grpc::Session dependent_session{};
              dependent_session.set_name(session_name);
              return dependent_session;
            });
        break;
      }
      case intf_ref_array_: {
        auto initiating_session_name = session_grpc_session.name();
        int32_t number_of_elements = property_size / sizeof(nxSessionRef_t);
        std::vector<nxSessionRef_t> property_value_vector(number_of_elements, 0U);
        nxSessionRef_t* property_value = property_value_vector.data();
        status = library_->GetProperty(session, property_id, property_size, property_value);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNxSessionRef_t(context, status, session);
        }
        response->mutable_intf_ref_array()->mutable_intf_ref()->Clear();
        response->mutable_intf_ref_array()->mutable_intf_ref()->Reserve(number_of_elements);
        std::transform(
            property_value_vector.begin(),
            property_value_vector.end(),
            google::protobuf::RepeatedFieldBackInserter(response->mutable_intf_ref_array()->mutable_intf_ref()),
            [&](auto x) {
              auto init_lambda = [&]() {
                return std::make_tuple(status, x);
              };
              std::string session_name;
              // We are adding it to session_repository_ and not to "interface repository", because interfaces don't have a close API,
              // so it makes sense to tie their lifetime with session's lifetime.
              status = session_repository_->add_dependent_session(session_name, init_lambda, initiating_session_name);
              nidevice_grpc::Session dependent_session{};
              dependent_session.set_name(session_name);
              return dependent_session;
            });
        break;
      }
      case nxEptRxFilter_Element_t_array_: {
        int32_t number_of_elements = property_size / sizeof(nxEptRxFilter_Element_t);
        std::vector<nxEptRxFilter_Element_t> property_value_vector(number_of_elements);
        nxEptRxFilter_Element_t* property_value = static_cast<nxEptRxFilter_Element_t*>(property_value_vector.data());
        status = library_->GetProperty(session, property_id, property_size, &property_value);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNxSessionRef_t(context, status, session);
        }
        convert_to_grpc(property_value_vector, response->mutable_ept_rx_filter_array()->mutable_ept_rx_filter());
        break;
      }
      default: {
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "Specified property_id is not supported.");
        break;
      }
    }
    response->set_status(status);
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
// Custom implementation reason same as GetProperty API.
::grpc::Status NiXnetService::GetSubProperty(::grpc::ServerContext* context, const GetSubPropertyRequest* request, GetSubPropertyResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto session_grpc_session = request->session();
    nxSessionRef_t session = session_repository_->access_session(session_grpc_session.name());
    u32 active_index = request->active_index();
    u32 property_id;
    switch (request->subproperty_id_enum_case()) {
      case nixnet_grpc::GetSubPropertyRequest::SubpropertyIdEnumCase::kPropertyId: {
        property_id = static_cast<u32>(request->property_id());
        break;
      }
      case nixnet_grpc::GetSubPropertyRequest::SubpropertyIdEnumCase::kPropertyIdRaw: {
        property_id = static_cast<u32>(request->property_id_raw());
        break;
      }
      case nixnet_grpc::GetSubPropertyRequest::SubpropertyIdEnumCase::SUBPROPERTY_ID_ENUM_NOT_SET: {
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for property_id was not specified or out of range");
        break;
      }
    }

    u32 property_size{};
    auto status = library_->GetSubPropertySize(session, active_index, property_id, &property_size);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForNxSessionRef_t(context, status, session);
    }

    switch (subproperty_type_map_[property_id]) {
      case u32_: {
        u32 property_value{};
        status = library_->GetSubProperty(session, active_index, property_id, property_size, &property_value);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNxSessionRef_t(context, status, session);
        }
        response->set_u32_scalar(property_value);
        break;
      }
      case f64_: {
        f64 property_value{};
        status = library_->GetSubProperty(session, active_index, property_id, property_size, &property_value);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNxSessionRef_t(context, status, session);
        }
        response->set_f64_scalar(property_value);
        break;
      }
      case string_: {
        std::string property_value(property_size, '\0');
        status = library_->GetSubProperty(session, active_index, property_id, property_size, const_cast<char*>(property_value.c_str()));
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNxSessionRef_t(context, status, session);
        }
        std::string property_value_utf8;
        convert_to_grpc(property_value, &property_value_utf8);
        response->set_str(property_value_utf8);
        break;
      }
      default: {
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "Specified property_id is not supported.");
        break;
      }
    }
    response->set_status(status);
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
// Custom implementation reason same as GetProperty API.
::grpc::Status NiXnetService::DbGetProperty(::grpc::ServerContext* context, const DbGetPropertyRequest* request, DbGetPropertyResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto dbobject_grpc_session = request->dbobject();
    nxDatabaseRef_t dbobject = nx_database_ref_t_resource_repository_->access_session(dbobject_grpc_session.name());
    u32 property_id;
    switch (request->dbproperty_id_enum_case()) {
      case nixnet_grpc::DbGetPropertyRequest::DbpropertyIdEnumCase::kPropertyId: {
        property_id = static_cast<u32>(request->property_id());
        break;
      }
      case nixnet_grpc::DbGetPropertyRequest::DbpropertyIdEnumCase::kPropertyIdRaw: {
        property_id = static_cast<u32>(request->property_id_raw());
        break;
      }
      case nixnet_grpc::DbGetPropertyRequest::DbpropertyIdEnumCase::DBPROPERTY_ID_ENUM_NOT_SET: {
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for property_id was not specified or out of range");
        break;
      }
    }

    u32 property_size{};
    auto status = library_->DbGetPropertySize(dbobject, property_id, &property_size);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForNxDatabaseRef_t(context, status, dbobject);
    }

    switch (dbproperty_type_map_[property_id]) {
      case u32_: {
        u32 property_value{};
        status = library_->DbGetProperty(dbobject, property_id, property_size, &property_value);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNxDatabaseRef_t(context, status, dbobject);
        }
        response->set_u32_scalar(property_value);
        break;
      }
      case boolean_: {
        bool property_value{};
        status = library_->DbGetProperty(dbobject, property_id, property_size, &property_value);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNxDatabaseRef_t(context, status, dbobject);
        }
        response->set_bool_scalar(property_value);
        break;
      }
      case u64_: {
        u64 property_value{};
        status = library_->DbGetProperty(dbobject, property_id, property_size, &property_value);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNxDatabaseRef_t(context, status, dbobject);
        }
        response->set_u64_scalar(property_value);
        break;
      }
      case f64_: {
        f64 property_value{};
        status = library_->DbGetProperty(dbobject, property_id, property_size, &property_value);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNxDatabaseRef_t(context, status, dbobject);
        }
        response->set_f64_scalar(property_value);
        break;
      }
      case string_: {
        std::string property_value(property_size, '\0');
        status = library_->DbGetProperty(dbobject, property_id, property_size, const_cast<char*>(property_value.c_str()));
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNxDatabaseRef_t(context, status, dbobject);
        }
        std::string property_value_utf8;
        convert_to_grpc(property_value, &property_value_utf8);
        response->set_str(property_value_utf8);
        break;
      }
      case u32_array_: {
        int32_t number_of_elements = property_size / sizeof(u32);
        response->mutable_u32_array()->mutable_u32_array()->Clear();
        response->mutable_u32_array()->mutable_u32_array()->Resize(number_of_elements, 0);
        u32* property_value = reinterpret_cast<u32*>(response->mutable_u32_array()->mutable_u32_array()->mutable_data());
        status = library_->DbGetProperty(dbobject, property_id, property_size, property_value);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNxDatabaseRef_t(context, status, dbobject);
        }
        break;
      }
      case u8_array_: {
        int32_t number_of_elements = property_size / sizeof(u8);
        std::string property_value(number_of_elements, '\0');
        status = library_->DbGetProperty(dbobject, property_id, property_size, (u8*)property_value.data());
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNxDatabaseRef_t(context, status, dbobject);
        }
        response->set_u8_array(property_value);
      }
      case db_ref_: {
        auto initiating_session_name = dbobject_grpc_session.name();
        auto init_lambda = [&]() {
          nxDatabaseRef_t property_value;
          status = library_->DbGetProperty(dbobject, property_id, property_size, &property_value);
          return std::make_tuple(status, property_value);
        };
        std::string session_name;
        status = nx_database_ref_t_resource_repository_->add_dependent_session(session_name, init_lambda, initiating_session_name);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNxDatabaseRef_t(context, status, dbobject);
        }
        response->mutable_db_ref()->set_name(session_name);
        break;
      }
      case db_ref_array_: {
        int32_t number_of_elements = property_size / sizeof(nxDatabaseRef_t);
        auto initiating_session_name = dbobject_grpc_session.name();
        std::vector<nxDatabaseRef_t> property_value_vector(number_of_elements, 0U);
        nxDatabaseRef_t* property_value = static_cast<nxDatabaseRef_t*>(property_value_vector.data());
        status = library_->DbGetProperty(dbobject, property_id, property_size, property_value);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNxDatabaseRef_t(context, status, dbobject);
        }
        response->mutable_db_ref_array()->mutable_db_ref()->Clear();
        response->mutable_db_ref_array()->mutable_db_ref()->Reserve(number_of_elements);
        std::transform(
            property_value_vector.begin(),
            property_value_vector.end(),
            google::protobuf::RepeatedFieldBackInserter(response->mutable_db_ref_array()->mutable_db_ref()),
            [&](auto x) {
              auto init_lambda = [&]() {
                return std::make_tuple(status, x);
              };
              std::string session_name;
              status = nx_database_ref_t_resource_repository_->add_dependent_session(session_name, init_lambda, initiating_session_name);
              nidevice_grpc::Session dependent_session{};
              dependent_session.set_name(session_name);
              return dependent_session;
            });
        break;
      }
      default: {
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "Specified property_id is not supported.");
        break;
      }
    }
    response->set_status(status);
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
// SetProperty API has an input of type void * which has different possible values based on PropertyId
// passed in by user. We have defined complex message with oneof corresponding to each of these possible
// value types. We need to read data from correct oneof based on property PropertyId passed in by user.
// This requires custom implementation.
::grpc::Status NiXnetService::SetProperty(::grpc::ServerContext* context, const SetPropertyRequest* request, SetPropertyResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto session_grpc_session = request->session();
    nxSessionRef_t session = session_repository_->access_session(session_grpc_session.name());
    u32 property_id;
    switch (request->property_id_enum_case()) {
      case nixnet_grpc::SetPropertyRequest::PropertyIdEnumCase::kPropertyId: {
        property_id = static_cast<u32>(request->property_id());
        break;
      }
      case nixnet_grpc::SetPropertyRequest::PropertyIdEnumCase::kPropertyIdRaw: {
        property_id = static_cast<u32>(request->property_id_raw());
        break;
      }
      case nixnet_grpc::SetPropertyRequest::PropertyIdEnumCase::PROPERTY_ID_ENUM_NOT_SET: {
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for property_id was not specified or out of range");
        break;
      }
    }

    nxStatus_t status;
    switch (property_type_map_[property_id]) {
      case u32_: {
        u32 property_size = sizeof(u32);
        u32 property_value = request->u32_scalar();
        status = library_->SetProperty(session, property_id, property_size, &property_value);
        break;
      }
      case boolean_: {
        u32 property_size = sizeof(bool);
        bool property_value = request->bool_scalar();
        status = library_->SetProperty(session, property_id, property_size, &property_value);
        break;
      }
      case u64_: {
        u32 property_size = sizeof(u64);
        u64 property_value = request->u64_scalar();
        status = library_->SetProperty(session, property_id, property_size, &property_value);
        break;
      }
      case i32_: {
        u32 property_size = sizeof(i32);
        i32 property_value = request->i32_scalar();
        status = library_->SetProperty(session, property_id, property_size, &property_value);
        break;
      }
      case f64_: {
        u32 property_size = sizeof(f64);
        f64 property_value = request->f64_scalar();
        status = library_->SetProperty(session, property_id, property_size, &property_value);
        break;
      }
      case string_: {
        auto property_value_mbcs = convert_from_grpc<std::string>(request->str());
        u32 property_size = static_cast<u32>(property_value_mbcs.size());
        status = library_->SetProperty(session, property_id, property_size, const_cast<char*>(property_value_mbcs.c_str()));
        break;
      }
      case u32_array_: {
        u32 property_size = request->u32_array().u32_array().size() * sizeof(u32);
        u32* property_value = const_cast<u32*>(request->u32_array().u32_array().data());
        status = library_->SetProperty(session, property_id, property_size, property_value);
        break;
      }
      case db_ref_: {
        u32 property_size = sizeof(nxDatabaseRef_t);
        auto db_ref = request->db_ref();
        nxDatabaseRef_t property_value = nx_database_ref_t_resource_repository_->access_session(db_ref.name());
        status = library_->SetProperty(session, property_id, property_size, &property_value);
        break;
      }
      case db_ref_array_: {
        int32_t number_of_elements = request->db_ref_array().db_ref().size();
        std::vector<nxDatabaseRef_t> property_value(number_of_elements, 0U);
        std::transform(
            request->db_ref_array().db_ref().begin(),
            request->db_ref_array().db_ref().begin() + number_of_elements,
            property_value.end(),
            [&](auto x) {
              nxDatabaseRef_t db_ref = nx_database_ref_t_resource_repository_->access_session(x.name());
              return db_ref;
            });
        u32 property_size = number_of_elements * sizeof(nxDatabaseRef_t);
        status = library_->SetProperty(session, property_id, property_size, static_cast<nxDatabaseRef_t*>(property_value.data()));
        break;
      }
      case nxEptRxFilter_Element_t_array_: {
        u32 property_size = request->ept_rx_filter_array().ept_rx_filter().size() * sizeof(nxEptRxFilter_Element_t);
        auto property_value = convert_from_grpc<nxEptRxFilter_Element_t>(request->ept_rx_filter_array().ept_rx_filter());
        status = library_->SetProperty(session, property_id, property_size, property_value.data());
        break;
      }
      default: {
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "Specified property_id is not supported.");
        break;
      }
    }
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForNxSessionRef_t(context, status, session);
    }
    response->set_status(status);
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
// Custom implementation reason same as SetProperty API.
::grpc::Status NiXnetService::SetSubProperty(::grpc::ServerContext* context, const SetSubPropertyRequest* request, SetSubPropertyResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto session_grpc_session = request->session();
    nxSessionRef_t session = session_repository_->access_session(session_grpc_session.name());
    u32 active_index = request->active_index();
    u32 property_id;
    switch (request->subproperty_id_enum_case()) {
      case nixnet_grpc::SetSubPropertyRequest::SubpropertyIdEnumCase::kPropertyId: {
        property_id = static_cast<u32>(request->property_id());
        break;
      }
      case nixnet_grpc::SetSubPropertyRequest::SubpropertyIdEnumCase::kPropertyIdRaw: {
        property_id = static_cast<u32>(request->property_id_raw());
        break;
      }
      case nixnet_grpc::SetSubPropertyRequest::SubpropertyIdEnumCase::SUBPROPERTY_ID_ENUM_NOT_SET: {
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for property_id was not specified or out of range");
        break;
      }
    }

    nxStatus_t status;
    switch (subproperty_type_map_[property_id]) {
      case u32_: {
        u32 property_size = sizeof(u32);
        u32 property_value = request->u32_scalar();
        status = library_->SetSubProperty(session, active_index, property_id, property_size, &property_value);
        break;
      }
      case f64_: {
        u32 property_size = sizeof(f64);
        f64 property_value = request->f64_scalar();
        status = library_->SetSubProperty(session, active_index, property_id, property_size, &property_value);
        break;
      }
      case string_: {
        auto property_value_mbcs = convert_from_grpc<std::string>(request->str());
        u32 property_size = static_cast<u32>(property_value_mbcs.size());
        status = library_->SetSubProperty(session, active_index, property_id, property_size, const_cast<char*>(property_value_mbcs.c_str()));
        break;
      }
      default: {
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "Specified property_id is not supported.");
        break;
      }
    }
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForNxSessionRef_t(context, status, session);
    }
    response->set_status(status);
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
// Custom implementation reason same as SetProperty API.
::grpc::Status NiXnetService::DbSetProperty(::grpc::ServerContext* context, const DbSetPropertyRequest* request, DbSetPropertyResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto dbobject_grpc_session = request->dbobject();
    nxDatabaseRef_t dbobject = nx_database_ref_t_resource_repository_->access_session(dbobject_grpc_session.name());
    u32 property_id;
    switch (request->dbproperty_id_enum_case()) {
      case nixnet_grpc::DbSetPropertyRequest::DbpropertyIdEnumCase::kPropertyId: {
        property_id = static_cast<u32>(request->property_id());
        break;
      }
      case nixnet_grpc::DbSetPropertyRequest::DbpropertyIdEnumCase::kPropertyIdRaw: {
        property_id = static_cast<u32>(request->property_id_raw());
        break;
      }
      case nixnet_grpc::DbSetPropertyRequest::DbpropertyIdEnumCase::DBPROPERTY_ID_ENUM_NOT_SET: {
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for property_id was not specified or out of range");
        break;
      }
    }

    nxStatus_t status;
    switch (dbproperty_type_map_[property_id]) {
      case u32_: {
        u32 property_size = sizeof(u32);
        u32 property_value = request->u32_scalar();
        status = library_->DbSetProperty(dbobject, property_id, property_size, &property_value);
        break;
      }
      case boolean_: {
        u32 property_size = sizeof(boolean_);
        bool property_value = request->bool_scalar();
        status = library_->DbSetProperty(dbobject, property_id, property_size, &property_value);
        break;
      }
      case u64_: {
        u32 property_size = sizeof(u64);
        u64 property_value = request->u64_scalar();
        status = library_->DbSetProperty(dbobject, property_id, property_size, &property_value);
        break;
      }
      case f64_: {
        u32 property_size = sizeof(f64);
        f64 property_value = request->f64_scalar();
        status = library_->DbSetProperty(dbobject, property_id, property_size, &property_value);
        break;
      }
      case string_: {
        auto property_value_mbcs = convert_from_grpc<std::string>(request->str());
        u32 property_size = static_cast<u32>(property_value_mbcs.size());
        status = library_->DbSetProperty(dbobject, property_id, property_size, const_cast<char*>(property_value_mbcs.c_str()));
        break;
      }
      case u32_array_: {
        u32* property_value = const_cast<u32*>(request->u32_array().u32_array().data());
        u32 property_size = (u32)(request->u32_array().u32_array().size()) * sizeof(u32);
        status = library_->DbSetProperty(dbobject, property_id, property_size, property_value);
        break;
      }
      case u8_array_: {
        u8* property_value = (u8*)request->u8_array().c_str();
        u32 property_size = (u32)(request->u8_array().size());
        status = library_->DbSetProperty(dbobject, property_id, property_size, property_value);
      }
      case db_ref_: {
        u32 property_size = sizeof(nxDatabaseRef_t);
        auto db_ref = request->db_ref();
        nxDatabaseRef_t property_value = nx_database_ref_t_resource_repository_->access_session(db_ref.name());
        status = library_->DbSetProperty(dbobject, property_id, property_size, &property_value);
        break;
      }
      case db_ref_array_: {
        int32_t number_of_elements = request->db_ref_array().db_ref().size();
        std::vector<nxDatabaseRef_t> property_value(number_of_elements, 0U);
        std::transform(
            request->db_ref_array().db_ref().begin(),
            request->db_ref_array().db_ref().begin() + number_of_elements,
            property_value.end(),
            [&](auto x) {
              nxDatabaseRef_t db_ref = nx_database_ref_t_resource_repository_->access_session(x.name());
              return db_ref;
            });
        u32 property_size = number_of_elements * sizeof(nxDatabaseRef_t);
        status = library_->DbSetProperty(dbobject, property_id, property_size, static_cast<nxDatabaseRef_t*>(property_value.data()));
        break;
      }
    }
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForNxDatabaseRef_t(context, status, dbobject);
    }
    response->set_status(status);
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
// This API uses size mechanism similar to `ivi-datance` but needs to call a different API to get
// buffer size. This could potentially be implemented as `xnet-dance` in codegen. Right now no codegen
// mechanism exists, so added a custom implementation for now.
::grpc::Status NiXnetService::DbGetDatabaseList(::grpc::ServerContext* context, const DbGetDatabaseListRequest* request, DbGetDatabaseListResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto ip_address = request->ip_address().c_str();
    u32 size_of_alias_buffer{};
    u32 size_of_file_path_buffer{};
    auto status = library_->DbGetDatabaseListSizes(ip_address, &size_of_alias_buffer, &size_of_file_path_buffer);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForNxDatabaseRef_t(context, status, 0);
    }

    std::string alias_buffer(size_of_alias_buffer, '\0');
    std::string file_path_buffer(size_of_file_path_buffer, '\0');
    u32 number_of_databases{};

    status = library_->DbGetDatabaseList(ip_address, size_of_alias_buffer, const_cast<char*>(alias_buffer.c_str()), size_of_file_path_buffer, const_cast<char*>(file_path_buffer.c_str()), &number_of_databases);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForNxDatabaseRef_t(context, status, 0);
    }
    response->set_status(status);
    std::string alias_buffer_utf8;
    convert_to_grpc(alias_buffer, &alias_buffer_utf8);
    response->set_alias_buffer(alias_buffer_utf8.c_str());
    std::string file_path_buffer_utf8;
    convert_to_grpc(file_path_buffer, &file_path_buffer_utf8);
    response->set_filepath_buffer(file_path_buffer_utf8.c_str());
    response->set_number_of_databases(number_of_databases);
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
// Custom implementation reason same as DbGetDatabaseList API.
::grpc::Status NiXnetService::DbGetDBCAttribute(::grpc::ServerContext* context, const DbGetDBCAttributeRequest* request, DbGetDBCAttributeResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto db_object_grpc_session = request->db_object();
    nxDatabaseRef_t dbobject = nx_database_ref_t_resource_repository_->access_session(db_object_grpc_session.name());
    u32 mode;
    switch (request->mode_enum_case()) {
      case nixnet_grpc::DbGetDBCAttributeRequest::ModeEnumCase::kMode: {
        mode = static_cast<u32>(request->mode());
        break;
      }
      case nixnet_grpc::DbGetDBCAttributeRequest::ModeEnumCase::kModeRaw: {
        mode = static_cast<u32>(request->mode_raw());
        break;
      }
      case nixnet_grpc::DbGetDBCAttributeRequest::ModeEnumCase::MODE_ENUM_NOT_SET: {
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for mode was not specified or out of range");
        break;
      }
    }

    auto attribute_name_mbcs = convert_from_grpc<std::string>(request->attribute_name());
    auto attribute_name = attribute_name_mbcs.c_str();
    u32 attribute_text_size{};
    auto status = library_->DbGetDBCAttributeSize(dbobject, mode, attribute_name, &attribute_text_size);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForNxDatabaseRef_t(context, status, dbobject);
    }

    std::string attribute_text(attribute_text_size, '\0');
    u32 is_default{};

    status = library_->DbGetDBCAttribute(dbobject, mode, attribute_name, attribute_text_size, const_cast<char*>(attribute_text.c_str()), &is_default);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForNxDatabaseRef_t(context, status, dbobject);
    }
    response->set_status(status);
    response->set_is_default(is_default);
    std::string attribute_text_utf8;
    convert_to_grpc(attribute_text, &attribute_text_utf8);
    response->set_attribute_text(attribute_text_utf8.c_str());
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

::grpc::Status NiXnetService::ConvertApiErrorStatusForNxSessionRef_t(::grpc::ServerContextBase* context, int32_t status, nxSessionRef_t session)
{
  static_assert(nidevice_grpc::kMaxGrpcErrorDescriptionSize >= 2048, "StatusToString expects a minimum buffer size.");
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  library_->StatusToString(status, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

::grpc::Status NiXnetService::ConvertApiErrorStatusForNxDatabaseRef_t(::grpc::ServerContextBase* context, int32_t status, nxDatabaseRef_t session)
{
  static_assert(nidevice_grpc::kMaxGrpcErrorDescriptionSize >= 2048, "StatusToString expects a minimum buffer size.");
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  library_->StatusToString(status, nidevice_grpc::kMaxGrpcErrorDescriptionSize, &description[0]);
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

void convert_to_grpc(std::vector<u8>& input, google::protobuf::RepeatedPtrField<nixnet_grpc::FrameBufferResponse>* output, u32 number_of_bytes, u32 protocol, std::map<std::int32_t, std::int32_t> enetflags_output_map)
{
  auto buffer_ptr = (void*)input.data();
  while (buffer_ptr < input.data() + number_of_bytes) {
    auto frame_buffer = new FrameBufferResponse();
    convert_to_grpc(buffer_ptr, frame_buffer, protocol, enetflags_output_map);
    output->AddAllocated(frame_buffer);
    if (protocol == nixnet_grpc::Protocol::PROTOCOL_ENET) {
      auto enet_frame_ptr = (nxFrameEnet_t*)buffer_ptr;
      buffer_ptr = nxFrameIterateEthernetRead(enet_frame_ptr);
    }
    else {
      buffer_ptr = nxFrameIterate((nxFrameVar_t*)buffer_ptr);
    }
  }
}

void convert_enet_frame_to_grpc(const void* input, nixnet_grpc::FrameBufferResponse* output, u32 protocol, std::map<std::int32_t, std::int32_t> enetflags_output_map)
{
  nixnet_grpc::EnetFrameResponse* enet_frame = new nixnet_grpc::EnetFrameResponse();
  nxFrameEnet_t* nxEnetFrame = (nxFrameEnet_t*)input;
  enet_frame->set_type(static_cast<nixnet_grpc::EnetFrameType>(nxEnetFrame->Type));
  enet_frame->set_type_raw(nxEnetFrame->Type);
  enet_frame->set_device_timestamp(nxEnetFrame->DeviceTimestamp);
  enet_frame->set_network_timestamp(nxEnetFrame->NetworkTimestamp);
  if (nxEnetFrame->Flags & 0x80000000) {
    auto enet_flags_enum_omap_it = enetflags_output_map.find(0x80000000);
    if (enet_flags_enum_omap_it != enetflags_output_map.end()) {
      enet_frame->add_flags_mapped(EnetFlags::ENET_FLAGS_TRANSMIT);
    }
  }
  if (nxEnetFrame->Flags & 0x40000000) {
    auto enet_flags_enum_omap_it = enetflags_output_map.find(0x40000000);
    if (enet_flags_enum_omap_it != enetflags_output_map.end()) {
      enet_frame->add_flags_mapped(EnetFlags::ENET_FLAGS_RECEIVE);
    }
  }
  if (nxEnetFrame->Flags & 0x00800000) {
    auto enet_flags_enum_omap_it = enetflags_output_map.find(0x00800000);
    if (enet_flags_enum_omap_it != enetflags_output_map.end()) {
      enet_frame->add_flags_mapped(EnetFlags::ENET_FLAGS_NETWORK_SYNCED);
    }
  }
  if (nxEnetFrame->Flags & 0x00010000) {
    auto enet_flags_enum_omap_it = enetflags_output_map.find(0x00010000);
    if (enet_flags_enum_omap_it != enetflags_output_map.end()) {
      enet_frame->add_flags_mapped(EnetFlags::ENET_FLAGS_ERROR);
    }
  }
  enet_frame->set_flags_raw(nxEnetFrame->Flags);
  auto frame_data_length = nxEnetFrame->Length - ENET_FRAME_HEADER_LENGTH - ENET_FRAME_FCS_SIZE;
  enet_frame->mutable_frame_data()->assign((const char*)nxEnetFrame->FrameData, frame_data_length);

  output->set_allocated_enet(enet_frame);
}

void convert_frame_to_grpc(const void* input, nixnet_grpc::FrameBufferResponse* output, u32 protocol, std::map<std::int32_t, std::int32_t> enetflags_output_map)
{
  nxFrameVar_t* nxFrame = (nxFrameVar_t*)input;
  nixnet_grpc::FrameResponse* frame = new nixnet_grpc::FrameResponse();
  frame->set_timestamp(nxFrame->Timestamp);
  frame->set_identifier(nxFrame->Identifier);
  frame->set_type(static_cast<nixnet_grpc::FrameType>(nxFrame->Type));
  frame->set_type_raw(nxFrame->Type);
  if (nxFrame->Flags & 0x01) {
    frame->add_flags(FrameFlags::FRAME_FLAGS_FLEX_RAY_STARTUP);
  }
  if (nxFrame->Flags & 0x02) {
    frame->add_flags(FrameFlags::FRAME_FLAGS_FLEX_RAY_SYNC);
  }
  if (nxFrame->Flags & 0x04) {
    frame->add_flags(FrameFlags::FRAME_FLAGS_FLEX_RAY_PREAMBLE);
  }
  if (nxFrame->Flags & 0x10) {
    frame->add_flags(FrameFlags::FRAME_FLAGS_FLEX_RAY_CH_A);
  }
  if (nxFrame->Flags & 0x20) {
    frame->add_flags(FrameFlags::FRAME_FLAGS_FLEX_RAY_CH_B);
  }
  frame->set_flags_raw(nxFrame->Flags);
  frame->set_info(nxFrame->Info);
  auto payload_length = nxFrameGetPayloadLength(nxFrame);
  frame->mutable_payload()->assign((const char*)nxFrame->Payload, payload_length);

  switch (protocol) {
    case nixnet_grpc::Protocol::PROTOCOL_CAN:
      output->set_allocated_can(frame);
      break;
    case nixnet_grpc::Protocol::PROTOCOL_LIN:
      output->set_allocated_lin(frame);
      break;
    case nixnet_grpc::Protocol::PROTOCOL_FLEX_RAY:
      output->set_allocated_flex_ray(frame);
      break;
    case nixnet_grpc::Protocol::PROTOCOL_J1939:
      output->set_allocated_j1939(frame);
      break;
    default:
      throw std::invalid_argument("The value for protocol was not specified or out of range");
      break;
  }
}

void convert_to_grpc(const void* input, nixnet_grpc::FrameBufferResponse* output, u32 protocol, std::map<std::int32_t, std::int32_t> enetflags_output_map)
{
  if (protocol == nixnet_grpc::Protocol::PROTOCOL_ENET) {
    convert_enet_frame_to_grpc(input, output, protocol, enetflags_output_map);
  }
  else {
    convert_frame_to_grpc(input, output, protocol, enetflags_output_map);
  }
}

void convert_to_grpc(std::vector<f64>& input, google::protobuf::RepeatedField<double>* output, u32 number_of_values_returned, u32 number_of_signals)
{
  output->Resize(number_of_signals * number_of_values_returned, 0U);
  std::transform(
      input.begin(),
      input.begin() + (number_of_signals * number_of_values_returned),
      google::protobuf::RepeatedFieldBackInserter(output),
      [&](auto x) {
        return x;
      });
}

u32 get_frame_buffer_size(int32 number_of_frames, u32 max_payload_per_frame, u32 protocol)
{
  if (protocol == Protocol::PROTOCOL_ENET) {
    return number_of_frames * (ENET_FRAME_HEADER_LENGTH + ENET_FRAME_FCS_SIZE + max_payload_per_frame);
  }
  else {
    return number_of_frames * nxFrameSize(max_payload_per_frame);
  }
}
}  // namespace nixnet_grpc

namespace nidevice_grpc {
namespace converters {
template <>
void convert_to_grpc(const _nxFlexRayStats_t& input, nixnet_grpc::FlexRayStats* output)
{
  output->set_num_syntax_error_ch_a(input.NumSyntaxErrorChA);
  output->set_num_syntax_error_ch_b(input.NumSyntaxErrorChB);
  output->set_num_content_error_ch_a(input.NumContentErrorChA);
  output->set_num_content_error_ch_b(input.NumContentErrorChB);
  output->set_num_slot_boundary_violation_ch_a(input.NumSlotBoundaryViolationChA);
  output->set_num_slot_boundary_violation_ch_b(input.NumSlotBoundaryViolationChB);
}

template <>
void convert_to_grpc(const _nxJ1939CommState_t& input, nixnet_grpc::J1939CommState* output)
{
  output->set_pgn(input.PGN);
  output->set_source_address(input.SourceAddress);
  output->set_destination_address(input.DestinationAddress);
  output->set_transmit_error(input.TransmitError);
  output->set_receive_error(input.ReceiveError);
}

template <>
void convert_to_grpc(const nxEptRxFilter_Element_t& input, nixnet_grpc::EptRxFilter* output)
{
  output->set_use_flags(input.UseFlags);
  output->set_vid(input.VID);
  output->set_priority(input.Priority);
  output->mutable_destination_mac()->copy((char*)input.DestinationMAC, sizeof(nxMACAddress_t));
}

template <>
nxEptRxFilter_Element_t convert_from_grpc(const nixnet_grpc::EptRxFilter& input)
{
  auto output = nxEptRxFilter_Element_t();
  output.UseFlags = input.use_flags();
  output.VID = input.vid();
  output.Priority = input.priority();
  memcpy(output.DestinationMAC, input.destination_mac().c_str(), sizeof(nxMACAddress_t));
  return output;
}

}  // namespace converters
}  // namespace nidevice_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/nixnetsocket_service.custom.cpp sha256=90220923f3be0cba7db8b52de5cf23df8f451bae94edc74169ac3a0d6beeeb95 bytes=1634 -->
## FILE: source/custom/nixnetsocket_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/nixnetsocket_service.custom.cpp`
- sha256: `90220923f3be0cba7db8b52de5cf23df8f451bae94edc74169ac3a0d6beeeb95`
- bytes: 1634

````cpp
#include <nixnetsocket/nixnetsocket_service.h>

namespace nixnetsocket_grpc {

::grpc::Status NiXnetSocketService::ConvertApiErrorStatusForNxSOCKET(::grpc::ServerContextBase* context, int32_t status, nxSOCKET socket)
{
  // This implementation assumes this method is always called on the same thread where the error occurred.
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  library_->GetLastErrorStr(&description[0], nidevice_grpc::kMaxGrpcErrorDescriptionSize);
  // XNET sockets have special behavior that returns both the API error code and the sockets error number.
  int errorNumber = library_->GetLastErrorNum();
  context->AddTrailingMetadata("ni-socket-error", std::to_string(errorNumber));
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

::grpc::Status NiXnetSocketService::ConvertApiErrorStatusForNxIpStackRef_t(::grpc::ServerContextBase* context, int32_t status, nxIpStackRef_t socket)
{
  // This implementation assumes this method is always called on the same thread where the error occurred.
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  library_->GetLastErrorStr(&description[0], nidevice_grpc::kMaxGrpcErrorDescriptionSize);
  // XNET sockets have special behavior that returns both the API error code and the sockets error number.
  int errorNumber = library_->GetLastErrorNum();
  context->AddTrailingMetadata("ni-socket-error", std::to_string(errorNumber));
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

}  // namespace nixnetsocket_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/visa_service.custom.cpp sha256=e1eac74f2e4302eda574fe9e959ed885a1764236896403e157b2157fd92a1b40 bytes=31159 -->
## FILE: source/custom/visa_service.custom.cpp

- repository: `ni/grpc-device`
- source_path: `source/custom/visa_service.custom.cpp`
- sha256: `e1eac74f2e4302eda574fe9e959ed885a1764236896403e157b2157fd92a1b40`
- bytes: 31159

````cpp
#include <visa/visa_attributes.h>
#include <visa/visa_service.h>

// Copied from NiVisaImpl.h
#define VI_ATTR_RSRC_USER_ALIAS        (0x3FFF018EUL) /* ViString  */
#define VI_ATTR_NUM_SUP_EVENTS         (0x3FFF019CUL) /* ViUInt16  */
#define VI_ATTR_SUP_EVENTS             (0x3FFF019DUL) /* ViAEventType */

namespace visa_grpc {
using nidevice_grpc::converters::convert_from_grpc;
using nidevice_grpc::converters::convert_to_grpc;

struct VisaAsyncOperation {
  ViSession vi;
  ViEvent event;
  std::vector<ViByte> buffer;

  VisaAsyncOperation(ViSession vi_):
    vi(vi_), event(VI_NULL)
  {
  }
};

static ViSession s_defaultRM = VI_NULL;
static std::shared_mutex s_server_object_lock;
static std::list<VisaAsyncOperation> s_async_operations;

// Returns true if it's safe to use outputs of a method with the given status.
inline bool status_ok(int32 status)
{
  return status >= VI_SUCCESS;
}

template <typename T>
inline ViByte* get_sized_buffer_data_pointer(T* buffer, ViUInt32 requestedCount)
{
  buffer->resize(requestedCount);
  auto buffer_ptr = requestedCount ? &buffer->front() : nullptr;
  return reinterpret_cast<ViByte*>(buffer_ptr);
}

class DriverErrorException : public std::runtime_error {
 private:
  int status_ = 0;

 public:
  DriverErrorException(int status) : std::runtime_error(""), status_(status)
  {
  }
  int status() const
  {
    return status_;
  }
};

static void ServerObjectCleanup(visa_grpc::VisaService::LibrarySharedPtr library)
{
  std::unique_lock<std::shared_mutex> lock(s_server_object_lock);
  library->Close(s_defaultRM);
  s_defaultRM = VI_NULL;
  s_async_operations.clear();
}

static ViSession GetResourceManagerSession(visa_grpc::VisaService::ResourceRepositorySharedPtr repository, visa_grpc::VisaService::LibrarySharedPtr library)
{
  auto cleanup_lambda = [library](ViSession id) { ServerObjectCleanup(library); };

  std::unique_lock<std::shared_mutex> lock(s_server_object_lock);
  if (!s_defaultRM) {
    ViStatus status = library->OpenDefaultRM(&s_defaultRM);
    if (!status_ok(status)) {
      throw DriverErrorException(status);
    }
    // This should be cleaned up only when the user explicitly resets the server to close all sessions.
    std::string manager_name = "INTERNAL::VISA::RESOURCE_MANAGER";
    auto init_lambda = [&] () { return std::make_tuple(0, s_defaultRM); };
    repository->add_session(manager_name, init_lambda, cleanup_lambda, nidevice_grpc::SESSION_INITIALIZATION_BEHAVIOR_UNSPECIFIED, NULL);
  }
  return s_defaultRM;
}

static ViStatus GetAttributeValue(ViObject vi, ViAttr attributeID, VisaService::LibrarySharedPtr library, visa_grpc::AttributeValueData* mutableValue)
{
  ViStatus status;
  switch (GetAttributeType(attributeID))
  {
    case AttributeValueData::kValueString: {
      ViChar attrValue[256] = {0};
      status = library->GetAttribute(vi, attributeID, attrValue);
      mutableValue->mutable_value_string()->assign(attrValue);
      break;
    }
    case AttributeValueData::kValueU64: {
      ViUInt64 val64;
      status = library->GetAttribute(vi, attributeID, &val64);
      mutableValue->set_value_u64(val64);
      break;
    }
    case AttributeValueData::kValueU32: {
      ViUInt32 val32;
      status = library->GetAttribute(vi, attributeID, &val32);
      mutableValue->set_value_u32(val32);
      break;
    }
    case AttributeValueData::kValueU16: {
      ViUInt16 val16;
      status = library->GetAttribute(vi, attributeID, &val16);
      // Special case logic for a specific property.
      // If the mapped address is a pointer, the remote client cannot use it as such
      if (attributeID == VI_ATTR_WIN_ACCESS && (val16 == VI_DEREF_ADDR || val16 == VI_DEREF_ADDR_BYTE_SWAP)) {
          val16 = VI_USE_OPERS;
      }
      mutableValue->set_value_u16(val16);
      break;
    }
    case AttributeValueData::kValueBool: {
      ViBoolean valBool;
      status = library->GetAttribute(vi, attributeID, &valBool);
      mutableValue->set_value_bool(valBool == VI_TRUE);
      break;
    }
    case AttributeValueData::kValueU8: {
      ViUInt8 val8;
      status = library->GetAttribute(vi, attributeID, &val8);
      mutableValue->set_value_u8(val8);
      break;
    }
    case AttributeValueData::kValueI32: {
      ViInt32 val32;
      status = library->GetAttribute(vi, attributeID, &val32);
      mutableValue->set_value_i32(val32);
      break;
    }
    case AttributeValueData::kValueI16: {
      ViInt16 val16;
      status = library->GetAttribute(vi, attributeID, &val16);
      mutableValue->set_value_i16(val16);
      break;
    }
    case AttributeValueData::kValueBytes: {
      if (attributeID == VI_ATTR_USB_RECV_INTR_DATA) {
        ViUInt16 byteCount;
        status = library->GetAttribute(vi, VI_ATTR_USB_RECV_INTR_SIZE, &byteCount);
        if (status >= VI_SUCCESS) {
          std::string* bytesAsString = mutableValue->mutable_value_bytes();
          auto buffer_pointer = get_sized_buffer_data_pointer(bytesAsString, byteCount);
          status = library->GetAttribute(vi, attributeID, buffer_pointer);
        }
      }
      else if (attributeID == VI_ATTR_TCPIP_SERVER_CERT) {
        ViUInt32 byteCount;
        status = library->GetAttribute(vi, VI_ATTR_TCPIP_SERVER_CERT_SIZE, &byteCount);
        if (status >= VI_SUCCESS) {
          std::string* bytesAsString = mutableValue->mutable_value_bytes();
          auto buffer_pointer = get_sized_buffer_data_pointer(bytesAsString, byteCount);
          status = library->GetAttribute(vi, attributeID, buffer_pointer);
        }
      }
      else if (attributeID == VI_ATTR_BUFFER) {
        ViUInt32 byteCount;
        status = library->GetAttribute(vi, VI_ATTR_RET_COUNT_32, &byteCount);
        auto matching_event_lambda = [&](const VisaAsyncOperation& v) { return v.event == vi; };
        std::unique_lock<std::shared_mutex> lock(s_server_object_lock);
        auto iter = std::find_if(s_async_operations.begin(), s_async_operations.end(), matching_event_lambda);
        if (status >= VI_SUCCESS && iter != s_async_operations.end()) {
          std::string* bytesAsString = mutableValue->mutable_value_bytes();
          bytesAsString->assign(reinterpret_cast<char*>((*iter).buffer.data()), byteCount);
        }
      }
      else {
        status = VI_ERROR_NSUP_ATTR;
      }
      break;
    }
    default:
      status = VI_ERROR_NSUP_ATTR;
      break;
  }
  return status;
}

::grpc::Status ConvertVisaApiErrorStatus(::grpc::ServerContextBase* context, ViStatus status, ViObject vi, VisaService::LibrarySharedPtr library, const char* extraInfo = nullptr)
{
  std::string description(nidevice_grpc::kMaxGrpcErrorDescriptionSize, '\0');
  library->StatusDesc(vi, status, &description[0]);
  // Although NI-VISA messages don't currently include context, we shouldn't assume it.
  if (extraInfo != nullptr && description.find(extraInfo) == description.npos) {
    nidevice_grpc::converters::trim_trailing_nulls(description);
    description.append("\n");
    description.append(extraInfo);
  }
  return nidevice_grpc::ApiErrorAndDescriptionToStatus(context, status, description);
}

::grpc::Status VisaService::ConvertApiErrorStatusForViSession(::grpc::ServerContextBase* context, int32_t status, ViSession vi)
{
  return ConvertVisaApiErrorStatus(context, status, vi, library_);
}

::grpc::Status VisaService::ConvertApiErrorStatusForViObject(::grpc::ServerContextBase* context, int32_t status, ViObject vi)
{
  return ConvertVisaApiErrorStatus(context, status, vi, library_);
}


//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status VisaService::CloseEvent(::grpc::ServerContext* context, const CloseEventRequest* request, CloseEventResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    ViEvent event_handle = request->event_handle();
    auto status = library_->CloseEvent(event_handle);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForViSession(context, status, 0);
    }
    auto matching_event_lambda = [&](const VisaAsyncOperation& v) { return v.event == event_handle; };
    std::unique_lock<std::shared_mutex> lock(s_server_object_lock);
    s_async_operations.remove_if(matching_event_lambda);
    response->set_status(status);
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status VisaService::FindRsrc(::grpc::ServerContext* context, const FindRsrcRequest* request, FindRsrcResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    ViSession rsrc_manager_handle = GetResourceManagerSession(session_repository_, library_);
    auto expression_mbcs = convert_from_grpc<std::string>(request->expression());
    auto expression = expression_mbcs.c_str();
    ViFindList find_handle{};
    ViUInt32 return_count{};
    ViChar descriptor[256];
    auto status = library_->FindRsrc(rsrc_manager_handle, expression, &find_handle, &return_count, descriptor);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForViSession(context, status, rsrc_manager_handle);
    }
    response->add_instrument_descriptor(descriptor);
    for (ViUInt32 index = 1; index < return_count; ++index) {
      status = library_->FindNext(find_handle, descriptor);
      if (!status_ok(status)) {
        library_->Close(find_handle);
        return ConvertApiErrorStatusForViSession(context, status, rsrc_manager_handle);
      }
      response->add_instrument_descriptor(descriptor);
    }
    library_->Close(find_handle);
    response->set_status(status);
    return ::grpc::Status::OK;
  }
  catch (const nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
  catch (const DriverErrorException& ex) {
    return ConvertApiErrorStatusForViSession(context, ex.status(), VI_NULL);
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status VisaService::GetAttribute(::grpc::ServerContext* context, const GetAttributeRequest* request, GetAttributeResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto vi_grpc_session = request->vi();
    ViSession vi = session_repository_->access_session(vi_grpc_session.name());
    ViAttr attributeID = request->attribute_name();
    ViStatus status = GetAttributeValue(vi, attributeID, library_, response->mutable_attribute_value());
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForViSession(context, status, vi);
    }
    response->set_status(status);
    return ::grpc::Status::OK;
  }
  catch (const nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status VisaService::GetAttributeEvent(::grpc::ServerContext* context, const GetAttributeEventRequest* request, GetAttributeEventResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    ViEvent vi = request->event_handle();
    ViAttr attributeID = request->attribute_name();
    ViStatus status = GetAttributeValue(vi, attributeID, library_, response->mutable_attribute_value());
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForViObject(context, status, vi);
    }
    response->set_status(status);
    return ::grpc::Status::OK;
  }
  catch (const nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status VisaService::Open(::grpc::ServerContext* context, const OpenRequest* request, OpenResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    ViSession rsrc_manager_handle = GetResourceManagerSession(session_repository_, library_);
    auto instrument_descriptor_mbcs = convert_from_grpc<std::string>(request->instrument_descriptor());
    ViConstRsrc instrument_descriptor = (ViConstRsrc)instrument_descriptor_mbcs.c_str();
    ViAccessMode access_mode;
    switch (request->access_mode_enum_case()) {
      case visa_grpc::OpenRequest::AccessModeEnumCase::kAccessMode: {
        access_mode = static_cast<ViAccessMode>(request->access_mode());
        break;
      }
      case visa_grpc::OpenRequest::AccessModeEnumCase::kAccessModeRaw: {
        access_mode = static_cast<ViAccessMode>(request->access_mode_raw());
        break;
      }
        default: {
          access_mode = VI_NO_LOCK;
        break;
      }
    }

    ViUInt32 open_timeout = request->open_timeout();
    auto initialization_behavior = request->initialization_behavior();

    bool new_session_initialized{};
    auto init_lambda = [&]() {
      ViSession vi;
      auto status = library_->Open(rsrc_manager_handle, instrument_descriptor, access_mode, open_timeout, &vi);
      return std::make_tuple(status, vi);
    };
    std::string grpc_device_session_name = request->session_name();
    // Capture the library shared_ptr by value. Do not capture `this` or any references.
    LibrarySharedPtr library = library_;
    auto cleanup_lambda = [library](ViSession id) { library->Close(id); };
    int status = session_repository_->add_session(grpc_device_session_name, init_lambda, cleanup_lambda, initialization_behavior, &new_session_initialized);
    if (!status_ok(status)) {
      return ConvertVisaApiErrorStatus(context, status, rsrc_manager_handle, library_, instrument_descriptor);
    }

    ViUInt16 numEvents = 0;
    ViSession vi = session_repository_->access_session(grpc_device_session_name);
    if (library->GetAttribute(vi, VI_ATTR_NUM_SUP_EVENTS, &numEvents) == VI_SUCCESS && numEvents > 0) {
      // NI-VISA writes the events followed by an extra "-1" value that we don't need.
      std::vector<EventType> events(numEvents+1);
      library->GetAttribute(vi, VI_ATTR_SUP_EVENTS, events.data());
      for (ViUInt16 index = 0; index < numEvents; ++index) {
        response->add_supported_events(events[index]);
      }
    }

    response->set_status(status);
    response->mutable_vi()->set_name(grpc_device_session_name);
    response->set_new_session_initialized(new_session_initialized);
    return ::grpc::Status::OK;
  }
  catch (const nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
  catch (const DriverErrorException& ex) {
    return ConvertApiErrorStatusForViSession(context, ex.status(), VI_NULL);
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status VisaService::MoveIn16(::grpc::ServerContext* context, const MoveIn16Request* request, MoveIn16Response* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  ViSession vi = VI_NULL;
  try {
    auto vi_grpc_session = request->vi();
    vi = session_repository_->access_session(vi_grpc_session.name());
    ViUInt16 address_space;
    switch (request->address_space_enum_case()) {
      case visa_grpc::MoveIn16Request::AddressSpaceEnumCase::kAddressSpace: {
        address_space = static_cast<ViUInt16>(request->address_space());
        break;
      }
      case visa_grpc::MoveIn16Request::AddressSpaceEnumCase::kAddressSpaceRaw: {
        address_space = static_cast<ViUInt16>(request->address_space_raw());
        break;
      }
      case visa_grpc::MoveIn16Request::AddressSpaceEnumCase::ADDRESS_SPACE_ENUM_NOT_SET: {
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for address_space was not specified or out of range");
        break;
      }
    }

    ViBusAddress64 offset = request->offset();
    ViBusSize count = request->count();
    std::vector<ViUInt16> driver_buffer(count);
    ViUInt16* buffer_pointer = driver_buffer.data();
    auto status = library_->MoveIn16(vi, address_space, offset, count, buffer_pointer);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForViSession(context, status, vi);
    }
    auto response_buffer = response->mutable_buffer();
    response_buffer->Resize(static_cast<int>(count), 0);
    for (ViUInt32 index = 0; index < count; ++index) {
      response_buffer->Set(index, *buffer_pointer++);
    }
    response->set_status(status);
    return ::grpc::Status::OK;
  }
  catch (const std::bad_alloc&) {
    return ConvertApiErrorStatusForViSession(context, VI_ERROR_ALLOC, vi);
  }
  catch (const nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status VisaService::ParseRsrc(::grpc::ServerContext* context, const ParseRsrcRequest* request, ParseRsrcResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    ViSession rsrc_manager_handle = GetResourceManagerSession(session_repository_, library_);
    auto resource_name_mbcs = convert_from_grpc<std::string>(request->resource_name());
    ViConstRsrc resource_name = (ViConstRsrc)resource_name_mbcs.c_str();
    ViUInt16 interface_type{};
    ViUInt16 interface_number{};
    std::string resource_class(256 - 1, '\0');
    std::string expanded_unaliased_name(256 - 1, '\0');
    std::string alias_if_exists(256 - 1, '\0');
    auto status = library_->ParseRsrc(rsrc_manager_handle, resource_name, &interface_type, &interface_number, (ViChar*)resource_class.data(), (ViChar*)expanded_unaliased_name.data(), (ViChar*)alias_if_exists.data());
    if (!status_ok(status)) {
      return ConvertVisaApiErrorStatus(context, status, rsrc_manager_handle, library_, resource_name);
    }
    response->set_status(status);
    response->set_interface_type(interface_type);
    response->set_interface_number(interface_number);
    std::string resource_class_utf8;
    convert_to_grpc(resource_class, &resource_class_utf8);
    response->set_resource_class(resource_class_utf8);
    nidevice_grpc::converters::trim_trailing_nulls(*(response->mutable_resource_class()));
    std::string expanded_unaliased_name_utf8;
    convert_to_grpc(expanded_unaliased_name, &expanded_unaliased_name_utf8);
    response->set_expanded_unaliased_name(expanded_unaliased_name_utf8);
    nidevice_grpc::converters::trim_trailing_nulls(*(response->mutable_expanded_unaliased_name()));
    std::string alias_if_exists_utf8;
    convert_to_grpc(alias_if_exists, &alias_if_exists_utf8);
    response->set_alias_if_exists(alias_if_exists_utf8);
    nidevice_grpc::converters::trim_trailing_nulls(*(response->mutable_alias_if_exists()));
    return ::grpc::Status::OK;
  }
  catch (const nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
  catch (const DriverErrorException& ex) {
    return ConvertApiErrorStatusForViSession(context, ex.status(), VI_NULL);
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status VisaService::Read(::grpc::ServerContext* context, const ReadRequest* request, ReadResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  ViSession vi = VI_NULL;
  try {
    auto vi_grpc_session = request->vi();
    vi = session_repository_->access_session(vi_grpc_session.name());
    ViUInt32 count = request->count();
    std::string* buffer = response->mutable_buffer();
    auto buffer_pointer = get_sized_buffer_data_pointer(buffer, count);
    ViUInt32 return_count{};
    auto status = library_->Read(vi, buffer_pointer, count, &return_count);
    if (!status_ok(status) && return_count == 0) {
      return ConvertApiErrorStatusForViSession(context, status, vi);
    }
    response->set_status(status);
    buffer->resize(return_count);
    response->set_return_count(return_count);
    return ::grpc::Status::OK;
  }
  catch (const std::bad_alloc&) {
    return ConvertApiErrorStatusForViSession(context, VI_ERROR_ALLOC, vi);
  }
  catch (const nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status VisaService::ReadAsync(::grpc::ServerContext* context, const ReadAsyncRequest* request, ReadAsyncResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  ViSession vi = VI_NULL;
  try {
    auto vi_grpc_session = request->vi();
    vi = session_repository_->access_session(vi_grpc_session.name());
    ViUInt32 count = request->count();

    auto outstanding_job_lambda = [&](const VisaAsyncOperation& v) { return v.vi == vi && v.event == VI_NULL; };
    std::unique_lock<std::shared_mutex> lock(s_server_object_lock);
    // Allow only 1 outstanding job per session
    if (std::find_if(s_async_operations.begin(), s_async_operations.end(), outstanding_job_lambda) != s_async_operations.end()) {
      return ConvertApiErrorStatusForViSession(context, VI_ERROR_IN_PROGRESS, vi);
    }
    auto operation_data_iter = s_async_operations.emplace(s_async_operations.end(), vi);
    auto buffer_pointer = get_sized_buffer_data_pointer(&operation_data_iter->buffer, count);
    // We release the lock while starting the actual I/O.
    lock.unlock();

    ViJobId job_identifier{};
    auto status = library_->ReadAsync(vi, buffer_pointer, count, &job_identifier);
    if (!status_ok(status)) {
      lock.lock();
      s_async_operations.erase(operation_data_iter);
      return ConvertApiErrorStatusForViSession(context, status, vi);
    }
    response->set_status(status);
    response->set_job_identifier(job_identifier);
    return ::grpc::Status::OK;
  }
  catch (const std::bad_alloc&) {
    return ConvertApiErrorStatusForViSession(context, VI_ERROR_ALLOC, vi);
  }
  catch (const nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status VisaService::SetAttribute(::grpc::ServerContext* context, const SetAttributeRequest* request, SetAttributeResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto vi_grpc_session = request->vi();
    ViSession vi = session_repository_->access_session(vi_grpc_session.name());
    ViAttr attributeID = request->attribute_name();
    ViAttrState attribute_value = 0;
    if (request->attribute_value().has_value_bool()) {
      attribute_value = static_cast<ViAttrState>(request->attribute_value().value_bool() ? VI_TRUE : VI_FALSE);
    }
#if defined(_VISA_ENV_IS_64_BIT)
    else if (request->attribute_value().has_value_u64()) {
      attribute_value = static_cast<ViAttrState>(request->attribute_value().value_u64());
    }
#endif
    else if (request->attribute_value().has_value_i32()) {
      attribute_value = static_cast<ViAttrState>(request->attribute_value().value_i32());
    }
    else if (request->attribute_value().has_value_u32()) {
      attribute_value = static_cast<ViAttrState>(request->attribute_value().value_u32());
    }
    else if (request->attribute_value().has_value_i16()) {
      attribute_value = static_cast<ViAttrState>(request->attribute_value().value_i16());
    }
    else if (request->attribute_value().has_value_u16()) {
      attribute_value = static_cast<ViAttrState>(request->attribute_value().value_u16());
    }
    else if (request->attribute_value().has_value_u8()) {
      attribute_value = static_cast<ViAttrState>(request->attribute_value().value_u8());
    }
    else {
      throw nidevice_grpc::NonDriverException(::grpc::INVALID_ARGUMENT, "The value for attribute_value was not specified or out of range");
    }
    auto status = library_->SetAttribute(vi, attributeID, attribute_value);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForViObject(context, status, vi);
    }
    response->set_status(status);
    return ::grpc::Status::OK;
  }
  catch (const nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status VisaService::UsbControlIn(::grpc::ServerContext* context, const UsbControlInRequest* request, UsbControlInResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  ViSession vi = VI_NULL;

  try {
    auto vi_grpc_session = request->vi();
    vi = session_repository_->access_session(vi_grpc_session.name());
    ViInt16 bm_request_type = (ViInt16)request->bm_request_type();
    ViInt16 b_request = (ViInt16)request->b_request();
    ViUInt16 w_value = request->w_value();
    ViUInt16 w_index = request->w_index();
    ViUInt16 w_length = request->w_length();
    std::string* buffer = response->mutable_buffer();
    auto buffer_pointer = get_sized_buffer_data_pointer(buffer, w_length);
    ViUInt16 return_count{};
    auto status = library_->UsbControlIn(vi, bm_request_type, b_request, w_value, w_index, w_length, buffer_pointer, &return_count);
    if (!status_ok(status) && return_count == 0) {
      return ConvertApiErrorStatusForViSession(context, status, vi);
    }
    response->set_status(status);
    buffer->resize(return_count);
    response->set_return_count(return_count);
    return ::grpc::Status::OK;
  }
  catch (const std::bad_alloc&) {
    return ConvertApiErrorStatusForViSession(context, VI_ERROR_ALLOC, vi);
  }
  catch (const nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status VisaService::WaitOnEvent(::grpc::ServerContext* context, const WaitOnEventRequest* request, WaitOnEventResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto vi_grpc_session = request->vi();
    ViSession vi = session_repository_->access_session(vi_grpc_session.name());
    ViEventType in_event_type;
    switch (request->in_event_type_enum_case()) {
      case visa_grpc::WaitOnEventRequest::InEventTypeEnumCase::kInEventType: {
        in_event_type = static_cast<ViEventType>(request->in_event_type());
        break;
      }
      case visa_grpc::WaitOnEventRequest::InEventTypeEnumCase::kInEventTypeRaw: {
        in_event_type = static_cast<ViEventType>(request->in_event_type_raw());
        break;
      }
      case visa_grpc::WaitOnEventRequest::InEventTypeEnumCase::IN_EVENT_TYPE_ENUM_NOT_SET: {
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for in_event_type was not specified or out of range");
        break;
      }
    }

    ViUInt32 timeout = request->timeout();
    ViEventType out_event_type {};
    ViEvent event_handle {};
    auto status = library_->WaitOnEvent(vi, in_event_type, timeout, &out_event_type, &event_handle);
    if (!status_ok(status)) {
      return ConvertApiErrorStatusForViSession(context, status, vi);
    }

    if (out_event_type == VI_EVENT_IO_COMPLETION) {
      auto outstanding_job_lambda = [&](const VisaAsyncOperation& v) { return v.vi == vi && v.event == VI_NULL; };
      std::unique_lock<std::shared_mutex> lock(s_server_object_lock);
      auto iter = std::find_if(s_async_operations.begin(), s_async_operations.end(), outstanding_job_lambda);
      if (iter != s_async_operations.end()) {
        (*iter).event = event_handle;
      }
    }

    response->set_status(status);
    response->set_out_event_type(static_cast<visa_grpc::EventType>(out_event_type));
    response->set_out_event_type_raw(out_event_type);
    response->set_event_handle(event_handle);
    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
::grpc::Status VisaService::WriteAsync(::grpc::ServerContext* context, const WriteAsyncRequest* request, WriteAsyncResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  ViSession vi = VI_NULL;
  try {
    auto vi_grpc_session = request->vi();
    vi = session_repository_->access_session(vi_grpc_session.name());
    ViUInt32 count = static_cast<ViUInt32>(request->buffer().size());

    auto outstanding_job_lambda = [&](const VisaAsyncOperation& v) { return v.vi == vi && v.event == VI_NULL; };
    std::unique_lock<std::shared_mutex> lock(s_server_object_lock);
    // Allow only 1 outstanding job per session
    if (std::find_if(s_async_operations.begin(), s_async_operations.end(), outstanding_job_lambda) != s_async_operations.end()) {
      return ConvertApiErrorStatusForViSession(context, VI_ERROR_IN_PROGRESS, vi);
    }
    auto operation_data_iter = s_async_operations.emplace(s_async_operations.end(), vi);
    auto buffer_pointer = get_sized_buffer_data_pointer(&operation_data_iter->buffer, count);
    memcpy(buffer_pointer, reinterpret_cast<const ViByte*>(&request->buffer().front()), count);
    // We release the lock while starting the actual I/O.
    lock.unlock();

    ViJobId job_identifier{};
    auto status = library_->WriteAsync(vi, buffer_pointer, count, &job_identifier);
    if (!status_ok(status)) {
      lock.lock();
      s_async_operations.erase(operation_data_iter);
      return ConvertApiErrorStatusForViSession(context, status, vi);
    }
    response->set_status(status);
    response->set_job_identifier(job_identifier);
    return ::grpc::Status::OK;
  }
  catch (const std::bad_alloc&) {
    return ConvertApiErrorStatusForViSession(context, VI_ERROR_ALLOC, vi);
  }
  catch (const nidevice_grpc::NonDriverException& ex) {
    return ex.GetStatus();
  }
}

}  // namespace visa_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/custom/xnetsocket_aliases.h sha256=c4062b2eaf126932e11a255e49b0a4f83dacb8e457a22d88eb55ca00743e7997 bytes=628 -->
## FILE: source/custom/xnetsocket_aliases.h

- repository: `ni/grpc-device`
- source_path: `source/custom/xnetsocket_aliases.h`
- sha256: `c4062b2eaf126932e11a255e49b0a4f83dacb8e457a22d88eb55ca00743e7997`
- bytes: 628

````c
#ifndef NIDEVICE_GRPC_DEVICE_XNET_SOCKET_ALIASES_H
#define NIDEVICE_GRPC_DEVICE_XNET_SOCKET_ALIASES_H

#include <nixnetsocket.pb.h>
#include <nixnetsocket/nixnetsocket_library_interface.h>
#include <nxsocket.h>
#include <server/converters.h>

#include <algorithm>
#include <cstring>

namespace nixnetsocket_grpc {
// Aliasing these particular usages allow us to use a custom converter
// that calls the paired nxIpStackFreeAllStacksInfoStr.
using IpStackInfoString = char*;
}  // namespace nixnetsocket_grpc
using nixnetsocket_grpc::IpStackInfoString;

#endif /* NIDEVICE_GRPC_DEVICE_XNET_SOCKET_ALIASES_H */
````
